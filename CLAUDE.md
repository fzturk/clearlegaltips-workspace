# ClearLegalTips — Claude Code Proje Bağlamı

> **Son doğrulama:** 24 Eylül 2026. Değerler canlı sitenin REST API'si (`/wp-json/wp/v2/`) taranarak alındı.
> Rakamlar değiştikçe bu dosyayı güncelle; şüphede kalırsan önce canlı siteyi kontrol et.

## Site Bilgileri

| Alan | Değer |
|---|---|
| Domain | clearlegaltips.com (canlı, yayında) |
| Hosting | WordPress.com (Atomic) + Cloudflare, HTTPS |
| Canlı REST API | https://clearlegaltips.com/wp-json/wp/v2/ |
| WordPress Studio (local, geliştirme kopyası) | C:\Users\fatih\Studio\clearlegaltips — http://localhost:8881 |
| WP-CLI (local) | C:\Users\fatih\AppData\Local\studio_app\bin\studio.bat |
| PHP scriptleri (local) | C:\Users\fatih\Studio\clearlegaltips\wp-content\ |
| SEO Eklentisi | Rank Math |
| Tema | Kadence |
| Affiliate link formatı | `/go/{slug}` → 302 redirect (bkz. aşağıdaki liste) |

> Local Studio kopyası canlı siteyle senkron olmayabilir. Canlı içerik değişikliklerini canlı site üzerinden yap veya önce senkronu doğrula.

## WP-CLI Kullanımı (local)

```powershell
# Doğru kullanım — relative path ile eval-file
C:\Users\fatih\AppData\Local\studio_app\bin\studio.bat wp eval-file wp-content\script.php --path="C:\Users\fatih\Studio\clearlegaltips" 2>&1 | Select-String -NotMatch "Warning:"
```

## Tema Renkleri (Kadence)

| Renk | Hex | Kullanım |
|---|---|---|
| Navy | #1C2B4A | Primary, header, footer background |
| Crimson | #C0392B | CTA buttons, accents |
| Cream | #F8F6F2 | Body background |

## Yazar / Editör

Sitede **tek kullanıcı** var. Kurgusal yazar profilleri (Sarah Jenkins, Marcus Thorne, Elena Rodriguez, David Miller) **kaldırıldı — tekrar kullanma.**

| Kullanıcı | Rol |
|---|---|
| ClearLegalTips | Tüm postların yazarı. Bio: bağımsız yayıncı; her makale kurucu ve editör **Fatih Öztürk** tarafından gözden geçirilir, resmi kaynaklara karşı fact-check edilir. "Not a law firm; nothing here is legal advice." |

**E-E-A-T kuralları:**
- Uydurma kişi, unvan, kariyer veya "attorney-reviewed" iddiası **asla** ekleme.
- Güven sinyali = gerçek kaynaklar (statute, mahkeme ücret tabloları, SOS/IRS sayfaları) + "Reviewed by" / "Fact-checked: {Ay Yıl}" satırları.
- Editör sayfası: `/editor-fatih-ozturk/`, Editorial standards: `/editorial-standards/`

## İçerik Durumu

| Metrik | Değer |
|---|---|
| Yayındaki post | **167** (Post ID 131 – 7570, ardışık değil) |
| Yayın aralığı | 4 Mayıs – 31 Temmuz 2026 (Mayıs 80, Haziran 38, Temmuz 49) |
| Son yeni post | 31 Temmuz 2026 |
| Son toplu güncelleme | Ağustos 2026 (tüm postlar) |
| Kelime sayısı | min ~1.900, medyan ~3.050, max ~5.400 |
| Sayfa | 12 |
| Medya | ~3.390 |

### Kategoriler

| Kategori | Post |
|---|---|
| Legal Templates | 112 |
| Filing Guides | 26 |
| Business Calculators | 15 |
| Estate & Family | 12 |
| Reviews & Comparisons | 2 |

### Etiketler
- 476 etiket var, **361'i boş** (temizlenecek). Post başına 3–4 etiket kullan.
- Tag arşivleri `noindex` (Rank Math) — böyle kalsın.

### Sayfalar
home, blog, about-clearlegaltips, editor-fatih-ozturk, editorial-standards, contact, affiliate-disclosure, legal-disclaimer, privacy-policy, cookie-policy, terms-of-use, opt-out-preferences

