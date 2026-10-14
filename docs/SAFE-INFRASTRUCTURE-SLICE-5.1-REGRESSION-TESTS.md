# Safe Infrastructure Slice 5.1 - Cross-Repo Regression and Destructive-Negative Tests

**Status:** COMPLETE  
**Canonical slice:** 5.1  
**Outcome:** a permanent composed qualification layer now proves the Safe Infrastructure laws together across Distribution plus the frozen OS/Skills owner contracts without changing product semantics or duplicating owner logic.

## Refreshed starting refs

Frozen before any Slice 5.1 product/test write:

- `aiverse-filmmakers/AI-Verse-System@db42146189d2d869925d26668a6683cf437fdd80`
- `aiverse-filmmakers/ai-verse-distribution@10d04c723e5918506f1f76aabf1c59bfa23f7b8b`
- `aiverse-filmmakers/AI-Verse-OS@470ad89e6b96d898161dee36d4e4fa8064dd6a8d`
- `aiverse-filmmakers/AI-Verse-Skills@d4a02888ba8d83c4a15ce1b538ffdafaaf83bee1`

No owner/product drift was found at Slice 5.1 start. The admitted OS and Skills descriptors publish no live structural migration recipe, so current real-member structural apply remains a truthful no-op while admitted synthetic fixtures exercise mutation semantics.

The System and Distribution repositories advanced concurrently during Slice 5.1 through independent canonical programs. Final closure therefore preserves current System main rather than rewinding it, and merged-main Distribution qualification includes the independently added candidate-evidence contract at `381ead50a9a4d790af945f4d95d268c65ed94060`.

## Final adaptive task list

- [x] **5.1-T1** Freeze fresh System/Distribution/OS/Skills refs and inventory the existing focused coverage so the new gate tests composed invariants rather than duplicating single-slice tests.
- [x] **5.1-T2** Add a dedicated Distribution Safe Infrastructure regression suite that composes read-only planning, normal update semantics, doctor fan-out truth, OPTIONAL/REQUIRED/BLOCKED gating, stale-plan refusal, idempotent apply/replay, retained recovery, destructive restore failure, and concise member-output invariants.
- [x] **5.1-T3** Add cross-owner contract checks that pin the current OS and Skills owner refs/evidence and prove the present Workspace relocation decision, OS promotion identity semantics, managed Skills ownership boundary, and unsupported structural directions remain fail-closed without inventing migrations.
- [x] **5.1-T4** Add explicit destructive-negative coverage for recovery-point retention, preview immutability, source drift, unsupported recipe/relocation, failed owner verification/final health, reference repair, restore-target survival, excluded credentials/external state, and injected mid-upgrade interruption by composing the focused permanent suites that already own those cases.
- [x] **5.1-T5** Add a dedicated six-job Safe Infrastructure Regression CI gate while preserving existing broad gates and the unchanged six-job Distribution CI matrix.
- [x] **5.1-T6** Qualify unchanged OS and Skills owner-native behavior at frozen refs, then qualify the exact Distribution PR head and merged main; classify qualification-scope or unrelated broad-gate behavior separately rather than weakening Slice 5.1 acceptance authority.
- [x] **5.1-T7** Record exact evidence and acceptance results in System, mark Slice 5.1 complete only after all required PR-head and merged-main composed/destructive-negative assertions are green, then stop before Slice 5.2.

## Implementation

Distribution PR #34 adds exactly two permanent files and changes no product/runtime implementation:

- `.github/workflows/safe-infrastructure-regression.yml`
- `tests/test_safe_infrastructure_cross_repo.py`

### Cross-repo owner boundary assertions

The test suite is activated only when the dedicated regression workflow supplies exact frozen owner checkouts. Normal Distribution unit discovery therefore remains compatible and does not require sibling repositories.

It proves:

