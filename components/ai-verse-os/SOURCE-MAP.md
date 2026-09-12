# AI-Verse OS Source Map

**Repository:** `aiverse-filmmakers/AI-Verse-OS`  
**Reviewed branch:** `main`  
**Reviewed head:** `3bb28154748f693ba2fd7f5473cc086ddc9d975f`  
**Fresh standalone review:** 2026-09-13  
**Scope rule:** only AI-Verse-OS repository evidence was used to reconstruct the component specification. Cross-component facts appear only where the OS repository itself encodes them in contracts, tests, CI or historical audit documents.

---

## 1. Repository inventory

Fresh tree review found:

- 241 tracked files;
- approximately 38.2 MB tracked;
- much of the size comes from 3D Brain media/build output and generated runtime adapter peers;
- canonical built-in capability sources are under `system/capabilities/`;
- `.claude/skills/` and `.agents/skills/` contain generated/runtime peer copies and must not be counted as three independent designs.

This distinction mattered during the audit because duplicated generated packages can make the repository look architecturally broader than it is.

---

## 2. Root identity and architecture evidence

### `README.md`

Evidence for:

- public product identity;
- domain-neutral AI OS framing;
- install commands;
- Unified Workspace Architecture;
- workspace model;
- system/user/derived ownership;
- knowledge lifecycle;
- source-of-truth summary;
- Four Cs / Three Ms;
- foundation capabilities;
- 3D Brain;
- privacy;
- legacy installations.

### `AI-VERSE.yaml`

Machine-readable architecture source.

Evidence for:

- schema version 2.0;
- architecture name `unified-workspace`;
- system-owned/user-owned/derived paths;
- current-context resolver;
- source-of-truth map;
- routing order;
- knowledge lifecycle;
- domain adaptation;
- privacy;
- legacy compatibility;
- named Memory support declaration that now coexists with the broader generic local extension registry.

### `AGENTS.md`

Canonical runtime behavior contract.

Evidence for:

- startup sequence;
- extension loading;
- ownership-aware current-context use;
- progressive disclosure;
- system/user/derived separation;
- component boundaries;
- Data host boundary;
- permission rules;
- extension rules;
- Brain-owned strategic behavior;
- no full-system eager load.

### `CLAUDE.md`

Evidence that runtime-specific entry material is intended to point back to the canonical runtime contract rather than become a second constitution.

### `EXPANSIONS.md`

Evidence for:

- stable top-level layers;
- workspace-first growth;
- promotion rules;
- future optional domain packs;
- new-top-level-folder test;
- anti-patterns.

This file is especially important for preventing scope creep in the final system.

### `.gitignore`

Evidence for privacy and ownership behavior:

- local extension/direction state ignored;
- operator state ignored;
- user knowledge ignored;
- workspaces ignored except template;
- registries ignored;
- automation definitions ignored;
- runtime ignored;
- generated/private app data ignored.

### `package.json`

Evidence for:

- package name `ai-verse-os`;
- package version `0.1.0`;
- Node >=18 CLI requirement;
- current CLI binary mapping;
- MIT license;
- GitHub repository identity.

---

## 3. Unified architecture evidence

### `system/architecture/README.md`

Canonical UWA design intent.

Key laws:

- one fact, one canonical editable home;
- current context smaller than long-term memory;
- workspace isolation;
- deliberate promotion;
- agents orchestrate rather than duplicate;
- apps/indexes derived;
- user state survives upgrades;
- generated adapters preserve unowned/modified files;
- new top-level structure must earn existence;
- permission floors cannot manufacture approval.

**Drift found:** its final "next capability integration contract" paragraph still describes external provider discovery as later work although provider discovery is now implemented.

### `system/architecture/ownership.md`

Evidence for:

- system-owned vs user-owned vs derived state;
- migration sequence;
- public-template privacy.

### `system/architecture/source-of-truth.md`

Evidence for:

- canonical runtime/architecture/current-state sources;
- Brain direction ownership;
- workspace identity;
- knowledge/decision authority;
- live external data;
- derived data non-authority;
- conflict handling;
- anti-duplication.

### `system/architecture/routing.md`

Evidence for the routing pipeline:

intent -> scope -> direction owner -> current context -> capability -> minimum knowledge -> connections -> execute -> validate -> writeback.

### `system/architecture/knowledge-lifecycle.md`

Evidence for inbox/context/memory/knowledge/decision/capability/archive semantics.

### `system/architecture/domain-adaptation.md`

Evidence for domain-neutral core and local-first specialization.

### `system/schemas/workspace.schema.yaml`

Evidence for:

- canonical workspace ID grammar;
- free-form type/domains;
- status;
- source routes;
- privacy;
- approval floors;
- capabilities/automations extension fields.

### `workspaces/_template/WORKSPACE.yaml`

Practical workspace contract.

---

## 4. User-state layer evidence

### `operator/README.md`

Operator-wide state boundaries.

### `operator/profile/README.md`

Stable identity/preferences/goals/voice semantics.

### `operator/context/README.md`

Compact current cross-workspace startup brief.

### `operator/memory/README.md`

Historical operator memory and derived-index rule.

### `operator/decisions/README.md`

Append/supersede decision behavior.

### `knowledge/README.md`

Shared cross-workspace reusable knowledge boundary.

### `workspaces/README.md`

Workspace isolation and deliberate promotion.

---

## 5. Connections, agents, cadence, apps and runtime

### `connections/README.md`
### `connections/registry.example.yaml`

Evidence that:

- registry is metadata/route truth, not proof of access;
- statuses distinguish planned/configured/verified/degraded/unavailable/retired;
- secrets do not belong in registry;
- scope is explicit.

### `agents/README.md`

Evidence that agents are orchestration definitions, not knowledge stores.

### `automations/README.md`
### `automations/jobs/README.md`
### `automations/triggers/README.md`
### `automations/policies/README.md`

Evidence for Cadence architecture and an important limitation:

> a job/trigger definition is not proof that execution occurs.

### `apps/README.md`

Evidence that apps are persistent interfaces but not canonical truth stores.

### `runtime/README.md`

Evidence for disposable/rebuildable runtime state.

---

## 6. Built-in capability evidence

Canonical sources reviewed:

- `system/capabilities/onboard/SKILL.md`
- `system/capabilities/workspace/SKILL.md`
- `system/capabilities/grill-me/SKILL.md`
- `system/capabilities/link/SKILL.md`
- `system/capabilities/audit/SKILL.md`
- `system/capabilities/level-up/SKILL.md`
- `system/capabilities/3d-brain/SKILL.md`

### Onboard

Evidence for:

- universal seven-question intake;
- resumability;
- existing-state preservation;
- direction-owner gate;
- connection-state honesty;
- minimum workspace setup;
- no automatic Q7 automation;
- no personalization of system-owned files.

### Workspace

Evidence for:

- workspace justification test;
- minimum useful scaffolding;
- direction-owner gate;
- local domain adaptation;
- source routing rather than blind copying;
- promotion discipline;
- no automatic bulk move of existing project folders.

### Grill Me

Evidence for:

- raw interview checkpointing;
- fact/tentative/history/decision classification;
- narrow canonical promotion;
- workflow-to-capability extraction.

### Link

Evidence for:

- routing to authoritative sources rather than duplication;
- explicit authority/scope/access verification.

### Audit

Evidence for:

- deterministic architecture check as only one input;
- architecture/Four-Cs operational inspection;
- evidence classes;
- report lifecycle;
- not modifying system just to improve score.

### Audit rubric

`system/capabilities/audit/rubric.md` provides:

- 100-point evidence model;
- architecture/context/connections/capabilities/cadence weights;
- hard score caps;
- "presence alone" rule.

### Level Up

Evidence for:

- Three Ms operational improvement;
- direction-owner gate;
- EAD;
- autonomy spectrum;
- artifact selection;
- local-first promotion;
- staged rollout.

### 3D Brain

Evidence for:

- app generated from selected actual sources;
- no invented graph chronology/edges;
- app remains derived;
- local-only serving by default;
- real acceptance checklist;
- source category approval;
- Node 22 requirement for full experience.

---

## 7. Capability authoring and registry

### `skills/registry.yaml`

Evidence that:

- canonical materialization is `system/capabilities/`;
- runtime peers are Claude/Codex;
- seven current built-ins are registered;
- workspace-local capabilities should be promoted only when portable/guarded/verifiable.