### Son içerik kümeleri (Temmuz 2026)
- Demand letter serisi (payment, contractor, unpaid invoice, loan, breach of contract, final demand) + "How to Collect Money Owed"
- LLC filing fee eyalet serisi: California, Texas, Florida, New York → diğer eyaletlere genişletilebilir
- Statute of limitations on debt, late payment interest calculator, security deposit calculator

## İçerik Standartları

- **Hedef kitle:** ABD'de hukuki işlemlerini kendisi yapan genel halk
- **Ton:** Açık, sade İngilizce, profesyonel — hukuki tavsiye değil bilgi
- **Uzunluk:** Hedef ~3.000 kelime; sınır değil, konu gerektirdiği kadar (mevcut min ~1.900)
- **Başlık kalıbı:** `{Konu}: Free Template (2026)` / `{Konu} (2026): {somut rakam}` — yıl değişiminde (Ocak 2027) toplu güncelleme gerekir
- **Zorunlu elementler (167/167 postta mevcut):**
  - FTC disclosure kutusu (`clt-disclosure`) — en üstte, ilk affiliate linkten önce
  - Download box (`clt-download-box`) — şablon indirme alanı
  - CTA kutusu + buton (`clt-cta-box` + `clt-affiliate-btn`) — `/go/` linki
  - Internal link box (`clt-related-articles`) — 3 link
  - Legal disclaimer (`clt-disclaimer`) — en altta
  - FAQPage schema (post içinde JSON-LD)
- **Kaynak gösterme:** Resmi kaynaklara dış link ver (law.cornell.edu, irs.gov, eyalet legislature/SOS/court siteleri).

## CSS Sınıfları (canlı sitede kullanılan)

| Sınıf | Kullanım |
|---|---|
| `clt-disclosure` | FTC disclosure kutusu |
| `clt-disclaimer` | Legal disclaimer kutusu |
| `clt-related-articles` | Internal link box |
| `clt-cta-box`, `clt-cta-text` | CTA bölümü container + metin |
| `clt-affiliate-btn` | Crimson CTA buton |
| `clt-download-box`, `clt-download-title`, `clt-download-sub`, `clt-download-grid`, `clt-dl-btn` | Şablon indirme alanı |
| `clt-inline-image` | Makale içi görseller |
| `clt-table` | Tablolar |
| `clt-keytakeaway` | Key takeaway kutusu |
| `clt-sources` | Kaynak listesi |
| `clt-callout`, `clt-template-box` | Vurgu / şablon önizleme kutuları |

## Rank Math SEO Konvansiyonları

Her post şunlara sahip olmalı:
- `rank_math_focus_keyword` — birincil keyword
- `rank_math_description` — meta description (155 karakter max)
- Featured image (tüm 167 postta mevcut)

## Affiliate Linkler (`/go/` — aktif)

Format:
```html
<a href="/go/lawdepot-non-disclosure-agreement" class="clt-affiliate-btn" rel="nofollow sponsored">
  Start with LawDepot →
</a>
```

Her zaman `/go/` slug kullan, doğrudan affiliate URL yazma. Yeni slug gerekiyorsa önce redirect'i oluştur, sonra linkle.

| Program | Ağ | Slug(lar) |
|---|---|---|
| LawDepot | CJ Affiliate | `lawdepot`, `lawdepot-business`, `lawdepot-realestate`, `lawdepot-family`, `lawdepot-estate`, `lawdepot-equipment-rental` + belge bazlı ~36 slug (ör. `lawdepot-last-will`, `lawdepot-living-trust`, `lawdepot-llc-operating-agreement`, `lawdepot-residential-lease`, `lawdepot-eviction-notice`, `lawdepot-payment-demand-letter`, `lawdepot-non-disclosure-agreement`, `lawdepot-power-of-attorney`, `lawdepot-quitclaim-deed`, `lawdepot-prenuptial-agreement` …) |
| doola | PartnerStack | `doola` |
| Termly | Impact | `termly` |
| DoorLoop | Impact | `doorloop` |
| Keeper Tax | go2cloud (HasOffers) | `keeper-tax` |
| Diğer | — | `shopify`, `signeasy`, `nordvpn`, `nordprotect` |

Tam liste: canlı postlardaki `/go/` linkleri (47 slug, Eylül 2026).

## Monetizasyon Durumu

