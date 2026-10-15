from pathlib import Path

path = Path("docs/SAFE-INFRASTRUCTURE-UPGRADE-AND-RECOVERY-IMPLEMENTATION-PLAN.md")
text = path.read_text(encoding="utf-8")


def replace_once(old: str, new: str, label: str) -> None:
    global text
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected exactly one match, found {count}")
    text = text.replace(old, new, 1)


old_header = """# AI-Verse Safe Infrastructure Upgrade, Convergence and Recovery Implementation Plan

**Status:** IN PROGRESS - PHASE 5; SLICE 5.3 IN PROGRESS  
**Canonical planning repo:** `aiverse-filmmakers/AI-Verse-System`  
**Primary orchestration repo:** `aiverse-filmmakers/ai-verse-distribution`  
**Initial owner repos:** `aiverse-filmmakers/AI-Verse-OS`, `aiverse-filmmakers/AI-Verse-Skills`  
**Started:** 2026-10-12  
**Planning method:** `docs/ADAPTIVE-IMPLEMENTATION-PLANNING-SKILL.md`  
**Program size:** 18 slices  
**Completed:** 17  
**Remaining:** 1  
**Overall progress:** 94.4%  
**Current phase:** Phase 5 - Prove safety, convergence, restore and closeout  
**Current phase progress:** 2/3  
**Slices until program complete:** 1  
**Next:** Slice 5.3 - Canonical closeout and handoff (IN PROGRESS)  
**Next slice task list:** 7 adaptive tasks recorded below"""

new_header = """# AI-Verse Safe Infrastructure Upgrade, Convergence and Recovery Implementation Plan

**Status:** COMPLETE - SAFE INFRASTRUCTURE PROGRAM  
**Canonical planning repo:** `aiverse-filmmakers/AI-Verse-System`  
**Primary orchestration repo:** `aiverse-filmmakers/ai-verse-distribution`  
**Initial owner repos:** `aiverse-filmmakers/AI-Verse-OS`, `aiverse-filmmakers/AI-Verse-Skills`  
**Started:** 2026-10-12  
**Completed:** 2026-10-15  
**Planning method:** `docs/ADAPTIVE-IMPLEMENTATION-PLANNING-SKILL.md`  
**Program size:** 18 slices  
**Completed:** 18  
**Remaining:** 0  
**Overall progress:** 100.0%  
**Current phase:** Phase 5 - Prove safety, convergence, restore and closeout (COMPLETE)  
**Current phase progress:** 3/3 COMPLETE  
**Slices until program complete:** 0  
**Next:** none - Safe Infrastructure is now maintenance infrastructure  
**Next slice task list:** none"""
replace_once(old_header, new_header, "program header")

old_phase = """# Phase 5 - Prove safety, convergence, restore and closeout

**Phase size:** 3 slices  
**Status:** IN PROGRESS  
**Phase progress:** 2/3"""
new_phase = """# Phase 5 - Prove safety, convergence, restore and closeout

**Phase size:** 3 slices  
**Status:** COMPLETE  
**Phase progress:** 3/3 COMPLETE"""
replace_once(old_phase, new_phase, "Phase 5 header")

slice_start = "## Slice 5.3 - Canonical closeout and handoff\n"
slice_boundary = "\n---\n\n# Program Change Log\n"
if text.count(slice_start) != 1:
    raise SystemExit(f"Slice 5.3 heading count={text.count(slice_start)}")
if text.count(slice_boundary) != 1:
    raise SystemExit(f"Slice 5.3 boundary count={text.count(slice_boundary)}")
before, rest = text.split(slice_start, 1)
old_slice, after = rest.split(slice_boundary, 1)
if "**Status:** IN PROGRESS" not in old_slice:
    raise SystemExit("Slice 5.3 is not IN PROGRESS")
if "**Adaptive tasks:** 0/7 COMPLETE" not in old_slice:
    raise SystemExit("Slice 5.3 task counter is not in expected start state")
for task in range(1, 8):
    if f"- [ ] **5.3-T{task}**" not in old_slice:
        raise SystemExit(f"Slice 5.3 T{task} is not unchecked as expected")

