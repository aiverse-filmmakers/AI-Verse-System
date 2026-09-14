# AI-Verse Interface Designer Implementation Plan

**Status:** Persistent execution source of truth  
**Project:** AI-Verse Interface Designer / Design Engineering Composite Skill  
**Canonical planning repo:** `aiverse-filmmakers/AI-Verse-System`  
**Primary implementation repo:** `aiverse-filmmakers/AI-Verse-Skills`  
**Started:** 2026-09-14  
**Rule:** Update this file before and after every implementation slice. A slice is COMPLETE only when implementation, focused tests, provenance/license evidence, and exact GitHub evidence are recorded.

## 0. Mission

Build a production-grade AI-Verse composite design capability that can design and implement:

- application/dashboard interfaces;
- web applications and PWAs;
- responsive websites and marketing pages;
- reference-driven recreations from screenshots, video, URLs, or named products;
- interaction-heavy interfaces;
- scroll-driven/immersive experiences when explicitly relevant;
- mobile/Expo interaction work when that specialist is relevant.

The user-facing capability should feel like one coherent **AI-Verse Interface Designer**, while internally routing to distinct expert Skills with preserved taste, methodology, and specialist authority.

The project must not collapse strong expert Skills into one generic mega-prompt.

## 0A. Stack-neutral design rule

The Interface Designer is a **design capability first**, not a React/Vercel/Node product template.

It must be able to design for the user's actual delivery target, including where relevant:

- plain persistent HTML/CSS/JavaScript artifacts hosted directly from GitHub/GitHub Pages or opened locally;
- framework-based web apps when the existing project already uses one;
- PWAs;
- desktop applications that use web UI wrappers such as Tauri/Electron;
- native desktop applications when an approved platform specialist exists, such as Swift/SwiftUI for macOS;
- interactive prototypes;
- visual systems that later feed code-driven video/motion workflows.

React, Vite, Tailwind, shadcn, Base UI, Vercel guidance, or any other framework/vendor may be selected **only when appropriate to the existing project or requested target**. Using a Vercel-authored engineering Skill does not imply Vercel hosting.

The orchestrator must first answer: **what is being designed and what implementation target already exists or best fits the request?** Then it loads only the relevant implementation specialists.

A plain GitHub artifact must not be rewritten into React merely to satisfy the Skill pack.

---

---

## 0B. Non-negotiable expert-taste preservation rule

This project deliberately imports or adapts design knowledge whose value comes from opinionated human taste.

Therefore:

1. **Do not flatten imported expert Skills into generic shared prose.**
2. Preserve each imported Skill's distinctive decision framework, craft rules, visual philosophy, interaction philosophy, review posture, and specialist workflow unless a concrete incompatibility requires a bounded adaptation.
3. Deduplication applies aggressively to **existing AI-Verse design/frontend Skills that are genuinely superseded**, not to stripping useful capability from stronger imported expert Skills.
4. Imported material may be trimmed only when it is:
   - unrelated to the capability being integrated;
   - infrastructure specific to an upstream environment that AI-Verse cannot or should not adopt;
   - duplicated wrapper/setup text with no specialist knowledge value;
   - legally non-redistributable, in which case use an external-provider/reference route rather than silently copying it.
5. If two imported experts overlap but each carries distinct useful taste, keep both and let the orchestrator route them by stage or concern.
6. When rules conflict, preserve both source Skills and resolve the conflict at orchestration/priority level. Do not rewrite both until they agree.
7. Provenance and license notices must remain traceable to the exact upstream source/ref.
8. Any material adaptation must record what changed and why.

**Default bias: preserve specialist intelligence; remove orchestration bloat, not expert taste.**

---

## 0C. Anti-bloat rule

The final system must not load every design Skill for every UI task.

Prefer:

- semantic capability routing;
- conditional specialist loading;
- scope-aware execution depth;
- reusable existing AI-Verse Skill lifecycle/provider primitives;
- immutable generations already owned by AI-Verse Skills.

Do not create a second Skill registry, package lifecycle, trust model, runtime, scheduler, or general memory system.

A tiny UI edit must not run a full-product design pipeline.

---

## 0D. Ownership boundaries

Preserve existing AI-Verse canonical ownership:

- **Skills** owns Skill packages, provenance, immutable generations, trust/admission/readiness and reusable learned procedures.
- **Brain** may reason about intent/strategy but does not become the owner of Interface Designer package bytes.
- **OS/Gateway** may invoke/routinely expose Skills but do not become a second Skill registry.
- **Memory** may preserve user/project history, but design-system persistence inside a project is represented through project artifacts such as `DESIGN.md`, not a new general memory subsystem.
- **Automations** owns schedules/triggers. Interface Designer orchestration is task-local composition, not a scheduler.
- deterministic security/authority rules remain stronger than any design Skill recommendation.

