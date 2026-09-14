# AI-Verse Composite Skill Packaging Decision

**Date:** 2026-09-14  
**Scope:** Interface Designer + Video Editor integration into AI-Verse-Skills

## Decision

Use the existing AI-Verse Skills registry, immutable generations, admission, trust and runtime adapters.

Do not create a second Skill registry or orchestration runtime.

The current 100-capability catalog will intentionally evolve to **120 canonical capabilities**:

- existing 20 foundation capabilities remain unchanged;
- existing 80 employee capabilities remain unless later evidence proves a true duplicate;
- add 20 new employee capabilities:
  - 1 AI-Verse Interface Designer orchestrator;
  - 18 attributed Interface Designer expert specialists;
  - 1 Nate-derived AI-Verse Video Editor composite.

Final target:

- 20 foundation
- 100 employee
- 120 total canonical capabilities

This is an intentional product expansion, not a regression against the earlier 100-capability public-beta benchmark.

## Why not hide expert Skills as support packages?

The current provider contract excludes packages of kind support from the capability index.

That is correct for mechanical dependencies, but it means a task-local orchestrator cannot reliably ask the provider to load a support Skill as another governed expert capability.

Do not depend on undocumented hidden-package loading.

The selected Interface Designer experts therefore remain normal attributed capabilities, with precise descriptions and conditional routing.

The Interface Designer orchestrator is the preferred broad entrypoint, but narrow requests may correctly route directly to a specialist.

## Interface Designer package model

### First-party orchestrator

Add:

- canonical ID: interface-designer
- ownership: AI-Verse first-party
- location: skills/imported/ai-verse/interface-designer
- purpose: scope classification, stage routing, conflict priority, design gates, progressive disclosure and final QA orchestration

The first-party package must not contain copied third-party Skill bodies.

It may name and route to attributed expert capability IDs.

### 18 new expert specialist capabilities

Add these as separately attributed upstream packages:

1. frontend-design
2. ui-ux-pro-max
3. react-best-practices
4. composition-patterns
5. web-design-guidelines
6. shadcn
7. design-first-ui-prompting
8. video-to-superprompt
9. stitched-full-page-capture
10. apple-design
11. animate
12. prototype
13. review-animations
14. pick-ui-library
15. improve-animations
16. find-animation-opportunities
17. animate-expo
18. scroll-craft

Each retains:

- its own upstream source identity;
- exact pinned commit;
- package license;
- original package body wherever possible;
- separate admission/trust evidence;
- immutable package digest.

Google DESIGN.md is used as a format/specification and project artifact contract, not another canonical Skill.

Google Stitch packages remain optional and are not part of the baseline 120.

### Routing principle

Broad requests such as "build a dashboard", "redesign this app", "make this like the reference", or "design this artifact" should route first to interface-designer.

Narrow specialist requests may route directly where appropriate, for example:

- "audit these animations" -> review-animations
- "create three UI directions" -> prototype
- "this project uses shadcn; build this component correctly" -> shadcn
- "turn this reference video into a recreation spec" -> video-to-superprompt

This is not duplication. The orchestrator owns the multi-stage job; specialists own bounded craft.

## Video Editor package model

### One Nate-derived composite capability

Add:

- canonical ID: video-editor
- member-facing name: AI-Verse Video Editor
- marketing framing: Edit Without an Editor
- upstream base: nateherkai/hyperframes-student-kit
- provenance: reviewed upstream, modified package
- source pin: b1afdb1dcbcad39dd27638ea699f132fe44ce6df until a later accepted update

Do not expose all 14 Nate internal Skills as separate new canonical capabilities.

Instead, create one attributed composite package that preserves Nate's tested kit internally.

### Allowed package adaptation

Because the upstream repository root is not itself an Agent Skill package, AI-Verse may create a package wrapper while preserving the original kit under a clearly attributed internal subtree.

Requirements:

- retain Nate's MIT license and third-party notices;
- retain original Nate Skill files intact unless an exact compatibility patch is required;
- record modified: true and a patch/adaptation manifest;
- preserve only one host-neutral Skill mirror, not both .agents and .claude duplicate trees;
- preserve relative sibling relationships needed by Nate's internal Skills;
- use AI-Verse runtime adapters for Claude/Codex/Hermes exposure;
- exclude or quarantine AIS brand/example assets that are not licensed for generic reuse;
- retain reusable scripts, validators, style resources and templates only when their licenses permit;
- document every omitted upstream path and why it was omitted.

The outer package entrypoint may add AI-Verse routing to existing canonical capabilities such as:

- ffmpeg-skill
- premiere-agent
- after-effects-assistant
- whisper
- interface-designer

The Nate editorial workflow remains authoritative for its own routes.

## HyperFrames rule

HyperFrames is a runtime/framework dependency inside the Video Editor integration, not a second member-facing editor.

Nate's accepted baseline remains HyperFrames 0.7.109.

Current candidate is HyperFrames 0.8.40 at cfe5dcfad310ced2a5844998628daa2b8a0f53d7.

Only replace the package runtime pin after the compatibility matrix and media tests pass.

Do not import the entire modern HyperFrames Skill catalog as separate canonical AI-Verse capabilities merely because upstream contains them.

That would duplicate Nate's tested editorial routing and bloat the member surface.

## Existing design/video capabilities

Keep the existing design and filmmaking capabilities identified in:

- AI-VERSE-SKILLS-DESIGN-VIDEO-OVERLAP-MAP-2026-09-14.md

They solve distinct jobs.

In particular:

- Figma skills remain target-specific implementation specialists.
- Canva/design-and-templates remain social/brand production skills.
- canvas-design remains static visual-art creation.
- director/storyboard/screenplay/camera skills remain pre-production.
- Premiere Agent remains an optional multimodal/NLE editing backend.
- FFmpeg Skill remains deterministic mechanical media execution.
- After Effects remains an optional AE-native backend.
- Whisper remains a transcription option.

## Registry consequences

Implementation must deliberately update:

- registry/skills.json counts and entries;
- registry/packages.json sources/packages;
- registry/sources.json;
- registry/trust-policy.json;
- registry/profiles.json;
- registry/roles.json where appropriate;
- THIRD_PARTY_NOTICES.md;
- validation tests that currently hard-code 80 employee / 100 total.

The old 100-capability benchmark should be preserved in history/release evidence, not enforced against the expanded product.

## Profiles

Expected routing at implementation time:

- full: includes all new capabilities;
- creator: includes interface-designer, its experts, and video-editor;
- filmmaker: includes video-editor plus relevant Interface Designer visual specialists;
- marketing: may include interface-designer and selected visual experts, but video-editor only if intentionally useful;
- universal/business/finance/sales remain unchanged unless a concrete reason exists.

Add a dedicated interface design or post-production profile only if it improves installation footprint without complicating member UX.

## Context-bloat rule

Installation count is not context count.

The runtime must still load only the selected Skill(s) for the current task.

interface-designer must never concatenate all 18 expert bodies into every request.

It should route by task class and load the smallest expert subset.

Video Editor must similarly load only the Nate specialist files relevant to the selected editing route.

## Next implementation steps

1. Interface Designer Phase 3: freeze semantic capability/routing map against the 18 expert IDs.
2. Video Editor Phase 3: complete HyperFrames 0.7.109 -> 0.8.40 compatibility matrix.
3. Create an implementation branch in AI-Verse-Skills only after those two architectural artifacts are complete.
