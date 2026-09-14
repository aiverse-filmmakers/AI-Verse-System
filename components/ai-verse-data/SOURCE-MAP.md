# AI-Verse Data Source Map

**Component:** AI-Verse Data  
**Canonical repository:** aiverse-filmmakers/AI-Verse-Data  
**Reviewed default branch:** main  
**Reviewed head:** 2497b54e5fbdf0fec4621d218302b3df30dbbc03  
**Reviewed tree:** 15402f5bddb618be6ca9f5461ef62d8dd98e4565  
**Head commit message:** Task 41/41 Phase 5.6: full release acceptance suite - FIRST RELEASE COMPLETE  
**Review date:** 2026-09-13  
**Audit method:** AI-Verse-System/docs/AUDIT-METHODOLOGY.md  
**Cross-repository rule:** no sibling repository was independently audited. Cross-repository observations are limited to pinned contracts/workflows contained inside AI-Verse-Data itself.

---

## 2026-09-14 current superseding source map

**CURRENT head:** `8edde7dca5afa34e300130cc6b8ee2b4170ad40f`

The original source map reviewed head `2497b54e5fbdf0fec4621d218302b3df30dbbc03`. The following later evidence supersedes conflicting current-state claims:

- `189b13264ab86115d2f21fee3ba8cd5a8dac6581` - merged PR #13 canonical five-component Data release hardening;
- `579dae596a1c929bbc0e900541d29742c18b875e` - safe retryable automatic Data structure ensure;
- `8edde7dca5afa34e300130cc6b8ee2b4170ad40f` - materialized engine trusted host-bound actor support;
- `test/os-host-protocol.test.ts` - callable OS host protocol, trusted actor and safe automatic structure behavior;
- `test/migrations.test.ts` / schema migration tests - explicit destructive/migration-required boundary;
- Distribution A-F run `34890195270` - real cross-owner scenarios E/F against exact Data head;
- frozen Agent clean-machine acceptance - real supported Data host path across Ubuntu/macOS/Windows.

The statements below that the materialized engine is registration-only, PR #13 is open, real product-path acceptance is unexecuted, or current CI is red are historical and no longer CURRENT.

---

## 1. Point-in-time repository record

### Repository metadata

- repository: aiverse-filmmakers/AI-Verse-Data
- visibility: private
- default branch: main
- reviewed main head: 2497b54e5fbdf0fec4621d218302b3df30dbbc03
- reviewed head timestamp: 2026-09-12T13:14:11Z
- main branch protection at review: disabled
- required status checks at review: none enforced by branch protection

### Canonical tree inventory

At the reviewed head:

| Area | Blob count | Approximate bytes | Classification |
|---|---:|---:|---|
| src/ | 122 | 733,742 | Canonical implementation |
| test/ | 41 | 641,322 | Canonical verification/evidence |
| docs/ | 52 | 595,160 | Canonical architecture/status/history, with drift noted below |
| examples/ | 6 runnable examples | small | Product examples / acceptance support |
| .github/workflows/ci.yml | 1 | n/a | Canonical CI |
| package.json | 1 | n/a | Canonical package/runtime contract |
| tsconfig.json | 1 | n/a | Build contract |
| README.md | 1 | n/a | Public identity/current-release narrative |

No tracked dist/ build tree or vendored dependency tree was found in the reviewed repository inventory. dist/ is generated.

The native extension files installed under a host's .aiverse/extensions/ai-verse-data/ are generated/materialized runtime artifacts whose source is the canonical TypeScript implementation.

---

## 2. Evidence hierarchy used

The audit followed the repository methodology's evidence priority:

1. current executable implementation;
2. current tests and CI;
3. machine-readable/package/protocol contracts;
4. current architecture/integration documents;
5. README;
6. phase/status/release claims;
7. PR and commit history;
8. older documents;
9. inference.

This ordering mattered because Data contains several contradictions where current implementation is narrower than release prose.

---

## 3. Top-level identity and package evidence

### package.json

Evidence for:

- package name @ai-verse/data;
- version 0.1.0-alpha.0;
- ESM package;
- Node >=22;
- bin ai-verse-data -> dist/src/cli.js;
- GitHub-install preparation through build;
- better-sqlite3 13.0.3;
- license UNLICENSED;
- public export surfaces:
  - protocol
  - storage
  - scope
  - catalog
  - records
  - query
  - transactions
  - idempotency
  - provenance
  - bulk
  - backup
  - schema-migrations
  - recovery
  - client
  - bots
  - brain
  - memory
  - dashboard
  - apps
  - connections
  - automation
  - native

