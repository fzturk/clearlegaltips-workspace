# 10 Yeni Dikey / Hub Araştırması — ClearLegalTips (26 Eylül 2026)

> Kapsam dışı: eyalet LLC kurma/ücret sayfaları (ayrı iş olarak sürüyor).
> Odak: eyalet bazlı (hub + 50 eyalet spoke) ölçeklenebilir alanlar.

## Yöntem ve veri kaynakları

| Kaynak | Ne için kullanıldı | Sınır |
|---|---|---|
| GSC (Supermetrics, son 90 gün, 1.000 sorgu×sayfa satırı) | Sitenin hangi konularda **zaten** gösterim aldığını görmek | 13.436 gösterim "(unknown)" anonim sorgu |
| Canlı site REST API (167 post) | Her dikeyde mevcut "tohum" postları bulmak, yamyamlığı önlemek | — |
| Keyword Tool (Google US autocomplete) | Eyalet varyantlı talep genişliği (öneri sayısı) | Ücretsiz planda hacim yalnızca önbellekli birkaç kelimede geliyor |
| Web araştırması (SERP + resmi kaynak + yasa değişiklikleri) | Rekabet, birincil kaynak, güncellik kancası, affiliate | Hacimler için Keyword Planner ile doğrulama önerilir |

**Hacim notu:** Keyword Tool yalnızca şu kesin hacmi verdi: `small estate affidavit` = **14.800/ay** (CPC bid $0,89–3,18), `what does probate mean` = 6.600/ay. Diğer dikeylerde talebi autocomplete genişliği (seed başına öneri sayısı + her eyaletin ayrı öneri olarak çıkması) ve GSC sinyali ile ölçtüm. Uygulamadan önce Google Ads Keyword Planner (ücretsiz, Ads hesabı yeter) ile eyalet kalıplarının hacmini çekmek bir sonraki adım.

### SERP'te gördüğüm ortak tablo (tüm dikeyler için kritik)

Her "X by state 2026" sorgusunun ilk sayfası artık **programatik / AI üretimli tek-konu sitelerle** dolu: `getsmallclaims.com`, `legalcostcalculator.org`, `pettylawsuit.com`, `divorce.law`, `rentlatefee.com`, `landlordfees.com`, `billofsalenow.com`, `statuterates.com`… Bunlar hızlı ama **hatalı veri** taşıyor. Somut örnek:

