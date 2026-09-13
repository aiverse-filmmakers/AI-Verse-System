# AI-Verse Token QC

## Remote public-beta QC closure

**Update date:** 2026-09-13  
**Verdict:** PASS for the requested Token public-beta implementation and hosted cross-platform release gate.

Canonical remote: `aiverse-filmmakers/ai-verse-token`  
Current version: `0.1.0-beta.2`  
Main/tag target: `8b24891cd9c230e191b2637b6db2122b3dd9984d`

Hosted CI run **34776309959** completed successfully on all six matrix legs: Ubuntu, macOS and Windows on Node 22 and Node 24.

Windows CI initially exposed two test-harness portability defects: file URL path conversion and direct `npm.cmd` spawning. Both were corrected without changing Token's accounting, authorization or ownership laws. The immutable beta.1 tag was not moved; beta.2 is the cross-platform follow-up release.

The former QC item "hosted cross-platform execution pending" is now closed.


## Public-beta closure verdict

**Update date:** 2026-09-13

**Implementation verdict:** PASS locally for the requested public-beta Token scope.  
**Remote release evidence verdict:** PENDING canonical Token repository creation/push and hosted matrix execution.

The alpha.1 gaps recorded by this QC have been closed in the restored `0.1.0-beta.1` implementation:

1. operational setup/activation and a durable installed runtime bundle;
2. built-in source discovery plus actual collector orchestration/backfill;
3. concrete pricing transport;
4. ACTUAL / CALCULATED / UNKNOWN primary read composition;
5. mandatory explicit read authorization and immutable scope floors;
6. operational doctor/readiness;
7. Gateway owner projection and Dashboard owner-backed cost projection;
8. Multiple Bots/workspace/task/Skill attribution without authority transfer;
9. state-preserving update/uninstall/reinstall behavior;
10. immutable local release artifacts and preserved provenance.

Local evidence is **255/255 normal tests + 3/3 release tests**, including clean packed installation.

The following laws remain enforced:

- UNKNOWN never becomes zero;
- actual zero remains real ACTUAL zero;
- fetched pricing payloads cannot self-promote trust;
- raw telemetry remains immutable;
- attribution never grants permission;
- projections never transfer Token ownership;
- recurring scheduling remains outside Token.

One item remains unverified rather than failed: hosted Linux/macOS/Windows CI. The workflow is present, but the connected GitHub tooling cannot create the missing `aiverse-filmmakers/AI-Verse-Token` repository, so no remote Actions run can yet exist.

The detailed audit below records the alpha.1 state before this public-beta closure and should be read historically where it conflicts with this section.


**Component:** AI-Verse Token  
**Reviewed artifact:** `AI-Verse-Token-hardened-alpha.1.zip`  
**Artifact SHA-256:** `4feb14ed9df2b82b7f4a07d571e77beda4afe695982e55b3dcfe0a7440588257`  
**Package:** `@ai-verse/token@0.1.0-alpha.1`  
**Review date:** 2026-09-13  
**Method:** `docs/AUDIT-METHODOLOGY.md`

## Overall verdict

**PASS WITH GAPS**

The Token repository contains a strong and unusually conservative telemetry/accounting core.

The following are genuinely implemented and acceptance-tested locally:

- strict UsageEvent protocol;
- immutable SQLite event evidence;
- source idempotency and exact cross-source deduplication;
- separated runtime/billing/provider/model identity;
- immutable effective-dated price snapshots;
- ACTUAL/CALCULATED/UNKNOWN monetary law;
- local collectors and remote normalizers;
- concurrency-correct time analysis;
- efficiency/budget calculations;
- bounded read/export/MCP surfaces;
- ownership-safe AI-Verse extension lifecycle;
- cross-component adapters that preserve Token ownership.

The repository-defined first-release implementation gate is complete at 32/32 and the hardened alpha.1 local release suite passes.

The component is **not yet seamless-system ready** because the product path stops between "installed/registered/enabled" and "operationally collecting, pricing-ready, cost-aware and authorized."

The principal blockers are:

