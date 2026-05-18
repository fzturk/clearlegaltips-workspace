---
name: pipeline-orchestrator
description: >
  The master pipeline that executes the full plan-to-system documentation
  generation workflow end-to-end. Takes a plan.md as input and produces all
  agents, skills, hooks, instructions, memory files, CI configs, and governance
  documents. Use this skill when a user provides a plan.md and wants the
  complete documentation ecosystem generated automatically.
  This is the primary entry point for the plan-to-system workflow.
allowed-tools:
  - bash
  - read
  - edit
  - search
  - web_search
---

# Pipeline Orchestrator Skill

## Purpose

Execute the complete plan-to-system documentation generation pipeline.
This is the main entry point. It orchestrates all other skills in the
correct order.

## Input

- `plan.md` — The system plan (required)
- `output_dir/` — Target directory (default: `generated-system/`)

## Output

A complete, production-ready documentation ecosystem for any system described in plan.md.

## Execution Order

```
PHASE 0: Research & Analysis
  └─ plan-analyzer skill

PHASE 1: Constitutional Layer
  ├─ manifest-generator skill
  ├─ ARCHITECTURE_DECISIONS.md
  ├─ copilot-instructions.md
  └─ AGENTS.md

PHASE 2: Agent Layer
  └─ agent-factory skill

PHASE 3: Skill Layer
  └─ skill-factory skill

PHASE 4: Enforcement Layer
  └─ hook-factory skill

PHASE 5: Instructions Layer
  └─ instruction-factory skill

PHASE 6: Memory Layer
  └─ memory-initializer skill

PHASE 7: CI/CD Layer
  ├─ ci.yml
  ├─ nightly-governance.yml
  └─ docker-compose.yml (if applicable)

PHASE 8: Validation
  └─ Consistency check across all documents
```

## Procedure

### Step 0 — Setup

```bash
# Create output directory structure
mkdir -p {OUTPUT_DIR}/.github/{instructions,agents,skills,hooks/scripts,workflows}
mkdir -p {OUTPUT_DIR}/.agent/{skills,rules,memory}
mkdir -p {OUTPUT_DIR}/configs
mkdir -p {OUTPUT_DIR}/analysis
```

### Step 1 — Run plan-analyzer

Execute the plan-analyzer skill:
1. Read plan.md completely
2. Research authoritative sources via web search
3. Extract all architectural decisions, constraints, forbidden items
4. Identify agent domains and skill domains
5. Save `analysis/plan_analysis.json`

**Checkpoint:** Verify `plan_analysis.json` is complete before proceeding.

### Step 2 — Generate SYSTEM_MANIFEST.md

Execute the manifest-generator skill using `plan_analysis.json`.

**Checkpoint:** Verify SYSTEM_MANIFEST.md:
- Contains all frozen decisions
- Contains all hard constraints (numbered)
- Contains all out-of-scope items
- Is at least 2000 words

### Step 3 — Generate ARCHITECTURE_DECISIONS.md

Quick reference document summarizing SYSTEM_MANIFEST.md:
- One section per decision category
- Tables for each frozen decision
- Development runtime policy section

### Step 4 — Generate copilot-instructions.md

```markdown
# {SYSTEM_NAME} — Copilot Instructions

## Constitutional Source
If any instruction conflicts with SYSTEM_MANIFEST.md, the manifest wins.

## Repository Scope
{SCOPE FROM PLAN}

## Absolute Prohibitions
{ALL FORBIDDEN ITEMS FROM PLAN}

## Engineering Defaults
{CODING STANDARDS}

## Working Rule
Before editing, read:
1. SYSTEM_MANIFEST.md
2. Relevant skills/*.md
3. Relevant rules/*.md
4. Relevant instructions/*.instructions.md

## Layer Expectations
{PER-DOMAIN EXPECTATIONS}

## Output Quality Rule
Code must be manifest-aligned, causally valid, resource-safe, testable.
```

### Step 5 — Generate AGENTS.md

Repository navigation guide with:
- Constitutional source reference
- Repository scope
- Absolute prohibitions
- Source layout (directory tree)
- Engineering defaults
- Safety expectations

### Step 6 — Run agent-factory

Execute agent-factory skill to generate all `*.agent.md` files.

**Checkpoint:** Verify:
- All agent domains covered
- architecture-governor present
- code-reviewer present
- Scopes are non-overlapping

### Step 7 — Run skill-factory

