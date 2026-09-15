# AI-Verse Skills Source Map

**Repository:** `aiverse-filmmakers/AI-Verse-Skills`  
**Reviewed branch:** `main`  
**Reviewed head:** `3ab838e6e64561bbb7cea8f85d0ebc75b9e84337`  
**Audit date:** 2026-09-13  
**Scope rule:** Skills was audited standalone. Cross-repository evidence was limited to contracts and acceptance surfaces that Skills itself names or depends on.

## 2026-09-14 merged source-map update

**CURRENT repository:** `aiverse-filmmakers/AI-Verse-Skills`  
**Branch:** `main`  
**Head:** `71264af6b2b9a575812fe18858d75a54ea2ff545`  
**Version:** `1.1.0-beta.1`  
**Merged PR:** #13

This section is the current merged source-map overlay. Conflicting counts/gaps in the retained 2026-09-13 audit below describe the older audited head and are historical.

Current registry truth:

- `registry/skills.json`: 20 foundation + 99 employee = 119 canonical;
- `registry/packages.json`: exact acquisition truth for the current employee catalog plus 5 support packages;
- original 100 canonical IDs are preserved;
- 19 additions are exactly the approved Interface Designer composite/expert set;
- `registry/trust-policy.json` carries explicit license/redistribution/trust/ownership decisions;
- `THIRD_PARTY_NOTICES.md` records the new design-source attribution and bounded Vercel adaptation;
- `installer/admission.py` implements deterministic package integrity/admission/security/trust projection;
- `installer/learning.py` and public-beta lifecycle code implement governed Skill proposals/promotion rather than a separate workshop runtime.

Interface Designer source surfaces:

- first-party package: `skills/imported/ai-verse/interface-designer/`;
- orchestrator: `SKILL.md`;
- AI-Verse machine contract: `aiverse.skill.yaml`;
- conditional graph: `references/orchestration.json`;
- project design persistence: `references/design-md-contract.md`;
- originality/fingerprint: `references/originality-policy.json`;
- signature interaction: `references/signature-interaction-policy.json`;
- experience curve: `references/experience-curve-policy.json`;
- visual QA: `references/visual-qa-policy.json`;
- scroll QA: `references/scroll-qa-policy.json`;
- mobile art direction: `references/mobile-art-direction-policy.json`;
- routing regression fixtures: `references/routing-fixtures.json`;
- expert preservation/provenance: `references/expert-preservation.json`;
- existing-design compatibility: `references/existing-design-compatibility.json`;
- security boundary: `references/security-boundaries.json`;
- golden workflows: `examples/interface-designer/golden-fixtures.json`.

Exact design-source pins are recorded in `registry/packages.json`. The external expert set includes Anthropic, UI/UX Pro Max, Vercel, shadcn, Meng To, Emil Kowalski and Scroll Craft at immutable 40-character Git refs. Anthropic frontend-design remains fetch-only under conservative upstream-controlled redistribution. The Vercel web-design-guidelines adaptation preserves upstream identity while replacing mutable runtime rule fetching with a package-local rules snapshot pinned to `e3d624baaf29dc1fc645aff3e38f03e564d2d6b1`.

Pre-merge candidate evidence:

- Validate: PASS, `34885862726`;
- Runtime Readiness: PASS, `34885862743`;
- Full E2E: PASS, `34885862596`.

Post-merge evidence on `main` head `71264af6b2b9a575812fe18858d75a54ea2ff545`:

- Validate: PASS, `34886502980`;
- Runtime Readiness: PASS, `34886502969`;
- Full E2E: PASS, `34886502946`.

## 2026-09-14 Invisible Intelligence self-learning evidence

This evidence is included in the current merged `1.1.0-beta.1` head `71264af6b2b9a575812fe18858d75a54ea2ff545` and supersedes older audit statements where they conflict.

Owner implementation lineage:

- `8b82e41bd8f0adecdfd93d64ae1fb30552802b99` - bounded safe auto-promotion of new learned Skills;
- `fb0c138ef424734cd2e5359040f376e35c4c5875` - constrained learned Skill identity before owner mutation;
- `installer/learning.py` - proposal/evaluation/promotion mechanics;
- immutable generation/pointer lifecycle remains the only production activation path;
- dangerous/secret or authority-expanding candidates remain non-auto/quarantined;
- external curated/provider ownership does not become agent-learned ownership.

Cross-owner acceptance:

