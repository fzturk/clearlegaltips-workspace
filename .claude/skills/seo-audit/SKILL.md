---
name: seo-audit
description: ClearLegalTips sitesini SEO açısından denetler. "SEO kontrol", "site audit", "hangi makaleler eksik", "performans kontrol" gibi taleplerde kullan.
allowed-tools: Read WebFetch Bash
effort: high
---

ClearLegalTips.com için kapsamlı SEO denetimi yap.

## Denetim Kapsamı: $ARGUMENTS (boşsa tüm site)

## Denetim Adımları

### 1. Rank Math Eksik Alanlar Kontrolü (WP-CLI)

```powershell
# WP-CLI ile Rank Math eksik alanları tespit et
C:\Users\fatih\AppData\Local\studio_app\bin\studio.bat wp eval '
$posts = get_posts(["post_type"=>"post","posts_per_page"=>-1,"post_status"=>"publish"]);
foreach($posts as $p) {
    $kw = get_post_meta($p->ID, "rank_math_focus_keyword", true);
    $desc = get_post_meta($p->ID, "rank_math_description", true);
    $img = get_post_thumbnail_id($p->ID);
    $issues = [];
    if(!$kw) $issues[] = "NO_KEYWORD";
    if(!$desc) $issues[] = "NO_META_DESC";
    if(!$img) $issues[] = "NO_FEATURED_IMG";
    if($issues) echo $p->ID . " | " . $p->post_title . " | " . implode(", ",$issues) . "\n";
}' --path="C:\Users\fatih\Studio\clearlegaltips"
```

### 2. Kelime Sayısı Kontrolü

```powershell
C:\Users\fatih\AppData\Local\studio_app\bin\studio.bat wp eval '
$posts = get_posts(["post_type"=>"post","posts_per_page"=>-1,"post_status"=>"publish"]);
foreach($posts as $p) {
    $wc = str_word_count(strip_tags($p->post_content));
    if($wc < 3000) echo $p->ID . " | " . $p->post_title . " | " . $wc . " words\n";
}' --path="C:\Users\fatih\Studio\clearlegaltips"
```

### 3. ThirstyAffiliates Placeholder Link Kontrolü

```powershell
C:\Users\fatih\AppData\Local\studio_app\bin\studio.bat wp eval '
$links = get_posts(["post_type"=>"thirstylink","posts_per_page"=>-1,"post_status"=>"publish"]);
foreach($links as $l) {
    $info = get_post_meta($l->ID, "_ta_link_info", true);
    $dest = is_array($info) ? ($info["destination"] ?? "") : (string)$info;
    if(empty($dest) || $dest === "#" || $dest === "") {
        echo $l->ID . " | " . $l->post_title . " | PLACEHOLDER\n";
    }
}' --path="C:\Users\fatih\Studio\clearlegaltips"
```

### 4. PageSpeed / Core Web Vitals (PageSpeed MCP aktifse)

Şu URL'leri kontrol et:
- Ana sayfa: http://clearlegaltips.com/
- En çok ziyaret edilen 3 makale
- Mobil + Desktop skorları

Hedefler:
- LCP < 2.5s
- CLS < 0.1
- INP < 200ms
- PSI Score > 85 (mobile), > 90 (desktop)

### 5. GSC Performans Analizi (GSC MCP aktifse)

Son 28 gün için:
- En yüksek impression'lı ama düşük CTR'li sayfalar (CTR < %2)
- Position 8-20 arası ranklar (hızlı kazanım fırsatı)
- Click almayan ama impression olan sayfalar
- Mobile vs Desktop performans farkı

### 6. İç Link Audit

```powershell
C:\Users\fatih\AppData\Local\studio_app\bin\studio.bat wp eval '
$posts = get_posts(["post_type"=>"post","posts_per_page"=>-1,"post_status"=>"publish"]);
foreach($posts as $p) {
    $has_related = strpos($p->post_content, "clt-related-articles") !== false;
    $has_disclosure = strpos($p->post_content, "clt-disclosure") !== false;
    $has_disclaimer = strpos($p->post_content, "clt-disclaimer") !== false;
    $issues = [];
    if(!$has_related) $issues[] = "NO_INTERNAL_LINKS";
    if(!$has_disclosure) $issues[] = "NO_DISCLOSURE";
    if(!$has_disclaimer) $issues[] = "NO_DISCLAIMER";
    if($issues) echo $p->ID . " | " . $p->post_title . " | " . implode(", ",$issues) . "\n";
}' --path="C:\Users\fatih\Studio\clearlegaltips"
```

### 7. Rapor Formatı

```
=== CLEARLEGALTIPS SEO AUDIT — [Tarih] ===

RANK MATH EKSİKLER:
[liste]

KISA İÇERİKLER (< 3000 kelime):
[liste]

PLACEHOLDER AFFILIATE LİNKLER:
[liste]

YAPI EKSİKLERİ (disclosure/disclaimer/iç link):
[liste]

PAGESPEED (varsa):
[skorlar]

GSC FIRSATLAR (varsa):
[pozisyon 8-20 listesi]

ÖNCELİKLİ AKSIYONLAR:
1. [En kritik sorun]
2. [İkinci sorun]
...
```
