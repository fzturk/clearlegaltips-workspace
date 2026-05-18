#!/usr/bin/env python3
"""
plan-to-system: Automated documentation ecosystem generator.

Usage:
    python generate_system.py --plan plan.md --output generated-system/
    python generate_system.py --plan plan.md --output generated-system/ --no-research
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate complete documentation ecosystem from plan.md"
    )
    parser.add_argument("--plan", type=Path, default=Path("plan.md"), help="Path to plan.md")
    parser.add_argument("--output", type=Path, default=Path("generated-system"), help="Output directory")
    parser.add_argument("--no-research", action="store_true", help="Skip web research phase")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be generated without writing")
    parser.add_argument("--validate-only", action="store_true", help="Only run consistency validation on existing output")
    return parser.parse_args()


def create_directory_structure(output_dir: Path) -> None:
    """Create the complete output directory structure."""
    dirs = [
        output_dir / ".github" / "instructions",
        output_dir / ".github" / "agents",
        output_dir / ".github" / "hooks" / "scripts",
        output_dir / ".github" / "hooks" / "logs",
        output_dir / ".github" / "workflows",
        output_dir / ".agent" / "skills",
        output_dir / ".agent" / "rules",
        output_dir / ".agent" / "memory",
        output_dir / "analysis",
        output_dir / "configs",
        output_dir / "src",
        output_dir / "tests",
    ]
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)
    print(f"✓ Directory structure created at {output_dir}")


def extract_system_info(plan_content: str) -> dict[str, Any]:
    """Extract key system information from plan.md content."""
    info: dict[str, Any] = {
        "name": "Unknown System",
        "version": "1.0",
        "purpose": "",
        "tech_stack": [],
        "frozen_decisions": [],
        "hard_constraints": [],
        "out_of_scope": [],
        "agent_domains": [],
        "skill_domains": [],
        "forbidden_patterns": {
            "architecture": [],
            "scope": [],
            "data": [],
            "security": [],
            "process": [],
        },
        "hardware_limits": {},
        "pipeline_phases": [],
        "promotion_gates": [],
        "leakage_risks": [],
        "security_requirements": [],
    }

    # Extract system name
    name_match = re.search(r"#\s+([^\n]+)", plan_content)
    if name_match:
        info["name"] = name_match.group(1).strip()

    # Extract forbidden items (common patterns)
    forbidden_patterns = {
        "lstm|gru|rnn": ("architecture", "Recurrent neural networks (LSTM/GRU/RNN)"),
        "transformer|attention": ("architecture", "Transformer/attention architectures"),
        "futures|margin|perpetual": ("scope", "Futures/margin/perpetual trading"),
        "short|shorting": ("scope", "Short selling"),
        "center=True": ("data", "Centered rolling calculations (lookahead)"),
        "shift\\(-": ("data", "Negative shift (lookahead)"),
        "ffill|forward.fill|interpolate": ("data", "Forward fill / interpolation on price data"),
        "api_key.*=.*['\"]|api_secret.*=.*['\"]": ("security", "Hardcoded API credentials"),
        "withdraw": ("security", "Withdraw API permission"),
        "online.learn": ("process", "Live online learning"),
    }

    content_lower = plan_content.lower()
    for pattern, (category, description) in forbidden_patterns.items():
        if re.search(pattern, content_lower):
            info["forbidden_patterns"][category].append(description)

    # Extract hardware limits
    ram_match = re.search(r"(\d+)\s*GB\s+RAM", plan_content, re.IGNORECASE)
    vram_match = re.search(r"(\d+)\s*GB\s+VRAM", plan_content, re.IGNORECASE)
    if ram_match:
        info["hardware_limits"]["ram_gb"] = int(ram_match.group(1))
    if vram_match:
        info["hardware_limits"]["vram_gb"] = int(vram_match.group(1))

    # Detect system type
    ml_keywords = ["ppo", "reinforcement learning", "training", "model", "neural network", "loss"]
    trading_keywords = ["binance", "spot", "trading", "portfolio", "order", "exchange"]
    api_keywords = ["api", "rest", "graphql", "endpoint", "webhook"]

    ml_score = sum(1 for kw in ml_keywords if kw in content_lower)
    trading_score = sum(1 for kw in trading_keywords if kw in content_lower)
    api_score = sum(1 for kw in api_keywords if kw in content_lower)

    if ml_score >= 3:
        info["system_type"] = "ml"
    if trading_score >= 3:
        info["system_type"] = info.get("system_type", "") + "_trading"
    if api_score >= 3 and ml_score < 3:
        info["system_type"] = "api"

    if "system_type" not in info:
        info["system_type"] = "generic"

    return info


def generate_analysis_report(plan_path: Path, output_dir: Path) -> dict[str, Any]:
    """Generate the plan analysis JSON report."""
    plan_content = plan_path.read_text(encoding="utf-8")
    info = extract_system_info(plan_content)

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": str(plan_path),
        "system": {
            "name": info["name"],
            "version": info["version"],
            "type": info.get("system_type", "generic"),
        },
        "forbidden_patterns": info["forbidden_patterns"],
        "hardware_limits": info["hardware_limits"],
        "plan_content_length": len(plan_content),
        "plan_content_hash": hash(plan_content) & 0xFFFFFFFF,
    }

    analysis_path = output_dir / "analysis" / "plan_analysis.json"
    with analysis_path.open("w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    # Generate human-readable summary
    summary_lines = [
        f"# Plan Analysis Summary",
        f"",
        f"Generated: {report['generated_at']}",
        f"Source: {plan_path}",
        f"",
        f"## System",
        f"- Name: {info['name']}",
        f"- Type: {info.get('system_type', 'generic')}",
        f"",
        f"## Forbidden Patterns Detected",
    ]
    for category, patterns in info["forbidden_patterns"].items():
        if patterns:
            summary_lines.append(f"### {category.title()}")
            for p in patterns:
                summary_lines.append(f"- {p}")
    summary_lines.extend([
        "",
        "## Hardware Limits",
    ])
    for k, v in info["hardware_limits"].items():
        summary_lines.append(f"- {k}: {v}")

    summary_path = output_dir / "analysis" / "plan_analysis_summary.md"
    summary_path.write_text("\n".join(summary_lines), encoding="utf-8")

    print(f"✓ Analysis complete: {analysis_path}")
    return report


def generate_ci_yml(output_dir: Path, system_name: str) -> None:
    """Generate GitHub Actions CI workflow."""
    content = f"""name: ci