### README.md

Useful for intended product identity and high-level release narrative.

Important claims:

- Data is canonical structured operational data;
- local-first SQLite;
- 41/41 tasks complete;
- first release complete;
- native workspace path;
- Data-vs-Memory boundary;
- package/adapter surfaces.

README claims were not treated as proof where current source contradicted them.

---

## 4. Core protocol and storage evidence

### src/protocol/

Primary evidence for:

- ai-verse-data/0.1 request/response model;
- actor, scope and authorization shapes;
- bounded operations;
- validation;
- rejection of unexpected/raw-path/raw-SQL shaped input.

Important files include:

- src/protocol/types.ts
- src/protocol/validation.ts
- src/protocol/index.ts

### src/storage/sqlite-driver.ts

Primary evidence for:

- SQLite driver behind storage abstraction;
- format identity;
- create/open behavior;
- fail-closed unrelated database handling;
- WAL;
- foreign keys;
- busy timeout;
- diagnostics;
- binding checks;
- migration-required behavior.

### src/storage/types.ts

Primary machine constants for:

- database format version;
- minimum migratable format;
- application identity;
- binding metadata;
- migration framework version.

### src/storage/sqlite-migrations.ts

Primary evidence for:

- v1 -> v2 internal migration;
- migration definitions/digests;
- _schema_migrations ledger;
- pre-migration verified backup;
- required/incomplete/current states;
- retry semantics;
- fail-closed incompatible/newer states.

### src/storage/sqlite-query-store.ts

Primary evidence that structured query plans become parameterized SQL rather than arbitrary caller SQL.

Important implementation observations:

- Data Space/entity predicates are bound;
- JSON field paths are bound;
- filter values are bound;
- sort directions/operators come from validated enums;
- aliases are quoted;
- ordinary caller text is never concatenated as executable SQL structure.

---

## 5. Scope and identity evidence

### src/scope/trusted-root.ts

Primary evidence for:

- root canonicalization;
- safe path derivation;
- existing symlink rejection;
- workspace scope path;
- standalone scope path;
- exact scope binding.

Canonical paths:

~~~text
workspace:
workspaces/<workspace-id>/data/ai-verse-data.sqlite

standalone:
.ai-verse-data/data.sqlite
~~~

### docs/SCOPE-AND-IDENTITY-V0.1.md

Architecture narrative for scope binding and early-database compatibility.

### docs/PHASE-1-STATUS.md

Important historical evidence:

- Task 4 introduced scope identity;
- recognized older unbound AI-Verse Data DB may be bound exactly once;
- workspace/kind mismatch later fails closed;
- same logical workspace ID under distinct trusted roots remains physically isolated.

This is the strongest evidence for legacy handling that exists today.

---

## 6. Catalog, schemas and record evidence

### src/catalog/engine.ts

Evidence for:

- Data Spaces;
- entity schemas;
- schema versions;
- schema digests;
- safe additive changes;
- migration-required changes.

### src/records/engine.ts

Evidence for:

- create/get/list/update/soft delete;
- stable record IDs;
- record and schema versions;
- actor attribution;
- stored validation;
- expectedVersion;
- relation updates.

### src/records/validation.ts and related validators

Evidence for:

- field type constraints;
- nullable/required semantics;
- defaults;
- enum/range/date/datetime checks;
- record size limits.

### docs/CATALOG-AND-SCHEMAS-V0.1.md

Architecture contract for Data Spaces and logical schemas.

### docs/RECORD-CRUD-V0.1.md

Architecture contract for canonical record behavior.

---

## 7. Query, relation and transaction evidence

### src/query/semantics.ts

Primary evidence for:

- schema-aware filters;
- valid operator/type combinations;
- enum checking;
- restricted JSON querying;
- projection validation;
- aggregate validation.

### src/query/engine.ts

Evidence for:

- cursor shape/fingerprint;
- bounded query execution;
- query semantics;
- aggregate execution.

### src/transactions/engine.ts

Evidence for:

- bounded multi-record transactions;
- create/update/delete only;
- one database/workspace;
- local clientRef references;
- all-or-nothing execution through the storage transaction boundary.

### relation storage/record logic

Evidence for:

- target existence/active checks;
- declared target entity/space;
- normalized relation index;
- inbound reference delete protection.

