from pathlib import Path


ROADMAP = Path("docs/SAFE-INFRASTRUCTURE-UPGRADE-AND-RECOVERY-IMPLEMENTATION-PLAN.md")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected one anchor, found {count}")
    return text.replace(old, new, 1)


text = ROADMAP.read_text(encoding="utf-8")

text = replace_once(
    text,
    "**Status:** IN PROGRESS - PHASE 4; SLICE 4.2 COMPLETE  \n",
    "**Status:** IN PROGRESS - PHASE 4; SLICE 4.3 COMPLETE  \n",
    "program status",
)
text = replace_once(text, "**Completed:** 13  \n", "**Completed:** 14  \n", "completed counter")
text = replace_once(text, "**Remaining:** 5  \n", "**Remaining:** 4  \n", "remaining counter")
text = replace_once(text, "**Overall progress:** 72.2%  \n", "**Overall progress:** 77.8%  \n", "overall progress")
text = replace_once(text, "**Current phase progress:** 2/4  \n", "**Current phase progress:** 3/4  \n", "header phase progress")
text = replace_once(text, "**Slices until Phase 5:** 2  \n", "**Slices until Phase 5:** 1  \n", "phase distance")
text = replace_once(
    text,
    "**Next:** Slice 4.3 - Implement one-command doctor and upgrade-plan aggregation with plain-English traffic-light UX  \n",
    "**Next:** Slice 4.4 - Implement `upgrade --apply` orchestration, resume and verification  \n",
    "next slice",
)
text = replace_once(
    text,
    "**Next slice task list:** STOP - derive only when Slice 4.3 starts\n",
    "**Next slice task list:** STOP - derive only when Slice 4.4 starts\n",
    "next task list",
)
text = replace_once(
    text,
    "**Phase progress:** 2/4\n\n## Slice 4.1",
    "**Phase progress:** 3/4\n\n## Slice 4.1",
    "phase 4 progress",
)

old_slice = '''## Slice 4.3 - Implement one-command doctor and upgrade-plan aggregation with plain-English traffic-light UX

**Status:** NOT STARTED  
**Dependencies:** 3.2, 3.4, 4.2  
**Adaptive tasks:** derive from owner doctor/recipe surfaces

`aiverse doctor` is one member command. Distribution invokes relevant owner checks internally in a controlled sequence and aggregates them without duplicating owner logic.

`aiverse upgrade` consumes owner findings/recipes and produces the structural convergence preview.

Default experience should resemble:

```text
AI-Verse Check

Healthy: YES
Safe improvements: 2
Needs your review: 1
Blocked: 0
Risk: LOW
Nothing will be deleted.

Recommended: Upgrade AI-Verse
```

When an upgrade is required for activation, wording should resemble:

```text
AI-Verse found one setup change that must be completed before the new version can finish.
Nothing has been changed yet.

Recommended: Upgrade AI-Verse
```

### Acceptance criteria

- one `aiverse doctor` command checks the whole supported installation from the member's perspective;
- owner checks execute internally with isolated evidence/results;
- one owner failure is surfaced accurately and cannot become a false whole-system PASS;
- member never needs component-specific doctor commands;
- default summary is concise and plain English;
- full technical evidence is available on demand and machine-readable;
- doctor/upgrade preview mutate nothing;
- OPTIONAL / REQUIRED / REVIEW-BLOCKED cases are impossible to misread;
- default output does not expose internal paths/generations/IDs unless no friendlier conflict identifier exists.

### NEXT

Slice 4.4.
'''

