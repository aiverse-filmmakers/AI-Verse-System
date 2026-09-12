# AI-Verse Apps Component Specification

## 1. Executive identity

**Component:** AI-Verse Apps  
**Repository:** `aiverse-filmmakers/AI-Verse-Apps`  
**Reviewed branch:** `main`  
**Reviewed revision:** `db5b0115bf59d6eae9149137a40e891968f3a637`  
**Review date:** 2026-09-13  
**Repository state at review:** one tracked file, `README.md`; one root commit; one branch; no implementation tree, tests, CI, releases, issues or pull requests.

**CURRENT:** AI-Verse Apps is a founding architecture and research seed. The repository explicitly states that implementation has not started.

**INTENDED:** AI-Verse Apps becomes the governed application-extension layer through which durable, versioned, permissioned applications can be created, previewed, installed, operated, updated, rolled back, disabled and removed without becoming mini operating systems or hidden sources of canonical truth.

**Current readiness summary:** the architectural seed is coherent and useful, but there is no executable Apps platform yet.

---

## 2. Status vocabulary

This specification uses:

- **CURRENT**: proven by the reviewed repository at the reviewed revision.
- **INTENDED**: desired behavior explicitly described by the repository or accepted system-level architecture.
- **GAP**: required behavior absent, partial or unverified.
- **LAW**: permanent architecture or safety invariant.
- **HISTORICAL**: previous state, repair or milestone relevant to provenance.
- **INSPIRATION**: evidenced external reference that materially influenced the design.

No implementation claim below is promoted from INTENDED to CURRENT unless executable evidence exists.

---

## 3. Role in the complete system

The founding architecture assigns AI-Verse Apps a specific role:

```text
AI-Verse Apps
  -> app definition
  -> package and manifest contract
  -> application lifecycle contract
  -> SDK
  -> sandbox/runtime contract
  -> app versions
  -> app permission requests
  -> app health/compatibility/migration contracts
  -> app-to-Dashboard extension protocol
```

The same document deliberately separates neighboring responsibilities:

- OS governs the environment, workspace/system boundaries, policy and canonical app registration.
- Dashboard hosts or presents installed app surfaces.
- Data owns canonical structured operational records where Data is the declared owner.
- Connections owns safe access to external services and credentials.
- Skills provides reusable capabilities used to build or operate apps.
- Multiple Bots may coordinate builders/operators.
- Brain may decide that an app should exist or change.
- Memory owns historical recall rather than operational application records.

**LAW:** Apps is an extension platform, not a second AI-Verse OS.

---

## 4. Problem the component solves

The repository identifies a product gap between:

1. one-off generated webpages/source folders; and
2. durable software that becomes a governed part of the user's AI environment.

The intended result is a first-class application that can survive the conversation that created it and participate in AI-Verse through stable contracts.

Examples in the founding architecture include:

- CRM;
- production manager;
- website builder;
- content planner;
- analytics/dashboard applications.

The differentiator is not merely code generation. It is durable installation, versioning, permissioning, safe host integration and lifecycle management.

---

## 5. Current architecture

### 5.1 CURRENT architecture

There is no executable architecture yet.

The entire current repository is:

```text
AI-Verse-Apps/
└── README.md
```

There is no current:

- package manager metadata;
- manifest schema;
- manifest validator;
- package format;
- installer;
- app registry implementation;
- SDK;
- runtime;
- sandbox;
- verifier;
- preview server;
- migration engine;
- permission engine;
- health engine;
- Dashboard adapter;
- OS adapter;
- CLI;
- API;
- test suite;
- CI workflow;
- release artifact.

### 5.2 INTENDED architecture

The founding document proposes a future shape around:

```text
packages/
  manifest/
  sdk/
  runtime/
  sandbox/
  installer/
  verifier/
templates/
examples/
docs/
tests/
```

That layout is illustrative only and does not constitute a committed implementation specification.

### 5.3 Architecture-vs-operation classification

| Area | Current classification |
|---|---|
| product identity | architecture/prose present |
| ownership boundaries | architecture/prose present |
| manifest | illustrative example only |
| package format | intended only |
| lifecycle state machine | intended only |
| SDK | intended only |
| sandbox/runtime | intended only |
| permission request model | intended only |
| app registry format | intended only |
| OS registration integration | intended boundary only |
| Dashboard hosting protocol | intended boundary only |
| Data/Connections/Skills bindings | intended boundary only |
| preview/security review | intended workflow only |
| update/rollback | intended only |
| health | intended only |
| import/export | intended only |
| signing/trust | intended only |
| implementation acceptance | absent |
| production/member path | absent |