- OS checkout HEAD equals `470ad89e6b96d898161dee36d4e4fa8064dd6a8d`;
- Skills checkout HEAD equals `d4a02888ba8d83c4a15ce1b538ffdafaaf83bee1`;
- OS descriptor remains owner-controlled, uses `unified-workspace-v2`, and publishes no structural recipe;
- Skills descriptor remains owner-controlled, uses `immutable-generation-v3`, and publishes no structural recipe;
- OS Workspace generation remains `workspace-id-slot-v1` with fail-closed `BLOCKED/REVIEW` evidence including symlink, missing-manifest and slot/identity mismatch cases;
- Workspace infrastructure detection is not a hidden relocation implementation;
- Workspace-to-personal capability promotion remains explicitly identity-changing with `qualified_identity_preserved: false`, `promoted-to` compatibility, resolver repair, provenance/history preservation and stale-plan rejection;
- Skills managed-generation validation remains Skills-owned;
- Distribution source does not absorb the OS Workspace generation, OS capability-promotion protocol or Skills managed-generation implementation constants.

### Composed regression gate

`Safe Infrastructure Regression` runs on:

- Ubuntu, macOS and Windows;
- Python 3.11 and 3.12.

Every one of the six jobs runs the Distribution and exact-ref cross-owner assertions covering:

- infrastructure update gating and structural apply;
- LKG/recovery and restore;
- experience/doctor/upgrade member UX;
- software update behavior, repeat/skip chains and read-only planning;
- adapter routing;
- Safe Infrastructure transition contracts.

OS and Skills owner-native executable suites run on Linux, matching the owners' admitted native qualification surface. The OS Workspace contract itself is Ubuntu/Node 22 in its owner repository; Slice 5.1 does not silently broaden that platform promise merely because Distribution is cross-platform.

The Linux owner-native block runs:

- OS Workspace owner and infrastructure tests plus a clean-tree mutation check;
- OS capability placement, promotion, resolver-core and adapter-sync tests;
- Skills registry validation, full unittest discovery, list command and full-profile dry-run install.

## Qualification discoveries

### Assertion label correction

The first composed run found a Slice 5.1 test-assumption defect, not a product defect. The new static assertion expected finding code `workspace-manifest-id-mismatch`; the frozen OS owner actually and correctly uses the more precise `workspace-id-slot-mismatch`. Only the new assertion was corrected. No owner or product behavior changed.

### Owner-native platform scope

An initial attempt to execute the OS standalone Workspace fixture on macOS reached the owner test and failed outside its admitted qualification platform. Inspection of OS `.github/workflows/workspace-infrastructure.yml` confirmed the canonical owner contract runs on Ubuntu with Node 22. The composed gate was therefore corrected to:

- keep Distribution regression plus exact-ref cross-owner assertions on all six matrix jobs;
- execute OS/Skills owner-native suites on Linux only, matching the owner-native contract.

This is qualification-scope alignment, not a weakened invariant or product fix.

### Concurrent Distribution movement

Between the Slice 5.1 branch point and PR merge, another canonical program advanced Distribution main from `10d04c723e5918506f1f76aabf1c59bfa23f7b8b` to `381ead50a9a4d790af945f4d95d268c65ed94060` by adding an immutable candidate-evidence contract. PR #34 merged on top of that current main. Exact merged-main qualification therefore proves the Safe Infrastructure gate remains compatible with the newer Distribution state rather than only the original 5.1 branch base.

## Exact qualification evidence

### System start record

- System PR #208: **Start Safe Infrastructure Slice 5.1**.
- exact PR head: `f2bf86dcba321420b1ef356d16091af1486c1e2d`.
- Contract Validation run `38636147331`: **SUCCESS**, Python 3.11 and 3.13.
- merged System start record: `2f9538830733d6726c390e6eedd737eaf03f0a9c`.

### Distribution PR head

- Distribution PR #34: **Add Safe Infrastructure cross-repo regression gate**.
- exact qualified head: `7525048d89b148912d53a4793c732aa49fed9c12`.
- Safe Infrastructure Regression run `38636882728`: **SUCCESS**, all six Ubuntu/macOS/Windows x Python 3.11/3.12 jobs.
- Distribution CI run `38636882685`: **SUCCESS**, all six Ubuntu/macOS/Windows x Python 3.11/3.12 jobs.
- Lifecycle Receipt Concurrency run `38636882701`: **SUCCESS**.

