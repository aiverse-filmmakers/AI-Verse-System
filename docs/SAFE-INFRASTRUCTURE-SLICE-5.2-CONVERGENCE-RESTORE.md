# Safe Infrastructure Slice 5.2 - Real Convergence and Restore Qualification

**Status:** COMPLETE  
**Canonical slice:** 5.2  
**Outcome:** a real admitted older Core installation was updated to the current admitted release, compared with a fresh current installation, exercised through the exact frozen OS owner capability-promotion contract, and restored to its retained pre-update Last-Known-Good point without inventing unsupported Workspace relocation or broadening release authority.

## Refreshed starting refs

Frozen before any Slice 5.2 implementation write:

- `aiverse-filmmakers/AI-Verse-System@69ea1553f8545350a0ab54211ed22e1ba8844b61`
- `aiverse-filmmakers/ai-verse-distribution@1f4559d88966e2a2ff26ca563d7a035ebc69a90b`
- `aiverse-filmmakers/AI-Verse-OS@470ad89e6b96d898161dee36d4e4fa8064dd6a8d`
- `aiverse-filmmakers/AI-Verse-Skills@d4a02888ba8d83c4a15ce1b538ffdafaaf83bee1`

The System and Distribution repositories advanced concurrently through the separate Distribution-system propagation program while Slice 5.2 was running. Final qualification therefore used the repaired concurrent Distribution main and final System closure preserves the current System main rather than rewinding unrelated work.

## Final adaptive task list

- [x] **5.2-T1** Freeze the real historical/current fixture set and exact owner contracts: real admitted Core transition, historical nested Workspace drift, current direct Workspace contract, Workspace-to-personal capability promotion, LKG/restore coverage and supported runtime adapter commands.
- [x] **5.2-T2** Execute a realistic older populated Core installation through the real admitted `core-stable-2026-10-10` -> `core-first-run-rc1-2026-10-12` transition and prove member-owned state survives while the authoritative receipt/status reaches the admitted target.
- [x] **5.2-T3** Prove Workspace convergence truth without inventing migration: current direct `workspaces/<id>` layout remains canonical while historical nested/domain-first layout stays `BLOCKED/REVIEW`, non-relocating and read-only because no Workspace relocation recipe is admitted.
- [x] **5.2-T4** Exercise the real OS Workspace-to-personal capability promotion through the exact frozen owner source against the real upgraded installation, preserving provenance/history/custom files, recording intentional identity change, compatibility repair, cross-Workspace resolution, stale-plan refusal evidence and idempotent replay.
- [x] **5.2-T5** Compose real software update plus owner mutation with Last-Known-Good and explicit restore: preserve the pre-action LKG, keep restore preview read-only, restore exactly declared covered files, retain excluded credential-shaped state, retain the recovery target and finish healthy.
- [x] **5.2-T6** Prove fresh-versus-upgraded convergence and runtime convergence: independently install the same current Core release, compare exact package-owned component contracts, and rerun lifecycle entrypoint and adapter convergence across the supported matrix.
- [x] **5.2-T7** Qualify exact owner-native evidence, exact Distribution PR head and merged main, record the real executable result, close Slice 5.2 only after all required gates are green, then stop before Slice 5.3.

## Implementation result

Distribution PR #35 is qualification-only. It added exactly three permanent files:

- `.github/workflows/safe-infrastructure-convergence.yml`;
- `scripts/safe-infra-52-real-convergence.py`;
- `tests/test_safe_infrastructure_convergence_contract.py`.

No Distribution product/runtime code changed. No OS or Skills owner implementation changed. No production structural migration or Workspace relocation recipe was invented.

### Real software convergence

The executable fixture uses the real admitted transition:

- source release: `core-stable-2026-10-10`;
- target release: `core-first-run-rc1-2026-10-12`;
- changed component: `ai-verse-os` only.

The fixture installs the real source release, adds realistic member-owned Workspace/local state, runs the canonical update plan and update, and verifies:

