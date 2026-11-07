# Sponsor Desk implementation contract

Baseline: Argus/Source/Sales predate this work. No private code or data is copied.
Read sibling argus-switch-entry, Ducket MCP/schema guides and Proofdesk demo format.
Switch inspected at 38b2c83b58387b29dcc532ae52acf48ee720870e; SSE down, HTTP up.
Official deadline Nov 7 18:29 UTC passed before this session; no timely submission claim.

## Message and save sequence
1. Human addresses `{team}-sourcer` with fixture brief. Sourcer restates it once,
   calls source_capabilities, source_create, source_brief (save only), asks confirm.
2. Human says `confirmed`. Confirm exact brief version/hash via source_brief.
   Argus read tools return dated receipts; no paid source_tool searches.
   source_candidates and source_report_save persist supported research. Read back.
3. Sourcer posts five sourced candidates. Human says `shortlist Microsoft Azure,
   skip AWS, not_now Google Cloud`. Save only those explicit choices. Shortlist
   enables drafting; not_now defers; skip excludes. None authorizes sending.
   All choices persist as Selection room documents; only explicit shortlists use
   source_workspace_save_batch. source_workspace_save has no selection enum.
4. Sourcer @mentions Outreach in the same thread with public handoff v1 below.
5. Outreach reads sales_playbook + sales_accounts. Internal sales is designed for
   organizer accounts: never force sponsor brands into that schema. Prefer
   source_outreach_save for sponsor-company drafts; sales_draft_save only if the
   live playbook permits that account type. Read back exact saved version.
6. Human says `approved <draft_id> v<version>` in the same thread. Outreach verifies
   sender is a room human and version current, then creates immutable room docs
   `Task-<draft>-vN` and `Decision-<message-id>` with exact approver/message reference.
   Approval is room review only; never invoke service approval or claim approval.
7. Human says `just send it`. Refuse: Room Rule 1 forbids sends/scheduling/mailboxes.

## Handoff v1
`type=sponsor_desk.handoff.v1`, run_id, thread_id, brief_version, candidate_id,
company, domain, decision=shortlist, receipts[{event,edition,tier,source_url,
observed_at}], fit_inference, gaps, report_ref, idempotency_key.
Only publicly redistributable receipts cross agents; private sessions stay private.
Draft binds run/candidate/brief/version; revision clears approval. Retry identical
operation keys and bodies; reread revisions on conflicts. No blind retries.

## Verification and fallbacks
Credential-free local state machine is a contract rehearsal, not an agent/Switch run.
CLI smoke independently exercises both actual instruction files when authorized host
usage is available. Console template/bridge, live MCP saves and screenshots need
actual access and stay unchecked until observed. Task ops are documented not ready;
use immutable room documents through create_room_document (not native Tasks).
Auth failure: announce cached once, use public receipt fixtures with provenance;
never mix cached and live records in one run. No web UI or backend.
