---
name: affiliate-research
description: Researches affiliate programs, compares commissions, and drafts application emails. Use for "research affiliate", "find program", "prepare application" requests.
allowed-tools: WebSearch WebFetch Read Write
effort: high
---

Research affiliate programs for ClearLegalTips and prepare applications.

## Target: $ARGUMENTS
(Program name, category, or "all")

---

## ClearLegalTips Priority Program List

| Program | Platform | Estimated Commission | Status |
|---|---|---|---|
| LawDepot | Impact | ~30% recurring | Not applied |
| ZenBusiness | ShareASale / Direct | ~$100-150/sale | Not applied |
| Northwest Registered Agent | ShareASale | ~$100/sale | Not applied |
| Rocket Lawyer | CJ Affiliate | ~$30/sale | Not applied |
| LegalZoom | CJ Affiliate | ~$15-30/sale | Not applied |
| Nolo | Direct | ~10-15% | Not applied |
| Incfile (Bizee) | Direct | ~$75/sale | Not applied |
| Trust & Will | Impact | ~$30-50/sale | Not applied |
| CompleteCasez | Direct | ~$50/sale | Not applied |
| BizFilings | CJ Affiliate | ~$50/sale | Not applied |

---

## Research Steps

### 1. Research Program Details
Find the following for each program:
- Affiliate program URL (usually site.com/affiliates)
- Commission rate and structure (CPS, CPA, recurring?)
- Cookie duration (30 days? 90 days?)
- Minimum payout threshold
- Payment method (PayPal, check, wire)
- Approval process (automatic or manual?)
- Prohibited traffic types (PPC prohibited?)
- Promotional materials (banners, text links)

Search: `"[PROGRAM NAME] affiliate program" commission cookie`

### 2. Commission Comparison Table

```
| Program | Commission | Cookie | Min Payout | Approval | Platform |
|---------|------------|--------|------------|----------|----------|
| LawDepot | % | days | $ | auto/manual | Impact |
...
```

### 3. Draft Application Email

Include the following:

```
Subject: Affiliate Partnership Inquiry — ClearLegalTips.com

Hello [Program Name] Affiliate Team,

My name is [Name], and I run ClearLegalTips.com, a legal education 
website helping US consumers navigate DIY legal processes.

SITE STATS (approximate, growing):
- Niche: Legal document templates, LLC formation, estate planning, 
  divorce guides for US consumers
- Content: 50+ in-depth articles (3,000+ words each)
- Target audience: US adults seeking affordable legal solutions
- Primary traffic: Organic search (Google)

WHY WE'RE A GOOD FIT:
Our content directly addresses the problems your service solves. 
For example, our article on [RELEVANT ARTICLE] naturally leads 
readers to need exactly what [PROGRAM] offers.

I'm interested in joining your affiliate program to recommend 
[PROGRAM] to our readers when it's genuinely the best solution 
for their needs.

Could you share details about your affiliate program, or point 
me to the application page?

Best regards,
[Name]
ClearLegalTips.com
[Email]
```

### 4. Find Program Application Pages

```
Search: "[program name] affiliate program apply"
Check:
- Does it have an Impact.com account?
- Does it have a ShareASale account?
- Does it have a CJ Affiliate account?
- Is it a direct program?
```

---

## Output Format

```
=== AFFILIATE RESEARCH REPORT ===
Date: [date]

PROGRAM: [Program Name]
URL: [affiliate program URL]
Platform: [Impact / ShareASale / CJ / Direct]
Commission: [rate]
Cookie: [days]
Min Payout: [$]
Approval: [Automatic / Manual / 2-5 days]
Application: [URL]
Notes: [Special terms, restrictions]

READY EMAIL:
[email content]

PRIORITY: [High / Medium / Low]
REASON: [Description]
```

---

## Next Step

When application is complete, update `workspace/OPERATIONS_MANUAL.md`:
```
| [Program] | [Platform] | [Date] | Applied | Pending |
```