- Affiliate: aktif (yukarıdaki programlar)
- Display reklam: **yok** (AdSense / Mediavine / Ezoic kodu yok) — trafik eşiğine göre başvuru değerlendirilecek

## Ölçüm

- Haftalık sıralama ölçümü Routine olarak çalışıyor ("Clearlegaltips haftalik siralama", PC'ye bağlı Remote Control oturumu). PC kapalıysa çalışmaz (28 Ağustos'ta `computer_unreachable`).
- GSC / GA4 / PageSpeed MCP'leri `.mcp.json`'da tanımlı; bulut oturumlarında bağlantı yok.

## İçerik İpuçları

- `insert_before_footer()` helper fonksiyonu: `.clt-related-articles` veya `.clt-disclaimer` div'inden önce içerik ekler
- `wp_update_post()` + `clean_post_cache()` → post güncelleme sonrası cache temizleme zorunlu
- `str_word_count(strip_tags($content))` → doğru kelime sayısı ölçümü
- Canlı site Cloudflare + WordPress.com Batcache arkasında — değişiklik sonrası cache birkaç dakika gecikebilir

## Çalışma Kuralları

1. PHP scriptleri yazmadan önce mevcut expand-*.php scriptlerini referans al
2. Yeni postlar gerçek yayın tarihiyle yayınlanır — geriye tarihleme yapma
3. Affiliate link eklerken her zaman `/go/` slug kullan, doğrudan URL değil
4. Featured image: 1200×630px JPG, dosya adı: `post-{id}-{slug}.jpg`
5. Rank Math alanları PHP üzerinden: `update_post_meta($pid, 'rank_math_focus_keyword', $kw)`
6. Yeni post kategorisi mevcut 5 kategoriden biri olmalı; yeni etiket açmadan önce mevcutları kontrol et
7. Kurgusal yazar/uzman/avukat iddiası yok (bkz. Yazar / Editör)

## Eklentiler (canlı sitede tespit edilen)

- Rank Math SEO
- Jetpack (WordPress.com)
- Kadence tema (+ Kadence Blocks)
- `/go/` redirect yöneticisi (eklenti adı doğrulanmadı)

> Local Studio kopyasında ayrıca ThirstyAffiliates, Simple Local Avatars, WP Fastest Cache, Complianz vardı; canlıda aktif olup olmadıkları doğrulanmadı.

## Görsel Üretim — ComfyUI

| Alan | Değer |
|---|---|
| ComfyUI URL | http://127.0.0.1:8000 |
| Varsayılan Model | juggernautXL_ragnarokBy.safetensors |
| Diğer Modeller | cyberrealisticXL_v100, flux1-dev-bnb-nf4-v2, flux1-schnell-fp8, sd_xl_base_1.0 |
| Donanım | CPU (RAM ~64GB) |
| Üretim Süresi | ~3-10 dakika / görsel (20 step) |
| Çıktı Boyutu | 1216×640 → PIL ile 1200×630'a yeniden boyutlandırılır |
| Helper Script | workspace/tools/comfyui_generate.py |
| Çıktı Dizini | workspace/generated-images/ |

**Kullanım:**
```bash
python3 workspace/tools/comfyui_generate.py \
  --prompt "professional NDA legal document, pen on paper, navy blue" \
  --output "workspace/generated-images/post-131-nda-featured.jpg"
```

**Skill:** `/generate-featured-image "NDA template article"`

---

## Workspace Yapısı

```
workspace/
├── articles/          İlk 50 makalenin markdown taslakları (Mayıs 2026 — canlı versiyonlar daha güncel)
├── articles.md        1.000 makalelik master plan (57 küme)
├── templates/         20 legal template markdown
├── images/            Logo, eski yazar fotoğrafları (kullanılmıyor)
├── site-setup/        Plugin kurulum rehberi (Mayıs 2026)
├── tools/             ComfyUI, PDF üretimi, affiliate e-posta şablonları
├── OPERATIONS_MANUAL.md   (Mayıs 2026 — /recommend/ ve 4 yazar bilgisi eskidi)
├── CLAUDE_CODE_WORDPRESS_REFERENCE.md
├── SETUP_CHECKLIST.md (MCP kurulum kılavuzu)
└── liste.md           Claude Code araç listesi (Türkçe)
```

> `workspace/` altındaki Mayıs 2026 dokümanları tarihsel referanstır. Canlı siteyle çelişirse bu CLAUDE.md ve canlı site esas alınır.
