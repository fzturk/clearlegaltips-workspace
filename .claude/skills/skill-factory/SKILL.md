---
name: skill-factory
description: >
  Generates all workflow skill files (SKILL.md) for a system based on the
  plan analysis. Each skill documents a concrete, repeatable procedure with
  prerequisites, steps, outputs, and validation checklists. Use after
  SYSTEM_MANIFEST.md and agents are generated.
allowed-tools:
  - read
  - edit
  - bash
---

# Skill Factory Skill

## Reference

- Input: `analysis/plan_analysis.json`, `SYSTEM_MANIFEST.md`
- Output: `.github/skills/{name}/SKILL.md`
- Template: `templates/skill.template.md`

## Purpose

Generate workflow skill files for each repeatable procedure in the system.
Skills provide detailed step-by-step guides for complex multi-phase operations.

## Procedure

### Step 1 — Enumerate Skill Domains

From `analysis/plan_analysis.json`, extract `skill_domains`.

For each domain, identify:
- The concrete procedure it documents
- Prerequisites (what must exist before)
- Major steps (5-15 steps)
- Output artifacts
- Validation criteria
- Error handling scenarios

### Step 2 — Generate Each SKILL.md

For each skill domain, generate `{skill-name}/SKILL.md`:

```markdown
---
name: {skill-name}
description: >
  {DESCRIPTION: what this skill enables, when to use it,
   what specific tasks trigger it. Make it "pushy" — include
   multiple trigger phrases to improve triggering accuracy.}
allowed-tools:
  - {tool_1}
  - {tool_2}
---

# {Skill Name} Skill

## Reference

- `.agent/SYSTEM_MANIFEST.md` — constitutional source of truth
- `.agent/skills/{related_skill}.md` — {description}
- `.github/instructions/{domain}.instructions.md` — coding rules
- {external_doc_url} — {description}

## Purpose

{2-3 sentences: what this skill produces, why it matters,
what breaks if it's not followed correctly}

## When to Use

Use this skill when:

- {trigger_condition_1}
- {trigger_condition_2}
- {trigger_condition_3}

## Prerequisites

- {prerequisite_1}
- {prerequisite_2}
- {prerequisite_3}

## Procedure

### Step 1 — {Step Name}

{Detailed description of what to do in this step}

Rules:
- {specific_rule_1}
- {specific_rule_2}

### Step 2 — {Step Name}

{Detailed description}

{Include code snippets where the procedure is deterministic:}

\`\`\`python
# Example of the correct approach
def example():
    pass
\`\`\`

### Step N — {Final Step}

{Description of final validation and output}

## Error Handling

| Error | Action |
|-------|--------|
| {error_type_1} | {action} |
| {error_type_2} | {action} |

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
```

### Step 3 — Generate Standard Cross-Cutting Skills

Always generate these skills:

#### 1. {system}-integrity-check
```
Purpose: Validate primary data/artifact format for schema, consistency, anomalies
Trigger: When new data/artifacts are created or modified
```

#### 2. {system}-leakage-detector (for data/ML systems)
```
Purpose: Detect future-data leakage in features, labels, normalization
Trigger: After any feature/label computation change
```

#### 3. promotion-gate-checker
```
Purpose: Verify promotion criteria before stage progression
Trigger: Before any promotion decision
```

#### 4. {domain}-pipeline (main workflow)
```
Purpose: End-to-end workflow for the system's primary operation
Trigger: When user wants to run the full pipeline
```

### Step 4 — Enrich with Research Findings

For each skill, incorporate authoritative best practices:
- Include known anti-patterns in error handling
- Reference official documentation where applicable
- Include concrete code examples where the procedure is deterministic
- Add performance/efficiency notes from research

### Step 5 — Generate skills/README.md

```markdown
# Skills Map

## Public Workflow Skills
(suitable for direct task-oriented usage)
- `{skill-1}` — {description}
- `{skill-2}` — {description}

## Internal / Audit Skills
(focused support and audit workflows)
- `{skill-3}` — {description}

## Usage Principle
Use instructions for always-on repository rules.
Use skills for repeatable workflows, audits, and report generation.

## Governance Rule
All skills are subordinate to `.agent/SYSTEM_MANIFEST.md`.
```

## Skill Quality Rules

Every SKILL.md must:
- Have a "pushy" description with multiple trigger phrases
- List ALL prerequisites clearly
- Have numbered, concrete steps (not vague)
- Include code snippets for deterministic operations
- Have an error handling table
- List ALL output artifacts with paths
- Have a complete validation checklist
- Stay under 500 lines (use reference files for overflow)

## Skill Count Guidelines

| System Complexity | Expected Skill Count |
|-------------------|---------------------|
| Simple | 4-6 skills |
| Medium | 7-12 skills |
| Complex | 12-20 skills |
| Always include | integrity-check, pipeline, promotion-gate-checker |

## Special Handling

### For ML/Data Systems
Generate:
- `data-download` — fetch, validate, cache
- `feature-engineering` — compute, normalize, validate features
- `label-pipeline` — generate labels
- `training-pipeline` — train, checkpoint, evaluate
- `walk-forward-backtest` — evaluation protocol
- `promotion-gate-checker` — gate verification

### For API/Web Systems
Generate:
- `api-integration-test` — validate API connectivity
- `schema-validation` — validate request/response schemas
- `load-test` — performance validation

### For Autonomous Agent Systems
Generate:
- `agent-orchestration` — coordinate multi-agent workflows
- `tool-validation` — validate tool integrations
- `output-quality-check` — evaluate agent outputs

## Output

Files: `.github/skills/{name}/SKILL.md` (one per skill)
File: `.github/skills/README.md`

## Validation Checklist

- [ ] All skill domains from analysis are covered
- [ ] Each skill has a clear trigger condition
- [ ] Each skill has concrete steps (not vague)
- [ ] Each skill has error handling
- [ ] Each skill has output artifacts
- [ ] Each skill has validation checklist
- [ ] Skills reference correct source code paths
- [ ] README.md is generated
