# AI-Verse Skills Component Specification

**Component:** AI-Verse Skills  
**Repository reviewed:** `aiverse-filmmakers/AI-Verse-Skills`  
**Reviewed branch:** `main`  
**Reviewed head:** `3ab838e6e64561bbb7cea8f85d0ebc75b9e84337`  
**Declared distribution version:** `1.0.0`  
**Fresh standalone review:** 2026-09-13  
**Method:** `docs/AUDIT-METHODOLOGY.md`

## 1. Executive identity

**CURRENT:** AI-Verse Skills is a standalone, original-first capability distribution and immutable package lifecycle for reusable agent skills.

It currently provides:

- 20 first-party foundation skills;
- 80 curated employee-facing capabilities pinned to exact upstream Git commits;
- 5 non-canonical support packages;
- profiles, roles, operators, aliases and runtime-adapter metadata;
- reproducible acquisition from vendored or pinned upstream sources;
- immutable installed generations;
- atomic activation through one active-generation pointer;
- generation pinning for in-flight execution;
- Provider Contract v1 manifest and capability-index publication;
- integrity doctoring and live operator-readiness checks;
- generic runtime adapter materialization;
- execution-receipt v2 validation semantics;
- first-class AI-Verse OS integration without moving Skills lifecycle ownership into OS.

Skills is not an agent runtime by itself. It installs, describes, validates and exposes procedural capability packages. A host/runtime still executes those capabilities.

**LAW:** a skill is procedural capability, not authority. Installation or discovery never grants filesystem scope, credentials, connections, approval, Memory authority, scheduling authority or strategic authority.

**LAW:** Skills owns distributed package bytes and their immutable lifecycle. AI-Verse OS owns host scope, provider resolution, permissions, approvals, connections and execution routing.

## 2. Current architectural thesis

The implemented path is:

```text
portable skill package
        ↓
curated distribution + provenance
        ↓
immutable installed generation
        ↓
host discovery
        ↓
readiness + permission + approval
        ↓
bounded execution
        ↓
receipt / verification
```

The repository deliberately separates reusable procedural capability from runtime authority. This is the core reason Skills can remain useful inside AI-Verse OS and outside it.

## 3. Canonical ownership

### 3.1 Skills owns

**CURRENT / LAW:**

Skills canonically owns:

- the distributed Skills catalog;
- distributed capability identities;
- distribution profiles;
- source pins and acquisition selectors;
- vendored package provenance;
- immutable generation construction;
- the active generation pointer;
- distributed provider manifest and capability index;
- package integrity verification;
- package/operator dependency metadata;
- generic adapters explicitly materialized by the user;
- Skills-specific readiness/doctor output;
- the Skills-side execution-receipt contract/validator.

Primary current truth surfaces are:

```text
registry/skills.json
registry/packages.json
registry/profiles.json
registry/operators.json
registry/roles.json
registry/runtime-adapters.json

<skills-root>/.aiverse/active.json
<skills-root>/.aiverse/generations/<generation-id>/.aiverse/installed.json
<skills-root>/.aiverse/generations/<generation-id>/.aiverse/capability-index.json
```

### 3.2 AI-Verse OS owns

**CURRENT / LAW:**

OS owns:

- operator/workspace scope;
- authorized roots;
- capability-provider resolution and ranking;
- protected OS aliases;
- connection registry and connection authorization;
- runtime permission floors;
- approvals;
- action routing;
- host-side effect verification;
- contextual readiness/authorization;
- OS-owned capabilities;
- local and workspace capability-provider boundaries.

Skills must not edit tracked OS state merely to become visible.

### 3.3 Skills explicitly does not own

Skills does not canonically own:

- workspace identity;
- OS current context;
- Memory history;
- Brain intent/objectives/strategy;
- Data structured records;
- credentials or OAuth state;
- connection authority;
- global scheduling;
- the model/tool runtime;
- host policy;
- durable user knowledge outside Skills packages.

## 4. Distribution and source-of-truth model

**CURRENT:** the repository separates catalog identity, acquisition truth and installed truth.

### Catalog identity

`registry/skills.json` fixes the canonical 20 foundation + 80 employee-facing capability set.

