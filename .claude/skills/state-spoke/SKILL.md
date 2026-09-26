---
name: state-spoke
description: Drafts a hub or state/country spoke post for the 2026-2027 vertical hub program (small estate, small claims, divorce, judgment, non-resident, etc.) from the editorial calendar, the verified data CSV, and the QA gate. Use for "draft next spoke", "draft W05", "write the Texas small claims page", or any calendar row in workspace/plans/editorial-calendar-2026-2027.csv.
allowed-tools: Read Write Edit Bash WebSearch WebFetch
effort: high
---

Draft one calendar row (or one week of rows) as a ready-to-paste package.

## Input: $ARGUMENTS
A slug from the calendar, or a week code like `W05`.

## Files
| Path | Role |
|---|---|
| `workspace/plans/editorial-calendar-2026-2027.csv` | Date, hub, type, slug, working title, category, focus keyword |
| `workspace/plans/vertical-hubs-plan-2026-2027.md` | Approved plan: hub scope, spoke contents, CTAs |
| `workspace/data/<vertical>.csv` | Verified 50-state + DC data. Single source of truth |
| `workspace/data/live-slugs.txt` | Slugs live on clearlegaltips.com (refresh via REST before a batch) |
| `workspace/drafts/<hub>/<slug>.html` + `.meta.json` | Output |
| `workspace/drafts/<hub>/hub-link-updates/Wnn.md` | Friday patch: link the week's new spokes from the hub and siblings |
| `workspace/tools/qa_draft.py` | Quality gate, must print 0 errors |

## Steps

### 1. Verify the data row(s) first
- Open the state's row in the vertical CSV. If `verified_date` is older than 60 days, or the row is empty, re-verify it.
- Sources allowed in `source_url`: the state legislature's code, the court system (courts.*.gov, judicial branch self-help), the agency (SOS, DOL, IRS, FinCEN), or the session law. Law.justia / law.cornell mirrors are acceptable when the official site will not deep-link. Give the citation text so readers can find it.
- Competitor sites (programmatic "by state" sites, law-firm blogs, form sellers) are leads only and never go in `source_url`.
- Search for 2025-2026 changes on the legislature site ("<topic> <state> 2025 bill" / "2026 amendment"). Record them in `notes` with an effective date.
- If two official sources conflict, use the statute and say so in the article.

### 2. Draft the HTML
Structure (spoke):
1. `clt-disclosure` (exact live wording, see write-seo-post)
2. `clt-download-box`: 2–3 buttons. PDF filenames come from meta `pdf_filename`; the user generates the files locally.
3. `clt-keytakeaway`: "The short version (2026/2027):" with the 3–5 numbers that answer the query
4. 2–3 intro paragraphs: focus keyword in the first 100 words, plain answer first
5. H2 sections with concrete numbers in the headings (model: live post 7538 `texas-llc-filing-fee`). Cover the plan's "spoke contents" list for the hub.
6. One `clt-cta-box` after the section where the reader needs the document/service (`/go/` slug from the plan, `rel="nofollow sponsored"`)
7. "Where {State} ranks" section comparing against the other states (link the hub only if the hub date is earlier)
8. `## Frequently Asked Questions`: 5–6 H3 Q&As plus a FAQPage JSON-LD with identical text, inside `<p><script type="application/ld+json">…</script></p>` as on the live site
9. `clt-related-articles`: 3 links, each live or earlier in the calendar
10. `clt-sources`: every URL used, then `<p><em>Fact-checked: {Month Year}</em></p>`
11. `clt-disclaimer`: live wording, last element

Hubs add (model: live post 5921 `security-deposit-limits-by-state`):
- The full 50-state + DC table in `<div style="overflow-x: auto;"><table class="clt-table">`, rows with `id="{state code}"`, a Source column, and a "Last updated" line
- The widget placeholder `<!-- WIDGET: <tool> (paste workspace/widgets/<tool>.html as a Custom HTML block here) -->`
- "Key Findings", "What Changed in 2025–2026", "How We Verified This Data", "Cite or Download This Data" (CSV + CC BY 4.0)
- State rows link to spoke slugs only once that spoke is published. Before that, plain text; the Friday patch adds the link.

Inline images: put `<!-- IMAGE: <alt text> | <prompt> -->` comments where the model post has a `clt-inline-image` figure, and list them in meta `inline_images`.

Writing rules: plain English, answer first, short paragraphs, no filler, no invented statistics, no fictional people, no "attorney-reviewed". Say "general information, not legal advice" where the reader might act on it. County variation: name the 3–5 biggest counties with their actual fee or say "check your county clerk" with the link.

### 3. Write meta.json
```json
{
  "slug": "", "publish_date": "YYYY-MM-DD", "title": "<H1, may exceed 60>",
  "rank_math_title": "<=60 chars", "rank_math_description": "<=155 chars",
  "focus_keyword": "", "category_id": 7, "tags": ["existing tag", "..."],
  "go_slugs": ["lawdepot-affidavit-form"], "internal_links": ["/slug/"],
  "sources": ["https://..."], "pdf_filename": "xx-....pdf",
  "pdf_outline": ["section", "..."], "featured_image_prompt": "",
  "inline_images": [{"alt": "", "prompt": ""}], "editor_notes": ""
}
```

### 4. QA
```bash
python3 workspace/tools/qa_draft.py workspace/drafts/<hub>/<slug>.html
```
Fix every ERROR. Warnings need a reason in `editor_notes` if left.

### 5. Friday patch
For each week, write `hub-link-updates/Wnn.md`: which hub table rows and sibling "Related Articles" lists get links to the spokes published that week (old text → new text), plus any live post (e.g. 3131, 165, 163) that should link in.

### 6. Commit
One commit per publish week: `drafts: Wnn <hub> (5)`.
