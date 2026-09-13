# AI-Verse Token Source Map

## Remote beta.2 source-of-truth closure

**Update date:** 2026-09-13

Canonical GitHub source now exists at `aiverse-filmmakers/ai-verse-token`.

Current immutable release evidence:

- package: `@ai-verse/token@0.1.0-beta.2`;
- main commit: `8b24891cd9c230e191b2637b6db2122b3dd9984d`;
- annotated tag: `v0.1.0-beta.2`;
- annotated tag object: `c860bd45f8f31c5d6d8f981ab848252cae047eb7`;
- tag target: `8b24891cd9c230e191b2637b6db2122b3dd9984d`;
- hosted CI run: `34776309959`;
- matrix result: 6/6 PASS across Ubuntu/macOS/Windows and Node 22/24.

Historical provenance remains intact: `artifact-0.1.0-alpha.1` retains the exact recovered audited alpha.1 baseline, and `v0.1.0-beta.1` remains immutable rather than being retagged after Windows CI exposed test-harness portability defects.


## Public-beta implementation evidence

**Update date:** 2026-09-13

The exact alpha.1 audit artifact was recovered and verified:

- source ZIP SHA-256: `4feb14ed9df2b82b7f4a07d571e77beda4afe695982e55b3dcfe0a7440588257`;
- packed alpha.1 TGZ SHA-256: `43545daa33922656889e4b5e4257e03f7ba7eaa573f13bc1cc361b938aa65abc`;
- package identity: `@ai-verse/token@0.1.0-alpha.1`;
- no `.git` metadata in the archive and no separate recoverable Git bundle.

A restored Git lineage was created without inventing history:

- `210ae2b3d12dc5ac9f10190d17a7652bfb0031cb`: untouched alpha.1 artifact import, tagged `artifact-0.1.0-alpha.1`;
- `1811d719b7ba47c9e68a78f5b9217751a6306faa`: public-beta operational implementation, tagged `v0.1.0-beta.1`.

Immutable beta.1 artifacts:

- source ZIP SHA-256: `d5fad270396ab317fdeece1330d45e09f75af5ca9bf4560cd7fd5fb563501773`;
- Git bundle SHA-256: `7cf04dbca22fcbf953219085b1222f89081586c93e173d6a39f3dbd0df0c7b24`;
- npm TGZ SHA-256: `6a9b51c22eba5a99d2e3c0433f86a890539a27b0359c2cfe3183e7d0af697567`.

New canonical implementation areas added in beta.1 include:

- `src/runtime/`: setup, source discovery, collector orchestration, collection, pricing sync, status and doctor;
- `src/pricing/transports.ts`: concrete bounded OpenRouter transport and generic Token-native HTTPS pricing manifest transport;
- `src/read/authorization.ts`: mandatory explicit owner/scoped read authority with immutable scope-floor enforcement;
- cost-aware `src/read/reader.ts` primary reads using Token pricing evidence and CostEngine;
- `src/gateway/`: host-authorized owner-backed Gateway usage projection;
- durable installed runtime materialization under the Token extension bundle;
- expanded query attribution dimensions and Multiple Bots Skill/system/agent attribution;
- `test/public-beta-runtime.test.mjs`: operational beta acceptance coverage.

Local verification after closure:

- TypeScript check: PASS;
- normal tests: **255/255**;
- release tests: **3/3**;
- clean packed install: PASS;
- package dry-run: PASS.

The six-leg GitHub Actions matrix remains configured for Ubuntu/macOS/Windows on Node 22 and 24. Hosted execution is pending creation/push of the canonical Token remote.

The original alpha.1 source map below remains useful historical archaeology and describes the pre-beta implementation state.


