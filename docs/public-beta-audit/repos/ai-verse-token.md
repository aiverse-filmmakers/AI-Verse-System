# A1.8 - Independent Repository Audit: ai-verse-token

**Audit date:** 2026-09-15  
**Frozen ref:** `23b7b8ecbc9d9ef267f5e10449f785eb11107dd4`  
**System baseline:** `0699feb49b761feb5cd1826bcb535aa3c072e4a2`  
**Status:** COMPLETE  
**Standalone verdict:** DOGFOOD BLOCKED  
**R-a:** COMPLETE / PASS  
**R-b:** COMPLETE / MATERIAL FAILURES FOUND  
**R-c:** COMPLETE / BLOCKED  
**Findings:** `WSA-2026-024`, `WSA-2026-025`  
**Next:** A1.9 AI-Verse-Automations

## Independence and drift control

A1.8 used only the frozen Token repository, Token-owned tests/workflows, release/provenance records and GitHub metadata/history.

At task start and pre-write recheck:

- Token main remained exactly `23b7b8ecbc9d9ef267f5e10449f785eb11107dd4`;
- System main remained `0699feb49b761feb5cd1826bcb535aa3c072e4a2`;
- no open scoped PR existed;
- no Token product file was modified;
- Dashboard MC1.4 remained paused.

The frozen Token tree contains **196 tracked entries**.

## Reconstructed ownership

AI-Verse Token is the canonical telemetry/cost owner for:

- normalized immutable usage observations;
- provider/runtime/model identity needed for attribution;
- request/session timing evidence;
- immutable effective-dated pricing snapshots;
- trusted ACTUAL charge evidence;
- CALCULATED/UNKNOWN cost truth;
- bounded rollups, query and efficiency projections;
- collector checkpoints and dedupe/correlation evidence;
- Token-native operational budgets/efficiency metrics.

It does not own:

- prompts or response content;
- OS workspace truth;
- Memory narrative state;
- Brain goals or strategic direction;
- Skills packages;
- Bot coordination;
- Connections credentials;
- Automations scheduling;
- Dashboard canonical state;
- invoice reconciliation or private financial accounting.

## Truth model

Token exposes only:

- `ACTUAL`: trusted provider/runtime supplied a real charge;
- `CALCULATED`: authoritative usage rated against a matching verified tariff;
- `UNKNOWN`: insufficient evidence.

Important verified laws:

- missing money is never converted to zero;
- a real zero charge stays ACTUAL zero;
- estimated usage cannot authorize calculated money;
- ambiguous model/route identity fails closed;
- stale current pricing cannot authorize calculated money;
- secondary catalogs cannot authorize calculated money;
- historical usage resolves historical effective tariffs;
- actual charge takes precedence over calculation;
- currencies are retained rather than silently mixed.

## Canonical usage ledger

The first-release ledger is SQLite format 2.

Required identity includes:

- application id `AVTK`;
- user version 2;
- `ai-verse-token/sqlite` metadata;
- protocol `ai-verse-token/0.1`.

Connection safety includes:

- WAL;
- foreign keys;
- trusted schema off;
- recursive triggers;
- bounded busy timeout;
- synchronous FULL;
- read-only `query_only`;
- quick integrity check on every open.

The schema has no prompt/response/credential columns.

Canonical usage rows are immutable through SQLite triggers.

Correlation and supersession rows are append-only.

Unknown/foreign databases are never silently adopted.

## Ingest, replay and exact correlation

Canonical ingest:

- strictly validates usage events;
- preserves zero versus missing;
- dedupes exact event replay;
- dedupes same collector/source fingerprint when semantic source facts match;
- rejects reused fingerprints with changed source facts;
- rejects same event ID with changed canonical data;
- writes event, correlation keys and checkpoint in one `BEGIN IMMEDIATE` transaction;
- performs exact cross-source correlation without deleting raw evidence;
- uses append-only supersession links for queryable canonical heads.

Exact correlated observations fail closed when exact scope, charge or identity facts conflict.

No fuzzy/time-similarity-only dedupe authority was found.

## Collector SDK

Collectors register:

- stable ID;
- version;
- allowed runtime scope.

The runner enforces:

- exact collector ID in provenance;
- exact collector version when supplied;
- runtime is inside collector registration;
- bounded checkpoint cursor;
- bounded event count.