new_slice = '''## Slice 4.3 - Implement one-command doctor and upgrade-plan aggregation with plain-English traffic-light UX

**Status:** COMPLETE  
**Dependencies:** 3.2, 3.4, 4.2  
**Adaptive tasks:** 6/6 COMPLETE

Extended the shipped doctor fan-out instead of replacing it. Whole-system `aiverse doctor` now presents one concise member overview while retaining full isolated owner evidence in JSON. Internal lifecycle `doctor()` remains unchanged for update/LKG/restore qualification. `aiverse upgrade` now exists as a read-only structural preview over the exact locked admitted release and reuses the Slice 4.2 owner infrastructure gate without executing owner migrations.

### Final adaptive task list

- [x] **4.3-T1** Refresh System, Distribution, OS and Skills refs; re-read Slice 4.3, Slice 2.3 doctor/member-UX invariants, Slice 4.2 structural gate, shipped doctor fan-out and current owner descriptor state; inventory overlapping work before writes.
- [x] **4.3-T2** Extend whole-install doctor results with deterministic aggregate health/member-summary data while preserving isolated owner evidence, continuing safe independent checks after one owner failure, and keeping doctor strictly read-only.
- [x] **4.3-T3** Implement read-only `upgrade` planning over the locked admitted release by reusing exact owner infrastructure metadata/detectors and producing OPTIONAL / REQUIRED / BLOCKED-REVIEW counts without applying any owner operation.
- [x] **4.3-T4** Add concise plain-English traffic-light formatting for `aiverse doctor` and `aiverse upgrade`; keep full technical evidence in `--json`; default output must not expose release IDs, repository/filesystem paths, Git hashes, infrastructure generations, recipe IDs or component-owner jargon.
- [x] **4.3-T5** Add focused positive/destructive-negative tests for healthy whole-system aggregation, injected isolated owner failure, continued unrelated safe checks, doctor/upgrade read-only proof, OPTIONAL/REQUIRED/BLOCKED clarity, no-live-infrastructure compatibility, JSON evidence retention, and default-output jargon/path/hash leakage.
- [x] **4.3-T6** Qualify exact Distribution PR head and merged main, record exact evidence and acceptance results in System, update canonical Phase 4/overall counters, close Slice 4.3 and stop before Slice 4.4.

### Exact evidence

- detailed evidence: `docs/SAFE-INFRASTRUCTURE-SLICE-4.3-DOCTOR-UPGRADE-UX.md`;
- start/task record: System PR #202, merged as `b35e0ea4cefa7c770d2b786f52291f45cdb054a7`;
- Distribution PR #32 qualified head: `5ee2cfea8155907a279e6a33fe64505712151cab`;
- PR-head `Distribution CI` run `38374443919`: **SUCCESS**, six jobs;
- Distribution merged main: `15e03219185f484cbbc4c5887d967ddc5630d1a6`;
- exact merged-main `Distribution CI` run `38375126907`: **SUCCESS**, six jobs.

### Validation discoveries

- Synthetic 4.3 orchestrator tests initially invoked real Core transition-catalog validation through an incomplete mock. Fixtures were corrected to inject a transition contract rather than weakening production validation.
- Pending lifecycle state is authoritatively stored in the separate pending-lifecycle record. The destructive-negative test was corrected to create a real owner effect with `lifecycle_transaction()` and `begin_effect()` rather than inserting a derived receipt field.
- Existing expert `doctor --component ...` routing is preserved. Only whole-system member doctor uses the new overview formatter, so component-scoped diagnostic compatibility was not silently removed.

### Acceptance criteria

- one `aiverse doctor` command checks the whole supported installation from the member's perspective: **PASS**;
- owner checks execute internally with isolated evidence/results: **PASS**;
- one owner failure is surfaced accurately and cannot become a false whole-system PASS: **PASS**;
- unrelated safe owner results remain represented after another owner failure: **PASS**;
- member never needs component-specific doctor commands: **PASS**;
- existing expert component doctor remains available without becoming the member workflow: **PASS**;
- default summary is concise and plain English: **PASS**;
- full technical evidence is available on demand and machine-readable through `--json`: **PASS**;
- doctor/upgrade preview mutate nothing: **PASS**;
- OPTIONAL / REQUIRED / REVIEW-BLOCKED cases are explicit and actionable: **PASS**;
- default output does not expose release IDs, repository/filesystem paths, Git hashes, infrastructure generations or recipe IDs: **PASS**;
- internal lifecycle doctor semantics used by update/LKG/restore remain unchanged: **PASS**;
- exact PR-head and exact merged-main six-platform Distribution CI are green: **PASS**.

### Completion report

```text
Completed: Slice 4.3 - Implement one-command doctor and upgrade-plan aggregation with plain-English traffic-light UX
Tasks: 6/6
Overall: 14/18 slices (77.8%)
Phase: Phase 4 - Implement Distribution orchestration and simple member UX
Phase progress: 3/4
Until Phase 5: 1 slice
Next: Slice 4.4 - Implement `upgrade --apply` orchestration, resume and verification
Blockers/drift/amendments: no Slice 4.3 blocker or protected-law amendment.
```

### NEXT

**STOP after Slice 4.3 under the current one-at-a-time execution request.**

Next execution unit: Slice 4.4. Derive its adaptive task list only after fresh refs are fetched. No Safe Infrastructure Slice 4.4 implementation was started here.
'''

text = replace_once(text, old_slice, new_slice, "Slice 4.3 section")
ROADMAP.write_text(text, encoding="utf-8")
