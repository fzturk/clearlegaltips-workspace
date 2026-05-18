# Claude Code — Complete Reference for WordPress Affiliate & Ad Revenue Sites
**Research Date:** 2026-05-18  
**Scope:** All Claude Code capabilities, MCP servers, skills, hooks, agents, and tools relevant to building a professional WordPress site with strong Google rankings, affiliate revenue, and ad monetization.

---

## TABLE OF CONTENTS

1. [Claude Code Core Architecture](#1-claude-code-core-architecture)
2. [Memory System](#2-memory-system)
3. [Skills / Slash Commands](#3-skills--slash-commands)
4. [Hooks](#4-hooks)
5. [Subagents & Agent Teams](#5-subagents--agent-teams)
6. [Plugins](#6-plugins)
7. [MCP Servers — WordPress & CMS](#7-mcp-servers--wordpress--cms)
8. [MCP Servers — SEO & Search Analytics](#8-mcp-servers--seo--search-analytics)
9. [MCP Servers — Google Products](#9-mcp-servers--google-products)
10. [MCP Servers — Web Research & Scraping](#10-mcp-servers--web-research--scraping)
11. [MCP Servers — Image Generation](#11-mcp-servers--image-generation)
12. [MCP Servers — Social Media](#12-mcp-servers--social-media)
13. [MCP Servers — Advertising & Monetization](#13-mcp-servers--advertising--monetization)
14. [MCP Servers — Email & Outreach](#14-mcp-servers--email--outreach)
15. [MCP Servers — Documents & PDF](#15-mcp-servers--documents--pdf)
16. [MCP Servers — Automation & Integration](#16-mcp-servers--automation--integration)
17. [MCP Servers — Hosting & Infrastructure](#17-mcp-servers--hosting--infrastructure)
18. [Community Skills & Agents for WordPress/SEO](#18-community-skills--agents-for-wordpressseo)
19. [Recommended MCP Configuration for WordPress Projects](#19-recommended-mcp-configuration-for-wordpress-projects)
20. [Recommended Agent Pipeline Architecture](#20-recommended-agent-pipeline-architecture)
21. [Recommended Hook Configuration](#21-recommended-hook-configuration)
22. [Sources & Links Index](#22-sources--links-index)

---

## 1. CLAUDE CODE CORE ARCHITECTURE

Claude Code is Anthropic's official AI coding agent. It runs an agentic loop, selects tools, and maintains context across turns. The architecture has these layers:

| Layer | What It Is | Config Location |
|---|---|---|
| **Memory** | CLAUDE.md + auto-memory files | `~/.claude/`, `./CLAUDE.md` |
| **Skills** | Slash commands with SKILL.md files | `~/.claude/skills/`, `.claude/skills/` |
| **Hooks** | Shell scripts triggered at lifecycle events | `settings.json` |
| **Subagents** | Isolated workers with own context | `~/.claude/agents/`, `.claude/agents/` |
| **MCP Servers** | External tool access via JSON-RPC | `.mcp.json` or `settings.json` |
| **Plugins** | Bundled packages of skills+agents+hooks+MCP | `.claude-plugin/plugin.json` |

**Official Docs:** https://code.claude.com/docs  
**Sub-Agents Docs:** https://code.claude.com/docs/en/sub-agents  
**Skills Docs:** https://code.claude.com/docs/en/skills  
**Hooks Docs:** https://code.claude.com/docs/en/hooks-guide  
**Memory Docs:** https://code.claude.com/docs/en/memory  
**Agent Teams Docs:** https://code.claude.com/docs/en/agent-teams  
**Agent View Docs:** https://code.claude.com/docs/en/agent-view  

---

## 2. MEMORY SYSTEM

### 2.1 CLAUDE.md Files (You write these)

CLAUDE.md files give Claude persistent instructions across sessions. They load into every session context window.

**Locations and scopes:**

| Scope | Location | Applies To |
|---|---|---|
| Managed/Org | `C:\Program Files\ClaudeCode\CLAUDE.md` | All users on machine |
| User | `~/.claude/CLAUDE.md` | All your projects |
| Project | `./CLAUDE.md` or `./.claude/CLAUDE.md` | Team-shared via git |
| Local | `./CLAUDE.local.md` (gitignored) | Personal project prefs |

**Path-scoped Rules:** Place in `.claude/rules/` with YAML frontmatter:
```yaml
---
paths:
  - "wp-content/**/*.php"
---
# Rules that apply only to WordPress PHP files
```

**For WordPress:** Use CLAUDE.md to store:
- WordPress REST API base URL and auth method
- Affiliate program conventions and link formats
- SEO writing style guidelines
- Yoast/RankMath field naming conventions
- Post status workflows (draft → review → publish)
- Category and tag taxonomy conventions

**Run `/init`** to generate a CLAUDE.md from your project automatically.

### 2.2 Auto-Memory (Claude writes these)

Auto-memory is enabled by default in Claude Code v2.1.59+. Claude accumulates learnings across sessions.

- Stored at: `~/.claude/projects/<project>/memory/MEMORY.md`
- First 200 lines or 25KB loaded every session
- Topic files (debugging.md, api-conventions.md) loaded on demand
- Toggle with `/memory` command

**claude-mem plugin** (89K+ stars, Feb 2026): Extends auto-memory with SQLite FTS5 search and semantic compression. Highly recommended for long-running projects.

**Import syntax in CLAUDE.md:**
```markdown
@README.md
@wp-content/themes/mytheme/style.css
@~/.claude/my-affiliate-programs.md
```

### 2.3 Auto-Memory for Subagents

Each subagent can have its own persistent memory at `~/.claude/agent-memory/`. Enable in subagent config with `memory: user`.

---

## 3. SKILLS / SLASH COMMANDS

### 3.1 How Skills Work

A skill is a directory containing `SKILL.md`. The directory name becomes the `/slash-command`. Skills can also be invoked automatically by Claude when the description matches context.

**File locations:**
- Personal (all projects): `~/.claude/skills/<skill-name>/SKILL.md`
- Project: `.claude/skills/<skill-name>/SKILL.md`
- Plugin: `<plugin>/skills/<skill-name>/SKILL.md`

**SKILL.md structure:**
```yaml
---
name: write-seo-post
description: Write an SEO-optimized WordPress blog post. Use when user asks to write content, create a post, or draft an article.
disable-model-invocation: false
allowed-tools: Read Write Bash(wp *)
effort: high
---

Write a complete SEO-optimized post for WordPress:
1. Research the topic using web search
2. Create an outline with H2/H3 structure
3. Write ~1500-2000 words with target keyword in first 100 words
4. Add FAQ schema markup
5. Include 3-5 internal links
6. Write meta title (60 chars) and meta description (155 chars)
7. Suggest featured image alt text

Target keyword: $ARGUMENTS
```

**Dynamic context injection** (`!` prefix runs shell commands):
```yaml
---
name: check-seo-status
---
## Current GSC data
!`curl -s "https://mysite.com/wp-json/wp/v2/posts?status=draft"`

Analyze these draft posts and suggest which to publish first for SEO impact.
```

**Key frontmatter fields:**

| Field | Purpose |
|---|---|
| `description` | Tells Claude when to auto-invoke |
| `disable-model-invocation: true` | Only YOU can invoke (for /publish, /deploy) |
| `user-invocable: false` | Only Claude auto-invokes (background knowledge) |
| `allowed-tools` | Pre-approved tools (no permission prompt) |
| `context: fork` | Run in isolated subagent |
| `effort: high` | Use max reasoning |
| `model: claude-haiku-4-5` | Use cheaper model for simple tasks |
| `paths` | Only activate for matching file patterns |

### 3.2 Built-in Bundled Skills

These come with Claude Code and are available in every session:

| Skill | Command | Purpose |
|---|---|---|
| simplify | `/simplify` | Review code for quality/reuse |
| debug | `/debug` | Debug issues systematically |
| batch | `/batch` | Process multiple items |
| loop | `/loop` | Repeat a command on interval |
| claude-api | `/claude-api` | Build/debug Claude API code |
| review | `/review` | Review a pull request |
| security-review | `/security-review` | Security audit of changes |
| init | `/init` | Initialize CLAUDE.md |
| update-config | `/update-config` | Configure settings.json hooks |

### 3.3 Community WordPress/SEO Skills to Install

**WordPress Skills:**
- `elvismdev/claude-wordpress-skills` — Professional WordPress engineering skills
- `jorgerosal/wordpress-skills` — WordPress development skills and agents

**SEO/Content Skills:**
- `aaron-he-zhu/seo-geo-claude-skills` — 20 SEO & GEO skills: keyword research, content writing, technical audits, CORE-EEAT + CITE frameworks
- `AgriciDaniel/claude-seo` — Universal SEO skill: 25 sub-skills + 18 sub-agents covering full SEO stack
- `TheCraigHewitt/seomachine` — SEO Machine workspace for long-form, SEO-optimized blog content
- `alirezarezvani/claude-skills` — 263+ skills including engineering, marketing, compliance

**Skill Marketplaces:**
- `tonsofskills.com` — Community marketplace with ccpi CLI package manager (jeremylongshore/claude-code-plugins-plus-skills: 425 plugins, 2,810 skills, 200 agents)
- `agentskills.io` — Open standard for cross-tool skills

---

## 4. HOOKS

Hooks are deterministic shell scripts that run at lifecycle events regardless of what Claude decides to do.

### 4.1 Hook Events

| Event | When It Fires | WordPress Use Case |
|---|---|---|
| `PreToolUse` | Before ANY tool call | Block writes to production files, validate content |
| `PostToolUse` | After tool call completes | Auto-format PHP/CSS, run SEO checks after file edit |
| `Notification` | When Claude needs input | Desktop alert while content batch runs |
| `Stop` | When session ends | Log completed articles, update status in tracker |
| `SubagentStop` | When subagent finishes | Collect research output, trigger next pipeline step |
| `InstructionsLoaded` | When CLAUDE.md loads | Debug which rules are active |

### 4.2 Hook Configuration in settings.json

Location: `~/.claude/settings.json` (user-level) or `.claude/settings.json` (project-level)

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.file_path' | xargs php -l",
            "timeout": 10000
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
            "command": "powershell -Command \"Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.MessageBox]::Show('Claude Code needs your attention')\""
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
            "command": "echo \"Session ended: $(date)\" >> ~/wp-content-log.txt"
          }
        ]
      }
    ]
  }
}
```

### 4.3 Exit Codes

- **Exit 0:** Action proceeds normally
- **Exit 2:** Action is BLOCKED (write reason to stderr — Claude sees it)

### 4.4 Prompt-based and Agent-based Hooks

For decisions requiring judgment (not just pattern matching), hooks can call Claude:
```json
{
  "type": "prompt",
  "prompt": "Does this file edit comply with our affiliate disclosure requirements? Return ALLOW or BLOCK with reason."
}
```

### 4.5 WordPress-Specific Hook Examples

**Block edits to published posts (require confirmation):**
```bash
#!/bin/bash
# hook: PreToolUse, matcher: Edit|Write
FILE=$(echo "$1" | jq -r '.tool_input.file_path // empty')
if [[ "$FILE" == *"/posts/"* ]] && [[ "$FILE" == *"published"* ]]; then
  echo "BLOCKED: Use staging workflow for published posts" >&2
  exit 2
fi
```

**Run PHP lint after every PHP file edit:**
```bash
#!/bin/bash
# hook: PostToolUse, matcher: Edit|Write
FILE=$(cat | jq -r '.tool_input.file_path // empty')
if [[ "$FILE" == *.php ]]; then
  php -l "$FILE" || true
fi
```

**Auto-commit article drafts to git:**
```bash
#!/bin/bash
# hook: Stop
cd /path/to/wp-content
if git diff --quiet; then exit 0; fi
git add -A
git commit -m "Auto-save: content session $(date +%Y%m%d-%H%M)"
```

**References:**
- Official hooks docs: https://code.claude.com/docs/en/hooks-guide
- Hooks mastery repo: https://github.com/disler/claude-code-hooks-mastery
- Complete guide: https://claudefa.st/blog/tools/hooks/hooks-guide

---

## 5. SUBAGENTS & AGENT TEAMS

### 5.1 Built-in Subagents

| Subagent | Model | Tools | Purpose |
|---|---|---|---|
| Explore | Haiku (fast) | Read-only | File discovery, code search |
| Plan | Inherits | Read-only | Research before planning |
| general-purpose | Inherits | All | Complex multi-step tasks |
| statusline-setup | Sonnet | — | Status line configuration |
| claude-code-guide | Haiku | — | Feature help |

### 5.2 Creating Custom Subagents

Use `/agents` command or create a `.md` file in `~/.claude/agents/` or `.claude/agents/`:

```markdown
---
name: wp-content-researcher
description: Research topics for WordPress blog posts. Use when asked to research a topic, find sources, gather data, or create content briefs.
model: claude-sonnet-4-6
tools: WebSearch WebFetch Bash(curl *)
memory: user
---

You are a specialist content researcher for a legal tips blog.

When researching:
1. Search for the topic + "explained" + current year
2. Find 5-10 authoritative sources (gov sites, law firms, established publications)
3. Extract key facts, statistics, and expert quotes
4. Identify primary and secondary keywords
5. Find related questions people ask (for FAQ sections)
6. Check what competitors rank for on this topic
7. Produce a structured research brief

Always cite sources with full URLs.
```

**Subagent config fields:**

| Field | Options | Notes |
|---|---|---|
| `model` | claude-haiku-4-5, claude-sonnet-4-6, etc. | Haiku = cheaper/faster |
| `tools` | Space-separated tool list | Read-only = Explore-like |
| `memory` | user, none | Persistent learning across sessions |
| `permissions` | Inherit parent or restrict | Override trust level |
| `skills` | Space-separated skill names | Preload skills into subagent |

### 5.3 Agent Teams (Parallel Execution)

Agent teams run multiple Claude instances in parallel, coordinating via a shared task file.

**Command:** `claude --team` or `/bg` to background a session

**Agent View** (May 2026): `claude agents` — single dashboard showing all sessions, token usage, status, needs-input alerts.

**Background sessions:** `claude --bg "Research and write draft for: NDA basics"` — returns immediately, Claude works async.

**WordPress Content Pipeline with Agent Teams:**
```
Orchestrator
├── Agent 1: Keyword Researcher (finds 10 article opportunities)
├── Agent 2: Content Researcher (gathers sources for each topic)  
├── Agent 3: Writer (drafts articles from briefs)
├── Agent 4: SEO Optimizer (adds schema, optimizes headings, meta)
└── Agent 5: WP Publisher (uploads to WordPress via REST API)
```

**Token cost:** Parallel agents consume tokens in parallel (~3x faster but ~3x cost). Use Haiku agents for research/simple tasks.

**Resources:**
- https://code.claude.com/docs/en/agent-teams
- https://github.com/VoltAgent/awesome-claude-code-subagents (100+ specialized subagents)
- https://github.com/wshobson/agents (multi-agent orchestration for Claude Code)

---

## 6. PLUGINS

Plugins bundle skills + agents + hooks + MCP servers into a single installable unit.

**Plugin structure:**
```
my-wordpress-plugin/
├── .claude-plugin/
│   └── plugin.json          # Manifest
├── skills/
│   ├── wp-publish/SKILL.md
│   └── seo-optimize/SKILL.md
├── agents/
│   └── content-researcher.md
├── hooks/
│   └── post-edit-lint.sh
└── .mcp.json                # Bundled MCP servers
```

**Install:** `claude plugin install <path-or-url>`

**Popular plugins (2026):**
- Frontend Design (96K installs) — UI/CSS generation
- Context7 (71K installs) — Up-to-date library documentation
- Ralph Loop (57K installs) — Iterative autonomous development
- Code Review (50K installs) — Systematic code review
- Playwright (28K installs) — Browser automation and testing

**Claude.ai Plugin Directory:** https://claude.com/plugins  
**Community repo:** https://github.com/Chat2AnyLLM/awesome-claude-plugins  
**Marketplace:** https://tonsofskills.com (9,000+ plugins as of Feb 2026)

---

## 7. MCP SERVERS — WORDPRESS & CMS

MCP servers expose external APIs as Claude tools. Configure in `.mcp.json` at project root or in `~/.claude/settings.json`.

### 7.1 WordPress Core MCP Servers

**WordPress/mcp-adapter (OFFICIAL — Automattic/WordPress.org)**
- URL: https://github.com/WordPress/mcp-adapter
- What: Official MCP adapter bridging WordPress Abilities API to MCP protocol
- Features: Core abilities (get-site-info, get-user-info, etc.), extensible via plugins registering new abilities, HTTP and STDIO transport
- Install: `npm install @wordpress/mcp-adapter`
- Note: WordPress 6.9+ required for Abilities API; becoming canonical standard
- Replaces deprecated: https://github.com/Automattic/wordpress-mcp

**InstaWP/mcp-wp**
- URL: https://github.com/InstaWP/mcp-wp
- What: MCP Server for WordPress via REST API, Node.js/TypeScript
- Features: Posts, pages, media, plugins, users, comments, multi-site support
- Install: `npx -y @instawp/mcp-wp` (one-line launch)
- Auth: Application Passwords (fine-grained access control)
- Docker support available
- Managed cloud version: instawp.com (single-click activation)

**wolffcatskyy/wordpress-mcp**
- URL: https://github.com/wolffcatskyy/wordpress-mcp
- What: Manage WordPress via REST API from Claude Desktop/Code
- Features: Create, edit, publish posts, manage categories/tags, site config

**gaupoit/wordpress-mcp**
- URL: https://github.com/gaupoit/wordpress-mcp
- What: Connect Claude Code/Cursor to WordPress via REST API
- Features: CRUD for posts, pages, media, users

**Automattic/mcp-wordpress-remote**
- URL: https://github.com/Automattic/mcp-wordpress-remote
- What: Remote WordPress MCP proxy
- Auth: OAuth 2.0, JWT, Application Passwords

**mcp-wp (CloudFest Hackathon origin)**
- URL: https://mcp-wp.github.io/docs
- What: WP-CLI integration with STDIO transport per MCP spec
- Features: Full WP-CLI command support

**juanma-wp/wordpress-org-mcp**
- URL: https://github.com/juanma-wp/wordpress-org-mcp
- What: Analyze, download, compare WordPress.org plugins for local use

### 7.2 WooCommerce MCP Servers

**WooCommerce official MCP**
- URL: https://developer.woocommerce.com/docs/features/mcp/
- What: Official WooCommerce MCP via local proxy pattern
- Integration: Works with WordPress MCP adapter

**woocommerce/woocommerce-claude**
- URL: https://github.com/woocommerce/woocommerce-claude
- What: AI-powered analytics — ask your store anything

**AmitGurbani/mcp-server-woocommerce**
- URL: https://github.com/AmitGurbani/mcp-server-woocommerce
- What: 101 tools — products, orders, customers, coupons, shipping, taxes, reports

**techspawn/woocommerce-mcp-server**
- URL: https://github.com/techspawn/woocommerce-mcp-server
- What: JSON-RPC 2.0 WooCommerce REST API server

### 7.3 WordPress SEO Plugin Integrations via MCP

**Royal MCP (WordPress.org plugin)**
- URL: https://wordpress.org/plugins/royal-mcp/
- What: Auto-detects Yoast SEO or Rank Math; reads/writes title, description, focus keyword, robots, OG fields via MCP

**WP MCP Ultimate / Easy MCP AI**
- URL: https://wordpress.com/plugins/easy-mcp-ai
- What: 58 abilities including Yoast and RankMath SEO metadata get/update, rendered SEO head output

**SEO Engine (free plugin)**
- URL: https://wordpress.org/plugins/seo-engine/
- What: Full MCP support; entire site SEO data queryable via Claude

**SEO Pilot Premium**
- URL: https://wildbeimwild.com/en/ai-translate-pro/seo-pilot/
- What: MCP Server Endpoint for AI agents; exposes meta tags, schema, redirects, audit results

---

## 8. MCP SERVERS — SEO & SEARCH ANALYTICS

### 8.1 Multi-Tool SEO Platforms

**AgriciDaniel/claude-seo**
- URL: https://github.com/AgriciDaniel/claude-seo
- What: Universal SEO skill + 25 sub-skills + 18 sub-agents
- Covers: Technical SEO, E-E-A-T, schema, GEO/AEO, backlinks, local SEO, semantic clustering, e-commerce SEO, international SEO, Google APIs, PDF/Excel reporting
- Optional MCP extensions: DataForSEO, Firecrawl, Banana (image gen)
- Website: https://claude-seo.md/

**DataForSEO/mcp-server-typescript**
- URL: https://github.com/dataforseo/mcp-server-typescript (via Skobyn/dataforseo-mcp-server)
- What: Live keyword, SERP, and backlink data; 100s of tools
- Setup: `npx @dataforseo/mcp-server` + API key
- Cost: Pay-per-use DataForSEO API

### 8.2 Ahrefs MCP

**Official Ahrefs MCP**
- URL: https://ahrefs.com/mcp/
- Package: `@ahrefs/mcp`
- What: Backlinks, keyword data, domain ratings, competitive analysis
- Auth: Ahrefs API key
- Note: Available as claude.ai integrated MCP (already in this Claude instance via `mcp__claude_ai_Ahrefs__*` tools)

**cnych/seo-mcp (free Ahrefs scraper)**
- URL: https://github.com/cnych/seo-mcp
- What: Free Ahrefs data via scraping; backlinks, keyword ideas
- 240 stars

### 8.3 Semrush MCP

**mrkooblu/semrush-mcp**
- URL: https://github.com/mrkooblu/semrush-mcp
- What: 77 tools — domain analytics, keyword research, backlinks, traffic, competitive intel
- Auth: Semrush API key

**Official Semrush connector:** Available in Claude.ai directory

### 8.4 SE Ranking MCP

**SE Ranking official MCP**
- URL: https://seranking.com/api/integrations/mcp/
- What: 160+ tools — keyword research, backlinks, domain analysis, site audits, AI search visibility, SERP analysis
- Skills repo: https://github.com/seranking/seo-skills
- Auth: SE Ranking API key

### 8.5 Serpstat MCP

**SerpstatGlobal/serpstat-mcp-server-js**
- URL: https://github.com/SerpstatGlobal/serpstat-mcp-server-js
- What: 65 tools — domain analysis, keyword research, backlinks, site audit, rank tracking, AI Overview monitoring
- Auth: Serpstat API key

### 8.6 Google Search Console MCP

Multiple implementations available:

| Repo | Features | URL |
|---|---|---|
| AminForou/mcp-gsc | OAuth browser flow, 20 tools, up to 25K rows | https://github.com/AminForou/mcp-gsc |
| ahonn/mcp-server-gsc | 25K rows, quick wins detection, advanced filtering | https://github.com/ahonn/mcp-server-gsc |
| saurabhsharma2u/search-console-mcp | GSC + Bing + GA4 combined | https://github.com/saurabhsharma2u/search-console-mcp |
| ncosentino/google-search-console-mcp | 50K rows per query | https://github.com/ncosentino/google-search-console-mcp |
| surendranb/google-search-console-mcp | Claude/Cursor/Windsurf support | https://github.com/surendranb/google-search-console-mcp |

**All use OAuth; data stays local on your machine.**

### 8.7 Bing Webmaster Tools MCP

**isiahw1/mcp-server-bing-webmaster**
- URL: https://github.com/isiahw1/mcp-server-bing-webmaster
- What: 40+ tools — search analytics, crawl diagnostics, URL submission, sitemap, keyword research, link analysis

**Multivariate-AI-Inc/bing-webmaster-mcp-server**
- URL: https://mcpservers.org/servers/Multivariate-AI-Inc/bing-webmaster-mcp-server
- What: Full Bing Webmaster Tools API access

### 8.8 PageSpeed Insights / Lighthouse

**ruslanlap/pagespeed-insights-mcp**
- URL: https://github.com/ruslanlap/pagespeed-insights-mcp
- What: Core Web Vitals (LCP, CLS, INP), screenshots, loading timelines, network analysis
- Install: `npx pagespeed-insights-mcp`

**ncosentino/google-psi-mcp**
- URL: https://github.com/ncosentino/google-psi-mcp
- What: PageSpeed Insights with Core Web Vitals ratings and 0-100 scores

**SiteAudit MCP**
- URL: https://github.com/hesreallyhim/awesome-claude-code/issues/1553
- What: 11 tools — SEO analysis, Lighthouse scores via PSI, security headers

### 8.9 Structured Data / Schema MCP

**Structured Data Extractor (Apify)**
- URL: https://apify.com/tropical_quince/structured-data-extractor/api/mcp
- What: Extracts and validates JSON-LD, Microdata, RDFa from any page

**SEO Inspector & Schema Validator**
- URL: https://playbooks.com/mcp/seo-inspector
- What: Validates structured data schemas, SEO issues directly from codebase

**InfraNodus SEO Skill**
- URL: https://infranodus.com/skills/seo
- What: Advanced topical clustering and content gap detection

---

## 9. MCP SERVERS — GOOGLE PRODUCTS

### 9.1 Google Analytics 4

**googleanalytics/google-analytics-mcp (OFFICIAL)**
- URL: https://github.com/googleanalytics/google-analytics-mcp
- What: Official Google MCP using Analytics Admin API + Data API
- Auth: OAuth 2.0
- Note: Already available in this Claude instance via Ahrefs integration

**mario-hernandez/google-analytics-mcp-claude-code**
- URL: https://github.com/mario-hernandez/google-analytics-mcp-claude-code
- What: Specialized for Claude Code with anomaly detection, traffic-drop classification, content decay analysis, conversion funnel, GSC→GA4 journey, channel attribution

**surendranb/google-analytics-mcp**
- URL: https://github.com/surendranb/google-analytics-mcp
- What: Analysis-ready access to traffic, user behavior, performance with schema discovery

**judicael-s/google-analytics-skill**
- URL: https://github.com/judicael-s/google-analytics-skill
- What: Claude Code skill file + mcp-server-google-analytics config for guided workflows

**Multi-platform: irinabuht12-oss/google-meta-ads-ga4-mcp**
- URL: https://github.com/irinabuht12-oss/google-meta-ads-ga4-mcp
- What: 250+ tools — Google Ads + Meta Ads + GA4 in one server

### 9.2 Google Ads

**Official Google Ads MCP**
- URL: https://github.com/googleads/google-ads-mcp
- Developer docs: https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server
- What: Official MCP using Google Ads API for LLMs

**freema/mcp-google-marketing**
- URL: https://github.com/freema/mcp-google-marketing
- What: Google Analytics + Search Console + Google Ads in one server

### 9.3 Google AdSense

**AppsYogi-com/adsense-mcp-server**
- URL: https://github.com/AppsYogi-com/adsense-mcp-server
- What: CLI-installable MCP for Claude/Cursor to interact with Google AdSense account
- Features: Revenue reporting, ad unit management, account analytics

### 9.4 Google Search (Web Search)

**mixelpixx/Google-Research-MCP**
- URL: https://github.com/mixelpixx/Google-Search-MCP-Server
- What: Google search + follow links + research websites; built for Claude Code

---

## 10. MCP SERVERS — WEB RESEARCH & SCRAPING

### 10.1 Web Scraping

**firecrawl/firecrawl-mcp-server (OFFICIAL)**
- URL: https://github.com/firecrawl/firecrawl-mcp-server
- What: Official Firecrawl MCP — search, scrape, crawl; JavaScript rendering, batch processing
- Install: `npx -y firecrawl-mcp`
- Auth: Firecrawl API key
- Use case: Full-site competitor crawls, content research, outlink discovery

**Playwright MCP**
- Package: `@modelcontextprotocol/server-playwright`
- What: Browser automation, screenshots, form filling, JavaScript execution
- Use case: Testing affiliate links, checking page layouts, screenshots for articles

**Puppeteer MCP**
- Package: `@modelcontextprotocol/server-puppeteer`
- What: Browser control for Claude Desktop
- Use case: Web scraping, automated screenshots

### 10.2 Deep Research / AI Search

**Exa AI MCP**
- Package: `@exa-ai/mcp-server`
- What: Real-time web search, academic papers, Twitter/X search via Exa API
- Note: Already available in this Claude instance as `mcp__claude_ai_Exa__web_search_exa`

**Perplexity MCP (OFFICIAL)**
- Install: `claude mcp add perplexity --env PERPLEXITY_API_KEY="key" -- npx -y @perplexity-ai/mcp-server`
- What: Real-time web search + deep research via Sonar models
- URL: https://docs.perplexity.ai/docs/getting-started/integrations/mcp-server

**Brave Search MCP**
- Package: `@modelcontextprotocol/server-brave-search`
- What: Web, local business, image, video, news search with safety controls
- Auth: Brave Search API key (free tier available)

**mcp-omnisearch**
- URL: https://github.com/spences10/mcp-omnisearch
- What: Unified access to Tavily + Perplexity + Kagi + Jina + Brave + Exa + Firecrawl

**web-search-plus-mcp**
- URL: https://github.com/robbyczgw-cla/web-search-plus-mcp
- What: 10 search providers with intelligent auto-routing by query intent

---

## 11. MCP SERVERS — IMAGE GENERATION

### 11.1 AI Image Generation

**AceDataCloud/MidjourneyMCP**
- URL: https://github.com/AceDataCloud/MidjourneyMCP
- What: Midjourney image and video generation via AceDataCloud API
- Use case: Generate featured images, social media graphics, infographics

**tadasant/mcp-server-stability-ai**
- URL: https://github.com/tadasant/mcp-server-stability-ai
- What: Stability AI (Stable Diffusion) — generate, edit, upscale images
- Auth: Stability AI API key

**DALL-E Image Generator (sammyl720)**
- URL: https://www.pulsemcp.com/servers/sammyl720-dall-e-image-generator
- What: DALL-E 3 integration for on-demand image generation

**shinpr/mcp-image**
- URL: https://github.com/shinpr/mcp-image
- What: Multi-model image generation (Gemini, GPT Image, Flux, SD, Midjourney)
- Features: Automatic prompt optimization, quality presets

**promptibus/mcp**
- URL: https://github.com/promptibus/mcp
- What: 67+ generative AI models — Midjourney, Flux, Suno, Runway, DALL-E, Stable Diffusion
- 7 tools for any MCP client

**Ichigo3766/image-gen-mcp**
- URL: https://github.com/Ichigo3766/image-gen-mcp
- What: Stable Diffusion WebUI API (ForgeUI/AUTOMATIC-1111) for local SD
- Use case: Free local image generation with full control

**nikolausm/huggingface-mcp-server**
- URL: https://github.com/nikolausm/huggingface-mcp-server
- What: Hugging Face API — Stable Diffusion and other models
- Note: Also available as `mcp__claude_ai_Hugging_Face__*` in this session

**AI Image Studio (Apify)**
- URL: https://apify.com/alizarin_refrigerator-owner/ai-image-studio/api/mcp
- What: DALL-E + Stable Diffusion + Midjourney multi-model server

### 11.2 Image Optimization for WordPress

Use Firecrawl + WP REST API for automated image upload workflows:
1. Generate image via DALL-E/Stability MCP
2. Save locally
3. Upload to WordPress Media Library via REST API
4. Get media ID for post assignment

---

## 12. MCP SERVERS — SOCIAL MEDIA

### 12.1 Multi-Platform Posting

**vanman2024/ayrshare-mcp**
- URL: https://github.com/vanman2024/ayrshare-mcp
- What: 75+ tools via Ayrshare API — Facebook, Instagram, Twitter/X, LinkedIn, TikTok, YouTube, Pinterest, Reddit, Snapchat, Telegram, Threads, Bluesky, Google Business Profile
- Use case: Auto-post published WordPress articles to all social channels

**posteverywhere/mcp**
- URL: https://github.com/posteverywhere/mcp
- What: Schedule/publish posts to Instagram, X, TikTok, LinkedIn, YouTube, Facebook, Threads, Pinterest
- Works with Claude Code, Claude Desktop, Cursor

**Socialync MCP**
- URL: https://www.socialync.io/blog/best-social-media-mcp-servers-2026
- What: All 8 major platforms (TikTok, Instagram, YouTube, X, LinkedIn, Facebook, Threads, Bluesky)

### 12.2 Single-Platform

**EnesCinr/twitter-mcp**
- URL: https://github.com/EnesCinr/twitter-mcp
- What: Post tweets, search Twitter

**rugvedp/Trends-MCP**
- URL: https://github.com/rugvedp/Trends-MCP
- What: Trending data from YouTube, TikTok, Instagram Reels
- Use case: Find trending topics for content calendar

---

## 13. MCP SERVERS — ADVERTISING & MONETIZATION

### 13.1 Google AdSense

**AppsYogi-com/adsense-mcp-server**
- URL: https://github.com/AppsYogi-com/adsense-mcp-server
- What: Interact with AdSense account from Claude/Cursor
- Features: Revenue reports, ad unit management, account analytics
- Auth: Google OAuth

### 13.2 Google Ads

**Official:** https://github.com/googleads/google-ads-mcp  
**Community:** https://github.com/cohnen/mcp-google-ads  
**Multi-platform:** https://github.com/amekala/ads-mcp (Google + Meta + LinkedIn + TikTok, 100+ tools)

### 13.3 Affiliate Marketing

**affise/mcp-affise**
- URL: https://github.com/affise/mcp-affise
- What: Affise affiliate platform data and analytics
- Features: Campaign analytics, affiliate monitoring, fraud detection

**wecantrack integration**
- Tracks affiliate conversions from display + affiliate channels
- API available for custom MCP integration

**Note:** No official MCP servers found for ShareASale, CJ Affiliate, or Impact Radius as of May 2026. Build custom MCP using their REST APIs.

### 13.4 Multi-Platform Ad Management

**markifact/markifact-mcp**
- URL: https://github.com/markifact/markifact-mcp
- What: Google Ads + Meta Ads + GA4 + TikTok Ads + LinkedIn Ads, 300+ operations
- Human-in-the-loop on every write action

**Pipeboard**
- URL: https://pipeboard.co/
- What: Meta + Google + TikTok + Snap + Reddit Ads via single MCP
- Features: Campaign analysis, spend optimization, automated operations

### 13.5 Competitive Monetization Research

Use combination of:
- Ahrefs MCP (traffic value, paid keywords)
- SE Ranking MCP (AI search visibility)
- DataForSEO MCP (CPC data, SERP features)

---

## 14. MCP SERVERS — EMAIL & OUTREACH

### 14.1 Gmail

**GongRzhe/Gmail-MCP-Server**
- URL: https://github.com/GongRzhe/Gmail-MCP-Server
- What: Full Gmail management with auto-authentication
- Features: Send, read, search, label, draft emails

### 14.2 Multi-Provider Email

**marlinjai/email-mcp**
- URL: https://github.com/marlinjai/email-mcp
- What: Unified email for Gmail, Outlook, iCloud, and IMAP
- Auth: OAuth2

### 14.3 SMTP/IMAP

**yunfeizhu/mcp-mail-server**
- URL: https://github.com/yunfeizhu/mcp-mail-server
- What: IMAP + SMTP via MCP; TypeScript, npm/npx deployment
- Config: smtp.gmail.com:587 for Gmail

**ai-zerolab/mcp-email-server**
- URL: https://github.com/ai-zerolab/mcp-email-server
- What: IMAP and SMTP MCP server

### 14.4 Cold Outreach

**AmeyMedewar/Cold-Mailer-MCP**
- URL: https://github.com/AmeyMedewar/Cold-Mailer-MCP
- What: Automates cold email — reads company websites, writes personalized emails, sends or saves as drafts
- Use case: Affiliate program applications, guest post outreach, link building

---

## 15. MCP SERVERS — DOCUMENTS & PDF

### 15.1 PDF Generation

**2b3pro/markdown2pdf-mcp**
- URL: https://github.com/2b3pro/markdown2pdf-mcp
- What: Markdown → PDF with syntax highlighting, custom styling, page numbers, watermarks
- Use case: Generate downloadable legal guides from article content

**FabianGenell/pdf-mcp-server**
- URL: https://github.com/FabianGenell/pdf-mcp-server
- What: Professional PDFs from markdown; multiple themes (Default, Professional, Minimal, Dark), headers/footers, template system

**skmprb/md-mermaid-chart-pdf-mcp**
- URL: https://github.com/skmprb/md-mermaid-chart-pdf-mcp
- What: Markdown + Mermaid diagrams + ApexCharts → PDF with S3 integration

### 15.2 PDF Reading/Processing

**jztan/pdf-mcp**
- URL: https://github.com/jztan/pdf-mcp
- What: Read large PDFs without context limits; chunked reading, OCR, table/image extraction, SQLite cache

**gufao/mcp-server-stirling-pdf**
- URL: https://github.com/gufao/mcp-server-stirling-pdf
- What: 10 tools — merge, split, watermark, OCR, compress PDFs via self-hosted Stirling PDF

**pdfdotco/pdfco-mcp**
- URL: https://github.com/pdfdotco/pdfco-mcp
- What: PDF.co API — convert to JSON/CSV/Text/Excel, convert documents to PDF

### 15.3 Document Workflow for WordPress

Recommended pipeline for downloadable content:
1. Write content in Claude
2. Generate PDF via markdown2pdf-mcp
3. Upload to WordPress Media Library via REST API MCP
4. Create download page/post linking to PDF
5. Add PDF to affiliate landing pages as lead magnets

---

## 16. MCP SERVERS — AUTOMATION & INTEGRATION

### 16.1 Zapier (30,000+ Actions)

**zapier/zapier-mcp**
- URL: https://github.com/zapier/zapier-mcp
- What: 30,000+ Zapier actions available to Claude
- Note: Already available in this Claude instance as `mcp__claude_ai_Zapier__*`
- Use cases: Trigger WordPress post publication → Mailchimp campaign, Slack notification, Google Sheets logging

### 16.2 Composio (1,000+ Apps)

**composio.dev**
- URL: https://composio.dev/
- MCP: https://mcp.composio.dev/
- What: 1,000+ pre-built toolkits (Slack, GitHub, Notion, Google Workspace, Instagram, Meta Ads, Figma, etc.)
- SOC 2 Type II certified
- Dynamic tool routing per task
- Claude Code integration: https://composio.dev/toolkits/composio/framework/claude-code

### 16.3 GitHub

**github/github-mcp-server (OFFICIAL)**
- URL: https://github.com/github/github-mcp-server
- What: Full GitHub API — repos, issues, PRs, code search, file management
- Use case: Version control for WordPress theme/plugin development

### 16.4 n8n Workflow Automation

Use n8n + Claude Code for:
- `tiagolemos05/claude-mcps-and-prompts` — Automated SEO blog generation using Claude with MCPs; 0 → 6K impressions in 30 days via n8n workflows

---

## 17. MCP SERVERS — HOSTING & INFRASTRUCTURE

### 17.1 Cloudflare

**cloudflare/mcp-server-cloudflare**
- URL: https://github.com/cloudflare/mcp-server-cloudflare
- What: Full Cloudflare API — DNS, Workers, R2, Zero Trust, CDN settings
- 2,500+ API endpoints via search() and execute() tools
- Use case: Manage WordPress CDN, DNS, security settings via Claude

**cloudflare/workers-mcp**
- URL: https://github.com/cloudflare/workers-mcp
- What: Connect Claude Desktop to Cloudflare Workers
- Deploy custom MCP servers on Cloudflare globally

### 17.2 Build Custom MCP Servers

If you need integrations that don't exist yet (ShareASale API, specific affiliate networks, custom WordPress REST endpoints):

**Build on Cloudflare Workers:**
```bash
wrangler generate my-affiliate-mcp cloudflare/mcp-server-cloudflare-template
# Connect to GitHub/GitLab for auto-deploy
```

**Build locally in TypeScript:**
```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
// Define tools for ShareASale, CJ, Impact APIs
```

---

## 18. COMMUNITY SKILLS & AGENTS FOR WORDPRESS/SEO

### 18.1 SEO/Content Writing Skills

**aaron-he-zhu/seo-geo-claude-skills**
- URL: https://github.com/aaron-he-zhu/seo-geo-claude-skills
- Skills: keyword-research, content-brief, seo-content-writer, technical-audit, rank-tracking
- Frameworks: CORE-EEAT + CITE
- Works with: Claude Code, Cursor, Codex, 35+ AI agents

**AgriciDaniel/claude-seo**
- URL: https://github.com/AgriciDaniel/claude-seo
- 25 sub-skills, 18 sub-agents covering full SEO stack
- Google APIs: PageSpeed, Search Console, GA4, Indexing API
- Website: https://claude-seo.md/

**TheCraigHewitt/seomachine**
- URL: https://github.com/TheCraigHewitt/seomachine
- What: Complete Claude Code workspace for long-form SEO blog content

**tiagolemos05/claude-mcps-and-prompts**
- URL: https://github.com/tiagolemos05/claude-mcps-and-prompts
- What: Automated SEO blog generation; n8n workflows + prompts + style guides
- Result: 0 → 6K impressions in 30 days

### 18.2 Content Calendar / Topic Cluster Skills

**Keyword Insights Content Calendar MCP**
- URL: https://suganthan.com/blog/content-calendar-mcp-server/
- What: Turns keyword cluster CSVs into schedulable content calendars in 3 minutes

**SE Ranking skills repo**
- URL: https://github.com/seranking/seo-skills
- Skills: Content briefs, AI search share of voice, keyword clusters, competitor gap analysis

### 18.3 Multi-Agent Collections

**VoltAgent/awesome-claude-code-subagents**
- URL: https://github.com/VoltAgent/awesome-claude-code-subagents
- What: 100+ specialized subagents for all use cases

**wshobson/agents**
- URL: https://github.com/wshobson/agents
- What: Intelligent automation and multi-agent orchestration for Claude Code

### 18.4 General Skill Collections

**hesreallyhim/awesome-claude-code**
- URL: https://github.com/hesreallyhim/awesome-claude-code
- What: Curated list of skills, hooks, slash-commands, agents, plugins (21.6K stars)
- Directory: https://awesomeclaude.ai/awesome-claude-code

**alirezarezvani/claude-skills**
- URL: https://github.com/alirezarezvani/claude-skills
- What: 263+ skills — engineering, marketing, product, compliance

---

## 19. RECOMMENDED MCP CONFIGURATION FOR WORDPRESS PROJECTS

Create `.mcp.json` at your WordPress project root:

```json
{
  "mcpServers": {
    "wordpress": {
      "command": "npx",
      "args": ["-y", "@instawp/mcp-wp"],
      "env": {
        "WP_URL": "https://yoursite.com",
        "WP_USER": "your-wp-username",
        "WP_APP_PASSWORD": "your-app-password"
      }
    },
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "your-key"
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
      "env": {
        "PAGESPEED_API_KEY": "your-key"
      }
    },
    "brave-search": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "your-key"
      }
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
      "env": {
        "STABILITY_API_KEY": "your-key"
      }
    },
    "pdf": {
      "command": "npx",
      "args": ["-y", "markdown2pdf-mcp"]
    }
  }
}
```

**Priority MCP servers to set up first:**
1. WordPress MCP (InstaWP or official WordPress/mcp-adapter)
2. Google Search Console MCP (essential for SEO monitoring)
3. Firecrawl MCP (content research and competitor analysis)
4. Brave/Perplexity Search MCP (deep research)
5. Ahrefs or DataForSEO MCP (keyword data)
6. AdSense MCP (revenue monitoring)
7. Image Generation MCP (featured images)

---

## 20. RECOMMENDED AGENT PIPELINE ARCHITECTURE

### Content Production Pipeline (Multi-Agent)

```
ORCHESTRATOR AGENT
├── Task: "Produce 5 SEO articles on [legal topic]"
│
├── RESEARCHER SUBAGENTS (parallel, Haiku model)
│   ├── Agent R1: Keyword research via Ahrefs/SE Ranking MCP
│   ├── Agent R2: SERP analysis via DataForSEO MCP
│   └── Agent R3: Competitor content audit via Firecrawl
│
├── BRIEF WRITER (Sonnet, sequential)
│   └── Creates content briefs from research outputs
│
├── CONTENT WRITERS (parallel, Sonnet)
│   ├── Agent W1: Article 1-2 (uses briefs + web search)
│   ├── Agent W2: Article 3-4
│   └── Agent W3: Article 5
│
├── SEO OPTIMIZER (Sonnet, sequential)
│   └── Adds schema markup, optimizes headings, meta tags
│
├── IMAGE GENERATOR (Haiku, parallel)
│   └── Creates featured images via Stability AI MCP
│
└── PUBLISHER (Sonnet, sequential)
    └── Uploads to WordPress via WP REST API MCP
```

**CLAUDE.md for this project should define:**
```markdown
# Clear Legal Tips — Content Pipeline

## Site Info
- URL: https://clearlegaltips.com
- WP REST API: https://clearlegaltips.com/wp-json/wp/v2/
- Primary SEO plugin: Yoast SEO

## Content Standards
- Target audience: US general public seeking legal info
- Tone: Clear, professional, not legal advice
- Word count: 1,500-2,500 words per post
- Required schema: Article, FAQPage, BreadcrumbList
- Disclosure: Every affiliate link needs [Affiliate Disclosure] tag

## Affiliate Programs
- Amazon Associates: amzn.to links, max 4 per post
- LegalZoom affiliate: code CLEARTIPS
- Rocket Lawyer: code CLEARLEGAL

## Publishing Workflow
1. Draft → category: "drafts"
2. SEO check → update Yoast fields
3. Add schema markup
4. Schedule → not publish directly
```

### Keyword Research → Content Brief Pipeline

```
/keyword-research "legal document templates"
→ Ahrefs MCP: volume, KD, intent data
→ SE Ranking MCP: ranking opportunities
→ DataForSEO MCP: SERP analysis
→ Output: Prioritized keyword list

/content-brief "how to write an NDA"
→ Firecrawl: scrape top 10 ranking pages
→ Perplexity: research current legal standards
→ Structure: H1, H2s, FAQ questions, internal links
→ Output: Comprehensive brief for writer agent

/seo-write-post brief.md
→ Writer agent: draft from brief
→ SEO optimizer: add schema, optimize meta
→ Image agent: generate featured image
→ Publisher agent: upload to WordPress as draft
```

---

## 21. RECOMMENDED HOOK CONFIGURATION

Save to `.claude/settings.json` in your WordPress project:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "FILE=$(cat | jq -r '.tool_input.file_path // empty'); if [[ \"$FILE\" == *.php ]]; then php -l \"$FILE\" 2>&1 || true; fi",
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
            "command": "powershell -Command \"[System.Windows.Forms.MessageBox]::Show('Claude Code: Input needed', 'Clear Legal Tips Agent')\"",
            "timeout": 5000
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
            "command": "echo \"$(date): Session ended\" >> ~/clear-legal-tips/content-log.txt",
            "async": true
          }
        ]
      }
    ],
    "SubagentStop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "echo \"$(date): Subagent completed: $CLAUDE_SUBAGENT_NAME\" >> ~/clear-legal-tips/agent-log.txt",
            "async": true
          }
        ]
      }
    ]
  }
}
```

---

## 22. SOURCES & LINKS INDEX

### Official Documentation
- Claude Code Docs: https://code.claude.com/docs
- Hooks Guide: https://code.claude.com/docs/en/hooks-guide
- Sub-Agents: https://code.claude.com/docs/en/sub-agents
- Skills: https://code.claude.com/docs/en/skills
- Memory: https://code.claude.com/docs/en/memory
- Agent Teams: https://code.claude.com/docs/en/agent-teams
- Agent View: https://code.claude.com/docs/en/agent-view
- Plugins Reference: https://code.claude.com/docs/en/plugins-reference
- MCP Registry: https://registry.modelcontextprotocol.io/

### WordPress MCP
- WordPress/mcp-adapter: https://github.com/WordPress/mcp-adapter
- InstaWP/mcp-wp: https://github.com/InstaWP/mcp-wp
- WooCommerce MCP: https://developer.woocommerce.com/docs/features/mcp/
- WordPress Developer Blog (MCP Adapter): https://developer.wordpress.org/news/2026/02/from-abilities-to-ai-agents-introducing-the-wordpress-mcp-adapter/
- Royal MCP plugin: https://wordpress.org/plugins/royal-mcp/
- Best WP MCP Servers compared: https://instawp.com/best-wordpress-mcp-servers-compared/

### SEO MCP
- Ahrefs MCP (official): https://ahrefs.com/mcp/
- DataForSEO MCP: https://github.com/Skobyn/dataforseo-mcp-server
- Semrush MCP: https://github.com/mrkooblu/semrush-mcp
- SE Ranking MCP: https://seranking.com/api/integrations/mcp/
- SE Ranking Skills: https://github.com/seranking/seo-skills
- Serpstat MCP: https://github.com/SerpstatGlobal/serpstat-mcp-server-js
- AgriciDaniel/claude-seo: https://github.com/AgriciDaniel/claude-seo
- SEO Machine: https://github.com/TheCraigHewitt/seomachine
- SEO/GEO Skills: https://github.com/aaron-he-zhu/seo-geo-claude-skills

### Google Search Console MCP
- AminForou/mcp-gsc: https://github.com/AminForou/mcp-gsc
- ahonn/mcp-server-gsc: https://github.com/ahonn/mcp-server-gsc
- saurabhsharma2u (GSC+Bing+GA4): https://github.com/saurabhsharma2u/search-console-mcp
- Setup guide: https://suganthan.com/blog/google-search-console-mcp-server/

### Google Analytics MCP
- Official: https://github.com/googleanalytics/google-analytics-mcp
- For Claude Code: https://github.com/mario-hernandez/google-analytics-mcp-claude-code
- Two Octobers guide: https://twooctobers.com/blog/connecting-to-the-google-analytics-mcp-with-claude/

### PageSpeed/Lighthouse MCP
- ruslanlap: https://github.com/ruslanlap/pagespeed-insights-mcp
- npm: https://www.npmjs.com/package/pagespeed-insights-mcp

### Google Ads & AdSense
- Official Google Ads MCP: https://github.com/googleads/google-ads-mcp
- AdSense MCP: https://github.com/AppsYogi-com/adsense-mcp-server
- Multi-platform: https://github.com/markifact/markifact-mcp

### Web Research & Scraping
- Firecrawl MCP: https://github.com/firecrawl/firecrawl-mcp-server
- Firecrawl use cases: https://www.firecrawl.dev/use-cases/ai-mcps
- Perplexity MCP: https://docs.perplexity.ai/docs/getting-started/integrations/mcp-server
- Exa AI MCP: available via claude.ai integration (mcp__claude_ai_Exa__)

### Image Generation MCP
- Stability AI: https://github.com/tadasant/mcp-server-stability-ai
- Midjourney: https://github.com/AceDataCloud/MidjourneyMCP
- Multi-model: https://github.com/shinpr/mcp-image
- SD WebUI local: https://github.com/Ichigo3766/image-gen-mcp

### Social Media MCP
- Ayrshare (75+ tools): https://github.com/vanman2024/ayrshare-mcp
- PostEverywhere: https://github.com/posteverywhere/mcp
- Twitter/X: https://github.com/EnesCinr/twitter-mcp
- Trends: https://github.com/rugvedp/Trends-MCP

### Email & Outreach MCP
- Gmail: https://github.com/GongRzhe/Gmail-MCP-Server
- Multi-provider: https://github.com/marlinjai/email-mcp
- Cold outreach: https://github.com/AmeyMedewar/Cold-Mailer-MCP
- SMTP/IMAP: https://github.com/yunfeizhu/mcp-mail-server

### PDF & Documents
- markdown2pdf: https://github.com/2b3pro/markdown2pdf-mcp
- PDF tools: https://github.com/hanweg/mcp-pdf-tools
- Stirling PDF: https://github.com/gufao/mcp-server-stirling-pdf

### Automation & Integration
- Zapier MCP: https://github.com/zapier/zapier-mcp
- Composio: https://composio.dev/
- GitHub MCP: https://github.com/github/github-mcp-server

### Cloudflare / Hosting
- Cloudflare MCP: https://github.com/cloudflare/mcp-server-cloudflare
- Build remote MCP: https://developers.cloudflare.com/agents/guides/remote-mcp-server/

### Awesome Lists
- awesome-claude-code: https://github.com/hesreallyhim/awesome-claude-code
- awesome-mcp-servers (punkpeye): https://github.com/punkpeye/awesome-mcp-servers
- awesome-mcp-servers (wong2): https://github.com/wong2/awesome-mcp-servers
- TensorBlock collection: https://github.com/TensorBlock/awesome-mcp-servers
- 100+ subagents: https://github.com/VoltAgent/awesome-claude-code-subagents
- Multi-agent orchestration: https://github.com/wshobson/agents

### Community Articles
- Claude Code Advanced Patterns PDF: https://resources.anthropic.com/hubfs/Claude%20Code%20Advanced%20Patterns_%20Subagents,%20MCP,%20and%20Scaling%20to%20Real%20Codebases.pdf
- Agent Teams 2026 Playbook: https://www.developersdigest.tech/blog/claude-code-agent-teams-subagents-2026
- Hooks mastery: https://github.com/disler/claude-code-hooks-mastery
- Inside Claude Code architecture: https://www.penligent.ai/hackinglabs/inside-claude-code-the-architecture-behind-tools-memory-hooks-and-mcp/
- SEO blog automation 2026: https://www.ramlit.com/blog/seo-blog-automation-content-engine-2026
- Automated SEO blog (0→6K impressions): https://github.com/tiagolemos05/claude-mcps-and-prompts

---

*This document was generated via deep research on 2026-05-18. The MCP ecosystem evolves rapidly; verify installation commands against current README files before use.*
