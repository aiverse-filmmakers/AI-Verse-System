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

**Status:** IN PROGRESS - PHASE 5; SLICE 5.1 COMPLETE  
**Canonical planning repo:** `aiverse-filmmakers/AI-Verse-System`  
**Primary orchestration repo:** `aiverse-filmmakers/ai-verse-distribution`  
**Initial owner repos:** `aiverse-filmmakers/AI-Verse-OS`, `aiverse-filmmakers/AI-Verse-Skills`  
**Started:** 2026-10-12  
**Planning method:** `docs/ADAPTIVE-IMPLEMENTATION-PLANNING-SKILL.md`  
**Program size:** 18 slices  
**Completed:** 16  
**Remaining:** 2  
**Overall progress:** 88.9%  
**Current phase:** Phase 5 - Prove safety, convergence, restore and closeout  
**Current phase progress:** 1/3  
**Slices until program complete:** 2  
**Next:** Slice 5.2 - Run real old-install -> current-architecture convergence and restore qualification (NOT STARTED)  
**Next slice task list:** STOP - derive only when Slice 5.2 starts"""

new_header = """# AI-Verse Safe Infrastructure Upgrade, Convergence and Recovery Implementation Plan

**Status:** IN PROGRESS - PHASE 5; SLICE 5.2 COMPLETE  
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
**Next:** Slice 5.3 - Canonical closeout and handoff (NOT STARTED)  
**Next slice task list:** STOP - derive only when Slice 5.3 starts"""
replace_once(old_header, new_header, "program header")

old_phase5 = """# Phase 5 - Prove safety, convergence, restore and closeout

**Phase size:** 3 slices  
**Status:** IN PROGRESS  
**Phase progress:** 1/3"""
new_phase5 = """# Phase 5 - Prove safety, convergence, restore and closeout

**Phase size:** 3 slices  
**Status:** IN PROGRESS  
**Phase progress:** 2/3"""
replace_once(old_phase5, new_phase5, "Phase 5 header")

slice_start = "## Slice 5.2 - Run real old-install -> current-architecture convergence and restore qualification\n"
slice_end = "\n---\n\n## Slice 5.3 - Canonical closeout and handoff\n"
if text.count(slice_start) != 1:
    raise SystemExit(f"Slice 5.2 heading count={text.count(slice_start)}")
if text.count(slice_end) != 1:
    raise SystemExit(f"Slice 5.3 boundary count={text.count(slice_end)}")
before, rest = text.split(slice_start, 1)
old_slice, after = rest.split(slice_end, 1)
if "**Status:** NOT STARTED" not in old_slice:
    raise SystemExit("Slice 5.2 is not in the expected pre-closure state")

completed_slice = """## Slice 5.2 - Run real old-install -> current-architecture convergence and restore qualification

**Status:** COMPLETE  
**Dependencies:** 5.1  
**Adaptive tasks:** 7/7 COMPLETE

Qualified one real admitted older Core installation through the current admitted architecture, the exact frozen OS owner capability-promotion contract and an explicit retained-LKG restore. No product/runtime code or owner mutation semantics were added by this slice.

### Final adaptive task list

- [x] **5.2-T1** Freeze the real historical/current fixture set and exact owner contracts: real admitted Core transition, historical nested Workspace drift, current direct Workspace contract, Workspace-to-personal capability promotion, LKG/restore coverage and supported runtime adapter commands.
- [x] **5.2-T2** Execute a realistic older populated Core installation through the real admitted `core-stable-2026-10-10` -> `core-first-run-rc1-2026-10-12` transition and prove member-owned state survives while authoritative receipt/status reaches the admitted target.
- [x] **5.2-T3** Prove Workspace convergence truth without inventing migration: current direct `workspaces/<id>` layout remains canonical while historical nested/domain-first layout stays `BLOCKED/REVIEW`, non-relocating and read-only because no Workspace relocation recipe is admitted.
- [x] **5.2-T4** Exercise the real OS Workspace-to-personal capability promotion through the exact frozen owner source against the real upgraded installation, preserving provenance/history/custom files, recording intentional identity change, compatibility repair, cross-Workspace resolution, stale-plan refusal evidence and idempotent replay.
- [x] **5.2-T5** Compose real software update plus owner mutation with Last-Known-Good and explicit restore: preserve the pre-action LKG, keep restore preview read-only, restore exactly declared covered files, retain excluded credential-shaped state, retain the recovery target and finish healthy.
- [x] **5.2-T6** Prove fresh-versus-upgraded convergence and runtime convergence: independently install the same current Core release, compare exact package-owned component contracts, and rerun lifecycle entrypoint and adapter convergence across the supported matrix.
- [x] **5.2-T7** Qualify exact owner-native evidence, exact Distribution PR head and merged main, record the real executable result, close Slice 5.2 only after all required gates are green, then stop before Slice 5.3.

