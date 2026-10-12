# Safe Infrastructure Slice 2.2 - Infrastructure Generation and Upgrade Recipe Contract

**Status:** COMPLETE  
**Slice:** 2.2 - Define versioned infrastructure generation and upgrade-recipe contract  
**Started:** 2026-10-12  
**Completed:** 2026-10-12

## Exact starting refs

- `aiverse-filmmakers/AI-Verse-System@84320b46a964c22c16f35a68207d9e1a388bee8a`
- `aiverse-filmmakers/ai-verse-distribution@90f175418f8d13faeece8bcb1ad0796d2adecfb1`
- `aiverse-filmmakers/AI-Verse-OS@64f7325444d18f94c9d4755d32eb89f3468bda6b`
- `aiverse-filmmakers/AI-Verse-Skills@afde5c06307fba7d074de2929c2eb6c3dc6bdab8`
- slice-start evidence commit: `aiverse-filmmakers/AI-Verse-System@a3555907a6ed149ae39594f465e068a9af34f310`

## Discovery result

The canonical `contracts/component-release-descriptor.schema.json` already contained a component-owned `migration` object with update compatibility, admitted source versions, owner-control and checkpoint policy. This proved the correct architecture is to extend that release metadata surface rather than create a second migration registry or parallel release catalog.

Current indexed owner code did not expose a separate canonical infrastructure recipe format. Slice 2.2 therefore defines the shared contract only. It does not implement any owner-specific Workspace relocation, Skill re-scope/promotion, or Distribution upgrade execution.

## Classification

- component release descriptor: **EXTEND**;
- existing component release validator/tests: **EXTEND**;
- infrastructure generation/upgrade recipe semantics: **CREATE as a versioned nested descriptor contract**;
- separate migration registry: **RETIRE/DO NOT CREATE**;
- owner-specific migration handlers: **DEFER** to later owner slices;
- Distribution upgrade planner/apply orchestration: **DEFER** to Phase 4;
- canonical Identity contract `ai-verse.durable-identity-reference/v1`: **IMPORT/REUSE**.

## Final derived task list

- [x] **2.2-T1** Refetch current roadmap, release descriptor, validator/tests and owner refs; prove whether an existing metadata surface can be extended.
- [x] **2.2-T2** Define the minimum versioned infrastructure-generation and upgrade-recipe semantics without duplicating release or identity ownership.
- [x] **2.2-T3** Extend `component-release-descriptor` with an optional owner-published infrastructure block so components without structural migration duties need no ceremonial metadata.
- [x] **2.2-T4** Encode deterministic source/target generation, disposition, owner lifecycle operations, reference-repair obligations, recovery/idempotency requirements, direct-versus-chain behavior and retirement conditions.
- [x] **2.2-T5** Extend validator/examples/tests with positive and destructive-negative cases that fail closed on ambiguous or unsafe recipes.
- [x] **2.2-T6** Run canonical System contract validation at the exact resulting ref and close Slice 2.2 only after every acceptance criterion passes.

## Canonical contract

New canonical shared contract:

- `docs/INFRASTRUCTURE-GENERATION-AND-UPGRADE-RECIPE-CONTRACT.md`
- contract ID: `ai-verse.infrastructure-upgrade/v1`
- initial contract commit: `aiverse-filmmakers/AI-Verse-System@af3d20433a21e765632a3622d52229afdf3c3911`

The contract is carried by optional `migration.infrastructure` metadata inside `ai-verse.component-release/v1`. It does not create a sibling registry.

## Descriptor extension

`contracts/component-release-descriptor.schema.json` now permits an optional `migration.infrastructure` block with:

- exact `contract_version`;
- canonical `owner`;
- owner-defined `current_generation`;
- mandatory no-match disposition `BLOCKED/REVIEW`;
- zero or more versioned recipes.

Each recipe includes:

- stable `recipe_id` plus `recipe_version`;
- explicit finite `from_generations`;
- exact `to_generation`;
- exact enclosing component revision binding;
- executable disposition `OPTIONAL` or `REQUIRED`;
- owner lifecycle detector/apply/verify operation IDs;
- machine preconditions/postconditions;
- imported identity contract `ai-verse.durable-identity-reference/v1` plus owner identity evidence ref;
- explicit owner-scoped reference-repair operations;
- mandatory whole-install LKG protection;
- optional owner checkpoint requirement bound to the descriptor checkpoint policy;
- mandatory idempotency declaration plus accepted evidence kind;
- `direct` versus `chain-step` path mode;
- verified legacy-retirement policy;
- concise plain-English member summary.

Schema extension commit:

- `aiverse-filmmakers/AI-Verse-System@33e5210fec74c8add9f7f7a014c2afa03fdc181f`

## Deterministic validation

`scripts/validate_component_release_descriptor.py` was extended to enforce semantic safety beyond JSON shape.

It rejects at least:

