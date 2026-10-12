# Safe Infrastructure Slice 3.1 - OS Workspace Generation and Structural Semantics

**Status:** IN PROGRESS  
**Slice:** 3.1 - Implement OS Workspace generation and evidence-backed structural semantics  
**Started:** 2026-10-12

## Exact starting refs

- `aiverse-filmmakers/AI-Verse-System@563659432d8609f908b44fae676f10496d47ec96`
- `aiverse-filmmakers/AI-Verse-OS@64f7325444d18f94c9d4755d32eb89f3468bda6b`

## Current implementation evidence reused

AI-Verse-OS already owns conservative Workspace creation and evolution through `scripts/workspace-owner.mjs`:

- canonical Workspace identity comes from `WORKSPACE.yaml:id`;
- new Workspaces are created at `workspaces/<id>`;
- existing Workspaces are discovered as direct children of `workspaces/`;
- domain/category information is semantic metadata, not a physical hierarchy;
- additive manifest evolution preserves unrelated/custom fields;
- unsupported YAML shapes are left unchanged instead of being normalized by guesswork;
- ambiguity and authority expansion fail closed;
- no arbitrary Workspace relocation resolver exists.

`workspaces/README.md` explicitly describes the full template tree as recommended/optional and says active Workspaces should not create every optional subfolder merely to look complete. Structural generation therefore cannot be defined as byte-for-byte/template-tree equality.

The canonical Identity contract remains `ai-verse.durable-identity-reference/v1`, with current supported physical storage `workspaces/<workspace-id>` and no arbitrary relocation support.

## Classification

- existing Workspace owner/create/evolve primitive: **REUSE**;
- current Workspace schema and ID-derived storage law: **REUSE**;
- read-only OS-owned Workspace infrastructure generation detector: **CREATE minimally**;
- owner architecture documentation for generation semantics: **CREATE/EXTEND**;
- Workspace relocation/move/reference-repair engine: **DEFER to Slice 3.2 and only if evidence requires it**;
- domain-first physical nesting: **RETIRE as an old roadmap assumption, not an implementation target**;
- component release `migration.infrastructure` publication: **CONDITIONAL** on exact release/evidence truth; do not publish stale or unqualified metadata merely to satisfy the roadmap.

## Derived task list

- [x] **3.1-T1** Refresh System/OS refs and inspect current Workspace schema, owner primitive, template/readme, tests, release descriptor and Phase 2 infrastructure contract.
- [ ] **3.1-T2** Define one OS-owned current Workspace infrastructure generation and fail-closed structural detection semantics that preserve `workspaces/<id>` and do not treat optional/custom content as drift.
- [ ] **3.1-T3** Implement a read-only OS Workspace infrastructure detector plus concise owner architecture documentation; reuse the shipped Workspace owner rather than creating a second creation/migration subsystem.
- [ ] **3.1-T4** Add destructive-negative tests proving current direct-child Workspaces pass, custom files survive classification, semantic domain metadata does not affect physical generation, identity/path conflicts fail closed, unsupported nested relocation is not silently accepted, and detection performs no mutation.
- [ ] **3.1-T5** Integrate the detector into exact OS validation/CI and decide from evidence whether the current release descriptor can truthfully publish the generation now or must defer publication to the next admitted descriptor revision.
- [ ] **3.1-T6** Run exact-ref OS CI, record implementation/evidence refs, update the canonical Safe Infrastructure roadmap, and close Slice 3.1 only if every acceptance criterion passes. Stop before Slice 3.2.

## Protected constraints

- OS owns Workspace generation/structural semantics. Distribution must not infer them from paths itself.
- Logical identity remains `WORKSPACE.yaml:id`.
- Current supported physical slot remains `workspaces/<id>`.
- Arbitrary/nested relocation remains unsupported unless a later explicit owner/System amendment admits it.
- A valid existing Workspace does not need to mirror every optional `_template` directory.
- Unknown/custom files and directories inside a valid Workspace are user-owned by default and must not be normalized or deleted by detection.
- Domain/category organization remains semantic metadata under current architecture.
- Duplicate, malformed, unreadable, symlinked or identity-conflicting Workspace evidence fails closed rather than being guessed.
- The detector is read-only. No migration, move, cleanup, reference repair or authority change belongs in this slice.
- Component release metadata must remain exact and evidence-backed. A stale accepted descriptor must not be rewritten to claim an unqualified new revision.

## NEXT

Implement 3.1-T2 through 3.1-T5, validate at exact refs, then close Slice 3.1 in the canonical roadmap. Do not start Slice 3.2 in this execution unit.