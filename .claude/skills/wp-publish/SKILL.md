---
name: wp-publish
description: Hazır makaleyi WordPress'e yükler. "Yayınla", "WordPress'e gönder", "post oluştur", "draft yap" gibi taleplerde kullan.
allowed-tools: Read Bash
effort: medium
---

ClearLegalTips.com WordPress sitesine makale yükle.

## Giriş: $ARGUMENTS
Format: "dosya_yolu | post_id (opsiyonel)" veya "makale başlığı"

## Ön Koşul: WP Studio Çalışıyor Olmalı
http://localhost:8881 erişilebilir olmalı.

---

## Seçenek A — WP-CLI ile Yükle (Local Studio)

### 1. Makale Dosyasını Oku
`workspace/articles/` altındaki .md dosyasını oku.

### 2. Post Meta Bilgilerini Belirle

Makaleden şunları tespit et:
- **Başlık** (H1 veya dosya adından)
- **Kategori** — şu 5 kategoriden birini seç:
  - Legal Document Templates (ID: tespit et)
  - Business & LLC (ID: tespit et)
  - Cost Guides & Calculators (ID: tespit et)
  - How-to Guides (ID: tespit et)
  - State-Specific Guides (ID: tespit et)
- **Etiketler** — içerikten uygun etiketleri seç
- **Focus keyword** — H1'den çıkar
- **Meta description** — 150-155 karakter

### 3. WP-CLI Post Oluştur

```powershell
# Yeni post oluştur (draft olarak)
$WPCLI = "C:\Users\fatih\AppData\Local\studio_app\bin\studio.bat"
$WP_PATH = "C:\Users\fatih\Studio\clearlegaltips"

& $WPCLI wp post create `
  --post_title="BAŞLIK" `
  --post_content="İÇERİK" `
  --post_status="draft" `
  --post_author="291" `
  --post_date="2026-04-26 10:00:00" `
  --porcelain `
  --path="$WP_PATH"
```

```powershell
# Meta verileri ayarla
$POST_ID = "YUKARIDAKI_ID"
& $WPCLI wp post meta update $POST_ID rank_math_focus_keyword "KEYWORD" --path="$WP_PATH"
& $WPCLI wp post meta update $POST_ID rank_math_description "META DESC" --path="$WP_PATH"
& $WPCLI wp post term add $POST_ID category KATEGORİ_ID --path="$WP_PATH"
```

### 4. Featured Image Yükle (varsa)

```powershell
# Görsel media library'e import et ve featured image yap
& $WPCLI wp media import "GORSEL_YOLU" --post_id=$POST_ID --featured_image --path="$WP_PATH"
```

### 5. Cache Temizle

```powershell
& $WPCLI wp cache flush --path="$WP_PATH"
```

---

## Seçenek B — REST API ile Yükle (Canlı Site)

WordPress MCP kuruluysa (`wordpress` server) şunu kullan:

```
WordPress MCP üzerinden:
1. Makale içeriğini al
2. wp_posts tablosuna yaz (status: draft)
3. postmeta: rank_math_focus_keyword, rank_math_description
4. Kategori ve etiket ata
5. Featured image yükle
```

---

## Çıktı

```
POST OLUŞTURULDU:
ID: [post_id]
Başlık: [title]
URL: http://localhost:8881/?p=[post_id]
Durum: draft
Kategori: [category]
Rank Math keyword: [keyword]
Featured image: [atandı/atanmadı]

Yayınlamak için:
  wp post update [ID] --post_status=publish --path="C:\Users\fatih\Studio\clearlegaltips"
```

---

## Mevcut Post Güncelleme

Var olan bir postu güncellemek için:

```powershell
& $WPCLI wp post update POST_ID --post_content="YENİ_İÇERİK" --path="$WP_PATH"
& $WPCLI wp cache flush --path="$WP_PATH"
```