### Acquisition truth

`registry/packages.json` is the authority for the 80 external employee package sources, exact commits, selectors, namespaces, dependencies and operators.

Current package policy is:

- original-first;
- exact source pin required;
- complete package directory copied;
- canonical AI-Verse names remain stable.

### Installed truth

A successful install creates an immutable generation under:

```text
~/.aiverse/skills/.aiverse/generations/<generation-id>/
```

The one mutable routing datum for new work is:

```text
~/.aiverse/skills/.aiverse/active.json
```

**LAW:** the capability index is derived discovery state. It cannot add trust, permission or an uninstalled package.

**LAW:** one execution pins one generation and continues reading that generation for instructions, scripts and resources.

## 5. Package model

### Foundation packages

**CURRENT:** 20 first-party procedural packages live under `skills/foundation/`.

They generally encode:

- a professional outcome;
- a bounded procedure;
- constraints;
- verification expectations;
- explicit deference to host authority.

### Employee packages

**CURRENT:** 80 employee-facing capabilities are curated from external ecosystems.

Acquisition is either:

- `vendored`: content is present in this repository with provenance;
- `upstream-fetch`: the installer fetches the exact pinned Git revision and resolves the package deterministically.

### Support packages

Support dependencies may be installed but are excluded from the canonical 100-capability count and from selectable provider records.

### Profiles, roles and operators

Profiles choose subsets such as full, creator, business, filmmaker, marketing, sales and finance.

Roles compose skill/operator metadata.

Operators describe software/runtime requirements.

**LAW:** role/operator metadata describes composition and prerequisites. It does not supply credentials or permission.

## 6. Immutable lifecycle

### Install

`install`:

1. resolves the selected profile;
2. resolves foundation, employee and support packages;
3. fetches exact pinned upstream revisions where needed;
4. copies complete packages into a staging generation;
5. emits Provider v1 metadata;
6. verifies paths, digests, generation and manifest/index binding;
7. commits the immutable generation;
8. atomically activates it.

### Update

**CURRENT:** `update` creates a fresh immutable generation and changes the active pointer only after verification.

It does not mutate an active generation in place.

**GAP / UX:** an installed update uses the source registry's current pins. A newer upstream package does not enter production until the curated Skills registry itself changes.

### Pin

`pin --json` exposes the verified active generation identity/path for a runtime needing stable bytes.

### Rollback

`rollback` selects a previously verified generation and changes only routing for new work.

### Uninstall

**CURRENT:** `uninstall` is deactivation, not destructive deletion. It marks the provider uninstalled while retaining generation bytes.

This preserves in-flight pinned work and rollback capability.

**GAP:** there is no separate destructive purge or generation garbage-collection policy.

### Legacy migration

**CURRENT:** the installer recognizes the earlier mutable installation shape and migrates it to the immutable lifecycle before mutation.

Schema-2 immutable generations remain legacy-compatible rather than being silently reinterpreted as Provider v1.

## 7. Capability Provider Contract v1

**CURRENT:** new generations publish:

```text
provider_contract: aiverse-capability-provider-v1
provider_id: aiverse-skills
manifest schema: 3
```

and a generation-local:

```text
.aiverse/capability-index.json
```

The index is bound to the exact UTF-8 bytes of `installed.json`.

Selectable IDs use:

```text
aiverse-skills:<normalized-id>
```

Current verification rejects:

- generation mismatch;
- stale manifest hash;
- injected/uninstalled capabilities;
- duplicate normalized IDs;
- invalid relative paths;
- physical generation escape;
- escaping symlinks;
- package digest mismatch;
- stale index metadata.

**LAW:** a valid content digest proves integrity, not trust, readiness or authorization.

## 8. Readiness

**CURRENT:** Readiness v2 corrected optimistic inference.

A package/operator is not considered ready merely because:

- a binary exists;
- an application is installed;
- an environment flag says connected;
- an adapter directory exists.

Connector/API/MCP-style operators require a live bounded probe proving matching identity, authentication, reachability and usability.

FFmpeg/ffprobe use deterministic direct checks.

