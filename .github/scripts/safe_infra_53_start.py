from pathlib import Path

path = Path("docs/SAFE-INFRASTRUCTURE-UPGRADE-AND-RECOVERY-IMPLEMENTATION-PLAN.md")
text = path.read_text(encoding="utf-8")


def replace_once(old: str, new: str, label: str) -> None:
    global text
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected exactly one match, found {count}")
    text = text.replace(old, new, 1)


replace_once(
    "**Status:** IN PROGRESS - PHASE 5; SLICE 5.2 COMPLETE  ",
    "**Status:** IN PROGRESS - PHASE 5; SLICE 5.3 IN PROGRESS  ",
    "program status",
)
replace_once(
    "**Next:** Slice 5.3 - Canonical closeout and handoff (NOT STARTED)  \n**Next slice task list:** STOP - derive only when Slice 5.3 starts",
    "**Next:** Slice 5.3 - Canonical closeout and handoff (IN PROGRESS)  \n**Next slice task list:** 7 adaptive tasks recorded below",
    "program next",
)

old_slice = """## Slice 5.3 - Canonical closeout and handoff

**Status:** NOT STARTED  
**Dependencies:** 5.2  
**Adaptive tasks:** derive only from real remaining closeout debt

Update canonical System truth, owner docs, Distribution lifecycle docs, runtime adapters, changelog/readiness and any repository-network state required by active governance.

### Acceptance criteria"""

new_slice = """## Slice 5.3 - Canonical closeout and handoff

**Status:** IN PROGRESS  
**Dependencies:** 5.2  
**Adaptive tasks:** 0/7 COMPLETE

Final closeout is documentation, handoff, repository-network truth and qualification only unless a concrete acceptance failure proves product/runtime work is still required. Fresh owner/source evidence outranks stale roadmap assumptions.

### Frozen start refs

- System `81a7f39b7d7a1b2cf3985641d355194a93d57ec9`;
- Distribution `16d7f0b8a4a2e75f1fd3af8dea89b7c63d5a934b`;
- OS `470ad89e6b96d898161dee36d4e4fa8064dd6a8d`;
- Skills `d4a02888ba8d83c4a15ce1b538ffdafaaf83bee1`.

At the frozen Distribution head, Distribution CI `38712853052`, Safe Infrastructure Regression `38712852961` and Safe Infrastructure Convergence `38712853167` are all successful. This is the current executable baseline before Slice 5.3 handoff edits.

### Adaptive task list

- [ ] **5.3-T1** Freeze final System/Distribution/OS/Skills refs and audit remaining closeout debt across public lifecycle docs, owner boundaries, runtime adapters, roadmap/history/readiness and exact current qualification evidence.
- [ ] **5.3-T2** Align Distribution member and coding-agent lifecycle docs around one canonical surface: software update/update preview, whole-install doctor, structural upgrade preview/apply and restore preview/apply, while keeping normal member UX free of repository, generation and migration internals.
- [ ] **5.3-T3** Align OS and Skills owner docs with the final owner boundary: owner-local component lifecycle stays owner-local; Distribution owns whole-install release selection/orchestration, aggregate doctor, structural-upgrade coordination, rotating LKG and restore.
- [ ] **5.3-T4** Publish a canonical Distribution Safe Infrastructure handoff/readiness document that freezes ownership, lifecycle semantics, runtime-adapter convergence, protected-state rules, known explicit exclusions and the permanent qualification gates without creating a duplicate owner.
- [ ] **5.3-T5** Update Distribution history/roadmap/readiness truth to record the Safe Infrastructure lifecycle layer as complete while preserving unrelated future Distribution work such as the Full profile.
- [ ] **5.3-T6** Qualify the exact documentation/handoff heads and merged mains with Distribution CI, Safe Infrastructure Regression and Safe Infrastructure Convergence plus unchanged owner-native evidence, and record exact final evidence in System.
- [ ] **5.3-T7** Close the canonical System roadmap only after all required merged-main evidence is green: 18/18, 100%, Phase 5 3/3, program COMPLETE, no next Safe Infrastructure slice, and remove all temporary closeout tooling.

### Acceptance criteria"""
replace_once(old_slice, new_slice, "Slice 5.3 start block")

old_pointer = """**Completed:** 17/18  
**Overall:** 94.4%  
**Phase:** Phase 5 - Prove safety, convergence, restore and closeout  
**Phase progress:** 2/3  
**Until program complete:** 1 slice  
**Next:** STOP after Slice 5.2 under the one-at-a-time execution rule  
**Next Safe Infrastructure slice:** Slice 5.3 - Canonical closeout and handoff  
**Next task:** none until Slice 5.3 starts and its adaptive task list is derived from fresh System/Distribution/owner refs and real remaining closeout debt  
**Blockers/drift/amendments:** no Safe Infrastructure blocker or protected-law amendment. Exact 5.2 PR-head and merged-main CI/Regression/Convergence gates are green. Concurrent propagation/candidate-admission work is preserved. The separately owned public-admitted-Core first-run/setup-required broad-gate defect remains outside Slice 5.2 acceptance authority. Slice 5.3 is not started."""

new_pointer = """**Completed:** 17/18  
**Overall:** 94.4%  
**Phase:** Phase 5 - Prove safety, convergence, restore and closeout  
**Phase progress:** 2/3  
**Until program complete:** 1 slice  
**Current Safe Infrastructure slice:** Slice 5.3 - Canonical closeout and handoff (IN PROGRESS)  
**Current task:** 5.3-T1 - freeze refs and closeout debt, then execute the seven recorded tasks in order  
**Frozen refs:** System `81a7f39b7d7a1b2cf3985641d355194a93d57ec9`; Distribution `16d7f0b8a4a2e75f1fd3af8dea89b7c63d5a934b`; OS `470ad89e6b96d898161dee36d4e4fa8064dd6a8d`; Skills `d4a02888ba8d83c4a15ce1b538ffdafaaf83bee1`  
**Blockers/drift/amendments:** no Safe Infrastructure blocker or protected-law amendment at start. The concrete closeout debt is documentation/handoff/readiness alignment; no product/runtime change is authorized unless qualification exposes a real acceptance failure."""
replace_once(old_pointer, new_pointer, "current execution pointer")

path.write_text(text, encoding="utf-8")
