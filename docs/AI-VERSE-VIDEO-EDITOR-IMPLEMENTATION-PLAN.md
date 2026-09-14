# AI-Verse Video Editor Implementation Plan

**Status:** Persistent execution source of truth  
**Project:** AI-Verse Video Editor / "Edit Without an Editor" Composite Skill  
**Canonical planning repo:** `aiverse-filmmakers/AI-Verse-System`  
**Primary implementation repo:** `aiverse-filmmakers/AI-Verse-Skills`  
**Started:** 2026-09-14  
**Rule:** Update this file before and after every implementation slice. A slice is COMPLETE only when implementation, focused tests, provenance/license evidence, media/render evidence where relevant, and exact GitHub evidence are recorded.

## 0. Mission

Build a flagship filmmaking capability that can take a user's footage and carry out a real editing workflow with minimal manual editing burden.

Member-facing concept:

**AI-Verse Video Editor**  
Marketing framing may use **Edit Without an Editor**.

The capability should preserve the tested Nate Herk HyperFrames student-kit editorial logic while integrating it into AI-Verse's governed Skill lifecycle, removing duplicate AI-Verse-native copies where proven, and selectively borrowing visual-design experts from the separate AI-Verse Interface Designer when that improves graphics without overriding editorial logic.

Target capability areas include:

- transcription and word-level timing;
- silence/dead-air editing;
- mistake, false-start, retake and stutter review;
- EDL creation and transcript retiming;
- short-form/reel/Shorts editing;
- long-form talking-head editing;
- hook, open-loop, payoff and retention structure;
- visual storytelling;
- transcript-synced motion graphics;
- captions;
- B-roll and source-footage planning;
- style selection;
- website-to-video conversion;
- HyperFrames composition;
- GSAP animation;
- FFmpeg media processing;
- preview/review gates;
- visual-frame inspection;
- cut-boundary and audio-sync review;
- final MP4 delivery.

This is a separate composite capability from **AI-Verse Interface Designer**.

---

## 0A. Tested-editorial-logic preservation rule

Nate Herk's `nateherkai/hyperframes-student-kit` is treated as a tested specialist system whose value includes editorial judgment, not merely implementation code.

Therefore:

1. Do not flatten its video-editing workflow into generic design or animation guidance.
2. Preserve the meaning and ordering of its major editorial stages unless testing proves a bounded change is better.
3. Preserve specialist separation where it is meaningful, including silence cutting, mistake review, storytelling, short-form editing, HyperFrames beats and final verification.
4. Interface Designer experts may improve:
   - typography;
   - composition;
   - visual direction;
   - design systems;
   - reference recreation;
   - color hierarchy;
   - layout;
   - depth;
   - motion taste.
5. Interface Designer experts must **not** take ownership of:
   - transcript truth;
   - edit decisions;
   - retake/mistake judgment;
   - silence policy;
   - EDL ownership;
   - hook/payoff editorial structure;
   - source-time mapping;
   - audio/video synchronization;
   - HyperFrames runtime correctness;
   - final media verification.
6. When generic web-motion guidance conflicts with a tested HyperFrames rendering/runtime requirement, the HyperFrames/video rule wins for the video project.
7. Any adaptation of Nate's tested logic must record exactly what changed and why.

**Default bias: preserve the editor's judgment system; add stronger visual specialists around it rather than rewriting it.**

---

## 0B. HyperFrames version policy

### Verified planning baseline on 2026-09-14

Nate Herk student kit currently pins:

- `hyperframes: 0.7.109`
- `gsap: 3.14.2`

Current upstream HyperFrames release observed during planning:

- `heygen-com/hyperframes` **v0.8.39**
- released 2026-09-14

This is a significant version gap.

Recent upstream releases include behavior/structure changes, including a v0.8.38 reorganization where the core Skill was narrowed to composition HTML and planning/review material moved to the main HyperFrames Skill, plus recent Studio/runtime fixes and at least one breaking API rename in the v0.8.36 release line.

### Hard rule

