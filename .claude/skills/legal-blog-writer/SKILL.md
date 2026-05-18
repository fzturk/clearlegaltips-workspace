---
name: legal-blog-writer
description: Writes 3000+ word SEO-optimized legal articles for ClearLegalTips. Use when asked to "write an article", "draft a post", "create content about [legal topic]", or "write a new article for the site".
---

# Legal Blog Writer

## Context

ClearLegalTips publishes DIY legal content for US adults. Articles are informational, not legal advice. Revenue comes from affiliate links to services like LawDepot, ZenBusiness, Northwest Registered Agent, Rocket Lawyer, LegalZoom, Nolo, Incfile.

**Site authors:**
- Sarah Jenkins (ID 291) — family law, estate planning
- Marcus Thorne (ID 292) — business law, contracts
- Elena Rodriguez (ID 293) — real estate, landlord-tenant
- David Miller (ID 294) — small business, LLC formation

## Instructions

### Step 1 — Article Brief

Before writing, confirm:
- **Primary keyword** (from keyword research or user input)
- **Article type**: template | cost/calculator | how-to guide | state guide
- **Target affiliate**: which service to feature (use ThirstyAffiliates slug)
- **Author**: assign based on topic expertise above

### Step 2 — Article Structure

```
H1: [Primary keyword — exact match or close variant]

[FTC Disclosure box — clt-disclosure class]

Introduction (150–200 words)
- Hook: answer the core question in 2 sentences
- Expand: who this is for, what they'll learn
- Soft keyword: primary keyword in first 100 words

H2: What Is [Topic]?
- Definition, plain English
- Why it matters for the reader

H2: [Core section — varies by type]
  For templates: "What to Include in a [Document]"
  For cost: "How Much Does [X] Cost? (State Breakdown)"
  For how-to: "How to [Task] Step by Step"
  For state: "[State]-Specific Rules You Need to Know"

H2: [Comparison or options section]
  "Best Online Services for [Task]" or "DIY vs. Hiring a Lawyer"
  → Place first affiliate CTA button here

H2: Common Mistakes to Avoid
H2: Frequently Asked Questions (3–5 Q&As — schema-ready)
H2: Final Thoughts

[CTA box — clt-cta-box class with affiliate button]
[Internal link box — clt-related-articles class, 3 links]
[Legal disclaimer — clt-disclaimer class]
```

### Step 3 — Writing Rules

- **Tone**: Clear, professional, empathetic. "You" throughout. Never "one should".
- **Reading level**: Grade 8–10. Short paragraphs (3–5 sentences max).
- **Not legal advice**: Never say "you should" without qualifying. Use "in most states", "generally", "typically".
- **Minimum length**: 3,000 words
- **Keyword density**: Primary keyword 1–1.5%. Secondary keywords naturally distributed.
- **No fluff openers**: Never start with "In today's world..." or "Are you wondering..."

### Step 4 — Required Elements (All Articles)

**FTC Disclosure** (top of article):
```html
<div class="clt-disclosure">
<p><strong>Disclosure:</strong> This article contains affiliate links. If you purchase through our links, we may earn a commission at no extra cost to you. We only recommend services we've researched and believe provide value.</p>
</div>
```

**Affiliate CTA button**:
```html
<a href="/recommend/[slug]" class="clt-affiliate-btn" rel="nofollow sponsored">
  Start with [Service Name] →
</a>
```

**Internal link box** (3 related articles from hub-spoke map):
```html
<div class="clt-related-articles">
<h3>Related Articles</h3>
<ul>
  <li><a href="/[slug-1]">[Title 1]</a></li>
  <li><a href="/[slug-2]">[Title 2]</a></li>
  <li><a href="/[slug-3]">[Title 3]</a></li>
</ul>
</div>
```

**Legal disclaimer** (bottom of article):
```html
<div class="clt-disclaimer">
<p><strong>Legal Disclaimer:</strong> The information provided on ClearLegalTips is for general informational purposes only and does not constitute legal advice. Laws vary by state and individual circumstances differ. Consult a licensed attorney for advice specific to your situation.</p>
</div>
```

### Step 5 — Rank Math Fields

After the article, provide:
```
Focus Keyword: [primary keyword]
SEO Title: [50-60 chars]
Meta Description: [140-155 chars]
Suggested Author ID: [291|292|293|294]
Suggested Publish Date: [next available date after 2026-04-25]
```

## Output Format

Full article in HTML (WordPress block editor compatible), followed by Rank Math fields block.

## Examples

**Input:** "Write an article about LLC operating agreements, target ZenBusiness"
**Output:** 3,200-word article with H1 "LLC Operating Agreement: What It Is and How to Create One", assigned to David Miller (ID 294), featuring ZenBusiness CTA at `/recommend/zenbusiness`.