**Component:** AI-Verse Token  
**Audit date:** 2026-09-13  
**Audit method:** `docs/AUDIT-METHODOLOGY.md`  
**Reviewed source artifact:** local `AI-Verse-Token-hardened-alpha.1.zip`  
**Package:** `@ai-verse/token@0.1.0-alpha.1`  
**Exact reviewed artifact SHA-256:** `4feb14ed9df2b82b7f4a07d571e77beda4afe695982e55b3dcfe0a7440588257`  
**Ledger format:** 2  
**Git revision:** unavailable in the reviewed local archive. The archive contains no `.git` metadata and there is no AI-Verse-Token repository in the connected `aiverse-filmmakers` GitHub account. The archive digest is therefore the exact revision identifier for this audit.

## 1. Evidence hierarchy used

The audit applied the canonical hierarchy in this order:

1. current executable implementation under `src/`;
2. current acceptance tests under `test/` and local CI execution;
3. current JSON schemas;
4. architecture and protocol documents;
5. README and lifecycle documentation;
6. build/release/status documentation;
7. the alpha.1 hardening audit;
8. the older alpha.0 local archive for historical comparison;
9. inferred intent only where explicitly labeled.

No AI-Verse sibling implementation repository was used as evidence.

The only non-Token repository material read was the canonical AI-Verse-System audit methodology and living-system documentation required for the requested output/propagation step.

## 2. Repository inventory

Reviewed alpha.1 source snapshot contains approximately:

- 80 TypeScript files under `src/`;
- 26 test files;
- 39 Token documentation files;
- 2 JSON schemas;
- 1 GitHub Actions workflow;
- generated `dist/` output with 316 files;
- package/CLI/root metadata.

Approximate TypeScript source size: 11,453 lines.

### Canonical implementation

- `src/`
- `schemas/`
- `bin/ai-verse-token.mjs`
- `package.json`
- `tsconfig.json`

### Canonical architecture/contracts

- current protocol, pricing, cost, collector, time, lifecycle and integration docs under `docs/`;
- JSON schemas under `schemas/`.

### Tests and acceptance

- `test/`
- `.github/workflows/ci.yml`

### Generated material

- `dist/`

`dist/` is treated as build output derived from TypeScript source, not an independent architecture source.

### Historical/status material

- `docs/PHASE-1-STATUS.md`
- `docs/PHASE-2-STATUS.md`
- `docs/BUILD-MAP.md`
- `docs/HARDENING-AUDIT-2026-09-12.md`
- older local alpha.0 archive.

### Vendor/third-party code

No vendored source tree was found.

`THIRD-PARTY-NOTICES.md` states that implementation source is original and that external projects influenced behavior/contracts/design ideas rather than being copied into the package.

## 3. Root identity, build and distribution evidence

### `README.md`

Primary product framing and current release state.

Key evidence:

- Token is headless usage intelligence;
- first-release monetary truth is ACTUAL/CALCULATED/UNKNOWN;
- local and AI-Verse use are intended;
- Token owns telemetry ledger truth;
- Dashboard consumes a projection;
- current build state is 32/32;
- alpha.1 is a hardened release candidate;
- npm publication and hosted CI are not yet claimed as complete.

### `package.json`

Canonical package/distribution contract.

Important current facts:

- package: `@ai-verse/token`;
- version: `0.1.0-alpha.1`;
- runtime requirement: Node `>=22.5.0`;
- CLI: `ai-verse-token`;
- exact TypeScript dev dependency;
- public export map for protocol, storage, identity, query, pricing, cost, collectors, adapters, time, efficiency, read, export, MCP, native and AI-Verse integration adapters;
- package contents are built output plus notices/README;
- license field is `UNLICENSED`.

### `bin/ai-verse-token.mjs`

Thin executable entry to the built CLI implementation.

### `.github/workflows/ci.yml`

Declared cross-platform CI contract:

- Ubuntu + Node 22;
- Ubuntu + Node 24;
- macOS + Node 22;
- macOS + Node 24;
- Windows + Node 22;
- Windows + Node 24.

Each leg runs install, CI, pack dry-run and CLI help checks.