### `SKILL-AUTHORING.md`

Evidence for the capability taxonomy and authoring standards.

**Drift found:** the file still describes `.claude/skills/<skill-name>/` as the "current materialized authoring source", which conflicts with current canonical-materialization architecture.

---

## 8. Runtime adapter synchronization

### `system/architecture/adapter-synchronization.md`
### `scripts/sync-runtime-adapters.mjs`
### `scripts/test-adapter-sync.mjs`

Evidence for:

- `system/capabilities/` as editable canonical source;
- Claude/Codex generated peers;
- ignored ownership ledger;
- digest-bound safe replacement;
- conflict preservation;
- extension/custom adapter preservation;
- safe removal only for unchanged owned output;
- symlink/path safety;
- fail-closed malformed ownership state.

---

## 9. Strategic direction ownership

### `system/architecture/direction-ownership.md`
### `scripts/direction-owner-core.mjs`
### `scripts/direction-owner.mjs`
### `scripts/current-context.mjs`
### `scripts/test-direction-owner.mjs`
### `scripts/test-current-context.mjs`
### `.github/workflows/direction-owner.yml`

Evidence for:

- one direction owner per scope;
- scope grammar;
- missing pre-handover record defaults to OS;
- malformed state fails closed;
- strategic-write assertion;
- Brain outage not ownership transfer;
- Brain-owned active-context filtering;
- explicit handback acceptance;
- symlink/current-context containment;
- generated runtime peer checks.

---

## 10. Permission boundary

### `system/architecture/action-permissions.md`
### `scripts/action-permission.mjs`
### `scripts/test-action-permission.mjs`
### `.github/workflows/brain-permission-contract.yml`

Evidence for:

- OS outer permission floor;
- action classes;
- default safe policy;
- strict operator/workspace intersection;
- paused/archived denial;
- malformed policy fail-closed;
- exact request binding;
- Brain deny beats OS allow;
- OS deny beats Brain allow;
- OS approval requirement adds restriction;
- late revocation before effect.

---

## 11. Capability Provider v1

### `system/contracts/capability-provider-v1/README.md`

Evidence for:

- canonical cross-repo provider contract;
- provider ownership;
- qualified IDs;
- immutable generation identity;
- package digests;
- contextual readiness semantics;
- receipt/effect boundary;
- migration compatibility;
- acceptance cases.

Important historical note: parts of this contract describe a future implementation stage because the document predates later resolver/host implementation. Current state must be read together with current resolver code/CI.

---

## 12. Capability discovery implementation

### `system/architecture/capability-resolution.md`
### `scripts/capability-resolver-core.mjs`
### `scripts/capability-resolver.mjs`
### `scripts/capability-resolver-cli.mjs`
### resolver tests
### Repository QC Skills-provider integration

Evidence for:

- OS/distributed/local/workspace providers;
- exact workspace scope derivation;
- physical path containment;
- distributed generation validation;
- protected OS aliases;
- relevance-before-limit;
- explicit qualified no-fallback behavior;
- provider degradation semantics;
- readiness intentionally `UNVERIFIED`;
- permission intentionally `unknown`.

---

## 13. Local extension architecture

### `system/extensions/README.md`
### `AGENTS.md`
### `.gitignore`

Evidence for:

- `.aiverse/extensions/registry.json`;
- gitignored attachment state;
- supported/installed/enabled semantics;
- health is live;
- registration is not authority;
- path containment;
- sibling/unknown field preservation contract;
- exact legacy Memory migration principles;
- OS owns contract, component owns its entry/files.

---

## 14. Component doctor and reconciliation

### `scripts/components.mjs`
### `scripts/test-components.mjs`
### Repository QC component step

Evidence for:

- known component list hardcoded to Brain/Memory/Data;
- Skills checked separately;
- absent / available-unattached / attached-enabled / attached-disabled / incompatible states;
- registry lock diagnosis;
- no automatic lock stealing;
- safe engine/instruction path checks;
- local-evidence heuristics;
- plan-only reconcile;
- component-owned suggested commands.

Key gap evidence:

```text
mode: plan-only
mutated: false
```

No generic apply/activation engine is present.

