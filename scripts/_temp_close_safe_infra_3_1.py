from pathlib import Path
import re

path = Path('docs/SAFE-INFRASTRUCTURE-UPGRADE-AND-RECOVERY-IMPLEMENTATION-PLAN.md')
text = path.read_text(encoding='utf-8')

old_header = '''**Status:** PAUSED - PHASE 2 COMPLETE; NEXT PHASE 3 / SLICE 3.1  
**Canonical planning repo:** `aiverse-filmmakers/AI-Verse-System`  
**Primary orchestration repo:** `aiverse-filmmakers/ai-verse-distribution`  
**Initial owner repos:** `aiverse-filmmakers/AI-Verse-OS`, `aiverse-filmmakers/AI-Verse-Skills`  
**Started:** 2026-10-12  
**Planning method:** `docs/ADAPTIVE-IMPLEMENTATION-PLANNING-SKILL.md`  
**Program size:** 18 slices  
**Completed:** 7  
**Remaining:** 11  
**Overall progress:** 38.9%  
**Current phase:** Phase 2 - COMPLETE  
**Current phase progress:** 3/3 COMPLETE  
**Slices until Phase 3:** 0  
**Next:** Phase 3 / Slice 3.1 - Implement OS Workspace generation and evidence-backed structural semantics  
**Next slice task list:** STOP - derive only when Slice 3.1 starts'''
new_header = '''**Status:** PAUSED - PHASE 3 IN PROGRESS; SLICE 3.1 COMPLETE  
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
if text.count(old_header) != 1:
    raise SystemExit('header guard failed: expected exactly one Phase 2 completion header')
text = text.replace(old_header, new_header, 1)

old_phase = '''**Phase size:** 4 slices  
**Status:** NOT STARTED  
**Phase progress:** 0/4'''
new_phase = '''**Phase size:** 4 slices  
**Status:** IN PROGRESS  
**Phase progress:** 1/4'''
if text.count(old_phase) != 1:
    raise SystemExit('Phase 3 guard failed: expected exactly one NOT STARTED header')
text = text.replace(old_phase, new_phase, 1)

slice31 = '''## Slice 3.1 - Implement OS Workspace generation and evidence-backed structural semantics

**Status:** COMPLETE  
**Dependencies:** 2.3 plus canonical Identity Hardening contract  
**Adaptive tasks:** 6/6 COMPLETE

### Starting refs

- `aiverse-filmmakers/AI-Verse-System@563659432d8609f908b44fae676f10496d47ec96`
- `aiverse-filmmakers/AI-Verse-OS@64f7325444d18f94c9d4755d32eb89f3468bda6b`
- slice-start task-list commit: `aiverse-filmmakers/AI-Verse-System@ddd51191b54498db45c924762b90074ff7ecc2e2`

### Final derived task list

- [x] **3.1-T1** Refresh System/OS refs and inspect current Workspace schema, owner primitive, template/readme, tests, release descriptor and Phase 2 infrastructure contract.
- [x] **3.1-T2** Define one OS-owned current Workspace infrastructure generation and fail-closed structural detection semantics that preserve `workspaces/<id>` and do not treat optional/custom content as drift.
- [x] **3.1-T3** Implement a read-only OS Workspace infrastructure detector plus concise owner architecture documentation; reuse the shipped Workspace owner rather than creating a second creation/migration subsystem.
- [x] **3.1-T4** Add destructive-negative tests proving current direct-child Workspaces pass, custom files survive classification, semantic domain metadata does not affect physical generation, identity/path conflicts fail closed, unsupported nested relocation is not silently accepted, and detection performs no mutation.
- [x] **3.1-T5** Integrate the detector into exact OS validation/CI and decide from evidence whether the current release descriptor can truthfully publish the generation now or must defer publication to the next admitted descriptor revision.
- [x] **3.1-T6** Run exact-ref OS CI, record implementation/evidence refs, update the canonical Safe Infrastructure roadmap, and close Slice 3.1 only if every acceptance criterion passes. Stop before Slice 3.2.

### Implementation

Canonical OS implementation:

- `aiverse-filmmakers/AI-Verse-OS@88ce41a95554e1323ba34aa71b536b9e98475808`.

Added:

- `system/architecture/workspace-infrastructure.md`;
- `scripts/workspace-infrastructure.mjs`;
- `scripts/test-workspace-infrastructure.mjs`;
- `.github/workflows/workspace-infrastructure.yml`.