---

## 0F. Relationship to AI-Verse Video Editor

The Interface Designer and AI-Verse Video Editor are separate composite capabilities.

- Interface Designer owns digital-interface/artifact/app visual design and implementation routing.
- Video Editor owns editorial decisions, transcript-driven cutting, storytelling, video pacing, audio/video sync, motion-graphics assembly and final video delivery.
- Video Editor may call selected Interface Designer capabilities for typography, composition, visual direction, reference recreation, design-system creation and motion taste.
- Interface Designer must not override Video Editor editorial logic or HyperFrames render/runtime rules.

See `docs/AI-VERSE-VIDEO-EDITOR-IMPLEMENTATION-PLAN.md`.

---

## 0E. Status vocabulary

- `NOT STARTED`
- `IN PROGRESS`
- `BLOCKED`
- `COMPLETE`

Every slice must record:

- affected repo(s);
- exact starting refs inspected;
- dependencies;
- anti-bloat decision;
- expert-taste preservation decision;
- acceptance criteria;
- tests;
- provenance/license evidence;
- commit/PR/workflow evidence;
- explicit NEXT slice.

---

# Phase 0 - Persistent plan

## Slice 0.1 - Create persistent execution plan

**Status:** COMPLETE  
**Repos:** AI-Verse-System  
**Dependencies:** none

### Acceptance criteria

- this plan exists in the canonical System repo;
- the imported-expert preservation rule is explicit;
- deduplication scope is explicit;
- phased implementation and QA work is represented as bounded slices;
- future agents can resume from GitHub without the original conversation;
- no implementation changes are made to AI-Verse-Skills before the owner gives the go-ahead.

### Evidence

- initial plan commit: `7b5792c2245bc0f85f803a78f0df52c860047b5f`
- canonical path: `docs/AI-VERSE-INTERFACE-DESIGNER-IMPLEMENTATION-PLAN.md`

### NEXT

**Slice 1.1 - Fresh full audit of CURRENT AI-Verse-Skills repository.**

---

# Phase 1 - Audit CURRENT AI-Verse-Skills before changing anything

## Slice 1.1 - Repository structure and lifecycle audit

**Status:** COMPLETE  
**Repos:** AI-Verse-Skills  
**Dependencies:** 0.1

Read the current repository deeply, including:

- root structure and package/workspace layout;
- Skill manifests and package format;
- provider contracts;
- immutable generation model;
- runtime adapters;
- install/setup/status/doctor/update/uninstall surfaces;
- trust/admission/security model;
- provenance/license metadata;
- protected/user/vendor/learned Skill ownership rules;
- tests/CI;
- docs/QC/source maps;
- current design/frontend-related Skills.

### Acceptance criteria

Produce a current-state map based on source, not old assumptions.

No deletions or imports yet.

### Evidence

- audited AI-Verse-Skills main head: `fb0c138ef424734cd2e5359040f376e35c4c5875`
- open PRs at audit: none
- repo version: `1.1.0-beta.1`
- complete recursive tree: 176 entries
- physically present non-template Skills: 26
- registry contract: 20 foundation + 80 employee = 100 canonical capabilities
- current design/video packages are primarily pinned upstream-fetch registry entries, not committed copies
- no committed HyperFrames package and no HyperFrames registry source/package found
- shared baseline audit: `docs/AI-VERSE-SKILLS-DESIGN-VIDEO-BASELINE-AUDIT-2026-09-14.md`
- audit commit: `0274e1456fdf20a5e7daa7de98eceed84a5f68d1`

### NEXT

**Slice 1.2 - Existing AI-Verse design Skill inventory at exact pinned upstream refs.**

## Slice 1.2 - Existing AI-Verse design Skill inventory

**Status:** COMPLETE  
**Repos:** AI-Verse-Skills  
**Dependencies:** 1.1

Classify every existing Skill that materially touches:

- UI design;
- UX;
- frontend coding;
- React;
- web design;
- dashboards;
- animation/motion;
- accessibility;
- responsive design;
- visual QA;
- design systems;
- screenshot/reference recreation;
- component libraries.

For each, label:

- KEEP;
- KEEP + NARROW;
- SUPERSEDED;
- MIGRATE CONTENT;
- UNRELATED.

### Hard deletion rule

Do not delete an existing Skill merely because its name sounds similar.

Removal requires evidence that its useful behavior is fully covered by the new canonical capability or intentionally migrated.

### Acceptance criteria

A written dedupe/migration map exists before any existing AI-Verse Skill is removed.

### Evidence

