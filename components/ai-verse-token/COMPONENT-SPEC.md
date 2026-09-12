# AI-Verse Token Component Specification

**Component:** AI-Verse Token  
**Package:** @ai-verse/token  
**Reviewed local package:** 0.1.0-alpha.1  
**Reviewed hardened archive SHA-256:** 4feb14ed9df2b82b7f4a07d571e77beda4afe695982e55b3dcfe0a7440588257  
**Review date:** 2026-09-13  
**Audit method:** docs/AUDIT-METHODOLOGY.md  
**Repository evidence source:** local hardened source archive AI-Verse-Token-hardened-alpha.1.zip  
**Git revision:** unavailable. The reviewed archive contains no .git metadata and no AI-Verse-Token remote repository exists in the connected aiverse-filmmakers GitHub account. The archive SHA-256 is therefore the exact point-in-time revision identifier for this audit.

## 1. Executive identity

**CURRENT**

AI-Verse Token is a headless, privacy-minimal usage intelligence and cost-truth engine for LLM calls, agents, coding assistants, gateways and AI operating systems.

Its strongest current capabilities are:

- strict runtime-neutral usage-event normalization;
- an immutable SQLite telemetry ledger;
- exact same-source idempotency and conservative cross-source deduplication;
- separate runtime, billing-platform, provider and model identity;
- immutable effective-dated pricing evidence;
- strict ACTUAL / CALCULATED / UNKNOWN monetary truth;
- passive local collectors and remote normalization adapters;
- concurrency-correct time analysis;
- efficiency and conservative budget calculations;
- bounded read, export, MCP and AI-Verse ecosystem projection surfaces;
- ownership-safe AI-Verse OS extension registration and uninstall/reinstall state preservation.

The core accounting/telemetry engine is real and well tested.

**CURRENT TARGET VERDICT**

The repository does satisfy its own self-defined internal "first-release implementation gate": Build Map 32/32 is complete, the hardened alpha.1 local release suite passes, and the package can be packed and clean-installed.

It does **not** yet satisfy the broader AI-Verse current product requirement of "install/activate and then work perfectly like a glove." The missing work is primarily operational composition and host adoption, not basic accounting correctness.

The most important missing current product paths are:

1. installed/enabled does not activate collection or expose a running Token service;
2. the installed engine.mjs is a metadata descriptor, not an operational engine;
3. there is no standalone first-run command that initializes a ledger and runs the built-in collectors;
4. there are no concrete pricing network fetchers, so fresh pricing requires caller-supplied fetchers/snapshots;
5. the public read/CLI/Dashboard path does not compose the CALCULATED cost engine, and read efficiency explicitly uses actual charges only;
6. doctor does not prove collector health, pricing freshness, cost-truth readiness or provider transport readiness;
7. read surfaces are bounded but not authorization-scoped by a host permission floor;
8. real AI-Verse OS end-to-end activation has not been acceptance-tested from this repository;
9. hosted cross-platform CI and npm/member distribution have not run because Token has no remote repository/publication.

## 2. Status vocabulary

This specification uses:

- **CURRENT**: present in the reviewed alpha.1 implementation and supported by tests/code.
- **INTENDED**: accepted desired behavior, but not fully implemented.
- **GAP**: required behavior absent, partial or unverified.
- **LAW**: invariant that must remain true as the system evolves.
- **HISTORICAL**: prior state/repair retained as architectural provenance.
- **INSPIRATION**: evidenced reference project or external design source.

## 3. Role in the complete system

**CURRENT**

Token is the canonical owner of AI usage telemetry evidence and Token-specific pricing evidence.

It is not a second OS, a second Data database, a second Memory system, a billing gateway, a credential manager, a scheduler or a Dashboard database.

Its correct place in the system is:

source runtimes / provider records / telemetry
-> Token collectors or adapters
-> canonical Token usage observations
-> Token identity/dedupe/pricing/time/efficiency logic
-> bounded read projections/references
-> Dashboard, Brain, Data, Memory, Bots and other consumers

**LAW**

Telemetry may inform operational decisions, but telemetry must not silently become canonical operational state belonging to another component.

Examples:

- a Token workspace_id is an attribution observation, not canonical proof that a workspace exists or that a caller is authorized to access it;
- a Token bot_id is usage attribution, not canonical Bot membership or authority;
- a Token Data projection is evidence/read material, not a transfer of structured-data ownership;
- a Memory candidate derived from Token is a proposal/evidence reference, not automatic Memory truth;
- a Dashboard display is a projection, not a second Token ledger;
- Brain may reason from Token, but does not own or rewrite Token telemetry.

## 4. Problem the component solves

Without Token, AI usage and cost evidence is fragmented across:

- local coding-agent histories;
- Hermes databases;
- direct provider response usage;
- OpenRouter/Command Code records;
- gateway logs;
- OpenTelemetry spans;
- different model aliases and billing routes;
- mutable/current-only pricing references;
- overlapping duplicate observations;
- incompatible timing semantics.

Token's job is to normalize these into traceable, conservative telemetry without pretending uncertain evidence is exact.

Its first-release cost promise is intentionally narrower than financial reconciliation.

## 5. Current architecture

### 5.1 Protocol layer

**CURRENT**

Protocol version: ai-verse-token/0.1.

The canonical UsageEvent separates:

