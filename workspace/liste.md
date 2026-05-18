# Claude Code — WordPress Affiliate & Reklam Sitesi İçin Kapsamlı Araç Listesi

**Amaç:** Reklam ve affiliate gelirlerine odaklanmış, Google rank için güven kazanmış, başarılı ve eksiksiz bir WordPress sitesi oluşturmak.  
**Araştırma tarihi:** 2026-05-18  
**Kaynak:** Claude Code resmi dokümantasyonu, GitHub, MCP Registry, Awesome Lists

---

## İÇİNDEKİLER

1. [Claude Code Temel Mimari](#1-claude-code-temel-mimari)
2. [Memory Sistemi](#2-memory-sistemi)
3. [Skills / Slash Commands](#3-skills--slash-commands)
4. [Hooks](#4-hooks)
5. [Subagents & Agent Teams](#5-subagents--agent-teams)
6. [Plugins](#6-plugins)
7. [MCP: WordPress & CMS](#7-mcp-wordpress--cms)
8. [MCP: SEO & Arama Analitiği](#8-mcp-seo--arama-analiti̇ği̇)
9. [MCP: Google Ürünleri](#9-mcp-google-ürünleri̇)
10. [MCP: Web Araştırma & Scraping](#10-mcp-web-araştırma--scraping)
11. [MCP: Görsel Üretimi](#11-mcp-görsel-üretimi)
12. [MCP: Sosyal Medya](#12-mcp-sosyal-medya)
13. [MCP: Reklam & Monetizasyon](#13-mcp-reklam--moneti̇zasyon)
14. [MCP: E-posta & Outreach](#14-mcp-e-posta--outreach)
15. [MCP: Döküman & PDF](#15-mcp-döküman--pdf)
16. [MCP: Otomasyon & Entegrasyon](#16-mcp-otomasyon--entegrasyon)
17. [MCP: Hosting & Altyapı](#17-mcp-hosting--altyapı)
18. [Topluluk Skills & Agents](#18-topluluk-skills--agents)
19. [Önerilen Kurulum Yapısı](#19-önerilen-kurulum-yapısı)
20. [Önerilen Agent Pipeline](#20-önerilen-agent-pipeline)
21. [Kaynaklar](#21-kaynaklar)

---

## 1. CLAUDE CODE TEMEL MİMARİ

Claude Code bir agentic loop üzerinde çalışır: araçları seçer, kodu yazar/okur/çalıştırır ve oturumlar arasında bağlam tutar. Mimari 6 katmandan oluşur:

| Katman | Ne İşe Yarar | Nerede Yapılandırılır |
|---|---|---|
| **Memory** | Kalıcı talimatlar ve öğrenilenler | `~/.claude/`, `./CLAUDE.md` |
| **Skills** | Slash komutları (örn: `/yaz-makale`) | `~/.claude/skills/`, `.claude/skills/` |
| **Hooks** | Olaylarda otomatik çalışan shell scriptleri | `settings.json` |
| **Subagents** | İzole çalışan alt Claude örnekleri | `~/.claude/agents/` |
| **MCP Servers** | Dış araçlara erişim (WordPress, SEO, GA4...) | `.mcp.json` |
| **Plugins** | Skills+Agents+Hooks+MCP'yi tek pakette sunar | `.claude-plugin/plugin.json` |

**Resmi Dokümantasyon:**
- https://code.claude.com/docs
- https://code.claude.com/docs/en/sub-agents
- https://code.claude.com/docs/en/skills
- https://code.claude.com/docs/en/hooks-guide

---

## 2. MEMORY SİSTEMİ

### 2.1 CLAUDE.md (Siz Yazarsınız)

CLAUDE.md dosyaları Claude'a tüm oturumlar boyunca kalıcı talimatlar verir. Her oturumun bağlamına otomatik yüklenir.

**Kapsam seviyeleri:**

| Kapsam | Konum | Etkisi |
|---|---|---|
| Kullanıcı geneli | `~/.claude/CLAUDE.md` | Tüm projeleriniz |
| Proje | `./CLAUDE.md` | O projeye özel |
| Yerel | `./CLAUDE.local.md` | Sadece siz (gitignore) |
| Yol bazlı | `.claude/rules/*.md` | Belirli dosya tipleri için |

**WordPress sitesi için CLAUDE.md'ye yazılacaklar:**
```markdown
# ClearLegalTips — Site Kuralları

## Site Bilgileri
- URL: https://clearlegaltips.com
- WP REST API: /wp-json/wp/v2/
- SEO Eklentisi: Rank Math
- Affiliate Sistemi: ThirstyAffiliates

## İçerik Standartları
- Hedef kitle: ABD'li hukuki bilgi arayan kullanıcılar
- Ton: Net, profesyonel, hukuki tavsiye değil
- Kelime sayısı: minimum 3.000 kelime
- Her makalede FTC açıklaması zorunlu
- Schema markup: Article + FAQPage + BreadcrumbList

## Affiliate Programları
- LegalZoom: /recommend/legalzoom/
- ZenBusiness: /recommend/zenbusiness/
- Rocket Lawyer: /recommend/rocketlawyer/
```

**Dosya import:**
```markdown
@README.md
@wp-content/themes/mytheme/functions.php
@~/.claude/affiliate-programs.md
```

**Başlatma:** `/init` komutuyla proje için otomatik CLAUDE.md oluşturulur.

### 2.2 Auto-Memory (Claude Yazar)

Claude Code v2.1.59+ sürümünden itibaren varsayılan olarak açık. Claude her oturumda öğrendiklerini otomatik kaydeder.

- Konum: `~/.claude/projects/<proje>/memory/MEMORY.md`
- İlk 200 satır veya 25KB her oturumda yüklenir
- Konu dosyaları (debugging.md, seo-conventions.md) talep üzerine yüklenir
- Açma/Kapama: `/memory` komutu

**claude-mem plugin** (89K+ star): SQLite FTS5 arama + semantik sıkıştırma ile genişletilmiş auto-memory.

**Nasıl Kullanılır:**  
Claude sitede bir hata düzeltince, kullandığı WordPress REST API endpoint'ini ve neden çalıştığını otomatik kaydeder. Sonraki oturumda aynı endpoint'i aramak zorunda kalmaz.

---

## 3. SKILLS / SLASH COMMANDS

### 3.1 Skill Nasıl Çalışır

Bir skill, `SKILL.md` dosyası içeren bir dizindir. Dizin adı `/slash-command` haline gelir. Açıklama eşleştiğinde Claude otomatik olarak da tetikleyebilir.

**Konum:**
- `~/.claude/skills/<skill-adı>/SKILL.md` (kişisel)
- `.claude/skills/<skill-adı>/SKILL.md` (proje)

**SKILL.md örneği — SEO Makale Yazma:**
```yaml
---
name: yaz-makale
description: SEO uyumlu WordPress makalesi yaz. Kullanıcı içerik, makale, blog yazısı istediğinde kullan.
allowed-tools: Read Write Bash(wp *) WebSearch WebFetch
effort: high
---

Şu adımları takip ederek SEO uyumlu makale yaz:
1. Konuyu araştır (web arama + competitor analizi)
2. H2/H3 yapısıyla outline oluştur
3. 3.000+ kelime, hedef anahtar kelime ilk 100 kelimede
4. FAQ bölümü ekle (FAQPage schema için)
5. 3-5 dahili link ekle
6. Meta başlık (60 karakter) ve açıklama (155 karakter) yaz
7. Featured image için alt text öner

Hedef anahtar kelime: $ARGUMENTS
```

**Önemli Frontmatter Alanları:**

| Alan | Amaç |
|---|---|
| `description` | Claude'un ne zaman otomatik kullanacağını belirler |
| `disable-model-invocation: true` | Sadece siz çağırabilirsiniz (/yayinla, /deploy) |
| `allowed-tools` | Önceden onaylı araçlar (izin istenmez) |
| `context: fork` | İzole subagent'ta çalıştırır |
| `effort: high` | Maksimum akıl yürütme kullanır |
| `model: claude-haiku-4-5` | Basit görevler için daha ucuz model |

### 3.2 Dahili (Built-in) Skilllar

| Skill | Komut | Amaç |
|---|---|---|
| debug | `/debug` | Sistematik hata ayıklama |
| batch | `/batch` | Toplu işlem |
| loop | `/loop` | Belirli aralıklarla tekrar |
| review | `/review` | Kod inceleme |
| security-review | `/security-review` | Güvenlik denetimi |
| init | `/init` | CLAUDE.md oluştur |
| ultrareview | `/ultrareview` | Çok-ajanlı bulut code review |

### 3.3 WordPress/SEO İçin Topluluk Skillları

**WordPress:**
- `elvismdev/claude-wordpress-skills` — Profesyonel WP mühendisliği skillları
- `jorgerosal/wordpress-skills` — WP geliştirme skillları ve agentları

**SEO/İçerik:**
- `aaron-he-zhu/seo-geo-claude-skills` — 20 SEO & GEO skilli: keyword araştırma, içerik yazma, teknik denetim, CORE-EEAT + CITE çerçeveleri
- `AgriciDaniel/claude-seo` — Evrensel SEO skilli: 25 alt-skill + 18 alt-agent, tam SEO yığını
- `TheCraigHewitt/seomachine` — Uzun form SEO blog içeriği için eksiksiz workspace
- `alirezarezvani/claude-skills` — 263+ skill (mühendislik, pazarlama, uyum)

**Skill Marketplaces:**
- https://tonsofskills.com — 425+ plugin, 2.810 skill, 200 agent
- https://agentskills.io — Çapraz araç skill standardı

---

## 4. HOOKS

Hooks, Claude'un kararlarından bağımsız olarak lifecycle olaylarında deterministik çalışan shell scriptleridir.

### 4.1 Hook Olayları ve WordPress Kullanım Senaryoları

| Olay | Ne Zaman Tetiklenir | WordPress Kullanımı |
|---|---|---|
| `PreToolUse` | Her araç çağrısından önce | Üretim dosyalarına yazmayı engelle, içerik doğrula |
| `PostToolUse` | Araç çağrısı tamamlandıktan sonra | PHP lint, SEO kontrolü, affiliate link doğrulama |
| `Notification` | Claude input beklediğinde | Toplu içerik işlerken masaüstü bildirimi |
| `Stop` | Oturum kapandığında | Tamamlanan makaleleri logla, git commit at |
| `SubagentStop` | Subagent tamamlandığında | Araştırma çıktısını topla, sıradaki pipeline adımını tetikle |
| `InstructionsLoaded` | CLAUDE.md yüklendiğinde | Aktif kuralları debug et |

### 4.2 settings.json Yapılandırması

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "FILE=$(cat | jq -r '.tool_input.file_path // empty'); if [[ \"$FILE\" == *.php ]]; then php -l \"$FILE\" 2>&1; fi",
            "timeout": 10000,
            "async": true
          }
        ]
      }
    ],
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "powershell -Command \"[System.Windows.Forms.MessageBox]::Show('Claude Code dikkat istiyor!')\""
          }
        ]
      }
    ],
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "echo \"$(date): Oturum bitti\" >> ~/wp-site/content-log.txt",
            "async": true
          }
        ]
      }
    ]
  }
}
```

### 4.3 Exit Kodları

- **Exit 0:** İşlem devam eder
- **Exit 2:** İşlem **BLOKE** edilir (Claude sebep metnini görür)

### 4.4 WordPress'e Özgü Hook Örnekleri

**Yayımlı post'lara yazılmayı engelle:**
```bash
#!/bin/bash
FILE=$(echo "$1" | jq -r '.tool_input.file_path // empty')
if [[ "$FILE" == *"/published/"* ]]; then
  echo "BLOKE: Yayımlanmış postlar için staging kullanın" >&2
  exit 2
fi
```

**Affiliate linkleri doğrula:**
```bash
#!/bin/bash
# Affiliate link olmayan href'leri yakala
CONTENT=$(cat | jq -r '.tool_input.new_string // empty')
if echo "$CONTENT" | grep -q 'href="http' && ! echo "$CONTENT" | grep -q '/recommend/'; then
  echo "UYARI: Affiliate link ThirstyAffiliates üzerinden geçmeli" >&2
fi
```

**Her oturum sonunda git commit:**
```bash
#!/bin/bash
cd ~/clearlegaltips
if git diff --quiet; then exit 0; fi
git add -A
git commit -m "Auto-save: içerik oturumu $(date +%Y%m%d-%H%M)"
```

**Kaynaklar:**
- https://code.claude.com/docs/en/hooks-guide
- https://github.com/disler/claude-code-hooks-mastery

---

## 5. SUBAGENTS & AGENT TEAMS

### 5.1 Dahili Subagentlar

| Subagent | Model | Araçlar | Amaç |
|---|---|---|---|
| Explore | Haiku (hızlı) | Salt-okunur | Dosya keşfi, kod arama |
| Plan | Devralır | Salt-okunur | Planlama öncesi araştırma |
| general-purpose | Devralır | Hepsi | Karmaşık çok-adımlı görevler |
| claude-code-guide | Haiku | — | Claude Code özellik yardımı |

### 5.2 Özel Subagent Oluşturma

`.claude/agents/` içine `.md` dosyası oluşturun:

```markdown
---
name: wp-icerik-arastirmaci
description: WordPress blog postları için konu araştır. Araştırma, kaynak toplama, brief oluşturma istendiğinde kullan.
model: claude-sonnet-4-6
tools: WebSearch WebFetch Bash(curl *)
memory: user
---

Hukuki ipuçları blogu için uzman içerik araştırmacısısın.

Araştırırken:
1. Konu + "explained" + güncel yıl ara
2. 5-10 otoriter kaynak bul (.gov, hukuk firmaları, köklü yayınlar)
3. Temel gerçekleri, istatistikleri ve uzman alıntıları çıkar
4. Birincil ve ikincil anahtar kelimeleri belirle
5. İnsanların sorduğu ilgili soruları bul (FAQ bölümleri için)
6. Rakiplerin bu konuda ne için sıralandığını kontrol et
7. Yapılandırılmış araştırma özeti üret

Her zaman tam URL ile kaynak göster.
```

**Subagent config alanları:**

| Alan | Seçenekler | Notlar |
|---|---|---|
| `model` | claude-haiku-4-5, claude-sonnet-4-6 | Haiku = daha ucuz/hızlı |
| `tools` | Boşlukla ayrılmış araç listesi | Read-only = Explore benzeri |
| `memory` | user, none | Oturumlar arası kalıcı öğrenme |
| `skills` | Önceden yüklenecek skiller | Subagente özel skill seti |

### 5.3 Agent Teams (Paralel Çalışma)

Agent Teams birden fazla Claude örneğini paralel çalıştırır, paylaşılan bir görev dosyası üzerinden koordine olurlar.

**Komut:** `claude --team` veya `/bg` ile oturumu arka plana al

**Agent View** (Mayıs 2026): `claude agents` — tüm oturumları, token kullanımını, durumu gösteren tek dashboard.

**Arka plan oturumu:** `claude --bg "NDA hakkında draft yaz"` — hemen geri döner, Claude arka planda çalışır.

**WordPress İçerik Pipeline — Agent Teams:**
```
Orkestratör
├── Agent 1: Keyword Araştırmacı (10 makale fırsatı bulur)
├── Agent 2: İçerik Araştırmacı (her konu için kaynak toplar)
├── Agent 3: Yazar (brieflerden makale yazar)
├── Agent 4: SEO Optimize Edici (schema, heading, meta)
└── Agent 5: WP Yayıncı (REST API ile WordPress'e yükler)
```

**Kaynaklar:**
- https://code.claude.com/docs/en/agent-teams
- https://github.com/VoltAgent/awesome-claude-code-subagents (100+ uzman subagent)
- https://github.com/wshobson/agents (çok-ajanlı orkestrasyon)

---

## 6. PLUGİNLER

Pluginler skills + agents + hooks + MCP sunucularını tek bir kurulabilir paket halinde sunar.

**Yapı:**
```
benim-wordpress-pluginim/
├── .claude-plugin/
│   └── plugin.json       # Manifest
├── skills/
│   ├── wp-publish/SKILL.md
│   └── seo-optimize/SKILL.md
├── agents/
│   └── content-researcher.md
├── hooks/
│   └── post-edit-lint.sh
└── .mcp.json             # Paketlenmiş MCP sunucuları
```

**Kurulum:** `claude plugin install <yol-veya-url>`

**Popüler Pluginler (2026):**

| Plugin | Kurulumlar | Amaç |
|---|---|---|
| Frontend Design | 96K | UI/CSS üretimi |
| Context7 | 71K | Güncel kütüphane dökümantasyonu |
| Ralph Loop | 57K | Yinelemeli otonom geliştirme |
| Code Review | 50K | Sistematik kod inceleme |
| Playwright | 28K | Tarayıcı otomasyonu ve test |

**Marketyerler:**
- https://claude.com/plugins — Resmi Claude.ai plugin dizini
- https://tonsofskills.com — 9.000+ plugin/skill marketplace

---

## 7. MCP: WORDPRESS & CMS

MCP sunucuları dış API'leri Claude araçlarına dönüştürür. `.mcp.json` dosyasıyla yapılandırılır.

### 7.1 WordPress Çekirdek MCP Sunucuları

---

**WordPress/mcp-adapter — RESMİ**
- URL: https://github.com/WordPress/mcp-adapter
- **Ne İşe Yarar:** WordPress Abilities API'sini MCP protokolüne köprüler. WordPress 6.9+ ile birlikte standart haline geliyor. Site bilgisi alma, post/sayfa CRUD, medya yükleme, plugin yönetimi.
- **Nasıl Kullanılır:**
  ```json
  { "command": "npm", "args": ["start"], "cwd": "/path/to/mcp-adapter" }
  ```
- **Gereksinim:** WordPress 6.9+, HTTP veya STDIO transport

---

**InstaWP/mcp-wp**
- URL: https://github.com/InstaWP/mcp-wp
- **Ne İşe Yarar:** WordPress REST API üzerinden post, sayfa, medya, plugin, kullanıcı, yorum yönetimi. Tek satır kurulum.
- **Nasıl Kullanılır:**
  ```bash
  npx -y @instawp/mcp-wp
  ```
  ```json
  {
    "WP_URL": "https://siteniz.com",
    "WP_USER": "kullanici_adi",
    "WP_APP_PASSWORD": "uygulama-sifresi"
  }
  ```
- **Kullanım Senaryosu:** Claude ile doğrudan "Bu makaleyi WordPress'e yükle, kategori: Hukuki Rehberler, durum: taslak" diyebilirsiniz.

---

**Automattic/mcp-wordpress-remote**
- URL: https://github.com/Automattic/mcp-wordpress-remote
- **Ne İşe Yarar:** Uzak WordPress proxy. OAuth 2.0, JWT, Uygulama Şifresi kimlik doğrulama.
- **Kullanım Senaryosu:** WordPress.com veya Jetpack bağlı siteler için.

---

**mcp-wp (WP-CLI entegrasyonu)**
- URL: https://mcp-wp.github.io/docs
- **Ne İşe Yarar:** WP-CLI komutlarını MCP araçlarına dönüştürür. Tüm WP-CLI komutlarını Claude üzerinden çalıştırmanızı sağlar.
- **Kullanım Senaryosu:** `wp post create`, `wp media import`, `wp option update` gibi komutları Claude'a söyleyerek çalıştırmak.

---

### 7.2 WordPress SEO Plugin MCP Entegrasyonları

**Royal MCP (WordPress.org plugin)**
- URL: https://wordpress.org/plugins/royal-mcp/
- **Ne İşe Yarar:** Yoast SEO veya Rank Math'i otomatik algılar; MCP üzerinden SEO başlığı, açıklaması, odak anahtar kelimesi, robots, OG alanlarını okur/yazar.
- **Kullanım Senaryosu:** Claude'a "Post 177'nin Rank Math meta başlığını 'LLC Nasıl Kapatılır: Adım Adım Kılavuz 2026' yap" demek.

**WP MCP Ultimate / Easy MCP AI**
- URL: https://wordpress.com/plugins/easy-mcp-ai
- **Ne İşe Yarar:** 58 yetenek — Yoast ve RankMath SEO metadata get/update, işlenmiş SEO head çıktısı.

**SEO Engine (ücretsiz plugin)**
- URL: https://wordpress.org/plugins/seo-engine/
- **Ne İşe Yarar:** Tam MCP desteği; tüm site SEO verisi Claude üzerinden sorgulanabilir.

---

## 8. MCP: SEO & ARAMA ANALİTİĞİ

### 8.1 Ahrefs MCP — RESMİ

- URL: https://ahrefs.com/mcp/
- Paket: `@ahrefs/mcp`
- **Ne İşe Yarar:** Backlink analizi, keyword verisi, domain rating, rekabetçi analiz.
- **Bu Claude oturumunda zaten mevcut:** `mcp__claude_ai_Ahrefs__*` araçları
- **Kullanım Senaryosu:** "clearlegaltips.com için en yüksek trafikli sayfaları göster ve hangi anahtar kelimeler için sıralandığını analiz et."

### 8.2 DataForSEO MCP

- URL: https://github.com/dataforseo/mcp-server-typescript
- **Ne İşe Yarar:** Canlı keyword, SERP ve backlink verisi. 100+ araç.
- **Kurulum:**
  ```bash
  npx @dataforseo/mcp-server
  ```
- **Kullanım Senaryosu:** "LLC formation keyword'ü için Google SERP'ini analiz et, kaç rakip var, featured snippet var mı."
- **Maliyet:** Kullandıkça öde (DataForSEO API)

### 8.3 Semrush MCP

- URL: https://github.com/mrkooblu/semrush-mcp
- **Ne İşe Yarar:** 77 araç — domain analitikleri, keyword araştırma, backlinkler, trafik, rekabetçi istihbarat.
- **Kurulum:** `npx semrush-mcp` + API key
- **Kullanım Senaryosu:** "Rakip sitenin hangi anahtar kelimelerden organik trafik aldığını göster."

### 8.4 SE Ranking MCP — RESMİ

- URL: https://seranking.com/api/integrations/mcp/
- Skills repo: https://github.com/seranking/seo-skills
- **Ne İşe Yarar:** 160+ araç — keyword araştırma, backlink, domain analizi, site denetimleri, AI arama görünürlüğü, SERP analizi.
- **Kullanım Senaryosu:** "Bu makalenin AI Overview'larda görünüp görünmediğini kontrol et."

### 8.5 Serpstat MCP

- URL: https://github.com/SerpstatGlobal/serpstat-mcp-server-js
- **Ne İşe Yarar:** 65 araç — domain analizi, keyword araştırma, backlinkler, site denetimi, rank takibi, AI Overview izleme.

### 8.6 Google Search Console MCP

**En iyi seçenekler:**

| Repo | Özellikler |
|---|---|
| AminForou/mcp-gsc | OAuth tarayıcı akışı, 20 araç, 25K satıra kadar |
| ahonn/mcp-server-gsc | 25K satır, hızlı kazanım tespiti, gelişmiş filtreleme |
| ncosentino/google-search-console-mcp | Sorgu başına 50K satır (UI'dan 50x fazla) |
| surendranb/google-search-console-mcp | Claude/Cursor/Windsurf desteği |

**Tüm seçenekler OAuth kullanır; veriler yerel makinenizde kalır.**

**Kurulum örneği:**
```json
{
  "mcpServers": {
    "search-console": {
      "command": "npx",
      "args": ["-y", "@surendranb/google-search-console-mcp"],
      "env": {
        "GOOGLE_CLIENT_ID": "...",
        "GOOGLE_CLIENT_SECRET": "..."
      }
    }
  }
}
```

**Kullanım Senaryosu:** "Son 90 günde 1.000-10.000 impressionı olan ama CTR'ı düşük makaleleri listele, başlık optimizasyonu için öner."

### 8.7 PageSpeed / Lighthouse MCP

- **ruslanlap/pagespeed-insights-mcp**
- URL: https://github.com/ruslanlap/pagespeed-insights-mcp
- **Ne İşe Yarar:** Core Web Vitals (LCP, CLS, INP), ekran görüntüleri, yükleme zaman çizelgesi, ağ analizi.
- **Kurulum:** `npx pagespeed-insights-mcp`
- **Kullanım Senaryosu:** "clearlegaltips.com/how-to-form-an-llc sayfasının mobil Core Web Vitals puanlarını analiz et, iyileştirme öner."

### 8.8 Bing Webmaster Tools MCP

- URL: https://github.com/isiahw1/mcp-server-bing-webmaster
- **Ne İşe Yarar:** 40+ araç — arama analitiği, tarama tanılamaları, URL gönderimi, site haritası, keyword araştırma, bağlantı analizi.

### 8.9 Schema / Yapısal Veri MCP

- **Structured Data Extractor (Apify):** Herhangi bir sayfadan JSON-LD, Microdata, RDFa çıkarır ve doğrular.
- **SEO Inspector & Schema Validator:** Kod tabanından doğrudan yapısal veri şemalarını doğrular.
- **InfraNodus SEO Skill:** Gelişmiş konu kümeleme ve içerik boşluğu tespiti.

---

## 9. MCP: GOOGLE ÜRÜNLERİ

### 9.1 Google Analytics 4

**googleanalytics/google-analytics-mcp — RESMİ**
- URL: https://github.com/googleanalytics/google-analytics-mcp
- **Ne İşe Yarar:** Analytics Admin API + Data API. Trafik, kullanıcı davranışı, dönüşüm analizi.
- **Kurulum:** OAuth 2.0

**mario-hernandez/google-analytics-mcp-claude-code**
- URL: https://github.com/mario-hernandez/google-analytics-mcp-claude-code
- **Ne İşe Yarar:** Claude Code için özelleştirilmiş — anomali tespiti, trafik düşüşü sınıflandırması, içerik çürümesi analizi, dönüşüm hunisi, kanal attribution.
- **Kullanım Senaryosu:** "Geçen haftaya göre trafik %30 düşmüş sayfaları bul ve neden olabileceğini analiz et."

### 9.2 Google Ads

**Resmi Google Ads MCP**
- URL: https://github.com/googleads/google-ads-mcp
- Geliştirici docs: https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server
- **Ne İşe Yarar:** LLM'ler için resmi Google Ads API MCP.

**Çok Platform:**
- `irinabuht12-oss/google-meta-ads-ga4-mcp` — 250+ araç: Google Ads + Meta Ads + GA4 tek sunucuda.
- `markifact/markifact-mcp` — 300+ operasyon: Google + Meta + TikTok + LinkedIn Ads.

### 9.3 Google AdSense

**AppsYogi-com/adsense-mcp-server**
- URL: https://github.com/AppsYogi-com/adsense-mcp-server
- **Ne İşe Yarar:** CLI kurulumu ile AdSense hesabınızla etkileşim.
- **Özellikler:** Gelir raporları, reklam birimi yönetimi, hesap analitiği.
- **Kullanım Senaryosu:** "Bu ayki en yüksek gelir getiren sayfaları listele, RPM değerlerini göster."

### 9.4 Birleşik Google Marketing

**freema/mcp-google-marketing**
- URL: https://github.com/freema/mcp-google-marketing
- **Ne İşe Yarar:** Google Analytics + Search Console + Google Ads tek sunucuda.
- **Kullanım Senaryosu:** Organik trafik ve ücretli trafik karşılaştırması, kanal attribution.

---

## 10. MCP: WEB ARAŞTIRMA & SCRAPING

### 10.1 Firecrawl MCP — RESMİ

- URL: https://github.com/firecrawl/firecrawl-mcp-server
- **Ne İşe Yarar:** Arama, scraping, tarama; JavaScript render etme, toplu işleme.
- **Kurulum:**
  ```bash
  npx -y firecrawl-mcp
  ```
  + Firecrawl API key
- **Kullanım Senaryoları:**
  - Rakip sitesinin tüm içeriğini tarayıp içerik boşluklarını analiz et
  - Belirli bir sayfanın tüm dahili linklerini çıkar
  - SERP'deki ilk 10 sayfanın ortalama kelime sayısını hesapla

### 10.2 Playwright MCP

- Paket: `@modelcontextprotocol/server-playwright`
- **Ne İşe Yarar:** Tarayıcı otomasyonu, ekran görüntüleri, form doldurma, JavaScript çalıştırma.
- **Kullanım Senaryoları:**
  - Affiliate linkleri test et (doğru yönlendiriyor mu?)
  - Sayfa layoutunu kontrol et (mobil görünüm)
  - Makaleler için ekran görüntüsü al

### 10.3 Perplexity MCP — RESMİ

- Kurulum:
  ```bash
  claude mcp add perplexity --env PERPLEXITY_API_KEY="key" -- npx -y @perplexity-ai/mcp-server
  ```
- **Ne İşe Yarar:** Gerçek zamanlı web araması + Sonar modelleri ile derin araştırma.
- **Kullanım Senaryosu:** "LLC fesih sürecindeki son yasal değişiklikler neler? Kaynaklı, güncel bilgi ver."

### 10.4 Brave Search MCP

- Paket: `@modelcontextprotocol/server-brave-search`
- **Ne İşe Yarar:** Web, yerel işletme, görsel, video, haber araması.
- **Ücretsiz katman mevcut.**

### 10.5 Exa AI MCP

- **Bu Claude oturumunda zaten mevcut:** `mcp__claude_ai_Exa__web_search_exa` ve `mcp__claude_ai_Exa__web_fetch_exa`
- **Ne İşe Yarar:** Gerçek zamanlı web araması, akademik makaleler, Twitter/X araması.

### 10.6 mcp-omnisearch

- URL: https://github.com/spences10/mcp-omnisearch
- **Ne İşe Yarar:** Tavily + Perplexity + Kagi + Jina + Brave + Exa + Firecrawl'a birleşik erişim.

---

## 11. MCP: GÖRSEL ÜRETİMİ

### 11.1 Stability AI (Stable Diffusion)

- **tadasant/mcp-server-stability-ai**
- URL: https://github.com/tadasant/mcp-server-stability-ai
- **Ne İşe Yarar:** Görsel üretme, düzenleme, büyütme (upscale).
- **Kullanım Senaryosu:** "LLC formation için 1200x630 featured image üret, mavi-lacivert profesyonel tasarım, hukuki tema."
- **Auth:** Stability AI API key

### 11.2 Midjourney MCP

- **AceDataCloud/MidjourneyMCP**
- URL: https://github.com/AceDataCloud/MidjourneyMCP
- **Ne İşe Yarar:** Midjourney görsel ve video üretimi (AceDataCloud API üzerinden).
- **Kullanım Senaryosu:** Yüksek kaliteli featured image üretimi.

### 11.3 DALL-E MCP

- **sammyl720/dall-e-image-generator**
- **Ne İşe Yarar:** DALL-E 3 entegrasyonu ile istek üzerine görsel üretimi.

### 11.4 Çok Model Görsel Üretimi

- **shinpr/mcp-image** — Gemini, GPT Image, Flux, SD, Midjourney; otomatik prompt optimizasyonu
- **promptibus/mcp** — 67+ üretici AI modeli (Midjourney, Flux, Suno, Runway, DALL-E, SD)

### 11.5 Yerel Stable Diffusion (Ücretsiz)

- **Ichigo3766/image-gen-mcp**
- URL: https://github.com/Ichigo3766/image-gen-mcp
- **Ne İşe Yarar:** AUTOMATIC1111/ForgeUI API üzerinden yerel SD ile görsel üretimi.
- **Kullanım Senaryosu:** API maliyeti olmadan sınırsız görsel üretimi (kendi GPU'nuz gerekli).

### 11.6 WordPress'e Görsel Yükleme Akışı

```
1. Görsel üret → Stability AI / DALL-E MCP
2. Yerel kaydet
3. WordPress Media Library'ye yükle → WP REST API MCP
4. Media ID'yi al
5. Post'a featured image olarak ata
```

---

## 12. MCP: SOSYAL MEDYA

### 12.1 Çok Platform (75+ Araç)

**vanman2024/ayrshare-mcp**
- URL: https://github.com/vanman2024/ayrshare-mcp
- **Ne İşe Yarar:** 75+ araç: Facebook, Instagram, Twitter/X, LinkedIn, TikTok, YouTube, Pinterest, Reddit, Snapchat, Telegram, Threads, Bluesky, Google Business Profile.
- **Kullanım Senaryosu:** "Bu makaleyi yayımladım, özeti Twitter, LinkedIn ve Google Business Profile'a paylaş."

**posteverywhere/mcp**
- URL: https://github.com/posteverywhere/mcp
- **Ne İşe Yarar:** 8 platformda zamanlama/yayımlama. Claude Code, Claude Desktop, Cursor desteği.

### 12.2 Trend Takibi

**rugvedp/Trends-MCP**
- URL: https://github.com/rugvedp/Trends-MCP
- **Ne İşe Yarar:** YouTube, TikTok, Instagram Reels trend verileri.
- **Kullanım Senaryosu:** Hukuki konularda popüler olan içerik formatlarını tespit et.

---

## 13. MCP: REKLAM & MONETİZASYON

### 13.1 Google AdSense

**AppsYogi-com/adsense-mcp-server**
- URL: https://github.com/AppsYogi-com/adsense-mcp-server
- **Ne İşe Yarar:** AdSense hesabıyla doğrudan etkileşim. Gelir raporları, reklam birimi yönetimi.
- **Kullanım Senaryoları:**
  - "En yüksek RPM'li sayfaları listele, içerik stratejisi için analiz et."
  - "Bu hafta elde edilen geliri göster, geçen haftayla karşılaştır."

### 13.2 Google Ads

- **Resmi:** https://github.com/googleads/google-ads-mcp
- **Topluluk:** https://github.com/cohnen/mcp-google-ads
- **Çok platform:** https://github.com/amekala/ads-mcp (Google + Meta + LinkedIn + TikTok, 100+ araç)

### 13.3 Affiliate Marketing

**affise/mcp-affise**
- URL: https://github.com/affise/mcp-affise
- **Ne İşe Yarar:** Affise affiliate platformu veri ve analitiği. Kampanya analitiği, affiliate izleme, sahtekarlık tespiti.

**⚠️ Not:** ShareASale, CJ Affiliate veya Impact Radius için resmi MCP sunucusu yoktur (Mayıs 2026 itibarıyla). Özel MCP Cloudflare Workers üzerinde oluşturulabilir.

### 13.4 Çok Platform Reklam Yönetimi

**markifact/markifact-mcp**
- URL: https://github.com/markifact/markifact-mcp
- **Ne İşe Yarar:** Google Ads + Meta Ads + GA4 + TikTok Ads + LinkedIn Ads, 300+ operasyon. Her yazma işleminde insan onayı.

**Pipeboard**
- URL: https://pipeboard.co/
- **Ne İşe Yarar:** Meta + Google + TikTok + Snap + Reddit Ads tek MCP üzerinden. Kampanya analizi, harcama optimizasyonu.

### 13.5 Rekabetçi Monetizasyon Araştırması

Şu araçların kombinasyonunu kullanın:
- **Ahrefs MCP:** Trafik değeri, ücretli anahtar kelimeler
- **SE Ranking MCP:** AI arama görünürlüğü
- **DataForSEO MCP:** CPC verileri, SERP özellikleri

---

## 14. MCP: E-POSTA & OUTREACH

### 14.1 Gmail

**GongRzhe/Gmail-MCP-Server**
- URL: https://github.com/GongRzhe/Gmail-MCP-Server
- **Ne İşe Yarar:** Otomatik kimlik doğrulama ile tam Gmail yönetimi. Gönder, oku, ara, etiketle, taslak oluştur.
- **Kullanım Senaryoları:**
  - Affiliate program başvuruları gönder
  - Misafir post outreach e-postaları yaz ve gönder
  - Backlink isteklerini yönet

### 14.2 Soğuk E-posta (Link Building & Affiliate Başvuruları)

**AmeyMedewar/Cold-Mailer-MCP**
- URL: https://github.com/AmeyMedewar/Cold-Mailer-MCP
- **Ne İşe Yarar:** Soğuk e-postayı otomatikleştirir — şirket web sitelerini okur, kişiselleştirilmiş e-postalar yazar, taslak olarak kaydeder veya gönderir.
- **Kullanım Senaryoları:**
  - Affiliate program başvuruları
  - Misafir blog yazısı teklifleri
  - Backlink link building outreach

### 14.3 Çok Sağlayıcı

**marlinjai/email-mcp**
- Gmail, Outlook, iCloud ve IMAP için birleşik e-posta. OAuth2.
- URL: https://github.com/marlinjai/email-mcp

---

## 15. MCP: DÖKÜMAN & PDF

### 15.1 PDF Üretimi (Download Edilebilir Materyal)

**2b3pro/markdown2pdf-mcp**
- URL: https://github.com/2b3pro/markdown2pdf-mcp
- **Ne İşe Yarar:** Markdown → sözdizimi vurgulaması, özel stil, sayfa numaraları, filigranlarla PDF.
- **Kullanım Senaryosu:** "NDA şablonu makalesini indirilebilir PDF rehbere dönüştür, ClearLegalTips logosuyla."

**FabianGenell/pdf-mcp-server**
- URL: https://github.com/FabianGenell/pdf-mcp-server
- **Ne İşe Yarar:** Markdowndan profesyonel PDF'ler; çoklu temalar (Varsayılan, Profesyonel, Minimal, Koyu), üst/alt bilgiler, şablon sistemi.

**skmprb/md-mermaid-chart-pdf-mcp**
- URL: https://github.com/skmprb/md-mermaid-chart-pdf-mcp
- **Ne İşe Yarar:** Markdown + Mermaid diyagramları + ApexCharts → S3 entegrasyonu ile PDF.
- **Kullanım Senaryosu:** "Eyalet bazlı LLC ücretleri tablosu içeren bir PDF rapor üret."

### 15.2 PDF Okuma/İşleme

**jztan/pdf-mcp**
- URL: https://github.com/jztan/pdf-mcp
- **Ne İşe Yarar:** Büyük PDF'leri bağlam sınırı olmadan okur; parçalı okuma, OCR, tablo/görsel çıkarma, SQLite önbellek.
- **Kullanım Senaryosu:** Yasal dokümanları analiz et ve içerik için kaynak kullan.

### 15.3 WordPress İçin Döküman Akışı

```
1. İçerik yaz → Claude
2. PDF üret → markdown2pdf-mcp
3. WordPress Media Library'ye yükle → WP REST API MCP
4. İndirme sayfası/postu oluştur → WP REST API MCP
5. PDF'yi affiliate açılış sayfalarına lead magnet olarak ekle
```

---

## 16. MCP: OTOMASYON & ENTEGRASYON

### 16.1 Zapier (30.000+ Aksiyon)

- URL: https://github.com/zapier/zapier-mcp
- **Bu Claude oturumunda zaten mevcut:** `mcp__claude_ai_Zapier__*`
- **Ne İşe Yarar:** 30.000+ Zapier aksiyonu Claude'a sunulur.
- **Kullanım Senaryoları:**
  - WordPress post yayımlandı → Mailchimp kampanyası tetikle
  - Yeni backlink kazanıldı → Slack bildirimi gönder
  - Günlük gelir raporu → Google Sheets'e kaydet
  - Affiliate başvurusu onaylandı → Thirsty Affiliates'i güncelle

### 16.2 Composio (1.000+ Uygulama)

- URL: https://composio.dev/
- MCP: https://mcp.composio.dev/
- **Ne İşe Yarar:** 1.000+ önceden oluşturulmuş araç seti (Slack, GitHub, Notion, Google Workspace, Instagram, Meta Ads, Figma vb.)
- SOC 2 Tip II sertifikalı
- **Claude Code entegrasyonu:** https://composio.dev/toolkits/composio/framework/claude-code

### 16.3 GitHub — RESMİ

- URL: https://github.com/github/github-mcp-server
- **Ne İşe Yarar:** Tam GitHub API — repolar, issue'lar, PR'lar, kod arama, dosya yönetimi.
- **Kullanım Senaryosu:** WordPress tema/plugin geliştirme için versiyon kontrolü.

### 16.4 n8n Workflow Otomasyonu

- **tiagolemos05/claude-mcps-and-prompts:** Claude + MCP + n8n ile otomatize SEO blog üretimi; 0 → 6K impression 30 günde.

---

## 17. MCP: HOSTİNG & ALTYAPI

### 17.1 Cloudflare — RESMİ

**cloudflare/mcp-server-cloudflare**
- URL: https://github.com/cloudflare/mcp-server-cloudflare
- **Ne İşe Yarar:** Tam Cloudflare API — DNS, Workers, R2, Zero Trust, CDN ayarları. 2.500+ API endpoint.
- **Kullanım Senaryoları:**
  - WordPress CDN ayarlarını yönet
  - DNS kayıtlarını güncelle
  - Güvenlik kuralları oluştur
  - Sayfa cache kuralları ayarla

### 17.2 Özel MCP Sunucusu Oluşturma

ShareASale, CJ Affiliate veya Impact gibi resmi MCP olmayan affiliate platformları için:

**Cloudflare Workers üzerinde:**
```bash
wrangler generate benim-affiliate-mcp cloudflare/mcp-server-cloudflare-template
```

**Yerel TypeScript ile:**
```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
// ShareASale, CJ, Impact API araçları tanımla
```

---

## 18. TOPLULUK SKILLS & AGENTS

### 18.1 SEO/İçerik Yazımı Skillları

**aaron-he-zhu/seo-geo-claude-skills**
- URL: https://github.com/aaron-he-zhu/seo-geo-claude-skills
- **Skilllar:** keyword-research, content-brief, seo-content-writer, technical-audit, rank-tracking
- **Çerçeveler:** CORE-EEAT + CITE (Google'ın E-E-A-T + GEO optimizasyonu)
- **Claude Code, Cursor, Codex ve 35+ AI agent ile çalışır.**

**AgriciDaniel/claude-seo**
- URL: https://github.com/AgriciDaniel/claude-seo
- **25 alt-skill, 18 alt-agent** tam SEO yığını:
  - Teknik SEO denetimi
  - Schema markup üretimi
  - GEO/AEO optimizasyonu
  - Backlink analizi
  - Yerel SEO
  - Semantik kümeleme
  - E-ticaret SEO
  - Uluslararası SEO
  - Google API entegrasyonları (PageSpeed, GSC, GA4, Indexing API)
  - PDF/Excel raporlama
- **Web sitesi:** https://claude-seo.md/

**TheCraigHewitt/seomachine**
- URL: https://github.com/TheCraigHewitt/seomachine
- **Ne İşe Yarar:** Uzun form SEO blog içeriği için eksiksiz Claude Code workspace.

**tiagolemos05/claude-mcps-and-prompts**
- URL: https://github.com/tiagolemos05/claude-mcps-and-prompts
- **Ne İşe Yarar:** Otomatik SEO blog üretimi; n8n akışları + prompt'lar + stil kılavuzları
- **Sonuç:** 30 günde 0 → 6.000 impression (gerçek sonuç)

### 18.2 İçerik Takvimi / Konu Kümeleme

**Keyword Insights Content Calendar MCP**
- URL: https://suganthan.com/blog/content-calendar-mcp-server/
- **Ne İşe Yarar:** Keyword cluster CSV'lerini 3 dakikada planlanabilir içerik takvimlerine dönüştürür.

**SE Ranking skills repo**
- URL: https://github.com/seranking/seo-skills
- **Skilllar:** İçerik briefleri, AI arama ses payı, keyword kümeleri, rakip boşluk analizi.

### 18.3 Çok-Agent Koleksiyonları

**VoltAgent/awesome-claude-code-subagents**
- URL: https://github.com/VoltAgent/awesome-claude-code-subagents
- 100+ uzman subagent (WordPress, SEO, içerik, e-ticaret, analitik dahil)

**wshobson/agents**
- URL: https://github.com/wshobson/agents
- Claude Code için akıllı otomasyon ve çok-ajanlı orkestrasyon.

### 18.4 Genel Skill Koleksiyonları

**hesreallyhim/awesome-claude-code** (21.600+ star)
- URL: https://github.com/hesreallyhim/awesome-claude-code
- Seçilmiş skilllar, hooklar, slash-commandlar, agentlar, pluginler dizini.
- **Web:** https://awesomeclaude.ai/awesome-claude-code

**alirezarezvani/claude-skills**
- URL: https://github.com/alirezarezvani/claude-skills
- 263+ skill — mühendislik, pazarlama, ürün, uyum.

---

## 19. ÖNERİLEN KURULUM YAPISI

### .mcp.json (Proje Kökü)

```json
{
  "mcpServers": {
    "wordpress": {
      "command": "npx",
      "args": ["-y", "@instawp/mcp-wp"],
      "env": {
        "WP_URL": "https://siteniz.com",
        "WP_USER": "kullanici",
        "WP_APP_PASSWORD": "uygulama-sifresi"
      }
    },
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "api-key"
      }
    },
    "search-console": {
      "command": "npx",
      "args": ["-y", "@surendranb/google-search-console-mcp"],
      "env": {
        "GOOGLE_CLIENT_ID": "...",
        "GOOGLE_CLIENT_SECRET": "..."
      }
    },
    "pagespeed": {
      "command": "npx",
      "args": ["pagespeed-insights-mcp"],
      "env": { "PAGESPEED_API_KEY": "key" }
    },
    "brave-search": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-brave-search"],
      "env": { "BRAVE_API_KEY": "key" }
    },
    "gmail": {
      "command": "npx",
      "args": ["-y", "gmail-mcp-server"],
      "env": {
        "GMAIL_CLIENT_ID": "...",
        "GMAIL_CLIENT_SECRET": "..."
      }
    },
    "image-gen": {
      "command": "npx",
      "args": ["-y", "@stability-ai/mcp-server"],
      "env": { "STABILITY_API_KEY": "key" }
    },
    "pdf": {
      "command": "npx",
      "args": ["-y", "markdown2pdf-mcp"]
    }
  }
}
```

### Öncelik Sırası (İlk Kurulacaklar)

1. **WordPress MCP** — site ile doğrudan etkileşim
2. **Google Search Console MCP** — SEO izleme için temel
3. **Firecrawl MCP** — içerik araştırma ve rakip analizi
4. **Brave/Perplexity Search MCP** — derin araştırma
5. **Ahrefs veya DataForSEO MCP** — keyword verisi
6. **AdSense MCP** — gelir izleme
7. **Image Generation MCP** — featured image üretimi
8. **Gmail MCP** — affiliate başvuruları ve outreach

---

## 20. ÖNERİLEN AGENT PİPELİNE

### İçerik Üretim Pipeline'ı (Çok-Agent)

```
ORKESTRATÖR AGENT
│
├── ARAŞTIRMA AGENTLARI (paralel, Haiku modeli)
│   ├── Agent R1: Keyword araştırma → Ahrefs/SE Ranking MCP
│   ├── Agent R2: SERP analizi → DataForSEO MCP  
│   └── Agent R3: Rakip içerik denetimi → Firecrawl MCP
│
├── BRIEF YAZICI (Sonnet, sıralı)
│   └── Araştırma çıktılarından içerik briefleri oluşturur
│
├── İÇERİK YAZARLARI (paralel, Sonnet)
│   ├── Agent W1: Makale 1-2
│   ├── Agent W2: Makale 3-4
│   └── Agent W3: Makale 5
│
├── SEO OPTİMİZE EDİCİ (Sonnet, sıralı)
│   └── Schema markup, heading optimizasyonu, meta etiketler
│
├── GÖRSEL ÜRETICI (Haiku, paralel)
│   └── Stability AI MCP ile featured image üretimi
│
└── YAYINCI (Sonnet, sıralı)
    └── WordPress WP REST API MCP ile yükleme
```

### Keyword Araştırma → Makale Pipeline'ı

```
/keyword-research "hukuki döküman şablonları"
→ Ahrefs MCP: hacim, KD, amaç verisi
→ SE Ranking MCP: sıralama fırsatları
→ DataForSEO MCP: SERP analizi
→ Çıktı: Öncelikli keyword listesi

/content-brief "NDA nasıl yazılır"
→ Firecrawl: İlk 10 sıradaki sayfaları tara
→ Perplexity: Güncel yasal standartları araştır
→ Yapı: H1, H2'ler, FAQ soruları, dahili linkler
→ Çıktı: Yazar agenti için kapsamlı brief

/yaz-makale brief.md
→ Yazar agent: brieften taslak
→ SEO optimizer: schema, meta optimize et
→ Görsel agent: featured image üret
→ Yayıncı agent: WordPress'e taslak olarak yükle
```

### Affiliate Program Keşif Pipeline'ı

```
Araştırma Agent (Firecrawl + Web Search):
→ Rekabet alanındaki affiliate programlarını tespit et
→ Komisyon oranlarını ve koşulları karşılaştır
→ Başvuru gereksinimlerini analiz et

Brief Agent:
→ Her program için başvuru materyali hazırla
→ Site metriklerini ve içerik stratejisini özetle

Email Agent (Gmail MCP):
→ Kişiselleştirilmiş başvuru e-postaları yaz
→ Taslak olarak kaydet veya gönder
```

---

## 21. KAYNAKLAR

### Resmi Dokümantasyon
- Claude Code: https://code.claude.com/docs
- Hooks: https://code.claude.com/docs/en/hooks-guide
- Sub-Agents: https://code.claude.com/docs/en/sub-agents
- Skills: https://code.claude.com/docs/en/skills
- Memory: https://code.claude.com/docs/en/memory
- Agent Teams: https://code.claude.com/docs/en/agent-teams
- MCP Registry: https://registry.modelcontextprotocol.io/

### WordPress MCP
- WordPress/mcp-adapter (RESMİ): https://github.com/WordPress/mcp-adapter
- InstaWP/mcp-wp: https://github.com/InstaWP/mcp-wp
- Royal MCP SEO plugin: https://wordpress.org/plugins/royal-mcp/
- Karşılaştırma: https://instawp.com/best-wordpress-mcp-servers-compared/

### SEO MCP
- Ahrefs MCP: https://ahrefs.com/mcp/
- DataForSEO MCP: https://github.com/dataforseo/mcp-server-typescript
- Semrush MCP: https://github.com/mrkooblu/semrush-mcp
- SE Ranking MCP: https://seranking.com/api/integrations/mcp/
- Serpstat MCP: https://github.com/SerpstatGlobal/serpstat-mcp-server-js
- AgriciDaniel/claude-seo: https://github.com/AgriciDaniel/claude-seo
- SEO Machine: https://github.com/TheCraigHewitt/seomachine
- SEO/GEO Skillları: https://github.com/aaron-he-zhu/seo-geo-claude-skills

### Google Ürünleri MCP
- GSC: https://github.com/AminForou/mcp-gsc
- GA4 (RESMİ): https://github.com/googleanalytics/google-analytics-mcp
- Google Ads (RESMİ): https://github.com/googleads/google-ads-mcp
- AdSense: https://github.com/AppsYogi-com/adsense-mcp-server
- PageSpeed: https://github.com/ruslanlap/pagespeed-insights-mcp

### Görsel & İçerik
- Firecrawl: https://github.com/firecrawl/firecrawl-mcp-server
- Perplexity: https://docs.perplexity.ai/docs/getting-started/integrations/mcp-server
- Stability AI: https://github.com/tadasant/mcp-server-stability-ai
- Midjourney: https://github.com/AceDataCloud/MidjourneyMCP

### Sosyal Medya & E-posta
- Ayrshare (75+ araç): https://github.com/vanman2024/ayrshare-mcp
- Gmail: https://github.com/GongRzhe/Gmail-MCP-Server
- Soğuk e-posta: https://github.com/AmeyMedewar/Cold-Mailer-MCP

### PDF & Döküman
- markdown2pdf: https://github.com/2b3pro/markdown2pdf-mcp
- PDF okuma: https://github.com/jztan/pdf-mcp

### Otomasyon
- Zapier MCP: https://github.com/zapier/zapier-mcp
- Composio (1.000+ uygulama): https://composio.dev/
- Cloudflare MCP: https://github.com/cloudflare/mcp-server-cloudflare

### Awesome Listeler (Başlangıç Noktası)
- awesome-claude-code (21.6K star): https://github.com/hesreallyhim/awesome-claude-code
- awesome-mcp-servers: https://github.com/punkpeye/awesome-mcp-servers
- 100+ subagent: https://github.com/VoltAgent/awesome-claude-code-subagents
- Topluluk skill marketplace: https://tonsofskills.com

### Referans Makaleler
- Claude Code Advanced Patterns PDF: https://resources.anthropic.com/hubfs/Claude%20Code%20Advanced%20Patterns_%20Subagents,%20MCP,%20and%20Scaling%20to%20Real%20Codebases.pdf
- Hooks rehberi: https://github.com/disler/claude-code-hooks-mastery
- SEO blog otomasyonu 0→6K impression: https://github.com/tiagolemos05/claude-mcps-and-prompts
- Agent Teams 2026 Playbook: https://www.developersdigest.tech/blog/claude-code-agent-teams-subagents-2026

---

*Bu liste 2026-05-18 tarihinde Claude Code resmi dokümantasyonu, GitHub ve topluluk kaynakları üzerinden derin araştırma ile oluşturulmuştur. MCP ekosistemi hızla gelişmektedir; kurulumdan önce ilgili README dosyalarını güncel versiyonlar için kontrol edin.*
