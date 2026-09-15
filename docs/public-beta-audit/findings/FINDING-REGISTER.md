# Independent Whole-System Audit Finding Register

**Program:** Independent Whole-System Public-Beta Audit  
**Register established by:** A0.3 Evidence/finding ledger  
**Established:** 2026-09-15  
**System task baseline:** `eba8f2e7a7005a4e597bbb75fef7913927e2f738`  
**Frozen product snapshot:** `../snapshots/A0-SNAPSHOT.md`  
**Protocol authority:** `../EVIDENCE-FINDING-PROTOCOL.md`  
**Status:** CANONICAL FINDING / CONTRADICTION / EVIDENCE REGISTER

## 1. Register law

This file is the canonical index for stable audit findings and the cross-task navigation index for contradiction and evidence IDs.

Rules:

1. Finding IDs use `WSA-2026-NNN`.
2. Published finding IDs are never renumbered or reused.
3. New findings take the next unused global number.
4. Contradiction and evidence IDs remain task-local exactly as published in their source packets.
5. A contradiction may exist without a finding when it is historical, explicitly superseded, intentional compatibility, or otherwise immaterial.
6. Evidence IDs are navigation labels only. Exact repository, path, SHA, run/job or source identity remains authoritative.
7. Findings are not repaired during A0-A6. State changes during those phases may record new evidence, duplication or invalidation, but product repair waits for the canonical repair program unless emergency containment is required.
8. The register summarizes source packets. It must not silently weaken, strengthen or rewrite their evidence.
9. If source evidence drifts, preserve the original record and append the recheck result rather than mutating history.
10. Dashboard MC1.4 remains paused regardless of the absence of BLOCKER/HIGH findings because the whole-system audit itself is incomplete.

**Next unused finding ID:** `WSA-2026-024`.

## 2. Allowed classifications

### Severity

- BLOCKER
- HIGH
- MEDIUM
- LOW
- INFO

### Confidence

- PROVEN
- STRONG
- POSSIBLE
- UNVERIFIED

### State

- OPEN
- DUPLICATE
- DEFERRED
- NOT-A-BUG
- FIXED-PENDING-RECHECK
- CLOSED

### Claim state

- VERIFIED
- CONTRADICTED
- PARTIAL
- PLAN-ONLY
- HISTORICAL
- UNVERIFIED
- NOT-APPLICABLE

## 3. Current finding summary

| Finding | Severity | Confidence | State | Root area | Affected repos | Opened by |
|---|---|---|---|---|---|---|
| `WSA-2026-001` | LOW | PROVEN | OPEN | release metadata / documentation drift | `ai-verse-distribution`, `AI-Verse-System` | A0.2 |
| `WSA-2026-002` | LOW | PROVEN | OPEN | System documentation drift | `AI-Verse-System`, `AI-Verse-Connections` | A0.2 |
| `WSA-2026-003` | INFO | PROVEN | OPEN | hosted CI / evidence availability | `AI-Verse-Connections`, `AI-Verse-System` | A0.2 |
| `WSA-2026-004` | LOW | PROVEN | OPEN | audit control-document drift | `AI-Verse-System` | A0.3 |
| `WSA-2026-005` | LOW | PROVEN | OPEN | capability source-of-truth / contract metadata drift | `AI-Verse-OS` | A1.1 |
| `WSA-2026-006` | BLOCKER | PROVEN | OPEN | destructive lifecycle / filesystem safety | `AI-Verse-Gateway` | A1.2 |
| `WSA-2026-007` | HIGH | PROVEN | OPEN | setup/disable/uninstall/status lifecycle truth | `AI-Verse-Gateway` | A1.2 |
| `WSA-2026-008` | HIGH | PROVEN | OPEN | concurrency / idempotency / session binding / run control | `AI-Verse-Gateway` | A1.2 |
| `WSA-2026-009` | HIGH | PROVEN | OPEN | filesystem containment / scope isolation | `AI-Verse-Brain` | A1.3 |
| `WSA-2026-010` | MEDIUM | PROVEN | OPEN | Goal concurrency / replay safety | `AI-Verse-Brain` | A1.3 |
| `WSA-2026-011` | LOW | PROVEN | OPEN | release/version identity | `AI-Verse-Brain` | A1.3 |
| `WSA-2026-012` | BLOCKER | PROVEN | OPEN | destructive lifecycle / filesystem containment | `AI-Verse-Memory` | A1.4 |
| `WSA-2026-013` | HIGH | PROVEN | OPEN | lifecycle authority / canonical writes | `AI-Verse-Memory` | A1.4 |
| `WSA-2026-014` | HIGH | PROVEN | OPEN | migration / canonical authority transfer | `AI-Verse-Memory` | A1.4 |
| `WSA-2026-015` | LOW | PROVEN | OPEN | release/version/bootstrap reproducibility | `AI-Verse-Memory` | A1.4 |
| `WSA-2026-016` | BLOCKER | PROVEN | OPEN | lifecycle controller containment | `AI-Verse-Skills` | A1.5 |
| `WSA-2026-017` | HIGH | PROVEN | OPEN | lifecycle concurrency / serialization | `AI-Verse-Skills` | A1.5 |
| `WSA-2026-018` | MEDIUM | PROVEN | OPEN | immutable generation retention | `AI-Verse-Skills` | A1.5 |
| `WSA-2026-019` | LOW | PROVEN | OPEN | release/version/bootstrap reproducibility | `AI-Verse-Skills` | A1.5 |
| `WSA-2026-020` | HIGH | PROVEN | OPEN | trusted scope provenance / workspace isolation | `AI-Verse-Data` | A1.6 |
| `WSA-2026-021` | LOW | PROVEN | OPEN | release/version/install reproducibility | `AI-Verse-Data` | A1.6 |
| `WSA-2026-022` | HIGH | PROVEN | OPEN | operator/domain authority binding | `AI-Verse-Multiple-Bots` | A1.7 |
| `WSA-2026-023` | HIGH | PROVEN | OPEN | Worker workspace isolation / canonical coordination authority | `AI-Verse-Multiple-Bots` | A1.7 |

Current counts:

| Dimension | Count |
|---|---:|
| BLOCKER | 3 |
| HIGH | 9 |
| MEDIUM | 2 |
| LOW | 8 |
| INFO | 1 |
| PROVEN | 23 |
| STRONG | 0 |
| POSSIBLE | 0 |
| UNVERIFIED | 0 |
| OPEN | 23 |
| CLOSED | 0 |

These counts do **not** imply public-beta approval. See the canonical execution tracker for current weighted audit progress.

## 4. Detailed finding records

### WSA-2026-001 — Invisible Intelligence candidate acceptance metadata disagrees with current acceptance record

**Severity:** LOW  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A0.2  
**Root area:** release metadata / documentation drift  
**Affected repos:** `ai-verse-distribution`, `AI-Verse-System`  
**Affected seam:** Distribution release metadata -> System release/status authority  
**Affected journeys:** release selection/status inspection; A5 release-evidence revalidation

**Summary:**  
The machine-readable Invisible Intelligence candidate manifest records nested Distribution acceptance as `qualification-pending`, while current System release evidence records the candidate as qualified and merged.

**Expected law:**  
Machine-readable release/candidate acceptance metadata and current canonical release/status evidence should not expose conflicting acceptance states for the same immutable candidate.

**Observed behavior:**  
At Distribution `31888c74235cc262910fb094335fd3a994f0ecf1`, `release-sets/agent-invisible-intelligence-rc1-2026-09-14.json` has:
- top-level `status: released`;
- `classification: explicit-install-qualification-candidate`;
- nested `distribution_acceptance.status: qualification-pending`.

At frozen System baseline `a10bf0e8ea230a6460adf45354f314bba68bb614`, `docs/PUBLIC-BETA-TRACKER.md` records final qualification and Distribution PR #7 merged at `a215c8777da55b299247ec9e564cca020cfe2020`.

**Contradiction:** `C-A0.2-001`.

**Primary evidence:** `E-A0.2-006`, `E-A0.2-007`, `E-A0.2-012`.

**Impact:**  
Automation or human readers can derive different candidate acceptance state depending on which canonical-looking source they consume.

**Required closure evidence:**  
After audit synthesis authorizes repair, machine-readable candidate acceptance metadata and canonical current release/status evidence must agree, with qualification history preserved rather than rewritten.

---

### WSA-2026-002 — System Connections component spec is stale against live implementation

**Severity:** LOW  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A0.2  
**Root area:** System documentation drift  
**Affected repos:** `AI-Verse-System`, `AI-Verse-Connections`  
**Affected seam:** live component implementation -> System component specification  
**Affected journeys:** operator architecture inspection; Full-profile planning; A1 Connections audit; A5 release evidence

**Summary:**  
The System Connections component specification still describes a pre-implementation research seed, while the frozen live Connections repository is a public-beta implementation candidate.

**Expected law:**  
System component status/specification material may preserve historical evidence, but current-status readers must not be left with a materially false implementation state.

**Observed behavior:**  
System `components/ai-verse-connections/COMPONENT-SPEC.md` anchors revision `76be3558eb6670b21195064b04acdd7d6dd41490` and states implementation is not started.