- observation source/runtime;
- billing platform;
- inference provider;
- requested model;
- resolved model;
- provider model ID;
- scope/attribution IDs;
- usage categories;
- request timing;
- optional trusted actual charge;
- provenance and source fingerprint.

Unknown, explicit null and real zero are intentionally distinct.

Prompt/response content is structurally excluded by requiring content_stored to be false.

### 5.2 Immutable usage ledger

**CURRENT**

The first storage driver is SQLite through Node's built-in node:sqlite.

Hardened alpha.1 uses ledger format version 2.

Core schema includes:

- token_metadata;
- usage_events;
- event_correlations;
- event_supersessions;
- collector_checkpoints;
- bounded indexes for common query dimensions.

Raw usage observations are protected by SQLite UPDATE/DELETE rejection triggers.

Correlation and supersession records are append-only.

Collector checkpoints are mutable Token-owned operational state and are transactionally advanced with ingest decisions.

### 5.3 Identity resolver

**CURRENT**

Identity resolution keeps separate:

- runtime;
- billing platform;
- inference provider;
- requested model;
- resolved model;
- provider model ID;
- service tier;
- region;
- billing mode.

Only exact, configured, effective-dated aliases may authorize pricing identity.

Fuzzy, near-name and typo matching do not authorize money.

### 5.4 Pricing evidence

**CURRENT**

Pricing is not stored in the usage SQLite ledger in the current implementation.

PriceSnapshotStore owns a separate Token pricing directory:

- immutable validated pricing snapshots;
- append-only sync-state observations.

Snapshot filenames are SHA-256 derived from snapshot identity so untrusted model/provider text does not become a filesystem path.

Trusted source identity and authority come from host configuration, not fetched payload self-declaration.

### 5.5 Pricing synchronization engine

**CURRENT**

PricingSynchronizer implements:

- stale startup refresh;
- periodic refresh while a process is active;
- forced unknown-model refresh;
- manual refresh through the library API;
- ETag/content-digest continuity;
- not-modified freshness evidence;
- safe failure state;
- immutable snapshot history.

**GAP**

The package does not ship concrete network PricingFetcher implementations for the declared official/secondary sources.

The synchronizer is therefore a trusted synchronization framework, not an out-of-the-box pricing network client.

### 5.6 Cost engine

**CURRENT**

CostEngine returns exactly one of:

- ACTUAL;
- CALCULATED;
- UNKNOWN.

ACTUAL has strict precedence and includes a legitimate zero-dollar charge.

CALCULATED requires authoritative usage, exact billing route/model identity, event-time matching, sufficient tariff dimensions and authoritative verified pricing.

Historical events use historical effective tariffs.

Secondary catalogs cannot independently authorize CALCULATED money.

Money uses exact decimal/rational arithmetic rather than floating-point tariff multiplication.

### 5.7 Collectors

**CURRENT**

Built-in collectors exist for:

- Hermes;
- Claude Code;
- Codex;
- OpenCode;
- Gemini CLI;
- OpenClaw.

CollectorRunner provides:

- bounded scans;
- source detection;
- health status;
- checkpoint delivery;
- provenance/runtime enforcement;
- transactional ingest/checkpoint advancement.

Local source discovery is explicit and path-bounded.

Hermes and OpenCode database paths are read-only.

**GAP**

There is no production default collector registry/orchestrator that discovers all built-in sources and runs them after installation.

The built-in collectors are reusable library components. They are not yet an activated product runtime.

### 5.8 Remote/provider adapters

**CURRENT**

Strict normalizers exist for:

- OpenRouter generation metadata;
- Command Code usage records/windows;
- OpenAI Responses usage;
- Anthropic Messages usage;
- Google Gemini usage;
- OpenTelemetry GenAI spans;
- LiteLLM logs;
- Bifrost logs;
- generic OpenAI-compatible gateway records.

These adapters do not discover credentials or make provider network calls. That is intentionally outside their ownership.

**GAP**

"Live ingest" and "OpenTelemetry-compatible ingest" currently mean normalization APIs, not a bundled OTLP receiver, daemon, gateway or network service.

### 5.9 Cross-source deduplication

**CURRENT**

Token distinguishes raw observations from the underlying call.

Same-source idempotency uses:

- event_id;
- collector_id + source_record_fingerprint.

Cross-source dedupe uses strong exact correlations only.

Strongly correlated compatible observations produce an append-only derived canonical event plus supersession relationships.

Raw source observations remain immutable evidence.

Normal queries exclude superseded observations to prevent double counting.

Weak similarity such as same trace, close time, model similarity or token similarity does not authorize dedupe.

Conflicting exact facts fail closed transactionally.

### 5.10 Time engine

**CURRENT**

The time engine distinguishes:

- request wall time;
- TTFT;
- generation duration;
- output throughput;
- summed compute time;
- active wall time;
- overlap;
- peak/average concurrency;
- session span;
- exact idle time only when justified.

Active wall time is an interval union, so parallel calls are not incorrectly summed as wall-clock time.

Hour/day rollups clip long intervals at UTC bucket boundaries without duplicating request/token counts.

### 5.11 Efficiency and budgets

**CURRENT**

Efficiency APIs provide:

- exact/lower-bound token summaries;
- cache ratio;
- reasoning share;
- time coverage;
- cost coverage by currency/truth;
- explicit retry tax;
- dimensional grouping;
- conservative request/token/time/cost budgets;
- quota-window evaluation.

