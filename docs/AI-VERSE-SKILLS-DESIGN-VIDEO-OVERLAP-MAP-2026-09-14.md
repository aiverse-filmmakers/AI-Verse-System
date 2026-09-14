# AI-Verse Design + Video Existing-Skill Overlap Map

**Date:** 2026-09-14  
**Source repo:** `aiverse-filmmakers/AI-Verse-Skills`  
**Baseline main:** `fb0c138ef424734cd2e5359040f376e35c4c5875`  
**Purpose:** Phase 1.2 classification before importing Interface Designer or Video Editor packages.

## Decision rule

An existing Skill is not removed because it shares a broad category name.

Removal requires functional duplication of the same user job with no unique stronger behavior worth preserving.

Current classifications:

- `KEEP`
- `KEEP + NARROW`
- `SPECIALIST DEPENDENCY`
- `MIGRATE UNIQUE BEHAVIOR`
- `SUPERSEDED`
- `UNRELATED`

No package marked KEEP/SPECIALIST DEPENDENCY may be deleted when the new composites are added.

---

# 1. Existing design-facing capabilities

## `brand-guidelines` — KEEP + NARROW

**Pinned source:** `anthropics/skills@41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f`

This is specifically Anthropic brand styling, including Anthropic colors and typography.

It is not a general interface-design skill.

**Future route:** invoke only when the requested artifact intentionally uses Anthropic brand identity or when the user explicitly wants that style.

Do not use it as the visual-direction owner for AI-Verse Interface Designer.

## `canvas-design` — KEEP

**Pinned source:** `anthropics/skills@41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f`

Static PNG/PDF art and poster-style visual philosophy.

This is a different deliverable class from applications/web interfaces.

Its strong art-direction ideas may be useful conceptually, but it should remain a separate static-art capability.

## `theme-factory` — KEEP + NARROW

**Pinned source:** `anthropics/skills@41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f`

Cross-artifact theme application for slides/docs/HTML/etc.

It does not replace interface architecture, component design, interaction physics or frontend implementation.

Keep as a lightweight artifact-theming specialist.

## `figma-use` — SPECIALIST DEPENDENCY

**Pinned source:** `figma/mcp-server-guide@f74a51c9aaec87a2e65c9121753b63fb42203d96`

Figma Plugin API/tool correctness skill.

This is exactly the kind of implementation/tool specialist the Interface Designer should call when the target is Figma.

It should never be mandatory for non-Figma work.

## `figma-generate-design` — SPECIALIST DEPENDENCY

**Pinned source:** `figma/mcp-server-guide@f74a51c9aaec87a2e65c9121753b63fb42203d96`

Build/update composed Figma screens from design-system components, Code Connect, variables and styles.

Strong and useful, but target-specific.

Keep intact and route conditionally from Interface Designer.

## `canva` — KEEP

**Pinned source:** `social-media-skills/skills@6e30eeb2f6736bda8683b6bbaa674af3641d7945`

Canva-specific social design workflow, Brand Kit, Bulk Create, Magic Resize and connector operation.

This is not a web/app interface skill.

Keep as a separate creator/social design capability.

## `design-and-templates` — KEEP

**Pinned source:** `social-media-skills/skills@6e30eeb2f6736bda8683b6bbaa674af3641d7945`

Reusable brand-kit/template system for social graphics.

Different problem from UI/product interface design.

Keep.

## `baoyu-article-illustrator` — KEEP

**Pinned source:** `NousResearch/hermes-agent@7dc796463d543a57270779b7f71f37f18b6faa5e`

Article illustration generation with Type × Style × Palette consistency.

Not an interface-design duplicate.

Keep.

### Design conclusion

**No current design-facing registry capability should be deleted as a direct duplicate of AI-Verse Interface Designer.**

The new Interface Designer fills a missing category: end-to-end interface/product/artifact design orchestration with conditional frontend/native/tool implementation.

Current Figma skills should become target-specific specialists. Existing static/social/artifact design skills remain separate capabilities.

---

# 2. Existing film/video-facing capabilities

## `director-agent` — KEEP

**Pinned source:** `62656456/ai-film-skills@678edc06d3318c1516f6eb73503f740427fdd831`

Screenwriting/director-treatment/pre-storyboard decision brain.

This is upstream of editing.

Keep as a filmmaking/pre-production specialist.

## `ai-storyboard-director` — KEEP

**Pinned source:** same AI-film ref.

Shot/storyboard/cinematography/prompt planning.

Not a raw-footage editing duplicate.

Keep.

## `produce-ai-video` — KEEP

**Pinned source:** same AI-film ref.

Autonomous production of an AI-generated video from an approved script/story.

It overlaps with the broad word "video", but its starting point and production job are different from editing supplied footage.

Keep. It may later provide generated B-roll/shot-production capability to the Video Editor when explicitly appropriate.

## `structure-screenplay` — KEEP

**Pinned source:** `zhangzhangco/film-production-skills@47b2a6a432235e716fa2aa0d08eefae76fdb34fd`

Converts narrative source into scenes/units/beats/production facts.

Pre-production structure, not post-production editing.

Keep.

## `plan-camera-shots` — KEEP

**Pinned source:** same film-production ref.

Creates executable shot segments, blocking, framing, camera movement and continuity.

Pre-production/cinematography, not post-production.

Keep.

## `ffmpeg-skill` — SPECIALIST DEPENDENCY

