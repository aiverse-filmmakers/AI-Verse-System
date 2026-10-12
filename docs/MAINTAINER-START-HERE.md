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
| What does a human read quickly? | Generated Repository State Ledger |
| What code/state does a component own? | Canonical component repository |
| What exact release set is admitted/promoted? | ai-verse-distribution |

Never copy a static Registry field into Repository State as a separately maintained truth. State entries bind to Registry entries by stable GitHub `repository_id`.

## Freshness rules

A date alone never proves freshness. Exact Git identity, evidence refs, scope and ancestry are the governing evidence.

Repository State is stored inside AI-Verse-System, so its own System `observed_head` has unavoidable self-publication semantics: it records the exact System head observed immediately before the State snapshot is published. The commit that publishes that State/ledger snapshot is therefore expected to be a direct descendant of the recorded System head. Do not treat that one publication step as unexplained drift. Any additional System movement after the snapshot requires a new relevant refresh before freshness can be claimed for a decision that depends on it.

Before a scoped decision, refresh only the Registry-derived scope required by that decision. For Core, that means System, Distribution, OS, Brain, Memory, Skills and Data. Component scope includes System, Distribution, the selected component and its declared direct dependency closure. Agent, Full and global scopes are derived from Registry lifecycle/release participation rather than hard-coded repository names.

`scripts/refresh_repository_state.py` is the single refresh and projection engine. Live refresh is read-only against sibling repositories. It verifies stable GitHub repository IDs, resolves exact default-branch heads, reads component release descriptors at those exact heads, evaluates owner acceptance only through the canonical descriptor validator, and reads Distribution release-set evidence at the exact observed Distribution head.

A descriptor can validly describe an accepted revision older than the descriptor publication commit. The descriptor's exact `revision` is the owner release target. The commit containing the descriptor is not silently substituted as the accepted release revision.

Distribution qualification never becomes owner acceptance. Multiple or ambiguous current Distribution pins fail closed instead of being resolved by filename or date. Inaccessible evidence is `unavailable`; an executed check that fails is `failed`.

The refresh engine checks that live System HEAD equals the exact local/evidence revision before a refresh can be published. Concurrent System movement fails the refresh instead of silently publishing stale State.

`WATCHDOG-STALE` and `WATCHDOG-FAILED` are never CLEAN. A valid scoped refresh may support a scoped decision while the full watchdog is stale only when the governance contract permits it. Slice 3.2 adds the scheduled/manual full-scan heartbeat using this same refresh engine.

## Drift and release blocking

Every canonical drift record uses `CANONICAL-DRIFT-DETECTED`, a severity of `INFO`, `WARNING` or `BLOCKING`, and a scope of `component`, `Core`, `Agent`, `Full` or `global`.

Only intersecting or global `BLOCKING` drift blocks a release decision. Warnings and informational drift remain visible and must not be silently discarded.

When System documentation conflicts with newer implementation, do not automatically overwrite either side. Stale System text cannot regress accepted implementation, and newer unvalidated code cannot automatically rewrite product intent. Reconcile evidence-first.

Ambiguous ownership is `BLOCKED - OWNER UNRESOLVED`.

## Registry and State commands

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

Publish a refreshed Core State and its generated ledger in a System checkout:

```bash
python scripts/refresh_repository_state.py --refresh --scope Core --write-state --write-ledger
```

`--write-state` and `--write-ledger` only modify the local System checkout. They never write sibling repositories. Publish the resulting State and ledger together so they describe one snapshot.

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

## Current state warning

The live refresh engine is operational, but the scheduled/manual Drift Watchdog heartbeat is intentionally not implemented until Slice 3.2. Repository State therefore remains `WATCHDOG-STALE`; a successful scoped refresh does not make the global watchdog CLEAN.

The existing Core release may have successful owner/Distribution test history, but current component descriptors do not yet prove exact owner acceptance for all current shipped refs. Repository State keeps that Core `BLOCKING` governance gap visible for future release admission rather than rewriting history or claiming the shipped refs were untested.