### docs/QUERY-AND-AGGREGATES-V0.1.md
### docs/RELATIONS-AND-TRANSACTIONS-V0.1.md

Supporting contracts.

---

## 8. Concurrency, idempotency and provenance evidence

### src/idempotency/engine.ts

Evidence for:

- durable idempotency keys;
- request fingerprinting;
- exact replay;
- conflict on same key/different request;
- response/result digest behavior.

### src/provenance/engine.ts

Evidence for:

- mutation event creation;
- mutation receipts;
- internal provenance writer;
- events and receipt lookup.

### test/concurrency.test.ts
### test/idempotency.test.ts
### test/provenance.test.ts

Verification for competing writers, replay and evidence.

### docs/PHASE-2-STATUS.md

Historical task-by-task evidence for reliability hardening.

---

## 9. Bulk operations evidence

### src/bulk/engine.ts

Evidence for:

- bounded bulk operations;
- preview;
- deterministic digest;
- execute-against-preview semantics;
- transactionality.

### test/bulk.test.ts

Adversarial and correctness evidence.

---

## 10. Backup, export and import evidence

### src/backup/engine.ts

Primary evidence for:

- consistent SQLite backup;
- manifests;
- SHA-256 verification;
- receipts;
- portable export/import;
- no-overwrite destination semantics;
- exact binding verification.

### docs/BACKUP-EXPORT-IMPORT-V0.1.md

Important boundary evidence:

- restore/import are not merge operations;
- binding must match;
- portability artifacts preserve identity;
- import does not silently remap one workspace into another.

### Consequence for legacy adoption

Because binding equality includes kind and workspaceId, a bound standalone source is not directly importable as a workspace-bound canonical database.

This is safe restore behavior but proves that backup/import is not the missing standalone-to-native adoption path.

---

## 11. User-schema migration evidence

### src/schema-migrations/engine.ts

Evidence for:

- preview/execute;
- explicit backfills;
- destructive approval metadata;
- bounded changes;
- atomic schema/record rewrite;
- relation-index rebuild;
- idempotency/provenance.

### test/schema-migrations.test.ts

Verification.

---

## 12. Corruption and recovery evidence

### src/recovery/engine.ts

Primary evidence for:

- diagnosis;
- quarantine;
- migration-required/incomplete distinction;
- scope conflict;
- corruption classification;
- staged recovery from backup or portable export;
- exact binding match;
- separate destination;
- destination health verification.

Critical current return value:

~~~text
promotion: manual-explicit-not-implemented
~~~

This is direct implementation evidence that verified recovery staging exists but canonical promotion is not implemented as a product operation.

### test/recovery.test.ts

Verification of failure/degraded states.

---

## 13. Typed client evidence

### src/client/client.ts
### src/client/types.ts

Evidence for:

- scope-first typed client;
- bound actor;
- bound authorization metadata;
- structured method groups;
- stable response/error envelopes.

Important enforcement finding:

The client validates and carries authorization but does not universally intersect capabilityRefs against every operation itself.

Permission reduction is implemented by consumer adapters.

This distinction is important to the PR #13 security hardening findings.

---

## 14. Consumer adapter evidence

### Multiple Bots

Files:

- src/bots/adapter.ts
- docs/BOTS-DATA-ADAPTER-V0.1.md
- test/bots-adapter.test.ts

Evidence for:

- lease workspace/principal/expiry checks;
- Data capability references;
- host-granted capabilityRefs requirement;
- per-operation cap checks;
- task-linked receipts.

### Brain

Files:

- src/brain/adapter.ts
- docs/BRAIN-DATA-ADAPTER-V0.1.md
- test/brain-adapter.test.ts

Evidence for:

- read-only structured Data use;
- no Brain-goal persistence into Data by default.

### Memory

Files:

- src/memory/bridge.ts
- docs/MEMORY-BRIDGE-V0.1.md
- docs/DATA-MEMORY-BOUNDARY.md
- test/memory-bridge.test.ts

Evidence for:

- stable Data references;
- evidence lookup;
- candidate proposals;
- no automatic Memory writes;
- Data events remain Data audit facts.

### Dashboard

Files:

- src/dashboard/projection.ts
- docs/DASHBOARD-PROJECTION-V0.1.md
- test/dashboard-projection.test.ts

Evidence for:

- read-only projection model;
- no raw DB path;
- Dashboard-local systemId.

### Apps

Files:

