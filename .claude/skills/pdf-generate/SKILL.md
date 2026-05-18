---
name: pdf-generate
description: Makale veya şablon içeriğinden indirilebilir PDF oluşturur. "PDF yap", "indirilebilir belge oluştur", "PDF üret" gibi taleplerde kullan.
allowed-tools: Read Write Bash
effort: medium
---

ClearLegalTips için indirilebilir PDF oluştur.

## Giriş: $ARGUMENTS
Format: "dosya_yolu" veya "post_id" veya "şablon adı"

---

## Adım 1 — Kaynağı Belirle

Şu kaynaklardan birini seç:
- `workspace/articles/XX_makale_adi.md` — makale içeriği
- `workspace/templates/Sözlesme_Template_2026.md` — hukuki şablon
- WordPress post içeriği (WP-CLI ile çek)

---

## Adım 2 — PDF İçeriğini Hazırla

Markdown dosyayı şu formatta düzenle:

```markdown
---
title: "Başlık"
author: "ClearLegalTips.com"
date: "2026"
---

# Başlık

**Önemli Not:** Bu belge genel bilgi amaçlıdır ve hukuki tavsiye niteliği taşımaz.

[İÇERİK]

---
*© 2026 ClearLegalTips.com — clearlegaltips.com*
*Bu belge yalnızca bilgilendirme amaçlıdır. Hukuki tavsiye için lisanslı bir avukana başvurun.*
```

---

## Adım 3A — Python ile PDF Oluştur (ReportLab)

```python
# workspace/tools/generate_pdf.py kullan
python3 "C:/Users/fatih/Desktop(1)/Claude/clear_legal_tips/workspace/tools/generate_pdf.py" \
  --input "workspace/templates/NDA_Template_2026.md" \
  --output "workspace/pdfs/NDA_Template_ClearLegalTips.pdf" \
  --title "Free NDA Template 2026"
```

---

## Adım 3B — Markdown2PDF MCP ile Oluştur (PDF MCP kuruluysa)

```
PDF MCP'ye gönder:
- Input: markdown içerik
- Theme: Professional
- Header: ClearLegalTips.com
- Footer: Sayfa numarası + URL
- Output: workspace/pdfs/DOSYA_ADI.pdf
```

---

## Adım 4 — WordPress'e Yükle

```powershell
$WPCLI = "C:\Users\fatih\AppData\Local\studio_app\bin\studio.bat"
$WP_PATH = "C:\Users\fatih\Studio\clearlegaltips"

# PDF'i media library'e yükle
& $WPCLI wp media import "workspace/pdfs/NDA_Template_ClearLegalTips.pdf" `
  --title="Free NDA Template PDF" `
  --path="$WP_PATH" `
  --porcelain
# Dönen media ID'yi kaydet

# İlgili makaleye download link ekle (post_id ile)
# Örnek: post 131 = NDA makalesi
```

---

## Adım 5 — Download Link HTML'i Üret

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

## PDF Adlandırma Kuralı

`ClearLegalTips_[Belge_Tipi]_Template_2026.pdf`

Örnekler:
- `ClearLegalTips_NDA_Template_2026.pdf`
- `ClearLegalTips_LLC_Operating_Agreement_2026.pdf`
- `ClearLegalTips_Last_Will_Template_2026.pdf`

---

## Toplu PDF Üretimi (20 Şablon İçin)

```
Sırayla şu şablonlar için PDF üret:
workspace/templates/ altındaki tüm *_Template_2026.md dosyaları
```
