# Safe Infrastructure Slice 2.3 - Convergence, Restore, Doctor and Member UX Invariants

**Status:** IN PROGRESS  
**Slice:** 2.3 - Define convergence, restore, doctor and member UX invariants  
**Started:** 2026-10-12

## Exact starting refs

- `aiverse-filmmakers/AI-Verse-System@e70a61c5fc9423ac2a5b5569f5829134c1e50f82`
- `aiverse-filmmakers/ai-verse-distribution@90f175418f8d13faeece8bcb1ad0796d2adecfb1`

## Current implementation evidence reused

Distribution already provides a reusable doctor aggregation substrate:

- `Orchestrator.doctor()` invokes owner doctor surfaces independently;
- owner failures are recorded per component rather than silently converted to PASS;
- safe remaining owner checks continue after an isolated failure;
- the OS composed-system doctor is run when present;
- aggregate `ok` is true only when all included required checks pass;
- the result retains machine-readable component/system evidence.

Distribution CLI already separates default human output from `--json` evidence output, but the current generic default doctor formatter still exposes component IDs and implementation-oriented details. Final plain-English traffic-light UX remains Phase 4 work.

Slice 2.1 already froze whole-install Last-Known-Good and restore semantics. Slice 2.2 already froze owner-published structural generations and upgrade recipes. The canonical Identity contract remains `ai-verse.durable-identity-reference/v1`.

## Classification

- existing Distribution doctor fan-out/aggregation: **REUSE**;
- current generic non-JSON CLI formatter for final doctor/upgrade/restore UX: **EXTEND later**, not implemented in this slice;
- convergence/restore/doctor/UX qualification invariants: **CREATE as canonical System contract**;
- machine-readable cross-invariant qualification evidence envelope: **CREATE minimally for later Phase 5 proof**;
- owner-specific migration/restore engines and Phase 4 member-facing implementation: **DEFER**;
- canonical Identity contract and infrastructure-upgrade contract: **IMPORT/REUSE**.

## Derived task list

- [x] **2.3-T1** Refresh System/Distribution refs and inspect current doctor aggregation, CLI evidence separation, completed restore law and completed upgrade-recipe law.
- [ ] **2.3-T2** Define the convergence invariant so fresh-current and historically-upgraded installations can be compared at the target contract level without requiring byte-for-byte equality of legitimate user-owned state.
- [ ] **2.3-T3** Define the restore invariant so covered state/reconstructed software exactness, exclusions and retained-target safety are machine-testable.
- [ ] **2.3-T4** Define the doctor invariant so owner fan-out, aggregate truth and isolated-failure behavior are machine-testable without Distribution duplicating owner domain logic.
- [ ] **2.3-T5** Define the member UX invariant plus a minimal machine-readable qualification evidence envelope that keeps technical evidence available while forbidding internal jargon in default member summaries.
- [ ] **2.3-T6** Add focused schema/validator/examples/tests, run exact-ref System Contract Validation, update the canonical roadmap, and close Slice 2.3 only if every acceptance criterion passes.

## Protected constraints

- Structural equivalence means equality against the target release's package-owned/generated/migratable contracts, not deletion or normalization of legitimate user-owned/custom state.
- Owner-defined durable identity/history/preservation guarantees must survive admitted upgrade according to `ai-verse.durable-identity-reference/v1`.
- Restore exactness is limited to the declared local recovery scope. External systems and excluded state are never claimed restored.
- Reconstructed software must resolve to the exact retained admitted release/revisions.
- Doctor is one member command backed by owner truth. Distribution aggregates; it does not reimplement owner health semantics.
- One owner doctor failure prevents false whole-system PASS but does not automatically suppress unrelated safe read-only owner checks.
- Default member summaries must not require repository paths, generations, IDs, SHAs, migration recipe IDs or component-owner jargon.
- Machine-readable details remain available for qualification/support.
- This slice defines testable contracts only. It does not implement the Phase 4 restore engine, upgrade orchestrator or final UX formatter.

## NEXT

Implement 2.3-T2 through 2.3-T5, validate, then close Slice 2.3 in the canonical roadmap. Do not start Phase 3 in this execution unit.