from pathlib import Path
import subprocess

path = Path('docs/SAFE-INFRASTRUCTURE-UPGRADE-AND-RECOVERY-IMPLEMENTATION-PLAN.md')
text = path.read_text(encoding='utf-8')
message = subprocess.check_output(['git', 'log', '-1', '--pretty=%s'], text=True).strip()

if message != 'TEMP run Safe Infrastructure Slice 3.4 closure':
    raise SystemExit(f'unexpected trigger for Slice 3.4 closure helper: {message}')

replacements = {
    '**Status:** PAUSED - PHASE 3 IN PROGRESS; SLICE 3.3 COMPLETE  \n': '**Status:** PAUSED - PHASE 3 COMPLETE; PHASE 4 NOT STARTED  \n',
    '**Completed:** 10  \n': '**Completed:** 11  \n',
    '**Remaining:** 8  \n': '**Remaining:** 7  \n',
    '**Overall progress:** 55.6%  \n': '**Overall progress:** 61.1%  \n',
    '**Current phase:** Phase 3 - Implement canonical owner migrations for proven motivating problems  \n': '**Current phase:** Phase 3 - Implement canonical owner migrations for proven motivating problems - COMPLETE  \n',
    '**Current phase progress:** 3/4  \n': '**Current phase progress:** 4/4 COMPLETE  \n',
    '**Slices until Phase 4:** 1  \n': '**Slices until Phase 4:** 0  \n',
    '**Next:** Slice 3.4 - Implement admitted capability promotion/re-scoping and reference repair  \n': '**Next:** Phase 4 / Slice 4.1 - Implement one rotating Last-Known-Good recovery point and restore engine  \n',
    '**Next slice task list:** STOP - derive only when Slice 3.4 starts\n': '**Next slice task list:** STOP - derive only when Phase 4 / Slice 4.1 starts\n',
    '# Phase 3 - Implement canonical owner migrations for proven motivating problems\n\n**Phase size:** 4 slices  \n**Status:** IN PROGRESS  \n**Phase progress:** 3/4': '# Phase 3 - Implement canonical owner migrations for proven motivating problems\n\n**Phase size:** 4 slices  \n**Status:** COMPLETE  \n**Phase progress:** 4/4 COMPLETE',
}

for old, new in replacements.items():
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'guard failed for roadmap replacement; expected one occurrence, found {count}: {old!r}')
    text = text.replace(old, new, 1)

slice_start_marker = '## Slice 3.4 - Implement admitted capability promotion/re-scoping and reference repair\n'
phase4_marker = '\n---\n\n# Phase 4 - Implement Distribution orchestration and simple member UX\n'
start = text.find(slice_start_marker)
end = text.find(phase4_marker, start)
if start < 0 or end < 0:
    raise SystemExit('could not locate the guarded Slice 3.4 section boundaries')
old_slice = text[start:end]
required_slice_evidence = [
    '**Status:** NOT STARTED',
    '**Dependencies:** 3.3',
    'migration/promotion is owner-controlled and idempotent;',
    'consumers/references continue resolving through admitted reference repair or explicit compatibility;',
    'duplicate canonical copies are not created accidentally;',
]
for needle in required_slice_evidence:
    if needle not in old_slice:
        raise SystemExit(f'Slice 3.4 guard failed; missing expected text: {needle}')

