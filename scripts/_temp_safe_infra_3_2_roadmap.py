from pathlib import Path
import re
import subprocess

path = Path('docs/SAFE-INFRASTRUCTURE-UPGRADE-AND-RECOVERY-IMPLEMENTATION-PLAN.md')
text = path.read_text(encoding='utf-8')
message = subprocess.check_output(['git', 'log', '-1', '--pretty=%s'], text=True).strip()

if message != 'TEMP run Safe Infrastructure Slice 3.2 closure':
    raise SystemExit(f'unexpected trigger for closure helper: {message}')

old_header = '''**Status:** PAUSED - PHASE 3 IN PROGRESS; SLICE 3.1 COMPLETE  
**Canonical planning repo:** `aiverse-filmmakers/AI-Verse-System`  
**Primary orchestration repo:** `aiverse-filmmakers/ai-verse-distribution`  
**Initial owner repos:** `aiverse-filmmakers/AI-Verse-OS`, `aiverse-filmmakers/AI-Verse-Skills`  
**Started:** 2026-10-12  
**Planning method:** `docs/ADAPTIVE-IMPLEMENTATION-PLANNING-SKILL.md`  
**Program size:** 18 slices  
**Completed:** 8  
**Remaining:** 10  
**Overall progress:** 44.4%  
**Current phase:** Phase 3 - Implement canonical owner migrations for proven motivating problems  
**Current phase progress:** 1/4  
**Slices until Phase 4:** 3  
**Next:** Slice 3.2 - Implement admitted OS Workspace migration/reference repair only if required  
**Next slice task list:** STOP - derive only when Slice 3.2 starts'''
new_header = '''**Status:** PAUSED - PHASE 3 IN PROGRESS; SLICE 3.2 COMPLETE  
**Canonical planning repo:** `aiverse-filmmakers/AI-Verse-System`  
**Primary orchestration repo:** `aiverse-filmmakers/ai-verse-distribution`  
**Initial owner repos:** `aiverse-filmmakers/AI-Verse-OS`, `aiverse-filmmakers/AI-Verse-Skills`  
**Started:** 2026-10-12  
**Planning method:** `docs/ADAPTIVE-IMPLEMENTATION-PLANNING-SKILL.md`  
**Program size:** 18 slices  
**Completed:** 9  
**Remaining:** 9  
**Overall progress:** 50.0%  
**Current phase:** Phase 3 - Implement canonical owner migrations for proven motivating problems  
**Current phase progress:** 2/4  
**Slices until Phase 4:** 2  
**Next:** Slice 3.3 - Implement cross-provider capability scope semantics and managed Skills generation alignment  
**Next slice task list:** STOP - derive only when Slice 3.3 starts'''
if text.count(old_header) != 1:
    raise SystemExit(f'header guard failed: expected one Slice 3.1 header, found {text.count(old_header)}')
text = text.replace(old_header, new_header, 1)

old_phase = '''**Phase size:** 4 slices  
**Status:** IN PROGRESS  
**Phase progress:** 1/4'''
new_phase = '''**Phase size:** 4 slices  
**Status:** IN PROGRESS  
**Phase progress:** 2/4'''
if text.count(old_phase) != 1:
    raise SystemExit(f'Phase 3 guard failed: found {text.count(old_phase)}')
text = text.replace(old_phase, new_phase, 1)

