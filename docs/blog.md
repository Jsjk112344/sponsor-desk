# Draft: Why a sponsor shortlist needs a shared room

A sponsor researcher’s useful output is not a list of brands. It is a decision the
organizer can inspect: what was observed, what remains uncertain, why this candidate
might fit, and what the team has actually approved next.

Sponsor Desk puts those transitions into a Switch room. Sourcer works from a
human-confirmed event brief, returns dated receipts, and records explicit shortlist,
defer, and skip decisions. Outreach receives a named, same-thread handoff and
prepares a role-addressed exploratory pitch. The room’s review record binds an
exact draft version. Every pitch remains unsent.

The first design correction came from reading the actual interfaces. Switch’s
current protocol documents native Tasks as not ready for use. The integration uses
immutable room documents for Tasks and Decisions, and says so. A second correction
came from Argus Sales: its internal prospecting workflow targets organizer accounts.
A sponsor brand must not be misrepresented as an organizer to satisfy a tool schema.
Source’s sponsor-company outreach-save path is the intended draft adapter instead.

The reproducible part begins with five public Gold sponsor listings from CNCF’s
KubeCon India 2025 transparency report. Those facts are dated observations, not
proof of current budget or intent. The proposed Singapore event is fictional. Its
pitch and fit explanations are authored cached material, not live Argus exports.
This keeps private records and paid research outside the public rehearsal.

The deterministic smoke test checks more than a happy-path transcript. It rejects
agent-authored approval, the wrong thread, stale draft versions, outdated briefs,
and drafting after a skip. Stable operation IDs detect conflicting retries. There
is no network or send implementation in the rehearsal. Live provider instructions
also refuse sending, but a prompt alone is not a server authorization boundary;
operators must limit the tools they attach to that host.

Switch’s proposed contribution is concrete: the agents and organizer share the
confirmed brief, see corrections where work happens, address each other by name,
and retain review context for someone joining later. The local rehearsal cannot
prove those room properties. The repository leaves Console import, live room
execution, actual MCP persistence, and the recorded demo pending until observed.

This draft describes a build in progress, not a submitted or winning entry. The
published event deadline passed before this session began. The next evidence must
come from the actual room and authorized host, with screenshots labeled by mode.

References: [Switch protocol](https://docs.switchagents.ai/llms.txt),
[CNCF report](https://www.cncf.io/wp-content/uploads/2025/09/KubeCon_India25_TransparencyReport.pdf),
[code and verification status](https://github.com/Jsjk112344/sponsor-desk).