- exact pinned upstream contents reviewed for all 8 current design-facing registry capabilities
- overlap map: `docs/AI-VERSE-SKILLS-DESIGN-VIDEO-OVERLAP-MAP-2026-09-14.md`
- overlap-map commit: `4e47d4b4e8fb253cb46f636108a08f9f9063f01d`
- conclusion: current design-facing capabilities are complementary rather than direct duplicates
- Figma packages remain target-specific specialists; static/social/artifact design packages remain separate
- no existing design package was removed

### NEXT

**Slice 2.1 - Re-verify and pin the selected Interface Designer upstream expert sources.**

---

# Phase 2 - Pin upstream expert sources, licenses, and provenance

## Slice 2.1 - Re-verify exact upstream sources and refs

**Status:** COMPLETE  
**Repos:** AI-Verse-Skills, AI-Verse-System for evidence if needed  
**Dependencies:** 1.1

Re-check CURRENT upstream repositories and pin exact commit refs for the selected expert sources.

Initial research candidates to verify:

### Visual/art direction

- Anthropic `frontend-design`
- NextLevelBuilder `ui-ux-pro-max`
- Google `DESIGN.md`

### Frontend engineering and review

- Vercel `react-best-practices`
- Vercel `composition-patterns`
- Vercel `web-design-guidelines`
- shadcn/ui agent Skill / component knowledge where redistribution/use is permitted

### Reference recreation / design-first analysis

- Meng To Skills, especially relevant screenshot/video/reference-recreation and design-first UI workflows
- Google Stitch-related Skills only if they add unique value after current verification

### Interaction and motion craft

From Emil Kowalski's `emilkowalski/skills`:

- `apple-design`
- `animate`
- `prototype`
- `review-animations`
- `pick-ui-library`
- `improve-animations` as conditional specialist
- `find-animation-opportunities` as conditional specialist
- `animate-expo` as platform specialist when relevant
- narrow helpers such as Sonner/Swift only if justified by the current architecture

Do not use `emil-design-eng` as a default core Skill if the narrower specialists already preserve its useful knowledge with less context overlap.

### Scroll/immersive specialist

From `nateherkai/scroll-craft`:

- preserve Scroll Craft as a conditional immersive/scrollytelling specialist;
- extract globally useful orchestration concepts only where appropriate:
  - design fingerprint gate;
  - signature interaction;
  - feeling/experience curve for major flows;
  - separate mobile art direction;
  - state/scroll visual verification.

Do not make Scroll Craft's custom engine the default dashboard/frontend architecture.

## Slice 2.2 - License and redistribution decision per upstream

**Status:** COMPLETE  
**Dependencies:** 2.1

For every source, record:

- exact repository and commit;
- exact files/subtrees used;
- license;
- redistribution/adaptation permission;
- required attribution;
- whether AI-Verse will:
  - vendor unchanged;
  - vendor with bounded adaptation;
  - implement a clean AI-Verse wrapper around the upstream Skill;
  - reference/install externally instead of redistributing.

### Hard rule

Unknown or incompatible license means **do not copy bytes** until the legal route is clear.

### Phase 2 evidence

- source/license pin document: `docs/AI-VERSE-INTERFACE-DESIGNER-UPSTREAM-PINS-2026-09-14.md`
- evidence commit: `cb4212def5ef21bac89f64e23910e2a765b4f054`
- Anthropic frontend-design: Apache-2.0 package-level license
- UI/UX Pro Max: MIT
- Vercel Agent Skills + Web Interface Guidelines: MIT
- shadcn/ui: MIT
- Google DESIGN.md: Apache-2.0
- Meng To Skills: MIT
- Emil Kowalski Skills: MIT
- Scroll Craft: MIT
- Google Stitch Skills: Apache-2.0 and optional only
- Vercel web-design-guidelines receives only a bounded reproducibility adaptation so its rule snapshot is generation-pinned rather than runtime-fetching mutable main
- no implementation stack/vendor becomes mandatory

---

# Phase 3 - Canonical capability map and deduplication design

## Slice 3.1 - Define canonical capabilities

**Status:** COMPLETE  
**Dependencies:** 1.2, 2.2

Define semantic capabilities independent of upstream package names, including at minimum:

- `interface.orchestrate`
- `design.visual_direction`
- `design.ui_ux_intelligence`
- `design.reference_analysis`
- `design.design_system`
- `design.prototype_divergence`
- `design.interaction_physics`
- `design.signature_interaction`
- `frontend.component_architecture`
- `frontend.library_selection`
- `implementation.target_selection`
- `frontend.plain_web`
- `frontend.react_quality` when React is actually the target
- `frontend.accessible_primitives`
- `desktop.webview_ui` when a Tauri/Electron-style target is selected
- `desktop.native_ui` only when an approved native-platform specialist exists
- `motion.build`
- `motion.review`
- `motion.audit`
- `visual.qa`
- `web.guideline_review`
- `experience.scrollcraft`
- `mobile.motion_expo`

