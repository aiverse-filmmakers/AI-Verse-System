# AI-Verse Identity Hardening Implementation Plan

**Status:** Persistent execution source of truth  
**Program:** AI-Verse durable identity hardening  
**Canonical planning repo:** `aiverse-filmmakers/AI-Verse-System`  
**Started:** 2026-10-12  
**Planning method:** `docs/ADAPTIVE-IMPLEMENTATION-PLANNING-SKILL.md`  
**Rule:** Update this file before and after every implementation slice. Overall progress is measured by completed slices, not by provisional task counts.

## 0. Mission

Make durable identity consistent across AI-Verse without creating another identity subsystem.

The program must preserve and standardize the strong owner-specific ID systems that already exist, define the minimum shared law needed for cross-owner references, fix only verified gaps, and prove that durable identities survive normal lifecycle and Core updates.

The target is not “IDs everywhere.” The target is stable identity where identity is actually required.

## 0A. Permanent laws

1. A durable first-class entity that must be referenced across time or by another AI-Verse owner has a stable owner-controlled ID.
2. Identity is separate from display name and other mutable descriptive properties.
3. The canonical owner owns ID generation, validation, lookup, migration and lifecycle semantics for its entities.
4. AI-Verse-System defines the shared law and reference contract only. It does not become a global identity registry or second source of truth.
5. Cross-owner durable references use the smallest common envelope needed to identify the canonical owner and entity: `owner`, `kind`, `id`, and `scope` only when scope is part of correct resolution.
6. Files, caches, generated indexes, temporary outputs and other non-durable implementation artifacts do not receive IDs merely for uniformity.
7. Filesystem independence is not a universal requirement. A canonical owner may intentionally derive a physical storage slot from an ID.
8. Workspace storage remains `workspaces/<workspace-id>` unless verified evidence justifies a separate plan amendment. This program does not introduce arbitrary workspace relocation.
9. Scope transfer is owner-defined. A scope change must not be assumed to preserve identity unless that owner explicitly supports and tests it.
10. Ambiguous, duplicate, malformed or conflicting identity evidence fails safely instead of being guessed or silently rebound.
11. Existing mature owner identity implementations are reused when they already satisfy these laws. This program must not rewrite them for stylistic uniformity.
12. Core updates must preserve durable user-owned identities and their references.

## 0B. Anti-bloat boundary

This program must not create:

- a global UUID service;
- a central identity database;
- a second registry of owner objects;
- a requirement that every file or row receive a new generic ID;
- a universal ID format when owners already have valid formats;
- an automatic workspace relocation engine;
- a generic re-scope framework;
- duplicated owner state inside AI-Verse-System;
- replacement implementations for working owner-specific identity systems.

If an existing mechanism satisfies the contract, classify it `REUSE` and leave it alone.

## 0C. Current reality baseline

The pre-plan audit found the following starting classification. Slice 1.1 refreshes this against current repository heads.

| Surface | Starting classification | Reason |
| --- | --- | --- |
| Workspace / OS | REUSE + CLARIFY | Stable logical ID exists; canonical storage is currently coupled to `workspaces/<id>`. |
| Brain objects / Goals | REUSE | Durable object IDs and revisioned identity already exist. |
| Memory records | REUSE | Durable record IDs already exist. |
| Data records | REUSE | Stable record identity and strict workspace identity checks already exist. |
| Skills | REUSE | Stable skill/proposal/generation identities already exist. |
| Automations | REUSE | Durable automation/trigger/run identities already exist. |
| Multiple Bots | REUSE | Durable typed IDs already exist across first-class bot entities. |
| Connections | REUSE | Connection identity is owner-managed and registry-backed. |
| Apps | CREATE / EXTEND | Stable app identity is required by architecture but implementation is incomplete. |
| OS canonical reference shape | EXTEND | Existing `owner + scope + kind + id` pattern is a strong basis for a shared reference contract. |
| System contracts | EXTEND | No single ecosystem-wide durable identity contract currently governs all owners. |
| Distribution preservation | EXTEND | Update safety exists; durable identity preservation should become explicit evidence. |
| Dashboard `systemId` | REUSE AS LOCAL ID | Dashboard-local connection identity remains Dashboard-owned and is not promoted into a global identity service by this program. |
| Canonical installation-wide AI-Verse instance ID | OUT OF SCOPE unless proven necessary | Do not add one merely for symmetry. |

