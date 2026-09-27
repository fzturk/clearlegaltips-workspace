---
name: popup-cro
description: Designs exit-intent and scroll-triggered popups for ClearLegalTips email capture and affiliate promotion. Use when asked to "create a popup", "exit popup", "scroll popup", "email capture popup", or "reduce exit rate with a popup".
allowed-tools: Read Write
effort: low
---

# Popup CRO — Exit-Intent & Scroll Triggers

## Context

ClearLegalTips legal content readers are skeptical of aggressive popups. The wrong popup destroys trust immediately. The right popup — timed correctly with relevant copy — converts 1–4% of exits into email subscribers or direct affiliate clicks.

**Popup philosophy for legal content:** Never interrupt the read. Catch only the exit or the deeply engaged.

## Popup Types for ClearLegalTips

### 1. Exit-Intent Popup (recommended first popup to implement)
**Trigger:** Cursor moves toward browser close/back button  
**Goal:** Email capture — lead magnet offer  
**Tone:** Helpful, not desperate

```
[Popup design]
Headline: "Before you go — get your free [relevant resource]"
Subheadline: "[Specific benefit tied to the article they just read]"
CTA: "Send Me the Free [Resource] →"
Dismiss: "No thanks, I'll figure it out myself"
```

**Legal-specific examples:**
- On LLC articles: "Before you go — get our free LLC formation checklist (7 steps, no email required for most states)"
- On NDA articles: "Get a free NDA template + 5-minute guide to filling it out correctly"
- On cost articles: "See the cheapest way to form an LLC in [their state] — free comparison chart"

### 2. Scroll-Triggered Popup (50–70% scroll depth)
**Trigger:** Reader has scrolled 50–70% through the article (engaged reader)  
**Goal:** Affiliate click or email capture  
**Tone:** Timely, contextual

```
[Slide-in from bottom right, not full-screen]
Headline: "Ready to [action]?"
Body: "[1 sentence connecting to what they just read]"
CTA: "[Strong affiliate CTA]"
Dismiss: "×" (small)
```

**Example on LLC formation how-to:**
"Ready to form your LLC? ZenBusiness gets it done for $49 — includes registered agent."
[Button: "Start with ZenBusiness →"]

### 3. Time-Delayed Popup (60 seconds — last resort)
Only use if no exit-intent or scroll option is available.  
**Trigger:** 60 seconds on page  
**Goal:** Email capture only (no hard affiliate push)

## Popup Rules for Legal Content

| ✅ DO | ❌ DON'T |
|---|---|
| Exit-intent only on first visit | Immediate popup on page load |
| Slide-in for scroll popups (non-blocking) | Full-screen overlay on mobile |
| Dismiss button clearly visible | Auto-close countdown timers |
| Copy relevant to the article topic | Generic "subscribe to our newsletter" |
| Show once per session | Show again on same visit after dismiss |
| Mobile: small slide-in at bottom | Mobile: full-screen popup |

## Copy Templates

**Exit-intent — Lead magnet:**
```
Headline: "Free [Topic] Checklist — Takes 30 Seconds to Download"
Body: "Everything you need to [achieve outcome] without a lawyer."
CTA: "Get the Free Checklist"
Dismiss: "No thanks"
```

**Scroll-triggered — Affiliate:**
```
Headline: "The easiest way to [achieve what this article teaches]"
Body: "[Service] does it for $[X]. Takes [time]."
CTA: "Start with [Service] →"
Dismiss: "×"
```

## WordPress Implementation Note

ClearLegalTips uses Kadence Blocks. Popup functionality requires either:
- Kadence Popup Builder (if available in theme)
- OptinMonster / ConvertBox plugin
- Custom CSS + JavaScript solution

Output popup copy + trigger settings, not WordPress-specific code (implementation depends on chosen tool).

## Output Format

```
POPUP DESIGN: [type — exit-intent | scroll | time-delayed]
Page/Article: [where it runs]
Trigger: [exact trigger condition]

COPY:
Headline: [text]
Body: [1-2 sentences]
CTA Button: [text]
Dismiss Link: [text]

TARGETING RULES:
- Show on: [article types or post IDs]
- Show once per: [session/day/week]
- Don't show on: [specific pages, e.g., homepage]
- Mobile: [show/hide/modified version]

AFFILIATE TRACKING:
CTA link: /recommend/[slug] — rel="nofollow sponsored"
```