**Do not blindly replace Nate's tested HyperFrames version with latest.**

Upgrade only through a compatibility gate:

1. audit Nate's exact HyperFrames assumptions;
2. audit CURRENT upstream HyperFrames skills/runtime/CLI;
3. compare commands, Skill contracts, composition rules, lint/validate behavior, Studio preview behavior, transcript support and rendering behavior;
4. run Nate's existing tests against the candidate newer version;
5. run synthetic media smoke tests;
6. run at least one representative short-form composition;
7. run at least one representative long-form/talking-head or motion-graphics composition;
8. verify preview, draft render, extracted frames and A/V sync;
9. verify no Nate-specific editorial instruction was lost by upstream Skill restructuring;
10. only then accept the newer HyperFrames version.

If latest breaks Nate's workflow, keep the last proven-compatible version and document the incompatibility. "Latest" is not more important than a working editor.

### Canonical-source rule

AI-Verse must have **one canonical HyperFrames provider/integration**, not duplicate HyperFrames skills from:

- an existing AI-Verse Skill;
- Nate's bundled copy;
- a separate upstream HeyGen import.

The implementation audit decides which package/generation becomes canonical while preserving Nate's editorial wrappers above it.

---

## 0C. Duplicate-removal rule

Before importing any video/editor/HyperFrames Skill:

1. inspect the entire CURRENT AI-Verse-Skills repository;
2. search by Skill ID, aliases, package metadata, manifests and capability rather than filename only;
3. identify existing:
   - HyperFrames;
   - GSAP;
   - FFmpeg/video;
   - transcription;
   - video editing;
   - captions;
   - storytelling;
   - website-to-video;
   - motion-graphics skills;
4. classify each as:
   - KEEP;
   - KEEP + NARROW;
   - SUPERSEDED;
   - MIGRATE UNIQUE BEHAVIOR;
   - REPLACE WITH CANONICAL PROVIDER;
   - UNRELATED.

Do not ship two member-visible Skills that claim the same canonical capability unless they are intentionally distinct specialists.

GitHub code search during planning returned no indexed `hyperframes` match in AI-Verse-Skills, but this is **not accepted as proof of absence**. A full tree/package audit is mandatory.

---

## 0D. Licensing and brand-asset rule

Planning evidence:

- Nate Herk student-kit original material: MIT;
- HyperFrames upstream: Apache-2.0;
- GSAP: its own applicable license;
- Google Fonts and other assets retain their own licenses;
- AIS example brand assets in Nate's repo are explicitly not reusable as generic AI-Verse brand assets.

AI-Verse integration must:

- preserve required notices;
- track exact source/ref;
- exclude or quarantine example brand assets that are not licensed for reuse;
- not imply that example media grants rights to embedded third-party brands;
- separate reusable code/skills/templates from demonstration-only assets.

---

## 0E. Relationship to AI-Verse Interface Designer

The two composites remain separate:

### AI-Verse Video Editor owns

- edit orchestration;
- transcript-driven editing;
- silence/mistake decisions;
- EDLs;
- hook/open-loop/payoff structure;
- video storytelling;
- captions and B-roll planning;
- timing;
- HyperFrames assembly;
- audio/video verification;
- final video delivery.

### AI-Verse Interface Designer may provide

- visual art direction;
- typography;
- layout/composition;
- design-system creation;
- reference-recreation support;
- motion taste/interaction principles where applicable to rendered graphics;
- prototype/divergence of graphic directions.

The Video Editor calls these capabilities conditionally.

Do not merge the two orchestrators.

See `docs/AI-VERSE-INTERFACE-DESIGNER-IMPLEMENTATION-PLAN.md`.

---

## 0F. Status vocabulary

- `NOT STARTED`
- `IN PROGRESS`
- `BLOCKED`
- `COMPLETE`

Every slice records:

- affected repo(s);
- exact starting refs inspected;
- dependencies;
- duplicate decision;
- preservation decision;
- compatibility decision;
- acceptance criteria;
- exact tests/media checks;
- provenance/license evidence;
- commit/PR/workflow evidence;
- explicit NEXT slice.

