---
description: Refresh one or all ClearLegalTips articles — update dates, prices, statistics, and stale content. Pass a post ID for a single article, or "all" for batch refresh of all 50 posts.
---

# Content Refresh

Refresh content for: **$ARGUMENTS**

If `$ARGUMENTS` is a number → refresh that single post.
If `$ARGUMENTS` is `all` → batch refresh all 50 posts (IDs 131–180).
If `$ARGUMENTS` is a range like `151-165` → refresh that ID range.

## Refresh Workflow

### Phase 1 — Staleness Audit

For each post in scope, use `content-refresher` skill to identify:

**Dates:**
- Publication year mentions (e.g., "As of 2024", "In 2023")
- Statute/law year references that may be outdated
- Any "current year" language that needs updating to 2026

**Prices (critical for IDs 151–165):**
- Filing fees (state government fees — verify against .gov sources)
- Affiliate service pricing: ZenBusiness, Northwest, LawDepot, LegalZoom, Rocket Lawyer, Incfile
- Attorney rate estimates ("$150–$300/hour")

**Statistics:**
- Percentage figures ("70% of small businesses...")
- Survey data with year citations
- Any statistic older than 2 years

**Affiliate Services:**
- Feature descriptions (plans/tiers may have changed)
- Pricing tiers
- Processing time claims

### Phase 2 — Classify Changes

For each flagged item:
- **Safe to auto-update** — year references (2024 → 2026), obvious date formatting
- **Requires verification** — affiliate prices (check official site before updating)
- **Requires manual check** — state filing fees (must use .gov source)

Only auto-update items classified as "safe". Flag the rest for manual review.

### Phase 3 — Generate Updates

For items verified as needing change, produce PHP update snippets:

```php
// Content text replacement
$post = get_post($pid);
$content = $post->post_content;
$content = str_replace('As of 2024', 'As of 2026', $content);
$content = str_replace('$49/year filing fee', '$55/year filing fee', $content);
wp_update_post(['ID' => $pid, 'post_content' => $content]);
clean_post_cache($pid);
echo "Updated post {$pid}\n";
```

### Phase 4 — Modified Date Refresh

For every post that received content changes:
```php
wp_update_post([
  'ID' => $pid,
  'post_modified' => current_time('mysql'),
  'post_modified_gmt' => current_time('mysql', 1),
]);
clean_post_cache($pid);
```

### Phase 5 — Cache Flush

After all updates:
```php
if (class_exists('WpFastestCache')) {
  $wpfc = new WpFastestCache();
  $wpfc->deleteCache();
  echo "Cache flushed.\n";
}
```

## Batch Safety Rules

- **Never run batch update on >10 posts without showing the change list first**
- Always show a diff summary (old value → new value) before executing
- Log all changes to `workspace/refresh-log-[date].txt`
- Never reduce word count below 3,000 words
- Never change post slugs

## Output Format

```
REFRESH REPORT — [scope] — [date]

POSTS REVIEWED: [X]
CHANGES IDENTIFIED: [X]

AUTO-UPDATES (safe to apply):
- Post [ID] "[title]": "[old]" → "[new]"

MANUAL VERIFICATION NEEDED:
- Post [ID] "[title]": [item] — needs verification at [source type]

PHP UPDATE SCRIPT:
[full PHP script for all auto-updates]

ESTIMATED IMPACT: [X posts refreshed, modified dates updated]
```