Application presence for Premiere Pro or After Effects remains installed-unverified without a live usable bridge.

**LAW:** installed/configured is not ready.

**LAW:** readiness is not permission or approval.

**GAP / BOUNDARY:** Skills readiness is operator/environment readiness, not workspace authorization. OS must still resolve current scope, permission, approval and connection usability.

## 9. Execution receipts

**CURRENT:** Skills defines and semantically validates `aiverse-execution-receipt-v2`.

A receipt can bind to:

- request fingerprint;
- scope;
- action class;
- operation;
- provider ID;
- capability ID;
- immutable generation ID;
- portable package digest.

It separates stable receipt identity from correlation-only trace identity and records effect certainty.

A side-effecting execution cannot claim verified success merely from the skill runtime's own assertion. Host-side effect verification is required.

**LAW:** trace is correlation, not proof.

**LAW:** capability metadata or receipts cannot manufacture permission, approval or a Brain objective verdict.

**CURRENT LIMIT:** Skills supplies the contract/validator, not a universal operator execution engine.

## 10. AI-Verse OS integration

Skills remains an external provider:

```text
AI-Verse OS
   |
   | dynamically reads current provider
   v
~/.aiverse/skills/
   |
   +-- .aiverse/active.json
   +-- .aiverse/generations/<id>/...
```

It does not register itself in the OS local extension registry.

It does not copy its library into the OS repository.

### Install-order result

**CURRENT: PASS.**

Skills can exist:

- before OS;
- after OS;
- with an OS host config created before Skills;
- standalone without OS.

Current OS resolver/host logic checks the configured or default Skills root dynamically during discovery/selection.

Therefore, installing Skills later at the canonical/configured root makes it discoverable without modifying tracked OS files or regenerating the host config.

### Does Skills need an OS attach/activate command?

**CURRENT answer: no, by design.**

For Skills, host adoption is external-provider discovery rather than local extension attachment.

No canonical OS-owned state changes and no authority transfer occurs merely because a provider appears.

The lifecycle is:

```text
installed immutable generation
        ↓
Skills active pointer
        ↓
OS dynamic discovery
        ↓
candidate available
        ↓
OS readiness / permission / approval
```

**LAW:** automatic discovery is not authorization.

## 11. Standalone and other runtimes

### Standalone

**CURRENT:** install, update, pin, rollback, doctor, readiness, adapter materialization and uninstall work without AI-Verse OS.

"Standalone" here means standalone distribution lifecycle, not a complete agent runtime.

### Generic runtimes

The repository exposes explicit adapter materialization for directory-oriented runtimes such as Claude, Codex, Hermes, OpenClaw, Gemini and Agent Skills-compatible consumers.

The user selects the target.

Skills does not silently edit runtime configuration.

Adapters are generation-bound and can be checked for staleness.

### Later-installed Skills in generic runtimes

**CURRENT:** installation alone does not automatically make Skills usable in every foreign runtime.

Unless the runtime already knows the canonical Skills root, an explicit `adapt`/host adoption step remains required.

After an update, a materialized adapter can become stale and must be refreshed deliberately.

**GAP:** current CI proves adapter materialization and generation integrity, not a complete discover -> select -> load -> invoke -> verified outcome path for every advertised generic runtime.

## 12. Security, isolation and trust

### Strong current controls

**CURRENT / PASS:**

- exact upstream Git commit pins;
- immutable generations;
- stage then verify before activation;
- lifecycle serialization;
- atomic active pointer;
- generation pinning;
- relative path validation;
- physical containment;
- escaping symlink rejection;
- package/generation integrity digests;
- strict provider/index validation;
- secret-minimizing readiness output;
- no Skills mutation of tracked OS state;
- host-owned permission/approval.

### Material admission gap

**GAP / HIGH PRIORITY:** the repository's own research says external/generated skills should enter through an admission pipeline covering security, license, secret/PII, concealed instruction, dependency, semantic-duplicate and behavioral-evaluation checks.

That pipeline is not implemented for the current 80-capability distribution.

