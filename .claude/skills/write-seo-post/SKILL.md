---
name: write-seo-post
description: ClearLegalTips için SEO uyumlu WordPress blog makalesi yazar. Kullanıcı "makale yaz", "içerik oluştur", "post yaz" veya bir hukuki konu hakkında içerik istediğinde kullan.
allowed-tools: Read Write WebSearch WebFetch
effort: high
---

ClearLegalTips.com için 3000+ kelimelik, Rank Math uyumlu, affiliate linkli SEO makalesi yaz.

## Hedef: $ARGUMENTS

## Yazma Adımları

### 1. Konu Araştırması
- Konuyu web'de araştır: "$ARGUMENTS + explained site:gov OR site:irs.gov OR site:law.cornell.edu"
- 3-5 otoriter kaynak bul (gov, law firm, established publication)
- Rakiplerin hangi açılardan yazdığını incele
- FAQ sorularını topla: "people also ask" için ara

### 2. Outline Oluştur
```
H1: [Ana başlık — focus keyword içermeli]
H2: What Is [Topic]? (tanım + temel bilgi)
H2: How [Topic] Works (mekanizma, süreç)
H2: [Topic] Requirements / Steps (liste formatı)
H2: Common Mistakes to Avoid
H2: Cost Breakdown (varsa)
H2: State-Specific Considerations (US odaklı)
H2: Frequently Asked Questions
H2: Bottom Line
```

### 3. İçerik Yazımı
- Minimum **3000 kelime**
- İlk 100 kelimede focus keyword geçmeli
- Ton: Açık, profesyonel, hukuki tavsiye değil bilgi
- Her H2 altında minimum 200 kelime
- Numbered/bulleted listeler kullan, taranabilirlik için
- İstatistik ve rakamlar varsa kaynak göster

### 4. Zorunlu Elementler (Her Makalede)

**FTC Disclosure** (makalenin en üstüne):
```html
<div class="clt-disclosure">
<strong>Disclosure:</strong> This article contains affiliate links. If you purchase through our links, we may earn a commission at no extra cost to you. We only recommend services we've researched and believe provide value.
</div>
```

**CTA Box** (konuya uygun affiliate servis için):
```html
<div class="clt-cta-box">
<h3>Ready to Get Started?</h3>
<p>[Brief description — why this service is the best option]</p>
<a href="/recommend/[slug]" class="clt-affiliate-btn" rel="nofollow sponsored">
  Get Started with [Service Name] →
</a>
</div>
```

**Internal Link Box** (hub-spoke map'e göre 3 ilgili makale):
```html
<div class="clt-related-articles">
<h3>Related Articles</h3>
<ul>
<li><a href="/[slug-1]">[Article 1 Title]</a></li>
<li><a href="/[slug-2]">[Article 2 Title]</a></li>
<li><a href="/[slug-3]">[Article 3 Title]</a></li>
</ul>
</div>
```

**Legal Disclaimer** (makalenin en altına):
```html
<div class="clt-disclaimer">
<strong>Legal Disclaimer:</strong> The information provided in this article is for general informational purposes only and does not constitute legal advice. For advice specific to your situation, consult a licensed attorney in your jurisdiction.
</div>
```

### 5. Rank Math SEO Alanları (makale sonunda belirt)

```
Focus Keyword: [birincil keyword]
Meta Title: [60 karakter max — keyword başta]
Meta Description: [150-155 karakter — keyword + value prop + CTA]
```

### 6. Featured Image Önerisi
```
Dosya adı: post-[id]-[slug].jpg
Boyut: 1200×630px
Alt text: [Focus keyword içeren açıklayıcı metin]
```

## Affiliate CTA Slug Rehberi

| Konu | Slug |
|---|---|
| LLC formation | /recommend/zenbusiness |
| Registered agent | /recommend/northwest-ra |
| Legal documents | /recommend/lawdepot |
| Online divorce | /recommend/completecase |
| Living trust | /recommend/trust-and-will |
| Trademark | /recommend/legalzoom |
| EIN / Business formation | /recommend/incfile |

## Çıktı Formatı

Makaleyi şu formatta sun:

1. **MAKALE İÇERİĞİ** (tam HTML veya Markdown)
2. **SEO ALANLARI** (Focus keyword, meta title, meta description)
3. **NOTLAR** (iç linkleme önerileri, featured image önerisi)