---

## 15. Dynamic AI-Verse host

### `scripts/ai_verse_host_adapter.py`
### `scripts/test-ai-verse-host-adapter.py`

Current code evidence:

- class `AIverseOSHost`;
- adapter ID `ai-verse-os:host`;
- legacy `OSFourComponentHost` alias;
- optional Memory;
- default external Skills root;
- no source checkout requirement;
- legacy skills-entrypoint accepted but unused;
- real connection metadata;
- optional `query_data`;
- permission delegation;
- generation-pinned capability read proof;
- no canonical state ownership.

**Drift evidence:** historical `docs/FOUR-COMPONENT-HOST-ADAPTER.md` is older than this implementation.

---

## 16. Data boundary

### `system/architecture/data-host-integration.md`
### `scripts/data-host.mjs`
### `scripts/test-data-host.mjs`
### `.github/workflows/data-host-boundary.yml`

Evidence for:

- registered Data engine loading;
- no direct SQLite access;
- exact workspace binding;
- explicit discover/init/request;
- action class mapping;
- destructive approval blocking;
- local human actor binding;
- Linux/macOS/Windows x Node 22/24 CI matrix.

---

## 17. Write-command boundary

### `system/architecture/write-command-boundary.md`
### `scripts/write-command.mjs`
### `scripts/test-write-command.mjs`
### `.github/workflows/write-command-boundary.yml`

Evidence for:

- immutable write request;
- SHA-256 fingerprint;
- bounded parameters;
- provenance;
- scope validation;
- idempotency;
- OS permission at enqueue;
- safe runtime queue;
- no canonical effect.

Critical exact semantics:

```text
status: queued
effect_occurred: false
canonical_effect_occurred: false
queue_state: pending_handler
canonical_handler_dispatched: false
```

The documentation explicitly says canonical knowledge/decision routing is later integration work.

This is direct evidence that the owner-controlled canonical write pipeline is incomplete beyond intake/transport.

---

## 18. CLI lifecycle evidence

### `bin/ai-verse-os.mjs`
### `package.json`
### `.github/workflows/cli-smoke.yml`

Current commands:

- install;
- update;
- doctor;
- onboard;
- components doctor;
- components reconcile;
- version.

Current install characteristics:

- Git clone;
- branch `main`;
- non-empty non-OS target refusal;
- required file validation.

Current update characteristics:

- Git checkout required;
- clean tracked OS required;
- fetch/fast-forward `origin/main`;
- no rollback command.

Cross-platform CLI smoke runs on Ubuntu, macOS and Windows with Node 22.

---

## 19. Architecture health evidence

### `system/health/README.md`
### `scripts/check-architecture.sh`
### Repository QC

Current deterministic architecture check covers:

- required files;
- manifest top-level keys;
- workspace template fields;
- approval fields;
- capability canonical-materialization declaration;
- runtime adapter parity;
- tracked user-state privacy warnings.

The health README explicitly says checks should increasingly cover more areas.

Therefore the check is intentionally not equivalent to full operational health.

---

## 20. Release and integration history

### `docs/SHIP-READINESS-AUDIT-2026-09-12.md`

Historical pre-hardening audit.

Used for:

- problems that motivated later fixes;
- install-order/lifecycle model;
- distribution/reproducibility concerns;
- original gaps.

Not all findings remain current.

### `docs/FIVE-COMPONENT-RELEASE-PRD.md`

Canonical release-hardening intent for the first member beta.

Key requirements:

- no tracked OS mutation;
- package availability != attachment;
- install chronology != authority;
- optional absence non-fatal;
- canonical state survives lifecycle;
- one local attachment registry;
- generic dynamic host;
- real connection metadata;
- read-only Data path;
- component doctor/reconcile;
- representative install orders;
- immutable release artifacts.

### `docs/FIVE-COMPONENT-RELEASE-STATUS.md`

Latest reviewed release snapshot.

Evidence that OS, Brain, Memory and Skills hardening were green, while Data's private CI runner execution was still the external five-component release gate at that snapshot.

### `docs/ASTRA-REPAIR-HANDOFF.md`

Closed five-repair sequence.

OS-relevant lessons:

- physical workspace containment;
- ownership-aware context;
- maintained host boundary;
- documentation correctness.

### `docs/FOUR-COMPONENT-HOST-ADAPTER.md`

Historical/public integration doc.

Now partially stale relative to actual dynamic host code.

### `docs/FOUR-REPO-ACCEPTANCE.md`
### `.github/workflows/four-repo-acceptance.yml`

Evidence for executable composition across OS/Memory/Brain/Skills.

Current workflow uses hardened Brain local-registry attach/init rather than old tracked manifest patch.

---

## 21. PR/history evolution reviewed

All visible OS PRs #1 through #23 were closed at review time.

Important sequence:

1. universal architecture v2;
2. capability-provider contract;
3. local extension registry;
4. ownership-safe adapter sync;
5. direction owner;
6. scoped provider discovery;
7. OS/Brain permission intersection;
8-9. four-repo acceptance evolution;
10. cross-workspace symlink repair;
11. frozen strategy repair;
12. Astra handoff;
13. maintained host;
14-15. integration docs/handoff closure;
16. write-command boundary;
17. Data host;
18. five-component dynamic-host hardening;
19. release status;
20. workspace ID normalization;
21. registry lock diagnosis;
22. release status refresh;
23. current acceptance refresh.

No open OS issues were returned by the OS repository search in this review.

---

## 22. CI evidence

### Repository QC

Covers:

- architecture;
- capability resolution;
- components doctor/reconcile;
- adapter synchronization;
- package metadata;
- install docs;
- local extension contract;
- 3D Brain package;
- branding check;
- Memory adapter coexistence;
- real external Skills provider discovery.

### CLI smoke

Ubuntu/macOS/Windows Node 22.

### Direction Ownership

OS ownership and current-context filters.

### OS Brain Permission Contract

Real restrictive intersection with pinned Brain revision.

### OS Write Command Boundary

Owner-controlled queue transport.

### Data Host Boundary

Ubuntu/macOS/Windows x Node 22/24.

### Four Repo Acceptance

OS + Memory + Brain + Skills full composition proof.

This CI structure is strong evidence that several architecture rules are executable rather than prose.

---

## 23. Inspiration/provenance evidence

### `THIRD-PARTY-NOTICES.md`

Explicitly states:

- portions are derived from software copyright 2026 Nate Herk;
- the names "The Three Ms of AI" and "The Four Cs of an AI OS" are identified as trademarks of their original publisher Nate Herk;
- AI-Verse-specific modifications/additions are maintained by AI-VERSE.

This is the strongest evidenced external conceptual provenance in the OS repository.

### 3D Brain third-party notices

`system/capabilities/3d-brain/assets/template/THIRD-PARTY-NOTICES.txt` documents the visualization software stack including 3d-force-graph, three.js, Preact, D3/ngraph ecosystem and supporting packages.

These are renderer dependencies, not OS architecture ownership.

### Evidence limitation

The reviewed OS repo does not name a definitive competitive list of other AI operating systems that inspired UWA.

No such list is inferred.

---

## 24. Documentation contradictions found

### A. Provider discovery status drift

`system/architecture/README.md` says external provider discovery remains later work.

Current resolver implementation/CI proves it exists.

### B. Authoring-source drift

`SKILL-AUTHORING.md` points to `.claude/skills/` as authoring source.

Current registry/architecture says `system/capabilities/` is canonical.

### C. Four-component host drift

Historical host doc requires old framing and Skills entrypoint.

Current adapter is dynamic and no longer requires source checkout.

### D. Named Memory support declaration

`AI-VERSE.yaml` still carries a Memory-specific support block beside generic local extension architecture.

### E. Health wording

Core doctor reports OS ready without automatically checking component doctor or full operational audit.

---

## 25. Evidence limitations

1. This review did not treat other component repositories as primary sources.
2. Cross-component details were accepted only where AI-Verse-OS itself references/tests them.
3. Historical audit claims were not automatically promoted to current truth after later hardening.
4. Repository/account governance settings that could not be verified through the available connector are not asserted as current facts.
5. No unrecorded external inspiration history is invented.
6. Current release status is a point-in-time repository record, not a permanent guarantee.
7. This source map focuses on architecture/product contracts rather than line-by-line implementation.
