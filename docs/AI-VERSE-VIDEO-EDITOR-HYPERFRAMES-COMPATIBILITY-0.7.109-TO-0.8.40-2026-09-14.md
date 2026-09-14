# AI-Verse Video Editor - HyperFrames 0.7.109 to 0.8.40 Compatibility Matrix

**Date:** 2026-09-14  
**Nate kit:** `nateherkai/hyperframes-student-kit@b1afdb1dcbcad39dd27638ea699f132fe44ce6df`  
**Nate tested HyperFrames:** `v0.7.109` / `12fd6d9087fab1347f8737c34901e3db61e4dfee`  
**Candidate HyperFrames:** `v0.8.40` / `cfe5dcfad310ced2a5844998628daa2b8a0f53d7`  
**Candidate CLI:** `@hyperframes/cli@0.8.40`, Apache-2.0, Node >=22

## Executive result

**Compatibility verdict:** `COMPATIBLE WITH REQUIRED ADAPTATION AND MEDIA ACCEPTANCE TESTS`

Nothing found in this source-level comparison requires AI-Verse to remain on HyperFrames 0.7.109.

However, Nate's student kit must **not** be upgraded by merely changing:

```json
"hyperframes": "0.7.109"
```

to:

```json
"hyperframes": "0.8.40"
```

Nate's editorial intelligence remains valuable and should be preserved. His bundled HyperFrames technical guidance reflects the older provider architecture and contains several rules that are now deprecated, overly strict, or incorrect for 0.8.40.

The safe target is:

```text
Nate editorial logic
  +
adapted Nate editorial helpers/tests
  +
one canonical HyperFrames 0.8.40 provider family
```

not:

```text
Nate's old HyperFrames Skill copies
  +
new HyperFrames 0.8.40 Skill copies
```

## Status vocabulary

- **UNCHANGED** - behavior/contract is materially the same.
- **COMPATIBLE** - old usage still works.
- **IMPROVED** - compatible and meaningfully stronger.
- **MIGRATION REQUIRED** - old guidance still may run but new AI-Verse material must change.
- **BEHAVIOR CHANGED** - default/semantics changed; explicit Nate behavior may still be safe.
- **OBSOLETE GUIDANCE** - old rule is no longer correct.
- **TEST REQUIRED** - source-level compatibility is promising but media/runtime acceptance is still required.
- **NOT APPLICABLE** - change does not touch Nate's used surface.

## Runtime and tooling matrix

