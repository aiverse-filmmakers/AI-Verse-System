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

**Status:** IN PROGRESS - PHASE 4 COMPLETE; PHASE 5 NOT STARTED  
**Canonical planning repo:** `aiverse-filmmakers/AI-Verse-System`  
**Primary orchestration repo:** `aiverse-filmmakers/ai-verse-distribution`  
**Initial owner repos:** `aiverse-filmmakers/AI-Verse-OS`, `aiverse-filmmakers/AI-Verse-Skills`  
**Started:** 2026-10-12  
**Planning method:** `docs/ADAPTIVE-IMPLEMENTATION-PLANNING-SKILL.md`  
**Program size:** 18 slices  
**Completed:** 15  
**Remaining:** 3  
**Overall progress:** 83.3%  
**Current phase:** Phase 4 - Implement Distribution orchestration and simple member UX (COMPLETE)  
**Current phase progress:** 4/4 COMPLETE  
**Slices until Phase 5:** 0  
**Next:** Phase 5 / Slice 5.1 - Add cross-repo regression and destructive-negative tests (NOT STARTED)  
**Next slice task list:** STOP - derive only when Slice 5.1 starts"""

new_header = """# AI-Verse Safe Infrastructure Upgrade, Convergence and Recovery Implementation Plan

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
replace_once(old_header, new_header, "program header")

old_phase5 = """# Phase 5 - Prove safety, convergence, restore and closeout

**Phase size:** 3 slices  
**Status:** NOT STARTED  
**Phase progress:** 0/3"""
new_phase5 = """# Phase 5 - Prove safety, convergence, restore and closeout

**Phase size:** 3 slices  
**Status:** IN PROGRESS  
**Phase progress:** 1/3"""
replace_once(old_phase5, new_phase5, "Phase 5 header")

slice_start = "## Slice 5.1 - Add cross-repo regression and destructive-negative tests\n"
slice_end = "\n---\n\n## Slice 5.2 - Run real old-install -> current-architecture convergence and restore qualification\n"
if text.count(slice_start) != 1:
    raise SystemExit(f"Slice 5.1 heading count={text.count(slice_start)}")
if text.count(slice_end) != 1:
    raise SystemExit(f"Slice 5.2 boundary count={text.count(slice_end)}")
before, rest = text.split(slice_start, 1)
old_slice, after = rest.split(slice_end, 1)
if "**Status:** NOT STARTED" not in old_slice:
    raise SystemExit("Slice 5.1 is not in the expected pre-closure state")

completed_slice = """## Slice 5.1 - Add cross-repo regression and destructive-negative tests

**Status:** COMPLETE  
**Dependencies:** 4.4  
**Adaptive tasks:** 7/7 COMPLETE

Added a permanent composed qualification layer in Distribution without changing product/runtime semantics. The new gate combines the existing focused update, doctor, upgrade, recovery, restore, adapter and transition-contract suites with exact frozen OS/Skills owner-boundary assertions.

### Final adaptive task list

- [x] **5.1-T1** Freeze fresh System/Distribution/OS/Skills refs and inventory focused coverage before any test implementation.
- [x] **5.1-T2** Add a dedicated composed Distribution regression suite over read-only planning, update semantics, doctor truth, structural gating/apply, recovery/restore and member UX.
- [x] **5.1-T3** Add cross-owner checks pinned to exact OS/Skills refs and preserve owner-defined Workspace, promotion and managed-Skills boundaries.
- [x] **5.1-T4** Compose the destructive-negative suites covering protected-state retention, stale plans, unsupported structures, failed verification/health, reference repair, restore-target survival, excluded state and interrupted upgrade.
- [x] **5.1-T5** Add a dedicated six-job Safe Infrastructure Regression CI gate while preserving normal Distribution CI and broad gates.
- [x] **5.1-T6** Qualify frozen OS/Skills owner-native behavior plus exact Distribution PR head and merged main, aligning owner-native execution to the owners' admitted Linux qualification surface.
- [x] **5.1-T7** Record exact evidence, close Slice 5.1 only after both required merged-main matrices are green, and stop before Slice 5.2.

### Implementation result

Distribution PR #34 added only:

- `.github/workflows/safe-infrastructure-regression.yml`;
- `tests/test_safe_infrastructure_cross_repo.py`.

No product code or owner implementation changed.

The regression gate runs Distribution and exact-ref cross-owner assertions on Ubuntu/macOS/Windows x Python 3.11/3.12. OS/Skills owner-native executable suites run on Linux, matching the owner repositories' admitted native qualification surface. This preserves full cross-platform Distribution qualification without silently broadening an owner-specific platform promise.

### Qualification discoveries

- The first new assertion used an incorrect expected OS finding label. The owner correctly uses `workspace-id-slot-mismatch`; only the new assertion was corrected.
- An initial macOS execution of the OS standalone Workspace fixture showed that the owner-native contract is Ubuntu/Node 22. The gate was aligned to that canonical owner surface while keeping Distribution and static cross-owner assertions on all six jobs.
- Distribution advanced concurrently through an independent candidate-evidence contract at `381ead50a9a4d790af945f4d95d268c65ed94060`. PR #34 merged on top of that current main, and merged-main qualification passed, proving compatibility with the newer Distribution state.

### Exact evidence

Detailed evidence: `docs/SAFE-INFRASTRUCTURE-SLICE-5.1-REGRESSION-TESTS.md`.

System start record:

- System PR #208 exact head `f2bf86dcba321420b1ef356d16091af1486c1e2d`;
- Contract Validation `38636147331`: **SUCCESS**, Python 3.11 and 3.13;
- merged start record `2f9538830733d6726c390e6eedd737eaf03f0a9c`.

Distribution PR head:

- PR #34 exact qualified head `7525048d89b148912d53a4793c732aa49fed9c12`;
- Safe Infrastructure Regression `38636882728`: **SUCCESS**, all six Ubuntu/macOS/Windows x Python 3.11/3.12 jobs;
- Distribution CI `38636882685`: **SUCCESS**, all six jobs;
- Lifecycle Receipt Concurrency `38636882701`: **SUCCESS**.

Distribution merged main:

- merged main `1f4559d88966e2a2ff26ca563d7a035ebc69a90b`;
- Distribution CI `38637231648`: **SUCCESS**, all six jobs;
- Safe Infrastructure Regression `38637231851`: **SUCCESS**, all six jobs.

Frozen owner supporting evidence remains green at exact refs:

- OS `470ad89e6b96d898161dee36d4e4fa8064dd6a8d`: Capability Placement Contract `38306623956` and Repository QC `38306623950` **SUCCESS**;
- Skills `d4a02888ba8d83c4a15ce1b538ffdafaaf83bee1`: Validate AI-Verse Skills `38298548847` and Release Descriptor `38298549229` **SUCCESS**.

### Acceptance criteria

- all Slice 5.1 permanent laws have executable proof or an explicit canonical owner boundary: **PASS**;
- destructive-negative refusal/failure preserves protected state: **PASS**;
- one-command/read-only update-plan, doctor/upgrade preview and restore preview semantics remain intact: **PASS**;
- owner doctor failure cannot become aggregate false PASS: **PASS**;
- OPTIONAL/REQUIRED/BLOCKED/REVIEW/unsupported behavior remains deterministic and fail-closed: **PASS**;
- stale plans, repeated apply/update and skip-version chains remain safe: **PASS**;
- unsupported Workspace relocation remains rejected without mutation: **PASS**;
- Workspace-to-personal promotion preserves explicit identity-change semantics and compatibility evidence: **PASS**;
- custom/user state, LKG and retained restore-target protections remain covered: **PASS**;
- credential/external-state exclusions remain truthful: **PASS**;
- injected mid-upgrade failure remains recoverable: **PASS**;
- supported adapters converge on the same lifecycle commands: **PASS**;
- default member output remains concise and non-technical: **PASS**;
- exact PR-head and merged-main Distribution CI plus Safe Infrastructure Regression are green across all six jobs: **PASS**.

No protected-law amendment or product-code change was required.

### Completion report

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

### NEXT

**STOP after Slice 5.1 under the current one-at-a-time execution request.**

Next execution unit is Slice 5.2. Derive its adaptive task list only after fresh System/Distribution/owner refs and real historical/current fixtures are fetched. No Slice 5.2 implementation was started here.
"""
text = before + completed_slice + slice_end + after

