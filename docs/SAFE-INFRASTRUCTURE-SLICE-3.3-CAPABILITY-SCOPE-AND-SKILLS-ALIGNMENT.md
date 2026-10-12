# Safe Infrastructure Slice 3.3 - Capability Scope and Skills Generation Alignment

**Status:** COMPLETE - IMPLEMENTED AND VALIDATED  
**Slice:** 3.3 - Implement cross-provider capability scope semantics and managed Skills generation alignment  
**Date:** 2026-10-12

## Refreshed refs

- `aiverse-filmmakers/AI-Verse-System@e6c20a1cd7c60d17095f4f24bd3745848667e924` at slice audit refresh
- Slice 3.3 task list recorded at `aiverse-filmmakers/AI-Verse-System@6a3cc21215b66fbafae72121efaabb0c57983279`
- starting OS ref: `aiverse-filmmakers/AI-Verse-OS@88ce41a95554e1323ba34aa71b536b9e98475808`
- final OS implementation ref: `aiverse-filmmakers/AI-Verse-OS@01571824d18421ea71251556b47c3308bfef4446`
- Skills ref: `aiverse-filmmakers/AI-Verse-Skills@afde5c06307fba7d074de2929c2eb6c3dc6bdab8`

## Decision

OS now exposes one practical placement planner for new user-owned capabilities while preserving the existing four provider identities and leaving managed Skills lifecycle ownership unchanged.

The placement law is:

- "only use this in this project" -> the trusted active Workspace provider;
- "use this for all YouTube work" or another practical related-work intent -> the user-owned `local` provider, retaining the practical context label without inventing another provider class;
- "use this everywhere" -> the user-owned `local` provider.

`os` is not a user-authoring target. `aiverse-skills` is not a user-authoring target. Publishing into the managed distribution remains a separate reviewed Skills-owned action.

This prevents a reusable capability from being trapped in Workspace-private storage merely because it was first conceived while a Workspace was active.

## OS implementation

Implemented at `aiverse-filmmakers/AI-Verse-OS@01571824d18421ea71251556b47c3308bfef4446`.

Changes:

- `scripts/capability-placement.mjs`
  - adds `aiverse-capability-placement-v1`;
  - normalizes practical placement intent;
  - maps project-only placement to the trusted Workspace;
  - maps related/all-work reuse to the user-owned local provider;
  - rejects internal provider words as member placement intent;
  - identifies cross-provider promotion as a separate unapplied migration requirement;
  - blocks OS/managed-distribution capabilities as personal writable placement sources.
- `scripts/capability-resolver.mjs`
  - exposes `planCapabilityPlacement()` through the existing canonical resolver surface;
  - reuses trusted Workspace boundary validation;
  - emits practical review when project-only placement has no trusted active Workspace;
  - does not mutate packages.
- `scripts/capability-resolver-cli.mjs`
  - adds read-only `plan-placement` operation;
  - does not add provider/path selection to member input.
- `scripts/test-capability-placement.mjs`
  - adds focused placement, review, identity and promotion-boundary acceptance coverage.
- `.github/workflows/capability-placement.yml`
  - validates syntax, placement semantics and existing resolver regression.
- `system/architecture/capability-resolution.md`
  - documents the practical placement contract and the managed Skills boundary.

Implementation commits leading to the exact final OS ref:

- `aca1c7d09a7a1597834b8ba0308c0937a454aa9c` - placement planner;
- `a3c00c07afdf0b5397f8988b430149e8858fa7ce` - resolver surface;
- `8693108ad5145b43f23a6916b53f79fdedea792a` - CLI operation;
- `9d8dd74c4ba8d420ab0c9e3423b949240f46a9b3` - focused tests;
- `8ac2c825ce6cf7e86a57226202b761713a0c4d18` - CI workflow;
- `01571824d18421ea71251556b47c3308bfef4446` - architecture documentation/final exact ref.

## Identity compatibility

No existing provider-qualified identity form changed:

```text
os:<name>
aiverse-skills:<name>
local:<name>
workspace:<workspace-id>:<name>
```

Provider/scope remains part of qualified capability identity.

When an existing Workspace capability is planned for broader personal reuse, the planner does **not** claim the qualified identity survives. Instead it reports that a separate promotion/migration is required and records these required properties for that later flow:

- `qualified_identity_preserved: false`;
- provenance must survive;
- history must survive;
- durable references require admitted repair;
- apply is not supported by Slice 3.3.

That deliberately preserves the Slice 3.4 boundary rather than smuggling a migration into placement planning.

## Member-language boundary

Focused tests verify member-facing placement messages do not expose:

- `workspace:` scope IDs;
- `aiverse-skills` provider IDs;
- filesystem paths.

A project-only request without a trusted active Workspace returns practical review wording asking the member to open or choose the project.

The machine result may contain canonical provider/qualified identity fields for trusted internal orchestration; the member does not choose them.

## Managed Skills alignment

No AI-Verse-Skills source change was required.

At current Skills ref `afde5c06307fba7d074de2929c2eb6c3dc6bdab8`, the managed provider already owns:

- immutable generations;
- the one atomic active generation pointer;
- exact generation pinning;
- provider-v1 manifest/index material;
- immutable update;
- pointer-only rollback;
- uninstall semantics that retain pinned generations;
- recovery after uninstall.

User-owned local and Workspace packages remain outside managed distribution ownership.

OS therefore consumes Skills generation evidence but does not write, publish or lifecycle-manage the distribution provider.

## Exact validation

### OS placement contract

Exact OS SHA:

`01571824d18421ea71251556b47c3308bfef4446`

`Capability Placement Contract` run `38291968753`: **SUCCESS**.

Passed:

- placement/resolver/CLI syntax checks;
- practical placement acceptance tests;
- existing scoped discovery and managed-generation resolver regression.

### OS repository integration

`Repository QC` run `38291968646`: **SUCCESS**.

All three jobs passed:

- `qc`;
- `adapter-integration`;
- `skills-provider-integration`.

The Skills-provider integration installed a real immutable Provider-v1 generation outside OS and successfully discovered/selected it through the OS resolver.

### Skills owner lifecycle

Exact Skills SHA:

`afde5c06307fba7d074de2929c2eb6c3dc6bdab8`

`Full E2E Install` run `38246389751`: **SUCCESS**.

Passed owner checks include:

- registry and generation lifecycle validation;
- full pinned upstream install;
- capability provider v1 output validation;
- integrity doctor and capability count;
- execution generation pinning;
- immutable update;
- pointer-only rollback;
- uninstall without deleting the pinned generation;
- recovery after uninstall.

## Acceptance mapping

- **OS owns provider scope/placement semantics:** PASS. The new planner is implemented in AI-Verse-OS and composes existing provider identities.
- **Skills continues owning managed provider package identity/lifecycle:** PASS. No Skills code changed; exact-ref Skills lifecycle E2E remains green and OS only consumes the active immutable provider.
- **current provider-qualified identity forms remain compatible unless explicitly versioned/amended:** PASS. All four existing forms are unchanged.
- **new reusable capabilities are not forced into a Workspace-private provider when wider user-owned reuse is clearly intended:** PASS. Related-work and all-work intents plan `local:<name>` even when called from a trusted Workspace scope.
- **provenance/history survives promotion according to the canonical identity contract:** PASS FOR THIS SLICE BOUNDARY. Any cross-provider change is explicitly classified as a separate unapplied promotion requiring provenance/history preservation and reference repair; Slice 3.3 does not falsely claim identity continuity. Actual promotion execution remains Slice 3.4.
- **member never chooses storage folders or internal scope IDs:** PASS. Placement uses practical intent; trusted scope is host context, and tests reject internal provider choice as member placement intent.

## Non-goals preserved

Slice 3.3 did not:

- move or copy an existing capability between providers;
- create provider aliases to fake identity continuity;
- write into `aiverse-skills`;
- add another managed generation lifecycle inside OS;
- publish a user capability into the distribution;
- implement reference repair;
- start Slice 3.4.

## Result

Slice 3.3 satisfies placement and managed-generation alignment by extending the existing OS resolver rather than replacing it and by reusing the already-correct Skills immutable lifecycle rather than duplicating it.

Next execution unit is Slice 3.4, which must separately implement any admitted promotion/re-scoping and reference repair against real current consumers.
