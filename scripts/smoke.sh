#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
if [[ "${SPONSOR_DESK_FIXTURES:-1}" != 1 ]]; then
  echo 'Live verification requires Console and authorized MCP access; follow docs/live-verification.md. No live pass claimed.' >&2
  exit 2
fi
"$ROOT/.venv/bin/python" "$ROOT/scripts/check_contract.py"
"$ROOT/.venv/bin/python" "$ROOT/scripts/desk.py" --output "$ROOT/.local/rehearsal.json" > "$ROOT/.local-transcript.tmp"
mkdir -p "$ROOT/.local"
mv "$ROOT/.local-transcript.tmp" "$ROOT/.local/transcript.txt"
echo 'PASS local fixture contract rehearsal; transcript: .local/transcript.txt'
echo 'NOT VERIFIED: actual agent replies, Switch template import, room persistence, live MCPs'