## 0D. Status vocabulary

- `NOT STARTED`
- `IN PROGRESS`
- `BLOCKED`
- `COMPLETE`

Every slice must record:

- affected repo(s);
- exact starting refs/state inspected;
- derived execution tasks;
- acceptance criteria;
- tests/validation;
- exact evidence;
- blockers/drift/amendments;
- explicit NEXT slice.

Low-level tasks are adaptive and are derived only when the slice starts.

## 0E. Progress

**Total slices:** 8  
**Completed slices:** 3  
**Overall:** 3/8 (37.5%)  
**Current phase:** Phase 1 - COMPLETE  
**Phase progress:** 2/2  
**Next program-local slice:** Slice 2.1 - Align owner integrations to the shared contract with minimum change  
**Cross-program execution pause:** reconcile the completed Identity contract against Safe Infrastructure, then resume Safe Infrastructure Phase 2 / Slice 2.1 before returning to Identity Phase 2, per owner sequencing.

---

# Phase 0 - Persistent plan

## Slice 0.1 - Create the canonical identity hardening plan

**Status:** COMPLETE  
**Repos:** AI-Verse-System  
**Dependencies:** none

### Outcome

A persistent adaptive implementation plan exists before any identity implementation changes begin.

### Acceptance criteria

- permanent identity laws are explicit;
- anti-bloat boundaries are explicit;
- current known mechanisms are classified as `REUSE`, `EXTEND`, `CREATE` or out of scope;
- phases and slices have fixed outcomes and measurable acceptance criteria;
- future low-level tasks are intentionally not frozen in advance;
- no owner implementation is changed by this slice.

### Evidence

- canonical path: `docs/AI-VERSE-IDENTITY-HARDENING-IMPLEMENTATION-PLAN.md`
- planning method: `docs/ADAPTIVE-IMPLEMENTATION-PLANNING-SKILL.md`
- initial plan commit: `9ce5ca1884718a210305de29ce896f873bdd94e9`

### NEXT

**Slice 1.1 - Refresh the cross-Core identity map.**

---

# Phase 1 - Freeze the shared identity contract from current reality

## Slice 1.1 - Refresh the cross-Core identity map

**Status:** COMPLETE  
**Repos:** AI-Verse-System plus identity-relevant Core owner repos  
**Dependencies:** 0.1  
**Adaptive tasks:** 6/6 COMPLETE

### Starting refs

Refs refreshed before Identity Slice 1.1 audit work:

- `aiverse-filmmakers/AI-Verse-System@423e04917a9f1a9b4f012fa9daf4366fc8135e8c`
- `aiverse-filmmakers/AI-Verse-OS@64f7325444d18f94c9d4755d32eb89f3468bda6b`
- `aiverse-filmmakers/AI-Verse-Brain@69f7912eeb35f0178f6952ff0554aec8d7f2c496`
- `aiverse-filmmakers/AI-Verse-Memory@f1327be48ba2ee0043959021365e6dbb9dcb1d3a`
- `aiverse-filmmakers/AI-Verse-Data@f8978f8f7a1bc94edecddc2662112233289159a3`
- `aiverse-filmmakers/AI-Verse-Skills@afde5c06307fba7d074de2929c2eb6c3dc6bdab8`
- `aiverse-filmmakers/AI-Verse-Automations@287ce9d6718ef06e4589a2a3e767c6a9ba376755`
- `aiverse-filmmakers/AI-Verse-Multiple-Bots@ddf70ac19736f6ca7f8d604901c20af9e46614fe`
- `aiverse-filmmakers/AI-Verse-Connections@602a1c52ab782cc9a8b7a4caa60ccb29efe403d1`
- `aiverse-filmmakers/AI-Verse-Apps@db5b0115bf59d6eae9149137a40e891968f3a637`
- `aiverse-filmmakers/AI-Verse-Gateway@1772b75e2add73a524715f746e87b3a6b5561bf6`
- `aiverse-filmmakers/AI-Verse-Dashboard@bd26986e202d4b911d0c5f64659db71363bfccfa`
- `aiverse-filmmakers/ai-verse-token@d36916323abb5f396bd8fd6b7f5c3ef84af519d0`
- `aiverse-filmmakers/ai-verse-distribution@fd11b4a95487638d47ff55472a3703b03892d0e8`

