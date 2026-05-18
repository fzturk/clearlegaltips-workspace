---
name: wp-publish
description: Publishes a ready article to WordPress. Use for "publish", "send to WordPress", "create post", "make draft" requests.
allowed-tools: Read Bash PowerShell
effort: medium
---

Upload an article to ClearLegalTips.com WordPress site.

## Input: $ARGUMENTS
Format: "file_path | post_id (optional)" or "article title"

## Prerequisite: WP Studio Must Be Running
http://localhost:8881 must be accessible.

---

## Option A — Upload via WP-CLI (Local Studio)

### 1. Read Article File
Read the .md file under `workspace/articles/`.

### 2. Determine Post Meta

Identify from the article:
- **Title** (from H1 or filename)
- **Category** — choose one of these 5 (to find IDs):
  ```powershell
  C:\Users\fatih\AppData\Local\studio_app\bin\studio.bat wp term list category --fields=term_id,name --path="C:\Users\fatih\Studio\clearlegaltips"
  ```
  Categories: Legal Document Templates | Business & LLC | Cost Guides & Calculators | How-to Guides | State-Specific Guides
- **Tags** — select appropriate tags from content
- **Focus keyword** — extract from H1
- **Meta description** — 150-155 characters

### 3. Create WP-CLI Post

Use `eval-file` instead of `--post_content` directly for multi-line HTML content:

```powershell
$WPCLI = "C:\Users\fatih\AppData\Local\studio_app\bin\studio.bat"
$WP_PATH = "C:\Users\fatih\Studio\clearlegaltips"

# Create post via PHP script (avoids content escape issues)
$php = @'
<?php
$pid = wp_insert_post([
    'post_title'   => 'TITLE',
    'post_content' => 'ARTICLE_HTML_CONTENT',
    'post_status'  => 'draft',
    'post_author'  => 291,
    'post_date'    => '2026-04-26 10:00:00',
    'post_type'    => 'post',
]);
if (is_wp_error($pid)) { echo "ERROR: " . $pid->get_error_message(); } else { echo "POST_ID: $pid"; }
'@
$php | Out-File -Encoding utf8 "$env:TEMP\wp_create_post.php"
& $WPCLI wp eval-file "$env:TEMP\wp_create_post.php" --path="$WP_PATH"
```

```powershell
# Set meta fields
$POST_ID = "ID_FROM_ABOVE"
& $WPCLI wp post meta update $POST_ID rank_math_focus_keyword "KEYWORD" --path="$WP_PATH"
& $WPCLI wp post meta update $POST_ID rank_math_description "META DESC" --path="$WP_PATH"
& $WPCLI wp post term add $POST_ID category CATEGORY_ID --path="$WP_PATH"
```

### 4. Upload Featured Image (if available)

```powershell
# Import image to media library and set as featured image
& $WPCLI wp media import "IMAGE_PATH" --post_id=$POST_ID --featured_image --path="$WP_PATH"
```

### 5. Flush Cache

```powershell
& $WPCLI wp cache flush --path="$WP_PATH"
```

---

## Option B — Upload via REST API (Live Site)

If the WordPress MCP is configured (`wordpress` server):

```
Via WordPress MCP:
1. Fetch article content
2. Write to wp_posts table (status: draft)
3. postmeta: rank_math_focus_keyword, rank_math_description
4. Assign category and tags
5. Upload featured image
```

---

## Output

```
POST CREATED:
ID: [post_id]
Title: [title]
URL: http://localhost:8881/?p=[post_id]
Status: draft
Category: [category]
Rank Math keyword: [keyword]
Featured image: [assigned/not assigned]

To publish:
  wp post update [ID] --post_status=publish --path="C:\Users\fatih\Studio\clearlegaltips"
```

---

## Update Existing Post

To update an existing post (use eval-file for HTML content):

```powershell
$php = @'
<?php
$pid = POST_ID;
$updated_content = 'NEW_HTML_CONTENT';
wp_update_post(['ID' => $pid, 'post_content' => $updated_content]);
clean_post_cache($pid);
echo "Updated: $pid\n";
'@
$php | Out-File -Encoding utf8 "$env:TEMP\wp_update_post.php"
& $WPCLI wp eval-file "$env:TEMP\wp_update_post.php" --path="$WP_PATH"
& $WPCLI wp cache flush --path="$WP_PATH"
```