The orchestrator resolves capabilities to approved Skill generations rather than hard-coding vendor names everywhere.

## Slice 3.2 - Existing-skill replacement/migration plan

**Status:** COMPLETE  
**Dependencies:** 3.1

Map existing AI-Verse design Skills to the canonical capability map.

Only after this map is reviewed may obsolete AI-Verse design Skills be removed.

### Phase 3 evidence

- capability/routing map: `docs/AI-VERSE-INTERFACE-DESIGNER-CAPABILITY-MAP-2026-09-14.md`
- evidence commit: `95941b7400568feb840939fbef4df6da7cf7d8d8`
- shared packaging decision: `docs/AI-VERSE-COMPOSITE-SKILL-PACKAGING-DECISION-2026-09-14.md`
- packaging commit: `1cb64f6c139631d4f94fe1179a106bf3bcc6f60a`
- no existing design capability is removed
- target catalog intentionally evolves from 100 to 120 canonical capabilities
- interface-designer is first-party; 18 experts retain their own upstream source identity

### Acceptance criteria

No useful existing AI-Verse behavior disappears silently.

---

# Phase 4 - Build the AI-Verse Interface Designer orchestrator

## Slice 4.1 - Scope classifier

**Status:** COMPLETE  
**Dependencies:** 3.1

Classify work into at least:

- MICRO CHANGE;
- COMPONENT;
- SCREEN;
- MULTI-SCREEN FLOW;
- FULL PRODUCT;
- REFERENCE RECREATION;
- INTERACTION-HEAVY UI;
- DESIGN SYSTEM CHANGE;
- SCROLL/IMMERSIVE EXPERIENCE;
- MOBILE/EXPO UI.

Scope determines pipeline depth.

### Current implementation evidence

- AI-Verse-Skills branch: `feature/interface-designer-2026-09-14`
- draft PR: #13
- first-party package created at `skills/imported/ai-verse/interface-designer/`
- package creation ref: `fb048e2c125b6f09f6ba4fd566a574f34c4a765a`
- registry wiring ref before E2E fix: `ef67e8ce5dcb42bea51a0885f1080a808a5069da`
- initial Validate workflow: PASS, run `34872390676`
- initial full E2E correctly exposed one remaining hard-coded 100-capability assertion
- E2E count fix ref: `f104822c25094d47115517bead64c99089c8ab77`
- rerun Validate workflow: PASS, run `34872606928`
- rerun Full E2E: PASS, run `34872606784`
- accepted implementation ref for Slice 4.1: `f104822c25094d47115517bead64c99089c8ab77`
- draft implementation PR: #13


### Implementation-target classification

Separately classify the delivery target before loading engineering specialists:

- PLAIN HTML/CSS/JS ARTIFACT;
- EXISTING WEB STACK;
- REACT WEB APP;
- PWA;
- DESKTOP WEBVIEW APP;
- NATIVE DESKTOP APP;
- PROTOTYPE ONLY;
- DESIGN-ONLY / HANDOFF;
- CODE-DRIVEN VIDEO/MOTION HANDOFF.

Do not migrate stacks unless the user explicitly asks or the existing project cannot satisfy the requirement.

## Slice 4.2 - Semantic trigger policy

**Status:** COMPLETE  
**Dependencies:** 4.1

Users should not need to name Skills.

### Current implementation evidence

- 18 expert canonical capabilities registered at exact pinned upstream refs
- adapted Vercel review package keeps exact pinned rules locally rather than fetching mutable main
- expert catalog implementation ref: `5baa5bebdf69af8bdcf6a1a07df2c0624a7b4ccb`
- Validate workflow: PASS, run `34873010619`
- Full E2E install: PASS, run `34873010676`
- Runtime Readiness matrix: PASS across Linux/macOS/Windows and Python 3.9/3.12, run `34873010624`
- no existing design capability removed

Examples:

- screenshot/video/reference named -> reference analysis;
- new full app/dashboard -> design + prototype + design system + architecture + implementation + QA;
- interaction-heavy drag/sheet/swipe -> Apple interaction physics + Animate + motion review;
- React implementation -> React quality rules;
- new dependency need -> library selection;
- significant finished UI -> visual QA;
- scroll-driven cinematic/immersive request -> Scroll Craft;
- Expo/React Native interaction -> Animate Expo.

## Slice 4.3 - Conditional pipeline graph

**Status:** COMPLETE  
**Dependencies:** 4.2

### Current implementation evidence