- src/apps/kit.ts
- docs/APPS-DATA-CONTRACT-V0.1.md
- test/apps-contract.test.ts

Important current-main defect:

The Apps capability model intentionally excludes delete, but nested transaction/bulk operation classification can map any non-create mutation to update, which allows record delete to tunnel through update authority.

PR #13 explicitly repairs this.

### Connections

Files:

- src/connections/authority.ts
- docs/CONNECTIONS-AUTHORITY-V0.1.md
- test/connections-authority.test.ts

Evidence for:

- local_canonical authority;
- explicit one-way imports;
- connections:// source references;
- no implicit bidirectional sync.

### Automation

Files:

- src/automation/events.ts
- docs/AUTOMATION-EVENTS-V0.1.md
- test/automation-events.test.ts

Evidence for:

- committed-event polling;
- facts only;
- no scheduler inside Data.

---

## 15. Native OS integration evidence

### src/native/compatibility.ts

Evidence for:

- AI-Verse OS v2 compatibility detection;
- compatible / no-os / incompatible;
- no silent fallback from a broken native host.

### src/native/extension-materialization.ts

Critical CURRENT main evidence.

At the original reviewed head the materialized engine was registration-only. CURRENT head materializes the callable host protocol and advertises trusted host-bound actor support.

### src/native/extension-installer.ts

Evidence for:

- owned extension placement;
- registry schema;
- lock;
- in-lock re-read;
- raw-text lost-update protection;
- atomic replace;
- preservation of unknown fields and unrelated entries;
- rollback around owned materialization.

### src/native/instruction-discovery.ts

Evidence for:

- safe read-only instruction/runtime discovery;
- engine file is inspected but not executed.

### src/native/workspace-resolver.ts

Evidence for:

- trusted OS root;
- WORKSPACE.yaml parsing;
- schema major;
- safe workspace ID;
- exact manifest ID;
- workspace status;
- canonical DB path.

### src/native/workspace-discovery.ts

Evidence for seven discovery states:

- missing;
- compatible;
- migration_required;
- quarantined;
- scope_conflict;
- unsupported;
- unavailable.

### src/native/workspace-init.ts

Evidence for:

- active-only explicit initialization;
- no every-workspace creation;
- target-path conflict safety;
- compatible reopen;
- no silent migrate/rebind/repair.

### src/native/lifecycle.ts

Evidence for current lifecycle:

- install;
- update;
- disable;
- uninstall.

Historical reviewed-head note. Current lifecycle behavior must be read from the merged release-hardening and post-release heads above.

### src/cli.ts

Critical user-path evidence.

Current main CLI exposes:

- install;
- update;
- disable;
- uninstall;
- doctor;
- status.

It does not expose:

- enable;
- init;
- adopt;
- migrate;
- reconcile;
- recovery promote;
- rollback.

### src/native/doctor.ts

Evidence for:

- deep doctor;
- light status;
- registration and extension checks;
- workspace/database state;
- migration/quarantine/scope diagnostics;
- SQLite runtime;
- integrity and WAL probes.

Important semantics:

- no OS may report standalone healthy;
- not registered is a notice;
- missing workspace DB is a notice;
- healthy therefore is not a final ready-to-serve verdict.

---

## 16. Lifecycle documentation evidence

### docs/INSTALLATION-AND-LIFECYCLE.md on main

Useful intent and lifecycle laws, but contains stale/forward-looking language.

### docs/NATIVE-CLI-LIFECYCLE-V0.1.md on main

Defines current main lifecycle boundary.

### docs/NATIVE-DOCTOR-STATUS-V0.1.md

Accurately distinguishes deep doctor from light status and confirms that missing registration/database can remain notices.

### docs/INSTALLATION-ORDER-COEXISTENCE-V0.1.md

Evidence for representative registry/order tests using local sibling fixtures.

### docs/AI-VERSE-OS-COMPATIBILITY-V0.1.md
### docs/EXTENSION-MATERIALIZATION-REGISTRATION-V0.1.md
### docs/WORKSPACE-RESOLVER-INITIALIZATION-V0.1.md
### docs/EXTENSION-INSTRUCTIONS-DISCOVERY-V0.1.md

Supporting native contracts.

---

## 17. Data-vs-Memory ownership evidence

### docs/DATA-MEMORY-BOUNDARY.md

Primary source.

Key laws:

- Data owns structured operational truth;
- Memory owns historical recall;
- Data SQLite is not Memory's canonical store;
- Memory's index is not Data;
- Data events do not automatically become Memory;
- current Data wins for Data-owned current values;
- references/evidence are preferred over duplication.

### docs/ECOSYSTEM-INTEGRATION.md

Broader integration map and non-ownership rules.

---

## 18. Security evidence

### docs/SECURITY-AND-AUTHORITY.md

Architecture intent for:

- host policy;
- workspace/principal/task intersections;
- registration != permission;
- least privilege;
- fail-closed boundaries.

### test/adversarial-security.test.ts

Important implementation evidence for:

- traversal;
- symlink components;
- Windows path forms;
- malformed registries;
- stale locks;
- oversized inputs;
- corrupt DB shapes;
- capability forgery;
- no mutation on rejected branches.

### PR #13

Important evidence that several permission issues survived the original Task 41 gate and required later hardening.

This is why current security is classified as strong but not final on main.

---

## 19. Tests used as architecture evidence

Current main test inventory:

1. adversarial-security.test.ts
2. apps-contract.test.ts
3. automation-events.test.ts
4. backup.test.ts
5. bots-adapter.test.ts
6. brain-adapter.test.ts
7. bulk.test.ts
8. catalog.test.ts
9. cli.test.ts
10. client.test.ts
11. concurrency-worker.ts
12. concurrency.test.ts
13. connections-authority.test.ts
14. dashboard-projection.test.ts
15. foundation.test.ts
16. idempotency-worker.ts
17. idempotency.test.ts
18. memory-bridge.test.ts
19. migrations.test.ts
20. native-coexistence.test.ts
21. native-compatibility.test.ts
22. native-doctor.test.ts
23. native-extension-registration.test.ts
24. native-instructions.test.ts
25. native-lifecycle.test.ts
26. native-workspace.test.ts
27. performance-baseline.test.ts
28. phase1-integration.test.ts
29. phase2-integration.test.ts
30. phase3-integration.test.ts
31. phase4-integration.test.ts
32. protocol.test.ts
33. provenance.test.ts
34. query.test.ts
35. records.test.ts
36. recovery.test.ts
37. relations-transactions.test.ts
38. release-acceptance.test.ts
39. schema-migrations.test.ts
40. scope.test.ts
41. storage.test.ts

### Architectural conclusions proven by tests

Tests prove more than unit correctness. They demonstrate intended laws around:

- no silent path escape;
- one-workspace scope;
- no unrelated registry overwrite;
- no automatic DB creation during lifecycle;
- canonical DB preservation;
- idempotent replay;
- OCC;
- transaction rollback;
- relation integrity;
- backup verification;
- migration fail-closed behavior;
- quarantine;
- adapter boundaries;
- install-order registry coexistence.

### Important test limitation

test/release-acceptance.test.ts on main directly imports internal Data APIs such as installDataExtension, initWorkspaceData and createDataClient.

It does not prove that the materialized extension engine can be selected and invoked by the actual OS host.

This is a central current-target gap.

---

## 20. CI evidence

### Current main workflow

.github/workflows/ci.yml runs:

~~~text
ubuntu-latest x Node 22
ubuntu-latest x Node 24
macos-latest  x Node 22
macos-latest  x Node 24
windows-latest x Node 22
windows-latest x Node 24
~~~

Each leg is intended to run:

- install;
- npm run check;
- npm pack --dry-run;
- CLI help smoke;
- actual pack artifact smoke.

### Exact reviewed-head Actions state

Run: 34695862605  
Head: 2497b54e5fbdf0fec4621d218302b3df30dbbc03  
Conclusion: failure

Observed jobs:

- ubuntu Node 22: failure
- ubuntu Node 24: success
- macOS Node 22: success
- macOS Node 24: success
- Windows Node 22: success
- Windows Node 24: success

The failed ubuntu Node 22 job exposes no retrievable step records or logs through the connector, so the audit does not invent a code-level cause.

### Corroborating in-repository PR evidence

PR #13 records the same no-step/no-checkout/no-log hosted-runner failure signature on later hardening workflows and attributes it to GitHub-hosted runner/account eligibility or budget.

This supports infrastructure-failure classification, but it does not turn the gate green.

---

## 21. Release/status evidence

### docs/BUILD-MAP.md

Canonical 41-task build sequence.