**Evidence limitation:** these hosted jobs are configured but were not run against a remote Token repository because no such remote repository currently exists.

## 4. Usage protocol evidence

### Canonical implementation

- `src/protocol/constants.ts`
- `src/protocol/types.ts`
- `src/protocol/validation.ts`
- `src/protocol/index.ts`

### Machine-readable contract

- `schemas/usage-event-v1.schema.json`

### Architecture documents

- `docs/PROTOCOL-V0.1.md`
- `docs/FIRST-RELEASE-SCOPE.md`

### Tests

- `test/protocol-validation.test.mjs`
- `test/package-foundation.test.mjs`
- `test/phase1-acceptance.test.mjs`

### Evidence established

The current protocol:

- separates observation runtime from billing platform and inference provider;
- preserves requested/resolved/provider model identities;
- includes workspace/project/agent/Bot/Worker/task/run/session attribution;
- supports detailed usage dimensions;
- supports exact timing;
- supports optional trusted actual charge;
- preserves provenance/source fingerprints;
- rejects unknown fields and malformed values;
- distinguishes missing/null/zero;
- structurally forbids prompt/response content storage by requiring `content_stored: false`.

## 5. Immutable ledger and query evidence

### Canonical implementation

- `src/storage/constants.ts`
- `src/storage/errors.ts`
- `src/storage/ledger.ts`
- `src/query/engine.ts`
- `src/query/types.ts`

### Architecture documents

- `docs/STORAGE-V0.1.md`
- `docs/QUERY-AND-AGGREGATES-V0.1.md`
- `docs/INGEST-AND-DEDUPE-V0.1.md`

### Tests

- `test/storage-ledger.test.mjs`
- `test/ingest-dedupe.test.mjs`
- `test/query-aggregate.test.mjs`
- `test/read-performance-baseline.test.mjs`

### Evidence established

Current alpha.1 ledger format is **2**.

Canonical tables include:

- `token_metadata`;
- `usage_events`;
- `event_correlations`;
- `event_supersessions`;
- `collector_checkpoints`.

SQLite triggers block UPDATE/DELETE of immutable event/correlation/supersession evidence.

The ledger validates schema definitions, metadata and integrity, rejects foreign nonempty databases and refuses unsafe final-path symlinks.

Queries exclude superseded observations by default.

Exact integer aggregation uses BigInt-safe handling.

### Documentation contradiction

`docs/STORAGE-V0.1.md` still documents ledger format/user version 1.

That prose is stale relative to alpha.1 implementation.

## 6. Identity evidence

### Canonical implementation

- `src/identity/resolver.ts`
- `src/identity/types.ts`

### Architecture document

- `docs/IDENTITY-RESOLUTION-V0.1.md`

### Test

- `test/identity-resolver.test.mjs`

### Evidence established

Only exact configured/effective-dated aliases authorize pricing identity.

Fuzzy/near-name matching cannot create monetary authority.

Ambiguous identity remains unpriceable instead of being guessed.

## 7. Pricing snapshot and source-authority evidence

### Canonical implementation

- `src/pricing/constants.ts`
- `src/pricing/types.ts`
- `src/pricing/validation.ts`
- `src/pricing/sources.ts`
- `src/pricing/store.ts`
- `src/pricing/sync.ts`

### Schema

- `schemas/price-snapshot-v1.schema.json`

### Architecture documents

- `docs/PRICE-SNAPSHOT-PROTOCOL-V0.1.md`
- `docs/PRICING-SOURCES-V0.1.md`
- `docs/PRICING-SYNC-V0.1.md`
- `docs/PRICING-TRUTH-MODEL.md`

### Tests

- `test/pricing-protocol.test.mjs`
- `test/pricing-source-registry.test.mjs`
- `test/pricing-sync.test.mjs`
- `test/phase2-pricing-acceptance.test.mjs`

### Evidence established