1. no activation/adoption/reconcile runtime;
2. installed `engine.mjs` is a descriptor rather than an operational engine;
3. no turnkey standalone collection/bootstrap UX;
4. no concrete built-in pricing network fetchers;
5. no CALCULATED cost composition in the main TokenReader/CLI/MCP/Dashboard path;
6. no host authorization floor in read interfaces;
7. native doctor is shallower than intended operational readiness;
8. actual AI-Verse OS end-to-end acceptance is unverified;
9. hosted cross-platform CI and npm/member distribution are unverified.

## 1. Architecture/ownership QC

**PASS WITH GAPS**

### What passes

Token's ownership boundary is coherent:

- usage observations are Token truth;
- pricing snapshots are Token pricing truth;
- correlations/supersessions remain Token evidence;
- collector checkpoints are Token operational state;
- derived costs/time/efficiency/budget views remain derived;
- sibling adapters retain Token authority rather than transferring it.

The architecture explicitly avoids becoming:

- a second Data store;
- a second Memory store;
- a Dashboard database;
- a Brain strategy store;
- a Bot authority store;
- a credential store;
- a scheduler.

### Gap

Scope/attribution IDs are represented correctly as telemetry fields, but the public read layer does not itself enforce a host authorization floor.

That must be solved at the host boundary without making Token the system identity/ACL owner.

## 2. Lifecycle/install-order QC

**PASS WITH GAPS**

### What passes

- local package can be packed and clean-installed;
- native install/update are idempotent over Token-owned registration/materialization;
- sibling/unknown registry fields are preserved;
- install does not invent telemetry;
- enable/disable exist;
- uninstall preserves user state;
- reinstall can reuse compatible preserved state;
- missing sibling components do not block Token core.

### Gaps

- attach/register is not followed by a real activation/adoption path;
- enabled does not mean source-active or collecting;
- there is no reconcile operation;
- no acceptance proves a running real host can resolve and invoke the package from the installed descriptor;
- no general schema rollback/migration lifecycle exists.

## 3. Migration/history QC

**PASS WITH GAPS**

### What passes

Existing local agent histories can be passively backfilled once collectors are explicitly run.

Source histories are not mutated.

Alpha.0 to alpha.1 migration was deliberately omitted because alpha.0 was not published.

### Gap

Before any incompatible format change after publication, Token needs a real state migration contract including:

- compatibility detection;
- backup/provenance;
- idempotent/resumable execution;
- verification;
- failure recovery/rollback;
- no parallel canonical ledger.

## 4. Integration QC

**PASS WITH GAPS**

### What passes

All Token-side sibling adapters are ownership-safe and avoid direct sibling database dependencies.

Dashboard/Brain/Memory/Data/Bots/Connections/correlation surfaces are bounded.

### Gaps

- real system host activation is not acceptance-tested;
- read APIs do not enforce host scope authorization;
- pricing transport/credential resolution has no reference host integration;
- main read path is not cost-engine aware.

## 5. Security/isolation QC

**PASS WITH GAPS**

### What passes

- strict validation;
- content storage prohibition;
- immutable event triggers;
- foreign DB rejection;
- schema-definition checking;
- symlink/path protections;
- bounded payloads;
- read-only database modes where required;
- atomic native writes;
- registry lock;
- exact trust registry for actual costs/pricing;
- no raw credentials in connection handle API;
- privacy-redacted agent-facing projections.

### Gaps

- no stale native lock recovery after a process crash;
- authorization scoping is external and currently not represented in TokenReader/MCP construction;
- hosted cross-platform filesystem behavior is unverified.

## 6. Runtime portability QC

**PASS WITH GAPS**

The core protocol/storage/pricing/cost/collector/adapter/time/read stack is not coupled to AI-Verse OS.

This is a good portable architecture for Hermes, coding agents and custom hosts.

The missing portability layer is an operational reference bootstrap that assembles:

- state initialization;
- collectors;
- recurring host cadence;
- pricing transports;
- scoped reads.

## 7. Product/UX QC

**PASS WITH GAPS**

The read and native lifecycle CLI is understandable.

However, a user cannot yet go from a fresh package to useful ongoing Token intelligence without writing application code or host glue.