---

# Phase 0 - Persistent plan

## Slice 0.1 - Create persistent Video Editor execution plan

**Status:** COMPLETE  
**Repos:** AI-Verse-System  
**Dependencies:** none

### Acceptance criteria

- Video Editor is planned separately from Interface Designer;
- Nate's tested editorial logic is protected;
- HyperFrames compatibility policy is explicit;
- duplicate-removal policy is explicit;
- latest-version intent is balanced against compatibility;
- future agents can resume without the originating chat;
- no AI-Verse-Skills implementation change occurs before owner go-ahead.

### Evidence

- initial Video Editor plan commit: `b20e69660155a104abbff32230f1d8e28c4618e6`
- canonical path: `docs/AI-VERSE-VIDEO-EDITOR-IMPLEMENTATION-PLAN.md`
- planning baseline verified Nate kit pin: HyperFrames `0.7.109`
- planning baseline verified current upstream release: HyperFrames `v0.8.39` on 2026-09-14
- planning-time AI-Verse-Skills code search returned no indexed `hyperframes` match; full-tree audit remains mandatory before treating it as absent

### NEXT

**Slice 1.1 - Fresh full video/design/HyperFrames inventory of CURRENT AI-Verse-Skills.**

---

# Phase 1 - Audit CURRENT AI-Verse-Skills and existing video capabilities

## Slice 1.1 - Full video-skill inventory

**Status:** COMPLETE  
**Repos:** AI-Verse-Skills  
**Dependencies:** 0.1

Inspect CURRENT Skills repo deeply for any existing:

- HyperFrames skill/package/provider;
- GSAP skill;
- FFmpeg/video processing;
- transcription;
- captioning;
- video editing;
- silence trimming;
- mistake/retake editing;
- storytelling;
- short-form editing;
- motion graphics;
- website-to-video;
- reference-video analysis;
- visual QA/media QA.

No imports or deletions yet.

### Evidence

- audited AI-Verse-Skills main head: `fb0c138ef424734cd2e5359040f376e35c4c5875`
- open PRs at audit: none
- repo version: `1.1.0-beta.1`
- complete recursive tree: 176 entries
- current registry contains 10 film/video employee capabilities and 8 design-facing capabilities relevant to cross-over analysis
- current filmmaker/post-production roles and profiles are explicitly mapped in the shared audit
- no committed HyperFrames package and no HyperFrames registry source/package found
- shared baseline audit: `docs/AI-VERSE-SKILLS-DESIGN-VIDEO-BASELINE-AUDIT-2026-09-14.md`
- audit commit: `0274e1456fdf20a5e7daa7de98eceed84a5f68d1`

### NEXT

**Slice 1.2 - Existing duplicate and migration map using exact pinned upstream package contents.**

## Slice 1.2 - Existing duplicate and migration map

**Status:** COMPLETE  
**Dependencies:** 1.1

Produce a written map before deletion.

Any existing AI-Verse video/design Skill can be removed only when:

- it is genuinely superseded;
- unique useful behavior has been migrated;
- callers/IDs have a safe compatibility path when needed.

### Evidence

- exact pinned upstream contents reviewed for all 10 current film/video registry capabilities
- overlap map: `docs/AI-VERSE-SKILLS-DESIGN-VIDEO-OVERLAP-MAP-2026-09-14.md`
- overlap-map commit: `4e47d4b4e8fb253cb46f636108a08f9f9063f01d`
- Premiere Agent remains a major optional multimodal/NLE backend
- FFmpeg Skill, After Effects and Whisper remain specialist dependencies
- director/storyboard/screenplay/camera/AI-video packages remain separate pre-production/generation capabilities
- no existing HyperFrames registry package exists at the audited baseline
- no existing video package was removed

### NEXT

**Slice 2.1 - Pin and inventory the exact current Nate Herk student-kit source.**

---

# Phase 2 - Audit Nate Herk kit as the editorial baseline