Pricing truth is kept in a separate Token-owned immutable price-snapshot store rather than the usage SQLite ledger.

The store:

- validates snapshots strictly;
- uses SHA-256-derived filenames;
- rejects unsafe symlink/path behavior;
- keeps append-only synchronization observations;
- preserves source/freshness/provenance evidence.

The synchronizer supports stale startup refresh, periodic refresh while active, unknown-model refresh, manual refresh, ETag/digest continuity and safe failed-refresh state.

### Important absence established

No concrete first-party network `PricingFetcher` implementation was found.

The current synchronizer therefore requires caller/host supplied fetchers or already available snapshot evidence.

## 8. ACTUAL / CALCULATED / UNKNOWN cost-law evidence

### Canonical implementation

- `src/cost/actual.ts`
- `src/cost/decimal.ts`
- `src/cost/engine.ts`
- `src/cost/types.ts`

### Architecture documents

- `docs/COST-ENGINE-V0.1.md`
- `docs/ACTUAL-COST-INGESTION-V0.1.md`
- `docs/PRICING-TRUTH-MODEL.md`

### Tests

- `test/cost-engine.test.mjs`
- `test/actual-cost-ingestion.test.mjs`
- `test/phase2-pricing-acceptance.test.mjs`

### Evidence established

The monetary truth law is runtime-enforced:

- trusted ACTUAL wins, including legitimate zero;
- CALCULATED requires exact authoritative usage, billing/model route and matching verified effective tariff;
- historical usage uses historical effective pricing;
- secondary catalogs cannot independently authorize CALCULATED;
- insufficient evidence returns UNKNOWN with no fake amount;
- monetary arithmetic is exact decimal/rational rather than floating point.

## 9. Collector evidence

### Collector framework

- `src/collectors/types.ts`
- `src/collectors/registry.ts`
- `src/collectors/runner.ts`
- `src/collectors/local-common.ts`

### Built-in passive collectors

- `src/collectors/hermes.ts`
- `src/collectors/claude-code.ts`
- `src/collectors/codex.ts`
- `src/collectors/opencode.ts`
- `src/collectors/gemini-cli.ts`
- `src/collectors/openclaw.ts`

### Architecture documents

- `docs/COLLECTOR-SDK-V0.1.md`
- `docs/HERMES-PASSIVE-COLLECTOR-V0.1.md`
- `docs/HERMES-INTEGRATION.md`
- `docs/LOCAL-AGENT-COLLECTORS-V0.1.md`

### Tests

- `test/collector-sdk.test.mjs`
- `test/hermes-collector.test.mjs`
- `test/local-agent-collectors.test.mjs`

### Evidence established

Collectors are bounded, passive and source-preserving.

CollectorRunner validates provenance/runtime expectations and advances checkpoints transactionally with accepted ingest.

Hermes/OpenCode database access is read-only.

### Important absence established

No production default collector registry/orchestrator was found that automatically composes and runs all built-in collectors after installation.

Recurring collection scheduling is explicitly outside the collector SDK.

## 10. Remote/provider adapter evidence

### Canonical implementation

- `src/adapters/openrouter.ts`
- `src/adapters/command-code.ts`
- `src/adapters/openai.ts`
- `src/adapters/anthropic.ts`
- `src/adapters/google-gemini.ts`
- `src/adapters/opentelemetry.ts`
- `src/adapters/gateways.ts`
- `src/adapters/common.ts`

### Architecture documents

- `docs/REMOTE-USAGE-ADAPTERS-V0.1.md`
- `docs/DIRECT-PROVIDER-ADAPTERS-V0.1.md`
- `docs/OTEL-GATEWAYS-DEDUPE-V0.1.md`

### Tests

- `test/remote-adapters.test.mjs`
- `test/direct-provider-adapters.test.mjs`
- `test/otel-gateway-dedupe.test.mjs`

### Evidence established

These are strict record/span normalizers.