A concrete repository example is the vendored LifeOS `Council` package. Its preserved original instructions still contain runtime-specific mandatory notification behavior, reads/writes under a Claude/LifeOS-specific home layout and assumptions about a particular subagent runtime. Its current static Skills registry entry does not describe those runtime-specific effects.

This is not evidence that the package is malicious. It demonstrates that:

> exact provenance + valid digest does not establish portability, safety or host compatibility.

Inside AI-Verse OS, host authority remains higher priority. Generic adapters can expose original package text more directly, making admission/compatibility review especially important.

### Probe registry

The readiness probe registry can name executable commands.

**LAW:** readiness-probe configuration is trusted host/user configuration. Package content must never be able to grant itself access to or rewrite that authority-bearing configuration.

## 13. Provenance and licensing

### Provenance strengths

**CURRENT:**

- exact upstream repositories and commits;
- stable namespaces;
- vendored provenance records;
- installed source commit metadata;
- immutable package/generation digests;
- third-party notices.

### Licensing gaps

**GAP / RELEASE BLOCKER:**

- no top-level first-party `LICENSE` exists at the reviewed head;
- release-hardening PR #7 explicitly states that no first-party license choice was made;
- multiple source records use unresolved/per-package license treatment such as `upstream-package`;
- registry validation does not enforce per-package license admissibility;
- full E2E does not make a package license decision;
- the research record specifically marked Premiere for rebuild because no clear license was found, while the current acquisition registry still fetches the pinned upstream package with unresolved package-level licensing.

Public/member redistribution needs an explicit release-owner decision plus machine-checkable per-package treatment.

## 14. Compatibility and schema evolution

**CURRENT:**

- Provider v1 is pinned to an OS-owned canonical contract;
- breaking provider changes require a new major contract;
- provider version, distribution version and generation ID are separate concepts;
- legacy schema-2 generations remain recognized;
- malformed or unsupported provider state fails closed.

**GAP / METADATA FIDELITY:** provider discovery reads simple top-level `name`, `description` and `version` frontmatter. Some upstream packages place version elsewhere in metadata, so discovery can fall back to the pinned source commit rather than upstream semantic version.

## 15. Concurrency and failure behavior

**CURRENT / PASS:**

- lifecycle mutation is serialized;
- a complete generation is verified before activation;
- activation uses atomic replacement;
- interrupted activation leaves the previous generation active;
- pinned readers remain on immutable old bytes while updates/rollback/uninstall affect only future routing;
- stale copied adapters are detectable;
- malformed provider state fails closed.

**GAP / LOW PRIORITY:** retained generations have no garbage collector or retention policy.

## 16. Historical repair line

### HISTORICAL: initial research

The repository researched Hermes, LifeOS, OpenClaw, Agent Skills, Anthropic Skills, OpenAI/Codex practices, DeepAgents, PydanticAI, Gemini CLI, Copilot CLI, browser-use, Letta, Aider, NVIDIA SkillSpector/SkillEvaluator and other systems.

The initial design emphasized:

- skills vs tools;
- progressive disclosure;
- skill not permission;
- deterministic mechanics in code;
- external-skill admission;
- proposal/evaluate/promote self-improvement.

### HISTORICAL: original-first policy

A later product decision chose to preserve original upstream packages wherever possible, with pinned provenance and host-side authority boundaries.

That is the current acquisition policy.

It does not remove the need for license, security and compatibility admission.

### PR #1

Corrected documentation that described planned OS integration as shipped behavior.

**LAW:** integration claims must match implemented consumer behavior.

### PR #2

Introduced immutable generations, atomic active pointer, pinning, rollback and generation-bound adapters.

**LAW:** one in-flight task must never mix generations.

### PR #3

Added Provider v1 manifest/index.

**LAW:** derived discovery data cannot inject package truth.

### PR #4

Added Readiness v2.

**LAW:** installed/configured is not ready.

### PR #5

Added action-bound receipt v2.

**LAW:** trace is not proof and a side-effecting skill runtime cannot self-certify external success.

### PR #6

Corrected integration docs after OS/Brain integration became real.

### PR #7

Hardened release docs and added the Windows PowerShell launcher while deliberately deferring the first-party license decision.

## 17. Inspiration lineage

### INSPIRATION: Hermes