---

## 6. Canonical ownership

The founding architecture establishes a strong ownership direction.

### 6.1 What Apps should own

**INTENDED:**

- app manifest specification;
- app package format;
- application lifecycle contract/state machine;
- app SDK;
- sandbox/runtime contract;
- permission request model;
- compatibility model;
- migration contract;
- app health contract;
- versioning and rollback contract;
- development/preview mode;
- import/export package contract;
- app-to-Dashboard extension protocol;
- app registry **format**, subject to the registration-state split below;
- trusted publishing/signing model if an ecosystem is created.

### 6.2 Registration-state split

The README states both:

- OS owns app registration; and
- Apps should eventually own the app registry format.

These statements can be coherent, but the exact contract is not yet defined.

The clean ownership interpretation is:

- Apps defines the versioned app registration schema/protocol.
- OS owns the authoritative registration records for an AI-Verse installation because registration changes the OS-visible environment.
- Apps tooling requests registration changes through the OS-owned boundary rather than maintaining a second independently editable registry.

**GAP:** no schema, API or state-location contract currently proves this split.

**LAW:** defining a registry format does not imply owning a second canonical registry instance.

---

## 7. Explicit non-ownership

The founding architecture explicitly rejects Apps becoming:

- the operating system;
- canonical Memory;
- the structured-data engine;
- a Bot framework;
- a Skills registry;
- an OAuth/token vault;
- Dashboard itself;
- mandatory cloud hosting;
- unrestricted host code execution.

Additional source-of-truth consequences follow from those boundaries.

**LAW:** App convenience must not silently absorb ownership from the canonical component responsible for the data or capability.

---

## 8. Sources of truth

### 8.1 CURRENT

The repository itself has no runtime state, so no current operational source-of-truth hierarchy exists.

### 8.2 INTENDED canonical categories

A mature Apps platform needs an explicit truth map.

| State class | Intended canonical owner |
|---|---|
| app identity/version/package contents | Apps package/install contract |
| app manifest | signed/versioned app package or Apps-owned package metadata |
| system app registration | OS-owned registration state using Apps-defined schema/protocol |
| enablement/scope assignment | OS/host policy/registration boundary |
| granted permissions | canonical host/policy owner, not app-local shadow state |
| structured business/operational records | Data or another explicitly declared canonical source |
| external credentials/tokens | Connections or owning credential system |
| reusable executable capabilities | Skills |
| historical recall | Memory |
| Dashboard navigation/presentation | derived host projection |
| app UI cache | rebuildable, scoped derived state only |
| ephemeral session state | app/runtime-local if non-canonical |
| app preferences | owner must be declared explicitly; not yet specified |
| app runtime logs/telemetry | operational evidence, not business truth |

### 8.3 Hidden-truth prohibition

The founding document's most important Apps-specific law is:

> structured operational data belongs to AI-Verse Data or another explicitly declared canonical source, not hidden app state.

Therefore an app must be deletable and rebuildable without losing records that another canonical owner is responsible for.

A local database inside an app is not automatically forbidden. It is forbidden to become an undeclared competing canonical store.

If an app legitimately owns a domain-specific canonical store in the future, that ownership must be:

- explicit in the manifest/contract;
- isolated by scope;
- exposed through a supported boundary;
- included in migration/export/backup rules;
- non-duplicative with Data or another owner.

The current repository does not yet define such an exception mechanism.

---

## 9. Write paths

### 9.1 CURRENT

No executable write path exists.

### 9.2 INTENDED

A UI mutation should not mean "write directly to whatever local database the app happens to have."

For canonical external state, the required shape is:

```text
user/agent interaction
  -> app UI/runtime
  -> declared operation
  -> current system + workspace scope
  -> permission/approval check
  -> canonical owner resolution
  -> owner-owned API/contract
  -> owner revalidation
  -> durable canonical effect
  -> receipt/provenance
  -> app projection refresh
```

**LAW:** the final write belongs to the canonical owner.

**GAP:** no write protocol, identity/fingerprint model, permission envelope, idempotency contract or mutation receipt exists yet.

---

## 10. Read paths and projections

### 10.1 CURRENT

No executable read path exists.

### 10.2 INTENDED

A mature app should consume:

- Data through a bounded Data API/projection;
- Connections through scoped handles;
- Skills through granted capabilities;
- Memory through the appropriate historical-recall boundary if needed;
- OS state through supported registration/context APIs.

The Dashboard should consume app registration/surface metadata as a projection, not copy app business logic or canonical records.

**LAW:** app and Dashboard views are projections unless explicitly declared canonical owners.

**LAW:** a view/cache may be stale or disposable, but it must never silently become the only surviving business truth.

---

## 11. Runtime model

### CURRENT

No runtime exists.

### INTENDED

The repository expects agent-generated apps to be treated as untrusted until verified and recommends:

- sandboxed execution;
- explicit capability manifests;
- least-privilege permissions;
- no arbitrary host filesystem access;
- no direct secret exposure;
- scoped Data access;
- scoped Connections access;
- CSP for hosted UI;
- outbound-network control where practical;
- dependency/package scanning;
- generated-code review gates;
- auditability of mutations;
- version pinning;
- signed/trusted packages for shared apps;
- explicit approval for permission expansion.

**GAP:** none of these controls are enforced by code at the reviewed revision.

---

## 12. Scope and isolation

### CURRENT

Isolation is architectural prose only.

### INTENDED

The README explicitly requires multi-system isolation.

An app named `App X` installed in System A and another `App X` in System B are separate installations unless explicit export/import is performed.

They must not implicitly share:

- data;
- provider sessions;
- permissions;
- app configuration;
- Connections;
- local state.

Future multi-user behavior should integrate with an AI-Verse identity/access layer rather than create a separate identity system inside Apps.

**GAP:** there is no current system/workspace identity model inside Apps, no scope validator, no physical path containment, no provider/session partitioning and no cross-system regression tests.

---

## 13. Current lifecycle

There is no executable lifecycle.

The README describes future concepts only.

### Install

**CURRENT:** absent.

### Attach/register

**CURRENT:** absent.

The architecture says OS owns app registration, but no registration protocol exists.

### Enable

**CURRENT:** absent.

### Activate/adopt

**CURRENT:** absent.

No command or host transaction exists that makes a newly installed app usable inside a running OS.

### Initialize

**CURRENT:** absent.

No app-scope initialization contract exists.

### Migrate/import

**CURRENT:** absent.

Migration requirements are listed as a future manifest concern.

### Doctor/status

**CURRENT:** absent.

Health checks are listed as a future manifest/contract concern.

### Update

**CURRENT:** absent.

Updates are expected to be versioned and permission-expanding updates must require explicit review.

### Disable

**CURRENT:** absent.

### Detach

**CURRENT:** absent.

### Uninstall

**CURRENT:** absent.

### Reinstall/reconcile

**CURRENT:** absent.

### Rollback

**CURRENT:** absent.

---

## 14. Intended lifecycle

The founding README gives the broad application flow:

```text
idea
 -> generated draft
 -> preview
 -> automated checks
 -> permission review
 -> user approval where required
 -> install
 -> operate
 -> update
 -> rollback if necessary
```

For seamless OS integration, that needs to become a deterministic host contract.

A recommended target, derived from the repo's explicit ownership rules and the system lifecycle laws, is:

```text
AVAILABLE PACKAGE
  -> manifest parsed
  -> package verified
  -> compatibility checked
  -> requested scopes/capabilities inspected
  -> preview/security checks
  -> user approval where required
  -> OS registration transaction
  -> app installed for target system/workspace
  -> app enabled
  -> required canonical schemas/resources initialized through owners
  -> runtime starts in sandbox
  -> dependency health verified
  -> Dashboard discovers declared surfaces
  -> app becomes READY
```

The states must remain distinct:

```text
AVAILABLE
INSTALLED
REGISTERED
ENABLED
INITIALIZED
HEALTHY
READY
AUTHORIZED
RUNNING
```

No state should imply the next without a contract proving it.

---

## 15. How OS should discover Apps and individual applications

This is not implemented today.

Two discovery problems must be kept separate.

### 15.1 Discovering the AI-Verse Apps platform

The Apps platform itself should eventually be installable independently and attachable to an existing compatible host.

**GAP:** AI-Verse Apps currently has no package identity, host adapter, component manifest, attach command or doctor surface.

A seamless host should not require hardcoding one repository path.

### 15.2 Discovering individual app packages

The Apps platform should define a self-describing, versioned app manifest.

OS should consume the supported Apps contract rather than inspect arbitrary source trees.

The minimum discoverable metadata should eventually include:

- stable app ID;
- app version;
- package format version;
- origin/author/provenance;
- compatible OS/Apps contract versions;
- target scope;
- UI surfaces;
- runtime/entrypoints;
- required Data schemas;
- required Skills/capabilities;
- required Connections;
- requested permissions;
- migrations;
- health checks;
- background behavior;
- update/rollback metadata.

**GAP:** the example YAML in the README is illustrative and explicitly not a fixed schema.

---

## 16. How installation should work

A correct future installation should preserve ownership.

### Required responsibilities

**Apps should:**

- validate package/manifest;
- verify package provenance/integrity;
- compute permission requirements;
- prepare app-owned package/runtime artifacts;
- expose migrations/checks through a stable contract.

**OS/host should:**

- validate target system/workspace;
- apply host policy;
- perform/record authoritative registration;
- grant only approved capability handles;
- preserve existing unrelated registrations;
- refuse incompatible or unsafe packages.

**Canonical owners should:**

- initialize or migrate their own state on request;
- perform final writes through their own boundaries.

**Dashboard should:**

- render registered/ready surfaces;
- not copy the app into a second canonical store.

### GAP

None of those steps currently exist as commands or APIs.

---

## 17. How activation should work

Installation must not equal activation.

A future app may be installed but:

- disabled;
- awaiting permission approval;
- awaiting required connection setup;
- awaiting Data schema initialization;
- incompatible;
- unhealthy.

Activation should therefore be a separate host transaction that:

1. selects the target system/workspace;
2. resolves the exact installed app version;
3. revalidates compatibility;
4. rechecks current requested permissions;
5. resolves dependency handles;
6. verifies required canonical resources;
7. starts/authorizes the runtime only within the granted envelope;
8. exposes Dashboard surfaces only when the readiness contract permits.

**LAW:** later installation must not require rebuilding the OS.

**LAW:** activation must not silently widen permissions or transfer unrelated canonical authority.

**GAP:** no activation/adoption implementation exists.

---

## 18. Install-order independence

### CURRENT

Unverified because no install/attachment implementation exists.

### INTENDED

The architecture should support at least:

- OS first, Apps platform later;
- Apps platform available first, OS attached later;
- individual app installed after a long-running OS already exists;
- optional Data/Skills/Connections becoming available later;
- app disabled/detached and re-enabled/reinstalled later.

Chronology must not decide ownership.

A late-installed dependency should be discoverable through reconciliation rather than requiring manual source edits.

---

## 19. Migration and history integration

### CURRENT

No migration engine or import/export implementation exists.

### INTENDED

The app contract should describe migration requirements and import/export packaging.

Important migration classes include:

- app version N to N+1;
- package/runtime format evolution;
- Data schema migration through Data-owned boundaries;
- app configuration migration;
- movement between AI-Verse systems;
- import of an externally built application into Apps format;
- reinstall over preserved state.

### LAW

Migration must not create two editable canonical copies.

### GAP

No ownership-specific migration protocol, transaction model, rollback, resumability, backup behavior or verification step is defined.

---

## 20. Portability outside AI-Verse OS

### CURRENT

Architecture only.

### INTENDED

The README says the distinction between Apps lifecycle and Skills/Bots should allow other agents/runtimes to build AI-Verse Apps without one specific coding agent.

Local-first operation is preferred, with cloud/remote/public deployment available through adapters rather than required architecture.

A mature portability model should separate:

- portable app package/manifest core;
- AI-Verse OS registration adapter;
- Dashboard surface adapter;
- runtime-specific build/operator adapters;
- optional external deployment adapters.

**LAW:** portability may not weaken scope, ownership, permission or provenance requirements.

**GAP:** no portable SDK, runtime protocol or host adapter exists yet.

---

## 21. Sibling integration contracts

The repository contains intended boundaries, not tested integrations.

### Data

**INTENDED:** app -> Data API -> canonical structured records.

**GAP:** no versioned Data client/contract, scope binding, query model, schema registration or mutation receipt.

### Connections

**INTENDED:** apps receive scoped connection handles rather than raw credentials.

**GAP:** no connection-handle contract or permission binding.

### Skills

**INTENDED:** Skills provide reusable build/operate capabilities.

**GAP:** no capability-resolution contract or app runtime binding.

### Multiple Bots

**INTENDED:** Bots may build or operate apps; Apps does not implement its own multi-agent system.

**GAP:** no task/build contract.

### Brain