### docs/PHASE-1-STATUS.md
### docs/PHASE-2-STATUS.md
### docs/PHASE-3-STATUS.md
### docs/PHASE-4-STATUS.md
### docs/PHASE-5-STATUS.md

Historical task evidence.

### docs/RELEASE-ACCEPTANCE.md

Claims:

- 344/344 local tests pass;
- first release complete;
- Phase 5.6 gate passed.

This is valid evidence for local library composition but is not sufficient evidence for the actual host product path because of the direct-import limitation above.

### Distribution evidence

docs/PACKAGING-INSTALL-V0.1.md records:

- GitHub package path;
- publication deferred;
- version remains alpha;
- license remains UNLICENSED;
- explicit version/license/registry decision still required for publication.

Querying the repository's latest GitHub release endpoint returned 404 during this audit. No current immutable GitHub release was therefore established as release evidence.

---

## 22. PR archaeology

Visible pull-request history:

| PR | Status at review | Purpose / significance |
|---|---|---|
| #1 | merged | Verified backup and portability foundation |
| #2 | merged | Internal migration framework |
| #3 | merged | User-schema migration framework |
| #4 | merged | Corruption quarantine and staged recovery |
| #5 | merged | Phase 2 reliability/adversarial gate |
| #6 | closed draft | Initial OS compatibility line |
| #7 | merged | OS compatibility detector |
| #8 | closed draft | Initial extension-registration line |
| #9 | merged | Hardened extension materialization/registration |
| #10 | closed draft | Native workspace initialization line |
| #11 | closed stale | Phase 3.3 work already present on main |
| #12 | closed draft | First post-release hardening line |
| #13 | open draft | Canonical current post-release/five-component hardening line |

### PR #13 exact state

Title: Fix post-release audit findings  
Head branch: fix/post-release-audit  
Head SHA: ebf1ff48adb1bd3696f4e2c28bddb540a98395af  
Base: main at 2497b54e5fbdf0fec4621d218302b3df30dbbc03  
State: open draft  
Mergeable at review: true  
Mergeable state: unstable  
Changed files: 38  
Additions/deletions: approximately +2827 / -237

### PR #13 repairs relevant to this audit

- Apps delete tunneling through transaction/bulk;
- Apps/Bots provenance visibility;
- explicit entity-scoped event reads;
- malformed adapter authority handling;
- secure Data client scope descriptor;
- live wrapper closed state;
- Memory exact canonical event lookup beyond first 200 events;
- stronger Data evidence/reference binding;
- Dashboard cross-space references;
- record-list cursor fail-closed validation;
- Connections/Automation parser hardening;
- uninstall rollback safety;
- explicit enable;
- update preserving disabled state;
- lifecycle documentation correction;
- real ai-verse-data-host/1.0 runtime;
- Brain trusted-host authorization documentation;
- regression coverage;
- release-smoke workflow;
- five-component acceptance workflow.

### Important negative-space finding

PR #13 does not change the core backup/scope/storage migration/recovery architecture to provide bound standalone -> native workspace adoption.

Therefore PR #13 should not be mistaken for solving the legacy structured-state adoption gap.

---

## 23. Data-owned five-component acceptance evidence

PR #13 adds:

- .github/workflows/five-component-acceptance.yml
- .github/workflows/release-smoke.yml

Because these files live in Data, they were reviewed as Data integration evidence.

The workflow pins:

- OS: 89fb9043ec58c05931d477ef3e154df428a06c22
- Brain: bef8261ad35d126d29aeff5d496f46904125b7b6
- Memory: f5b417f9e7ce1b3f05bc80d10a483d10f6ad10ee
- Skills: 3ab838e6e64561bbb7cea8f85d0ebc75b9e84337

It attempts to prove:

- host config exists before optional components;
- multiple install orders;
- late Memory/Skills/Data/Connections discovery;
- Memory recall;
- Skills resolution;
- read-only Data query through host;
- Data disable -> update stays disabled -> explicit enable;
- Brain ownership handover/handback;
- Memory/Data/Brain detach/reinstall with canonical state preservation;
- final doctors;
- no tracked OS mutation.

This is much closer to the exact product-path acceptance required by the audit methodology than main's release-acceptance.test.ts.

### Execution status

PR #13 current head workflows, attempt 2:

- CI 34716822571: failure
- Release Smoke 34716822441: failure
- Five-Component Release Acceptance 34716822443: failure

PR body records no checkout/setup/steps/logs, consistent with hosted-runner infrastructure failure.

No green execution evidence exists yet for that exact hardening head.

