---
name: seo-brief-builder
description: Creates detailed SEO content briefs for new ClearLegalTips articles before writing begins. Use when asked to "create a brief", "content brief", "article brief", "brief for [topic]", or before using legal-blog-writer skill.
allowed-tools: Read Write WebSearch WebFetch
effort: medium
---

# SEO Brief Builder

## Context

A content brief is the planning document that runs BEFORE writing. It defines the keyword target, structure, competition gaps, required sections, and affiliate placement strategy. Using a brief ensures every new article scores ≥80 on Rank Math and targets real search intent.

ClearLegalTips article types: template | cost/calculator | how-to guide | state guide

## Instructions

### Step 1 — Keyword Analysis
- Primary keyword (exact match for H1)
- Secondary keywords (3–5, for H2s and body)
- LSI keywords (semantic variations to include naturally)
- Search intent classification: informational / navigational / commercial / transactional

### Step 2 — SERP Analysis
Research the top 3–5 ranking pages for the primary keyword:
- What content format do they use? (list, guide, comparison, FAQ)
- What H2 sections do they cover?
- What do they miss? (gaps = your opportunity)
- What's the average word count?
- Do any have featured snippets? (FAQ, table, list)

### Step 3 — Article Architecture
Define the exact structure:
```
H1: [primary keyword — exact or close variant]
H2: [section 1]
  H3: [subsection if needed]
H2: [section 2]
...
H2: Frequently Asked Questions
H2: Final Thoughts / Conclusion
```

### Step 4 — Affiliate Integration Plan
- Which affiliate(s) to feature
- Where to place first CTA (after which H2)
- Comparison section needed? (which services to compare)
- ThirstyAffiliates slugs to use

### Step 5 — Required Elements Checklist
Every article needs:
- [ ] FTC disclosure box (top)
- [ ] Primary keyword in H1
- [ ] Primary keyword in first 100 words
- [ ] At least 1 CTA button above fold (within first 600 words)
- [ ] FAQ section (3–5 questions, schema-ready)
- [ ] Internal link box (3 related articles)
- [ ] Legal disclaimer (bottom)
- [ ] Featured image prompt (for ComfyUI)

### Step 6 — Word Count & Depth Target
| Article Type | Target Words | Depth |
|---|---|---|
| Template article | 2,500–3,500 | Template explanation + usage guide |
| Cost guide | 3,000–4,000 | State-by-state breakdown + comparison table |
| How-to guide | 3,500–5,000 | Step-by-step + screenshots descriptions |
| State guide | 3,000–4,000 | State-specific rules + comparison with nearby states |

## Output Format

```
═══════════════════════════════════════════════
SEO CONTENT BRIEF
═══════════════════════════════════════════════
Article Title (H1): [title]
Article Type: [template | cost | how-to | state guide]
Primary Keyword: [keyword] | Est. Volume: [X]/mo
Secondary Keywords: [list]
Target Author: [Sarah Jenkins | Marcus Thorne | Elena Rodriguez | David Miller]
Target Word Count: [X]
Target Affiliate(s): [service — ThirstyAffiliates slug]
Publish Date: [next staggered slot — query latest WP `post_date` + 1 day]

SEARCH INTENT: [informational / commercial]

COMPETITOR GAPS (what to cover that top 3 don't):
1. [gap 1]
2. [gap 2]
3. [gap 3]

ARTICLE STRUCTURE:
H1: [title]
  [FTC Disclosure]
  Intro (150-200 words): [what to cover]
H2: [section] — [what to cover, ~word count]
H2: [section] — [what to cover, ~word count]
...
H2: Frequently Asked Questions
  Q: [question 1]
  Q: [question 2]
  Q: [question 3]
H2: Final Thoughts
  [CTA box]
  [Related articles box]
  [Legal disclaimer]

AFFILIATE INTEGRATION:
- First CTA placement: after H2 "[section name]"
- CTA button text: "[text]"
- Comparison section: YES/NO — comparing [service A] vs [service B]

SCHEMA TYPE: FAQPage | HowTo | Both

INTERNAL LINKS (3 required):
1. Link to: [article title] (/[slug]) — anchor: [text]
2. Link to: [article title] (/[slug]) — anchor: [text]
3. Link to: [article title] (/[slug]) — anchor: [text]

FEATURED IMAGE PROMPT (ComfyUI):
"[descriptive prompt for legal-themed image, navy blue tones]"

RANK MATH TARGETS:
Focus Keyword: [keyword]
SEO Title (XX chars): [title]
Meta Description (XXX chars): [description]
═══════════════════════════════════════════════
```
