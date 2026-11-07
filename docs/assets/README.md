# Evidence assets
No real room screenshots have been captured yet. Do not substitute mock chat images
or a PDF screenshot for a verified room run. Credential-free smoke writes its actual
transcript to .local/transcript.txt and CI uploads it as an artifact.

Actual text evidence from the final instruction revision:
- claude-sourcer-fixture.txt — Claude CLI response with all tools/MCP disabled.
- claude-outreach-fixture.txt — Claude CLI response with all tools/MCP disabled.
- contract-rehearsal.txt — deterministic local contract run.

These are text transcripts, not room screenshots. Human messages supplied by the
agent conformance harness are simulated fixture inputs, not live room approvals.
The roles correctly mark service saves and room-document operations pending.
