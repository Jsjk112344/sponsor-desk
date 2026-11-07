#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
# Exact known local files only. Never deletes room/server data or unknown paths.
rm -f "$ROOT/.local/rehearsal.json" "$ROOT/.local/transcript.txt"
echo 'Local rehearsal reset. For Switch create a fresh team name and rerun setup.'
echo 'Keep prior room approvals as audit history; this script does not clear Switch.'