- OS learning route: `3ebb0530a876c404031274d4fa4d3ec1909ec21a`;
- OS later-use/rollback proof: `caa38f46d29e66363493d0e11da83aa924af1dea`;
- Distribution A-F acceptance: run `34890195270`.

The acceptance proves candidate routing, safe owner mutation, restart/later use and dangerous-candidate refusal without making Gateway or Brain a second Skills registry.

---

## 1. Exact revision and repository inventory

Audit point:

- repository: `aiverse-filmmakers/AI-Verse-Skills`;
- default branch: `main`;
- reviewed head: `3ab838e6e64561bbb7cea8f85d0ebc75b9e84337`;
- declared distribution version: `1.0.0`;
- initial commit used for tree reconstruction: `b33ad1cefb1e0fcf6749cad6d58477c8f2346c6a`.

The initial-to-current compare reconstructed 109 tracked/current paths across:

| Area | Count |
|---|---:|
| `.github/` | 3 |
| `docs/` | 16 |
| `installer/` | 7 |
| `registry/` | 8 |
| `research/` | 2 |
| `schemas/` | 4 |
| `scripts/` | 1 |
| `skills/` | 50 |
| `templates/` | 3 |
| `tests/` | 4 |
| root launch/identity files | remaining |

Important negative-space findings from the tree:

- no top-level first-party `LICENSE`;
- no implemented top-level `toolpacks/`;
- no implemented top-level `evals/`;
- no implemented top-level `workshop/`.

Those concepts appear in architecture/research but are not current runtime subsystems.

## 2. Root identity and release surfaces

### `README.md`

Primary current public product description.

Evidence for:

- separate Skills and OS installation;
- 20 + 80 canonical capability model;
- immutable generations;
- Provider v1;
- original-first distribution;
- generic runtime adapters;
- standalone lifecycle;
- canonical root `~/.aiverse/skills`.

Caution:

some high-level readiness/runtime language is older than the strongest current implementation semantics and should not override code/tests.

### `VERSION`

Current declared value:

```text
1.0.0
```

### `THIRD_PARTY_NOTICES.md`

Attribution/provenance surface for imported ecosystems.

Limitation:

not a machine-enforced per-package license-admission mechanism.

### `bootstrap.sh`

macOS/Linux bootstrap.

Evidence for:

- repository checkout/update;
- CLI linking;
- install;
- doctor/readiness.

Release caution:

the normal bootstrap path follows moving repository state rather than proving an immutable member-release ref.

### `aiverse-skills`, `aiverse-skills.cmd`, `aiverse-skills.ps1`

Platform launch surfaces.

PR #7 added the PowerShell launcher during release hardening.

## 3. Canonical registries

### `registry/skills.json`

Canonical capability identity set:

- 20 foundation;
- 80 employee-facing.

### `registry/packages.json`

Primary external acquisition authority.

Current facts:

- schema version 3;
- 20 foundation;
- 80 employee;
- 5 support;
- 100 canonical total;
- original-first;
- exact pin required;
- complete package directory copied;
- canonical names stable.

The source registry contains exact commit pins and mixed license treatment including resolved repository licenses such as MIT/Apache-2.0 and generic package-level values such as `upstream-package`.

### `registry/profiles.json`

Profiles include:

- full;
- universal;
- creator;
- business;
- filmmaker;
- marketing;
- sales;
- finance.

### `registry/operators.json`

Operator metadata includes requirements for ecosystems such as:

- Google Workspace;
- Canva;
- Figma;
- HubSpot;
- Premiere Pro;
- After Effects;
- FFmpeg;
- Shopify;
- Airtable;
- Notion;
- spreadsheets;
- browser/computer use.

### `registry/runtime-adapters.json`

Evidence for:

- AI-Verse OS external-reference mode;
- directory-oriented generic adapters;
- explicit rule that adapters do not grant scope, secrets, connections, approval, Memory or scheduling authority.

### `registry/roles.json`

Role Bundle composition metadata.

### `registry/aliases.json`

Stable alias mapping.

### `registry/sources.json`

Source/provenance catalog.

Several sources explicitly carry per-package verification-style license status, reinforcing that repository-level attribution is not enough for final redistribution decisions.

## 4. Installer and lifecycle implementation

### `installer/aiverse_skills.py`

Stable public entry point.

It layers current provider/readiness behavior over the v3 installer implementation.

Evidence for historical compatibility strategy: hardening was added without splitting public command identity.

### `installer/aiverse_skills_v3.py`