- machine-readable graph: `skills/imported/ai-verse/interface-designer/references/orchestration.json`
- conditional graph ref: `388df165169d1a0cae2373cddff590f7650d1911`
- focused tests prove micro tasks skip prototype/art direction and target-specific experts remain gated
- Validate workflow: PASS, run `34873435751`
- Validate: PASS, run `34873435751`
- Runtime Readiness: PASS, run `34873435627`
- Full E2E: PASS, run `34873435714`

Canonical full-product path should support:

1. reference analysis if present;
2. UI/UX intelligence;
3. frontend art direction;
4. prototype/divergence when the design decision is substantial or ambiguous;
5. user selection when explicit selection is required;
6. create/update `DESIGN.md`;
7. component architecture;
8. UI library/primitives selection;
9. interaction-physics specialist when relevant;
10. motion construction when relevant;
11. target-specific implementation quality, with React guidance only for React targets;
12. render/browser/native-preview validation appropriate to the target;
13. visual QA;
14. animation review when motion exists;
15. web/accessibility review;
16. fix failures and re-run relevant gates.

Micro changes skip irrelevant stages.

## Slice 4.4 - DESIGN.md persistence contract

**Status:** COMPLETE  
**Dependencies:** 4.3

Use project-local `DESIGN.md` as the persistent visual grammar where appropriate.

It should preserve:

- product design principles;
- typography;
- type scale/tracking/leading;
- color roles/tokens;
- spacing;
- radii/elevation/surfaces;
- layout/navigation grammar;
- component rules;
- motion language;
- responsive/mobile decisions;
- accessibility requirements;
- signature interaction where one exists;
- forbidden patterns specific to that product.

Existing `DESIGN.md` must be read before substantial design changes.

### Current implementation evidence

- persistence contract: `skills/imported/ai-verse/interface-designer/references/design-md-contract.md`
- minimal template: `skills/imported/ai-verse/interface-designer/references/DESIGN.template.md`
- Google DESIGN.md structural reference pinned at `google-labs-code/design.md@9bf8eae67128b6cc55ad9bf86665767deb4c11cd`
- DESIGN.md contract implementation ref: `9c3902ec169e215832de91d188a04f3372463fb0`
- contract distinguishes read/create/update authority
- micro changes are explicitly excluded from automatic design-system persistence
- accepted reusable product grammar must actually change before an existing DESIGN.md is rewritten
- accepted implementation ref: `56a5b886b151f2215c0e3eef42416a4147a3464e`
- Validate: PASS, run `34877531986`
- Runtime Readiness: PASS, run `34877532039`
- Full E2E: PASS, run `34877531989`

---

# Phase 5 - Originality without destroying consistency

## Slice 5.1 - Design fingerprint gate

**Status:** COMPLETE  
**Dependencies:** 4.3

Adapt the useful Scroll Craft uniqueness concept beyond landing pages.

Track design fingerprint dimensions such as:

- information architecture;
- navigation model;
- layout grammar;
- density;
- typography hierarchy;
- surface/material treatment;
- interaction model;
- motion language;
- primary composition;
- signature element.

Purpose:

- prevent AI-Verse from repeatedly producing the same SaaS shell with different colors;
- detect accidental template convergence;
- preserve consistency within one product while encouraging genuine divergence across distinct products/briefs.

Do not force arbitrary novelty when the reference or established `DESIGN.md` intentionally demands consistency.

### Phase 5.1 evidence

- guide: `skills/imported/ai-verse/interface-designer/references/originality.md`
- machine policy: `skills/imported/ai-verse/interface-designer/references/originality-policy.json`
- fingerprint gate implementation ref: `189ca6c630d52b5cc6fbdea09516afc200f8ccf1`
- 10 fingerprint dimensions, including 6 structural dimensions
- reskin review triggers at 5/6 structural matches
- high-similarity review triggers at 8/10 total matches
- exact-reference, established-DESIGN.md, platform, accessibility and explicit-intent bypasses preserved
- comparison scope is workspace/user scoped; cross-member private fingerprint comparison is forbidden
- Validate: PASS, run `34877911885`
- Runtime Readiness: PASS, run `34877911799`
- Full E2E: PASS, run `34877911939`

## Slice 5.2 - Signature interaction rule

**Status:** COMPLETE  
**Dependencies:** 5.1

For marketing/experience work, require one meaningful signature move when appropriate.

For applications/dashboards, treat it as optional and functional, never decorative by default.

### Phase 5.2 evidence

