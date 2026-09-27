---
description: Full audit of a single ClearLegalTips article. Checks SEO, CRO, hook quality, schema, internal links, and brand voice. Pass a post ID or URL.
---

# Single Article Audit

Run a comprehensive audit on post: **$ARGUMENTS**

## Audit Checklist

### 1 — Fetch Content
Read the article content via WP-CLI:
```php
$post = get_post($pid);
$meta = get_post_meta($pid);
echo "Title: " . $post->post_title . "\n";
echo "Words: " . str_word_count(strip_tags($post->post_content)) . "\n";
echo "Rank Math Title: " . ($meta['rank_math_title'][0] ?? 'MISSING') . "\n";
echo "Rank Math Desc: " . ($meta['rank_math_description'][0] ?? 'MISSING') . "\n";
echo "Focus KW: " . ($meta['rank_math_focus_keyword'][0] ?? 'MISSING') . "\n";
echo "Schema type: " . ($meta['rank_math_rich_snippet'][0] ?? 'MISSING') . "\n";
```

### 2 — Hook Quality
Use `hook-analyzer` on the first 150 words. Score out of 25. Flag if < 18/25.

### 3 — SEO Meta Quality
Use `seo-meta-optimizer` to evaluate (not rewrite — just score):
- Title: keyword present? Under 60 chars? Has brand? Power word?
- Description: benefit-forward? Under 155 chars? Has CTA word?
- Focus keyword density in content (target: 0.5–1.5%)

### 4 — Schema Status
Use `schema-markup-legal` to check:
- Does the article have a FAQ section? Is it schema-ready?
- Is `rank_math_rich_snippet` set?
- Is the JSON-LD block present in post_content?

### 5 — CTA Audit
Use `affiliate-cta-optimizer` to check all 7 dimensions:
1. Value proposition clarity (first 2 seconds)
2. Headline effectiveness (H1 matches search intent?)
3. CTA placement — is there one above fold? One mid-article? One at end?
4. CTA copy quality — does it use the formula: [Action] + [Outcome] + [Price anchor]?
5. Trust signals — author bio, publish date, disclaimer visible?
6. Objection handling — "is this free?", "is this legal advice?" addressed?
7. Friction points — any affiliate link using direct URL instead of `/recommend/`?

### 6 — Internal Link Health
Use `internal-link-auditor` to check:
- Does the article have a `clt-related-articles` div?
- Are there 3 internal links?
- Are the links to appropriate hub/spoke partners?

### 7 — Brand Voice Check
Use `brand-voice-legal` to scan for:
- Legal advice language ("you must", "you should" without qualifier)
- Missing hedging on legal claims
- Tone issues (alarmist, condescending, overly casual)

### 8 — Required Elements
Verify presence of:
- [ ] `<div class="clt-disclosure">` at top
- [ ] `<div class="clt-disclaimer">` at bottom
- [ ] `<div class="clt-related-articles">` with 3 links
- [ ] Minimum 2 `clt-affiliate-btn` CTAs
- [ ] Primary keyword in H1 and first 100 words

## Output Format

```
AUDIT REPORT — Post [ID]: "[title]"
Date: [date]

SCORES:
Hook quality:       [X/25] [PASS/FAIL — threshold 18]
SEO title:          [PASS/FAIL] — [issue if fail]
SEO description:    [PASS/FAIL] — [issue if fail]
Schema:             [SET/MISSING] — type: [faqpage/howto/none]
CTA count:          [X] — placement: [above fold? mid? end?]
Internal links:     [X] — [PASS/FAIL — threshold 3]
Brand voice:        [PASS/FAIL] — [issue if fail]
Required elements:  [X/5] present

TOP 3 PRIORITIES:
1. [highest impact fix]
2. [second fix]
3. [third fix]

PHP FIX SNIPPETS:
[ready-to-run PHP for any meta fixes identified]
```
