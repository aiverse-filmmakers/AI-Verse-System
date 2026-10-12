# Safe Infrastructure Slice 3.4 - Capability Promotion / Re-scoping Evidence

Status: IN PROGRESS

## Refreshed refs

- System: `aiverse-filmmakers/AI-Verse-System@181cdee251e6d76dac50ff2cfde484f7e4be3b4d`
- OS: `aiverse-filmmakers/AI-Verse-OS@866359d877bfb3df0d8011d2d651a5ff947e21ca`
- Skills: `aiverse-filmmakers/AI-Verse-Skills@d4a02888ba8d83c4a15ce1b538ffdafaaf83bee1`

## Canonical decision

Slice 3.4 admits only the proven motivating promotion required by the roadmap fixture: a user-owned Workspace capability promoted to the user-owned personal `local` provider for reuse beyond one Workspace.

This is not an identity-preserving move. Under `ai-verse.durable-identity-reference/v1`, provider/scope participates in the current qualified identity, so `workspace:<workspace-id>:<name>` and `local:<name>` are different qualified identities. Promotion must therefore record an explicit source-to-target relationship, preserve source provenance/history, and repair exact old qualified-ID consumers through an OS-owned compatibility mechanism without pretending the old and new IDs are the same identity.

Managed `aiverse-skills` and `os` sources remain outside this personal promotion path. No generic cross-provider migration framework, local-to-Workspace demotion, distributed publication path, Workspace relocation, or new identity registry is admitted in this slice.

## Consumer/reference inventory

The shipped OS resolver is the canonical consumer boundary for user-owned capability qualified IDs. Explicit qualified selection currently resolves only a candidate with exactly that ID in the authorized providers and otherwise returns unavailable. The host/runtime binds executions and receipts to qualified capability identity plus generation/digest, but there is no canonical cross-owner database of durable user-capability references that can safely be batch-rewritten today.

Therefore reference repair for the proven fixture is implemented at the resolver boundary through a verified promotion compatibility record: an exact request for the retired Workspace-qualified identity may resolve to the promoted local identity only when OS-owned promotion evidence authorizes that relationship. The selection must expose the actual local identity and an explicit compatibility relationship; it must never report qualified identity continuity.

Workspace and local providers are directory-backed OS providers with deterministic `aiverse-package-sha256-v1` content evidence. Skills' immutable managed-generation lifecycle is separate and must remain unchanged.

## Adaptive task list

- [x] **3.4-T1** Refresh System, OS and Skills refs and re-read Slice 3.4, the durable identity law, provider contract, placement planner, resolver and current managed Skills boundary.
- [x] **3.4-T2** Inventory actual qualified-ID consumers/reference surfaces and determine the narrowest admitted repair mechanism. Confirm there is no owner-published durable user-capability reference registry to mutate; exact resolver selection is the compatibility boundary for the proven fixture.
- [x] **3.4-T3** Freeze the admitted migration semantics before implementation: Workspace -> local only; new qualified identity; source digest/generation-bound plan; provenance/history receipt; exact-ID compatibility repair; managed/OS sources blocked; ambiguity/conflict/source drift fail closed; no silent promotion.
- [ ] **3.4-T4** Implement the OS-owned promotion plan/apply transaction with verified staging, target conflict checks, source-drift invalidation, source-history preservation, deterministic receipt/compatibility metadata, source live-route retirement only after target verification, and idempotent replay/recovery behavior.
- [ ] **3.4-T5** Extend explicit qualified-ID selection to consume only validated active promotion compatibility records, returning the real target identity plus relationship evidence. Add the mandatory cross-context YouTube transcript/book fixture and destructive-negative tests for stale plans, conflicts, ambiguity, managed sources and replay.
- [ ] **3.4-T6** Document the owner boundary and validate exact current OS/Skills behavior. Skills must remain unchanged unless validation exposes an actual managed-provider lifecycle defect.
- [ ] **3.4-T7** Record exact commits and CI evidence, close all Slice 3.4 acceptance criteria in the canonical roadmap, complete Safe Infrastructure Phase 3, and stop before Phase 4 / Slice 4.1.

## Protected constraints

- Never infer identity continuity from matching names, paths or bytes.
- Never mutate `aiverse-skills` or OS built-ins through personal promotion.
- Never overwrite a different existing local capability.
- Never apply a stale plan after source drift.
- Preserve the original Workspace package as non-live promotion history before retiring its live provider route.
- Compatibility repair maps an old qualified ID to a new qualified ID; it is not an alias claiming identity equivalence.
- The member must not choose storage paths/provider IDs in normal placement UX.
- No Workspace relocation or distributed publication is implemented here.
