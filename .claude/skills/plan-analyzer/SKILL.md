---
name: plan-analyzer
description: >
  Deep analysis of a plan.md file to extract all architectural decisions,
  constraints, technology stack, forbidden items, data flows, agent domains,
  and governance requirements needed to generate the full documentation
  ecosystem. Always use this skill FIRST before generating any documents.
allowed-tools:
  - read
  - search
  - web_search
  - bash
---

# Plan Analyzer Skill

## Reference

- Input: `plan.md` (the system plan to analyze)
- Output: Structured analysis report used by all downstream generators

## Purpose

Extract and structure ALL information from plan.md into a canonical analysis
object that drives the entire document generation pipeline.

This is the foundation step. Every subsequent generator depends on this output.

## When to Use

Use this skill immediately after receiving a plan.md. Run it before generating
ANY documents.

## Prerequisites

- `plan.md` exists and is readable
- Web search is available for research

## Procedure

### Step 1 — Read and Parse plan.md

Read the entire plan.md file. Extract the following structural elements:

```
EXTRACTION TARGETS:
1.  System name and version
2.  System purpose / mission statement
3.  Technology stack (languages, frameworks, libraries)
4.  Architecture decisions (FROZEN)
5.  Hard constraints (ABSOLUTE RULES)
6.  Out-of-scope items (explicitly forbidden)
7.  Data flow description
8.  Agent/component responsibilities
9.  Security requirements
10. Hardware/resource limits
11. Validation/testing requirements
12. Deployment pipeline
13. Promotion/gate criteria
14. Primary optimization metrics
15. Risk categories
```

### Step 2 — Research Authoritative Sources

For each major technology/concept mentioned in plan.md, search for:

1. **Official documentation** — framework docs, API references
2. **Academic papers** — arXiv, Google Scholar, key papers cited
3. **Reference implementations** — official GitHub repos
4. **Best practices** — known anti-patterns, common failure modes
5. **Claude/Copilot docs** — agent patterns, skill patterns

Research keywords:
```python
keywords = extract_technologies(plan.md) + extract_algorithms(plan.md)
for kw in keywords:
    search(f"{kw} official documentation")
    search(f"{kw} best practices architecture")
    search(f"{kw} failure modes pitfalls")
```

### Step 3 — Classify Agent Domains

From the plan, identify distinct functional domains that each need their own agent:

```
DOMAIN CLASSIFICATION CRITERIA:
- Has distinct responsibilities
- Has distinct inputs/outputs
- Has distinct forbidden patterns
- Represents a phase of the pipeline
- Has distinct expertise requirements

EXAMPLES:
- data-engineer (data download, validation, caching)
- feature-architect (feature engineering, normalization)
- model-trainer (training, checkpointing)
- validation-auditor (backtesting, metrics)
- live-ops-engineer (deployment, reconciliation)
- architecture-governor (manifest compliance)
- leakage-auditor (causality, data integrity)
```

### Step 4 — Classify Skill Domains

Identify discrete, repeatable workflows that need skill files:

```
SKILL CLASSIFICATION CRITERIA:
- Multi-step procedure that recurs
- Has clear prerequisites
- Has auditable output artifacts
- Requires specialized knowledge
- Is reusable across runs

EXAMPLES:
- data-download (fetch, validate, cache)
- integrity-check (schema, gaps, anomalies)
- feature-freeze (schema versioning)
- training-pipeline (full train/eval loop)
- walk-forward-backtest (fold-based evaluation)
- promotion-gate-check (gate verification)
```

### Step 5 — Extract Forbidden Patterns

Identify EVERYTHING that is explicitly forbidden or out-of-scope:

```
FORBIDDEN PATTERN CATEGORIES:
1. Architecture prohibitions (e.g., "no LSTM", "no Transformer")
2. Scope prohibitions (e.g., "no futures trading", "no short selling")
3. Data prohibitions (e.g., "no forward-fill", "no lookahead")
4. Security prohibitions (e.g., "no hardcoded secrets")
5. Process prohibitions (e.g., "no live online learning")
```

These directly become hook rules.

### Step 6 — Extract Hard Constraints

Identify absolute rules that must NEVER be violated:

```
CONSTRAINT CATEGORIES:
1. Market/exchange scope
2. Direction/position constraints
3. Data causality rules
4. Hardware resource limits
5. Security rules
6. Validation requirements
7. Deployment prerequisites
```

### Step 7 — Identify Leakage Risks

For ML/data systems, identify all potential data leakage vectors:

```
LEAKAGE RISK CATEGORIES:
1. Time-series leakage (future data in features)
2. Label leakage (target in features)
3. Split contamination (test data in training)
4. Scaler leakage (fitting on wrong split)
5. Fill leakage (forward-fill creating future info)
6. Benchmark leakage (different assumptions for model vs baseline)
```

### Step 8 — Structure the Analysis Report

Produce a structured JSON analysis:

```json
{
  "system": {
    "name": "...",
    "version": "...",
    "purpose": "...",
    "mission": "...",
    "primary_metric": "..."
  },
  "tech_stack": {
    "language": "...",
    "frameworks": [],
    "libraries": [],
    "infrastructure": []
  },
  "frozen_decisions": [
    {"decision": "...", "rationale": "...", "forbidden_alternatives": []}
  ],
  "hard_constraints": [
    {"rule": "...", "category": "...", "violation_consequence": "..."}
  ],
  "out_of_scope": [
    {"item": "...", "category": "...", "reason": "..."}
  ],
  "agent_domains": [
    {
      "name": "...",
      "role": "...",
      "scope": [],
      "not_scope": [],
      "skills": [],
      "ref_docs": []
    }
  ],
  "skill_domains": [
    {
      "name": "...",
      "purpose": "...",
      "trigger": "...",
      "procedure_steps": [],
      "outputs": []
    }
  ],
  "forbidden_patterns": {
    "architecture": [],
    "scope": [],
    "data": [],
    "security": [],
    "process": []
  },
  "leakage_risks": [
    {"risk": "...", "detection": "...", "prevention": "..."}
  ],
  "pipeline_phases": [
    {"phase": 1, "name": "...", "components": [], "output": "..."}
  ],
  "promotion_gates": [
    {"gate": 1, "condition": "...", "threshold": "..."}
  ],
  "hardware_limits": {
    "ram_gb": 0,
    "vram_gb": 0,
    "disk_min_gb": 0
  },
  "security_requirements": [],
  "research_findings": []
}
```

### Step 9 — Validate Analysis Completeness

Before proceeding, verify:

- [ ] System name and purpose are captured
- [ ] All tech stack components identified
- [ ] All frozen decisions documented
- [ ] All hard constraints listed
- [ ] All forbidden items listed
- [ ] Sufficient agent domains identified (minimum 4)
- [ ] Sufficient skill domains identified (minimum 5)
- [ ] All forbidden patterns captured for hooks
- [ ] Leakage risks identified (for data/ML systems)
- [ ] Hardware limits captured
- [ ] Security requirements captured
- [ ] Promotion/gate criteria captured

## Output

Save the analysis report as:
```
analysis/plan_analysis.json
```

Also produce a human-readable summary:
```
analysis/plan_analysis_summary.md
```

## Validation Checklist

- [ ] plan.md was read completely
- [ ] Web research was performed for major technologies
- [ ] Agent domains are distinct (no overlapping responsibilities)
- [ ] Skill domains map to concrete procedures
- [ ] Forbidden patterns are specific and detectable
- [ ] Analysis JSON is valid and parseable
- [ ] All downstream generators can use this analysis
