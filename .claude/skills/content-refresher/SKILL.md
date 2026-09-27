---
name: content-refresher
description: Updates existing ClearLegalTips articles with current dates, statistics, law changes, and pricing. Use when asked to "update this article", "refresh content", "content is outdated", "update the stats", or when running quarterly content maintenance.
allowed-tools: Read Write Bash
effort: medium
---

# Content Refresher

## Context

ClearLegalTips has 50 articles published between April 1–25, 2026. Content staleness hurts both SEO rankings and user trust. Legal content specifically ages quickly due to:
- State filing fee changes
- New online service pricing
- Law amendments (especially LLC, estate planning, landlord-tenant)
- Affiliate service changes (pricing tiers, features, availability)

## Instructions

### Step 1 — Staleness Audit

Check for these common outdated elements:

| Element | What to Check |
|---|---|
| Publication date | Update "Last updated" date in post meta |
| Year references | Any "2024" or "2025" in article text |
| Filing fees | State LLC fees, court fees, registration fees |
| Affiliate pricing | LawDepot, ZenBusiness, etc. current prices |
| Statistics | Any cited stats with year attached |
| Law references | "As of [year], the law requires..." |
| Service features | Features/tiers of recommended services |
| State-specific rules | LLC laws, landlord-tenant rules, probate thresholds |

### Step 2 — Priority Refresh Targets

High priority (refresh first):
1. Cost/calculator articles (151–165) — pricing changes most often
2. State-specific guides (176–180) — laws change by legislative session
3. How-to guides (166–175) — online service workflows update frequently

Medium priority:
4. Template articles (131–150) — legal standards change less often

### Step 3 — Update Types

**Date update only** (5 min):
- Change `rank_math_description` if it mentions a year
- Update "Last updated: [date]" in article
- PHP: `wp_update_post(['ID' => $pid, 'post_modified' => date('Y-m-d H:i:s')]);`

**Pricing update** (15 min):
- Update all price mentions in article body
- Update CTA button copy if it includes a price
- Verify ThirstyAffiliates link still works

**Content refresh** (30–60 min):
- Rewrite outdated sections
- Add new FAQ entries for emerging questions
- Update schema markup if FAQs change
- Add "Editor's Note" callout if law changed significantly

**Full rewrite** (when traffic is dropping and content is >12 months old):
- Treat as a new article with updated brief
- Use existing URL (don't change slug)
- 301 redirect not needed — same URL

### Step 4 — Seasonal Opportunities

| Time of Year | Content Angle |
|---|---|
| January | "LLC Formation in [Year]: New Rules and Costs" |
| March–April | "Tax Season: Business Structure Implications" |
| Q3 | "Annual Report Deadlines by State" |
| November | "Year-End Business Compliance Checklist" |

### Step 5 — PHP Update Script

```php
// Refresh post modified date and update meta
$pid = [ID];
$current_year = date('Y');

// Update post modified date
wp_update_post([
  'ID' => $pid,
  'post_modified' => current_time('mysql'),
  'post_modified_gmt' => current_time('mysql', 1),
]);

// Update meta description year if needed
$desc = get_post_meta($pid, 'rank_math_description', true);
$desc_updated = preg_replace('/\b202[0-9]\b/', $current_year, $desc);
if ($desc !== $desc_updated) {
  update_post_meta($pid, 'rank_math_description', $desc_updated);
  echo "Updated meta description year for post $pid\n";
}

clean_post_cache($pid);
echo "Refreshed post $pid\n";
```

## Output Format

**For a single article audit:**
```
CONTENT REFRESH AUDIT: Post [ID] — [Title]
Last Published: [date]
Refresh Priority: HIGH | MEDIUM | LOW

OUTDATED ELEMENTS FOUND:
- [element]: "[old text]" → "[suggested update]"
- ...

RECOMMENDED ACTION: Date-only | Pricing update | Content refresh | Full rewrite
ESTIMATED TIME: [X minutes]
PHP SNIPPET: [code if needed]
```

**For batch quarterly refresh:**
```
QUARTERLY REFRESH PLAN — Q[X] [Year]

URGENT (do this week):
- Post [ID]: [reason]

SCHEDULED (do this month):
- Post [ID]: [reason]

MONITOR ONLY:
- Post [ID]: [reason]
```