Frozen Connections main is `baaac641558dbff1c2eabb0b5ec785a633f49a5b`. Its README declares `0.1.0-beta.1` and documents executable install/setup/status/doctor, generic API and MCP paths, credential handles, explicit capability admission/approval and execution.

**Contradiction:** `C-A0.2-002`.

**Primary evidence:** `E-A0.2-002`, `E-A0.2-012`.

**Impact:**  
System-level readers can materially misunderstand current Connections capability and readiness.

**Required closure evidence:**  
After audit synthesis/repair authorization, reconstruct and refresh the System Connections current-state evidence/spec from the exact accepted live revision, retaining prior historical evidence where useful.

---

### WSA-2026-003 — Hosted CI does not execute on private Connections/System repositories

**Severity:** INFO  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A0.2  
**Root area:** hosted CI / evidence availability  
**Affected repos:** `AI-Verse-Connections`, `AI-Verse-System`  
**Affected seam:** repository -> hosted validation infrastructure  
**Affected journeys:** audit acceptance; release verification; contributor verification

**Summary:**  
GitHub Actions runs for both private scoped repositories currently terminate before workflow step execution. The GitHub run conclusion says failure, but job payloads contain `steps: null`.

**Expected law:**  
Audit evidence must distinguish executed test failure from infrastructure inability to start a job.

**Observed behavior:**  
At the frozen A0.2 snapshot:
- Connections run `34775251071`: six matrix jobs, all `steps: null`;
- System run `34999475462`: Python 3.11 and 3.13 jobs, both `steps: null`.

A0.2 checkpoint validation reproduced the same condition on System PR run `35000648591` and post-merge run `35000689297`.

**Contradiction:** none. The issue is evidence availability, not conflicting source claims.

**Primary evidence:** `E-A0.2-004`, `E-A0.2-005`; A0.2 PR/post-merge validation evidence.

**Impact:**  
Hosted CI cannot currently serve as executed current-head validation for these private repositories. Later audit tasks must not call these runs product test failures or green validation.

**Required closure evidence:**  
A required workflow run that actually executes its steps, or a policy-approved exact-input alternate validation route where the relevant audit phase permits it.

---

### WSA-2026-004 — Audit README still tells fresh auditors to start at A0.1

**Severity:** LOW  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A0.3  
**Root area:** audit control-document drift  
**Affected repos:** `AI-Verse-System`  
**Affected seam:** audit entrypoint README -> canonical execution tracker  
**Affected journeys:** new-chat audit continuation; auditor handoff

**Summary:**  
The audit README says the program is only planned and that execution begins at A0.1, while the canonical execution tracker records A0.1 and A0.2 complete and A0.3 as NEXT.

**Expected law:**  
A fresh auditor following the documented entrypoint should be routed to the canonical current task without being told to restart completed work.

**Observed behavior:**  
At System `eba8f2e7a7005a4e597bbb75fef7913927e2f738`:
- `docs/public-beta-audit/README.md` says: current state planned; execution begins at A0.1;
- `docs/public-beta-audit/EXECUTION-TRACKER-2026-09-15.md` records accepted progress 2/100, A0.1 COMPLETE, A0.2 COMPLETE, A0.3 NEXT.

The README itself correctly says the tracker determines the exact next task, but its headline/current-state sentence is stale and contradictory.

**Contradiction:** `C-A0.3-001`.

**Primary evidence:** `E-A0.3-001`, `E-A0.3-005`.

**Impact:**  
A fresh auditor can be confused into restarting completed scope work before reaching the tracker.

**Required closure evidence:**  
After audit synthesis/repair authorization, the audit entrypoint must state that the tracker is authoritative without hardcoding a stale starting task, and a fresh-reader check must confirm it routes to the current NEXT task.

### WSA-2026-005 — OS canonical capability-source metadata is stale against implemented provider architecture

**Severity:** LOW  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A1.1  
**Root area:** capability source-of-truth / contract metadata drift  
**Affected repos:** `AI-Verse-OS`  
**Affected seams:** OS -> Claude/Codex runtime adapters; OS -> external capability providers  
**Affected journeys:** capability authoring/discovery; future provider maintenance; A2 capability seams; A5 documentation/status scan

**Summary:**  
OS machine-readable architecture metadata still names `.claude/skills/` as shared capability methodology truth and the provider-v1 contract README still describes already-implemented discovery/migration behavior as future. Current executable code, architecture, capability registry, synchronizer, tests and exact-head CI establish `system/capabilities/` plus implemented Provider v1 discovery as current truth.

**Expected law:**  
High-authority machine-readable architecture metadata and canonical contract status prose should agree with the implemented canonical capability source and supported provider lifecycle.

**Observed behavior:**  
The deterministic runtime uses `system/capabilities/` correctly and generated peers remain synchronized, so no current execution failure was proven. The stale metadata can still misdirect humans or model-driven maintainers toward a generated adapter or obsolete implementation state.

**Contradictions:** `C-A1.1-001`, `C-A1.1-002`.

**Primary evidence:** `E-A1.1-004`, `E-A1.1-005`, `E-A1.1-014`.

**Impact:**  
Maintenance/source attribution can diverge from the canonical implementation, and future changes can be designed against an obsolete provider-migration state.

**Required closure evidence:**  
After A6 authorizes repair: align `AI-VERSE.yaml` with `system/capabilities/`; update Provider v1 implementation-status/migration prose without weakening the contract; add an architecture/QC invariant preventing recurrence; rerun Repository QC, adapter-sync and provider integration on the repaired exact ref.

---

### WSA-2026-006 — Gateway destructive purge is not confined to a validated Gateway-owned root

**Severity:** BLOCKER  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A1.2  
**Root area:** destructive lifecycle / filesystem safety  
**Affected repos:** `AI-Verse-Gateway`  
**Affected journeys:** install/uninstall/reinstall; operator recovery; dogfood safety

**Summary:**  
Gateway accepts an arbitrary `--home PATH`; `gatewayHome()` resolves it, and `uninstallComponent({ purge:true })` recursively force-removes that entire resolved path without first proving the target is a Gateway-owned installation root.

**Expected law:**  
A destructive component purge must be confined to a verified component-owned realpath and refuse filesystem roots, broad user/system roots, unrelated directories, symlink escapes, missing ownership markers and wrong ownership markers.

**Observed behavior:**  
The executable path is `CLI --home -> path.resolve(home) -> rm(home,{recursive:true,force:true})`. No valid `install.json`, matching `component_id`, realpath ownership boundary, root refusal or bounded owned-child deletion is required before the recursive removal.

**Primary evidence:** `E-A1.2-004`, `E-A1.2-015`.

**Impact:**  
A typo, unsafe automation argument or custom home can delete unrelated user/system data. Proven data-loss risk is a dogfood BLOCKER under the audit protocol.

**Required closure evidence:**  
After A6 authorizes repair: require and verify an exact Gateway ownership marker at the target realpath; reject root/broad/symlink/foreign targets; prefer removal of known Gateway-owned children; add cross-platform negative tests for unrelated directory, missing/wrong marker, root-like target and safe custom home; re-audit uninstall/reinstall on the repaired exact ref.

---

### WSA-2026-007 — Gateway lifecycle state is not operationally authoritative

**Severity:** HIGH  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A1.2  
**Root area:** setup/disable/uninstall/status lifecycle truth  
**Affected repos:** `AI-Verse-Gateway`  
**Affected journeys:** setup; status/doctor; serve; disable/enable; uninstall; remote exposure

**Summary:**  
Gateway's file-backed lifecycle state is not coordinated with the live server process, and setup publishes configuration before its own readiness verification has safely completed.

**Expected law:**  
Setup, status, doctor, live serving, disable and uninstall must project one authoritative lifecycle state. A successful disable/uninstall must not leave an already-running listener continuing normal authenticated work.

**Observed behavior:**  
`setupComponent` writes config before host `describe` succeeds and does not validate the built config before publishing it. `setEnabled(false)` only rewrites `config.json`; a running server retains its already-loaded in-memory config and checks `enabled` only at startup. `doctorComponent` does not make disabled config produce a disabled verdict. Normal uninstall removes on-disk integration/config files but has no live-process stop/refusal mechanism. The clean-install acceptance test closes the server before disable/uninstall, so the gap is outside the green happy path.

**Contradiction:** `C-A1.2-001`.

**Primary evidence:** `E-A1.2-004`, `E-A1.2-005`, `E-A1.2-013`.

**Impact:**  
An operator can believe Gateway is disabled or absent while a previously started network listener continues serving. Setup/status/doctor/live status can disagree materially.

**Required closure evidence:**  
After A6 authorizes repair: validate and transactionally publish setup or roll back on failure; establish one authoritative live lifecycle control; make disable/uninstall stop or make the existing process refuse work; align CLI status, doctor and live status; add live-server disable/uninstall plus failed-setup tests.

---

### WSA-2026-008 — Gateway durable state transitions are not linearizable under concurrency