The broad clean-machine and composed-isolation workflows remain independent qualification surfaces. Slice 5.1 does not replace them or redefine their ownership.

### Distribution merged main

- PR #34 merged exactly from qualified head `7525048d89b148912d53a4793c732aa49fed9c12`.
- exact merged Distribution main: `1f4559d88966e2a2ff26ca563d7a035ebc69a90b`.
- merged-main Distribution CI run `38637231648`: **SUCCESS**, all six Ubuntu/macOS/Windows x Python 3.11/3.12 jobs.
- merged-main Safe Infrastructure Regression run `38637231851`: **SUCCESS**, all six Ubuntu/macOS/Windows x Python 3.11/3.12 jobs.

### Frozen owner evidence

The composed Linux jobs reran the relevant owner-native suites successfully at the exact frozen refs. Existing exact-ref owner CI remains valid supporting evidence:

- OS `470ad89e6b96d898161dee36d4e4fa8064dd6a8d`: Capability Placement Contract `38306623956` **SUCCESS** and Repository QC `38306623950` **SUCCESS**;
- Skills `d4a02888ba8d83c4a15ce1b538ffdafaaf83bee1`: Validate AI-Verse Skills `38298548847` **SUCCESS** and Release Descriptor `38298549229` **SUCCESS**.

## Acceptance results

- all permanent laws exercised by Slice 5.1 have executable proof or an explicit canonical owner boundary: **PASS**;
- negative/destructive cases preserve protected state on refusal/failure: **PASS**;
- normal `aiverse update` apply behavior remains unchanged: **PASS**;
- update plan, doctor/upgrade preview and restore preview remain read-only: **PASS**;
- owner doctor failure cannot become false aggregate PASS: **PASS**;
- OPTIONAL work remains outside normal update: **PASS**;
- REQUIRED/BLOCKED/REVIEW and unsupported structural states remain explicit/fail-closed: **PASS**;
- stale plans fail before owner mutation: **PASS**;
- replay/repeat and skip-version chains remain safe: **PASS**;
- current unsupported Workspace relocation remains rejected without mutation: **PASS**;
- Workspace-to-personal promotion preserves explicit identity-change semantics and compatibility evidence: **PASS**;
- user custom state remains protected by the composed existing owner/recovery tests: **PASS**;
- sole valid LKG/retained restore target cannot be silently lost by the covered destructive failures: **PASS**;
- credential/external-state exclusions remain truthful: **PASS**;
- injected mid-upgrade failure remains recoverable: **PASS**;
- supported adapters remain routed through the same lifecycle commands: **PASS**;
- default member output remains concise and avoids internal IDs/paths/generations/migration jargon: **PASS**;
- exact PR-head and exact merged-main Distribution CI are green across all six jobs: **PASS**;
- exact PR-head and exact merged-main Safe Infrastructure Regression are green across all six jobs: **PASS**.

No protected-law amendment or product code change was required.

## Completion report

```text
Completed: Slice 5.1 - Add cross-repo regression and destructive-negative tests
Tasks: 7/7
Overall: 16/18 slices (88.9%)
Phase: Phase 5 - Prove safety, convergence, restore and closeout
Phase progress: 1/3
Until program complete: 2 slices
Next: Slice 5.2 - Run real old-install -> current-architecture convergence and restore qualification
Blockers/drift/amendments: no Safe Infrastructure blocker or protected-law amendment; concurrent System/Distribution programs were preserved and merged-main qualification includes their current Distribution state.
```

## NEXT

**STOP after Slice 5.1 under the one-at-a-time execution request.**

Next execution unit is Slice 5.2. Derive its adaptive task list only after fresh System/Distribution/owner refs and real historical/current fixtures are fetched. No Slice 5.2 implementation was started here.
