---
name: affiliate-cta-optimizer
description: Analyzes and optimizes affiliate CTA placement, copy, and conversion signals on ClearLegalTips article pages. Use when asked to "improve CTAs", "optimize affiliate buttons", "page CRO", "improve conversions", "why aren't people clicking", or "analyze this article for conversion".
allowed-tools: Read Write Bash
effort: medium
---

# Affiliate CTA Optimizer (Page CRO)

## Context

ClearLegalTips earns revenue through affiliate links. The primary conversion action is a reader clicking a `clt-affiliate-btn` and purchasing a service (LawDepot, ZenBusiness, Northwest Registered Agent, etc.).

ThirstyAffiliates link format: `/recommend/[slug]`  
CTA class: `clt-affiliate-btn` (Crimson #C0392B button)

## Instructions — 7-Dimension Analysis

Analyze the article across these 7 dimensions:

### 1. Value Proposition Clarity
- Does the article headline (H1) immediately tell the reader what they'll get?
- Is the article's core benefit stated in the first 100 words?
- **Red flags:** Vague H1s ("Understanding NDAs"), buried payoff, no clear outcome promised

### 2. Headline Effectiveness
- Does the H1 match the search query intent?
- Does it include a number, "free", "step-by-step", or year for CTR?
- **Fix:** Rewrite H1 to front-load the keyword + benefit

### 3. CTA Placement & Hierarchy
- Is there at least one CTA above the fold (within first 600 words)?
- Is there a CTA after the comparison/options section?
- Is there a final CTA before the disclaimer?
- **Ideal placement:** Introduction area → After comparison section → End of article
- **Red flags:** Only one CTA at the very end; CTA buried in middle of a paragraph

### 4. CTA Copy Quality
Evaluate the button text against this rubric:

| Score | Example | Reason |
|---|---|---|
| ❌ Weak | "Click Here" | No value |
| ❌ Weak | "Learn More" | No action |
| ✅ Good | "Start with ZenBusiness →" | Brand + action |
| ✅ Good | "Get Your Free NDA Template →" | Outcome + free |
| ✅ Best | "Form Your LLC for $49 →" | Price anchor + action |

### 5. Trust Signals
Check for:
- [ ] Author byline visible (name + expertise note)
- [ ] Article publish/update date visible
- [ ] FTC disclosure box present at top (`clt-disclosure`)
- [ ] Legal disclaimer present at bottom (`clt-disclaimer`)
- [ ] At least one external source linked (gov site, statutes)
- **Missing trust signals reduce conversion** — readers won't click affiliate links if they don't trust the page

### 6. Objection Handling
Common reader objections on legal affiliate pages:
- "Is this service legit?" → Add "Trusted by X users" or BBB rating note
- "Is it really free/cheap?" → State price clearly in CTA or nearby text
- "Do I actually need this?" → Address the "DIY without any service" option honestly, then show why the service is worth it
- "Is this legal advice?" → FTC + disclaimer already handles this, but don't be preachy

### 7. Friction Points
- Page load speed: images optimized? (featured image = 1200×630 JPG)
- Mobile CTA: is the button large enough on mobile? (min 44×44px touch target)
- Too many ads/popups competing with affiliate CTA?
- CTA color contrast: Crimson #C0392B on white — passes WCAG AA?

## Output Format

```
CTA AUDIT: [Post ID] — [Title]
Overall Score: [X/7 dimensions passing]

✅ PASSING:
- [dimension]: [brief note]

⚠️ ISSUES:
- [dimension]: [what's wrong] → [recommended fix]

RECOMMENDED CHANGES:
1. [Change 1 — most impactful]
2. [Change 2]
...

NEW CTA COPY SUGGESTIONS:
Button 1 (above fold): [text]
Button 2 (after comparison): [text]
Button 3 (end of article): [text]

PHP UPDATE SNIPPET (if content change needed):
[code]
```

## CTA Copy Bank (Affiliate-Specific)

| Affiliate | Strong CTA Options |
|---|---|
| LawDepot | "Get Your Free [Document] Template →" / "Create Your [Document] Now →" |
| ZenBusiness | "Form Your LLC for $49 →" / "Start Your LLC with ZenBusiness →" |
| Northwest | "Get a Free Registered Agent Year →" / "Form LLC + Free Registered Agent →" |
| Rocket Lawyer | "Try Rocket Lawyer Free for 7 Days →" / "Get Legal Help from $39.99/mo →" |
| LegalZoom | "Start Your LLC with LegalZoom →" / "File Your Business Documents →" |
| Incfile | "Form Your LLC Free (Pay State Fee Only) →" |
