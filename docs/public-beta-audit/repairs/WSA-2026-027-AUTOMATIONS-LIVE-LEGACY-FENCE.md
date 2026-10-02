# WSA-2026-027 Closure - Automations Live Legacy Authority Fence

**Finding:** `WSA-2026-027`  
**Severity / confidence:** HIGH / PROVEN  
**Owner:** `AI-Verse-Automations`  
**Repair wave:** R2.4  
**Closure date:** 2026-10-02  
**State:** **CLOSED**

## 1. Finding

Automations correctly detected legacy OS automation definitions during setup, but the protection was snapshot-based.

After a successful migration-free setup, a legacy definition could appear and create a recognized authority conflict while:

- status still reported `ready`;
- doctor detected the conflict but reported the descriptor's stale ready state;
- scheduler tick still claimed and advanced Automations-owned work;
- already-claimed work could still reach downstream delivery.

Canonical contradiction: `C-A1.9-002`.

Required closure evidence:

- live legacy-authority detection must be part of readiness and execution;
- status and doctor must agree;
- scheduler tick and delivery must fail closed on post-setup conflict;
- the handoff/clearing state must be explicit;
- post-setup conflict injection and removal must have permanent regressions.

## 2. Baseline and repair identity

**Pre-repair Automations ref:** `e5ec241f1d86e76b15bab5be81e720a827e4fa09`  
**Open Automations PRs before repair:** 0

**Repair branch:** `repair/wsa-2026-027-live-legacy-fence`  
**Repair PR:** `AI-Verse-Automations#5`  
**Final tested PR head:** `d9b2d9bbbfdf0175dae75b70422d20f335d61c3b`  
**Merged Automations ref:** `017eaf3e74d604208c606cc08f4137006f723625`  
**Tested/merged product tree:** `47193905f91583ed82aa197062d724e2ed515fd5`

The exact tested PR head and merged `main` commit have the same product tree.

Open Automations PRs after merge: **0**.

## 3. Final implementation contract

### 3.1 One live migration-authority reader owns the conflict truth

A shared `migration_authority()` reader now combines:

- configured migration-required state;
- configured migration source paths;
- currently discovered legacy definition paths.

It returns one required/configured/discovered/source view consumed by lifecycle and scheduler code.

Post-setup file discovery is therefore operational authority, not doctor-only metadata.

### 3.2 Status changes immediately on post-setup conflict

`descriptor()` now consumes the live reader.

A component that was ready becomes `migration-required` as soon as a legacy definition is discovered under the configured OS root.

The status response exposes both configured and discovered migration sources.

### 3.3 Doctor and status use the same authority snapshot

Doctor obtains one descriptor snapshot and uses that same migration source view for the legacy-definition-handoff check and returned lifecycle state.

Under a stable filesystem snapshot, doctor can no longer report a failed legacy-handoff check alongside a ready lifecycle state.

### 3.4 Enablement cannot bypass a newly discovered conflict

`set_enabled(..., True)` now checks the same combined live authority.

It refuses enablement when either:

- configured migration state remains unresolved; or
- a post-setup legacy definition currently exists.

### 3.5 Scheduler tick does not claim or advance work during conflict

`tick()` and the internal due-claim boundary both recheck live migration authority.

When a conflict exists:

- no due run is claimed;
- no retry is executed;
- no due trigger is advanced/completed;
- no downstream delivery occurs.

Removing a purely post-setup discovered conflict restores dynamic readiness because no configured handoff state was created.

### 3.6 Manual and event ingress fail before run creation

Manual execution and normalized event/webhook ingress check live migration authority before opening a new run.

A live conflict therefore cannot create a new manual/event run or replay receipt through these ingress paths.

### 3.7 Already-claimed work becomes blocked, not destroyed

A run claimed before the conflict appeared is rechecked at `execute_run()`.

If the conflict now exists, the run becomes:

- `status=blocked`;
- `last_error_code=LEGACY_AUTHORITY_CONFLICT`.

No permission call or delivery is made from that path.

Using `blocked` preserves the occurrence for explicit recovery after the authority conflict is cleared.

The permanent regression removes the legacy source, invokes explicit retry, and proves the same blocked run succeeds.

### 3.8 Authority is re-read at the final delivery edge

The repair performs another current config and migration-authority read after OS permission succeeds and immediately before downstream delivery state/effect.

The final-edge regression injects a legacy definition inside the OS permission callback.

Result:

- permission returns allow;
- the newly appearing legacy authority is detected at the final recheck;
- the run becomes blocked;
- downstream request count remains zero.

This closes the important claim/authorization-to-delivery window without changing WSA-2026-028 attachment semantics.

### 3.9 Handoff clearing semantics remain explicit

There are two distinct cases.

**Post-setup discovered conflict:** the current filesystem conflict is the authority fence. Removing that newly discovered source restores dynamic readiness because no configured migration handoff was recorded.

**Setup-time configured migration:** the existing setup contract remains authoritative. Removing the source alone does not erase configured migration state. Re-running the explicit setup/handoff path is required to clear the stored migration-required state and establish ready authority.

The pre-existing setup regression continues to prove that explicit path.

## 4. Permanent regressions

