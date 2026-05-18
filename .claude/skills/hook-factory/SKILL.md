---
name: hook-factory
description: >
  Generates all safety hooks, enforcement scripts, and hook configuration JSON
  files for a system based on the plan analysis. Hooks enforce forbidden patterns,
  audit tool usage, and prevent architectural drift. Use after SYSTEM_MANIFEST.md
  is complete and all forbidden patterns are identified.
allowed-tools:
  - read
  - edit
  - bash
---

# Hook Factory Skill

## Reference

- Input: `analysis/plan_analysis.json`, `SYSTEM_MANIFEST.md`
- Output: `.github/hooks/` directory structure

## Purpose

Generate the safety enforcement layer: hooks, scripts, and config files that
automatically block forbidden patterns and audit all tool usage.

## Hook Architecture

```text
hooks/
├── {system}-safety.json      ← Main hook config (preToolUse, postToolUse)
├── {system}-guard.json       ← Focused guard configs (optional)
└── scripts/
    ├── safety-check.sh       ← Main safety checker (preToolUse)
    ├── audit-log.sh          ← Audit logger (postToolUse)
    ├── forbidden-pattern.sh  ← Prompt scope guard (userPromptSubmitted)
    ├── {domain}-scan.py      ← Domain-specific Python scanner
    └── smoke-test-hooks.sh   ← Test suite for all hooks
```

## Procedure

### Step 1 — Extract Hook Rules from Analysis

From `plan_analysis.json`, collect:
- All forbidden architecture components
- All forbidden scope items
- All forbidden data operations
- All security prohibitions
- All coding anti-patterns

Map each to hook type:
```
userPromptSubmitted → block prompt-level scope requests
preToolUse         → block code edits with forbidden patterns
postToolUse        → audit all tool usage
```

### Step 2 — Generate Main Hook Config JSON

```json
{
  "version": 1,
  "hooks": {
    "userPromptSubmitted": [
      {
        "type": "command",
        "command": "bash .github/hooks/scripts/forbidden-pattern.sh"
      }
    ],
    "preToolUse": [
      {
        "type": "command",
        "command": "bash .github/hooks/scripts/safety-check.sh"
      }
    ],
    "postToolUse": [
      {
        "type": "command",
        "command": "bash .github/hooks/scripts/audit-log.sh"
      }
    ]
  }
}
```

Save as: `.github/hooks/{system-name}-safety.json`

### Step 3 — Generate safety-check.sh

This is the main preToolUse gate. Customize based on forbidden patterns:

```bash
#!/usr/bin/env bash
# {SYSTEM_NAME} Safety Hook — preToolUse
# Exit 0 = allow
# Exit 1 = deny

set -euo pipefail

INPUT="$(cat 2>/dev/null || true)"

json_get() {
  local filter="$1"
  printf '%s' "$INPUT" | jq -r "$filter // empty" 2>/dev/null || true
}

TOOL="$(json_get '.toolName')"
[[ -z "${TOOL}" ]] && TOOL="$(json_get '.tool')"
FILE_PATH="$(json_get '.path')"
[[ -z "${FILE_PATH}" ]] && FILE_PATH="$(json_get '.input.path')"
CONTENT="$(json_get '.input.content')"
[[ -z "${CONTENT}" ]] && CONTENT="$(json_get '.content')"
COMMAND="$(json_get '.input.command')"

TOOL_LC="$(printf '%s' "${TOOL}" | tr '[:upper:]' '[:lower:]')"

deny() {
  echo "$1" >&2
  exit 1
}

is_edit_tool() {
  [[ "${TOOL_LC}" =~ ^(editfile|createfile|edit|create|write|replace|multiedit)$ ]]
}

# ---- SECTION 1: Protected paths ----
# (Generated from plan.md holdout/immutable paths)
{FOR EACH PROTECTED_PATH IN ANALYSIS}
if [[ "${FILE_PATH}" =~ (^|/)({PROTECTED_PATH})(/|$) ]]; then
  deny "DENIED: {PROTECTED_PATH} is protected and may not be modified."
fi
{END FOR}

# ---- SECTION 2: Architecture prohibitions ----
if is_edit_tool && [[ "${FILE_PATH}" == src/* ]]; then
  {FOR EACH FORBIDDEN_ARCHITECTURE IN ANALYSIS}
  if printf '%s' "${CONTENT}" | grep -qiE '{FORBIDDEN_PATTERN}'; then
    deny "DENIED: {REASON}"
  fi
  {END FOR}
fi

# ---- SECTION 3: Data/causality prohibitions ----
if is_edit_tool && [[ "${FILE_PATH}" == src/{DATA_OR_FEATURE_PATH}/* ]]; then
  {FOR EACH FORBIDDEN_DATA_PATTERN IN ANALYSIS}
  if printf '%s' "${CONTENT}" | grep -qiE '{PATTERN}'; then
    deny "DENIED: {REASON}"
  fi
  {END FOR}
fi

# ---- SECTION 4: Security prohibitions ----
if printf '%s' "${CONTENT}" | grep -qiE '({SECRET_PATTERN_1}|{SECRET_PATTERN_2})'; then
  deny "DENIED: {SECURITY_REASON}"
fi

exit 0
```

