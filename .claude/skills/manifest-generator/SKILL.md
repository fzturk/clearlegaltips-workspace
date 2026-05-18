---
name: manifest-generator
description: >
  Generates a complete, production-quality SYSTEM_MANIFEST.md from a plan
  analysis report. This is the constitutional document that all other generated
  files reference. Must be run before any other document generator. Use this
  skill whenever a SYSTEM_MANIFEST.md needs to be created from a plan.
allowed-tools:
  - read
  - edit
  - bash
---

# Manifest Generator Skill

## Reference

- Input: `analysis/plan_analysis.json` (from plan-analyzer)
- Output: `SYSTEM_MANIFEST.md`
- Template: `templates/SYSTEM_MANIFEST.template.md`

## Purpose

Generate the SYSTEM_MANIFEST.md — the single source of truth / constitutional
document for the entire system. This document defines everything that all other
documents must be consistent with.

## Critical Rule

**SYSTEM_MANIFEST.md is the ONLY document that other documents must never
contradict.** It is generated first and never overridden.

## Procedure

### Step 1 — Load Analysis

Read `analysis/plan_analysis.json` from the plan-analyzer output.

### Step 2 — Generate Document Status Section

```markdown
## Document Status

This document is the **single source of truth** for the {SYSTEM_NAME} system.
All other documents, implementation decisions, and configurations must be
consistent with this manifest.

**Frozen decisions:**
{LIST ALL FROZEN DECISIONS FROM ANALYSIS}
```

### Step 3 — Generate System Identity

```markdown
## 1 — System Identity

### 1.1 System Name
**{SYSTEM_NAME}**

### 1.2 System Type
{ONE SENTENCE DESCRIPTION OF SYSTEM TYPE}

### 1.3 Purpose
{DETAILED PURPOSE STATEMENT}

### 1.4 Mission Statement
> {MISSION IN BLOCKQUOTE FORMAT}
```

### Step 4 — Generate Primary Optimization Target

```markdown
## 2 — Primary Optimization Target

### 2.1 Core Objective
{PRIMARY METRIC AND DESCRIPTION}

### 2.2 Metric Hierarchy
| Class     | Metric        | Target | Note |
|-----------|---------------|--------|------|
| Primary   | {METRIC_1}    | {TARGET} | {NOTE} |
| Secondary | {METRIC_2}    | {TARGET} | {NOTE} |
```

### Step 5 — Generate Architecture

Include:
- High-level architecture diagram (text-based)
- Architecture rationale table
- Technology stack

### Step 6 — Generate Frozen Decisions

This is CRITICAL. Every frozen decision from analysis must appear here:

```markdown
## 4 — Frozen Core Design Decisions

### 4.1 {DECISION_CATEGORY_1}
| Decision | Value |
|----------|-------|
| {item}   | {value} |

### 4.2 {DECISION_CATEGORY_2}
...
```

### Step 7 — Generate Global Hard Constraints

Number each constraint. These become hook enforcement rules:

```markdown
## 5 — Global Hard Constraints

The following rules are valid at every layer of the system, under all conditions,
without exception:

1. **{CONSTRAINT_1}**
2. **{CONSTRAINT_2}**
...
```

### Step 8 — Generate Out of Scope

```markdown
## 6 — Out of Scope

The following areas are outside the scope of this system:

- {ITEM_1}
- {ITEM_2}
...
```

### Step 9 — Generate Domain-Specific Contracts

For each major domain (data, model, validation, live, etc.) generate a dedicated
contract section:

```markdown
## N — {DOMAIN} Contract

### N.1 {Sub-topic}
{RULES AND REQUIREMENTS}
```

### Step 10 — Generate Promotion Gates

```markdown
## {N} — Promotion Gates

A {MODEL/SERVICE/COMPONENT} may only proceed to {NEXT_STAGE} if ALL of the
following conditions are met:

| # | Condition | Threshold |
|---|-----------|-----------|
| 1 | {condition} | {threshold} |
...
```

### Step 11 — Generate Resource Contract

```markdown
## {N} — Hardware Resource Contract

| Resource | Hard Limit | Safe Usage Limit |
|----------|------------|------------------|
| RAM      | {value}GB  | {value}GB |
| VRAM     | {value}GB  | {value}GB |
| Disk     | {value}    | {value} |
```

### Step 12 — Generate Security Contract

```markdown
## {N} — Security Contract

| Rule | Policy |
|------|--------|
| {rule} | {policy} |
```

### Step 13 — Generate Reproducibility Contract

```markdown
## {N} — Reproducibility Contract

### Mandatory Controls
- Global random seed ({FRAMEWORKS})
- {DETERMINISM_SETTINGS}
- Config versioning
- Dataset fingerprint
- Artifact naming standard
```

### Step 14 — Generate Critical Warnings

```markdown
## {N} — Critical Architecture Warnings

### W-{N}: {WARNING_TITLE}
{DETAILED WARNING}
```

### Step 15 — Generate Document Hierarchy

```markdown
## {N} — Document Hierarchy

{TREE STRUCTURE OF ALL GENERATED DOCUMENTS}

### Hierarchy Rule
In the event of a conflict, document priority order is:
1. **SYSTEM_MANIFEST.md** (this file)
2. Relevant **rules/** file
3. Relevant **skills/** file
```

### Step 16 — Generate Definition of Ready

```markdown
## {N} — Definition of Ready

Before starting to code, all of the following must be yes:

| # | Check | Status |
|---|-------|--------|
| 1 | {check} | ✅ |
...
```

### Step 17 — Generate Definition of Done

```markdown
## {N} — Definition of Done

For each major component, define completion criteria:

### {Component 1}
- [ ] {criterion_1}
- [ ] {criterion_2}
```

### Step 18 — Generate Final Summary

```markdown
## {N} — Final Decision Summary

The final architecture of this system is:

- **{KEY_DECISION_1}**
- **{KEY_DECISION_2}**
...
```

## Quality Rules

Every SYSTEM_MANIFEST.md must:
- Be completely self-contained
- Capture ALL frozen decisions from plan.md
- List ALL hard constraints as numbered items
- List ALL out-of-scope items
- Include promotion/gate criteria
- Include hardware resource limits
- Include security contract
- Include reproducibility requirements
- Be at least 2000 words (comprehensive)

## Output

File: `SYSTEM_MANIFEST.md`

## Validation Checklist

- [ ] All frozen decisions from plan_analysis.json are present
- [ ] All hard constraints are numbered
- [ ] All out-of-scope items are listed
- [ ] Architecture diagram is present
- [ ] All domain contracts are present
- [ ] Promotion gates match plan.md
- [ ] Hardware limits are correct
- [ ] Security contract is present
- [ ] Hierarchy rule is defined
- [ ] Definition of Done covers all components
- [ ] Document is internally consistent
