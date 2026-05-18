# ClearLegalTips — Claude Code Proje Bağlamı

## Site Bilgileri

| Alan | Değer |
|---|---|
| Domain | clearlegaltips.com |
| WordPress Studio (local) | C:\Users\fatih\Studio\clearlegaltips |
| Local URL | http://localhost:8881 |
| WP REST API (local) | http://localhost:8881/wp-json/wp/v2/ |
| WP-CLI | C:\Users\fatih\AppData\Local\studio_app\bin\studio.bat |
| PHP scriptleri | C:\Users\fatih\Studio\clearlegaltips\wp-content\ |
| SEO Eklentisi | Rank Math |
| Tema | Kadence |
| Affiliate Link Yönetimi | ThirstyAffiliates (prefix: /recommend/) |

## WP-CLI Kullanımı

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

## Yazarlar

| ID | Ad | Uzmanlık |
|---|---|---|
| 291 | Sarah Jenkins | Family law, estate planning |
| 292 | Marcus Thorne | Business law, contracts |
| 293 | Elena Rodriguez | Real estate, landlord-tenant |
| 294 | David Miller | Small business, LLC formation |

## İçerik Yapısı

- **Toplam makale:** 50 (Post ID 131–180), tümü yayında
- **Tarih aralığı:** 1 Nisan – 25 Nisan 2026 (staggered)
- **Kategoriler:** 5 adet
- **Etiketler:** 35 adet
- **PDF indirilebilir doküman:** 20 adet (Post 131–150'ye bağlı)
- **ThirstyAffiliates linki:** 38 adet (şu an placeholder '#')

## Post ID Haritası (Kategori Grupları)

| Grup | Post ID Aralığı | İçerik Tipi |
|---|---|---|
| Template articles | 131–150 | Legal document templates |
| Cost/calculator articles | 151–165 | Fee guides & calculators |
| How-to guides | 166–175 | Step-by-step online services |
| State/specialty guides | 176–180 | State-specific legal guides |

## İçerik Standartları

- **Minimum kelime sayısı:** 3000 (tüm makaleler bu limiti karşılıyor)
- **Hedef kitle:** ABD'de hukuki DIY işlemler yapan genel halk
- **Ton:** Açık, profesyonel — hukuki tavsiye değil bilgi
- **Zorunlu elementler:**
  - FTC disclosure kutusu (`<div class="clt-disclosure">`) — her makalenin üstünde
  - Legal disclaimer (`<div class="clt-disclaimer">`) — her makalenin altında
  - Internal link box (`<div class="clt-related-articles">`) — 3 link, hub-spoke map'e göre
  - CTA button (`<a class="clt-affiliate-btn">`) — ThirstyAffiliates /recommend/ formatı

## CSS Sınıfları

| Sınıf | Kullanım |
|---|---|
| `clt-affiliate-btn` | Crimson CTA buton |
| `clt-cta-box` | CTA bölümü container |
| `clt-article-img` | Makale içi görseller |
| `clt-disclosure` | FTC disclosure kutusu |
| `clt-disclaimer` | Legal disclaimer kutusu |
| `clt-related-articles` | Internal link box |

## Rank Math SEO Konvansiyonları

Her post şunlara sahip olmalı:
- `rank_math_focus_keyword` — birincil keyword
- `rank_math_description` — meta description (155 karakter max)
- Featured image (1200×630px JPG, tüm 50 makalede mevcut)

## ThirstyAffiliates Link Formatı

```html
<a href="/recommend/lawdepot" class="clt-affiliate-btn" rel="nofollow sponsored">
  Start with LawDepot →
</a>
```

Mevcut placeholder linkler `'#'` destination ile kayıtlı — gerçek affiliate URL'leri onaylanınca ThirstyAffiliates Link Manager'dan güncellenecek.

## Hedef Affiliate Programlar (Başvuru Bekliyor)

| Program | Platform | Komisyon |
|---|---|---|
| LawDepot | Impact | ~30% |
| ZenBusiness | ShareASale / Direct | ~$100-150/sale |
| Northwest Registered Agent | ShareASale | ~$100/sale |
| Rocket Lawyer | CJ Affiliate | ~$30/sale |
| LegalZoom | CJ Affiliate | ~$15-30/sale |
| Nolo | Direct | ~10-15% |
| Incfile | Direct | ~$75/sale |

## İçerik İpuçları

- `insert_before_footer()` helper fonksiyonu: `.clt-related-articles` veya `.clt-disclaimer` div'inden önce içerik ekler
- `wp_update_post()` + `clean_post_cache()` → post güncelleme sonrası cache temizleme zorunlu
- `str_word_count(strip_tags($content))` → doğru kelime sayısı ölçümü
- WP Fastest Cache aktif — içerik değişikliği sonrası cache flush gerekebilir

## Çalışma Kuralları

1. PHP scriptleri yazmadan önce mevcut expand-*.php scriptlerini referans al
2. Yeni makale eklerken staggered tarihleri koru (sıradaki tarih: 26 Nisan 2026)
3. Affiliate link eklerken her zaman ThirstyAffiliates slug kullan, doğrudan URL değil
4. Featured image boyutu: 1200×630px JPG, dosya adı: `post-{id}-{slug}.jpg`
5. Rank Math alanları PHP üzerinden: `update_post_meta($pid, 'rank_math_focus_keyword', $kw)`

## Eklentiler (Aktif)

- Rank Math SEO
- ThirstyAffiliates
- Simple Local Avatars
- WP Fastest Cache
- Complianz GDPR (US/CCPA)
- Kadence Blocks

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
├── articles/          50 makale markdown dosyası
├── templates/         20 legal template markdown
├── images/            Logo, yazar fotoğrafları
├── site-setup/        Plugin kurulum rehberi
├── OPERATIONS_MANUAL.md
├── CLAUDE_CODE_WORDPRESS_REFERENCE.md
├── SETUP_CHECKLIST.md (MCP kurulum kılavuzu)
└── liste.md           Claude Code araç listesi (Türkçe)
```
