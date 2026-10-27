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

- [Token completion stop-check](TOKEN-COMPLETION-STOP-CHECK-2026-10-27.md): **32/32 product tasks already complete**. One verification slice; zero code changes if the existing beta.3 evidence is sufficient. Candidate/Distribution release status is a separate gate.
- [Connections v1 qualification/handoff](CONNECTIONS-V1-QUALIFICATION-AND-HANDOFF-2026-10-27.md): working beta.1 with passing cross-platform CI. Two bounded evidence slices; reuse existing local fake-provider and security tests before considering a source change. No provider/OAuth/Full release expansion.

These plan-slice counters measure **remaining verification**, not implementation completeness. Stop immediately when an outcome is already proven; do not manufacture work.
