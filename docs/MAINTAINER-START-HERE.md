# AI-Verse Repository Network Maintainer Start Here

This is the source-only entrypoint for maintainers and agents making changes that can affect more than one AI-Verse repository.

It does not replace component documentation, release evidence or the permanent governance contract. It tells you which source owns which kind of truth and what must be refreshed before acting.

## Canonical read order

1. Read `docs/REPOSITORY-NETWORK-GOVERNANCE-CONTRACT.md` for permanent ownership, validation, drift, member-isolation and emergency-release laws.
2. Read `governance/repository-registry.json` for static repository identity, canonical responsibility, lifecycle, rollout wave, release participation and expected owner surfaces.
3. Read `governance/repository-state.json` for current dynamic observations and evidence state: observed heads, owner acceptance evidence, Distribution pins, descriptor observations, System synchronization, freshness, watchdog state and drift.
4. Use `docs/REPOSITORY-STATE-LEDGER.md` only as the generated human-readable projection of Registry + State. Never treat the Markdown ledger as machine authority and never hand-edit it.
5. Read `docs/ARCHITECTURE-TOMBSTONES.md` before recreating architecture from an old plan, branch, audit or copied document.
6. Read the applicable update/release contracts and the canonical owner repository before changing implementation.

The implementation roadmap `docs/DISTRIBUTION-SYSTEM-PROPAGATION-IMPLEMENTATION-PLAN.md` records execution history and sequencing. It does not replace the permanent governance contract.

## Authority boundaries

| Question | Canonical source |
| --- | --- |
| What repository/component exists and who owns it? | Repository Registry |
| What is its current observed head? | Repository State |
| What exact owner revision is accepted? | Owner evidence recorded by Repository State |
| What exact revision is Distribution shipping? | Distribution release evidence recorded by Repository State |
| What does the component descriptor currently say? | Owner descriptor observation recorded by Repository State |
| Is System synchronized with accepted implementation? | Repository State + exact reconciliation evidence |
| What drift is open and how severe is it? | Repository State |
| What is the last full watchdog attempt/heartbeat? | Repository State refresh + watchdog records |
| What does a human read quickly? | Generated Repository State Ledger |
| What code/state does a component own? | Canonical component repository |
| What exact release set is admitted/promoted? | ai-verse-distribution |

Never copy a static Registry field into Repository State as a separately maintained truth. State entries bind to Registry entries by stable GitHub `repository_id`.

## Freshness rules

A date alone never proves repository lineage. Exact Git identity, evidence refs, scope and ancestry are the governing evidence. Time is used only for operational watchdog heartbeat freshness where the architecture explicitly requires daily expected scans.

Repository State is stored inside AI-Verse-System, so its own System `observed_head` has unavoidable self-publication semantics: it records the exact System head observed immediately before the State snapshot is published. The commit that publishes that State/ledger snapshot is therefore expected to be a direct descendant of the recorded System head. Any additional System movement after the snapshot requires a new relevant refresh before freshness can be claimed for a decision that depends on it.

Before a scoped decision, refresh only the Registry-derived scope required by that decision. For Core, that means System, Distribution, OS, Brain, Memory, Skills and Data. Component scope includes System, Distribution, the selected component and its declared direct dependency closure. Agent, Full and global scopes are derived from Registry lifecycle/release participation rather than hard-coded repository names.

`scripts/refresh_repository_state.py` is the single discovery/comparison/projection engine. Live refresh is read-only against sibling repositories. It verifies stable GitHub repository IDs, resolves exact default-branch heads, reads component release descriptors at those exact heads, evaluates owner acceptance only through the canonical descriptor validator, and reads Distribution release-set evidence at the exact observed Distribution head.

`scripts/run_repository_watchdog.py` is watchdog orchestration around that same engine. It performs only a Registry-derived `global` refresh, records heartbeat transitions in the same Repository State, preserves unrelated drift, and never writes sibling repositories or release pins.

A descriptor can validly describe an accepted revision older than the descriptor publication commit. The descriptor's exact `revision` is the owner release target. The commit containing the descriptor is not silently substituted as the accepted release revision.

Distribution qualification never becomes owner acceptance. Multiple or ambiguous current Distribution pins fail closed instead of being resolved by filename or date. Inaccessible evidence is `unavailable`; an executed check that fails is `failed`.

The refresh engine checks that live System HEAD equals the exact local/evidence revision before a refresh can be published. Concurrent System movement fails the refresh instead of silently publishing stale State. The watchdog workflow also relies on a normal non-force Git push, so movement after refresh fails publication rather than overwriting newer work.

`WATCHDOG-STALE` and `WATCHDOG-FAILED` are never CLEAN. The daily/manual watchdog uses a successful global refresh to set `WATCHDOG-CURRENT`. The first unsuccessful expected full scan after a current heartbeat becomes `WATCHDOG-FAILED`; a second consecutive unsuccessful expected scan becomes `WATCHDOG-STALE`. A timestamped current heartbeat is also treated as operationally stale when it is at least two expected daily windows old. A valid scoped refresh may still support a scoped decision while global watchdog state is WARNING-stale only when the governance contract permits it.

## Drift and release blocking

