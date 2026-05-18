---
name: seo-audit
description: Audits ClearLegalTips site for SEO issues. Use for "SEO check", "site audit", "which articles are missing", "performance check" requests.
allowed-tools: Read WebFetch Bash
effort: high
---

Perform a comprehensive SEO audit for ClearLegalTips.com.

## Audit Scope: $ARGUMENTS (leave blank for full site)

## Audit Steps

### 1. Rank Math Missing Fields Check (WP-CLI)

```powershell
# Detect Rank Math missing fields via WP-CLI
C:\Users\fatih\AppData\Local\studio_app\bin\studio.bat wp eval '
$posts = get_posts(["post_type"=>"post","posts_per_page"=>-1,"post_status"=>"publish"]);
foreach($posts as $p) {
    $kw = get_post_meta($p->ID, "rank_math_focus_keyword", true);
    $desc = get_post_meta($p->ID, "rank_math_description", true);
    $img = get_post_thumbnail_id($p->ID);
    $issues = [];
    if(!$kw) $issues[] = "NO_KEYWORD";
    if(!$desc) $issues[] = "NO_META_DESC";
    if(!$img) $issues[] = "NO_FEATURED_IMG";
    if($issues) echo $p->ID . " | " . $p->post_title . " | " . implode(", ",$issues) . "\n";
}' --path="C:\Users\fatih\Studio\clearlegaltips"
```

### 2. Word Count Check

```powershell
C:\Users\fatih\AppData\Local\studio_app\bin\studio.bat wp eval '
$posts = get_posts(["post_type"=>"post","posts_per_page"=>-1,"post_status"=>"publish"]);
foreach($posts as $p) {
    $wc = str_word_count(strip_tags($p->post_content));
    if($wc < 3000) echo $p->ID . " | " . $p->post_title . " | " . $wc . " words\n";
}' --path="C:\Users\fatih\Studio\clearlegaltips"
```

### 3. ThirstyAffiliates Placeholder Link Check

```powershell
C:\Users\fatih\AppData\Local\studio_app\bin\studio.bat wp eval '
$links = get_posts(["post_type"=>"thirstylink","posts_per_page"=>-1,"post_status"=>"publish"]);
foreach($links as $l) {
    $info = get_post_meta($l->ID, "_ta_link_info", true);
    $dest = is_array($info) ? ($info["destination"] ?? "") : (string)$info;
    if(empty($dest) || $dest === "#" || $dest === "") {
        echo $l->ID . " | " . $l->post_title . " | PLACEHOLDER\n";
    }
}' --path="C:\Users\fatih\Studio\clearlegaltips"
```

### 4. PageSpeed / Core Web Vitals (if PageSpeed MCP active)

Check these URLs:
- Homepage: http://clearlegaltips.com/
- Top 3 most-visited articles
- Mobile + Desktop scores

Targets:
- LCP < 2.5s
- CLS < 0.1
- INP < 200ms
- PSI Score > 85 (mobile), > 90 (desktop)

### 5. GSC Performance Analysis (if GSC MCP active)

Last 28 days:
- Pages with high impressions but low CTR (CTR < 2%)
- Rankings between positions 8-20 (quick win opportunities)
- Pages with impressions but zero clicks
- Mobile vs Desktop performance gap

### 6. Internal Link Audit

```powershell
C:\Users\fatih\AppData\Local\studio_app\bin\studio.bat wp eval '
$posts = get_posts(["post_type"=>"post","posts_per_page"=>-1,"post_status"=>"publish"]);
foreach($posts as $p) {
    $has_related = strpos($p->post_content, "clt-related-articles") !== false;
    $has_disclosure = strpos($p->post_content, "clt-disclosure") !== false;
    $has_disclaimer = strpos($p->post_content, "clt-disclaimer") !== false;
    $issues = [];
    if(!$has_related) $issues[] = "NO_INTERNAL_LINKS";
    if(!$has_disclosure) $issues[] = "NO_DISCLOSURE";
    if(!$has_disclaimer) $issues[] = "NO_DISCLAIMER";
    if($issues) echo $p->ID . " | " . $p->post_title . " | " . implode(", ",$issues) . "\n";
}' --path="C:\Users\fatih\Studio\clearlegaltips"
```

### 7. Report Format

```
=== CLEARLEGALTIPS SEO AUDIT — [Date] ===

RANK MATH MISSING FIELDS:
[list]

SHORT CONTENT (< 3000 words):
[list]

PLACEHOLDER AFFILIATE LINKS:
[list]

STRUCTURE ISSUES (disclosure/disclaimer/internal links):
[list]

PAGESPEED (if available):
[scores]

GSC OPPORTUNITIES (if available):
[positions 8-20 list]

PRIORITY ACTIONS:
1. [Most critical issue]
2. [Second issue]
...
```