Concrete local collectors include Hermes, Claude Code, Codex, OpenCode, Gemini CLI and OpenClaw.

Supported local databases/files are handled read-only where applicable.

The collector boundary contains one material monetary-authority defect under `WSA-2026-024`.

## Identity resolution

Runtime, billing platform, inference provider, requested model, resolved model and provider-native ID stay separate.

Model aliases are exact and declarative.

Overlapping/conflicting exact evidence becomes ambiguous.

No fuzzy/prefix/typo model match can authorize pricing.

## Pricing authority

Pricing snapshots are immutable effective-dated facts.

Snapshot authority is restricted to registered source classes.

Fetched payloads cannot choose their own registered source ID or authority because the synchronizer stamps those from the trusted source registry.

Same-day freshness is enforced for current calculated cost where required.

A not-modified refresh can renew freshness only when ETag/content-digest continuity matches the immutable snapshot.

Fetch errors persist stable error codes without storing raw exception/credential text.

The pricing store rejects:

- symlinked store roots;
- unsafe snapshot/state nodes;
- oversized files;
- same snapshot ID with conflicting content;
- malformed sync-state records.

Cross-process batch failure atomicity remains incomplete under `WSA-2026-025`.

## ACTUAL-cost source registry

The explicit actual-cost registry is well designed in isolation.

Built-in trusted first-release sources include:

- OpenRouter Generation API as provider-reported for OpenRouter;
- Hermes state DB as runtime-reported for Hermes;
- Command Code usage API for Command Code.

The registry:

- rejects unknown source IDs;
- constrains provider sources to registered billing platforms;
- constrains runtime sources to registered runtimes;
- preserves exact decimal money/currency;
- treats exact replay as idempotent;
- rejects replacing an existing different actual charge.

OpenRouter/Hermes concrete adapters use this registry.

However the canonical ledger/collector boundary does not require all actual charges to pass through it. See `WSA-2026-024`.

## Read authorization and privacy

Token's read surfaces require an authorization envelope.

The envelope is explicitly supplied by the outer host; Token does not claim to authenticate that principal itself.

For scoped readers, Token imposes an immutable exact filter floor across dimensions such as workspace, Bot, Worker, Skill, automation, run, task and session.

A requested conflicting scope fails closed.

Gateway projection is read-only and requires the host authorization envelope.

Default JSON/Gateway/MCP projections remove raw source record IDs, source fingerprints and provider external-charge IDs.

Raw provenance export requires explicit opt-in.

MCP is bounded and read-only.

## Native lifecycle

Native Token lifecycle is strongly bounded.

Host compatibility requires:

- OS schema major 2;
- unified-workspace architecture;
- real non-symlink host control files/directories.

Token owns only its local extension entry, runtime bundle and Token state.

Filesystem controls include:

- fixed repository-relative paths;
- selected root must be a real directory;
- traversal/absolute/NUL rejection;
- symlink rejection for host and extension path components;
- exclusive registry lock;
- in-lock registry re-read;
- raw-text lost-update detection;
- atomic same-directory rename.

Install creates no telemetry ledger.

Setup initializes Token state.

Disable/update/uninstall preserve canonical ledger, runtime config and pricing state.

Doctor opens existing state read-only and does not silently repair pricing/ledger state.

## C-A1.8-001 - collector/canonical ingest can assert ACTUAL without trusted actual-cost source proof

**Source A:** Token truth law says ACTUAL requires a trusted provider/runtime real charge, and the collector SDK explicitly says collectors do not gain pricing truth or convert estimated cost into ACTUAL.

**Source B:** `validateUsageEvent` accepts any syntactically valid `actual_charge` whose `source` is one of the closed enum values. `CollectorRunner` validates collector identity/runtime but does not verify actual-charge source authority. `TokenLedger.ingestUsageEvent` then persists the event directly.

**Source C:** `CostEngine` returns attached actual charge as ACTUAL before tariff calculation.

**Higher-authority source:** executable protocol validation, collector runner, ledger and cost engine.

**Finding:** `WSA-2026-024`.

## WSA-2026-024 - ACTUAL monetary truth can bypass the trusted actual-cost source registry

**Severity:** HIGH  
**Confidence:** PROVEN  
**State:** OPEN  
**Root area:** canonical cost truth / trusted source enforcement  
**Affected repo:** `ai-verse-token`

