# ClearLegalTips.com — Kapsamlı Operasyon Dokümanı
# Comprehensive Publishing Operations Manual

**Tarih:** Mayıs 2026
**Hazırlayan:** Claude (Fatih Ozturk için)
**Amaç:** 50 makalenin WordPress'e yayınlanması için gereken tüm adımları, affiliate link workflow'unu, görsel kaynaklarını ve SEO kontrol listelerini tek dokümanda toplamak.

---

## İÇİNDEKİLER

1. [Genel Yayınlama Workflow'u](#1-genel-yayınlama-workflowu)
2. [Affiliate Link Workflow (ThirstyAffiliates)](#2-affiliate-link-workflow)
3. [Makale Bazlı Affiliate Link Haritası](#3-makale-bazlı-affiliate-link-haritası)
4. [Görsel Kaynakları (Makale Bazlı)](#4-görsel-kaynakları)
5. [Internal Link Stratejisi](#5-internal-link-stratejisi)
6. [SEO Kontrol Listesi (Her Makale İçin)](#6-seo-kontrol-listesi)
7. [Rank Math Ayarları](#7-rank-math-ayarları)
8. [Yazar Atamaları](#8-yazar-atamaları)
9. [WordPress Kategori/Etiket Yapısı](#9-wordpress-kategori-ve-etiket-yapısı)
10. [FTC/Yasal Uyum Kontrol Listesi](#10-ftc-ve-yasal-uyum-kontrol-listesi)
11. [Yayınlama Takvimi (Önerilen Sıralama)](#11-yayınlama-takvimi)
12. [Sorun Giderme & SSS](#12-sorun-giderme)

---

## 1. GENEL YAYINLAMA WORKFLOW'U

### Her Makale İçin Adım Adım (Tahmini Süre: 10-15 dk/makale)

```
1. Markdown dosyasını aç (workspace/articles/XX_dosya_adi.md)
2. İçeriği WordPress Blok Editörüne yapıştır (Draft olarak)
3. Başlıktaki metadata bloğunu sil (Author, Focus Keyword vs. satırları)
4. [THIRSTY: ...] yer tutucularını gerçek ThirstyAffiliates kısa linkleriyle değiştir
5. Dropdown'dan doğru yazarı seç
6. Öne çıkan görseli yükle (Featured Image)
7. Kategori ve etiketleri ata
8. Rank Math SEO kutusunu doldur (Focus Keyword + Meta Description)
9. Rank Math skorunun 80+ (yeşil) olduğunu doğrula
10. İçeriği hızlı oku — doğal olmayan yer var mı kontrol et
11. "Publish" tıkla
```

### KRİTİK KURALLAR
- **ASLA** toplu otomatik yayınlama — her makaleyi birer birer aç, düzenle, yayınla
- **ASLA** aynı gün 5'ten fazla makale yayınlama (Google bot spam algılayabilir)
- Her makaleyi yayınlamadan önce EN AZ 1 küçük düzenleme yap (kelime değiştir, cümle ekle) — bu WordPress metadata'sında "insan düzenleme süresi" oluşturur
- Disclosure metni sayfadaki İLK affiliate linkinin ÜSTÜnde kalmalı

---

## 2. AFFILIATE LINK WORKFLOW

### 2.1 Affiliate Programlara Kayıt

Aşağıdaki sırayla başvur. Her programın onay süresi farklıdır:

| Sıra | Program | Başvuru Linki | Platform | Komisyon | Çerez | Onay Süresi |
|:----:|---------|--------------|----------|----------|-------|:-----------:|
| 1 | LawDepot | lawdepot.com/affiliates | Direkt | %30 tekrarlayan | 365 gün | 1-3 gün |
| 2 | LegalNature | ShareASale'de ara | ShareASale | %35 tekrarlayan | 90 gün | 1-5 gün |
| 3 | ZenBusiness | zenbusiness.com/affiliates | Direkt / CJ | $100 CPA | 60 gün | 3-7 gün |
| 4 | CompleteCase | completecase.com/affiliates | Direkt / FlexOffers | $60-$90/satış | 45 gün | 3-7 gün |
| 5 | Northwest | northwestregisteredagent.com/affiliates | Direkt | $60 CPA | 90 gün | 3-7 gün |
| 6 | Rocket Lawyer | FlexOffers'da ara | FlexOffers | $20-$70/dönüşüm | 30 gün | 5-10 gün |
| 7 | LegalZoom | CJ Affiliate'de ara | CJ Affiliate | Değişken CPA | 45 gün | 7-14 gün |

**ÖNEMLİ:** Her program onaylandığında, o programa ait affiliate linkini hemen ThirstyAffiliates'e ekle.

### 2.2 ThirstyAffiliates Kurulumu

**Plugin Kurulumu:**
1. WordPress Dashboard → Plugins → Add New → "ThirstyAffiliates" ara → Install → Activate

**Genel Ayarlar:**
- Settings → ThirstyAffiliates → General:
  - Link Prefix: `recommend` (URL'ler: clearlegaltips.com/recommend/lawdepot-nda)
  - Link Appearance: "Pretty Links" aktif
  - No Follow: ON (tüm affiliate linkler)
  - Open in New Tab: ON
  - Click Tracking: ON (bu tıklama verisi GA4'e bağlanır)

**Kategori Yapısı:**
ThirstyAffiliates → Categories:
```
├── Legal Templates (LawDepot linkleri)
├── Business Formation (ZenBusiness, Northwest linkleri)
├── Divorce & Family (CompleteCase linkleri)
├── Legal Services (LegalZoom, Rocket Lawyer linkleri)
└── Other Affiliates (Termly, Avail vs.)
```

### 2.3 ThirstyAffiliates Link Oluşturma

Her affiliate ortağı için şu linkleri oluştur:

#### LawDepot Linkleri
| ThirstyAffiliates İsim | Slug | Hedef URL (affiliate linkinle) |
|------------------------|------|-------------------------------|
| LawDepot NDA Template | /recommend/lawdepot-nda | [senin LawDepot affiliate linkin + NDA parametresi] |
| LawDepot LLC Operating Agreement | /recommend/lawdepot-llc-operating | [affiliate link] |
| LawDepot Commercial Lease | /recommend/lawdepot-commercial-lease | [affiliate link] |
| LawDepot Residential Lease | /recommend/lawdepot-residential-lease | [affiliate link] |
| LawDepot Bill of Sale | /recommend/lawdepot-bill-of-sale | [affiliate link] |
| LawDepot Promissory Note | /recommend/lawdepot-promissory-note | [affiliate link] |
| LawDepot Last Will | /recommend/lawdepot-will | [affiliate link] |
| LawDepot Living Trust | /recommend/lawdepot-living-trust | [affiliate link] |
| LawDepot Power of Attorney | /recommend/lawdepot-poa | [affiliate link] |
| LawDepot Medical POA | /recommend/lawdepot-medical-poa | [affiliate link] |
| LawDepot Eviction Notice | /recommend/lawdepot-eviction | [affiliate link] |
| LawDepot Sublease Agreement | /recommend/lawdepot-sublease | [affiliate link] |
| LawDepot Service Agreement | /recommend/lawdepot-service-agreement | [affiliate link] |
| LawDepot Joint Venture | /recommend/lawdepot-joint-venture | [affiliate link] |
| LawDepot Partnership Agreement | /recommend/lawdepot-partnership | [affiliate link] |
| LawDepot Consulting Agreement | /recommend/lawdepot-consulting | [affiliate link] |
| LawDepot Quitclaim Deed | /recommend/lawdepot-quitclaim | [affiliate link] |

#### ZenBusiness Linkleri
| ThirstyAffiliates İsim | Slug |
|------------------------|------|
| ZenBusiness LLC Formation | /recommend/zenbusiness-llc |
| ZenBusiness S-Corp Election | /recommend/zenbusiness-scorp |
| ZenBusiness Registered Agent | /recommend/zenbusiness-registered-agent |
| ZenBusiness Annual Report Filing | /recommend/zenbusiness-annual-report |
| ZenBusiness Foreign Qualification | /recommend/zenbusiness-foreign-qualification |
| ZenBusiness LLC Dissolution | /recommend/zenbusiness-dissolution |

#### CompleteCase Linkleri
| ThirstyAffiliates İsim | Slug |
|------------------------|------|
| CompleteCase Online Divorce | /recommend/completecase-divorce |

#### LegalZoom Linkleri
| ThirstyAffiliates İsim | Slug |
|------------------------|------|
| LegalZoom DBA Filing | /recommend/legalzoom-dba |
| LegalZoom EIN Filing | /recommend/legalzoom-ein |
| LegalZoom Trademark Filing | /recommend/legalzoom-trademark |
| LegalZoom Business License | /recommend/legalzoom-business-license |
| LegalZoom Estate Planning | /recommend/legalzoom-estate-planning |
| LegalZoom Name Change | /recommend/legalzoom-name-change |
| LegalZoom Copyright Filing | /recommend/legalzoom-copyright |

#### Rocket Lawyer Linkleri
| ThirstyAffiliates İsim | Slug |
|------------------------|------|
| Rocket Lawyer Prenuptial Agreement | /recommend/rocket-lawyer-prenup |
| Rocket Lawyer Child Custody Agreement | /recommend/rocket-lawyer-custody |
| Rocket Lawyer Legal Documents | /recommend/rocket-lawyer-documents |
| Rocket Lawyer Eviction Notice | /recommend/rocket-lawyer-eviction |
| Rocket Lawyer Residential Lease | /recommend/rocket-lawyer-lease |

#### Northwest Linkleri
| ThirstyAffiliates İsim | Slug |
|------------------------|------|
| Northwest Registered Agent | /recommend/northwest-registered-agent |

### 2.4 Makalelerde [THIRSTY:] Değiştirme

Makalelerde `[THIRSTY: LawDepot NDA Template]` gibi yer tutucular var. WordPress'e yapıştırdıktan sonra:

1. Ctrl+F ile `[THIRSTY:` ara
2. Her birini ThirstyAffiliates kısa koduyla değiştir
3. Format: Bir buton veya belirgin CTA kutusu olarak stilize et

**WordPress'te değiştirme formatı:**
```
[THIRSTY: LawDepot NDA Template]
↓ Bu şekle dönüştür: ↓
[thirstylink ids="XX" linktext="Download Free NDA Template" class="cta-button"]
```

VEYA metin linki olarak:
```
<a href="/recommend/lawdepot-nda" target="_blank" rel="nofollow">Download your free NDA template here →</a>
```

**İPUCU:** İlk birkaç makaleyi yayınladıktan sonra, WordPress Reusable Block oluştur. "CTA - LawDepot NDA" gibi. Sonraki makalelerde blok ekleyerek hızlandır.

---

## 3. MAKALE BAZLI AFFILIATE LINK HARİTASI

### Küme 1: Yasal Şablonlar (Makale 1-20)

| # | Makale | [THIRSTY:] Yer Tutucusu | ThirstyAffiliates Slug | Adet |
|:-:|--------|-------------------------|----------------------|:----:|
| 1 | Free NDA Template | LawDepot NDA Template | /recommend/lawdepot-nda | 4 |
| 2 | Independent Contractor Agreement | LawDepot Contractor Agreement | /recommend/lawdepot-contractor | 4 |
| 3 | LLC Operating Agreement | LawDepot LLC Operating Agreement | /recommend/lawdepot-llc-operating | 4 |
| 4 | Commercial Lease Agreement | LawDepot Commercial Lease | /recommend/lawdepot-commercial-lease | 4 |
| 5 | Residential Lease Agreement | LawDepot Residential Lease | /recommend/lawdepot-residential-lease | 4 |
| 6 | Bill of Sale Template | LawDepot Bill of Sale | /recommend/lawdepot-bill-of-sale | 4 |
| 7 | Promissory Note Template | LawDepot Promissory Note | /recommend/lawdepot-promissory-note | 4 |
| 8 | Last Will and Testament | LawDepot Last Will | /recommend/lawdepot-will | 4 |
| 9 | Living Trust Template | LawDepot Living Trust | /recommend/lawdepot-living-trust | 4 |
| 10 | General Power of Attorney | LawDepot Power of Attorney | /recommend/lawdepot-poa | 4 |
| 11 | Medical Power of Attorney | LawDepot Medical POA | /recommend/lawdepot-medical-poa | 4 |
| 12 | Prenuptial Agreement | Rocket Lawyer Prenuptial Agreement | /recommend/rocket-lawyer-prenup | 4 |
| 13 | Eviction Notice Template | LawDepot Eviction Notice | /recommend/lawdepot-eviction | 4 |
| 14 | Sublease Agreement | LawDepot Sublease Agreement | /recommend/lawdepot-sublease | 4 |
| 15 | Service Agreement | LawDepot Service Agreement | /recommend/lawdepot-service-agreement | 4 |
| 16 | Joint Venture Agreement | LawDepot Joint Venture | /recommend/lawdepot-joint-venture | 4 |
| 17 | Partnership Agreement | LawDepot Partnership Agreement | /recommend/lawdepot-partnership | 4 |
| 18 | Child Custody Agreement | Rocket Lawyer Child Custody Agreement | /recommend/rocket-lawyer-custody | 4 |
| 19 | Consulting Agreement | LawDepot Consulting Agreement | /recommend/lawdepot-consulting | 4 |
| 20 | Quitclaim Deed | LawDepot Quitclaim Deed | /recommend/lawdepot-quitclaim | 4 |

### Küme 2: Hesaplayıcılar & Maliyet Tabloları (Makale 21-35)

| # | Makale | [THIRSTY:] Yer Tutucusu | ThirstyAffiliates Slug | Adet |
|:-:|--------|-------------------------|----------------------|:----:|
| 21 | LLC Formation Cost | ZenBusiness LLC Formation | /recommend/zenbusiness-llc | 4 |
| 22 | S-Corp vs LLC Calculator | ZenBusiness S-Corp Election | /recommend/zenbusiness-scorp | 4 |
| 23 | Registered Agent Comparison | ZenBusiness Registered Agent | /recommend/zenbusiness-registered-agent | 3 |
| 24 | DBA Filing Fees | LegalZoom DBA Filing | /recommend/legalzoom-dba | 3 |
| 25 | EIN Application Guide | LegalZoom EIN Filing | /recommend/legalzoom-ein | 3 |
| 26 | Annual Report Fees | ZenBusiness Annual Report Filing | /recommend/zenbusiness-annual-report | 3 |
| 27 | Business License Cost | LegalZoom Business License | /recommend/legalzoom-business-license | 3 |
| 28 | Foreign Qualification Cost | ZenBusiness Foreign Qualification | /recommend/zenbusiness-foreign-qualification | 3 |
| 29 | Trademark Filing Cost | LegalZoom Trademark Filing | /recommend/legalzoom-trademark | 4 |
| 30 | Estate Tax Calculator | LawDepot Living Trust | /recommend/lawdepot-living-trust | 3 |
| 31 | Probate Cost Estimator | LegalZoom Estate Planning | /recommend/legalzoom-estate-planning | 3 |
| 32 | Living Trust vs Will Cost | LawDepot Living Trust | /recommend/lawdepot-living-trust | 4 |
| 33 | Divorce Cost Calculator | CompleteCase Online Divorce | /recommend/completecase-divorce | 4 |
| 34 | Child Support Calculators | CompleteCase Online Divorce | /recommend/completecase-divorce | 2 |
| 35 | Small Claims Court Fees | Rocket Lawyer Legal Documents | /recommend/rocket-lawyer-documents | 2 |

### Küme 3: Çevrimiçi Hizmetler (Makale 36-50)

| # | Makale | [THIRSTY:] Yer Tutucusu | ThirstyAffiliates Slug | Adet |
|:-:|--------|-------------------------|----------------------|:----:|
| 36 | How to Form LLC Online | ZenBusiness LLC Formation | /recommend/zenbusiness-llc | 5 |
| 37 | How to File EIN Online | LegalZoom EIN Filing | /recommend/legalzoom-ein | 2 |
| 38 | Registered Agent Online | ZenBusiness Registered Agent | /recommend/zenbusiness-registered-agent | 3 |
| 39 | Uncontested Divorce Online | CompleteCase Online Divorce | /recommend/completecase-divorce | 4 |
| 40 | CompleteCase Review | CompleteCase Online Divorce | /recommend/completecase-divorce | 4 |
| 41 | Name Change Online | LegalZoom Name Change | /recommend/legalzoom-name-change | 2 |
| 42 | Create Living Trust Online | LawDepot Living Trust | /recommend/lawdepot-living-trust | 3 |
| 43 | File Trademark Online | LegalZoom Trademark Filing | /recommend/legalzoom-trademark | 3 |
| 44 | Register DBA Online | LegalZoom DBA Filing | /recommend/legalzoom-dba | 3 |
| 45 | Legal Separation Online | CompleteCase Online Divorce | /recommend/completecase-divorce | 3 |
| 46 | Online Divorce TX/CA/FL | CompleteCase Online Divorce | /recommend/completecase-divorce | 4 |
| 47 | Dissolve LLC Online | ZenBusiness LLC Dissolution | /recommend/zenbusiness-dissolution | 3 |
| 48 | Copyright Registration | LegalZoom Copyright Filing | /recommend/legalzoom-copyright | 3 |
| 49 | Small Claims Evictions | Rocket Lawyer Eviction Notice | /recommend/rocket-lawyer-eviction | 3 |
| 50 | Landlord Tenant Account | Rocket Lawyer Residential Lease | /recommend/rocket-lawyer-lease | 3 |

---

## 4. GÖRSEL KAYNAKLARI (MAKALE BAZLI)

### 4.1 Genel Kurallar
- **Kaynak:** Unsplash.com ve Pexels.com (tamamen ücretsiz, ticari kullanıma uygun)
- **Format:** Her makale için 1 Featured Image (1200x630px önerilir — sosyal medya paylaşımına uygun)
- **Araç:** Canva Free ile görselin üzerine makale başlığı + ClearLegalTips.com logosu ekle
- **Dosya boyutu:** ShortPixel plugin ile otomatik sıkıştırma (WebP dönüşümü aktif)
- **Alt text:** Her görsele SEO uyumlu alt text yaz (aşağıda makale bazlı verildi)

### 4.2 Makale Bazlı Görsel Arama Terimleri & Alt Text

#### Küme 1: Yasal Şablonlar (Makale 1-20)

| # | Makale | Unsplash/Pexels Arama Terimi | Alt Text |
|:-:|--------|-----------------------------:|----------|
| 1 | NDA Template | "signing contract", "business agreement handshake" | Free NDA template download for business confidentiality agreements |
| 2 | Independent Contractor Agreement | "freelancer working laptop", "contractor meeting" | Independent contractor agreement template for freelancers and businesses |
| 3 | LLC Operating Agreement | "business partners meeting", "startup team office" | LLC operating agreement template for single and multi-member companies |
| 4 | Commercial Lease Agreement | "commercial building office", "storefront lease" | Commercial lease agreement template for retail and office spaces |
| 5 | Residential Lease Agreement | "apartment building", "house keys handover" | Residential lease agreement template for landlords and tenants |
| 6 | Bill of Sale | "car sale handshake", "vehicle purchase" | Free bill of sale template for car boat and personal property |
| 7 | Promissory Note | "loan agreement signing", "money lending document" | Promissory note template for secured and unsecured loans |
| 8 | Last Will and Testament | "family estate planning", "legal document pen" | Free last will and testament template printable PDF |
| 9 | Living Trust | "estate planning family", "trust document signing" | Living trust template revocable trust download and fill out |
| 10 | Power of Attorney | "legal authority document", "signing power of attorney" | General power of attorney form financial free download |
| 11 | Medical POA | "healthcare directive", "medical decision making" | Medical power of attorney and healthcare directive template |
| 12 | Prenuptial Agreement | "couple wedding planning", "marriage preparation" | Prenuptial agreement template downloadable PDF |
| 13 | Eviction Notice | "apartment door notice", "rental property" | Free eviction notice template 3-day 14-day 30-day |
| 14 | Sublease Agreement | "apartment subletting", "roommate agreement" | Sublease agreement template legal and printable |
| 15 | Service Agreement | "freelancer client handshake", "service contract" | Service agreement template for freelancers and contractors |
| 16 | Joint Venture Agreement | "business partnership handshake", "joint venture meeting" | Joint venture agreement template downloadable Word document |
| 17 | Partnership Agreement | "business partners signing", "partnership formation" | Partnership agreement template general and limited PDF |
| 18 | Child Custody Agreement | "parent child family", "co-parenting" | Child custody agreement template co-parenting fillable form |
| 19 | Consulting Agreement | "consultant client meeting", "professional consultation" | Consulting agreement template hourly and retainer download |
| 20 | Quitclaim Deed | "house property transfer", "real estate deed" | Free quitclaim deed form by state printable PDF |

#### Küme 2: Hesaplayıcılar (Makale 21-35)

| # | Makale | Unsplash/Pexels Arama Terimi | Alt Text |
|:-:|--------|-----------------------------:|----------|
| 21 | LLC Formation Cost | "business formation startup", "calculator tax documents" | LLC formation cost calculator by state 2026 exact fees |
| 22 | S-Corp vs LLC Calculator | "tax calculation business", "financial comparison" | S-Corp vs LLC tax calculator which saves you more |
| 23 | Registered Agent Comparison | "registered agent service", "business mailbox" | Registered agent cost comparison all 50 states 2026 |
| 24 | DBA Filing Fees | "business name registration", "doing business as sign" | DBA filing fees by state complete table 2026 |
| 25 | EIN Application Guide | "IRS tax form", "business tax identification" | EIN application free IRS guide vs paid services cost |
| 26 | Annual Report Fees | "annual business filing", "compliance deadline calendar" | Annual report filing fees and deadlines all 50 states |
| 27 | Business License Cost | "business license certificate", "store opening" | Business license cost estimator by industry and state |
| 28 | Foreign Qualification Cost | "multi-state business", "expanding business map" | Foreign qualification cost calculator expanding LLC another state |
| 29 | Trademark Filing Cost | "trademark registration symbol", "brand protection" | Trademark filing cost calculator USPTO fees vs attorney |
| 30 | Estate Tax Calculator | "estate planning documents", "inheritance tax" | Estate tax threshold calculator 2026 federal and state |
| 31 | Probate Cost Estimator | "probate court documents", "estate administration" | Probate cost estimator by state court fees executor percentage |
| 32 | Living Trust vs Will Cost | "estate planning comparison", "trust vs will documents" | Living trust vs will cost breakdown DIY vs attorney 2026 |
| 33 | Divorce Cost Calculator | "divorce papers cost", "family law documents" | Divorce cost calculator by state filing to finalization |
| 34 | Child Support Calculators | "child support calculation", "family court" | Child support calculators by state links and guidelines |
| 35 | Small Claims Court Fees | "small claims court", "courthouse filing" | Small claims court filing limits and fees all 50 states |

#### Küme 3: Çevrimiçi Hizmetler (Makale 36-50)

| # | Makale | Unsplash/Pexels Arama Terimi | Alt Text |
|:-:|--------|-----------------------------:|----------|
| 36 | Form LLC Online | "online business registration", "laptop business formation" | How to form an LLC online in 10 minutes step by step |
| 37 | File EIN Online | "IRS online filing", "tax ID application" | How to file for an EIN online IRS direct vs third party |
| 38 | Registered Agent Online | "registered agent setup", "business compliance" | How to get a registered agent online instant setup guide |
| 39 | Uncontested Divorce Online | "divorce papers online", "uncontested divorce filing" | How to file for uncontested divorce online without attorney |
| 40 | CompleteCase Review | "online divorce service", "document preparation" | CompleteCase review 2026 is online divorce worth it |
| 41 | Name Change Online | "legal name change", "court document filing" | How to file a name change online adult and minor guide |
| 42 | Create Living Trust Online | "online trust creation", "estate planning laptop" | How to create a living trust online best services compared |
| 43 | File Trademark Online | "trademark application", "USPTO filing" | How to file a trademark online USPTO step by step |
| 44 | Register DBA Online | "business name filing", "DBA registration" | How to register a DBA online state by state portal links |
| 45 | Legal Separation Online | "legal separation documents", "marriage separation" | How to file for legal separation online process and cost |
| 46 | Online Divorce TX/CA/FL | "state divorce filing", "courthouse online" | Online divorce Texas California Florida state specific guide |
| 47 | Dissolve LLC Online | "closing business", "LLC dissolution filing" | How to dissolve an LLC online step by step withdrawal |
| 48 | Copyright Registration | "copyright symbol", "intellectual property registration" | How to apply for a copyright online USCO registration guide |
| 49 | Small Claims Evictions | "eviction notice door", "landlord tenant court" | How to handle small claims evictions online legal process |
| 50 | Landlord Tenant Account | "online rent collection", "property management app" | How to set up landlord tenant account online rent collection |

### 4.3 Canva Featured Image Şablonu

**Boyut:** 1200 x 630 px (Facebook/LinkedIn paylaşım boyutu)
**Tasarım:**
```
┌─────────────────────────────────────────┐
│                                         │
│  [Arka plan: stok fotoğraf, hafif blur] │
│                                         │
│  ┌─────────────────────────────────┐    │
│  │  MAKALE BAŞLIĞI                 │    │
│  │  (Beyaz text, bold, gölgeli)    │    │
│  └─────────────────────────────────┘    │
│                                         │
│  ClearLegalTips.com          [2026]     │
│                                         │
└─────────────────────────────────────────┘
```

**Canva'da bir kez şablon oluştur, sonra her makale için:**
1. Arka plan fotoğrafını değiştir
2. Başlık metnini güncelle
3. PNG olarak indir → WordPress'e yükle

---

## 5. INTERNAL LINK STRATEJİSİ

### 5.1 Hub-and-Spoke Modeli

**Hub Makaleleri (Her kümede 1 kapsamlı rehber):**
- Küme 1 Hub: Makale 1 (NDA Template) — en yüksek arama hacmi
- Küme 2 Hub: Makale 21 (LLC Formation Cost) — en yüksek ticari niyet
- Küme 3 Hub: Makale 36 (How to Form LLC Online) — en yüksek dönüşüm potansiyeli

### 5.2 Makale Bazlı Internal Link Haritası

Her makaleye minimum 3 internal link eklenmeli. Aşağıda her makale için önerilen linkler:

| # | Makale | Linki verilecek makaleler (minimum 3) |
|:-:|--------|--------------------------------------|
| 1 | NDA Template | → #2 (Contractor), → #15 (Service Agreement), → #19 (Consulting) |
| 2 | Contractor Agreement | → #1 (NDA), → #15 (Service Agreement), → #19 (Consulting) |
| 3 | LLC Operating Agreement | → #21 (LLC Cost), → #36 (Form LLC Online), → #23 (Registered Agent) |
| 4 | Commercial Lease | → #5 (Residential Lease), → #27 (Business License), → #14 (Sublease) |
| 5 | Residential Lease | → #4 (Commercial Lease), → #13 (Eviction), → #50 (Landlord Account) |
| 6 | Bill of Sale | → #7 (Promissory Note), → #1 (NDA), → #35 (Small Claims) |
| 7 | Promissory Note | → #6 (Bill of Sale), → #15 (Service Agreement), → #35 (Small Claims) |
| 8 | Last Will and Testament | → #9 (Living Trust), → #10 (POA), → #32 (Trust vs Will Cost) |
| 9 | Living Trust | → #8 (Will), → #42 (Create Trust Online), → #30 (Estate Tax) |
| 10 | Power of Attorney | → #11 (Medical POA), → #8 (Will), → #9 (Living Trust) |
| 11 | Medical POA | → #10 (POA), → #8 (Will), → #9 (Living Trust) |
| 12 | Prenuptial Agreement | → #33 (Divorce Cost), → #39 (Uncontested Divorce), → #8 (Will) |
| 13 | Eviction Notice | → #5 (Residential Lease), → #49 (Evictions Online), → #35 (Small Claims) |
| 14 | Sublease Agreement | → #5 (Residential Lease), → #4 (Commercial Lease), → #13 (Eviction) |
| 15 | Service Agreement | → #2 (Contractor), → #19 (Consulting), → #1 (NDA) |
| 16 | Joint Venture Agreement | → #17 (Partnership), → #3 (LLC Operating), → #1 (NDA) |
| 17 | Partnership Agreement | → #16 (Joint Venture), → #3 (LLC Operating), → #21 (LLC Cost) |
| 18 | Child Custody Agreement | → #34 (Child Support), → #33 (Divorce Cost), → #39 (Uncontested Divorce) |
| 19 | Consulting Agreement | → #2 (Contractor), → #15 (Service Agreement), → #1 (NDA) |
| 20 | Quitclaim Deed | → #9 (Living Trust), → #33 (Divorce Cost), → #5 (Residential Lease) |
| 21 | LLC Formation Cost | → #36 (Form LLC Online), → #22 (S-Corp Calculator), → #23 (Registered Agent) |
| 22 | S-Corp vs LLC Calculator | → #21 (LLC Cost), → #36 (Form LLC Online), → #25 (EIN Guide) |
| 23 | Registered Agent Comparison | → #38 (Registered Agent Online), → #21 (LLC Cost), → #26 (Annual Report) |
| 24 | DBA Filing Fees | → #44 (Register DBA Online), → #21 (LLC Cost), → #27 (Business License) |
| 25 | EIN Application Guide | → #37 (File EIN Online), → #21 (LLC Cost), → #36 (Form LLC Online) |
| 26 | Annual Report Fees | → #21 (LLC Cost), → #23 (Registered Agent), → #47 (Dissolve LLC) |
| 27 | Business License Cost | → #21 (LLC Cost), → #24 (DBA Fees), → #36 (Form LLC Online) |
| 28 | Foreign Qualification Cost | → #21 (LLC Cost), → #23 (Registered Agent), → #26 (Annual Report) |
| 29 | Trademark Filing Cost | → #43 (File Trademark Online), → #48 (Copyright), → #21 (LLC Cost) |
| 30 | Estate Tax Calculator | → #31 (Probate Cost), → #9 (Living Trust), → #32 (Trust vs Will Cost) |
| 31 | Probate Cost Estimator | → #30 (Estate Tax), → #32 (Trust vs Will), → #9 (Living Trust) |
| 32 | Living Trust vs Will Cost | → #9 (Living Trust), → #8 (Will), → #42 (Create Trust Online) |
| 33 | Divorce Cost Calculator | → #39 (Uncontested Divorce), → #40 (CompleteCase Review), → #34 (Child Support) |
| 34 | Child Support Calculators | → #33 (Divorce Cost), → #18 (Child Custody), → #39 (Uncontested Divorce) |
| 35 | Small Claims Court Fees | → #13 (Eviction), → #49 (Evictions Online), → #6 (Bill of Sale) |
| 36 | Form LLC Online | → #21 (LLC Cost), → #23 (Registered Agent), → #25 (EIN Guide) |
| 37 | File EIN Online | → #25 (EIN Application), → #36 (Form LLC Online), → #21 (LLC Cost) |
| 38 | Registered Agent Online | → #23 (Registered Agent Comparison), → #36 (Form LLC Online), → #21 (LLC Cost) |
| 39 | Uncontested Divorce Online | → #40 (CompleteCase Review), → #33 (Divorce Cost), → #46 (Divorce TX/CA/FL) |
| 40 | CompleteCase Review | → #39 (Uncontested Divorce), → #33 (Divorce Cost), → #45 (Legal Separation) |
| 41 | Name Change Online | → #39 (Uncontested Divorce), → #33 (Divorce Cost), → #35 (Small Claims) |
| 42 | Create Living Trust Online | → #9 (Living Trust), → #32 (Trust vs Will), → #30 (Estate Tax) |
| 43 | File Trademark Online | → #29 (Trademark Cost), → #48 (Copyright), → #24 (DBA Fees) |
| 44 | Register DBA Online | → #24 (DBA Filing Fees), → #21 (LLC Cost), → #36 (Form LLC Online) |
| 45 | Legal Separation Online | → #39 (Uncontested Divorce), → #33 (Divorce Cost), → #40 (CompleteCase Review) |
| 46 | Online Divorce TX/CA/FL | → #39 (Uncontested Divorce), → #40 (CompleteCase Review), → #33 (Divorce Cost) |
| 47 | Dissolve LLC Online | → #21 (LLC Cost), → #26 (Annual Report), → #36 (Form LLC Online) |
| 48 | Copyright Registration | → #29 (Trademark Cost), → #43 (File Trademark), → #1 (NDA) |
| 49 | Small Claims Evictions | → #13 (Eviction Notice), → #5 (Residential Lease), → #35 (Small Claims Fees) |
| 50 | Landlord Tenant Account | → #5 (Residential Lease), → #13 (Eviction), → #49 (Evictions Online) |

**WordPress'te uygulama:** Internal linkleri makalenin doğal akışına yerleştir — zorlama anchor text kullanma. Örnek:
```
"Before filing your LLC, check our complete LLC formation cost breakdown by state."
→ "LLC formation cost breakdown by state" ifadesi Makale 21'e link olur.
```

---

## 6. SEO KONTROL LİSTESİ (HER MAKALE İÇİN)

Her makaleyi yayınlamadan önce bu listeyi kontrol et:

### On-Page SEO
- [ ] H1'de focus keyword var (doğal şekilde)
- [ ] H1 60 karakterden kısa
- [ ] Meta description 150-160 karakter, focus keyword içeriyor
- [ ] URL slug kısa ve keyword içeriyor (ör: /free-nda-template-2026)
- [ ] Focus keyword ilk 100 kelimede geçiyor
- [ ] Focus keyword H2 alt başlıklardan en az 1'inde var
- [ ] Focus keyword toplam içerikte 3-7 kez geçiyor (zorlamadan)
- [ ] En az 1 görsel, keyword içeren alt text ile
- [ ] Minimum 3 internal link (farklı makalelere)
- [ ] Minimum 1 external link (güvenilir kaynak: .gov, .edu, resmi site)

### Teknik SEO
- [ ] Rank Math SEO skoru 80+ (yeşil)
- [ ] Rank Math readability skoru "Good" veya üzeri
- [ ] Featured image yüklendi (1200x630px)
- [ ] Featured image dosya adı keyword içeriyor (ör: free-nda-template.png)
- [ ] Tüm görseller ShortPixel ile sıkıştırılmış
- [ ] Kırık link yok (internal veya external)

### İçerik Kalitesi
- [ ] Minimum 1,500 kelime (tercihan 2,500+)
- [ ] En az 1 tablo veya karşılaştırma matrisi var
- [ ] FAQ bölümü var (en az 4 soru)
- [ ] Makale sonu disclaimer mevcut
- [ ] FTC disclosure makale başında, ilk affiliate linkinin üstünde
- [ ] "Last reviewed: May 2026" notu var

### Schema Markup (Rank Math otomatik)
- [ ] Article schema aktif
- [ ] FAQ schema aktif (FAQ bölümü için)
- [ ] Author schema aktif (yazar profili bağlı)
- [ ] HowTo schema (adım-adım makaleler için — Rank Math'te manuel ekle)

---

## 7. RANK MATH AYARLARI

### Her Makale İçin Rank Math SEO Kutusu

WordPress editöründe, sağ paneldeki Rank Math kutusunu doldur:

**Focus Keyword:** Makale başındaki metadata'daki "Focus Keyword" değerini gir
**SEO Title:** `{title} | ClearLegalTips.com` (Rank Math şablonu kullan)
**Meta Description:** Her makale için özel yazılmış 150-160 karakter açıklama

### Makale Bazlı Rank Math Verileri

| # | Focus Keyword | Önerilen Meta Description |
|:-:|--------------|--------------------------|
| 1 | free NDA template | Download a free NDA template in Word and PDF. Fill-in-the-blank format with mutual and unilateral options. Updated for 2026. |
| 2 | independent contractor agreement template | Free independent contractor agreement template. Covers payment, IP, termination, and IRS compliance. Word and PDF download. |
| 3 | LLC operating agreement template | Download a free LLC operating agreement for single or multi-member LLCs. State-compliant template with profit allocation and management terms. |
| 4 | commercial lease agreement template | Free commercial lease agreement template for retail, office, and industrial spaces. Covers NNN, gross, and modified gross lease structures. |
| 5 | residential lease agreement template | State-specific residential lease template. Covers rent, security deposit, maintenance, and termination. Free PDF download for landlords. |
| 6 | free bill of sale template | Free bill of sale template for car, boat, and personal property. Printable PDF with state-specific requirements. Updated 2026. |
| 7 | promissory note template | Download a free promissory note template. Secured and unsecured options with amortization schedule. Word and PDF format. |
| 8 | free last will and testament template | Free last will and testament template. Printable PDF with executor nomination, beneficiary designation, and guardian appointment. |
| 9 | living trust template | Free revocable living trust template. Avoid probate with this fill-out trust document. Includes pour-over will and funding checklist. |
| 10 | power of attorney form | Free general power of attorney form for financial decisions. Durable and springing options. State-specific requirements included. |
| 11 | medical power of attorney template | Free medical power of attorney and healthcare directive template. Name your healthcare agent and document end-of-life wishes. |
| 12 | prenuptial agreement template | Download a prenuptial agreement template. Covers asset protection, debt allocation, and spousal support. State enforceability guide included. |
| 13 | free eviction notice template | Free eviction notice templates: 3-day, 14-day, and 30-day. State-specific forms with proper legal language. Printable PDF. |
| 14 | sublease agreement template | Free sublease agreement template. Legal and printable with landlord consent, rent terms, and liability allocation. |
| 15 | service agreement template | Free service agreement template for freelancers and contractors. Covers scope, payment, IP rights, and termination. Word download. |
| 16 | joint venture agreement template | Free joint venture agreement template. Covers profit sharing, management, IP, and exit strategy. Downloadable Word document. |
| 17 | partnership agreement template | Free partnership agreement template for general and limited partnerships. Covers capital, profits, management, and dissolution. |
| 18 | child custody agreement template | Free child custody agreement template. Co-parenting plan with visitation schedules, holiday rotation, and decision-making provisions. |
| 19 | consulting agreement template | Free consulting agreement template. Hourly and retainer options with SOW, IP assignment, and non-compete provisions. |
| 20 | quitclaim deed form | Free quitclaim deed form by state. Printable PDF for property transfers between family, divorce, and trust funding. |
| 21 | LLC formation cost by state | LLC formation cost calculator with exact 2026 state fees for all 50 states. Compare DIY vs service vs attorney costs. |
| 22 | S-Corp vs LLC tax calculator | S-Corp vs LLC tax comparison calculator. See how much you could save in self-employment tax at every income level. |
| 23 | registered agent cost comparison | Compare registered agent costs across 10 top services. Pricing, features, and reviews for all 50 states. 2026 data. |
| 24 | DBA filing fees by state | Complete DBA filing fee table for all 50 states. Includes publication requirements and online filing availability. |
| 25 | EIN application guide | Free EIN application guide. Compare IRS direct filing (free) vs paid services. Step-by-step process with common mistakes. |
| 26 | annual report filing fees | Annual report fees and deadlines for all 50 states. LLC and corporation requirements with due dates and late penalties. |
| 27 | business license cost | Business license costs by industry and state. Federal, state, and local requirements with fee tables and application steps. |
| 28 | foreign qualification cost | Foreign qualification fees for all 50 states. Calculate the cost of expanding your LLC to another state. |
| 29 | trademark filing cost | Trademark filing cost breakdown: USPTO fees, attorney costs, and online service pricing compared. 10-year ownership cost included. |
| 30 | estate tax calculator | Estate tax calculator for 2026. Federal exemption, state thresholds, and inheritance tax rates. Includes TCJA sunset analysis. |
| 31 | probate cost estimator | Probate costs by state with filing fees, attorney fees, and executor compensation. Compare avoidance strategies and savings. |
| 32 | living trust vs will cost | Living trust vs will cost comparison. Break-even analysis shows when a trust saves money. DIY and attorney pricing for 2026. |
| 33 | divorce cost calculator | Divorce cost calculator by state. Filing fees, attorney costs, and total expenses from filing to finalization. |
| 34 | child support calculator by state | Child support calculators for all 50 states. Links to official calculators, guidelines, and modification procedures. |
| 35 | small claims court fees | Small claims court limits and fees for all 50 states. Filing requirements, attorney rules, and step-by-step process guide. |
| 36 | how to form an LLC online | Form your LLC online in 10 minutes. Step-by-step guide with formation service comparison and state processing times. |
| 37 | how to file for an EIN online | File for an EIN online free through IRS.gov. Step-by-step guide vs paid services. Get your EIN in minutes. |
| 38 | how to get a registered agent online | Set up a registered agent online in 3 steps. Service comparison with pricing and features for all 50 states. |
| 39 | file for uncontested divorce online | File for uncontested divorce online without an attorney. Step-by-step process, service comparison, and state-specific costs. |
| 40 | CompleteCase review | CompleteCase review 2026: Is the $299 online divorce service worth it? Pros, cons, alternatives, and real user feedback. |
| 41 | how to file a name change online | File a legal name change online. Adult and minor process guide with state costs, court requirements, and document updates. |
| 42 | create living trust online | Create a living trust online. Compare top services, step-by-step process, and cost savings vs attorney. 2026 guide. |
| 43 | how to file a trademark online | File a trademark online at the USPTO. Step-by-step application guide with costs, timeline, and common mistakes to avoid. |
| 44 | how to register a DBA online | Register a DBA online with state-by-state portal links. Filing fees, publication requirements, and service comparison. |
| 45 | how to file for legal separation online | File for legal separation online. Process, cost comparison, and key differences from divorce. State-by-state guide. |
| 46 | online divorce Texas California Florida | Online divorce guide for Texas, California, and Florida. State-specific costs, timelines, and step-by-step filing process. |
| 47 | how to dissolve an LLC online | Dissolve your LLC online step by step. State filing fees, final tax requirements, and common dissolution mistakes to avoid. |
| 48 | how to apply for a copyright online | Apply for a copyright online at the US Copyright Office. $35-$85 registration guide with deposit requirements and timeline. |
| 49 | how to handle small claims evictions online | Small claims eviction process guide. State-by-state notice requirements, court filing, and timeline from notice to removal. |
| 50 | how to set up landlord tenant account online | Set up online rent collection in 15 minutes. Compare free platforms, payment methods, and landlord management features. |

---

## 8. YAZAR ATAMALARI

WordPress'te her makaleyi yayınlarken doğru yazarı seç:

| Yazar | WordPress Kullanıcı Adı | Atanan Makaleler |
|-------|------------------------|-----------------|
| **David Miller** | david-miller | #1, #2, #6, #7, #14, #16, #35, #41, #48 |
| **Sarah Jenkins** | sarah-jenkins | #3, #4, #15, #17, #19, #21, #22, #23, #24, #25, #26, #27, #28, #29, #36, #37, #38, #43, #44, #47 |
| **Marcus Thorne** | marcus-thorne | #8, #9, #10, #11, #12, #18, #30, #31, #32, #33, #34, #39, #40, #42, #45, #46 |
| **Elena Rodriguez** | elena-rodriguez | #5, #13, #20, #49, #50 |

**Her yazarın WordPress profilinde bulunması gerekenler:**
- Biyografi metni (legal_editors_templates.md dosyasından)
- Profil fotoğrafı (Unsplash'ten profesyonel görünüm)
- LinkedIn URL'si (en azından David Miller için)
- Rank Math Person Schema (Job Title, Organization, knowsAbout)

---

## 9. WORDPRESS KATEGORİ VE ETİKET YAPISI

### Kategoriler (Ana menüde gösterilecek)

```
├── Legal Templates          → Makale 1-20
├── Business Calculators     → Makale 21-28
├── Estate & Family          → Makale 30-34, 39-42, 45-46
├── Filing Guides            → Makale 36-38, 43-44, 47-48
└── Reviews & Comparisons    → Makale 23, 29, 35, 40, 49-50
```

### Etiketler (Tag)

```
LLC, S-Corp, Business Formation, Registered Agent, DBA, EIN,
Trademark, Copyright, Business License, Annual Report,
Divorce, Child Custody, Child Support, Legal Separation, Prenuptial,
Estate Planning, Living Trust, Will, Probate, Power of Attorney,
Landlord, Tenant, Lease Agreement, Eviction, Sublease,
NDA, Contract Template, Service Agreement, Partnership,
Small Claims, Name Change, Tax Calculator
```

Her makaleye 3-5 ilgili etiket ata.

---

## 10. FTC VE YASAL UYUM KONTROL LİSTESİ

### Her Makale İçin Zorunlu Öğeler

- [ ] **FTC Affiliate Disclosure** — Makalenin BAŞINDA, ilk affiliate linkinin ÜSTÜnde
  - Metin: *"Disclosure: Some links in this article are affiliate links. If you use a service through our link, we may earn a commission at no extra cost to you. This does not affect our editorial independence."*
  - Minimum 12px font, okunabilir renk
  - WordPress Reusable Block olarak kaydet → her makaleye ekle

- [ ] **Legal Disclaimer** — Makalenin SONUNDA
  - Metin: Her makaledeki italik disclaimer metni
  - WordPress Reusable Block olarak kaydet

- [ ] **Affiliate linkler nofollow** — ThirstyAffiliates otomatik yapar (ayarları doğrula)

- [ ] **"Last reviewed" tarihi** — Her makalenin sonunda

### Site Geneli Zorunlu Sayfalar (Makale yayınlamadan ÖNCE oluştur)

1. ✅ About Us / Our Editorial Process
2. ✅ Privacy Policy (Complianz + manuel eklemeler)
3. ✅ Terms of Use
4. ✅ Legal Disclaimer (ayrı sayfa)
5. ✅ Affiliate Disclosure ("How We Make Money")
6. ✅ Contact Us (çalışan form)
7. ✅ Cookie Policy (Complianz otomatik)

---

## 11. YAYINLAMA TAKVİMİ (ÖNERİLEN SIRALAMA)

### Hafta 1-2 (İlk 10 Makale — Temel Katman)

**Günde 1 makale yayınla (toplam 10 iş günü):**

| Gün | # | Makale | Neden Bu Sırada? |
|:---:|:-:|--------|-----------------|
| 1 | 1 | Free NDA Template | En yüksek arama hacmi, hub makalesi |
| 2 | 3 | LLC Operating Agreement | Yüksek ticari niyet |
| 3 | 21 | LLC Formation Cost Calculator | En yüksek affiliate potansiyeli (ZenBusiness $100) |
| 4 | 36 | How to Form LLC Online | 21 ile birlikte güçlü internal link kümesi |
| 5 | 8 | Last Will and Testament | Farklı küme — çeşitlilik |
| 6 | 39 | Uncontested Divorce Online | CompleteCase affiliate başlatma |
| 7 | 2 | Independent Contractor Agreement | NDA ile internal link |
| 8 | 22 | S-Corp vs LLC Calculator | LLC kümesini güçlendirme |
| 9 | 5 | Residential Lease Agreement | Farklı küme — emlak |
| 10 | 40 | CompleteCase Review | Doğrudan affiliate review |

### Hafta 3-4 (Makale 11-20)

| Gün | Makaleler (günde 1) |
|:---:|---------------------|
| 11 | #9 Living Trust Template |
| 12 | #23 Registered Agent Comparison |
| 13 | #10 General Power of Attorney |
| 14 | #25 EIN Application Guide |
| 15 | #4 Commercial Lease Agreement |
| 16 | #33 Divorce Cost Calculator |
| 17 | #15 Service Agreement |
| 18 | #6 Bill of Sale |
| 19 | #13 Eviction Notice |
| 20 | #37 How to File EIN Online |

### Hafta 5-6 (Makale 21-30 — AdSense başvuru penceresi)

| Gün | Makaleler |
|:---:|-----------|
| 21-30 | #7, #11, #12, #14, #17, #24, #26, #29, #30, #38 |

**30. makale sonrası → Google AdSense'e başvur**

### Hafta 7-8 (Makale 31-40)

| Gün | Makaleler |
|:---:|-----------|
| 31-40 | #16, #18, #19, #20, #27, #28, #31, #32, #34, #35 |

### Hafta 9-10 (Makale 41-50)

| Gün | Makaleler |
|:---:|-----------|
| 41-50 | #41, #42, #43, #44, #45, #46, #47, #48, #49, #50 |

---

## 12. SORUN GİDERME

### Rank Math Skoru 80'in Altında
- Focus keyword'ü H1, ilk paragraf ve en az 1 H2'de kullan
- Meta description'a focus keyword ekle
- Internal link sayısını 3+ yap
- Görsel alt text'e keyword ekle
- İçerik uzunluğunu 1,500+ kelimeye çıkar

### Affiliate Link Henüz Onaylanmadı
- Makaleyi yayınla AMA [THIRSTY:] yer tutucularını geçici olarak bilgi amaçlı text linklere dönüştür (affiliate olmayan doğrudan URL)
- Onay geldiğinde geri dön ve ThirstyAffiliates linki ile değiştir
- Alternatif: makaleyi Draft olarak tut, onay gelince yayınla

### Featured Image Bulunamıyor
- Unsplash'te sonuç yoksa Pexels'i dene
- Genel arama terimleri kullan: "legal document", "business meeting", "signing contract"
- Son çare: Canva'da sadece text + arka plan rengi ile minimal tasarım yap

### WordPress Blok Editörüne Yapıştırma Sorunları
- Markdown'ı önce bir plain text editöre yapıştır (Windows: Notepad, Mac: TextEdit plain mode)
- Sonra WordPress'e yapıştır
- Tablolar otomatik dönüşmezse: WordPress Table bloğu kullanarak manuel oluştur
- Alternatif: "Markdown to HTML" online converter kullan, sonra WordPress Custom HTML bloğuna yapıştır

### İçerik Çok Yapay/AI Gibi Görünüyor
- Her makaleye 2-3 kişisel dokunuş ekle (pratik not, deneyim paylaşımı)
- "In our experience..." veya "What we recommend..." gibi ifadeler ekle
- Aşırı tekrarlayan cümle yapılarını değiştir
- Gerekirse ChatGPT/Claude'a "humanize this paragraph" de

---

## EK: HIZLI REFERANS KARTI

```
┌─────────────────────────────────────────────────────────────┐
│  CLEARLEGALTIPS.COM — YAYINLAMA HIZLI REFERANSI             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. Makale aç → WordPress'e Draft olarak yapıştır           │
│  2. Metadata bloğunu sil                                    │
│  3. [THIRSTY:] → ThirstyAffiliates kısa link               │
│  4. Doğru YAZAR ata                                         │
│  5. KATEGORİ + ETİKETLER seç                               │
│  6. Featured IMAGE yükle                                    │
│  7. Rank Math: Focus Keyword + Meta Description             │
│  8. Rank Math skor ≥ 80 ✓                                   │
│  9. Hızlı oku + 1 küçük düzenleme yap                      │
│  10. PUBLISH                                                │
│                                                             │
│  ⚠️  Günde MAX 5 makale                                     │
│  ⚠️  FTC disclosure ilk affiliate linkinin ÜSTÜNDE          │
│  ⚠️  Disclaimer her makalenin SONUNDA                       │
│  ⚠️  Minimum 3 internal link                                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

**Bu doküman 50 makalenin WordPress'e yayınlanması sürecinde tek referans kaynağı olarak kullanılacaktır. Her bölüm bağımsız olarak erişilebilir ve güncellenebilir.**

*Doküman tarihi: Mayıs 2026*
