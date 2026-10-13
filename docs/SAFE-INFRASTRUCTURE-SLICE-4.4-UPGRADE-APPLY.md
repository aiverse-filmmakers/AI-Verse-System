# Safe Infrastructure Slice 4.4 - Upgrade Apply Orchestration, Resume and Verification

**Status:** COMPLETE  
**Canonical slice:** 4.4  
**Outcome:** explicit `aiverse upgrade --apply` now orchestrates admitted owner-controlled structural work through the shipped Distribution lifecycle/recovery substrate without changing normal software-update semantics or inventing owner migrations.

## Refreshed starting refs

Refreshed before Slice 4.4 product implementation:

- `aiverse-filmmakers/AI-Verse-System@64717ca18123c333ebc64fd0a1412329ad13618a`
- `aiverse-filmmakers/ai-verse-distribution@15e03219185f484cbbc4c5887d967ddc5630d1a6`
- `aiverse-filmmakers/AI-Verse-OS@470ad89e6b96d898161dee36d4e4fa8064dd6a8d`
- `aiverse-filmmakers/AI-Verse-Skills@d4a02888ba8d83c4a15ce1b538ffdafaaf83bee1`

The System repository advanced concurrently because another canonical program was updating independent governance files. Final Slice 4.4 bookkeeping was therefore refreshed against current System main `c006cf0c21450f0399b11efb3916372558528d16` rather than rewinding unrelated work.

## Canonical acceptance target

Slice 4.4 had to prove:

- exact upgrade plan revalidation immediately before apply;
- Last-Known-Good before owner mutation;
- dependency-safe owner-handler ordering;
- truthful resumable partial failure;
- canonical identity/reference revalidation;
- reference-repair and postcondition verification;
- no false success after failed verification or final health;
- retained restore availability after upgrade;
- explicit apply intent for OPTIONAL work;
- REQUIRED work remains explicit and separate from normal update;
- practical non-jargon completion output.

All acceptance criteria pass. Exact evidence follows below.

## Final adaptive task list

- [x] **4.4-T1** Freeze refreshed refs and the real owner/transaction inventory before product implementation; classify current production no-recipe behavior and reject invented Workspace/Skills migrations.
- [x] **4.4-T2** Bind executable infrastructure plans deterministically to the exact admitted release, component revision, source detection evidence and exact owner recipe path while keeping previews read-only and owner operation IDs opaque.
- [x] **4.4-T3** Implement explicit `upgrade --apply` orchestration using the existing lifecycle transaction, exact pending-owner-effect recovery, immediate re-plan, LKG-first protection and a trusted owner lifecycle executor.
- [x] **4.4-T4** Verify preconditions, identity/reference evidence, repairs, owner verification, postconditions and final whole-install health before committing success; persist truthful completion/recovery evidence without changing the installed software release.
- [x] **4.4-T5** Keep default member output concise/non-technical for no-op, success, stale-plan and recovery-required outcomes while retaining full machine-readable JSON evidence and preserving existing doctor/update/restore routing.
- [x] **4.4-T6** Add focused positive/destructive-negative coverage for current no-recipe no-op, OPTIONAL/REQUIRED explicit apply, source drift, LKG ordering, dependency order, repair, identity failure, interruption/resume, failed final health, idempotent replay, post-receipt crash recovery and retained restore availability.
- [x] **4.4-T7** Qualify exact Distribution PR head and merged main across the full six-job Distribution CI matrix, record exact evidence, close Phase 4 at 4/4 and stop before Phase 5 / Slice 5.1.

## Owner and current-release boundary

Phase 3 evidence was reused instead of creating a second migration implementation:

- Workspace physical relocation remains unadmitted and unnecessary; `workspaces/<workspace-id>` is still the canonical OS slot.
- OS remains owner of the real Workspace-to-personal capability promotion transaction, including source digest/generation revalidation, target staging/verification, source-history preservation, explicit identity change and retired-qualified-ID compatibility repair.
- Skills remains owner of managed immutable `aiverse-skills` generations; no managed Skills structural defect is currently admitted.
- `detect_operation`, `apply_operation`, `verify_operation`, pre/postconditions and reference-repair operation IDs remain opaque owner operation identifiers. Distribution sequences/invokes trusted adapters; it does not translate metadata into file operations or shell commands.

