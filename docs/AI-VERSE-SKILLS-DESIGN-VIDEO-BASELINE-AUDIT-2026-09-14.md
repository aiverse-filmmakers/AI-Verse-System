# AI-Verse Skills Design + Video Baseline Audit

**Date:** 2026-09-14  
**Purpose:** Shared Phase 1 baseline for AI-Verse Interface Designer and AI-Verse Video Editor  
**Audited repo:** `aiverse-filmmakers/AI-Verse-Skills`  
**Audited main head:** `fb0c138ef424734cd2e5359040f376e35c4c5875`  
**Repo version:** `1.1.0-beta.1`  
**Open PRs at audit:** none

## 1. Repository state

The current repository is already a governed Skill distribution and lifecycle owner. It is not a flat folder of prompts.

Observed structure:

- 176 Git tree entries;
- 20 first-party foundation Skills;
- 80 canonical employee-facing registry capabilities;
- 100 canonical capability contract currently enforced by registry validation;
- 27 `SKILL.md` files physically present including the template;
- 26 non-template physically present Skills:
  - 20 AI-Verse foundation Skills;
  - 4 vendored Google persona Skills;
  - 1 vendored Hermes email Skill;
  - 1 vendored LifeOS Council Skill;
- most employee-facing Skills are exact pinned upstream-fetch packages rather than committed copies.

No current committed `SKILL.md` path is a dedicated web/interface-design Skill or a dedicated HyperFrames/video-editor Skill.

## 2. Important lifecycle architecture already present

### Original-upstream-first policy

`docs/ORIGINAL_UPSTREAM_POLICY.md` explicitly requires:

- prefer the best original upstream package;
- do not rewrite an upstream Skill merely to brand it as AI-Verse;
- preserve package structure, authorship and notices;
- pin provenance;
- prefer adapter-side compatibility over modifying upstream instructions;
- default to zero modification.

This strongly aligns with the owner requirement to preserve expert design/editorial taste.

### Package acquisition

`registry/packages.json` plus `installer/aiverse_skills_v3.py` support:

- `vendored` packages;
- `upstream-fetch` packages;
- exact source commit pins;
- deterministic selectors by path, repository root or Skill frontmatter name;
- support dependencies installed without necessarily being user-facing canonical capabilities.

### Immutable generations

The installer builds an entire generation, verifies package and generation digests, commits it immutably, then atomically activates the generation pointer.

Executions pin one generation before loading Skill content.

This is the correct lifecycle to use for the new composite capabilities. Do not create a second package/version system.

### Admission / trust

Current policy deliberately separates:

`integrity != admission != trust != readiness != authorization`

Unknown redistribution defaults to fetch-only. Package admission includes deterministic static checks and never grants runtime authority.

### Runtime exposure

Current adapters include:

- AI-Verse OS, current end-to-end public-beta path;
- Agent Skills-compatible directory exposure;
- Claude exposure;
- Codex exposure;
- Hermes exposure;
- OpenClaw exposure;
- Gemini exposure.

The new capabilities should use these existing adapters.

## 3. Registry constraint that matters

Current validation hard-enforces:

- 20 foundation Skills;
- 80 employee Skills;
- 100 canonical capabilities total.

Profiles and roles may reference only known employee Skill IDs.

Therefore new composites cannot simply be appended without intentionally changing this contract.

Possible future strategies to evaluate in later slices:

1. replace weaker/overlapping employee capabilities while preserving specialist packages as dependencies;
2. intentionally evolve the canonical capability-count contract;
3. introduce composite first-party packages plus non-canonical support dependencies through the existing package model.

No decision is made in this baseline audit. The correct option will be chosen only after overlap analysis.

## 4. Existing design-facing registry capabilities

The current registry already exposes the following design-related employee capabilities:

| ID | Source | Current handling |
|---|---|---|
| `brand-guidelines` | `anthropics/skills` | pinned upstream-fetch |
| `canvas-design` | `anthropics/skills` | pinned upstream-fetch |
| `figma-use` | `figma/mcp-server-guide` | pinned upstream-fetch |
| `figma-generate-design` | `figma/mcp-server-guide` | pinned upstream-fetch |
| `canva` | `social-media-skills/skills` | pinned upstream-fetch |
| `design-and-templates` | `social-media-skills/skills` | pinned upstream-fetch |
| `baoyu-article-illustrator` | `NousResearch/hermes-agent` | pinned upstream-fetch |
| `theme-factory` | `anthropics/skills` | pinned upstream-fetch |

These are currently present in creator/filmmaker/marketing profiles and the creative-director role in different combinations.

They are **not yet classified as keep/replace/migrate**. Their exact pinned upstream contents must be read before any removal.

## 5. Existing film/video-facing registry capabilities

The current registry already exposes:

| ID | Source | Current handling |
|---|---|---|
| `director-agent` | `62656456/ai-film-skills` | pinned upstream-fetch |
| `ai-storyboard-director` | `62656456/ai-film-skills` | pinned upstream-fetch |
| `produce-ai-video` | `62656456/ai-film-skills` | pinned upstream-fetch |
| `structure-screenplay` | `zhangzhangco/film-production-skills` | pinned upstream-fetch |
| `plan-camera-shots` | `zhangzhangco/film-production-skills` | pinned upstream-fetch |
| `ffmpeg-skill` | `kajisho5/ffmpeg-skill` | pinned upstream-fetch |
| `premiere-agent` | `Kemerd/premiere-agent` | pinned upstream-fetch |
| `after-effects-assistant` | `aedev-tools/adobe-agent-skills` | pinned upstream-fetch |
| `kanban-video-orchestrator` | `NousResearch/hermes-agent` | pinned upstream-fetch |
| `whisper` | `NousResearch/hermes-agent` | pinned upstream-fetch |

Current profiles/roles include dedicated:

- `creator` profile;
- `filmmaker` profile;
- `creative-director` role;
- `ai-filmmaker` role;
- `film-producer` role;
- `post-producer` role.

These routes must be migrated deliberately when the new Video Editor lands.

## 6. HyperFrames current-state finding

No physical HyperFrames Skill is present in the current AI-Verse-Skills tree.

No indexed `hyperframes` code-search result was found at planning time.

However the authoritative conclusion comes from the complete recursive tree audit: there is currently no committed HyperFrames package directory or `SKILL.md`.

The registry also does not currently define a HyperFrames source/package/provider.

Therefore HyperFrames is not duplicated **inside the current canonical registry/tree at this baseline**.

This must be rechecked immediately before implementation because other agents can change GitHub concurrently.

## 7. Release-state note

`release/component-release.json` reports accepted release revision:

`042fda1ea2ddd8b79b74f1db9d3f65212953b64a`

Current `main` is newer:

`fb0c138ef424734cd2e5359040f376e35c4c5875`

The new Interface Designer / Video Editor project must not assume the release descriptor automatically represents all later main-branch work. Release evidence must be refreshed only through the repo's existing release process.

## 8. Architectural conclusion for the two new composites

The existing repo already contains the infrastructure needed for:

- source pinning;
- fetch-only vs vendored decisions;
- original-upstream preservation;
- dependency packaging;
- trust/admission;
- immutable generations;
- runtime exposure;
- profiles/roles;
- deterministic validation.

Therefore:

**Do not build a second Skill system.**

The new capabilities should become first-class packages inside this existing architecture.

The likely shape to evaluate is:

- a first-party AI-Verse Interface Designer orchestrator;
- a first-party AI-Verse Video Editor orchestrator;
- expert upstream Skills retained as separately pinned specialist packages/dependencies;
- profiles/roles routed to the composites;
- old overlapping registry capabilities replaced only after their exact behavior is inspected and unique useful behavior is preserved.

## 9. Next audit slice

Read the exact pinned upstream contents of the existing design and film/video employee Skills, then classify every one as:

- KEEP;
- KEEP + NARROW;
- SPECIALIST DEPENDENCY;
- MIGRATE UNIQUE BEHAVIOR;
- SUPERSEDED;
- UNRELATED TO THE NEW COMPOSITES.

No existing design/video registry capability should be removed before that map exists.