Missing first-run concepts include:

- initialize;
- discover sources;
- backfill;
- activate collection;
- refresh pricing;
- show readiness;
- reconcile.

The README product promise also exceeds the current main read path for CALCULATED/UNKNOWN cost reporting.

## 8. Historical-learning QC

**PASS**

The alpha.1 hardening record contains meaningful architectural repairs rather than cosmetic changes.

The audit successfully promotes the important lessons into permanent laws:

- unknown is not zero;
- real zero remains real;
- money provenance is part of the value;
- exact money uses exact representation;
- payloads cannot self-promote trust;
- raw observations remain immutable;
- dedupe requires exact evidence;
- telemetry attribution does not grant operational authority;
- projections do not transfer ownership;
- installation must not invent usage;
- enabled is not ready.

## 9. Inspiration/curation QC

**PASS**

External references are explicitly recorded.

The repository distinguishes adopted ideas from rejected architecture patterns.

No evidence was found that external source code was copied into the package.

The curated design improves on several source patterns by preserving stronger money truth, event immutability and ownership boundaries.

## 10. Current-target readiness QC

**PASS for the repository-defined implementation gate. PASS WITH MAJOR GAPS for the AI-Verse seamless-product target.**

### Repository-defined gate

- Build Map: 32/32;
- local `npm run ci`: pass;
- normal tests: 249/249;
- release tests: 3/3;
- pack dry-run: pass.

### Seamless target

Not complete.

The component is best described as:

> a hardened alpha.1 portable telemetry/cost engine with safe native registration, but without the final operational activation, pricing transport, cost-aware read composition and host-readiness layer.

## 11. Future-state coherence QC

**PASS**

The current architecture can reach the desired seamless state without being rewritten from scratch.

The missing work can be added as:

- host/bootstrap orchestration;
- concrete pricing transport;
- a cost-aware read service;
- authorization-scoped reader construction;
- deeper health/readiness;
- lifecycle migration/reconcile/release hardening.

None of those require Token to absorb sibling canonical ownership.

## 12. Methodology lens-by-lens verdict