**Pinned source:** `kajisho5/ffmpeg-skill@0055f7b295ab4d5ef4dc30af76638775eccd0667`

This is a strong deterministic mechanical media layer.

Unique useful behavior includes:

- typed scripts instead of ad-hoc raw shell commands;
- probe-first workflow;
- dry-run/JSON planning;
- platform checks;
- output probing;
- contact-sheet visual inspection;
- many mechanical operations including trim/join/resize/captions/sync/loudness/HDR-SDR/etc.

It explicitly does **not** own editorial taste.

Perfect fit as a Video Editor support specialist.

Do not replace Nate's tested cut scripts with FFmpeg Skill merely because both call FFmpeg. Use each at its correct ownership layer.

## `premiere-agent` — KEEP + MAJOR SPECIALIST BACKEND

**Pinned source:** `Kemerd/premiere-agent@77ed50f4bff14b67b054a64d26aedd7ec217b701`

This is the closest current overlap with the planned AI-Verse Video Editor, but it is too valuable and materially different to delete.

Unique capabilities include:

- Parakeet word-level speech analysis;
- Florence-2 visual captions;
- CLAP audio-event analysis;
- one interleaved `merged_timeline.md` for multimodal editorial reasoning;
- strict word-boundary cut verification;
- project-persistent edit state;
- editable `cut.fcpxml` + `cut.xml` + `master.srt` delivery to Premiere/Resolve/FCP;
- strong local health/smoke tooling.

It does not render a flat final MP4 as its primary deliverable. The cut lives in an NLE.

### Future ownership

AI-Verse Video Editor should be the user-facing orchestrator.

`premiere-agent` becomes an optional **NLE / multimodal editorial backend** when:

- the user wants an editable Premiere/Resolve/FCP timeline;
- visual/audio-event analysis of source footage materially helps;
- the project is more naturally handled as an NLE edit than a HyperFrames render.

Nate's HyperFrames workflow remains separately preserved for its tested talking-head, short-form, motion-graphics and final-MP4 path.

Do not flatten these into one instruction file.

## `after-effects-assistant` — SPECIALIST DEPENDENCY

**Pinned source:** `aedev-tools/adobe-agent-skills@00f131ee5481cd597e6f63f997d92c6fe26586a0`

After Effects automation through ExtendScript.

Useful for projects that explicitly use AE or need AE-native compositing/motion graphics.

Keep as optional backend. HyperFrames does not replace AE and AE does not replace HyperFrames.

## `kanban-video-orchestrator` — KEEP + NARROW

**Pinned source:** `NousResearch/hermes-agent@7dc796463d543a57270779b7f71f37f18b6faa5e`

Multi-agent video-production project orchestration.

It scopes, builds teams, launches Hermes profiles/tasks and monitors production. It does not render/edit directly.

Keep for complex production pipelines.

Do not let it become a competing canonical raw-footage edit orchestrator.

## `whisper` — SPECIALIST DEPENDENCY

**Pinned source:** same Hermes ref.

General local Whisper transcription/translation.

Keep as a transcription option/fallback where it fits.

Nate's preferred transcription path or another verified word-timestamp provider can remain default for the Video Editor when its workflow requires that timing shape.

### Video conclusion

**No current film/video capability should be blindly deleted when AI-Verse Video Editor is introduced.**

The planned Video Editor fills the missing user-level job:

> take my footage and carry the edit through editorial decisions, motion graphics, QA and delivery.

The existing skills become a richer backend ecosystem:

```text
AI-Verse Video Editor
|
+-- Nate HyperFrames editorial workflow
|   +-- short-form
|   +-- talking-head
|   +-- storytelling
|   +-- motion graphics
|   +-- final MP4
|
+-- Premiere Agent backend
|   +-- multimodal source analysis
|   +-- editable NLE timeline
|   +-- Premiere / Resolve / FCP XML
|
+-- FFmpeg Skill
|   +-- deterministic media operations
|
+-- After Effects
|   +-- AE-native motion/compositing
|
+-- Whisper
|   +-- transcription option
|
+-- existing film pre-production specialists
    +-- director
    +-- storyboard
    +-- screenplay structure
    +-- camera planning
    +-- AI-video production
```

---

# 3. HyperFrames duplicate decision

At the audited AI-Verse-Skills baseline:

- no committed HyperFrames Skill exists;
- no HyperFrames source exists in `registry/packages.json`;
- no HyperFrames canonical employee capability exists.

Therefore there is currently **no AI-Verse HyperFrames duplicate to delete**.

This must be rechecked immediately before implementation.

---

# 4. What will actually be deduplicated later

Deduplication should focus on:

1. any newly imported expert package that duplicates another newly selected expert;
2. member-facing routing, so the user does not see several skills claiming "design a web app" or "edit my video";
3. profile/role lists that currently expose low-level specialists when the new composite should become the primary entrypoint;
4. any future discovery of an existing package with genuinely identical user outcome and weaker behavior.

Do not delete useful specialist backends merely to make the registry visually smaller.

---

# 5. Next architectural question

The repo currently enforces exactly 100 canonical capabilities.

The new composites must now be modeled without creating user-facing duplication.

The next implementation/design phase should decide whether to:

- evolve canonical count beyond 100;
- replace selected canonical entrypoints while retaining old packages as support dependencies;
- or introduce first-party composite packages as a distinct existing-registry package class while leaving the original 100 base capability benchmark intact.

Whichever route is chosen must use the existing immutable generation, admission, provenance and adapter architecture.
