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

## Authorized OS access and subscription locking (2026-10-28)

- **[Authorized OS Access: Skool Membership and Revocable App Licensing](AUTHORIZED-OS-ACCESS-AND-SKOOL-LICENSING-2026-10-28.md)**: 0/7 fixed slices. Research/feasibility first; no implementation or automatic cancellation claim. Audits real OS/Gateway/Distribution/Dashboard execution bypasses and requires a verified Skool membership-status source or deliberate billing-source decision before commercial launch.

## New evidence-gated plans (2026-10-27)

- **Token stop-check CLOSED**: [completed 1/1 plan](../completed/TOKEN-COMPLETION-STOP-CHECK-2026-10-27.md). Existing beta.3 was verified with **zero Token code changes**; 32/32 product tasks remain complete. Release admission remains a separate decision.
- **Connections V1 qualification CLOSED**: [completed 2/2 plan](../completed/CONNECTIONS-V1-QUALIFICATION-AND-HANDOFF-2026-10-27.md). A single reproduced missing-capability-grant bypass was fixed in [owner PR #14](https://github.com/aiverse-filmmakers/AI-Verse-Connections/pull/14) with 6/6 final CI; [Dashboard consumption boundary](https://github.com/aiverse-filmmakers/AI-Verse-Connections/blob/main/docs/DASHBOARD-CONSUMPTION-HANDOFF-2026-10-27.md) documents existing local service methods. No provider features, new host API or member Full release.

These plan-slice counters measure **remaining verification**, not implementation completeness. Stop immediately when an outcome is already proven; do not manufacture work.

## Guided provider connections follow-up

- [Provider Connections backend plan](GUIDED-PROVIDER-CONNECTIONS-BACKEND-2026-10-27.md): separate new scope from the completed Connections V1 closeout. S1 is a bounded, synthetic provider key-check repair in Connections; S2 is blocked on an authenticated Dashboard host route and ChatGPT route eligibility. No Dashboard parallel edits or release admission.
