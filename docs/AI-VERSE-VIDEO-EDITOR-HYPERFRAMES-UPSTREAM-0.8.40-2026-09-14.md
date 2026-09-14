# AI-Verse Video Editor - HyperFrames Upstream Audit

**Date:** 2026-09-14  
**Upstream:** `heygen-com/hyperframes`  
**Latest release inspected:** `v0.8.40`  
**Immutable release commit:** `cfe5dcfad310ced2a5844998628daa2b8a0f53d7`  
**Nate tested baseline for later compatibility comparison:** `v0.7.109` / upstream commit `12fd6d9087fab1347f8737c34901e3db61e4dfee`

## Release identity

The latest GitHub release is `v0.8.40`, published 2026-09-14.

The CLI package declares:

- package: `@hyperframes/cli`
- version: `0.8.40`
- license: Apache-2.0
- Node engine: `>=22`
- binary: `hyperframes`

## Current upstream architecture

HyperFrames is no longer represented by one monolithic agent instruction set.

Current specialist packages include at least:

- `hyperframes` - mandatory workflow/router entry point;
- `hyperframes-core` - composition HTML/timing/determinism contract;
- `hyperframes-cli` - init/lint/check/preview/render/publish/diagnostics command contract;
- `hyperframes-animation` - motion rules, scene blueprints, transitions and runtime adapters;
- `hyperframes-keyframes` - seek-safe animation/keyframe diagnostics;
- `hyperframes-creative` - design specs, concept, palette, typography, narration and beat planning;
- `hyperframes-audio` - voiceover carve, automation, effect chains and placed-audio mixing;
- `hyperframes-registry` - reusable registry blocks/components;
- `general-video` - custom/longer/freeform video authoring and editing;
- `embedded-captions` - caption-specific workflow.

The main `hyperframes` Skill owns workflow selection and project-state routing. Domain Skills do not own the full deliverable.

## Current canonical authoring loop

Current upstream documentation recommends:

```bash
npx hyperframes lint
npx hyperframes check
npx hyperframes preview
npx hyperframes render --output final.mp4
```

Important current semantics:

- `check` is the maintained browser/runtime/layout/motion/media/contrast verification surface;
- `validate`, `inspect`, and `layout` remain deprecated compatibility aliases and should not appear in new instructions;
- final rendered output must be watched/verified separately from preview;
- project scaffolds pin a HyperFrames version for reproducibility;
- upgrade probes are read-only until explicitly applied;
- an applied project-version bump must be followed by `hyperframes check`, and failed verification must revert the pin.

## Current composition contract

A composition remains HTML with timing expressed through framework-owned `data-*` attributes.

Key current rules include:

- top-level/nested compositions use `data-composition-id`;
- timed clips use `class="clip"`;
- scripts own creative motion but must not fight framework-owned media timing/playback;
- nested composition timing is local by default;
- legacy global media timing can be preserved explicitly;
- reusable nested compositions support declared variables plus per-host values;
- deterministic rendering remains a core requirement.

## Studio, preview, and render

Current upstream supports:

- Studio preview/export;
- CLI preview;
- snapshots at selected semantic times;
- local MP4/MOV/WebM/GIF/PNG-sequence render paths;
- Docker rendering;
- batch rendering;
- hosted cloud rendering;
- AWS Lambda;
- Google Cloud Run.

Normal local rendering is still the simplest default path.

## Transcript and caption support

Current upstream includes:

- `hyperframes transcribe <file>`;
- caption/talking-head workflows;
- JSON transcript support;
- stable generated word IDs (`w0`, `w1`, ...) as of v0.8.39 for per-word caption overrides.

## Current workflow-routing behavior

The main HyperFrames Skill now routes fresh work by deliverable to specialized workflows such as:

- embedded captions;
- talking-head overlays;
- motion graphics;
- product/site launch video;
- faceless explainer;
- general video;
- presentation/deck;
- music-to-video;
- PR/code-change explainer.

For creator edits such as trim/splice/reorder, zoom/reframe, transitions, placed-audio mixing or media preprocessing, the main Skill explicitly composes multiple domain specialists rather than pretending one package owns everything.

## Relevant release changes after Nate's 0.7.109 baseline

### v0.8.36

- Studio pause/edit behavior fixed.
- Studio server API rename: `consumeFileWriteReceipt` -> `identifyFileWrite`.
- `BROWSER_HOSTILE_CODECS` entries changed shape.

This is a real API compatibility risk for code that consumes Studio-server internals.

### v0.8.37

- supported local fonts/raster images up to 2 MiB can be embedded in bundled HTML;
- render fallback on low disk improved;
- nested-video layout/clip visibility fixes;
- AAC peak-correction behavior improved.

### v0.8.38

- `init` scaffolding default changed;
- local render uses the faster capture path;
- default encode quality changed to `looks`;
- most importantly, the **Skill architecture was reorganized**:
  - `hyperframes-core` now focuses on composition HTML;
  - planning and review material moved to the main `hyperframes` Skill.

This means Nate's bundled Skill assumptions cannot be upgraded by replacing only one core Skill directory.

### v0.8.39

- JSON transcripts receive stable word IDs for per-word caption overrides;
- lint false-positive around split closing tags fixed.

### v0.8.40

- sandboxed compositions no longer lose audio due to incorrect Web Audio routing on opaque security origins.

This fix is directly relevant to reliable preview/render audio behavior.

## Canonical-provider implication for AI-Verse

v0.8.40 is a viable **candidate**, not yet an accepted upgrade.

The upstream package layout has materially changed since Nate's tested v0.7.109 baseline. AI-Verse therefore must compare Nate-used surfaces against the complete current provider family, not copy Nate's old `hyperframes` folder and then install v0.8.40 underneath it.

The desired architecture remains:

```text
AI-Verse Video Editor editorial orchestration
        |
        +-- Nate-derived editorial specialists
        |
        +-- one canonical HyperFrames provider family
                |
                +-- main workflow/runtime contract
                +-- core composition contract
                +-- CLI contract
                +-- animation/keyframes
                +-- audio
                +-- registry
                +-- other approved domain specialists
```

No latest-version upgrade is accepted until the Nate compatibility matrix and media tests pass.

## Evidence sources inspected

At exact `v0.8.40` commit:

- root `package.json`;
- `packages/cli/package.json`;
- `skills/hyperframes/SKILL.md`;
- `skills/hyperframes-core/SKILL.md`;
- `skills/hyperframes-cli/SKILL.md`;
- `skills/general-video/SKILL.md`;
- `skills/embedded-captions/SKILL.md`;
- `skills/hyperframes-animation/SKILL.md`;
- `skills/hyperframes-creative/SKILL.md`;
- `skills/hyperframes-audio/SKILL.md`;
- `skills/hyperframes-registry/SKILL.md`;
- composition, CLI, rendering, Studio, caption/recut documentation;
- GitHub release notes v0.8.36 through v0.8.40.