### Step 4 — Generate audit-log.sh

Non-blocking audit logger:

```bash
#!/usr/bin/env bash
# {SYSTEM_NAME} Audit Hook — postToolUse
# Non-blocking by design

set -uo pipefail

INPUT="$(cat 2>/dev/null || true)"
TIMESTAMP="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
LOG_DIR=".github/hooks/logs"
LOG_FILE="${LOG_DIR}/audit.jsonl"
mkdir -p "${LOG_DIR}"

json_get() {
  local filter="$1"
  printf '%s' "$INPUT" | jq -r "$filter // empty" 2>/dev/null || true
}

TOOL="$(json_get '.toolName')"
[[ -z "${TOOL}" ]] && TOOL="unknown"
FILE_PATH="$(json_get '.path')"
[[ -z "${FILE_PATH}" ]] && FILE_PATH="$(json_get '.input.path')"
STATUS="$(json_get '.status')"
[[ -z "${STATUS}" ]] && STATUS="unknown"

jq -nc \
  --arg timestamp "${TIMESTAMP}" \
  --arg tool "${TOOL}" \
  --arg path "${FILE_PATH}" \
  --arg status "${STATUS}" \
  '{timestamp: $timestamp, tool: $tool, path: $path, status: $status}' \
  >> "${LOG_FILE}" 2>/dev/null || \
printf '%s | tool=%s | path=%s | status=%s\n' \
  "${TIMESTAMP}" "${TOOL}" "${FILE_PATH}" "${STATUS}" >> "${LOG_FILE}"

exit 0
```

### Step 5 — Generate forbidden-pattern.sh

Prompt-level scope guard:

```bash
#!/usr/bin/env bash
# {SYSTEM_NAME} Prompt Guard — userPromptSubmitted

set -euo pipefail
INPUT="$(cat 2>/dev/null || true)"

json_get() {
  local filter="$1"
  printf '%s' "$INPUT" | jq -r "$filter // empty" 2>/dev/null || true
}

PROMPT_TEXT="$(json_get '.prompt')"
[[ -z "${PROMPT_TEXT}" ]] && PROMPT_TEXT="$(json_get '.input')"
[[ -z "${PROMPT_TEXT}" ]] && exit 0

deny() { echo "$1" >&2; exit 1; }

{FOR EACH FORBIDDEN_ARCHITECTURE IN ANALYSIS}
if printf '%s' "${PROMPT_TEXT}" | grep -qiE '(implement|add|use|switch to|replace with).*(FORBIDDEN_TECH)'; then
  deny "DENIED: {FORBIDDEN_TECH} is forbidden by the manifest. {REASON}"
fi
{END FOR}

{FOR EACH FORBIDDEN_SCOPE IN ANALYSIS}
if printf '%s' "${PROMPT_TEXT}" | grep -qiE '(implement|add|enable|support).*(FORBIDDEN_SCOPE)'; then
  deny "DENIED: {FORBIDDEN_SCOPE} scope is forbidden by the manifest."
fi
{END FOR}

exit 0
```

### Step 6 — Generate Domain-Specific Python Scanners

For each major risk category (e.g., leakage, security), generate a Python scanner:

```python
#!/usr/bin/env python3
"""
{SYSTEM_NAME} {DOMAIN} scanner.
Reads hook payload JSON from stdin.
Exit code: 0 = allow, 1 = deny
"""

from __future__ import annotations
import json
import re
import sys
from typing import Any

EDIT_TOOLS = {"editfile", "createfile", "edit", "create", "write", "replace", "multiedit"}
TARGET_PREFIXES = ({COMMA_SEPARATED_SOURCE_PATHS},)

# Forbidden patterns with messages
PATTERNS = [
  {FOR EACH FORBIDDEN_PATTERN}
  (
    re.compile(r"{REGEX_PATTERN}"),
    "DENIED: {HUMAN_READABLE_MESSAGE}",
  ),
  {END FOR}
]

def _get(payload: dict[str, Any], *keys: str) -> str:
    for key in keys:
        cur: Any = payload
        ok = True
        for part in key.split("."):
            if isinstance(cur, dict) and part in cur:
                cur = cur[part]
            else:
                ok = False
                break
        if ok and isinstance(cur, str) and cur:
            return cur
    return ""

def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0

    tool = _get(payload, "toolName", "tool").lower()
    if tool not in EDIT_TOOLS:
        return 0

    path = _get(payload, "path", "input.path", "filePath")
    content = _get(payload, "input.content", "content", "newString")

    if not path or not any(path.startswith(prefix) for prefix in TARGET_PREFIXES):
        return 0

    for pattern, message in PATTERNS:
        if pattern.search(content):
            print(message, file=sys.stderr)
            return 1

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
```