## Slice 2.1 - Pin exact Nate source and inventory

**Status:** COMPLETE  
**Repos:** AI-Verse-Skills  
**Dependencies:** 1.1

Pin the exact current commit of `nateherkai/hyperframes-student-kit`.

Inventory at least these canonical skills:

- `edit-video`
- `cut-silences`
- `cut-mistakes`
- `video-storytelling`
- `short-form-edit`
- `short-form-video` compatibility/history
- `make-a-video`
- `hyperframes-video-beats`
- `style-library`
- `website-to-hyperframes`
- `hyperframes`
- `hyperframes-cli`
- `hyperframes-registry`
- `gsap`

Also inventory:

- `MOTION_PHILOSOPHY.md`;
- style library;
- templates;
- tests;
- validators;
- examples;
- helper scripts;
- licenses/notices.

## Slice 2.2 - Editorial authority map

**Status:** COMPLETE  
**Dependencies:** 2.1

Document which specialist owns each decision.

Example:

- edit orchestrator -> complete workflow;
- cut-silences -> deterministic silence pass;
- cut-mistakes -> reviewed spoken-error decisions;
- short-form-edit -> reels/Shorts/ad editorial structure;
- video-storytelling -> persistent-world long-form visual storytelling;
- HyperFrames beats -> supporting overlays/retention graphics;
- style library -> reusable card/scene direction;
- HyperFrames -> composition/runtime rules.

Purpose: prevent later imported design skills from stealing editorial ownership.

### Phase 2 evidence

- Nate source/authority document: `docs/AI-VERSE-VIDEO-EDITOR-NATE-BASELINE-2026-09-14.md`
- evidence commit: `e6bbc792314df95a50da8b75dd3cf564582f6be4`
- Nate pinned source: `b1afdb1dcbcad39dd27638ea699f132fe44ce6df`
- Nate kit version: `2.0.0`
- tested Nate HyperFrames baseline: `0.7.109`
- tested Nate GSAP baseline: `3.14.2`
- current upstream HyperFrames candidate observed: `0.8.40` at `cfe5dcfad310ced2a5844998628daa2b8a0f53d7`
- 14 unique Nate Skills inventoried
- `.agents/skills` and `.claude/skills` confirmed as host mirrors; AI-Verse will keep one canonical package copy and use runtime adapters rather than duplicate bytes
- short-form-video classified as legacy maintenance only; short-form-edit is the modern short-form route
- no editorial authority is transferred to Interface Designer

---

# Phase 3 - HyperFrames upstream compatibility and canonical-provider decision

## Slice 3.1 - Inspect CURRENT upstream HyperFrames

**Status:** COMPLETE  
**Dependencies:** 2.1

Re-check latest release at execution time, not the planning-time v0.8.39 assumption.

Inspect:

- package version;
- CLI;
- Skill packages;
- composition contract;
- validation/lint;
- preview/Studio;
- render behavior;
- transcripts/captions;
- registry;
- breaking changes since 0.7.109.

### Slice 3.1 evidence

- current latest upstream release: `v0.8.40`
- immutable upstream release commit: `cfe5dcfad310ced2a5844998628daa2b8a0f53d7`
- CLI package version: `0.8.40`
- CLI license: Apache-2.0
- CLI engine floor: Node `>=22`
- canonical current verification loop uses `lint -> check -> preview -> render`
- `validate`, `inspect`, and `layout` are deprecated compatibility aliases
- current Skill family separates main workflow routing, core composition rules, CLI, animation/keyframes, creative direction, audio, registry, captions and general-video concerns
- v0.8.38 materially reorganized Skill ownership by moving planning/review out of core and into the main HyperFrames Skill
- v0.8.39 adds stable JSON transcript word IDs
- v0.8.40 fixes sandboxed-composition audio routing
- upstream audit: `docs/AI-VERSE-VIDEO-EDITOR-HYPERFRAMES-UPSTREAM-0.8.40-2026-09-14.md`
- upstream audit commit: `dd3ba89c2474e4172e7aefe1bde305366d57d907`

