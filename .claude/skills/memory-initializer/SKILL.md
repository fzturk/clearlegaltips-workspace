---
name: memory-initializer
description: >
  Generates all persistent memory files for a system — known failure modes,
  leakage patterns, false positives, validation immutables, promotion history,
  and schema placeholders. These files form the system's institutional knowledge
  base. Use after all other documentation is generated.
allowed-tools:
  - read
  - edit
  - bash
---

# Memory Initializer Skill

## Reference

- Input: `analysis/plan_analysis.json`, `SYSTEM_MANIFEST.md`
- Output: `.agent/memory/*.md`, `.agent/memory/*.json`

## Purpose

Generate the institutional knowledge base: persistent files that capture
known patterns, failure modes, invariants, and history that agents
reference across sessions.

## Memory File Categories

### Always-Generated Files

1. `ARCHITECTURE_DECISIONS.md` — Summary of frozen decisions
2. `KNOWN_FAILURE_MODES.md` — System-specific failure patterns
3. `VALIDATION_IMMUTABLES.md` — Rules that may never be relaxed
4. `KNOWN_FALSE_POSITIVES.md` — Hook patterns that may false-alarm
5. `PROMOTION_HISTORY.json` — Audit trail for promotions
6. `README.md` — Memory directory governance

### Conditionally-Generated Files

For ML/Data systems:
- `KNOWN_LEAKAGE_PATTERNS.md` — Data leakage catalog
- `FEATURE_SCHEMA.json` — Feature registry placeholder
- `REWARD_FAILURE_MODES.md` — RL reward gaming patterns

For financial/trading systems:
- `EXCHANGE_EXECUTION_INVARIANTS.md` — Exchange operation rules

For any system with paper/live modes:
- `PAPER_TRADING_OPERATIONS.md` — Paper mode operational rules

## Procedure

### Step 1 — Generate ARCHITECTURE_DECISIONS.md

Extract from plan analysis and SYSTEM_MANIFEST.md:

```markdown
# Architecture Decisions

## Purpose
Convenience summary of core architectural decisions frozen in the manifest.

## Status
- Source of truth: SYSTEM_MANIFEST.md
- This file is a convenience summary, not the constitutional source
- If this file conflicts with the manifest, the manifest wins

---

## 1. {DECISION_CATEGORY_1}

{TABLE OF DECISIONS}
- {Decision}: **{Value}**
- {Forbidden}: **{Item}**

## 2. {DECISION_CATEGORY_2}
...

## N. Development Runtime Policy
{DESCRIBE DOCKER/LOCAL EXECUTION MODEL}
```

### Step 2 — Generate KNOWN_FAILURE_MODES.md

From plan_analysis.json, extract risk categories and generate concrete failure mode catalog:

```markdown
# Known Failure Modes

## Purpose
Lists failure modes requiring special attention and high probability of recurrence.

## Severity Policy
- Any confirmed {PRIMARY_FAILURE} invalidates affected results
- There is no acceptable "small {FAILURE_TYPE}"

---

## 1. {FAILURE_MODE_NAME}

### Pattern
{What the failure looks like}

### Typical Cause
- {cause_1}
- {cause_2}

### Symptoms
- {symptom_1}
- {symptom_2}

### Mitigation
- {mitigation_1}
- {mitigation_2}

---

## N. Audit Questions

When making changes, ask:
1. {question_1}
2. {question_2}
```

### Step 3 — Generate VALIDATION_IMMUTABLES.md

```markdown
# Validation Immutables

## Purpose
Invariants that must never be relaxed during validation and promotion.

---

## 1. {IMMUTABLE_RULE_1}
{Description and rationale}

## 2. {IMMUTABLE_RULE_2}
{Description and rationale}

...

## N. Auditor Mindset

The primary question to always ask:
> "{CORE_AUDIT_QUESTION}"

If the answer is not clear:
- Do not promote
- Request more audit
- Treat the result as suspicious
```

### Step 4 — Generate KNOWN_FALSE_POSITIVES.md

```markdown
# Known False Positives

## Purpose
Collects known false positive examples encountered in hooks, static scans,
and security checks. Prevents diluting real violations.

## Important Rule
This file does not declare any real violation "automatically safe."
Context check and manual review are always required.

---

## 1. {FALSE_POSITIVE_PATTERN_1}

### Pattern
{Hook or scan catches this pattern}

### Example
\`\`\`python
# This might be flagged but is actually safe
{EXAMPLE_CODE}
\`\`\`

### Why It Can Be False Positive
{REASON}

### Review Rule
- {HOW_TO_DISTINGUISH_FP_FROM_REAL}

---

## What Must Never Become a False Positive Excuse
{LIST PATTERNS THAT MUST ALWAYS BE FLAGGED}
```

