# CTR Rewrite — 24 Eylül 2026

Hedef: GSC'de ortalama pozisyon 7–10, 90 günde 0 tık alan 5 sayfa.
Uygulama: `workspace/scripts/update-ctr-meta-2026-09.php` (Rank Math `rank_math_title` + `rank_math_description`).
Ölçüm: 4 hafta sonra (~22 Ekim) aynı sayfaların CTR/poz değerini Supermetrics GW ile karşılaştır.

| ID | Sayfa | 90g gös / poz | Eski title | Yeni title | Yeni meta |
|---|---|---|---|---|---|
| 7386 | /statute-of-limitations-on-debt-by-state/ | 463 / 7,6 | Statute of Limitations on Debt by State: 2026 Table | Statute of Limitations on Debt by State (2026): 3–10 Years | Debt deadlines for all 50 states + DC: 3 to 10 years on written contracts, often shorter for oral. Check your state before you pay or sue. Verified 2026. |
| 1509 | /free-short-term-rental-airbnb-agreement-template/ | 123 / 8,9 | Free Short-Term Rental (Airbnb) Agreement Template (2026) | Free Airbnb Rental Agreement Template (2026) + House Rules | Free short-term rental agreement for Airbnb and VRBO hosts: house rules, quiet hours, damage deposit, and the 30-day rule that turns guests into tenants. |
| 5836 | /small-business-donations-legal/ | 90 / 9,5 | Small Business Donations: Legal to Ask? Tax Rules 2026 | Can a Small Business Ask for Donations? Yes, but It's Taxed | Yes, a small business can legally ask for donations, but the money is taxable income and donors can't deduct it. Rules, safe wording, and a free template. |
| 1389 | /commercial-property-management-agreement-template/ | 55 / 8,1 | Free Commercial Property Management Agreement Template 2026 | Free Commercial Property Management Agreement Template 2026 *(değişmedi)* | Copy our 15-section commercial property management agreement: fees on collected rent, spending limits, trust accounts, and the broker-license check. |
| 5921 | /security-deposit-limits-by-state/ | 49 / 8,6 | Security Deposit Limits by State (2026): Caps & Deadlines | Security Deposit Limits by State (2026): Max & Return Days | Max security deposit and return deadline for all 50 states + DC. 29 states cap it; deadlines run 10 to 60 days. Miss one and most states charge double. |

## Uyarı: pozisyon 7–10 ortalaması yanıltıcı
Sorgu kırılımı (90 gün) gösteriyor ki görünür sorguların çoğu gerçek kullanıcı araması değil, metin doğrulayan tam-eşleşme aramaları:
- Airbnb sayfası: `"quiet hours" "10:00 pm and 8:00 am daily" "material breach" lease` varyasyonları (poz 3–11)
- SOL sayfası: `rcw 62a.2-309 washington text`, `"2305.07" "senate bill 13" ohio` (poz 3–10)
- Asıl hedef sorgu `statute of limitations on debts by state` → poz **89**; `... in oregon` → 98
Gösterimlerin çoğu anonim ("(unknown)"). Başlık değişikliği tek başına büyük CTR artışı getirmeyebilir; asıl kazanç bu sayfaların baş sorgularda sıralama almasıyla gelir.
