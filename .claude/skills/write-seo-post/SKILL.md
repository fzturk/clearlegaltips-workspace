---
name: write-seo-post
description: Writes an SEO-optimized WordPress blog article for ClearLegalTips. Use when the user asks to "write an article", "create content", "write a post", or requests content about a legal topic.
allowed-tools: Read Write WebSearch WebFetch
effort: high
---

Write a 3000+ word, Rank Math-compliant, affiliate-linked SEO article for ClearLegalTips.com.

## Target: $ARGUMENTS

## Writing Steps

### 1. Topic Research
- Research the topic on the web: "$ARGUMENTS + explained site:gov OR site:irs.gov OR site:law.cornell.edu"
- Find 3-5 authoritative sources (gov, law firm, established publication)
- Analyze competitors' angles
- Collect FAQ questions: search for "people also ask"

### 2. Create Outline
```
H1: [Main title — must contain focus keyword]
H2: What Is [Topic]? (definition + basic info)
H2: How [Topic] Works (mechanism, process)
H2: [Topic] Requirements / Steps (list format)
H2: Common Mistakes to Avoid
H2: Cost Breakdown (if applicable)
H2: State-Specific Considerations (US-focused)
H2: Frequently Asked Questions
H2: Bottom Line
```

### 3. Write Content
- Minimum **3000 words**
- Focus keyword must appear in first 100 words
- Tone: Clear, professional — information not legal advice
- Minimum 200 words under each H2
- Use numbered/bulleted lists for scannability
- Cite sources for statistics and numbers

### 4. Required Elements (Every Article)

**FTC Disclosure** (top of article, before the first `/go/` link — exact live wording):
```html
<div class="clt-disclosure"><strong>Affiliate Disclosure:</strong> ClearLegalTips is reader-supported. When you buy through links on this page we may earn a commission at no extra cost to you. This never affects which services we recommend. <a href="/affiliate-disclosure/">Learn more</a>.</div>
```

**CTA Box** (for the relevant affiliate service):
```html
<div class="clt-cta-box">
<p class="clt-cta-text">[Brief description — why this service fits this reader's situation]</p>
<p><a href="/go/[slug]" class="clt-affiliate-btn" rel="nofollow sponsored">[Action] &rarr;</a></p>
</div>
```

**Internal Link Box** (3 related articles per hub-spoke map):
```html
<div class="clt-related-articles">
<h3>Related Articles</h3>
<ul>
<li><a href="/[slug-1]">[Article 1 Title]</a></li>
<li><a href="/[slug-2]">[Article 2 Title]</a></li>
<li><a href="/[slug-3]">[Article 3 Title]</a></li>
</ul>
</div>
```

**Legal Disclaimer** (bottom of article):
```html
<div class="clt-disclaimer"><strong>Legal Disclaimer:</strong> This article is general information, not legal advice. ClearLegalTips is not a law firm and does not provide legal representation. Laws vary by state and change over time. For guidance on your specific situation, consult a licensed attorney in your jurisdiction.</div>
```

**Sources block** (before the disclaimer; every number in the article must trace to one of these):
```html
<div class="clt-sources">
<h3>Sources &amp; References</h3>
<ul>
<li><a href="[official URL]" target="_blank" rel="noopener nofollow">[domain]</a></li>
</ul>
<p><em>Fact-checked: [Month Year]</em></p>
</div>
```

### 5. Rank Math SEO Fields (state at end of article)

```
Focus Keyword: [primary keyword]
Meta Title: [60 chars max — keyword first]
Meta Description: [150-155 chars — keyword + value prop + CTA]
```

### 6. Featured Image Recommendation
```
File name: post-[id]-[slug].jpg
Dimensions: 1200×630px
Alt text: [Descriptive text containing the focus keyword]
```

## Affiliate CTA Slug Guide

Always link through `/go/{slug}` (302 redirects managed on the live site). Never write a direct affiliate URL, and never use the retired `/recommend/` paths. The full live list is in CLAUDE.md.

| Topic | Slug |
|---|---|
| Legal documents (general) | /go/lawdepot |
| Business documents / operating agreement | /go/lawdepot-business, /go/lawdepot-llc-operating-agreement |
| Real estate / landlord documents | /go/lawdepot-realestate, /go/lawdepot-eviction-notice, /go/lawdepot-residential-lease |
| Family / divorce documents | /go/lawdepot-family |
| Estate (will, trust, affidavit) | /go/lawdepot-estate, /go/lawdepot-last-will, /go/lawdepot-living-trust, /go/lawdepot-affidavit-form |
| Demand letters / collections | /go/lawdepot-payment-demand-letter |
| LLC formation (incl. non-residents) | /go/doola |
| Landlord software | /go/doorloop |
| Privacy policy / terms | /go/termly |
| Freelancer taxes | /go/keeper-tax |

New programs (Trust & Will, OnlineDivorce, CompleteCase, NEXT Insurance, Gusto) get a `/go/` slug only after approval and after the redirect exists on the live site. Until then use the LawDepot fallback.

## Categories (live IDs)

| ID | Category |
|---|---|
| 1 | Legal Templates |
| 6 | Business Calculators |
| 7 | Estate & Family |
| 8 | Filing Guides |
| 9 | Reviews & Comparisons |

Use existing tags only (3–4 per post). Author is always the single ClearLegalTips user. Publish with the real date — never backdate. No fictional experts and no "attorney-reviewed" claims.

## Output Format

Present the article in this format:

1. **ARTICLE CONTENT** (full HTML or Markdown)
2. **SEO FIELDS** (Focus keyword, meta title, meta description)
3. **NOTES** (internal linking recommendations, featured image suggestion)