OS, Brain, Memory, Data, Skills and Distribution still matched the exact refs used by Safe Infrastructure Phase 1. Their completed identity findings were therefore reused rather than re-audited.

Slice-start bookkeeping commit:

- `aiverse-filmmakers/AI-Verse-System@4d8b7cf51705bdf8e2c498549a2003e50b6abb50`

### Final derived task list

- [x] **1.1-T1** Refresh all in-scope repository heads and verify which Safe Infrastructure Phase 1 evidence remains exact-current.
- [x] **1.1-T2** Reuse Safe Infrastructure Slice 1.2/1.3 evidence to confirm Workspace, Skill/provider and Distribution identity conclusions without duplicating those audits.
- [x] **1.1-T3** Inspect only identity-relevant surfaces in Automations, Multiple Bots, Connections, Apps, Gateway, Dashboard and Token that Safe Infrastructure did not cover.
- [x] **1.1-T4** Refresh current System identity/spec/reference surfaces and identify any duplicate or competing identity mechanisms.
- [x] **1.1-T5** Produce the final cross-Core identity matrix with canonical owner and `REUSE` / `EXTEND` / `CREATE` / `RETIRE` / `BLOCK/UNKNOWN` classification for every relevant durable identity surface.
- [x] **1.1-T6** Record exact evidence, acceptance closure, remaining gaps and the minimal handoff to Slice 1.2. No component implementation changes were made.

### Evidence reuse

Authoritative completed Safe Infrastructure inputs reused directly:

- `docs/SAFE-INFRASTRUCTURE-SLICE-1.2-INVENTORY.md`
- `docs/SAFE-INFRASTRUCTURE-SLICE-1.3-ARCHITECTURE-FREEZE.md`
- final Phase 1 decisions in `docs/SAFE-INFRASTRUCTURE-UPGRADE-AND-RECOVERY-IMPLEMENTATION-PLAN.md`

Detailed Identity Slice 1.1 evidence and final matrix:

- `docs/IDENTITY-HARDENING-SLICE-1.1-CROSS-CORE-IDENTITY-MAP.md`
- evidence commit: `aiverse-filmmakers/AI-Verse-System@b412a0b668aeaa050e2f92bba20fca0d2985ab17`

### Final classification summary

#### `REUSE`

- Workspace logical ID `WORKSPACE.yaml:id` and current ID-derived storage contract `workspaces/<id>`;
- OS provider scope/resolution/ranking;
- managed Skills package identity/lifecycle and immutable generation model;
- user-owned personal reusable capability provider;
- Workspace-owned local capability provider;
- Brain durable object IDs;
- Memory record IDs;
- Data space/entity/record IDs;
- Automations automation/trigger/run/invocation identities;
- Multiple Bots typed durable IDs;
- Connections registry identity;
- Gateway session/run local identities and external owner bindings;
- Dashboard `systemId` as Dashboard-local connection identity only;
- Token runtime/provider/model identity-resolution model;
- repository-governance repository IDs within repository governance only.

#### `EXTEND`

- existing OS `{owner, scope, kind, id}` canonical-reference precedent into one minimal System-wide cross-owner reference contract in Slice 1.2;
- Distribution preservation tests later to prove durable IDs/references survive Core update without creating a second updater.

#### `CREATE`

- Apps durable App identity implementation. Apps architecture intends stable identity, but executable registry/manifest/identity lifecycle is still absent.

#### `BLOCK/UNKNOWN`

- arbitrary Workspace relocation / path-independent ID-to-location lookup: unsupported by current owners;
- identity-preserving cross-provider Skill/capability re-scope: not admitted by current qualified-ID contract.

These are unsupported capabilities, not blockers to Slice 1.2. The shared contract must preserve the fail-closed result rather than inventing semantics.

#### `RETIRE`

- none. No competing global identity service, duplicate runtime identity registry or unsafe owner identity mechanism was found that should be retired.

