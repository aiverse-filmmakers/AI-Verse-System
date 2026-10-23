# Personal tool dependency placement — implementation plan

Date: 23 October 2026. Status: implementing. Progress: 0/3 slices.
Method: canonical Adaptive Implementation Planning Skill, standard depth with explicit release/preservation evidence. Owner: OS; System owns plan, Distribution owns qualified member delivery.

## Product brief

Members create scripts and tools inside an installed OS. Previously an assistant added a tool's SDK and runner to the Core root package.json, so a later canonical update correctly refused the modified source. The local incident was repaired with exact backups and user approval. This program prevents that placement mistake in supported tool creation/install workflows for all members.

Journey: resolve scope → create a private tool package beneath apps/<name> or workspaces/<id>/tools/<name> → install dependencies using a checked package root → keep Core manifests and user state unchanged → receive the same helper through canonical Core update.

Non-goals: Skills repository curation, automatic migration/deletion, new hook trust, process/filesystem sandboxing, blocking arbitrary shell/editor writes, intercepting every package manager, or changing Core maintenance/release authority. Package installation can execute third-party code; placement validation is not security isolation.

## Laws

Preserve personal state and existing tools. No root manifest adoption/overwrite, new credentials, permission expansion, or alternate updater. One OS helper; no daemon, registry, database or new library dependency. Explicit Core source development remains legitimate and separate from personal tooling.

## Requirements

| ID | Success / refusal / unchanged behavior | Evidence |
|---|---|---|
| R01 | Tool creation chooses private app or scoped workspace tool root; refuses invalid scope/name, symlink escape, existing destination | Helper behavior and focused regression |
| R02 | Node installs use explicit tool prefix and ignore lifecycle scripts; Python installs use a private venv, never Core environment; package arguments cannot become flags/paths | Dispatch arguments and refusal regressions; isolated local package creation |
| R03 | All runtime contract peers route personal tool creation/install through the same helper; Core software development and canonical update remain intact | AGENTS/CLAUDE routing, architecture/owner CI |
| R04 | Root package/locks remain byte-identical after successful and rejected operations; originals are never migrated | Preservation fixtures and actual member smoke |
| R05 | Accepted OS source is qualified and delivered through Distribution, with installed health and preserved member state | Owner PR checks, exact release qualification, canonical member update |

## Current flow / design

REUSE apps/, workspaces/, current-context resolver, Node standard library, OS contracts, existing lifecycle/release controls. EXTEND AGENTS and architecture guidance. CREATE one deterministic personal-tool helper and focused tests. No generic action-permission schema change: its existing action classes do not describe filesystem targets and widening it would affect unrelated owners without ensuring shell interception.

Helper exposes init, check, install. Scope is explicit. Init is preview unless --apply; no overwrite. Install validates existing tool root/manifest and receives registry package specs rather than arbitrary shell text. npm uses explicit prefix and scripts disabled. Python uses a tool-owned .venv and pip isolated mode. Errors preserve originals; existing packages are checked without automatic conversion. A hand-created tool can be checked if it has a normal self-contained manifest. The helper does not execute the tool itself or move credentials.

Risks: reject symlinks on all controlled ancestors; validate workspace through existing resolver; reject root/traversal/flag specs; concurrent create uses mkdir exclusive; failed install may leave tool-local package-manager state and reports failure (no automatic destructive cleanup). Third-party executable dependencies are outside the placement boundary. Platform behavior must pass Linux/macOS/Windows owner checks. No performance target needed for bounded local checks.

## Slices

### 1 — Contract and safe tool owner (active)
Start: OS main50f9f67; installed shared Skills Core v4. Tasks: inspect existing caller/owners; implement helper and contract; exercise meaningful success/refusal/preservation cases. Acceptance: R01–R04 locally verified, no new dependencies. Recovery: discard source branch; no member mutation.

### 2 — Owner acceptance and official delivery
Depends on slice1. Tasks derived at start: owner review/CI, accepted descriptor, System State source update, Distribution exact candidate and platform qualification/promotion. Acceptance: R05 release published with no weakening of existing lifecycle gates. Recovery: retain prior admitted Core; no direct installed source patch.

### 3 — Personal rollout and closeout
Depends on slice2. Canonical update, selected personal-state fingerprints, real helper preview/check without external package execution, doctor/version, final plan evidence. Acceptance: installed accepted release, preserved member files, honest enforcement limits. Recovery: canonical lifecycle recovery only; no migration of old tools.

Execution pointer: slice1. New tasks may refine implementation but not weaken requirements or enlarge scope.
