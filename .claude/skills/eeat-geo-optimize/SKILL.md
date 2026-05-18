---
name: eeat-geo-optimize
description: Optimizes articles to E-E-A-T and GEO (Generative Engine Optimization) standards. Use for "E-E-A-T check", "AI search optimization", "build trust", "GEO" requests.
allowed-tools: Read WebSearch Bash
effort: high
---

Optimize a ClearLegalTips article for E-E-A-T and GEO.

## Target: $ARGUMENTS
(Post ID, article title, or file path)

---

## E-E-A-T Checklist (Google EEAT Framework)

### Experience
- [ ] Does the author profile mention relevant experience? (bio: "X years in legal field...")
- [ ] Does the article include real usage examples? ("When I reviewed 50 NDA templates...")
- [ ] Is there first-hand observation or case study?
- [ ] Is the date stamp current?

### Expertise
- [ ] Does the author bio match the article's topic?
- [ ] Is legal terminology used correctly?
- [ ] Are sources authoritative? (.gov, .edu, established law firms)
- [ ] Does the content demonstrate depth? (not surface-level, real knowledge)

### Authoritativeness
- [ ] Are the author and site About pages detailed?
- [ ] Is there social proof? (citations, mentions)
- [ ] Is internal linking strong? (hub-spoke structure)
- [ ] Is the editorial process documented?

### Trustworthiness
- [ ] FTC disclosure present in every article? ✓ (clt-disclosure div)
- [ ] Legal disclaimer present in every article? ✓ (clt-disclaimer div)
- [ ] Privacy Policy, Terms, Disclaimer pages exist? ✓
- [ ] SSL active? (verify on live site)
- [ ] Affiliate relationship clearly disclosed?
- [ ] Contact info (Contact page) available? ✓

---

## GEO — Generative Engine Optimization

GEO ensures ChatGPT / Gemini / Perplexity / Bing Copilot cite your content as a source.

### GEO Optimization Techniques

**1. Direct Answer Format**
Provide a clear, concise definition at the start for AI snippets:
```
"An NDA (Non-Disclosure Agreement) is a legally binding contract 
that prevents parties from sharing confidential information. 
In the US, NDAs are enforceable in all 50 states."
```

**2. Question-Answer Structure**
Write each H2 as a question:
- Instead of "What is an NDA?" use "What Is an NDA and When Do You Need One?"
- AI systems more easily quote Q&A format

**3. Numbered/List Format**
AI systems prefer to cite numbered lists:
```
"5 key elements every NDA must include:
1. Definition of confidential information
2. Obligations of receiving party
3. Exclusions from confidentiality
4. Duration of agreement
5. Consequences of breach"
```

**4. Source Citations**
Explicitly reference official sources:
```
"According to the Uniform Trade Secrets Act (UTSA), adopted in 
47 states, trade secrets include..."
```

**5. Freshness Signals**
- Year in title: "NDA Template 2026"
- "Last updated: [date]" tag
- Include recent legal changes

**6. Geographic Signals (State-Specific)**
AI returns regional content for regional queries:
```
"In Texas, NDAs must... In California, NDAs cannot..."
```

---

## Elements to Optimize

### Read the Article and Check:

```powershell
# Fetch article content
$WPCLI = "C:\Users\fatih\AppData\Local\studio_app\bin\studio.bat"
$WP_PATH = "C:\Users\fatih\Studio\clearlegaltips"
& $WPCLI wp post get $ARGUMENTS --fields=post_content --path="$WP_PATH"
```

Identify:
1. Does the opening paragraph give a direct answer?
2. Are H2 headings in question format?
3. Are there numbered lists?
4. Are there official source citations?
5. Is there an author bio section?

---

## Output

```
=== E-E-A-T / GEO OPTIMIZATION REPORT ===
Post: [ID / Title]

E-E-A-T SCORE:
Experience: [✓/✗] [description]
Expertise:  [✓/✗] [description]
Authority:  [✓/✗] [description]
Trust:      [✓/✗] [description]

GEO OPTIMIZATION:
Direct Answer: [✓/✗]
Q&A Format:   [✓/✗]
Number Lists:  [✓/✗]
Citations:     [✓/✗]
Freshness:     [✓/✗]

RECOMMENDED CHANGES:
1. [Change 1]
2. [Change 2]

WP-CLI UPDATE COMMAND:
[command]
```