**Severity:** HIGH  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A1.2  
**Root area:** concurrency / idempotency / session binding / run control  
**Affected repos:** `AI-Verse-Gateway`  
**Affected journeys:** run creation/retry; Automation wake replay; session isolation; pause/cancel; approval/control

**Summary:**  
Atomic JSON replacement protects file integrity, but several semantic read-check-write operations happen outside one serialized state transition. Concurrent callers can therefore violate higher-level idempotency, session-binding and privileged-control guarantees.

**Expected law:**  
Idempotency reservation, first session binding and privileged run-control transitions must be atomic at the semantic state level, not merely produce valid JSON files.

**Observed behavior:**  
`claimIdempotency` reads/checks the ledger before the serialized `atomicJson` replacement, so concurrent first claims can both observe an unused key and both return `new`. `createSession` similarly reads/validates before the write, allowing concurrent conflicting first bindings. `saveRun` replaces current run state from a previously captured candidate with no revision/CAS or terminal/control-state guard; execution holds mutable run objects across asynchronous boundaries, so a stale execution writer can overwrite a just-persisted pause/cancel before the next signal/status guard.

**Contradictions:** `C-A1.2-002`, `C-A1.2-003`.

**Primary evidence:** `E-A1.2-006`, `E-A1.2-007`, `E-A1.2-014`.

**Impact:**  
Possible duplicate runs/provider cost/owner effects, conflicting first session bindings, and pause/cancel that does not remain authoritative. A stale completion can also trigger post-completion digest/organization work after an operator believed the run was canceled.

**Required closure evidence:**  
After A6 authorizes repair: make claim/compare/reservation one atomic mutation; make first session binding atomic create-or-validate; add run revision/CAS or transition logic that rejects stale writers and preserves control/terminal states; check cancellation immediately before durable/effect boundaries; add deterministic concurrent tests for same/conflicting idempotency keys, conflicting first session binds, pause/cancel during result streaming and no post-cancel owner handoff.

---

### WSA-2026-009 — Native Brain state can escape the selected host root through symlinked parent directories

**Severity:** HIGH  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A1.3  
**Root area:** filesystem containment / scope isolation  
**Affected repos:** `AI-Verse-Brain`  
**Affected journeys:** native setup; initialization; canonical Brain writes; runtime locks; standalone-to-native adoption

**Summary:**  
Core native Brain state and runtime paths do not reject a symlinked `operator/` or `workspaces/` parent. Host compatibility follows directory symlinks, and later containment compares children against those already-resolved parents, so state can be written outside the selected AI-Verse root.

**Expected law:**  
All Brain-owned native state/runtime writes must remain physically inside the selected host root and intended operator/workspace scope, including hostile or malformed symlink layouts.

**Observed behavior:**  
`inspect_host` accepts `operator` and `workspaces` through `Path.is_dir()`. `StorageLayout.state_root` then checks `operator/brain` relative to resolved `operator`, or workspace relative to resolved `workspaces`. If the parent itself is a symlink outside the host root, both resolved paths share that outside base and the check succeeds. Initialization/adoption/runtime paths subsequently write there. Extension and direction registries separately reject symlinks, demonstrating the stricter intended pattern.

**Contradiction:** `C-A1.3-001`.

**Primary evidence:** `E-A1.3-004`, `E-A1.3-005`, `E-A1.3-006`.

**Impact:**  
A malformed or adversarial native host layout can place canonical Brain state outside the selected authority boundary.

**Required closure evidence:**  
After A6 authorizes repair: reject symlinked native operator/workspaces/workspace/runtime parents; realpath-confine final state/runtime/adoption destinations to the selected root and scope; apply the check to installation markers; add parent symlink/junction escape tests; re-audit native setup, writes and adoption.

---

### WSA-2026-010 — Goal operation-ID idempotency can race across different Goals

**Severity:** MEDIUM  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A1.3  
**Root area:** Goal concurrency / replay safety  
**Affected repos:** `AI-Verse-Brain`  
**Affected journeys:** Goal edit; transition; criteria mutations; progress recording

**Summary:**  
Goal operation receipts are keyed by scope + `operation_id`, but non-create Goal mutations serialize on scope + `goal_id`. Concurrent first-use mutations on two different Goals can therefore reuse one operation ID, both mutate canonical state and race to leave one receipt.

**Expected law:**  
Within one scope, one operation ID identifies one durable Goal mutation and changed-payload reuse must be rejected even under concurrent first use.

**Observed behavior:**  
`create` locks `scope|operation_id`. `edit`, `transition`, criteria add/remove/clear and `record_progress` lock `scope|goal_id`. Each performs a second receipt check inside that Goal lock, but different Goal IDs do not share a lock even though they share the operation-receipt namespace.

**Contradiction:** `C-A1.3-002`.

**Primary evidence:** `E-A1.3-008`, `E-A1.3-013`.

**Impact:**  
Conflicting concurrent callers can produce two canonical Goal mutations while later replay/audit state retains only one operation receipt.

**Required closure evidence:**  
After A6 authorizes repair: serialize admission on scope + operation ID as well as Goal revision; add deterministic cross-Goal same-operation-ID concurrent tests; prove exactly one mutation commits and the other receives an idempotency conflict.

---

### WSA-2026-011 — Materially different Brain source trees build with the same beta.2 package version

**Severity:** LOW  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A1.3  
**Root area:** release/version identity  
**Affected repos:** `AI-Verse-Brain`  
**Affected journeys:** source installs; artifact identification; support/debugging; update/release evidence

**Summary:**  
The accepted beta.2 descriptor pins `80019be5e6df29aee70371544bd96cedbf0329b9`, while frozen current main is 13 commits later with production-code changes but still builds and reports exactly `0.1.0-beta.2`.

**Expected law:**  
An accepted public-beta package version should identify one materially defined artifact, or later development code should carry a distinct development/pre-release identity.

**Observed behavior:**  
Current main `6f986e8d06c7f9c069fbf05aa92ae7b7a1af9bf4` is 13 commits ahead of accepted beta.2 and changes production `learning.py` / `local_host.py`, while `_version.py`, README and package build remain `0.1.0b2`. Release docs correctly instruct immutable-SHA installation, which bounds the risk.

**Contradiction:** `C-A1.3-003`.

**Primary evidence:** `E-A1.3-002`, `E-A1.3-017`, `E-A1.3-018`.

**Impact:**  
Version-only diagnostics, installation markers or source-built artifacts cannot distinguish accepted beta.2 from newer development code carrying the same version.

**Required closure evidence:**  
After A6 authorizes repair: give post-release main a distinct version identity or formally accept/reissue the new immutable beta revision; align README/changelog/version/release metadata semantics; add release QC preventing unintentional post-release production changes under the exact accepted version.

---

### WSA-2026-012 — Memory lifecycle parent-symlink escape can write or recursively delete outside the selected target

**Severity:** BLOCKER  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A1.4  
**Root area:** destructive lifecycle / filesystem containment  
**Affected repos:** `AI-Verse-Memory`  
**Affected journeys:** install; setup; uninstall; adapter installation/removal; runtime replacement

**Summary:**  
Canonical atomic Memory writes use strong path confinement, but lifecycle runtime/adapter operations do not validate the full parent chain. A symlinked parent can redirect copy and recursive deletion outside the selected target root.

**Expected law:**  
Every lifecycle write/delete path must be physically confined to the selected target. Recursive deletion must never follow a symlinked parent into external user/system data.

**Observed behavior:**  
Native runtime is lexically `target/scripts/ai-verse-memory`. Uninstall only checks whether that final directory itself is a symlink and then calls `shutil.rmtree(runtime)`. If `target/scripts` is a symlink to an external directory and its `ai-verse-memory` child is a normal directory, the final `is_symlink()` check is false and recursive deletion occurs outside target. Adapter paths under `.claude/skills` and `.agents/skills` have the same parent-chain class. Install/setup copy operations can also write outside root through those parents.

**Contradiction:** `C-A1.4-001`.

**Primary evidence:** `E-A1.4-010`, `E-A1.4-011`, `E-A1.4-017`.

**Impact:**  
Supported lifecycle commands can destroy unrelated external files/directories. This is a proven data-loss risk and therefore a dogfood BLOCKER.

**Required closure evidence:**  
After A6 authorizes repair: add one safe lifecycle-target resolver; reject symlink/junction/reparse parents; realpath-confine copy/remove targets; never rmtree before containment proof; add external-sentinel tests for symlinked scripts/.claude/.agents parent chains across supported platforms.

---

### WSA-2026-013 — Native canonical Memory writes ignore install/setup/attachment/enable lifecycle authority

**Severity:** HIGH  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A1.4  
**Root area:** lifecycle authority / canonical writes  
**Affected repos:** `AI-Verse-Memory`  
**Affected journeys:** pre-setup use; disable; detach; uninstall; migration-required state

**Summary:**  
Native canonical mutation is not gated by the component lifecycle state that status/doctor expose.

**Expected law:**  
Install must not imply setup/write authority. Disabled/detached/uninstalled Memory must not accept normal canonical writes. Migration-required state must not behave as normal ready authority.

