# A1.6 — Independent Repository Audit: AI-Verse-Data

**Audit date:** 2026-09-15  
**Frozen ref:** `8edde7dca5afa34e300130cc6b8ee2b4170ad40f`  
**System baseline:** `380b5ad5a86444ec0388519390e5dfa918fec82f`  
**Status:** COMPLETE  
**Standalone verdict:** DOGFOOD BLOCKED  
**R-a:** COMPLETE / PASS  
**R-b:** COMPLETE / MATERIAL FAILURE FOUND  
**R-c:** COMPLETE / BLOCKED  
**Findings:** `WSA-2026-020`, `WSA-2026-021`  
**Next:** A1.7 AI-Verse-Multiple-Bots

## Independence and drift control

A1.6 used only the frozen Data repository, Data-owned tests/workflows, and Data GitHub metadata/history. No sibling implementation was used to fill a standalone gap.

At task start and pre-write recheck:

- Data main remained `8edde7dca5afa34e300130cc6b8ee2b4170ad40f`;
- System main remained `380b5ad5a86444ec0388519390e5dfa918fec82f`;
- no open Data/System PRs existed;
- no Data product file was modified;
- Dashboard MC1.4 remained paused.

## Reconstruction

The frozen tree contains **272 tracked entries**.

Data identifies itself as the canonical structured-data layer for AI-Verse. It owns structured operational records and their storage/reliability state, including:

- Data Spaces and entity schemas;
- canonical records and relations;
- bounded query and aggregate execution;
- optimistic concurrency;
- durable idempotency;
- immutable events and mutation receipts;
- backup/export/import;
- internal database-format migrations;
- user-schema migrations;
- corruption quarantine and staged recovery;
- native extension integration;
- typed Data client and bounded adapters for Bots, Brain, Memory, Dashboard, Apps, Connections and Automations.

Data does not claim canonical ownership of:

- Memory narrative/history;
- Brain goals or strategic direction;
- OS workspace/actor identity;
- Connections credentials;
- Dashboard system identity;
- automation scheduling;
- host approval policy.

## Trusted storage model

Native workspace storage is derived as:

`<trusted-root>/workspaces/<workspace-id>/data/ai-verse-data.sqlite`

`TrustedDataRoot`:

- canonicalizes the selected root;
- validates cross-platform workspace IDs;
- rejects traversal and unsafe path segments;
- checks existing components for symlinks;
- verifies the trusted root has not changed;
- keeps resolved paths physically beneath the trusted root.

Native workspace resolution additionally requires a real non-symlink workspace directory and a bounded regular `WORKSPACE.yaml` whose ID matches the requested workspace.

Workspace initialization is explicit and refuses paused/archived, migration-required, quarantined, conflicting or unsupported existing state.

## SQLite identity and binding

Database identity is independent from package/protocol/entity-schema versions.

Current database format uses:

- format `ai-verse-data/sqlite`;
- format version 2;
- SQLite application ID;
- SQLite user version 2;
- engine metadata;
- optional persistent scope binding.

Existing empty/unrecognized files are never silently initialized.

A scoped database binds to:

- scope kind;
- workspace ID;
- binding version.

Once bound, a conflicting scope fails closed.

## Canonical mutation safety

Record mutation uses:

- schema validation;
- stable record IDs;
- version-aware update/delete;
- short SQLite transactions;
- durable actor attribution;
- idempotency keys;
- immutable mutation events/receipts.

Optimistic concurrency is enforced at the storage update predicate. Separate-process tests prove one winner when multiple writers race the same expected record version.

Idempotency binds a key to operation, trusted actor and semantic request. Matching committed retries replay the original result. Changed reuse conflicts.

Mutation provenance, canonical effects and idempotency commit atomically.

## Query, transaction and bulk safety

Public query is a bounded structured AST rather than raw SQL.

Transactions:

- stay within one workspace database;
- cap operation count;
- resolve only earlier client references;
- roll back all required operations together.

Bulk mutation:

- caps operation count and payload bytes;
- previews using the real mutation engine under rollback;
- binds a preview digest to actor, operations and current state;
- requires exact digest match at commit;
- commits all-or-nothing.

## Schema migration safety

Normal schema evolution allows safe additive changes and reports migration-required for destructive changes.

User-schema migration:

- has read-only preview;
- binds a digest to executor, owner, schema state and active record state;
- recomputes under write intent;
- requires destructive approval metadata when applicable;
- uses bounded deterministic backfills only;
- rewrites schema, records, relations, idempotency and provenance atomically.

No arbitrary SQL or model-generated migration code is accepted.

## Backup, recovery and quarantine

Backup/export uses consistent SQLite snapshots plus manifest/payload/state digests.

Restore/import:

- verifies artifact identity;
- requires expected binding;
- stages before installation;
- refuses an existing canonical destination.

Confirmed corruption records a durable quarantine marker. Quarantine blocks canonical writes.

Recovery diagnoses the original source without automatically repairing or replacing it and stages verified recovery into a different same-binding destination.

## Native lifecycle

Native extension installation:

