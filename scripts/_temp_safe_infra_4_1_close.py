from pathlib import Path

roadmap_path = Path('docs/SAFE-INFRASTRUCTURE-UPGRADE-AND-RECOVERY-IMPLEMENTATION-PLAN.md')
evidence_path = Path('docs/SAFE-INFRASTRUCTURE-SLICE-4.1-LKG-RESTORE.md')

roadmap = roadmap_path.read_text(encoding='utf-8')
evidence = evidence_path.read_text(encoding='utf-8')


def replace_once(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label}: expected one occurrence, found {count}: {old!r}')
    return text.replace(old, new, 1)

evidence = replace_once(evidence, 'update the canonical roadmap to 12/18 (66.7%) with Phase 4 at 1/3, and stop before Slice 4.2.', 'update the canonical roadmap to 12/18 (66.7%) with Phase 4 at 1/4, and stop before Slice 4.2.', 'evidence Phase 4 task denominator')
evidence = replace_once(evidence, 'Phase progress: 1/3\n', 'Phase progress: 1/4\n', 'evidence completion denominator')
evidence = replace_once(evidence, 'Until Phase 5: 2 slices\n', 'Until Phase 5: 3 slices\n', 'evidence until Phase 5')

for old, new, label in [
    ('**Status:** PAUSED - PHASE 3 COMPLETE; PHASE 4 NOT STARTED  \n', '**Status:** IN PROGRESS - PHASE 4; SLICE 4.1 COMPLETE  \n', 'top status'),
    ('**Completed:** 11  \n', '**Completed:** 12  \n', 'top completed'),
    ('**Remaining:** 7  \n', '**Remaining:** 6  \n', 'top remaining'),
    ('**Overall progress:** 61.1%  \n', '**Overall progress:** 66.7%  \n', 'top progress'),
    ('**Current phase:** Phase 3 - Implement canonical owner migrations for proven motivating problems - COMPLETE  \n', '**Current phase:** Phase 4 - Implement Distribution orchestration and simple member UX  \n', 'top phase'),
    ('**Current phase progress:** 4/4 COMPLETE  \n', '**Current phase progress:** 1/4  \n', 'top phase progress'),
    ('**Slices until Phase 4:** 0  \n', '**Slices until Phase 5:** 3  \n', 'top until phase'),
    ('**Next:** Phase 4 / Slice 4.1 - Implement one rotating Last-Known-Good recovery point and restore engine  \n', '**Next:** Slice 4.2 - Extend shipped update staging/activation around structural upgrade requirements  \n', 'top next'),
    ('**Next slice task list:** STOP - derive only when Phase 4 / Slice 4.1 starts\n', '**Next slice task list:** STOP - derive only when Slice 4.2 starts\n', 'top next task'),
]:
    roadmap = replace_once(roadmap, old, new, label)

roadmap = replace_once(roadmap, '# Phase 4 - Implement Distribution orchestration and simple member UX\n\n**Phase size:** 4 slices\n', '# Phase 4 - Implement Distribution orchestration and simple member UX\n\n**Phase size:** 4 slices  \n**Status:** IN PROGRESS  \n**Phase progress:** 1/4\n', 'Phase 4 header')

slice_start = roadmap.find('## Slice 4.1 - Implement one rotating Last-Known-Good recovery point and restore engine\n')
slice_end = roadmap.find('\n---\n\n## Slice 4.2 - Extend shipped update staging/activation around structural upgrade requirements\n', slice_start)
if slice_start < 0 or slice_end < 0:
    raise SystemExit('could not find Slice 4.1 guarded boundaries')
old_slice = roadmap[slice_start:slice_end]
for needle in ['**Status:** NOT STARTED', '**Dependencies:** 2.3', 'before every mutating `aiverse update` or `aiverse upgrade --apply`, a valid recovery point exists;', '`aiverse restore` is preview-only and mutates nothing;', 'failed restore has a transaction-safe recovery path without destroying the retained Last-Known-Good target;']:
    if needle not in old_slice:
        raise SystemExit(f'Slice 4.1 guard missing expected text: {needle}')

