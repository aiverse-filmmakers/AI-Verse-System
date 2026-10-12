# Safe Infrastructure Slice 2.1 - Contract Reconciliation

**Status:** IN PROGRESS  
**Slice:** 2.1 - Amend the Safe Update and State Preservation Contract  
**Started:** 2026-10-12  

## Entry-gate reconciliation

Safe Infrastructure Phase 1 is complete. Identity Hardening Phase 1 is also complete and now publishes the canonical System identity/reference contract:

- `docs/DURABLE-IDENTITY-AND-CANONICAL-REFERENCE-CONTRACT.md`
- contract ID: `ai-verse.durable-identity-reference/v1`
- Identity Phase 1 closure: `aiverse-filmmakers/AI-Verse-System@7587e9e13a6d712b8a8e50f18aca64d349859ff1`

The reconciliation checkpoint found no protected-law conflict. The Identity contract confirms the Safe Infrastructure Phase 1 freezes:

- Workspace logical identity is `WORKSPACE.yaml:id`;
- current supported Workspace storage remains `workspaces/<workspace-id>`;
- arbitrary Workspace relocation remains unsupported;
- capability provider/scope remains part of current qualified capability identity;
- cross-provider re-scope is not assumed identity-preserving;
- owner-specific durable IDs remain canonical;
- ambiguous/conflicting identity evidence fails closed;
- update, upgrade, recovery and restore may rely only on identity guarantees explicitly published by the canonical owner.

Safe Infrastructure therefore consumes the Identity contract without duplicating or weakening it.

## Exact starting refs

- `aiverse-filmmakers/AI-Verse-System@7587e9e13a6d712b8a8e50f18aca64d349859ff1`
- `aiverse-filmmakers/ai-verse-distribution@fd11b4a95487638d47ff55472a3703b03892d0e8`

Primary existing Distribution contracts inspected:

- `docs/CORE-UPDATE-OWNERSHIP-CONTRACT.md`
- `docs/CORE-UPDATE-TRANSITION-CONTRACT.md`

## Classification

- existing Core updater and one-action `aiverse update`: **REUSE**;
- existing ownership/pre-write zero-loss contract: **REUSE**;
- existing Core update transition/state-preservation contract: **EXTEND**;
- owner-native transaction checkpoints/journal recovery: **REUSE**;
- whole-install Last-Known-Good product guarantee: **EXTEND contract now, implementation later**;
- whole-install restore preview/apply implementation: **CREATE later on existing Distribution transaction substrate**;
- Identity contract: **IMPORT/REUSE**, never duplicate.

## Derived task list

- [x] **2.1-T1** Reconcile completed Identity Phase 1 against Safe Infrastructure Phase 1 and prove the Phase 2 gate is satisfied.
- [ ] **2.1-T2** Extend the existing Distribution Core Update Transition Contract to distinguish software update, update preview, owner-native transaction recovery, software rollback, structural upgrade and whole-install restore without changing shipped update semantics.
- [ ] **2.1-T3** Define the one rotating whole-install Last-Known-Good contract: candidate staging, verification, atomic promotion, bounded retention and failure behavior.
- [ ] **2.1-T4** Define restore preview/apply semantics and explicit exclusions, including external systems and security-sensitive state, while importing identity/reference guarantees from the canonical System Identity contract.
- [ ] **2.1-T5** Add focused contract validation/tests proving the separation and preservation laws without implementing restore yet.
- [ ] **2.1-T6** Run exact-ref Distribution validation, record evidence, update the canonical Safe Infrastructure roadmap and close Slice 2.1 only if every acceptance criterion passes.

## Protected constraints

- `aiverse update` remains the mutating one-action safe software updater.
- `aiverse update --plan` remains read-only.
- `aiverse upgrade` remains structural preview; `aiverse upgrade --apply` is the explicit structural mutation path.
- software rollback remains software-only by default and does not rewind user state.
- owner-native checkpoints remain authoritative for component transaction safety.
- whole-install Last-Known-Good is a separate recovery layer, not a replacement for owner checkpoints.
- only one usable retained whole-install recovery point is required.
- a previous valid recovery point cannot be destroyed until a verified successor is promoted.
- restore must be preview-first and explicit before mutation.
- restore must not claim to rewind external systems or side effects it cannot control.
- durable identity/reference semantics are imported from `ai-verse.durable-identity-reference/v1`.

## NEXT

Implement 2.1-T2 through 2.1-T5, validate, then close the slice in the canonical roadmap.