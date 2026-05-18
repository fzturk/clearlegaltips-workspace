---
name: pdf-generate
description: Generates a downloadable PDF from article or template content. Use for "make PDF", "create downloadable document", "generate PDF" requests.
allowed-tools: Read Write Bash
effort: medium
---

Generate a downloadable PDF for ClearLegalTips.

## Input: $ARGUMENTS
Format: "file_path" or "post_id" or "template name"

---

## Step 1 — Identify Source

Choose one of these sources:
- `workspace/articles/XX_article_name.md` — article content
- `workspace/templates/Contract_Template_2026.md` — legal template
- WordPress post content (fetch via WP-CLI)

---

## Step 2 — Prepare PDF Content

Format the Markdown file as follows:

```markdown
---
title: "Title"
author: "ClearLegalTips.com"
date: "2026"
---

# Title

**Important:** This document is for general informational purposes only and does not constitute legal advice.

[CONTENT]

---
*© 2026 ClearLegalTips.com — clearlegaltips.com*
*This document is for informational purposes only. Consult a licensed attorney for advice specific to your situation.*
```

---

## Step 3A — Generate PDF with Python (ReportLab)

```powershell
# Use workspace/tools/generate_pdf.py (use absolute paths)
python "C:/Users/fatih/Desktop(1)/Claude/clear_legal_tips/workspace/tools/generate_pdf.py" `
  --input "C:/Users/fatih/Desktop(1)/Claude/clear_legal_tips/workspace/templates/NDA_Template_2026.md" `
  --output "C:/Users/fatih/Desktop(1)/Claude/clear_legal_tips/workspace/pdfs/NDA_Template_ClearLegalTips.pdf" `
  --title "Free NDA Template 2026"
```

---

## Step 3B — Generate with Markdown2PDF MCP (if PDF MCP is installed)

```
Send to PDF MCP:
- Input: markdown content
- Theme: Professional
- Header: ClearLegalTips.com
- Footer: Page number + URL
- Output: workspace/pdfs/FILENAME.pdf
```

---

## Step 4 — Upload to WordPress

```powershell
$WPCLI = "C:\Users\fatih\AppData\Local\studio_app\bin\studio.bat"
$WP_PATH = "C:\Users\fatih\Studio\clearlegaltips"

# Upload PDF to media library
& $WPCLI wp media import "workspace/pdfs/NDA_Template_ClearLegalTips.pdf" `
  --title="Free NDA Template PDF" `
  --path="$WP_PATH" `
  --porcelain
# Save the returned media ID

# Add download link to relevant article (with post_id)
# Example: post 131 = NDA article
```

---

## Step 5 — Generate Download Link HTML

```html
<div class="clt-cta-box">
  <h3>Download Free NDA Template (PDF)</h3>
  <p>Ready-to-use NDA template in PDF format. Fill in the blanks and sign.</p>
  <a href="[WP MEDIA URL]" class="clt-affiliate-btn" download>
    Download Free NDA Template →
  </a>
</div>
```

---

## PDF Naming Convention

`ClearLegalTips_[Document_Type]_Template_2026.pdf`

Examples:
- `ClearLegalTips_NDA_Template_2026.pdf`
- `ClearLegalTips_LLC_Operating_Agreement_2026.pdf`
- `ClearLegalTips_Last_Will_Template_2026.pdf`

---

## Bulk PDF Generation (20 Templates)

```
Generate PDFs in order for:
All *_Template_2026.md files under workspace/templates/
```