---

## 24. Important commit-history evidence

### Release line

- 2497b54 - Task 41/41 Phase 5.6 full release acceptance, FIRST RELEASE COMPLETE
- 2f51007 - Task 40 packaging/simple install
- 218da11 - Task 39 docs/examples
- cca68b4 - Task 38 performance baseline
- 50b3853 - Task 37 adversarial security
- 417fb46 - Task 36 cross-platform CI matrix

### Cross-platform repair sequence

- dcc2ae7 - normalize snapshots for Windows/macOS
- b81e512 - realpath temp dirs for macOS
- 6970e0f - handle macOS /var -> /private/var
- e81cb15 - wait for worker exit + retry temp delete for Windows file locks
- b8a776d - apply similar Windows worker cleanup hardening to performance tests

These commits establish permanent portability lessons.

### Phase 4 integration sequence

- ad727b0 - typed Data client
- 572e2ee - Bots adapter
- c1c2a91 - Brain adapter
- af2a063 - Memory bridge
- f611981 - Dashboard projection
- 5b4d31e - Apps contract
- b98cc1e - Connections authority
- 3293ea9 - Automation events
- 1c9b9db - Phase 4 integration gate

### Phase 3 native sequence

- 6839878 - workspace resolver/init
- e86749f - instruction discovery
- 616506e - CLI install/update/disable/uninstall
- 1491fad - doctor/status
- d22d0cf - install-order coexistence
- 78d8fbb - Phase 3 acceptance

### Earlier installation commits

- 518ae0d and surrounding Phase 3.2 history - safe extension materialization/registration
- dd827d6 / merge line - OS compatibility detector

### Phase 2 reliability PR sequence

PRs #1-#5 provide better historical grouping than commit search for:

- backup;
- internal migrations;
- schema migrations;
- recovery;
- adversarial/reliability gate.

---

## 25. Documentation contradictions

### docs/PRD.md

Still says:

~~~text
Implementation: Not started
~~~

This is clearly stale relative to current implementation.

### src/index.ts

AI_VERSE_DATA_FOUNDATION_PHASE remains 4.1 on main while release docs say 5.6/complete.

PR #13 fixes this.

### src/cli.ts

Help/current command set is behind the final release narrative and lacks enable/init/migrate/adopt.

### src/native/extension-materialization.ts

Still identifies materialized runtime as Phase 3.2 and registrationOnly.

### docs/RELEASE-ACCEPTANCE.md / docs/PHASE-5-STATUS.md

Call release complete while:

- main product host runtime is incomplete;
- package is alpha;
- license is UNLICENSED;
- public/member publication decision is deferred;
- exact current head CI is red;
- post-release hardening found substantive defects.

### Health wording

Doctor's healthy flag is environment/diagnostic health, not full scope readiness.

Documentation generally explains this, but product surfaces do not expose a separate combined readiness state.

---

## 26. Negative-space searches/findings

The audit explicitly searched for adoption, standalone migration, rebind, existing database, legacy, canonical store and related terms.

### Found

- one-time binding of older unbound Data DBs;
- standalone scope;
- internal migrations;
- backup/import;
- reinstall discovery;
- exact binding conflict rejection.

### Not found as supported behavior at the original reviewed head

- bound standalone -> workspace adoption;
- arbitrary legacy DB importer;
- canonical-store merge;
- automatic conflict reconciliation;
- native migration command;
- native adopt command;
- duplicate canonical detector across legacy routes;
- adoption receipt/handover record;
- recovery promotion command;
- public reconcile command.

Absence conclusions are limited to the reviewed revision and visible repository history.

---

## 27. Inspiration evidence

### docs/RESEARCH-AND-DECISIONS.md

Primary source.

Recorded inspirations/references include:

- Kylon for first-class structured-data/application thinking;
- SQLite official behavior and documentation;
- better-sqlite3 as mature Node implementation;
- review of node:sqlite.

The document also contains architectural decisions D001-D020 and records alternatives/rejections.

**Evidence rule:** inspiration is not implementation truth. The audit uses these sources only to explain design lineage.

---

## 28. Historical versus current evidence map

### CURRENT

- reviewed main source;
- main tests;
- main package metadata;
- main docs where consistent with source;
- current Actions run;
- current PR states.

### HISTORICAL

- phase status documents;
- completed task gates;
- prior PRs;
- earlier implementation commits;
- cross-platform repair sequence;
- older release statements.