old_slice = '''## Slice 3.2 - Implement admitted OS Workspace migration/reference repair only if required

**Status:** IN PROGRESS  
**Dependencies:** 3.1  
**Adaptive tasks:** 3/5 COMPLETE

### Refreshed refs

- `aiverse-filmmakers/AI-Verse-System@ed98c92028dc7b0659ffb11a237976e924705034`
- `aiverse-filmmakers/AI-Verse-OS@88ce41a95554e1323ba34aa71b536b9e98475808`
- `aiverse-filmmakers/AI-Verse-Data@f8978f8f7a1bc94edecddc2662112233289159a3`
- `aiverse-filmmakers/AI-Verse-Brain@69f7912eeb35f0178f6952ff0554aec8d7f2c496`
- `aiverse-filmmakers/AI-Verse-Memory@f1327be48ba2ee0043959021365e6dbb9dcb1d3a`

### Derived task list

- [x] **3.2-T1** Refresh System, OS, Data, Brain and Memory refs and re-read the canonical durable-identity/Workspace law plus Slice 3.1 generation contract.
- [x] **3.2-T2** Reverify every proven path-coupled Workspace consumer and determine whether any owner now exposes an alternate admitted Workspace location, locator/registry, source generation or relocation contract.
- [x] **3.2-T3** Decide from owner evidence whether a Workspace migration/reference-repair operation is actually required. If no alternate admitted source/target exists, explicitly classify relocation as not admitted and do not create mutation code merely to satisfy the roadmap example.
- [ ] **3.2-T4** Prove reference repair and writable-slot retirement are not required when no path changes, and prove unsupported nested/misplaced/custom layouts continue to fail closed through the OS structural detector rather than being auto-moved.
- [ ] **3.2-T5** Record exact evidence and conditional acceptance results, validate the unchanged owner contracts/current System state, close Slice 3.2, and stop before Slice 3.3.

A physical Workspace relocation is conditional, not presumed.

If the canonical Identity Hardening/System contract keeps `workspaces/<id>` as the supported physical slot and no real migration requires a move, this slice must not invent a relocation. It may instead implement only genuinely required OS-owned structural migration/reference repair.

If a later canonical contract admits relocatable Workspace storage, the owner migration must preserve the Workspace ID and repair the complete owner-declared reference graph before retiring the old writable route.

### Acceptance criteria

- migration is idempotent;
- files/content are preserved;
- owner-defined Workspace identity continuity rules are satisfied;
- affected owner references are repaired or proven unaffected;
- no supported owner is left resolving only a retired slot;
- old writable structure retires only after verification;
- ambiguous/custom layouts fail safely or require practical user review;
- default output explains practical effect without exposing internal paths unless details are requested.

### NEXT

Slice 3.3.
'''
new_slice = '''## Slice 3.2 - Implement admitted OS Workspace migration/reference repair only if required

**Status:** COMPLETE - MIGRATION NOT REQUIRED UNDER CURRENT CANONICAL ARCHITECTURE  
**Dependencies:** 3.1  
**Adaptive tasks:** 5/5 COMPLETE

### Refreshed refs

- `aiverse-filmmakers/AI-Verse-System@ed98c92028dc7b0659ffb11a237976e924705034`
- task-list commit: `aiverse-filmmakers/AI-Verse-System@8fe317453fd4f535d9cc1954e6a4f803008c2dbc`
- `aiverse-filmmakers/AI-Verse-OS@88ce41a95554e1323ba34aa71b536b9e98475808`
- `aiverse-filmmakers/AI-Verse-Data@f8978f8f7a1bc94edecddc2662112233289159a3`
- `aiverse-filmmakers/AI-Verse-Brain@69f7912eeb35f0178f6952ff0554aec8d7f2c496`
- `aiverse-filmmakers/AI-Verse-Memory@f1327be48ba2ee0043959021365e6dbb9dcb1d3a`

### Final derived task list

- [x] **3.2-T1** Refresh System, OS, Data, Brain and Memory refs and re-read the canonical durable-identity/Workspace law plus Slice 3.1 generation contract.
- [x] **3.2-T2** Reverify every proven path-coupled Workspace consumer and determine whether any owner now exposes an alternate admitted Workspace location, locator/registry, source generation or relocation contract.
- [x] **3.2-T3** Decide from owner evidence whether a Workspace migration/reference-repair operation is actually required. If no alternate admitted source/target exists, explicitly classify relocation as not admitted and do not create mutation code merely to satisfy the roadmap example.
- [x] **3.2-T4** Prove reference repair and writable-slot retirement are not required when no path changes, and prove unsupported nested/misplaced/custom layouts continue to fail closed through the OS structural detector rather than being auto-moved.
- [x] **3.2-T5** Record exact evidence and conditional acceptance results, validate the unchanged owner contracts/current System state, close Slice 3.2, and stop before Slice 3.3.

### Decision

No Workspace relocation/move/reference-repair handler is admitted or required by the current canonical architecture.

The only supported physical Workspace slot remains `workspaces/<workspace-id>`, derived from canonical `WORKSPACE.yaml:id`. The System identity contract explicitly states that current OS, Brain, Memory and Data integrations intentionally derive this slot and that arbitrary/nested relocation is unsupported. No ID-to-location resolver, alternate admitted Workspace location or older owner generation exists that can be migrated safely into `workspace-id-slot-v1`.

Creating a relocation engine here would therefore invent a new architecture instead of implementing a proven migration. Slice 3.2 deliberately makes no owner code change.

### Reference-consumer proof

Current refs were rechecked directly:

- OS current-context resolution derives `workspaces/<id>/context/CURRENT.md` and requires the expected real physical slot;
- OS Workspace capability resolution derives `workspaces/<id>/skills/` beneath the real workspaces root;
- Data derives `workspaces/<id>/WORKSPACE.yaml` and `workspaces/<id>/data/ai-verse-data.sqlite`, failing closed on ID/slot mismatch;
- Brain direction ownership derives Workspace current-context sources/targets from `workspaces/<id>/context/CURRENT.md`;
- Memory discovers direct-child Workspaces and stores native Workspace atomic memory under `workspaces/<id>/memory/atomic/`.

No owner is resolving a deprecated alternate location. Because no path changes and no writable route retires, cross-owner reference repair is proven unnecessary for this slice.

### Fail-closed proof

The existing OS Slice 3.1 destructive-negative tests already prove that nested/domain-first Workspace manifests, identity/slot mismatch, duplicate identity evidence, symlinked slots, missing manifests and invalid identity return review/failure without relocation or mutation. The detector snapshots the filesystem before and after every scenario and asserts exact equality.

Unsupported structures therefore remain `BLOCKED/REVIEW`; they are not treated as hidden migration instructions.

### Exact evidence

Detailed decision evidence:

- `docs/SAFE-INFRASTRUCTURE-SLICE-3.2-WORKSPACE-MIGRATION-DECISION.md`;
- evidence commit: `aiverse-filmmakers/AI-Verse-System@7274500ca9c4d94d46513b9d0a9c3a1ac5de1c18`.

No OS, Data, Brain or Memory source changed in this slice.

### Acceptance criteria

- migration is idempotent: **NOT APPLICABLE** because no owner migration is admitted; repeated structural detection is read-only;
- files/content are preserved: **PASS**, no Workspace state is moved, rewritten or deleted;
- owner-defined Workspace identity continuity rules are satisfied: **PASS**, the existing `WORKSPACE.yaml:id` / `workspaces/<id>` contract remains intact;
- affected owner references are repaired or proven unaffected: **PASS**, proven unaffected because no path/identity changes occur;
- no supported owner is left resolving only a retired slot: **PASS**, no slot is retired;
- old writable structure retires only after verification: **NOT APPLICABLE**, there is no admitted old Workspace route to retire;
- ambiguous/custom layouts fail safely or require practical user review: **PASS** through the OS `BLOCKED/REVIEW` detector behavior;
- default output explains practical effect without exposing internal paths unless details are requested: **NO NEW MEMBER-FACING MIGRATION SURFACE REQUIRED** because there is no migration operation; aggregate member UX remains a later Distribution slice.

### Completion report

```text
Completed: Slice 3.2 - Implement admitted OS Workspace migration/reference repair only if required
Result: no migration required; no owner mutation introduced
Tasks: 5/5
Overall: 9/18 slices (50.0%)
Phase: Phase 3 - Implement canonical owner migrations for proven motivating problems
Phase progress: 2/4
Until next phase: 2 slices
Next: Slice 3.3 - Implement cross-provider capability scope semantics and managed Skills generation alignment
Blockers/drift/amendments: none. Arbitrary Workspace relocation remains intentionally unsupported under the canonical identity/storage contract.
```

### NEXT

**STOP after Slice 3.2 for the current one-at-a-time execution request.**

Next execution unit: Slice 3.3. Derive its adaptive task list only after fresh OS/Skills/System refs are fetched. No Slice 3.3 scope-placement or Skills-generation work was started here.
'''
if text.count(old_slice) != 1:
    raise SystemExit(f'Slice 3.2 closure guard failed: expected one in-progress block, found {text.count(old_slice)}')
