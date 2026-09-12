# AI-Verse Component Audit Methodology

## Purpose

This document defines the mandatory forensic review method for every component documented in AI-Verse-System.

It exists so that component quality does not depend on one chat, one model, one memory state, or one reviewer remembering how a previous audit was performed.

The method was formalized after the fresh standalone re-audit of AI-Verse OS on 2026-09-13.

The goal is not merely to summarize a repository.

The goal is to reconstruct, with evidence:

1. what the component is;
2. what it owns;
3. what it must never own;
4. what is actually implemented;
5. what is only described or intended;
6. what is enforced in tests/runtime rather than just stated in prose;
7. what historical defects changed the architecture;
8. what is missing for the current milestone;
9. what is missing for the final seamless system;
10. which permanent laws the rest of AI-Verse should inherit.

---

# 1. Independence rule

Each component must first be audited from its **own repository alone**.

Do not use the existing AI-Verse-System component document as evidence.

Do not use another component repository to fill gaps during the first-pass reconstruction.

Do not assume a previous chat summary is correct.

Cross-component facts may be recorded during this first pass only when the component repository itself contains evidence for them, such as:

- integration contracts;
- pinned cross-repo CI;
- host adapters;
- compatibility documents;
- release matrices;
- historical audit records.

After the standalone component baseline is complete, later cross-component synthesis may refine it.

This prevents circular documentation where one summary merely repeats another.

---

# 2. Fresh-state rule

Before writing or revising a component specification:

1. identify the current default branch;
2. identify the exact reviewed head revision;
3. inventory the repository tree;
4. identify generated/duplicated/vendor/build material;
5. separate canonical source files from generated peers;
6. note the review date.

Every component spec, source map and QC document must record the exact revision reviewed.

A component audit is a point-in-time evidence statement.

---

# 3. Canonical-vs-generated inventory

Do not count every tracked file as an independent architectural source.

The reviewer must classify repository material into at least:

- canonical implementation;
- canonical architecture/contracts;
- generated runtime peers;
- build output;
- media/demo assets;
- vendor/third-party code;
- user-state templates;
- historical/status documentation;
- tests;
- CI;
- compatibility shims;
- legacy surfaces.

This prevents duplicated generated code from inflating perceived feature breadth or causing the same logic to be audited multiple times as if independently implemented.

Where a generator exists, determine:

- which source is canonical;
- who owns generated targets;
- how drift is detected;
- whether local edits are preserved;
- whether regeneration is safe.

---

# 4. Evidence hierarchy

The audit should not treat every source as equally authoritative.

Use this working hierarchy:

1. current executable implementation;
2. current acceptance tests and CI behavior;
3. current machine-readable contracts/schemas;
4. current architecture docs;
5. current README/member docs;
6. current release/status docs;
7. historical audits/PR descriptions;
8. older compatibility docs;
9. inferred intent.

When sources disagree, record the contradiction instead of silently choosing whichever is more convenient.

Historical documents are evidence of previous state and design intent, not automatic evidence of current implementation.

---

# 5. Current / Intended / Gap / Law / Historical / Inspiration classification

Important statements should be classified mentally, and explicitly in the documentation where ambiguity is possible.

### CURRENT

Implemented and supported now.

### INTENDED

Desired future behavior or accepted requirement.

### GAP

Required behavior that is absent, partial or unverified.

### LAW

A permanent architecture/safety invariant.

### HISTORICAL

A previous implementation, defect, workaround or milestone retained for provenance.

### INSPIRATION

An evidenced external idea, framework or system that materially influenced the design.

Never rewrite INTENDED as CURRENT.

Never call HISTORICAL behavior current simply because an old status document describes it.

---

# 6. Implementation-vs-prose enforcement rule

For every important architecture claim, ask:

> Is this merely written down, or is it deterministically enforced?

Look for:

- validators;
- schemas;
- permission checks;
- path containment;
- locks;
- idempotency;
- immutable identities;
- runtime dispatch checks;
- tests;
- CI;
- failure codes;
- acceptance workflows.

Classify the claim as:

- prose-only;
- partially enforced;
- fully enforced;
- externally enforced by another component;
- unverified.

This lens is mandatory because many AI systems have excellent architecture documents with weak runtime enforcement.

