---
name: instruction-factory
description: >
  Generates all *.instructions.md files for a system — path-specific always-on
  coding rules for each major source directory. Instructions define implementation
  patterns, forbidden practices, and references for each domain. Use after
  SYSTEM_MANIFEST.md and agents are complete.
allowed-tools:
  - read
  - edit
  - bash
---

# Instruction Factory Skill

## Reference

- Input: `analysis/plan_analysis.json`, `SYSTEM_MANIFEST.md`
- Output: `.github/instructions/*.instructions.md`
- Template: `templates/instruction.template.md`

## Purpose

Generate always-on instruction files that apply automatically whenever Claude
edits files in specific directories. Instructions encode domain-specific rules
into the development environment itself.

## Instruction File Anatomy

```markdown
---
description: '{DESCRIPTION}: what rules these instructions define and for which domain'
applyTo: "src/{domain}/**"
---

# {Domain} Instructions

Reference:
- `.agent/SYSTEM_MANIFEST.md` — constitutional source of truth
- `.agent/skills/{relevant_skill}.md` — {description}
- `.agent/rules/{relevant_rule}.md` — {description}

## Scope
{What these instructions cover}

## Core Rule
{THE MOST IMPORTANT RULE IN ONE SENTENCE}

## {Category 1} Policy
{Rules for this category}

## {Category 2} Policy
{Rules for this category}

## Mandatory Checks
{Before, during, or after operations}

## Forbidden Patterns
{Explicitly forbidden with reasons}

## Implementation Rules
{Concrete coding standards}
```

## Procedure

### Step 1 — Identify Instruction Domains

From `plan_analysis.json`, map source directories to instruction files:

```
src/data/           → data-layer.instructions.md
src/features/       → feature-engineering.instructions.md
src/labeling/       → labeling.instructions.md (ML systems)
src/environment/    → environment.instructions.md (RL systems)
src/reward/         → reward-design.instructions.md (RL systems)
src/agent/          → model-training.instructions.md
src/backtest/       → backtest-validation.instructions.md
src/live/           → live-execution.instructions.md
src/common/         → common-utilities.instructions.md
configs/            → configuration.instructions.md
tests/              → testing-standards.instructions.md
**/*.py             → no-leakage.instructions.md (global, ML systems)
```

### Step 2 — Generate Data Layer Instructions

```markdown
---
description: 'Defines canonical data handling, schema rules, integrity checks,
  gap policy, and memory-safe processing for src/data code.'
applyTo: "src/data/**"
---

# Data Layer Instructions

Reference:
- `.agent/SYSTEM_MANIFEST.md`
- `.agent/skills/{data-skill}.md`

## Canonical Root
{CANONICAL_DATA_ROOT from plan}

## Required Canonical Schema
{SCHEMA from plan}

## Time Standard
{TIME_STANDARD from plan (e.g., UTC only)}

## Mandatory Integrity Checks
{LIST ALL INTEGRITY CHECKS from plan}

## Gap Policy
{GAP_POLICY from plan}

## Memory and Throughput Rules
{HARDWARE_LIMITS from plan}

## Implementation Rules
- {rule_1}
- {rule_2}
```

### Step 3 — Generate Domain-Specific Instructions

For each source domain, generate an instructions file that includes:

1. **Scope section** — what this domain is responsible for
2. **Core rule** — the single most important invariant
3. **Policy sections** — one per major concern (data, time, security, etc.)
4. **Mandatory checks** — explicit pre/post operation checks
5. **Forbidden patterns** — explicitly named anti-patterns with reasons
6. **Implementation rules** — concrete standards (e.g., "use pathlib.Path")

### Step 4 — Generate Global Instructions

Always generate these regardless of system type:

#### no-leakage.instructions.md (for data/ML systems)
```markdown
---
description: 'Enforces no-lookahead rules across ALL Python code. MTF alignment,
  scaler fitting, label usage, fill realism, and causal reward behavior.'
applyTo: "**/*.py"
---
```

#### testing-standards.instructions.md
```markdown
---
description: 'Defines deterministic pytest standards, fixture conventions,
  safety-focused assertions for all test code.'
applyTo: "tests/**"
---
```

### Step 5 — Extract Rules from Plan Analysis

For each instructions file, pull the relevant rules from `plan_analysis.json`:

```python
def extract_rules_for_domain(domain, analysis):
    rules = []
    # Get forbidden patterns for this domain
    for pattern in analysis["forbidden_patterns"].get(domain, []):
        rules.append(f"Forbidden: {pattern}")
    # Get constraints that apply to this domain
    for constraint in analysis["hard_constraints"]:
        if constraint["category"] == domain:
            rules.append(constraint["rule"])
    return rules
```

### Step 6 — Generate applyTo Paths

Map each instruction to correct `applyTo` glob:

| Instruction File | applyTo |
|-----------------|---------|
| no-leakage | `**/*.py` |
| data-layer | `src/data/**` |
| feature-engineering | `src/features/**` |
| testing-standards | `tests/**` |
| live-execution | `src/live/**` |
| configuration | `configs/**,experiments/**,src/common/**` |

## Special Pattern: Forbidden Pattern Tables

Every instructions file should have a "Forbidden Patterns" section:

```markdown
## Forbidden Patterns

Never use the following in this domain:

| Pattern | Why Forbidden |
|---------|---------------|
| `{pattern_1}` | {reason} |
| `{pattern_2}` | {reason} |
```

## Special Pattern: Code Examples

For critical rules, include correct and incorrect examples:

```markdown
## {Rule Name}

❌ Forbidden:
\`\`\`python
# This is wrong because {reason}
df["x"] = df["close"].shift(-1)
\`\`\`

✅ Required:
\`\`\`python
# This is correct
df["x"] = df["close"].shift(1)
\`\`\`
```

## Output

Files: `.github/instructions/{name}.instructions.md` (one per domain)

## Validation Checklist

- [ ] Every major source directory has a corresponding instructions file
- [ ] Every instructions file has correct `applyTo` glob
- [ ] Every instructions file has `description` in frontmatter
- [ ] All forbidden patterns from analysis appear in instructions
- [ ] Global instructions (no-leakage, testing) are always present
- [ ] Code examples illustrate critical forbidden patterns
- [ ] Implementation rules are concrete (not vague)
