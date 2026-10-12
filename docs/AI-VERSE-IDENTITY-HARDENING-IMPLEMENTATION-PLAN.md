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

The pre-plan audit found the following starting classification. Slice 1.1 must refresh this against current repository heads before implementation begins.

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
**Completed slices:** 1  
**Overall:** 1/8 (12.5%)  
**Current phase:** Phase 1  
**Next:** Slice 1.1 - IN PROGRESS

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

**Status:** IN PROGRESS  
**Repos:** AI-Verse-System plus identity-relevant Core owner repos  
**Dependencies:** 0.1

### Starting refs

Refs refreshed before Identity Slice 1.1 implementation/audit work:

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

OS, Brain, Memory, Data, Skills and Distribution still match the exact refs used by Safe Infrastructure Phase 1, so its completed identity findings are reused rather than re-audited.

### Derived task list

- [x] **1.1-T1** Refresh all in-scope repository heads and verify which Safe Infrastructure Phase 1 evidence remains exact-current.
- [ ] **1.1-T2** Reuse Safe Infrastructure Slice 1.2/1.3 evidence to confirm Workspace, Skill/provider and Distribution identity conclusions without duplicating those audits.
- [ ] **1.1-T3** Inspect only identity-relevant surfaces in Automations, Multiple Bots, Connections, Apps, Gateway, Dashboard and Token that Safe Infrastructure did not cover.
- [ ] **1.1-T4** Refresh current System identity/spec/reference surfaces and identify any duplicate or competing identity mechanisms.
- [ ] **1.1-T5** Produce the final cross-Core identity matrix with canonical owner and `REUSE` / `EXTEND` / `CREATE` / `RETIRE` / `BLOCK/UNKNOWN` classification for every relevant durable identity surface.
- [ ] **1.1-T6** Record exact evidence, acceptance closure, remaining gaps and the minimal handoff to Slice 1.2. No component implementation changes are permitted in this slice.

### Outcome

A current evidence-backed map identifies every durable first-class entity that participates in long-lived or cross-owner identity and classifies each implementation as `REUSE`, `EXTEND`, `CREATE`, `RETIRE` or `BLOCK/UNKNOWN`.

### Scope

Inspect only identity-relevant surfaces in:

- AI-Verse-OS;
- AI-Verse-Brain;
- AI-Verse-Memory;
- AI-Verse-Data;
- AI-Verse-Skills;
- AI-Verse-Automations;
- AI-Verse-Multiple-Bots;
- AI-Verse-Connections;
- AI-Verse-Apps;
- AI-Verse-Gateway;
- AI-Verse-Dashboard;
- ai-verse-token;
- ai-verse-distribution;
- AI-Verse-System contracts/specs.

Do not perform a general-purpose repo audit outside identity-relevant code, contracts and tests.

### Acceptance criteria

- every durable first-class entity requiring stable identity is accounted for;
- every canonical owner is identified;
- duplicate or competing identity mechanisms are identified;
- path/name-based cross-owner references are identified only where they create real identity coupling;
- no new subsystem is proposed where `REUSE` or `EXTEND` is sufficient;
- the starting classification in section 0C is either confirmed or corrected with evidence.

### Required evidence

- exact repository refs inspected;
- concise identity matrix in this plan or a directly linked System document;
- exact source/test evidence for every `EXTEND`, `CREATE`, `RETIRE` or `BLOCK/UNKNOWN` classification.

### Adaptive task rule

At slice start, derive the smallest task list needed to satisfy this acceptance gate. The first task should refresh current heads and relevant identity surfaces.

### NEXT

**Slice 1.2 - Define the System identity and canonical-reference contract.**

## Slice 1.2 - Define the System identity and canonical-reference contract

**Status:** NOT STARTED  
**Repos:** AI-Verse-System  
**Dependencies:** 1.1

### Outcome

AI-Verse-System canonically defines the minimum identity law and one common cross-owner durable-reference shape without taking ownership of component identities.

### Acceptance criteria

- a concise normative identity contract exists;
- the contract distinguishes entity identity from display name, storage path, revision and temporary execution IDs;
- owner authority and lookup responsibility are explicit;
- the common reference shape is versioned and minimal;
- `scope` is optional unless required by the owner to resolve identity correctly;
- ambiguity and duplicate identity fail closed;
- the contract explicitly permits owner-specific ID formats;
- Workspace path semantics and scope-transfer semantics remain owner-defined;
- no central identity registry or service is introduced.

### Required evidence

- System contract/schema/document changes;
- contract validation tests;
- examples covering at least Workspace, Skill, Brain object, Automation, Bot, Connection, Data record and Memory record references.

### NEXT

**Slice 2.1 - Align owner integrations to the shared contract with minimum change.**

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