---

# 7. Required audit sequence

The following sequence should be used unless a component clearly makes one step irrelevant.

## Phase A - Repository reconstruction

### A1. Repository inventory

Capture:

- file count/rough size where practical;
- top-level structure;
- primary languages;
- generated/vendor/build regions;
- canonical roots.

### A2. Root identity files

Read:

- README;
- package/pyproject/build metadata;
- top-level agent/runtime instructions;
- manifest/config files;
- license/notices;
- contributor/authoring docs where relevant.

### A3. Architecture and product contracts

Read:

- architecture docs;
- schemas;
- ownership docs;
- source-of-truth docs;
- routing;
- lifecycle;
- security;
- integration contracts;
- PRDs;
- build maps.

### A4. User-facing lifecycle

Inspect real surfaces for:

- install;
- attach/register;
- enable;
- activate/adopt;
- initialize;
- migrate/import;
- doctor/status;
- update;
- disable;
- detach;
- uninstall;
- reinstall;
- reconcile;
- rollback.

Do not assume a command exists because the architecture expects it.

### A5. Runtime/host boundaries

Inspect:

- adapters;
- host protocols;
- APIs;
- CLIs;
- extension registries;
- RPC/JSON subprocess/MCP interfaces;
- plugin boundaries.

### A6. Tests and CI

Read the tests that encode architecture boundaries.

Tests often reveal stronger truth than READMEs.

### A7. Historical evolution

Review:

- meaningful PR sequence;
- recent commits;
- repair/audit handoffs;
- release-hardening changes;
- migrations;
- regressions.

### A8. Inspiration/provenance

Search:

- third-party notices;
- framework credits;
- research references;
- explicit comparison docs;
- dependency provenance.

Do not invent inspirations not evidenced by repository history or separately documented research.

---

# 8. Mandatory audit lenses

Every component should be inspected through the following lenses.

Not every lens will produce a finding, but every lens should be considered.

## Lens 1 - Product identity

- What problem does the component solve?
- What should a user believe it is?
- Is the name/product framing accurate relative to implementation?

## Lens 2 - Architecture

- What are the component's major layers?
- Is the internal architecture coherent?
- Are responsibilities separated cleanly?

## Lens 3 - Ownership

- What canonical state does it own?
- What must it never own?
- Are any responsibilities duplicated with another subsystem?

## Lens 4 - Source of truth

- Which file/store/API is authoritative for each responsibility?
- Are editable duplicates possible?
- Are derived views clearly non-canonical?

## Lens 5 - Provenance

- Does historical/source provenance survive transformations?
- Can old evidence remain available without retaining current authority?

## Lens 6 - Scope model

- operator/global/workspace/project/task scopes;
- how scope IDs are validated;
- whether scope can be forged or confused.

## Lens 7 - Isolation

- cross-workspace/cross-user/cross-project leakage;
- filesystem boundaries;
- query boundaries;
- provider boundaries.

## Lens 8 - Privacy/local-first behavior

- what is tracked;
- what is ignored;
- what leaves the machine;
- secret handling;
- telemetry defaults.

## Lens 9 - Installation

- is there a real supported install path?
- what prerequisites exist?
- does it modify sibling-owned files?
- can it install independently?

## Lens 10 - Attachment / registration

- is package availability separate from host attachment?
- is attachment idempotent?
- where is attachment state stored?

## Lens 11 - Activation / adoption

- can an already-running host or agent begin using it later?
- does activation accidentally transfer authority?
- is adoption explicit?

## Lens 12 - Initialization

- what scope/state is created?
- can initialization be repeated safely?
- does it invent state?

## Lens 13 - Migration / legacy integration

- old standalone state;
- previous architecture versions;
- history import;
- duplicate truth prevention;
- resumability;
- verification before retirement.

## Lens 14 - Update / upgrade

- update mechanism;
- version compatibility;
- schema migration;
- moving branch vs immutable release;
- rollback.

## Lens 15 - Disable / detach / uninstall / reinstall

- does user-owned canonical data survive?
- can the component be reattached later?
- are ownership transfers safe?

## Lens 16 - Install-order independence

Test the conceptual orders:

- host first;
- component first;
- sibling first;
- component added much later;
- reinstall after detach.

