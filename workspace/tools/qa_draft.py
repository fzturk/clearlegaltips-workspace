#!/usr/bin/env python3
"""Quality gate for ClearLegalTips draft packages (HTML + meta.json).

Checks each workspace/drafts/<hub>/<slug>.html against CLAUDE.md rules and the
editorial calendar. Exit code 1 if any ERROR is found.

Usage:
  python3 workspace/tools/qa_draft.py workspace/drafts/H2-small-estate/
  python3 workspace/tools/qa_draft.py workspace/drafts/H2-small-estate/texas-small-estate-affidavit.html
  python3 workspace/tools/qa_draft.py <path> --check-links   # also fetch every external URL (404 = error)
"""
import csv
import glob
import html as htmllib
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CAL = os.path.join(ROOT, "workspace", "plans", "editorial-calendar-2026-2027.csv")
LIVE = os.path.join(ROOT, "workspace", "data", "live-slugs.txt")

REQUIRED_CLASSES = ["clt-disclosure", "clt-download-box", "clt-cta-box",
                    "clt-affiliate-btn", "clt-related-articles", "clt-disclaimer"]
BANNED = [r"attorney[- ]reviewed", r"reviewed by (an? )?attorney", r"lawyer[- ]reviewed",
          r"Sarah Jenkins", r"Marcus Thorne", r"Elena Rodriguez", r"David Miller",
          r"/recommend/", r"\bEsq\.", r"\bJ\.D\.\b"]
AFFILIATE_HOSTS = ["lawdepot.com", "doola.com", "termly.io", "doorloop.com", "keepertax.com",
                   "trustandwill.com", "onlinedivorce.com", "completecase.com", "nextinsurance.com",
                   "gusto.com", "anrdoezrs", "jdoqocy", "tkqlhce", "dpbolvw", "kqzyfj", "partnerstack", "impact.com"]
MIN_WORDS = {"hub": 3000, "hub-upgrade": 3000, "spoke": 1900}


def load_calendar():
    with open(CAL, newline="", encoding="utf-8") as f:
        return {r["slug"]: r for r in csv.DictReader(f)}


def load_live():
    if not os.path.exists(LIVE):
        return set()
    with open(LIVE, encoding="utf-8") as f:
        return {l.strip() for l in f if l.strip()}


def text_of(h):
    h = re.sub(r"<script.*?</script>", " ", h, flags=re.S)
    h = re.sub(r"<style.*?</style>", " ", h, flags=re.S)
    return htmllib.unescape(re.sub(r"<[^>]+>", " ", h))


