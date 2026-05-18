---
name: affiliate-research
description: Affiliate program araştırır, komisyon karşılaştırması yapar, başvuru emaili hazırlar. "Affiliate araştır", "program bul", "başvuru hazırla" gibi taleplerde kullan.
allowed-tools: WebSearch WebFetch Read Write
effort: high
---

ClearLegalTips için affiliate program araştırması yap ve başvuru hazırla.

## Hedef: $ARGUMENTS
(Program adı, kategori, veya "tümü")

---

## ClearLegalTips Öncelikli Program Listesi

| Program | Platform | Tahmini Komisyon | Durum |
|---|---|---|---|
| LawDepot | Impact | ~30% recurring | Başvurulmadı |
| ZenBusiness | ShareASale / Direct | ~$100-150/sale | Başvurulmadı |
| Northwest Registered Agent | ShareASale | ~$100/sale | Başvurulmadı |
| Rocket Lawyer | CJ Affiliate | ~$30/sale | Başvurulmadı |
| LegalZoom | CJ Affiliate | ~$15-30/sale | Başvurulmadı |
| Nolo | Direct | ~10-15% | Başvurulmadı |
| Incfile (Bizee) | Direct | ~$75/sale | Başvurulmadı |
| Trust & Will | Impact | ~$30-50/sale | Başvurulmadı |
| CompleteCasez | Direct | ~$50/sale | Başvurulmadı |
| BizFilings | CJ Affiliate | ~$50/sale | Başvurulmadı |

---

## Araştırma Adımları

### 1. Program Detaylarını Araştır
Her program için şunları bul:
- Affiliate program URL'i (genellikle site.com/affiliates)
- Komisyon oranı ve yapısı (CPS, CPA, recurring?)
- Cookie süresi (30 gün? 90 gün?)
- Minimum ödeme eşiği
- Ödeme yöntemi (PayPal, check, wire)
- Onay süreci (otomatik mi, manuel mi?)
- Yasaklı trafik türleri (PPC yasak mı?)
- Promosyon materyalleri (banner, text link)

Arama: `"[PROGRAM ADI] affiliate program" commission cookie`

### 2. Komisyon Karşılaştırma Tablosu

```
| Program | Komisyon | Cookie | Min Ödeme | Onay | Platform |
|---------|----------|--------|-----------|------|----------|
| LawDepot | % | gün | $ | oto/manuel | Impact |
...
```

### 3. Başvuru Emaili Şablonu Oluştur

Şu bilgileri içerecek şekilde:

```
Subject: Affiliate Partnership Inquiry — ClearLegalTips.com

Hello [Program Name] Affiliate Team,

My name is [Ad], and I run ClearLegalTips.com, a legal education 
website helping US consumers navigate DIY legal processes.

SITE STATS (approximate, growing):
- Niche: Legal document templates, LLC formation, estate planning, 
  divorce guides for US consumers
- Content: 50+ in-depth articles (3,000+ words each)
- Target audience: US adults seeking affordable legal solutions
- Primary traffic: Organic search (Google)

WHY WE'RE A GOOD FIT:
Our content directly addresses the problems your service solves. 
For example, our article on [RELEVANT ARTICLE] naturally leads 
readers to need exactly what [PROGRAM] offers.

I'm interested in joining your affiliate program to recommend 
[PROGRAM] to our readers when it's genuinely the best solution 
for their needs.

Could you share details about your affiliate program, or point 
me to the application page?

Best regards,
[Ad]
ClearLegalTips.com
[Email]
```

### 4. Program Başvuru Sayfalarını Bul

```
Arama: "[program adı] affiliate program apply"
Kontrol et:
- Impact.com hesabı var mı?
- ShareASale hesabı var mı?
- CJ Affiliate hesabı var mı?
- Direct program mu?
```

---

## Çıktı Formatı

```
=== AFİLİATE ARAŞTIRMA RAPORU ===
Tarih: [tarih]

PROGRAM: [Program Name]
URL: [affiliate program URL]
Platform: [Impact / ShareASale / CJ / Direct]
Komisyon: [oran]
Cookie: [gün]
Min Ödeme: [$]
Onay: [Otomatik / Manuel / 2-5 gün]
Başvuru: [URL]
Not: [Özel şartlar, yasaklar]

HAZIR EMAIL:
[email içeriği]

ÖNCELİK: [Yüksek / Orta / Düşük]
NEDEN: [Açıklama]
```

---

## Sonraki Adım

Başvuru tamamlandığında `workspace/OPERATIONS_MANUAL.md` güncellenecek:
```
| [Program] | [Platform] | [Tarih] | Başvuruldu | Bekliyor |
```