Main distribution implementation.

Evidence for:

- default root `~/.aiverse/skills`;
- cache behavior;
- exact pinned Git checkout;
- offline cache failure behavior;
- deterministic package resolution;
- complete package copying;
- staging/verification;
- legacy mutable-install migration;
- install/update/rollback/doctor/readiness/list/uninstall/adapt/adapter-verify/pin/e2e wiring;
- refusal to materialize AI-Verse OS as an ordinary directory adapter.

### `installer/generation_lifecycle.py`

Canonical immutable-generation machinery.

Evidence for:

- generation IDs;
- lifecycle lock;
- generation containment;
- active pointer;
- atomic activation;
- pin;
- rollback;
- deactivation;
- retained generations.

### `installer/provider_contract_v1.py`

Skills producer implementation of the canonical Provider v1 contract.

Evidence for:

- contract ID and provider ID;
- manifest schema 3;
- qualified IDs;
- path grammar;
- physical path containment;
- symlink containment;
- portable package digest;
- capability index;
- exact manifest-byte binding;
- semantic verification;
- legacy schema-2 compatibility.

Important metadata limitation:

the producer reads only simple top-level `name`, `description` and `version` frontmatter fields.

### `installer/readiness_v2.py`

Current readiness implementation.

Evidence for:

- host/user-owned probe registry;
- argv execution with no shell;
- bounded timeouts;
- strict result shape;
- authentication/reachability/usability requirements;
- fail-closed malformed output;
- FFmpeg direct self-test;
- installed/configured not being enough for `ready`.

### `installer/execution_receipt_v2.py`

Current receipt semantic validator.

Evidence for:

- request/action/scope/generation/package binding;
- effect certainty;
- evidence provenance;
- trace separation;
- side-effect success requiring host verification.

### `installer/README.md`

Current concise lifecycle/operator documentation.

## 5. Schemas and templates

### `schemas/aiverse-skill-v1.schema.json`

Richer AI-Verse skill contract.

### `schemas/tool-v1.schema.json`

Typed tool-contract concept.

### `schemas/execution-receipt-v1.schema.json`

Legacy receipt contract retained for compatibility.

### `schemas/execution-receipt-v2.schema.json`

Current receipt shape.

### `templates/skill/`

Portable skill authoring templates.

### `templates/toolpack/tool.json`

Evidence of intended richer toolpack architecture.

Classification:

- schemas/templates are CURRENT repository assets;
- a complete toolpack/eval/workshop execution system is INTENDED rather than implemented.

## 6. Package content inspected

All 20 first-party foundation `SKILL.md` files were read.

They consistently encode bounded procedures, constraints, verification and host-authority separation.

Vendored proof-package content inspected:

- Google persona executive assistant;
- Google persona project manager;
- Google persona HR coordinator;
- Google persona event coordinator;
- Hermes email inbox triage;
- LifeOS Council.

### Concrete portability/admission finding

The vendored `Council` package preserves upstream runtime assumptions and mandatory side effects, including:

- a mandatory local notification action;
- reads from a Claude/LifeOS-specific customization path;
- writes to a Claude/LifeOS-specific execution log;
- assumptions about a particular subagent runtime.

Its package registry entry does not currently declare operator/dependency metadata that explains those behaviors.

This directly supports the audit finding that integrity-valid original packages are not automatically portable, trusted or host-compatible.

## 7. Validation implementation

### `scripts/validate_registry.py`

Enforces:

- foundation count 20;
- employee count 80;
- unique canonical IDs;
- exact 40-character source pins;
- selector validity;
- known dependency/operator references;
- vendored `SKILL.md` presence;
- package registry matching the employee catalog;
- valid profile/role references.

Not enforced here:

- per-package license decision;
- behavioral security scan;
- sandbox evaluation;
- hidden/runtime-specific instruction effects;
- explicit trust/promotion decision.

## 8. CI workflows

### `.github/workflows/validate.yml`

Runs:

- registry validation;
- unit tests;
- CLI list smoke;
- full-profile dry-run.

### `.github/workflows/e2e-install.yml`

High-value architecture evidence.

The workflow performs a real networked full-profile installation and validates:

- canonical OS Provider v1 schema compatibility;
- provider semantic verification;
- portable package digests;
- doctor/readiness;
- 100-capability count;
- generation pin;
- copy adapter;
- update;
- stale-adapter rejection;
- integrity-only stale verification;
- rollback;
- uninstall/deactivation;
- pinned-byte survival;
- recovery.