Budget results are OK, WARNING, EXCEEDED or UNKNOWN.

Missing data cannot create optimistic remaining capacity.

Currencies are never silently mixed.

**CURRENT BOUNDARY**

Budget definitions/evaluations are computation APIs. Token does not currently persist canonical budget policy, run a scheduler, send alerts or enforce provider routing.

### 5.12 Read surfaces

**CURRENT**

Read surfaces include:

- TokenReader;
- CLI summary/query/export;
- JSON/CSV export;
- read-only MCP;
- Dashboard projection;
- Brain adapter;
- Data references/projections;
- Memory evidence/candidates.

Read paths are bounded and reject arbitrary SQL.

Agent-facing projections redact source forensic identifiers by default.

**GAP**

TokenReader.efficiency explicitly has cost_scope = actual_only.

The public read/CLI/Dashboard path does not load the pricing store and rate canonical events through CostEngine.

Therefore the core cost engine can return CALCULATED/UNKNOWN when explicitly called, but the main read path cannot yet answer the README's complete "What did it cost, and is it ACTUAL, CALCULATED or UNKNOWN?" promise end to end.

## 6. Canonical ownership

### 6.1 Token-owned canonical state

**CURRENT / LAW**

Token owns:

1. canonical validated raw usage observations;
2. exact Token event identities and source fingerprints;
3. append-only correlation evidence;
4. append-only supersession relationships;
5. collector checkpoints for Token collection progress;
6. Token ledger format metadata;
7. immutable price snapshots;
8. append-only price-source synchronization observations;
9. trusted Token source-registry configuration supplied by the host/process;
10. direct trusted actual charges attached to canonical events when evidence meets the actual-cost source rules.

### 6.2 Token-owned derived results

**CURRENT**

The following are Token-derived outputs, not separate editable canonical stores in alpha.1:

- CALCULATED cost results;
- UNKNOWN cost results/reasons;
- query aggregates;
- time rollups;
- concurrency metrics;
- efficiency metrics;
- budget evaluations;
- Dashboard projections;
- Brain answers;
- Data projections;
- Memory candidates.

**LAW**

Derived results may be cached later, but a cache/index/projection must never become an independent editable authority that can diverge from Token's canonical evidence.

## 7. Explicit non-ownership

**LAW**

Token must never become canonical owner of:

- prompts/responses or conversation content;
- AI-Verse workspace/project definitions;
- user/agent identity and access-control policy;
- Memory's canonical memory;
- Data's operational structured records;
- Brain goals/strategy/direction;
- Multiple Bots team/bot lifecycle or authority;
- Skill definitions/capabilities;
- Automation scheduler ownership;
- provider credentials/secrets;
- connection definitions;
- provider routing policy;
- invoices/taxes/accounting reconciliation in first release;
- Dashboard UI state.

## 8. Sources of truth

| Responsibility | Current source of truth | Classification |
|---|---|---|
| Usage observation | usage_events plus protocol validation | Canonical |
| Source idempotency | event_id and collector/source fingerprint | Canonical |
| Cross-source relationship | event_correlations | Canonical evidence |
| Queryable merged call | derived canonical event plus event_supersessions | Canonical Token query representation, raw evidence retained |
| Collector progress | collector_checkpoints | Token operational state |
| Pricing tariff evidence | immutable PriceSnapshotStore files | Canonical Token pricing evidence |
| Pricing refresh evidence | append-only sync-state files | Canonical Token pricing evidence |
| Trusted pricing source definitions | process/host PricingSourceRegistry | Trusted configuration |
| Actual charge | validated event.actual_charge | Canonical observed monetary fact |
| Calculated cost | CostEngine result from event + price evidence | Derived |
| Time/efficiency/budget result | pure/bounded analysis APIs | Derived |
| Dashboard/Brain/Data/Memory views | Token projection/reference adapters | Derived/non-owning |

## 9. Runtime model

### 9.1 Standalone library

**CURRENT**

The package can be clean-installed and imported without AI-Verse OS.

A caller can:

- create/open a ledger;
- discover a source;
- construct a collector registry/runner;
- ingest events;
- supply pricing snapshots/fetchers;
- rate events;
- read/export/analyze results.

### 9.2 Standalone product experience

**GAP**

There is no turnkey standalone lifecycle such as:

- init;
- collect;
- ingest;
- discover;
- run;
- prices sync;
- serve;
- doctor --db;
- background/watch mode.

Current CLI read commands require an already-created database.

Current native lifecycle commands require an AI-Verse OS root.

So "standalone works" is true at the package/library level, not yet at the no-code operator product level.

### 9.3 AI-Verse native extension

**CURRENT**

Native lifecycle writes only:

- Token's own local extension registry entry;
- Token INSTRUCTIONS.md;
- Token engine.mjs;
- Token extension.json.

It deliberately creates no telemetry ledger on install.

User state under the Token state path survives uninstall.

**GAP**

The materialized engine.mjs exports metadata only:

- extension ID/version;
- package name;
- read export name;
- Dashboard export name;
- ledger relative path.

It does not execute collection, create a ledger, start pricing refresh, expose RPC/MCP, register runtime hooks or provide an activation handshake.

## 10. Scope and isolation

