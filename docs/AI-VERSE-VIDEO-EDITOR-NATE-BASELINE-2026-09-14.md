# AI-Verse Video Editor Nate Baseline + Authority Map

Verified: 2026-09-14
Purpose: Phase 2 baseline for AI-Verse Video Editor
Nate repo: nateherkai/hyperframes-student-kit
Pinned commit: b1afdb1dcbcad39dd27638ea699f132fe44ce6df
Kit package version: 2.0.0

## 1. Tested dependency baseline

At the pinned Nate commit:

- Node >=22
- HyperFrames 0.7.109
- GSAP 3.14.2
- Playwright ^1.59.1

Nate's repository is MIT for original kit material.

Brand caveat:

- AI Automation Society brand assets/examples remain separately owned and are not licensed for generic AI-Verse reuse.
- Those demonstration assets must not become reusable AI-Verse member assets.
- Replace or exclude them from distributable templates unless the owner has a separate right to use them.

Third-party material retains its own terms:

- HyperFrames: Apache-2.0
- GSAP: its own applicable license
- fonts/assets: their individual licenses

## 2. Current upstream HyperFrames comparison point

Latest upstream observed during this Phase 2 audit:

- repository: heygen-com/hyperframes
- commit: cfe5dcfad310ced2a5844998628daa2b8a0f53d7
- CLI/core version: 0.8.40
- license: Apache-2.0

This is not yet accepted as Nate's runtime version.

Nate remains pinned to 0.7.109 until the Phase 3 compatibility gate passes.

The current upstream surface is substantially broader than Nate's baseline and now includes dedicated Skills for HyperFrames routing/core/CLI/creative/animation/keyframes/audio/registry, talking-head recut, motion graphics, embedded captions, faceless explainer, product-launch video, slideshow, music-to-video, PR-to-video, Remotion-to-HyperFrames, media use, storyboard, color, audio and editing capabilities.

That breadth is useful but increases migration risk.

## 3. Nate Skill inventory

The kit contains the same specialist tree mirrored under both:

- .agents/skills/
- .claude/skills/

Canonical unique Skill names:

1. edit-video
2. cut-silences
3. cut-mistakes
4. short-form-edit
5. short-form-video
6. video-storytelling
7. hyperframes-video-beats
8. style-library
9. website-to-hyperframes
10. make-a-video
11. hyperframes
12. hyperframes-cli
13. hyperframes-registry
14. gsap

### Mirror deduplication decision

Do not import both .agents and .claude copies into the canonical AI-Verse package library.

They are runtime exposure mirrors, not distinct expert Skills.

AI-Verse already has immutable package generations plus Claude, Codex and Hermes directory adapters.

Therefore:

- preserve one canonical original package copy per unique Skill
- preserve Nate's package content and references
- use AI-Verse runtime adapters to expose the same pinned generation to each supported host
- do not maintain duplicate bytes merely to recreate Nate's repository mirror layout

This is packaging deduplication only. It must not alter the expert instructions.

## 4. Editorial authority map

### edit-video: FULL RAW-FOOTAGE EDIT ORCHESTRATOR

Owns the tested end-to-end talking-head edit route:

1. inspect source
2. obtain/reuse word-level transcript
3. silence pass
4. mistake/retake pass
5. visual storytelling
6. motion beats/style
7. HyperFrames composition
8. preflight/lint/Studio
9. draft render
10. frame/transition/audio review
11. final MP4 plus edit artifacts and verification report

This should become the main technical foundation beneath the member-facing AI-Verse Video Editor full-edit route.

Do not rewrite its editorial order casually.

### cut-silences: DETERMINISTIC SILENCE SPECIALIST

Owns only silence/dead-air removal from word-timed transcripts.

It explicitly does not remove mistakes/retakes.

Produces EDL, retimed transcript and optional local FFmpeg cut.

Keep its boundary.

### cut-mistakes: REVIEW-GATED SPOKEN-ERROR SPECIALIST

Owns stutters, repeats, false starts and retakes.

Mechanical detection proposes candidates, but editorial judgment decides what is actually a mistake.

Keep the review boundary. Do not turn rhetorical repetition into an automatic cut.

### short-form-edit: MODERN SHORT-FORM EDITOR

Owns new reels, Shorts and short ads.

Core logic includes reference-reel analysis, full transcript review, hook/open-loop/payoff design, three materially different rough openings, truthful first-three-seconds gate, story-driven B-roll, captions, sound design, aspect-ratio-specific composition, motion graphics and final verification.

This is the canonical Nate short-form route for new work.

### short-form-video: LEGACY MAINTENANCE ONLY

The Skill explicitly says it exists to maintain the May Shorts legacy scaffold.