The currently admitted Core OS and Skills descriptors still do not publish `migration.infrastructure`. Therefore a real current member installation has no structural recipe to apply and `aiverse upgrade --apply` truthfully returns a healthy no-op. Mutation behavior was qualified with exact synthetic admitted descriptors and an injected trusted owner executor. No production migration or owner release descriptor was fabricated merely to make this slice mutate something.

## Distribution implementation

Distribution PR #33 added/changed seven files:

- `src/aiverse_distribution/infrastructure_upgrade.py`
- `src/aiverse_distribution/experience_orchestrator.py`
- `src/aiverse_distribution/experience_output.py`
- `src/aiverse_distribution/entrypoint.py`
- `tests/test_infrastructure_upgrade_apply.py`
- `tests/test_infrastructure_upgrade_recovery_edges.py`
- `scripts/project-bootstrap.py` for one narrow qualification defect described below.

### Exact executable-plan binding

`ExperienceOrchestrator` now re-reads the exact admitted component descriptor and binds executable work to:

- release set;
- component and exact component revision;
- source/target infrastructure generation;
- source detection evidence digest;
- exact unique recipe path/version/disposition;
- owner detect/apply/verify operation IDs;
- declared preconditions/postconditions;
- canonical identity contract/evidence reference;
- declared reference-repair operations.

Preview remains read-only. Before any owner mutation, `upgrade_apply()` takes/qualifies LKG, rebuilds the plan from current source state and refuses with `REPLAN_REQUIRED` if the fingerprint changed.

### Durable resume/recovery

A private `InfrastructureUpgradeJournal` records one exact transaction with an integrity-bound execution plan, retained LKG ID, base receipt generation and per-step verified evidence. The existing `StateStore.begin_effect()` / `commit_effect()` marker remains the authoritative crash-visible lifecycle owner effect.

A retry may resume only the matching journal plus matching pending lifecycle marker. Completed owner steps are detected/verified rather than blindly replayed. A crash after the authoritative receipt commit but before journal archival is recognized from `last_infrastructure_upgrade` and completes evidence cleanup without rerunning owner mutation.

The retained pre-upgrade LKG is verified again after owner work and is deliberately not rotated away, so explicit restore remains available.

### Final-health ownership discovery and fix

A real transaction interaction was discovered during qualification: ordinary `status()` / `doctor()` correctly report `recovery-required` whenever any lifecycle owner effect is pending. Calling them unchanged while the Slice 4.4 owner-effect marker remained durable would therefore make every real structural apply fail its final-health gate.

The fix did not clear, weaken or globally hide recovery ownership. `OwnedEffectHealthState` provides a read-only state view only to the orchestrator that owns the exact pending marker. It:

- requires an active lifecycle transaction;
- validates exact token, operation key, base generation and metadata;
- validates the receipt has not advanced;
- hides only that exact `_pending_lifecycle` field from the owner-local read view;
- blocks state mutation through the view;
- rejects a mismatched token/owner;
- leaves the real durable pending marker visible to all normal status/doctor callers until authoritative receipt commit.

Final health therefore uses the existing `status()` / `doctor()` logic through that exact owned-effect view, preserving normal recovery-required semantics everywhere else.

## Member behavior

- `aiverse upgrade` remains read-only preview.
- `aiverse upgrade --apply` is the only structural mutation route.
- `aiverse update` / `aiverse update --plan` retain shipped software-update semantics; no `update --apply` was introduced.
- REQUIRED structural work remains explicit rather than silently entering normal update.
- `doctor --component` expert compatibility remains unchanged.
- default apply output states practical improvement count, preservation, health and recovery availability without release IDs, hashes, paths, generations, recipe IDs or migration jargon;
- `--json` retains detailed machine-readable evidence.

## Focused destructive-negative proof

Coverage proves at minimum:

- current admitted no-recipe release is a clean no-op and does not rotate LKG;
- OPTIONAL preview mutates nothing and requires explicit apply;
- REQUIRED remains explicit until apply;
- LKG is secured before first owner apply operation;
- stale source evidence after LKG forces re-plan before owner mutation;
- components execute in install/dependency order;
- required reference repair executes and is verified;
- identity evidence mismatch cannot report success;
- interruption after owner mutation leaves exact pending/journal evidence and resumes safely;
- failed final whole-install health cannot commit success;
- completed replay is idempotent and does not repeat apply or rotate LKG;
- crash after receipt commit but before journal archival finalizes without replaying owner effects;
- exact-owned-effect health view hides only the matching marker, rejects a wrong token and cannot mutate state;
- default member output does not leak internal IDs or migration jargon.

