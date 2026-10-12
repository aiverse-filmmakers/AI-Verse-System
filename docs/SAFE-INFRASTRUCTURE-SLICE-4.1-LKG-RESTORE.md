# Safe Infrastructure Slice 4.1 - Last-Known-Good and Restore Evidence

Status: COMPLETE

## Slice-start refs

- System: `aiverse-filmmakers/AI-Verse-System@ad260107669b5525523c98f1dd8302c4675c8939`
- task-list commit: `aiverse-filmmakers/AI-Verse-System@487bbd7fe5eac1172e03756dbb2abe7338697894`
- Distribution: `aiverse-filmmakers/ai-verse-distribution@90f175418f8d13faeece8bcb1ad0796d2adecfb1`
- OS: `aiverse-filmmakers/AI-Verse-OS@470ad89e6b96d898161dee36d4e4fa8064dd6a8d`
- Skills: `aiverse-filmmakers/AI-Verse-Skills@d4a02888ba8d83c4a15ce1b538ffdafaaf83bee1`

The canonical Safe Infrastructure roadmap was reconciled before this slice began and truthfully recorded Phase 3 complete at 11/18 slices (61.1%), with Phase 4 / Slice 4.1 next. Temporary Slice 3.4 roadmap-closure helper/workflow/trigger files were removed before this task list was recorded.

## Verified shipped substrate

### REUSE

- Distribution private state home (`~/.aiverse/distribution` or `AIVERSE_DISTRIBUTION_HOME`).
- `StateStore.lifecycle_transaction()` cross-platform kernel lock and receipt-generation CAS boundary.
- `StateStore._atomic_json()` temp+fsync+atomic replace semantics.
- Existing Core update journal and owner-native interrupted-update recovery.
- Existing exact release receipt / released catalog bindings.
- Existing member-state fingerprint and semantic SQLite preservation helpers.
- Existing Core status/doctor/final-health verification.

### EXTEND

- Core mutating update path now requires a verified LKG candidate before first admitted mutation.
- Distribution installed CLI now exposes `aiverse restore` preview and explicit `aiverse restore --apply`.
- Existing component staging, owner setup/update, source verification and final-health paths are reused during recovery.

### CREATE

- One Distribution-owned manifest-backed whole-install LKG store using immutable generation material plus an atomic current pointer.
- Recovery coverage manifest with CAPTURE / RECONSTRUCT / REBUILD / EXTERNAL-EXCLUDED classes.
- Transaction-safe restore engine and focused destructive-negative tests.

### NOT CREATED

- no second lifecycle lock/transaction system;
- no second canonical live state store;
- no generic backup service;
- no owner-domain migration inference;
- no silent secret copying;
- no multi-snapshot history product;
- no Workspace relocation semantics;
- no structural `upgrade --apply` implementation from Slice 4.2;
- no change to the read-only meaning of `aiverse update --plan`, `aiverse doctor`, or `aiverse upgrade`.

## Frozen Slice 4.1 semantics

1. Exactly one retained usable whole-install LKG is the product promise. Temporary candidate/restore transaction material does not count as another retained LKG.
2. Candidate material is staged and fully verified before the retained `current` pointer moves.
3. The prior valid LKG remains untouched until successor promotion succeeds.
4. If the current install is unhealthy, ambiguous, source-dirty where exact reconstruction is required, or cannot be represented truthfully, a mutating update stops before mutation and preserves the old LKG.
5. Recovery material lives under Distribution private state and is never a live provider/canonical owner state source.
6. Large Workspace `assets/` and `outputs/` remain user-owned CAPTURE data. Size alone never excludes them.
7. Known derived/disposable material is REBUILD and is not copied merely for completeness.
8. External side effects and credential/security state that cannot be safely rewound are EXTERNAL-EXCLUDED and reported plainly.
9. Exact software/release state is RECONSTRUCT only from verified exact-release evidence retained as Git bundles plus digests.
10. `aiverse restore` is read-only preview. `aiverse restore --apply` is the only whole-install restore mutation surface.
11. Restore keeps its target LKG intact throughout apply. A temporary transaction checkpoint protects pre-restore current state but never replaces the retained LKG.
12. Restore failure either rolls back through the temporary transaction checkpoint or stops `recovery-required` with the retained LKG still usable; it does not guess.

## Final adaptive task list

