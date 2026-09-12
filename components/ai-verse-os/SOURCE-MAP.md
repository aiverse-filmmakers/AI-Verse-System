# AI-Verse OS Source Map

**Repository:** `aiverse-filmmakers/AI-Verse-OS`  
**Reviewed branch:** `main`  
**Latest reviewed commit:** `3bb28154748f693ba2fd7f5473cc086ddc9d975f`  
**Review date:** 2026-09-12

This file records the evidence used to derive `COMPONENT-SPEC.md`. It is intentionally selective. It maps the architecture and historical decisions rather than cataloguing every implementation file.

---

## 1. Canonical identity and runtime evidence

### `README.md`

Primary public description of:

- domain-neutral OS identity;
- Unified Workspace Architecture;
- installation/CLI surface;
- system-vs-user ownership;
- workspace model;
- knowledge lifecycle;
- Four Cs / Three Ms;
- current built-in capabilities;
- privacy and legacy migration.

### `AI-VERSE.yaml`

Machine-readable architecture manifest.

Key evidence:

- schema `2.0`;
- architecture `unified-workspace`;
- ownership categories;
- canonical paths;
- source-of-truth declarations;
- routing order;
- knowledge lifecycle;
- domain-neutrality rules;
- privacy defaults;
- legacy compatibility.

### `AGENTS.md`

Canonical runtime contract.

Key evidence:

- startup protocol;
- progressive disclosure;
- current-context resolver use;
- local extension loading;
- component ownership;
- permission and authority boundaries;
- Brain-owned strategy behavior;
- no direct Data database access;
- capability/provider discovery rules.

### `package.json` and `bin/ai-verse-os.mjs`

Evidence for current CLI packaging and one-command development installation model.

---

## 2. Architecture documents

### `system/architecture/README.md`

Canonical intent of Unified Workspace Architecture.

Important laws:

- one canonical editable home per fact;
- current context smaller than memory;
- workspace isolation;
- deliberate promotion of shared knowledge;
- agents orchestrate instead of duplicate;
- apps/indexes are derived;
- user state survives upgrades;
- generated adapters do not overwrite unknown/modified files.

### `system/architecture/ownership.md`

Defines system-owned, user-owned and derived state and explicit migration rules.

### `system/architecture/source-of-truth.md`

Defines authority precedence and anti-duplication behavior.

Especially important for:

- Brain direction handover;
- ownership-aware current context;
- live external data vs local snapshots;
- derived indexes/dashboards.

### `system/architecture/routing.md`

Evidence for intent -> scope -> owner -> context -> capability -> evidence -> connection -> execute -> validate -> writeback routing.

### `system/architecture/direction-ownership.md`

Defines exactly one strategic owner per scope and symmetric explicit OS <-> Brain handover.

Important properties:

- installation never changes strategic ownership;
- Brain outage does not return ownership to OS;
- provenance survives handover;
- raw frozen strategy is not active direction;
- Brain detach is blocked while Brain owns a scope.

### `system/architecture/action-permissions.md`

Defines OS permission floor and restrictive intersection with intelligence-layer policy.

### `system/architecture/capability-resolution.md`

Defines provider classes:

- OS built-ins;
- external AI-Verse Skills;
- personal local skills;
- workspace-local skills.

Also provides evidence for:

- qualified identities;
- protected aliases;
- generation binding;
- relevance-before-limit selection;
- physical workspace/path containment.

### `system/architecture/knowledge-lifecycle.md`

Defines inbox/context/memory/knowledge/decision/capability/archive meanings.

### `system/architecture/domain-adaptation.md`

Defines the principle:

> specialize content and policies, not the fundamental architecture.

---

## 3. Extension and interoperability contracts

### `system/extensions/README.md`

Canonical local extension attachment contract.

Key evidence:

