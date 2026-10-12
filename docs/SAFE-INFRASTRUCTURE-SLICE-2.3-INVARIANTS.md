# Safe Infrastructure Slice 2.3 - Convergence, Restore, Doctor and Member UX Invariants

**Status:** COMPLETE  
**Slice:** 2.3 - Define convergence, restore, doctor and member UX invariants  
**Started:** 2026-10-12  
**Completed:** 2026-10-12

## Exact starting refs

- `aiverse-filmmakers/AI-Verse-System@e70a61c5fc9423ac2a5b5569f5829134c1e50f82`
- `aiverse-filmmakers/ai-verse-distribution@90f175418f8d13faeece8bcb1ad0796d2adecfb1`

Slice-start record:

- `aiverse-filmmakers/AI-Verse-System@6d9f976d9776d44f0b0c8b58656e759563809ebc`

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

## Final derived task list

- [x] **2.3-T1** Refresh System/Distribution refs and inspect current doctor aggregation, CLI evidence separation, completed restore law and completed upgrade-recipe law.
- [x] **2.3-T2** Define the convergence invariant so fresh-current and historically-upgraded installations can be compared at the target contract level without requiring byte-for-byte equality of legitimate user-owned state.
- [x] **2.3-T3** Define the restore invariant so covered state/reconstructed software exactness, exclusions and retained-target safety are machine-testable.
- [x] **2.3-T4** Define the doctor invariant so owner fan-out, aggregate truth and isolated-failure behavior are machine-testable without Distribution duplicating owner domain logic.
- [x] **2.3-T5** Define the member UX invariant plus a minimal machine-readable qualification evidence envelope that keeps technical evidence available while forbidding internal jargon in default member summaries.
- [x] **2.3-T6** Add focused schema/validator/examples/tests, run exact-ref System Contract Validation, update the canonical roadmap, and close Slice 2.3 only after every acceptance criterion passes.

## Canonical qualification contract

Created:

- `docs/SAFE-INFRASTRUCTURE-QUALIFICATION-INVARIANTS-CONTRACT.md`
- contract ID: `ai-verse.safe-infrastructure-qualification/v1`
- contract commit: `aiverse-filmmakers/AI-Verse-System@5a525520931de03d9fd4255ffd4ddd172a7c589f`

The contract imports rather than redefines:

- `ai-verse.durable-identity-reference/v1`;
- `ai-verse.infrastructure-upgrade/v1`;
- the Slice 2.1 whole-install Last-Known-Good/restore law.

## Convergence invariant

A fresh installation and a historically upgraded installation qualify as converged only when both are bound to the same exact admitted target release and satisfy the same target owner architecture/postcondition checks for package-owned/generated/migratable infrastructure.

Convergence is **not** whole-directory byte equality.

Legitimate user-owned/custom state, history and durable identities remain preserved rather than normalized away. Cache/rebuildable-runtime differences do not by themselves fail convergence when their canonical owners classify them as derived state.

Unsupported or ambiguous state must fail closed rather than being guessed into the target architecture.

## Restore invariant

A successful restore qualifies only when the declared covered local scope matches or reproducibly represents the retained Last-Known-Good point:

- `CAPTURE` state is byte-exact or owner-verified equivalent canonical state;
- `RECONSTRUCT` material resolves to exact immutable retained release/revision/digest evidence;
- `REBUILD` material is rebuilt only where owner-declared derived/disposable and postconditions pass;
- `EXTERNAL/EXCLUDED` state remains truthfully excluded;
- the retained target survives until restore verification succeeds;
- durable identity/reference guarantees pass again after restore.

The contract cannot report remote/external effects as restored merely because local restore succeeded.

## Doctor invariant

The canonical member command remains:

```text
aiverse doctor
```

Qualification requires:

- every required owner check runs or is explicitly not applicable;
- each owner result remains independently identifiable in machine evidence;
- a required owner failure prevents whole-system PASS;
- unrelated safe read-only checks continue after isolated failure unless a declared dependency blocks them;
- composed-system evidence supplements rather than replaces required owner checks;
- doctor remains read-only;
- the member does not need component ownership knowledge.

Injected-failure proof is mandatory for final qualification.

## Member UX invariant

Default doctor/upgrade/restore output must be plain English, compact and practical. It must not require repository names, filesystem paths, Git SHAs, release-set IDs, infrastructure generations, migration recipe IDs, owner IDs or component-internal jargon.