on:
  push:
    branches:
      - main
      - master
      - develop
      - "feature/**"
      - "fix/**"
  pull_request:
  workflow_dispatch:

concurrency:
  group: ci-${{{{ github.ref }}}}
  cancel-in-progress: true

env:
  PYTHONUNBUFFERED: "1"
  PIP_DISABLE_PIP_VERSION_CHECK: "1"

jobs:
  governance-check:
    name: Governance / repo structure check
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Validate required repo governance files
        shell: bash
        run: |
          python - <<'PY'
          from pathlib import Path
          import sys

          required_files = [
              "AGENTS.md",
              ".github/copilot-instructions.md",
              ".agent/SYSTEM_MANIFEST.md",
          ]

          errors = []
          for path in required_files:
              if not Path(path).exists():
                  errors.append(f"Missing required file: {{path}}")

          if errors:
              print("Governance check FAILED:")
              for err in errors:
                  print(f" - {{err}}")
              sys.exit(1)

          print("Governance check PASSED")
          PY

  quality:
    name: Lint / type / tests
    runs-on: ubuntu-latest
    needs: governance-check

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
          cache: "pip"

      - name: Install system dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y jq

      - name: Install Python dependencies
        shell: bash
        run: |
          python -m pip install --upgrade pip
          if [ -f requirements.txt ]; then
            pip install -r requirements.txt
          fi
          pip install ruff mypy pytest

      - name: Make scripts executable
        run: |
          chmod +x .github/hooks/scripts/*.sh || true

      - name: Ruff
        run: |
          ruff check src tests || true

      - name: Mypy
        run: |
          mypy src || true

      - name: Pytest
        run: |
          pytest tests -v -m "not slow and not gpu" || true

  tooling-smoke:
    name: Hook smoke tests
    runs-on: ubuntu-latest
    needs: governance-check

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install system dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y jq

      - name: Make scripts executable
        run: chmod +x .github/hooks/scripts/*.sh || true

      - name: Run hook smoke tests
        run: |
          bash .github/hooks/scripts/smoke-test-hooks.sh || true
"""
    path = output_dir / ".github" / "workflows" / "ci.yml"
    path.write_text(content, encoding="utf-8")
    print(f"✓ Generated: {path.relative_to(output_dir)}")


def generate_nightly_yml(output_dir: Path) -> None:
    """Generate nightly governance workflow."""
    content = """name: nightly-governance

on:
  schedule:
    - cron: "0 3 * * *"
  workflow_dispatch:

concurrency:
  group: nightly-governance
  cancel-in-progress: true

jobs:
  nightly-audit:
    name: Nightly governance audit
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
          cache: "pip"

      - name: Install system dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y jq

      - name: Install Python dependencies
        shell: bash
        run: |
          python -m pip install --upgrade pip
          if [ -f requirements.txt ]; then
            pip install -r requirements.txt
          fi
          pip install pytest ruff mypy

      - name: Make scripts executable
        run: chmod +x .github/hooks/scripts/*.sh || true

      - name: Run hook smoke tests
        run: bash .github/hooks/scripts/smoke-test-hooks.sh || true

      - name: Run lint
        run: ruff check src tests || true

      - name: Upload nightly artifacts
        uses: actions/upload-artifact@v4
        with:
          name: nightly-governance-artifacts
          path: |
            .github/hooks/logs/
          if-no-files-found: warn
"""
    path = output_dir / ".github" / "workflows" / "nightly-governance.yml"
    path.write_text(content, encoding="utf-8")
    print(f"✓ Generated: {path.relative_to(output_dir)}")


def generate_promotion_history(output_dir: Path, system_info: dict) -> None:
    """Generate PROMOTION_HISTORY.json placeholder."""
    data = {
        "schema_version": "1.0",
        "system_version": system_info.get("version", "1.0"),
        "source_of_truth": ".agent/SYSTEM_MANIFEST.md",
        "notes": [
            "This file stores promotion and deployment history for governance.",
            "It is a hard-memory audit artifact, not a replacement for reports.",
            "If this file conflicts with manifest or artifacts, manifest wins."
        ],
        "current_champion": None,
        "history": [],
        "fields_reference": {
            "model_id": "Canonical artifact name",
            "decision": "REJECT | REVISE_AND_REEVALUATE | PASS_TO_PAPER | ELIGIBLE",
            "dataset_hash": "12-char dataset fingerprint",
            "config_version": "Experiment config version string",
            "reason": "Human-readable decision rationale",
            "timestamp_utc": "Decision timestamp in UTC"
        }
    }
    path = output_dir / ".agent" / "memory" / "PROMOTION_HISTORY.json"
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"✓ Generated: {path.relative_to(output_dir)}")


def validate_output(output_dir: Path) -> dict[str, list[str]]:
    """Validate consistency across generated documents."""
    issues = {"errors": [], "warnings": []}

    required_files = [
        ".agent/SYSTEM_MANIFEST.md",
        "AGENTS.md",
        ".github/copilot-instructions.md",
        ".agent/memory/PROMOTION_HISTORY.json",
        ".github/workflows/ci.yml",
        ".github/workflows/nightly-governance.yml",
        ".agent/memory/ARCHITECTURE_DECISIONS.md",
    ]

    for f in required_files:
        if not (output_dir / f).exists():
            issues["errors"].append(f"Missing required file: {f}")

    # Check agents directory has files
    agents_dir = output_dir / ".github" / "agents"
    if agents_dir.exists():
        agent_files = list(agents_dir.glob("*.agent.md"))
        if len(agent_files) < 2:
            issues["warnings"].append(f"Only {len(agent_files)} agent files found (expected 4+)")

    # Check skills directory
    skills_dir = output_dir / ".github" / "skills"
    if skills_dir.exists():
        skill_dirs = [d for d in skills_dir.iterdir() if d.is_dir() and (d / "SKILL.md").exists()]
        if len(skill_dirs) < 3:
            issues["warnings"].append(f"Only {len(skill_dirs)} skill directories found (expected 5+)")

    # Check hooks
    hooks_dir = output_dir / ".github" / "hooks"
    if not list(hooks_dir.glob("*.json")) if hooks_dir.exists() else True:
        issues["warnings"].append("No hook config JSON files found")

    return issues


def generate_summary(output_dir: Path, issues: dict) -> None:
    """Generate GENERATION_SUMMARY.md."""
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    # Count generated files
    file_counts = {}
    for category, glob in [
        ("Agents", ".github/agents/*.agent.md"),
        ("Skills", ".github/skills/*/SKILL.md"),
        ("Instructions", ".github/instructions/*.instructions.md"),
        ("Memory files", ".agent/memory/*"),
        ("Hook scripts", ".github/hooks/scripts/*"),
        ("CI/CD configs", ".github/workflows/*.yml"),
    ]:
        count = len(list(output_dir.glob(glob)))
        file_counts[category] = count

    lines = [
        "# System Documentation Generated",
        "",
        f"**Generated:** {timestamp}",
        f"**Output:** `{output_dir}/`",
        "",
        "## Generated Files",
        "",
    ]

    for category, count in file_counts.items():
        status = "✅" if count > 0 else "⚠️"
        lines.append(f"- {status} **{category}**: {count} files")

    lines.extend([
        "",
        "## Validation Results",
        "",
    ])

    if issues["errors"]:
        lines.append("### ❌ Errors (Must Fix)")
        for e in issues["errors"]:
            lines.append(f"- {e}")
        lines.append("")

    if issues["warnings"]:
        lines.append("### ⚠️ Warnings")
        for w in issues["warnings"]:
            lines.append(f"- {w}")
        lines.append("")

    if not issues["errors"] and not issues["warnings"]:
        lines.append("✅ All validation checks passed!")
        lines.append("")

    lines.extend([
        "## Next Steps",
        "",
        "1. Review `SYSTEM_MANIFEST.md` and ensure it accurately captures your plan",
        "2. Run: `bash .github/hooks/scripts/smoke-test-hooks.sh`",
        "3. Run: `ruff check src tests && mypy src && pytest tests -v`",
        "4. Review each agent in `.github/agents/` and customize scope",
        "5. Review each skill in `.github/skills/` and add domain-specific steps",
        "6. Start implementation following the build order in `SYSTEM_MANIFEST.md`",
        "",
        "## Document Hierarchy",
        "",
        "When documents conflict:",
        "1. `.agent/SYSTEM_MANIFEST.md` (constitutional source — ALWAYS WINS)",
        "2. `.agent/rules/*.md`",
        "3. `.agent/skills/*.md`",
        "4. `.agent/memory/*`",
    ])

    path = output_dir / "GENERATION_SUMMARY.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\n✓ Generation summary: {path}")


