---
name: plan-to-system
description: >
  Automatically generates the complete documentation ecosystem (SYSTEM_MANIFEST,
  agents, skills, hooks, instructions, memory files, CI configs) for any system
  described in a plan.md file. Eliminates weeks of manual documentation work.
  Use this skill whenever a user provides a plan.md or describes a system they
  want to build and needs governance documentation, agent files, skill files,
  safety hooks, and CI/CD configs generated automatically. This skill replaces
  1 month of manual documentation work with a fully automated pipeline.
  Trigger phrases: "generate from plan", "create system docs", "automate
  documentation", "build agents from plan", "I have a plan.md".
allowed-tools:
  - bash
  - read
  - edit
  - search
  - web_search
---

# Plan-to-System Skill

## What This Skill Does

Takes a `plan.md` file → produces a **complete governance and documentation
ecosystem** ready to use in Claude Code or GitHub Copilot.

**Before (manual):** ~1 month of documentation work  
**After (this skill):** Minutes

## Output Structure

```
generated-system/
├── SYSTEM_MANIFEST.md          ← Constitutional source of truth
├── ARCHITECTURE_DECISIONS.md   ← Frozen decisions quick reference  
├── AGENTS.md                   ← Repository navigation guide
├── .github/
│   ├── copilot-instructions.md ← Copilot configuration
│   ├── agents/                 ← Specialized agent files
│   │   ├── {domain}-engineer.agent.md
│   │   ├── architecture-governor.agent.md
│   │   └── code-reviewer.agent.md
│   ├── skills/                 ← Workflow skill files
│   │   └── {skill}/SKILL.md
│   ├── hooks/                  ← Safety enforcement
│   │   ├── {system}-safety.json
│   │   └── scripts/
│   │       ├── safety-check.sh
│   │       ├── audit-log.sh
│   │       ├── forbidden-pattern.sh
│   │       └── smoke-test-hooks.sh
│   ├── instructions/           ← Always-on coding rules
│   │   └── {domain}.instructions.md
│   └── workflows/              ← CI/CD configs
│       ├── ci.yml
│       └── nightly-governance.yml
├── .agent/
│   ├── SYSTEM_MANIFEST.md      ← Constitutional source (copy)
│   ├── skills/                 ← Rule-level skill specs
│   ├── rules/                  ← Hard rule specs
│   └── memory/                 ← Persistent knowledge
│       ├── ARCHITECTURE_DECISIONS.md
│       ├── KNOWN_FAILURE_MODES.md
│       ├── VALIDATION_IMMUTABLES.md
│       ├── KNOWN_FALSE_POSITIVES.md
│       └── PROMOTION_HISTORY.json
└── configs/
    └── experiment_v1.yaml
```

## When to Use

Use this skill when:
- User provides a `plan.md` describing a system to build
- User says "generate documentation from my plan"
- User wants to automate the agent/skill creation process
- User has a technical specification and needs governance docs
- User spent weeks writing docs manually and wants automation

## Prerequisites

- `plan.md` exists and describes the system
- Web search available (for research phase)
- Write access to output directory

## Execution Pipeline

### Step 1 — Read plan.md

```bash
# Read the plan
cat plan.md
```

Read the ENTIRE plan.md file before doing anything else.

### Step 2 — Research Phase

Search for authoritative resources related to the system:

```
web_search("{system_name} best practices architecture")
web_search("{primary_technology} official documentation")
web_search("{algorithm/approach} failure modes pitfalls")
web_search("claude agent skill best practices")
```

Collect findings to enrich the generated documentation.

### Step 3 — Initialize Structure

```bash
python scripts/generate_system.py --plan plan.md --output generated-system/
```

This creates the directory structure, analysis report, CI/CD configs, and memory placeholders.

### Step 4 — Generate SYSTEM_MANIFEST.md

Follow the `manifest-generator` skill.

Key sections to generate:
1. Document Status
2. System Identity
3. Primary Optimization Target
4. Architecture (text diagram)
5. Frozen Core Design Decisions
6. Global Hard Constraints (numbered)
7. Out of Scope
8. Domain Contracts (one per major domain)
9. Promotion Gates
10. Hardware Resource Contract
11. Security Contract
12. Reproducibility Contract
13. Critical Warnings
14. Document Hierarchy
15. Definition of Ready / Done