### Frozen conclusions confirmed

- Workspace logical identity is `WORKSPACE.yaml:id`: **CONFIRMED**;
- current Workspace storage is `workspaces/<workspace-id>`: **CONFIRMED**;
- filesystem independence is not universal: **CONFIRMED**;
- Workspace relocation is unsupported without a future explicit ID-to-location owner contract: **CONFIRMED**;
- OS owns provider/scope resolution for Skills/capabilities: **CONFIRMED**;
- Skills owns managed `aiverse-skills` provider lifecycle: **CONFIRMED**;
- personal reusable Skills/capabilities are user-owned: **CONFIRMED**;
- Workspace-local Skills/capabilities are Workspace-owned: **CONFIRMED**;
- provider/scope is part of current qualified Skill identity: **CONFIRMED**;
- managed Skill package identity is separate from generation/version/digest: **CONFIRMED**;
- scope transfer does not automatically preserve identity: **CONFIRMED**;
- Brain, Memory, Data, Automations, Multiple Bots, Connections, Gateway, Dashboard-local and Token identity implementations should be reused: **CONFIRMED**;
- Apps remains the known incomplete stable-identity area: **CONFIRMED**.

### Duplicate/competing mechanism result

No global runtime identity authority exists today, and none is required by current evidence.

- Dashboard `systemId` remains Dashboard-local and owns zero domain truth.
- Gateway session/run IDs remain Gateway-local.
- System repository IDs remain repository-governance identities.
- Data request/event/transaction/receipt IDs remain separate from Data record identity.
- Skills generation/version/digest remain separate from package identity.
- Token model/provider identities remain domain-specific.

A canonical installation-wide AI-Verse instance ID remains out of scope unless later evidence proves a real requirement.

### Concurrent work/drift

System repository-network-governance work advanced concurrently after the Slice 1.1 start record. The Identity plan was refetched before writes; inspected concurrent commits did not alter this Identity plan or the owner identity contracts used for the map. No concurrent plan content was overwritten.

### Acceptance criteria

- every durable first-class entity requiring stable identity is accounted for: **PASS**;
- every canonical owner is identified: **PASS**;
- duplicate or competing identity mechanisms are identified: **PASS**;
- path/name-based cross-owner coupling is recorded only where current evidence proves it: **PASS**;
- no new subsystem is proposed where `REUSE` or `EXTEND` is sufficient: **PASS**;
- the starting classification is confirmed or corrected with exact evidence: **PASS**;
- no product/component implementation was changed during Slice 1.1: **PASS**.

### Completion report

```text
Completed: Slice 1.1 - Refresh the cross-Core identity map
Tasks: 6/6
Overall: 2/8 slices (25.0%)
Phase: Phase 1 - Freeze the shared identity contract from current reality
Phase progress: 1/2
Until next phase: 1 slice
Next: Slice 1.2 - Define the System identity and canonical-reference contract
Blockers/drift/amendments: No protected directional change required. Workspace relocation and identity-preserving cross-provider re-scope remain intentionally unsupported/fail-closed. Concurrent System governance work did not overlap Identity surfaces.
```

### NEXT

**STOP after Slice 1.1 for the current one-at-a-time execution request.**

Next execution unit: **Slice 1.2 - Define the System identity and canonical-reference contract.**

---

## Slice 1.2 - Define the System identity and canonical-reference contract

**Status:** COMPLETE  
**Repos:** AI-Verse-System  
**Dependencies:** 1.1  
**Adaptive tasks:** 5/5 COMPLETE  
**Starting ref:** `aiverse-filmmakers/AI-Verse-System@a04c58f1e41f0097dccf24353d675af993a06df4`

### Final derived task list

- [x] **1.2-T1** Refresh the current System head and verify Slice 1.1 conclusions and the Identity plan remain authoritative despite concurrent System governance work.
- [x] **1.2-T2** Define one concise normative System identity contract preserving owner authority, owner-specific ID formats, current Workspace storage semantics and current qualified Skill/provider semantics.
- [x] **1.2-T3** Add the minimal versioned JSON Schema for the common durable-reference envelope: required `owner`, `kind`, `id`; optional `scope`; no owner-state registry or lookup database.
- [x] **1.2-T4** Add contract examples and focused validation tests covering Workspace, Skill/capability, Brain object, Automation, Bot, Connection, Data record and Memory record references, including invalid ambiguity/extra-shape cases.
- [x] **1.2-T5** Record exact implementation/test evidence, close acceptance criteria and stop before Slice 2.1.

