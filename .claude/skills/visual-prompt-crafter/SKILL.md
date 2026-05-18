---
name: visual-prompt-crafter
description: Generates optimized ComfyUI prompts for ClearLegalTips featured images. Use when asked to "create image prompt", "ComfyUI prompt", "featured image prompt", "generate image for article", or before running generate-featured-image skill.
---

# Visual Prompt Crafter

## Context

ClearLegalTips uses ComfyUI to generate featured images via `workspace/tools/comfyui_generate.py`. Images are 1216×640px, cropped to 1200×630px JPG. Default model: `juggernautXL_ragnarokBy.safetensors` (photorealistic). Site colors: Navy #1C2B4A, Crimson #C0392B, Cream #F8F6F2.

**Image naming convention:** `post-{id}-{slug}.jpg`  
**Output directory:** `workspace/generated-images/`

## Visual Style Guidelines

### DO — ClearLegalTips Image Aesthetic
- Professional, clean, real-world photography style
- Legal documents, pens, desks, courthouses, official stamps
- Navy and cream color tones dominant
- Shallow depth of field (bokeh background)
- Natural lighting, no dramatic shadows
- People: professional attire, diverse representation, approachable expressions
- No text overlays in the image itself (text added separately by WordPress)

### DON'T
- No cartoon or illustrated styles
- No dark/gloomy courthouse imagery (intimidating)
- No stressed people / courtroom drama
- No handcuffs, police, prison imagery
- No visible brand logos or specific software UIs
- No stock-photo-style fake smiles

## Prompt Templates by Article Type

### Template Articles (131–150)
**Core elements:** Document on desk, pen ready to sign, professional context

```
professional legal document on wooden desk, fountain pen beside it, 
soft natural window light, shallow depth of field, navy blue folder, 
cream paper, warm professional office background, photorealistic, 
4k detail, --ar 16:9
```

### Cost/Calculator Articles (151–165)
**Core elements:** Calculator, financial documents, clean desk

```
modern desk with calculator and legal documents, professional hands 
reviewing paperwork, warm office lighting, navy and cream color palette, 
clean minimal composition, photorealistic business photography, 4k
```

### How-To Guide Articles (166–175)
**Core elements:** Action-oriented, laptop or form being filled out

```
person at laptop filling out official forms online, professional home 
office setting, natural light, focused composition, [state flag colors 
if state-specific], clean modern desk, photorealistic, 4k
```

### State Guide Articles (176–180)
**Core elements:** State-specific visual if possible, official documents

```
official government building exterior with clear blue sky, professional 
photography style, [state name] implied setting, clean architectural 
composition, warm lighting, photorealistic, 4k
```

## Topic-Specific Prompt Formulas

| Article Topic | Key Visual Elements to Include |
|---|---|
| NDA / Confidentiality | Two people shaking hands over a document |
| LLC Formation | Business stamp on official documents, navy folder |
| Operating Agreement | Multi-page document with signatures, professional desk |
| Lease Agreement | Keys on a rental agreement document |
| Will / Estate Planning | Older hands holding an official document |
| LLC Cost / Fees | Calculator, dollar bills, official form |
| Registered Agent | Mailbox + official envelope, professional context |
| Divorce / Family Law | Two rings, legal document (tasteful, not dramatic) |
| Business Formation | Professional handshake, business documents |

## Instructions

1. **Identify the article topic** from the post title or H1
2. **Select the base template** matching the article type
3. **Add topic-specific elements** from the table above
4. **Include negative prompt** to avoid unwanted elements
5. **Output the full ComfyUI command**

## Output Format

```
FEATURED IMAGE PROMPT
Article: [title] (Post ID: [id])
Output filename: post-[id]-[slug].jpg

POSITIVE PROMPT:
[full prompt text]

NEGATIVE PROMPT:
cartoon, illustration, text overlay, brand logos, handcuffs, 
prison, courtroom drama, stock photo fake smile, dark gloomy, 
watermark, blurry, low quality, oversaturated

COMFYUI COMMAND:
python3 workspace/tools/comfyui_generate.py \
  --prompt "[positive prompt]" \
  --negative "[negative prompt]" \
  --output "workspace/generated-images/post-[id]-[slug].jpg" \
  --steps 20 \
  --width 1216 \
  --height 640
```
