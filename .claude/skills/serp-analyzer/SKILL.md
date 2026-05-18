---
name: serp-analyzer
description: Analyzes search engine results for target keywords to understand what Google is rewarding and identify ranking opportunities for ClearLegalTips. Use when asked to "analyze SERP", "what's ranking for X", "competitor analysis", "what does Google want for this keyword", or before writing any new article.
---

# SERP Analyzer

## Context

SERP analysis reveals what Google considers the best answer for a query. For ClearLegalTips, this determines: content format, required sections, schema types, word count targets, and competitive differentiation angles.

Target keywords are legal DIY topics in the US market. Main competitors: Nolo.com, LegalZoom Blog, UpCounsel, Avvo, Rocket Lawyer Blog, FindLaw.

## Instructions

### Step 1 — Query Classification

Before analyzing, classify the keyword:

| Intent Type | Signal | ClearLegalTips Strategy |
|---|---|---|
| Informational | "what is", "how does", "explain" | Long-form guide, FAQ schema |
| Navigational | Brand names in query | Comparison article |
| Commercial | "best", "top", "vs", "review" | Comparison + affiliate CTAs |
| Transactional | "template", "form", "download", "free" | Template article + direct CTA |

### Step 2 — SERP Feature Inventory

Note which SERP features appear:
- [ ] Featured snippet (paragraph / list / table)
- [ ] People Also Ask box
- [ ] Knowledge panel
- [ ] Image pack
- [ ] Video results
- [ ] Local pack
- [ ] Sitelinks

**Featured snippet present?** → Write a direct 40–60 word answer in the first H2 answer block.  
**PAA present?** → Use PAA questions as FAQ section headings.  
**Table in snippet?** → Include a comparison table early in the article.

### Step 3 — Top 5 Results Analysis

For each top-ranking result, document:

```
Rank [X]: [URL]
Domain Authority: [estimate — Nolo=high, small blog=low]
Content Format: [guide / list / FAQ / tool]
Word Count: [estimate]
H2 Sections: [list]
Schema Present: [FAQPage / HowTo / Article / none]
Affiliate Links: [yes/no — which services]
Key Strengths: [what makes it rank]
Key Weaknesses: [what's missing or thin]
```

### Step 4 — Gap Identification

After analyzing all results:
1. **Coverage gap** — topics none of the top 5 cover
2. **Depth gap** — topics covered superficially
3. **Format gap** — no comparison table / no FAQ / no state breakdown
4. **Freshness gap** — outdated stats/years
5. **Intent gap** — results don't fully match what the searcher needs

### Step 5 — Winning Strategy

Based on gaps, define how ClearLegalTips will beat the current results:
- **10x content** (cover everything, cover it better)
- **Format advantage** (add table/FAQ/schema no one else has)
- **Freshness** (more current data)
- **Local specificity** (state-specific data)
- **Trust signals** (author bio, legal disclaimer, cited sources)

## Output Format

```
SERP ANALYSIS: "[keyword]"
Date: [date]
Search Intent: [informational | commercial | transactional]

SERP FEATURES PRESENT:
- Featured Snippet: YES/NO — [type if yes]
- People Also Ask: YES/NO — [questions if yes]
- Image Pack: YES/NO

TOP RESULTS:
#1: [domain] — [format] — [word count est.] — [key H2s] — [strength/weakness]
#2: [domain] — ...
#3: [domain] — ...

GAPS FOUND:
1. [gap] — [how to fill it]
2. [gap] — [how to fill it]
3. [gap] — [how to fill it]

WINNING STRATEGY FOR CLEARLEGALTIPS:
[2–3 sentence description of how to write an article that outranks these results]

RECOMMENDED CONTENT FORMAT: [guide | list | comparison | template]
RECOMMENDED SCHEMA: [FAQPage | HowTo | Both]
TARGET WORD COUNT: [X]
FEATURED SNIPPET OPPORTUNITY: YES/NO — [what format to use]

PEOPLE ALSO ASK (use as FAQ headings):
- [question 1]
- [question 2]
- [question 3]
```