### Canonical contract

The shared identity law is now defined by:

- `docs/DURABLE-IDENTITY-AND-CANONICAL-REFERENCE-CONTRACT.md`
- contract ID: `ai-verse.durable-identity-reference/v1`
- implementation commit: `aiverse-filmmakers/AI-Verse-System@32235170a99296104c0f90eef56691cbc4d781bd`

The contract standardizes composition law only. Canonical owners retain their own ID formats, generation, validation, lookup, migration, collision handling and lifecycle semantics.

It explicitly establishes:

- stable owner-controlled IDs for durable first-class entities requiring long-lived/cross-owner references;
- identity separate from display name, label, path, revision/version and temporary execution/correlation IDs;
- no global ID service, UUID allocator, entity database or owner-object registry;
- owner-defined filesystem independence and owner-defined scope-transfer semantics;
- fail-closed behavior on ambiguous, malformed, duplicate or conflicting identity evidence;
- current Workspace identity/storage law: `WORKSPACE.yaml:id` at `workspaces/<workspace-id>` with arbitrary relocation unsupported;
- current capability provider semantics retained, including provider/scope as part of qualified capability identity;
- managed package identity, qualified identity, generation, version and digest as distinct concepts;
- update/upgrade/recovery/restore may rely only on identity guarantees explicitly published by the canonical owner.

### Machine-readable reference envelope

Normative schema:

- `contracts/durable-entity-reference-v1.schema.json`
- schema commit: `aiverse-filmmakers/AI-Verse-System@2d4db6140628d931aab886fb85f8e6bbfdd4015f`

The v1 envelope is intentionally minimal:

```json
{
  "owner": "ai-verse-brain",
  "kind": "brain-object",
  "id": "5b3bb42e-b423-4f68-8349-d8db64800f55"
}
```

`scope` is optional and is present only when required by the canonical owner for correct resolution.

The schema rejects extra representation/lifecycle fields. It intentionally does not impose owner-specific ID patterns beyond a non-empty bounded string.

### Validator, examples and tests

Added:

- `scripts/validate_durable_entity_reference.py` at commit `8db084762e943393f215a4abef9709025ecb1272`;
- `contracts/examples/durable-entity-references.valid.json` at commit `d9799704b6d3e63e23217aa21e1866a93e9e72d2`;
- `tests/test_durable_entity_reference.py`, final tested revision at `ee4f494692c9cc36c024dacb390a1841362d1ca6`.

Examples cover:

1. Workspace;
2. Skill/capability;
3. Brain object;
4. Automation;
5. Bot;
6. Connection;
7. Data record;
8. Memory record.

Focused tests prove:

- only `owner`, `kind`, `id`, optional `scope` belong in the common envelope;
- `scope` is syntactically optional;
- owner-specific ID/scope syntax remains opaque to System;
- missing or empty required identity fails closed;
- display name, filesystem path, generic version and other extra state are rejected from the shared reference envelope;
- an attempted ambiguous-candidate shape is not a valid canonical reference;
- the normative contract requires one unambiguous canonical result and fail-closed ambiguity handling;
- Workspace and Skill constraints remain frozen;
- no global identity registry/allocator is introduced.

### Validation evidence

The first exact-ref Contract Validation run on `52f04a04a50ebfbf238a6499c29b9a2be5910fc6` was **FAILURE** because one test asserted wording that did not exactly match the contract text. No contract law failed. The assertion was corrected without weakening behavior in commit `ee4f494692c9cc36c024dacb390a1841362d1ca6`.

Final exact-ref evidence:

- GitHub Actions workflow: `Contract Validation`;
- run ID: `38267780226`;
- exact head SHA: `ee4f494692c9cc36c024dacb390a1841362d1ca6`;
- event: push to `main`;
- conclusion: **SUCCESS**;
- Python 3.11 contract tests: **SUCCESS**;
- Python 3.13 contract tests: **SUCCESS**;
- Python 3.11 live read-only Core repository refresh: **SUCCESS**.

