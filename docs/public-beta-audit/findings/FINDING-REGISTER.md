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

**Next unused finding ID:** `WSA-2026-012`.

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

Current counts:

| Dimension | Count |
|---|---:|
| BLOCKER | 1 |
| HIGH | 3 |
| MEDIUM | 1 |
| LOW | 5 |
| INFO | 1 |
| PROVEN | 11 |
| STRONG | 0 |
| POSSIBLE | 0 |
| UNVERIFIED | 0 |
| OPEN | 11 |
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
| `WSA-2026-012` | **NEXT UNUSED** |

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
