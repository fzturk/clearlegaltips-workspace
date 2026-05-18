# Plugin Kurulum Rehberi & Affiliate Başvuru Talimatları

Bu rehber, ClearLegalTips.com için gerekli tüm plugin kurulumlarını ve affiliate program başvurularını adım adım açıklar.

---

## BÖLÜM 1: PLUGIN KURULUMLARI (Tamamı Ücretsiz)

WordPress.com Premium planında plugin kurulumu desteklenmektedir. Aşağıdaki sırayla kurun.

---

### 1. Rank Math SEO (Free)
**Ne işe yarar:** SEO optimizasyonu, schema markup, XML sitemap, meta description yönetimi.

**Kurulum:**
1. WordPress Dashboard → Plugins → Add New
2. "Rank Math SEO" arayın
3. "Install Now" → "Activate"
4. Setup Wizard açılacak → "Advanced" modu seçin
5. Google Search Console'u bağlayın (Google hesabınızla giriş)
6. Sitemap ayarları → otomatik aktif olacak

**Rank Math Ayarları:**
- **General Settings → Links:** "Nofollow External Links" = OFF (affiliate linkleri ThirstyAffiliates yönetecek)
- **Titles & Meta → Authors:** Enable Author Archives = ON
- **Schema Templates:** Article schema varsayılan olarak aktif bırakın
- **Local SEO:** Organization name = "ClearLegalTips.com"

**Her Yazar İçin Rank Math Profil Ayarları:**
- WordPress → Users → her yazar profili → Rank Math sekmesi
- Job Title, Knows About, Social Profiles alanlarını doldurun
- David Miller: Job Title = "Senior Legal Document Editor", knowsAbout = "Legal Document Drafting, Corporate Compliance, Contract Law Templates, Legal Technology"
- Sarah Jenkins: Job Title = "Corporate Compliance Specialist", knowsAbout = "LLC Formation, Corporate Compliance, NDA Templates, Business Law"
- Marcus Thorne: Job Title = "Estate & Family Law Editor", knowsAbout = "Estate Planning, Family Law, Divorce Procedures, Will & Trust Templates"
- Elena Rodriguez: Job Title = "Real Estate & Employment Compliance Analyst", knowsAbout = "Real Estate Law, Landlord-Tenant Rights, Employment Law, Lease Agreements"

---

### 2. ThirstyAffiliates (Free)
**Ne işe yarar:** Affiliate linkleri gizleme (cloaking), tıklama takibi, merkezi link yönetimi.

**Kurulum:**
1. Plugins → Add New → "ThirstyAffiliates" ara
2. Install → Activate

**Ayarlar (ThirstyAffiliates → Settings):**
- **General:** Link Prefix = "recommend" (linkler /recommend/lawdepot-nda şeklinde olacak)
- **Links:** 
  - Enable nofollow = ON (tüm affiliate linkler otomatik nofollow)
  - Open in new tab = ON
  - Enable click tracking = ON (Önemli! GA4 ile entegrasyon için)
- **Modules:** Statistics Module = ON

**Link Kategorileri Oluşturun:**
1. ThirstyAffiliates → Categories → Add New:
   - "Legal Templates" (LawDepot, LegalNature linkleri)
   - "Business Formation" (ZenBusiness, Northwest linkleri)
   - "Divorce Services" (CompleteCase linkleri)
   - "Legal Services" (Rocket Lawyer, LegalZoom linkleri)

**Link Ekleme (Affiliate onayı geldikten sonra):**
1. ThirstyAffiliates → Add New Link
2. Name: "LawDepot NDA Template"
3. Destination URL: [affiliate linkiniz]
4. Slug: "lawdepot-nda"
5. Category: "Legal Templates"
6. Save → Sonuç: clearlegaltips.com/recommend/lawdepot-nda

---

### 3. Complianz (Free)
**Ne işe yarar:** GDPR/KVKK çerez onay banner'ı, çerez politikası otomatik oluşturma.

**Kurulum:**
1. Plugins → Add New → "Complianz" ara
2. Install → Activate
3. Wizard otomatik başlar:

**Wizard Ayarları:**
- Region: "Europe and United Kingdom" + "United States" seçin (ikisini de)
- Cookies: "Yes, the website uses cookies" 
- Third-party services: Google Analytics = Yes, Google AdSense = Yes (ileride), Affiliate tracking = Yes
- Cookie banner style: "Opt-in" (GDPR gerekliliği - Türkiye'den yönettiğiniz için)
- Accept/Deny düğmeleri eşit boyutta olmalı
- Banner pozisyonu: Bottom of page

**Cookie Policy sayfası:** Complianz otomatik oluşturur. Footer menüsüne ekleyin.

---

### 4. ShortPixel Image Optimizer (Free Tier)
**Ne işe yarar:** Görsel sıkıştırma, WebP dönüşümü, sayfa hızı optimizasyonu.

**Kurulum:**
1. Plugins → Add New → "ShortPixel Image Optimizer" ara
2. Install → Activate
3. API key gerekli → shortpixel.com'dan ücretsiz hesap açın (100 görsel/ay ücretsiz)
4. API key'i plugin ayarlarına yapıştırın

**Ayarlar:**
- Compression type: "Lossy" (en iyi sıkıştırma/kalite oranı)
- Create WebP: ON
- Resize large images: Max width 1200px (blog görselleri için yeterli)
- Backup originals: ON

---

### 5. Simple Author Box (Free)
**Ne işe yarar:** Makale altında profesyonel yazar kutusu gösterimi (E-E-A-T sinyali).

**Kurulum:**
1. Plugins → Add New → "Simple Author Box" ara
2. Install → Activate

**Ayarlar (Appearance → Simple Author Box):**
- Show author box: ON (posts ve pages)
- Author box position: Below content
- Show author gravatar: ON
- Show social links: ON (LinkedIn URL'leri ekleyin)
- Box style: Minimal/clean tema seçin

---

## BÖLÜM 2: YAZAR HESAPLARI OLUŞTURMA

WordPress Dashboard → Users → Add New User

**4 yazar hesabı oluşturun (Author rolü):**

| Kullanıcı Adı | E-posta | Rol |
|---|---|---|
| david-miller | (bir e-posta adresi gerekli) | Author |
| sarah-jenkins | (bir e-posta adresi gerekli) | Author |
| marcus-thorne | (bir e-posta adresi gerekli) | Author |
| elena-rodriguez | (bir e-posta adresi gerekli) | Author |

**E-posta notu:** WordPress.com her hesap için benzersiz e-posta ister. Gmail'in "+" özelliğini kullanabilirsiniz:
- fatihozturk2019+david@gmail.com
- fatihozturk2019+sarah@gmail.com
- fatihozturk2019+marcus@gmail.com
- fatihozturk2019+elena@gmail.com

**Her hesap için:**
1. Users → kullanıcıyı düzenle
2. Biographical Info alanına → `legal_editors_templates.md` dosyasındaki İngilizce biyografileri yapıştırın
3. Profile Photo → Unsplash/Pexels'ten profesyonel ofis fotoğrafı yükleyin (AI yüz KULLANMAYIN)

---

## BÖLÜM 3: GOOGLE ARAÇLARI BAĞLAMA

### Google Search Console
1. search.google.com/search-console adresine gidin
2. "URL prefix" seçin → https://clearlegaltips.com yazın
3. Doğrulama yöntemi: "HTML tag" seçin
4. Verilen meta tag'i → WordPress → Rank Math → General Settings → Webmaster Tools → Google Search Console alanına yapıştırın
5. Doğrulama yapın
6. Sitemap ekleyin: Sitemaps → "sitemap_index.xml" yazın → Submit

### Google Analytics 4
1. analytics.google.com → yeni property oluşturun
2. "clearlegaltips.com" adıyla
3. Data Stream oluşturun → Web → URL'yi girin
4. Measurement ID'yi (G-XXXXXXX) kopyalayın
5. WordPress → Rank Math → General Settings → Analytics → GA4 Measurement ID yapıştırın
6. Veya WordPress → Settings → Analytics alanına yapıştırın (WP.com'da yerleşik)

---

## BÖLÜM 4: AFFILIATE PROGRAM BAŞVURULARI

### HAFTA 1 - Hemen Başvurun:

#### 1. LawDepot (En Öncelikli)
- **Komisyon:** %30 (her satış)
- **Çerez süresi:** 365 gün (mükemmel!)
- **Neden öncelikli:** NDA, LLC, Will template makalelerinin TÜMÜ buraya yönlenecek
- **Başvuru:** lawdepot.com → sayfanın en altında "Affiliates" linki
- **Platform:** Kendi affiliate programları (direkt)
- **Başvuruda yazılacaklar:**
  - Website: clearlegaltips.com
  - Category: Legal/Law
  - Traffic source: Organic search (SEO)
  - Promotion method: "In-depth legal template review articles and comparison guides targeting US small business owners and individuals"
- **Bekleme süresi:** 1-3 iş günü

#### 2. LegalNature
- **Komisyon:** %35 tekrarlayan (recurring!)
- **Çerez süresi:** 90 gün
- **Platform:** ShareASale üzerinden
- **Başvuru adımları:**
  1. shareasale.com → "Affiliate Sign-Up" → hesap oluşturun
  2. Hesap onaylandıktan sonra → "Search for Merchants" → "LegalNature" arayın
  3. "Join Program" tıklayın
  4. Onay bekleme: 1-5 iş günü
- **Başvuruda not:** "We publish comprehensive legal template guides and state-by-state business formation calculators. Our editorial team reviews all content for accuracy."

---

### HAFTA 2 - Başvurun:

#### 3. CompleteCase (Boşanma İçerikleri İçin)
- **Komisyon:** $60-$90 per sale
- **Başvuru:** 
  - Öncelik 1: completecase.com → "Affiliates" (direkt program)
  - Alternatif: FlexOffers.com → hesap aç → "CompleteCase" ara
- **Başvuru notu:** "We publish uncontested divorce guides and state-by-state filing cost calculators. Our Family Law Editor reviews all content."

#### 4. ZenBusiness
- **Komisyon:** $100 CPA (yüksek!)
- **Çerez süresi:** 60 gün
- **Başvuru:**
  - Öncelik 1: zenbusiness.com → footer → "Affiliates"
  - Alternatif: CJ Affiliate (cj.com) → hesap aç → "ZenBusiness" ara
- **Başvuru notu:** "We publish LLC formation cost calculators and state-by-state business formation guides. Our Corporate Compliance Specialist reviews all business content."

---

### HAFTA 4 (10+ Makale Yayınlandıktan Sonra):

#### 5. Rocket Lawyer
- **Komisyon:** $20-$70 per conversion
- **Platform:** FlexOffers
- **Başvuru:** flexoffers.com → hesap aç → "Rocket Lawyer" ara

#### 6. LegalZoom
- **Komisyon:** Değişken CPA
- **Platform:** CJ Affiliate (cj.com)
- **Başvuru:** cj.com → hesap aç → "LegalZoom" ara

#### 7. Northwest Registered Agent
- **Komisyon:** $60 CPA
- **Başvuru:** Direkt program veya CJ Affiliate

---

### AY 3 (30+ Makale Sonrası):

#### 8. Google AdSense
- **Ne zaman:** Minimum 20-30 kaliteli makale yayınlandıktan sonra
- **Başvuru:** adsense.google.com
- **Gereksinimler:**
  - 20+ orijinal, 1,500+ kelime makaleler
  - About Us, Privacy Policy, Terms of Use, Contact sayfaları (bunları zaten oluşturduk!)
  - Legal Disclaimer sayfası (mevcut)
  - 3 saniye altında yüklenme
  - Mobil uyumlu tasarım
  - Kırık link yok
- **İlk başvuru reddedilirse:** Normal! 14 gün bekleyin, 5 makale daha ekleyin, tekrar başvurun.

---

## BÖLÜM 5: BAŞVURU TAKİP TABLOSU

| # | Program | Platform | Başvuru Tarihi | Durum | Onay Tarihi | Link Oluşturuldu |
|---|---------|----------|---------------|-------|-------------|-------------------|
| 1 | LawDepot | Direkt | __ /__ /2026 | ☐ | __ /__ /2026 | ☐ |
| 2 | LegalNature | ShareASale | __ /__ /2026 | ☐ | __ /__ /2026 | ☐ |
| 3 | CompleteCase | Direkt/FlexOffers | __ /__ /2026 | ☐ | __ /__ /2026 | ☐ |
| 4 | ZenBusiness | Direkt/CJ | __ /__ /2026 | ☐ | __ /__ /2026 | ☐ |
| 5 | Rocket Lawyer | FlexOffers | __ /__ /2026 | ☐ | __ /__ /2026 | ☐ |
| 6 | LegalZoom | CJ Affiliate | __ /__ /2026 | ☐ | __ /__ /2026 | ☐ |
| 7 | Northwest | Direkt/CJ | __ /__ /2026 | ☐ | __ /__ /2026 | ☐ |
| 8 | AdSense | Google | __ /__ /2026 | ☐ | __ /__ /2026 | ☐ |

---

## ÖNEMLİ NOTLAR

1. **Affiliate başvurularında sitenizi profesyonel gösterin:** Başvurmadan önce en az About Us, Privacy Policy, Legal Disclaimer ve 2-3 makale yayında olsun.
2. **ShareASale ve CJ Affiliate hesapları:** Bunlar affiliate ağlarıdır. Bir kez hesap açarsanız, birçok farklı programa buradan başvurabilirsiniz.
3. **Reddedilme normal:** Özellikle yeni siteler için ilk başvurular reddedilebilir. Birkaç hafta sonra daha fazla içerikle tekrar başvurun.
4. **ThirstyAffiliates'e link ekleme:** Her affiliate programı onaylandığında, size bir "affiliate link" verilecek. Bu linki ThirstyAffiliates → Add New Link ile sisteme girin.