### Step 7 — Generate smoke-test-hooks.sh

```bash
#!/usr/bin/env bash
# Smoke tests for {SYSTEM_NAME} hook scripts

set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
cd "${ROOT_DIR}"

PASS_COUNT=0; FAIL_COUNT=0

pass() { echo "PASS: $1"; PASS_COUNT=$((PASS_COUNT + 1)); }
fail() { echo "FAIL: $1"; FAIL_COUNT=$((FAIL_COUNT + 1)); }

run_expect_pass() {
  local name="$1"; local cmd="$2"
  if eval "$cmd" >/dev/null 2>&1; then pass "$name"; else fail "$name"; fi
}
run_expect_fail() {
  local name="$1"; local cmd="$2"
  if eval "$cmd" >/dev/null 2>&1; then fail "$name"; else pass "$name"; fi
}

echo "Running hook smoke tests..."

# --- safety-check.sh tests ---
run_expect_pass "safety-check allows benign edit" \
  "printf '{\"toolName\":\"edit\",\"path\":\"src/test.py\",\"input\":{\"content\":\"x = 1\"}}' | bash .github/hooks/scripts/safety-check.sh"

{FOR EACH FORBIDDEN_PATTERN IN ANALYSIS}
run_expect_fail "safety-check blocks {DESCRIPTION}" \
  "printf '{\"toolName\":\"edit\",\"path\":\"{TARGET_PATH}\",\"input\":{\"content\":\"{FORBIDDEN_CODE}\"}}' | bash .github/hooks/scripts/safety-check.sh"
{END FOR}

# --- forbidden-pattern.sh tests ---
run_expect_pass "forbidden-pattern allows benign prompt" \
  "printf '{\"prompt\":\"Improve error handling\"}' | bash .github/hooks/scripts/forbidden-pattern.sh"

{FOR EACH FORBIDDEN_SCOPE IN ANALYSIS}
run_expect_fail "forbidden-pattern blocks {DESCRIPTION}" \
  "printf '{\"prompt\":\"{FORBIDDEN_PROMPT}\"}' | bash .github/hooks/scripts/forbidden-pattern.sh"
{END FOR}

# --- audit-log.sh test ---
rm -f .github/hooks/logs/audit.jsonl || true
run_expect_pass "audit-log writes entry" \
  "printf '{\"toolName\":\"edit\",\"path\":\"src/test.py\",\"status\":\"ok\"}' | bash .github/hooks/scripts/audit-log.sh && test -f .github/hooks/logs/audit.jsonl"

echo ""
echo "Smoke test summary: PASS=${PASS_COUNT} FAIL=${FAIL_COUNT}"
[[ "${FAIL_COUNT}" -gt 0 ]] && exit 1
exit 0
```

### Step 8 — Generate HOOK_TEST_CHECKLIST.md

```markdown
# Hook Test Checklist

## A. safety-check.sh
- [ ] Allows benign edits
{FOR EACH FORBIDDEN_PATTERN}
- [ ] Blocks {description}
{END FOR}

## B. forbidden-pattern.sh
- [ ] Blocks forbidden architecture prompts
- [ ] Blocks forbidden scope prompts
- [ ] Allows benign prompts

## C. Domain-specific scanners
{FOR EACH SCANNER}
- [ ] {scanner_name}: Blocks {forbidden_pattern}
- [ ] {scanner_name}: Allows {safe_pattern}
{END FOR}

## D. audit-log.sh
- [ ] Creates log file
- [ ] Writes structured entries
- [ ] Non-blocking in all cases

## Acceptance Criteria
- Critical prohibitions are blocked deterministically
- Audit log is produced
- False positive rate is acceptable
- Benign changes are not blocked
```

## Output Structure

```
.github/hooks/
├── {system}-safety.json
├── {domain}-guard.json (if applicable)
├── HOOK_TEST_CHECKLIST.md
└── scripts/
    ├── safety-check.sh
    ├── audit-log.sh
    ├── forbidden-pattern.sh
    ├── {domain}-scan.py
    └── smoke-test-hooks.sh
```

## Validation Checklist

- [ ] All forbidden architecture patterns have hook rules
- [ ] All forbidden scope items have prompt guards
- [ ] All security prohibitions have scanners
- [ ] Protected paths are blocked from edits
- [ ] Smoke tests cover all critical blocks
- [ ] Smoke tests verify benign cases pass
- [ ] audit-log.sh is non-blocking
- [ ] All scripts are executable (chmod +x)
