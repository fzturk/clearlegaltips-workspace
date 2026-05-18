---
name: keyword-research
description: Performs keyword research for ClearLegalTips. Use for "find keywords", "what topic should we write about", "SEO opportunity" requests.
allowed-tools: WebSearch WebFetch Read
effort: high
---

Perform legal DIY keyword research for ClearLegalTips.com.

## Research Topic: $ARGUMENTS

## Steps

### 1. Seed Keyword Expansion
Research these variations:
- "$ARGUMENTS + free"
- "$ARGUMENTS + online"
- "$ARGUMENTS + template"
- "$ARGUMENTS + cost"
- "$ARGUMENTS + how to"
- "$ARGUMENTS + form"
- "how to [do $ARGUMENTS] yourself"
- "[state] + $ARGUMENTS" (for TX, CA, FL, NY, IL)

### 2. Ahrefs MCP Usage
If Ahrefs MCP is active (`mcp__claude_ai_Ahrefs__keywords-explorer-overview`) pull:
- Search volume (US)
- Keyword difficulty (KD)
- Traffic potential
- SERP features (featured snippet, people also ask)

### 3. Competitor Content Analysis
Review top 3-5 ranking pages:
- Title structure
- Content length
- Topics covered / not covered
- Which affiliate services they recommend
- Featured snippet present?

### 4. Intent Classification
Determine intent for each keyword:
- **Informational** ("what is", "how does") → template/guide article
- **Transactional** ("best", "review", "vs") → affiliate comparison
- **Navigational** (brand searches) → skip
- **Commercial Investigation** ("cost", "price", "cheap") → calculator/cost guide

### 5. Overlap Check with Existing Content
Already written topics at ClearLegalTips (Post IDs 131-180):
- NDA, LLC Operating Agreement, Commercial Lease, Residential Lease
- Bill of Sale, Promissory Note, Last Will, Living Trust, POA
- Medical POA, Prenup, Eviction Notice, Sublease, Service Agreement
- Partnership, Child Custody, Consulting Agreement, Quitclaim Deed
- LLC formation cost, S-Corp vs LLC, Registered Agent, DBA, EIN
- Annual reports, Business license, Foreign qualification, Trademark
- Estate tax, Probate cost, Living trust vs will, Divorce cost
- Child support, Small claims, LLC online, EIN online, RA online
- Uncontested divorce, CompleteCasez, Name change, Living trust online
- Trademark online, DBA online, Legal separation, Online divorce (state)
- Dissolve LLC, Copyright, Small claims evictions, Landlord accounting

### 6. Priority Matrix

| Keyword | Volume | KD | Intent | Content Type | Priority |
|---|---|---|---|---|---|
| [keyword 1] | [vol] | [kd] | [intent] | [type] | [P1/P2/P3] |

### 7. Result Report

**Top 10 Highest-Potential Keywords:**
1. Keyword — Volume: X, KD: Y, Intent: Z, Recommendation: [content type]
...

**Quick Win Opportunities (KD < 20, Volume > 500):**
- ...

**Long-Term Targets (KD 30-50, Volume > 2000):**
- ...

**Skip These (reason):**
- ...