| Lens | Verdict | Finding |
|---|---|---|
| 1. Product identity | PASS WITH GAPS | Product framing is accurate at core-engine level. "What did it cost?" is not fully delivered through primary read UX. |
| 2. Architecture | PASS | Protocol, immutable evidence, identity, pricing, cost, collectors, adapters, analysis and projections are cleanly layered. |
| 3. Ownership | PASS | Token owns telemetry/pricing evidence and avoids sibling operational ownership. |
| 4. Source of truth | PASS WITH GAPS | Canonical event/pricing evidence is clear. Some architecture prose incorrectly describes persisted derived state. |
| 5. Provenance | PASS | Source fingerprints, correlations, supersessions, price source/effective time and historical raw evidence are retained. |
| 6. Scope model | PASS WITH GAPS | Rich attribution exists, but scope IDs are telemetry labels, not an authorization model. |
| 7. Isolation | PASS WITH GAPS | Strong physical/path isolation. Logical caller authorization must be imposed by host/scoped-reader contract. |
| 8. Privacy/local-first behavior | PASS | Prompt/response content excluded, passive local reads, reduced agent/export surfaces, no secret ownership. |
| 9. Installation | PASS WITH GAPS | Local package/native install are real. Native install registers/materializes but does not make Token operational. |
| 10. Attachment / registration | PASS WITH GAPS | Idempotent local extension registration exists. Real host consumption of the descriptor is unverified. |
| 11. Activation / adoption | FAIL / REQUIRES CORRECTION | No supported activate/adopt/reconcile transaction exists. |
| 12. Initialization | PASS WITH GAPS | Library can create ledger. Native install deliberately does not. No operator init path exists. |
| 13. Migration / legacy integration | PASS WITH GAPS | Source-history backfill is possible. No general released-ledger migration framework exists. |
| 14. Update / upgrade | PASS WITH GAPS | Extension files update safely, but state schema migration and rollback are absent. |
| 15. Disable / detach / uninstall / reinstall | PASS | Enable/disable/uninstall/reinstall preserve state appropriately. Explicit detach is folded into uninstall. |
| 16. Install-order independence | PASS WITH GAPS | Token core is sibling-independent. Late installation becoming operational in a running host is unproven. |
| 17. Discovery | PASS WITH GAPS | Collectors can detect configured sources. No product-level discover-all/activate workflow exists. |
| 18. Readiness | FAIL / REQUIRES CORRECTION | Installed/registered/enabled states are present, but source-active, collecting, pricing-ready and cost-ready are not modeled end to end. |
| 19. Health / doctor / observability | PASS WITH GAPS | Structural/attachment/ledger integrity exist. Collector/pricing/cost operational health does not. |
| 20. Permissions / approvals | PASS WITH GAPS | Trust-sensitive data is validated. Caller authorization/approval is assumed to be handled by the host. |
| 21. Security / path safety | PASS WITH GAPS | Strong path/symlink/schema safety. Stale lock recovery remains. |
| 22. Idempotency / replay safety | PASS | Stable event identities, source fingerprints, transactional dedupe and checkpointing are strong. |
| 23. Concurrency / locking | PASS WITH GAPS | SQLite transactions and registry lock are good. Crash-left lock recovery is absent. |
| 24. Failure behavior | PASS | Important ambiguity/corruption/pricing/dedupe paths fail closed rather than widen authority or invent values. |
| 25. Capability taxonomy | PASS | Collectors, adapters, read projections and lifecycle are not misrepresented as Skills, schedulers or canonical sibling stores. |
| 26. Runtime/agent portability | PASS WITH GAPS | Core is portable. Reference bootstrap/operational host integration is missing. |
| 27. Integration boundaries | PASS | Sibling adapters use bounded projections/opaque handles and preserve owner boundaries. |
| 28. Cross-component writes | PASS | Token intentionally performs no durable sibling canonical writes. Memory candidate auto-write is false. |
| 29. Read path / retrieval | PASS WITH GAPS | Bounded reader exists. Cost engine is not composed into main reads and caller authorization is not enforced inside the reader. |
| 30. Data model / schema evolution | PASS WITH GAPS | Stable schema/format validation is strong. Future released migration framework is absent and storage docs lag format 2. |
| 31. Performance / scalability | PASS WITH GAPS | Bounded scans, indexes, checkpoint pushdown and a performance baseline exist. Large production installations remain unverified. |
| 32. Product/UX | PASS WITH GAPS | CLI reads/lifecycle are usable, but no fresh-install-to-live-intelligence flow exists. |
| 33. Automation / Cadence | PASS | Token correctly does not claim scheduler ownership. Ongoing collection cadence still needs host integration. |
| 34. Agent/orchestration behavior | PASS WITH GAPS | Agent-facing read projections are safe. Existing agents lack one universal Token adoption transaction. |
| 35. Apps/UI projections | PASS WITH GAPS | Dashboard is a projection and cannot own Token DB. Projection is currently actual-only for cost intelligence. |
| 36. Release / distribution | PASS WITH GAPS | Local TGZ release acceptance passes. Remote immutable release/npm distribution does not yet exist. |
| 37. Cross-platform behavior | UNVERIFIED | Six CI legs are declared. Hosted Linux/macOS/Windows execution is unavailable without a Token remote repository. |
| 38. Documentation consistency | FAIL / REQUIRES CORRECTION | Storage format, architecture storage boundaries/status, read-path cost composition and doctor depth contain drift. |
| 39. Historical-learning | PASS | Hardened alpha.1 repairs are documented and yield reusable laws. |
| 40. Inspiration / curation | PASS | References and adopted/rejected ideas are explicitly documented with no copied-source claim. |
| 41. Negative-space analysis | FAIL / REQUIRES CORRECTION | Expected operational activation, concrete pricing fetchers, cost-aware primary reads, deep readiness and standalone bootstrap are absent. |
| 42. Architecture-vs-operation analysis | PASS WITH GAPS | Strong distinction is possible, but product docs need to state more clearly which pieces are frameworks versus active services. |
| 43. Current-target readiness | PASS WITH GAPS | 32/32 internal first-release implementation gate is real. Broader seamless target is not met. |
| 44. Final seamless-system gap | FAIL / REQUIRES CORRECTION | Exact operational blockers remain before Token "works perfectly like a glove." |
| 45. Scope-creep check | PASS | Required fixes can remain inside Token/host contracts without absorbing Data, Memory, Brain, Connections or scheduler ownership. |
| 46. Definition-of-done | PASS WITH GAPS | A testable internal gate exists and is met. Seamless-system definition of done is now documented but not yet satisfied. |