- [x] **4.1-T1** Reconcile the corrected Phase 3 closure, refresh System/Distribution/OS/Skills refs, and inventory shipped Distribution transaction, update-journal, preservation, exact-release and CLI surfaces.
- [x] **4.1-T2** Define and implement the Distribution-owned LKG manifest/store: immutable staged generation, content verification, atomic current pointer, previous-LKG preservation until promotion, and bounded retention of exactly one successful generation.
- [x] **4.1-T3** Implement evidence-backed recovery coverage classification and capture: canonical/user state CAPTURE (including large Workspace assets/outputs), exact software/release RECONSTRUCT evidence, owner-declared derived REBUILD exclusions, explicit security/external exclusions, and no blind secret copying.
- [x] **4.1-T4** Integrate LKG qualification/rotation into the mutating installed Core `aiverse update` path before first mutation, reusing the existing lifecycle transaction and refusing mutation if a safe successor LKG cannot be qualified. Expose the reusable guard needed by future `upgrade --apply` without implementing Slice 4.2 orchestration.
- [x] **4.1-T5** Implement `aiverse restore` preview and `aiverse restore --apply`: coverage/exclusion/replacement-risk preview, exact target validation, temporary restore checkpoint, covered local-state restore/reconstruction, owner/system verification, retained-target preservation, and truthful external-effect reporting.
- [x] **4.1-T6** Add focused positive and destructive-negative tests for first LKG creation, rotation, failed candidate preservation, unhealthy refusal, exactly-one retention, large user assets, security exclusions, read-only preview, successful apply, restore failure recovery, and unchanged no-op/update-plan semantics.
- [x] **4.1-T7** Run exact-head and exact-merged-main Distribution CI, record evidence, close every Slice 4.1 acceptance criterion, update the canonical roadmap to 12/18 (66.7%) with Phase 4 at 1/3, and stop before Slice 4.2.

## Distribution implementation

PR #30, `Implement Safe Infrastructure Slice 4.1 LKG recovery`, was squash-merged into Distribution `main` as:

- `aiverse-filmmakers/ai-verse-distribution@2fec4675287be748ae222efa61330bdaee37b0bc`

The exact pre-merge qualified PR head was:

- `0f5fd5fa0e5392957376ac8a679125f13dc2a11d`

### `src/aiverse_distribution/recovery.py`

Implements the Distribution-owned LKG store.

Recovery material lives only under Distribution private state:

```text
recovery/
  current.json
  generations/lkg-<opaque-id>/
    manifest.json
    capture/
    reconstruct/
  transactions/
```

Key behavior:

- stages candidates outside the retained generation set;
- captures user/canonical regular files by evidence-backed rules;
- stores exact SHA-256 and byte size for every captured file;
- preserves Workspace `assets/` and `outputs/` as CAPTURE regardless of size;
- captures private reusable local capability state;
- retains exact software revisions as verified Git bundles bound to the released catalog and current Distribution receipt;
- records derived/disposable material as REBUILD;
- excludes credential/private-key shaped data, symlinks/external targets and special filesystem entries rather than copying them blindly;
- verifies candidate manifest, captured bytes and software bundles before promotion;
- atomically publishes `current.json` only after successful verification;
- deletes the obsolete retained generation only after successor promotion;
- if obsolete-generation retirement fails, restores the previous pointer and discards the candidate instead of reporting a successful rotation with two retained LKGs;
- validates the retained pointer/manifest/bytes on every load/preview/apply.

### `src/aiverse_distribution/recovery_orchestrator.py`

Adds `RecoveryOrchestrator(CoreUpdateOrchestrator)` without replacing the existing update transaction model.

For a real installed Core update:

1. enter the existing Distribution lifecycle transaction;
2. run existing owner-native interrupted-update recovery;
3. compute the ordinary update plan;
4. if no-op, preserve existing no-op behavior and do not rotate an LKG;
5. if mutating, call `ensure_last_known_good()` before `_apply_core_update()`;
6. refuse the mutation if LKG qualification fails.

`ensure_last_known_good()` is the explicit reusable pre-mutation guard that future Slice 4.2 structural `upgrade --apply` must call. Slice 4.1 does not implement structural upgrade orchestration.

Restore apply:

1. reuses the existing lifecycle lock;
2. completes admitted owner-native interrupted-update recovery first;
3. revalidates the retained LKG and preview safety;
4. creates a separate temporary current-state checkpoint;
5. reconstructs exact software from verified retained bundles;
6. reuses existing component staging/owner setup/update paths;
7. restores covered canonical/user CAPTURE state;
8. commits the retained Distribution receipt;
9. requires existing composed status/doctor final health;
10. deletes only the temporary checkpoint after success.

A failed restore attempts to recover the pre-restore receipt/software and temporary checkpoint. If that rollback also fails, the operation raises recovery-required and explicitly leaves the retained LKG target intact.

### Installed command surface

`src/aiverse_distribution/entrypoint.py` now routes installed commands through `RecoveryOrchestrator` and adds:

- `aiverse restore` -> read-only preview;
- `aiverse restore --apply` -> explicit whole-install restore;
- `--json` support through the existing redaction/output boundary.

The implementation does not change `python -m aiverse_distribution.cli` acceptance tooling or ordinary read-only CLI semantics.

### Documentation

`docs/LAST-KNOWN-GOOD-RECOVERY.md` documents storage, recovery classes, rotation, preview/apply behavior, failure handling and ownership boundaries.

## Recovery coverage proof

Focused tests prove:

- first LKG creation;
- exact one-generation retention after successful rotation;
- failed/unhealthy candidate cannot replace the prior LKG;
- 2 MiB Workspace asset content is captured and verified, proving size alone is not an exclusion;
- Workspace outputs are captured;
- personal local capability state is captured;
- `.env`, private-key-shaped material and external/symlink-shaped state are excluded rather than copied blindly;
- OS runtime/dependency/cache material is REBUILD rather than copied for completeness;
- exact software is recoverable from retained verified Git bundles;
- restore preview is read-only and reports replacement risk/exclusions;
- covered newer local files are replaced only by explicit restore apply;
- excluded secret material remains untouched during restore;
- temporary restore checkpoint can recover pre-restore local bytes while the retained LKG remains unchanged;
- a real mutating installed update calls owner recovery -> LKG qualification -> parent update mutation in that order;
- no-op update does not rotate LKG;
- pending owner-native update recovery prevents whole-install restore from bypassing the narrower transaction recovery;
- successful restore uses a temporary checkpoint and retained LKG without rotating it;
- failed restore rolls back through the checkpoint and does not mutate/delete the retained target;
- `aiverse restore` defaults to preview and `--apply` is explicit.

## Validation discoveries and corrections

Two real issues were found by CI and corrected before merge.

### 1. Installed orchestrator regression assertion

The first PR matrix run correctly failed an existing test that asserted the installed CLI orchestrator was exactly `CoreUpdateOrchestrator`. Slice 4.1 intentionally introduces `RecoveryOrchestrator` as a subclass so existing Core behavior remains inherited while adding the pre-mutation LKG guard.

The regression test was corrected to require:

- installed class is exactly `RecoveryOrchestrator`;
- `RecoveryOrchestrator` remains a subclass of `CoreUpdateOrchestrator`.

This preserved, rather than weakened, the existing Core compatibility boundary.

### 2. Cross-platform physical-root canonicalization

The next PR matrix exposed one product bug on both macOS and Windows: component receipt source paths were canonicalized with `Path.resolve()` but the LKG install root had not been canonicalized at its trust boundary. Linux happened to compare equal; macOS `/var` -> `/private/var` and Windows normalization exposed the mismatch.

The recovery engine now canonicalizes the LKG root before receipt/source binding. This was fixed in product code rather than weakening platform tests.

## Exact CI evidence

### Qualified PR head

Exact head: `0f5fd5fa0e5392957376ac8a679125f13dc2a11d`.

`Distribution CI` run `38317665390`: **SUCCESS**.

All six jobs passed unit tests and CLI catalog smoke:

- Ubuntu / Python 3.11;
- Ubuntu / Python 3.12;
- macOS / Python 3.11;
- macOS / Python 3.12;
- Windows / Python 3.11;
- Windows / Python 3.12.

Additional successful PR-head gates included:

- `Lifecycle Receipt Concurrency` run `38317665368`: **SUCCESS**;
- `Invisible Intelligence Scenarios A-F` run `38317665366`: **SUCCESS**;
- composed semantic migration and two-system isolation passed on the completed Linux/macOS jobs inspected during qualification, with Windows still executing when the scoped merge decision was made.

Two broad PR workflows exposed defects outside the Slice 4.1 diff/path and were deliberately not folded into this slice:

