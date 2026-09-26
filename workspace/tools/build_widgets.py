#!/usr/bin/env python3
"""Build paste-ready widget HTML for WordPress Custom HTML blocks.

Each widget has a source template at workspace/widgets/src/<tool>.html that
contains the literal token __DATA__. This script replaces that token with a
JSON array built from the widget's data CSV (workspace/data/<file>.csv), so the
hub table, spoke numbers and the widget all come from one verified source.

Usage:
  python3 workspace/tools/build_widgets.py            # build all widgets
  python3 workspace/tools/build_widgets.py <tool>     # build one
"""
import csv
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(ROOT, "workspace", "widgets", "src")
OUT = os.path.join(ROOT, "workspace", "widgets")
DATA = os.path.join(ROOT, "workspace", "data")

# tool -> (data csv or None, columns to embed or None for all)
WIDGETS = {
    "test-hello": (None, None),
    "small-estate-eligibility-checker": ("small-estate.csv", None),
    "small-claims-cost-estimator": ("small-claims.csv", None),
    "divorce-cost-timeline-estimator": ("divorce.csv", None),
    "judgment-interest-calculator": ("judgment-interest.csv", None),
}

# Columns that never ship to the browser
PRIVATE = {"notes_internal"}


def num(v):
    try:
        f = float(v)
        return int(f) if f.is_integer() else f
    except (TypeError, ValueError):
        return v


def load_rows(name, cols):
    with open(os.path.join(DATA, name), newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    out = []
    for r in rows:
        keep = {k: num(v) for k, v in r.items() if k not in PRIVATE and (cols is None or k in cols)}
        out.append(keep)
    return out


def build(tool):
    data_file, cols = WIDGETS[tool]
    src = os.path.join(SRC, f"{tool}.html")
    if not os.path.exists(src):
        print(f"skip {tool}: no source template")
        return
    tpl = open(src, encoding="utf-8").read()
    data = load_rows(data_file, cols) if data_file else []
    if "__DATA__" not in tpl:
        sys.exit(f"{tool}: template has no __DATA__ token")
    html = tpl.replace("__DATA__", json.dumps(data, separators=(",", ":"), ensure_ascii=False))
    dst = os.path.join(OUT, f"{tool}.html")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"built {os.path.relpath(dst, ROOT)} ({len(data)} rows, {len(html):,} bytes)")


def main():
    tools = sys.argv[1:] or list(WIDGETS)
    for t in tools:
        if t not in WIDGETS:
            sys.exit(f"unknown widget {t}")
        build(t)


if __name__ == "__main__":
    main()