| Surface | Nate 0.7.109 assumption/use | HyperFrames 0.8.40 | Status | AI-Verse action |
|---|---|---|---|---|
| Node runtime | Node >=22 | CLI still requires Node >=22 | UNCHANGED | Preserve >=22 floor |
| GSAP | Nate pins 3.14.2 | Current exact v0.8.40 guidance still loads GSAP 3.14.2 | UNCHANGED | Preserve 3.14.2 where directly pinned |
| CLI binary | `npx hyperframes` | Same | UNCHANGED | Use canonical CLI |
| `init` | older examples/template expectations | default now centered title on dark frame | BEHAVIOR CHANGED | Do not rely on old implicit scaffold; create/verify project state explicitly |
| `lint` | required | maintained | COMPATIBLE | Keep |
| `validate` | Nate uses as final browser/contrast gate | still exists but explicitly deprecated | MIGRATION REQUIRED | Replace new/adapted guidance with `check`; do not ship new `validate` instructions |
| `check` | absent from Nate baseline | canonical maintained runtime/layout/motion/media/contrast gate | IMPROVED | Make this the required post-build gate |
| `inspect` / `layout` | not materially used in Nate core | deprecated compatibility aliases | NOT APPLICABLE | Do not introduce them |
| `preview` | Studio/browser review | still supported, richer context/selection surfaces | IMPROVED | Keep and test |
| `snapshot` | representative frame review | still supported | COMPATIBLE | Keep and expand frame QA |
| `render` | normal final output | maintained | COMPATIBLE | Keep and test actual encoded output |
| `--quality draft` | iteration | supported | UNCHANGED | Keep |
| `--quality standard` | final/common Nate path | still accepted | COMPATIBLE | Accept old projects; prefer `looks` in new guidance when appropriate |
| `--quality high` | final/archive Nate path | still accepted | COMPATIBLE | Accept old projects; prefer `delivery` in new guidance |
| `--quality looks` | not in Nate baseline | new default alias to standard + CRF 16 | IMPROVED | Use for first real encode/new default path |
| `--quality delivery` | not in Nate baseline | alias to high | IMPROVED | Use for new final-delivery guidance |
| Docker render | reproducible/archive use | supported | COMPATIBLE | Preserve as optional reproducible path |
| MP4/WebM | Nate supported | supported | COMPATIBLE | Preserve |
| MOV / PNG sequence | not central Nate baseline | first-class current output paths | IMPROVED | Optional future expansion, not required for initial Video Editor |
| `transcribe` | audio/video + model + language, JSON word timing | still supported | COMPATIBLE | Preserve |
| JSON transcript IDs | no stable generated IDs assumed | v0.8.39 adds `w0`, `w1`, ... | IMPROVED | Exploit only after 3.3 tests; do not replace Nate EDL/source-time truth |
| TTS | used by some Nate workflows | current provider still exposes TTS/media domain | COMPATIBLE | Keep conditionally |
| Registry `add` | install blocks/components | maintained, dependency-aware, compatibility-gated | IMPROVED | Use canonical registry provider |
| Registry `catalog` | discovery | maintained and expanded | IMPROVED | Preserve intent-first search |
| Studio | preview/edit | significantly richer | IMPROVED / TEST REQUIRED | Test Nate representative compositions in current Studio |
| render metadata | not relied on for authority | current unsigned HyperFrames tags are diagnostic only | COMPATIBLE | Never treat metadata as authenticity/licensing proof |

## Composition contract matrix

| Surface | Nate baseline | v0.8.40 | Status | AI-Verse action |
|---|---|---|---|---|
| HTML as video source | yes | yes | UNCHANGED | Preserve |
| `data-composition-id` | required | canonical | UNCHANGED | Preserve |
| `data-start` | canonical | canonical | UNCHANGED | Preserve |
| `data-duration` | canonical | canonical, semantics more explicit | COMPATIBLE | Preserve; adopt current compile-time root-duration rules |
| `data-media-start` | canonical trim offset | canonical | UNCHANGED | Preserve |
| `data-composition-src` | nested comps | canonical | UNCHANGED | Preserve |
| `data-playback-start` | limited Nate usage | supported | COMPATIBLE | Use current contract if needed |
| `data-track-index` | Nate says same-track overlap is forbidden | Studio lane/display metadata; render allows overlap | OBSOLETE GUIDANCE | Remove hard prohibition. Track overlap should be an editorial/layout decision, not a false runtime law |
| `class="clip"` | Nate treats as required on timed visual elements | convention/edit hint; lint warns when absent, runtime does not require it | COMPATIBLE / GUIDANCE RELAXED | Continue using it where appropriate without claiming runtime hard requirement |
| muted video + separate audio | Nate standard | current documented pattern for independent picture/sound editing | COMPATIBLE | Preserve |
| media `id` | not always emphasized in old guidance | every video/audio needs stable id; id-less audio can render silent | MIGRATION REQUIRED | Make media IDs a mandatory adapted rule and test Nate fixtures |
| `crossorigin` | Nate broad Skill says add `crossorigin="anonymous"` to external media | current lint rejects `crossorigin` on video/audio | MIGRATION REQUIRED | Remove blanket media rule. Do not add `crossorigin` to video/audio. Image/script/font cases remain separate |
| nested media timing | Nate predates current explicit local-basis rule | nested media `data-start` is scene-local and rebased to root; legacy root basis needs explicit marker | BEHAVIOR CLARIFIED / TEST REQUIRED | Test representative Nate nested-media projects; never infer global basis from numbers |
| framework-owned playback | Nate forbids manual play/pause/seek | same | UNCHANGED | Preserve |
| GSAP timeline | paused, seek-driven | same | UNCHANGED | Preserve |
| timeline key | `window.__timelines[id]` matches composition id | same | UNCHANGED | Preserve |
| async timeline build | Nate blanket forbids async construction | current supports async setup if registration occurs only after build completes | OBSOLETE OVER-RESTRICTION | Synchronous remains safe; adapt guidance to current precise rule instead of preserving false prohibition |
| unseeded randomness | banned | banned | UNCHANGED | Preserve |
| infinite repeat | banned | banned | UNCHANGED | Preserve |
| finite repeat formula | Nate explicitly recommends `ceil(duration/cycle)-1` | current rules require floor-based bounded count; ceil can overshoot and lint | MIGRATION REQUIRED | Replace old formula with current floor-based formula |
| empty tween for duration | Nate checklists/examples may pad timelines | current says use root/clip `data-duration`, do not pad with empty tweens | MIGRATION REQUIRED | Remove duration-padding pattern from adapted guidance |
| clip visibility | framework owned | framework owned, stricter lint | COMPATIBLE | Preserve; animate children rather than fight clip lifecycle |
| media nesting | older Nate restrictions are broad | current runtime supports media at any nesting depth with one timed-wrapper constraint | GUIDANCE RELAXED | Use current rule, not obsolete blanket restrictions |

