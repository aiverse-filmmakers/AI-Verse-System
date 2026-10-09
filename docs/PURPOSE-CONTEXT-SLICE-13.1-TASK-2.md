# Purpose Context Slice 13.1 Task 2

**Status:** COMPLETE / ACCEPTED  
**Date:** 2026-10-09  
**Task:** document CLI/API usage

## Result

Created `docs/PURPOSE-CONTEXT-USAGE.md` and documented the admitted Purpose Context v1 CLI and library interfaces against the exact admitted OS contract.

Documented:

- CLI `read` and `explain` commands;
- `--root` / `--dir`, `--scope`, `--profile`, `--relevant-domain`, `--max-bytes`, and `--ref` inputs;
- JSON output and fail-closed behavior;
- public library surfaces `composePurposeContext(root, scope, options)` and `composeProfiledPurposeContext(root, scope, options)`;
- owner-reader integration without authority transfer;
- schema `1.0`, 16,384-byte default budget, admitted 4,096-65,536-byte caller range;
- no durable Purpose store/cache and rebuild-from-owner behavior;
- explicit Brain-owner unavailability behavior and Data ownership boundary.

## Exact implementation source inspected

- AI-Verse OS: `4f03849444b1d01ad81317bf0fece082d5a30e79`
- `system/architecture/purpose-context.md`
- `scripts/purpose-context.mjs`
- `scripts/purpose-context-core.mjs`
- `scripts/purpose-context-profile.mjs`
- qualified Gateway runtime remains `1772b75e2add73a524715f746e87b3a6b5561bf6`

## Ownership decision

Documentation exposes the existing OS read surface only. It does not define a new Purpose HTTP service, database, cache, or owner. Gateway remains a runtime consumer/integrator rather than the canonical Purpose owner.

## Change type

Documentation only. No runtime, owner contract, release ref, or schema behavior changed.

## NEXT

Slice 13.1 Task 3 - document operator vs workspace behavior.