A dedicated `tests/test_live_legacy_fence.py` suite proves:

1. a post-setup legacy definition changes status from ready to migration-required;
2. the discovered source appears in lifecycle truth;
3. doctor returns migration-required and failed handoff truth from the same snapshot;
4. enable is refused while the discovered conflict exists;
5. removing the post-setup source restores dynamic ready state;
6. scheduler tick does not claim a due run during conflict;
7. scheduler tick does not advance the due trigger during conflict;
8. removing the conflict allows the same due occurrence to execute;
9. a run claimed before conflict becomes blocked with LEGACY_AUTHORITY_CONFLICT;
10. blocked run recovery succeeds after conflict removal;
11. a conflict injected during OS permission is caught at the final delivery edge;
12. the final-edge race produces zero downstream requests;
13. manual run ingress is rejected before run creation;
14. event ingress is rejected before run creation.

The existing setup-time migration regression remains green and proves configured migration state is cleared by the explicit setup/handoff path.

## 5. Validation evidence

### Final PR-head acceptance

Final PR-head workflow:

`37048094225`

On exact final head `d9b2d9bbbfdf0175dae75b70422d20f335d61c3b`:

- Ubuntu Python 3.11: **PASS**
- Ubuntu Python 3.12: **PASS**
- Ubuntu Python 3.13: **PASS**
- macOS Python 3.11: **PASS**
- macOS Python 3.12: **PASS**
- macOS Python 3.13: **PASS**
- Windows Python 3.11: **PASS**
- Windows Python 3.12: **PASS**
- Windows Python 3.13: **PASS**

Representative exact-head suite:

- tests run: **46**
- passed: **46**
- failed: **0**
- skipped: **0**

### Intermediate refinement note

An earlier accepted-shape head used `canceled` for a claimed run fenced by a newly appearing legacy conflict.

The repair was deliberately refined so the run becomes `blocked`, preserving it for explicit recovery after handoff.

Intermediate workflow `37048079389` ran after production status had changed to `blocked` but before the corresponding two test assertions were updated. Its failures were exactly those stale `canceled` assertions.

The final accepted head `d9b2d9bbbfdf0175dae75b70422d20f335d61c3b` includes the matching blocked/recovery regressions and is green across all nine jobs.

### Post-merge acceptance

Merged-main workflow:

`37048371219`

On merged Automations `main` ref `017eaf3e74d604208c606cc08f4137006f723625`:

- all 9 Ubuntu/macOS/Windows Python 3.11/3.12/3.13 jobs: **PASS**
- representative suite: **46 / 46 passed**

The tested PR-head tree and merged-main tree are identical:

`47193905f91583ed82aa197062d724e2ed515fd5`

## 6. Finding-specific recheck

### C-A1.9-002

**RESOLVED for WSA-2026-027.**

Post-setup legacy definition appearance is now an operational migration-required fence.

### Status and doctor

**PASS.**

Both consume the same live migration-authority snapshot and report migration-required while the conflict exists.

### Scheduler tick

**PASS.**

No claim or trigger advancement occurs while the conflict is present.

### Claimed-run execution

**PASS.**

A run claimed before the conflict becomes blocked before permission/delivery and remains recoverable.

### Final delivery edge

**PASS.**

A conflict injected during the OS permission step is detected before downstream delivery and produces zero external requests.

### Conflict removal / handoff

**PASS.**

A purely discovered post-setup conflict clears when the source is removed. A configured setup-time migration remains latched until the explicit setup/handoff path clears it.

### A2.3 lifecycle/readiness graph

**RESOLVED for the WSA-2026-027 Automations legacy-authority branch only.**

Live authority conflict now controls ready/migration-required operational state.

### A3.2 migration/adoption

**RESOLVED for the live legacy-authority handoff fence under this finding.**

This does not close unrelated migration atomicity findings.

### A3.7 automation replay

The complete event/replay owner suite remains green with the new ingress fence.

### A3.10 lifecycle/recovery

Blocked-run recovery after conflict removal is explicitly proven and the complete owner recovery suite remains green.

## 7. Adjacent finding remains open

This closure is limited to `WSA-2026-027`.

The following remains **OPEN** and was intentionally not repaired here:

- `WSA-2026-028` - component lifecycle and attached OS registry lifecycle diverge.

The whole-system verdict remains **NO-GO**.

Dashboard MC1.4 and owner dogfood remain paused.

## 8. Closure verdict

Required WSA-2026-027 behavior is present on merged Automations `main`:

- post-setup legacy definitions are live lifecycle authority;
- status and doctor agree on migration-required truth;
- enablement cannot bypass a live conflict;
- scheduler tick does not claim or advance work during conflict;
- manual/event ingress cannot create new runs during conflict;
- claimed work is blocked with zero delivery and remains recoverable;
- live authority is rechecked immediately before downstream delivery;
- conflict injection during permission still yields zero downstream requests;
- clearing semantics distinguish dynamic discovery from configured handoff state;
- all 9 exact-head CI jobs pass;
- all 9 merged-main CI jobs pass;
- representative suite is 46 / 46;
- tested and merged product trees are identical;
- open Automations PRs are zero.

**WSA-2026-027: CLOSED.**