They do not discover credentials or own provider network transport.

OpenTelemetry parsing intentionally avoids message/prompt/tool content.

Gateway estimated/computed cost is not silently promoted to ACTUAL.

### Important boundary

"Live ingest" and "OpenTelemetry ingest" are normalization interfaces, not a bundled daemon, OTLP receiver or gateway.

## 11. Deduplication and reconciliation evidence

### Canonical implementation

Primary implementation is in:

- `src/storage/ledger.ts`;
- collector/adapters that generate correlation keys;
- `src/correlation/index.ts`.

### Architecture document

- `docs/INGEST-AND-DEDUPE-V0.1.md`
- `docs/OTEL-GATEWAYS-DEDUPE-V0.1.md`

### Tests

- `test/ingest-dedupe.test.mjs`
- `test/otel-gateway-dedupe.test.mjs`

### Evidence established

Same-source replay protection uses stable exact identities.

Cross-source dedupe requires strong exact evidence.

Compatible duplicate observations can produce a derived canonical event plus append-only supersession records.

Raw source observations remain immutable.

Exact conflicts fail transactionally.

Weak time/model/token similarity is not treated as identity.

## 12. Time-engine evidence

### Canonical implementation

- `src/time/engine.ts`
- `src/time/types.ts`

### Architecture documents

- `docs/TIME-ENGINE-V0.1.md`
- `docs/TIME-METRICS.md`

### Test

- `test/time-engine.test.mjs`

### Evidence established

Token distinguishes:

- request wall time;
- TTFT;
- generation duration;
- output throughput;
- summed compute time;
- active wall time;
- overlap;
- peak and average concurrency;
- session span;
- exact idle time when justified.

Active wall time is calculated through interval union.

UTC hour/day rollups clip intervals at boundaries without duplicating request/token starts.

## 13. Efficiency and budget evidence

### Canonical implementation

- `src/efficiency/engine.ts`
- `src/efficiency/budgets.ts`
- `src/efficiency/types.ts`

### Architecture document

- `docs/EFFICIENCY-BUDGETS-V0.1.md`

### Test

- `test/efficiency-budgets.test.mjs`

### Evidence established

The package computes:

- completeness-aware token summaries;
- cache/reasoning efficiency;
- time coverage;
- cost coverage grouped by currency/truth;
- explicit retry tax;
- dimensional usage;
- request/token/time/cost budgets;
- quota-window status.

Missing evidence propagates to UNKNOWN where necessary.

No persistent scheduler/alerting/enforcement subsystem is implemented here.

## 14. Read, CLI, export and MCP evidence

### Canonical implementation

- `src/read/reader.ts`
- `src/read/types.ts`
- `src/export/exporter.ts`
- `src/mcp/read-only.ts`
- `src/cli.ts`

### Architecture document

- `docs/READ-EXPORT-MCP-V0.1.md`

### Test

- `test/read-export-mcp.test.mjs`

### Evidence established

Read surfaces are bounded and do not expose arbitrary SQL.

Agent-facing data is privacy-reduced by default.

### Important implementation gap

The primary TokenReader efficiency/read path currently rates only event-embedded ACTUAL charges and labels its cost scope `actual_only`.

No main read/CLI/MCP/Dashboard path was found that composes:

`PriceSnapshotStore -> CostEngine -> ACTUAL/CALCULATED/UNKNOWN read result`.

The cost engine therefore exists, but the main read UX does not yet expose its complete truth model.

## 15. AI-Verse ecosystem boundary evidence

### Shared helpers

- `src/ecosystem-common.ts`

### Dashboard

- `src/dashboard/index.ts`

### Brain

- `src/brain/index.ts`

### Memory

- `src/memory/index.ts`

### Data

- `src/data/index.ts`

### Multiple Bots

- `src/bots/index.ts`

### Connections

- `src/connections/index.ts`

### Skills/Automations correlation

- `src/correlation/index.ts`

