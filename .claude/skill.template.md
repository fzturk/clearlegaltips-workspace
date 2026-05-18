---
name: {skill-name}
description: >
  {DESCRIPTION: what this skill enables, when to trigger it, what
  specific tasks it covers. Include multiple trigger phrases. Make
  it specific enough that it won't false-trigger but broad enough
  to cover all legitimate use cases.}
allowed-tools:
  - bash
  - read
  - edit
  - search
---

# {Skill Name} Skill

## Reference

- `.agent/SYSTEM_MANIFEST.md` — constitutional source of truth
- `.agent/skills/{related_skill}.md` — {description}
- `.github/instructions/{domain}.instructions.md` — coding rules

## Purpose

{2-3 sentences: what this skill produces, why it matters,
what breaks if it's not followed correctly.}

## When to Use

Use this skill when:

- {trigger_condition_1}
- {trigger_condition_2}
- {trigger_condition_3}

## Prerequisites

- {prerequisite_1}
- {prerequisite_2}

## Procedure

### Step 1 — {Step Name}

{Detailed description. Be concrete, not vague.}

Rules:
- {specific_rule_1}
- {specific_rule_2}

### Step 2 — {Step Name}

{Description}

```python
# Correct approach
{CODE_EXAMPLE}
```

### Step N — {Final Validation Step}

{How to verify the output is correct}

## Error Handling

| Error | Action |
|-------|--------|
| {error_type_1} | {action_to_take} |
| {error_type_2} | {action_to_take} |

## Output

- {artifact_1}: `{path}`
- {artifact_2}: `{path}`

## Source Code Location

Implementation should live in:
- `src/{domain}/{module}.py`

## Validation Checklist

- [ ] {check_1}
- [ ] {check_2}
- [ ] {check_3}
- [ ] Output artifacts exist at expected paths
- [ ] Manifest constraints are not violated
