#!/usr/bin/env python3
"""Render a hub's 50-state HTML table from its verified data CSV.

The output is pasted into the hub draft between the TABLE markers, so the
table on the page always matches workspace/data/<vertical>.csv.

Usage:
  python3 workspace/tools/render_hub_table.py small-estate            # print table HTML
  python3 workspace/tools/render_hub_table.py small-estate --stats    # print summary numbers
  python3 workspace/tools/render_hub_table.py small-estate --inject workspace/drafts/H2-small-estate/small-estate-affidavit-limits-by-state.html
  python3 workspace/tools/render_hub_table.py small-estate --inject <draft> --link-published
"""
import csv
import html
import os
import re
import statistics
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CAL = os.path.join(ROOT, "workspace", "plans", "editorial-calendar-2026-2027.csv")
START, END = "<!-- TABLE:START -->", "<!-- TABLE:END -->"

REAL = {"no": "Not allowed", "yes": "Included", "separate": "Separate procedure",
        "homestead": "Homestead only", "check": "Limited (see statute)"}
COURT = {"no": "None (affidavit)", "filed": "Filed with court office",
         "approval": "Judge approval", "petition": "Court petition"}


def e(s):
    return html.escape(str(s or ""), quote=True)


def published_slugs():
    """Spoke slugs whose calendar status is published."""
    if not os.path.exists(CAL):
        return {}
    out = {}
    with open(CAL, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["status"] == "published":
                out[r["slug"]] = r
    return out


def small_estate(rows, link):
    pub = published_slugs() if link else {}
    head = ["State", "Limit", "Real estate", "Wait", "Court step", "Law"]
    body = []
    for r in rows:
        slug = r["state"].lower().replace(" ", "-") + "-small-estate-affidavit"
        name = e(r["state"])
        if slug in pub:
            name = f'<a href="/{slug}/">{name}</a>'
        wait = f'{r["wait_days"]} days' if r["wait_days"] else "None set"
        body.append(
            f'<tr id="{r["code"].lower()}">\n<td>{name}</td>\n<td>{e(r["limit_text"])}</td>\n'
            f'<td>{REAL.get(r["real_estate"], e(r["real_estate"]))}</td>\n<td>{wait}</td>\n'
            f'<td>{COURT.get(r["court"], e(r["court"]))}</td>\n'
            f'<td><a href="{e(r["source_url"])}" rel="nofollow noopener" target="_blank">{e(r["statute"])}</a></td>\n</tr>')
    return head, body


def small_claims(rows, link):
    pub = published_slugs() if link else {}
    head = ["State", "Limit", "Other limits", "Court", "Filing fee", "Law"]
    body = []
    for r in rows:
        slug = r["state"].lower().replace(" ", "-") + "-small-claims-court"
        name = e(r["state"])
        if slug in pub:
            name = f'<a href="/{slug}/">{name}</a>'
        lim = e(r["limit_text"])
        if r["changed"]:
            lim += f'<br><small>{e(r["changed"])}</small>'
        body.append(
            f'<tr id="{r["code"].lower()}">\n<td>{name}</td>\n<td>{lim}</td>\n'
            f'<td>{e(r["other_limits"]) or "—"}</td>\n<td>{e(r["court"])}</td>\n<td>{e(r["fee_text"])}</td>\n'
            f'<td><a href="{e(r["source_url"])}" rel="nofollow noopener" target="_blank">{e(r["statute"])}</a></td>\n</tr>')
    return head, body


def divorce(rows, link):
    pub = published_slugs() if link else {}
    head = ["State", "Residency", "Waiting period", "No-fault ground", "Filing fee", "Law"]
    body = []
    for r in rows:
        slug = "how-to-file-for-divorce-in-" + r["state"].lower().replace(" ", "-")
        name = e(r["state"])
        if slug in pub:
            name = f'<a href="/{slug}/">{name}</a>'
        res = e(r["residency_text"])
        if r["changed"]:
            res += f'<br><small>{e(r["changed"])}</small>'
        body.append(
            f'<tr id="{r["code"].lower()}">\n<td>{name}</td>\n<td>{res}</td>\n<td>{e(r["wait_text"])}</td>\n'
            f'<td>{e(r["no_fault_text"])}</td>\n<td>{e(r["fee_text"])}</td>\n'
            f'<td><a href="{e(r["source_url"])}" rel="nofollow noopener" target="_blank">{e(r["statute"])}</a></td>\n</tr>')
    return head, body


RENDER = {"small-estate": small_estate, "small-claims": small_claims, "divorce": divorce}


def load(vertical):
    with open(os.path.join(ROOT, "workspace", "data", f"{vertical}.csv"), newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def table(vertical, link=False):
    head, body = RENDER[vertical](load(vertical), link)
    th = "".join(f"<th>{h}</th>" for h in head)
    return (f'{START}\n<div style="overflow-x: auto;">\n<table class="clt-table" style="min-width: 680px; font-size: .875rem;">\n'
            f"<thead>\n<tr>{th}</tr>\n</thead>\n<tbody>\n" + "\n".join(body) + f"\n</tbody>\n</table>\n</div>\n{END}")


def stats(vertical):
    rows = load(vertical)
    if vertical == "divorce":
        c = {}
        for r in rows:
            c[r["wait_from"]] = c.get(r["wait_from"], 0) + 1
        print("rows:", len(rows), "| wait_from:", c)
        res = sorted((int(r["residency_days"]), r["code"]) for r in rows)
        print("residency days:", res)
        print("no wait:", [r["code"] for r in rows if r["wait_from"] == "none"])
        print("changed:", [(r["code"], r["changed"]) for r in rows if r["changed"]])
        return
    if vertical != "small-estate":
        lim = sorted((int(r["limit_usd"]), r["state"]) for r in rows if r["limit_usd"])
        vals = [v for v, _ in lim]
        print("rows:", len(rows), "| max:", lim[-1], "min:", lim[0], "median:", statistics.median(vals))
        c = {}
        for v in vals:
            c[v] = c.get(v, 0) + 1
        print("by limit:", sorted(c.items()))
        ch = [(r["state"], r["changed"]) for r in rows if r["changed"]]
        print("changed:", len(ch))
        for x in ch:
            print("  ", x)
        return
    lim = [(int(r["limit_usd"]), r["state"]) for r in rows if r["limit_usd"]]
    vals = sorted(v for v, _ in lim)
    print("states with dollar limit:", len(lim), "| no cap:", [r["state"] for r in rows if not r["limit_usd"]])
    print("max:", max(lim), "min:", min(lim), "median:", statistics.median(vals))
    print(">=100k:", sum(v >= 100000 for v in vals), "| <=50k:", sum(v <= 50000 for v in vals))
    ch = [(r["state"], r["changed"]) for r in rows if r["changed"]]
    print("changed 2025-26:", len(ch), ch)
    for k in ("real_estate", "court"):
        c = {}
        for r in rows:
            c[r[k]] = c.get(r[k], 0) + 1
        print(k, c)
    w = [int(r["wait_days"]) for r in rows if r["wait_days"]]
    print("wait days:", sorted(set(w)), "most common:", statistics.mode(w))


def main():
    a = sys.argv[1:]
    vertical = a[0]
    if "--stats" in a:
        return stats(vertical)
    t = table(vertical, "--link-published" in a)
    if "--inject" in a:
        p = a[a.index("--inject") + 1]
        s = open(p, encoding="utf-8").read()
        if START not in s:
            sys.exit(f"{p}: no {START} marker")
        s = re.sub(re.escape(START) + ".*?" + re.escape(END), lambda m: t, s, flags=re.S)
        open(p, "w", encoding="utf-8").write(s)
        print(f"injected table into {p}")
    else:
        print(t)


if __name__ == "__main__":
    main()