### 10.1 Attribution scope

**CURRENT**

UsageEvent supports opaque attribution dimensions including:

- system;
- workspace;
- project;
- agent;
- Bot;
- Worker;
- Skill;
- automation;
- tool;
- task/run/session IDs.

Multiple Bots and generic correlation adapters use exact conflict detection so trusted enrichment cannot silently overwrite existing exact attribution.

### 10.2 Attribution is not authority

**LAW**

Token scope labels are telemetry attributes.

They are not proof of:

- workspace existence;
- workspace membership;
- permission;
- execution authority;
- Bot authority;
- strategic authority.

### 10.3 Read authorization

**GAP**

Token's read APIs are bounded, but they do not carry a host authorization envelope or immutable scope floor.

An MCP/Brain/Dashboard caller with a reader can submit a workspace/project filter of its choosing or omit a scope filter and read all accessible ledger telemetry.

For a seamless multi-workspace AI-Verse host, the outer host/adapter must intersect requested filters with caller authorization, or Token needs a host-facing scoped-reader contract.

Token should not become the account/permission owner, but the effect boundary must not rely on voluntary filtering.

## 11. Current lifecycle

### Install/package

**CURRENT**

Local TGZ clean installation is acceptance-tested.

Intended future member path after npm publication:

npx @ai-verse/token install --root <os-root>

### Attach/register

**CURRENT WITH LIMITATIONS**

install/update validate an AI-Verse OS v2 fixture and write the local extension registry entry idempotently.

Unknown registry fields and sibling entries are preserved.

**LIMITATION**

Acceptance uses a synthetic Token-owned OS fixture, not a real checked-out AI-Verse OS member path.

### Enable/disable

**CURRENT**

Enable/disable update only Token's own registry enabled field.

### Activate/adopt

**GAP**

There is no separate activation/adoption operation and enable does not prove operational collection.

### Initialize

**PARTIAL**

Library callers can create a Token ledger with create-or-open.

Native install intentionally does not initialize usage state.

There is no public native/standalone init command.

### Migrate/import

**PARTIAL**

Existing source histories can be passively backfilled when local collectors are explicitly run.

Hardened alpha.1 intentionally has no ledger format 1 -> 2 migration because alpha.0 was never published.

There is no general Token ledger migration command/framework for future released formats.

### Status/doctor

**CURRENT WITH LIMITATIONS**

Native status proves:

- host compatibility;
- registration;
- installed-file materialization;
- ledger presence.

Native doctor additionally opens an existing native ledger read-only and runs quick integrity checking.

**GAP**

It does not currently prove:

- collection is running;
- collector health across sources;
- pricing source/fetcher readiness;
- pricing freshness;
- cost-truth coverage/unpriced share;
- Connections/provider transport availability;
- actual OS consumption of engine.mjs;
- operational request ingest.

Standalone doctor reports healthy when no OS is detected and does not inspect a standalone ledger/runtime.

### Update

**CURRENT WITH LIMITATIONS**

update repairs/replaces Token-owned installed files/registration while preserving ledger state.

It is not a schema migration command and does not migrate incompatible ledgers.

### Disable

**CURRENT**

Disable changes registration state and preserves state.

### Detach/uninstall

**CURRENT**

uninstall removes Token-owned materialization and registry entry only.

Token user state survives.

### Reinstall

**CURRENT WITH LIMITATIONS**

Reinstall can restore materialization around preserved compatible state.

### Reconcile

**GAP**

There is no Token reconcile/activate operation that turns discovered installed sources, pricing transport and host read surfaces into a verified ready state.

### Rollback

**GAP**

No package/state rollback command exists.

## 12. Lifecycle matrix

| Stage | Exists? | Command/API | Idempotent? | State owner | Acceptance evidence | Gap |
|---|---|---|---|---|---|---|
| install package | Yes | npm install TGZ | Yes enough for package install | package manager | release acceptance | npm publication absent |
| native install | Yes | ai-verse-token install | Yes | Token registry/materialization | native tests | real OS acceptance absent |
| attach/register | Yes, combined with install | native install/update | Yes | Token registry entry | native tests | no separate host activation |
| enable | Yes | ai-verse-token enable | Yes | Token registry entry | native tests | enabled does not mean collecting |
| activate/adopt | No | none | N/A | should be host + Token contract | none | required |
| initialize ledger | Library only | openTokenLedger create-or-open | repeat-safe on compatible ledger | Token | storage tests | no user command/native flow |
| migrate/import source history | Library collector path | collector discovery + runner | checkpoint/idempotent | Token observations, sources remain source-owned | collector tests | no one-command adoption |
| migrate Token state | No general framework | none | N/A | Token | alpha0 explicitly not migrated | required before future released format change |
| doctor/status | Partial | status/doctor | read-only | Token | native tests | shallow readiness |
| update | Yes, extension materialization | ai-verse-token update | Yes | Token registry/files | native tests | no state migration/rollback |
| disable | Yes | ai-verse-token disable | Yes | Token registry | native tests | runtime effect depends on host |
| detach/uninstall | Yes | ai-verse-token uninstall | Yes enough | Token registration/files, user state preserved | native/release tests | no explicit detach separate from uninstall |
| reinstall | Yes | install after uninstall | Yes with compatible state | Token | release test | no incompatible-state migration |
| reconcile | No | none | N/A | future host/Token | none | required |
| rollback | No | none | N/A | future release/state lifecycle | none | required for mature releases |