- requires a compatible OS host;
- owns only the Data extension entry/files;
- preserves unrelated registry state and unknown fields;
- rejects unsafe paths/symlinks;
- uses exclusive registry locking;
- never steals an existing lock;
- re-reads registry state under lock;
- compares exact expected raw registry bytes before atomic replacement;
- rolls back owned files on pre-commit failure.

Install/update/disable/enable/uninstall do not delete canonical workspace databases.

## Integration adapters

### Multiple Bots

The Bots adapter rechecks:

- workspace;
- Bot/Worker principal;
- task lease;
- expiry;
- space/entity/action capability.

Lease capabilities must also exist in the host-bound client authorization references. Delegation narrows authority.

### Brain

Brain adapter is read-only.

### Memory

Memory bridge exposes evidence/provenance references and candidate-memory material. It does not automatically write Memory.

### Dashboard

Dashboard is a bounded read-only projection.

### Apps

App manifests do not grant authority on their own. Declared access must also exist in host-bound capability references. Delete is denied, including through transaction/bulk paths.

### Connections

Current authority is local-canonical plus bounded import concepts. No bidirectional sync engine is silently introduced.

### Automations

Data exposes committed event facts. It does not own scheduling or trigger activation.

## Host authorization boundary

The base typed client accepts a host-supplied authorization context and records it on results/provenance.

A1.6 does **not** classify the absence of a second independent policy engine inside the base client as a defect. Data's documented contract deliberately leaves host policy, principal grants and approvals with OS/Bots/App integration boundaries, while Data applies structural safety.

Narrow adapters such as Bots and Apps do intersect their local grant with the host capability references.

## C-A1.6-001 — public client does not prove that its scope came from TrustedDataRoot

**Source A:** client/security documentation says the client requires a trusted `DataDatabaseScope` derived from `TrustedDataRoot`, and raw filesystem paths are not accepted.

**Source B:** `DataDatabaseScope` is an exported structural TypeScript interface with no runtime brand. Client scope validation checks only object shape/workspace identity, then trusts the supplied object's `databasePath()` and `binding`.

**Higher-authority source:** executable public client + scope implementation.

**Finding:** `WSA-2026-020`.

## WSA-2026-020 — structurally forgeable Data scope bypasses trusted-root path provenance

**Severity:** HIGH  
**Confidence:** PROVEN  
**State:** OPEN  
**Root area:** trusted scope provenance / filesystem and workspace isolation  
**Affected repo:** `AI-Verse-Data`

### Summary

The public client contract says callers provide a trusted scope produced from `TrustedDataRoot`. Runtime enforcement does not prove that provenance.

### Observed behavior

`DataDatabaseScope` is a normal exported interface containing:

- kind;
- workspaceId;
- binding;
- root view;
- `databasePath()`.

The public client validates only that the scope is an object with a string workspace ID. It then passes the supplied `databasePath()` and binding directly to storage.

The secure client wrapper preserves this same scope and adds no nominal provenance check.

### Impact

A structurally compatible caller-supplied scope object can bypass the path derivation guarantees of `TrustedDataRoot`. The public client therefore does not itself guarantee that its database path came from the trusted-root/workspace constructors described by the API.

Native OS host flows remain stronger because they construct scopes internally. The defect is still HIGH because the public client is an exported supported surface and the violated invariant is workspace/filesystem authority.

### Required closure evidence

After repair authorization:

- make trusted scopes runtime-verifiable/nominal rather than structural-only;
- have public open/client paths reject unbranded scopes;
- derive or validate the database path/binding from the trusted root instead of trusting arbitrary scope methods;
- add regressions for structurally compatible forged scopes, including wrong-workspace and non-derived path cases.

## C-A1.6-002 — accepted component identity is older than current material behavior

**Source A:** accepted component descriptor binds `0.1.0-alpha.0` to `189b13264ab86115d2f21fee3ba8cd5a8dac6581`.

**Source B:** frozen current main is 10 commits newer, still reports `0.1.0-alpha.0`, and the documented GitHub install path follows the mutable default branch.

**Higher-authority source:** current package/source + immutable release descriptor + commit comparison.

**Finding:** `WSA-2026-021`.

## WSA-2026-021 — accepted Data alpha identity does not uniquely identify frozen current behavior

**Severity:** LOW  
**Confidence:** PROVEN  
**State:** OPEN  
**Root area:** release/version/install reproducibility  
**Affected repo:** `AI-Verse-Data`

Accepted component revision:

`189b13264ab86115d2f21fee3ba8cd5a8dac6581`

Frozen current main:

`8edde7dca5afa34e300130cc6b8ee2b4170ad40f`

Current is **10 commits ahead** while package/index identity remains `0.1.0-alpha.0`.

The later commits include material supported behavior such as safe additive structure emergence and host-bound actor request support.

The documented GitHub install path is:

`npm install github:aiverse-filmmakers/AI-Verse-Data`

with no accepted revision pin.

### Impact

Version-only support/debugging cannot distinguish the accepted component artifact from later current source, and the default GitHub install path can move independently of the accepted descriptor.