Chronology must not determine authority.

## Lens 17 - Discovery

- how does the host find the component/capability?
- is discovery hardcoded or self-describing?
- can stale/unsafe providers be excluded?

## Lens 18 - Readiness

Explicitly separate:

- discovered;
- installed;
- attached;
- enabled;
- healthy;
- ready;
- permitted;
- approved.

Look for false equivalence.

## Lens 19 - Health / doctor / observability

- what does doctor actually prove?
- core health vs integration health;
- component-specific health;
- logs/status/diagnostics;
- actionable errors.

## Lens 20 - Permissions / approvals

- outer permission floor;
- scope policy;
- high-stakes behavior;
- restrictive intersection;
- late re-check before effect.

## Lens 21 - Security / path safety

- symlink escape;
- traversal;
- untrusted input;
- bounded payloads;
- arbitrary code/path execution;
- unsafe deserialization;
- registry corruption.

## Lens 22 - Idempotency / replay safety

- duplicate requests;
- retry behavior;
- durable vs disposable idempotency;
- exactly-once claims;
- effect receipts.

## Lens 23 - Concurrency / locking

- shared registries;
- state races;
- concurrent handovers;
- update-during-execution;
- lock recovery.

## Lens 24 - Failure behavior

For every major path:

- fail open or closed?
- what survives partial failure?
- does it silently widen authority?
- can recovery overwrite newer state?

## Lens 25 - Capability taxonomy

When relevant:

- skill;
- script;
- agent;
- automation;
- app;
- template;
- data source.

Check that machinery is not misclassified or unnecessarily duplicated.

## Lens 26 - Runtime/agent portability

- AI-Verse-specific dependencies;
- generic contracts;
- Claude/Codex/Hermes/other-host compatibility;
- portability without weakening canonical behavior.

## Lens 27 - Integration boundaries

- does the component call the owning component's API/host boundary?
- does it reach directly into sibling databases/files?
- are boundaries versioned?

## Lens 28 - Cross-component writes

- how does another component request durable changes?
- who performs the final write?
- are ownership/permission/idempotency rechecked at the actual effect boundary?

## Lens 29 - Read path / retrieval

- how does another component consume state?
- are projections bounded?
- can raw internal stores be bypassed?

## Lens 30 - Data model / schema evolution

- stable IDs;
- migrations;
- backward compatibility;
- unknown fields;
- schema versioning;
- canonical serialization.

## Lens 31 - Performance / scalability

- bounded scans;
- pagination;
- indexing;
- large installations;
- concurrency;
- generated-state cost;
- obvious O(n) assumptions that will fail at scale.

## Lens 32 - Product/UX

- can a non-author understand setup?
- can the agent explain what is happening?
- are commands simple?
- does the user need repository-internal knowledge?

## Lens 33 - Automation / Cadence

- definition vs actual execution;
- scheduler owner;
- triggers;
- retries;
- dedupe;
- monitoring;
- kill switch.

## Lens 34 - Agent/orchestration behavior

- agent definition vs runtime;
- giant prompt duplication;
- canonical knowledge ownership;
- coordination contracts.

## Lens 35 - Apps/UI projections

- does UI own hidden truth?
- can it be deleted/rebuilt?
- are displayed states authoritative or derived?

## Lens 36 - Release / distribution

- package publication;
- license;
- immutable tags/releases;
- member access;
- tested install path;
- release channels.

## Lens 37 - Cross-platform behavior

- Linux;
- macOS;
- Windows;
- shell assumptions;
- path conventions;
- runtime versions.

## Lens 38 - Documentation consistency

Compare:

- README;
- architecture;
- code;
- tests;
- CI;
- status docs;
- install docs;
- examples.

Record stale docs as defects rather than silently correcting them in the system summary.

## Lens 39 - Historical-learning

For each meaningful defect:

1. what failed?
2. why?
3. how was it repaired?
4. what permanent invariant was learned?
5. does the invariant apply elsewhere?

## Lens 40 - Inspiration / curation

- explicit external inspirations;
- adopted ideas;
- rejected ideas;
- improvements over source systems;
- legal/provenance obligations.

## Lens 41 - Negative-space analysis

Ask explicitly:

