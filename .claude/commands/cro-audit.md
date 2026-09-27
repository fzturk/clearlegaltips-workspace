---
description: Full CRO audit of all 50 ClearLegalTips articles. Scores affiliate CTA effectiveness, identifies conversion leaks, and produces a ranked fix list. Run quarterly.
---

# CRO Audit — All 50 Articles

Run a full conversion rate optimization audit across all ClearLegalTips articles.

## Audit Workflow

### Phase 1 — Data Collection

Read all 50 posts (IDs 131–180) and extract:

```php
$posts = get_posts(['post_type' => 'post', 'numberposts' => -1, 'post_status' => 'publish', 'orderby' => 'ID', 'order' => 'ASC']);
foreach ($posts as $post) {
  $content = $post->post_content;
  $cta_count = substr_count($content, 'clt-affiliate-btn');
  $has_disclosure = (strpos($content, 'clt-disclosure') !== false) ? 'YES' : 'NO';
  $has_disclaimer = (strpos($content, 'clt-disclaimer') !== false) ? 'YES' : 'NO';
  $has_related = (strpos($content, 'clt-related-articles') !== false) ? 'YES' : 'NO';
  $above_fold_cta = /* check if CTA appears within first 600 words */;
  echo "{$post->ID}|{$post->post_title}|{$cta_count}|{$has_disclosure}|{$has_disclaimer}|{$has_related}\n";
}
```

### Phase 2 — CRO Scoring

Use `affiliate-cta-optimizer` to score each article on 7 dimensions (0–3 points each = 21 max):

| Dimension | Points | Criteria |
|---|---|---|
| Value proposition | 0–3 | Clear benefit in first 2 seconds? |
| Headline match | 0–3 | H1 matches search intent exactly? |
| CTA count/placement | 0–3 | 3 CTAs at right positions? |
| CTA copy quality | 0–3 | [Action] + [Outcome] + [Price anchor]? |
| Trust signals | 0–3 | Author, date, disclaimer all visible? |
| Objection handling | 0–3 | "Free?", "Legal advice?" addressed? |
| Friction audit | 0–3 | No direct URLs, fast load, mobile-friendly? |

**Score interpretation:**
- 18–21: Excellent — monitor only
- 12–17: Good — minor fixes
- 6–11: Needs work — prioritize in next sprint
- 0–5: Critical — fix immediately

### Phase 3 — Quick Win Identification

Flag articles where a single change would make the biggest impact:

**Type A — Missing above-fold CTA** (highest priority):
No affiliate link in first 600 words = losing readers who don't scroll.
Fix: insert a `clt-cta-box` block after the intro paragraph.

**Type B — Weak CTA copy:**
Button text is "Click here" or "Learn more" = no conversion context.
Fix: use `legal-copywriter` skill to generate 3 variants, pick best.

**Type C — Zero trust signals:**
No author bio reference, no publish date visible, disclosure buried.
Fix: verify `clt-disclosure` is at top, add author byline to Rank Math.

**Type D — Missing FAQ / schema:**
No FAQ section = missing featured snippet opportunity + lower E-E-A-T.
Fix: use `schema-markup-legal` to generate FAQ block + JSON-LD.

### Phase 4 — Lead Magnet Audit

Review the quiz/lead capture setup:
- Is the "Which LLC Service Is Right For You?" quiz live?
- Is there an exit-intent popup configured?
- Is there a scroll-triggered CTA for email capture?

Use `form-cro` skill to evaluate any quiz form.
Use `popup-cro` skill to design/evaluate exit-intent popup.

### Phase 5 — A/B Test Recommendations

Use `ab-test-setup` skill to identify the single highest-priority A/B test to run next, based on the audit findings.

Criteria for selecting the test:
- Affects the highest-traffic article
- Tests a CTA element (copy, color, placement)
- Measurable within 4 weeks of normal traffic

## Output Format

```
CRO AUDIT REPORT
Date: [date]
Articles audited: 50

SCORE DISTRIBUTION:
Excellent (18–21): [X] articles
Good (12–17):      [X] articles
Needs work (6–11): [X] articles
Critical (0–5):    [X] articles

RANKED FIX LIST (by impact):
Rank 1: Post [ID] "[title]" — Score: [X/21] — Main issue: [one line fix]
Rank 2: ...
...
[top 10 only]

QUICK WIN PHP SNIPPETS:
[PHP to inject above-fold CTAs for critical posts]

LEAD MAGNET STATUS:
Quiz: [live/not live]
Exit popup: [configured/not configured]
Email capture rate: [X%] (if trackable)

RECOMMENDED A/B TEST:
Post: [ID] "[title]"
Hypothesis: [formula: "If we change X, Y will increase by Z because..."]
Variant A: [control]
Variant B: [test]
Success metric: [affiliate link clicks]
Duration: [X days]

NEXT CRO AUDIT: [3 months from today]
```
