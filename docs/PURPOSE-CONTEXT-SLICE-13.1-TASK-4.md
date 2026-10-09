# Purpose Context Slice 13.1 Task 4

**Status:** COMPLETE / ACCEPTED  
**Date:** 2026-10-09  
**Task:** document optional rich workspace fields

## Result

Extended `docs/PURPOSE-CONTEXT-USAGE.md` with the admitted optional rich-workspace contract.

Documented:

- `narratives` and `kpis` as rich-profile contextual sections suppressed by `workspace_basic`;
- exact optional owner-backed domains: `risks`, `team_resources`, `customers`, `infrastructure`, and `budget_cost`;
- exact-scope evidence requirement and omission of absent/malformed/foreign-scope rich data;
- `current_state` and `recent_material_changes` as relevance inputs without creating a new current-state/activity owner;
- initiative lifecycle status remains on the canonical Brain initiative object rather than a duplicate Purpose operational-status field;
- explicit `rich` and automatic rich-resolution examples using `--relevant-domain`;
- progressive-disclosure rule: simple workspaces remain simple and rich mode grants no authority or cross-workspace access.

## Exact implementation source inspected

- AI-Verse OS `4f03849444b1d01ad81317bf0fece082d5a30e79`
- `system/architecture/purpose-context.md`
- `scripts/purpose-context-profile.mjs`
- `scripts/purpose-context-rich-domains.mjs`
- canonical implementation plan rich-workspace contract in `docs/PURPOSE-CONTEXT-IMPLEMENTATION-PLAN.md`

## Change type

Documentation only. No rich-domain registry, owner read, workspace profile, schema, release ref, or runtime behavior changed.

## NEXT

Slice 13.1 Task 5 - document explain/trajectory behavior.