pointer_marker = "\n---\n\n# Current execution pointer\n"
if text.count(pointer_marker) != 1:
    raise SystemExit(f"current execution pointer marker count={text.count(pointer_marker)}")
history, _ = text.split(pointer_marker, 1)
if "## 2026-10-14 - Slice 5.1 completed; composed regression gate operational" in history:
    raise SystemExit("Slice 5.1 changelog already exists")

changelog = """## 2026-10-14 - Slice 5.1 completed; composed regression gate operational

- Added a permanent Distribution Safe Infrastructure Regression workflow and exact-ref cross-owner assertion suite without changing product/runtime semantics.
- Qualified Distribution update/doctor/upgrade/recovery/restore/adapter/transition invariants on Ubuntu/macOS/Windows x Python 3.11/3.12 while rerunning OS/Skills owner-native suites on their admitted Linux surface.
- Corrected one new assertion label and one qualification-platform assumption without modifying owner or product behavior.
- Qualified PR #34 exact head `7525048d89b148912d53a4793c732aa49fed9c12`: Safe Infrastructure Regression `38636882728` and Distribution CI `38636882685`, both all-six-job **SUCCESS**.
- Merged on top of concurrent Distribution candidate-evidence work as `1f4559d88966e2a2ff26ca563d7a035ebc69a90b`; merged-main Distribution CI `38637231648` and Safe Infrastructure Regression `38637231851` both passed all six jobs.
- Recorded detailed evidence in `docs/SAFE-INFRASTRUCTURE-SLICE-5.1-REGRESSION-TESTS.md`.
- Program progress is 16/18, 88.9%. Phase 5 is 1/3. Slice 5.2 remains unstarted.
"""

pointer = """**Completed:** 16/18  
**Overall:** 88.9%  
**Phase:** Phase 5 - Prove safety, convergence, restore and closeout  
**Phase progress:** 1/3  
**Until program complete:** 2 slices  
**Next:** STOP after Slice 5.1 under the one-at-a-time execution rule  
**Next Safe Infrastructure slice:** Slice 5.2 - Run real old-install -> current-architecture convergence and restore qualification  
**Next task:** none until Slice 5.2 starts and its adaptive task list is derived from fresh refs plus real historical/current fixtures  
**Blockers/drift/amendments:** no Safe Infrastructure blocker or protected-law amendment. Distribution merged-main qualification includes concurrent candidate-evidence work. Current production structural apply remains a truthful no-op where owners publish no admitted structural recipe. Slice 5.2 is not started.
"""

text = history.rstrip() + "\n\n---\n\n" + changelog.strip() + pointer_marker + "\n" + pointer
path.write_text(text, encoding="utf-8")
