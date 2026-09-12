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
10. Future-state coherence QC
11. Contradiction scan
12. Final documentation verdict

Every QC should state:

- PASS
- PASS WITH GAPS
- FAIL / REQUIRES CORRECTION

and explain why.

## Documentation rule

Never "fix" the source repository merely to make the documentation cleaner.

If current implementation and intended architecture differ, document the gap precisely. Source changes belong in a separately scoped implementation task.
