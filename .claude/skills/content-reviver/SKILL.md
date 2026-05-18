---
name: content-reviver
description: Rewrites or substantially upgrades underperforming ClearLegalTips articles to recover or improve their search rankings. Use when asked to "revive this article", "article not ranking", "rewrite for better SEO", "this article is underperforming", or "update and improve post [ID]".
---

# Content Reviver

## Context

Content Reviver goes deeper than Content Refresher. While Refresher updates dates/prices, Reviver does a **full strategic rewrite** of articles that are:
- Ranking on page 2–3 (positions 11–30) — tantalizingly close but not getting clicks
- Getting traffic but low time-on-page (bounce rate >75%)
- Getting traffic but zero affiliate clicks
- >12 months old with significant competitive content improvements

ClearLegalTips has 50 articles. Reviver applies to the bottom 10–15 performers.

## Revival Triggers

Run this skill when ANY of these are true:
- Article ranks position 11–30 for its primary keyword
- Article gets >500 monthly impressions but <1% CTR
- Article has high traffic but affiliate CTR <0.5%
- Competitor added better content on the same topic in last 6 months
- Article is thin (<2,500 words) on a topic that deserves depth

## Revival Framework — 5-Level Approach

### Level 1 — Hook & Structure Fix (30 min)
- Rewrite the opening 200 words using hook-analyzer criteria
- Restructure H2s to match SERP intent better
- Add missing sections competitors have
- Fix weak CTA placement

### Level 2 — Depth Expansion (60 min)
- Add 500–1,000 words to thin sections
- Add a comparison table if one is missing
- Add state-specific data where relevant
- Add real-world examples / mini case study

### Level 3 — Schema & Snippet Optimization (20 min)
- Add/rewrite FAQ section (5+ questions)
- Add FAQPage schema
- Add HowTo schema if process article
- Optimize for featured snippet (direct 40–60 word answer blocks)

### Level 4 — Trust Signal Upgrade (20 min)
- Add author byline with expertise note
- Add/update external citations (government sources, .gov links)
- Add "Last updated: [date]" prominently
- Add a credibility callout box: "Reviewed by [author], [credentials]"

### Level 5 — Full Rewrite (2–4 hours)
When levels 1–4 aren't enough: treat as a new article. Keep the URL (slug). Delete the old content. Use seo-brief-builder to create a new brief first, then legal-blog-writer to produce the article.

## Instructions

1. **Diagnose the article** — which revival triggers apply? Which level is needed?
2. **Audit the gaps** — compare against top 3 competitors on the same keyword
3. **Execute the revival** — apply the appropriate level
4. **Verify Rank Math score** — target ≥80 after revival
5. **Update post modified date** — `wp_update_post` with current timestamp
6. **Flush cache** — WP Fastest Cache flush after update

## Diagnosis Checklist

```
ARTICLE REVIVAL DIAGNOSIS: Post [ID] — [Title]

PERFORMANCE SIGNALS:
- Current ranking position: [X] for "[keyword]"
- Monthly impressions: [X] | CTR: [X]%
- Bounce rate estimate: [high/medium/low]
- Affiliate clicks: [X]

CONTENT AUDIT:
- Word count: [X] (target: 3,000+)
- Has FAQ section: YES/NO
- Has schema: YES/NO
- Has comparison table: YES/NO
- Hook quality: [1-5]
- CTA placement: [above fold? / how many?]

TOP COMPETITOR GAPS:
- [Competitor 1] has: [what we're missing]
- [Competitor 2] has: [what we're missing]

REVIVAL LEVEL NEEDED: 1 / 2 / 3 / 4 / 5
ESTIMATED TIME: [X] minutes/hours
```

## Output Format

For Level 1–4: Output the specific additions/rewrites as HTML blocks ready to replace existing content.

For Level 5: Output "FULL REWRITE NEEDED — use seo-brief-builder then legal-blog-writer" with the brief parameters filled in.

```
REVIVAL PLAN: Post [ID]
Level: [1-5]
Primary Changes:
1. [change + why]
2. [change + why]

[REVISED CONTENT BLOCKS — HTML]

POST-REVIVAL CHECKLIST:
- [ ] Rank Math score ≥ 80
- [ ] All required elements present (disclosure, disclaimer, CTA, related)
- [ ] Modified date updated
- [ ] Cache flushed
```