completed_slice = """## Slice 5.3 - Canonical closeout and handoff

**Status:** COMPLETE  
**Dependencies:** 5.2  
**Adaptive tasks:** 7/7 COMPLETE

Closed the Safe Infrastructure program as permanent maintenance infrastructure after aligning Distribution/member/agent handoff, OS and Skills owner boundaries, Distribution roadmap/history/readiness and exact final cross-platform qualification. Slice 5.3 changed documentation and canonical handoff truth only; no product/runtime behavior or owner implementation was modified.

### Final adaptive task list

- [x] **5.3-T1** Freeze final System/Distribution/OS/Skills refs and audit remaining closeout debt across public lifecycle docs, owner boundaries, runtime adapters, roadmap/history/readiness and exact current qualification evidence.
- [x] **5.3-T2** Align Distribution member and coding-agent lifecycle docs around one canonical surface: software update/update preview, whole-install doctor, structural upgrade preview/apply and restore preview/apply, while keeping normal member UX free of repository, generation and migration internals.
- [x] **5.3-T3** Align OS and Skills owner docs with the final owner boundary: owner-local component lifecycle stays owner-local; Distribution owns whole-install release selection/orchestration, aggregate doctor, structural-upgrade coordination, rotating LKG and restore.
- [x] **5.3-T4** Publish a canonical Distribution Safe Infrastructure handoff/readiness document that freezes ownership, lifecycle semantics, runtime-adapter convergence, protected-state rules, known explicit exclusions and the permanent qualification gates without creating a duplicate owner.
- [x] **5.3-T5** Update Distribution history/roadmap/readiness truth to record the Safe Infrastructure lifecycle layer as complete while preserving unrelated future Distribution work such as the Full profile.
- [x] **5.3-T6** Qualify the exact documentation/handoff heads and merged mains with Distribution CI, Safe Infrastructure Regression and Safe Infrastructure Convergence plus owner-native evidence, and record exact final evidence in System.
- [x] **5.3-T7** Close the canonical System roadmap only after all required merged-main evidence is green: 18/18, 100%, Phase 5 3/3, program COMPLETE, no next Safe Infrastructure slice, and remove all temporary closeout tooling.

### Implementation and handoff result

Distribution PR #36 aligned `README.md`, `INSTALL.md`, `AGENTS.md`, `docs/ROADMAP.md`, `docs/HISTORY.md` and added `docs/SAFE-INFRASTRUCTURE-LIFECYCLE.md`. OS PR #75 and Skills PR #22 each added a documentation-only Distribution lifecycle owner-boundary handoff.

The final member-facing whole-install lifecycle is:

```text
aiverse update
aiverse update --plan
aiverse doctor
aiverse upgrade
aiverse upgrade --apply
aiverse restore
aiverse restore --apply
aiverse status
aiverse open
```

Distribution remains the single whole-install release/update/aggregate-doctor/structural-upgrade/LKG/restore/runtime-adapter orchestrator. Component owners retain their local lifecycle, health, state and migration semantics. OS remains the Workspace/capability placement and promotion owner. Skills remains the managed reusable-capability generation/lifecycle owner.

No duplicate update, migration, backup/recovery or doctor owner was introduced.

### Qualification discovery

The final audit initially appeared to show that `upgrade` and `restore` were absent from `src/aiverse_distribution/cli.py`. The shipped executable contract was traced before any code change: `pyproject.toml` binds `aiverse` to `aiverse_distribution.entrypoint:main`, and that entrypoint explicitly supplies whole-install `doctor`, preview-first `upgrade`/`restore` and their `--apply` mutation routes. The apparent gap was therefore documentation/audit interpretation only. No runtime fix was required.

### Exact final evidence

Detailed evidence: `docs/SAFE-INFRASTRUCTURE-SLICE-5.3-CLOSEOUT-HANDOFF.md`.

System Slice 5.3 start:

- start PR #214 exact head `0ccb87cddae368531686a6869a94b71981316bbc`;
- Contract Validation `38714771049`: **SUCCESS**;
- start merged as `20cc38e6dd2728f915f23ce6a421fe30afde6741`;
- one-shot start bookkeeping `38714832984`: **SUCCESS**;
- canonical start roadmap `b5ccc7a8d6b3e24fc449cc81aecfaf2e9007d69b`;
- temporary start-tool cleanup PR #215 exact head `84e79d66300d56749ee9b68e10e956770d46f883`, Contract Validation `38714953228`: **SUCCESS**;
- cleanup merged as `45893e1ef471bdabca3332bf6be1ba9c144ed76e`.

Final Distribution handoff:

- PR #36 exact qualified head `bbe06bbb779ed6ee6068bfe3ecc798b5c1a6d468`;
- PR-head Distribution CI `38715602678`: **SUCCESS**;
- PR-head Safe Infrastructure Regression `38715602749`: **SUCCESS**;
- PR-head Safe Infrastructure Convergence `38715602528`: **SUCCESS**;
- merged main `d41c3abc1702fba85693c971de49a3a539ee7327`;
- merged-main Distribution CI `38716176205`: **SUCCESS**;
- merged-main Safe Infrastructure Regression `38716176343`: **SUCCESS**;
- merged-main Safe Infrastructure Convergence `38716176280`: **SUCCESS**.

Final OS handoff:

- PR #75 exact head `2337dd558baa796c8a5df1e3c2122fcbfad9a393`;
- Capability Placement Contract `38715617878`: **SUCCESS**;
- Repository QC `38715617910`: **SUCCESS**;
- Workspace Infrastructure Contract `38715617720`: **SUCCESS**;
- Update Request Contract `38715617943`: **SUCCESS**;
- merged main `83747a90998077ad2ab4636f202ca2e065a9a6bb`;
- merged-main Capability Placement Contract `38716077161`: **SUCCESS**;
- merged-main Repository QC `38716077129`: **SUCCESS**.

Final Skills handoff:

- PR #22 exact head `f8051d620dd3285f94a2990a4ca39aa6dbd172e8`;
- Validate AI-Verse Skills `38715632290`: **SUCCESS**;
- merged main `f2eb46015a07d1cc057f72610f967f2b994907e1`;
- merged-main Validate AI-Verse Skills `38716088957`: **SUCCESS**.

System advanced concurrently through separately owned propagation bookkeeping. Final canonical closeout was therefore prepared from current System main `ea99c822631297084976f7612c95df0fca973162`, preserving that unrelated work without modifying Safe Infrastructure semantics.

### Acceptance criteria

- all 18 slices COMPLETE with exact evidence: **PASS**;
- no duplicate update/migration/backup/doctor owner exists: **PASS**;
- shipped `aiverse update` remains clean, safe and non-invasive to optional structure: **PASS**;
- one-command doctor is operational without user component knowledge: **PASS**;
- existing installations can converge safely when explicitly requested: **PASS**;
- OPTIONAL / REQUIRED / BLOCKED behavior is deterministic and understandable: **PASS**;
- one rotating Last-Known-Good recovery point is operational: **PASS**;
- restore is preview-first, explicit, truthful and tested: **PASS**;
- recovery scope is storage-conscious and reproducible rather than a blind-copy promise: **PASS**;
- Workspace and capability-scope fixtures pass according to the canonical identity contract: **PASS**;
- supported runtime adapters converge on one lifecycle contract: **PASS**;
- user-owned data/state protection remains satisfied: **PASS**;
- default member UX requires no repository/path/generation/migration knowledge: **PASS**;
- exact final Distribution PR-head and merged-main CI/Regression/Convergence gates are green: **PASS**;
- exact final OS and Skills owner handoff qualification is green: **PASS**;
- no Slice 5.3 product/runtime change or protected-law amendment was required: **PASS**;
- program becomes COMPLETE only now: **PASS**.

The separately owned public-admitted-Core first-run/setup-required broad-gate defect remains outside Safe Infrastructure acceptance authority and is not misrepresented as resolved by this program.

### Completion report

```text
Completed: Slice 5.3 - Canonical closeout and handoff
Tasks: 7/7
Overall: 18/18 slices (100.0%)
Phase: Phase 5 - Prove safety, convergence, restore and closeout
Phase progress: 3/3 COMPLETE
Until program complete: 0 slices
Next: none - Safe Infrastructure program complete
Blockers/drift/amendments: no Safe Infrastructure blocker or protected-law amendment; concurrent System propagation work preserved; separate broad-gate first-run/setup-required evidence remains outside this program's acceptance authority.
```

### NEXT

None. Safe Infrastructure is complete and handed off as permanent maintenance infrastructure. Future changes must preserve the canonical ownership and qualification laws or explicitly amend them through System governance with new executable evidence.
"""
text = before + completed_slice + slice_boundary + after