- infrastructure owner mismatch;
- wrong/floating recipe target revision;
- shell-like/free-form operation strings;
- executable `BLOCKED/REVIEW` recipes;
- non-fail-closed no-match behavior;
- duplicate source-generation claims that create ambiguous paths;
- current generation reused as a migration source;
- source/target self-cycles;
- direct recipes that do not reach the current generation;
- dangling migration chains;
- cyclic migration chains;
- recipes published with unsupported checkpoint policy;
- owner checkpoint requirements without `owner-evidence-required` descriptor policy;
- missing whole-install LKG requirement;
- non-idempotent recipes;
- idempotency evidence kinds absent from passing descriptor acceptance evidence;
- replacement identity contracts;
- required reference repair without an owner operation;
- hidden repair operations when repair is declared unnecessary;
- unknown recipe fields such as `shell_command`.

Validator commit:

- `aiverse-filmmakers/AI-Verse-System@51e36ca1edf0a765b5cbbc232164a75d0f1614f6`

## Positive fixture and regression coverage

New fixture:

- `contracts/examples/component-release-descriptor.valid-infrastructure-upgrade.json`
- fixture commit: `aiverse-filmmakers/AI-Verse-System@d89089a9e41d4b96df67315f14a2a6edb1938c75`

The fixture proves both:

- a direct old-generation -> current-generation recipe;
- a deterministic multi-step chain whose exact outputs become the next exact sources.

Existing descriptors without `migration.infrastructure` remain valid, proving the extension does not force ceremonial structural metadata onto components that do not need it.

Expanded contract tests:

- `tests/test_component_release_descriptor.py`
- tested commit: `aiverse-filmmakers/AI-Verse-System@187269760d128867585bebe915d2f2b593f6fb73`

## Exact validation evidence

GitHub Actions:

- workflow: `Contract Validation`;
- run ID: `38283320350`;
- exact head SHA: `187269760d128867585bebe915d2f2b593f6fb73`;
- conclusion: **SUCCESS**;
- Python 3.11 job: **SUCCESS**;
- Python 3.13 job: **SUCCESS**;
- contract tests: **SUCCESS** on both versions;
- schema/example/repository-state validation: **SUCCESS**;
- live read-only Core repository refresh on Python 3.11: **SUCCESS**.

## Frozen semantics

- Structural upgrade metadata lives inside the existing component release descriptor, not in a second registry.
- Infrastructure metadata is optional. Components publish it only when they own a real structural generation/migration responsibility.
- Recipe operations are owner lifecycle operation identifiers, never free-form shell commands or AI-authored mutation instructions.
- `OPTIONAL` and `REQUIRED` are explicit executable recipe dispositions. If no uniquely admitted path applies, the result is `BLOCKED/REVIEW`.
- v1 source generations are explicit finite sets. The contract does not invent free-form opaque generation ranges that an orchestrator would need to guess how to interpret.
- Every recipe binds to the exact component revision carried by the target descriptor; the enclosing admitted release set supplies the exact System release binding.
- Identity guarantees are imported from `ai-verse.durable-identity-reference/v1` and owner evidence; they are not redefined here.
- Reference repair may cross owner boundaries only through explicitly named owner operations.
- Structural apply requires the whole-install Last-Known-Good guarantee frozen by Slice 2.1.
- Recipes must declare and prove idempotency before they can be admitted.
- Skip-version behavior is explicit and deterministic: direct path or unique exact chain. Ambiguous, cyclic, dangling or unsupported paths fail closed.
- Legacy writable infrastructure can retire only after required postconditions/reference repair succeed.

## Acceptance criteria

- `upgrade --apply` never depends on free-form AI inference to know what structural mutation to execute: **PASS**;
- exact owner and exact migration path are machine-resolvable: **PASS**;
- OPTIONAL versus REQUIRED behavior is machine-resolvable: **PASS**;
- unsupported/unknown path fails closed or becomes REVIEW/BLOCKED: **PASS**;
- recipe internals are not required knowledge for the member: **PASS**;
- recipes rely only on identity guarantees explicitly admitted by the canonical identity contract: **PASS**;
- no parallel release/migration registry was introduced: **PASS**;
- legacy component descriptors remain valid without ceremonial infrastructure metadata: **PASS**;
- deterministic direct/chain semantics and idempotency/recovery requirements have executable contract tests: **PASS**.

## Completion report

```text
Completed: Slice 2.2 - Define versioned infrastructure generation and upgrade-recipe contract
Tasks: 6/6
Overall: 6/18 slices (33.3%)
Phase: Phase 2 - Define canonical convergence, migration and recovery contracts
Phase progress: 2/3
Until next phase: 1 slice
Next: Slice 2.3 - Define convergence, restore, doctor and member UX invariants
Blockers/drift/amendments: none. Existing component release metadata was safely extended; no parallel migration registry was created.
```

## NEXT

**STOP after Slice 2.2 for the current one-at-a-time execution request.**

Next execution unit: Slice 2.3.