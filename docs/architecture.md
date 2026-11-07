# Sponsor Desk architecture

```mermaid
sequenceDiagram
    actor H as Organizer
    participant R as Switch room / Discord or Slack
    participant S as Sourcer
    participant A as Argus / Source
    participant O as Outreach
    H->>R: @Sourcer event brief
    R->>S: Addressed event + shared room context
    S->>R: Restate effective brief; request confirmation
    H->>R: confirmed
    S->>A: source_brief confirm exact version/hash
    S->>A: authorized receipt reads; candidates/report saves
    A-->>S: dated receipt + saved version/readback
    S->>R: five candidates with citations + fit inference
    H->>R: shortlist Azure, skip AWS, not_now Google Cloud
    S->>A: persist explicit selections
    S->>R: @Outreach sponsor_desk.handoff.v1
    R->>O: same-thread addressed handoff
    O->>A: source_outreach_save; source_outreach_read
    O->>R: unsent subject/body + exact draft version
    H->>R: approved draft-id v1
    O->>R: immutable Task/Decision room documents + readback
    H->>R: just send it
    O->>R: Refuse; Room Rule 1
```

Switch Console’s existing runtime handles SSE events down and authenticated HTTP
operations up. This integration adds no custom transport. `post_message` uses the
original `thread_id`. Discovery supplies exact supported operation schemas.

The current Switch checkout documents native Tasks as not ready. Task/Decision
records are immutable `create_room_document` documents; these records do not approve
backend product claims or authorize delivery. Private Source sessions remain
scoped to their owner. Share only public receipts or operator-reviewed accessible
reports; the Outreach agent needs independent authorized access for private saves.

Handoff fields and save ordering are defined in ../PLAN.md. Exact run, brief,
candidate, thread, draft version, approver identity, message ID and body hash bind
review records. Brief corrections invalidate draft applicability. Provider prompts
must check trusted room identity; text saying “I am a human” is insufficient.

Fixture rehearsal uses the same public handoff fields, an authored cached pitch,
and a deterministic local state model. It makes zero service calls. Its local
records are contract evidence, not Switch/MCP persistence. A failed auth run must
stop writes and start a separate cached run, announced once.