**INTENDED:** Brain may contribute intent/planning/evaluation.

**GAP:** no app-generation planning contract.

### Dashboard

**INTENDED:** Dashboard hosts surfaces through a controlled extension contract.

**GAP:** no extension protocol.

### OS

**INTENDED:** OS owns environment policy and app registration.

**GAP:** no app registration/discovery lifecycle contract.

No sibling repository was audited to fill these gaps. They are recorded only from explicit Apps-repository statements.

---

## 22. Permissions, security and privacy

### CURRENT

Prose-only requirements.

### INTENDED laws

1. App permissions are explicit and least-privilege.
2. Agent-generated code is untrusted until verified.
3. Raw secrets are not exposed when scoped handles can be used.
4. Workspace/system isolation cannot be bypassed.
5. Permission-expanding updates require explicit review.
6. Arbitrary host filesystem access is not a default capability.
7. App-originated mutations are auditable.
8. Package/version identity is pinned and reviewable.

### Missing enforcement

No:

- schema validator;
- permission evaluator;
- approval token/binding;
- sandbox;
- path containment;
- network policy;
- secret broker;
- update permission diff;
- package signature;
- trust root;
- dependency scanner;
- audit event schema;
- security regression tests.

---

## 23. Idempotency and concurrency

### CURRENT

No implementation exists.

### Required future behavior

App lifecycle operations should be replay-safe:

- install same package twice;
- re-run registration;
- retry initialization;
- retry migration after interruption;
- disable already-disabled app;
- uninstall already-uninstalled package;
- reconcile after partial failure.

Shared registration and package state will require deterministic locking or transactional semantics.

Canonical owner writes should use durable idempotency at the effect boundary.

**GAP:** no idempotency identities, locks, transaction logs or recovery semantics are defined.

---

## 24. Failure and degraded modes

The intended design should fail closed when:

- manifest invalid;
- package untrusted;
- incompatible contract version;
- requested permissions not approved;
- required Data/Connection/Skill unavailable;
- scope identity invalid;
- migration cannot be safely completed;
- app update widens privileges without approval;
- runtime sandbox cannot be established.

Optional dependencies should degrade only the dependent capability.

An app should not fall back to direct raw credentials, direct sibling database access or unrestricted host execution when a governed integration is unavailable.

**CURRENT:** none of these semantics are implemented.

---

## 25. Local-first behavior

### INTENDED

Apps should be able to run against a local AI-Verse installation without forcing AI-Verse into hosted SaaS.

Cloud hosting, remote deployment, team deployment and public website deployment should be adapter choices.

### GAP

No runtime/distribution implementation exists, so:

- local data locations are undefined;
- offline behavior is undefined;
- telemetry defaults are undefined;
- secret persistence is undefined;
- remote execution boundaries are undefined.

---

## 26. Cross-platform behavior

### CURRENT

Unverified.

No code or CI exists for Linux, macOS or Windows.

### INTENDED

Because the wider architecture is local-first and host-portable, the eventual runtime/package contract should avoid unnecessary shell/path assumptions and test supported OS/runtime matrices.

---

## 27. Historical evolution and repairs

### HISTORICAL

The repository has one visible commit:

`db5b0115bf59d6eae9149137a40e891968f3a637`  
`docs: establish AI-Verse Apps founding architecture`

It is the root commit and adds the single README.

No earlier implementation generation exists in the reviewed repository.

No issues, pull requests or repair sequence were found.

Therefore:

- there are no historical implementation defects to promote into repair-derived laws;
- the current laws come from founding architecture intent, not repaired runtime failures.

---

## 28. Inspirations and curation

### INSPIRATION: Kylon

The founding README explicitly credits Kylon for highlighting the value of agents creating and operating durable applications inside the workspace.

Adopted lesson:

- applications should be first-class, persistent workspace objects rather than throwaway generated code.

### INSPIRATION: Lovable

Adopted lesson:

- natural-language requests can become working applications.

### INSPIRATION: Replit

Adopted lesson:

- full application generation and iteration can be integrated into an AI development experience.

### INSPIRATION: Retool

Adopted lesson:

- durable operational/internal tools can sit close to structured data and workflows.

### AI-Verse-specific adaptation

The README explicitly rejects simply cloning one product.

The intended improvement is to combine application generation with:

- local-first operation;
- strict source-of-truth boundaries;
- modular sibling ownership;
- permission governance;
- install/update/rollback lifecycle;
- safe Data/Connections/Skills integration.

