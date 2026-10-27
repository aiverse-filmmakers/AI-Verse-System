# In-progress implementation plans

Put plans here when they are ready for implementation or actively being implemented.

Each plan should state:

- status and date;
- problem and fixed destination;
- permanent laws/non-negotiables;
- current-state evidence;
- affected repositories and canonical owners;
- phases;
- slices with acceptance criteria;
- adaptive task list for the current slice;
- required validation/evidence;
- blockers, drift, and plan amendments;
- next slice.

When implementation and acceptance evidence are complete, move the plan to `../completed/`. If protected direction needs to change, move or copy it to `../blocked/` and record the amendment proposal before continuing.

## New evidence-gated plans (2026-10-27)

- **Token stop-check CLOSED**: [completed 1/1 plan](../completed/TOKEN-COMPLETION-STOP-CHECK-2026-10-27.md). Existing beta.3 was verified with **zero Token code changes**; 32/32 product tasks remain complete. Release admission remains a separate decision.
- **Connections V1 qualification CLOSED**: [completed 2/2 plan](../completed/CONNECTIONS-V1-QUALIFICATION-AND-HANDOFF-2026-10-27.md). A single reproduced missing-capability-grant bypass was fixed in [owner PR #14](https://github.com/aiverse-filmmakers/AI-Verse-Connections/pull/14) with 6/6 final CI; [Dashboard consumption boundary](https://github.com/aiverse-filmmakers/AI-Verse-Connections/blob/main/docs/DASHBOARD-CONSUMPTION-HANDOFF-2026-10-27.md) documents existing local service methods. No provider features, new host API or member Full release.

These plan-slice counters measure **remaining verification**, not implementation completeness. Stop immediately when an outcome is already proven; do not manufacture work.

## Dashboard Personal-first amendment

- [Personal-first Dashboard delivery and guided connections](DASHBOARD-PERSONAL-FIRST-HANDOFF-2026-10-27.md): System coordination summary linking the detailed Dashboard plan and provider UX handoff in [Dashboard draft PR #41](https://github.com/aiverse-filmmakers/AI-Verse-Dashboard/pull/41). Preserves 15 accepted baseline points; future gates/scope require reconciliation. Token and Connections closeouts remain complete; no new member release or executable integration is claimed.
