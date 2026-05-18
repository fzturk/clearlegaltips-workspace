---
description: Write a new 3000+ word legal article for ClearLegalTips from a keyword or topic. Runs the full content pipeline: brief → research → write → SEO → image prompt.
---

# New Article Pipeline

Write a complete, publish-ready article for ClearLegalTips on the topic: **$ARGUMENTS**

## Pipeline

### Step 1 — Content Brief
Use the `seo-brief-builder` skill to produce a full content brief:
- Primary keyword and secondary keywords (3–5)
- Target reader intent (informational / navigational / commercial)
- Recommended H2 structure (6–8 sections)
- Word count target (minimum 3,000)
- Competitor articles to beat
- Affiliate services to recommend
- Author assignment (291 Sarah / 292 Marcus / 293 Elena / 294 David — match to topic)

### Step 2 — SERP Research
Use the `serp-analyzer` skill on the primary keyword:
- Top 5 competitor URLs and their H2 structures
- Schema types they use
- Gaps they miss

### Step 3 — Write the Article
Use the `legal-blog-writer` skill to produce the full HTML article.

**Required elements (every article):**
```html
<div class="clt-disclosure"> ... </div>         <!-- top of article -->
<a class="clt-affiliate-btn" href="/recommend/[slug]" rel="nofollow sponsored"> ... </a>
<div class="clt-related-articles"> ... </div>   <!-- 3 internal links -->
<div class="clt-disclaimer"> ... </div>         <!-- bottom of article -->
```

CTA placement: above fold (within first 600 words), after comparison section, at end. Max 3 CTAs.

### Step 4 — SEO Fields
Use the `seo-meta-optimizer` skill to produce:
- `rank_math_title` — primary keyword + brand modifier, max 60 chars
- `rank_math_description` — benefit-forward, max 155 chars
- `rank_math_focus_keyword` — primary keyword
- `rank_math_rich_snippet` — `faqpage` or `howto`

### Step 5 — Schema
Use the `schema-markup-legal` skill to produce:
- FAQPage JSON-LD (minimum 3 Q&A pairs from article FAQ section)
- OR HowTo JSON-LD if it's a how-to guide

### Step 6 — Brand Voice Check
Use the `brand-voice-legal` skill to verify:
- No legal advice language (no "you should", "you must" without qualifier)
- Correct hedging: "generally", "in most states", "typically"
- Tone: clear, professional, empathetic

### Step 7 — Hook Score
Use the `hook-analyzer` skill on the opening 150 words. If score < 18/25, rewrite before final output.

### Step 8 — Featured Image Prompt
Use the `visual-prompt-crafter` skill to produce a ComfyUI prompt for the featured image.
- Target: 1216×640px → PIL resize to 1200×630px
- Model: juggernautXL_ragnarokBy.safetensors
- File naming: `post-{id}-{slug}.jpg`

## Output Format

```
ARTICLE: [title]
PRIMARY KEYWORD: [keyword]
AUTHOR: [ID — Name]
WORD COUNT: ~[X]
NEXT PUBLISH DATE: [next staggered slot — read from latest WP post_date + 1 day]

--- ARTICLE HTML ---
[full article HTML]

--- SEO FIELDS (PHP) ---
update_post_meta($pid, 'rank_math_title', '...');
update_post_meta($pid, 'rank_math_description', '...');
update_post_meta($pid, 'rank_math_focus_keyword', '...');
update_post_meta($pid, 'rank_math_rich_snippet', '...');

--- SCHEMA JSON-LD ---
[full JSON-LD block]

--- FEATURED IMAGE PROMPT ---
[ComfyUI prompt]

--- WORDPRESS PUBLISH SCRIPT ---
[PHP wp_insert_post snippet]
```

## Constraints
- Never assign a post slug that already exists
- Publish date: query the latest `post_date` in WP, stagger one per day from there (initial 50 articles ran 2026-04-01 to 2026-04-25; check WP for the actual next available slot)
- All affiliate links: `/recommend/[slug]` format only
- Featured image: 1200×630px JPG required before publishing
