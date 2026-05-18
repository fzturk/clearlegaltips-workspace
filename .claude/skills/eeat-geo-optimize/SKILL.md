---
name: eeat-geo-optimize
description: Makaleyi E-E-A-T ve GEO (Generative Engine Optimization) standartlarına göre optimize eder. "E-E-A-T kontrol", "AI arama optimizasyonu", "güven artır", "GEO" gibi taleplerde kullan.
allowed-tools: Read WebSearch
effort: high
---

ClearLegalTips makalesini E-E-A-T ve GEO için optimize et.

## Hedef: $ARGUMENTS
(Post ID, makale başlığı veya dosya yolu)

---

## E-E-A-T Kontrol Listesi (Google EEAT Framework)

### Experience (Deneyim)
- [ ] Yazar profilinde ilgili deneyim belirtilmiş mi? (bio'da "X yıl hukuk alanında...")
- [ ] Makalede gerçek kullanım örnekleri var mı? ("When I reviewed 50 NDA templates...")
- [ ] Birinci elden gözlem veya vaka çalışması var mı?
- [ ] Tarih damgası güncel mi?

### Expertise (Uzmanlık)
- [ ] Yazar biyografisi makalenin konusuyla eşleşiyor mu?
- [ ] Hukuki terminoloji doğru kullanılmış mı?
- [ ] Kaynaklar akademik/resmi mi? (.gov, .edu, established law firms)
- [ ] İçerik derinlik gösteriyor mu? (yüzeysel değil, gerçek bilgi)

### Authoritativeness (Otorite)
- [ ] Yazar ve site about sayfası detaylı mı?
- [ ] Sosyal kanıt var mı? (atıflar, bahsedilmeler)
- [ ] İç linkleme güçlü mü? (hub-spoke yapısı)
- [ ] Editöryal süreç belgelenmiş mi?

### Trustworthiness (Güvenilirlik)
- [ ] FTC disclosure her makalede var mı? ✓ (clt-disclosure div)
- [ ] Legal disclaimer her makalede var mı? ✓ (clt-disclaimer div)
- [ ] Privacy Policy, Terms, Disclaimer sayfaları var mı? ✓
- [ ] SSL aktif mi? (canlı geçişte kontrol et)
- [ ] Affiliate ilişkisi açıkça belirtilmiş mi?
- [ ] İletişim bilgisi (Contact sayfası) var mı? ✓

---

## GEO — Generative Engine Optimization

GEO, ChatGPT / Gemini / Perplexity / Bing Copilot gibi AI arama motorlarının içeriğini kaynak olarak göstermesini sağlar.

### GEO Optimizasyon Teknikler

**1. Doğrudan Cevap Formatı (Direct Answer)**
AI'ların snippet olarak alması için içeriğin başında açık, kısa tanım ver:
```
"An NDA (Non-Disclosure Agreement) is a legally binding contract 
that prevents parties from sharing confidential information. 
In the US, NDAs are enforceable in all 50 states."
```

**2. Soru-Cevap Yapısı**
Her H2'yi soru formatında yaz:
- "What is an NDA?" yerine "What Is an NDA and When Do You Need One?"
- AI'lar soru-cevap formatını daha kolay alıntılar

**3. Sayısal/Liste Formatı**
AI'lar sayısal listeleri kaynak göstermeyi sever:
```
"5 key elements every NDA must include:
1. Definition of confidential information
2. Obligations of receiving party
3. Exclusions from confidentiality
4. Duration of agreement
5. Consequences of breach"
```

**4. Kaynak Atıfları**
Resmi kaynakları açıkça belirt:
```
"According to the Uniform Trade Secrets Act (UTSA), adopted in 
47 states, trade secrets include..."
```

**5. Güncellik Sinyalleri**
- Yıl içeren başlıklar: "NDA Template 2026"
- "Last updated: [tarih]" etiketi
- Yeni yasal değişiklikleri ekle

**6. Coğrafi Sinyal (State-Specific)**
AI'lar bölgesel sorulara bölgesel içerik döndürür:
```
"In Texas, NDAs must... In California, NDAs cannot..."
```

---

## Optimize Edilecek Elementler

### Makaleyi Oku ve Şunları Kontrol Et:

```powershell
# Makale içeriğini al
$WPCLI = "C:\Users\fatih\AppData\Local\studio_app\bin\studio.bat"
$WP_PATH = "C:\Users\fatih\Studio\clearlegaltips"
& $WPCLI wp post get $ARGUMENTS --fields=post_content --path="$WP_PATH"
```

Şunları tespit et:
1. Açılış paragrafı doğrudan cevap veriyor mu?
2. H2'ler soru formatında mı?
3. Sayısal listeler var mı?
4. Resmi kaynak atıfları var mı?
5. Yazar bio bölümü var mı?

---

## Çıktı

```
=== E-E-A-T / GEO OPTİMİZASYON RAPORU ===
Post: [ID / Başlık]

E-E-A-T SKORU:
Experience: [✓/✗] [açıklama]
Expertise:  [✓/✗] [açıklama]
Authority:  [✓/✗] [açıklama]
Trust:      [✓/✗] [açıklama]

GEO OPTİMİZASYONU:
Direct Answer: [✓/✗]
Q&A Format:   [✓/✗]
Number Lists:  [✓/✗]
Citations:     [✓/✗]
Freshness:     [✓/✗]

ÖNERİLEN DEĞİŞİKLİKLER:
1. [Değişiklik 1]
2. [Değişiklik 2]

PHP GÜNCELLEME KOMUTU:
[WP-CLI komutu]
```