- Bazı siteler "California small estate limiti 1 Nisan 2026'da $239.700'e çıktı" diyor. **Yanlış.** Resmi Judicial Council DE-300 formu ve Probate Code §890 tablosuna göre limit **$208.850**, 1 Nisan 2025 – 31 Mart 2028 arası geçerli; bir sonraki ayar 2028. ([courts.ca.gov – Probate Code 890 adjusted amounts](https://courts.ca.gov/system/files/file/probate-code-890-adjusted-amounts.pdf), [DE-300](https://courts.ca.gov/sites/default/files/courts/default/2024-11/de300.pdf), [Nolo](https://www.nolo.com/legal-updates/california-raised-small-estate-values-in-2022.html))

➡ **Farklılaşma stratejisi (her hub için):** her eyalet satırında birincil kaynak linki (statute / mahkeme / kurum), "Verified: {Ay Yıl}" damgası, resmi form linki, ilçe düzeyinde ücret farkı notu ve bir hesaplayıcı. Bu, Google'ın YMYL hukuk konularında ödüllendirdiği şey ve AI-programatik rakiplerin yapmadığı şey. Mevcut E-E-A-T kurallarıyla (gerçek kaynak + fact-check tarihi) birebir uyumlu.

---

## Özet sıralama

| # | Dikey / Hub | Talep kanıtı | Site tohumu (mevcut post) | Para kazanma | Rekabet | Öncelik |
|---|---|---|---|---|---|---|
| 1 | Small Claims Court by State | GSC: 47 sorgu / 516 gösterim, tek sayfadan | 1 small claims + 6 demand letter + collect money | Orta (LawDepot demand letter slug'ları) | Yüksek ama hatalı veri | **A** |
| 2 | Small Estate & Probate by State | 14.800/ay tek başına head term | 7 post (affidavit, heirship, probate estimator…) | Yüksek (Trust & Will %20, LawDepot estate) | Orta (hukuk büroları + eForms) | **A** |
| 3 | Divorce by State (ücret, ikamet, bekleme) | GSC: 70 sorgu / 1.293 gösterim | 9 post (uncontested, cost calc, alimony…) | Yüksek ($80–100/satış) | Yüksek (divorce.law programatik) | **A** |
| 4 | Judgment Collection & Wage Garnishment by State | 545 öneri; değişken faiz oranı = sürekli güncelleme | 5 post (collect money, SOL, late interest calc…) | Orta | Orta (statuterates.com) | **B+** |
| 5 | Will Requirements by State (+ e-will) | GSC trust/will: 89 sorgu / 2.431 gösterim | 8 post (will, codicil, trust…) | Yüksek (Trust & Will) | Orta | **B+** |
| 6 | Eviction Process & Squatter Laws by State | 599 öneri; 2024–25 yeni yasalar | 7 post (eviction notice, pay-or-quit…) | Orta (DoorLoop, TurboTenant) | Yüksek | **B** |
| 7 | Rent Rules by State (late fee, rent increase, rent cap) | GSC late rent: 167 gösterim, ~49. sıra | 5 post + security deposit serisi (model) | Orta (DoorLoop) | Yüksek | **B** |
| 8 | Contractor License & Lien Deadlines by State | Autocomplete güçlü; CA eşiği 2025'te değişti | 5 post (mechanics lien, lien waiver…) | Orta (NEXT Insurance $25/teklif) | Orta (lien SaaS blogları) | **B** |
| 9 | Non-Compete Laws by State | 2025–26 yoğun yasa değişikliği | 3 post (non-compete template + NDA…) | Düşük–orta (LawDepot) | Orta (hukuk büroları) | **B−** |
| 10 | Employer Compliance by State (final paycheck, sick leave, PTO) | 302 öneri; "paycor/adp" varyantları talep kanıtı | 6 post + remote-work withholding tablosu | Yüksek (Gusto $100–300) | **Çok yüksek** (bordro devleri) | **C+** |

Yedekler: Sales Tax Economic Nexus by State, POA Execution Requirements by State (UPOAA), Vehicle Bill of Sale by State (en doygun olanı, önermiyorum).

---

## 1. Small Claims Court by State — öncelik A

**Neden:** Site bu konuda zaten Google'a "ilgili" görünüyor. Tek bir sayfa (`/small-claims-court-filing-limits-and-fees/`) 90 günde 47 farklı sorguda gösterim aldı: "how much is the filing fee for small claims", "dollar limit for small claims court" gibi, 50–70. sıralarda. Hub'ın tamamlayıcısı olan demand letter serisi var; `final-demand-letter` bazı sorgularda 6. sırada. Bu kullanıcı demand letter yazar, ödeme gelmezse small claims'e gider, kazanırsa tahsilata geçer. Tam bir huni ve içerik boşluğu yok.

**Talep:** "small claims court limit" için 386 öneri var; her eyalet ayrı sorgu (ohio, michigan, florida, colorado…). Ayrıca "small claims court limit by state" ve "what is the dollar amount limit…" soruları.

**Veri (doğrulanmış örnekler):**
- Limitler $2.500 (Kentucky) ile $25.000 (Tennessee, Delaware) arasında. Texas $20.000. California'da bireyler için $12.500, işletmeler için $6.250 ([Nolo 50-state](https://www.nolo.com/legal-encyclopedia/small-claims-suits-how-much-30031.html), [Sue.com 2026](https://www.sue.com/blog/small-claims-court-limits-by-state-2026)).
- Ohio: limit $6.000, dosya ücreti mahkemeye göre ~$35–80, ödeme güçlüğü için affidavit of indigency var ([Ohio Legal Help](https://www.ohiolegalhelp.org/topic/small-claims), [Cleveland Municipal Court](https://clevelandmunicipalcourt.org/clerk-of-courts/civil-division/how-to-file-a-small-claim)).
- New York'ta 2025'te justice court limitini $3.000'den $5.000/$10.000/$15.000'e çıkaran üç ayrı teklif var: [S2636](https://www.nysenate.gov/legislation/bills/2025/S2636), [A3113](https://www.nysenate.gov/legislation/bills/2025/A3113). Yasalaşırsa güncelleme fırsatı.
- Ulusal referans: NCSC, "How small is a small claims case?" ([NCSC, 2023](https://ncsc.contentdm.oclc.org/digital/api/collection/civil/id/233/download)).

**Hub yapısı:**
- Hub: mevcut sayfa genişletilir. 50 eyalet tablosu: limit (birey/işletme), dosya ücreti aralığı, avukat izni, temyiz hakkı, resmi form linki.
- Spoke: `{state}-small-claims-court` (ilk 10 nüfus eyaleti ile başla). Her spoke: limit, ücret, **ilçe bazında** ücret örnekleri, tebligat yöntemi, duruşma süresi, karar sonrası tahsilat (bkz. Dikey 4), resmi form PDF'i.
- Araç: "Small Claims Filing Cost Estimator" (eyalet + talep tutarı → ücret + tebligat maliyeti).

**Para kazanma:** Doğrudan affiliate zayıf. Ama her spoke'un CTA'sı mevcut `/go/lawdepot-payment-demand-letter` slug'ı. Mahkemeden önce demand letter zaten birçok eyalette ilk adım. Huni ve trafik dikeyi.

---

## 2. Small Estate Affidavit & Probate by State — öncelik A

**Neden:** Bulduğum en net hacim kanıtı bu. `small estate affidavit` tek başına **14.800 arama/ay** (Google US). 527 öneri var ve her eyalet ayrı sorgu (virginia, california, illinois, texas, indiana, new york, florida, michigan, arizona…). Hatta ilçe düzeyinde sorgular çıkıyor ("maricopa county", "allegheny county"). Site elinde 7 tohum var: `small-estate-affidavit-template-2026`, `affidavit-of-heirship-template-2026`, `probate-cost-estimator`, `interactive-estate-tax-probate-exposure-quiz`, `estate-tax-by-state`, `transfer-on-death-deed-template-2026`, `how-to-close-a-deceased-persons-accounts…`.

**Veri ve güncellik:**
- Eşikler Rhode Island'da $15.000, Wyoming'de $400.000 (2025'te büyük artış). 2025–2026'da **12'den fazla eyalet eşik değiştirdi** ([Ezel 50-state survey](https://ezel.ai/surveys/small-estate-affidavit-thresholds), [Afterkin](https://www.afterkin.com/blog/articles/small-estate-affidavit-by-state)). Yani rakiplerin tabloları eskiyor; güncel tablo kalıcı avantaj.
- California: $208.850, 2028'e kadar (yukarıdaki resmi kaynaklar). Rakiplerde hatalı $239.700 iddiası var.
- Texas'ın farkı: $75.000 limit (homestead ve muaf mal hariç), vasiyetname olmamalı, ölümden sonra 30 gün beklenir, iki tarafsız tanık ve noter gerekir, **hakim onayı** şart ve ilçeye özel form kullanılır ([TexasLawHelp](https://texaslawhelp.org/article/small-estate-affidavits), [Dallas County formu](https://www.dallascounty.org/Assets/uploads/docs/courts/probate/SmallEstateAffidavitRequiredForm-amended-02282020.pdf)). Her eyaletin böyle "tuzakları" var; spoke içeriği bunlarla dolar.

**Hub yapısı:**
- Hub: "Small Estate Affidavit Limits by State (2026)". Kolonlar: eşik, bekleme süresi, gayrimenkul dahil mi, mahkemeye dosyalanır mı, noter/tanık, resmi form.
- Spoke'lar:
  - `{state}-small-estate-affidavit` (ilk 10: TX, CA, FL, IL, NY, PA, OH, MI, VA, IN; autocomplete sırası bunu destekliyor).
  - Yan spoke: "How long does probate take in {state}".
- Araç: "Do I Need Probate?" karar ağacı (mevcut probate estimator ile bağlanır).

**Para kazanma:**
- [Trust & Will](https://trustandwill.com/affiliate-program) ürün başına %20, ortalama $80, tek satışta $180'e kadar (Impact).
- Mevcut LawDepot estate slug'ları. Açı: "Bir dahaki sefere mirasçılarınız bununla uğraşmasın → living trust".

---

## 3. Divorce by State (ücret, ikamet şartı, bekleme süresi) — öncelik A

**Neden:** Sitenin ikinci büyük organik sinyali. 90 günde 70 boşanma sorgusu ve 1.293 gösterim var, sayfalar 50–89. sırada; Google konuyu siteyle ilişkilendiriyor ama sayfalar zayıf. 9 tohum post var: uncontested divorce, is-online-divorce-worth-it, TX/CA/FL online divorce, divorce-cost-calculator, alimony-calculator-by-state, legal separation, parenting plan, custody, prenup.

**Talep:** "divorce filing fee" için 332 öneri; eyalet ve ilçe varyantları (tarrant county, harris county, maricopa county, colorado, utah…) ve fee waiver soruları.

**Veri:**
- İkamet şartı sıfır günden (Alaska, South Dakota, Washington) 2 yıla (New York bazı durumlarda) kadar; en yaygını 6 ay.
- Örnekler: Texas'ta 6 ay eyalet + 90 gün ilçe ikameti, 60 gün bekleme. California'da tebligattan itibaren 6 ay bekleme, ücret $435. Washington'da 90 gün bekleme ([divorce.law residency](https://divorce.law/learn/residency-requirements/)). Bu rakip programatik; rakamlar mahkeme ücret tablolarıyla **tek tek doğrulanmalı**.

**Hub yapısı:**
- Hub: "Divorce Cost & Requirements by State (2026)". Mevcut `divorce-cost-calculator` hub'a gömülür.
- Spoke'lar: `how-to-file-for-divorce-in-{state}` (ikamet, bekleme, dosya ücreti, fee waiver formu, uncontested yolu, resmi self-help formları).
- İkinci katman: "divorce filing fee {county}" için ilk 20 ilçe bir tabloda.

**Para kazanma:** Doğrulandı. [OnlineDivorce.com](https://www.onlinedivorce.com/affiliates/) satış başına $80, $90 ve $100 kademeli (FlexOffers üzerinden). Alternatifler: CompleteCase, Divorce.com (FlexOffers) ([APDB listesi](https://www.affiliateprogramdb.com/divorce-affiliate-programs/)). Mevcut CLAUDE.md affiliate tablosunda boşanma programı yok. Bu dikey açılırsa önce başvuru yapılmalı.

---

## 4. Judgment Collection, Wage Garnishment & Judgment Interest by State — öncelik B+

**Neden:** Small claims hub'ının (Dikey 1) doğal devamı: "kazandım ama para gelmedi" aşaması. Mevcut `how-to-collect-money-owed`, `statute-of-limitations-on-debt-by-state`, `late-payment-interest-calculator` ve demand letter serisiyle kapalı bir döngü kurar. İki kitleye de hitap eder: alacaklı (nasıl tahsil ederim) ve borçlu (ne kadarı korunur).

**Veri ve güncellik (sürekli):**
- Karar sonrası faiz oranları eyaletten eyalete değişiyor ve **birçoğu değişken**:
  - Minnesota 2026: genel %4, $50.000 üstü kararlar %10 ([MN Courts 2026 PDF](https://mncourts.gov/_media/migration/ciomedialibrary/news-and-public-notices/2026-Interest-Rates-on-State-Court-Judgements.pdf))
  - Texas: 1 Eylül 2026 itibarıyla %6,75 (prime rate'e bağlı, %5 taban, %15 tavan) ([OCCC geçmiş tablo](https://occc.texas.gov/wp-content/uploads/2026/03/PostjudgmentInterestRate_History.pdf))
  - Florida: çeyreklik değişken, 2026 2. çeyrekte %8,25
  - Iowa: 1 yıllık Treasury + %2 ([Iowa Courts](https://www.iowacourts.gov/iowa-courts/district-court/post-judgment-interest-table))
  - Periyodik güncelleme gerektiği için "fresh" içerik avantajı sağlar.
- Maaş haczi korumaları:
  - Federal taban: maaşın %75'i veya haftalık 30 × federal asgari ücret.
  - NCLC'nin 2025 raporunda hiçbir eyalet "A" almadı. AZ, CA, MA, NM, TX "B"; GA, IN, KY, MI, MS, MO, NJ, UT, WY "F" ([NCLC No Fresh Start 2025](https://www.nclc.org/resources/no-fresh-start/), [eyalet özetleri PDF](https://www.nclc.org/wp-content/uploads/2026/01/2025_Report_No-Fresh-Start_State-Summaries.pdf)). Güçlü, alıntılanabilir birincil veri.

**Hub yapısı:**
- Hub A: "Judgment Interest Rates by State (2026)" ve **Judgment Interest Calculator** (mevcut late payment calculator altyapısı yeniden kullanılır).
- Hub B: "Wage Garnishment Limits by State". Spoke'lar: `{state}-wage-garnishment-laws`, "how to collect a small claims judgment in {state}".

**Para kazanma:** Orta. LawDepot demand letter ve settlement slug'ları. Borç rahatlatma affiliate'lerinden **kaçın**: E-E-A-T riski ve YMYL finans hassasiyeti. Değer esasen trafik ve iç linkte.

---

## 5. Will Requirements by State (+ elektronik vasiyet) — öncelik B+

**Neden:**
- GSC'de trust/will kümesi 90 günde 89 sorgu ve **2.431 gösterim** aldı (living trust online sayfası 54–61. sırada).
- Estate planning, sitenin en yüksek komisyonlu alanı (Trust & Will ortalama $80).
- Mevcut vasiyetname şablonunun eyalet geçerlilik sorusu ("is a handwritten will valid in {state}", "does a will need to be notarized in {state}") cevapsız.

**Veri ve güncellik:**
- Uniform Electronic Wills Act'i benimseyenler: Utah, Colorado, North Dakota (2020–21), Washington (2022), Idaho, DC, Minnesota (2023 versiyonu).
- **New York** Electronic Wills Act'i 12 Aralık 2025'te çıkardı, yürürlük **10 Haziran 2027** ([Rivkin Radler](https://www.rivkinradler.com/publications/new-york-electronic-wills-act-enacted-not-yet-effective/)).
- **Minnesota**'nın e-will yasası 1 Ağustos 2026'da yürürlüğe girdi ([MN House](https://www.house.mn.gov/NewLaws/story/2026/5696)).
- North Carolina 2026'da elektronik vasiyet saklama kuralı getirdi ([Wake Forest Law Review](https://www.wakeforestlawreview.com/2026/02/north-carolinas-new-electronic-will-storage-law-a-step-towards-modernizing-estate-planning/)).
- Toplam 15 eyalet ve DC e-will'e izin veriyor ([Nolo e-wills](https://www.nolo.com/legal-encyclopedia/what-is-an-electronic-will.html)).

**Hub yapısı:**
- Hub tablo kolonları: tanık sayısı, noter, self-proving affidavit, holografik (el yazısı) vasiyet geçerli mi, e-will yasası, resmi statute.
- Spoke'lar: `how-to-make-a-will-in-{state}`, "holographic will {state}".
- Yan konu: "Living trust vs will in {state}" (probate eşiği Dikey 2'den gelir, çapraz link).

**Para kazanma:** Trust & Will (%20, Impact) ve mevcut `lawdepot-last-will` / `lawdepot-living-trust`.

---

## 6. Eviction Process, Timeline & Squatter Laws by State — öncelik B

**Neden:** Landlord kitlesi sitenin en geniş şablon tabanı (eviction notice, pay-or-quit, notice to vacate, lease violation, file-an-eviction-online, compliance table). Ama sürecin **zaman çizelgesi ve maliyeti** eyalet bazında yok. "eviction process" için 599 öneri var: texas, florida, california, nc, ohio, michigan, arizona… ve "after 3 day notice", "after 30 day notice" gibi süreç soruları.

**Güncellik kancası — squatter yasaları:**
- 2024'te AL, FL, GA, TN, WV squatting'i suç yaptı ve hızlı tahliye prosedürü getirdi. Georgia HB 1017 ile polis, geçerli kira sözleşmesi göstermeyen işgalciyi 3 günde çıkarabiliyor.
- ALEC Temmuz 2024'te model "Stop Squatters Act" yayımladı.
- **Arkansas HB 1049** 4 Mart 2025'te imzalandı ([Rolling Stone analizi](https://www.rollingstone.com/politics/politics-features/red-states-crack-down-squatters-alec-1235404301/), [iPropertyManagement](https://ipropertymanagement.com/laws/squatters-rights)). Eyaletler hâlâ yasa çıkarıyor; iyi bir haber/güncelleme kancası.
- Bildirim süreleri: ödenmeyen kirada 0 gün (West Virginia) ile 30 gün (New Jersey) arası, çoğu 3–14 gün. Aydan aya kiracılıkta 7 günden (NC) 60 güne (DE, GA, MD) ([Eviction Research Network – atıflı veri seti](https://evictionresearch.net/state-eviction-timeframes/)). Bu veri seti statute atıfları ve yürürlük tarihleri içeriyor, birincil kaynak doğrulaması için ideal başlangıç.

**Hub yapısı:**
- Hub: "Eviction Timeline by State". Kolonlar: bildirim, dava açma → duruşma, karar → tahliye emri, toplam asgari süre, dosya ücreti.
- Spoke'lar: `eviction-process-in-{state}`, `squatters-rights-{state}` (önce 2024–25'te yasa çıkaran 6 eyalet).

**Para kazanma:** DoorLoop (Impact, mevcut) ve [TurboTenant affiliate](https://www.turbotenant.com/affiliates/) (FlexOffers; oran açıklanmıyor). LawDepot eviction slug'ı mevcut.

---

## 7. Rent Rules by State: Late Fees, Rent Increases & Rent Caps — öncelik B

**Neden:**
- `late-rent-notice-template` 90 günde "rent late fee policy template" gibi sorgularda 167 gösterim aldı (~49. sıra). Kullanıcı "ne kadar geç ödeme ücreti alabilirim" diye soruyor; cevap eyalete bağlı.
- Site elinde başarılı bir **eyalet-tablo modeli** var: security deposit serisi (limits, interest, calculator, return letter). Aynı kalıp late fee ve rent increase için kopyalanabilir.

**Veri ve güncellik:**
- Late fee: 27 eyalette yasal tavan yok, "makul olma" standardı var.
  - Maine: %4 ve zorunlu 15 gün ek süre (ülkedeki en düşük yüzde).
  - Texas: 1–4 daireli binalarda %12.
  - New York: $50 ya da %5, hangisi düşükse.
  - Seattle: eyalet tavanı olmamasına rağmen %10 ve 14 gün ek süre ([Landlord Studio](https://www.landlordstudio.com/blog/a-state-by-state-guide-to-late-fees)).
- **Washington HB 1217** (7 Mayıs 2025): yıllık kira artışı "%7 + CPI veya %10, hangisi düşükse". İlk 12 ayda artış yasak. Commerce Bakanlığı her yıl tavanı yayımlıyor ([WA Commerce](https://www.commerce.wa.gov/housing-policy/hb1217-landlord-resource-center/), [WA AG](https://www.atg.wa.gov/landlord-tenant)). Yıllık güncellenen resmi rakam, yani sürekli fresh içerik.

**Hub yapısı:**
- Hub A: "Late Fee Laws by State" + **Late Fee Calculator** (mevcut prorated rent ve security deposit calculator stili).
- Hub B: "Rent Increase Laws by State" (bildirim süresi, rent control/stabilization eyaletleri: OR, WA, CA AB1482).
- Spoke'lar: `{state}-rent-increase-laws`. Mevcut `rent-increase-notice-letter-template-2026` ve `late-rent-notice-template` hub'a bağlanır.

**Para kazanma:** DoorLoop / TurboTenant (online kira tahsilatı ve otomatik late fee özelliği ile doğal CTA).

---

## 8. Contractor License Thresholds & Construction Payment (Lien) Deadlines by State — öncelik B

**Neden:**
- Sitenin küçük ama somut bir inşaat kümesi var: `how-to-file-mechanics-lien-online` (GSC'de "file mechanic's lien online" ~49. sıra), `lien-waiver-release-form…`, `demand-letter-to-contractor`, `construction-equipment-rental-agreement`, independent contractor agreement.
- Kitle **küçük işletme sahibi** (handyman / taşeron), yani yüksek niyetli B2B.

**Veri ve güncellik:**
- Çoğu eyalette ayrı bir handyman lisansı yok. Bunun yerine iş başına bir dolar eşiği var (tipik olarak $500–10.000); altındaki işler lisanssız yapılabiliyor.
- **California AB 2622**: 1 Ocak 2025'ten itibaren lisanssız iş eşiği $500'den **$1.000'e** çıktı. Ama iş izin gerektiriyorsa ya da işçi çalıştırılıyorsa lisans şart. İşler bölünemiyor (toplam tutar sayılıyor). İlanlarda "lisanssız" beyanı zorunlu ([CSLB bülteni](https://www.cslb.ca.gov/Resources/IndustryBulletins/2024/AB%202622%20Implementation.FINAL.pdf), [USD CPIL](https://sites.sandiego.edu/cpil-blog/2024/10/09/governor-signs-bill-increasing-minor-work-exemption-for-unlicensed-contracting-from-500-to-1000/)). Birçok rakip hâlâ "$500" yazıyor.
- Lien süreleri:
  - Kayıt süresi Hawaii'de son teslimattan itibaren 45 gün, New York'ta 240 gün; çoğu eyalette 60–120 gün.
  - 30'dan fazla eyalet ön bildirim (preliminary notice) istiyor. CA, MI, FL ve MN'de bildirim yapılmazsa lien hakkı tamamen kayboluyor ([CNS](https://cnslien.com/2026/01/16/when-is-the-deadline-to-file-a-mechanics-lien/), [SubShield](https://www.trysubshield.com/blog/mechanics-lien-deadlines-by-state)).

**Hub yapısı:**
- Hub A: "Handyman / Contractor License Requirements by State".
- Hub B: "Mechanics Lien Deadlines by State" + **Lien Deadline Calculator** (son teslimat tarihi girilince eyalet bazında son gün).
- Spoke'lar: `{state}-contractor-license-requirements`, `{state}-mechanics-lien-deadlines`.

**Para kazanma:** [NEXT Insurance](https://www.nextinsurance.com/become-a-next-insurance-affiliate/): nitelikli teklif başına $25, 30 gün cookie, Impact (mevcut hesapla aynı ağ). Lisans başvurularında sigorta/bond zorunlu olduğundan CTA doğal duruyor.

---

## 9. Non-Compete Laws by State — öncelik B−

**Neden:**
- `free-non-compete-agreement-template-state-enforceability-2026` zaten eyalet geçerliliğini başlığa koymuş ama tek sayfa. Hukuk bu alanda çok hızlı değişiyor; **güncel olan kazanıyor**.
- Hacim diğerlerinden düşük, ama işveren ve çalışan niyeti yüksek.

**Güncellik (2025–2026):**
- **FTC** Eylül 2025'te temyizini geri çekti; federal yasak tamamen bitti.
- **Wyoming SF 107** (2025): çalışan non-compete'lerinin çoğu geçersiz. İşletme satışı ve ticari sır istisnaları var.
- **Florida CHOICE Act** (1 Temmuz 2025): yüksek ücretlilerde 4 yıla kadar non-compete ve garden leave'e izin veriyor. Ülkedeki trendin tersi.
- **Virginia SB 170** (1 Temmuz 2026): işveren sebepsiz işten çıkarır ve önceden açıklanmış kıdem tazminatını ödemezse non-compete uygulanamaz. 2025'te "low-wage employee" tanımı FLSA fazla mesai hakkı olanların tümünü kapsayacak şekilde genişledi ([Foley 2026 overview](https://www.foley.com/insights/publications/2026/07/noncompete-agreements-federal-state-overview/), [Epstein Becker Green – VA SB170](https://www.tradesecretsandemployeemobility.com/virginia-approves-sb170-expanded-restrictions-on-enforcement-of-noncompetes-take-effect-july-1-2026), [Duane Morris – VA & WY](https://www.duanemorris.com/alerts/virginia_wyoming_latest_states_tighten_restrictions_noncompete_agreements_0425.html)).

**Hub yapısı:**
- Mevcut şablon hub'a dönüşür. Tablo kolonları: yasak / ücret eşiği / süre sınırı / bildirim şartı / son değişiklik tarihi.
- Spoke'lar: `{state}-non-compete-laws` (önce CA, TX, FL, NY, VA, WY, MN, IL, WA, CO).
- İçerik: "Non-compete vs non-solicitation" (mevcut freelancer non-solicitation ile bağlanır).

**Para kazanma:** Düşük–orta. LawDepot non-compete/NDA slug'ları. Asıl değeri, yüksek komisyonlu işveren kümesine (Dikey 10) iç link otoritesi.

---

## 10. Employer Compliance by State: Final Paycheck, Paid Sick Leave, PTO Payout — öncelik C+

**Neden:**
- Affiliate açısından en değerli dikey: Gusto, [PartnerStack](https://market.partnerstack.com/program/gusto) üzerinden referans başına ~$100–300 ödüyor (doola ile aynı ağ, mevcut hesap).
- Site tohumları: employment contract, offer letter, separation agreement, adverse action notice, misclassification quiz ve zaten eyalet bazlı olan `state-by-state-remote-work-tax-withholding-table`.

**Neden düşük öncelik:** SERP'te bordro şirketlerinin kendi 50 eyalet rehberleri var (Paycor, Paycom, Rippling, Patriot, ADP), yüksek otoriteyle ([Paycor](https://www.paycor.com/resource-center/articles/final-paycheck-laws-by-state/), [Patriot](https://www.patriotsoftware.com/blog/payroll/final-paycheck-laws-by-state/)). "paycor final paycheck laws by state" gibi markalı autocomplete sorguları, kullanıcının bu markalara gittiğinin kanıtı. Ancak **uzun kuyruk** eyalet sorguları ("indiana final paycheck laws", "ct final paycheck laws") ve çalışan tarafı ("son maaşımı alamadım, ne yapmalıyım" → demand letter) boşta.

**Güncellik:**
- **Nebraska**: paid sick leave 1 Ekim 2025'te yürürlüğe girdi (11+ çalışan; 30 saatte 1 saat; 40/56 saat tavan; LB 415) ([NDOL](https://dol.nebraska.gov/PressRelease/Details/335), [LB 415](https://nebraskalegislature.gov/FloorDocs/109/PDF/Slip/LB415.pdf)).
- **Missouri**: seçmen onaylı yasa 28 Ağustos 2025'te yürürlükten kaldırıldı.
- **Connecticut**: 1 Ocak 2026'da 11+ çalışana genişledi, 2027'de tüm işverenleri kapsayacak ([Womble Bond Dickinson](https://www.womblebonddickinson.com/us/insights/alerts/state-leave-laws-continue-expand-2026-what-multistate-employers-should-know)).
- AL, FL, GA, MS'de ayrı bir final paycheck yasası yok; FLSA tabanı geçerli.

**Açı (farklılaşma):** İşveren değil **çalışan** tarafı. "Final paycheck late in {state}? Penalties + demand letter" → mevcut demand letter kümesine bağlanır. İşveren tarafı (Gusto CTA) ikinci katman.

---

## Yedek dikeyler (kısa)

- **Sales Tax Economic Nexus by State**:
  - Çok güncel: 17+ eyalet 200 işlem eşiğini kaldırdı. Illinois 1 Ocak 2026, Iowa ve Wisconsin 1 Ocak 2026, Kentucky 1 Ağustos 2026, Alaska 2025, Utah 2025 ([Avalara](https://www.avalara.com/blog/en/north-america/2025/06/states-eliminating-economic-nexus-transaction-thresholds.html), [TaxCloud](https://taxcloud.com/blog/sales-tax-nexus-by-state/)).
  - Mevcut `how-to-get-a-sellers-permit-online-by-state-2026` ve online store postlarıyla uyumlu.
  - Rekabet: vergi yazılımı şirketlerinin kendi rehberleri.
- **POA Execution Requirements by State**:
  - UPOAA 26–31 eyalet ve DC'de benimsendi ([ULC](https://www.uniformlaws.org/committees/community-home?CommunityKey=b1975254-8370-4a7c-947f-e5af0d6cb07c)).
  - Tanık ve noter şartları eyalete göre değişiyor.
  - Mevcut general/medical POA ve revocation şablonlarıyla uyumlu.
  - Para: Proof/Notarize referral ([terms](https://www.proof.com/legal/affiliate-partner-terms)).
- **Vehicle Bill of Sale by State**: önermiyorum. DMV programatik siteleriyle çok doygun (carpaperwork, billofsalenow…) ve affiliate zayıf.

---

## Önerilen uygulama sırası (LLC eyalet işiyle paralel)

1. **Ekim–Kasım:** Dikey 2 (Small Estate) ve Dikey 1 (Small Claims). Hub + 10 eyalet spoke'u her biri için. En güçlü talep ve site sinyali bunlarda.
2. **Aralık:** Dikey 3 (Divorce). Önce OnlineDivorce/CompleteCase affiliate başvurusu. Ocak'taki "boşanma ayı" sezonundan önce yayında olmalı.
3. **Ocak 2027:** Dikey 4 (Judgment interest + garnishment). Ocak'ta birçok eyalet yeni faiz oranı yayımlıyor, yayın zamanı ideal. Yıl başı "2027" başlık güncellemesiyle birleştir.
4. **Q1 2027:** Dikey 5, 6, 7 (estate + landlord).
5. **Q2 2027:** Dikey 8, 9, 10.

**Her hub için şablon kontrol listesi:**
- Birincil kaynaklı 50 eyalet tablosu, satır başına "Verified" tarihi.
- Resmi form linki; ilçe istisnaları notu.
- Hesaplayıcı veya karar aracı.
- Mevcut postlara en az 5 iç link; hub ↔ spoke çift yönlü link.
- FAQPage schema.
- Değişken veri için yıllık/çeyreklik güncelleme hatırlatıcısı (small estate eşikleri, judgment faizleri, WA rent cap, sick leave).

## Bir sonraki doğrulama adımları

- Google Keyword Planner ile şu kalıpların eyalet bazlı hacmini çek: `{state} small claims court limit`, `small estate affidavit {state}`, `how to file for divorce in {state}`, `{state} wage garnishment laws`, `{state} late fee laws`, `{state} contractor license requirements`.
- Hedef affiliate'lere başvur: Trust & Will (Impact), OnlineDivorce (FlexOffers), NEXT Insurance (Impact), Gusto (PartnerStack).
- Her hub yayınından 4–6 hafta sonra Supermetrics GSC ile hub ve spoke gösterim/sıralama ölçümü.
