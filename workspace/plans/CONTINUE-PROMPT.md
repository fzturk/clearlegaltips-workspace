# Devam Promptu (26 Eylül 2026 sonu)

Yeni bir Claude Code oturumunda aşağıdaki bloğu olduğu gibi yapıştır.

---

```
clearlegaltips-workspace, branch claude/amazing-fermat-7ieefh (draft PR #2 açık). Caveman mode, Türkçe.
Önce oku: CLAUDE.md, workspace/plans/CONTINUE-PROMPT.md, workspace/plans/editorial-calendar-2026-2027.csv.
Görev: Hub 3 Divorce taslaklarını bitir (W11, W12), sonra Hub 4 (W14–W17). Her yayın haftası = 1 commit + push.
Kurallar, iş akışı ve araçlar CONTINUE-PROMPT.md'de. Kredi sınırı var: hafta hafta commit et, gereksiz fetch yapma.
```

---

## Durum

| Hub | Haftalar | Durum | Commit |
|---|---|---|---|
| Hazırlık (araçlar, takvim, skill'ler) | W00 | ✅ | a35fa11 öncesi |
| Hub 2 Small Estate | W01–W04 (20) | ✅ | pushed |
| Hub 1 Small Claims | W05–W08 (20) | ✅ | pushed (4b718f8) |
| Hub 3 Divorce | W09 (hub + TX, CA, FL, NY) | ✅ | 957b311 |
| Hub 3 Divorce | W10 (PA, IL, OH, GA, NC) | ✅ | "drafts: W10 divorce (5)" |
| **Hub 3 Divorce** | **W11: MI, NJ, VA, WA, AZ** | ⏳ sıradaki | — |
| Hub 3 Divorce | W12: TN, CO, IN, MO, MA | ⏳ | — |
| Hub 4 Judgment/Garnishment | W14–W17 (20) | ⏳ | — |

Tarihler, slug'lar ve başlıklar: `workspace/plans/editorial-calendar-2026-2027.csv` (H3 satırları 52–61). Plan dosyası: `/root/.claude/plans/keen-riding-hopper.md` (bulut oturumuna özel; yoksa bu dosya esastır).

## Önemli dosyalar (git)

**Veri:**
- `workspace/data/divorce.csv` — 51 satır. Ücretler doğrulandı:
  - Eyalet geneli: CA, NY, NC, CO.
  - İlçe bazlı: TX (Harris), FL (Collier), PA (Philadelphia), IL (Cook), OH (Franklin), GA (Fulton).
  - **W11–W12 eyaletlerinin `fee_text` alanı hâlâ "Set by county".** Önce resmi ücret tablosunu bul ve CSV'ye yaz.
- Diğer: `small-estate.csv`, `small-claims.csv`, `live-slugs.txt` (canlı slug'lar; iç link kuralı için).

**Araçlar:**
- `workspace/tools/qa_draft.py <dir> [--check-links]` — 0 hata şart. Kontroller:
  - Kelime sayısı: spoke ≥1.900, hub ≥3.000.
  - title ≤60, meta description ≤155.
  - Takvim bazlı iç link kuralı.
- `workspace/tools/render_hub_table.py divorce [--stats | --inject <hub.html> [--link-published]]`
- `workspace/tools/build_widgets.py divorce-cost-timeline-estimator` — CSV değişince çalıştır, sonra `--inject` ile hub tablosunu yenile.
- FAQ JSON-LD: taslakta FAQ'nun sonuna `<!-- FAQ-JSONLD -->` koy. `/tmp/claude-0/faqld.py` yeni oturumda yok; kısa bir Python ile yeniden yaz. Yaptığı iş: `<h2 id="faq">` ile yorum arasındaki `<h3>` soru / `<p>` cevap çiftlerinden FAQPage JSON-LD'yi `<p><script type="application/ld+json">…</script></p>` olarak üretmek.
- Meta üretimi: `{slug}.meta.json` dosyasını W10 örneğine bakarak yaz. Örnek: `workspace/drafts/H3-divorce/how-to-file-for-divorce-in-ohio.meta.json`.

**Taslaklar:**
- `workspace/drafts/H3-divorce/`
  - Hub: `divorce-requirements-by-state`.
  - Spoke'lar: TX, CA, FL, NY, PA, IL, OH, GA, NC.
  - Yamalar: `hub-link-updates/W09.md` (163 widget embed ve 176 daraltma önerisi dahil) ve `W10.md`.
- Widget: `workspace/widgets/divorce-cost-timeline-estimator.html` (build) ve `workspace/widgets/src/…` (kaynak).

## Spoke şablonu (W09–W10 ile birebir aynı yapı)

1. `clt-disclosure`
2. `clt-download-box`: `{state}-divorce-filing-checklist.pdf` (uploads/2026/12) + ortak `uncontested-divorce-filing-checklist.pdf` (uploads/2026/11).
3. `clt-keytakeaway`: "Here is how to file for divorce in {State} in brief: …". Focus keyword ilk 100 kelimede olmalı.
4. H2 bölümleri: residency, grounds, waiting period, cost (ilçe ücret tablosu + fee waiver), `clt-cta-box` → `/go/lawdepot-family`, forms, steps (ol), `<!-- IMAGE -->`, property, alimony/support, children, mistakes, online (opsiyonel), compare (önceki spoke'lara ve hub'a link).
5. FAQ: 6 soru + JSON-LD.
6. `clt-related-articles`: 3 link.
7. `clt-sources`: resmi statute + ücret sayfası, sonunda "Fact-checked: September 2026".
8. `clt-disclaimer`.

**Uzunluk ve meta:**
- Hedef ~2.100–2.400 kelime. 1.900'ün altındaysa bir bölüm ekle: separation, name change/after decree, online.
- Meta: kategori 8, etiketler ["Divorce","Family Law", …].
- title = takvimdeki başlık; ≤60 karakter değilse hem takvimde hem meta'da kısalt.

**İç link kuralı:** yalnız canlı slug'lar + takvimde kendisinden ÖNCE yayınlanan taslaklar.

## Doğrulama yöntemi (kredi dostu)

- **Statute metni:** önce eyaletin resmi sitesi (curl). Engelliyse FindLaw WebFetch (`codes.findlaw.com/{st}/...`). Hangi yolun kullanıldığını `editor_notes`'a yaz.
- **Engelli siteler:** nycourts, mass.gov, njcourts, nccourts, ilga, justia (403).
- **Ücretler:** WebSearch ile ilçe fee schedule PDF'ini bul, curl + pypdf ile doğrula.
  - pypdf yoksa: `pip install pypdf` veya WebFetch.
- **W11 aday kaynakları:**
  - MI: Wayne County / MCL 600.2529.
  - NJ: $300 statewide, N.J. Court Rules / njcourts — engelli, FindLaw kullan.
  - VA: Code §16.1-69.48:5 ya da circuit court fee.
  - WA: King County $314?
  - AZ: Maricopa.
  - Bu rakamlar tahmin; **doğrulamadan yazma.**
- CSV'deki residency ve bekleme verileri zaten doğrulandı; spoke'ta CSV ile tutarlı kal.

## Haftalık akış

1. Ücretleri doğrula → `divorce.csv` → `build_widgets` → `render_hub_table --inject`.
2. 5 spoke HTML + FAQ JSON-LD + meta.json yaz.
3. `qa_draft.py workspace/drafts/H3-divorce --check-links` → 0 hata.
4. `hub-link-updates/W{nn}.md` yamasını yaz (W10.md formatı).
5. Commit ve push:
   ```
   git add ... && git commit -m "drafts: W{nn} divorce (5)" && git push -u origin claude/amazing-fermat-7ieefh
   ```
   PR #2 zaten açık; yeni PR açma.

## Hub 4 (W14–W17) için hazır veriler
- Kategoriler: HUB A (Business Calculators 6), diğerleri Filing Guides 8.
- Takvim: satır 62+.
- `judgment-interest.csv` için 2026 oranları (resmi kaynakla tekrar teyit et):

| Eyalet | Oran |
|---|---|
| FL | Q4 %7.87 |
| OH | %7 |
| MI | %4.959 (1 Tem 2026) |
| NJ | %4.5 |
| NY | %9; tüketici borcu %2 |
| IL | %9; tüketici ≤$25k %5 |
| PA | %6 |
| NC | %8 |
| VA | %6 |
| MD | %10; kira %6 |
| GA | prime+3 |
| AZ | min(%10, prime+1) |
| UT | fed+2 |
| WA | türe göre |
| TX | prime, %5–15 |
| CA | %10 / %5 |

- Widget: judgment interest calculator. Model: `divorce-cost-timeline-estimator` src.

## Açık kullanıcı işleri (lokal)
- **W09 yaması:** canlı 163'e widget embed et, 176'yı daralt (`W09.md` §4–5).
- **W13 tamponu:** 1 Ocak 2027 ücret değişikliklerini kontrol et. CA fee schedule, Harris, Collier, Philadelphia.
- **Affiliate onayları:** OnlineDivorce / CompleteCase onaylanırsa CTA slug'ını değiştir.
