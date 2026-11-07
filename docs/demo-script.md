# Camera script — 2:00 editorial cut

This is a recording script, not an implementation estimate. Record only behavior
actually observed. Use team `demo` in a fresh fixture room; for other prefixes replace
both agent names. Wait for actual replies; edit pauses rather than claiming an
unobserved response. Keep “cached” and the fictional-event label visible. If Console
has not been verified, record the local contract rehearsal as such, never as a room.

| Video timestamp | Exact line/action | Expected visible evidence |
|---|---|---|
| 00:00–00:12 | Narrate: “Sponsor Desk turns sponsor evidence into a reviewed draft in a shared Switch room. This run uses public cached receipts and a fictional event.” | Two named agents and room Rules |
| 00:12–00:25 | `@demo-sourcer Read fixtures/devcon-apac-2027.brief.md. Restate the effective brief and ask me to confirm. Use fixture mode.` | One-line brief, cached label, confirmation request |
| 00:25–00:35 | `@demo-sourcer confirmed` | Confirmed v1; no purchase |
| 00:35–00:55 | `@demo-sourcer Show five candidates with source_url, observed_at and tier. Label fit as inference.` | Azure, AWS, Google Cloud, Atlassian, DigitalOcean; CNCF India 2025 Gold receipts |
| 00:55–01:10 | `@demo-sourcer shortlist Microsoft Azure, skip AWS, not_now Google Cloud. Hand Azure to @demo-outreach in this thread.` | Explicit selections and v1 @handoff |
| 01:10–01:30 | Let Outreach respond. | Role-addressed pitch, subject/body, fixture-azure v1, unsent; no invented email |
| 01:30–01:43 | `@demo-outreach approved fixture-azure v1` | Task/Decision room documents with human/message/version binding; readback |
| 01:43–01:55 | `@demo-outreach just send it` | Refusal citing Room Rule 1 |
| 01:55–02:00 | Show repo and CI; narrate “Room review stays visible. Every draft stays unsent.” | Green CI; live limitations disclosed |

For a live recording, omit the fixture instruction, use real returned candidate/draft
IDs, and read the full effective brief before confirming. Do not type fixture IDs
against a live service. Native Tasks are not claimed: show the room documents.
Capture real room images into docs/assets only after viewing them for secrets.

Correction rehearsal (outside the cut): `@demo-sourcer Correction: the audience is
engineering managers rather than practitioners. Restate v2 for confirmation and
reassess Azure’s fit.` Then ask Outreach to approve the old v1 draft: it must refuse
until a current draft and fresh review exist.