No separate licenses/notices or copied third-party implementation were found because there is no third-party code in the repository.

---

## 29. Contradictions and ambiguities

### 29.1 No implementation-status contradiction

The repository clearly says implementation has not started, so missing code is not documentation drift.

### 29.2 Registry ownership ambiguity

**AMBIGUITY:** OS owns app registration, while Apps should own app registry format.

Required clarification:

- Apps owns contract/schema/package semantics.
- OS owns authoritative registration state for each system.
- one party performs each canonical write.

This must become explicit before implementation.

### 29.3 Local state ownership is underspecified

The README correctly prohibits hidden operational truth but does not fully classify:

- app preferences;
- app-specific configuration;
- generated assets;
- draft/unpublished content;
- runtime session state;
- logs;
- local indexes/caches.

Before SDK/runtime implementation, each class needs canonical vs derived/disposable rules.

### 29.4 Background behavior owner is underspecified

The manifest is expected to describe background behavior, but the repository does not define who schedules it.

Apps should not silently invent a competing universal scheduler.

### 29.5 App identity and package trust are underspecified

Stable ID, author/origin, provenance, signing and publishing are listed but no trust model exists.

---

## 30. Current intended milestone

The repository's explicit current status is:

> Founding architecture / research seed  
> Implementation status: Not started

Its own milestone list says the first implementation milestone would be:

1. define the stable App manifest and lifecycle.

The current repository does not claim that milestone is complete. It says exact schemas are intentionally not fixed and implementation phases should be researched before construction.

### Verdict

**CURRENT-TARGET VERDICT: COMPLETE AS A FOUNDING RESEARCH SEED, NOT COMPLETE AS MILESTONE 1 AND NOT USABLE AS AN APPLICATION PLATFORM.**

The seed succeeds at:

- identifying the product category;
- defining the north star;
- separating major component responsibilities;
- establishing non-negotiable invariants;
- capturing inspiration;
- outlining a sensible future milestone sequence.

It intentionally does not yet provide:

- stable contracts;
- code;
- lifecycle commands;
- host integration;
- acceptance;
- distribution.

---

## 31. Implementation completeness by dimension

| Dimension | Status | Evidence / reason |
|---|---|---|
| ENGINE / CORE | MISSING | no implementation |
| ARCHITECTURE / CONTRACT | PARTIAL | strong founding architecture; exact schemas/contracts explicitly unfixed |
| INSTALL / PACKAGE | MISSING | no package format or installer |
| HOST INTEGRATION | MISSING | no OS adapter/protocol |
| ATTACH / REGISTER | MISSING | only ownership intent |
| ACTIVATE / ADOPT | MISSING | no path |
| SCOPE INITIALIZATION | MISSING | no implementation |
| MIGRATION / LEGACY | MISSING | future requirement only |
| HEALTH / DOCTOR | MISSING | future requirement only |
| PERMISSION / SAFETY | ARCHITECTURE ONLY | strong intended controls, zero runtime enforcement |
| CROSS-COMPONENT READ | ARCHITECTURE ONLY | intended Data/Connections/Skills boundaries |
| CROSS-COMPONENT WRITE | ARCHITECTURE ONLY | canonical owner law, no protocol |
| UPDATE / UPGRADE | MISSING | intended version/rollback model only |
| DISABLE / DETACH / UNINSTALL | MISSING | intended lifecycle only |
| REINSTALL / RECONCILE | MISSING | no implementation |
| CROSS-PLATFORM | UNVERIFIED | no runtime or CI |
| ACCEPTANCE | MISSING | no tests |
| RELEASE / DISTRIBUTION | MISSING | no releases/package/license metadata |
| DOCUMENTATION CONSISTENCY | COMPLETE WITH LIMITATIONS | README accurately labels the project a seed; registry/local-state details remain intentionally unresolved |

---

## 32. Command/lifecycle matrix

