# Taslaklar — yayın akışı (lokal)

Takvim: `workspace/plans/editorial-calendar-2026-2027.csv`. Plan: `workspace/plans/vertical-hubs-plan-2026-2027.md`.

## Her yayın günü
1. `git pull`. Takvimde bugünün satırını bul; `draft_path` taslağı gösterir.
2. `<slug>.html` içeriğini Gutenberg'e **Custom HTML** olarak ya da Kod Düzenleyici'ye yapıştır, düzenle.
   - `<!-- WIDGET: ... -->` gördüğün yere `workspace/widgets/<tool>.html` içeriğini ayrı bir Custom HTML bloğu olarak yapıştır.
   - `<!-- IMAGE: alt | prompt -->` yorumlarını görselle değiştir (`generate-featured-image`), ya da sil.
   - `<!-- EDITOR: ... -->` notlarını oku ve kaldır.
3. `<slug>.meta.json` → Rank Math başlık, açıklama ve focus keyword; kategori ve tag'ler; slug.
4. PDF: `pdf_filename` ve `pdf_outline` ile `pdf-generate`. Dosyayı `wp-content/uploads/YYYY/MM/` altına yükle, download box linklerini kontrol et.
5. Featured image: `featured_image_prompt` → `post-{id}-{slug}.jpg`, 1200×630.
6. **Bugünün tarihiyle** yayınla (geriye tarihleme yok).
7. Takvim CSV'sinde `status=published` yap, `post_id` gir, commit et.

## Cuma
`<hub>/hub-link-updates/Wnn.md` yamasını uygula: hub tablosunda ve kardeş postlarda o haftanın spoke linkleri.

## Kurallar
- Taslaktaki iç linkler yalnızca canlı veya daha önce yayınlanan postlara gider. Sıra bozulursa (bir gün atlanırsa) linki yayından önce kontrol et.
- Affiliate linkleri sadece `/go/{slug}`. Yeni program onaylanınca önce redirect'i oluştur.
- Rakamı değiştirirsen `workspace/data/<vertical>.csv` satırını da güncelle; widget'ı `python3 workspace/tools/build_widgets.py` ile yeniden üret.
- Kontrol: `python3 workspace/tools/qa_draft.py <dosya veya klasör>` → 0 hata.