### `.github/workflows/readiness.yml`

Cross-platform readiness matrix across:

- Ubuntu;
- macOS;
- Windows;
- Python 3.9;
- Python 3.12.

## 9. Unit/adversarial test evidence

### `tests/test_generation_lifecycle.py`

Proves:

- pinned work survives update/rollback/uninstall;
- interrupted activation preserves previous active generation;
- lifecycle mutation serialization;
- generation tamper detection;
- copied-adapter staleness behavior.

### `tests/test_provider_contract_v1.py`

Proves:

- public Provider v1 generation;
- support packages excluded from selectable capabilities;
- portable digest semantics;
- exact manifest-byte binding;
- injected capability rejection;
- stale index rejection;
- traversal/escape rejection;
- escaping symlink rejection;
- deterministic ID normalization;
- legacy schema-2 compatibility.

### `tests/test_readiness_v2.py`

Proves:

- binary existence alone is not readiness;
- environment connection hints are not readiness;
- live auth/reachability/usability requirements;
- strict malformed-output rejection;
- no secret-bearing payload leak through readiness report;
- timeout/nonzero failure;
- local app presence remains unverified;
- FFmpeg self-test;
- package readiness depends on operator readiness.

### `tests/test_execution_receipt_v2.py`

Proves:

- v1 compatibility remains;
- action/generation binding;
- side-effect self-certification rejection;
- trace is not evidence;
- strong evidence cannot be self-labeled;
- passed criteria need evidence;
- fresh-context independence;
- partial/uncertain effects remain distinct.

## 10. CI run evidence

Visible successful PR-head workflow runs for the implementation repair line:

### PR #2 - immutable generation lifecycle

- Validate AI-Verse Skills: success, run 13;
- Full E2E Install: success, run 8.

### PR #3 - Provider v1

- Validate: success, run 15;
- Full E2E: success, run 10.

### PR #4 - Readiness v2

- Runtime Readiness: success, run 1;
- Full E2E: success, run 12;
- Validate: success, run 17.

### PR #5 - Receipt v2

- Full E2E: success, run 14;
- Validate: success, run 19.

### PR #7 - release cleanup / Windows launcher

- Validate: success, run 23.

The GitHub connector did not return PR-triggered workflow runs for the reviewed merge commit itself. The code-bearing repair PRs above do have successful relevant workflow evidence.

## 11. Historical PR archaeology

### PR #1 - Align Skills producer requirements with Provider v1

Head: `630d225bce6b3dc29d64642fe17382e8cdb18982`

Issue repaired:

documentation claimed OS behavior not yet implemented.

Permanent lesson:

planned integration is not shipped integration.

### PR #2 - Make Skills lifecycle generation-immutable

Head: `17c9b5fcd6d7faa2e129f5df48b2b6857a425276`

Added:

- immutable generations;
- atomic pointer;
- lifecycle lock;
- execution pinning;
- rollback;
- deactivation-only uninstall;
- generation-bound adapters.

### PR #3 - Publish generation-bound capability provider index

Head: `551f1adb3dd3711c88e44e841f934a1981c29591`

Added:

- schema-3 provider manifest;
- Provider v1 index;
- portable digest;
- strict semantic validation.

### PR #4 - Require live proof for runtime readiness

Head: `c792d64b211f566ef31ce97c355ca5e70c0c5ac9`

Added live readiness proof and removed optimistic `ready` inference.

### PR #5 - Add action-bound execution receipt v2

Head: `aa0f3bc5f8049e337cedff06ca046e0c9a940cbe`

Added effect-aware and generation-bound receipt semantics.

### PR #6 - Correct Skills OS integration documentation

Head: `fe868730e26e8e80ae3f748ffeb752733303d9f7`

Documentation-only correction after integration became real.

### PR #7 - Release hardening: provider-v1 shipping and Windows entrypoint

Head: `09599d4269c4fbe0ddfac98a97ec4fc3f7aa3b7c`

Important explicit release fact:

the change deliberately did not choose a first-party license and remained within the broader five-component release-hardening sequence.

Reviewed merged main head after PR #7:

`3ab838e6e64561bbb7cea8f85d0ebc75b9e84337`.

## 12. Architecture and status documents

### `docs/ARCHITECTURE.md`

Important ownership/future architecture.

Contains both LAW and INTENDED surfaces, including richer tool/policy/trust concepts.