> What would I expect this component to have, based on its product claim, that is not actually present?

Examples:

- scheduler architecture but no scheduler;
- write boundary but no effect handler;
- component registry but hardcoded component list;
- capability discovery but no readiness;
- doctor but no deep operational health;
- agent registry but no agent runtime.

This lens is mandatory.

## Lens 42 - Architecture-vs-operation analysis

For every major subsystem classify it as:

- architecture only;
- contract only;
- implementation present;
- acceptance proven;
- production/member-path proven.

This prevents "folder exists" from becoming "feature works."

## Lens 43 - Current-target readiness

Identify the component's **current intended milestone**, not only its final vision.

Then audit whether that milestone is actually complete.

Separate:

- engine/core;
- integration;
- lifecycle;
- migration;
- command/UX;
- acceptance;
- release/distribution.

## Lens 44 - Final seamless-system gap

Ask:

> What remains between today's component and "works perfectly together like a glove"?

Produce exact blockers, not vague aspirations.

## Lens 45 - Scope-creep check

For every proposed fix:

- should this component own it?
- should a sibling own it?
- should it be a shared protocol?
- is it merely UI convenience?
- would implementing it here duplicate responsibility?

## Lens 46 - Definition-of-done

Write a concrete component-specific definition of done.

It must be testable.

---

# 9. Contradiction scan

After the main review, perform a dedicated contradiction pass.

At minimum compare:

- README vs implementation;
- architecture docs vs code;
- current code vs old release docs;
- status docs vs CI;
- CLI docs vs actual parser;
- schemas vs validators;
- "supported" vs actual supported path;
- "ready" vs doctor depth;
- "integrated" vs direct-storage shortcuts;
- "automatic" vs plan-only/manual steps.

Each contradiction should be classified as:

- stale documentation;
- implementation defect;
- intentional backward compatibility;
- unresolved architecture ambiguity;
- historical-only wording.

---

# 10. Negative claims require evidence too

Do not write "X does not exist" merely because it was not noticed.

Before declaring a meaningful absence, search for:

- command names;
- likely filenames;
- operation symbols;
- tests;
- CI steps;
- PRs;
- historical references.

Then phrase appropriately:

- "No generic implementation was found in the reviewed repository";
- "The current implementation explicitly stops at...";
- "The repository describes this as later work."

This reduces false negatives.

---

# 11. Tests are architecture evidence

Tests and CI must be read as architectural documents.

Look for:

- what is explicitly asserted;
- which failure modes have regressions;
- what is only mocked;
- what uses real sibling repositories;
- what patches hidden prerequisites;
- whether acceptance tests use actual member paths;
- what platforms/runtime versions are exercised;
- whether current or pinned old revisions are used.

A feature with only unit tests is not equivalent to real integration acceptance.

A CI workflow that prepares hidden state differently from users must not be treated as proof of the user path.

---

# 12. Historical archaeology

Do not only inspect the latest code.

Review enough PR/commit history to reconstruct architectural evolution.

Prioritize commits/PRs containing themes such as:

- architecture;
- repair;
- audit;
- security;
- migration;
- lifecycle;
- provider;
- ownership;
- isolation;
- release;
- hardening;
- acceptance;
- compatibility;
- handoff;
- update;
- reinstall;
- detach.

The goal is to learn **why** current invariants exist.

---

# 13. Repair-to-law promotion

A meaningful historical fix should become a permanent system lesson where applicable.

Example transformation:

```text
Defect:
workspace skill symlink could escape scope

Repair:
physical containment validation

Permanent law:
scope isolation must be physical and logical
```

The audit must check whether repaired anti-patterns appear elsewhere in the component or ecosystem.

---

# 14. Lifecycle matrix requirement

Every component spec must include, where applicable, a matrix covering:

| Stage | Exists? | Command/API | Idempotent? | State owner | Acceptance evidence | Gap |
|---|---|---|---|---|---|---|
| install | | | | | | |
| attach/register | | | | | | |
| enable | | | | | | |
| activate/adopt | | | | | | |
| initialize | | | | | | |
| migrate/import | | | | | | |
| doctor/status | | | | | | |
| update | | | | | | |
| disable | | | | | | |
| detach | | | | | | |
| uninstall | | | | | | |
| reinstall | | | | | | |
| reconcile | | | | | | |
| rollback | | | | | | |