The shipped `scripts/workspace-owner.mjs` remains the canonical create/evolve primitive. Slice 3.1 did not create a second mutation or migration subsystem.

### Current Workspace generation

OS now owns the current machine generation:

```text
workspace-id-slot-v1
```

A Workspace is current when it is a real direct child of `workspaces/`, its slot is a valid Workspace ID, it contains a real readable `WORKSPACE.yaml`, the manifest ID is valid and exactly matches the slot, identity evidence is not duplicated/conflicting, and there is no nested `WORKSPACE.yaml` implying unsupported nested/relocated Workspace storage.

`workspaces/_template/` is not a real Workspace. Zero real Workspaces is a valid current structure.

Generation is deliberately not template completeness. Missing optional folders, custom user files/directories, Workspace assets/outputs and semantic `type`/`domains` metadata do not make an otherwise valid Workspace stale.

### Read-only structural detector

Owner operation:

```text
node scripts/workspace-infrastructure.mjs detect --root <AI-Verse-root>
```

It emits `ai-verse.workspace-infrastructure-status/v1`, owner `ai-verse-os`, current generation `workspace-id-slot-v1`, per-Workspace observations, machine findings, aggregate `CURRENT` or `BLOCKED/REVIEW`, and `mutated: false`.

It fails closed on symlinked Workspace storage, missing/unreadable manifests, invalid IDs, ID/slot mismatch, duplicate identity evidence and unsupported nested Workspace manifests. It never creates, moves, deletes, normalizes or repairs Workspace state.

### Release-descriptor decision

The currently accepted OS `release/component-release.json` is exact-revision-bound to:

```text
9600929b946746c25c64e48471fcc83031fddda9
```

That accepted revision predates the Slice 3.1 detector. Rewriting the descriptor now to claim `workspace-id-slot-v1` while retaining its older exact revision would make release evidence false.

Therefore `migration.infrastructure` publication is deferred to the next properly admitted OS component-release descriptor/revision where the detector and generation contract exist at the descriptor-bound revision. This is truthful evidence preservation, not a blocker or protected-law amendment.

### Exact evidence

Detailed System evidence:

- `docs/SAFE-INFRASTRUCTURE-SLICE-3.1-WORKSPACE-GENERATION.md`;
- evidence closure commit: `aiverse-filmmakers/AI-Verse-System@fd2a9e68f90e6a1ccb6991f03e10dcd2b45744ef`.

OS exact implementation ref:

- `aiverse-filmmakers/AI-Verse-OS@88ce41a95554e1323ba34aa71b536b9e98475808`.

Canonical `main` push validation:

- `Workspace Infrastructure Contract` run `38287690112`: **SUCCESS**;
- detector syntax: **SUCCESS**;
- existing Workspace owner regression: **SUCCESS**;
- generation/fail-closed destructive-negative tests: **SUCCESS**;
- read-only checkout verification: **SUCCESS**;
- `Repository QC` run `38287690162`: **SUCCESS** across `qc`, `adapter-integration` and `skills-provider-integration`.

Additional existing OS push workflows on the same exact SHA also completed successfully, including Update Request, migration concurrency, direction ownership, Brain permission, write-command boundary and multi-repo/public-beta acceptance workflows.

### Preservation and ownership result

- OS owns the structural rule and detector;
- Distribution was not changed and does not infer Workspace hierarchy;
- logical identity remains `WORKSPACE.yaml:id`;
- current supported physical slot remains `workspaces/<id>`;
- unknown/custom content remains preserved;
- domain/category organization remains semantic metadata;
- arbitrary relocation remains unsupported;
- no migration, move, cleanup or reference repair was implemented in this slice.

### Acceptance criteria

- OS owns the rule, not Distribution: **PASS**;
- Workspace ID/storage semantics follow the canonical identity contract: **PASS**;
- current `workspaces/<id>` compatibility is preserved: **PASS**;
- user custom structure is not blindly normalized: **PASS**;
- ambiguous/unsupported structure fails closed for review instead of guesswork: **PASS**;
- no relocation engine was created merely to satisfy the original roadmap example: **PASS**;
- structural detection is read-only with executable negative proof: **PASS**;
- accepted release metadata remains truthful instead of being rewritten against a stale exact revision: **PASS**.

### Completion report

