---
name: internal-link-auditor
description: Audits and improves internal linking across ClearLegalTips articles using the hub-spoke model. Use when asked to "fix internal links", "improve internal linking", "audit links", "hub-spoke", or "which articles should link to each other".
allowed-tools: Read Write Bash
effort: medium
---

# Internal Link Auditor

## Context

ClearLegalTips uses a hub-spoke content model:
- **Hub articles**: broad topic pages (e.g., "How to Form an LLC")
- **Spoke articles**: specific subtopics (e.g., "LLC Operating Agreement Template", "LLC Annual Report Requirements")

Internal links are placed in:
1. `<div class="clt-related-articles">` — the dedicated related articles box (3 links max, at article bottom)
2. Contextual inline links within article body text

**Post ID map:**
- 131–150: Template articles (spokes — link TO hub how-to guides)
- 151–165: Cost articles (spokes — link TO template articles + hub guides)
- 166–175: How-to guides (HUBS — link TO relevant templates + cost articles)
- 176–180: State guides (spokes — link TO relevant how-to hubs)

## Instructions

### Step 1 — Map the Hub-Spoke Clusters

Identify the 5 main topic clusters:
1. **LLC Formation** — Hub: 166-175 how-to guides | Spokes: LLC templates (131-150), LLC costs (151-165)
2. **Contracts & Agreements** — Hub: how-to guides | Spokes: NDA, operating agreement, contract templates
3. **Estate Planning** — Hub: how-to guides | Spokes: will templates, trust templates, probate guides
4. **Real Estate** — Hub: how-to guides | Spokes: lease templates, landlord-tenant guides
5. **Business Law** — Hub: how-to guides | Spokes: business formation templates, compliance guides

### Step 2 — Audit Rules

For each article, verify:
- [ ] Hub articles link to at least 3–5 relevant spoke articles
- [ ] Each spoke article links back to its hub
- [ ] No orphan articles (every article has at least 2 inbound internal links)
- [ ] `clt-related-articles` box has exactly 3 links, all relevant
- [ ] Anchor text is descriptive (not "click here" or "this article")
- [ ] No reciprocal link loops between just 2 articles

### Step 3 — Anchor Text Rules

| ❌ Bad Anchor | ✅ Good Anchor |
|---|---|
| click here | free NDA template |
| this article | how to form an LLC in California |
| read more | LLC operating agreement requirements |
| here | cost to hire a real estate attorney |

### Step 4 — Generate PHP Update Script

When fixing internal links in the `clt-related-articles` box:

```php
// Update related articles box for post [ID]
$pid = [ID];
$content = get_post_field('post_content', $pid);

$related_box = '<div class="clt-related-articles">
<h3>Related Articles</h3>
<ul>
  <li><a href="/[slug-1]">[Anchor Text 1]</a></li>
  <li><a href="/[slug-2]">[Anchor Text 2]</a></li>
  <li><a href="/[slug-3]">[Anchor Text 3]</a></li>
</ul>
</div>';

// Replace existing box or append before disclaimer
$content = preg_replace('/<div class="clt-related-articles">.*?<\/div>/s', $related_box, $content);
wp_update_post(['ID' => $pid, 'post_content' => $content]);
clean_post_cache($pid);
echo "Updated post $pid\n";
```

## Output Format

**For audit report:**
```
INTERNAL LINK AUDIT
Cluster: [name]

Hub Article: [title] (ID [x])
  Outbound links to spokes: [count] — [list]
  Missing links: [list]

Spoke Articles:
  [title] (ID [x]) — Links back to hub: YES/NO | Inbound links: [count]
  ...

ISSUES FOUND: [count]
RECOMMENDED FIXES: [list with PHP snippets]
```

**For a single article fix:**
```
POST [ID]: [title]
Current related-articles box: [existing links]
Recommended related-articles box: [new links with anchor text]
PHP update snippet: [code]
```
