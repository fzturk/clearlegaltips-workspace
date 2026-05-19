---
description: Competitor content gap analysis for ClearLegalTips. Finds topics competitors rank for that ClearLegalTips doesn't cover. Pass a competitor domain (e.g. nolo.com) or "all" for analysis against all main competitors.
---

# Content Gap Analysis

Run competitor gap analysis against: **$ARGUMENTS**

Default competitors (if `$ARGUMENTS` is `all`):
- nolo.com
- legalzoom.com/articles
- upcounsel.com
- avvo.com
- findlaw.com/legal-professionals

## Gap Analysis Workflow

### Step 1 — Map ClearLegalTips Coverage

Inventory all 50 existing articles by topic:
- **Template articles** (IDs 131–150): legal document templates
- **Cost/calculator articles** (IDs 151–165): fee guides
- **How-to guides** (IDs 166–175): step-by-step online services
- **State/specialty guides** (IDs 176–180): state-specific content

Extract: primary keyword, topic cluster, affiliate services mentioned.

### Step 2 — Competitor Analysis

Use `content-gap-finder` skill on the target domain(s):

For each competitor:
1. Identify their top 30 legal content URLs (by estimated traffic)
2. Map to topic clusters:
   - LLC formation
   - Contract templates
   - Estate planning / wills
   - Divorce / family law
   - Real estate / leases
   - Business formation (other)
   - State-specific guides
3. Note: affiliate services they promote, schema types, word counts

### Step 3 — Gap Identification

Cross-reference competitor topics against ClearLegalTips coverage:

**Coverage gap** = competitor ranks in top 10, ClearLegalTips has no article on the topic
**Depth gap** = ClearLegalTips has an article but competitor's version is significantly more comprehensive
**State gap** = competitor has state-specific versions, ClearLegalTips only has generic national guide

Use `seo-keyword-hunter` to score each gap by:
- Search volume (use keyword data if available, estimate if not)
- Affiliate intent (does it lead naturally to a ZenBusiness/LawDepot/etc. recommendation?)
- Competition difficulty (can ClearLegalTips realistically rank?)
- Revenue potential (high-commission affiliate services = higher priority)

### Step 4 — Prioritized Gap List

Output gaps in three tiers:

**Tier 1 — Quick wins** (write now):
- Gaps where ClearLegalTips can likely rank in 3–6 months
- Topic naturally leads to high-commission affiliate recommendation
- Competitor content is thin or outdated

**Tier 2 — Medium-term** (write next quarter):
- Competitive topics requiring strong content to rank
- Good affiliate fit but harder to win

**Tier 3 — Research needed** (evaluate later):
- Highly competitive, unclear affiliate monetization path

### Step 5 — Article Brief Stubs

For each Tier 1 gap, produce a quick `seo-brief-builder` stub:
- Primary keyword
- Search intent
- Recommended H2 structure (3–4 headings minimum)
- Affiliate service to feature
- Suggested author (by topic)

## Output Format

```
GAP ANALYSIS REPORT
Competitor(s): [domain(s)]
Date: [date]
ClearLegalTips articles reviewed: 50

SUMMARY:
Coverage gaps found:     [X]
Depth gaps found:        [X]  
State gaps found:        [X]

TIER 1 — WRITE NOW ([X] topics):
1. "[topic/keyword]" — Est. volume: [X]/mo — Affiliate: [service] — Gap reason: [one line]
2. ...

TIER 2 — NEXT QUARTER ([X] topics):
...

TIER 3 — EVALUATE LATER ([X] topics):
...

ARTICLE BRIEF STUBS (Tier 1):
---
TOPIC: [keyword]
INTENT: [informational/commercial]
STRUCTURE: H2: [list]
AFFILIATE: [service + /recommend/slug]
AUTHOR: [ID — Name]
---
[repeat for each Tier 1 gap]

RECOMMENDED NEXT ACTION:
Use /new-article "[top Tier 1 keyword]" to start writing immediately.
```