The descriptor itself remains immutable and the package is explicitly pre-release, so standalone severity is LOW. A5 must determine release-set consequences.

### Required closure evidence

After release/repair authorization:

- accept a new immutable Data revision or change package version for materially newer behavior;
- provide an immutable public-beta GitHub install reference when reproducibility is required;
- add release/install identity QC.

## Exact-head executable evidence

Frozen Data head:

`8edde7dca5afa34e300130cc6b8ee2b4170ad40f`

CI run:

`34864837334` — **SUCCESS**

All six matrix jobs passed with real executed steps:

- Node 22, Windows: `104045937458`
- Node 24, Windows: `104045937676`
- Node 24, Ubuntu: `104045937881`
- Node 22, macOS: `104045937902`
- Node 22, Ubuntu: `104045937911`
- Node 24, macOS: `104045937944`

Each leg executed:

- checkout;
- Node setup;
- dependency installation;
- full build/test;
- package smoke;
- CLI smoke;
- install smoke.

## Negative-space checks

A1.6 found no evidence that Data:

- silently turns Memory, Brain, Dashboard or Connections state into competing canonical Data;
- accepts raw SQL through normal agent/client operations;
- permits unsafe workspace identifiers through `TrustedDataRoot`;
- follows existing scoped symlink components;
- silently rebinds a database to a conflicting workspace;
- silently initializes an existing unknown/empty database;
- silently migrates database format on normal open;
- silently repairs or overwrites a quarantined canonical source;
- overwrites an existing canonical restore/import destination;
- uses last-write-wins for versioned records;
- duplicates committed mutations on matching idempotent retry;
- allows a stale bulk/schema preview to commit unchanged;
- lets Apps gain delete through transaction/bulk composition;
- lets Bot/App manifest or lease strings expand beyond host-bound capability refs;
- lets Brain mutate Data;
- automatically writes Memory;
- gives Dashboard a competing canonical identity;
- implements an Automation scheduler;
- steals an existing extension registry lock;
- mutates sibling extension entries as part of its own lifecycle.

## Evidence limitations

- A1.6 did not independently validate sibling implementations.
- Native OS composition and cross-repo authority must be revalidated in A2.
- The forged-scope finding is established from the exported runtime type boundary and client/open implementation; no product code was changed to add a reproduction test during audit.
- Package licensing remains explicitly `UNLICENSED` and npm publication remains deferred by Data's own packaging contract. No separate legal/publication conclusion is made in A1.6; A5 owns release consequences.
- Release-set acceptance belongs to A5.

## Evidence IDs

- `E-A1.6-001` frozen Data tree and repository metadata.
- `E-A1.6-002` README/architecture ownership reconstruction.
- `E-A1.6-003` trusted-root and workspace path implementation.
- `E-A1.6-004` SQLite identity/binding/open behavior.
- `E-A1.6-005` record OCC and separate-process race evidence.
- `E-A1.6-006` idempotency implementation.
- `E-A1.6-007` events/receipts provenance implementation.
- `E-A1.6-008` transaction/bulk safety.
- `E-A1.6-009` internal and user-schema migration contracts.
- `E-A1.6-010` backup/export/import implementation and tests.
- `E-A1.6-011` quarantine/recovery implementation.
- `E-A1.6-012` native extension registry locking/materialization/lifecycle.
- `E-A1.6-013` Bots/App authority narrowing and adversarial tests.
- `E-A1.6-014` Brain/Memory/Dashboard/Connections/Automation boundaries.
- `E-A1.6-015` public client scope validation and open path.
- `E-A1.6-016` exported structural `DataDatabaseScope` contract.
- `E-A1.6-017` secure-client wrapper preserves base scope without provenance branding.
- `E-A1.6-018` exact-head CI run `34864837334`.
- `E-A1.6-019` six exact-head cross-platform CI jobs.
- `E-A1.6-020` accepted component descriptor `189b1326…`.
- `E-A1.6-021` accepted-to-current comparison: 10 commits.
- `E-A1.6-022` current package/index version `0.1.0-alpha.0`.
- `E-A1.6-023` documented mutable GitHub install path.
- `E-A1.6-024` live pre-write ref/open-PR recheck.

## Verdict and progress

**AI-Verse-Data at `8edde7dca5afa34e300130cc6b8ee2b4170ad40f`: AUDIT COMPLETE, DOGFOOD BLOCKED.**

Data's core storage/reliability architecture is strong. The blocking standalone defect is the public trusted-scope provenance gap.

New findings:

1. `WSA-2026-020` HIGH trusted-scope provenance / workspace-path bypass.
2. `WSA-2026-021` LOW release/version/install identity drift.

No Data product repair is made during A1.6.

After acceptance:

- weighted audit: **17 / 100 = 17%**
- remaining: **83%**
- tracker tasks: **11 / 51 complete**, **40 / 51 remaining**
- phases: **1 / 7 complete**, **6 / 7 incomplete**
- A1 repositories: **6 / 14 complete**, **8 / 14 remaining**
- A1 weight: **12 / 28**
- next task: **A1.7 AI-Verse-Multiple-Bots**