## 13. Install-order independence

**CURRENT / LAW**

Token-side ecosystem adapters have no runtime dependency on sibling repositories.

Missing Dashboard, Brain, Memory, Data, Multiple Bots, Skills, Automations or Connections does not block Token's library/core.

Native install preserves sibling registry entries.

**CURRENT LIMITATION**

Install-order independence has been proven primarily as component-local non-coupling.

The actual "component installed later becomes operationally usable by a running OS/agent" path is not implemented/proven in Token.

## 14. Activation/adoption by existing agents

**INTENDED**

A running compatible agent/host should be able to:

1. discover that Token is installed;
2. attach the package/runtime;
3. choose/verify Token state path;
4. discover supported local sources;
5. initialize a ledger if the operator approves;
6. run bounded historical backfill;
7. activate live/passive collection;
8. bind provider/pricing transports through host-owned Connections;
9. refresh required authoritative pricing;
10. expose bounded authorized read surfaces;
11. report collection/pricing/cost readiness;
12. keep Token canonical for telemetry while leaving all sibling operational truth with its owner.

**GAP**

No single implementation flow currently performs this sequence.

## 15. Portability outside AI-Verse OS

### Strong portable core

**CURRENT**

The following are OS-independent:

- protocol;
- ledger;
- query engine;
- identity resolver;
- pricing store/synchronizer framework;
- cost engine;
- collector SDK;
- built-in collectors;
- provider/gateway/OTel normalizers;
- time engine;
- efficiency/budget calculators;
- TokenReader/export/MCP.

This architecture is reusable by Hermes, custom agents, coding assistants and other hosts.

### Host-specific layer

**CURRENT**

src/native is the AI-Verse OS-specific lifecycle layer.

Ecosystem adapters are AI-Verse-aware but still avoid sibling package dependencies.

### Portability gap

**GAP**

A non-AI-Verse host still needs its own bootstrap/orchestration code for:

- source discovery;
- ledger creation;
- collector cadence;
- pricing fetch transports;
- scoped/authorized read exposure.

## 16. Sibling integration boundaries

### Dashboard

**CURRENT**

Dashboard receives a TokenReader-backed projection.

It does not receive a SQLite path or database handle from the Dashboard adapter.

**LAW**

Dashboard is deletable/rebuildable presentation. It must never become Token's ledger or shadow accounting authority.

### Brain

**CURRENT**

Brain receives bounded read answers with Token provenance.

Recent events are privacy-safe.

No write authority is granted.

### Memory

**CURRENT**

Token can create evidence references and proposed historical usage candidates.

auto_write is always false.

**LAW**

Token telemetry must not be bulk-copied into Memory as a second event store.

### Data

**CURRENT**

Data references/projections explicitly retain authority = ai-verse-token and ownership_transferred = false.

**LAW**

Data may model operational records that reference Token evidence, but may not become the canonical Token telemetry database.

### Multiple Bots

**CURRENT**

Trusted Bot/Worker/TeamRun/task/workspace/project attribution can enrich missing exact fields.

Conflicts fail closed.

**LAW**

Attribution must not grant Bot authority or workspace permission.

### Skills/Automations

**CURRENT**

Correlation metadata may add missing exact IDs.

It does not grant execution or connection authority.

**LAW**

Token does not become scheduler owner.

### Connections

**CURRENT**

Token accepts opaque connection/credential handles only.

Unknown fields, including attempted raw secrets, are rejected by the handle factory.

**LAW**

Credential resolution remains outside Token.

## 17. Permissions, security and privacy

### Strong current controls

**CURRENT**

- protocol unknown-field rejection;
- NUL/size/range validation;
- strict ISO timestamps;
- exact money representation;
- content_stored false;
- no prompt/response/secret schema columns;
- foreign SQLite refusal;
- schema-object definition verification;
- SQLite immutable triggers;
- WAL + FULL synchronization for writable ledger;
- read-only query_only mode;
- symlink/path rejection for ledger/native/pricing state;
- extension registry lock;
- raw-text lost-update detection;
- atomic registry/materialization writes;
- privacy-safe exports/agent projections;
- no network/credential code hidden in core adapters.

### Permission boundary gap

**GAP**

Token currently assumes that code given a TokenLedger writer or TokenReader has already been authorized by the host.

It does not implement a user/workspace ACL model, which is appropriate for ownership, but AI-Verse integration still needs a host-enforced scoped writer/reader boundary.

### Lock recovery gap

**GAP**

The native registry lock is an exclusive file created with wx and removed in finally.

A process crash can leave the lock file behind.

There is no stale-lock owner/timestamp validation or automated recovery path in alpha.1.

## 18. Failure and degraded modes

**CURRENT**

Token generally fails closed:

- invalid protocol input does not enter the ledger;
- conflicting idempotency identities fail;
- cross-source exact conflicts roll back;
- unknown model/tariff becomes UNKNOWN;
- stale/unverified pricing cannot authorize current calculated cost;
- price fetch failure preserves prior success evidence;
- malformed pricing files fail;
- incompatible/foreign ledger fails;
- unsafe/symlink paths fail;
- incompatible OS fails before Token-owned mutation;
- malformed registry fails rather than being replaced;
- missing collector source becomes unavailable rather than fabricated usage.