**Observed behavior:**  
Effective Memory writes call `public_beta_assert_writable_authority`. That helper enforces retired authority only for standalone mode and returns immediately for native mode. It does not check local registry attachment, supported/installed/enabled flags, setup receipt or migration-required state. Therefore source code or already-loaded runtime can still mutate canonical native Memory before setup or after disable/detach/uninstall.

**Contradiction:** `C-A1.4-002`.

**Primary evidence:** `E-A1.4-004`, `E-A1.4-006`, `E-A1.4-010`, `E-A1.4-016`.

**Impact:**  
Lifecycle controls can report Memory unavailable while canonical historical state continues changing.

**Required closure evidence:**  
After A6 authorizes repair: make native write readiness consume authoritative registry/setup state; require supported+installed+attached+enabled+setup-complete for normal writes; narrow explicit bootstrap/migration exceptions; add tests for atomics, digests, promotion and metadata mutation before setup and after disable/detach/uninstall.

---

### WSA-2026-014 — Standalone-to-native Memory authority handoff is not failure-atomic across the two roots

**Severity:** HIGH  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A1.4  
**Root area:** migration / canonical authority transfer  
**Affected repos:** `AI-Verse-Memory`  
**Affected journeys:** Memory-first adoption; crash recovery; canonical owner handoff

**Summary:**  
Migration copy/verification is careful, but final authority transfer publishes target completion before source retirement is durably proven.

**Expected law:**  
No failure point may expose two writable canonical Memory routes. Handoff must be resumable and singular-authority preserving.

**Observed behavior:**  
`_retire_legacy_authority` writes in order: target native `authority-handoff.json=status:complete`; source `AUTHORITY.json=status:retired`; optional old-writer backup/stub. There is no cross-root journal/two-phase state. A failure after target complete but before source retirement leaves the old route active. Because WSA-2026-013 means native writes also ignore migration-required lifecycle state, the target can remain writable during the inconsistency.

**Contradiction:** `C-A1.4-003`.

**Primary evidence:** `E-A1.4-012`, `E-A1.4-018`.

**Impact:**  
An interrupted adoption can violate the architecture's one-canonical-owner rule and allow historical Memory divergence.

**Required closure evidence:**  
After A6 authorizes repair: implement prepared/pending/complete handoff states with stable handoff ID across both roots; do not publish target complete until source retirement is verified; make target normal writes fail while handoff incomplete; add fault-injection tests at every cross-root transition and prove idempotent recovery.

---

### WSA-2026-015 — Accepted Memory artifact identity and remote bootstrap are not pinned to current immutable source

**Severity:** LOW  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A1.4  
**Root area:** release/version/bootstrap reproducibility  
**Affected repos:** `AI-Verse-Memory`  
**Affected journeys:** remote install; support/debugging; release identification

**Summary:**  
Accepted beta.1 is pinned to `031e1e77c97ed3c9012235c7ffe0a4ece05e3695`, while frozen current main is 119 commits newer with material production behavior and still reports `0.3.0-beta.1`. Legacy remote bootstrap downloads mutable `main`.

**Expected law:**  
An accepted beta version should identify one materially defined artifact, and default release bootstrap should resolve an immutable accepted source.

**Observed behavior:**  
Current main `406b14fb4398eb1b16dd5f30e50520e8c3540972` remains versioned beta.1 despite 119 later commits. `install.sh` and `install.ps1` hardcode raw GitHub `main/scripts`; installer default ref is also `main`. README release language says bootstrap refs are pinned after acceptance.

**Contradiction:** `C-A1.4-004`.

**Primary evidence:** `E-A1.4-019`, `E-A1.4-020`, `E-A1.4-021`.

**Impact:**  
Version-only diagnostics cannot distinguish accepted beta.1 from later development source, and legacy remote bootstrap can install moving code. The formal release descriptor remains correctly pinned, so standalone severity is LOW; A5 must revisit release consequences.

**Required closure evidence:**  
After repair/release authorization: distinguish post-release main by version or issue a new accepted beta; pin remote bootstrap to immutable accepted ref by default; make development-main install explicit; add bootstrap pin QC.

---

### WSA-2026-016 — Skills lifecycle controller is not physically confined like provider packages

**Severity:** BLOCKER  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A1.5  
**Root area:** lifecycle controller containment  
**Affected repos:** `AI-Verse-Skills`

**Summary:**  
Provider package paths use physical containment, but the Skills controller directory `root/.aiverse` is not independently validated with the same rule before lifecycle state and retention operations derive from it.

**Contradiction:** `C-A1.5-001`.

**Primary evidence:** `E-A1.5-004`, `E-A1.5-010`, `E-A1.5-011`.

**Impact:**  
Lifecycle state may resolve outside the selected root, making destructive maintenance unsafe.

**Required closure evidence:**  
Add one controller-path safety primitive, reject unsafe controller indirection, prove all controller/generation/state paths remain inside the selected root, and add platform containment regressions.

---

### WSA-2026-017 — Skills lifecycle lock can be reclaimed while its holder is still live

**Severity:** HIGH  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A1.5  
**Root area:** lifecycle concurrency / serialization  
**Affected repos:** `AI-Verse-Skills`

**Summary:**  
The lifecycle lock records holder metadata, but stale recovery is based on age alone and does not confirm that the recorded holder is no longer live.

**Contradiction:** `C-A1.5-002`.

**Primary evidence:** `E-A1.5-004`, `E-A1.5-012`, `E-A1.5-014`.

**Impact:**  
Long lifecycle/learning operations can overlap a second mutation and lose semantic state updates.

**Required closure evidence:**  
Use holder-aware stale recovery and add deterministic tests for a live old holder plus dead/crashed-holder recovery.

---

### WSA-2026-018 — Skills retention cleanup does not protect active execution pins

**Severity:** MEDIUM  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A1.5  
**Root area:** immutable generation retention  
**Affected repos:** `AI-Verse-Skills`

**Summary:**  
Retention protects active/history generations and learning provenance, but there is no live execution lease/reference for a generation pinned by a running task.

**Contradiction:** `C-A1.5-003`.

**Primary evidence:** `E-A1.5-004`, `E-A1.5-010`, `E-A1.5-013`, `E-A1.5-014`.

**Impact:**  
Explicit retention maintenance can invalidate an otherwise valid long-running execution.

**Required closure evidence:**  
Add execution-generation leases or equivalent in-use protection and prove cleanup preserves a pin until the execution releases it.

---

### WSA-2026-019 — Accepted Skills beta identity and mutable bootstrap are not aligned with frozen current source

**Severity:** LOW  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A1.5  
**Root area:** release/version/bootstrap reproducibility  
**Affected repos:** `AI-Verse-Skills`

**Summary:**  
The accepted component descriptor binds `1.1.0-beta.1` to `042fda1ea2ddd8b79b74f1db9d3f65212953b64a`, while frozen current main is 190 commits newer, still reports the same version, and bootstrap follows mutable `main`.

**Contradiction:** `C-A1.5-004`.

**Primary evidence:** `E-A1.5-020`, `E-A1.5-021`, `E-A1.5-022`, `E-A1.5-023`.

**Impact:**  
Version-only diagnostics and default bootstrap do not uniquely identify the accepted immutable component artifact.

**Required closure evidence:**  
Use distinct post-release versioning or accept a new immutable component revision, and pin public-beta bootstrap to an immutable accepted ref by default.

---

### WSA-2026-020 — Data public client does not prove trusted scope provenance

**Severity:** HIGH  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A1.6  
**Root area:** trusted scope provenance / workspace isolation  
**Affected repos:** `AI-Verse-Data`

**Summary:**  
The public Data client contract says callers provide a trusted scope produced from `TrustedDataRoot`, but the exported scope is structural-only at runtime. Client validation does not prove scope provenance before trusting its database path and binding.

**Contradiction:** `C-A1.6-001`.

**Primary evidence:** `E-A1.6-003`, `E-A1.6-015`, `E-A1.6-016`, `E-A1.6-017`.

**Impact:**  
A structurally compatible scope object can bypass the path-derivation invariant advertised by the supported client surface. Native OS flows remain stronger because they construct scopes internally.

**Required closure evidence:**  
Make trusted scopes runtime-verifiable/nominal, reject untrusted structural substitutes, derive or validate path/binding from trusted root state, and add forged-scope regressions.

---

### WSA-2026-021 — Accepted Data alpha identity is older than frozen current behavior

**Severity:** LOW  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A1.6  
**Root area:** release/version/install reproducibility  
**Affected repos:** `AI-Verse-Data`

**Summary:**  
The accepted descriptor binds `0.1.0-alpha.0` to `189b13264ab86115d2f21fee3ba8cd5a8dac6581`, while frozen current main is 10 commits newer under the same version and the documented GitHub install path follows the mutable default branch.

**Contradiction:** `C-A1.6-002`.

**Primary evidence:** `E-A1.6-020`, `E-A1.6-021`, `E-A1.6-022`, `E-A1.6-023`.

**Impact:**  
Version-only diagnostics and the default GitHub install path do not uniquely identify the accepted immutable artifact.

**Required closure evidence:**  
Accept/version the newer behavior and use an immutable install reference when public-beta reproducibility is required.