Execute skill-factory skill to generate all `SKILL.md` files.

**Checkpoint:** Verify:
- All skill domains covered
- Each skill has procedures
- Each skill has validation checklists

### Step 8 — Run hook-factory

Execute hook-factory skill to generate hooks and scripts.

**Checkpoint:** Verify:
- All forbidden patterns have hook rules
- Smoke test script is generated

### Step 9 — Run instruction-factory

Execute instruction-factory skill for all source directories.

**Checkpoint:** Verify:
- Every major source path has instructions
- applyTo globs are correct

### Step 10 — Run memory-initializer

Execute memory-initializer skill for all memory files.

**Checkpoint:** Verify:
- All failure mode files generated
- PROMOTION_HISTORY.json is valid JSON

### Step 11 — Generate CI/CD Configs

Generate GitHub Actions workflows:

```yaml
# ci.yml template
name: ci
on:
  push:
    branches: [main, master, develop, "feature/**", "fix/**"]
  pull_request:
  workflow_dispatch:

jobs:
  governance-check:
    name: Governance / repo structure check
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: {python-version: "3.11"}
      - name: Validate required governance files
        run: python scripts/validate_governance.py

  quality:
    name: Lint / type / tests
    runs-on: ubuntu-latest
    needs: governance-check
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: {python-version: "3.11", cache: "pip"}
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Ruff
        run: ruff check src tests
      - name: Mypy
        run: mypy src
      - name: Pytest
        run: pytest tests -v -m "not slow and not gpu"

  tooling-smoke:
    name: Hook smoke tests
    runs-on: ubuntu-latest
    needs: governance-check
    steps:
      - uses: actions/checkout@v4
      - name: Run hook smoke tests
        run: bash .github/hooks/scripts/smoke-test-hooks.sh
```

### Step 12 — Cross-Document Consistency Validation

Run consistency checks:

```python
def validate_consistency(output_dir):
    manifest = read(f"{output_dir}/SYSTEM_MANIFEST.md")
    analysis = read_json(f"{output_dir}/analysis/plan_analysis.json")

    # All frozen decisions in SYSTEM_MANIFEST appear in ARCHITECTURE_DECISIONS
    # All forbidden patterns in manifest appear in hooks
    # All agent domains in analysis have agent files
    # All skill domains in analysis have skill files
    # All forbidden patterns in hooks have smoke tests
    # AGENTS.md references all generated agents
    # copilot-instructions lists all absolute prohibitions

    return validation_report
```

### Step 13 — Generate Final Summary

Produce `GENERATION_SUMMARY.md`:

```markdown
# System Documentation Generated

## Generation Date: {DATE}
## Source: plan.md
## Output: {OUTPUT_DIR}

## Generated Files ({COUNT})

### Constitutional Layer
- SYSTEM_MANIFEST.md ✅
- ARCHITECTURE_DECISIONS.md ✅
- AGENTS.md ✅
- copilot-instructions.md ✅

### Agent Layer ({N} agents)
{LIST}

### Skill Layer ({N} skills)
{LIST}

### Enforcement Layer
{LIST}

### Instruction Layer ({N} files)
{LIST}

### Memory Layer ({N} files)
{LIST}

### CI/CD Layer
{LIST}

## Validation Results
{CONSISTENCY_CHECK_RESULTS}

## Next Steps
1. Review SYSTEM_MANIFEST.md for accuracy
2. Run: bash .github/hooks/scripts/smoke-test-hooks.sh
3. Start implementation following the build order in SYSTEM_MANIFEST.md
```

## Error Handling

| Phase | Error | Action |
|-------|-------|--------|
| Phase 0 | plan.md not found | Abort with clear message |
| Phase 0 | Web search fails | Continue with plan.md analysis only |
| Phase 1 | SYSTEM_MANIFEST too short | Flag and expand |
| Phase 6 | Hook smoke tests fail | Report and continue |
| Phase 12 | Consistency violations | List violations in summary |

## Validation Checklist

- [ ] plan.md was read and analyzed
- [ ] Web research was performed
- [ ] SYSTEM_MANIFEST.md is complete (2000+ words)
- [ ] All agents are generated
- [ ] All skills are generated
- [ ] All hooks are generated
- [ ] All instructions are generated
- [ ] All memory files are generated
- [ ] CI/CD configs are generated
- [ ] Consistency check passed
- [ ] Generation summary is produced
- [ ] Output directory has correct structure