**LAW**

Failure must never widen authority, convert unknown to zero or make a secondary source authoritative.

## 19. Historical evolution

### HISTORICAL: alpha.0 first-release completion

The older local first-release archive was package version 0.1.0-alpha.0 and already claimed 32/32 first-release implementation completion.

### HISTORICAL: hardened alpha.1

A subsequent forensic hardening pass changed alpha.0 to alpha.1 and ledger format 2.

The hardening audit records material fixes in:

- aggregate unknown truth and exact BigInt accumulation;
- context-sensitive pricing using context_input_tokens;
- exact ACTUAL money stored as decimal text;
- dedupe attribution and conflict handling;
- zero-duration/time correctness;
- strict Hermes actual-cost trust;
- Anthropic web-search billable units;
- SQLite schema-tamper resistance;
- pricing-store path/symlink/size safety;
- native lifecycle rollback/symlink/lock safety;
- privacy redaction of external charge IDs;
- collector scalability/checkpoint pushdown;
- protocol/JSON Schema parity.

The hardened archive differs materially across protocol, storage, pricing, cost, collectors, adapters, lifecycle, exports, tests and docs.

## 20. Permanent laws established by repairs

**LAW 1: Unknown is not zero.**

This applies to usage, time and money.

**LAW 2: Money provenance is part of the value.**

ACTUAL and CALCULATED may share the same numeric amount while having different truth semantics.

**LAW 3: Real zero remains real.**

A trusted zero-dollar charge must not collapse into UNKNOWN.

**LAW 4: Exact financial values use exact decimal text/arithmetic.**

Do not round through JavaScript floating point.

**LAW 5: Payloads cannot self-promote authority.**

Trusted actual-cost/pricing source identity must come from trusted configuration.

**LAW 6: Raw observations remain immutable.**

Deduplication/reconciliation must add correlation/supersession evidence rather than mutate source history.

**LAW 7: Dedupe requires exact evidence.**

Similarity is not identity.

**LAW 8: Attribution must not change operational authority.**

Telemetry labels do not grant permission or canonical ownership.

**LAW 9: Derived projections retain source ownership.**

Data/Memory/Brain/Bots/Dashboard may consume Token evidence without acquiring Token truth.

**LAW 10: Installation must not invent telemetry.**

Native install creates registration/materialization, not fake usage state.

**LAW 11: Installed/enabled is not operationally ready.**

For Token, readiness additionally requires source/runtime availability and, for cost intelligence, pricing/cost-truth readiness.

## 21. Inspirations and curated references

**INSPIRATION**

The repository explicitly records ten primary references:

1. Tokscale;
2. CodeBurn;
3. ccusage;
4. Pydantic genai-prices;
5. Portkey Models;
6. LiteLLM;
7. OpenLIT;
8. Langfuse;
9. OpenMeter;
10. Bifrost.

Secondary references include:

- OpenLLMetry;
- Helicone;
- Hermes Agent.

Adopted/curated ideas include:

- passive multi-runtime collection;
- explicit attribution;
- immutable metering events;
- effective-dated pricing;
- provider/model normalization;
- OpenTelemetry timing semantics;
- provided-vs-derived cost separation;
- hierarchical trace attribution;
- bounded aggregation;
- active-wall versus compute separation.

Explicitly avoided ideas include:

- mandatory gateway architecture;
- fuzzy/hardcoded pricing presented as authoritative;
- current-price retroactive historical repricing;
- prompt/response observability storage by default;
- full billing/subscription/invoice stack in Token;
- arbitrary timestamp-gap heuristics labeled active time.

The repository states that source implementation is original and only public behavior/contracts/ideas were used. Any future copied/vendor code requires exact license/version review and attribution.

## 22. Current contradictions and documentation drift

### Contradiction A: storage format document is stale

**CURRENT code:** ledger format version 2.

**STALE DOC:** docs/STORAGE-V0.1.md still states PRAGMA user_version = 1 and token_metadata.format_version = 1.

**Required correction:** update the storage document to distinguish historical v1 from current alpha.1 v2.

### Contradiction B: architecture blueprint overstates SQLite ownership

docs/ARCHITECTURE-BLUEPRINT.md says the ledger owns immutable pricing snapshots, derived cost records and bounded rollups/budget state.

**CURRENT implementation:**

- pricing snapshots are in the separate PriceSnapshotStore filesystem tree;
- CALCULATED costs are returned by CostEngine, not persisted as canonical ledger rows;
- rollups/efficiency/budget evaluations are computed from source evidence, not persisted as canonical ledger state.

The current implementation is architecturally cleaner than the stale wording, but the doc must be corrected.

### Contradiction C: blueprint status is stale

docs/ARCHITECTURE-BLUEPRINT.md still says "implementation in progress" while current README/Build Map say hardened alpha.1 release candidate and 32/32 implementation tasks complete.

### Contradiction D: README cost/read diagram implies end-to-end composition

README routes Pricing -> ACTUAL/CALCULATED -> Time/rollup -> CLI/JSON/MCP/Dashboard.

**CURRENT implementation:** main TokenReader/CLI/MCP/Dashboard efficiency paths use only event-embedded ACTUAL charges and do not compose CostEngine + PriceSnapshotStore.