pointer_marker = "\n---\n\n# Current execution pointer\n"
if text.count(pointer_marker) != 1:
    raise SystemExit(f"current execution pointer marker count={text.count(pointer_marker)}")
history, current_pointer = text.split(pointer_marker, 1)
if "**Completed:** 17/18" not in current_pointer:
    raise SystemExit("current pointer is not at 17/18")
if "Slice 5.3 - Canonical closeout and handoff (IN PROGRESS)" not in current_pointer:
    raise SystemExit("current pointer is not at Slice 5.3 IN PROGRESS")
if "## 2026-10-15 - Slice 5.3 completed; Safe Infrastructure program complete" in history:
    raise SystemExit("Slice 5.3 final changelog already exists")

changelog = """## 2026-10-15 - Slice 5.3 completed; Safe Infrastructure program complete

- Aligned Distribution member and coding-agent lifecycle documentation around one whole-install surface: update/update preview, aggregate doctor, structural upgrade preview/apply and restore preview/apply.
- Published `docs/SAFE-INFRASTRUCTURE-LIFECYCLE.md` as the permanent Distribution handoff for whole-install ownership, protected state, recovery classes, runtime adapters and permanent qualification gates.
- Added documentation-only owner handoffs in OS and Skills without changing runtime semantics or component ownership.
- Qualified Distribution PR #36 exact head `bbe06bbb779ed6ee6068bfe3ecc798b5c1a6d468` with CI `38715602678`, Regression `38715602749` and Convergence `38715602528`, all **SUCCESS**.
- Merged Distribution handoff as `d41c3abc1702fba85693c971de49a3a539ee7327`; merged-main CI `38716176205`, Regression `38716176343` and Convergence `38716176280` all **SUCCESS**.
- Merged OS handoff as `83747a90998077ad2ab4636f202ca2e065a9a6bb`; merged-main Capability Placement `38716077161` and Repository QC `38716077129` **SUCCESS**.
- Merged Skills handoff as `f2eb46015a07d1cc057f72610f967f2b994907e1`; merged-main Validate AI-Verse Skills `38716088957` **SUCCESS**.
- Preserved concurrent System propagation work and based final closeout on current System main `ea99c822631297084976f7612c95df0fca973162`.
- Recorded final evidence in `docs/SAFE-INFRASTRUCTURE-SLICE-5.3-CLOSEOUT-HANDOFF.md`.
- Program progress is 18/18, 100.0%. Phase 5 is 3/3 COMPLETE. There is no next Safe Infrastructure slice.
"""

pointer = """**Completed:** 18/18  
**Overall:** 100.0%  
**Phase:** Phase 5 - Prove safety, convergence, restore and closeout (COMPLETE)  
**Phase progress:** 3/3 COMPLETE  
**Until program complete:** 0 slices  
**Program status:** COMPLETE  
**Next Safe Infrastructure slice:** none  
**Maintenance handoff:** Distribution owns the whole-install lifecycle; component owners retain component-local semantics; permanent Distribution CI, Safe Infrastructure Regression and Safe Infrastructure Convergence gates protect the handoff.  
**Final implementation heads:** Distribution `d41c3abc1702fba85693c971de49a3a539ee7327`; OS `83747a90998077ad2ab4636f202ca2e065a9a6bb`; Skills `f2eb46015a07d1cc057f72610f967f2b994907e1`  
**Blockers/drift/amendments:** no Safe Infrastructure blocker or protected-law amendment. Slice 5.3 was documentation/handoff-only. Concurrent System propagation work is preserved. Separately owned broad-gate first-run/setup-required evidence remains outside this completed program's acceptance authority.
"""

text = history.rstrip() + "\n\n---\n\n" + changelog.strip() + pointer_marker + "\n" + pointer
path.write_text(text, encoding="utf-8")