- the update result identifies the exact target;
- the authoritative Distribution receipt and status reach the target;
- a pre-action LKG is retained;
- final update health passes;
- member-owned state is preserved.

It independently installs a fresh copy of the exact current release and verifies that the fresh and upgraded installations have identical package-owned component repository/revision contracts. Both OS checkouts resolve to the accepted current OS revision.

### Workspace convergence truth

The frozen OS owner contract retains the real historical nested fixture `workspaces/YouTube/channel-a/WORKSPACE.yaml`. It remains review-only with findings including invalid slot/nested-manifest state and is not automatically relocated.

The current accepted OS descriptor does not publish `migration.infrastructure` and does not require an explicit structural migration. Slice 5.2 therefore proves safe non-mutation for that historical layout rather than manufacturing a relocation path.

### Owner capability promotion and identity

The accepted Core release currently ships OS revision:

`64f7325444d18f94c9d4755d32eb89f3468bda6b`

The frozen current owner-source contract is:

`470ad89e6b96d898161dee36d4e4fa8064dd6a8d`

That later owner-source revision still publishes an accepted descriptor binding the shipped OS revision `64f7325444d18f94c9d4755d32eb89f3468bda6b`. The live fixture therefore invokes the exact frozen owner-source capability CLI against the real upgraded shipped installation. This qualifies current owner-defined convergence behavior without falsely claiming the later owner-source command surface is already part of the shipped Core checkout.

The executable promotion proves:

- explicit member intent such as `use this for all YouTube work` produces a personal/local placement plan;
- `workspace:alpha:transcript-book` becomes `local:transcript-book`;
- qualified identity is intentionally **not** preserved;
- provenance/history and custom member files survive;
- compatibility repair is active;
- another Workspace resolves the historical qualified ID to the promoted target;
- replay returns already-promoted/no-effect behavior;
- owner-native tests retain stale-plan refusal evidence.

### Recovery and restore

The real update captures the pre-action LKG before mutation. After update and owner promotion, the fixture creates additional realistic covered changes and modifies an excluded `.env` secret-shaped file.

The fixture proves:

- restore preview is truthful and read-only;
- the retained LKG pointer does not change during preview;
- explicit restore returns the Distribution receipt and software to the stable source release;
- covered project and personal-skill files reproduce the retained pre-action point;
- post-LKG covered files are removed;
- the pre-LKG Workspace capability returns;
- `.env` remains at its current value because credential-shaped material is explicitly excluded;
- the retained LKG survives restore;
- final doctor passes.

Recovery coverage is file-level. A post-LKG capability directory may remain empty after every covered file/symlink is removed; empty directory identity is not represented in the LKG manifest and Slice 5.2 does not claim otherwise.

### Runtime convergence

The dedicated convergence gate reruns the canonical lifecycle entrypoint and adapter tests on Ubuntu/macOS/Windows with Python 3.11/3.12. Claude/Codex/Gateway-compatible routing therefore continues to converge on the same lifecycle surfaces while normal member output remains separate from internal release IDs and paths.

## Qualification discoveries

The executable fixture intentionally exposed several assumptions before final qualification. None required a product-law amendment:

1. The first fixture expected a top-level `release_set_id` in update output. The canonical updater returns `to`; authoritative installed-release truth is the Distribution receipt/status. The fixture was corrected only.
2. A concurrent propagation change temporarily caused two candidate-admission tests to fail on the PR merge ref. That separately owned program repaired its own main. Final Slice 5.2 qualification used the repaired base and its candidate-admission gate passed.
3. The released Core OS checkout predates the later owner-source placement/promotion command surface. The fixture was corrected to invoke the exact frozen owner source against the real upgraded installation while verifying its accepted descriptor binds the shipped OS revision.
4. The first restore assertion treated an empty post-LKG directory as covered state. The recovery contract indexes captured files, not empty directory identity. The final assertion requires zero residual promoted files/symlinks and does not broaden restore ownership.
5. A temporary Actions-authored patch commit produced `action_required` runs before jobs were created. A maintainer-authored no-semantic-change retrigger produced the exact final qualified head. This was CI authorization state, not a code/test failure.