### Implementation result

Distribution PR #35 added only:

- `.github/workflows/safe-infrastructure-convergence.yml`;
- `scripts/safe-infra-52-real-convergence.py`;
- `tests/test_safe_infrastructure_convergence_contract.py`.

The real fixture:

- installs `core-stable-2026-10-10` with realistic member-owned state;
- updates through the exact admitted transition to `core-first-run-rc1-2026-10-12`;
- independently installs a fresh copy of the same current release and compares package-owned component contracts;
- preserves the unsupported nested Workspace example as review-only rather than inventing relocation;
- invokes the frozen OS owner placement/promotion command surface against the real upgraded installation;
- proves `workspace:alpha:transcript-book` -> `local:transcript-book` is an intentional qualified-identity change with active compatibility repair, custom-file preservation, cross-Workspace consumption and idempotent replay;
- retains the pre-action Last-Known-Good recovery point;
- proves restore preview is read-only and explicit restore reproduces declared covered file state while credential-shaped `.env` state remains excluded;
- ends with a healthy whole-install doctor result.

No Distribution product/runtime code changed. No OS or Skills owner implementation changed. No production Workspace relocation recipe or broader release-transition authority was invented.

### Qualification discoveries

- The fixture initially expected a non-canonical top-level update-result field and was corrected to use the updater's real result plus authoritative receipt/status truth.
- Concurrent candidate-admission work briefly failed on the PR merge ref, then its owning propagation program repaired current Distribution main. The final 5.2 head was qualified on that repaired base.
- The released Core OS checkout predates the later owner-source placement/promotion command surface. Qualification therefore invokes the exact frozen owner source against the real upgraded installation while verifying that its accepted descriptor binds the shipped OS revision, rather than claiming that command surface is already in the released checkout.
- Recovery captures file-level covered state, not empty directory identity. The restore assertion was corrected to require no residual promoted files or symlinks instead of inventing a broader recovery promise.
- Two broad PR workflows, Project Bootstrap and Clean Machine Core Acceptance, still expose the separately owned pre-existing public-admitted-Core first-run/setup-required defect already isolated in earlier slices. They are not Slice 5.2 acceptance authority. The exact 5.2 CI, Regression and Convergence gates are green.

### Exact evidence

Detailed evidence: `docs/SAFE-INFRASTRUCTURE-SLICE-5.2-CONVERGENCE-RESTORE.md`.

System start record:

- System PR #211 exact head `eee514a6ba843ef6dea20ebfb371bd955c882817`;
- merged start record `d7a7e5b38712a32c417d49b47c3d39b7015b92b9`;
- merged-start Contract Validation `38641788395`: **SUCCESS**.

Distribution PR head:

- PR #35 exact qualified head `8ca22a1fbacf17f067af2e2e83418c4810ccc70d`;
- Distribution CI `38644724266`: **SUCCESS**, all six Ubuntu/macOS/Windows x Python 3.11/3.12 jobs;
- Safe Infrastructure Regression `38644724292`: **SUCCESS**, all six jobs;
- Safe Infrastructure Convergence `38644724402`: **SUCCESS**, all six jobs;
- Lifecycle Receipt Concurrency `38644724547`: **SUCCESS**.

Distribution merged main:

- PR #35 merged as `004112410ec4608e4b9a758b651c4d6bba3b7f8c`;
- Distribution CI `38645538247`: **SUCCESS**, all six jobs;
- Safe Infrastructure Regression `38645538145`: **SUCCESS**, all six jobs;
- Safe Infrastructure Convergence `38645538333`: **SUCCESS**, all six jobs.

At canonical closure preparation, Distribution main is one direct test-only commit ahead at `16d7f0b8a4a2e75f1fd3af8dea89b7c63d5a934b`; its only change relative to the qualified 5.2 merge is `tests/test_candidate_admission_regressions.py`. OS remains `470ad89e6b96d898161dee36d4e4fa8064dd6a8d`, Skills remains `d4a02888ba8d83c4a15ce1b538ffdafaaf83bee1`, and the current System closure base is `df05327fa43f8fd4dfbacbf75c7809b7a40bc10f`. No Safe Infrastructure implementation drift is introduced by those concurrent heads.

### Acceptance criteria

- real admitted older Core transition executes with realistic member state and preserves it: **PASS**;
- fresh-current and upgraded historical installations converge on identical package-owned component contracts: **PASS**;
- historical unsupported Workspace relocation remains review-only and non-mutating: **PASS**;
- owner-defined capability promotion requires explicit intent/apply and records intentional qualified-identity change: **PASS**;
- provenance/history/custom capability files survive promotion: **PASS**;
- compatibility mapping and cross-Workspace consumption work: **PASS**;
- stale-plan refusal remains owner-native evidence and replay is idempotent: **PASS**;
- pre-action LKG is retained before update: **PASS**;
- restore preview is read-only: **PASS**;
- restore reproduces exactly declared file-level covered state: **PASS**;
- excluded credential-shaped state is not falsely rewound: **PASS**;
- retained LKG survives restore: **PASS**;
- final doctor aggregation is healthy: **PASS**;
- supported runtime lifecycle routing remains convergent: **PASS**;
- exact PR-head and merged-main CI/Regression/Convergence gates are green: **PASS**.