## 13. Enforcement versus prose

### Fully enforced

- protocol validation;
- content exclusion;
- ledger immutability;
- raw evidence retention;
- exact idempotency;
- strong-evidence dedupe;
- schema tamper checks;
- ACTUAL/CALCULATED/UNKNOWN core engine;
- exact money arithmetic;
- pricing snapshot immutability/path safety;
- trusted source authority separation;
- active wall/concurrency math;
- budget UNKNOWN behavior;
- native registry preservation;
- state-preserving uninstall/reinstall;
- privacy reduction in selected agent/export surfaces.

### Partially enforced

- pricing freshness, because the synchronizer exists but concrete network fetchers do not;
- source discovery, because collectors detect sources but there is no default run-all runtime;
- native host integration, because registration/materialization is real but host activation is absent;
- scope isolation, because physical/path safety is enforced while caller authorization is external;
- read cost truth, because CostEngine is enforced but primary reader does not compose it.

### Prose-only or intended

- full collector/pricing/cost readiness envelope described in AI-Verse integration docs;
- automatic operational adoption after native installation;
- complete "what did it cost?" experience through CLI/MCP/Dashboard;
- member/public npm installation;
- hosted cross-platform release proof.

## 14. Contradiction scan

### README vs implementation

**Finding:** README/product architecture implies pricing/cost truth feeds primary CLI/JSON/MCP/Dashboard.

**Implementation:** main reader efficiency is `actual_only`.

**Classification:** implementation gap plus product wording drift.

### Architecture docs vs implementation

**Finding:** architecture blueprint places pricing/derived cost/rollups inside the ledger.

**Implementation:** pricing is a separate immutable Token store; derived calculations are not canonical ledger rows.

**Classification:** stale architecture document.

### Status docs vs implementation

Build Map/README agree on 32/32 alpha.1.

Architecture Blueprint still says implementation is in progress.

**Classification:** stale status wording.

### CLI docs vs parser

Documented current commands match implemented parser for summary/query/export and native lifecycle.

No activate/init/collect/prices sync command is documented or implemented.

**Classification:** consistent absence.

### Schemas vs validators

Alpha.1 hardening includes schema/protocol parity tests.

**Classification:** PASS.

### "Supported" vs actual supported path

Standalone support is valid as a library.

Standalone one-command operational product support is not present.

**Classification:** wording requires precision.

### "Ready" vs doctor depth

Doctor proves only a shallower health layer than the broader integration document suggests.

**Classification:** current-vs-intended ambiguity.

### "Integrated" vs direct-storage shortcuts

No direct sibling database shortcuts were found in ecosystem adapters.

**Classification:** PASS.

### "Automatic" vs manual/custom composition

Collectors/pricing synchronizer require caller composition.

**Classification:** product operational gap.

## 15. Negative-space findings

Based on Token's product claim, the following expected capabilities are not currently present as a supported end-to-end path:

1. a fresh standalone initialization command;
2. a default collector composition;
3. a live collection activation mechanism;
4. a host cadence registration/reference implementation;
5. concrete pricing network fetchers;
6. a cost-aware TokenReader/CLI/Dashboard path;
7. a scoped-reader authorization envelope;
8. a deep collector/pricing/cost readiness doctor;
9. an activate/adopt/reconcile transaction for an existing host;
10. durable package-resolution acceptance after native npx install;
11. a released-ledger migration/rollback framework;
12. stale registry-lock recovery;
13. actual current AI-Verse host acceptance;
14. hosted cross-platform release proof.