---

### WSA-2026-022 — Multiple Bots operator/domain authority is not bound to trusted authenticated identity

**Severity:** HIGH  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A1.7  
**Root area:** operator/domain authority binding  
**Affected repos:** `AI-Verse-Multiple-Bots`

**Summary:**  
The repository's security contract distinguishes Gateway transport access from operator/domain authority, but sensitive control paths authorize against caller-supplied actor identity rather than trusted authenticated operator identity.

**Contradiction:** `C-A1.7-001`.

**Primary evidence:** `E-A1.7-010`, `E-A1.7-011`, `E-A1.7-012`, `E-A1.7-013`, `E-A1.7-014`.

**Impact:**  
Gateway access can satisfy operator-only domain controls without a second trusted operator binding. Affected classes include Approval decisions, durable Bot lifecycle/rebind, dead-letter retry and coordination cancellation/control surfaces.

**Required closure evidence:**  
Bind operator authorization to trusted host/session identity, separate provenance from authorization, and add negative tests showing transport access alone cannot satisfy operator-only mutations.

---

### WSA-2026-023 — Multiple Bots generic Worker coordination can cross workspace scope

**Severity:** HIGH  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A1.7  
**Root area:** Worker workspace isolation / canonical coordination authority  
**Affected repos:** `AI-Verse-Multiple-Bots`

**Summary:**  
Managed Team Run Worker creation is workspace-bound, but generic coordination policy does not apply equivalent pre-persistence Worker scope checks. Foreign-workspace coordination state can therefore target an existing Worker, and runner failure handling can subsequently update that Worker's canonical status.

**Contradiction:** `C-A1.7-002`.

**Primary evidence:** `E-A1.7-015`, `E-A1.7-016`, `E-A1.7-017`, `E-A1.7-018`, `E-A1.7-019`.

**Impact:**  
This creates a canonical cross-workspace coordination corruption/denial path. Runtime execution itself is blocked once the mismatch is detected, so this is not classified as external tool/credential takeover.

**Required closure evidence:**  
Make Workers first-class in generic workspace policy, reject foreign-workspace delegation/message state before persistence, and prevent failure/cancel paths from mutating a Worker until scope binding is proven.

---

## 5. Contradiction register

| Contradiction | Task | Classification | Material? | Finding | Status |
|---|---|---|---:|---|---|
| `C-A0.1-001` | A0.1 | historical-only wording | no | none | RECORDED / EXPLICITLY SUPERSEDED |
| `C-A0.2-001` | A0.2 | stale release metadata / documentation conflict | yes | `WSA-2026-001` | OPEN |
| `C-A0.2-002` | A0.2 | stale documentation | yes | `WSA-2026-002` | OPEN |
| `C-A0.3-001` | A0.3 | stale audit control documentation | yes | `WSA-2026-004` | OPEN |
| `C-A1.1-001` | A1.1 | stale machine-readable architecture metadata | yes | `WSA-2026-005` | OPEN |
| `C-A1.1-002` | A1.1 | stale implementation-status contract prose | yes | `WSA-2026-005` | OPEN |
| `C-A1.1-003` | A1.1 | historical-only superseded readiness wording | no | none | RECORDED / SUPERSEDED |
| `C-A1.2-001` | A1.2 | implementation defect / lifecycle truth split | yes | `WSA-2026-007` | OPEN |
| `C-A1.2-002` | A1.2 | implementation defect / concurrency gap | yes | `WSA-2026-008` | OPEN |
| `C-A1.2-003` | A1.2 | implementation defect / control-state race | yes | `WSA-2026-008` | OPEN |
| `C-A1.3-001` | A1.3 | implementation defect / filesystem containment | yes | `WSA-2026-009` | OPEN |
| `C-A1.3-002` | A1.3 | implementation defect / concurrency-idempotency gap | yes | `WSA-2026-010` | OPEN |
| `C-A1.3-003` | A1.3 | release/version identity drift | yes | `WSA-2026-011` | OPEN |
| `C-A1.4-001` | A1.4 | implementation defect / destructive lifecycle path containment | yes | `WSA-2026-012` | OPEN |
| `C-A1.4-002` | A1.4 | implementation defect / lifecycle write authority | yes | `WSA-2026-013` | OPEN |
| `C-A1.4-003` | A1.4 | implementation defect / migration handoff atomicity | yes | `WSA-2026-014` | OPEN |
| `C-A1.4-004` | A1.4 | release/version/bootstrap drift | yes | `WSA-2026-015` | OPEN |
| `C-A1.5-001` | A1.5 | implementation defect / lifecycle controller containment | yes | `WSA-2026-016` | OPEN |
| `C-A1.5-002` | A1.5 | implementation defect / lifecycle serialization | yes | `WSA-2026-017` | OPEN |
| `C-A1.5-003` | A1.5 | lifecycle contract / in-use generation retention | yes | `WSA-2026-018` | OPEN |
| `C-A1.5-004` | A1.5 | release/version/bootstrap drift | yes | `WSA-2026-019` | OPEN |
| `C-A1.6-001` | A1.6 | implementation defect / trusted scope provenance | yes | `WSA-2026-020` | OPEN |
| `C-A1.6-002` | A1.6 | release/version/install drift | yes | `WSA-2026-021` | OPEN |
| `C-A1.7-001` | A1.7 | implementation defect / operator authority binding | yes | `WSA-2026-022` | OPEN |
| `C-A1.7-002` | A1.7 | implementation defect / Worker workspace isolation | yes | `WSA-2026-023` | OPEN |

### C-A0.1-001

**Source A:** older `docs/PUBLIC-BETA-EXECUTION-PLAN.md` language says Agent remained blocked.  
**Source B:** current release record and public-beta tracker say Agent Distribution is released/accepted and explicitly supersede the older wording.  
**Higher-authority source:** current release record + current tracker.  
**Classification:** historical-only wording.  
**Finding:** none.

### C-A0.2-001

See `WSA-2026-001`.  
**Classification:** stale release metadata / documentation conflict.  
**Higher-authority resolution:** deliberately not collapsed during A0-A6; machine-readable and System sources remain separately recorded pending later revalidation/repair.

### C-A0.2-002

See `WSA-2026-002`.  
**Classification:** stale documentation.  
**Higher-authority source for current implementation state:** live executable Connections repository.

### C-A0.3-001

**Source A:** `docs/public-beta-audit/README.md` at `eba8f2e7a7005a4e597bbb75fef7913927e2f738` says audit execution begins at A0.1.  
**Source B:** `docs/public-beta-audit/EXECUTION-TRACKER-2026-09-15.md` at `eba8f2e7a7005a4e597bbb75fef7913927e2f738` says A0.1/A0.2 COMPLETE and A0.3 NEXT.  
**Higher-authority source:** canonical execution tracker.  
**Classification:** stale audit control documentation.  
**Finding:** `WSA-2026-004`.

### C-A1.1-001

**Source A:** `AI-VERSE.yaml` at OS `924a21a3dc1094d0fb6cc422f55fdfc714634e4d` names `.claude/skills/` as `source_of_truth.shared_skill_methodology`.  
**Source B:** current synchronizer, capability registry, runtime contract, capability architecture and architecture-check script all name `system/capabilities/` as canonical and `.claude/skills/` / `.agents/skills/` as generated peers.  
**Higher-authority source:** executable synchronizer/resolver + current exact-head tests/CI.  
**Classification:** stale machine-readable architecture metadata.  
**Finding:** `WSA-2026-005`.

### C-A1.1-002

**Source A:** `system/contracts/capability-provider-v1/README.md` still says external discovery/built-in migration are future/not activated.  
**Source B:** current resolver/synchronizer/architecture and exact-head real-provider integration show Provider v1 discovery and `system/capabilities/` migration implemented.  
**Higher-authority source:** executable implementation + current tests/CI.  
**Classification:** stale implementation-status prose in an otherwise active contract.  
**Finding:** `WSA-2026-005`.

### C-A1.1-003

**Source A:** dated `docs/SHIP-READINESS-AUDIT-2026-09-12.md` contains pre-fix “do not ship unchanged” wording and old blockers.  
**Source B:** later same-repository release/public-beta status records plus current implementation/tests show the bounded repairs.  
**Higher-authority source:** current executable implementation + current CI.  
**Classification:** historical-only superseded readiness wording.  
**Finding:** none.

### C-A1.2-001

**Source A:** Gateway README/lifecycle surfaces present setup, disable and uninstall as authoritative lifecycle transitions.  
**Source B:** current executable lifecycle/server code publishes config before setup verification completes, checks enabled only at server startup, leaves doctor independent of disabled state, and has no live-process stop/refusal path for uninstall.  
**Higher-authority source:** executable lifecycle/server implementation.  
**Classification:** implementation defect / lifecycle truth split.  
**Finding:** `WSA-2026-007`.

### C-A1.2-002

**Source A:** README says `Idempotency-Key` durably binds retries to the original payload and changed reuse is rejected.  
**Source B:** `claimIdempotency` performs the semantic read/check outside the serialized file-write critical section, so concurrent first claims can both be admitted.  
**Higher-authority source:** executable store implementation.  
**Classification:** implementation defect / concurrency gap.  
**Finding:** `WSA-2026-008`.

