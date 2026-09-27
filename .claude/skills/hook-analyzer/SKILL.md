---
name: hook-analyzer
description: Analyzes and rewrites the opening 150 words of ClearLegalTips articles to reduce bounce rate and increase time-on-page. Use when asked to "improve the intro", "fix the hook", "rewrite the opening", "reduce bounce rate", or "make this more engaging".
allowed-tools: Read Write
effort: low
---

# Hook Analyzer

## Context

The opening 150 words of a legal article determine whether a reader stays or bounces. Legal content is inherently dry — the hook must immediately signal: "This page answers your exact question AND it won't waste your time."

ClearLegalTips reader psychology: arrived from Google with a specific question, skeptical of legal jargon, time-constrained, wants practical action steps — not theory.

## The 5 Hook Archetypes

### 1. Answer-First Hook (Best for informational queries)
Lead with the direct answer, then expand.
```
An LLC operating agreement is a legal document that outlines how your LLC is owned, managed, and operated. Most states don't require it — but without one, state default rules govern your business, which may not be what you want.

In this guide, you'll learn exactly what to include, see a free template, and find out the fastest way to create one online in under 30 minutes.
```

### 2. Problem-Agitation Hook (Best for cost/decision articles)
Name the reader's fear, then promise relief.
```
Filing LLC paperwork yourself sounds simple — until you realize a single mistake can delay your formation by weeks and cost you hundreds in refiling fees.

Here's what to watch out for, and how to get it done right the first time.
```

### 3. Number Hook (Best for how-to guides)
Lead with a specific, credible number.
```
Forming an LLC in California takes 3–5 business days online and costs $70 in state filing fees. That's it.

What most guides don't tell you: the $70 is just the start. Here's the full cost breakdown — and the cheapest legal way to do it.
```

### 4. Contrast Hook (Best for comparison articles)
Set up a contrast that creates curiosity.
```
ZenBusiness costs $49. Northwest Registered Agent charges $225. Both form your LLC correctly.

So why does anyone pay the premium? And is it ever worth it? We break down exactly what you get — and what you don't — at every price point.
```

### 5. Story Hook (Use sparingly — best for state-specific/personal articles)
Open with a brief, relatable scenario.
```
A landlord in Texas recently learned that the lease agreement she'd been using for 10 years didn't include a required disclosure. The tenant sued. She won — but only after spending $3,000 in legal fees to prove it.

One paragraph in a properly written lease would have prevented the entire situation.
```

## Analysis Criteria

Rate the existing hook on:
1. **Clarity** — Does it answer the search query within the first 2 sentences? (1–5)
2. **Specificity** — Does it include a number, state, price, or timeframe? (1–5)
3. **Reader relevance** — Does it acknowledge the reader's situation/concern? (1–5)
4. **Momentum** — Does it make you want to read the next sentence? (1–5)
5. **Jargon-free** — No unexplained legal terms in the first paragraph? (1–5)

Score below 15/25 = rewrite recommended.

## Instructions

1. Read the article's H1 and first 150 words.
2. Identify the search intent (informational / cost / how-to / comparison).
3. Score the hook on the 5 criteria above.
4. Identify the single biggest weakness.
5. Rewrite the hook using the most appropriate archetype.

## Output Format

```
HOOK ANALYSIS: [Post ID] — [Title]

CURRENT HOOK:
"[first 150 words quoted]"

SCORES:
Clarity: [X/5] — [note]
Specificity: [X/5] — [note]
Reader relevance: [X/5] — [note]
Momentum: [X/5] — [note]
Jargon-free: [X/5] — [note]
TOTAL: [X/25]

VERDICT: [Pass (≥20) | Improve (15–19) | Rewrite (<15)]

REWRITTEN HOOK:
[new 150-word intro]

ARCHETYPE USED: [name]
KEY CHANGE: [one sentence explaining the main improvement]
```