text = text.replace(old_slice, new_slice, 1)

changelog = '''## 2026-10-12 - Slice 3.2 completed; Workspace relocation not required

- Refreshed System, OS, Data, Brain and Memory refs and rechecked the canonical Workspace identity/storage law.
- Reverified every proven path-coupled Workspace consumer against current owner source.
- Confirmed all supported consumers intentionally derive the same `workspaces/<id>` slot and no alternate locator/registry or admitted source generation exists.
- Confirmed the canonical System identity contract explicitly keeps arbitrary/nested Workspace relocation unsupported.
- Reused Slice 3.1 destructive-negative evidence proving nested/misplaced/custom ambiguity fails closed without automatic relocation or mutation.
- Proved reference repair is unnecessary because no path or identity changes and no writable route retires.
- Made no OS/Data/Brain/Memory source changes and created no compatibility route for an invented location model.
- Recorded detailed evidence in `docs/SAFE-INFRASTRUCTURE-SLICE-3.2-WORKSPACE-MIGRATION-DECISION.md` at `7274500ca9c4d94d46513b9d0a9c3a1ac5de1c18`.

'''
marker = '\n---\n\n# Current execution pointer\n'
if text.count(marker) != 1:
    raise SystemExit(f'changelog insertion guard failed: found {text.count(marker)}')
text = text.replace(marker, '\n' + changelog + '---\n\n# Current execution pointer\n', 1)

pointer_pattern = re.compile(r'# Current execution pointer\n.*\Z', re.S)
if len(pointer_pattern.findall(text)) != 1:
    raise SystemExit('current execution pointer guard failed')
pointer = '''# Current execution pointer

**Completed:** 9/18  
**Overall:** 50.0%  
**Phase:** Phase 3 - Implement canonical owner migrations for proven motivating problems  
**Phase progress:** 2/4  
**Until Phase 4:** 2 slices  
**Next:** STOP after Slice 3.2 under the one-at-a-time execution rule  
**Next Safe Infrastructure slice:** Phase 3 / Slice 3.3 - Implement cross-provider capability scope semantics and managed Skills generation alignment  
**Next task:** none until Slice 3.3 starts and its adaptive task list is derived from fresh OS/Skills/System refs  
**Blockers/drift/amendments:** none. Slice 3.2 proved no Workspace relocation migration is currently admitted or required; current owner path consumers remain aligned and no writable route was retired.
'''
text = pointer_pattern.sub(pointer, text, count=1)

path.write_text(text, encoding='utf-8')