### Architecture document

- `docs/AI-VERSE-ECOSYSTEM-ADAPTERS-V0.1.md`

### Test

- `test/ecosystem-adapters.test.mjs`

### Evidence established

The adapters preserve Token ownership:

- Dashboard receives projections, not the Token database;
- Brain receives bounded answers;
- Memory receives evidence/candidates with `auto_write: false`;
- Data projections explicitly retain Token authority and do not transfer ownership;
- Bot/Worker/TeamRun attribution cannot overwrite conflicting exact state;
- connection handles remain opaque and contain no secret material.

**System law derived:** telemetry attribution/projection is evidence, not transfer of canonical operational ownership.

## 16. Native AI-Verse lifecycle evidence

### Canonical implementation

- `src/native/constants.ts`
- `src/native/compatibility.ts`
- `src/native/paths.ts`
- `src/native/registry.ts`
- `src/native/materialization.ts`
- `src/native/lifecycle.ts`
- `src/native/doctor.ts`

### Architecture documents

- `docs/AI-VERSE-NATIVE-LIFECYCLE-V0.1.md`
- `docs/AI-VERSE-INTEGRATION.md`

### Tests

- `test/native-lifecycle.test.mjs`
- native portions of `test/release-acceptance.release.mjs`

### Evidence established

Native lifecycle:

- validates a compatible OS-v2-shaped root before writes;
- owns only Token's local extension registration/materialization;
- preserves sibling/unknown registry fields;
- uses atomic registry/materialization writes;
- uses an exclusive registry lock;
- rejects unsafe symlink/traversal states;
- supports install/update/enable/disable/uninstall/status/doctor;
- deliberately creates no telemetry ledger on install;
- preserves Token user state through uninstall/reinstall.

### Important operational gap

The generated installed `engine.mjs` is a metadata descriptor containing package/export/state metadata.

It is not a running collector/service engine and does not itself:

- import/run the Token package;
- initialize a ledger;
- start collectors;
- refresh pricing;
- expose MCP/RPC;
- activate provider hooks.

Therefore registered/enabled is not operationally ready.

### Lock-recovery limitation

The exclusive registry lock has no stale-lock recovery protocol after a process crash.

## 17. Release/build/current-progress evidence

### Build plan

- `docs/BUILD-MAP.md`

Current state: 32/32 tasks complete.

### Release acceptance

- `docs/PACKAGING-RELEASE-ACCEPTANCE-V0.1.md`
- `test/release-acceptance.release.mjs`

### Local verification performed during this audit

On Node 22.16.0:

- `npm run ci`: PASS;
- normal tests: 249/249 passed;
- release tests: 3/3 passed;
- total observed checks: 252;
- failures: 0;
- skipped: 0;
- cancelled: 0;
- `npm pack --dry-run`: PASS;
- dry-run package size approximately 185.7 kB;
- 320 package files.

### Acceptance limitation

Native release tests use a synthetic compatible host fixture.

They do not prove end-to-end activation against a real current AI-Verse OS installation.

## 18. Historical repair evidence

### Current hardening record

- `docs/HARDENING-AUDIT-2026-09-12.md`

It documents the alpha.0 to alpha.1 hardening work.

Major repair categories include:

- unknown-vs-zero aggregate truth;
- exact BigInt accumulation;
- context-sensitive pricing;
- exact ACTUAL monetary storage;
- dedupe attribution/conflict behavior;
- timing zero/monotonic correctness;
- trusted Hermes actual-cost qualification;
- Anthropic billable web-search units;
- SQLite schema-tamper resistance;
- pricing-store path/symlink/size hardening;
- native lifecycle rollback/lock/path hardening;
- privacy redaction;
- collector scalability;
- protocol/schema parity.

### Older local artifact

`AI-Verse-Token-first-release.zip` was inspected only for historical comparison.

It identifies package `0.1.0-alpha.0`.