| Stage | Exists? | Command/API | Idempotent? | State owner | Acceptance evidence | Gap |
|---|---|---|---|---|---|---|
| install Apps platform | no | none | unverified | not defined | none | package/distribution missing |
| discover Apps platform | no | none | unverified | host/OS intended | none | component discovery contract missing |
| install individual app | no | none | unverified | Apps + OS split intended | none | package/installer missing |
| attach/register app | no | none | unverified | OS registration intended | none | registration API/schema missing |
| enable | no | none | unverified | host policy intended | none | state machine missing |
| activate/adopt | no | none | unverified | host + Apps intended | none | activation transaction missing |
| initialize | no | none | unverified | canonical owners by resource | none | init contracts missing |
| migrate/import | no | none | unverified | owner-specific | none | migration framework missing |
| doctor/status | no | none | unverified | Apps/host split not fixed | none | health contract missing |
| update | no | none | unverified | Apps package + host policy | none | updater/permission diff missing |
| disable | no | none | unverified | host registration intended | none | lifecycle missing |
| detach | no | none | unverified | OS registration intended | none | lifecycle missing |
| uninstall | no | none | unverified | package owner + preserved canonical state | none | lifecycle missing |
| reinstall | no | none | unverified | package owner + OS | none | rediscovery missing |
| reconcile | no | none | unverified | host/OS likely coordinator | none | reconciliation missing |
| rollback | no | none | unverified | Apps package lifecycle | none | version/rollback missing |

---

## 33. Exact remaining work before Apps plugs into AI-Verse seamlessly

This list is the minimum implementation path implied by the current architecture, not a claim that all final ecosystem features are required for the first prototype.

### P0. Freeze ownership before coding

1. Specify Apps-owned package/manifest state versus OS-owned registration state.
2. Classify app local state into canonical, derived/cache, session, log and user-preference categories.
3. Define who owns background scheduling/execution.
4. Define app IDs, installation IDs, system/workspace scope IDs and version identity.

### P1. Stable application contract

5. Define a versioned manifest schema.
6. Define compatibility/version negotiation.
7. Define declared Data, Connections, Skills and runtime requirements.
8. Define permission request semantics and permission-expansion diff rules.
9. Define package layout, integrity/provenance and migration metadata.
10. Define app surfaces/entrypoints without binding them to one Dashboard implementation.

### P2. Reference Apps engine

11. Implement manifest parser/validator.
12. Implement package verifier.
13. Implement app installation store that contains only Apps-owned package artifacts.
14. Implement lifecycle state machine.
15. Implement scoped runtime/sandbox.
16. Implement lifecycle idempotency and locking/recovery.
17. Implement status/doctor with truthful health depth.
18. Implement update and rollback.
19. Implement disable/uninstall/reinstall while preserving externally owned canonical data.

### P3. OS integration

20. Define a versioned Apps-to-OS registration API.
21. Make registration idempotent and scope-bound.
22. Ensure OS remains authoritative for installed/registered/enabled app state.
23. Implement late discovery/reconciliation so an existing OS can adopt Apps installed later.
24. Keep availability, registration, enablement, health, readiness and authorization distinct.
25. Ensure app removal cannot delete sibling-owned canonical records by accident.

### P4. Canonical data and capability integration

26. Implement Data reads/writes through Data-owned boundaries.
27. Implement scoped Connections handles with no raw-secret fallback.
28. Implement Skills capability resolution through supported capability contracts.
29. Define receipts/provenance for app-originated durable effects.
30. Recheck scope and permission at the actual owner write edge.

### P5. Dashboard projection

31. Define the controlled app-surface protocol.
32. Make Dashboard discover only registered/ready surfaces.
33. Ensure Dashboard can be deleted/rebuilt without loss of app/business truth.
34. Prevent Dashboard from importing/copying app business logic into a second canonical implementation.

### P6. Preview and trust

35. Implement untrusted preview mode.
36. Implement automated package/security checks.
37. Implement explicit approval for initial privileged install where required.
38. Implement explicit approval for permission-expanding updates.
39. Add dependency/package scanning and trust/signature model appropriate to distribution.

### P7. Acceptance and release

40. Add unit/contract/security tests.
41. Add install-order tests.
42. Add cross-system isolation tests.
43. Add lifecycle replay/partial-failure tests.
44. Add real supported-path integration acceptance with OS and Dashboard contracts when those contracts are available.
45. Test supported Linux/macOS/Windows runtime matrices.
46. Publish immutable versioned artifacts.
47. Document exact installation, activation, update, rollback and removal paths.
48. Prove one manually authored app can install, appear, read/write through canonical owners, update, disable, rollback and uninstall without hidden truth.

Only after these are proven should the Apps platform be described as seamlessly integrated.

---

## 34. Definition of done

### 34.1 Current seed definition of done

The founding seed is done when it:

- names the product category;
- establishes responsibility boundaries;
- records non-negotiable source-of-truth laws;
- records security direction;
- records initial inspirations;
- identifies initial milestones without pretending implementation exists.