This should be documented explicitly until cost-aware reads are implemented.

### Contradiction E: integration health contract is more ambitious than doctor

docs/AI-VERSE-INTEGRATION.md says health should distinguish collector health, pricing freshness, cost truth, unpriced usage share, provider auth and migration requirements.

**CURRENT doctor:** host/registration/materialization plus optional ledger quick integrity only.

The integration document is INTENDED behavior, not current doctor depth.

## 23. Current intended milestone

The repository itself defines the present milestone as:

**Hardened alpha.1 first-release implementation release candidate, with 32/32 build tasks complete and local release acceptance passed, while npm publication and hosted CI remain separate distribution steps.**

That milestone contains two different notions of completion:

1. **Repository implementation gate**, which is substantially complete.
2. **Seamless AI-Verse product readiness**, which is not complete.

The AI-Verse-System audit uses the second standard when deciding whether Token "works like a glove."

## 24. Implementation completeness by dimension

| Dimension | Status | Evidence/meaning |
|---|---|---|
| ENGINE / CORE | COMPLETE WITH LIMITATIONS | protocol, ledger, dedupe, identity, pricing framework, cost, collectors, adapters, time, efficiency all implemented; end-to-end composition still incomplete |
| ARCHITECTURE / CONTRACT | COMPLETE WITH LIMITATIONS | strong ownership model, but several docs are stale |
| INSTALL / PACKAGE | COMPLETE WITH LIMITATIONS | local packed clean install proven; npm/public artifact not published |
| HOST INTEGRATION | PARTIAL | native registry/materialization exists; operational host loading/collection not proven |
| ATTACH / REGISTER | COMPLETE WITH LIMITATIONS | idempotent Token-side registration proven against fixture |
| ACTIVATE / ADOPT | MISSING | no activation/reconciliation flow |
| SCOPE INITIALIZATION | PARTIAL | ledger API can create state; install deliberately does not; no init UX |
| MIGRATION / LEGACY | COMPLETE WITH LIMITATIONS | old source history can be collected; no general Token ledger migration framework |
| HEALTH / DOCTOR | PARTIAL | attachment and ledger structural health only |
| PERMISSION / SAFETY | COMPLETE WITH LIMITATIONS | strong data/path/trust safety; authorized scope floor not modeled in read interface |
| CROSS-COMPONENT READ | COMPLETE WITH LIMITATIONS | bounded Token-side adapters implemented; real system acceptance absent |
| CROSS-COMPONENT WRITE | NOT APPLICABLE for sibling canonical state | Token intentionally does not write sibling truth |
| UPDATE / UPGRADE | PARTIAL | materialization update yes; schema migration/rollback no |
| DISABLE / DETACH / UNINSTALL | COMPLETE | state-preserving disable/uninstall proven |
| REINSTALL / RECONCILE | PARTIAL | reinstall proven; reconcile/adopt missing |
| CROSS-PLATFORM | UNVERIFIED | 6-leg CI matrix defined, but no remote Token repo to execute it |
| ACCEPTANCE | COMPLETE WITH LIMITATIONS | local 249 normal + 3 release tests pass; real OS/provider transport paths not proven |
| RELEASE / DISTRIBUTION | PARTIAL / EXTERNALLY BLOCKED | local TGZ passes; no Token remote repo/npm publication |
| DOCUMENTATION CONSISTENCY | PARTIAL | material drift identified above |

## 25. Verified local acceptance state

On the reviewed archive under Node 22.16.0:

- npm run ci: PASS;
- normal test suite: 249 / 249 pass;
- release test suite: 3 / 3 pass;
- total observed checks: 252;
- failures: 0;
- skipped: 0;
- cancelled: 0;
- npm pack --dry-run: PASS;
- package dry-run size: approximately 185.7 kB;
- packaged files: 320.

CI configuration declares:

- Ubuntu latest + Node 22/24;
- macOS latest + Node 22/24;
- Windows latest + Node 22/24.

Those hosted legs are configured but not executed/proven because no Token remote repository exists.

## 26. Exact missing work before seamless operation

### Priority 0: operational activation

Implement a supported host/standalone runtime bootstrap that turns installed Token from metadata into a working service.

It must separate:

- installed;
- registered;
- enabled;
- source-active;
- collecting;
- pricing-ready;
- cost-ready;
- healthy;
- authorized;
- ready.

It must not invent telemetry during install.

### Priority 0: cost-aware read composition

Add a canonical read-service path that can:

1. read canonical events;
2. resolve/validate identity;
3. obtain matching immutable pricing evidence;
4. rate each event as ACTUAL/CALCULATED/UNKNOWN;
5. preserve original currency/status/provenance;
6. aggregate costs without mixing currencies/truth;
7. expose that through CLI/MCP/Dashboard/Brain as appropriate.

Do not persist CALCULATED cost as a competing editable truth store.

### Priority 0: usable collection path

Provide a default built-in collector composition and an explicit operator/host action for:

- source discovery;
- bounded backfill;
- repeated incremental scans;
- collector health;
- checkpoint visibility.

Token must not become the OS scheduler. Ongoing cadence should be delegated to the canonical scheduler/host through a versioned contract.

### Priority 0: pricing transport

Provide concrete, tested pricing fetchers for the authoritative sources needed by the first-release cost promise, or a versioned host transport contract with an acceptance-tested reference implementation.

