---
name: ab-test-setup
description: Designs A/B tests for ClearLegalTips CTAs, headlines, and conversion elements. Use when asked to "set up an A/B test", "test this CTA", "what should we test", "A/B test plan", or "which version converts better".
---

# A/B Test Setup

## Context

ClearLegalTips is an affiliate blog with WordPress + Kadence theme. Native A/B testing requires a plugin (Nelio A/B Testing, Split Hero, or Google Optimize alternative). Without a dedicated tool, A/B tests run as sequential tests (version A for 2 weeks → version B for 2 weeks) or via manual URL variants.

**What's worth testing:** Only elements with high impact on affiliate revenue — CTA buttons, article headlines, comparison section structure, lead magnet copy.

**Minimum viable sample:** At least 200 unique visitors per variant before drawing conclusions.

## Test Priority Matrix

| Element | Impact | Ease | Priority |
|---|---|---|---|
| CTA button text | High | Easy | 🔴 Test first |
| CTA button color (Crimson vs Navy) | Medium | Easy | 🟡 |
| Article H1 (headline) | High | Medium | 🔴 Test second |
| CTA placement (1 vs 2 vs 3 CTAs) | High | Medium | 🔴 |
| Form headline on lead magnet | High | Easy | 🔴 |
| Article intro (hook type) | Medium | Hard | 🟡 |
| Popup timing (exit vs scroll) | Medium | Medium | 🟡 |
| Comparison table position | Medium | Medium | 🟡 |

## A/B Test Design Framework

### Step 1 — Hypothesis
```
"Changing [element] from [A] to [B] will [increase/decrease] [metric] 
because [reason based on CRO principles]."
```

Example:
"Changing the CTA button from 'Start with ZenBusiness →' to 'Form My LLC for $49 →' 
will increase affiliate clicks because it includes a price anchor and first-person framing."

### Step 2 — Define Success Metric
| Test Type | Primary Metric |
|---|---|
| CTA button | Click-through rate on affiliate link |
| Headline | Organic CTR (Google Search Console) |
| Lead magnet form | Email conversion rate |
| Popup | Email capture rate |
| Article intro | Time on page / bounce rate |

### Step 3 — Test Duration
- Minimum: 2 weeks per variant
- Minimum sample: 200 visitors per variant
- Statistical significance target: 95% (use a calculator: abtestguide.com)

### Step 4 — Implementation Options

**Option A — Sequential test (no plugin required):**
- Week 1–2: Version A, record results manually
- Week 3–4: Version B, record results manually
- Risk: seasonal variation, traffic differences between weeks

**Option B — WordPress A/B plugin:**
- Nelio A/B Testing (paid) — full split testing
- Split Hero (paid) — simpler UI
- Google Optimize was deprecated — avoid

**Option C — CTA variant via PHP:**
For CTA button text tests, use a random 50/50 split via PHP:
```php
$cta_variants = [
  'Start with ZenBusiness →',
  'Form My LLC for $49 →'
];
$variant = $cta_variants[rand(0,1)];
// Track which variant via custom event in analytics
```

## Instructions

1. **Identify what to test** (use priority matrix above)
2. **Write the hypothesis**
3. **Define success metric and baseline** (current rate)
4. **Create both variants** (A = control, B = challenger)
5. **Set duration and sample requirements**
6. **Document tracking method**

## Output Format

```
A/B TEST PLAN: [element being tested]
Article/Page: [Post ID or page]

HYPOTHESIS:
"Changing [A] to [B] will [impact] [metric] because [reason]."

VARIANT A (Control):
[exact copy/element as it exists now]

VARIANT B (Challenger):
[exact copy/element being tested]

SUCCESS METRIC: [metric name] — current baseline: [X%]
TEST DURATION: [X] weeks | Minimum visitors needed: [X] per variant
IMPLEMENTATION: Sequential | Plugin | PHP random

TRACKING NOTES:
[How to measure — Analytics event, affiliate link click count, GSC CTR]

DECISION RULE:
"If Variant B shows [X]% improvement with [X] visitors, implement permanently."
```
