---
name: schema-markup
description: Adds HowTo, FAQPage, or Article schema markup to WordPress articles. Use for "add schema", "structured data", "rich result" requests.
allowed-tools: Read Bash
effort: medium
---

Add JSON-LD schema markup to ClearLegalTips articles.

## Target: $ARGUMENTS
(Post ID or article type)

---

## Schema Selection by Article Type

| Article Type | Schema | Why |
|---|---|---|
| Template articles (131-150) | HowTo + FAQPage | Has "How to use/fill" steps |
| Cost guides (151-165) | FAQPage + Article | Q&A heavy |
| How-to guides (166-175) | HowTo + FAQPage | Step-by-step process |
| State guides (176-180) | FAQPage + Article | Regional information |

---

## Schema Templates

### HowTo Schema
```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "TITLE",
  "description": "META DESCRIPTION",
  "step": [
    {
      "@type": "HowToStep",
      "name": "STEP 1 TITLE",
      "text": "STEP 1 DESCRIPTION"
    },
    {
      "@type": "HowToStep",
      "name": "STEP 2 TITLE",
      "text": "STEP 2 DESCRIPTION"
    }
  ],
  "estimatedCost": {
    "@type": "MonetaryAmount",
    "currency": "USD",
    "value": "ACTUAL_COST_OR_0"
  }
}
```
Note: For template articles (131-150), `value: "0"` is appropriate (template is free).
For cost guide articles (151-165), enter the actual cost range (e.g. "50-500") or remove this field entirely.

### FAQPage Schema
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "QUESTION 1?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "ANSWER 1"
      }
    },
    {
      "@type": "Question",
      "name": "QUESTION 2?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "ANSWER 2"
      }
    }
  ]
}
```

### Article Schema
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "TITLE",
  "description": "META DESCRIPTION",
  "author": {
    "@type": "Person",
    "name": "AUTHOR NAME",
    "url": "https://clearlegaltips.com/author/SLUG/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "ClearLegalTips",
    "url": "https://clearlegaltips.com",
    "logo": {
      "@type": "ImageObject",
      "url": "https://clearlegaltips.com/wp-content/uploads/clear_legal_tips_logo_for_google.png"
    }
  },
  "datePublished": "DATE",
  "dateModified": "DATE"
}
```

---

## Steps

### 1. Analyze Article Content
If Post ID is given, read via WP-CLI:
```powershell
$WPCLI = "C:\Users\fatih\AppData\Local\studio_app\bin\studio.bat"
$WP_PATH = "C:\Users\fatih\Studio\clearlegaltips"
& $WPCLI wp post get POST_ID --fields=post_title,post_content,post_date --path="$WP_PATH"
```

### 2. Generate Schema JSON
- H2 headings in article → HowTo steps
- Questions in FAQ section → FAQPage mainEntity
- Author info → from CLAUDE.md

### 3. Add to WordPress

Add schema to the beginning of the post's `post_content` as `<script type="application/ld+json">`:

```powershell
# Add via PHP script
$script = @'
<?php
$pid = POST_ID;
$p = get_post($pid);
$schema = '{"@context":"https://schema.org",...}';
$script_tag = '<script type="application/ld+json">' . $schema . '</script>';
if (strpos($p->post_content, 'application/ld+json') === false) {
    $updated = $script_tag . "\n" . $p->post_content;
    wp_update_post(['ID' => $pid, 'post_content' => $updated]);
    clean_post_cache($pid);
    echo "Schema added: $pid\n";
} else {
    echo "Schema already exists: $pid\n";
}
'@
$script | Out-File -Encoding utf8 "$env:TEMP\add_schema.php"
& $WPCLI wp eval-file "$env:TEMP\add_schema.php" --path="$WP_PATH"
```

### 4. Validate
After schema is added, provide the Google Rich Results Test URL:
```
https://search.google.com/test/rich-results?url=https://clearlegaltips.com/SLUG/
```

---

## Bulk Schema Addition

To add schema to all 50 articles by type:
```
Posts 131-150: HowTo + FAQPage
Posts 151-165: FAQPage + Article
Posts 166-175: HowTo + FAQPage
Posts 176-180: FAQPage + Article
```