A fetched payload must never self-promote source authority.

### Priority 1: real AI-Verse host acceptance

Test the actual member/product path against the current supported AI-Verse host contract:

package availability
-> install/register
-> host discovery
-> activate
-> initialize/backfill
-> read projection
-> disable
-> reinstall
-> state reuse.

Synthetic fixture acceptance is not enough for a "like a glove" claim.

### Priority 1: authorization-scoped readers

Add or define an outer host contract that creates scoped readers or intersects every requested scope with caller authorization.

Do not make Token the identity/permission database.

### Priority 1: deeper doctor/readiness

Doctor or a delegated health surface must expose, without conflation:

- attachment health;
- ledger integrity;
- collector/source availability;
- last collection/checkpoint status;
- pricing-source/fetcher availability;
- pricing freshness;
- cost-truth coverage/unpriced share;
- optional provider connection missing/degraded;
- migration requirement;
- operational sample readiness.

### Priority 1: durable package resolution

Define and acceptance-test how a native host resolves @ai-verse/token after npx installation.

Writing a package name into engine.mjs is not proof that a running host can import or invoke the package later.

### Priority 2: lifecycle hardening

Add:

- stale registry-lock recovery policy;
- explicit reconcile/adopt operation;
- release/state compatibility checks on update;
- rollback policy;
- state migration framework before any published incompatible ledger format.

### Priority 2: documentation repair

Correct:

- STORAGE-V0.1 current format;
- ARCHITECTURE-BLUEPRINT ownership/storage claims and status;
- README/read-surface cost composition wording;
- AI-VERSE-INTEGRATION health sections to label current versus intended behavior.

### Priority 2: release/distribution proof

Create/publish the intended remote/artifact channel, then run:

- hosted Linux/macOS/Windows matrix;
- immutable release/tag verification;
- exact member installation command;
- clean host activation from the exact released artifact.

## 27. Desired future state

**INTENDED**

A mature Token installation should support this product path:

1. install package anywhere;
2. host discovers Token through a self-describing extension/component contract;
3. operator explicitly activates Token;
4. Token discovers existing supported local histories without mutating them;
5. operator approves/init state;
6. historical backfill runs idempotently;
7. host schedules continued passive collection through the canonical scheduler owner;
8. remote provider/pricing access uses Connections-owned credential handles;
9. pricing refresh establishes current cost readiness;
10. Token exposes authorized, bounded, cost-aware read projections;
11. Dashboard/Brain/Data/Memory/Bots consume those projections without acquiring Token ownership;
12. doctor distinguishes structural health, collection health, pricing health and operational readiness;
13. disable/uninstall leaves user-owned telemetry state intact;
14. reinstall/update validates/migrates compatible state rather than creating parallel truth;
15. non-AI-Verse runtimes can use the same portable core through their own host adapter.

## 28. Definition of done

### Current repository implementation gate

This is satisfied when:

- all 32 planned core tasks are implemented;
- local full test/release suite passes;
- package can be clean-installed;
- first-release truth/safety invariants hold.

The reviewed alpha.1 satisfies this repository-defined gate.

### Seamless AI-Verse/current product target

Token is done for the broader AI-Verse target only when all of the following are proven from a released artifact:

- package is durably available to the host;
- install/attach is safe and idempotent;
- activation is explicit and real;
- a new ledger can be initialized without fake usage;
- existing agent histories can be backfilled through the supported path;
- built-in collectors can become active without custom application code;
- pricing evidence can refresh through supported transports;
- ACTUAL/CALCULATED/UNKNOWN is visible through primary read surfaces;
- reader scope is bounded by host authorization;
- doctor proves the correct health depth;
- disabling/uninstalling preserves state;
- reinstall/update rediscover compatible state;
- incompatible future state has an explicit migration path;
- actual AI-Verse host acceptance passes;
- compatible standalone host/reference flow passes;
- immutable release and cross-platform CI are verified.

## 29. Contribution to the supreme AI-Verse vision

Token contributes a critical evidence plane:

- immutable AI-use telemetry;
- conservative cost truth;
- exact time/concurrency evidence;
- traceable runtime/provider/model attribution;
- reusable read-only usage intelligence.

Its most important architectural contribution is not "token counting." It is the separation of **observed evidence** from **operational authority**.

That separation should become a supreme-system law:

> AI-Verse may use telemetry to reason, budget, prioritize and display, but telemetry projections never silently become the canonical state of the component they describe.

## 30. Open decisions

1. What exact component/host contract activates Token after registration?
2. Which host owns recurring collector/pricing cadence? Token should expose jobs/operations, not own the global scheduler.
3. Should the first reference runtime be a local daemon, host-invoked commands, MCP/RPC service, or a combination?
4. How should durable package resolution work after an npx native install?
5. Should cost-aware reads be computed on demand from PriceSnapshotStore, cached with provenance, or exposed through a dedicated rating service?
6. What is the canonical authorized-reader envelope for workspace/project-scoped telemetry?
7. Which official pricing sources must have first-party concrete fetchers for the first member release?
8. What migration/version policy must exist before ledger format changes after publication?
9. What stale-lock recovery strategy is acceptable without risking two concurrent registry writers?
10. What exact health levels make Token "ready": source collection only, cost intelligence, or both with explicitly separate readiness dimensions?