Use "not applicable" only when the component genuinely does not have that lifecycle stage.

---

# 15. Completeness matrix requirement

Never collapse completion into one vague percentage.

Every component should be classified across:

- ENGINE / CORE
- ARCHITECTURE / CONTRACT
- INSTALL / PACKAGE
- HOST INTEGRATION
- ATTACH / REGISTER
- ACTIVATE / ADOPT
- SCOPE INITIALIZATION
- MIGRATION / LEGACY
- HEALTH / DOCTOR
- PERMISSION / SAFETY
- CROSS-COMPONENT READ
- CROSS-COMPONENT WRITE
- UPDATE / UPGRADE
- DISABLE / DETACH / UNINSTALL
- REINSTALL / RECONCILE
- CROSS-PLATFORM
- ACCEPTANCE
- RELEASE / DISTRIBUTION
- DOCUMENTATION CONSISTENCY

Preferred status vocabulary:

- COMPLETE
- COMPLETE WITH LIMITATIONS
- PARTIAL
- PLAN-ONLY
- ARCHITECTURE ONLY
- EXTERNALLY BLOCKED
- MISSING
- NOT APPLICABLE
- UNVERIFIED

---

# 16. Current-target vs final-target rule

Two definitions of done must be maintained.

## Current target

What must be true for the component's present milestone or beta.

## Final target

What must be true for seamless AI-Verse operation.

A component may be current-target complete while still having final-state gaps.

Conversely, a strong engine is not current-target complete if its present milestone requires install/activation/migration paths that do not exist.

---

# 17. Product-path acceptance rule

When a component claims a user-facing capability, verify the exact supported path.

Examples:

- the documented install command;
- the actual attach command;
- the real agent/host config;
- the actual migration command;
- real disable/detach;
- real update/reinstall.

Acceptance that manually patches hidden state does not prove the member path.

---

# 18. Health-depth rule

Health claims must state what depth they prove.

Suggested levels:

### STRUCTURAL

Required files/schema/paths exist.

### ATTACHMENT

Host registration and owned integration files are valid.

### RUNTIME

Process/engine can start and answer.

### DEPENDENCY

Required providers/connections/models are available.

### OPERATIONAL

Representative real work succeeds.

### SYSTEM

Cross-component workflow succeeds through supported public paths.

A "doctor PASS" must not be interpreted as deeper health than it actually tests.

---

# 19. Readiness-state rule

Never merge these states:

```text
AVAILABLE
INSTALLED
SUPPORTED
ATTACHED
ENABLED
HEALTHY
READY
INITIALIZED
AUTHORIZED
APPROVED
EXECUTING
SUCCEEDED
VERIFIED
```

A component may skip irrelevant states, but no state should imply another unless the contract explicitly guarantees it.

---

# 20. Cross-component boundary rule

When the component integrates with a sibling:

1. identify the sibling's public/owned boundary;
2. check whether integration uses it;
3. reject direct internal storage access unless that is explicitly the contract;
4. preserve sibling canonical ownership;
5. record version compatibility;
6. test optional absence;
7. test degraded/incompatible presence;
8. test late installation.

The audit should flag "works only because both repos know each other's internals" as architectural debt.

---

# 21. Write-path rule

For any durable write, trace the complete path:

```text
request
→ validation
→ identity/fingerprint
→ scope
→ permission
→ approval
→ owner resolution
→ durable idempotency
→ canonical effect
→ receipt/event
→ verification
```

If the pipeline stops before canonical effect, document it as transport/intake rather than complete write integration.

---

# 22. Read-path rule

For important retrieval, trace:

```text
caller
→ scope
→ owner/source
→ query/projection boundary
→ canonical/derived distinction
→ result
→ freshness/provenance
```

Direct DB/file access by non-owners should be examined closely.

---

# 23. UI/app/dashboard rule

A visual interface must be audited for hidden ownership.

Ask:

- can the app be deleted and rebuilt?
- is displayed state a projection?
- does editing in UI write through the canonical owner?
- does UI maintain a shadow copy?
- are stale projections labeled?

A convenient UI must not become a second source of truth.

---

# 24. Portability rule