- guide: `skills/imported/ai-verse/interface-designer/references/signature-interaction.md`
- machine policy: `skills/imported/ai-verse/interface-designer/references/signature-interaction-policy.json`
- signature interaction implementation ref: `bf1711b725ead61573e296194bf779efcf131eaa`
- required only for experience-led contexts where distinctiveness is part of the brief
- dashboards/admin/CRUD/settings/productivity surfaces remain optional-functional
- generic component/easing/parameter tweaks explicitly do not count
- accessibility and reduced-motion equivalents are mandatory where needed
- exact-reference behavior never invents a competing signature move
- Validate: PASS, run `34878261307`
- Runtime Readiness: PASS, run `34878261171`
- Full E2E: PASS, run `34878261195`

## Slice 5.3 - Experience/feeling curve for major flows

**Status:** COMPLETE  
**Dependencies:** 5.1

Use only for meaningful multi-stage experiences such as onboarding, major agent flows, launches, or narrative marketing pages.

Do not add emotional-arc ceremony to ordinary CRUD screens.

### Phase 5.3 evidence

- guide: `skills/imported/ai-verse/interface-designer/references/experience-curve.md`
- machine policy: `skills/imported/ai-verse/interface-designer/references/experience-curve-policy.json`
- experience curve implementation ref: `b47786a36a72da359bb899bf5802e66d5d631ef2`
- operational states such as clarity/control/confidence/readiness are preferred for software
- ordinary CRUD/settings/tables/routine dashboard inspection/micro changes are explicit skip cases
- intended-vs-rendered review cannot rewrite the intended curve merely to hide mismatch
- loading/error/mobile/reduced-motion/accessibility paths remain part of the flow
- Validate: PASS, run `34878613292`
- Runtime Readiness: PASS, run `34878613310`
- Full E2E: PASS, run `34878613290`

---

# Phase 6 - Integrate specialist Skills without flattening them

## Slice 6.1 - Visual direction specialists

**Status:** COMPLETE  
**Dependencies:** 2.2, 3.1

Integrate approved visual-direction/UI-UX experts with provenance intact.

## Slice 6.2 - Reference recreation specialists

**Status:** COMPLETE  
**Dependencies:** 2.2, 3.1

Preserve screenshot/video/reference workflows as specialist capabilities.

## Slice 6.3 - Emil interaction and motion specialists

**Status:** COMPLETE  
**Dependencies:** 2.2, 3.1

Preserve the distinctive methodologies of:

- Apple Design interaction physics;
- Animate construction sequence;
- Prototype divergence workflow;
- Review Animations quality gate;
- Pick UI Library curated dependency selection;
- conditional motion audit/opportunity specialists.

Do not merge these into a generic `motion.md`.

## Slice 6.4 - Frontend engineering specialists

**Status:** COMPLETE  
**Dependencies:** 2.2, 3.1

Integrate React/component/web-quality guidance without stealing visual-direction ownership.

## Slice 6.5 - Scroll Craft specialist

**Status:** COMPLETE  
**Dependencies:** 2.2, 3.1

Keep Scroll Craft conditional to immersive/scroll-driven experiences.

Preserve its unique page-grammar/scrollytelling expertise where licensed and relevant, while keeping its bespoke engine/workspace/tooling isolated from ordinary app builds.

---

### Phase 6 integration evidence

- all selected Interface Designer expert packages are present in the live PR registry
- visual direction: `frontend-design`, `ui-ux-pro-max`
- reference recreation: `design-first-ui-prompting`, `video-to-superprompt`, `stitched-full-page-capture`
- Emil specialists preserved independently: `apple-design`, `animate`, `prototype`, `review-animations`, `pick-ui-library`, `improve-animations`, `find-animation-opportunities`, `animate-expo`
- frontend engineering: `react-best-practices`, `composition-patterns`, `shadcn`, pinned `web-design-guidelines`
- Scroll Craft remains a separate conditional capability
- source identity/provenance remains separate rather than flattened into the AI-Verse orchestrator
- clean-install/provider/readiness acceptance has repeatedly passed with the integrated expert set
- current catalog remains 20 foundation + 99 employee = 119 until Video Editor adds capability 120

---

# Phase 7 - Existing AI-Verse design Skill migration and cleanup

## Slice 7.1 - Migrate unique useful behavior from superseded Skills

**Status:** COMPLETE  
**Dependencies:** Phase 6 complete

Before deleting any existing AI-Verse design Skill:

- prove what supersedes it;
- migrate any unique useful rule, test, trigger or project integration;
- record its replacement capability;
- preserve history/provenance where required.

## Slice 7.2 - Remove confirmed duplicates

**Status:** COMPLETE  
**Dependencies:** 7.1

Only remove confirmed redundant AI-Verse-native design/frontend Skills.

Imported expert specialists are not deleted merely because they partially overlap.

## Slice 7.3 - Compatibility/migration handling