## Slice 3.2 - Nate 0.7.109 -> candidate-latest compatibility matrix

**Status:** COMPLETE  
**Dependencies:** 3.1

Compare every Nate-used surface.

Classify:

- unchanged;
- compatible;
- migration needed;
- behavior changed;
- broken;
- removed;
- improved and safe.

## Slice 3.3 - Candidate latest compatibility test

**Status:** COMPLETE  
**Dependencies:** 3.2

Test newest candidate without mutating the canonical Nate baseline first.

Must pass:

- Nate kit checks;
- skill mirror checks;
- behavior tests;
- synthetic media smoke;
- HyperFrames lint;
- HyperFrames validate;
- Studio preview;
- draft render;
- extracted-frame visual verification;
- audio/video sync;
- representative short-form path;
- representative longer/motion-graphics path.

### Slice 3.3 evidence

Isolated live acceptance was executed without modifying canonical AI-Verse-Skills `main`.

Disposable test branch:

- repository: `aiverse-filmmakers/AI-Verse-Skills`
- branch: `test/video-editor-hyperframes-v0840-acceptance`
- final harness head: `b638eb5516002b53f31a7949df8bb9bab16322a2`
- successful workflow: `Video Editor HyperFrames 0.8.40 Acceptance`
- successful run: `34888930903`
- successful job: `104126423042`
- evidence artifact: `hyperframes-v0840-acceptance`
- artifact id: `10365912711`
- artifact digest: `sha256:fd3c97c062b2d7d86688119a0425f5d09010f484440c9b08c4d73141365ec244`

Acceptance result: **PASS**.

Verified in the successful run:

- Nate pinned baseline resolved to HyperFrames `0.7.109`;
- Nate baseline behavior suite: **11/11 PASS**;
- Nate Skill mirrors: **94 files / 0 discrepancies**;
- candidate injected into the isolated copy: HyperFrames `0.8.40`;
- Nate behavior suite after candidate swap: **11/11 PASS**;
- Nate Skill mirrors after candidate swap: **94 files / 0 discrepancies**;
- HyperFrames pinned Chrome bootstrap: PASS;
- required doctor checks: Version, Node.js, CPU, Memory, Disk, FFmpeg, FFprobe and Chrome all PASS;
- optional Whisper/Kokoro/MusicGen absence did not block render acceptance;
- SRT transcript import: PASS;
- transcript sidecar export: PASS;
- current HyperFrames lint gate: PASS with only the intentionally exercised nested-media local-basis warning;
- current HyperFrames `check`: PASS;
- deprecated `validate` compatibility path emits the expected deprecation signal;
- Studio background preview/status/context/stop path: PASS;
- draft render: PASS, 6.0 seconds, audio present;
- looks render: PASS, 6.0 seconds, audio present;
- FFprobe video-stream assertion: PASS;
- FFprobe audio-stream assertion: PASS;
- duration assertion: PASS;
- A/V duration sync assertion: PASS;
- extracted frames at 0.5s, 2.5s, 3.5s and 5.5s: PASS;
- all representative frames passed nonblank/dynamic-range checks;
- final harness result: `ACCEPTANCE PASS`.

The acceptance also caught and corrected one old fixture assumption before success:

- nested composition assets must use project-root paths such as `assets/source.mp4`, not directory-relative `../assets/source.mp4`.

This confirms the source-level migration matrix with actual browser, Studio, audio and encode evidence.

## Slice 3.4 - Choose canonical HyperFrames version/provider

**Status:** COMPLETE  
**Dependencies:** 3.3

Decision:

- use latest proven-compatible upstream;
- or use newest proven-compatible intermediate version;
- or retain Nate's 0.7.109 temporarily if upgrade breaks tested behavior.

There must be one canonical HyperFrames provider in AI-Verse-Skills.

### Slice 3.4 decision

**Canonical AI-Verse Video Editor HyperFrames provider version:** `0.8.40`