### Step 5 — Generate PROMOTION_HISTORY.json

```json
{
  "schema_version": "1.0",
  "system_version": "{VERSION}",
  "source_of_truth": ".agent/SYSTEM_MANIFEST.md",
  "notes": [
    "This file stores promotion and deployment history.",
    "It is a hard-memory audit artifact.",
    "If this file conflicts with manifest or artifacts, the manifest wins."
  ],
  "current_champion": null,
  "history": [],
  "fields_reference": {
    "model_id": "Canonical artifact name",
    "decision": "REJECT | REVISE_AND_REEVALUATE | PASS_TO_NEXT_STAGE | ELIGIBLE",
    "dataset_hash": "12-char dataset fingerprint",
    "config_version": "Experiment config version string",
    "reason": "Human-readable decision rationale",
    "timestamp_utc": "Decision timestamp in UTC"
  }
}
```

### Step 6 — Generate KNOWN_LEAKAGE_PATTERNS.md (ML systems)

```markdown
# Known Leakage Patterns

## Purpose
Lists leakage patterns requiring particular attention.
Every item here can artificially inflate performance results.

## Severity Policy
- Any confirmed leakage invalidates affected results
- There is no acceptable "small leakage"

---

## 1. {LEAKAGE_TYPE_1}

### Pattern
{What causes this leakage}

### Example
{CODE EXAMPLE of the wrong approach}

### Correct Rule
{WHAT TO DO INSTEAD}

### Detection
{HOW TO DETECT THIS IN CODE REVIEW}

---

## N. Rule of Thumb

Ask:
> "Could this information really be known at that moment?"

If not clear → suspicious → audit required → performance claim suspended.
```

### Step 7 — Generate FEATURE_SCHEMA.json (ML systems)

```json
{
  "schema_version": "1.0",
  "system_version": "{VERSION}",
  "status": "placeholder_until_feature_freeze",
  "source_of_truth": ".agent/SYSTEM_MANIFEST.md",
  "notes": [
    "Update only after feature registry and observation block order are finalized.",
    "If this file conflicts with the manifest, the manifest wins."
  ],
  "timeframes": {
    "main": "{MAIN_TIMEFRAME}",
    "informative": "{INFORMATIVE_TIMEFRAME}"
  },
  "observation_contract": {
    "forbidden_inputs": []
  },
  "raw_canonical_schema": [],
  "feature_registry": [],
  "schema_hash": null,
  "last_updated_utc": null
}
```

### Step 8 — Generate memory/README.md

```markdown
# {SYSTEM_NAME} Memory

## Purpose
Persistent knowledge base for the {SYSTEM_NAME} system.

## Governance
No file here may conflict with SYSTEM_MANIFEST.md.

Priority order:
1. SYSTEM_MANIFEST.md
2. relevant rules/*.md
3. relevant skills/*.md
4. memory/*

## Files
{LIST ALL MEMORY FILES WITH ONE-LINE DESCRIPTIONS}

## Editing Policy
Only update under these conditions:
- Manifest revision requires alignment
- New persistent failure mode confirmed
- Schema formalized
- New decision added to history
- Operational invariants clarified

## Non-Goals
NOT a temporary notes repository.
NOT a scratchpad.
NOT a second constitution overriding the manifest.
```

## Output Structure

```
.agent/memory/
├── README.md
├── ARCHITECTURE_DECISIONS.md
├── KNOWN_FAILURE_MODES.md
├── KNOWN_FALSE_POSITIVES.md
├── VALIDATION_IMMUTABLES.md
├── PROMOTION_HISTORY.json
├── KNOWN_LEAKAGE_PATTERNS.md (ML systems)
├── FEATURE_SCHEMA.json (ML systems)
├── REWARD_FAILURE_MODES.md (RL systems)
└── EXCHANGE_EXECUTION_INVARIANTS.md (financial systems)
```

## Validation Checklist

- [ ] All failure modes from plan analysis are documented
- [ ] All validation invariants are captured
- [ ] PROMOTION_HISTORY.json is valid JSON
- [ ] False positive catalog covers hook patterns
- [ ] ARCHITECTURE_DECISIONS.md matches SYSTEM_MANIFEST.md
- [ ] Memory README explains governance
- [ ] System-specific files generated for detected system type