### C-A1.2-003

**Source A:** security/README present pause and cancel as authenticated privileged controls.  
**Source B:** `saveRun` can persist a stale execution candidate after a newer pause/cancel state because the transition has no revision/CAS or terminal/control guard.  
**Higher-authority source:** executable run/store implementation.  
**Classification:** implementation defect / control-state race.  
**Finding:** `WSA-2026-008`.

### C-A1.3-001

**Source A:** Brain security/architecture says state paths are validated for scope/path safety.  
**Source B:** native host/storage/installation code follows a symlinked `operator/` or `workspaces/` parent and validates descendants relative to that already-resolved outside parent.  
**Higher-authority source:** executable implementation.  
**Classification:** implementation defect / filesystem containment.  
**Finding:** `WSA-2026-009`.

### C-A1.3-002

**Source A:** Brain Goal contract says operation IDs are replay-safe/idempotent and changed reuse is rejected.  
**Source B:** non-create mutations use Goal-keyed locks while durable receipts are operation-ID keyed, leaving concurrent cross-Goal first use unserialized.  
**Higher-authority source:** executable Goal implementation.  
**Classification:** implementation defect / concurrency-idempotency gap.  
**Finding:** `WSA-2026-010`.

### C-A1.3-003

**Source A:** accepted release descriptor pins beta.2 to `80019be5e6df29aee70371544bd96cedbf0329b9`.  
**Source B:** frozen current main is 13 commits later with production-code changes and still reports/builds `0.1.0-beta.2`.  
**Higher-authority source:** current version source + immutable release descriptor + commit comparison.  
**Classification:** release/version identity drift.  
**Finding:** `WSA-2026-011`.

### C-A1.4-001

**Source A:** Memory safety/docs say escaping destination paths are rejected.  
**Source B:** lifecycle runtime/adapter copy/removal validates only final paths and can follow symlinked parents outside target before `shutil.rmtree`.  
**Higher-authority source:** executable lifecycle/installer implementation.  
**Classification:** implementation defect / destructive lifecycle path containment.  
**Finding:** `WSA-2026-012`.

### C-A1.4-002

**Source A:** public lifecycle separates install/setup/enablement and reports disabled/detached/uninstalled states.  
**Source B:** effective native canonical writer's authority helper returns without checking those native lifecycle states.  
**Higher-authority source:** executable writer/lifecycle implementation.  
**Classification:** implementation defect / lifecycle write authority.  
**Finding:** `WSA-2026-013`.

### C-A1.4-003

**Source A:** migration contract says no migration leaves two writable canonical Memory stores.  
**Source B:** target complete authority marker is written before source retirement is durably completed, with no cross-root transaction journal.  
**Higher-authority source:** executable migration implementation.  
**Classification:** implementation defect / migration handoff atomicity.  
**Finding:** `WSA-2026-014`.

### C-A1.4-004

**Source A:** accepted descriptor pins beta.1 and README says accepted bootstrap refs are immutable.  
**Source B:** current main is 119 commits newer under the same version and remote bootstrap hardcodes mutable main.  
**Higher-authority source:** current version/installer code + immutable descriptor + commit comparison.  
**Classification:** release/version/bootstrap drift.  
**Finding:** `WSA-2026-015`.

### C-A1.5-001

**Source A:** Skills filesystem architecture requires canonicalized targets.  
**Source B:** lifecycle controller state derives from `root/.aiverse` without equivalent physical containment.  
**Higher-authority source:** executable lifecycle implementation.  
**Finding:** `WSA-2026-016`.

### C-A1.5-002

**Source A:** immutable-generation docs say lifecycle mutation is serialized and only stale locks recover.  
**Source B:** recovery uses age without holder-liveness verification.  
**Higher-authority source:** executable lifecycle lock.  
**Finding:** `WSA-2026-017`.

### C-A1.5-003

**Source A:** a generation pin is documented as complete for an execution lifetime.  
**Source B:** retention protection has no active-execution lease/reference input.  
**Higher-authority source:** executable retention implementation.  
**Finding:** `WSA-2026-018`.

### C-A1.5-004

**Source A:** accepted descriptor binds beta.1 to `042fda1e…`.  
**Source B:** frozen current main is 190 commits newer under the same version and mutable-main bootstrap.  
**Higher-authority source:** current source + immutable descriptor + commit comparison.  
**Finding:** `WSA-2026-019`.

### C-A1.6-001

**Source A:** client/security docs require a trusted `DataDatabaseScope` derived from `TrustedDataRoot`.  
**Source B:** runtime client validation accepts structural scope identity and trusts supplied path/binding without nominal provenance.  
**Higher-authority source:** executable client/scope implementation.  
**Finding:** `WSA-2026-020`.

### C-A1.6-002

**Source A:** accepted descriptor binds alpha.0 to `189b1326…`.  
**Source B:** frozen current main is 10 commits newer under the same version and mutable GitHub install route.  
**Higher-authority source:** current package/source + immutable descriptor + commit comparison.  
**Finding:** `WSA-2026-021`.

### C-A1.7-001

**Source A:** secure-remote contract says transport authentication does not grant domain authority.  
**Source B:** sensitive operator controls accept caller-supplied actor identity and validate operator status syntactically rather than through trusted authenticated identity.  
**Higher-authority source:** executable server/Gateway/recovery/control implementation.  
**Finding:** `WSA-2026-022`.

### C-A1.7-002

**Source A:** temporary Workers are documented and implemented as Team Run/workspace-scoped principals.  
**Source B:** generic coordination policy does not apply equivalent Worker workspace validation before delegation/message persistence, while failure handling can update the resolved Worker after a mismatched Task is rejected.  
**Higher-authority source:** executable policy, delegation, queue/store and principal-runner implementation.  
**Finding:** `WSA-2026-023`.

## 6. Evidence ID register

Evidence IDs remain local to their originating task. This section indexes published IDs without replacing the source packets.

### A0.1 evidence IDs

| Evidence ID | Short description | Canonical source packet |
|---|---|---|
| `E-A0.1-001` | live owner repository inventory | `snapshots/A0-REPOSITORY-UNIVERSE.md` |
| `E-A0.1-002` | canonical audit program/tracker | same |
| `E-A0.1-003` | System identity/current component family | same |
| `E-A0.1-004` | public-beta repository/product decisions | same |
| `E-A0.1-005` | current Agent release boundary | same |
| `E-A0.1-006` | `hub` identity evidence | same |
| `E-A0.1-007` | `real-estate-visuals` identity evidence | same |
| `E-A0.1-008` | `animation-shorts` identity evidence | same |
| `E-A0.1-009` | `JujiStats` identity evidence | same |
| `E-A0.1-010` | current System GitHub/runner state | same |

### A0.2 evidence IDs

| Evidence ID | Short description | Canonical source packet |
|---|---|---|
| `E-A0.2-001` | metadata/default branches/visibility/license | `snapshots/A0-SNAPSHOT.md` |
| `E-A0.2-002` | exact default-branch refs | same |
| `E-A0.2-003` | open PR state | same |
| `E-A0.2-004` | exact-head GitHub Actions | same |
| `E-A0.2-005` | private-runner job detail | same |
| `E-A0.2-006` | Distribution release catalog | same |
| `E-A0.2-007` | Agent release manifests | same |
| `E-A0.2-008` | Core/Full release manifests | same |
| `E-A0.2-009` | Distribution product path | same |
| `E-A0.2-010` | Token tag namespace | same |
| `E-A0.2-011` | GitHub Releases state | same |
| `E-A0.2-012` | current milestone evidence | same |

### A0.3 evidence IDs

#### E-A0.3-001 — current audit control state

**Sources:**
- `docs/public-beta-audit/EXECUTION-TRACKER-2026-09-15.md`
- `docs/public-beta-audit/EVIDENCE-FINDING-PROTOCOL.md`
- `docs/public-beta-audit/PROGRAM-2026-09-15.md`

**Ref:** `eba8f2e7a7005a4e597bbb75fef7913927e2f738`  
**Claim supported:** A0.3 is the only NEXT task; finding ID format/severity/confidence/state law; product repos remain read-only; every task gets its own checkpoint.

#### E-A0.3-002 — frozen product snapshot drift recheck

**Source:** live GitHub `refs/heads/main` for the 13 non-System scoped repositories.  
**Frozen refs:** A0.2 Section 3.  
**Result:** all 13 non-System scoped repository heads still exactly match the A0.2 freeze.

#### E-A0.3-003 — System audit-only drift classification

**Source:** compare `a10bf0e8ea230a6460adf45354f314bba68bb614...eba8f2e7a7005a4e597bbb75fef7913927e2f738`.  
**Result:** System is ahead only by A0.2 audit records:
- `docs/public-beta-audit/EXECUTION-TRACKER-2026-09-15.md`;
- `docs/public-beta-audit/snapshots/A0-SNAPSHOT.md`.

