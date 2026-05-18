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

**FTC Disclosure** (top of article):
```html
<div class="clt-disclosure">
<strong>Disclosure:</strong> This article contains affiliate links. If you purchase through our links, we may earn a commission at no extra cost to you. We only recommend services we've researched and believe provide value.
</div>
```

**CTA Box** (for the relevant affiliate service):
```html
<div class="clt-cta-box">
<h3>Ready to Get Started?</h3>
<p>[Brief description — why this service is the best option]</p>
<a href="/recommend/[slug]" class="clt-affiliate-btn" rel="nofollow sponsored">
  Get Started with [Service Name] →
</a>
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
<div class="clt-disclaimer">
<strong>Legal Disclaimer:</strong> The information provided in this article is for general informational purposes only and does not constitute legal advice. For advice specific to your situation, consult a licensed attorney in your jurisdiction.
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

| Topic | Slug |
|---|---|
| LLC formation | /recommend/zenbusiness |
| Registered agent | /recommend/northwest-ra |
| Legal documents | /recommend/lawdepot |
| Online divorce | /recommend/completecase |
| Living trust | /recommend/trust-and-will |
| Trademark | /recommend/legalzoom |
| EIN / Business formation | /recommend/incfile |

## Output Format

Present the article in this format:

1. **ARTICLE CONTENT** (full HTML or Markdown)
2. **SEO FIELDS** (Focus keyword, meta title, meta description)
3. **NOTES** (internal linking recommendations, featured image suggestion)
