# Personal tool dependency placement — implementation plan

Date: 23 October 2026. Status: COMPLETE. Progress: 3/3 slices (100%).
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

### 1 — Contract and safe tool owner (complete)
Start: OS main50f9f67; installed shared Skills Core v4. Tasks: inspect existing caller/owners; implement helper and contract; exercise meaningful success/refusal/preservation cases. Acceptance: R01–R04 locally verified, no new dependencies. Recovery: discard source branch; no member mutation.

### 2 — Owner acceptance and official delivery (complete)
Depends on slice1. Tasks derived at start: owner review/CI, accepted descriptor, System State source update, Distribution exact candidate and platform qualification/promotion. Acceptance: R05 release published with no weakening of existing lifecycle gates. Recovery: retain prior admitted Core; no direct installed source patch.

### 3 — Personal rollout and closeout (complete)
Depends on slice2. Canonical update, selected personal-state fingerprints, real helper preview/check without external package execution, doctor/version, final plan evidence. Acceptance: installed accepted release, preserved member files, honest enforcement limits. Recovery: canonical lifecycle recovery only; no migration of old tools.

Execution pointer: NONE. All three slices are complete. New tasks may refine implementation but not weaken requirements or enlarge scope.

## Slice1 evidence

OS PR106, exact source7bb6226783396ef7a00b325306da26b0f4b17474. One dependency-free production helper;34 local behavioral checks pass and architecture check passes with zero warnings. Native placement checks pass on Linux/macOS/Windows (exact run link retained in PR106). Core manifests remain unchanged; personal apps are gitignored. Official plan accepted through System PR265. All41 source checks passed; OS PR106/107 accepted the exact source as0.3.9. Distribution now publishes it through the qualified release below.

## Slice2 completion — official delivery

Completed tasks: exact owner acceptance and descriptor; authenticated System source State; immutable candidate admission; real three-platform fresh/populated/optional qualification; preservation/qualification receipts; normal synchronized promotion; exact final-head CI; live-default verification.

OS source7bb6226783396ef7a00b325306da26b0f4b17474 is accepted as0.3.9. System PR265 adopted this plan; PR266 merged source snapshot343a13b1d8fade4553878a4deefb7c9da6f44cfe. All147 System tests pass. Distribution definitiond9e7c85f397a8515b9aaec7c45001ede99d01e47 is bound to exact authenticated owner evidence. The three new-release jobs in40014222597 and allsix unit jobs in40014222655 passed on tested head4346b8aa494284bc6b8a318d4b955f7b1cbc495b. The superseded aggregate40014222597 was stopped only after those three required jobs passed, to unblock final publication; no whole-workflow success is claimed for that superseded run.

Canonical whole-product qualification and normal synchronized promotion passed with zero debt. Distribution PR76 merged at a3db40f5418eef5c8b8ca030d251c66f623dfe1a after all65 checks passed on exact publication headab59ac4240cdd16ab7f8a3e5037cf696f7273da1. Final Core workflow40017661046 succeeded, including allhistorical and new-release platform jobs. Live default is `core-tool-placement-candidate-2026-10-23`; other component pins and dependency locks are unchanged.

Adaptive findings: the populated fixture now seeds Skills in the prior configured personal library, using its historical fallback only when no binding exists. Historical version identity remains exact; the current version label is checked against the current accepted descriptor. These are qualification-fixture corrections, not member data moves or relaxed preservation. Final network checks bind the exact qualified System/owner heads; no harness safety logic was weakened.

## Slice3 completion — actual member rollout

Completed tasks: ready preflight;143-file selected baseline; official repeated bootstrap into the receipt-owned tool refresh and canonical default updater; health/version; installed helper and scoped preview; skill routing/privacy and native optional-package preservation; durable private completion evidence.

The actual update succeeded and changed only OS. Installed/latest version is0.3.9, status ready and doctor passes. All143 selected personal/configuration/tool files are byte-identical after update. All66 shared/scoped Skills routing checks pass. Existing private tool package check passes; new workspace tool creation preview makes no changes. Architecture check passes with zero warnings. The unchanged optional Codex package reports READY with approval_required=false and actual execution/review observed. No new hook behavior or trust action was introduced.

Private member evidence remains in its development workspace and runtime reports; no credentials, private workspace names, tool contents or user paths are published here. No SDK task, caption retrieval, advertising action or generation was executed on the real member installation. New-member and populated-member dependency installs were exercised in isolated qualification fixtures.

## Closure and remaining scope

R01–R05 accepted.3/3 slices complete. Execution pointer:NONE. This is enforcement for supported AI-Verse tool creation/install paths, not arbitrary process/filesystem isolation. Existing tools are not automatically migrated. Skills repository content curation remains a separate effort. Postmerge main workflow40020025558 is additional live validation; its current status must be read from GitHub rather than inferred from this closeout.