Adopted:

- progressive skill disclosure;
- capability composition;
- provenance/curation ideas.

AI-Verse improvement:

- immutable distribution generations and external host authority.

### INSPIRATION: LifeOS

Adopted:

- strong judgment skills;
- skill-gap vs skill-creation separation;
- validation-first authoring.

Current lesson:

- preserved foreign runtime behavior still needs compatibility/admission review.

### INSPIRATION: OpenClaw

Adopted direction:

- multiple roots;
- path containment;
- quarantine/workshop thinking;
- external-skill trust caution.

**GAP:** the comparable admission pipeline remains intended rather than implemented.

### INSPIRATION: Agent Skills, Anthropic, OpenAI/Codex

Adopted:

- portable `SKILL.md` package shape;
- progressive disclosure;
- supporting scripts/references/assets;
- lean procedural instruction style.

### INSPIRATION: PydanticAI, Gemini CLI, Copilot CLI

Adopted architectural lesson:

- visibility, readiness, permission and approval are separate.

### INSPIRATION: NVIDIA SkillSpector / SkillEvaluator

Research selected:

- static/semantic scanning;
- deterministic validation;
- semantic deduplication;
- sandboxed evaluation.

**GAP:** not yet enforced over the released external catalog.

## 18. Explicit state classification

### CURRENT

- standalone original-first distribution;
- 20 foundation + 80 employee capabilities;
- exact source pins;
- immutable generations;
- Provider v1;
- Readiness v2;
- Receipt v2 validator;
- generic adapters;
- dynamic AI-Verse OS external-provider discovery;
- safe generation-bound instruction retrieval in the maintained OS host path.

### INTENDED

- dependable professional abilities rather than prompt quantity;
- progressive discovery;
- portable host-neutral skill core;
- richer toolpacks/evals/workshop;
- proposal/evaluation/promotion self-improvement;
- complete runtime-specific invocation acceptance wherever support is advertised.

### GAP

- external package security/admission gate;
- first-party and per-package license resolution;
- generic runtime end-to-end invocation acceptance;
- stale status documentation;
- immutable member-release freeze;
- generation purge/retention policy;
- richer metadata normalization;
- intended toolpack/eval/workshop surfaces not yet fully implemented.

### LAW

- skill is not permission;
- installed is not ready;
- ready is not approved;
- digest validity is not trust;
- index is not package truth;
- one execution pins one generation;
- Skills owns package lifecycle;
- OS owns host authority;
- dynamic discovery is not authorization;
- package text cannot expand host authority.

### HISTORICAL

- initial architecture proposed more normalization/adaptation;
- original-first later became the current acquisition policy;
- immutable/provider/readiness/receipt repairs hardened the current model;
- several snapshot docs still describe superseded stages.

### INSPIRATION

Hermes, LifeOS, OpenClaw, Agent Skills, Anthropic, OpenAI/Codex, DeepAgents, PydanticAI, Gemini CLI, Copilot CLI, browser-use, Letta, Aider, NVIDIA SkillSpector/SkillEvaluator and other sources recorded in repository research.

## 19. Lifecycle / command matrix

| Concern | Current mechanism | Verdict |
|---|---|---|
| Install | `install` / bootstrap | PASS |
| Dry-run plan | `install --dry-run` | PASS |
| OS attach | None, intentionally external | PASS |
| Provider activation | atomic active pointer | PASS |
| OS late adoption | dynamic external discovery | PASS |
| Generic runtime adoption | explicit `adapt` | PASS WITH UX GAP |
| Readiness | `readiness`, doctor readiness | PASS |
| Pin execution | `pin --json` | PASS |
| Update | immutable `update` | PASS |
| Rollback | `rollback` | PASS |
| Adapter verify | `adapter-verify` | PASS |
| Legacy migration | guarded migration | PASS |
| Disable/deactivate | `uninstall` marks provider absent | PASS WITH NAMING CAUTION |
| Purge all generations | none | GAP |
| Generic adapter refresh | run `adapt` again | PARTIAL |
| Reinstall/recover | install/rollback paths | PASS WITH UX CAUTION |

## 20. Completeness matrix