**Immutable upstream release commit:** `cfe5dcfad310ced2a5844998628daa2b8a0f53d7`

**Provider source:** `heygen-com/hyperframes`

Decision basis:

- newest upstream release inspected at execution time;
- source-level compatibility matrix passed with bounded required adaptations;
- Nate editorial tests remained green after runtime swap;
- current HyperFrames lint/check/Studio/render/media paths passed;
- transcript import/export passed;
- final encoded video and audio passed runtime assertions;
- no Nate dependency on identified v0.8.36 Studio-internal breaking APIs;
- v0.8.40 includes the sandboxed-audio fix directly relevant to reliable video editing/rendering.

Canonical-provider rule:

- AI-Verse ships **one** HyperFrames provider family based on upstream v0.8.40;
- Nate's bundled `hyperframes`, `hyperframes-cli` and `hyperframes-registry` copies are **not** separate canonical providers;
- Nate-derived editorial specialists remain above the provider and call it through AI-Verse capability/provider resolution;
- uniquely useful Nate motion/editorial guidance may be preserved in Nate-derived specialists, but must not fork the provider's runtime contract;
- future HyperFrames upgrades must rerun the pinned regression suite before provider promotion.

---

# Phase 4 - Build canonical AI-Verse Video Editor capability map

## Slice 4.1 - Define semantic capabilities

**Status:** IN PROGRESS  
**Dependencies:** 1.2, 2.2, 3.4

At minimum:

- `video.edit.orchestrate`
- `video.transcribe`
- `video.cut.silence`
- `video.cut.mistakes`
- `video.edl`
- `video.shortform.edit`
- `video.longform.storytelling`
- `video.hook_payoff`
- `video.reference_analysis`
- `video.caption`
- `video.broll.plan`
- `video.motion_beats`
- `video.style_select`
- `video.website_to_video`
- `video.hyperframes.compose`
- `video.gsap.motion`
- `video.ffmpeg.media`
- `video.qa.visual`
- `video.qa.audio_sync`
- `video.render.final`

## Slice 4.2 - Edit orchestrator routing

**Status:** NOT STARTED  
**Dependencies:** 4.1

Representative routing:

### Full talking-head edit

transcribe -> silence -> mistake review -> editorial/story plan -> visual beats -> style -> HyperFrames/GSAP -> QA -> final

### Short-form reel/Short

reference analysis if supplied -> transcript/cut -> three opening directions where appropriate -> truthful hook/payoff -> scene/caption/B-roll/sound plan -> HyperFrames -> QA -> final

### Single operation

"remove silences" -> silence specialist only

### Website promo

website capture -> DESIGN.md -> script -> storyboard -> timing/VO -> HyperFrames -> QA

### Motion-graphics-only video

brief -> storyboard -> selected design experts -> HyperFrames/GSAP -> QA

---

# Phase 5 - Integrate Nate editorial specialists into AI-Verse Skills

## Slice 5.1 - Edit orchestrator

**Status:** NOT STARTED

Preserve `edit-video` logic as the main full-edit coordinator, adapted only where required by AI-Verse lifecycle/routing conventions.

## Slice 5.2 - Deterministic cut specialists

**Status:** NOT STARTED

Integrate silence and mistake/retake workflows with tests and exact transcript/EDL contracts preserved.

## Slice 5.3 - Short-form editor

**Status:** NOT STARTED

Preserve hook/payoff, reference analysis, footage ledger, captions, moving footage and sound-design logic.

## Slice 5.4 - Long-form storytelling

**Status:** NOT STARTED

Preserve persistent-world, camera-as-edit, spotlight hierarchy, spatial open-loop and transcript-anchor logic.

## Slice 5.5 - Motion beats and style system

**Status:** NOT STARTED

Integrate motion-beat planning, style library and reusable templates while distinguishing draft assets from verified final components.

## Slice 5.6 - Website-to-video

**Status:** NOT STARTED

Preserve the existing website capture -> DESIGN.md -> script -> storyboard -> VO/timing -> composition -> validation route.