new_slice = '''## Slice 4.1 - Implement one rotating Last-Known-Good recovery point and restore engine

**Status:** COMPLETE  
**Dependencies:** 2.3  
**Adaptive tasks:** 7/7 COMPLETE

Implemented the bounded whole-install recovery guarantee by extending Distribution's existing lifecycle transaction rather than creating a second transaction/backup owner.

### Final implementation

Distribution now owns one verified rotating Last-Known-Good recovery point under private Distribution state. Recovery uses four explicit classes: CAPTURE for canonical/user state that cannot safely be reconstructed, RECONSTRUCT for exact released software represented by verified Git bundles, REBUILD for owner-declared derived/disposable material, and EXTERNAL / EXCLUDED for external effects or credential/security material that cannot truthfully be rewound or should not be copied blindly.

Workspace `assets/` and `outputs/` are CAPTURE regardless of size. Candidate recovery material is staged and verified before the retained pointer moves. The previous valid LKG remains intact until successor promotion succeeds. Successful rotation retains exactly one usable generation; failed obsolete-generation retirement restores the previous pointer instead of claiming success with multiple retained LKGs.

The installed mutating Core update path now calls the reusable `ensure_last_known_good()` guard before parent update mutation. No-op updates do not rotate recovery state. Slice 4.1 does not implement structural `upgrade --apply`; future admitted structural mutation must reuse the same guard.

`aiverse restore` is read-only preview. `aiverse restore --apply` is explicit, runs under the existing lifecycle lock, keeps the retained LKG target immutable, creates a separate temporary rollback checkpoint, reconstructs exact software, restores covered local state, reuses owner setup/update and final health, and either recovers pre-restore state on failure or stops recovery-required with the retained LKG still intact.

### Final adaptive task list

- [x] **4.1-T1** Reconcile Phase 3 closure, refresh refs, and inventory shipped Distribution transaction/update/preservation/release/CLI surfaces.
- [x] **4.1-T2** Implement the Distribution-owned LKG manifest/store with immutable staging, verification, atomic current pointer, prior-point preservation and exactly-one successful retention.
- [x] **4.1-T3** Implement evidence-backed CAPTURE / RECONSTRUCT / REBUILD / EXTERNAL-EXCLUDED coverage, including large Workspace media and safe credential/security exclusions.
- [x] **4.1-T4** Guard real mutating installed Core update before first parent mutation and expose the same reusable LKG guard for future admitted structural mutation without implementing Slice 4.2/4.4.
- [x] **4.1-T5** Implement read-only restore preview and explicit transaction-safe restore apply with rollback checkpoint, exact reconstruction, covered-state restore, verification and truthful external-effect reporting.
- [x] **4.1-T6** Add focused positive/destructive-negative tests for rotation, failed qualification, exactly-one retention, large assets, secret exclusions, preview/apply and restore rollback.
- [x] **4.1-T7** Qualify exact PR head and exact merged-main Distribution CI, record evidence, close Slice 4.1 and stop before Slice 4.2.

### Exact evidence

- detailed evidence: `docs/SAFE-INFRASTRUCTURE-SLICE-4.1-LKG-RESTORE.md`;
- task-list commit: `487bbd7fe5eac1172e03756dbb2abe7338697894`;
- Distribution PR #30 qualified head: `0f5fd5fa0e5392957376ac8a679125f13dc2a11d`;
- Distribution merged main: `2fec4675287be748ae222efa61330bdaee37b0bc`;
- PR-head `Distribution CI` run `38317665390`: **SUCCESS**, six jobs;
- exact merged-main `Distribution CI` run `38318052035`: **SUCCESS**, six jobs;
- `Lifecycle Receipt Concurrency` run `38317665368`: **SUCCESS**;
- `Invisible Intelligence Scenarios A-F` run `38317665366`: **SUCCESS**.

Two broad PR gates exposed defects outside the Slice 4.1 diff/execution path and were deliberately not absorbed: bootstrap `--help` target-routing behavior (`38317665281`) and an existing first-run Core release-candidate OS `setup-required` result (`38317665472`). Neither enters the new installed recovery/LKG path.

### Validation discoveries

- Existing entrypoint regression coverage was corrected to require `RecoveryOrchestrator` while still proving it subclasses `CoreUpdateOrchestrator`.
- macOS and Windows exposed a physical-path canonicalization bug hidden on Linux; LKG root binding now canonicalizes at the recovery trust boundary.

### Acceptance criteria

- every currently shipped mutating installed Core `aiverse update` is LKG-guarded before parent mutation: **PASS**;
- future admitted structural mutation has a reusable LKG guard; no current shipped mutating `upgrade --apply` remains unguarded: **PASS**;
- candidate verified before previous LKG replacement: **PASS**;
- unhealthy/ambiguous/unrepresentable install cannot destroy sole LKG: **PASS**;
- exactly one retained LKG after successful rotation: **PASS**;
- canonical/user state required for recovery is durably represented: **PASS**;
- exact software RECONSTRUCT uses verified immutable exact-release evidence only: **PASS**;
- disposable/rebuildable material is not copied for cosmetic completeness: **PASS**;
- Workspace media/assets/outputs have explicit size-independent coverage: **PASS**;
- secrets/credentials follow explicit safe exclusion rather than blind copying: **PASS**;
- recovery material is private, immutable/non-live and non-canonical: **PASS**;
- `aiverse restore` is preview-only: **PASS**;
- restore preview reports coverage, exclusions and replacement risk: **PASS**;
- `aiverse restore --apply` restores and verifies declared local scope: **PASS**;
- failed restore has transaction-safe rollback/recovery-required behavior without destroying retained target: **PASS**;
- external/non-restorable effects are reported truthfully: **PASS**;
- existing owner-native update recovery remains authoritative for its narrower transaction: **PASS**;
- no duplicate transaction owner, canonical state store, generic backup service, Workspace relocation or structural upgrade orchestration was introduced: **PASS**;
- exact merged-main six-platform Distribution CI is green: **PASS**.

### Completion report

```text
Completed: Slice 4.1 - Implement one rotating Last-Known-Good recovery point and restore engine
Tasks: 7/7
Overall: 12/18 slices (66.7%)
Phase: Phase 4 - Implement Distribution orchestration and simple member UX
Phase progress: 1/4
Until Phase 5: 3 slices
Next: Slice 4.2 - Extend shipped update staging/activation around structural upgrade requirements
Blockers/drift/amendments: no Slice 4.1 blocker or protected-law amendment. Two unrelated pre-existing broad-gate defects remain separate.
```

### NEXT

**STOP after Slice 4.1 under the current one-at-a-time execution request.**

Next execution unit: Slice 4.2. Derive its adaptive task list only after fresh refs are fetched. No Slice 4.2 implementation was started here.
'''
roadmap = roadmap[:slice_start] + new_slice + roadmap[slice_end:]