def main() -> int:
    args = parse_args()

    if not args.plan.exists():
        print(f"ERROR: plan.md not found at {args.plan}", file=sys.stderr)
        print("Usage: python generate_system.py --plan plan.md --output generated-system/")
        return 1

    print(f"\n{'='*60}")
    print(f"  Plan-to-System Documentation Generator")
    print(f"{'='*60}")
    print(f"  Input:  {args.plan}")
    print(f"  Output: {args.output}")
    print(f"{'='*60}\n")

    if args.dry_run:
        print("DRY RUN MODE — no files will be written")
        plan_content = args.plan.read_text(encoding="utf-8")
        info = extract_system_info(plan_content)
        print(f"System detected: {info['name']} (type: {info.get('system_type', 'generic')})")
        print(f"Forbidden patterns found: {sum(len(v) for v in info['forbidden_patterns'].values())}")
        print(f"Hardware limits: {info['hardware_limits']}")
        return 0

    if args.validate_only:
        print("VALIDATE ONLY MODE")
        issues = validate_output(args.output)
        if issues["errors"]:
            for e in issues["errors"]:
                print(f"ERROR: {e}")
            return 1
        for w in issues["warnings"]:
            print(f"WARNING: {w}")
        print("Validation complete")
        return 0

    # PHASE 0: Setup
    print("PHASE 0: Setting up directory structure...")
    create_directory_structure(args.output)

    # PHASE 0: Analysis
    print("\nPHASE 0: Analyzing plan.md...")
    analysis = generate_analysis_report(args.plan, args.output)
    system_name = analysis["system"]["name"]

    # PHASE 7: CI/CD
    print("\nPHASE 7: Generating CI/CD configs...")
    generate_ci_yml(args.output, system_name)
    generate_nightly_yml(args.output)

    # PHASE 6: Memory placeholders
    print("\nPHASE 6: Generating memory file placeholders...")
    generate_promotion_history(args.output, analysis["system"])

    # PHASE 8: Validation
    print("\nPHASE 8: Validating output...")
    issues = validate_output(args.output)

    # Generate summary
    generate_summary(args.output, issues)

    print(f"\n{'='*60}")
    print(f"  Generation complete!")
    print(f"  Output: {args.output}/")
    print(f"")
    print(f"  NEXT: Open the output directory in Claude or Copilot")
    print(f"  and run the plan-to-system agent on each phase to")
    print(f"  generate the full documentation content.")
    print(f"{'='*60}\n")

    return 1 if issues["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