---

# Phase 6 - Selective cooperation with Interface Designer

## Slice 6.1 - Visual-direction handoff

**Status:** NOT STARTED  
**Dependencies:** relevant Interface Designer capabilities available

Video Editor may request:

- visual direction;
- typography;
- composition;
- palette hierarchy;
- visual-system cleanup.

Editorial timing remains Video Editor-owned.

## Slice 6.2 - Reference-recreation handoff

**Status:** NOT STARTED

When a reference reel/site/frame is supplied, combine:

- Video Editor's editorial/reference timing analysis;
- Interface Designer's visual reconstruction analysis.

Never claim audio was analyzed when only images/frames were inspected.

## Slice 6.3 - Prototype visual directions

**Status:** NOT STARTED

For significant motion-graphic identity decisions, optionally generate multiple visual directions before producing the whole edit.

Do not prototype every ordinary lower third.

## Slice 6.4 - Motion-taste handoff

**Status:** NOT STARTED

Use Apple/Emil motion knowledge only where it improves rendered graphic motion without conflicting with HyperFrames timing/render rules or Nate's video-specific motion philosophy.

---

# Phase 7 - Deduplicate existing AI-Verse video skills

## Slice 7.1 - Migrate unique behavior

**Status:** NOT STARTED  
**Dependencies:** Phases 4-6

For each existing overlapping AI-Verse Skill:

- identify unique useful behavior;
- migrate it;
- record replacement capability;
- preserve public compatibility where needed.

## Slice 7.2 - Remove confirmed duplicates

**Status:** NOT STARTED

Remove duplicate AI-Verse-native HyperFrames/video/editor skills only after canonical replacements are proven.

Do not keep multiple copies of the same upstream HyperFrames Skill under different wrappers unless there is a documented compatibility reason.

---

# Phase 8 - Media QA and verification

## Slice 8.1 - Structural validation

**Status:** NOT STARTED

Verify:

- transcript/source identity;
- EDL validity;
- timing maps;
- beat anchors;
- footage-ledger integrity;
- no invalid same-track overlaps;
- deterministic compositions;
- lint/validate clean.

## Slice 8.2 - Visual verification

**Status:** NOT STARTED

Draft output must be inspected at:

- hook;
- major beats;
- transitions;
- CTA/outro;
- aspect-ratio-specific compositions.

Check:

- cropping;
- text;
- face coverage;
- blank/black frames;
- transition integrity;
- graphic legibility;
- brand consistency.

## Slice 8.3 - Audio verification

**Status:** NOT STARTED

Review:

- cut joins;
- breaths;
- abrupt sentence boundaries;
- sync;
- levels;
- music/SFX placement when present.

Automated waveform checks are not substitutes for listening where listening is required.

## Slice 8.4 - Multi-format verification

**Status:** NOT STARTED

9:16, 16:9 and 1:1 outputs are separately authored/verified where requested. Do not assume a center crop is a valid alternate edit.

---

# Phase 9 - Testing

## Slice 9.1 - Existing Nate tests retained

**Status:** NOT STARTED

Preserve and adapt the kit's existing test coverage.

## Slice 9.2 - AI-Verse orchestrator routing tests

**Status:** NOT STARTED

Representative prompts must route correctly:

- full raw talking-head edit;
- remove silences only;
- clean retakes only;
- make a Reel;
- make a long-form visual explainer;
- animate a website into a promo;
- add motion graphics only;
- use supplied reference reel;
- make three visual directions.

## Slice 9.3 - HyperFrames upgrade regression suite

**Status:** NOT STARTED

Pin a regression suite so future upstream upgrades cannot silently break Nate's workflow.

## Slice 9.4 - Duplicate/provider regression

**Status:** NOT STARTED

Prove only one canonical HyperFrames provider is active and all dependent video specialists resolve to it.

---

# Phase 10 - Member-facing UX and packaging

## Slice 10.1 - One simple member-facing capability

**Status:** NOT STARTED

