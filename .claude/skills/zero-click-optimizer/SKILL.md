---
name: zero-click-optimizer
description: Optimizes ClearLegalTips content to win featured snippets and answer boxes (position zero) in Google. Use when asked to "featured snippet", "position zero", "answer box", "zero-click", "snippet optimization", or "how do we get the snippet for X".
allowed-tools: Read Write WebSearch
effort: medium
---

# Zero-Click Optimizer

## Context

Featured snippets appear above organic results for 12–23% of legal queries. For ClearLegalTips, winning a snippet means:
- Visibility even if someone doesn't click (brand awareness)
- Higher CTR when snippet includes site name
- Trust signal for readers who do click through

Legal queries with high snippet potential:
- "what is [legal term]?" → paragraph snippet
- "how to [legal task]?" → numbered list snippet
- "[state] LLC requirements" → table or list snippet
- "how much does [legal service] cost?" → paragraph or table snippet

## Snippet Types & Optimization Tactics

### 1. Paragraph Snippet (most common for legal "what is" queries)

**Trigger:** Definition questions, "what is", "what does X mean"

**Format:** 40–60 words, direct answer, no fluff opener

**Template:**
```
[Term] is [definition in plain English]. [One sentence expanding on why it matters or when it applies]. [One sentence on the key requirement or caveat].
```

**Example:**
```
An LLC operating agreement is a legal document that outlines the ownership structure, management rules, and operational procedures of a limited liability company. Most states don't legally require one, but without it, state default rules govern your business — which may not match your intentions.
```

**Where to place it:** Immediately after the H2 heading that matches the snippet query. The paragraph must stand alone without the heading.

### 2. Numbered List Snippet ("how to" queries)

**Trigger:** "How to form...", "steps to...", "how do I..."

**Format:** 5–8 steps, each ≤12 words, action verbs

**Template:**
```html
<ol>
  <li>Choose your state of formation</li>
  <li>Select a unique business name</li>
  <li>Appoint a registered agent</li>
  <li>File Articles of Organization</li>
  <li>Create an operating agreement</li>
  <li>Get an EIN from the IRS</li>
  <li>Open a business bank account</li>
</ol>
```

**Placement:** Directly under H1 or under the first H2 that covers the process.

### 3. Table Snippet (cost/comparison queries)

**Trigger:** "cost by state", "fees comparison", "[A] vs [B]"

**Format:** 2–4 columns, ≤8 rows, clear headers

**Example:**
```html
<table>
  <tr><th>State</th><th>LLC Filing Fee</th><th>Annual Report Fee</th></tr>
  <tr><td>Delaware</td><td>$90</td><td>$300</td></tr>
  <tr><td>Wyoming</td><td>$100</td><td>$52</td></tr>
  <tr><td>Texas</td><td>$300</td><td>$0</td></tr>
</table>
```

**Placement:** Early in the article (within first 800 words).

## Instructions

1. **Identify the target snippet query** — what exact question is the reader asking?
2. **Check current SERP** — who holds the snippet? What format?
3. **Select snippet type** — paragraph / list / table
4. **Write the snippet-optimized block** — self-contained, direct, correct word count
5. **Place it correctly** — immediately under the matching heading, before any further explanation
6. **Add schema** — FAQPage or HowTo schema reinforces the snippet signal

## Snippet Audit for Existing Articles

For each of the 50 existing articles, check:
- [ ] Is there a direct 40–60 word definition/answer block under the first H2?
- [ ] For process articles: is there a numbered list of steps ≤12 words each?
- [ ] For cost articles: is there a table with state/price data?
- [ ] Does the FAQ section have direct, concise answers (not long paragraphs)?

## Output Format

```
SNIPPET OPTIMIZATION: Post [ID] — [Title]
Target Query: "[query]"
Snippet Type: Paragraph | List | Table
Current Snippet Holder: [domain] / None

OPTIMIZED SNIPPET BLOCK (ready to insert):
[HTML or markdown block]

Placement: Under H2 "[section name]", line [approx position]

Supporting Schema (add to FAQPage):
Q: [question]
A: [40-60 word answer]
```
