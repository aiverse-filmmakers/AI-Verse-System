# AI-Verse Interface Designer Upstream Source Pins

**Verified:** 2026-09-14  
**Purpose:** Phase 2 source/provenance baseline for AI-Verse Interface Designer  
**Implementation repo:** `aiverse-filmmakers/AI-Verse-Skills`

## Packaging rule

Use original upstream packages wherever possible. Preserve expert taste and package structure. Do not rewrite third-party Skills merely to make them sound like AI-Verse.

Any AI-Verse-specific routing, permission, generation, trust, or authorization behavior belongs outside the upstream Skill body.

## Selected core sources

| Capability | Upstream source | Pinned commit | Selected path(s) | License | Planned handling |
|---|---|---|---|---|---|
| Distinctive frontend art direction | `anthropics/skills` | `34040c9c568585f6929bedeaad110ad08f079624` | `skills/frontend-design/` | Apache-2.0 at package level | Vendor original package with attribution |
| UI/UX searchable design intelligence | `nextlevelbuilder/ui-ux-pro-max-skill` | `7f69fed6a2717900085f1bc3b263721f8ba025e2` | `.claude/skills/ui-ux-pro-max/` | MIT | Vendor original package with attribution |
| React performance | `vercel-labs/agent-skills` | `063bee94c3f4df8453406c830b0a7df0f2860278` | `skills/react-best-practices/` | MIT | Vendor or pinned-fetch original package |
| React component architecture | `vercel-labs/agent-skills` | `063bee94c3f4df8453406c830b0a7df0f2860278` | `skills/composition-patterns/` | MIT | Vendor or pinned-fetch original package |
| Web design/accessibility review | `vercel-labs/agent-skills` + rules source | skill: `063bee94c3f4df8453406c830b0a7df0f2860278`; rules: `e3d624baaf29dc1fc645aff3e38f03e564d2d6b1` | `skills/web-design-guidelines/`; `vercel-labs/web-interface-guidelines/command.md` | MIT | Preserve Skill logic, but freeze guideline rules into the immutable generation instead of runtime-fetching mutable `main` |
| shadcn project/component specialist | `shadcn-ui/ui` | `2b3e6d4f8d9161fe5c19340dc383aade392012dd` | `skills/shadcn/` | MIT | Conditional specialist only when project uses shadcn/components.json or user chooses it |
| Persistent visual identity format | `google-labs-code/design.md` | `9bf8eae67128b6cc55ad9bf86665767deb4c11cd` | spec/CLI methodology + project `DESIGN.md` | Apache-2.0 | Use as the project-local design-system persistence contract; do not force Google hosting/services |
| Reference-video reconstruction | `MengTo/Skills` | `321c769739b823de5eb94eb3a52aa1974fe783a2` | `agent-skills/codex/video-to-superprompt/` | MIT | Conditional specialist |
| Reliable full-page reference capture | `MengTo/Skills` | same | `agent-skills/codex/stitched-full-page-capture/` | MIT | Conditional specialist |
| Design-first specification | `MengTo/Skills` | same | `agent-skills/ui/design-first-ui-prompting/` | MIT | Conditional specialist / early-stage design analysis |
| Apple interaction physics | `emilkowalski/skills` | `d23d7f88a2e21c9e4b1418c7abe420f5c1052ba7` | `skills/apple-design/` | MIT | Preserve original package |
| Motion construction | `emilkowalski/skills` | same | `skills/animate/` | MIT | Preserve original package |
| Prototype/divergence workflow | `emilkowalski/skills` | same | `skills/prototype/` | MIT | Preserve original package |
| Animation QA | `emilkowalski/skills` | same | `skills/review-animations/` | MIT | Preserve original package |
| UI dependency/library selection | `emilkowalski/skills` | same | `skills/pick-ui-library/` | MIT | Preserve original package |
| Existing-animation audit | `emilkowalski/skills` | same | `skills/improve-animations/` | MIT | Conditional specialist |
| Animation-opportunity audit | `emilkowalski/skills` | same | `skills/find-animation-opportunities/` | MIT | Conditional specialist |
| Expo/native motion | `emilkowalski/skills` | same | `skills/animate-expo/` | MIT | Conditional React Native/Expo specialist |
| Immersive scroll/scrollytelling | `nateherkai/scroll-craft` | `0b816225945e45380397d6a0487efa3c98916858` | `plugins/nateherk-design/skills/scroll-craft/` | MIT | Preserve as conditional specialist, including its references/scripts when admitted |
| Optional Stitch ecosystem | `google-labs-code/stitch-skills` | `0337446dadde6f8c94210444e2aa9d546126480f` | selected Stitch utilities/build skills only when needed | Apache-2.0 | Optional provider set, never a core dependency |