## Skill architecture matrix

| Nate package/surface | Nate role | 0.8.40 relationship | Decision |
|---|---|---|---|
| `hyperframes` | broad technical + visual + workflow Skill | current main `hyperframes` is mandatory router/workflow owner | **REPLACE NATE TECHNICAL COPY WITH CURRENT CANONICAL PROVIDER** |
| `hyperframes-cli` | CLI instructions | current dedicated CLI Skill is richer/current | **REPLACE WITH CURRENT CANONICAL PROVIDER** |
| `hyperframes-registry` | registry discovery/install | current registry Skill is richer/current | **REPLACE WITH CURRENT CANONICAL PROVIDER** |
| `gsap` | generic GSAP guidance adapted for Nate | current HyperFrames animation/keyframes family contains renderer-aware GSAP rules and still uses 3.14.2 | **DO NOT CREATE A SECOND HYPERFRAMES GSAP OWNER**; preserve uniquely useful Nate motion taste elsewhere if any |
| `hyperframes-video-beats` | Nate beat/timing helper | no identical current upstream editorial equivalent | **KEEP NATE-DERIVED SPECIALIST**, migrate technical assumptions |
| `edit-video` | Nate master editorial route | current HyperFrames `general-video` has creator-edit mechanics but not Nate's exact editorial ownership model | **KEEP NATE-DERIVED EDITORIAL OWNER** |
| `cut-silences` | deterministic silence edit | renderer-independent Nate procedure | **KEEP NATE-DERIVED** |
| `cut-mistakes` | review-gated mistakes/retakes | renderer-independent editorial procedure | **KEEP NATE-DERIVED** |
| `short-form-edit` | modern Nate short-form editorial system | current upstream offers general/specialized video workflows but not this exact editorial philosophy | **KEEP NATE-DERIVED** |
| `short-form-video` | legacy Nate short-form path | superseded inside Nate kit by short-form-edit | **DO NOT PROMOTE AS NEW CANONICAL MEMBER CAPABILITY**; preserve only migration/reference value if needed |
| `video-storytelling` | editorial/visual storytelling | useful unique taste above renderer | **KEEP NATE-DERIVED** |
| `make-a-video` | old general video intake/build workflow | overlaps current main HyperFrames router and Nate edit-video/short-form routes | **MIGRATE UNIQUE NATE INTAKE/EDITORIAL VALUE; DO NOT SHIP AS A SECOND TOP-LEVEL ROUTER UNCHANGED** |
| `style-library` | Nate-specific style system | distinct from HyperFrames registry and Interface Designer | **KEEP NARROW** if its reusable style assets pass licensing/provenance review; do not copy demo brands as generic assets |
| `website-to-hyperframes` | site-to-video workflow | current HyperFrames has product/site workflows, but Nate workflow contains useful process/taste | **KEEP/ADAPT AS CONDITIONAL SPECIALIST**, migrate CLI/provider rules |