### Step 5 — Generate Agents

Follow the `agent-factory` skill.

Always generate:
- `architecture-governor.agent.md`
- `code-reviewer.agent.md`

Generate domain-specific agents based on plan analysis.

### Step 6 — Generate Skills

Follow the `skill-factory` skill.

Generate one `SKILL.md` per major workflow:
- Data pipeline skills
- Training/evaluation skills
- Deployment/operational skills
- Governance/audit skills

### Step 7 — Generate Hooks

Follow the `hook-factory` skill.

Generate:
- `{system}-safety.json` (hook config)
- `safety-check.sh` (pre-tool-use gate)
- `audit-log.sh` (post-tool-use logger)
- `forbidden-pattern.sh` (prompt guard)
- Domain-specific Python scanners
- `smoke-test-hooks.sh` (test suite)

### Step 8 — Generate Instructions

Follow the `instruction-factory` skill.

One `*.instructions.md` per major source directory.

### Step 9 — Generate Memory Files

Follow the `memory-initializer` skill.

Generate:
- `ARCHITECTURE_DECISIONS.md`
- `KNOWN_FAILURE_MODES.md`
- `VALIDATION_IMMUTABLES.md`
- `KNOWN_FALSE_POSITIVES.md`
- System-specific failure mode files

### Step 10 — Cross-Validate

Check consistency:
- All frozen decisions in SYSTEM_MANIFEST appear in ARCHITECTURE_DECISIONS
- All forbidden patterns in SYSTEM_MANIFEST appear in hooks
- All agent domains have agent files
- All major workflows have skill files
- All major source paths have instruction files

## Sub-Skills

This skill orchestrates these sub-skills:
- `plan-analyzer` — deep plan analysis and research
- `manifest-generator` — SYSTEM_MANIFEST.md generation
- `agent-factory` — agent file generation
- `skill-factory` — skill file generation
- `hook-factory` — hook and script generation
- `instruction-factory` — instruction file generation
- `memory-initializer` — memory file generation
- `pipeline-orchestrator` — full end-to-end execution

## Quality Rules

Every generated document must:
- Reference SYSTEM_MANIFEST.md as constitutional source
- Be internally consistent with all other documents
- Follow the exact template patterns
- Include concrete examples, not vague guidance
- Include validation checklists
- Include failure modes and error handling

## Error Handling

| Problem | Solution |
|---------|----------|
| plan.md is vague | Ask user for clarification before generating |
| No web search | Continue with plan.md analysis only |
| Output too generic | Re-read plan.md and extract more specific constraints |
| Consistency violations | Fix conflicts before delivering |

## Validation Checklist

- [ ] plan.md was read completely
- [ ] Web research was performed for major technologies
- [ ] `analysis/plan_analysis.json` exists and is complete
- [ ] `SYSTEM_MANIFEST.md` is at least 2000 words
- [ ] All frozen decisions from plan appear in SYSTEM_MANIFEST
- [ ] All forbidden items from plan appear in hooks
- [ ] All major domains have agent files
- [ ] All major workflows have skill files
- [ ] All major source paths have instruction files
- [ ] Memory files are generated
- [ ] CI/CD configs are generated
- [ ] Smoke tests pass
- [ ] GENERATION_SUMMARY.md is produced
- [ ] All documents reference SYSTEM_MANIFEST.md

## Reference Files

Sub-skill documentation:
- `skills/plan-analyzer/SKILL.md` — Analysis procedure
- `skills/manifest-generator/SKILL.md` — Manifest generation
- `skills/agent-factory/SKILL.md` — Agent generation
- `skills/skill-factory/SKILL.md` — Skill generation
- `skills/hook-factory/SKILL.md` — Hook generation
- `skills/instruction-factory/SKILL.md` — Instruction generation
- `skills/memory-initializer/SKILL.md` — Memory generation
- `skills/pipeline-orchestrator/SKILL.md` — Full pipeline
