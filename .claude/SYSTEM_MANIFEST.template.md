# {SYSTEM_NAME} — System Manifest

## Document Status

This document is the **single source of truth** for the {SYSTEM_NAME} system.

All skill files, rule files, implementation decisions, experiment designs, and
deployment processes must be consistent with this manifest.

Any lower-level document that conflicts with this document shall be considered
invalid. **This manifest always takes precedence.**

**Frozen decisions:**

{LIST_FROZEN_DECISIONS}

---

## 1 — System Identity

### 1.1 System Name
**{SYSTEM_NAME}**

### 1.2 System Type
{SYSTEM_TYPE_DESCRIPTION}

### 1.3 Purpose
{SYSTEM_PURPOSE}

### 1.4 Mission Statement

> {MISSION_STATEMENT}

### 1.5 Core Operating Principle
{CORE_PRINCIPLE}

### 1.6 Design Philosophy
{DESIGN_PHILOSOPHY_LIST}

---

## 2 — Primary Optimization Target

### 2.1 Core Objective
{PRIMARY_OBJECTIVE}

### 2.2 Metric Hierarchy

| Class | Metric | Target | Note |
|-------|--------|--------|------|
| **Primary** | {METRIC_1} | {TARGET_1} | {NOTE_1} |
| Secondary | {METRIC_2} | {TARGET_2} | {NOTE_2} |

---

## 3 — High-Level Architecture

```text
{ARCHITECTURE_DIAGRAM}
```

### 3.1 Architecture Rationale

| # | Rationale |
|---|-----------|
| 1 | {RATIONALE_1} |
| 2 | {RATIONALE_2} |

---

## 4 — Frozen Core Design Decisions

### 4.1 {DECISION_CATEGORY_1}

| Decision | Value |
|----------|-------|
| {DECISION_1} | **{VALUE_1}** |
| {DECISION_2} | **{VALUE_2}** |

---

## 5 — Global Hard Constraints

{CONSTRAINT_LIST}

---

## 6 — Out of Scope

{OUT_OF_SCOPE_LIST}

---

## 7 — {DOMAIN_1} Contract

### 7.1 {SUB_TOPIC_1}
{RULES}

---

## {N} — Promotion Gates

{PROMOTION_GATES_TABLE}

---

## {N+1} — Hardware Resource Contract

| Resource | Hard Limit | Safe Usage Limit |
|----------|------------|------------------|
| RAM | {RAM_LIMIT}GB | {RAM_SAFE}GB |
| VRAM | {VRAM_LIMIT}GB | {VRAM_SAFE}GB |

---

## {N+2} — Security Contract

{SECURITY_RULES}

---

## {N+3} — Reproducibility Contract

### Mandatory Controls
{REPRODUCIBILITY_CONTROLS}

---

## {N+4} — Critical Architecture Warnings

### W-1: {WARNING_1}
{WARNING_DETAIL}

---

## {N+5} — Document Hierarchy

```text
.agent/
├── SYSTEM_MANIFEST.md          ← THIS FILE (constitutional source)
├── skills/
│   └── *.md
└── rules/
    └── *.md
```

### Hierarchy Rule

In the event of a conflict, document priority:
1. **SYSTEM_MANIFEST.md** (this file)
2. Relevant **rules/** file
3. Relevant **skills/** file

---

## {N+6} — Definition of Ready

| # | Check | Status |
|---|-------|--------|
| 1 | {CHECK_1} | ✅ |

---

## {N+7} — Definition of Done

### {COMPONENT_1}
- [ ] {CRITERION_1}
- [ ] {CRITERION_2}

---

## {N+8} — Final Decision Summary

The final architecture of this system is:

{FINAL_SUMMARY_LIST}

---

## Enforcement Clause

The rules defined in this manifest are binding throughout code writing,
data processing, training, validation, and deployment.

**Version:** {VERSION}  
**Status:** Frozen  
**Change policy:** May only be changed by revision of this file.