- `.aiverse/extensions/registry.json`;
- gitignored attachment state;
- preserve unknown fields/sibling entries;
- supported/installed/enabled are distinct;
- health is live;
- registration is not permission;
- extension paths must be contained;
- tracked OS files must not be modified during normal extension install;
- exact legacy Memory cleanup rules.

### `system/contracts/capability-provider-v1/README.md`

Cross-repository capability ownership contract.

Important evidence:

- external Skills remains independently owned;
- OS owns resolver;
- workspace/private capability scope;
- immutable generation identity/digests;
- provider metadata never grants authority;
- host receipt/Brain boundary.

### `docs/FOUR-COMPONENT-HOST-ADAPTER.md`

Historical/current supported composition evidence for OS + Memory + Brain + Skills.

Important lesson: integration wiring belongs in a maintained host boundary, not CI-only inline code.

### `docs/FOUR-REPO-ACCEPTANCE.md`

Cross-repository acceptance contract proving ownership-aware composition.

---

## 4. Release-hardening and lifecycle evidence

### `docs/SHIP-READINESS-AUDIT-2026-09-12.md`

Important historical audit.

This document is used primarily for **historical gaps and lessons**, because several findings were subsequently repaired.

Major findings that shaped later architecture:

- package installation != OS attachment;
- arbitrary install chronology should not determine authority;
- Brain tracked-manifest registration was wrong;
- fixed host topology was too rigid;
- Memory lifecycle/docs lagged installer reality;
- standalone-state migration needed explicit handling;
- extension registry writers needed common locking;
- member release paths needed immutable refs;
- missing optional components should degrade gracefully;
- OS needed component doctor/reconcile.

### `docs/FIVE-COMPONENT-RELEASE-PRD.md`

Canonical release-hardening design.

Important target laws:

- no tracked OS mutation by optional installers;
- one local attachment registry;
- canonical state survives lifecycle;
- generic optional-component host;
- dynamic component discovery;
- read-only Data routing;
- component doctor/reconcile;
- representative install-order acceptance;
- immutable release artifacts.

### `docs/FIVE-COMPONENT-RELEASE-STATUS.md`

Latest reviewed release-state snapshot.

At the reviewed main revision:

- OS release-hardening green;
- Brain release-hardening green;
- Memory release-hardening green;
- Skills release-hardening green;
- Data repair implementation existed but private-repo Actions runner execution remained the gate for declaring the full five-component beta green.

This is release evidence, not a permanent architecture law.

### `docs/ASTRA-REPAIR-HANDOFF.md`

Canonical record of the five-repair Astra sequence.

Repairs documented:

1. cross-workspace Skills symlink leakage;
2. frozen OS strategy re-entering after Brain handover;
3. concurrent Brain direction-ownership handover race;
4. supported four-component host adapter;
5. correction of user-facing integration documentation.

The sequence is explicitly closed and should not be reimplemented absent a new regression.

---

## 5. Internal product frameworks

### `references/3ms-framework.md`

Three Ms:

- Mindset;
- Method;
- Machine.

Important architectural influence inside AI-Verse:

- least necessary complexity;
- deterministic where possible;
- modular execution blocks;
- staged autonomy;
- source/scope discipline;
- kill-switch mentality.

### `references/4cs-framework.md`

Four Cs:

- Context;
- Connections;
- Capabilities;
- Cadence.

Important lesson: evaluate operation from evidence, not folder counts or declarations.

---

## 6. Important commit history reviewed

The commit history was used to understand architectural evolution, not to derive every implementation detail.

### Universal architecture

- `6a8cf2bb0cc511d977f5a2b188fefc99383fc430` - add universal AI-Verse OS v2 architecture contract.
- `0bf14032bc7c681eda6cb60b05126de2f2439a0e` - domain-neutral operator/workspace infrastructure.
- `171e88ea8b29dacd32b9299b9faf9a0e4b6193cb` - domain-neutral onboarding/workspaces/audits/capabilities.
- `2e04833a5f3d37b9db2a7a3d9780b40896d44397` - make Three Ms/Four Cs domain-neutral.
- `32c4e84ee6e57595f92f28b3c8c4359abf206c17` - merge universal architecture v2.