### INTENDED / in-flight

- PR #13 changes;
- PR #13 updated lifecycle docs;
- PR #13 host runtime;
- PR #13 five-component workflows.

### GAP

Derived only where current implementation and accepted/current target differ, especially:

- executable main host path;
- explicit enable on main;
- adapter security repairs on main;
- bound standalone/legacy adoption;
- native migration UX;
- recovery promotion;
- readiness envelope;
- executed final release gate;
- immutable distribution.

---

## 29. Evidence limitations

1. The audit did not independently inspect OS, Brain, Memory or Skills repositories. Any information about them comes only from Data-owned pinned integration workflows/contracts.
2. GitHub connector access did not return logs/step records for the failed main ubuntu Node 22 job. Cause is therefore not inferred from that job alone.
3. PR #13 body contains runner-infrastructure diagnosis. That is repository-maintainer evidence, not a green test result.
4. No current immutable GitHub release could be established from releases/latest at review time.
5. The audit does not claim all possible external legacy database formats are known. The gap is that no generic supported adoption path exists, not that every possible importer should exist.
6. The audit does not treat generated dist/ output as canonical source.
7. Documentation status claims were downgraded whenever implementation/tests contradicted them.
8. The active PR is not CURRENT until merged.
9. The current audit records no numerical completeness percentage because the remaining product work has no honest denominator.
10. The lack of a feature is only claimed where repository search, lifecycle surfaces, tests and PR history consistently support the absence.

---

## 30. Source-to-conclusion trace

| Conclusion | Strongest evidence |
|---|---|
| Core Data engine is mature | src modules + Phase 1/2 tests + release suite |
| SQLite is implementation, not public contract | storage abstraction + protocol + docs |
| Workspace isolation is technical | trusted-root, scope binding, resolver, tests |
| Old unbound DB can be adopted once | scope/storage implementation + Phase 1 status |
| Bound standalone cannot become workspace implicitly | exact binding comparison |
| Backup/import is not adoption | backup binding equality + no-overwrite semantics |
| Native main attachment is registration-only | extension-materialization.ts |
| Main release test bypasses real host runtime | release-acceptance.test.ts direct imports |
| Main lacks enable | cli.ts + lifecycle.ts |
| Main lacks native migrate/adopt/reconcile | cli.ts + native exports/search |
| Doctor health != readiness | doctor.ts + doctor/status docs |
| Recovery promotion incomplete | recovery engine promotion marker |
| Known adapter security defects remain on main | current adapter source + PR #13 repair set |
| PR #13 materially fixes host/lifecycle/security | PR diff/body/files |
| PR #13 is not release evidence yet | open draft + failed/unexecuted workflows |
| Distribution is not immutable member release | package version/license + packaging docs + no latest release |
| Data != Memory | DATA-MEMORY-BOUNDARY.md + Memory bridge |
| Cross-platform behavior required repairs | Task 36/38 repair commits |
| Current milestone is not truly 100% | all above combined under methodology's product-path rule |

---

## 31. Files most important for future re-audits

Re-audit these first after Data changes:

1. package.json
2. README.md
3. src/index.ts
4. src/cli.ts
5. src/native/extension-materialization.ts
6. src/native/host-engine.ts if merged
7. src/native/host-adapter.ts if merged
8. src/native/lifecycle.ts
9. src/native/workspace-init.ts
10. src/native/workspace-discovery.ts
11. src/native/doctor.ts
12. src/scope/trusted-root.ts
13. src/storage/sqlite-driver.ts
14. src/storage/sqlite-migrations.ts
15. src/backup/engine.ts
16. src/recovery/engine.ts
17. src/client/client.ts
18. src/apps/*
19. src/bots/*
20. src/memory/*
21. test/release-acceptance.test.ts
22. test/post-release-audit.test.ts if merged
23. test/os-host-protocol.test.ts if merged
24. .github/workflows/ci.yml
25. .github/workflows/release-smoke.yml if merged
26. .github/workflows/five-component-acceptance.yml if merged
27. docs/INSTALLATION-AND-LIFECYCLE.md
28. docs/RELEASE-ACCEPTANCE.md
29. docs/PHASE-5-STATUS.md
30. docs/DATA-MEMORY-BOUNDARY.md
31. docs/RESEARCH-AND-DECISIONS.md
32. open/merged PR history since #13
33. exact post-change Actions runs
34. exact immutable release/tag if one exists
