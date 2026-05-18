---
name: generate-featured-image
description: Generates WordPress featured images using ComfyUI. Use for "create image", "make featured image", "article image" requests. ComfyUI must be running (localhost:8000).
allowed-tools: Bash Read Write
effort: medium
---

Generate a 1200×630px featured image for ClearLegalTips.com.

## Input: $ARGUMENTS
(Format: "article title | topic description" or just article title)

## Step 1 — Check ComfyUI Status

```bash
python3 -c "
import urllib.request, json, sys
try:
    r = urllib.request.urlopen('http://127.0.0.1:8000/system_stats', timeout=3)
    data = json.loads(r.read())
    print('COMFYUI_RUNNING: OK')
    print('GPU:', data.get('system', {}).get('cuda_device_name', 'CPU'))
except Exception as e:
    print('COMFYUI_NOT_RUNNING:', e)
    print('Please start ComfyUI and try again.')
    sys.exit(1)
"
```

Stop and notify the user if ComfyUI is not running.

## Step 2 — Check Available Models

```bash
python3 -c "
import urllib.request, json
r = urllib.request.urlopen('http://127.0.0.1:8000/object_info/CheckpointLoaderSimple', timeout=5)
data = json.loads(r.read())
models = data['CheckpointLoaderSimple']['input']['required']['ckpt_name'][0]
print('Available models:')
for m in models[:5]:
    print(' -', m)
"
```

## Step 3 — Create Image Prompt

Write an English image prompt based on the article title and topic:

**Prompt template (for legal content):**
```
professional legal document illustration, [TOPIC-RELATED ELEMENT], 
clean minimalist design, navy blue #1C2B4A and white color scheme, 
law office aesthetic, modern flat design, no text, 
high quality 4K, sharp edges, professional photography style,
wide format 1200x630
```

**Negative prompt:**
```
text, watermark, signature, blurry, low quality, cartoon, 
anime, people faces, hands, distorted, ugly, bad anatomy,
cluttered, busy background
```

## Step 4 — Send to ComfyUI API

```bash
python3 "C:/Users/fatih/Desktop(1)/Claude/clear_legal_tips/workspace/tools/comfyui_generate.py" \
  --prompt "PROMPT_HERE" \
  --negative "NEGATIVE_PROMPT" \
  --output "C:/Users/fatih/Desktop(1)/Claude/clear_legal_tips/workspace/generated-images/FILENAME.jpg"
```
Note: Script internally generates at 1216×640 and resizes to 1200×630 via PIL.

## Step 5 — Manual Mode (if ComfyUI is offline)

If ComfyUI is not running, provide this format to the user:

```
=== COMFYUI MANUAL PROMPT ===

POSITIVE PROMPT:
[prompt]

NEGATIVE PROMPT:
[negative prompt]

SETTINGS:
- Width: 1200
- Height: 630
- Steps: 25
- CFG Scale: 7
- Sampler: DPM++ 2M Karras

Save location: workspace/generated-images/[filename].jpg
```

## Output

When image is generated:
1. Report file path: `workspace/generated-images/[filename].jpg`
2. Provide the upload command:

```powershell
# Upload to WordPress Media Library (WP Studio)
C:\Users\fatih\AppData\Local\studio_app\bin\studio.bat wp media import "C:/Users/fatih/Desktop(1)/Claude/clear_legal_tips/workspace/generated-images/FILENAME.jpg" --post_id=POST_ID --featured_image --path="C:\Users\fatih\Studio\clearlegaltips"
```

## Naming Convention

`post-{ID}-{slug}-featured.jpg`  
Example: `post-131-free-nda-template-featured.jpg`

## Batch Generation

For multiple articles:
```
/generate-featured-image post-131 | NDA template article
/generate-featured-image post-132 | Independent contractor agreement
```