For new reels, Shorts or ads, it routes to short-form-edit.

AI-Verse should not expose this as a competing modern short-form entry point.

Preserve only as a compatibility/legacy specialist if the associated examples/assets are intentionally retained.

### video-storytelling: LONG-FORM VISUAL STORYTELLING

Owns the visual language for long-form talking-head work.

Distinctive tested concepts include one persistent visual world, camera as the edit, three altitude levels, spotlight attention hierarchy, spatial open loops, travelling subject, global token discipline, transcript-linked visual decisions and verification gates.

This is not equivalent to generic UI animation and must not be replaced by Interface Designer motion guidance.

### hyperframes-video-beats: SUPPORTING OVERLAY / RETENTION GRAPHICS

Owns transcript-synced supporting beats for talking-head HyperFrames videos, including lower thirds, callouts, full-screen takeovers, coverage/pacing maps and retention graphics.

It is distinct from video-storytelling, which designs the persistent world.

### style-library: NATE MOTION-GRAPHICS STYLE CATALOG

Owns selection, customization and extension of Nate's reusable cards and scene templates.

The library contains draft resources that still require lint, render and inspection.

Preserve the selection logic and verification posture.

Remove or replace only brand/example assets that are not reusable under the repository license.

### website-to-hyperframes: WEBSITE PROMO WORKFLOW

Owns website capture -> working summary -> DESIGN.md -> narration script -> creative plan/storyboard -> voice/timing -> HyperFrames composition -> verification.

This bridges the future Interface Designer and Video Editor, but remains a Video Editor workflow because the final deliverable is video.

### make-a-video: BEGINNER VIDEO CREATION ROUTER

Owns beginner-friendly creation from concept/script/outline to finished MP4.

It is not the raw-footage editor.

It already routes website inputs to website-to-hyperframes, vertical face-cam builds to short-form-edit and framework questions to hyperframes.

Keep as a video-creation specialist if AI-Verse exposes general video generation in addition to footage editing.

### hyperframes: TESTED NATE FRAMEWORK CONTRACT / ENTRY

Owns Nate's expected HyperFrames authoring/runtime rules.

Until Phase 3 proves compatibility, this contract is tied to the tested 0.7.109 baseline.

Do not silently replace it with the current 0.8.40 upstream Skill.

### hyperframes-cli: CLI SPECIALIST

Owns CLI usage/verification for Nate's tested HyperFrames version.

Subject to the same version compatibility gate.

### hyperframes-registry: COMPONENT / REGISTRY SPECIALIST

Owns reuse of registry blocks/components within Nate's workflow.

Subject to compatibility mapping against current upstream.

### gsap: MOTION IMPLEMENTATION SPECIALIST

Owns GSAP-specific animation implementation in the Nate/HyperFrames environment.

Do not replace it with generic UI animation guidance.

Interface Designer motion experts can inform taste, but HyperFrames/GSAP correctness remains authoritative inside the video render.

## 5. AI-Verse Video Editor authority hierarchy

AI-Verse Video Editor owns user-facing edit orchestration.

Nate edit-video, short-form-edit and video-storytelling own editorial decisions and visual storytelling.

The selected HyperFrames provider owns HTML-video composition/runtime correctness.

The GSAP specialist owns seek-safe motion implementation.

FFmpeg Skill owns deterministic mechanical media operations when selected.

Premiere Agent remains an optional multimodal/NLE backend.

After Effects remains an optional AE-native backend.

Interface Designer specialists provide visual taste only when requested/routed.

## 6. Interface Designer cooperation boundary

Interface Designer experts may improve typography, composition, palette, material treatment, reference reconstruction, design-system quality and motion taste.

They do not override silence cuts, retake/mistake decisions, transcript/source timing, hook/payoff editorial truth, EDL authority, HyperFrames composition contract or final A/V verification.

When a generic UI motion rule conflicts with HyperFrames/video correctness, the Video Editor rule wins.

## 7. Phase 3 compatibility target

Compare Nate 0.7.109 assumptions against upstream HyperFrames 0.8.40 at commit cfe5dcfad310ced2a5844998628daa2b8a0f53d7.

The candidate upgrade must prove:

- Nate's scripts/tests still pass or have bounded documented migrations
- composition HTML remains valid
- CLI command behavior used by Nate remains available or has safe mappings
- lint/check/preview/render behavior remains correct
- transcript-sync validation remains correct
- Nate's editorial specialists do not lose required capabilities
- final media remains visually and audibly acceptable

Until that gate passes, 0.7.109 remains the accepted Nate baseline.

## Next

Build the detailed 0.7.109 -> 0.8.40 compatibility matrix without mutating Nate's canonical baseline first.