**Status:** COMPLETE  
**Dependencies:** 7.2

If old Skill IDs or package names are public/currently referenced, provide the smallest safe compatibility path rather than silently breaking callers.

---

### Phase 7 cleanup conclusion

Fresh comparison against `docs/AI-VERSE-SKILLS-DESIGN-VIDEO-OVERLAP-MAP-2026-09-14.md` and the current PR registry confirms:

- no existing design-facing capability is functionally superseded enough to delete;
- `brand-guidelines`, `canvas-design`, `figma-use`, `figma-generate-design`, `canva`, `design-and-templates`, `theme-factory` and the other existing creator Skills remain distinct;
- target-specific specialists remain conditionally routed instead of replaced;
- no old public Skill ID is removed;
- therefore no compatibility alias/migration shim is required.

Phase 7 completes with **zero destructive removals**, which is the intended safe outcome.

---

# Phase 8 - Visual and interaction QA system

## Slice 8.1 - State-based visual QA

**Status:** COMPLETE  
**Dependencies:** Phase 6

For applications, validate meaningful states such as:

- empty;
- loading;
- populated;
- error;
- disabled;
- expanded/collapsed;
- dialog/sheet open;
- hover/focus/active where relevant;
- desktop;
- tablet;
- mobile;
- dark/light where supported;
- reduced motion.

## Slice 8.2 - Scroll-state QA

**Status:** COMPLETE  
**Dependencies:** 8.1

For scroll-driven experiences, sample multiple positions and verify:

- no accidental dead scroll;
- major content reaches intended visibility;
- changing backgrounds preserve legibility;
- scroll/video/state progression actually advances;
- reduced-motion alternative is complete;
- mobile experience is intentionally authored.

Do not force Scroll Craft's exact harness onto ordinary apps if simpler browser-state QA is sufficient.

## Slice 8.3 - Separate mobile art direction gate

**Status:** COMPLETE  
**Dependencies:** 8.1

A full-product design is not complete merely because desktop CSS shrinks.

For substantial interfaces, explicitly verify:

- mobile information hierarchy;
- touch target sizing;
- interaction differences;
- crop/layer/order changes where visual media exists;
- mobile navigation;
- safe-area behavior where applicable;
- reduced-motion behavior.

---

### Phase 8 acceptance evidence

- state-based visual QA: `references/visual-qa.md` + `visual-qa-policy.json`
- scroll-state QA: `references/scroll-qa.md` + `scroll-qa-policy.json`
- mobile art direction: `references/mobile-art-direction.md` + `mobile-art-direction-policy.json`
- final Phase 8 accepted ref: `881e42cdb077d81ddf1b2c8e998f5ecd98ceba6f`
- rendered evidence is required for verified visual results
- source inspection alone cannot produce a visual pass
- blocked render states remain `UNVERIFIED_BLOCKED`
- scroll QA samples semantic transitions rather than only fixed percentages
- Scroll Craft verification infrastructure is not forced onto ordinary apps
- mobile must be intentionally authored rather than merely shrinking desktop
- Validate: PASS, run `34879463395`
- Runtime Readiness: PASS, run `34879463453`
- Full E2E: PASS, run `34879463424`

---

# Phase 9 - Tests and quality gates

## Slice 9.1 - Orchestrator routing tests

**Status:** IN PROGRESS

Add deterministic fixtures proving that representative requests trigger the correct specialists and skip irrelevant ones.

Required examples include:

- tiny padding change;
- dashboard from scratch;
- recreate screenshot;
- draggable floating panel;
- React refactor;
- cinematic scroll landing page;
- Expo sheet interaction;
- finished UI review.

## Slice 9.2 - Context/bloat tests

**Status:** NOT STARTED

Prove that:

- tiny tasks do not load the full design pack;
- full-product tasks can resolve all required capabilities;
- conditional specialists stay conditional;
- vendor Skills are not concatenated into one giant always-on context.

## Slice 9.3 - Expert preservation/provenance tests

**Status:** NOT STARTED

Verify that vendored/adapted specialists retain:

- source identity;
- license/attribution metadata;
- pinned provenance;
- expected core rules or reference assets;
- immutable generation integrity.

## Slice 9.4 - Regression tests for removed AI-Verse duplicates

**Status:** NOT STARTED

Every removed/replaced existing design Skill needs coverage proving its supported useful behavior still resolves through the new capability system.

## Slice 9.5 - Security and trust regression

**Status:** NOT STARTED

Imported design Skills must not bypass:

- Skill admission/trust;
- package integrity;
- authority boundaries;
- external-tool approval;
- workspace scoping;
- license/redistribution rules.

---

# Phase 10 - Documentation, examples, and member-facing UX

