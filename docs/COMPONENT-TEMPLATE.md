# Component Documentation Template

Use this structure for every component folder.

## Files

```text
components/<component>/
├── COMPONENT-SPEC.md
├── SOURCE-MAP.md
└── QC.md
```

## COMPONENT-SPEC.md headings

1. Executive identity
2. Status vocabulary
3. Role in the complete system
4. Problem the component solves
5. Current architecture
6. Canonical ownership
7. Explicit non-ownership
8. Sources of truth
9. Runtime model
10. Scope and isolation
11. Current lifecycle
    - install
    - attach/register
    - initialize
    - enable/disable
    - status/doctor
    - update
    - detach
    - uninstall
12. Migration/history integration
13. Intended lifecycle
14. Install-order independence
15. Activation/adoption by existing agents
16. Portability outside AI-Verse OS
17. Sibling integrations
18. Permissions/security/privacy
19. Failure and degraded modes
20. Important historical repairs
21. Permanent laws established by repairs
22. Inspirations and curated references
23. Current gaps and contradictions
24. Desired future state
25. Definition of done
26. Contribution to the supreme AI-Verse vision
27. Open decisions
28. Current intended milestone
29. Current-target readiness verdict
30. Implementation completeness by dimension
31. Command/lifecycle matrix
32. Exact missing work before seamless operation

## Required labels

Use these semantics consistently:

- **CURRENT** - proven implementation/support.
- **LAW** - invariant the architecture is intended to preserve.
- **INTENDED** - desired future behavior.
- **GAP** - missing path between current and intended.
- **HISTORICAL** - previous/legacy behavior relevant to migration or lessons.
- **INSPIRATION** - evidenced reference system/framework/project.

## SOURCE-MAP.md

Capture:

- canonical repository and reviewed revision/date;
- identity/runtime files;
- architecture docs;
- lifecycle/install docs;
- status/release docs;
- tests/CI used as evidence;
- major repair/audit documents;
- major commits/PRs;
- inspiration/reference documents;
- evidence limitations.

This file should make the component spec auditable without turning it into a code listing.

## QC.md

Record these independent verdicts:

1. Architecture/ownership QC
2. Lifecycle/install-order QC
3. Migration/history QC
4. Integration QC
5. Security/isolation QC
6. Runtime portability QC
7. Product/UX QC
8. Historical-learning QC
9. Inspiration/curation QC
10. Current-target readiness QC
11. Future-state coherence QC
12. Contradiction scan
13. Final documentation verdict

Every QC should state:

- PASS
- PASS WITH GAPS
- FAIL / REQUIRES CORRECTION

and explain why.

## Documentation rule

Never "fix" the source repository merely to make the documentation cleaner.

If current implementation and intended architecture differ, document the gap precisely. Source changes belong in a separately scoped implementation task.


## Mandatory current-target readiness section

Every component specification must include a present-stage readiness block with:

### Current intended milestone

State what this repository is supposed to accomplish **now**, based on current release/build/status evidence.

### Completeness dimensions

Use:

- Engine/core functionality
- OS/host integration
- Install/package path
- Attach/register path
- Activation/adoption path
- Scope initialization
- Legacy/history migration
- Doctor/status/health
- Disable/detach/uninstall/reinstall
- Cross-component acceptance
- Member/public distribution

Each dimension must be labeled one of:

- COMPLETE
- COMPLETE WITH LIMITATIONS
- PARTIAL
- MISSING
- EXTERNALLY BLOCKED
- NOT REQUIRED FOR CURRENT TARGET

### Command/lifecycle matrix

| Capability | Required now? | Command/path | End-to-end proven? | Missing work |
|---|---|---|---|---|
| Install | | | | |
| Attach/register | | | | |
| Activate/adopt | | | | |
| Initialize | | | | |
| Migrate/import | | | | |
| Doctor/status | | | | |
| Update | | | | |
| Disable | | | | |
| Detach/uninstall | | | | |
| Reinstall/reconcile | | | | |

### Seamless-operation blockers

End the section with the exact remaining work before the component can be described as:

> works perfectly together like a glove with the current AI-Verse system.

This must be concrete implementation work, not vague future aspirations.


## Continuous maintenance

After the initial component review, update these files whenever the component changes materially.

### Idea accepted but not implemented

- add/update **INTENDED** behavior in COMPONENT-SPEC;
- add a **GAP** if current implementation does not satisfy it;
- update current-target readiness when the accepted idea becomes part of the current milestone;
- preserve provenance through IDEA-INBOX / SYSTEM-CHANGELOG.

### Implementation lands

- promote applicable INTENDED/GAP statements to CURRENT;
- update command/lifecycle matrix;
- update completeness dimensions;
- update SOURCE-MAP with commit/test/release evidence;
- rerun QC;
- append SYSTEM-CHANGELOG.

### Repair lands

Also record:

- old defect;
- repair;
- permanent law;
- potential cross-component applicability.

### Plan changes

If a feature is deferred/rejected/superseded, change its status explicitly. Never leave stale intent looking active.

The component documents should always describe the **latest known current system + accepted intended system**.
