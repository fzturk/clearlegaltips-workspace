# Plan: Eyalet/ülke bazlı 8 hub — Ekim 2026 – Temmuz 2027 (190 post)

## Context
26 Eylül araştırma raporu (`workspace/reports/vertical-hub-research-2026-09-26.md`) 10 dikey önerdi. Kullanıcının kararları:
- **Faz A (1–4. hub'lar):** Small Estate, Small Claims, Divorce, Judgment/Garnishment. **80 postun taslağı şimdi bulutta** hazırlanır. Kullanıcı yayın günü gelen taslağı lokal Claude Code'da düzenler, PDF/görsel üretir ve yayınlar.
- **Tempo:** haftada 5 post, Pazartesi–Cuma, günde 1 post.
- **Etkileşimli JS araçları** istendi.
- **Post 176** (Online Divorce TX/CA/FL) "online divorce" açısına daraltılır.
- **Yeni 11. hub:** ABD dışında yaşayanların ABD'de şirket/ortaklık kurması (araştırması aşağıda).
- **Faz B (5–11. hub'lar):** takvim ve iş akışı bu planda. Taslakları, yayından en az 4 hafta önce dalga dalga üretilir.

LLC eyalet kurma/ücret sayfaları kullanıcının ayrı işi; bu plan onlarla çakışmaz, yalnızca link verir.

---

## 1. Ortak mimari (tüm hub'lar)
- **Veri tek kaynaktan:** `workspace/data/{vertical}.csv`.
  - Kapsam: 50 eyalet + DC (hub 11'de ülke/konu satırları).
  - Kolonlar: değer(ler), `source_url` (statute/mahkeme/kurum/IRS), `verified_date`, `notes`.
  - Rakip siteler yalnızca ipucu; kaynak kolonuna giremez. Örnek: CA small estate $239.700 hatası; resmi DE-300 = $208.850, 2028'e kadar.
- **Taslak paketi:** `workspace/drafts/{hub}/{slug}.html` (Gutenberg'e yapıştırılır) ve `{slug}.meta.json`. Meta içeriği:
  - title ≤60, rank_math_title, rank_math_description ≤155, focus_keyword
  - category_id, 3–4 mevcut tag
  - internal_links, go_slugs, sources
  - pdf_filename, pdf_outline, featured_image_prompt, publish_date
- **Modeller:**
  - Spoke: canlı ID 7538 `texas-llc-filing-fee` (rakamlı H2'ler, `clt-sources`, "diğer 49 eyalet").
  - Hub: ID 5921 `security-deposit-limits-by-state` ("How We Verified This Data", "What Changed", "Cite or Download This Data").
- **Zorunlu 6 element** (CLAUDE.md), FAQPage JSON-LD, "Fact-checked: {Ay Yıl}" satırı.
- **İç link kuralı (kritik):**
  - Bir taslak yalnızca **canlı** postlara ya da **takvimde kendisinden önce yayınlanan** postlara link verir.
  - Hub'daki eyalet satırı, spoke yayınlanana kadar düz metin kalır.
  - Her Cuma için `workspace/drafts/{hub}/hub-link-updates/W{nn}.md` yama dosyası üretilir: o hafta yayınlanan spoke'ları hub'a ve kardeş spoke'lara linkler.
- **JS araçları:** `workspace/widgets/{tool}.html`, Custom HTML bloğuna yapıştırılır.
  - Harici bağımlılık yok, CSV'den gömülü JSON, clt renkleri, 375px mobil.
  - `<script>` çalışmazsa aynı veriyle statik tabloya düşer.
- **Kalite kapısı:** `workspace/tools/qa_draft.py` sıfır hata vermeli. Kontroller:
  - 6 zorunlu sınıf var mı; yalnızca `/go/` affiliate linki
  - Kelime sayısı: hub ≥3.000, spoke ≥1.900
  - title ≤60, meta ≤155
  - Yasak ifadeler ("attorney-reviewed", kurgusal kişi)
  - İç link takvim kuralı
  - Tablodaki her rakamın CSV'de kaynağı olması
  - Geçerli JSON-LD
- **Yıl etiketi:**
  - Ekim–Kasım postları "(2026)" alır, Ocak 2027 toplu yıl güncellemesi listesine girer.
  - 30 Kasım'dan sonra yayınlananlar "(2027)" alır; veriler 1 Ocak 2027 ücret/oran değişikliklerine göre.

## 2. Hazırlık — Hafta 0 (28 Eyl – 2 Eki, bulut)
1. `.claude/skills/write-seo-post/SKILL.md` güncellenir:
   - `/recommend/` → `/go/`
   - Canlı kategori ID'leri: 1 Legal Templates, 6 Business Calculators, 7 Estate & Family, 8 Filing Guides, 9 Reviews
   - Tek yazar, geriye tarihleme yok
2. Yeni `.claude/skills/state-spoke/SKILL.md`: CSV → birincil kaynak → taslak → QA akışı, hub ve spoke outline şablonları.
3. Araçlar: `workspace/tools/qa_draft.py`, `workspace/tools/build_widgets.py`, test widget'ı `workspace/widgets/test-hello.html`.
4. Takvim dosyası `workspace/plans/editorial-calendar-2026-2027.csv`: tarih, gün, hafta, hub, tür, slug, çalışma başlığı, kategori, focus kw, taslak yolu, durum, post_id. Bu plandaki tablolardan birebir üretilir.

**Kullanıcı (lokal, Hafta 0):**
- Test widget'ını canlıda Custom HTML bloğunda dene.
- Affiliate başvuruları: Trust & Will (Impact), OnlineDivorce (FlexOffers), CompleteCase.
- İsteğe bağlı: Keyword Planner ile eyalet sıralamasını doğrula. Farklı çıkarsa spoke sırası o hub'ın taslakları üretilmeden değişir.

## 3. Taslak üretim sırası (bulut, şimdi)
Taslaklar yayın takvimi sırasıyla üretilir ve her **yayın haftası = 1 commit** olur ("drafts: W01 small-estate (5)"):
1. Hazırlık araçları
2. Hub 2 → W01–W04
3. Hub 1 → W05–W08
4. Hub 3 → W09–W12
5. Hub 4 → W14–W17

Her hub'ın CSV'si ve widget'ı, o hub'ın ilk commit'inde gelir.

## 4. Kullanıcının günlük lokal akışı (her yayın günü)
1. `git pull`, sonra takvim CSV'sinde bugünün satırı.
2. Taslak HTML'i düzenle, Rank Math alanlarını `meta.json`'dan gir, kategori ve tag'leri ata.
3. PDF (`pdf-generate`, `pdf_outline`'dan) ve featured image (`generate-featured-image`, `post-{id}-{slug}.jpg`).
4. **Bugünün tarihiyle** yayınla, geriye tarihleme yok. CSV'de `status=published`, `post_id` gir.
5. **Cuma:** o haftanın `hub-link-updates/W{nn}.md` yamasını uygula.

Ben sonraki oturumda REST ile slug, `/go/` linklerini ve hub linklerini doğrularım.

---

## 5. FAZ A — Gün gün yayın takvimi (80 post)

### Hub 2 — Small Estate & Probate by State
- Kategori: Estate & Family (7); spoke'lar da 7.
- JS: **Small Estate Eligibility Checker** (eyalet + tahmini değer + gayrimenkul var mı + vasiyet var mı → affidavit uygun mu, bekleme süresi, mahkemeye dosyalama gerekir mi, resmi form).
- CTA: `/go/trust-and-will` (onay gelene kadar `lawdepot-living-trust`), `lawdepot-affidavit-form`.

| Hafta | Pzt | Sal | Çar | Per | Cum |
|---|---|---|---|---|---|
| W01 5–9 Eki | **HUB** `small-estate-affidavit-limits-by-state` + widget + 3131 güncellemesi (eyalet bölümü özet + hub linki) | `texas-small-estate-affidavit` | `california-small-estate-affidavit` | `florida-small-estate-affidavit` | `illinois-small-estate-affidavit` |
| W02 12–16 Eki | `new-york-small-estate-affidavit` | `pennsylvania-…` | `ohio-…` | `michigan-…` | `virginia-…` |
| W03 19–23 Eki | `indiana-…` | `georgia-…` | `north-carolina-…` | `arizona-…` | `washington-…` |
| W04 26–30 Eki | `new-jersey-…` | `tennessee-…` | `missouri-…` | `maryland-…` | `colorado-…` |

Spoke içeriği:
- Eşik; hesaba katılan/katılmayan varlıklar; bekleme süresi.
- Gayrimenkul kuralı; mahkeme dosyalaması; tanık/noter.
- İlçe formu (TX gibi); resmi form linki.
- Aşarsa ne olur (probate/summary administration); 2025–26 değişikliği; FAQ.

### Hub 1 — Small Claims Court by State
- Kategori: Filing Guides (8).
- **Hub = mevcut ID 165**, URL korunur. 50 satır baştan doğrulanır, kaynak ve tarih kolonu eklenir.
- JS: **Small Claims Cost Estimator** (eyalet + talep tutarı → limit içinde mi, dosya ücreti aralığı, tebligat maliyeti, bir üst mahkeme alternatifi).
- CTA: `lawdepot-payment-demand-letter`.

| Hafta | Pzt | Sal | Çar | Per | Cum |
|---|---|---|---|---|---|
| W05 2–6 Kas | **HUB** 165 yükseltmesi + widget | `california-small-claims-court` | `texas-small-claims-court` | `florida-…` | `new-york-…` |
| W06 9–13 Kas | `ohio-…` | `michigan-…` | `pennsylvania-…` | `illinois-…` | `georgia-…` |
| W07 16–20 Kas | `north-carolina-…` | `virginia-…` | `arizona-…` | `colorado-…` | `washington-…` |
| W08 23–27 Kas | `new-jersey-…` | `tennessee-…` | `massachusetts-…` | `maryland-…` | `utah-…` |

Spoke içeriği:
- Limit (birey/işletme); en büyük 3–5 ilçenin ücretleri; tebligat yolları.
- Avukat izni; duruşma süresi; temyiz.
- Karar sonrası tahsilat (W16–17 spoke'larına Cuma yamasıyla link); resmi formlar.
- Demand letter serisine ve 7341'e link.

### Hub 3 — Divorce by State (başlık ve veriler 2027)
- Kategori: hub 7, spoke'lar Filing Guides (8).
- JS: **Divorce Cost & Timeline Estimator** (eyalet + uncontested/contested + ikamet süresi → dosya ücreti, fee waiver, en erken kesinleşme tarihi). 163 `divorce-cost-calculator`'a da gömülür.
- 176 daraltma: yeni başlık, meta ve giriş önerisi. Niyeti "online divorce services in TX/CA/FL".
- CTA: OnlineDivorce/CompleteCase (onaya kadar `lawdepot-family`).

| Hafta | Pzt | Sal | Çar | Per | Cum |
|---|---|---|---|---|---|
| W09 30 Kas–4 Ara | **HUB** `divorce-requirements-by-state` + widget + 163 embed + 176 daraltma | `how-to-file-for-divorce-in-texas` | `…-in-california` | `…-in-florida` | `…-in-new-york` |
| W10 7–11 Ara | `…-in-pennsylvania` | `…-in-illinois` | `…-in-ohio` | `…-in-georgia` | `…-in-north-carolina` |
| W11 14–18 Ara | `…-in-michigan` | `…-in-new-jersey` | `…-in-virginia` | `…-in-washington` | `…-in-arizona` |
| W12 21–25 Ara | `…-in-tennessee` | `…-in-colorado` | `…-in-indiana` | `…-in-missouri` | `…-in-massachusetts` |

Spoke içeriği:
- İkamet (eyalet + ilçe); bekleme/cooling-off; gerekçeler (no-fault).
- Dosya ücreti ve ilçe farkları; fee waiver formu.
- Uncontested adımlar; resmi self-help formları; çocuk varsa ek şartlar.
- 169, alimony, parenting plan postlarına link.

### W13 28 Ara – 1 Oca — Tampon (yeni yayın yok)
- 1 Ocak 2027'de değişen divorce ve small claims ücretlerinin kontrolü; düzeltme yamaları.
- Ocak 2027 toplu yıl güncellemesi listesi (Ekim–Kasım postları dahil).

### Hub 4 — Judgment Collection & Wage Garnishment (2027)
- Hub A kategorisi Business Calculators (6); diğerleri Filing Guides (8).
- JS: **Judgment Interest Calculator** (eyalet + karar tarihi + tutar + ödeme tarihi → faiz). Değişken oranlı eyaletlerde (TX, FL, IA…) dönem tablosu.
- Borç rahatlatma affiliate'i yok. CTA: `lawdepot` / `lawdepot-payment-demand-letter`.

| Hafta | Pzt | Sal | Çar | Per | Cum |
|---|---|---|---|---|---|
| W14 4–8 Oca | **HUB A** `judgment-interest-rates-by-state` + widget | **HUB B** `wage-garnishment-laws-by-state` (NCLC 2025 notları) | `texas-wage-garnishment-laws` | `california-wage-garnishment-laws` | `florida-wage-garnishment-laws` |
| W15 11–15 Oca | `new-york-wage-garnishment-laws` | `pennsylvania-…` | `illinois-…` | `ohio-…` | `georgia-…` |
| W16 18–22 Oca | `north-carolina-wage-garnishment-laws` | `how-to-collect-a-small-claims-judgment-in-california` | `…-in-texas` | `…-in-florida` | `…-in-new-york` |
| W17 25–29 Oca | `…-in-ohio` | `…-in-michigan` | `…-in-pennsylvania` | `…-in-illinois` | `…-in-georgia` |

Spoke içeriği:
- Garnishment: koruma yüzdesi (federal %75 / 30× asgari ücret ile karşılaştırma), banka hesabı muafiyeti, head-of-household istisnası, itiraz formu.
- Collect: writ/levy, debtor exam, lien, ücretler, faiz oranı (hub A), zaman aşımı/yenileme.

---

## 6. Hub 11 — ABD dışında yaşayanlar için ABD şirketi ve ortaklık (araştırma özeti)

**Talep ve değer:**
- `form 5472` ayda **8.100** arama (global), `form 5472 instructions` 1.900.
- `llc for non us residents` 390 arama, CPC **$16,88**; `wyoming llc for non us residents` 170 arama, CPC $28,42 (Keyword Tool). Hacim orta, niyet ve ticari değer çok yüksek.
- Ülke kalıbında autocomplete: "open us llc from india / pakistan / bangladesh / canada / nepal".

**Para kazanma:** doola zaten `/go/doola` üzerinden PartnerStack'te. %30, referans başına **$899'a kadar** ([PartnerStack](https://market.partnerstack.com/program/doola)). Sitedeki en yüksek komisyonlu ürün, kitleyle birebir örtüşüyor. İkincil: `lawdepot-llc-operating-agreement`.

**Doğrulanmış birincil gerçekler (içeriğin omurgası):**
- **Form 5472 + pro forma 1120:** yabancı sahipli tek üyeli LLC'ler (disregarded entity) 2017'den beri gelir olmasa da her yıl dosyalar. Son tarih 15 Nisan. Ceza form başına **$25.000**, IRS bildiriminden 90 gün sonra her 30 günde +$25.000 (IRC §6038A(d); [IRS i5472](https://www.irs.gov/instructions/i5472)).
- **EIN, SSN olmadan:**
  - Telefon: 267-941-1099 (ET 06:00–23:00).
  - Faks: 304-707-9471.
  - SS-4 7b satırına "Foreign" yazılır ([IRS iSS4](https://www.irs.gov/instructions/iss4)).
- **BOI/CTA:** FinCEN 26 Mart 2025 interim rule'u **11 Ağustos 2026 final rule** ile kalıcı hale geldi (yürürlük 14 Ağustos 2026). ABD'de kurulan şirketler ve ABD kişileri muaf. Yalnızca ABD'de kayıtlı **yabancı** şirketler raporlar ([FinCEN](https://www.fincen.gov/boi), [Mayer Brown](https://www.mayerbrown.com/en/insights/publications/2026/08/the-final-chapter-fincen-permanently-eliminates-boi-reporting-requirements-for-us-companies-and-us-persons)). Rakiplerin çoğu hâlâ eski BOI uyarısı taşıyor: güncellik fırsatı.
- **Vergi:** ABD'de ticari faaliyeti (ECI) olmayan non-resident sahibin LLC geliri genelde federal gelir vergisine tabi değil. Vergilenen iki kalem: ECI (1040-NR, artan oranlı) ve ABD kaynaklı FDAP ([IRS Pub 519](https://www.irs.gov/publications/p519)).
- **Yabancı ortaklı ortaklık:** §1446 kapsamında ortaklık, yabancı ortağa düşen ECTI üzerinden yıl içinde vergi öder. Form 8804 + her ortak için 8805 + 8813 vouchers; dağıtım olmasa bile dosyalanır ([IRS partnership withholding](https://www.irs.gov/individuals/international-taxpayers/partnership-withholding), [i8804 Ocak 2026](https://www.irs.gov/pub/irs-pdf/i8804.pdf)).
- **Banka:** Mercury, SSN'siz 180+ ülkeden kurucu kabul ediyor. Kısıt OFAC'a ve **ikamet ülkesine** bağlı, vatandaşlığa değil ([Mercury eligibility](https://support.mercury.com/hc/en-us/articles/28770467511060-Eligibility-and-requirements-for-opening-a-Mercury-account)).
- **E-2 vizesi:** State Dept listesinde 81 ülke. **Türkiye var, Hindistan, Çin, Brezilya yok.** Göç hukuku bilgisi "bilgi, tavsiye değil" çerçevesinde verilir.

**Sınır:** eyalet LLC ücret sayfaları kullanıcının işi. Hub 11 yalnızca "non-resident için hangi eyalet" açısını işler ve ücretler için o sayfalara link verir.

**E-E-A-T notu:** editör Türkiye merkezli. Türkiye spoke'unda **yalnızca gerçekse** birinci el deneyim eklenir; uydurma yok. Taslakta `<!-- EDITOR: kişisel deneyim varsa ekle -->` işareti bırakılır.

## 7. FAZ B — Hub 5–11 takvimi (110 post; günler Pzt→Cum sırasıyla)

Taslak dalgaları:
- Hub 11 taslakları: **15 Ocak 2027**'ye kadar.
- Diğer hub'lar: yayından ≥4 hafta önce.

Her hub'ın ilk taslak commit'inde CSV + widget + skill şablonu gelir.

### Hub 11 — US Company for Non-Residents
- Takvim: W18–W21, **1–26 Şubat 2027**, 20 post.
- Neden şimdi: 15 Mart (1065/1120-S) ve **15 Nisan (5472)** son tarihlerinden önce.
- Kategori: Filing Guides (8); şablon Legal Templates (1).
- JS: **Non-Resident US Compliance Checker** (varlık türü + üye sayısı + ABD faaliyeti var mı → dosyalanacak formlar, son tarihler, ceza riski).

| Hafta | Pzt | Sal | Çar | Per | Cum |
|---|---|---|---|---|---|
| W18 1–5 Şub | **HUB** `us-company-for-non-residents` + widget | `form-5472-guide-foreign-owned-llc` | `ein-for-non-us-residents` | `us-llc-taxes-for-non-residents` | `us-business-bank-account-non-resident` |
| W19 8–12 Şub | `llc-vs-c-corp-for-non-residents` | `best-state-for-llc-non-residents` | `foreign-partner-us-partnership-1446-withholding` | `foreign-owned-llc-operating-agreement-template` | `boi-reporting-2026-non-residents` |
| W20 15–19 Şub | `itin-vs-ein-non-residents` | `w-8ben-e-us-llc-payments-stripe-paypal` | `foreign-owned-llc-annual-compliance-calendar` | `e-2-visa-business-requirements` | `how-to-open-a-us-llc-from-turkey` |
| W21 22–26 Şub | `…-from-india` | `…-from-pakistan` | `…-from-bangladesh` | `…-from-canada` (US LLC'yi Kanada'nın şirket sayması → çifte vergi tuzağı) | `…-from-the-uk` |

Ülke spoke'ları: vergi anlaşması var/yok (IRS treaty listesi), E-2, döviz/banka pratikleri, yerel vergi beyanı uyarısı (tavsiye değil), doola CTA.

### Hub 8 — Contractor License & Lien Deadlines
- Takvim: W22–W24, 1–19 Mart, 15 post. İnşaat sezonu başı.
- JS: **Mechanics Lien Deadline Calculator**.
- CTA: NEXT Insurance (başvuru Şubat'ta), LawDepot.
- Mevcut `how-to-file-mechanics-lien-online` yamalanır.

| Hafta | Pzt | Sal | Çar | Per | Cum |
|---|---|---|---|---|---|
| W22 | **HUB A** `contractor-license-requirements-by-state` | **HUB B** `mechanics-lien-deadlines-by-state` + widget | `california-contractor-license-requirements` (AB 2622, $1.000) | `texas-…` | `florida-…` |
| W23 | `new-york-…` | `arizona-…` | `north-carolina-…` | `georgia-…` | `california-mechanics-lien-deadlines` |
| W24 | `texas-mechanics-lien-deadlines` | `florida-…` | `new-york-…` | `pennsylvania-…` | `illinois-…` |

### Hub 6 — Eviction Timeline & Squatter Laws
- Takvim: W25–W27, 22 Mart – 9 Nisan, 15 post. Bahar kira sezonu.
- JS: **Eviction Timeline Estimator**.
- CTA: DoorLoop, `lawdepot-eviction-notice`.

| Hafta | Pzt | Sal | Çar | Per | Cum |
|---|---|---|---|---|---|
| W25 | **HUB A** `eviction-timeline-by-state` + widget | **HUB B** `squatters-rights-by-state` | `eviction-process-in-texas` | `…-in-california` | `…-in-florida` |
| W26 | `…-in-new-york` | `…-in-georgia` | `…-in-north-carolina` | `…-in-ohio` | `…-in-michigan` |
| W27 | `…-in-arizona` | `squatters-rights-florida` (2024 yasası) | `squatters-rights-georgia` (HB 1017) | `squatters-rights-alabama` | `squatters-rights-tennessee` |

### Hub 7 — Rent Rules (late fee, rent increase, rent cap)
- Takvim: W28–W30, 12–30 Nisan, 15 post.
- JS: **Late Fee Checker** (eyalet + kira + gün → yasal tavan, ek süre).
- CTA: DoorLoop.

| Hafta | Pzt | Sal | Çar | Per | Cum |
|---|---|---|---|---|---|
| W28 | **HUB A** `late-fee-laws-by-state` + widget | **HUB B** `rent-increase-laws-by-state` | `washington-rent-increase-laws` (HB 1217) | `california-…` (AB 1482) | `oregon-…` |
| W29 | `new-york-…` | `new-jersey-…` | `florida-…` | `texas-…` | `illinois-…` |
| W30 | `massachusetts-…` | `colorado-…` | `texas-rent-late-fee-laws` | `florida-rent-late-fee-laws` | `california-rent-late-fee-laws` |

### Hub 5 — Will Requirements by State (+ e-will)
- Takvim: W31–W33, 3–21 Mayıs, 15 post.
- JS: **Will Validity Checker** (eyalet + el yazısı mı + tanık sayısı + noter → geçerlilik ve self-proving durumu).
- CTA: Trust & Will, `lawdepot-last-will`.

| Hafta | Pzt | Sal | Çar | Per | Cum |
|---|---|---|---|---|---|
| W31 | **HUB A** `will-requirements-by-state` + widget | **HUB B** `electronic-wills-by-state` (MN 2026, NY 2027) | `how-to-make-a-will-in-california` | `…-in-texas` | `…-in-florida` |
| W32 | `…-in-new-york` | `…-in-pennsylvania` | `…-in-illinois` | `…-in-ohio` | `…-in-georgia` |
| W33 | `…-in-north-carolina` | `…-in-michigan` | `…-in-new-jersey` | `…-in-virginia` | `holographic-wills-by-state` |

### W34 (24–28 Mayıs) — Tampon ve ölçüm (yeni yayın yok)
- Hub 1–4'ün 4–6 aylık GSC analizi (Supermetrics).
- Genişleme kararı: 8 haftada spoke başına ≥100 gösterim varsa kalan 31 eyalet Q3 2027'ye.

### Hub 9 — Non-Compete Laws by State
- Takvim: W35–W37, 31 Mayıs – 18 Haziran, 15 post. 1 Temmuz yürürlük tarihlerinden önce.
- JS: **Non-Compete Enforceability Checker** (eyalet + maaş + çalışan türü + işten çıkış türü).
- Mevcut şablon postu template niyetinde kalır; yeni hub tablo niyetinde.

| Hafta | Pzt | Sal | Çar | Per | Cum |
|---|---|---|---|---|---|
| W35 | **HUB** `non-compete-laws-by-state` + widget | `california-non-compete-laws` | `texas-…` | `florida-…` (CHOICE Act) | `new-york-…` |
| W36 | `virginia-…` (SB 170) | `wyoming-…` (SF 107) | `minnesota-…` | `illinois-…` | `washington-…` |
| W37 | `colorado-…` | `massachusetts-…` | `georgia-…` | `oklahoma-…` | `non-compete-vs-non-solicitation` |

### Hub 10 — Employer Compliance (çalışan açısı)
- Takvim: W38–W40, 21 Haziran – 9 Temmuz, 15 post. 1 Temmuz yasa değişiklikleri.
- JS: **Final Paycheck Deadline Checker**.
- CTA: çalışan tarafı `lawdepot-payment-demand-letter`; işveren tarafı Gusto (PartnerStack).

| Hafta | Pzt | Sal | Çar | Per | Cum |
|---|---|---|---|---|---|
| W38 | **HUB A** `final-paycheck-laws-by-state` + widget | **HUB B** `paid-sick-leave-laws-by-state` (NE 2025, CT 2026–27, MO repeal) | `california-final-paycheck-law` | `texas-…` | `florida-…` |
| W39 | `new-york-…` | `illinois-…` | `pennsylvania-…` | `ohio-…` | `georgia-…` |
| W40 | `north-carolina-…` | `michigan-…` | `washington-…` | `pto-payout-laws-by-state` | `employer-wont-pay-final-paycheck-what-to-do` |

---

## 8. Kritik dosyalar
- **Yeni:**
  - `workspace/plans/editorial-calendar-2026-2027.csv`
  - `workspace/data/*.csv`
  - `workspace/drafts/{hub}/**` (+ `hub-link-updates/`)
  - `workspace/widgets/*.html`
  - `workspace/tools/{qa_draft.py,build_widgets.py}`
  - `.claude/skills/state-spoke/SKILL.md`
- **Güncellenecek:**
  - `.claude/skills/write-seo-post/SKILL.md`
  - CLAUDE.md'ye yeni içerik kümeleri + yeni `/go/` slug'ları (onaylandıkça)
- **Referans canlı postlar:** 7538, 5921, 165, 3131, 3411, 161, 163, 169, 176, 7341, 7371, `how-to-file-mechanics-lien-online`, non-compete şablonu.

## 9. Riskler
- **Script engeli:** widget'lar statik tabloya düşer.
- **Affiliate onayı gecikirse:** LawDepot yedek slug'ları kullanılır; onay gelince toplu slug değişimi yapılır.
- **Takvim kayması:** kullanıcı bir günü atlarsa sıra kayar, tarih değişmez. Geriye tarihleme yok. CSV'de `status` ile izlenir.
- **Yamyamlık:**
  - 3131 ve SE hub: şablon / tablo niyeti ayrılır.
  - 176 ve divorce spoke'ları: online servis / dosyalama niyeti ayrılır.
  - Non-compete şablonu ve hub'ı ayrılır.
  - Hub 11 ile LLC eyalet sayfaları: non-resident açısı / ücret.
- **YMYL:** göç (E-2) ve vergi içeriği: "bilgi, tavsiye değil" + resmi kaynak. Kurgusal uzman yok.

## 10. Doğrulama
- Her haftalık commit öncesi: `python3 workspace/tools/qa_draft.py workspace/drafts/<hub>/` → 0 hata.
- Widget'lar: Playwright/Chromium (`/opt/pw-browsers/chromium`) ile 5 eyalet × kenar değer (limit altı/üstü, değişken oran dönemi) ve 375px taşma testi.
- Takvim CSV'si ile taslak dosyalarının birebir eşleşmesi (script kontrolü).
- Yayın sonrası REST kontrolü: slug, kategori, `/go/`, hub linkleri.
- Her hub'ın son yayınından +4 ve +8 hafta sonra Supermetrics GSC ölçümü.
