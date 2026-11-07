# Sponsor Desk

Sponsor Desk is a two-agent Switch room that turns an event brief into sourced sponsor candidates and an unsent exploratory pitch. Sourcer gathers dated receipts and records human shortlist decisions; Outreach prepares a role-addressed draft for review. Humans steer the work in the same thread, and every pitch stays unsent.

## The two-minute demo

Video: **not recorded — add the final hosted recording URL here before submission.**
[Exact camera script](docs/demo-script.md) · [Architecture](docs/architecture.md)

**Verified:** credential-free contract rehearsal, both actual Claude CLI fixture
instruction responses, installed Switch template lint (no findings), and CI. **Deployed:** the two agents and `demo-sponsor-desk` Discord room; both report live.
**Pending:** kickoff reply verification, actual room handoff/persistence and authenticated live MCP flow. The receipt
facts are public CNCF sponsor listings inspected on Nov 7, 2026; cached candidate
and pitch outputs are authored demo fixtures, not exported Argus responses. The event
is fictional. See [provenance](fixtures/cached/PROVENANCE.md) and [readiness](docs/READINESS.md).

## Why Switch is essential

The room gives both agents the same confirmed brief, the organizer’s corrections,
and the exact human selection. Sourcer addresses Outreach by name in the original
thread; Outreach binds its draft review to that thread and the human message.
Without Switch, shared human identity, addressed delivery, context and durable room
records would need another collaboration layer. Argus research itself works independently.
The local rehearsal checks the contract; it does not demonstrate these Switch capabilities.

Rules are room instructions plus an attached Rules document. Current Switch protocol
docs mark native Task operations not ready. Outreach therefore creates immutable
Task/Decision **room documents**, not native Tasks or a native Decisions feature.
Only the creating agent can update its document; immutable records avoid cross-agent
ownership conflicts. Room review never changes a backend claim-approval state.

## Reproduce

1. Clone this public integration and install its one Python dependency:
   ```bash
   git clone https://github.com/Jsjk112344/sponsor-desk.git
   cd sponsor-desk
   python3 -m venv .venv
   .venv/bin/pip install -r requirements.txt
   ```
2. Run the credential-free checks. Python 3.9+ is required; no Docker, model or MCP
   credentials are needed for fixture rehearsal. Setup reports missing live prerequisites.
   ```bash
   SPONSOR_DESK_FIXTURES=1 bash scripts/setup.sh
   SPONSOR_DESK_FIXTURES=1 bash scripts/smoke.sh
   cat .local/transcript.txt
   ```
   Expect PASS and a transcript: brief → confirm → five receipts → skip/defer/shortlist
   → @handoff → unsent draft → local Task + Decision → send refusal.
3. For an actual room, install [Switch Console](https://github.com/sandbox-quantum/switch/releases/latest),
   open it, start its Docker server and connect Discord (Slack fallback). Link your
   chat identity. Both agents use `owner-agents`, so the linked owner and their agents
   can address them; additional human collaborators need a deliberate addressing change.
   Sign in to the selected Claude/Codex/OpenCode provider in Console.
4. Run setup again with your desired team prefix, for example
   `SPONSOR_DESK_TEAM=demo SPONSOR_DESK_FIXTURES=1 bash scripts/setup.sh`.
   In Console Templates import `sponsor-desk.template.yaml`, choose `team=demo`,
   `provider=claude` (or your installed provider), `location=local`, the **absolute
   directory parameter printed by setup**, and the exact connected `bridge` name.
   Create the template. It requests `demo-sourcer`, `demo-outreach`, `demo-sponsor-desk`
   and the linked creator. Avoid reusing an existing team name. Instructions are
   embedded in the YAML and also present in the staged agent directories.
5. Follow [the exact chat lines](docs/demo-script.md). Fixture agents read `MODE`
   and the staged public fixtures. They use Switch room operations for Task/Decision
   documents; do not mistake local `.local/rehearsal.json` for room persistence.
   Capture real room evidence using [live verification](docs/live-verification.md).
6. For live tools follow [MCP setup](docs/mcp-setup.md); repeat the flow in a new room,
   with fresh human confirmation and no paid research. Never call sends or mailbox setup.
   Reset only local outputs with `bash scripts/demo_reset.sh`. Use a new team prefix
   for a clean room, retaining prior approval history.

Optional actual agent instruction smoke (existing signed-in Claude subscription,
no API keys): `.venv/bin/python scripts/agent_smoke.py`. It disables all tools/MCPs,
feeds the actual instruction files and fixtures, and checks handoff/refusal responses.
It does not prove Switch delivery or MCP saves. CI runs deterministic contract checks;
it cannot reproduce private provider authentication.

## Architecture

Human → Switch room/thread → Sourcer → dated public/Argus evidence → human selection
→ @Outreach → authorized draft save → exact human review → room Task/Decision documents.
See [message sequence and Mermaid diagram](docs/architecture.md) and [PLAN.md](PLAN.md).
No web UI, backend, email transport or paid research client is added.

A policy prompt governs live provider tools; this repository does not claim a sandbox
that can prevent arbitrary tools added by a host administrator. The deterministic
rehearsal has no network or sending implementation. Keep live tool access limited to
the documented research/draft operations.

## Team

Justin ([Jsjk112344](https://github.com/Jsjk112344)); existing Argus/Ducket services
supply research and draft persistence. Claude Code or Codex runs the two roles.
Apollo is excluded from this entry’s setup and verification.

## What’s next

Verify Console import and the live room flow, record the video, and replace pending
checks with observed evidence. Adopt native Tasks when supported. Explore a public
read-only research adapter without exposing proprietary services or licensed records.

## Judging map

| Criterion | Weight supplied in brief | Review artifact |
|---|---:|---|
| Use of Switch | 30% | template, room rules, named handoff, original-thread approval |
| Technical execution/reproducibility | 25% | setup/smoke scripts, CI, fixtures and provenance |
| Creativity/impact | 25% | evidence-to-selection-to-unsent-review loop; no buying-intent claims |
| Presentation | 20% | camera script, architecture, submission/blog/social drafts; video pending |

Track: 01 Best Business Workflow. The [official schedule](https://www.wemakedevs.org/hackathons/switch/schedule)
closed Nov 7, 2026 at 23:59 IST (18:29 UTC). This build began after that deadline;
no on-time submission or eligibility is claimed. Registration and submission remain
manual under the [organizer rules](https://www.wemakedevs.org/hackathons/switch/rules).

Original integration code: MIT. Existing Argus/Source/Sales and Switch predate this
work; only this integration is published. See [third-party references](THIRD_PARTY.md).