def check(path, cal, live):
    errs, warns = [], []
    slug = os.path.basename(path)[:-5]
    h = open(path, encoding="utf-8").read()
    row = cal.get(slug)
    if not row:
        errs.append("slug not in editorial calendar")
        return errs, warns

    meta_path = path[:-5] + ".meta.json"
    meta = {}
    if not os.path.exists(meta_path):
        errs.append("missing .meta.json")
    else:
        try:
            meta = json.load(open(meta_path, encoding="utf-8"))
        except ValueError as e:
            errs.append(f"meta.json invalid: {e}")

    # required elements
    for c in REQUIRED_CLASSES:
        if f'class="{c}' not in h and f"class='{c}" not in h and not re.search(rf'class="[^"]*\b{c}\b', h):
            errs.append(f"missing element .{c}")
    if h.find("clt-disclosure") > h.find("/go/") > -1:
        errs.append("FTC disclosure must come before the first /go/ link")
    if h.rfind("clt-disclaimer") < h.rfind("clt-related-articles"):
        warns.append("disclaimer should be the last box")

    # FAQ schema
    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, flags=re.S)
    if not blocks:
        errs.append("no JSON-LD block")
    faq = False
    for b in blocks:
        try:
            data = json.loads(b)
        except ValueError as e:
            errs.append(f"invalid JSON-LD: {e}")
            continue
        items = data if isinstance(data, list) else data.get("@graph", [data])
        faq = faq or any(isinstance(i, dict) and i.get("@type") == "FAQPage" for i in items)
    if blocks and not faq:
        errs.append("no FAQPage schema")

    # words
    words = len(text_of(h).split())
    need = MIN_WORDS.get(row["type"], 1900)
    if words < need:
        errs.append(f"word count {words} < {need}")

    # banned phrases
    for b in BANNED:
        if re.search(b, h, flags=re.I):
            errs.append(f"banned phrase: {b}")

    # affiliate links must be /go/
    for href in re.findall(r'href="([^"]+)"', h):
        if any(a in href for a in AFFILIATE_HOSTS):
            errs.append(f"direct affiliate URL (use /go/): {href}")
    for a in re.findall(r"<a [^>]*href=\"/go/[^\"]+\"[^>]*>", h):
        if "sponsored" not in a:
            errs.append(f"/go/ link missing rel=sponsored: {a[:80]}")

    # internal links: live or published earlier in the calendar
    my_date = row["date"]
    for s in re.findall(r'href="(?:https://clearlegaltips\.com)?/([a-z0-9-]+)/?(?:#[^"]*)?"', h):
        if s in ("go", "wp-content", "affiliate-disclosure", "editorial-standards", "editor-fatih-ozturk",
                 "legal-disclaimer", "about-clearlegaltips", "contact", "privacy-policy"):
            continue
        if s in live:
            continue
        other = cal.get(s)
        if other and other["date"] < my_date:
            continue
        if other:
            errs.append(f"links to /{s}/ which publishes later ({other['date']})")
        else:
            errs.append(f"links to unknown slug /{s}/ (not live, not in calendar)")

    # sources
    if "clt-sources" not in h:
        errs.append("missing .clt-sources block")
    if not re.search(r"Fact-checked:\s*\w+ \d{4}", h):
        errs.append("missing 'Fact-checked: {Month Year}' line")
    ext = [u for u in re.findall(r'href="(https?://[^"]+)"', h) if "clearlegaltips.com" not in u]
    if len(ext) < 3:
        errs.append(f"only {len(ext)} external source links (need >=3)")

    # meta
    if meta:
        t, d = meta.get("rank_math_title", ""), meta.get("rank_math_description", "")
        if not t or len(t) > 60:
            errs.append(f"rank_math_title length {len(t)} (1-60)")
        if not d or len(d) > 155:
            errs.append(f"rank_math_description length {len(d)} (1-155)")
        kw = meta.get("focus_keyword", "").lower()
        if kw and kw not in text_of(h).lower()[:1500]:
            warns.append("focus keyword not in first ~100 words")
        if str(meta.get("category_id")) != str(row["category_id"]):
            errs.append(f"category_id {meta.get('category_id')} != calendar {row['category_id']}")
        if meta.get("publish_date") != row["date"]:
            errs.append(f"publish_date {meta.get('publish_date')} != calendar {row['date']}")
        for k in ("title", "tags", "sources", "pdf_filename", "featured_image_prompt"):
            if not meta.get(k):
                errs.append(f"meta missing {k}")
    return errs, warns


_LINK_CACHE = {}


def link_status(url):
    """HTTP status via curl (follows redirects). 0 = no response."""
    if url not in _LINK_CACHE:
        r = subprocess.run(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "-L", "-m", "20",
                            "-A", "Mozilla/5.0", url], capture_output=True, text=True)
        _LINK_CACHE[url] = int(r.stdout or 0)
    return _LINK_CACHE[url]


def check_links(path):
    errs, warns = [], []
    h = open(path, encoding="utf-8").read()
    for u in sorted(set(re.findall(r'href="(https?://[^"]+)"', h))):
        u = htmllib.unescape(u)
        if "clearlegaltips.com" in u:
            continue
        code = link_status(u)
        if code in (404, 410):
            errs.append(f"dead link {code}: {u}")
        elif code == 0 or code >= 500 or code in (401, 403):
            warns.append(f"link not verifiable ({code}): {u}")
    return errs, warns


def main():
    argv = [a for a in sys.argv[1:] if a != "--check-links"]
    want_links = "--check-links" in sys.argv
    args = argv or [os.path.join(ROOT, "workspace", "drafts")]
    files = []
    for a in args:
        if os.path.isdir(a):
            files += sorted(glob.glob(os.path.join(a, "**", "*.html"), recursive=True))
        else:
            files.append(a)
    files = [f for f in files if "/hub-link-updates/" not in f]
    cal, live = load_calendar(), load_live()
    if not live:
        print("WARN: workspace/data/live-slugs.txt missing; internal links to live posts will fail")
    total = 0
    for f in files:
        errs, warns = check(f, cal, live)
        if want_links:
            e2, w2 = check_links(f)
            errs += e2
            warns += w2
        total += len(errs)
        status = "OK " if not errs else "ERR"
        print(f"[{status}] {os.path.relpath(f, ROOT)}")
        for e in errs:
            print(f"    ERROR: {e}")
        for w in warns:
            print(f"    warn:  {w}")
    print(f"\n{len(files)} file(s), {total} error(s)")
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