### CLI / install

- `80581de5aabd249811ddbf3c69f5c5577e5aa51d` - CLI package.
- `4dfccb449552726b244f707d21e6b85713e0719a` - install CLI.
- `c0d0a44011a6692ff39d74849538d5fd1caceead` - cross-platform CLI smoke.
- `f2ada922c12efdf7ac2868b7f7d3dbacd8082173` - direct npx install test.
- `fc7bddb61ab9f0ce6f550b6091903231eb15ef0a` - CLI validation/onboarding hardening.

### Extension/capability integration

- `1d2280a031a60b5dd5cee23eabd19677debf1352` - Capability Provider v1 boundaries.
- `a7b18ac1b0e4dfb2aa1e4bb4ec48433e8f2b2ec3` - local extension registry contract.
- `f175745f0e4317c8a6dc62850ed812908520c1b1` - ownership-safe runtime adapter synchronization.
- `1504dad9bcf9d2e42b84dddcb578e4158a14bd16` - scoped four-provider capability discovery.

### Direction/permission safety

- `ea2541265b9a4d0a54f3bb1b323aafd61d400044` - single strategic direction owner.
- `3c8457f7536d1fdef7af42af7db69a42fe57bd6c` - restrictive OS/Brain permission intersection.

### Astra repairs

- `67197710354c440c17f1eb375f3b9dde4b3082b5` - block cross-workspace capability symlink leakage.
- `e07fd379a96239f98aa4f89797e432dc29b5dfdc` - prevent frozen OS strategy re-entering active direction.
- `7bc505c2f6164eceb6f8f623ad5a23fdb35b7798` through `e92cf226...` - maintained four-component host.
- `b04d7df3003cfa0b88d29f9ac3e12195e4dfb871` - corrected four-component integration documentation.

### Data and release hardening

- `d04f9eee5e195b85843c7206d09dc86d4335784d` - optional Data host integration.
- `a076fe730b2e53919c7be9ed6f359b04e795c6bf` - five-component release hardening, dynamic optional-component discovery, component doctor/reconcile, direction handback.
- `8e2549cfafe5c786b314b7310d7aa266e45bf178` - canonical workspace scope IDs.
- `603bc6575b689334b7896939fd5f89559845125f` - shared extension registry lock diagnosis.
- `89fb9043ec58c05931d477ef3e154df428a06c22` - refresh public component acceptance.
- `3bb28154748f693ba2fd7f5473cc086ddc9d975f` - final reviewed release-candidate documentation state.

---

## 7. Tests/CI considered architectural evidence

Important workflow surfaces found in the repository:

- Repository QC;
- CLI smoke;
- direction ownership;
- OS Brain permission contract;
- write-command boundary;
- Data host boundary;
- four-repo acceptance.

Tests matter because they encode boundaries more strongly than narrative documentation in several areas.

---

## 8. Inspiration evidence

No canonical OS document reviewed names a definitive external competitive/reference set used to design the OS architecture.

Therefore the component spec deliberately does not invent external inspirations.

Evidenced references are:

- AI-Verse Three Ms;
- AI-Verse Four Cs;
- Unified Workspace Architecture;
- Capability Provider Contract v1;
- 3D Brain third-party implementation notices for that optional capability.

Future system work should preserve explicit source/reference maps when external projects are researched so the curation history can be audited later.

---

## 9. Evidence limitations

1. This documentation focuses on architectural/product truth, not line-by-line code equivalence.
2. Historical audit findings are not assumed current if later release-hardening evidence shows they were fixed.
3. Release-status documents capture a point in time and may lag a later component repo's newest commit.
4. No external-inspiration names are inferred without repository or research evidence.
5. The desired universal activation UX is current product intent, not a shipped OS command contract.