| Dimension | Verdict | Reason |
|---|---|---|
| Engine complete | **PASS** | catalog, acquisition, immutable lifecycle, provider, readiness and integrity are real |
| AI-Verse OS integration complete for current target | **PASS** | dynamic provider discovery and generation-bound safe instruction use exist |
| Lifecycle complete | **PASS WITH MINOR GAPS** | no purge/GC and uninstall naming is overloaded |
| Known Skills migration complete | **PASS** | mutable/schema-2 legacy is handled conservatively |
| Existing-agent generic adoption complete | **PARTIAL** | adapters exist but universal host adoption/invocation does not |
| Command/UX complete | **PARTIAL** | generic adoption/refresh and destructive lifecycle UX can improve |
| Security/admission complete | **FAIL FOR TRUSTED PUBLIC DISTRIBUTION** | integrity is strong, package admission/eval is not |
| Acceptance complete | **PARTIAL** | Skills/OS provider acceptance is strong, final exact-ref five-component gate remains |
| Release/distribution complete | **FAIL** | license decisions and immutable member freeze remain |
| Documentation current | **PARTIAL** | current integration docs coexist with stale status snapshots |

## 21. Exact remaining work before perfect AI-Verse fit

### P0 release blockers

1. Choose and document the first-party repository license.
2. Resolve and machine-enforce third-party package redistribution/license status.
3. Reconcile the Premiere package with the research record that found no clear license.
4. Freeze an immutable member release ref/tag and point member install docs to it.

### P1 trust/admission

5. Implement the external package admission gate already specified by repository research:
   - license verification;
   - static instruction/script security review;
   - concealed-instruction/exfiltration checks;
   - secret/path/runtime-authority analysis;
   - semantic duplication review;
   - sandbox/live evaluation where appropriate;
   - explicit promotion record.
6. Define `package_state: valid` clearly as integrity-valid rather than globally trusted.
7. Model or adapt runtime-specific assumptions/effects that survive original-first import.

### P1 portability/product polish

8. Acceptance-test every runtime that is publicly claimed as supported through a real discover/load/invoke/verified-outcome path.
9. Keep generic adapters explicit, but provide a supported refresh/reconcile UX after generation changes.
10. Decide whether current `uninstall` should be renamed/paired with explicit destructive purge.
11. Add a generation retention policy that cannot remove active or pinned bytes.

### P2 metadata/docs

12. Repair stale status/distribution/readiness documentation.
13. Improve upstream metadata/version normalization.
14. Keep Role Bundles and Operator Packs described as metadata until runtime behavior exists.
15. Keep toolpacks/evals/workshop/self-improvement architecture labeled INTENDED until implemented.

### External system-level gate

16. Run and freeze the five-component member acceptance on exact immutable component revisions after the remaining release repairs.

Universal execution of every Skills operator is not a current five-component-beta requirement and should not be invented as a blocker for this milestone.

## 22. Definition of done for the current member-beta target

Skills should be called complete for member release only when:

- the release revision is immutable and documented;
- first-party distribution licensing is explicit;
- every redistributed/fetched package has a resolved release decision;
- the full-profile install is reproducible from the release artifact;
- Provider v1 verification is green;
- immutable update/rollback/deactivate/pin acceptance is green;
- OS-before-Skills and Skills-before-OS both work;
- missing Skills degrades as absence;
- Skills never mutates tracked OS files;
- package admission/trust is explicitly separated from integrity and enforced for the released catalog;
- generic runtimes are either end-to-end acceptance-tested or described only as adapter/exposure targets;
- member docs match the exact release artifact;
- final five-component acceptance passes on those immutable revisions.

## 23. Supreme-system contribution

Skills contributes the reusable procedural capability layer:

```text
Brain identifies useful capability
        ↓
OS resolves authorized provider/capability
        ↓
Skills supplies immutable procedure/package
        ↓
OS verifies readiness + permission + approval
        ↓
Host/runtime executes
        ↓
Host/provider evidence produces outcome/receipt
        ↓
Brain/Memory consume evidence only within their own ownership boundaries
```

Skills works best with AI-Verse precisely because it does not become another OS.