No protected-law amendment and no product-code change was required.

### Completion report

```text
Completed: Slice 5.2 - Run real old-install -> current-architecture convergence and restore qualification
Tasks: 7/7
Overall: 17/18 slices (94.4%)
Phase: Phase 5 - Prove safety, convergence, restore and closeout
Phase progress: 2/3
Until program complete: 1 slice
Next: Slice 5.3 - Canonical closeout and handoff
Blockers/drift/amendments: no Safe Infrastructure blocker or protected-law amendment; concurrent propagation/candidate-admission work is preserved and does not overlap the qualified 5.2 implementation.
```

### NEXT

**STOP after Slice 5.2 under the current one-at-a-time execution rule.**

Next execution unit is Slice 5.3 - Canonical closeout and handoff. Derive its adaptive task list only after fresh System/Distribution/owner refs are fetched. No Slice 5.3 implementation was started here.
"""
text = before + completed_slice + slice_end + after

pointer_marker = "\n---\n\n# Current execution pointer\n"
if text.count(pointer_marker) != 1:
    raise SystemExit(f"current execution pointer marker count={text.count(pointer_marker)}")
history, current_pointer = text.split(pointer_marker, 1)
if "## 2026-10-15 - Slice 5.2 completed; real convergence and restore qualified" in history:
    raise SystemExit("Slice 5.2 changelog already exists")
if "**Completed:** 16/18" not in current_pointer or "Slice 5.2 is not started" not in current_pointer:
    raise SystemExit("Current execution pointer is not in the expected Slice 5.1 closure state")

changelog = """## 2026-10-15 - Slice 5.2 completed; real convergence and restore qualified

- Qualified a real populated `core-stable-2026-10-10` installation through the admitted `core-first-run-rc1-2026-10-12` update and compared it with a fresh current install.
- Preserved historical nested Workspace drift as `BLOCKED/REVIEW` with no invented relocation recipe.
- Exercised the real frozen OS Workspace-to-personal capability promotion against the upgraded installation with intentional qualified-identity change, compatibility repair, custom-file preservation, cross-Workspace consumption and idempotent replay.
- Proved retained Last-Known-Good protection, read-only restore preview, explicit covered-state restore, credential exclusion, retained recovery target and final doctor health.
- Qualified Distribution PR #35 exact head `8ca22a1fbacf17f067af2e2e83418c4810ccc70d` with all-six-job Distribution CI `38644724266`, Safe Infrastructure Regression `38644724292` and Safe Infrastructure Convergence `38644724402` successful.
- Merged PR #35 as `004112410ec4608e4b9a758b651c4d6bba3b7f8c`; merged-main Distribution CI `38645538247`, Safe Infrastructure Regression `38645538145` and Safe Infrastructure Convergence `38645538333` all passed all six jobs.
- Preserved concurrent System propagation work and the later Distribution candidate-admission regression-only commit without rebasing or weakening the exact 5.2 evidence boundary.
- Recorded detailed evidence in `docs/SAFE-INFRASTRUCTURE-SLICE-5.2-CONVERGENCE-RESTORE.md`.
- Program progress is 17/18, 94.4%. Phase 5 is 2/3. Slice 5.3 remains unstarted.
"""

pointer = """**Completed:** 17/18  
**Overall:** 94.4%  
**Phase:** Phase 5 - Prove safety, convergence, restore and closeout  
**Phase progress:** 2/3  
**Until program complete:** 1 slice  
**Next:** STOP after Slice 5.2 under the one-at-a-time execution rule  
**Next Safe Infrastructure slice:** Slice 5.3 - Canonical closeout and handoff  
**Next task:** none until Slice 5.3 starts and its adaptive task list is derived from fresh System/Distribution/owner refs and real remaining closeout debt  
**Blockers/drift/amendments:** no Safe Infrastructure blocker or protected-law amendment. Exact 5.2 PR-head and merged-main CI/Regression/Convergence gates are green. Concurrent propagation/candidate-admission work is preserved. The separately owned public-admitted-Core first-run/setup-required broad-gate defect remains outside Slice 5.2 acceptance authority. Slice 5.3 is not started.
"""

text = history.rstrip() + "\n\n---\n\n" + changelog.strip() + pointer_marker + "\n" + pointer
path.write_text(text, encoding="utf-8")