Every canonical drift record uses `CANONICAL-DRIFT-DETECTED`, a severity of `INFO`, `WARNING` or `BLOCKING`, and a scope of `component`, `Core`, `Agent`, `Full` or `global`.

Only intersecting or global `BLOCKING` drift blocks a release decision. Warnings and informational drift remain visible and must not be silently discarded.

When System documentation conflicts with newer implementation, do not automatically overwrite either side. Stale System text cannot regress accepted implementation, and newer unvalidated code cannot automatically rewrite product intent. Reconcile evidence-first.

Ambiguous ownership is `BLOCKED - OWNER UNRESOLVED`.

## Registry, State and watchdog commands

Validate static Registry truth:

```bash
python scripts/validate_repository_registry.py governance/repository-registry.json
```

Validate dynamic State against Registry:

```bash
python scripts/validate_repository_state.py governance/repository-state.json
```

Run a read-only live Core refresh without changing files:

```bash
python scripts/refresh_repository_state.py --refresh --scope Core
```

Run a read-only live component refresh:

```bash
python scripts/refresh_repository_state.py --refresh --scope component --component ai-verse-os
```

Run a read-only full registered-repository refresh:

```bash
python scripts/refresh_repository_state.py --refresh --scope global
```

Publish a refreshed Core State and generated ledger in a System checkout:

```bash
python scripts/refresh_repository_state.py --refresh --scope Core --write-state --write-ledger
```

Run the full watchdog locally against the exact checked-out System head and write only local State + ledger:

```bash
python scripts/run_repository_watchdog.py --write
```

Check whether the persisted heartbeat is current:

```bash
python scripts/run_repository_watchdog.py --check-current
```

The canonical automation is `.github/workflows/repository-drift-watchdog.yml`. It runs once daily and supports manual dispatch. Its GitHub token is scoped to the current System repository only. Before publication it rejects any working-tree change outside:

- `governance/repository-state.json`
- `docs/REPOSITORY-STATE-LEDGER.md`

It never patches component/Distribution repositories, changes release pins or promotes releases. A non-fast-forward push or System-head concurrency causes failure rather than overwrite.

`--write-state`, `--write-ledger` and watchdog `--write` only modify the local System checkout. Publish State and ledger together so they describe one snapshot.

Regenerate the human ledger from already-recorded machine truth:

```bash
python scripts/refresh_repository_state.py --write-ledger
```

Check that the committed ledger is current:

```bash
python scripts/refresh_repository_state.py --check-ledger
```

Do not edit `docs/REPOSITORY-STATE-LEDGER.md` directly.

## Cross-repository change route

For a defect or change discovered anywhere in the network:

1. identify the canonical owner;
2. fix the owner repository;
3. run owner-native CI/acceptance;
4. produce an exact immutable accepted ref and evidence;
5. refresh the relevant Repository State scope;
6. let Distribution adopt the exact owner ref;
7. run Distribution whole-product qualification;
8. synchronize System truth where required;
9. requalify if any candidate-bound input changed;
10. promote only when all relevant blocking gates pass.

Do not fix a sibling defect in Distribution merely because Distribution discovered it. Do not let local component CI claim a member release. Do not let System become a second component implementation home.

## Member-install boundary

Registry, Repository State, generated governance ledger, tombstones, implementation plans, candidate qualification internals and maintainer instructions are source-only governance surfaces. They do not enter member installations by default.

Member installs receive only admitted runtime/product artifacts plus legitimate member-facing generated files. Unknown and user-owned files remain protected.

## Current operational evidence and program handoff

The 20-slice repository-network governance program's exact acceptance matrix, source-only closeout and ongoing operator caveats are in [Repository Network Program Closeout and Handoff](REPOSITORY-NETWORK-PROGRAM-CLOSEOUT-HANDOFF-2026-10-18.md). The canonical Registry/State files and successful workflow runs remain the machine/evidence truth; this entrypoint is not a separate current-health or release authority.

The last verified global heartbeat at program closeout is `WATCHDOG-CURRENT`, a complete 14/14 Registry-derived scan observed `2026-10-18T19:54:04Z` on evidence revision `c5e0920d155b6b284b8d68f16ddf694bbb5dd6ab`, published in System commit `5557c734982776f73b8aaed07ed67fcd1adf0ab5`. It reported zero evidence failures and zero open drift, and its State/ledger were validated. That historic exact snapshot is not a claim that a later unrelated System/owner ref is automatically synchronized. For future full-network decisions, obtain a properly scoped fresh refresh/watchdog at the exact decision boundary. The preceding failed scheduled watchdog attempts remain genuine failures in the roadmap.

All five released Core pins have exact accepted owner descriptors at the inspected T2 refs, but the historical three-OS clean-machine acceptance failure `38807901169` still reported `Setup: setup-required` and does not authorize a **new** promotion. Wave 2/3 current-head acceptance remains `unverified`/`unpinned`; Agent historical release is nondefault, Full blocked and Apps experimental despite Apps now being public. Real emergency debt closure requires independently authenticated remote canonical System State. Do not equate source acceptance, passing isolated regressions or the global heartbeat with a universal live member-health or promotion pass.