### Summary

The repository includes a correct trusted actual-cost registry, but that registry is not mandatory at the canonical ingest boundary.

A collector or direct storage caller can submit a usage event that already contains an `actual_charge` marked provider- or runtime-reported.

The normal protocol validator verifies shape, decimal money, currency and enum value, but not which trusted source produced that charge.

CollectorRunner verifies collector identity/version/runtime but does not strip or re-verify `actual_charge`.

The ledger persists the event.

The cost engine then labels that charge `ACTUAL`.

### Impact

A buggy or over-privileged collector can elevate untrusted monetary data into canonical ACTUAL truth without passing the source registry that Token itself defines as the trusted monetary boundary.

This violates Token's most important accounting rule.

### Required closure evidence

After repair authorization:

- make canonical ACTUAL admission require verifiable trusted-source evidence;
- either remove direct actual-charge authority from generic collector emissions or bind it to collector/source registration;
- prevent plain `ingestUsageEvent` from creating ACTUAL truth unless a trusted ingestion token/registry result is supplied;
- preserve concrete OpenRouter/Hermes trusted adapters;
- add tests proving an arbitrary collector/direct ledger caller cannot self-assert ACTUAL while registered trusted sources still work.

## C-A1.8-002 - failed pricing refresh can leave a partial snapshot batch committed

**Source A:** pricing-sync contract describes an updated source response as storing the new immutable snapshots plus source-check observation, while failed/invalid refreshes retain prior successful state.

**Source B:** `PriceSnapshotStore.putMany` validates the whole batch first but then creates individual immutable snapshot files sequentially without a transaction, staging directory or batch commit marker.

**Source C:** if a later write fails or races with conflicting content after earlier new files were created, `putMany` throws; `PricingSynchronizer` records the refresh as failed, but previously created snapshot files are not rolled back.

**Higher-authority source:** executable pricing store/synchronizer.

**Finding:** `WSA-2026-025`.

## WSA-2026-025 - failed pricing synchronization is not failure-atomic across an immutable snapshot batch

**Severity:** MEDIUM  
**Confidence:** PROVEN  
**State:** OPEN  
**Root area:** pricing evidence transactionality / concurrency  
**Affected repo:** `ai-verse-token`

### Summary

Normal invalid batches are prevalidated and therefore insert nothing, which current tests cover.

But after validation, individual files are committed one by one.

A cross-process race or later filesystem failure can happen after one or more new snapshots have already been persisted.

The synchronizer catches the later failure and records the source refresh as failed, but does not remove the earlier files.

Because immutable snapshots can be read directly by the pricing/cost engine, a subset of a failed source response can become usable pricing evidence.

### Impact

A refresh reported as failed can still change the set of tariffs available for CALCULATED money.

This requires an I/O/concurrency failure after validation, so severity is MEDIUM rather than HIGH.

### Required closure evidence

After repair authorization:

- make one fetched snapshot batch failure-atomic;
- stage the complete batch before visibility or use a durable batch commit manifest;
- ensure a failed refresh leaves no newly visible authoritative snapshots from that response;
- support cross-process writers safely;
- add deterministic fault/race tests where a later snapshot write fails after earlier staged members.

## Exact-head CI

Frozen Token head:

`23b7b8ecbc9d9ef267f5e10449f785eb11107dd4`

CI run:

`34778240376` - **SUCCESS**

All six jobs executed and passed:

- macOS Node 22: `103780261556`
- macOS Node 24: `103780261632`
- Windows Node 22: `103780261661`
- Ubuntu Node 24: `103780261711`
- Ubuntu Node 22: `103780261713`
- Windows Node 24: `103780261759`

Each leg executed:

- checkout;
- Node setup;
- dependency install;
- TypeScript check/full tests;
- release acceptance;
- npm pack dry-run;
- CLI help smoke.

This is real executed cross-platform evidence.

## Release/provenance status

Token is unusual among the repos because its lost historical Git chain is explicitly documented.

The repository was restored from an exact audited alpha.1 source artifact and does not fabricate historical Git lineage.

Immutable tags exist for:

- alpha.1;
- beta.1;
- beta.2.

Frozen current head is explicitly beta.3:

`@ai-verse/token@0.1.0-beta.3`