pointer_marker = '# Current execution pointer\n'
pointer_start = roadmap.find(pointer_marker)
if pointer_start < 0:
    raise SystemExit('Current execution pointer not found')
old_pointer = roadmap[pointer_start:]
for needle in ['**Completed:** 11/18', '**Overall:** 61.1%', 'Phase 3', 'Slice 4.1']:
    if needle not in old_pointer:
        raise SystemExit(f'current pointer guard missing {needle!r}')

changelog = '''## 2026-10-13 - Slice 4.1 completed; Phase 4 recovery substrate operational

- Added one Distribution-owned rotating whole-install Last-Known-Good recovery point using the existing lifecycle transaction and private Distribution state.
- Added explicit CAPTURE / RECONSTRUCT / REBUILD / EXTERNAL-EXCLUDED coverage with large Workspace assets/outputs protected regardless of size and credential-shaped material excluded safely.
- Added exact software reconstruction through verified Git bundles bound to exact released receipt/catalog revisions.
- Guarded every currently shipped mutating installed Core update with LKG qualification before parent mutation while preserving no-op/update-plan behavior.
- Added read-only `aiverse restore` preview and explicit transaction-safe `aiverse restore --apply` with a separate rollback checkpoint and retained-target preservation.
- Landed Distribution PR #30 at `2fec4675287be748ae222efa61330bdaee37b0bc`.
- Qualified exact PR-head Distribution CI `38317665390` and exact merged-main Distribution CI `38318052035`, both successful across Ubuntu/macOS/Windows × Python 3.11/3.12.
- Corrected a real macOS/Windows physical-path canonicalization defect exposed by CI before merge.
- Isolated unrelated bootstrap-help and existing first-run release-candidate health defects instead of contaminating Slice 4.1 ownership/scope.
- Recorded detailed evidence in `docs/SAFE-INFRASTRUCTURE-SLICE-4.1-LKG-RESTORE.md`.

---

'''
if '## 2026-10-13 - Slice 4.1 completed; Phase 4 recovery substrate operational' in roadmap[:pointer_start]:
    raise SystemExit('Slice 4.1 changelog already exists')
roadmap = roadmap[:pointer_start] + changelog + '''# Current execution pointer

**Completed:** 12/18  
**Overall:** 66.7%  
**Phase:** Phase 4 - Implement Distribution orchestration and simple member UX  
**Phase progress:** 1/4  
**Until Phase 5:** 3 slices  
**Next:** STOP after Slice 4.1 under the one-at-a-time execution rule  
**Next Safe Infrastructure slice:** Slice 4.2 - Extend shipped update staging/activation around structural upgrade requirements  
**Next task:** none until Slice 4.2 starts and its adaptive task list is derived from fresh System/Distribution/owner refs  
**Blockers/drift/amendments:** no Slice 4.1 blocker or protected-law amendment. The canonical Phase 4 denominator is four slices; two unrelated pre-existing broad-gate defects remain separate from the LKG/restore implementation.
'''

roadmap_path.write_text(roadmap, encoding='utf-8')
evidence_path.write_text(evidence, encoding='utf-8')
