---
name: seo-keyword-hunter
description: Finds high-value keyword opportunities for ClearLegalTips beyond the existing 50 articles. Use when asked to "find keywords", "keyword research", "what keywords should we target", "expand keyword coverage", or before planning new articles.
allowed-tools: Read Write WebSearch WebFetch
effort: high
---

# SEO Keyword Hunter

## Context

ClearLegalTips targets US adults doing DIY legal tasks. Current coverage: 50 articles across templates (131–150), cost guides (151–165), how-to guides (166–175), state guides (176–180). Affiliate revenue comes from LawDepot, ZenBusiness, Northwest Registered Agent, Rocket Lawyer, LegalZoom, Nolo, Incfile.

**Revenue-weighted keyword priority:** Keywords that lead to affiliate clicks > pure traffic keywords.

## Keyword Evaluation Framework

Score each keyword opportunity on 4 dimensions (1–5 each):

| Dimension | What It Measures |
|---|---|
| **Search Volume** | Monthly US searches (use estimates: <500=1, 500–2K=2, 2K–5K=3, 5K–20K=4, >20K=5) |
| **Affiliate Intent** | Does the searcher likely need a paid service? (low=1, high=5) |
| **Difficulty** | How hard to rank? (easy=5, hard=1) |
| **Coverage Gap** | Does ClearLegalTips have this? (covered=1, gap=5) |

**Priority Score = Volume + Affiliate Intent + Difficulty + Coverage Gap**
Score ≥ 16: Write immediately | 12–15: Plan within 60 days | <12: Monitor

## High-Value Keyword Categories

### 1. Service Comparison (highest affiliate intent)
- "[Service A] vs [Service B]" — ZenBusiness vs Northwest, LegalZoom vs Rocket Lawyer
- "best LLC formation service [year]"
- "cheapest way to form an LLC"
- "incfile vs zenbusiness vs northwest"

### 2. State-Specific LLC (high volume × 50 states)
- "how to form an LLC in [state]"
- "[state] LLC requirements"
- "[state] LLC annual report"
- "[state] registered agent requirements"

### 3. Cost/Price Queries
- "how much does [legal document] cost"
- "[state] LLC filing fee [year]"
- "registered agent fee comparison"
- "cost to dissolve an LLC"

### 4. Template Variants
- "free [document type] template [state]"
- "simple [document] template"
- "printable [document] form"
- "[document] template word/pdf"

### 5. Process/How-To
- "how to [legal task] without a lawyer"
- "do I need a lawyer to [task]"
- "can I [legal task] myself"
- "DIY [legal task] guide"

### 6. Long-Tail Informational
- "what happens if you don't have an operating agreement"
- "can an LLC have one member"
- "difference between LLC and sole proprietorship"

## Instructions

1. **Understand scope** — topic area, article type, target affiliate
2. **Generate 20–30 keyword candidates** from the categories above
3. **Score each** using the 4-dimension framework
4. **Cluster related keywords** — group into articles (1 article can target 3–5 related keywords)
5. **Output prioritized list** with article recommendations

## Output Format

```
KEYWORD RESEARCH: [Topic/Scope]
Date: [date]

TOP OPPORTUNITIES (Score ≥ 16):
┌─────────────────────────────────────────────────────────────────┐
│ Keyword: [keyword]
│ Est. Volume: [X]/mo | Affiliate Intent: [X/5] | Difficulty: [X/5] | Gap: [X/5]
│ Priority Score: [X/20]
│ Recommended Article: [title]
│ Target Affiliate: [service]
│ Notes: [why this is valuable]
└─────────────────────────────────────────────────────────────────┘

STATE EXPANSION OPPORTUNITIES:
- [existing article] can be forked into [X] state-specific variants
  High-priority states: [list by population/search volume]

KEYWORD CLUSTERS (group into single articles):
- Article: "[title]" → covers keywords: [list]
```

## Quick Win Targets (Pre-Researched)

These are known high-value gaps based on competitor analysis:

| Keyword | Est. Volume | Affiliate | Score |
|---|---|---|---|
| zenbusiness vs northwest registered agent | 3,000/mo | High | 17/20 |
| how to form an LLC in Texas | 8,000/mo | High | 18/20 |
| best registered agent service | 5,000/mo | High | 17/20 |
| free LLC operating agreement template | 4,000/mo | Medium | 16/20 |
| how to dissolve an LLC | 2,500/mo | Low | 14/20 |
| single member LLC operating agreement | 3,500/mo | Medium | 16/20 |
