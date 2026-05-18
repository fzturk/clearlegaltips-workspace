---
name: schema-markup-legal
description: Adds FAQ and HowTo structured data (JSON-LD) to ClearLegalTips articles for featured snippets. Use when asked to "add schema", "add structured data", "FAQ schema", "rich snippet", or for any article that answers questions or explains a process.
---

# Schema Markup — Legal Content

## Context

ClearLegalTips uses Rank Math SEO. Schema is injected via Rank Math's `rank_math_rich_snippet_*` post meta fields, or directly in article content as a JSON-LD `<script>` block. Target: FAQ and HowTo rich results in Google Search for legal DIY queries.

Rank Math meta fields for FAQ schema:
- `rank_math_rich_snippet` → `"faqpage"` or `"howto"`
- FAQ questions stored as serialized data in `rank_math_faq_questions`

## Instructions

### Step 1 — Identify Schema Type

| Article Type | Schema Type | Example |
|---|---|---|
| Template articles (131–150) | FAQPage | "What is an NDA?" "Is an NDA legally binding?" |
| Cost/calculator (151–165) | FAQPage | "How much does an LLC cost in Texas?" |
| How-to guides (166–175) | HowTo | "How to form an LLC online in 5 steps" |
| State/specialty (176–180) | FAQPage + HowTo | Both if article covers process AND questions |

### Step 2 — Write FAQPage Schema

Rules:
- Minimum 3 questions, maximum 8
- Each answer: 40–300 words (Google truncates longer answers)
- Questions must match actual search queries (use keyword research)
- Answers must be self-contained (readable without the full article)
- No promotional language in answers ("Click here", "Buy now")

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is a non-disclosure agreement (NDA)?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A non-disclosure agreement (NDA) is a legally binding contract that prevents one or more parties from sharing confidential information with third parties. NDAs are commonly used when sharing trade secrets, business plans, or proprietary data with employees, contractors, or potential business partners."
      }
    }
  ]
}
```

### Step 3 — Write HowTo Schema

Rules:
- `name`: the task, e.g. "How to Form an LLC Online"
- `totalTime`: ISO 8601 duration, e.g. `"PT30M"` (30 minutes)
- Each step: 1–2 sentences, action-oriented
- `image` on each step: optional but boosts rich results

```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to Form an LLC Online",
  "totalTime": "PT30M",
  "step": [
    {
      "@type": "HowToStep",
      "name": "Choose your state",
      "text": "Select the state where you want to register your LLC. Most small businesses register in their home state."
    },
    {
      "@type": "HowToStep",
      "name": "Choose a registered agent",
      "text": "Designate a registered agent — a person or service that receives legal documents on behalf of your LLC."
    }
  ]
}
```

### Step 4 — Output for Implementation

Output schema as:
1. A JSON-LD `<script>` block ready to paste into the WordPress block editor (Custom HTML block, placed at end of article)
2. A WP-CLI PHP snippet to set Rank Math fields programmatically

## Output Format

```
POST ID: [id]
SCHEMA TYPE: FAQPage | HowTo | Both

--- JSON-LD (paste into Custom HTML block) ---
<script type="application/ld+json">
{ ... }
</script>

--- PHP (WP-CLI) ---
update_post_meta([id], 'rank_math_rich_snippet', '[faqpage|howto]');
```

## Examples

**Input:** Post 131 — NDA template article  
**Output:** FAQPage schema with 5 questions: "What is an NDA?", "When do you need an NDA?", "Is an NDA legally binding?", "Can I write my own NDA?", "What happens if someone violates an NDA?"