```text
Completed: Slice 3.1 - Implement OS Workspace generation and evidence-backed structural semantics
Tasks: 6/6
Overall: 8/18 slices (44.4%)
Phase: Phase 3 - Implement canonical owner migrations for proven motivating problems
Phase progress: 1/4
Until next phase: 3 slices
Next: Slice 3.2 - Implement admitted OS Workspace migration/reference repair only if required
Blockers/drift/amendments: none. Descriptor publication deferred truthfully to the next admitted OS release descriptor revision; no protected-law amendment.
```

### NEXT

**STOP after Slice 3.1 for the current one-at-a-time execution request.**

Next execution unit: Slice 3.2. Derive its adaptive task list only after fresh System/OS/reference-consumer refs are fetched. No Slice 3.2 migration, relocation or reference-repair work was started here.
'''

pattern = re.compile(
    r'## Slice 3\.1 - Implement OS Workspace generation and evidence-backed structural semantics\n.*?\n---\n\n## Slice 3\.2 - Implement admitted OS Workspace migration/reference repair only if required',
    re.S,
)
matches = pattern.findall(text)
if len(matches) != 1:
    raise SystemExit(f'Slice 3.1 guard failed: expected one slice block, found {len(matches)}')
text = pattern.sub(
    slice31 + '\n---\n\n## Slice 3.2 - Implement admitted OS Workspace migration/reference repair only if required',
    text,
    count=1,
)

changelog = '''## 2026-10-12 - Slice 3.1 completed; OS Workspace generation defined

- Reused OS's conservative Workspace owner/schema instead of creating a second Workspace mutation subsystem.
- Added OS-owned current generation `workspace-id-slot-v1` and read-only detector `scripts/workspace-infrastructure.mjs`.
- Kept `WORKSPACE.yaml:id` as canonical logical identity and `workspaces/<id>` as the current supported physical slot.
- Defined structural generation as identity/storage conformance rather than full template-tree equality, so optional folders and legitimate custom/user content do not create false drift.
- Added fail-closed handling for symlinks, missing/unreadable manifests, invalid IDs, ID/slot conflicts, duplicate identity evidence and unsupported nested Workspace manifests.
- Added destructive-negative tests proving detection is read-only and does not relocate or normalize unsupported structures.
- Landed implementation on OS main at `88ce41a95554e1323ba34aa71b536b9e98475808`.
- Qualified exact push runs `38287690112` (`Workspace Infrastructure Contract`) and `38287690162` (`Repository QC`) as successful.
- Deferred `migration.infrastructure` publication to the next exact admitted OS release descriptor revision because the currently accepted descriptor is bound to older revision `9600929b946746c25c64e48471fcc83031fddda9`.
- Recorded detailed evidence in `docs/SAFE-INFRASTRUCTURE-SLICE-3.1-WORKSPACE-GENERATION.md` at `fd2a9e68f90e6a1ccb6991f03e10dcd2b45744ef`.
- Did not start Workspace relocation, migration or reference repair.

'''
marker = '\n---\n\n# Current execution pointer\n'
if text.count(marker) != 1:
    raise SystemExit('current-pointer insertion guard failed')
text = text.replace(marker, '\n' + changelog + '---\n\n# Current execution pointer\n', 1)

pointer_pattern = re.compile(r'# Current execution pointer\n.*\Z', re.S)
if len(pointer_pattern.findall(text)) != 1:
    raise SystemExit('current-pointer replacement guard failed')
pointer = '''# Current execution pointer

**Completed:** 8/18  
**Overall:** 44.4%  
**Phase:** Phase 3 - Implement canonical owner migrations for proven motivating problems  
**Phase progress:** 1/4  
**Until Phase 4:** 3 slices  
**Next:** STOP after Slice 3.1 under the one-at-a-time execution rule  
**Next Safe Infrastructure slice:** Phase 3 / Slice 3.2 - Implement admitted OS Workspace migration/reference repair only if required  
**Next task:** none until Slice 3.2 starts and its adaptive task list is derived from fresh System/OS/reference-consumer refs  
**Blockers/drift/amendments:** none. Slice 3.1 defined the current OS-owned Workspace generation without relocation; component-release generation publication is truthfully deferred to the next exact admitted OS descriptor revision.
'''
text = pointer_pattern.sub(pointer, text, count=1)

path.write_text(text, encoding='utf-8')