The beta.3 changes are documented as the read-only pricing-store readiness correction and associated package/version/release evidence updates.

Frozen current-head CI passes the required six-leg hosted matrix.

A1.8 does not open a standalone missing-beta.3-tag finding. Tag/sealing/publication truth is an A5 release-evidence concern.

## Negative-space checks

A1.8 found no evidence that Token:

- stores prompt or response content in canonical usage rows;
- stores provider credentials in telemetry rows;
- treats telemetry attribution IDs as permission;
- fuzzy-matches models for pricing;
- represents UNKNOWN cost as zero;
- lets secondary price catalogs authorize CALCULATED;
- lets fetched pricing payloads self-promote source authority;
- silently reprices historical usage with today's tariff;
- silently rewrites immutable usage events;
- silently deletes raw evidence during dedupe;
- directly opens sibling canonical databases as competing owner state;
- takes Memory/Brain/Bots/Skills/Connections/Automations ownership;
- gives Dashboard direct canonical write authority;
- silently repairs incompatible/corrupt ledger state during read-only doctor;
- deletes Token user state during uninstall;
- steals the native extension registry lock.

## Evidence limitations

- A1.8 does not independently validate sibling implementations.
- Host authorization envelopes are trusted inputs by explicit Token contract; cross-component authentication belongs to A2.
- Invoice reconciliation, contract tariffs, credits and FX accounting are explicitly deferred and are not treated as missing first-release functionality.
- The pricing batch finding is code-proven from visible sequential commit behavior; no product fault-injection patch/test was added during the read-only audit.
- Release tag/publication sealing belongs to A5.

## Evidence IDs

- `E-A1.8-001` frozen Token tree/repository metadata.
- `E-A1.8-002` README/package/provenance identity.
- `E-A1.8-003` architecture/ownership reconstruction.
- `E-A1.8-004` usage protocol and validation.
- `E-A1.8-005` immutable ledger schema/triggers.
- `E-A1.8-006` ingest/dedupe/checkpoint transaction.
- `E-A1.8-007` collector SDK and runner enforcement.
- `E-A1.8-008` actual-cost registry and built-in trusted sources.
- `E-A1.8-009` direct-provider/Hermes actual-cost adapters.
- `E-A1.8-010` cost engine ACTUAL/CALCULATED/UNKNOWN precedence.
- `E-A1.8-011` pricing source registry and source assessment.
- `E-A1.8-012` pricing synchronizer trusted-source stamping/freshness.
- `E-A1.8-013` pricing immutable store and batch writes.
- `E-A1.8-014` identity resolver exact-match behavior.
- `E-A1.8-015` read authorization/filter-floor implementation.
- `E-A1.8-016` privacy-safe read/export/MCP surfaces.
- `E-A1.8-017` native filesystem/registry/lifecycle controls.
- `E-A1.8-018` public-beta runtime setup/doctor behavior.
- `E-A1.8-019` hardening audit provenance.
- `E-A1.8-020` exact-head CI run `34778240376`.
- `E-A1.8-021` six exact-head successful CI jobs.
- `E-A1.8-022` release acceptance packed-artifact tests.
- `E-A1.8-023` alpha.1/beta.1/beta.2 tag lineage evidence.
- `E-A1.8-024` beta.3 current-head provenance/version records.
- `E-A1.8-025` live pre-write ref/open-PR recheck.

## Verdict and progress

**ai-verse-token at `23b7b8ecbc9d9ef267f5e10449f785eb11107dd4`: AUDIT COMPLETE, DOGFOOD BLOCKED.**

New findings:

1. `WSA-2026-024` HIGH - ACTUAL truth can bypass trusted actual-cost source enforcement.
2. `WSA-2026-025` MEDIUM - failed pricing-sync batches are not cross-process failure-atomic.

No Token product repair is made during A1.8.

After acceptance:

- weighted audit: **21 / 100 = 21%**
- remaining: **79%**
- tasks: **13 / 51 complete**
- tasks remaining: **38 / 51**
- phases fully complete: **1 / 7**
- phases incomplete: **6 / 7**
- A1 repositories: **8 / 14 complete**
- A1 repositories remaining: **6 / 14**
- A1 weight: **16 / 28**
- next task: **A1.9 AI-Verse-Automations**
