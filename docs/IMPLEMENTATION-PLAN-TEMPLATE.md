# Implementation Plan Template

Use only as much structure as the change needs. A small fix can be a few paragraphs; a cross-component migration needs more detail. Omit irrelevant prompts without explaining their absence. The [Adaptive Implementation Planning Skill](ADAPTIVE-IMPLEMENTATION-PLANNING-SKILL.md) is the rule source.

A plan does not authorize implementation, checks, external actions or publication. Record only useful metadata: <owner, repository, source revision, date and current status>.

## 1. Problem and boundary

- **Observed problem and intended behavior:** <who encounters it, concrete before/after and supporting evidence>
- **Scope:** <what this change must accomplish and its boundaries>
- **Preserve:** <existing behavior, data, contracts and ownership that this change could affect>

## 2. Existing path and smallest change

- **Current implementation:** <relevant caller → logic → state/effects → result; exact useful file, symbol or contract references>
- **Reuse first:** <what already works and the smallest complete correction, wiring or extension needed; no code change if existing behavior meets the requirement>
- **Design choice:** <why this is the smallest maintainable solution; explain a new dependency, service, store or abstraction only if one is necessary>

Keep compatibility, permissions, data preservation and recovery details beside the change they constrain. Add contract, migration, security or architecture detail only where the actual work needs it. Exclude unrelated cleanup and speculative infrastructure.

## 3. Acceptance and planned verification

| ID | Observable behavior to establish or preserve | Planned verification and expected result |
|---|---|---|
| A1 | <success, relevant failure or unaffected behavior> | <exact command with working directory, caller or observation; expected result> |

Record each requirement once. Stronger proof may clarify an existing requirement; a new behavior or quality target is a scope decision, not an automatic addition. Include performance, accessibility, resource or cost targets only when they matter to this change.

Describe planned checks here; record actual evidence only after authorized execution. Reuse relevant existing checks and add only the coverage needed to demonstrate the behavior.

## 4. Execution

<Use a short sequence for a single change. Create slices only for outcomes that can be completed and verified separately. Detail the next work; keep later milestones broad.>

### <Slice, only if needed> — <one complete outcome>

- **Acceptance references / owner:** <A1, A2; relevant repository or component owner>
- **Change:** <bounded surfaces and immediate steps, using existing entry points>
- **Dependencies or start condition:** <only evidence or decisions required before this work>
- **Delivery and recovery:** <only rollout, disable, migration or recovery steps this change needs>

Reference section 3 instead of copying acceptance criteria or checks into every slice. Do not add a phase, subsystem or review ceremony merely to fill the template.

## 5. Checkpoint and next action

- **Confirmed:** <current implementation facts and links to evidence>
- **Assumptions / blockers:** <only unresolved points that could change the implementation, with the next evidence or decision needed>
- **Status and next action:** <what is complete, what remains and the next concrete step>
- **Execution evidence:** <when available: what ran, result and artifact/ref; distinguish local, merged, qualified and released>

Keep one living plan. Replace stale statements as work changes and link detailed evidence rather than duplicating it. A plan is ready when the next implementer can make the bounded change and demonstrate it without inventing requirements.
