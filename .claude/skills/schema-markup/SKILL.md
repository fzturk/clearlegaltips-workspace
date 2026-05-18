---
name: schema-markup
description: WordPress makalelerine HowTo, FAQPage veya Article schema markup ekler. "Schema ekle", "yapılandırılmış veri", "rich result" gibi taleplerde kullan.
allowed-tools: Read Bash
effort: medium
---

ClearLegalTips makalelerine JSON-LD schema markup ekle.

## Hedef: $ARGUMENTS
(Post ID veya makale türü)

---

## Makale Türüne Göre Schema Seçimi

| Makale Tipi | Schema | Neden |
|---|---|---|
| Template articles (131-150) | HowTo + FAQPage | "How to use/fill" adımları var |
| Cost guides (151-165) | FAQPage + Article | Soru-cevap ağırlıklı |
| How-to guides (166-175) | HowTo + FAQPage | Adım adım süreç |
| State guides (176-180) | FAQPage + Article | Bölgesel bilgi |

---

## Schema Şablonları

### HowTo Schema
```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "BAŞLIK",
  "description": "META DESCRIPTION",
  "step": [
    {
      "@type": "HowToStep",
      "name": "ADIM 1 BAŞLIĞI",
      "text": "ADIM 1 AÇIKLAMA"
    },
    {
      "@type": "HowToStep",
      "name": "ADIM 2 BAŞLIĞI",
      "text": "ADIM 2 AÇIKLAMA"
    }
  ],
  "estimatedCost": {
    "@type": "MonetaryAmount",
    "currency": "USD",
    "value": "GERÇEK_MALİYET_VEYA_0"
  }
}
```
Not: Template articles (131-150) için `value: "0"` uygundur (şablon ücretsiz).
Cost guide makalelerde (151-165) gerçek maliyet aralığını gir (örn. "50-500") veya bu alanı tamamen kaldır.
```json
```

### FAQPage Schema
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "SORU 1?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "CEVAP 1"
      }
    },
    {
      "@type": "Question",
      "name": "SORU 2?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "CEVAP 2"
      }
    }
  ]
}
```

### Article Schema
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "BAŞLIK",
  "description": "META DESCRIPTION",
  "author": {
    "@type": "Person",
    "name": "YAZAR ADI",
    "url": "https://clearlegaltips.com/author/SLUG/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "ClearLegalTips",
    "url": "https://clearlegaltips.com",
    "logo": {
      "@type": "ImageObject",
      "url": "https://clearlegaltips.com/wp-content/uploads/clear_legal_tips_logo_for_google.png"
    }
  },
  "datePublished": "TARİH",
  "dateModified": "TARİH"
}
```

---

## Adımlar

### 1. Makale İçeriğini Analiz Et
Post ID verildiyse WP-CLI ile oku:
```powershell
$WPCLI = "C:\Users\fatih\AppData\Local\studio_app\bin\studio.bat"
$WP_PATH = "C:\Users\fatih\Studio\clearlegaltips"
& $WPCLI wp post get POST_ID --fields=post_title,post_content,post_date --path="$WP_PATH"
```

### 2. Schema JSON Üret
- Makale içindeki H2 başlıkları → HowTo steps
- FAQ bölümündeki sorular → FAQPage mainEntity
- Yazar bilgisi → CLAUDE.md'den al

### 3. WordPress'e Ekle

Schema'yı post'un `post_content` başına `<script type="application/ld+json">` olarak ekle:

```powershell
# PHP script ile ekle
$script = @'
<?php
$pid = POST_ID;
$p = get_post($pid);
$schema = '{"@context":"https://schema.org",...}';
$script_tag = '<script type="application/ld+json">' . $schema . '</script>';
if (strpos($p->post_content, 'application/ld+json') === false) {
    $updated = $script_tag . "\n" . $p->post_content;
    wp_update_post(['ID' => $pid, 'post_content' => $updated]);
    clean_post_cache($pid);
    echo "Schema eklendi: $pid\n";
} else {
    echo "Schema zaten var: $pid\n";
}
'@
$script | Out-File -Encoding utf8 "$env:TEMP\add_schema.php"
& $WPCLI wp eval-file "$env:TEMP\add_schema.php" --path="$WP_PATH"
```

### 4. Doğrula
Schema eklenince Google Rich Results Test URL'ini ver:
```
https://search.google.com/test/rich-results?url=https://clearlegaltips.com/SLUG/
```

---

## Toplu Schema Ekleme

Tüm 50 makaleye türlerine göre schema eklemek için:
```
Post 131-150: HowTo + FAQPage
Post 151-165: FAQPage + Article
Post 166-175: HowTo + FAQPage
Post 176-180: FAQPage + Article
```