The existing `.github/workflows/contract-validation.yml` required no modification because it already executes `python -m unittest discover -s tests -p "test_*.py"` on Python 3.11 and 3.13.

### Anti-bloat result

Slice 1.2 created no runtime identity service, no central lookup registry, no universal UUID layer, no Workspace relocation engine and no generic re-scope framework.

No owner repo was modified. Existing owner identity implementations remain canonical.

### Acceptance criteria

- concise normative identity contract exists: **PASS**;
- identity is distinguished from display name, storage path, revision and temporary execution IDs: **PASS**;
- owner authority and lookup responsibility are explicit: **PASS**;
- common reference shape is versioned and minimal: **PASS**;
- `scope` is optional unless required by the owner: **PASS**;
- ambiguity and duplicate/conflicting identity fail closed: **PASS**;
- owner-specific ID formats remain permitted: **PASS**;
- Workspace path semantics and scope-transfer semantics remain owner-defined: **PASS**;
- no central identity registry or service was introduced: **PASS**;
- required examples and validation tests exist and pass exact-ref CI: **PASS**.

### Completion report

```text
Completed: Slice 1.2 - Define the System identity and canonical-reference contract
Tasks: 5/5
Overall: 3/8 slices (37.5%)
Phase: Phase 1 - Freeze the shared identity contract from current reality
Phase progress: 2/2
Until next phase: 0 slices
Next program-local slice: Identity Slice 2.1 - Align owner integrations to the shared contract with minimum change
Cross-program next execution unit: reconcile Identity Phase 1 against Safe Infrastructure, then resume Safe Infrastructure Phase 2 / Slice 2.1
Blockers/drift/amendments: none. No protected directional change was required. Initial CI wording-assertion failure was corrected and final exact-ref Contract Validation passed.
```

### NEXT

**STOP after Slice 1.2 for the current one-at-a-time execution request.**

Program-local next slice remains **Identity Slice 2.1**. Under the owner's cross-program sequencing instruction, the next execution unit is the reconciliation checkpoint against Safe Infrastructure before any further Identity implementation.

---

# Phase 2 - Fix verified gaps only

## Slice 2.1 - Align owner integrations to the shared contract with minimum change

**Status:** NOT STARTED  
**Repos:** only owners with verified drift from Slice 1.1  
**Dependencies:** 1.2

### Outcome

Cross-owner identity usage follows the shared contract wherever durable references cross an ownership boundary, while mature internal owner identity implementations remain untouched.

### Acceptance criteria

- every verified cross-owner durable reference resolves through canonical owner identity rather than display name or accidental representation;
- current Workspace canonical storage semantics remain compatible across OS, Brain, Memory and Data;
- no owner is forced to adopt another owner's ID format;
- no duplicate source of truth is created;
- path references that are merely internal storage implementation remain internal and are not replaced without need;
- all changed integrations fail safely on missing, duplicate or conflicting identity evidence.

### Required evidence

- exact changed call sites/contracts;
- focused tests for each changed integration;
- explicit list of audited owners requiring no change.

### NEXT

**Slice 2.2 - Complete stable App identity.**

## Slice 2.2 - Complete stable App identity

**Status:** NOT STARTED  
**Repos:** AI-Verse-Apps, AI-Verse-System only where contract/spec evidence must be updated  
**Dependencies:** 1.2

### Outcome

Apps has a real owner-controlled durable App identity implementation consistent with its existing architecture and the shared System contract.

### Acceptance criteria

- App identity is separate from display name and mutable metadata;
- duplicate App identity fails safely;
- App lookup/reference does not depend on UI label;
- rename does not silently create a new App identity;
- persistence/restart preserves App identity;
- implementation reuses existing Apps architecture rather than introducing a separate generic registry;
- appropriate tests prove the identity lifecycle.

### Required evidence

- implementation and focused tests in AI-Verse-Apps;
- System component spec/QC evidence updated only if required;
- no unrelated Apps expansion bundled into this slice.

### NEXT

**Slice 3.1 - Add lightweight identity conformance tests.**