## Explicit non-lock-in rules

These upstream packages do **not** force their vendors or stacks onto users.

- Vercel-authored Skills provide React/UI engineering knowledge; they do not require Vercel hosting.
- shadcn is loaded only when the project already uses it or the user intentionally selects it.
- React-only Skills are not loaded for plain HTML/CSS/JS, SwiftUI, native desktop, or other implementation targets.
- Figma/Canva/Stitch remain optional tool targets, not mandatory design surfaces.
- The Interface Designer decides the delivery target before loading implementation specialists.

## Expert-taste preservation

Preserve the following packages largely intact:

- Anthropic `frontend-design`;
- UI/UX Pro Max;
- Emil Kowalski's selected specialist Skills;
- Meng To reference-analysis specialists;
- Scroll Craft;
- shadcn Skill when selected.

Do not merge them into one giant prompt.

The AI-Verse orchestrator owns:

- scope classification;
- capability routing;
- stage order;
- conflict priority;
- context minimization;
- verification orchestration.

The upstream experts own their specialist craft.

## Necessary bounded adaptations

### Vercel web-design-guidelines

The upstream Skill currently says to fetch the latest rules from a mutable URL each time.

That conflicts with AI-Verse immutable-generation reproducibility.

AI-Verse should preserve the review methodology while resolving the rules to an exact pinned snapshot during package-generation/update time.

Accepted adaptation:

1. pin `vercel-labs/web-interface-guidelines@e3d624baaf29dc1fc645aff3e38f03e564d2d6b1`;
2. include or generation-materialize its `command.md` as a package reference;
3. adjust only the rules-loading line in the AI-Verse compatibility wrapper if required;
4. record `modified: true` only for that compatibility wrapper, not falsely claim the original Skill is unchanged;
5. review a newer upstream rules commit during future Skills updates before it replaces the generation.

This preserves the actual Vercel review rules while removing mutable runtime drift.

### Google DESIGN.md

This is a format/specification and CLI, not a conventional UI design Skill.

Use it as a persistent project artifact contract, not as an always-loaded expert.

### Scroll Craft global concepts

Do not extract and then delete Scroll Craft.

Keep the original specialist intact. The AI-Verse-native orchestrator may independently implement general routing concepts inspired by it, such as:

- design fingerprint gate;
- signature interaction;
- major-flow feeling curve;
- separate mobile art direction;
- state/scroll visual verification.

The specialist remains available for actual scroll-driven experiences.

## Sources intentionally not made core

- `emil-design-eng`: broad umbrella overlap; narrower Emil Skills preserve the useful specialist knowledge with less context collision.
- narrow Sonner helper: only needed if a project actually uses Sonner.
- Swift specialist: may be added later as a native implementation provider, but it is not required to prove Interface Designer composition.
- Google Stitch packages: useful optional integrations, but they require Stitch-specific infrastructure and must not become a baseline dependency.

## License conclusion

Current selected source licenses permit the planned redistribution/adaptation routes:

- Apache-2.0: Anthropic frontend-design package, Google DESIGN.md, Google Stitch Skills.
- MIT: UI/UX Pro Max, Vercel Agent Skills, Vercel Web Interface Guidelines, shadcn/ui, Meng To Skills, Emil Kowalski Skills, Scroll Craft.

All required license/notice text must be retained in the final AI-Verse distribution metadata or vendored package according to the applicable license.

## Next

Define the canonical semantic capability map and package/provider structure using the existing AI-Verse Skills immutable-generation architecture.