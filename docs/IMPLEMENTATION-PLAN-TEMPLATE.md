# Implementation Plan Template

Use this as a starting structure for work that needs a written plan. Scale it to the risk; remove unused prompts. The [Adaptive Implementation Planning Skill](ADAPTIVE-IMPLEMENTATION-PLANNING-SKILL.md) remains the rule source. A template does not authorize implementation, tests, external actions or publication.

## Plan details

- **Outcome / owner / repository:** <what changes and who owns it>
- **Planning depth:** <compact / standard / extended; why this is enough>
- **Current revision and status:** <exact source ref; local / proposed / accepted / implementing>
- **Fixed outcomes:** <slice count if there is more than one>

## Product brief

- **Who needs this and what happens today:** <observed evidence>
- **Desired result / main journey:** <plain language>
- **Scope and non-goals:** <bounded>
- **Behavior, data and contracts to preserve:** <invariants>
- **Assumptions or decisions still open:** <impact, owner and next evidence>

## Requirements and checks

| ID | Observable success, important failure and unaffected behavior | Owner / slice | Verification and expected result |
|---|---|---|---|
| R01 | <specific behavior> | <owner / slice> | <caller, command or observation> |

Relevant performance, resource, accessibility or cost target: <evidence or measurement task; omit with reason if not relevant>.

## Current flow and design choice

- **Current caller and owner path:** <trigger → validation → logic → state/effects → result or failure>
- **Reuse / extend / create / retire / blocked:** <existing mechanisms and owners>
- **Chosen design and simpler alternative:** <why this meets the requirement with the least ongoing burden>
- **New dependency, service, store, abstraction or configuration:** <requirement and why existing facilities are insufficient; or none>
- **Compatibility, permission and recovery boundary:** <what must remain safe>

## Applicable risks

| Risk area | Decision and evidence | Owner or open blocker |
|---|---|---|
| <relevant privacy, security, state, concurrency, platform, UX or AI risk> | <concrete mitigation/check or reason it does not apply> | <owner / none> |

## Phases and slices

### Slice <ID> — <one stable outcome>

- **Requirement IDs / owner:**
- **Dependencies and exact start evidence:**
- **Bounded repository and surface:**
- **Acceptance and required evidence:**
- **First useful behavior/check:** <public failure → smallest complete fix → green/refactor, or characterization/document review>
- **Rollout, disable and recovery:**
- **Completion evidence and next slice:**

<Repeat only for actual outcomes. Derive detailed tasks when each slice starts.>

## Reviews and progress

- **Product/architecture:** <requirements, ownership, risks, simpler approach>
- **Code/adversarial:** <diff, failure paths, test quality and simplification>
- **Behavior/delivery:** <real journey, supported platforms, release truth and recovery>
- **Current checkpoint:** <accepted/total slices; exact refs; local vs merged vs qualified vs released>
- **Next action / blocker:**

## Choosing depth: small examples

- **Compact:** fix one parser edge case with a known owner; record current behavior, one regression, the focused check and recovery.
- **Standard:** add a read-only capability used by several callers; map the user journey, requirements, existing flow, scope and failure behavior.
- **Extended:** change an owner-backed migration across components; add contract decisions, data preservation, compatibility, interruption/recovery, owner checks and composed qualification.

Avoid repeating the method's permanent laws. Keep one living plan and link detailed evidence instead of duplicating it.
