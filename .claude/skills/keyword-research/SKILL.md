---
name: keyword-research
description: ClearLegalTips için keyword araştırması yapar. "Keyword bul", "hangi konuyu yazalım", "SEO fırsatı" gibi taleplerde kullan.
allowed-tools: WebSearch WebFetch Read
effort: high
---

ClearLegalTips.com için hukuki DIY keyword araştırması yap.

## Araştırma Konusu: $ARGUMENTS

## Adımlar

### 1. Seed Keyword Genişletme
Şu varyasyonları araştır:
- "$ARGUMENTS + free"
- "$ARGUMENTS + online"
- "$ARGUMENTS + template"
- "$ARGUMENTS + cost"
- "$ARGUMENTS + how to"
- "$ARGUMENTS + form"
- "how to [do $ARGUMENTS] yourself"
- "[state] + $ARGUMENTS" (TX, CA, FL, NY, IL için)

### 2. Mevcut Ahrefs MCP Kullanımı
Eğer Ahrefs MCP aktifse (`mcp__claude_ai_Ahrefs__keywords-explorer-overview`) şunları çek:
- Search volume (US)
- Keyword difficulty (KD)
- Traffic potential
- SERP features (featured snippet, people also ask)

### 3. Rakip İçerik Analizi
Top 3-5 sıralanan sayfaları incele:
- Başlık yapısı
- İçerik uzunluğu
- Hangi konuları kapsıyor / kapsamıyor
- Hangi affiliate servisleri öneriyorlar
- Featured snippet var mı?

### 4. Intent Sınıflandırması
Her keyword için intent belirle:
- **Informational** ("what is", "how does") → template/guide makalesi
- **Transactional** ("best", "review", "vs") → affiliate karşılaştırma
- **Navigational** (marka aramaları) → pas geç
- **Commercial Investigation** ("cost", "price", "cheap") → calculator/cost guide

### 5. Mevcut İçerikle Örtüşme Kontrolü
ClearLegalTips'te zaten yazılmış konular (Post ID 131-180):
- NDA, LLC Operating Agreement, Commercial Lease, Residential Lease
- Bill of Sale, Promissory Note, Last Will, Living Trust, POA
- Medical POA, Prenup, Eviction Notice, Sublease, Service Agreement
- Partnership, Child Custody, Consulting Agreement, Quitclaim Deed
- LLC formation cost, S-Corp vs LLC, Registered Agent, DBA, EIN
- Annual reports, Business license, Foreign qualification, Trademark
- Estate tax, Probate cost, Living trust vs will, Divorce cost
- Child support, Small claims, LLC online, EIN online, RA online
- Uncontested divorce, CompleteCasez, Name change, Living trust online
- Trademark online, DBA online, Legal separation, Online divorce (state)
- Dissolve LLC, Copyright, Small claims evictions, Landlord accounting

### 6. Öncelik Matrisi

| Keyword | Volume | KD | Intent | İçerik Tipi | Öncelik |
|---|---|---|---|---|---|
| [keyword 1] | [vol] | [kd] | [intent] | [tip] | [P1/P2/P3] |

### 7. Sonuç Raporu

**En Yüksek Potansiyelli 10 Keyword:**
1. Keyword — Volume: X, KD: Y, Intent: Z, Öneri: [içerik tipi]
...

**Hızlı Kazanım Fırsatları (KD < 20, Volume > 500):**
- ...

**Uzun Vadeli Hedefler (KD 30-50, Volume > 2000):**
- ...

**Atlanacaklar (neden):**
- ...