For components intended to work outside AI-Verse OS:

Separate:

- core portable engine;
- AI-Verse-specific host adapter;
- runtime-specific adapter;
- optional integrations.

Portability must not require weakening:

- scope;
- ownership;
- permissions;
- provenance;
- isolation.

---

# 25. Inspiration review

For each evidenced inspiration:

1. name the source;
2. cite where the repository records it;
3. identify what was adopted;
4. identify what was changed;
5. identify what was deliberately not adopted where known;
6. preserve attribution/license obligations.

Do not create a competitive-history narrative from guesses.

---

# 26. Documentation drift review

Documentation is an operational dependency because agents read it.

A stale doc that directs an agent to obsolete architecture is a real system defect.

Every audit must explicitly check:

- old naming;
- old commands;
- old paths;
- old component topology;
- obsolete ownership;
- stale "future work" that has already shipped;
- shipped features still described as planned;
- old release pins.

---

# 27. Final component outputs

After completing the audit, write or replace:

```text
components/<component>/COMPONENT-SPEC.md
components/<component>/SOURCE-MAP.md
components/<component>/QC.md
```

## COMPONENT-SPEC.md must include

- identity;
- purpose;
- philosophy;
- architecture;
- ownership;
- source-of-truth;
- lifecycle;
- integration;
- security;
- historical evolution;
- inspirations;
- current milestone;
- completeness matrix;
- lifecycle/command matrix;
- exact gaps;
- definition of done;
- open decisions;
- supreme-system contribution.

## SOURCE-MAP.md must include

- exact reviewed revision;
- canonical source inventory;
- important files;
- implementation evidence;
- tests/CI;
- history/PR evidence;
- provenance;
- contradictions;
- evidence limitations.

## QC.md must include

- independent lens-by-lens verdicts;
- enforcement vs prose distinctions;
- contradictions;
- negative-space findings;
- readiness;
- blockers;
- final verdict.

---

# 28. Living-spec propagation

A component audit is not complete when only its three files are updated.

Also ask:

> Did this audit reveal a system-wide law, shared protocol need, roadmap change, new accepted intent or open system decision?

If yes:

- update `docs/IDEA-INBOX.md`;
- update `docs/MASTER-PLAN.md` when methodology/system-wide rules change;
- update relevant cross-component specs;
- update the supreme blueprint once it exists;
- append `docs/SYSTEM-CHANGELOG.md`.

---

# 29. Audit completion checklist

Before saying a component audit is complete, verify:

- [ ] exact current revision recorded;
- [ ] repository inventoried;
- [ ] canonical/generated/vendor boundaries identified;
- [ ] root identity files read;
- [ ] architecture/contracts read;
- [ ] source-of-truth/ownership reconstructed;
- [ ] lifecycle commands inspected in code, not only docs;
- [ ] tests and CI inspected;
- [ ] relevant PR/repair history inspected;
- [ ] security/isolation inspected;
- [ ] install-order behavior inspected;
- [ ] migration behavior inspected;
- [ ] portability inspected;
- [ ] permissions/approval inspected;
- [ ] read/write boundaries traced;
- [ ] health/readiness depth inspected;
- [ ] negative-space analysis performed;
- [ ] contradiction scan performed;
- [ ] documentation drift recorded;
- [ ] inspirations/provenance searched;
- [ ] current milestone identified;
- [ ] completeness dimensions separated;
- [ ] "works like a glove" blockers listed;
- [ ] definition of done written;
- [ ] component spec replaced/updated;
- [ ] source map replaced/updated;
- [ ] QC replaced/updated;
- [ ] system-wide findings propagated;
- [ ] changelog updated.

If any materially relevant item is skipped, the audit should say so explicitly.

---

# 30. Reviewer discipline

The reviewer must prefer:

- "not found in the reviewed repo" over absolute unsupported absence claims;
- "unverified" over assumed;
- "plan-only" over "implemented";
- "architecture exists" over "feature works";
- "historical" over "current" when evidence is old;
- "current code proves" over "README claims";
- precise boundaries over flattering completeness statements.

The purpose of this methodology is not to make every component look finished.

The purpose is to make the final AI-Verse system specification reliable enough that a future model, developer or operator can build on it without repeating old mistakes.