**Claim supported:** System drift since the frozen pre-A0.2 baseline is audit-record-only and does not invalidate product/meta baseline truth.

#### E-A0.3-004 — live open PR state

**Source:** GitHub PR search across all 14 scoped repositories.  
**Result:** zero open PRs before A0.3 branch creation.

#### E-A0.3-005 — stale audit README

**Source A:** `docs/public-beta-audit/README.md` at `eba8f2e7a7005a4e597bbb75fef7913927e2f738`.  
**Source B:** canonical tracker at `eba8f2e7a7005a4e597bbb75fef7913927e2f738`.  
**Claim supported:** README says execution begins at A0.1 while tracker says A0.3 NEXT.

#### E-A0.3-006 — pre-existing register negative-space check

**Source:** live `docs/public-beta-audit/` tree at `eba8f2e7a7005a4e597bbb75fef7913927e2f738`.  
**Result:** no `findings/` directory or `FINDING-REGISTER.md` existed before A0.3.

### A0.4 evidence IDs

| Evidence ID | Short description | Canonical source packet |
|---|---|---|
| `E-A0.4-001` | relationship-matrix protocol | `seams/RELATIONSHIP-MATRIX.md` |
| `E-A0.4-002` | frozen repository universe and refs | same |
| `E-A0.4-003` | pre-task drift recheck | same |
| `E-A0.4-004` | open PR state | same |
| `E-A0.4-005` | deterministic 182-pair enumeration | same |
| `E-A0.4-006` | canonical finding-register allocation state | same |

### A0.5 evidence IDs

| Evidence ID | Short description | Canonical source packet |
|---|---|---|
| `E-A0.5-001` | canonical freeze-gate contract | `snapshots/A0-FREEZE-GATE.md` |
| `E-A0.5-002` | frozen non-System ref recheck | same |
| `E-A0.5-003` | System audit-only drift classification | same |
| `E-A0.5-004` | scoped open PR state | same |
| `E-A0.5-005` | Dashboard MC1.4 pause state | same |
| `E-A0.5-006` | release-surface tag recheck | same |
| `E-A0.5-007` | GitHub Release recheck | same |
| `E-A0.5-008` | accepted A0 control artifacts | same |

### A1.1 evidence IDs

| Evidence ID | Short description | Canonical source packet |
|---|---|---|
| `E-A1.1-001` | frozen OS tree and repository metadata | `repos/AI-Verse-OS.md` |
| `E-A1.1-002` | product/runtime identity | same |
| `E-A1.1-003` | architecture/ownership/source layers | same |
| `E-A1.1-004` | canonical capability implementation | same |
| `E-A1.1-005` | stale capability metadata/contract | same |
| `E-A1.1-006` | lifecycle implementation | same |
| `E-A1.1-007` | permissions and write edge | same |
| `E-A1.1-008` | direction/current-context ownership | same |
| `E-A1.1-009` | workspace/profile owner automation | same |
| `E-A1.1-010` | host adapter and owner routes | same |
| `E-A1.1-011` | Data host boundary | same |
| `E-A1.1-012` | semantic migration | same |
| `E-A1.1-013` | progressive onboarding | same |
| `E-A1.1-014` | exact-head push CI | same |
| `E-A1.1-015` | merged PR-head owner-route CI | same |
| `E-A1.1-016` | current release/status boundaries | same |
| `E-A1.1-017` | history/repair provenance | same |
| `E-A1.1-018` | live pre/post evidence-collection control state | same |
| `E-A1.1-019` | branch-protection evidence limitation | same |

### A1.2 evidence IDs

| Evidence ID | Short description | Canonical source packet |
|---|---|---|
| `E-A1.2-001` | frozen Gateway tree and repository metadata | `repos/AI-Verse-Gateway.md` |
| `E-A1.2-002` | identity/package/component contract | same |
| `E-A1.2-003` | architecture/protocol/security | same |
| `E-A1.2-004` | lifecycle/CLI implementation | same |
| `E-A1.2-005` | server/auth boundary | same |
| `E-A1.2-006` | store/durability implementation | same |
| `E-A1.2-007` | run engine and privileged controls | same |
| `E-A1.2-008` | adapter/runtime/subprocess boundaries | same |
| `E-A1.2-009` | Context Ladder implementation | same |
| `E-A1.2-010` | core test suite | same |
| `E-A1.2-011` | exact-head CI | same |
| `E-A1.2-012` | current merged PR-head integration | same |
| `E-A1.2-013` | lifecycle test coverage gap | same |
| `E-A1.2-014` | concurrency test coverage gap | same |
| `E-A1.2-015` | destructive purge implementation trace | same |
| `E-A1.2-016` | rejected architecture evaluations | same |
| `E-A1.2-017` | history and research provenance | same |
| `E-A1.2-018` | GitHub Release state | same |
| `E-A1.2-019` | live control-state recheck | same |

### A1.3 evidence IDs

| Evidence ID | Short description | Canonical source packet |
|---|---|---|
| `E-A1.3-001` | frozen Brain tree and repository metadata | `repos/AI-Verse-Brain.md` |
| `E-A1.3-002` | README/BRAIN/package/version/license identity | same |
| `E-A1.3-003` | protocol/security ownership and authority laws | same |
| `E-A1.3-004` | storage/scope/object-write implementation | same |
| `E-A1.3-005` | integration/native paths/write readiness | same |
| `E-A1.3-006` | installation/lifecycle/adoption implementation | same |
| `E-A1.3-007` | direction ownership implementation/tests | same |
| `E-A1.3-008` | canonical Goal implementation | same |
| `E-A1.3-009` | effective policy / permission intersection | same |
| `E-A1.3-010` | action replay/receipt implementation | same |
| `E-A1.3-011` | owner-write / learning / Data candidate gates | same |
| `E-A1.3-012` | bridge/vendor subprocess hardening | same |
| `E-A1.3-013` | 26-module test inventory | same |
| `E-A1.3-014` | exact-head CI run 34969997987 | same |
| `E-A1.3-015` | exact-head Skills contract run 34969998014 | same |
| `E-A1.3-016` | exact-head OS direction run 34969997970 | same |
| `E-A1.3-017` | accepted beta.2 release descriptor | same |
| `E-A1.3-018` | accepted beta.2 -> frozen-main 13-commit comparison | same |
| `E-A1.3-019` | recent PR/repair history | same |
| `E-A1.3-020` | live pre-write ref/open-PR recheck | same |

### A1.4 evidence IDs

| Evidence ID | Short description | Canonical source packet |
|---|---|---|
| `E-A1.4-001` | frozen Memory tree and repository metadata | `repos/AI-Verse-Memory.md` |
| `E-A1.4-002` | README/manifest/SKILL/security identity and ownership | same |
| `E-A1.4-003` | architecture/protocol/migration contracts | same |
| `E-A1.4-004` | public wrapper and public-beta patch installation | same |
| `E-A1.4-005` | canonical path containment implementation | same |
| `E-A1.4-006` | mutation lock/atomic/idempotency implementation | same |
| `E-A1.4-007` | capture/forget/supersession implementation | same |
| `E-A1.4-008` | session digest/promotion implementation | same |
| `E-A1.4-009` | progressive recall/orientation/relationship implementation | same |
| `E-A1.4-010` | component lifecycle implementation | same |
| `E-A1.4-011` | installer/extension registry implementation | same |
| `E-A1.4-012` | migration authority-handoff ordering | same |
| `E-A1.4-013` | 18-module test inventory | same |
| `E-A1.4-014` | exact-head Test run 34983522129 | same |
| `E-A1.4-015` | 12 exact-head successful jobs and executed steps | same |
| `E-A1.4-016` | lifecycle disabled-write coverage gap | same |
| `E-A1.4-017` | lifecycle parent-symlink coverage gap | same |
| `E-A1.4-018` | migration interruption coverage gap | same |
| `E-A1.4-019` | accepted beta.1 descriptor | same |
| `E-A1.4-020` | accepted beta.1 -> frozen-main 119-commit comparison | same |
| `E-A1.4-021` | remote bootstrap mutable-main sources | same |
| `E-A1.4-022` | recent Context Ladder/relationship/benchmark history | same |
| `E-A1.4-023` | live pre-write ref/open-PR recheck | same |

### A1.5 evidence IDs

| Evidence ID | Short description | Canonical source packet |
|---|---|---|
| `E-A1.5-001` | frozen Skills tree and repository metadata | `repos/AI-Verse-Skills.md` |
| `E-A1.5-002` | README/architecture ownership model | same |
| `E-A1.5-003` | registry counts, source pins and trust policy | same |
| `E-A1.5-004` | immutable generation lifecycle | same |
| `E-A1.5-005` | provider path/digest/index validation | same |
| `E-A1.5-006` | admission/security/trust implementation | same |
| `E-A1.5-007` | readiness v2 | same |
| `E-A1.5-008` | execution receipt v2 | same |
| `E-A1.5-009` | governed learning lifecycle | same |
| `E-A1.5-010` | public lifecycle/retention implementation | same |
| `E-A1.5-011` | controller-path construction | same |
| `E-A1.5-012` | stale-lock recovery | same |
| `E-A1.5-013` | retention protection inputs | same |
| `E-A1.5-014` | generation lifecycle tests | same |
| `E-A1.5-015` | exact-head Validate run 34901693154 | same |
| `E-A1.5-016` | exact-head Readiness run 34901693118 | same |
| `E-A1.5-017` | exact-head Full E2E run 34901693143 | same |
| `E-A1.5-018` | Video Editor PR #14 evidence | same |
| `E-A1.5-019` | Video Editor acceptance run 34901198219 | same |
| `E-A1.5-020` | accepted component descriptor | same |
| `E-A1.5-021` | accepted-to-current 190-commit comparison | same |
| `E-A1.5-022` | current distribution version | same |
| `E-A1.5-023` | mutable-main bootstrap route | same |
| `E-A1.5-024` | live pre-write ref/open-PR recheck | same |

