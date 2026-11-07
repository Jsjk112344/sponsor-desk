# Live MCP setup

Do not paste secrets into chat, git, a template, or screenshots. `.env.example`
is a variable inventory; setup neither sources it nor injects credentials into Console.
In a trusted shell export needed values yourself, or use the provider’s supported
OAuth configuration. OS desktop apps do not necessarily inherit shell exports.

| Role | Server | Required access |
|---|---|---|
| Sourcer | ARGUS_SOURCE_MCP_URL (current default https://api.ducket.io/source-mcp) | ARGUS_SOURCE_TOKEN: source:read, source:write; no paid tool use |
| Sourcer | DUCKET_ARGUS_MCP_URL (https://api.ducket.io/mcp) | DUCKET_API_KEY: existing licensed argus:read access |
| Outreach | ARGUS_SOURCE_MCP_URL | independently authorized Source read/write for sponsor-company drafts |
| Outreach | ARGUS_SALES_MCP_URL (documented https://mcp.ducket.io/sales-mcp) | ARGUS_SALES_TOKEN: restricted internal staff sales:read/write grant |

These URL defaults come from local Ducket docs, which disagree on older Source
aliases. Use the URL shown by your actual connection page. Credentials that work
in a web connector do not prove access inside a Switch-launched CLI.

1. Start a fresh live team with `SPONSOR_DESK_FIXTURES=0 bash scripts/setup.sh`.
   Setup stages `.mcp.json.example` but deliberately does not activate remote tools.
2. For Claude Code, configure these HTTP MCP servers in that agent’s project using
   the provider’s supported OAuth login, or copy the example to `.mcp.json` after
   securely exporting private terminal keys in the process that launches the provider.
   Verify `${ENV_VAR}` interpolation is supported by the installed host version.
   Never interpolate real keys into tracked files. For Codex/OpenCode use their native
   MCP config; `.mcp.json` is a Claude config, not portable configuration for all CLIs.
3. Authenticate Source and Ducket Argus separately. Source read/write does not grant
   licensed corpus access, paid supplier authority, sharing rights or report access.
   Sales additionally requires current Ducket staff membership and explicit staff grants.
4. Discover current tools/schemas. Successful `source_capabilities`, an authorized
   bounded Argus read, and `sales_playbook` + `sales_accounts` establish access only
   for that host/principal. tools/list or OAuth consent alone is insufficient.
5. Use `source_outreach_save` + `source_outreach_read` for a sponsor brand. Current
   internal Sales guidance targets organizer accounts, so only use `sales_draft_save`
   when the discovered playbook actually permits that account and the owner has access.
   Do not manufacture an organizer record for Azure to make a demo pass.

No Apollo setup is included. No contact reveal, research purchase, mailbox connection,
sequence enrollment, sends or backend approvals are allowed. Authentication failure
starts a separate labeled cached run; never claim its local files are service saves.