## Slice 10.1 - Member-facing capability documentation

**Status:** NOT STARTED

Present one coherent capability:

**AI-Verse Interface Designer**

Members should not need to understand the vendor Skill graph.

Document examples such as:

- "Build me a dashboard like this reference";
- "Redesign this page";
- "Make this sheet interaction feel native";
- "Build three directions for this component";
- "Audit the animations";
- "Create an immersive scroll landing page."

## Slice 10.2 - Maintainer architecture documentation

**Status:** NOT STARTED

Document:

- capability map;
- provider mapping;
- stage ordering;
- conflict/priority rules;
- scope classifier;
- provenance;
- replacement map for removed AI-Verse Skills;
- how to add or replace an expert provider later.

## Slice 10.3 - Golden demonstration fixtures

**Status:** NOT STARTED

Provide small, testable example projects or fixtures that demonstrate:

- full dashboard workflow;
- reference recreation;
- interaction-heavy component;
- scroll specialist;
- mobile/responsive quality gates.

---

# Phase 11 - Release gate

## Slice 11.1 - Fresh end-to-end audit

**Status:** NOT STARTED

Re-read CURRENT AI-Verse-Skills after implementation and verify:

- no accidental second Skill architecture;
- no lost useful pre-existing design capability;
- no flattened expert taste;
- no unlicensed vendored content;
- no always-on context explosion;
- no duplicate canonical design orchestrators;
- no broken public Skill IDs without compatibility handling.

## Slice 11.2 - CI and package acceptance

**Status:** NOT STARTED

All focused tests plus the repository's required full CI/public-beta gates must pass.

## Slice 11.3 - System evidence sync

**Status:** NOT STARTED

Update canonical System documents required by the Living Specification Protocol:

- this plan with final evidence;
- relevant Skills component spec/source map/QC;
- blueprint/owner intent if architecture or product intent changed materially;
- system changelog.

## Slice 11.4 - Final release/merge evidence

**Status:** NOT STARTED

Record:

- accepted PR(s);
- merged commit(s);
- workflow runs;
- exact immutable Skill generation/release refs where applicable;
- final capability inventory;
- final removed/superseded Skill inventory.

Only then mark the project COMPLETE.

---

# Canonical design pipeline target

The target full-product orchestration is:

```text
USER INTENT / REFERENCES
        |
        v
SCOPE CLASSIFIER
        |
        +--> reference analysis, when reference exists
        |
        v
UI/UX INTELLIGENCE
        |
        v
FRONTEND ART DIRECTION
        |
        +--> PROTOTYPE / DIVERGENCE, when substantial or ambiguous
        |
        v
DESIGN.md CREATE / UPDATE
        |
        v
COMPONENT ARCHITECTURE
        |
        v
UI LIBRARY / PRIMITIVES
        |
        +--> APPLE INTERACTION PHYSICS, when interaction-heavy
        |
        +--> SCROLL CRAFT, when immersive/scrollytelling
        |
        +--> EXPO MOTION, when React Native/Expo
        |
        v
TARGET-SPECIFIC IMPLEMENTATION QUALITY
        |
        +--> ANIMATE, when motion is required
        |
        v
RENDER / BROWSER STATE VERIFICATION
        |
        v
VISUAL QA
        |
        +--> REVIEW ANIMATIONS, when motion exists
        |
        v
WEB / ACCESSIBILITY REVIEW
        |
        v
FIX FAILURES + RE-RUN RELEVANT GATES
```

The pipeline is conditional. It is not a mandatory sequence for every request.

---

# Resume protocol for future agents

Before doing any work on this project:

1. Read this file in full.
2. Read the latest AI-Verse-System living-spec/owner-intent documents relevant to the task.
3. Inspect CURRENT `AI-Verse-Skills` main and open PRs.
4. Find the first slice whose status is not COMPLETE and whose dependencies are complete.
5. Re-check upstream refs if that slice depends on external sources.
6. Execute only that bounded slice unless the plan explicitly groups multiple slices.
7. Run focused tests.
8. Record exact evidence here.
9. Set the next slice explicitly.
10. Do not rely on chat memory when GitHub evidence differs.

---

# Current project status

**Completed:** Phase 0 / Slice 0.1  
**In progress:** Phase 9 / Slice 9.1 - Orchestrator routing tests
**Next:** Phase 9 / Slice 9.1 - Add deterministic routing fixtures
**Implementation authorization:** WAITING FOR OWNER GO-AHEAD

**Cross-project note:** AI-Verse Video Editor is planned separately in `docs/AI-VERSE-VIDEO-EDITOR-IMPLEMENTATION-PLAN.md`; shared design capabilities are consumed selectively rather than merged.
