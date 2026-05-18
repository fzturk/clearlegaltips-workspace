---
description: '{DESCRIPTION}: Defines {WHAT_RULES} for {WHICH_DOMAIN} code.'
applyTo: "src/{domain}/**"
---

# {Domain} Instructions

Reference:
- `.agent/SYSTEM_MANIFEST.md` — constitutional source of truth
- `.agent/skills/{relevant_skill}.md` — {description}
- `.agent/rules/{relevant_rule}.md` — {description}

## Scope

{What these instructions cover and why they matter.}

## Core Rule

{THE SINGLE MOST IMPORTANT RULE FOR THIS DOMAIN IN ONE SENTENCE.}

## {Category_1} Policy

{Rules for this category. Be concrete.}

```python
# ❌ Forbidden
{BAD_EXAMPLE}

# ✅ Required
{GOOD_EXAMPLE}
```

## {Category_2} Policy

{Rules}

## Mandatory Checks

Before submitting {domain} code, verify:
- [ ] {check_1}
- [ ] {check_2}

## Forbidden Patterns

| Pattern | Why Forbidden |
|---------|---------------|
| `{pattern_1}` | {reason} |
| `{pattern_2}` | {reason} |

## Implementation Rules

- {implementation_rule_1}
- {implementation_rule_2}
- Public functions require type hints
- Public functions require docstrings
- Use `pathlib.Path`, not string concatenation
- Use structured logging, not `print()`
