# AI-Verse Interface Designer Capability + Routing Map

**Date:** 2026-09-14  
**Status:** Phase 3 architecture baseline  
**Primary entrypoint:** interface-designer

## 1. User-facing contract

A user should be able to ask for a page, website, artifact, dashboard, app interface, redesign, reference recreation, interaction, or immersive web experience without naming a framework or expert Skill.

The Interface Designer determines:

1. task scope;
2. delivery target;
3. whether a reference exists;
4. whether the product already has a DESIGN.md;
5. which design stages are needed;
6. the smallest expert subset needed;
7. the required QA gates.

It does not migrate the user's stack merely because one expert prefers a stack.

## 2. Scope classes

- MICRO_CHANGE
- COMPONENT
- SCREEN
- MULTI_SCREEN_FLOW
- FULL_PRODUCT
- REFERENCE_RECREATION
- INTERACTION_HEAVY
- DESIGN_SYSTEM_CHANGE
- SCROLL_IMMERSIVE
- MOBILE_EXPO

Scope controls pipeline depth.

## 3. Delivery-target classes

- PLAIN_HTML_CSS_JS_ARTIFACT
- EXISTING_WEB_STACK
- REACT_WEB_APP
- PWA
- FIGMA
- CANVA_OR_STATIC_DESIGN_TOOL
- DESKTOP_WEBVIEW_APP
- NATIVE_DESKTOP_APP
- REACT_NATIVE_EXPO
- PROTOTYPE_ONLY
- DESIGN_ONLY_HANDOFF
- CODE_DRIVEN_VIDEO_MOTION_HANDOFF

The target is detected from the existing project and user request.

Never assume React, Vercel, shadcn, Tailwind, Node, Figma or Canva.

## 4. Semantic capability map

| Semantic capability | Preferred expert capability | When loaded |
|---|---|---|
| interface.orchestrate | interface-designer | broad or multi-stage interface jobs |
| design.visual-direction | frontend-design | new direction, redesign, anti-generic art direction |
| design.ui-ux-intelligence | ui-ux-pro-max | product type, UX, typography, palette, layout, accessibility/design-system choices |
| design.specification | design-first-ui-prompting | vague brief or when a builder-ready design spec is needed |
| design.reference-video-analysis | video-to-superprompt | reference video supplied for recreation/inspiration |
| design.reference-page-capture | stitched-full-page-capture | live reference page needs trustworthy full-page evidence |
| design.system.persistence | Google DESIGN.md contract | substantial product/page system; existing DESIGN.md is read first |
| design.prototype-divergence | prototype | substantial or ambiguous design decision where alternatives add value |
| design.interaction-physics | apple-design | drag/swipe/sheet/drawer/carousel/spatial/interruptible/physical interaction |
| frontend.library-selection | pick-ui-library | new UI dependency/component library decision is needed |
| frontend.react-quality | react-best-practices | only when React/Next is actually used |
| frontend.react-architecture | composition-patterns | only for React component/API architecture |
| frontend.shadcn | shadcn | only when project uses components.json/shadcn or user selects it |
| motion.build | animate | meaningful UI animation must be implemented |
| motion.review | review-animations | significant UI motion exists and needs delivery QA |
| motion.audit | improve-animations | user asks to improve/audit existing animation system |
| motion.opportunity-scan | find-animation-opportunities | explicit polish pass after functional UI is mature |
| mobile.expo-motion | animate-expo | React Native/Expo motion work |
| web.final-review | web-design-guidelines | substantial web UI delivery/review |
| experience.scrollcraft | scroll-craft | cinematic scroll/scrollytelling/scroll-scrubbed immersive work |

Existing AI-Verse specialists outside the new 18 remain available when target-specific:

- figma-use
- figma-generate-design
- canva
- canvas-design
- theme-factory
- design-and-templates

They are not default Interface Designer stages.

## 5. Trigger rules

### Reference triggers

If the user supplies or names:

- screenshot;
- reference video;
- URL;
- live page;
- "copy this";
- "make it like this";
- "recreate this";
- "same feel as";

then classify REFERENCE_RECREATION and load only the reference specialists required by the media type.

Video reference:
video-to-superprompt.

Live scroll-heavy page:
stitched-full-page-capture when native full-page capture is not trustworthy.

### Prototype triggers

Load prototype when:

- full product visual direction is unresolved;
- user explicitly asks for options;
- a major component/system has multiple viable interaction models;
- redesign involves a meaningful structural choice.

Do not load prototype for:

- padding;
- copy changes;
- icon swaps;
- bug fixes;
- small visual adjustments;
- an already locked reference recreation unless the user asks for alternatives.

### Apple interaction triggers

Load apple-design for:

- drag;
- swipe;
- sheet;
- drawer;
- carousel;
- direct manipulation;
- reordering;
- momentum;
- spring;
- rubber-band;
- interruptible transitions;
- spatial continuity;
- shared-element motion;
- touch-first/native-feeling interaction.

Do not use Apple aesthetics as a mandatory visual style.

The Skill contributes interaction craft, not an instruction to make everything look like iOS.

### Scroll Craft triggers

