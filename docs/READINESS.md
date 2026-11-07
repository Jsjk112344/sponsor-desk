# Observed readiness

Evidence date: November 7, 2026. Public repo:
https://github.com/Jsjk112344/sponsor-desk

- [x] Original integration published with MIT license and no proprietary code/data.
- [x] GitHub Actions fixture contract job passes.
- [x] README credential-free instructions executed from public clean clone at
  /tmp/sponsor-desk-clean, using Python 3.9.6 and PyYAML 6.0.3. Setup, smoke,
  reset, repeated setup and repeated smoke pass. CI uses Python 3.12.
- [x] Five real public Gold-tier listings visually checked against CNCF India 2025
  report page 12. Receipt inspection timestamps are explicit; current fit is inference.
- [x] Fixture model covers brief, confirmation, candidates, defer/skip/shortlist,
  @handoff, full unsent draft, local review records and never-send refusal.
- [x] Negative contract tests reject nonhuman approval, wrong thread/version,
  stale brief, conflicting retries and drafting/approval after skip.
- [x] Both actual Claude CLI roles return fixture responses with the handoff,
  five receipts, role-addressed pitch and Rule 1 refusal. Tools/MCP disabled;
  this demonstrates instruction behavior, not room integration or service writes.
  Actual sanitized text responses are retained in docs/assets.
- [x] Installed Switch server 0.31.0 template lint returns no errors or warnings.
  Reference checkout: 38b2c83b58387b29dcc532ae52acf48ee720870e.
- [x] Switch Console installed/open; local API /health returns 200 at port 50218.
  This installation uses native local services; Docker daemon is also available.
  Global Claude and Codex MCP configuration contain no configured servers.
- [x] Claude and Codex report signed-in state. No API key or paid fallback used.
- [x] Camera script, 100-/500-word submission copy, blog and #HowISwitch drafts written.
- [ ] Template imported/run in Console; expected agents and room observed.
- [x] Discord bridge verified through authenticated Switch API: exact display name
  `Discord`, type `discord`, status `active`, channel creation enabled.
  The current Switch account has a linked Discord identity. Use `bridge=Discord`.
- [ ] Actual fixture room sequence, Selection/Task/Decision documents and readbacks observed.
- [ ] Authenticated live Source/Argus/Sales calls from the actual Switch host verified.
- [ ] Live flow and real room screenshots captured under docs/assets.
- [ ] Recorded video hosted and README link replaced.
- [ ] Manual submission receipt obtained. Published deadline passed before session start.

## Remaining owner dependencies

Discord connection and owner identity are verified.
Complete provider-side Source/corpus/Sales authorization with the required grants;
web connector consent alone does not establish CLI access. Apollo stays excluded.
Record and host the actual demo, and handle any organizer communication/submission
manually. Do not publish private licensed receipts or credentials in evidence.

## Scope of the fallback

Room Rules are instructions plus a document. Task/Decision records are immutable
room documents, not native Switch Tasks. Fixture outputs are authored demo data
using public receipt facts, not cached private MCP responses. The local contract
state machine has no network or send path. Live host policy is instructed, not a
new server-side authorization implementation. No complete live-integration claim.
