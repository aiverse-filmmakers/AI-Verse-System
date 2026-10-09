# Purpose Context Slice 13.1 Task 3

**Status:** COMPLETE / ACCEPTED  
**Date:** 2026-10-09  
**Task:** document operator vs workspace behavior

## Result

Extended `docs/PURPOSE-CONTEXT-USAGE.md` with the admitted scope behavior for `operator` and `workspace:<id>`.

Documented:

- `operator` as the personal/global trajectory scope;
- operator `auto` -> `operator_default` behavior and rejection of workspace-only `basic`/`rich` requests;
- `workspace:<id>` as one bounded project/product/client/team/business/custom scope;
- workspace `auto`, `basic`, and `rich` behavior;
- compact workspace trajectory shape;
- deterministic rich-profile eligibility rather than inference from name/type/importance/free text;
- no v1 `purpose_context` block in `WORKSPACE.yaml`;
- fail-closed workspace isolation and exact-scope owner evidence;
- explicit cross-scope refs do not grant implicit foreign-scope resolution/enumeration/ingestion.

## Exact implementation source inspected

- AI-Verse OS `4f03849444b1d01ad81317bf0fece082d5a30e79`
- `system/architecture/purpose-context.md`
- `scripts/purpose-context-profile.mjs`
- `system/schemas/workspace.schema.yaml`

## Change type

Documentation only. No scope validator, workspace manifest, owner contract, release ref, or runtime behavior changed.

## NEXT

Slice 13.1 Task 4 - document optional rich workspace fields.