---

# Phase 3 - Prove identity stability

## Slice 3.1 - Add lightweight identity conformance tests

**Status:** NOT STARTED  
**Repos:** AI-Verse-System plus only applicable owner repos  
**Dependencies:** 2.1, 2.2

### Outcome

A small reusable acceptance model proves the properties that should be common across durable identities without forcing identical implementations.

### Acceptance criteria

Applicable owners prove only the relevant shared properties:

- display-name change does not change durable identity;
- restart/reload does not change durable identity;
- duplicate identity is rejected or deterministically resolved according to the owner contract;
- malformed or ambiguous identity fails safely;
- canonical cross-owner reference resolves to the same durable entity;
- unsupported scope/path mutation does not silently rebind identity.

Owners are not required to support rename, re-scope or relocation operations they do not canonically provide.

### Required evidence

- shared conformance guidance or helper only if it removes duplication;
- focused owner tests;
- no test-only abstraction larger than the behavior it is proving.

### NEXT

**Slice 3.2 - Prove identity preservation across Core updates.**

## Slice 3.2 - Prove identity preservation across Core updates

**Status:** NOT STARTED  
**Repos:** ai-verse-distribution plus affected owner fixtures/tests only as needed  
**Dependencies:** 3.1

### Outcome

The existing Core update preservation program explicitly proves that durable user-owned identities and durable cross-owner references survive an admitted Core update.

### Acceptance criteria

- populated pre-update fixtures contain representative durable identities;
- before/after checks prove IDs are preserved;
- durable cross-owner references still resolve after update;
- update verification fails if identity is silently reminted, rebound or lost;
- the existing preservation framework is extended rather than replaced;
- no second update or migration system is introduced.

### Required evidence

- Distribution preservation tests;
- exact admitted transition evidence used by the test;
- before/after identity proof.

### NEXT

**Slice 4.1 - Cross-Core acceptance and closeout.**

---

# Phase 4 - Cross-Core acceptance and closeout

## Slice 4.1 - End-to-end identity acceptance

**Status:** NOT STARTED  
**Repos:** AI-Verse-System plus relevant Core repos  
**Dependencies:** 3.2

### Outcome

The identity model is proven coherent across owners and no unnecessary identity infrastructure remains.

### Acceptance criteria

- System contract validation passes;
- all affected owner tests pass;
- cross-owner reference examples resolve correctly;
- Workspace continues to work under the existing `workspaces/<id>` canonical storage rule;
- Apps stable identity is implemented and tested;
- Core update preservation includes identity continuity;
- no global identity registry, UUID service or duplicate owner state was introduced;
- final identity matrix contains no unresolved `CREATE`, `EXTEND`, `RETIRE` or `BLOCK/UNKNOWN` item required for this program;
- any intentionally deferred idea is explicitly marked out of scope rather than partially implemented.

### Required evidence

- exact final repository refs;
- test/workflow evidence;
- final identity matrix;
- concise anti-bloat review confirming what was deliberately not built.

### NEXT

**Program complete.**

---

# Change-authority boundary

Adaptive task discovery may add, remove, split, merge or reorder low-level tasks inside a slice when current evidence requires it.

It may not silently:

- change any permanent law in section 0A;
- introduce a central/global identity owner;
- change Workspace canonical storage away from `workspaces/<id>`;
- declare scope transfer identity-preserving for all owners;
- weaken fail-closed identity behavior;
- remove an acceptance criterion;
- expand the program into a general refactor of Core repos.

Any such change requires the plan-amendment protocol from `docs/ADAPTIVE-IMPLEMENTATION-PLANNING-SKILL.md`.

# Completion report format

After every completed slice report:

```text
Completed: Slice X.Y - <title>
Tasks: <completed>/<derived total>
Overall: <completed>/8 slices (<percent>%)
Phase: <phase number> - <title>
Phase progress: <completed>/<total>
Until next phase: <N> slice(s)
Next: <next slice/task>
Blockers/drift/amendments: <none or concise status>
```

# Planning principle

**Standardize the law, not every implementation.**

Reuse strong owner identity systems, add only the minimum shared contract needed for safe composition, and prove continuity instead of building identity infrastructure for its own sake.