The current alpha.1 artifact materially changes protocol/storage/pricing/cost/collectors/adapters/native/tests/docs and advances the ledger format from 1 to 2.

### History limitation

No Git commit/PR history is available for Token because the reviewed local archive contains no VCS metadata and no Token GitHub repository is accessible.

The hardening audit plus old/new archive comparison therefore serve as the available historical archaeology.

## 19. Inspiration/provenance evidence

### Primary documents

- `docs/RESEARCH-2026-09.md`
- `docs/REFERENCE-ADOPTION-MAP.md`
- `docs/SOURCE-REFERENCES.md`
- `THIRD-PARTY-NOTICES.md`

### Explicit primary references

- Tokscale;
- CodeBurn;
- ccusage;
- Pydantic genai-prices;
- Portkey Models;
- LiteLLM;
- OpenLIT;
- Langfuse;
- OpenMeter;
- Bifrost.

### Secondary references

- OpenLLMetry;
- Helicone;
- Hermes Agent.

The source map treats these as inspirations only where the Token repository itself records them.

## 20. Contradictions and documentation drift

### Storage version drift

`src/storage/constants.ts` and current alpha.1 ledger behavior use format 2.

`docs/STORAGE-V0.1.md` still describes format 1.

Classification: **stale documentation**.

### Architecture storage-boundary drift

`docs/ARCHITECTURE-BLUEPRINT.md` describes pricing snapshots, derived costs and bounded rollup/budget state as ledger-owned material.

Current implementation instead keeps price snapshots in a separate immutable Token pricing store and computes calculated cost/rollups/budgets as derived results.

Classification: **stale architecture wording**.

### Architecture status drift

`docs/ARCHITECTURE-BLUEPRINT.md` still says implementation is in progress while Build Map and README mark 32/32 first-release implementation work complete.

Classification: **stale status wording**.

### Read-path cost composition drift

README/product architecture implies ACTUAL/CALCULATED pricing flows into CLI/JSON/MCP/Dashboard.

Current TokenReader/CLI path exposes actual-only cost scope unless another caller explicitly invokes CostEngine.

Classification: **implementation gap plus over-broad product wording**.

### Doctor-depth drift

`docs/AI-VERSE-INTEGRATION.md` describes richer collector/pricing/cost health expectations than current native doctor implements.

Classification: **INTENDED behavior currently written near CURRENT integration prose**.

## 21. Negative-space search performed

Before recording meaningful absences, the audit searched source/docs/tests for likely implementations of:

- activate/adopt/reconcile;
- init/create-ledger user command;
- collect/discover/run/watch/daemon;
- pricing fetchers and network transport;
- CostEngine composition inside TokenReader/CLI/Dashboard/MCP;
- authorization/scoped-reader/ACL handling;
- stale-lock recovery;
- schema migration/rollback;
- real host activation acceptance.

No generic current implementation was found for the missing paths recorded in the component specification/QC.

## 22. Evidence limitations

1. **No Token Git revision:** exact revision is identified by archive SHA-256 instead.
2. **No Token PR/commit history:** historical reconstruction is limited to repository hardening records and alpha.0/alpha.1 artifact comparison.
3. **No hosted Token CI result:** the matrix exists, but only the local Node 22 gate was executed during this audit.
4. **No real AI-Verse OS integration acceptance:** native tests use a synthetic host fixture.
5. **No live pricing network acceptance:** no built-in concrete network pricing fetchers exist in the package.
6. **No production provider credential/network acceptance:** provider adapters normalize supplied records and intentionally do not own credentials/network transport.
7. **No current published npm/member artifact verification:** local TGZ packaging/install is proven; remote publication is not.
8. **Standalone library capability is stronger than standalone operator UX:** package APIs work independently, but no turnkey collector/bootstrap command exists.

These limitations are explicitly reflected as UNVERIFIED, PARTIAL or GAP rather than being inferred as complete.