**Verdict:** met.

### 34.2 Milestone 1 definition of done

"Define the stable App manifest and lifecycle" is done only when:

- the manifest is versioned and machine-validated;
- lifecycle states and transitions are explicit;
- ownership of registration and app-local state is unambiguous;
- permission, scope, compatibility, migration and health fields are specified;
- invalid examples fail deterministically;
- the contract is tested.

**Verdict:** not started.

### 34.3 Seamless-system definition of done

Apps works "like a glove" when:

1. Apps can be installed before or after OS.
2. OS discovers it without manual source edits.
3. A valid app package can be discovered without hardcoded app names.
4. User can preview requested permissions.
5. Installation performs only Apps-owned package changes plus an OS-owned registration transaction.
6. Required canonical resources are initialized through their owners.
7. The app is activated for an explicit system/workspace.
8. Runtime executes inside the granted sandbox/capability envelope.
9. Dashboard discovers the ready app surface.
10. Reads come from declared canonical sources.
11. Writes are performed by canonical owners.
12. App/Dashboard caches can be deleted and rebuilt.
13. Cross-system state cannot leak.
14. Raw credentials are not exposed where scoped handles exist.
15. Permission-expanding updates require approval.
16. Update and rollback preserve canonical user state.
17. Disable/detach/uninstall are reversible where appropriate.
18. Reinstall/reconcile can rediscover preserved compatible state.
19. Doctor reports truthful structural/runtime/dependency/operational health.
20. Supported install and lifecycle paths are proven in CI/acceptance.
21. Immutable release artifacts match documentation.
22. No app, Dashboard surface or local cache has become a hidden canonical truth store.

---

## 35. Open decisions

1. Exact OS-registration vs Apps-registry-format split.
2. App package format and implementation language/runtime neutrality.
3. Sandbox technology by host platform.
4. App-local state taxonomy and allowed canonical exceptions.
5. Identity model for app package ID versus installation ID.
6. Background behavior and scheduler ownership.
7. Runtime/network isolation policy.
8. Trust/signing model and who can establish trust.
9. Permission vocabulary and relationship to OS policy.
10. Data schema declaration/migration handshake.
11. Dashboard surface protocol.
12. App export/import semantics across systems.
13. Multi-user identity/role integration when the wider platform supports it.
14. Whether public apps can declare their own canonical stores, and under what governance.
15. Minimum first supported host/runtime matrix.

These should be decided before implementation choices accidentally become architecture.

---

## 36. Permanent laws established by the founding architecture

Even without runtime repairs, the repo establishes important laws:

1. An app never becomes a second OS.
2. Application code is untrusted until verified.
3. Permissions are explicit and least-privilege.
4. Raw secrets are avoided when scoped handles can be used.
5. System/workspace isolation is mandatory.
6. Structured operational truth belongs to the declared canonical owner, not hidden app state.
7. Dashboard is a host/presentation surface, not the application's source of truth.
8. Apps must be removable without corrupting the OS.
9. Updates are versioned and rollbackable.
10. Permission-expanding updates require review.
11. A visual convenience layer must remain rebuildable from canonical state.
12. App installation must not silently create duplicate canonical ownership.

---

## 37. Contribution to the supreme AI-Verse vision

Apps turns AI-Verse from a fixed set of product screens into a governed self-extension platform.

Its supreme-system contribution is not "more UI."

It is the contract that allows:

```text
repeatable user need
  -> planned software
  -> generated/verified app
  -> governed installation
  -> canonical integrations
  -> durable user-facing capability
```

without sacrificing:

- one canonical owner per responsibility;
- local-first operation;
- isolation;
- permissions;
- provenance;
- portability;
- upgrade/rollback safety.

---

## 38. Final verdict

**CURRENT:** AI-Verse Apps is a well-framed founding architecture seed at exactly one commit and one README.

**INTENDED:** it should become a first-class, host-portable app platform with a stable package/manifest contract, safe runtime, versioned lifecycle and controlled integrations.

**GAP:** the complete executable layer is still absent.

The most important implementation rule is to preserve the founding source-of-truth discipline from the first line of code. Apps and Dashboard must remain clients/projections of canonical owners unless a new ownership contract is explicitly declared.

The correct next work is not to begin with a large visual app builder. It is to freeze the app contract, ownership split, lifecycle and security model, then prove one manually authored app end to end through supported OS registration and canonical read/write paths.