### A1.6 evidence IDs

| Evidence ID | Short description | Canonical source packet |
|---|---|---|
| `E-A1.6-001` | frozen Data tree and repository metadata | `repos/AI-Verse-Data.md` |
| `E-A1.6-002` | README/architecture ownership reconstruction | same |
| `E-A1.6-003` | trusted-root and workspace path implementation | same |
| `E-A1.6-004` | SQLite identity/binding/open behavior | same |
| `E-A1.6-005` | OCC and separate-process race evidence | same |
| `E-A1.6-006` | idempotency implementation | same |
| `E-A1.6-007` | events/receipts provenance implementation | same |
| `E-A1.6-008` | transaction/bulk safety | same |
| `E-A1.6-009` | internal/user-schema migration contracts | same |
| `E-A1.6-010` | backup/export/import implementation/tests | same |
| `E-A1.6-011` | quarantine/recovery implementation | same |
| `E-A1.6-012` | native registry/materialization/lifecycle | same |
| `E-A1.6-013` | Bots/App authority narrowing | same |
| `E-A1.6-014` | Brain/Memory/Dashboard/Connections/Automation boundaries | same |
| `E-A1.6-015` | public client scope validation/open path | same |
| `E-A1.6-016` | exported structural DataDatabaseScope | same |
| `E-A1.6-017` | secure-client scope wrapper | same |
| `E-A1.6-018` | exact-head CI run 34864837334 | same |
| `E-A1.6-019` | six exact-head cross-platform CI jobs | same |
| `E-A1.6-020` | accepted component descriptor | same |
| `E-A1.6-021` | accepted-to-current 10-commit comparison | same |
| `E-A1.6-022` | current package/index alpha.0 identity | same |
| `E-A1.6-023` | documented mutable GitHub install path | same |
| `E-A1.6-024` | live pre-write ref/open-PR recheck | same |

### A1.7 evidence IDs

| Evidence ID | Short description | Canonical source packet |
|---|---|---|
| `E-A1.7-001` | frozen Multiple Bots tree and repository metadata | `repos/AI-Verse-Multiple-Bots.md` |
| `E-A1.7-002` | ownership reconstruction | same |
| `E-A1.7-003` | Bot/Worker distinction and managed Worker binding | same |
| `E-A1.7-004` | durable Bot coordination policy | same |
| `E-A1.7-005` | remote lease narrowing and receipt checks | same |
| `E-A1.7-006` | operational budget enforcement | same |
| `E-A1.7-007` | Token ownership boundary | same |
| `E-A1.7-008` | execution queue/concurrency/recovery | same |
| `E-A1.7-009` | Handoff ownership/lease transfer | same |
| `E-A1.7-010` | secure remote Gateway contract | same |
| `E-A1.7-011` | bearer/loopback implementation | same |
| `E-A1.7-012` | public operator-control routes | same |
| `E-A1.7-013` | operator validation implementation | same |
| `E-A1.7-014` | release acceptance security interpretation | same |
| `E-A1.7-015` | generic Worker policy scope behavior | same |
| `E-A1.7-016` | generic delegation route | same |
| `E-A1.7-017` | Worker execution workspace validation | same |
| `E-A1.7-018` | runner failure Worker update path | same |
| `E-A1.7-019` | Worker mailbox/delivery scope behavior | same |
| `E-A1.7-020` | OS write-command owner boundary | same |
| `E-A1.7-021` | Brain/Memory/Skills/Automations boundaries | same |
| `E-A1.7-022` | native registry/materialization/lifecycle | same |
| `E-A1.7-023` | uninstall ownership/preservation tests | same |
| `E-A1.7-024` | exact-head CI run 34872178884 | same |
| `E-A1.7-025` | exact-head CI job 104070507325 | same |
| `E-A1.7-026` | beta.1 release merge to frozen-current comparison | same |
| `E-A1.7-027` | current release-evaluation source | same |
| `E-A1.7-028` | live pre-write ref/open-PR recheck | same |

## 7. Finding allocation ledger

| Range | Status |
|---|---|
| `WSA-2026-001` | allocated A0.2 |
| `WSA-2026-002` | allocated A0.2 |
| `WSA-2026-003` | allocated A0.2 |
| `WSA-2026-004` | allocated A0.3 |
| `WSA-2026-005` | allocated A1.1 |
| `WSA-2026-006` | allocated A1.2 |
| `WSA-2026-007` | allocated A1.2 |
| `WSA-2026-008` | allocated A1.2 |
| `WSA-2026-009` | allocated A1.3 |
| `WSA-2026-010` | allocated A1.3 |
| `WSA-2026-011` | allocated A1.3 |
| `WSA-2026-012` | allocated A1.4 |
| `WSA-2026-013` | allocated A1.4 |
| `WSA-2026-014` | allocated A1.4 |
| `WSA-2026-015` | allocated A1.4 |
| `WSA-2026-016` | allocated A1.5 |
| `WSA-2026-017` | allocated A1.5 |
| `WSA-2026-018` | allocated A1.5 |
| `WSA-2026-019` | allocated A1.5 |
| `WSA-2026-020` | allocated A1.6 |
| `WSA-2026-021` | allocated A1.6 |
| `WSA-2026-022` | allocated A1.7 |
| `WSA-2026-023` | allocated A1.7 |
| `WSA-2026-024` | **NEXT UNUSED** |

Future tasks must inspect this register before allocating a new finding ID.

## 8. Negative-space checks

A0.3 explicitly checked:

- no pre-existing canonical finding register existed under `docs/public-beta-audit/`;
- no product repository head drifted from the frozen A0.2 snapshot;
- no open PR existed across the scoped 14-repository universe before the A0.3 branch was created;
- System drift from the pre-A0.2 frozen baseline was confined to audit tracker/snapshot records;
- no published finding ID above `WSA-2026-003` was present in the completed A0.1/A0.2 packets;
- no finding was silently closed merely because its severity is LOW/INFO;
- no historical contradiction was promoted into a defect without material impact;
- no product repair was performed while instantiating the ledger.

## 9. Evidence limitations

- GitHub code-search indexing is not used as proof that IDs are absent; allocation is based on completed canonical A0 packets plus the live audit tree.
- A0.3 does not independently re-prove the underlying technical substance of A0.2 findings. It verifies and registers the published records.
- Future findings may raise severity or confidence when later repository/seam/journey evidence exposes broader impact.
- Finding severity/state may change only with explicit new evidence and must preserve change history.
- The private-repository runner limitation remains unresolved and may constrain hosted validation of this checkpoint.

## 10. Downstream rules for later audit tasks

Every later task must:

1. read this register before allocating a new finding ID;
2. continue from `WSA-2026-005`;
3. cite local evidence IDs and exact source refs;
4. add every material contradiction to the contradiction register;
5. update affected finding state/severity/confidence only with cited new evidence;
6. preserve prior wording/history rather than overwriting the record silently;
7. leave product repair for the repair phase unless emergency containment is required.

A0.4 may now create the relationship-matrix skeleton with all relations initially UNKNOWN as required by its own protocol. It must not begin seam auditing yet.

## 11. Task completion record

**Task:** A0.3 Evidence/finding ledger  
**System task baseline:** `eba8f2e7a7005a4e597bbb75fef7913927e2f738`  
**Frozen product refs rechecked:** all 13 non-System product/distribution repos unchanged from A0.2; System audit-only drift classified by `E-A0.3-003`  
**Evidence read:** A0.1/A0.2 completed packets; canonical tracker; audit program; evidence/finding protocol; audit README; live PR/ref/tree state  
**Claims verified:** stable ID law instantiated; existing evidence/contradiction IDs indexed; four findings registered with severity/confidence/state; next finding ID reserved as `WSA-2026-005`  
**Contradictions:** inherited `C-A0.1-001`, `C-A0.2-001`, `C-A0.2-002`; opened `C-A0.3-001`  
**Findings:** inherited `WSA-2026-001` through `003`; opened `WSA-2026-004`  
**Negative-space checks:** Section 8  
**Evidence limitations:** Section 9  
**Verdict:** COMPLETE / PASS for audit ledger instantiation  
**Tracker change:** A0.3 COMPLETE; accepted progress 3/100; A0.4 NEXT  
**Next task:** A0.4 Relationship matrix skeleton
