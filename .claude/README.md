# Plan-to-System

> **From `plan.md` to complete documentation ecosystem in minutes, not months.**

## What This Does

You write a `plan.md` describing your system.  
This tool generates everything else:

| Document Type | Count | What It Does |
|--------------|-------|--------------|
| `SYSTEM_MANIFEST.md` | 1 | Constitutional source of truth |
| `*.agent.md` | 4-12 | Specialized AI agents per domain |
| `SKILL.md` | 5-20 | Workflow guides for each procedure |
| `*.instructions.md` | 5-10 | Always-on coding rules per directory |
| Hook scripts | 4-6 | Safety enforcement (blocks forbidden patterns) |
| Memory files | 5-8 | Persistent knowledge base |
| CI/CD configs | 2 | GitHub Actions workflows |

**Before:** ~1 month of manual work  
**After:** Minutes

## Quick Start

### Option 1: Use as a Claude Skill

Install this skill package, then give Claude your `plan.md`:

```
"I have a plan.md for my system. Please use the plan-to-system skill 
to generate all the documentation."
```

Claude will run the full pipeline automatically.

### Option 2: Use the Python Script

```bash
# Basic usage
python scripts/generate_system.py --plan plan.md --output my-system/

# Dry run (preview what would be generated)
python scripts/generate_system.py --plan plan.md --output my-system/ --dry-run

# Validate existing output
python scripts/generate_system.py --output my-system/ --validate-only
```

### Option 3: Run Manually with Claude

Give Claude this prompt:

```
Read plan.md and use the plan-to-system skill to:
1. Analyze the plan and research relevant technologies
2. Generate SYSTEM_MANIFEST.md (constitutional source)
3. Generate all agent files
4. Generate all skill files
5. Generate all hook scripts
6. Generate all instruction files
7. Generate all memory files
8. Run the smoke tests to verify hooks work
9. Produce a GENERATION_SUMMARY.md
```

## How It Works

```
plan.md
   │
   ▼
PHASE 0: plan-analyzer
   ├── Reads plan.md completely
   ├── Researches authoritative sources (web search)
   └── Produces analysis/plan_analysis.json
   │
   ▼
PHASE 1: Constitutional Layer
   ├── SYSTEM_MANIFEST.md (generated from template)
   ├── ARCHITECTURE_DECISIONS.md
   ├── copilot-instructions.md
   └── AGENTS.md
   │
   ▼
PHASE 2: agent-factory
   └── .github/agents/*.agent.md
   │
   ▼
PHASE 3: skill-factory
   └── .github/skills/*/SKILL.md
   │
   ▼
PHASE 4: hook-factory
   └── .github/hooks/{scripts,configs}
   │
   ▼
PHASE 5: instruction-factory
   └── .github/instructions/*.instructions.md
   │
   ▼
PHASE 6: memory-initializer
   └── .agent/memory/*.{md,json}
   │
   ▼
PHASE 7: CI/CD
   └── .github/workflows/{ci,nightly}.yml
   │
   ▼
PHASE 8: Validation
   └── Cross-document consistency check
```

## What Makes a Good plan.md

The richer your `plan.md`, the better the generated documentation.

Include:
- **System purpose** — why does this exist?
- **Technology stack** — what languages, frameworks, libraries?
- **Architecture decisions** — what is frozen and why?
- **Hard constraints** — what MUST NEVER happen?
- **Out of scope** — what will NOT be built?
- **Pipeline phases** — what is the build order?
- **Promotion gates** — when can we advance to the next stage?
- **Hardware limits** — RAM, VRAM, disk requirements?
- **Security rules** — credential handling, API permissions?

## Document Priority

When documents conflict, this hierarchy applies:

```
1. SYSTEM_MANIFEST.md      ← ALWAYS WINS
2. .agent/rules/*.md
3. .agent/skills/*.md
4. .agent/memory/*
5. Everything else
```

## File Structure

```
plan-to-system/
├── SKILL.md                    ← Main skill file (this is the entry point)
├── README.md                   ← This file
│
├── plan-to-system.agent.md     ← Master orchestrator agent
│
├── skills/
│   ├── plan-analyzer/          ← Phase 0: Deep plan analysis
│   │   └── SKILL.md
│   ├── manifest-generator/     ← Phase 1: SYSTEM_MANIFEST generation
│   │   └── SKILL.md
│   ├── agent-factory/          ← Phase 2: Agent file generation
│   │   └── SKILL.md
│   ├── skill-factory/          ← Phase 3: Skill file generation
│   │   └── SKILL.md
│   ├── hook-factory/           ← Phase 4: Hook/script generation
│   │   └── SKILL.md
│   ├── instruction-factory/    ← Phase 5: Instruction file generation
│   │   └── SKILL.md
│   ├── memory-initializer/     ← Phase 6: Memory file generation
│   │   └── SKILL.md
│   └── pipeline-orchestrator/  ← Full end-to-end pipeline
│       └── SKILL.md
│
├── templates/
│   ├── SYSTEM_MANIFEST.template.md
│   ├── agent.template.md
│   ├── skill.template.md
│   └── instruction.template.md
│
└── scripts/
    └── generate_system.py      ← Python automation script
```

## After Generation

1. **Review `SYSTEM_MANIFEST.md`** — verify it accurately captures your plan
2. **Run smoke tests** — `bash .github/hooks/scripts/smoke-test-hooks.sh`
3. **Customize agents** — add domain-specific knowledge to each agent
4. **Customize skills** — add concrete implementation steps to each skill
5. **Start implementing** — follow the build order in SYSTEM_MANIFEST.md

## Customization

The generated documentation is a starting point. You should:

- **SYSTEM_MANIFEST.md** — Review all frozen decisions for accuracy
- **Agents** — Add system-specific constraints and checks
- **Skills** — Add concrete implementation steps for your specific tech stack
- **Hooks** — Add additional forbidden patterns specific to your domain
- **Instructions** — Add domain-specific implementation patterns

## Requirements

- Python 3.11+ (for scripts)
- `jq` (for hook scripts)
- Claude Code or GitHub Copilot (for AI-assisted generation)

## Contributing

This tool improves with better templates. If you find that:
- A generated document is missing a common pattern → add it to the template
- A generated document is too generic → add more extraction logic to plan-analyzer
- A hook misses a common forbidden pattern → add it to hook-factory

## Governance

This tool follows the same governance principles it generates:
- All decisions are documented
- All constraints are explicit
- All forbidden patterns are blocked by hooks
- The README is the constitutional source for this tool itself