### `docs/SKILL_SPEC.md`

Richer authoring contract.

Classification: INTENDED where it exceeds current package enforcement.

### `docs/SELF_IMPROVEMENT.md`

Proposal/evaluation/promotion/curation design.

Classification: largely INTENDED.

The complete workshop/eval/promotion machinery is not present in the current tree.

### `docs/DISTRIBUTION_INSTALL_ARCHITECTURE.md`

Historical distribution design with some enduring laws.

Contains stale "planned" language for capabilities now implemented.

### `docs/PROJECT_STATE.md`

Material documentation drift at reviewed head.

It still describes Provider v1/OS discovery as future work even though current code/tests implement them.

### `docs/SHIPPING.md`

Useful current shipping rules and component separation.

Still narrower than the research-defined external-package admission standard.

### `docs/IMPLEMENTATION_STATUS.md`

Historical/current snapshot predating some provider/readiness/receipt hardening.

### `docs/COMPLETION_REPORT.md`

Historical initial distribution completion report.

Not valid evidence that the current full member-release target is complete.

### `docs/ORIGINAL_UPSTREAM_POLICY.md`

Current important policy:

- preserve original packages;
- preserve provenance;
- do not mislabel vendored upstream content as first-party authorship;
- host policy remains authoritative;
- upstream changes require review before trust.

### `docs/PACKAGE_RESOLUTION.md`

Current acquisition/reproducibility evidence.

### `docs/AI_VERSE_OS_INTEGRATION.md`

Current cross-repository integration description.

### `docs/READINESS_VERIFICATION.md`

Current Readiness v2 semantics.

### `docs/EXECUTION_RECEIPTS.md`

Current receipt-v2 semantics.

### `docs/IMMUTABLE_GENERATIONS.md`

Current generation/pinning contract.

## 13. Research and inspiration evidence

### `research/2026-09-agent-capability-landscape.md`

Material inspirations include:

- Hermes;
- LifeOS;
- OpenClaw;
- Agent Skills;
- Anthropic Skills;
- OpenAI/Codex skills;
- DeepAgents;
- PydanticAI;
- Gemini CLI;
- GitHub Copilot CLI;
- browser-use;
- Letta;
- Aider;
- NVIDIA SkillSpector;
- NVIDIA SkillEvaluator;
- additional agent/tool frameworks listed in the source.

Important research laws:

- skill != tool;
- skill != permission;
- progressive disclosure;
- deterministic mechanics belong in code;
- external/generated skills require admission;
- self-improvement should be proposal -> evaluation -> promotion/curation.

### `research/2026-09-top-80-existing-employee-skills.md`

Evidence for:

- selection rationale;
- source quality;
- proposed ADAPT / WRAP / REBUILD treatment;
- film-specific cautions;
- license concerns;
- intended security/evaluation gate;
- early plan to normalize foreign runtime assumptions.

Important historical contradiction:

the later original-first policy preserves originals more literally than the initial adaptation plan.

The audit resolves this as:

- original-first = CURRENT acquisition policy;
- broad mandatory rewriting = HISTORICAL/INTENDED only where compatibility requires it;
- license/security/authority constraints remain active requirements.

## 14. Narrow cross-repository evidence

No general audit of other AI-Verse repos was performed.

Only OS surfaces necessary to validate Skills' own contract/integration claims were inspected.

### Canonical Provider v1 contract

Pinned OS revision named by Skills integration history:

`1d2280a031a60b5dd5cee23eabd19677debf1352`

Files:

- `system/contracts/capability-provider-v1/README.md`;
- `system/contracts/capability-provider-v1/capability-index.schema.json`.

Evidence for:

- Skills vs OS ownership;
- qualified IDs;
- index/manifest laws;
- contextual readiness;
- installation-order requirements;
- generation pinning;
- runtime-support acceptance definition;
- receipt boundary.

### Current OS consumer surfaces

Inspected because current Skills integration documentation claims the supported consumer exists:

- `scripts/capability-resolver-core.mjs`;
- `scripts/capability-resolver.mjs`;
- `scripts/capability-resolver-cli.mjs`;
- `scripts/ai_verse_host_adapter.py`;
- `scripts/test-ai-verse-host-adapter.py`;
- `.github/workflows/repo-qc.yml`;
- `docs/FIVE-COMPONENT-RELEASE-PRD.md`.

Evidence for:

- default external root `~/.aiverse/skills`;
- dynamic discovery;
- no Skills local extension attachment;
- provider integrity checks;
- workspace boundary validation;
- safe generation-bound instruction retrieval;
- update-during-execution pin acceptance;
- no runtime dependency on the Skills source checkout;
- five-component release target and remaining release decisions.

## 15. Contradictions found

### A. Current Provider implementation vs `PROJECT_STATE.md`

The document describes schema 2 / Provider v1 as next work.

Current code is schema 3 Provider v1 and current OS consumes it.

**Resolution:** implementation/tests/current integration docs win.

### B. Security research vs current admission implementation

Research requires package security/quality admission.

Current install/registry validator does not implement that pipeline.

**Resolution:** real GAP.

### C. Initial top-80 adaptation plan vs later original-first policy

Research initially proposed stronger normalization/adaptation of foreign runtime assumptions.

Later policy explicitly preserves originals.

**Resolution:** original-first is CURRENT. Security, license and host-authority constraints remain LAW.

### D. Premiere license research vs current acquisition registry

Research says Premiere should be rebuilt because no clear license was found.

Current registry fetches the pinned upstream package under unresolved package-level licensing.

**Resolution:** unresolved release GAP.

### E. `package_state: valid` vs trust

Provider records can be structurally/integrity valid without security admission.

**Resolution:** valid must not be interpreted as trusted/authorized.

### F. Generic adapter exposure vs full runtime support

Adapters are real.

The canonical Provider contract defines runtime support more strongly as discover -> select -> load -> invoke -> verified receipt/outcome.

**Resolution:** current generic adapter compatibility is CURRENT; universal end-to-end runtime support is PARTIAL.

## 16. Negative-space evidence

Confirmed absent or intentionally not implemented:

- first-party top-level license;
- mandatory package-security admission scanner;
- behavioral eval gate across the external catalog;
- workshop/quarantine/promotion runtime;
- destructive generation purge;
- generation garbage collection;
- automatic generic-runtime adapter refresh;
- universal operator execution engine;
- package-manager publication.

Intentional absences:

- no OS attach command is correct for the external-provider model;
- no universal executor belongs inside Skills;
- package-manager publication is not required for the current five-component beta.

## 17. Evidence limitations

1. Upstream source repositories were not audited. Skills' pins, selectors, vendored content, installer behavior and CI were audited.
2. The networked full install was not manually rerun in this chat. Successful GitHub Actions runs are the execution evidence.
3. The connector did not surface PR-triggered runs for the reviewed merge commit itself. Relevant implementation PR heads have successful workflow evidence.
4. Cross-repository inspection was limited to the OS contract/consumer path necessary to understand Skills.
5. No third-party package is treated as legally/security approved merely because it has a pin, digest or successful fetch.


## 18. Video Editor 1.0.0 source lineage

**First-party orchestrator**

- repository: `aiverse-filmmakers/AI-Verse-Skills`;
- package: `skills/imported/ai-verse/video-editor/`;
- release: `1.0.0`;
- accepted release head: `47ca55b11850b1432882a1c1c015e0a253d4c1d0`;
- merged main: `8c321c03421a2e0e470280cc40e588a27c1a510d`;
- implementation PR: **#14**.

**Editorial lineage**

- upstream: `nateherkai/hyperframes-student-kit`;
- immutable commit: `b1afdb1dcbcad39dd27638ea699f132fe44ce6df`;
- license: MIT;
- handling: bounded package-local editorial adaptations with provenance retained;
- deterministic silence cutting, mistake candidate detection, approved-cut application and EDL review are regression-locked;
- demonstration/AIS brand assets are excluded from reusable Video Editor content.

**Canonical renderer/provider lineage**

- upstream: `heygen-com/hyperframes`;
- version: `0.8.40`;
- immutable commit: `cfe5dcfad310ced2a5844998628daa2b8a0f53d7`;
- license: Apache-2.0;
- redistribution: fetch-only;
- role: one canonical composition/runtime/rendering provider family beneath the member-facing Video Editor.

**Cross-skill lineage**

Interface Designer provides only bounded presentation handoffs. Transcript truth, EDLs, source-time mapping, edit decisions, HyperFrames correctness and final media acceptance remain outside Interface Designer ownership.

**Compatibility evidence**

Comparison from Skills baseline `71264af6b2b9a575812fe18858d75a54ea2ff545` to accepted head `47ca55b11850b1432882a1c1c015e0a253d4c1d0` reported 63 added files, 10 modified files and **0 removed files**.