new_slice = '''## Slice 3.4 - Implement admitted capability promotion/re-scoping and reference repair

**Status:** COMPLETE  
**Dependencies:** 3.3  
**Adaptive tasks:** 7/7 COMPLETE

### Final implementation decision

The admitted migration is deliberately narrow: an existing user-owned Workspace capability may be promoted into the user-owned personal `local` provider when the member wants reuse beyond one Workspace.

The provider change creates a new qualified identity. For example, `workspace:alpha:transcript-book` and `local:transcript-book` are not the same identity. OS records an explicit `promoted-to` relationship, preserves the original package as non-live history, and repairs exact old qualified-ID consumers through validated promotion compatibility evidence. Matching names or bytes never establish identity continuity.

Managed `aiverse-skills` and OS built-ins remain outside this personal promotion path. Skills continues owning its managed immutable generations and lifecycle unchanged.

### Final adaptive task list

- [x] **3.4-T1** Refresh System, OS and Skills refs and re-read Slice 3.4, the durable identity law, provider contract, placement planner, resolver and current managed Skills boundary.
- [x] **3.4-T2** Inventory actual qualified-ID consumers/reference surfaces and prove the current resolver exact-selection boundary is the narrowest admitted compatibility-repair surface; no canonical cross-owner durable user-capability reference database exists to batch-rewrite.
- [x] **3.4-T3** Freeze Workspace -> local semantics before implementation: new qualified identity, digest/generation-bound preview, provenance/history preservation, exact-ID compatibility repair, managed/OS sources blocked and fail-closed conflict/drift behavior.
- [x] **3.4-T4** Implement the OS-owned promotion plan/apply transaction with verified staging, target conflict checks, source-drift invalidation, source-history preservation, deterministic receipt metadata, source live-route retirement only after target verification and idempotent replay/recovery behavior.
- [x] **3.4-T5** Extend explicit qualified-ID selection to consume only validated active promotion compatibility records and add the mandatory cross-context YouTube transcript/book fixture plus destructive-negative tests.
- [x] **3.4-T6** Document the owner boundary and validate exact current OS/Skills behavior without modifying Skills because no managed-provider lifecycle defect was found.
- [x] **3.4-T7** Record exact commits and CI evidence, close all Slice 3.4 acceptance criteria, complete Safe Infrastructure Phase 3 and stop before Phase 4 / Slice 4.1.

### Exact evidence

Detailed evidence:

- `docs/SAFE-INFRASTRUCTURE-SLICE-3.4-CAPABILITY-PROMOTION.md`;
- task-list commit: `aiverse-filmmakers/AI-Verse-System@84afaa49a77bc8c9869a0172e13f2c9f61718ddc`;
- evidence closure commit: `aiverse-filmmakers/AI-Verse-System@47b636eb7ce7d6ba16832ff79e399552bb2a1232`.

OS implementation:

- exact head: `aiverse-filmmakers/AI-Verse-OS@470ad89e6b96d898161dee36d4e4fa8064dd6a8d`;
- `Capability Placement Contract` run `38306623956`: **SUCCESS**;
- `Repository QC` run `38306623950`: **SUCCESS** across `qc`, `adapter-integration` and `skills-provider-integration`.

Skills independent validation:

- exact unchanged head: `aiverse-filmmakers/AI-Verse-Skills@d4a02888ba8d83c4a15ce1b538ffdafaaf83bee1`;
- `Validate AI-Verse Skills` run `38298548847`: **SUCCESS**;
- `Release Descriptor` run `38298549229`: **SUCCESS**;
- no Skills source change was required.

### Mandatory fixture result

The cross-context transcript/book fixture proves that a private Workspace package can be promoted for reuse without silent identity continuity or data loss:

- Workspace `beta` cannot directly consume Workspace `alpha`'s private source before promotion;
- preview binds the exact Workspace generation/digest and targets `local:transcript-book`;
- complete custom package content survives byte-for-byte;
- target is staged and digest-verified before source retirement;
- original source survives in hidden non-live promotion history;
- the old Workspace-qualified ID resolves from another context only through an active validated `promoted-to` compatibility relationship to the real local identity;
- discovery exposes only the current local capability, not a duplicate old canonical copy;
- replay is a no-op;
- source drift, different target content, wrong owning context, managed sources and unsafe symlink-bearing packages fail closed without silent overwrite/promotion.

### Acceptance criteria

- migration/promotion is owner-controlled and idempotent: **PASS**;
- source/destination identity relationship follows the canonical Identity contract: **PASS**, provider change creates a different qualified identity and every promotion record states `qualified_identity_preserved: false`;
- provenance/history survives: **PASS**, through digest-bound receipt plus non-live source history containing the complete original package;
- consumers/references continue resolving through admitted reference repair or explicit compatibility: **PASS**, exact retired Workspace-qualified requests may use only validated active OS promotion evidence to select the real local target;
- duplicate canonical copies are not created accidentally: **PASS**, the live Workspace route retires only after verified target publication and hidden history is not a provider candidate;
- ambiguous user-created/local-only capabilities are not silently promoted: **PASS**, promotion is explicit and conflicts/drift/unsupported sources fail closed;
- custom files survive: **PASS**;
- stale plans fail before admitted source retirement: **PASS**;
- managed Skills ownership/lifecycle remains unchanged: **PASS**;
- no generic identity registry, Workspace relocation, distributed publication path or broad provider-migration framework was introduced: **PASS**.

### Phase 3 closure

Phase 3 is complete at 4/4 slices. It established the current OS Workspace generation, proved Workspace relocation is not presently admitted/required, implemented practical provider placement semantics, and implemented the one proven cross-provider Workspace-to-personal promotion with explicit new identity, provenance/history preservation and compatibility repair.

No protected-law amendment was required.

### Completion report

```text
Completed: Slice 3.4 - Implement admitted capability promotion/re-scoping and reference repair
Tasks: 7/7
Overall: 11/18 slices (61.1%)
Phase: Phase 3 - Implement canonical owner migrations for proven motivating problems
Phase progress: 4/4 COMPLETE
Until next phase: 0 slices
Next: Phase 4 / Slice 4.1 - Implement one rotating Last-Known-Good recovery point and restore engine
Blockers/drift/amendments: none. Provider changes remain identity-changing; compatibility is explicit and evidence-bound. Skills lifecycle ownership remains unchanged.
```

### NEXT

**STOP after Slice 3.4 under the current one-at-a-time execution request.**

Next execution unit: Phase 4 / Slice 4.1. Derive its adaptive task list only after fresh System/Distribution/owner refs are fetched. No Phase 4 implementation was started here.
'''

