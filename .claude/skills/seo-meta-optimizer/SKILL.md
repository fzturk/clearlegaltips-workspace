---
name: seo-meta-optimizer
description: Rewrites Rank Math meta titles and descriptions for ClearLegalTips articles to maximize CTR. Use when asked to "optimize meta", "improve meta description", "fix SEO title", or when running a batch update on post metadata.
allowed-tools: Read Write Bash
effort: medium
---

# SEO Meta Optimizer

## Context

ClearLegalTips uses Rank Math SEO. Meta fields are stored as post meta:
- `rank_math_title` — SEO title (50–60 chars)
- `rank_math_description` — Meta description (140–155 chars)
- `rank_math_focus_keyword` — Primary keyword

Target audience: US adults doing DIY legal tasks. Search intent is always informational → transactional.

## Instructions

1. **Identify the article's primary keyword and search intent**
   - Template articles (IDs 131–150): intent = "get a free [document] template"
   - Cost/calculator articles (IDs 151–165): intent = "how much does X cost"
   - How-to guides (IDs 166–175): intent = "how to [do X] online"
   - State/specialty guides (IDs 176–180): intent = "[state] specific legal info"

2. **Write the SEO title** (50–60 characters)
   - Lead with the primary keyword
   - Add a power word or number: "Free", "Step-by-Step", "2025 Guide", "#1 Way"
   - Include site name only if space allows: `| ClearLegalTips`
   - Example: `Free NDA Template + How to Use It (2025) | ClearLegalTips`

3. **Write the meta description** (140–155 characters)
   - Open with the user's core question answered in 5–8 words
   - Include the primary keyword naturally in the first sentence
   - Add a secondary benefit or differentiator
   - End with a soft CTA: "Get started today.", "See options →", "Download free."
   - No quotation marks, no em-dashes, no ALL CAPS
   - Example: `Download a free NDA template and learn how to fill it out in minutes. Compare top legal services — no lawyer required.`

4. **Validate**
   - Title: 50–60 chars ✓
   - Description: 140–155 chars ✓
   - Primary keyword appears in both ✓
   - No keyword stuffing ✓

## Output Format

For a single article:
```
POST ID: [id]
SEO Title (XX chars): [title]
Meta Description (XX chars): [description]
Focus Keyword: [keyword]
```

For batch updates, output a PHP snippet ready for WP-CLI:
```php
$updates = [
  131 => ['title' => '...', 'desc' => '...', 'kw' => '...'],
  // ...
];
foreach ($updates as $pid => $data) {
  update_post_meta($pid, 'rank_math_title', $data['title']);
  update_post_meta($pid, 'rank_math_description', $data['desc']);
  update_post_meta($pid, 'rank_math_focus_keyword', $data['kw']);
  clean_post_cache($pid);
}
echo "Done.\n";
```

## Examples

**Input:** Post 151 — "How Much Does an LLC Cost?" (cost/calculator article)
**Output:**
```
SEO Title (52 chars): How Much Does an LLC Cost? 2025 State Guide
Meta Description (153 chars): LLC formation costs $50–$500 depending on your state. Compare filing fees, registered agent costs, and the cheapest online services available today.
Focus Keyword: how much does an LLC cost
```
