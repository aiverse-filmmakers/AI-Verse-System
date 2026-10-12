# Safe Infrastructure Slice 2.2 - Infrastructure Generation and Upgrade Recipe Contract

**Status:** IN PROGRESS  
**Slice:** 2.2 - Define versioned infrastructure generation and upgrade-recipe contract  
**Started:** 2026-10-12

## Exact starting refs

- `aiverse-filmmakers/AI-Verse-System@84320b46a964c22c16f35a68207d9e1a388bee8a`
- `aiverse-filmmakers/ai-verse-distribution@90f175418f8d13faeece8bcb1ad0796d2adecfb1`
- `aiverse-filmmakers/AI-Verse-OS@64f7325444d18f94c9d4755d32eb89f3468bda6b`
- `aiverse-filmmakers/AI-Verse-Skills@afde5c06307fba7d074de2929c2eb6c3dc6bdab8`

## Discovery result

The canonical `contracts/component-release-descriptor.schema.json` already contains a component-owned `migration` object with update compatibility, admitted source versions, owner-control and checkpoint policy. This is the correct release-metadata surface to extend. A second migration registry or parallel release metadata system is unnecessary.

Current indexed owner code does not expose a separate canonical infrastructure recipe format. Slice 2.2 therefore defines the shared contract only. It does not implement any owner-specific Workspace relocation, Skill re-scope/promotion, or Distribution upgrade execution.

## Classification

- component release descriptor: **EXTEND**;
- existing component release validator/tests: **EXTEND**;
- infrastructure generation/upgrade recipe semantics: **CREATE as a versioned nested descriptor contract**;
- separate migration registry: **RETIRE/DO NOT CREATE**;
- owner-specific migration handlers: **DEFER** to later owner slices;
- Distribution upgrade planner/apply orchestration: **DEFER** to Phase 4;
- canonical Identity contract `ai-verse.durable-identity-reference/v1`: **IMPORT/REUSE**.

## Derived task list

- [x] **2.2-T1** Refetch current roadmap, release descriptor, validator/tests and owner refs; prove whether an existing metadata surface can be extended.
- [ ] **2.2-T2** Define the minimum versioned infrastructure-generation and upgrade-recipe semantics without duplicating release or identity ownership.
- [ ] **2.2-T3** Extend `component-release-descriptor` with an optional owner-published infrastructure block so components without structural migration duties need no ceremonial metadata.
- [ ] **2.2-T4** Encode deterministic source/target generation, disposition, owner lifecycle operations, reference-repair obligations, recovery/idempotency requirements, direct-versus-chain behavior and retirement conditions.
- [ ] **2.2-T5** Extend validator/examples/tests with positive and destructive-negative cases that fail closed on ambiguous or unsafe recipes.
- [ ] **2.2-T6** Run canonical System contract validation at the exact resulting ref and close Slice 2.2 only if all acceptance criteria pass.

## Protected decisions for this slice

- Structural upgrade metadata lives inside the existing component release descriptor, not in a second registry.
- Infrastructure metadata is optional. Components publish it only when they own a real structural generation/migration responsibility.
- Recipe operations are owner lifecycle operation identifiers, never free-form shell commands or AI-authored mutation instructions.
- `OPTIONAL` and `REQUIRED` are explicit recipe dispositions. If no uniquely admitted recipe applies, the result is `BLOCKED/REVIEW`.
- v1 source generations are explicit finite sets. The contract does not invent free-form opaque generation ranges that an orchestrator would need to guess how to interpret.
- Every recipe binds to the exact component revision carried by the target descriptor; the enclosing admitted release set supplies the exact System release binding.
- Identity guarantees are referenced from `ai-verse.durable-identity-reference/v1` and owner evidence; they are not redefined here.
- Reference repair may cross owner boundaries only through explicitly named owner operations.
- Structural apply requires the whole-install Last-Known-Good guarantee frozen by Slice 2.1.
- Recipes must declare and prove idempotency before they can be admitted.
- Skip-version behavior is explicit: a recipe is either a direct path or a chain step. Ambiguous chains fail closed.

## NEXT

Implement 2.2-T2 through 2.2-T5, validate, then close the slice in the canonical roadmap.