text = text[:start] + new_slice + text[end:]

pointer_marker = '# Current execution pointer\n'
pointer_start = text.find(pointer_marker)
if pointer_start < 0:
    raise SystemExit('current execution pointer not found')
old_pointer = text[pointer_start:]
for needle in ['**Completed:** 10/18', '**Overall:** 55.6%', '**Phase progress:** 3/4', 'Slice 3.4']:
    if needle not in old_pointer:
        raise SystemExit(f'current pointer guard failed; missing {needle}')

changelog = '''## 2026-10-12 - Slice 3.4 completed; Phase 3 complete

- Added the OS-owned evidence-bound Workspace-to-personal capability promotion transaction without creating a generic provider migration framework.
- Kept provider changes identity-changing under the canonical Identity contract; promotion records an explicit old-qualified-ID -> new-qualified-ID relationship with `qualified_identity_preserved: false`.
- Staged and digest-verified the complete target before retiring the live Workspace route, preserving the original package as hidden non-live promotion history.
- Added exact retired-ID compatibility repair through validated active OS promotion receipts while discovery exposes only the real current local capability.
- Added the mandatory cross-context transcript/book fixture plus stale-plan, conflict, wrong-context, managed-source, replay and unsafe-filesystem negative coverage.
- Landed OS implementation at `470ad89e6b96d898161dee36d4e4fa8064dd6a8d` and qualified `Capability Placement Contract` run `38306623956` plus `Repository QC` run `38306623950` as successful.
- Revalidated unchanged Skills head `d4a02888ba8d83c4a15ce1b538ffdafaaf83bee1` with `Validate AI-Verse Skills` run `38298548847` and `Release Descriptor` run `38298549229`, both successful.
- Recorded detailed evidence in `docs/SAFE-INFRASTRUCTURE-SLICE-3.4-CAPABILITY-PROMOTION.md` at `47b636eb7ce7d6ba16832ff79e399552bb2a1232`.
- Completed Safe Infrastructure Phase 3 at 4/4 slices without a protected-law amendment.

---

'''

if '## 2026-10-12 - Slice 3.4 completed; Phase 3 complete' in text[:pointer_start]:
    raise SystemExit('Slice 3.4 changelog entry already exists')
text = text[:pointer_start] + changelog + '''# Current execution pointer

**Completed:** 11/18  
**Overall:** 61.1%  
**Phase:** Phase 3 - Implement canonical owner migrations for proven motivating problems - COMPLETE  
**Phase progress:** 4/4 COMPLETE  
**Until Phase 4:** 0 slices  
**Next:** STOP after Slice 3.4 under the one-at-a-time execution rule  
**Next Safe Infrastructure slice:** Phase 4 / Slice 4.1 - Implement one rotating Last-Known-Good recovery point and restore engine  
**Next task:** none until Phase 4 / Slice 4.1 starts and its adaptive task list is derived from fresh System/Distribution/owner refs  
**Blockers/drift/amendments:** none. Slice 3.4 admitted only evidence-bound Workspace-to-personal promotion, preserved provider-qualified identity law and left managed Skills lifecycle ownership unchanged.
'''

path.write_text(text, encoding='utf-8')
