# ClearLegalTips — MCP Kurulum Kontrol Listesi

**Tarih:** 2026-05-18  
**Amaç:** Ücretsiz MCP sunucularını öncelik sırasına göre kurmak

---

## Önce Bilmen Gerekenler

MCP sunucuları `.mcp.json` dosyasında tanımlı (`C:\Users\fatih\Desktop(1)\Claude\clear_legal_tips\.mcp.json`).  
API key'lerin `DOLDURUN` yazan yerlere girilmesi gerekiyor.  
Kurulumdan sonra Claude Code'u yeniden başlat — MCP sunucuları session başlangıcında yüklenir.

---

## P1 — Hemen Kur (Site Canlıya Geçince)

### 1. WordPress MCP (InstaWP/mcp-wp)

**Ne işe yarar:** Claude doğrudan WordPress'e bağlanır — post oluşturma, güncelleme, meta veri yazma, medya yükleme.

**Gereksinimler:**
- WordPress Application Password (admin panelinden)
- Canlı site URL'i

**Kurulum:**
```bash
# Node.js gerektiriyor (node -v ile kontrol et)
npm install -g @instawp/mcp-wp

# .mcp.json'da doldur:
# WP_URL: https://clearlegaltips.com
# WP_USER: admin kullanıcı adı
# WP_APP_PASSWORD: Users > Profile > Application Passwords
```

**Test:**
```
Claude'a sor: "WordPress siteme bağlan ve son 5 postu listele"
```

---

### 2. Google Search Console MCP

**Ne işe yarar:** GSC verilerini Claude'a çeker — hangi keyword'ler ranklanıyor, CTR, impression, pozisyon.

**Gereksinimler:** Google hesabı + GSC'ye eklenmiş site

**Adımlar:**
1. Google Cloud Console → Yeni proje oluştur
2. Search Console API'yi etkinleştir
3. OAuth 2.0 credentials oluştur (Desktop app)
4. `client_id` ve `client_secret`'ı al

**Kurulum:**
```bash
npm install -g @ahonn/mcp-server-gsc

# .mcp.json'da doldur:
# GOOGLE_CLIENT_ID: ...
# GOOGLE_CLIENT_SECRET: ...
# GOOGLE_REDIRECT_URI: http://localhost:3000/callback
```

**Test:**
```
Claude'a sor: "clearlegaltips.com için son 30 günün top 10 keyword'ünü göster"
```

---

### 3. PageSpeed Insights MCP

**Ne işe yarar:** Core Web Vitals (LCP, CLS, INP) ve genel PSI skoru — mobile + desktop.

**Gereksinimler:** Google API key (ücretsiz)

**API Key Alma:**
1. console.cloud.google.com → API & Services → Enable APIs
2. "PageSpeed Insights API" ara ve etkinleştir
3. Credentials → Create API Key

**Kurulum:**
```bash
npm install -g pagespeed-insights-mcp

# .mcp.json'da doldur:
# PAGESPEED_API_KEY: AIza...
```

**Test:**
```
Claude'a sor: "clearlegaltips.com ana sayfasının Core Web Vitals skorlarını göster"
```

---

## P2 — Site Canlıya Geçtikten Sonra Kur

### 4. Google Analytics 4 MCP

**Ne işe yarar:** Traffic analizi, user behavior, conversion funnel, channel attribution.

**Gereksinimler:** GA4 property + Analytics API erişimi

**Adımlar:**
1. analytics.google.com → ClearLegalTips property oluştur
2. Google Cloud → Analytics Admin API etkinleştir
3. OAuth credentials oluştur
4. GA4 Property ID'yi al (Measurement ID değil, Property ID)

**Kurulum:**
```bash
npm install -g @mario-hernandez/google-analytics-mcp-claude-code

# .mcp.json'da doldur:
# GA4_PROPERTY_ID: 123456789
# GOOGLE_CLIENT_ID + GOOGLE_CLIENT_SECRET
```

---

### 5. Brave Search MCP

**Ne işe yarar:** Web araması — Exa ve Ahrefs'in kapsamadığı nişler için, rakip içerik araştırması, güncel haber.

**Gereksinimler:** Brave Search API key (ücretsiz: 2.000 istek/ay)

**API Key Alma:** brave.com/search/api → Sign up → Free tier seç

**Kurulum:**
```bash
npm install -g @modelcontextprotocol/server-brave-search

# .mcp.json'da doldur:
# BRAVE_API_KEY: BSA...
```

---

### 6. PDF MCP (markdown2pdf)

**Ne işe yarar:** Markdown'dan profesyonel PDF oluşturur — downloadable legal guide'lar için.

**Gereksinimler:** Node.js (npm)

**Kurulum:**
```bash
npm install -g markdown2pdf-mcp
# API key gerekmez — .mcp.json'da "pdf" sunucusu hazır
```

**Kullanım:**
```
Claude'a sor: "workspace/templates/NDA_Template_2026.md dosyasından PDF oluştur"
```

---

## P3 — İsteğe Bağlı

### 7. Gmail MCP

**Ne işe yarar:** Claude üzerinden email gönder/oku — affiliate program başvuruları için.

**Kurulum:**
```bash
npm install -g gmail-mcp-server
# Gmail OAuth credentials gerekiyor (Google Cloud → Gmail API)
```

---

### 8. Playwright MCP

**Ne işe yarar:** Browser otomasyonu — affiliate linklerin çalışıp çalışmadığını test et, sayfa screenshot'ları.

**Kurulum:**
```bash
npm install -g @modelcontextprotocol/server-playwright
# API key gerekmez — .mcp.json'da "playwright" sunucusu hazır
```

---

### 9. GitHub MCP

**Ne işe yarar:** clearlegaltips-workspace reposunu Claude'dan yönet — dosya güncelleme, commit, issue açma.

**Gereksinimler:** GitHub Personal Access Token

**Token Alma:** github.com/settings/tokens → Generate new token → repo scope

**Kurulum:**
```bash
npm install -g @modelcontextprotocol/server-github

# .mcp.json'da doldur:
# GITHUB_PERSONAL_ACCESS_TOKEN: ghp_...
```

---

## Zaten Mevcut (Kurulum Gerektirmez)

Bu araçlar claude.ai entegrasyonu olarak her session'da hazır:

| Araç | Ne İşe Yarar |
|---|---|
| `mcp__claude_ai_Ahrefs__*` | Keyword data, backlinks, competitor analysis |
| `mcp__claude_ai_Exa__web_search_exa` | Gerçek zamanlı web araması |
| `mcp__claude_ai_Zapier__*` | 30.000+ uygulama entegrasyonu |
| `mcp__claude_ai_Google_Drive__*` | Google Drive dosya yönetimi |

---

## Genel Kontrol

```bash
# Kurulu MCP sunucularını listele
claude mcp list

# Belirli sunucuyu test et
claude mcp test wordpress

# Node.js var mı?
node -v
npm -v
```

---

## Skill'leri Test Et

```
/write-seo-post "how to write a cease and desist letter"
/keyword-research "small business legal documents"
/seo-audit
```

---

## Skills Konumu

```
.claude/
├── skills/
│   ├── write-seo-post/SKILL.md    → /write-seo-post
│   ├── keyword-research/SKILL.md  → /keyword-research
│   └── seo-audit/SKILL.md         → /seo-audit
└── agents/
    ├── content-researcher.md      → Agent: content-researcher
    └── seo-optimizer.md           → Agent: seo-optimizer
```