Present:

**AI-Verse Video Editor**

Members should be able to say:

- "Edit this video for me."
- "Turn this into a Reel."
- "Remove the silences and mistakes."
- "Make this edit feel like this reference."
- "Add motion graphics."
- "Turn this website into a promo video."
- "Make three visual styles for this edit."

They should not need to know HyperFrames, GSAP, FFmpeg, EDL terminology or provider internals.

## Slice 10.2 - Maintainer docs

**Status:** NOT STARTED

Document:

- editorial authority map;
- capability map;
- HyperFrames provider/version decision;
- upstream provenance;
- Interface Designer cooperation boundary;
- duplicate-removal map;
- upgrade procedure.

---

# Phase 11 - Release gate

## Slice 11.1 - Fresh end-to-end audit

**Status:** NOT STARTED

Verify:

- no flattened Nate editorial logic;
- no duplicate HyperFrames provider;
- no lost existing AI-Verse video capability;
- no unlicensed brand/example asset bundled as reusable content;
- no Interface Designer ownership leak into editorial decisions;
- no unverified latest-version upgrade.

## Slice 11.2 - Full CI/media acceptance

**Status:** NOT STARTED

Required code tests plus media smoke/render verification pass.

## Slice 11.3 - System evidence sync

**Status:** NOT STARTED

Update:

- this plan;
- relevant Skills component spec/source map/QC;
- System changelog;
- blueprint/owner intent if necessary.

## Slice 11.4 - Final evidence

**Status:** NOT STARTED

Record:

- accepted PR(s);
- merged commit(s);
- workflow runs;
- canonical HyperFrames version/ref;
- Nate source ref;
- final Skill/capability inventory;
- removed duplicate inventory;
- final media acceptance evidence.

Only then mark COMPLETE.

---

# Canonical Video Editor pipeline target

```text
USER FOOTAGE / SCRIPT / URL / REFERENCE
        |
        v
VIDEO EDIT ORCHESTRATOR
        |
        +--> TRANSCRIPTION, when needed
        |
        v
SILENCE PASS
        |
        v
MISTAKE / RETAKE REVIEW
        |
        v
EDITORIAL STORY PLAN
        |
        +--> SHORT-FORM HOOK / PAYOFF, when short-form
        |
        +--> LONG-FORM PERSISTENT-WORLD STORYTELLING, when relevant
        |
        +--> REFERENCE ANALYSIS, when reference exists
        |
        v
VISUAL BEAT + B-ROLL + CAPTION PLAN
        |
        +--> INTERFACE DESIGNER VISUAL SPECIALISTS, only when useful
        |
        v
STYLE / DESIGN.md
        |
        v
HYPERFRAMES + GSAP + FFMPEG
        |
        v
LINT / VALIDATE / PREVIEW
        |
        v
DRAFT RENDER
        |
        v
FRAME + TRANSITION + AUDIO REVIEW
        |
        v
FIX FAILURES
        |
        v
FINAL RENDER
```

---

# Resume protocol for future agents

Before any implementation work:

1. Read this file in full.
2. Read the Interface Designer plan for shared-capability boundaries.
3. Inspect CURRENT AI-Verse-Skills main/open PRs and full Skill inventory.
4. Inspect CURRENT Nate student-kit source/ref.
5. Inspect CURRENT HyperFrames upstream release/version.
6. Find the first incomplete unblocked slice.
7. Work one bounded slice at a time.
8. Never upgrade HyperFrames solely because a newer version exists.
9. Record tests/media evidence here after every slice.
10. Use GitHub evidence over chat memory when they differ.

---

# Current project status

**Completed:** Phases 0-3 / HyperFrames provider decision complete  
**In progress:** Phase 4 / Slice 4.1 - Define semantic Video Editor capabilities against current Skills architecture  
**Next:** Phase 4 / Slice 4.1 - Inspect current Skills registry/package conventions and add the canonical Video Editor capability map without duplicate ownership  
**Implementation authorization:** ACTIVE - owner said continue