## Exact evidence

### System start record

- System PR #211 exact head `eee514a6ba843ef6dea20ebfb371bd955c882817`;
- Contract Validation `38641741000`: **SUCCESS**, Python 3.11 and 3.13;
- merged start record `d7a7e5b38712a32c417d49b47c3d39b7015b92b9`.

### Distribution PR head

Final exact qualified head:

`8ca22a1fbacf17f067af2e2e83418c4810ccc70d`

PR-head qualification:

- Distribution CI `38644724266`: **SUCCESS**, all six Ubuntu/macOS/Windows x Python 3.11/3.12 jobs;
- Safe Infrastructure Regression `38644724292`: **SUCCESS**, all six jobs;
- Safe Infrastructure Convergence `38644724402`: **SUCCESS**, all six jobs;
- Lifecycle Receipt Concurrency `38644724547`: **SUCCESS**, Ubuntu/macOS/Windows.

The Linux/Python 3.11 convergence job `116128813327` executed the real install/update/fresh-compare/promotion/restore path and emitted successful evidence for member-state preservation, fresh-vs-upgraded component equality, compatibility mapping, cross-Workspace consumption, idempotent replay, LKG retention, read-only preview, covered-state restore, credential exclusion, retained recovery point and final doctor health.

### Distribution merged main

PR #35 merged as:

`004112410ec4608e4b9a758b651c4d6bba3b7f8c`

Merged-main qualification:

- Distribution CI `38645538247`: **SUCCESS**, all six jobs;
- Safe Infrastructure Regression `38645538145`: **SUCCESS**, all six jobs;
- Safe Infrastructure Convergence `38645538333`: **SUCCESS**, all six jobs.

Lifecycle Receipt Concurrency does not trigger on this main push; the exact qualified PR-head run `38644724547` remains the applicable lifecycle-concurrency evidence.

## Acceptance criteria

- real admitted older Core transition executes with realistic member state and preserves it: **PASS**;
- fresh-current and upgraded historical installations converge on identical package-owned component contracts: **PASS**;
- historical unsupported Workspace relocation remains review-only and non-mutating: **PASS**;
- no fake production structural recipe or broader transition authority was introduced: **PASS**;
- owner-defined capability promotion requires explicit intent/apply and records intentional qualified-identity change: **PASS**;
- provenance/history/custom capability files survive promotion: **PASS**;
- compatibility mapping and cross-Workspace consumption work: **PASS**;
- stale-plan refusal remains owner-native evidence and replay is idempotent: **PASS**;
- pre-action LKG is retained before update: **PASS**;
- restore preview is read-only: **PASS**;
- restore reproduces exactly declared file-level covered state: **PASS**;
- excluded credential-shaped `.env` state is not falsely rewound: **PASS**;
- retained LKG survives restore: **PASS**;
- final doctor aggregation is healthy: **PASS**;
- supported runtime lifecycle routing remains convergent: **PASS**;
- exact PR-head and merged-main CI/Regression/Convergence gates are green: **PASS**.

No protected-law amendment and no product-code change was required.

## Completion report

```text
Completed: Slice 5.2 - Run real old-install -> current-architecture convergence and restore qualification
Tasks: 7/7
Overall: 17/18 slices (94.4%)
Phase: Phase 5 - Prove safety, convergence, restore and closeout
Phase progress: 2/3
Until program complete: 1 slice
Next: Slice 5.3 - Canonical closeout and handoff
Blockers/drift/amendments: no Safe Infrastructure blocker or protected-law amendment; concurrent propagation work was preserved and final qualification used its repaired Distribution base.
```

## NEXT

**STOP after Slice 5.2 under the current one-at-a-time execution rule.**

Next execution unit is Slice 5.3 - Canonical closeout and handoff. Derive its adaptive task list only after fresh System/Distribution/owner refs are fetched. No Slice 5.3 implementation was started here.