Load scroll-craft only for:

- immersive scroll storytelling;
- scroll-driven product narrative;
- scroll-scrubbed video or image sequence;
- cinematic launch/marketing page;
- explicitly Apple-style product-story website;
- user asks for a page where scroll itself is the interaction.

Do not load it for ordinary dashboards/settings/chat/admin screens.

### React triggers

Load react-best-practices and composition-patterns only when source inspection confirms React/Next or the user explicitly selects React.

A plain GitHub Pages artifact remains plain HTML/CSS/JS unless migration is requested.

### shadcn triggers

Load shadcn only when:

- components.json exists;
- existing project is shadcn;
- user explicitly chooses shadcn;
- a new React project has already selected shadcn through a stack decision.

Never choose shadcn because it is installed in AI-Verse.

## 6. Full-product pipeline

For a substantial new product/interface:

1. classify scope and target;
2. inspect project instructions and existing DESIGN.md;
3. analyze references if present;
4. ui-ux-pro-max for design intelligence;
5. frontend-design for art direction;
6. prototype when divergence is useful;
7. lock/update DESIGN.md;
8. plan component/information architecture;
9. pick-ui-library if implementation needs a dependency decision;
10. load target-specific implementation experts;
11. apple-design when interaction physics matters;
12. animate when meaningful motion is required;
13. implement;
14. render/preview in the actual target;
15. visual state QA;
16. review-animations when motion exists;
17. web-design-guidelines for substantial web UI;
18. fix failures and re-run affected gates.

This is a maximum path, not a mandatory list.

## 7. Micro-task pipeline

For a small change:

1. read local project conventions/DESIGN.md;
2. identify target;
3. load only the directly relevant expert if needed;
4. make change;
5. verify affected state.

No prototype, global redesign or unrelated expert loading.

## 8. Reference-recreation pipeline

1. establish exact vs inspired boundary;
2. capture/inspect reference evidence;
3. extract layout, typography, materials, hierarchy and motion;
4. identify implementation target;
5. create/update DESIGN.md only when the recreation becomes a persistent product direction;
6. implement with target-specific experts;
7. compare rendered output against reference evidence;
8. iterate on visible deltas;
9. run accessibility/responsive/reduced-motion checks.

Do not copy protected branding/assets beyond the user's authorized scope.

## 9. Native/desktop behavior

Design intelligence remains useful for native apps.

For native targets:

- ui-ux-pro-max remains useful;
- frontend-design remains useful for art direction;
- apple-design is useful for interaction craft when appropriate;
- DESIGN.md remains useful as visual system memory;
- React/Vercel/shadcn experts are skipped unless the app actually uses a web/React layer.

If no approved native coding specialist exists for the target, Interface Designer may produce the design/spec and work with the project's existing native implementation conventions rather than migrating to web technology.

## 10. Video/motion handoff

When the output is a rendered video/motion composition rather than an interactive interface:

- Interface Designer may provide visual direction, typography, layout and reference recreation;
- hand execution to AI-Verse Video Editor / HyperFrames route;
- do not let web UX rules override video editorial/timing rules.

## 11. Conflict precedence

Apply this order:

1. explicit current user instruction;
2. repository/project authority and locked constraints;
3. existing project DESIGN.md;
4. exact reference boundary chosen by user;
5. target/runtime correctness rules;
6. specialist domain authority;
7. general visual taste recommendations;
8. optional polish.

Examples:

- HyperFrames render rule beats generic UI animation advice in a video project.
- Existing native app architecture beats a React recommendation.
- Existing DESIGN.md beats a generic palette suggestion.
- User-requested reference fidelity beats originality pressure.
- Accessibility/correctness beats decorative flourish.

## 12. Originality gate

For new visual directions, compare:

- navigation model;
- information architecture;
- layout grammar;
- density;
- typography hierarchy;
- surface/material treatment;
- interaction model;
- motion language;
- primary composition;
- signature element.

The gate prevents accidental template repetition.

It must not force novelty when:

- reference fidelity is requested;
- an established product DESIGN.md requires consistency;
- conventional platform behavior is the usability-safe choice.

## 13. Signature interaction

For marketing/immersive experiences, identify one meaningful signature interaction when appropriate.

For working applications, signature behavior is optional and must serve function.

Do not add novelty that slows frequent workflows.

## 14. QA minimums

For substantial interfaces verify, where applicable:

- initial;
- loading;
- empty;
- populated;
- error;
- disabled;
- hover;
- focus;
- active;
- expanded/collapsed;
- dialog/sheet;
- desktop;
- tablet;
- mobile;
- light/dark;
- reduced motion.

For scroll experiences, also inspect multiple actual scroll positions.

## 15. Existing capability migration conclusion

No existing design capability from the Phase 1 overlap map is removed.

The new orchestrator and 18 specialists expand the catalog.

The 100-capability benchmark evolves to the shared 120-capability target described in AI-VERSE-COMPOSITE-SKILL-PACKAGING-DECISION-2026-09-14.md.

## Next

Implement the first-party interface-designer package and register the 18 pinned experts using the existing AI-Verse package, trust and immutable-generation model.
