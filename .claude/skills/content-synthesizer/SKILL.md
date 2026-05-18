---
name: content-synthesizer
description: Synthesizes research, notes, and raw inputs into structured ClearLegalTips article outlines and drafts. Use when asked to "synthesize this research", "turn these notes into an article", "I have research — help me write this", or when multiple source materials need combining into a single article.
---

# Content Synthesizer

## Context

Content Synthesizer sits between research and writing. Input: raw research (search results, competitor articles, notes, data), Output: structured article ready for legal-blog-writer or a direct draft. This is the Deep Research Agent adapted for affiliate blog content — not sales intelligence, but content intelligence.

The synthesizer extracts signal from noise: what facts are confirmed, what's contested, what's missing, and how to structure it for maximum SEO and affiliate value.

## Input Types It Handles

- Web research notes (pasted text from multiple sources)
- Competitor article summaries
- Official government source data (state filing fees, requirements)
- Affiliate service feature lists
- Reader FAQ / forum questions (Reddit, Avvo)
- Existing ClearLegalTips article drafts needing improvement

## Synthesis Process

### Step 1 — Source Evaluation
For each input source:
- Authority: .gov / established legal site / random blog
- Recency: year of publication / last updated
- Accuracy: cross-reference key facts across 2+ sources
- Relevance: does it serve the target reader's actual question?

Flag anything as [CONFIRMED], [SINGLE SOURCE], or [VERIFY]:
- [CONFIRMED] — 2+ authoritative sources agree
- [SINGLE SOURCE] — only found once, include with caveat
- [VERIFY] — contradictory or unclear, needs state-specific check

### Step 2 — Key Facts Extraction

Extract and organize:
```
CORE FACTS:
- [fact] [CONFIRMED/SINGLE SOURCE/VERIFY] — Source: [domain]

STATISTICS / NUMBERS:
- [stat] — Source: [domain], Year: [year]

STATE-SPECIFIC DATA:
- [state]: [specific rule/fee/requirement]

AFFILIATE CONTEXT:
- [service] offers: [what's relevant to this topic]
- Price: $[X] — as of [date]
- Best for: [use case]
```

### Step 3 — Reader Question Mapping

From research, identify the 5–8 questions the reader most needs answered:
1. [Most important — usually the search query itself]
2. [Second — biggest fear or concern]
3. [Third — cost or effort question]
4. [Fourth — "do I really need this?" question]
5. [Fifth — state-specific variation question]

Each question becomes an H2 in the article.

### Step 4 — Article Structure Generation

Map extracted facts to the article structure:
```
H1: [Primary keyword]
H2: [Reader question 1] — supported by: [facts]
H2: [Reader question 2] — supported by: [facts]
H2: [Comparison / options section] — using: [affiliate data]
H2: [State-specific section if relevant]
H2: FAQ — using: [questions 3-8 from above]
```

### Step 5 — Gaps Identification

After synthesis, flag what's still missing:
- Data that needs current verification (fees, prices)
- State-specific rules not in research
- Affiliate pricing that may be outdated

## Output Format

```
CONTENT SYNTHESIS REPORT
Topic: [article topic]
Primary Keyword: [keyword]
Sources Processed: [X]

CONFIRMED KEY FACTS:
- [fact] [CONFIRMED] — [source]
- [fact] [SINGLE SOURCE] — [source] — include with caveat

STATISTICS:
- [stat] — [source], [year]

AFFILIATE DATA:
- [service]: $[X], best for [use case], slug: [slug]

READER QUESTIONS TO ANSWER (H2 map):
1. [question] → [answer summary, 1-2 sentences]
2. ...

RECOMMENDED ARTICLE STRUCTURE:
[H1 + H2 outline with brief notes on each section]

GAPS / VERIFY BEFORE PUBLISHING:
- [item that needs verification]
- [item that needs verification]

READY FOR: legal-blog-writer skill
Estimated article length: [X] words
```