## Nate editorial invariants that remain above HyperFrames

The candidate runtime does not supersede these Nate-owned editorial decisions:

- source-video identity and provenance;
- transcript truth;
- source-time to edited-time mapping;
- silence/dead-air decisions;
- false-start/stutter/retake judgment;
- review-gated mistake removal;
- EDL construction and retiming;
- clean-cut derivation;
- dependency rebuild when cut timing changes;
- hook/open-loop/payoff structure;
- first-three-seconds editorial judgment;
- B-roll selection/provenance;
- authentic brand asset verification;
- multi-ratio editorial reframing;
- final A/V sync and edit continuity.

Current HyperFrames may provide mechanics for cuts, trims, camera moves, audio mixing, captions or rendering. Those mechanics do not become canonical editorial authority.

## Concrete Nate baseline migrations required

### 1. `validate` -> `check`

Found in Nate's:

- bundled HyperFrames Skill;
- house-style;
- website-to-hyperframes workflow and validation step;
- mirrored Claude/Agents copies.

AI-Verse adaptations must use:

```bash
npx hyperframes lint
npx hyperframes check
```

### 2. Remove blanket `crossorigin` advice for media

Nate's bundled HyperFrames Skill says:

> Add crossorigin="anonymous" to external media

That is unsafe under the current contract for video/audio. v0.8.40 lint explicitly rejects `crossorigin` on those elements.

This does **not** mean all HTML `crossorigin` attributes are forbidden. Nate examples use it validly for scripts/fonts/images in places. The migration must be media-element specific.

### 3. Correct track-index semantics

Nate repeatedly states same-track clips cannot overlap.

Current HyperFrames states `data-track-index` is a Studio display lane and does not constrain renderer overlap.

Adapted Nate material may still choose separate lanes for clarity, but must not call it a runtime requirement.

### 4. Correct finite-repeat formula

Nate's bundled HyperFrames Skill says:

```js
repeat: Math.ceil(duration / cycleDuration) - 1
```

Current deterministic guidance uses a floor-based bounded count because ceil can overshoot the visible duration and trip lint.

New AI-Verse guidance must use the current provider's formula.

### 5. Remove timeline-duration padding pattern

Nate checklists contain older empty-tween duration padding.

Current provider explicitly says composition/clip `data-duration` owns visible/render duration and empty duration tweens should not be used to pad the timeline.

### 6. Make media IDs explicit

Current lint/runtime behavior makes IDs consequential, especially for audio mixing.

Adapted AI-Verse Video Editor must require stable IDs on placed audio/video.

### 7. Preserve one provider family

Do not package:

- Nate `hyperframes`;
- Nate `hyperframes-cli`;
- Nate `hyperframes-registry`;

as canonical copies alongside the current upstream equivalents.

Instead, Nate-derived editorial Skills call the one approved HyperFrames provider family.

## Studio-server breaking changes

v0.8.36 changed internal Studio-server API names/shapes.

Search of Nate's pinned student kit found no use of:

- `consumeFileWriteReceipt`;
- `BROWSER_HOSTILE_CODECS`.

Therefore this breaking change is **not currently a Nate compatibility blocker**.

## Candidate upgrade decision before media tests

Source-level result:

```text
HyperFrames 0.8.40
    = viable candidate
    != accepted canonical version yet
```

Required next gate is live isolated acceptance against Nate-relevant media behavior:

1. Nate kit internal tests;
2. Skill mirror checks;
3. synthetic/representative media;
4. lint;
5. current `check`;
6. Studio preview;
7. draft/looks render;
8. extracted-frame visual verification;
9. transcript/EDL timing;
10. audio presence and A/V sync;
11. representative short-form path;
12. representative longer/motion path.

Only if that passes may Slice 3.4 select 0.8.40 as the canonical AI-Verse HyperFrames provider.