- `Project bootstrap qualification` run `38317665281` fails while handling `bootstrap.sh --help` because the bootstrap router inspects the non-empty repository checkout as though it were a target Core install. Slice 4.1 changes none of `bootstrap.sh`, `project-bootstrap.py`, project routing or project layout, and the failure occurs before recovery orchestration is entered.
- `Clean Machine Core Acceptance` run `38317665472` fails in existing first-run release-candidate owner health because OS doctor reports `setup-required`. The acceptance invokes `python -m aiverse_distribution.cli`, bypassing the new installed `entrypoint.py`/`RecoveryOrchestrator`, so no Slice 4.1 LKG/restore path is entered.

These are separate existing bootstrap/release-candidate issues and are not used as evidence for, or against, the Slice 4.1 recovery acceptance gate.

### Exact merged `main`

Distribution merge commit:

- `2fec4675287be748ae222efa61330bdaee37b0bc`

`Distribution CI` push run `38318052035`: **SUCCESS**.

All six Linux/macOS/Windows × Python 3.11/3.12 jobs passed unit tests and CLI catalog smoke on the exact merged `main` commit.

## Acceptance criteria

- Before every currently shipped mutating installed Core `aiverse update`, a valid LKG is qualified/rotated before the parent update mutation begins: **PASS**.
- Future mutating structural `upgrade --apply` has a reusable required guard without being prematurely implemented in Slice 4.1: **PASS**; `RecoveryOrchestrator.ensure_last_known_good()` is the reusable pre-mutation guard. There is no current shipped mutating `upgrade --apply` surface left unguarded.
- Candidate LKG is staged and verified before prior valid LKG is replaced: **PASS**.
- Unhealthy/ambiguous/unrepresentable current install cannot destroy the sole valid LKG: **PASS**.
- Exactly one retained usable LKG remains after successful rotation: **PASS**.
- Required canonical/user state is durably represented: **PASS**.
- Workspace `assets/` and `outputs/` have explicit recovery coverage and are not dropped for size: **PASS**.
- Software is RECONSTRUCT only from exact reproducible evidence: **PASS**, through exact released receipts plus verified Git bundles/digests.
- Derived caches/dependency/runtime material is not copied merely for completeness: **PASS**.
- Credentials/security-sensitive state is not blindly copied and exclusions are reported: **PASS**.
- Recovery material is private, immutable/non-live and never treated as canonical owner/provider state: **PASS**.
- `aiverse restore` is read-only and reports coverage, exclusions and replacement risk: **PASS**.
- `aiverse restore --apply` explicitly verifies and restores the retained local recovery scope: **PASS**.
- Restore reuses existing owner setup/update and final health instead of inventing owner migration logic: **PASS**.
- Failed restore preserves the retained LKG and either recovers the pre-restore checkpoint or stops recovery-required: **PASS**.
- External/cloud/already-performed side effects are reported as not rewound: **PASS**.
- Existing owner-native update journal/recovery remains authoritative for its narrower transaction: **PASS**.
- No second lifecycle transaction system, canonical state store, Workspace relocation, generic backup product or Slice 4.2 structural orchestration was introduced: **PASS**.
- Exact merged-main six-platform Distribution CI is green: **PASS**.

## Phase result

Slice 4.1 establishes the Distribution recovery substrate required for the rest of Phase 4:

- one verified rotating whole-install LKG;
- mutating Core update preflight protection;
- truthful recovery coverage/exclusions;
- explicit read-only restore preview;
- explicit transaction-safe restore apply;
- reusable LKG guard for the future admitted structural upgrade path.

No protected-law amendment was required.

## Completion report

```text
Completed: Slice 4.1 - Implement one rotating Last-Known-Good recovery point and restore engine
Tasks: 7/7
Overall: 12/18 slices (66.7%)
Phase: Phase 4 - Implement Distribution orchestration and simple member UX
Phase progress: 1/3
Until Phase 5: 2 slices
Next: Slice 4.2 - Implement admitted structural upgrade orchestration
Blockers/drift/amendments: no Slice 4.1 blocker or protected-law amendment. Two unrelated pre-existing broad-gate defects were isolated and not folded into this recovery slice.
```

## NEXT

**STOP after Slice 4.1 under the current one-at-a-time execution request.**

Next execution unit: Slice 4.2. Derive its adaptive task list only after fresh System/Distribution/owner refs are fetched. No Slice 4.2 implementation was started here.