## Qualification discovery outside Slice 4.4 ownership

The broad Project Bootstrap gate exposed a pre-existing `--help` defect: `scripts/project-bootstrap.py --help` inspected the working project directory before argparse could return help, so a checked-out repository was rejected as non-empty. The fix is intentionally narrow: `-h/--help` now enters the canonical parser before project inspection. No bootstrap install/update routing semantics changed.

Two unrelated broad-gate defects remain outside Slice 4.4 ownership and were not hidden or absorbed:

- Clean Machine Core still exposes the already-known first-run release-candidate defect where OS reports `setup-required`; this predates Slice 4.4 and never enters the structural upgrade path.
- Clean Machine Agent on Windows exposed a Gateway runtime `EPERM` atomic-rename failure for Gateway run-state JSON. Ubuntu passes; the failure occurs inside Gateway runtime state, not the Slice 4.4 orchestration path.

These do not weaken the exact Slice 4.4 Distribution qualification below.

## Exact qualification evidence

### System start/task record

- System PR #204: **Start Safe Infrastructure Slice 4.4**.
- exact PR head: `1284b419f9725f99ef5c5d92be5be167daee36fa`.
- Contract Validation run `38383576199`: **SUCCESS**, Python 3.11 and 3.13.
- merged System start record: `1c824059e32d1e1bab5727aaea3b9636b146658b`.

### Distribution PR head

- Distribution PR #33: **Add explicit infrastructure upgrade apply orchestration**.
- exact qualified PR head: `6aee670cdee7417b9822aeacc0e6638c29d79a5e`.
- exact PR-head Distribution CI run `38386061553`: **SUCCESS**, all six jobs:
  - Ubuntu Python 3.11;
  - Ubuntu Python 3.12;
  - macOS Python 3.11;
  - macOS Python 3.12;
  - Windows Python 3.11;
  - Windows Python 3.12.
- exact-head supporting gates also passed:
  - Lifecycle Receipt Concurrency `38386061543`;
  - Invisible Intelligence Scenarios A-F `38386062170`;
  - Composed Semantic Migration Acceptance `38386061676`;
  - Composed Two-System Isolation Acceptance `38386061693`.

### Distribution merged main

- PR #33 merged exactly from head `6aee670cdee7417b9822aeacc0e6638c29d79a5e`.
- exact Distribution merged main: `10d04c723e5918506f1f76aabf1c59bfa23f7b8b`.
- exact merged-main Distribution CI run `38386952080`: **SUCCESS**, all six Ubuntu/macOS/Windows x Python 3.11/3.12 jobs.

## Acceptance criteria

- exact upgrade plan is revalidated against source state immediately before apply: **PASS**;
- Last-Known-Good is secured first: **PASS**;
- owner handlers execute in dependency-safe order: **PASS**;
- partial failure remains resumable/recoverable/truthful: **PASS**;
- identity/reference conditions from the canonical Identity Hardening contract are revalidated: **PASS**;
- required reference repairs and postconditions are verified: **PASS**;
- failed upgrade never reports success: **PASS**;
- restore remains available after upgrade: **PASS**;
- OPTIONAL upgrades require explicit apply intent: **PASS**;
- REQUIRED upgrades remain explicit rather than hidden inside normal update: **PASS**;
- completion output explains practical improvement, preservation and health without migration jargon: **PASS**;
- normal software update, expert component doctor and restore semantics remain intact: **PASS**;
- exact PR-head and exact merged-main six-job Distribution CI are green: **PASS**.

No protected-law amendment was required.

## Completion report

```text
Completed: Slice 4.4 - Implement `upgrade --apply` orchestration, resume and verification
Tasks: 7/7
Overall: 15/18 slices (83.3%)
Phase: Phase 4 - Implement Distribution orchestration and simple member UX
Phase progress: 4/4 COMPLETE
Until Phase 5: 0 slices
Next: Phase 5 / Slice 5.1 - Add cross-repo regression and destructive-negative tests
Blockers/drift/amendments: no Slice 4.4 blocker or protected-law amendment; known unrelated broad-gate defects remain separately owned.
```

## NEXT

**STOP after Slice 4.4 under the current one-at-a-time execution request.**

Next execution unit is Phase 5 / Slice 5.1. Derive its adaptive task list only after fresh refs are fetched. No Safe Infrastructure Slice 5.1 implementation was started here.