These are not evidence that the core is broken. They are the exact boundary between the current engine and a finished operational product.

## 16. Readiness-state QC

The current component must not collapse these states:

| State | Current evidence |
|---|---|
| AVAILABLE | local artifact exists |
| INSTALLED | package/native install can complete |
| SUPPORTED | compatible host fixture can pass compatibility |
| ATTACHED | extension registration exists |
| ENABLED | registry field can be enabled |
| HEALTHY, structural | materialization/host/ledger integrity can pass |
| SOURCE-ACTIVE | not generally modeled/proven |
| COLLECTING | not generally modeled/proven |
| PRICING-READY | not generally modeled/proven |
| COST-READY | not generally modeled/proven |
| AUTHORIZED | owned externally, not represented in Token reader |
| READY | no complete aggregate contract |
| INITIALIZED | ledger may exist, but no public initialization lifecycle |
| EXECUTING | only when caller explicitly invokes APIs |
| VERIFIED | local core/release tests only, not full real-host operation |

**LAW:** Token cannot describe ENABLED as READY.

## 17. Completeness matrix

| Dimension | Verdict |
|---|---|
| ENGINE / CORE | COMPLETE WITH LIMITATIONS |
| ARCHITECTURE / CONTRACT | COMPLETE WITH LIMITATIONS |
| INSTALL / PACKAGE | COMPLETE WITH LIMITATIONS |
| HOST INTEGRATION | PARTIAL |
| ATTACH / REGISTER | COMPLETE WITH LIMITATIONS |
| ACTIVATE / ADOPT | MISSING |
| SCOPE INITIALIZATION | PARTIAL |
| MIGRATION / LEGACY | COMPLETE WITH LIMITATIONS |
| HEALTH / DOCTOR | PARTIAL |
| PERMISSION / SAFETY | COMPLETE WITH LIMITATIONS |
| CROSS-COMPONENT READ | COMPLETE WITH LIMITATIONS |
| CROSS-COMPONENT WRITE | NOT APPLICABLE for sibling canonical state |
| UPDATE / UPGRADE | PARTIAL |
| DISABLE / DETACH / UNINSTALL | COMPLETE |
| REINSTALL / RECONCILE | PARTIAL |
| CROSS-PLATFORM | UNVERIFIED |
| ACCEPTANCE | COMPLETE WITH LIMITATIONS |
| RELEASE / DISTRIBUTION | PARTIAL |
| DOCUMENTATION CONSISTENCY | PARTIAL |

## 18. Current milestone verdict

### Repository milestone

**PASS**

The repository's stated first-release implementation milestone is complete:

- 32/32 tasks;
- hardened alpha.1;
- local release gate passing;
- package clean-install acceptance passing.

### AI-Verse current product milestone

**PASS WITH MAJOR GAPS**

If the target is "install Token at any point and have a running AI-Verse/compatible agent adopt it and immediately gain safe ongoing telemetry/cost intelligence," it is not complete.

The remaining work is implementation work, not merely documentation.

## 19. Exact blockers before "works like a glove"

### P0

- operational activation/bootstrap;
- cost-aware primary read composition;
- default collector/discovery/backfill path;
- supported pricing transport/fetchers.

### P1

- real current host acceptance;
- authorized scoped readers;
- deeper readiness/doctor;
- durable package resolution after native installation.

### P2

- stale-lock recovery;
- reconcile/adopt UX;
- future ledger migration/rollback framework;
- documentation corrections;
- immutable remote release/npm publication and hosted cross-platform proof.

## 20. Final documentation verdict

**PASS WITH GAPS**

The three AI-Verse-System Token audit documents should describe Token as:

> a hardened and locally acceptance-tested alpha.1 telemetry/cost engine whose canonical evidence, financial-truth rules and ownership boundaries are strong, but whose final operational activation, pricing transport, cost-aware read composition, host authorization/readiness and public distribution layers remain incomplete.

It would be inaccurate to call Token 100% complete for seamless AI-Verse operation today.

It would also be inaccurate to describe it as an early architecture-only project. Its core implementation is substantial and real.
