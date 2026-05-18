---
name: generate-featured-image
description: ComfyUI kullanarak WordPress featured image oluşturur. "Görsel oluştur", "featured image yap", "makale görseli" gibi taleplerde kullan. ComfyUI'nin açık olması gerekir (localhost:8000).
allowed-tools: Bash Read Write
effort: medium
---

ClearLegalTips.com için 1200×630px featured image oluştur.

## Giriş: $ARGUMENTS
(Format: "makale başlığı | konu açıklaması" veya sadece makale başlığı)

## Adım 1 — ComfyUI Durumunu Kontrol Et

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
    print('Lütfen ComfyUI başlatın ve tekrar deneyin.')
    sys.exit(1)
"
```

ComfyUI çalışmıyorsa dur ve kullanıcıya bildir.

## Adım 2 — Mevcut Modeli Kontrol Et

```bash
python3 -c "
import urllib.request, json
r = urllib.request.urlopen('http://127.0.0.1:8000/object_info/CheckpointLoaderSimple', timeout=5)
data = json.loads(r.read())
models = data['CheckpointLoaderSimple']['input']['required']['ckpt_name'][0]
print('Mevcut modeller:')
for m in models[:5]:
    print(' -', m)
"
```

## Adım 3 — Image Prompt Oluştur

Makale başlığı ve konusuna göre İngilizce image prompt yaz:

**Prompt şablonu (legal content için):**
```
professional legal document illustration, [KONU İLE İLGİLİ ELEMENT], 
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

## Adım 4 — ComfyUI API'ye Gönder

```bash
python3 "C:/Users/fatih/Desktop(1)/Claude/clear_legal_tips/workspace/tools/comfyui_generate.py" \
  --prompt "PROMPT_BURAYA" \
  --negative "NEGATIVE_PROMPT" \
  --output "C:/Users/fatih/Desktop(1)/Claude/clear_legal_tips/workspace/generated-images/DOSYAADI.jpg"
```
Not: Script dahili olarak 1216×640 üretir, PIL ile 1200×630'a yeniden boyutlandırır.

## Adım 5 — Manuel Mod (ComfyUI kapalıysa)

ComfyUI açık değilse şu formatı kullanıcıya ver:

```
=== COMFYUI MANUEL PROMPT ===

POSITIVE PROMPT:
[prompt]

NEGATIVE PROMPT:
[negative prompt]

AYARLAR:
- Width: 1200
- Height: 630
- Steps: 25
- CFG Scale: 7
- Sampler: DPM++ 2M Karras

Kayıt yeri: workspace/generated-images/[dosya-adı].jpg
```

## Çıktı

Görsel oluşturulunca:
1. Dosya yolu bildir: `workspace/generated-images/[dosya-adı].jpg`
2. WordPress'e yüklemek için komut ver:

```powershell
# WordPress Media Library'e yükle (WP Studio)
C:\Users\fatih\AppData\Local\studio_app\bin\studio.bat wp media import "C:/Users/fatih/Desktop(1)/Claude/clear_legal_tips/workspace/generated-images/DOSYA.jpg" --post_id=POST_ID --featured_image --path="C:\Users\fatih\Studio\clearlegaltips"
```

## Adlandırma Kuralı

`post-{ID}-{slug}-featured.jpg`  
Örnek: `post-131-free-nda-template-featured.jpg`

## Toplu Üretim

Birden fazla makale için:
```
/generate-featured-image post-131 | NDA template article
/generate-featured-image post-132 | Independent contractor agreement
```