Read-only previews must make it clear that nothing has changed yet.

Detailed machine evidence remains separately available through JSON/details mode. Human simplicity never replaces qualification evidence.

## Machine-readable qualification envelope

Created:

- `contracts/safe-infrastructure-qualification-v1.schema.json`
- schema commit: `aiverse-filmmakers/AI-Verse-System@993d2878e1671ef829b4ad94282c31c6dd4ae5d8`

The envelope has four independent required sections:

- `convergence`;
- `restore`;
- `doctor`;
- `member_ux`.

A whole qualification may report `PASS` only when every required section is `PASS` and the validator's cross-field rules pass.

## Deterministic validation

Validator:

- `scripts/validate_safe_infrastructure_qualification.py`
- validator commit: `aiverse-filmmakers/AI-Verse-System@56d42ca9e52d67f4f448082422928dbcbefef0a5`

The validator rejects, among other unsafe claims:

- overall PASS when any section is not PASS;
- convergence PASS without exact target equivalence, user-state preservation or identity/reference proof;
- restore PASS without covered-state exactness, exact software reconstruction, truthful exclusions or retained-target survival;
- PASS sections relying on failed evidence;
- missing or duplicate required doctor owner results;
- doctor PASS hiding a required owner failure;
- injected required-owner failure that still reports aggregate success;
- doctor mutation;
- failure injection that names a non-required owner;
- default member summaries exposing Git SHAs, Workspace paths, release/component IDs, infrastructure-generation jargon or migration-recipe jargon;
- oversized default summaries that exceed the small-screen evidence bound;
- replacement identity or upgrade contracts.

## Example and tests

Positive qualification fixture:

- `contracts/examples/safe-infrastructure-qualification.valid.json`
- fixture commit: `aiverse-filmmakers/AI-Verse-System@f82cd7e9ecdfa40095609e0c87189511c5f95322`

Focused tests:

- `tests/test_safe_infrastructure_qualification.py`
- tested commit: `aiverse-filmmakers/AI-Verse-System@7526d23bcbbc3ca0af7dfdadab927725baf3fdcc`

The tests include destructive-negative cases for false whole-system PASS, restore incompleteness, failed evidence under PASS, missing/duplicate owner results, hidden owner failure, false injected-failure aggregate success, doctor mutation, leaked SHAs/internal paths/jargon and small-screen summary bounds.

The test suite also proves that a truthful failed qualification can be represented as `overall=FAIL` rather than forcing every fixture to pretend success.

## Exact validation evidence

GitHub Actions:

- workflow: `Contract Validation`;
- run ID: `38285001313`;
- exact head SHA: `7526d23bcbbc3ca0af7dfdadab927725baf3fdcc`;
- conclusion: **SUCCESS**;
- Python 3.11 contract tests: **SUCCESS**;
- Python 3.13 contract tests: **SUCCESS**;
- existing component-release/repository-state contract validation: **SUCCESS**;
- live read-only Core repository refresh on Python 3.11: **SUCCESS**.

## Acceptance criteria

- fresh-install versus upgraded-install structural equivalence is testable at the target contract level: **PASS**;
- restore exactness/reproducibility is testable: **PASS**;
- doctor fan-out and aggregation are testable: **PASS**;
- user-facing simplicity does not remove machine-readable evidence: **PASS**;
- member output does not require paths, generations, IDs or migration jargon: **PASS**;
- identity continuity assertions are testable against the canonical Identity Hardening contract: **PASS**;
- no owner migration, restore engine or final Phase 4 UX implementation was prematurely introduced: **PASS**.

## Phase 2 result

Safe Infrastructure Phase 2 now has all three canonical contract layers required before owner migration implementation begins:

1. Slice 2.1: safe update/state preservation, one rotating Last-Known-Good and restore separation;
2. Slice 2.2: versioned owner infrastructure generation/upgrade-recipe contract;
3. Slice 2.3: testable convergence/restore/doctor/member-UX qualification invariants.

No protected-law conflict or directional amendment was required in Slice 2.3.

## NEXT

**STOP after Slice 2.3 for the current one-at-a-time execution request.**

Next execution unit: Phase 3 / Slice 3.1 - Implement OS Workspace generation and evidence-backed structural semantics. Derive that slice's adaptive task list only from fresh refs when it starts.