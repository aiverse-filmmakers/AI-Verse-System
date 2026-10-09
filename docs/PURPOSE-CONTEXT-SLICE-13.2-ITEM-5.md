# Purpose Context Slice 13.2 - Completion Item 5

**Item:** supported scope/profile behavior  
**Status:** COMPLETE / ACCEPTED  
**Date:** 2026-10-09

The final completion statement now records the admitted v1 scope/profile contract:

- scopes: `operator` and exact `workspace:<id>` only;
- operator: `auto` only, resolving to `operator_default`;
- workspace: `auto`, `basic`, and `rich`;
- `auto` promotes from `workspace_basic` to `workspace_rich` only when relevant rich context is backed by canonical owner evidence;
- optional rich domains are owner-backed and omitted when unsupported;
- no `purpose_context` block is added to `WORKSPACE.yaml`;
- cross-workspace reads remain fail-closed;
- no profile grants authority or creates a Purpose truth store.

Canonical record: `docs/PURPOSE-CONTEXT-FINAL-COMPLETION.md`.

## Result

Completion item 5 is **COMPLETE / ACCEPTED**.

## NEXT

Slice 13.2 completion item 6 - record the Slice 7.3 value-gate outcome and measured overhead.
