---
name: agent-factory
description: >
  Generates all specialized agent files (*.agent.md) for a system based on
  the plan analysis. Each agent gets clear scope, tool access, reference docs,
  and hard constraints. Use this skill after SYSTEM_MANIFEST.md is complete.
allowed-tools:
  - read
  - edit
  - bash
---

# Agent Factory Skill

## Reference

- Input: `analysis/plan_analysis.json`, `SYSTEM_MANIFEST.md`
- Output: `.github/agents/*.agent.md`
- Template: `templates/agent.template.md`

## Purpose

Generate specialized agent files for each functional domain identified in the
plan analysis. Each agent is a focused specialist with clear responsibilities.

## Agent Taxonomy

Agents fall into two categories:

### Public Agents (user-invocable: true)
- Directly invoked by users for specific tasks
- Example: data-engineer, model-trainer, live-ops-engineer

### Internal / Governance Agents (user-invocable: false)
- Support and cross-cutting concerns
- Example: architecture-governor, leakage-auditor, code-reviewer

## Procedure

### Step 1 — Enumerate Agent Domains

From `analysis/plan_analysis.json`, extract `agent_domains`.

For each domain, determine:
- Public or internal classification
- Which skills it uses
- Which documents it references
- Which source directories it owns

### Step 2 — Generate Each Agent File

For each agent domain, generate a complete `{name}.agent.md`:

```markdown
---
name: {agent-name}
description: >
  {ONE PARAGRAPH: what this agent does, what problems it solves,
   and what kind of tasks to delegate to it}
tools:
  - {tool_1}
  - {tool_2}
user-invocable: {true|false}
---

# {Agent Name} Agent

## Role

You are the {Agent Title} for the {SYSTEM_NAME} project.

{2-3 sentences describing the agent's core responsibility and how it
fits into the overall system pipeline.}

## Reference Documents (read before any task)

- `.agent/SYSTEM_MANIFEST.md` — constitutional source of truth
- `.agent/skills/{relevant_skill}.md` — {description}
- `.agent/rules/{relevant_rule}.md` — {description}
- `.github/instructions/{relevant}.instructions.md` — coding rules

## Skills You Use

- `{skill-1}` — {when and why}
- `{skill-2}` — {when and why}

## Your Scope

### You DO:
- {concrete action 1}
- {concrete action 2}
- {concrete action 3}
...

### You DO NOT:
- {out of scope item 1}
- {out of scope item 2}
- {forbidden action}
...

## Hard Constraints

1. **Manifest wins:** {brief restatement}
2. **{CONSTRAINT_2}**
3. **{CONSTRAINT_3}**
...

## Operational Rules

- {rule_1}
- {rule_2}
...

## Critical Self-Check

Before submitting any {domain} code/artifact, verify:

- [ ] {check_1}
- [ ] {check_2}
- [ ] {check_3}
...

## Working Directories

- {domain} code: `src/{domain}/`
- Tests: `tests/{domain}/`
- Artifacts: `{artifact_path}/`

## Acceptance Standard

A {domain} task is complete only if {specific completion criterion}.
```

### Step 3 — Generate Standard Governance Agents

Always generate these agents regardless of system type:

#### 1. architecture-governor
```
Purpose: Manifest-alignment and scope-governance specialist
user-invocable: false
Detects architectural drift, forbidden scope expansion, frozen decision violations
```

#### 2. code-reviewer
```
Purpose: Read-only quality, safety, and maintainability reviewer
user-invocable: false
Reviews code for correctness, safety, architecture compliance
```

#### 3. {system-specific}-auditor
```
Purpose: Audit specialist for the system's primary risk category
user-invocable: false
Example: leakage-auditor for ML, security-auditor for fintech
```

### Step 4 — Generate System-Specific Agents

Based on `plan_analysis.json`, generate agents for each pipeline phase:

For each agent_domain in analysis:
1. Extract: name, role, scope, not_scope, skills, ref_docs
2. Generate the full agent file following the template
3. Ensure scope boundaries are clear and non-overlapping
4. Ensure forbidden actions match plan constraints

### Step 5 — Generate agents/README.md

```markdown
# Agents Map

## Public Agents
(suitable for direct user-facing task delegation)
- `{agent-1}` — {one line description}
- `{agent-2}` — {one line description}

## Internal / Governance Agents
(best used as supporting or governance-focused agents)
- `architecture-governor` — manifest compliance
- `code-reviewer` — quality review
- `{system}-auditor` — safety audit

## Usage Principle
Use the smallest specialized agent that matches the task.

## Governance Rule
All agents are subordinate to `.agent/SYSTEM_MANIFEST.md`.
```

## Quality Rules

Every agent file must:
- Have a description that clearly triggers for its use case
- List ALL relevant reference documents
- Have explicit DO/DO NOT scope sections
- Have numbered hard constraints
- Have a critical self-check list
- Have a clear acceptance standard
- Reference the SYSTEM_MANIFEST as constitutional source

## Agent Count Guidelines

| System Complexity | Expected Agent Count |
|-------------------|---------------------|
| Simple (1-2 pipeline phases) | 3-5 agents |
| Medium (3-5 phases) | 5-8 agents |
| Complex (5+ phases) | 8-12 agents |
| Always include | architecture-governor, code-reviewer |

## Output

Files: `.github/agents/{name}.agent.md` (one per agent)
File: `.github/agents/README.md`

## Validation Checklist

- [ ] All agent domains from analysis are covered
- [ ] Scope boundaries are non-overlapping
- [ ] All forbidden items from plan appear in relevant agents
- [ ] architecture-governor agent is always present
- [ ] code-reviewer agent is always present
- [ ] All agents reference SYSTEM_MANIFEST.md
- [ ] All agents have concrete DO/DO NOT sections
- [ ] All agents have self-check checklists
- [ ] README.md is generated
