#!/usr/bin/env bash
# Checklist-only for account prerequisites; never installs apps or calls paid tools.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TEAM="${SPONSOR_DESK_TEAM:-demo}"
AGENT_ROOT="${SPONSOR_DESK_AGENT_ROOT:-$ROOT/.local/agents}"
[[ "$TEAM" =~ ^[a-z][a-z0-9-]*$ ]] || { echo 'Invalid team name'; exit 1; }
PY="$ROOT/.venv/bin/python"
if [[ ! -x "$PY" ]]; then
  echo 'MISSING Python environment: python3 -m venv .venv; .venv/bin/pip install -r requirements.txt'
  exit 1
fi
"$PY" "$ROOT/scripts/check_contract.py"
for tool in docker claude codex; do
  if command -v "$tool" >/dev/null 2>&1; then echo "FOUND $tool"; else echo "MISSING $tool"; fi
done
if command -v docker >/dev/null 2>&1 && docker info >/dev/null 2>&1; then echo 'READY Docker daemon'; else echo 'MISSING running Docker daemon'; fi
if [[ -d '/Applications/Switch Console.app' || -d '/Applications/Switch.app' ]]; then echo 'FOUND Switch Console'; else echo 'CHECK Switch Console installation (custom paths need manual check)'; fi
if [[ -n "${SWITCH_BRIDGE_URL:-}" ]]; then
  if curl --fail --silent --max-time 3 "${SWITCH_BRIDGE_URL%/}/health" >/dev/null; then echo 'READY Switch health (does not prove bridge or room access)'; else echo 'MISSING Switch health'; fi
else echo 'MISSING SWITCH_BRIDGE_URL for public /health probe'; fi
for key in ARGUS_SOURCE_MCP_URL ARGUS_SOURCE_TOKEN DUCKET_ARGUS_MCP_URL DUCKET_API_KEY ARGUS_SALES_MCP_URL ARGUS_SALES_TOKEN; do
  if [[ -n "${!key:-}" ]]; then echo "SET $key (not authentication proof)"; else echo "MISSING $key (or configure host OAuth)"; fi
done
for role in sourcer outreach; do
  dest="$AGENT_ROOT/$TEAM-$role"
  mkdir -p "$dest/room" "$dest/fixtures"
  cp "$ROOT/agents/$role/INSTRUCTIONS.md" "$ROOT/agents/$role/AGENTS.md" "$ROOT/agents/$role/CLAUDE.md" "$dest/"
  cp "$ROOT/room/RULES.md" "$dest/room/"
  cp -R "$ROOT/fixtures/." "$dest/fixtures/"
  # Fixture runs must not initiate MCP authentication or accidentally use live tools.
  if [[ "${SPONSOR_DESK_FIXTURES:-1}" == 1 ]]; then
    printf 'fixture\n' > "$dest/MODE"
  else
    printf 'live\n' > "$dest/MODE"
    cp "$ROOT/agents/$role/.mcp.json" "$dest/.mcp.json.example"
    echo "LIVE $role: configure host OAuth/MCP explicitly; .mcp.json.example is not activated"
  fi
done
printf 'Template directory parameter: %s\nTeam parameter: %s\n' "$AGENT_ROOT" "$TEAM"
echo 'CHECK provider sign-in, connected Discord/Slack bridge name and linked owner in Console'
echo 'CHECK import sponsor-desk.template.yaml; directory must match above; select bridge; create'
