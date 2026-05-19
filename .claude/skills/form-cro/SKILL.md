---
name: form-cro
description: Optimizes lead capture forms on ClearLegalTips for maximum email signup conversion. Use when asked to "optimize the form", "improve signups", "lead form CRO", "why aren't people signing up", or when building the lead magnet quiz form.
allowed-tools: Read Write
effort: medium
---

# Form CRO — Lead Capture Optimization

## Context

ClearLegalTips captures emails via:
1. Lead magnet quiz ("Which LLC Service Is Right For You?") — built in Tally
2. Newsletter signup form — embedded in articles or sidebar
3. PDF download gates — "Get the free [document] checklist"

Form conversion benchmark: 2–5% of visitors who see the form complete it. Below 2% = optimization needed.

## The 5 Form Friction Points

### 1. Field Count
- Every additional field reduces completion by ~10%
- Minimum viable: **email only** for newsletter
- Maximum for quiz: **5 questions** before email ask
- Never ask for phone number (kills legal audience trust)

### 2. Value-Ask Balance
The form must answer: "What do I get for giving my email?"
- Weak: "Subscribe to our newsletter"
- Strong: "Get your personalized LLC service recommendation + free checklist"
- The value must be specific, immediate, and relevant to what the reader just read

### 3. Trust Signals Near the Form
Required elements near every form:
- [ ] "No spam. Unsubscribe anytime." (below submit button)
- [ ] Privacy policy link
- [ ] Sample of what they'll receive ("You'll get: [specific thing]")
- [ ] For quiz: progress indicator ("Question 2 of 4")

### 4. Submit Button Copy
| ❌ Weak | ✅ Strong |
|---|---|
| Submit | Get My Recommendation |
| Sign Up | Send Me the Free Checklist |
| Subscribe | Yes, I Want Legal Tips |
| Go | Show My LLC Options |

Rule: Button text = what happens when they click, in first person.

### 5. Form Placement
- **Best:** Inline within article content, after a value-building section
- **Good:** Bottom of article, above related links
- **Avoid:** Sidebar (low visibility on mobile)
- **Never:** Immediate popup on page load (violates reader trust on legal content)
- **Acceptable:** Exit-intent popup (use popup-cro skill for this)

## Lead Magnet Quiz — Tally Form Optimization

The "Which LLC Service Is Right For You?" quiz should:

```
Question 1: "What state are you forming your LLC in?"
  (dropdown — 50 states)

Question 2: "What's your primary goal?"
  ○ Save money (cheapest option)
  ○ Get it done fast
  ○ Maximum privacy
  ○ Best ongoing support

Question 3: "How many members will your LLC have?"
  ○ Just me (single-member)
  ○ 2-4 members
  ○ 5+ members

Question 4: "Do you need a registered agent service?"
  ○ Yes, included please
  ○ I'll handle it myself
  ○ Not sure

[Email capture screen]
Headline: "Your personalized LLC recommendation is ready"
Subheadline: "Enter your email to see which service fits your answers"
Field: Email address
Button: "Show My Recommendation →"
Trust line: "No spam. Unsubscribe anytime. Takes 10 seconds."
```

## Instructions

1. **Identify the form being optimized** (newsletter / quiz / PDF gate)
2. **Audit against 5 friction points** above
3. **Rewrite button copy, headline, and trust signals**
4. **Recommend field changes** (remove or reorder)
5. **Output Tally-compatible form structure** if building new

## Output Format

```
FORM CRO AUDIT: [form name/location]

CURRENT CONVERSION ISSUES:
- [issue 1] → [fix]
- [issue 2] → [fix]

OPTIMIZED FORM:
Headline: [new headline]
Subheadline: [new subheadline]
Fields: [list — minimum viable]
Button: [new button text]
Trust line: [new trust copy]

TALLY FORM STRUCTURE (if new build):
[question sequence with options]
```
