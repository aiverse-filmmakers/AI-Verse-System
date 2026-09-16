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

**Next unused finding ID:** `WSA-2026-058`.

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
| `WSA-2026-024` | HIGH | PROVEN | OPEN | canonical cost truth / trusted ACTUAL source enforcement | `ai-verse-token` | A1.8 |
| `WSA-2026-025` | MEDIUM | PROVEN | OPEN | pricing evidence transactionality / concurrency | `ai-verse-token` | A1.8 |
| `WSA-2026-026` | HIGH | PROVEN | OPEN | canonical store ownership / lifecycle safety / health truth | `AI-Verse-Automations` | A1.9 |
| `WSA-2026-027` | HIGH | PROVEN | OPEN | canonical schedule authority / migration handoff / readiness truth | `AI-Verse-Automations` | A1.9 |
| `WSA-2026-028` | MEDIUM | PROVEN | OPEN | native attachment lifecycle / host discovery truth | `AI-Verse-Automations` | A1.9 |
| `WSA-2026-029` | BLOCKER | PROVEN | OPEN | destructive lifecycle / filesystem containment | `AI-Verse-Connections` | A1.10 |
| `WSA-2026-030` | HIGH | PROVEN | OPEN | system scope isolation / canonical installation binding | `AI-Verse-Connections` | A1.10 |
| `WSA-2026-031` | HIGH | PROVEN | OPEN | credential origin binding / token passthrough prevention | `AI-Verse-Connections` | A1.10 |
| `WSA-2026-032` | HIGH | PROVEN | OPEN | final-edge authority / concurrency / safety budgets | `AI-Verse-Connections` | A1.10 |
| `WSA-2026-033` | HIGH | PROVEN | OPEN | external path authorization / provider-edge containment | `AI-Verse-Connections` | A1.10 |
| WSA-2026-034 | HIGH | PROVEN | OPEN | lifecycle concurrency / release receipt authority | ai-verse-distribution | A1.12 |
| WSA-2026-035 | MEDIUM | PROVEN | OPEN | first-run requirements / executable compatibility truth | ai-verse-distribution | A1.12 |
| WSA-2026-036 | MEDIUM | PROVEN | OPEN | diagnostics / secret redaction / failure handling | ai-verse-distribution | A1.12 |
| WSA-2026-037 | LOW | PROVEN | OPEN | repository-local release/status documentation drift | ai-verse-distribution | A1.12 |
| WSA-2026-038 | HIGH | PROVEN | OPEN | workspace isolation / realtime subscription lifecycle | AI-Verse-Dashboard | A1.13 |
| WSA-2026-039 | HIGH | PROVEN | OPEN | system identity / registered-root authority binding | AI-Verse-Dashboard | A1.13 |
| WSA-2026-040 | HIGH | PROVEN | OPEN | local gateway authentication / privacy boundary | AI-Verse-Dashboard | A1.13 |
| WSA-2026-041 | MEDIUM | PROVEN | OPEN | local browser integration / Origin policy | AI-Verse-Dashboard | A1.13 |
| WSA-2026-042 | MEDIUM | PROVEN | OPEN | canonical ownership / projection truth | AI-Verse-Dashboard | A1.13 |
| WSA-2026-043 | MEDIUM | PROVEN | OPEN | release contract consistency / machine-readable acceptance | AI-Verse-System | A1.14 |
| WSA-2026-044 | MEDIUM | PROVEN | OPEN | meta authority / living-spec synchronization / current release truth | AI-Verse-System | A1.14 |
| WSA-2026-045 | MEDIUM | PROVEN | OPEN | retrieval freshness / provenance cache invalidation | AI-Verse-Gateway | A2.5 |
| WSA-2026-046 | MEDIUM | PROVEN | OPEN | release composition / public-member product path | AI-Verse-Skills, ai-verse-distribution, AI-Verse-System | A2.8 |
| WSA-2026-047 | MEDIUM | PROVEN | OPEN | migration release evidence / cross-owner persistence | AI-Verse-OS, AI-Verse-Gateway, AI-Verse-Memory, AI-Verse-Data, ai-verse-distribution | A3.2 |
| WSA-2026-048 | MEDIUM | PROVEN | OPEN | learning release evidence / cross-owner user journey | AI-Verse-Gateway, AI-Verse-OS, AI-Verse-Brain, AI-Verse-Skills, ai-verse-distribution | A3.5 |
| WSA-2026-049 | MEDIUM | PROVEN | OPEN | system isolation release evidence / multi-root journey | ai-verse-distribution, AI-Verse-OS, AI-Verse-Gateway, AI-Verse-Memory, AI-Verse-Data, AI-Verse-Multiple-Bots, AI-Verse-Automations, ai-verse-token | A3.10 |
| WSA-2026-050 | MEDIUM | PROVEN | OPEN | authentication availability / pre-auth resource exhaustion | AI-Verse-Gateway | A4.1 |
| WSA-2026-051 | HIGH | PROVEN | OPEN | SSRF / DNS rebinding / credential-bearing provider edge | AI-Verse-Connections | A4.1 |
| WSA-2026-052 | HIGH | PROVEN | OPEN | migration concurrency / source-level idempotency | AI-Verse-OS | A4.2 |
| WSA-2026-053 | HIGH | PROVEN | OPEN | structured Data concurrency / natural-key uniqueness | AI-Verse-OS, AI-Verse-Brain, AI-Verse-Data | A4.2 |
| WSA-2026-054 | HIGH | PROVEN | OPEN | crash recovery / state-lock ownership / external-effect receipt safety | AI-Verse-Connections | A4.3 |
| WSA-2026-055 | MEDIUM | PROVEN | OPEN | external-effect idempotency / crash uncertainty / recovery | AI-Verse-Connections | A4.3 |
| WSA-2026-056 | MEDIUM | PROVEN | OPEN | canonical receipt corruption / health truth / recovery | AI-Verse-Connections | A4.3 |
| WSA-2026-057 | MEDIUM | PROVEN | OPEN | provider-error diagnostics / receipt minimization / secret-at-rest boundary | AI-Verse-Connections | A4.4 |

Current counts:

| Dimension | Count |
|---|---:|
| BLOCKER | 4 |
| HIGH | 24 |
| MEDIUM | 19 |
| LOW | 9 |
| INFO | 1 |
| PROVEN | 57 |
| STRONG | 0 |
| POSSIBLE | 0 |
| UNVERIFIED | 0 |
| OPEN | 57 |
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

### WSA-2026-024 — Token ACTUAL monetary truth can bypass the trusted actual-cost source registry

**Severity:** HIGH  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A1.8  
**Root area:** canonical cost truth / trusted ACTUAL source enforcement  
**Affected repos:** `ai-verse-token`

**Summary:**  
Token has an explicit trusted actual-cost source registry, but the canonical ledger and generic CollectorRunner do not require an attached actual charge to prove that it passed through that registry. A syntactically valid event can therefore reach the immutable ledger with provider/runtime-reported monetary data and later be rated as ACTUAL.

**Contradiction:** `C-A1.8-001`.

**Primary evidence:** `E-A1.8-004`, `E-A1.8-006`, `E-A1.8-007`, `E-A1.8-008`, `E-A1.8-010`.

**Impact:**  
A buggy or overly trusted collector/direct storage caller can elevate unverified money into Token's strongest canonical monetary truth class.

**Required closure evidence:**  
Make ACTUAL admission require trusted source evidence at canonical ingest; prevent generic collector/storage input from self-asserting ACTUAL; retain trusted provider/runtime adapters; add negative regression coverage.

---

### WSA-2026-025 — Token failed pricing sync can leave part of a snapshot batch visible

**Severity:** MEDIUM  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A1.8  
**Root area:** pricing evidence transactionality / concurrency  
**Affected repos:** `ai-verse-token`

**Summary:**  
Pricing batches are fully validated before persistence, but new immutable snapshot files are then committed sequentially. A later write/race failure can leave earlier files visible while the synchronizer records the source refresh as failed.

**Contradiction:** `C-A1.8-002`.

**Primary evidence:** `E-A1.8-012`, `E-A1.8-013`.

**Impact:**  
A source refresh reported as failed can still change the tariff set available to CALCULATED cost logic. The path requires an I/O or cross-process failure after validation, so severity is MEDIUM.

**Required closure evidence:**  
Stage and atomically publish one fetched pricing batch or add a durable batch commit manifest; ensure failed refreshes expose no new batch members; add deterministic fault/race regressions.

---

### WSA-2026-026 — Automations canonical store has no ownership/format identity gate

**Severity:** HIGH  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A1.9  
**Root area:** canonical store ownership / lifecycle safety / health truth  
**Affected repos:** `AI-Verse-Automations`

**Summary:**  
Setup/update can initialize and stamp an existing SQLite file at the configured Automations database path without first proving the file belongs to Automations. Lifecycle health then checks generic SQLite integrity rather than exact Automations format/schema identity.

**Contradiction:** `C-A1.9-001`.

**Primary evidence:** `E-A1.9-005`, `E-A1.9-006`, `E-A1.9-019`.

**Impact:**  
A foreign or structurally incompatible SQLite database can be modified or treated as healthy canonical scheduler state.

**Required closure evidence:**  
Add durable database ownership/format identity, exact schema verification, fail-closed foreign-database handling and compatible-version migration gates, with negative tests.

---

### WSA-2026-027 — Automations legacy-definition conflict is not a live execution kill fence

**Severity:** HIGH  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A1.9  
**Root area:** canonical schedule authority / migration handoff / readiness truth  
**Affected repos:** `AI-Verse-Automations`

**Summary:**  
Legacy OS automation definitions correctly block initial setup enablement, but live conflicts introduced after setup are only detected by doctor. Normal status can remain ready and the scheduler continues execution because Engine does not recheck the live legacy-authority condition.

**Contradiction:** `C-A1.9-002`.

**Primary evidence:** `E-A1.9-019`, `E-A1.9-020`.

**Impact:**  
The component's own anti-dual-authority law is not continuously enforced, leaving a supported path where conflicting definition authority exists while Automations remains active.

**Required closure evidence:**  
Make live legacy conflict part of readiness/execution fencing, align status and doctor, define explicit handoff clearing semantics and add post-setup conflict regressions.

---

### WSA-2026-028 — Automations component lifecycle and attached OS extension lifecycle diverge

**Severity:** MEDIUM  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A1.9  
**Root area:** native attachment lifecycle / host discovery truth  
**Affected repos:** `AI-Verse-Automations`

**Summary:**  
OS attachment creates an installed/enabled registry entry and bridge files, but component enable/disable/uninstall do not synchronize that registry state or detach those integration files.

**Contradiction:** `C-A1.9-003`.

**Primary evidence:** `E-A1.9-019`, `E-A1.9-021`, `E-A1.9-022`.

**Impact:**  
Host discovery can disagree with Automations owner state. The retained bridge fails closed after uninstall, so this is lifecycle/discovery inconsistency rather than residual execution authority.

**Required closure evidence:**  
Synchronize component and registry lifecycle under existing lock controls, or define a separate explicit attach/detach state model; preserve canonical SQLite state and add attached lifecycle regressions.

---

### WSA-2026-029 — Connections destructive purge is not confined to a verified owned root

**Severity:** BLOCKER  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A1.10  
**Root area:** destructive lifecycle / filesystem containment  
**Affected repos:** `AI-Verse-Connections`

**Summary:**  
`uninstall --purge` recursively force-removes the configured Connections home. That home can be supplied by `AIVERSE_CONNECTIONS_HOME` or the public service constructor, and no ownership marker or safe-root validation is required before deletion.

**Contradiction:** `C-A1.10-001`.

**Primary evidence:** `E-A1.10-005`.

**Impact:**  
A typo or unsafe lifecycle invocation can delete unrelated user data. This is a proven destructive data-loss path.

**Required closure evidence:**  
Require a verified Connections ownership marker/realpath, reject root/broad/foreign targets, prefer known-owned-child deletion and add negative purge tests.

---

### WSA-2026-030 — Connections setup system binding is not enforced by connection/execution state

**Severity:** HIGH  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A1.10  
**Root area:** system scope isolation / canonical installation binding  
**Affected repos:** `AI-Verse-Connections`

**Summary:**  
Setup stores one lifecycle system ID, but Generic/MCP connection creation accepts any system ID and execution only compares the request against the connection, not against the installation binding.

**Contradiction:** `C-A1.10-002`.

**Primary evidence:** `E-A1.10-005`, `E-A1.10-006`, `E-A1.10-010`, `E-A1.10-011`.

**Impact:**  
One Connections home can hold and execute external authority for systems other than the system to which setup claims it is bound.

**Required closure evidence:**  
Enforce lifecycle-system identity during creation and final execution, and add an explicit migration/rebind workflow plus two-system tests.

---

### WSA-2026-031 — MCP reauth bypasses the cross-origin bearer-handle isolation rule

**Severity:** HIGH  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A1.10  
**Root area:** credential origin binding / token passthrough prevention  
**Affected repos:** `AI-Verse-Connections`

**Summary:**  
Initial MCP registration forbids one credential handle from being reused across different origins, but reauth does not repeat that check. The next verification resolves and transmits the reused bearer token to the second origin.

**Contradiction:** `C-A1.10-003`.

**Primary evidence:** `E-A1.10-007`, `E-A1.10-009`, `E-A1.10-014`.

**Impact:**  
A token intended for one MCP security origin can be disclosed to another through a supported reauthentication path.

**Required closure evidence:**  
Centralize origin/credential binding checks across add, reauth and verify, fail before credential transmission, and add two-origin regressions.

---

### WSA-2026-032 — Connections final provider edge omits lifecycle and budget authority rechecks

**Severity:** HIGH  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A1.10  
**Root area:** final-edge authority / concurrency / safety budgets  
**Affected repos:** `AI-Verse-Connections`

**Summary:**  
The security contract says the complete authority intersection is recalculated immediately before provider execution, including component readiness and current rate/budget limits. Code checks both only during initial planning; the final edge reloads only the connection/capability state.

**Contradiction:** `C-A1.10-004`.

**Primary evidence:** `E-A1.10-003`, `E-A1.10-010`, `E-A1.10-011`, `E-A1.10-012`.

**Impact:**  
A concurrent disable/uninstall can fail to fence already-planned work, and concurrent different-key executions can exceed the same configured call budget.

**Required closure evidence:**  
Re-read lifecycle at the provider edge, atomically reserve/check budgets across concurrent executions, and add deterministic lifecycle/budget race tests.

---

### WSA-2026-033 — Generic API normalized path can escape the admitted prefix

**Severity:** HIGH  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A1.10  
**Root area:** external path authorization / provider-edge containment  
**Affected repos:** `AI-Verse-Connections`

**Summary:**  
Generic API path-prefix authorization checks the raw caller string before WHATWG URL normalization. Encoded or plain dot-segments can therefore pass an admitted prefix and normalize to a path outside it while remaining on the same origin.

**Contradiction:** `C-A1.10-005`.

**Primary evidence:** `E-A1.10-013`, `E-A1.10-019`.

**Impact:**  
A trusted connection credential can be sent to a same-origin endpoint outside the operator-admitted path boundary.

**Required closure evidence:**  
Normalize first, authorize the final pathname, reject path-confusion forms and add encoded/plain traversal regressions.

---


### WSA-2026-034 - concurrent Distribution lifecycle commands can overwrite newer receipt truth

**Severity:** HIGH  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A1.12  
**Root area:** lifecycle concurrency / release receipt authority  
**Affected repos:** ai-verse-distribution

**Summary:**  
Distribution atomically replaces individual receipt files but does not serialize complete mutating lifecycle operations across processes. Two supported commands can load the same current receipt, perform different owner effects, and then commit conflicting stale snapshots.

**Contradiction:** C-A1.12-004.

**Primary evidence:** E-A1.12-008, E-A1.12-010, E-A1.12-012, E-A1.12-013, E-A1.12-017, E-A1.12-027.

**Impact:**  
A later stale writer can resurrect or erase Distribution lifecycle receipt state after another owner mutation completed, leaving release/install truth inconsistent with the actual owner state.

**Required closure evidence:**  
Add one cross-platform single-writer lifecycle boundary covering owner mutation plus receipt commit, stale-writer/version rejection, deterministic stale-lock recovery and concurrency regressions for setup/install/uninstall/update interactions.

---

### WSA-2026-035 - ordinary Agent documentation understates the required Python version

**Severity:** MEDIUM  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A1.12  
**Root area:** first-run requirements / executable compatibility truth  
**Affected repos:** ai-verse-distribution

**Summary:**  
The ordinary Agent README path says Python 3.9+ and package metadata permits installation on Python 3.9+, while the released Agent compatibility record requires Python 3.11 and executable preflight rejects lower versions.

**Contradiction:** C-A1.12-001.

**Primary evidence:** E-A1.12-003, E-A1.12-005, E-A1.12-029.

**Impact:**  
A user can satisfy documented prerequisites and install Distribution successfully, then fail at the ordinary aiverse start product path on Python 3.9 or 3.10.

**Required closure evidence:**  
Align public prerequisites and product messaging with executable release requirements, distinguish Core/Agent floors and add a requirement-consistency regression.

---

### WSA-2026-036 - failed owner-process secrets can bypass CLI redaction through the exception message

**Severity:** MEDIUM  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A1.12  
**Root area:** diagnostics / secret redaction / failure handling  
**Affected repos:** ai-verse-distribution

**Summary:**  
ProcessError embeds raw child stderr/stdout in its exception text. The CLI emits that raw exception text as the top-level message even though the separate stdout and stderr fields are sanitized.

**Contradiction:** C-A1.12-002.

**Primary evidence:** E-A1.12-015, E-A1.12-016, E-A1.12-019, E-A1.12-028.

**Impact:**  
Credentials printed by a failing owner process can leak through terminal or JSON error output and captured logs.

**Required closure evidence:**  
Remove or sanitize raw child output from user-visible exception messages, sanitize secret-bearing argv where applicable and add plain/JSON regressions for bearer tokens, API keys and passwords.

---

### WSA-2026-037 - current architecture and roadmap retain stale Agent release status

**Severity:** LOW  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A1.12  
**Root area:** repository-local release/status documentation drift  
**Affected repos:** ai-verse-distribution

**Summary:**  
Current machine-readable release truth and README show the Agent public beta released, but architecture still describes Agent as blocked and Roadmap Phase 5 still leaves the release-branch merge incomplete after it occurred.

**Contradiction:** C-A1.12-003.

**Primary evidence:** E-A1.12-004, E-A1.12-006, E-A1.12-026.

**Impact:**  
Maintainer-facing documentation gives contradictory current release state while runtime behavior remains unaffected.

**Required closure evidence:**  
Align current architecture/roadmap with machine release truth and retain obsolete pre-merge wording only as historical evidence.

---


### WSA-2026-038 - WebSocket resubscribe leaves prior workspace subscription active

**Severity:** HIGH  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A1.13  
**Root area:** workspace isolation / realtime subscription lifecycle  
**Affected repos:** AI-Verse-Dashboard

**Summary:**  
A socket that subscribes to workspace A and then workspace B receives a new B subscription without removing the A subscription. The old listener stays in SubscriptionHub and can keep delivering A events to the same socket.

**Contradiction:** C-A1.13-001.

**Primary evidence:** E-A1.13-011, E-A1.13-013, E-A1.13-021.

**Impact:**  
Live workspace context can bleed across an explicit workspace switch and contaminate the selected workspace UI.

**Required closure evidence:**  
Fence or remove the previous subscription before accepting a new workspace scope, validate the subscribed workspace, release every subscription on close, and add deterministic A -> B -> A resubscribe regressions.

---

### WSA-2026-039 - registered systemId can silently follow a replaced OS filesystem root

**Severity:** HIGH  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A1.13  
**Root area:** system identity / registered-root authority binding  
**Affected repos:** AI-Verse-Dashboard

**Summary:**  
SystemRegistry stores a canonical pathname at registration, but later reads follow whatever filesystem object currently resolves at that pathname. A replaced or redirected path can therefore change the OS behind an existing systemId without explicit user reapproval.

**Contradiction:** C-A1.13-002.

**Primary evidence:** E-A1.13-008, E-A1.13-009, E-A1.13-016, E-A1.13-022.

**Impact:**  
A stable Dashboard system identity can silently move from approved OS A to different filesystem content B while retaining A's UI/runtime identity.

**Required closure evidence:**  
Bind registration to durable root identity, detect root replacement before reads, fail closed on drift, require explicit rebind/reapproval and add replacement/symlink/rename regressions.

---

### WSA-2026-040 - Dashboard-local Gateway exposes OS read APIs without authentication

**Severity:** HIGH  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A1.13  
**Root area:** local gateway authentication / privacy boundary  
**Affected repos:** AI-Verse-Dashboard

**Summary:**  
The temporary Dashboard-local Gateway is loopback-only but does not authenticate HTTP or WebSocket clients. Missing Origin is intentionally accepted for non-browser clients, and those clients can enumerate systems/workspaces and request read projections.

**Contradiction:** C-A1.13-003.

**Primary evidence:** E-A1.13-004, E-A1.13-011, E-A1.13-014, E-A1.13-015.

**Impact:**  
Any local process able to connect to the port can access Dashboard-exposed AI-Verse read data outside the intended UI authorization flow.

**Required closure evidence:**  
Require local authenticated client identity if this gateway remains executable, preserve loopback binding, reject unauthenticated HTTP/WS requests and add negative local-client tests.

---

### WSA-2026-041 - browser Origin check rejects normal localhost origins with explicit ports

**Severity:** MEDIUM  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A1.13  
**Root area:** local browser integration / Origin policy  
**Affected repos:** AI-Verse-Dashboard

**Summary:**  
The local Gateway allows only exact Origin values http://localhost and http://127.0.0.1. A normal browser app at http://localhost:5173 or another explicit local port is rejected.

**Contradiction:** C-A1.13-004.

**Primary evidence:** E-A1.13-011, E-A1.13-012, E-A1.13-020, E-A1.13-021, E-A1.13-023.

**Impact:**  
The intended separate browser/Vite host cannot communicate with the local Dashboard Gateway under ordinary local port layouts without a workaround.

**Required closure evidence:**  
Define an explicit trusted loopback-origin policy supporting approved ports and add HTTP/WS browser-origin tests for localhost and 127.0.0.1.

---

### WSA-2026-042 - synthetic Health/Inbox projections create Dashboard shadow semantics

**Severity:** MEDIUM  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A1.13  
**Root area:** canonical ownership / projection truth  
**Affected repos:** AI-Verse-Dashboard

**Summary:**  
Current read models synthesize health and inbox meaning from generic file presence, headings and filenames instead of consuming owner-declared domain truth. The repository's own preservation report now identifies these semantics as shadow-authority scaffolding.

**Contradiction:** C-A1.13-005.

**Primary evidence:** E-A1.13-003, E-A1.13-006, E-A1.13-017, E-A1.13-018.

**Impact:**  
The Dashboard can present authoritative-looking health/attention state that no canonical owner actually declared.

**Required closure evidence:**  
Replace production semantics with owner-backed projections, preserve unknown/unavailable when owner truth is absent, and explicitly label any retained heuristic as derived/non-authoritative.

---


### WSA-2026-043 - Whole-Release Preservation Schema and semantic validator disagree on evidence metadata

**Severity:** MEDIUM  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A1.14  
**Root area:** release contract consistency / machine-readable acceptance  
**Affected repos:** AI-Verse-System

**Summary:**  
The published Whole-Release Preservation JSON Schema allows evidence items containing only kind, status and revision. It defines run_id, job_id and url as optional. The canonical semantic validator instead requires all six keys exactly.

**Contradiction:** C-A1.14-001.

**Primary evidence:** E-A1.14-012, E-A1.14-013, E-A1.14-014, E-A1.14-016, E-A1.14-017.

**Impact:**  
A release-evidence producer following the published Schema and contract prose can create an artifact that is Schema-valid but rejected by official semantic validation.

**Required closure evidence:**  
Choose one normative rule, align Schema/prose/validator, add explicit optionality or mandatory-field regressions, and rerun exact canonical contract validation on Python 3.11 and 3.13.

---

### WSA-2026-044 - System living-spec propagation leaves canonical current-state surfaces inconsistent

**Severity:** MEDIUM  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A1.14  
**Root area:** meta authority / living-spec synchronization / current release truth  
**Affected repos:** AI-Verse-System

**Summary:**  
System's Living Specification Protocol requires accepted implementation and release changes to propagate into current component specs, source maps, QC/readiness, system synthesis and changelog. That propagation did not complete after accepted Context Ladder and other release evolution.

**Contradiction:** C-A1.14-002.

**Primary evidence:** E-A1.14-002, E-A1.14-004, E-A1.14-005, E-A1.14-006, E-A1.14-007, E-A1.14-008, E-A1.14-009.

**Impact:**  
Different canonical-looking System files give different answers about current component heads, readiness and release/candidate state, which can misdirect agents, maintainers and later release decisions.

**Required closure evidence:**  
Synchronize current System truth from exact accepted owner/release refs, update tracker/Blueprint/changelog and affected component spec/QC/source maps, establish a canonical Gateway component evidence record, align Token current state, preserve historical provenance, and add bounded consistency checks where practical.

---

### WSA-2026-045 - repeated Gateway deep-context reads can replay stale exact-source evidence

**Severity:** MEDIUM  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A2.5  
**Root area:** retrieval freshness / provenance cache invalidation  
**Affected repos:** AI-Verse-Gateway

**Summary:**  
Gateway exact-source reads correctly revalidate Memory/Gateway source freshness during a real owner read, but the per-run deep-context dedupe cache keys only on the retrieval request. A repeated identical request can return the prior result without re-running source-version/fingerprint validation.

**Contradiction:** C-A2.5-001.

**Primary evidence:** E-A2.5-006, E-A2.5-008, E-A2.5-009, E-A2.5-010, E-A2.5-011.

**Impact:**  
Within one long-running run, an exact-source request repeated after the underlying source changes can receive stale prior exact content instead of the current owner result or a stale response.

**Required closure evidence:**  
Bind exact-source cache entries to validated source identity/version/fingerprint, revalidate before replay, return stale or perform a fresh owner read after source drift, and add Memory-source and Gateway-external-source drift regressions.

---

### WSA-2026-046 - accepted member-facing Video Editor release is absent from every admitted Distribution composition

**Severity:** MEDIUM  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A2.8  
**Root area:** release composition / public-member product path  
**Affected repos:** AI-Verse-Skills, ai-verse-distribution, AI-Verse-System

**Summary:**  
AI-Verse Video Editor is marked 100% complete and member-facing at accepted Skills head `8c321c03421a2e0e470280cc40e588a27c1a510d`. No admitted Distribution release set contains that Skills revision. The newest Agent candidate pins `71264af6b2b9a575812fe18858d75a54ea2ff545`, which predates the Video Editor package.

**Contradiction:** C-A2.8-006.

**Primary evidence:** E-A2.8-006, E-A2.8-008, E-A2.8-012, E-A2.8-013, E-A2.8-014, E-A2.8-015, E-A2.8-016.

**Impact:**  
A member using the canonical one-product Distribution path cannot receive the accepted member-facing Video Editor capability. Standalone current Skills installation can reach it, but whole-Agent compatibility for that Skills revision has not been proven by an admitted Distribution clean-machine composition.

**Required closure evidence:**  
Create a new immutable Agent candidate containing an exact accepted Skills ref with Video Editor, rerun Distribution and three-platform clean-machine Agent acceptance plus relevant Context Ladder/Invisible regressions, prove Video Editor is installed/discoverable/selectable, and update System release/member-path truth. Do not mutate an existing immutable release set.

---

### WSA-2026-047 - semantic migration-drop lacks real composed owner acceptance

**Severity:** MEDIUM  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A3.2  
**Root area:** migration release evidence / cross-owner persistence  
**Affected repos:** AI-Verse-OS, AI-Verse-Gateway, AI-Verse-Memory, AI-Verse-Data, ai-verse-distribution

**Summary:**  
Semantic migration-drop is a current user-facing migration path. OS/Gateway tests verify classification, clarification, source binding, owner request shape and replay, but replace real sibling Memory/Data/workspace owners with stubs or fixtures. No reviewed composed acceptance executes the full migration through real owners and verifies persistence/restart/replay.

**Contradiction:** C-A3.2-001.

**Primary evidence:** E-A3.2-002 through E-A3.2-010.

**Impact:**  
A3 cannot fully verify the no-loss cross-owner migration journey. This is an acceptance-evidence gap, not proof that real owner routing currently fails.

**Required closure evidence:**  
Add a composed acceptance using exact admitted refs that imports a raw prior-assistant context drop through real OS, workspace, Memory and Data owners, survives restart/clarification resume, proves replay does not duplicate writes, verifies no wholesale raw-source copy, and exercises one downstream owner rejection/failure.

---

### WSA-2026-048 - Goal-to-learned-Skill journey lacks one real composed acceptance

**Severity:** MEDIUM  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A3.5  
**Root area:** learning release evidence / cross-owner user journey  
**Affected repos:** AI-Verse-Gateway, AI-Verse-OS, AI-Verse-Brain, AI-Verse-Skills, ai-verse-distribution

**Summary:**  
The product has strong evidence for Brain Goal evaluation, Brain learning-candidate admission, OS owner routing, Skills proposal/evaluation/auto-promotion, later capability discovery/use, quarantine and rollback. But no reviewed acceptance executes the entire real user journey from one Goal-bound Gateway run through real OS/Brain/Skills learning and later real Gateway reuse.

**Contradiction:** C-A3.5-001.

**Primary evidence:** E-A3.5-002 through E-A3.5-019.

**Impact:**  
The audit cannot certify the complete Goal/self-learning user journey under one real run/session/Goal/proposal/generation evidence chain. This is an end-to-end release-evidence gap, not proof of an implementation failure.

**Required closure evidence:**  
Add one composed acceptance at exact admitted refs that creates a real Brain Goal, runs a real authenticated Gateway task bound to it, evaluates the Goal, routes a safe learning candidate through real OS/Brain/Skills, exercises propose and auto modes, restarts, rediscovers and uses the learned Skill with exact generation/digest binding, quarantines an unsafe candidate, rolls back, proves replay safety and confirms Brain Goal truth remains unchanged by the Skills lifecycle.

---

### WSA-2026-049 - no real two-system A/B isolation acceptance exists for the supported product path

**Severity:** MEDIUM  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A3.10  
**Root area:** system isolation release evidence / multi-root journey  
**Affected repos:** ai-verse-distribution, AI-Verse-OS, AI-Verse-Gateway, AI-Verse-Memory, AI-Verse-Data, AI-Verse-Multiple-Bots, AI-Verse-Automations, ai-verse-token

**Summary:**  
A3 requires a real two-system A/B isolation journey. Current Distribution product acceptance contains exactly two acceptance scripts and each creates one AI-Verse root per run. Existing component-level system/workspace isolation tests do not prove two full systems can coexist without cross-root, cross-system or lifecycle interference.

**Contradiction:** C-A3.10-005.

**Primary evidence:** E-A3.10-020 through E-A3.10-023.

**Impact:**  
The audit cannot certify that two simultaneous AI-Verse installations remain isolated under same-named workspaces/resources, concurrent runtime activity, lifecycle changes or restart. This is an end-to-end release-evidence gap, not proof that two-system operation currently fails.

**Required closure evidence:**  
Add immutable clean-machine acceptance that creates Systems A and B in separate roots and Distribution homes, gives them distinct system IDs and Gateway ports, uses same-named workspaces in both, proves distinct Memory/Data/Bot/Automation/Token state, attempts cross-system access, restarts and lifecycle-mutates one system while the other remains unchanged, and runs on Ubuntu/macOS/Windows.

---

### WSA-2026-050 - invalid bearer requests can exhaust Gateway CPU before rate limiting

**Severity:** MEDIUM  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A4.1  
**Root area:** authentication availability / pre-auth resource exhaustion  
**Affected repo:** AI-Verse-Gateway

**Summary:**  
Gateway performs synchronous scrypt bearer verification before its only request rate limiter. Invalid bearer requests never reach that principal-scoped limiter, so an unauthenticated caller can repeatedly force event-loop KDF work. Default loopback binding reduces exposure, but supported remote mode remains reachable behind a TLS proxy.

**Contradiction:** C-A4.1-001.

**Primary evidence:** E-A4.1-002 through E-A4.1-005.

**Impact:**  
Unauthenticated local callers, or remote callers in supported remote mode, can degrade or deny Gateway service without bypassing authentication.

**Required closure evidence:**  
Add bounded pre-auth rate limiting, avoid unbounded synchronous KDF work on the request event loop, define proxy/client-address semantics, and prove invalid-bearer flooding does not starve authenticated traffic.

---

### WSA-2026-051 - Connections DNS rebinding can bypass private-network containment at the credential-bearing fetch edge

**Severity:** HIGH  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A4.1  
**Root area:** SSRF / DNS rebinding / credential-bearing provider edge  
**Affected repo:** AI-Verse-Connections

**Summary:**  
Connections validates private-network policy using a standalone DNS lookup, then performs ordinary fetch which can resolve the hostname again. Generic API and MCP attach trusted credentials before this fetch. A controlled hostname can therefore pass the public-address check and later resolve to a private address for the actual credential-bearing connection.

**Contradiction:** C-A4.1-002.

**Primary evidence:** E-A4.1-012 through E-A4.1-016.

**Impact:**  
Potential private/internal network SSRF and trusted bearer/header credential disclosure through a supported provider connection.

**Required closure evidence:**  
Pin outbound connections to policy-approved addresses or equivalent non-rebinding resolver/dispatcher behavior, validate actual remote address, preserve TLS hostname verification, and add deterministic rebinding tests for Generic API and MCP.

---

### WSA-2026-052 - concurrent semantic migration can execute multiple classifier plans for one source

**Severity:** HIGH  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A4.2  
**Root area:** migration concurrency / source-level idempotency  
**Affected repo:** AI-Verse-OS

**Summary:**  
Semantic migration treats source identity as stronger than classifier-plan variation, but same-source admission is a read/check followed by owner effects followed by late receipt publication. Two simultaneous first imports of the same source with different plans can both pass the no-prior-source check. Because their subaction idempotency keys are derived from different plan-dependent import keys, both plans can execute canonical owner writes.

**Contradiction:** C-A4.2-007.

**Primary evidence:** E-A4.2-013 through E-A4.2-017.

**Impact:**  
One imported context source can concurrently create divergent/duplicate operator, workspace, Memory or Data state even though sequential semantics promise source-level replay.

**Required closure evidence:**  
Add a durable source-identity reservation/serialization boundary before owner effects, define crash recovery for in-progress imports, and prove concurrent same-source same/different-plan requests collapse to one canonical import.

---

### WSA-2026-053 - concurrent automatic Data candidates can create duplicate canonical natural-key records

**Severity:** HIGH  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A4.2  
**Root area:** structured Data concurrency / natural-key uniqueness  
**Affected repos:** AI-Verse-OS, AI-Verse-Brain, AI-Verse-Data

**Summary:**  
Automatic structured truth uses an OS query-then-create natural-key check. Brain candidate IDs can differ for the same natural key. Data create idempotency is candidate-specific, and storage uniqueness is by generated record ID rather than semantic natural key. Two concurrent admitted candidates can therefore both see zero matches and commit separate canonical records for one logical key.

**Contradiction:** C-A4.2-008.

**Primary evidence:** E-A4.2-018 through E-A4.2-024.

**Impact:**  
Concurrent automatic organization can create duplicate canonical current truth and make later automatic updates ambiguous/blocked.

**Required closure evidence:**  
Move semantic uniqueness into the Data owner via atomic unique constraint/upsert/CAS semantics and prove simultaneous different candidate IDs for one natural key result in exactly one canonical record.

---


### WSA-2026-054 - Connections crash can orphan the global write lock and indefinitely wedge canonical mutations

**Severity:** HIGH  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A4.3  
**Root area:** crash recovery / state-lock ownership / external-effect receipt safety  
**Affected repo:** AI-Verse-Connections

**Summary:**  
Connections serializes canonical mutation with a persistent `.write.lock` directory. The lock has no holder identity, liveness check, stale age protocol or crashed-holder recovery. If the owning process terminates before its `finally` cleanup, the directory remains and all later `withLock` mutations time out.

**Contradiction:** C-A4.3-006.

**Primary evidence:** E-A4.3-021, E-A4.3-022, E-A4.3-023.

**Impact:**  
Lifecycle, registry, idempotency and terminal receipt mutations can remain unavailable until manual filesystem intervention. Doctor does not detect the stale lock. Requests without an idempotency key can also reach an external provider and only then fail terminal receipt publication against the orphaned lock, creating effect-without-durable-receipt risk.

**Required closure evidence:**  
Add holder-aware crash recovery, expose lock health through doctor, prove dead holders can be reclaimed without stealing live locks, and add process-death tests around reservation and terminal receipt publication.

---

### WSA-2026-055 - Connections crash after reservation can leave an external effect permanently unknown under a pending idempotency key

**Severity:** MEDIUM  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A4.3  
**Root area:** external-effect idempotency / crash uncertainty / recovery  
**Affected repo:** AI-Verse-Connections

**Summary:**  
Connections persists a pending idempotency reservation before provider execution, but the reservation remains `attemptedExternal:false` until a later terminal receipt is appended. A crash after provider-edge entry but before that terminal append leaves the same key permanently pending with no durable unknown-effect state or recovery protocol.

**Contradiction:** C-A4.3-007.

**Primary evidence:** E-A4.3-023, E-A4.3-024, E-A4.3-027.

**Impact:**  
The same key cannot be safely retried or explicitly reconciled, and durable state cannot distinguish pre-effect crash from an effect that may already have occurred. Usage-budget accounting also counts only `attemptedExternal:true` receipts, so unknown post-edge attempts are not represented correctly.

**Required closure evidence:**  
Persist a provider-edge/unknown state, classify abandoned reservations on restart, require explicit reconciliation or provider-supported safe replay, include unknown attempts in budget semantics, and fault-test every pre/post-provider crash boundary.

---

### WSA-2026-056 - Connections receipt-log corruption can disable execution while health checks remain unaware

**Severity:** MEDIUM  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A4.3  
**Root area:** canonical receipt corruption / health truth / recovery  
**Affected repo:** AI-Verse-Connections

**Summary:**  
Connections reads its append-only NDJSON receipt log by parsing every non-empty line. A single malformed/truncated line makes the entire receipt read fail. External execution depends on that history, while doctor does not validate receipt-store readability.

**Contradiction:** C-A4.3-008.

**Primary evidence:** E-A4.3-025, E-A4.3-026, E-A4.3-028.

**Impact:**  
Corruption can block external execution and make idempotency/budget evidence unavailable while lifecycle/registry-based health can remain apparently ready. The behavior fails closed rather than silently discarding history, which bounds severity to MEDIUM.

**Required closure evidence:**  
Define a receipt corruption/quarantine protocol, surface corruption in doctor, preserve trustworthy prior evidence, provide explicit recovery/rebuild semantics, and add deterministic malformed/truncated receipt tests.

---

### WSA-2026-057 - MCP provider errors can persist or print unredacted sensitive content through Connections receipts and CLI diagnostics

**Severity:** MEDIUM  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A4.4  
**Root area:** provider-error diagnostics / receipt minimization / secret-at-rest boundary  
**Affected repo:** AI-Verse-Connections

**Summary:**  
Connections normally keeps credentials behind opaque handles and minimizes normal effect receipts, but the MCP JSON-RPC error path accepts provider-controlled error text/details without sanitization. The execution failure path persists the remote message in the append-only receipt and CLI error handling can emit the complete remote RPC error object.

**Contradiction:** C-A4.4-007.

**Primary evidence:** E-A4.4-019 through E-A4.4-024.

**Impact:**  
A malicious or compromised MCP provider can deliberately echo bearer-like or private content into provider errors, causing that content to be persisted outside the credential vault and/or emitted to terminal/JSON diagnostics and captured logs. The provider already receives its bearer, so the defect broadens persistence/exposure rather than granting the provider a new secret.

**Required closure evidence:**  
Add a provider-error sanitization/minimization boundary before receipt and CLI output, persist only safe bounded error categories/summaries, and add deterministic MCP regressions proving a bearer echoed in remote error message/data is absent from receipts, CLI output and support artifacts.

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
| `C-A1.8-001` | A1.8 | implementation defect / ACTUAL source authority bypass | yes | `WSA-2026-024` | OPEN |
| `C-A1.8-002` | A1.8 | implementation defect / pricing batch failure atomicity | yes | `WSA-2026-025` | OPEN |
| `C-A1.9-001` | A1.9 | implementation defect / canonical database ownership identity | yes | `WSA-2026-026` | OPEN |
| `C-A1.9-002` | A1.9 | implementation defect / live legacy authority fence | yes | `WSA-2026-027` | OPEN |
| `C-A1.9-003` | A1.9 | implementation defect / native lifecycle synchronization | yes | `WSA-2026-028` | OPEN |
| `C-A1.10-001` | A1.10 | implementation defect / destructive purge containment | yes | `WSA-2026-029` | OPEN |
| `C-A1.10-002` | A1.10 | implementation defect / installation system scope binding | yes | `WSA-2026-030` | OPEN |
| `C-A1.10-003` | A1.10 | implementation defect / MCP credential origin binding | yes | `WSA-2026-031` | OPEN |
| `C-A1.10-004` | A1.10 | implementation defect / final-edge lifecycle and budgets | yes | `WSA-2026-032` | OPEN |
| `C-A1.10-005` | A1.10 | implementation defect / normalized path authorization | yes | `WSA-2026-033` | OPEN |
| C-A1.12-001 | A1.12 | product/documentation requirements contradiction | yes | WSA-2026-035 | OPEN |
| C-A1.12-002 | A1.12 | implementation defect / failure-path secret redaction | yes | WSA-2026-036 | OPEN |
| C-A1.12-003 | A1.12 | stale release/status documentation | yes | WSA-2026-037 | OPEN |
| C-A1.12-004 | A1.12 | implementation defect / lifecycle concurrency | yes | WSA-2026-034 | OPEN |
| C-A1.13-001 | A1.13 | implementation defect / workspace subscription isolation | yes | WSA-2026-038 | OPEN |
| C-A1.13-002 | A1.13 | implementation defect / registered root identity binding | yes | WSA-2026-039 | OPEN |
| C-A1.13-003 | A1.13 | implementation defect / local gateway authentication | yes | WSA-2026-040 | OPEN |
| C-A1.13-004 | A1.13 | implementation defect / browser Origin policy | yes | WSA-2026-041 | OPEN |
| C-A1.13-005 | A1.13 | implementation defect / shadow projection authority | yes | WSA-2026-042 | OPEN |
| C-A1.14-001 | A1.14 | machine-contract inconsistency | yes | WSA-2026-043 | OPEN |
| C-A1.14-002 | A1.14 | meta-authority synchronization defect | yes | WSA-2026-044 | OPEN |
| C-A2.1-001 | A2.1 | cross-side idempotency enforcement contradiction | yes | WSA-2026-008 | OPEN |
| C-A2.2-001 | A2.2 | Dashboard shadow-authority contradiction | yes | WSA-2026-042 | OPEN |
| C-A2.2-002 | A2.2 | Token monetary admission contradiction | yes | WSA-2026-024 | OPEN |
| C-A2.2-003 | A2.2 | Distribution receipt/write-path contradiction | yes | WSA-2026-034 | OPEN |
| C-A2.2-004 | A2.2 | Automations owner-vs-attachment truth contradiction | yes | WSA-2026-028 | OPEN |
| C-A2.3-001 | A2.3 | Automations owner/OS discovery lifecycle divergence | yes | WSA-2026-028 | OPEN |
| C-A2.3-002 | A2.3 | legacy schedule authority fence is setup-only | yes | WSA-2026-027 | OPEN |
| C-A2.3-003 | A2.3 | owner lifecycle surface can be unsafe when invoked by Distribution | yes | WSA-2026-006 / WSA-2026-012 / WSA-2026-016 / WSA-2026-029 | OPEN |
| C-A2.3-004 | A2.3 | Distribution receipt can diverge from completed owner effects | yes | WSA-2026-034 | OPEN |
| C-A2.4-001 | A2.4 | transport authentication vs Multiple Bots operator authority | yes | WSA-2026-022 | OPEN |
| C-A2.4-002 | A2.4 | managed vs generic Worker workspace binding | yes | WSA-2026-023 | OPEN |
| C-A2.4-003 | A2.4 | trusted Data scope provenance not enforced by public client | yes | WSA-2026-020 | OPEN |
| C-A2.4-004 | A2.4 | Connections installation system identity not authoritative | yes | WSA-2026-030 | OPEN |
| C-A2.4-005 | A2.4 | Connections credential-origin binding bypass on reauth | yes | WSA-2026-031 | OPEN |
| C-A2.4-006 | A2.4 | Dashboard local projection server lacks authenticated principal | yes | WSA-2026-040 | OPEN |
| C-A2.4-007 | A2.4 | Dashboard system/workspace identity drift | yes | WSA-2026-038 / WSA-2026-039 | OPEN |
| C-A2.5-001 | A2.5 | exact-source freshness vs Gateway retrieval cache | yes | WSA-2026-045 | OPEN |
| C-A2.5-002 | A2.5 | Dashboard projection-only vs synthetic owner-like semantics | yes | WSA-2026-042 | OPEN |
| C-A2.5-003 | A2.5 | Data trusted-read scope vs forgeable provenance | yes | WSA-2026-020 | OPEN |
| C-A2.5-004 | A2.5 | Skills pinned read vs generation retention | yes | WSA-2026-018 | OPEN |
| C-A2.6-001 | A2.6 | Automations stable invocation vs Gateway concurrent admission | yes | WSA-2026-008 | OPEN |
| C-A2.6-002 | A2.6 | Gateway pause/cancel vs stale execution writer | yes | WSA-2026-008 | OPEN |
| C-A2.6-003 | A2.6 | Multiple Bots operator controls vs trusted identity | yes | WSA-2026-022 | OPEN |
| C-A2.6-004 | A2.6 | generic Worker event scope vs managed Worker scope | yes | WSA-2026-023 | OPEN |
| C-A2.6-005 | A2.6 | canonical Automations scheduler vs late legacy authority | yes | WSA-2026-027 | OPEN |
| C-A2.7-001 | A2.7 | Token ACTUAL truth vs generic actual-charge admission | yes | WSA-2026-024 | OPEN |
| C-A2.7-002 | A2.7 | failed pricing batch vs partial immutable snapshot subset | yes | WSA-2026-025 | OPEN |
| C-A2.7-003 | A2.7 | Connections current budget law vs final-edge implementation | yes | WSA-2026-032 | OPEN |
| C-A2.7-004 | A2.7 | Distribution sanitized diagnostics vs raw ProcessError message | yes | WSA-2026-036 | OPEN |
| C-A2.8-001 | A2.8 | Invisible candidate released qualification vs nested pending metadata | yes | WSA-2026-001 | OPEN |
| C-A2.8-002 | A2.8 | Agent runtime floor vs ordinary Distribution requirements | yes | WSA-2026-035 | OPEN |
| C-A2.8-003 | A2.8 | Full compatibility blocker text says Agent release is missing | yes | WSA-2026-037 | OPEN |
| C-A2.8-004 | A2.8 | System current release/meta surfaces lag accepted candidates | yes | WSA-2026-044 | OPEN |
| C-A2.8-005 | A2.8 | component current source vs immutable release identity | yes | WSA-2026-011 / WSA-2026-015 / WSA-2026-019 / WSA-2026-021 | OPEN |
| C-A2.8-006 | A2.8 | accepted member-facing Video Editor vs every Distribution release set | yes | WSA-2026-046 | OPEN |
| C-A3.1-001 | A3.1 | public Python requirement vs executable Agent requirement | yes | WSA-2026-035 | OPEN |
| C-A3.1-002 | A3.1 | sanitized failure fields vs raw ProcessError message | yes | WSA-2026-036 | OPEN |
| C-A3.1-003 | A3.1 | accepted Video Editor vs default Distribution composition | yes | WSA-2026-046 | OPEN |
| C-A3.2-001 | A3.2 | semantic migration current user journey vs stubbed owner acceptance | yes | WSA-2026-047 | OPEN |
| C-A3.2-002 | A3.2 | Memory singular-authority migration law vs non-atomic handoff | yes | WSA-2026-014 | OPEN |
| C-A3.2-003 | A3.2 | migration-required lifecycle state vs native Memory write admission | yes | WSA-2026-013 | OPEN |
| C-A3.2-004 | A3.2 | existing-system lifecycle containment vs Memory parent-symlink path | yes | WSA-2026-012 | OPEN |
| C-A3.2-005 | A3.2 | Brain native destination scope law vs symlinked parent acceptance | yes | WSA-2026-009 | OPEN |
| C-A3.3-001 | A3.3 | stable run idempotency vs concurrent first-claim race | yes | WSA-2026-008 | OPEN |
| C-A3.3-002 | A3.3 | authenticated pause/cancel vs stale asynchronous writer | yes | WSA-2026-008 | OPEN |
| C-A3.3-003 | A3.3 | lifecycle status wording vs real process ownership | yes | WSA-2026-007 | OPEN |
| C-A3.3-004 | A3.3 | exact-source freshness vs per-run deep-retrieval cache | yes | WSA-2026-045 | OPEN |
| C-A3.4-001 | A3.4 | exact-source freshness law vs per-run deep-context cache | yes | WSA-2026-045 | OPEN |
| C-A3.5-001 | A3.5 | Goal/self-learning user journey vs split acceptance evidence | yes | WSA-2026-048 | OPEN |
| C-A3.5-002 | A3.5 | Skills lifecycle serialization law vs age-only stale-lock reclaim | yes | WSA-2026-017 | OPEN |
| C-A3.5-003 | A3.5 | pinned immutable capability lifetime vs retention cleanup | yes | WSA-2026-018 | OPEN |
| C-A3.5-004 | A3.5 | Goal operation idempotency vs cross-Goal concurrent admission | yes | WSA-2026-010 | OPEN |
| C-A3.6-001 | A3.6 | sensitive operator controls vs caller actor authority | yes | WSA-2026-022 | OPEN |
| C-A3.6-002 | A3.6 | managed Worker workspace binding vs generic Worker coordination | yes | WSA-2026-023 | OPEN |
| C-A3.7-001 | A3.7 | stable invocation replay vs concurrent Gateway first-claim admission | yes | WSA-2026-008 | OPEN |
| C-A3.7-002 | A3.7 | Automations canonical store ownership vs foreign SQLite adoption | yes | WSA-2026-026 | OPEN |
| C-A3.7-003 | A3.7 | one canonical scheduler authority vs post-setup legacy definition | yes | WSA-2026-027 | OPEN |
| C-A3.7-004 | A3.7 | Automations owner lifecycle vs OS attachment state | yes | WSA-2026-028 | OPEN |
| C-A3.8-001 | A3.8 | Connections installation system identity vs connection/execution identity | yes | WSA-2026-030 | OPEN |
| C-A3.8-002 | A3.8 | MCP credential-origin isolation vs reauth | yes | WSA-2026-031 | OPEN |
| C-A3.8-003 | A3.8 | complete final-edge authority law vs partial recheck | yes | WSA-2026-032 | OPEN |
| C-A3.8-004 | A3.8 | admitted Generic API path prefix vs normalized provider path | yes | WSA-2026-033 | OPEN |
| C-A3.8-005 | A3.8 | expected hosted current-head execution vs private-repo Actions infrastructure | yes | WSA-2026-003 | OPEN |
| C-A3.9-001 | A3.9 | trusted ACTUAL law vs generic actual-charge admission | yes | WSA-2026-024 | OPEN |
| C-A3.9-002 | A3.9 | failed pricing refresh vs visible partial snapshot batch | yes | WSA-2026-025 | OPEN |
| C-A3.10-001 | A3.10 | owner-safe uninstall law vs destructive lifecycle containment | yes | WSA-2026-006 / WSA-2026-012 / WSA-2026-016 / WSA-2026-029 | OPEN |
| C-A3.10-002 | A3.10 | owner lifecycle truth vs live/attached/write authority | yes | WSA-2026-007 / WSA-2026-013 / WSA-2026-028 | OPEN |
| C-A3.10-003 | A3.10 | lifecycle/recovery serialization vs stale/concurrent writers | yes | WSA-2026-008 / WSA-2026-017 / WSA-2026-034 | OPEN |
| C-A3.10-004 | A3.10 | singular migration authority vs non-atomic Memory handoff | yes | WSA-2026-014 | OPEN |
| C-A3.10-005 | A3.10 | two-system A/B journey requirement vs one-root acceptance inventory | yes | WSA-2026-049 | OPEN |
| C-A4.1-001 | A4.1 | authenticated rate-limit claim vs pre-auth synchronous KDF work | yes | WSA-2026-050 | OPEN |
| C-A4.1-002 | A4.1 | private-network deny law vs independent DNS resolutions | yes | WSA-2026-051 | OPEN |
| C-A4.1-003 | A4.1 | owner-root confinement vs destructive/symlink path findings | yes | WSA-2026-006 / WSA-2026-009 / WSA-2026-012 / WSA-2026-016 / WSA-2026-029 / WSA-2026-033 / WSA-2026-039 | OPEN |
| C-A4.1-004 | A4.1 | authenticated/permission-bound control vs local/domain authority findings | yes | WSA-2026-020 / WSA-2026-022 / WSA-2026-023 / WSA-2026-030 / WSA-2026-032 / WSA-2026-038 / WSA-2026-040 | OPEN |
| C-A4.1-005 | A4.1 | secret boundary vs supported failure/origin paths | yes | WSA-2026-031 / WSA-2026-036 / WSA-2026-051 | OPEN |
| C-A4.2-001 | A4.2 | Gateway one-key/one-run law vs concurrent first claim | yes | WSA-2026-008 | OPEN |
| C-A4.2-002 | A4.2 | Brain operation-ID law vs cross-Goal concurrent admission | yes | WSA-2026-010 | OPEN |
| C-A4.2-003 | A4.2 | Skills single-writer lifecycle law vs live-holder stale reclaim | yes | WSA-2026-017 | OPEN |
| C-A4.2-004 | A4.2 | Token failed-refresh atomicity vs partial batch publication | yes | WSA-2026-025 | OPEN |
| C-A4.2-005 | A4.2 | Connections current-budget law vs concurrent different-key effects | yes | WSA-2026-032 | OPEN |
| C-A4.2-006 | A4.2 | Distribution one lifecycle truth vs concurrent stale receipt writers | yes | WSA-2026-034 | OPEN |
| C-A4.2-007 | A4.2 | semantic migration source-identity replay vs concurrent first imports | yes | WSA-2026-052 | OPEN |
| C-A4.2-008 | A4.2 | one structured natural-key truth vs query-then-create race | yes | WSA-2026-053 | OPEN |
| C-A4.3-001 | A4.3 | Gateway setup readiness vs failed setup publication | yes | WSA-2026-007 | OPEN |
| C-A4.3-002 | A4.3 | singular Memory authority vs partial cross-root handoff | yes | WSA-2026-014 | OPEN |
| C-A4.3-003 | A4.3 | failed Token refresh vs partial authoritative snapshot visibility | yes | WSA-2026-025 | OPEN |
| C-A4.3-004 | A4.3 | Automations canonical store identity vs mutation-before-ownership proof | yes | WSA-2026-026 | OPEN |
| C-A4.3-005 | A4.3 | Distribution lifecycle truth vs owner effect before receipt commit | yes | WSA-2026-034 | OPEN |
| C-A4.3-006 | A4.3 | serialized Connections state vs crash-orphaned lock | yes | WSA-2026-054 | OPEN |
| C-A4.3-007 | A4.3 | idempotent external effect vs permanent pending crash uncertainty | yes | WSA-2026-055 | OPEN |
| C-A4.3-008 | A4.3 | Connections ready/healthy projection vs unreadable receipt state | yes | WSA-2026-056 | OPEN |
| C-A4.3-009 | A4.3 | source-level migration replay vs crash before final source receipt | yes | WSA-2026-052 | OPEN |
| C-A4.4-001 | A4.4 | Memory exact-source provenance vs cross-scope probing | no | none | VERIFIED |
| C-A4.4-002 | A4.4 | Token privacy-safe projection vs explicit raw provenance export | no | none | VERIFIED / EXPLICIT OPT-IN |
| C-A4.4-003 | A4.4 | selected Dashboard workspace vs retained old realtime subscription | yes | WSA-2026-038 | OPEN |
| C-A4.4-004 | A4.4 | Dashboard local projection privacy vs unauthenticated loopback reads | yes | WSA-2026-040 | OPEN |
| C-A4.4-005 | A4.4 | trusted Data scope provenance vs structural public scope | yes | WSA-2026-020 | OPEN |
| C-A4.4-006 | A4.4 | Distribution sanitized diagnostics vs raw exception message | yes | WSA-2026-036 | OPEN |
| C-A4.4-007 | A4.4 | Connections opaque credential/receipt minimization vs raw provider-error propagation | yes | WSA-2026-057 | OPEN |

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

### C-A1.8-001

**Source A:** Token truth/collector contracts require trusted provider/runtime evidence for ACTUAL and say collectors do not gain pricing truth.  
**Source B:** protocol validation and generic collector/ledger ingest accept a pre-attached actual charge without trusted actual-source registry proof.  
**Source C:** cost engine promotes attached actual charge to ACTUAL before calculation.  
**Higher-authority source:** executable protocol, collector, ledger and cost implementation.  
**Finding:** `WSA-2026-024`.

### C-A1.8-002

**Source A:** pricing synchronization describes one updated response as storing its immutable snapshots plus source-check observation and failed refreshes as preserving prior successful state.  
**Source B:** snapshot batch persistence writes individual files sequentially with no batch transaction/staging visibility barrier.  
**Higher-authority source:** executable pricing store/synchronizer.  
**Finding:** `WSA-2026-025`.

### C-A1.9-001

**Source A:** Automations architecture defines SQLite as the component-owned canonical scheduler store.  
**Source B:** database initialization opens any selected `automations.db`, creates/alters tables and stamps metadata without proving Automations ownership or compatible format.  
**Source C:** health checks generic SQLite integrity rather than exact Automations schema identity.  
**Higher-authority source:** executable database/lifecycle implementation.  
**Finding:** `WSA-2026-026`.

### C-A1.9-002

**Source A:** README states discovered legacy OS automation definitions require migration and keep execution disabled to prevent competing authorities.  
**Source B:** live legacy discovery after setup is doctor-only; status and Engine execution use stored migration flags and can remain ready/active.  
**Higher-authority source:** executable lifecycle/engine implementation.  
**Finding:** `WSA-2026-027`.

### C-A1.9-003

**Source A:** public lifecycle includes enable/disable/uninstall and README describes uninstall/detach with canonical state preservation.  
**Source B:** attached OS registry/files are not synchronized or detached by those component lifecycle commands.  
**Higher-authority source:** executable lifecycle and OS-extension implementation.  
**Finding:** `WSA-2026-028`.

### C-A1.10-001

**Source A:** Connections exposes destructive purge as a lifecycle command.  
**Source B:** configured home is arbitrary and purge recursively force-removes that whole path without ownership validation.  
**Higher-authority source:** executable lifecycle/state-store implementation.  
**Finding:** `WSA-2026-029`.

### C-A1.10-002

**Source A:** setup claims to bind one installation to an explicit AI-Verse system.  
**Source B:** connection creation/execution trusts each connection's independently supplied system ID and does not intersect it with lifecycle system ID.  
**Higher-authority source:** executable lifecycle/registry/policy/execute implementation.  
**Finding:** `WSA-2026-030`.

### C-A1.10-003

**Source A:** MCP security/research contract forbids bearer token passthrough and cross-origin credential-handle reuse.  
**Source B:** initial add enforces this rule, while reauth replaces the handle without cross-origin validation and verify subsequently transmits it.  
**Higher-authority source:** executable registry/admission/MCP adapter.  
**Finding:** `WSA-2026-031`.

### C-A1.10-004

**Source A:** security contract says component lifecycle and current call budgets are part of the authority intersection recalculated at the final provider edge.  
**Source B:** execute checks lifecycle/budgets only before planning and final-edge code reloads only connection/capability state.  
**Higher-authority source:** executable execution/policy implementation.  
**Finding:** `WSA-2026-032`.

### C-A1.10-005

**Source A:** Generic API security contract claims explicit path-prefix admission.  
**Source B:** raw path is prefix-checked before URL normalization and normalized pathname is not rechecked.  
**Runtime proof:** `/v1/%2e%2e/admin` normalizes to `/admin` under Node WHATWG URL handling.  
**Higher-authority source:** executable Generic API adapter plus required runtime semantics.  
**Finding:** `WSA-2026-033`.


### C-A1.12-001

**Source A:** README says the released Agent beta requires Python 3.9+.  
**Source B:** package metadata permits Python >=3.9.  
**Source C:** machine Agent compatibility requires Python 3.11.  
**Source D:** executable preflight enforces the machine release floor.  
**Higher-authority source:** compatibility plus executable preflight.  
**Finding:** WSA-2026-035.

### C-A1.12-002

**Source A:** diagnostic/support behavior claims sensitive output is redacted.  
**Source B:** explicit stdout/stderr fields are sanitized.  
**Source C:** ProcessError embeds raw child output and CLI emits raw str(exc) as message.  
**Higher-authority source:** executable process/CLI implementation.  
**Finding:** WSA-2026-036.

### C-A1.12-003

**Source A:** current release catalog and README say Agent is released.  
**Source B:** current architecture says Agent is modeled but blocked.  
**Source C:** current roadmap still leaves the release-branch merge incomplete.  
**Higher-authority source:** current machine-readable catalog plus implementation/history.  
**Finding:** WSA-2026-037.

### C-A1.12-004

**Source A:** Distribution lock is described as recoverable release/install truth.  
**Source B:** StateStore only guarantees atomic individual file replacement.  
**Source C:** mutating lifecycle paths perform load -> owner effect -> stale-capable receipt write with no cross-process lock/CAS/version.  
**Higher-authority source:** executable state/orchestrator implementation.  
**Finding:** WSA-2026-034.


### C-A1.13-001

**Source A:** Dashboard architecture requires workspace-scoped subscriptions and no context leakage across workspace switches.  
**Source B:** WebSocket resubscribe creates a new hub subscription without removing the previous one.  
**Higher-authority source:** executable server and SubscriptionHub.  
**Finding:** WSA-2026-038.

### C-A1.13-002

**Source A:** systemId is documented as one explicitly approved OS identity boundary.  
**Source B:** implementation stores only a pathname and later follows the current filesystem target at that path.  
**Higher-authority source:** executable registry/path resolver.  
**Finding:** WSA-2026-039.

### C-A1.13-003

**Source A:** architecture defines a local authenticated control/read gateway.  
**Source B:** current Dashboard-local server authenticates neither HTTP nor WebSocket clients and accepts missing Origin.  
**Higher-authority source:** executable server.  
**Finding:** WSA-2026-040.

### C-A1.13-004

**Source A:** architecture expects a separate local browser/Vite UI consuming the Gateway.  
**Source B:** Origin comparison rejects loopback origins containing explicit ports.  
**Higher-authority source:** executable server.  
**Finding:** WSA-2026-041.

### C-A1.13-005

**Source A:** Dashboard owns zero domain truth.  
**Source B:** current read models create health/inbox classifications from generic files and filenames.  
**Source C:** current preservation report explicitly calls this shadow-authority risk.  
**Higher-authority source:** executable read models.  
**Finding:** WSA-2026-042.


### C-A1.14-001

**Source A:** Whole-Release Preservation JSON Schema requires only kind/status/revision in an evidence item and defines run_id/job_id/url as optional.  
**Source B:** contract prose says evidence may include those metadata fields.  
**Source C:** semantic validator requires all six keys exactly.  
**Higher-authority resolution:** unresolved inside the canonical contract surfaces; repair must align them.  
**Finding:** WSA-2026-043.

### C-A1.14-002

**Source A:** Living Specification Protocol requires accepted changes to update current component and system records.  
**Source B:** Context Ladder is 25/25 accepted with an immutable candidate and accepted OS/Brain/Memory/Gateway refs.  
**Source C:** Public Beta Tracker, Blueprint and multiple component records remain at older current-state/release evidence.  
**Source D:** Gateway lacks the standard first-class System component record, while Token current-state surfaces also disagree.  
**Higher-authority source:** exact accepted owner/release evidence plus the completed project plans.  
**Finding:** WSA-2026-044.

### C-A2.1-001

**Source A:** Automations supplies one stable `invocation_id` and defines it as the downstream idempotency key for Gateway delivery.  
**Source B:** Gateway accepts Automation wake ingress and maps it into run creation.  
**Source C:** Gateway concurrent first-claim idempotency admission is not linearizable; two simultaneous first claims can both become new runs.  
**Higher-authority source:** executable Automations/Gateway implementation already captured in A1.2 and A1.9.  
**Finding:** existing `WSA-2026-008`. No duplicate finding opened.

### C-A2.2-001

**Source A:** Dashboard is projection/presentation only and must not own canonical domain truth.  
**Source B:** current Dashboard Health/Inbox read models synthesize owner-like semantics from generic filesystem observations.  
**Finding:** existing `WSA-2026-042`.

### C-A2.2-002

**Source A:** Token is the sole canonical normalized telemetry/pricing/cost owner and ACTUAL requires trusted monetary evidence.  
**Source B:** generic collector/direct ingest may supply syntactically valid actual_charge without mandatory trusted-source proof.  
**Finding:** existing `WSA-2026-024`.

### C-A2.2-003

**Source A:** Distribution receipt is release/install truth and owner live state remains authoritative.  
**Source B:** concurrent Distribution lifecycle operations can commit stale receipt snapshots after different owner effects complete.  
**Finding:** existing `WSA-2026-034`.

### C-A2.2-004

**Source A:** Automations owns schedule truth while OS extension registry is attachment metadata only.  
**Source B:** component lifecycle can diverge from the attached OS registry state.  
**Finding:** existing `WSA-2026-028`.

### C-A2.3-001

**Source A:** OS registry is attachment/discovery metadata and Automations owns schedule execution truth.  
**Source B:** Automations enable/disable/uninstall does not synchronize the OS extension entry.  
**Finding:** existing `WSA-2026-028`.

### C-A2.3-002

**Source A:** Automations forbids dual legacy/canonical scheduler authority.  
**Source B:** legacy conflict is enforced during setup but a later legacy definition does not continuously fence readiness/execution.  
**Finding:** existing `WSA-2026-027`.

### C-A2.3-003

**Source A:** Distribution correctly delegates lifecycle mutations to component owners.  
**Source B:** Gateway, Memory, Skills and Connections each have existing destructive lifecycle containment defects on supported or future-admitted owner surfaces.  
**Findings:** existing `WSA-2026-006`, `WSA-2026-012`, `WSA-2026-016`, `WSA-2026-029`.

### C-A2.3-004

**Source A:** Distribution coordinates owner effects and stores release/install receipt truth.  
**Source B:** concurrent mutating Distribution commands can commit stale receipt snapshots after owner effects complete.  
**Finding:** existing `WSA-2026-034`.

### C-A2.4-001

**Source A:** Gateway/Tailscale bearer authentication proves transport access only.  
**Source B:** Multiple Bots sensitive operator controls authorize caller-supplied actor identity rather than trusted authenticated operator identity.  
**Finding:** existing `WSA-2026-022`.

### C-A2.4-002

**Source A:** managed Team Run Workers are bound to Task/run/workspace and leases.  
**Source B:** generic Worker paths do not preserve equivalent pre-persistence workspace binding.  
**Finding:** existing `WSA-2026-023`.

### C-A2.4-003

**Source A:** Data public-client contract requires TrustedDataRoot-derived scope.  
**Source B:** exported structural DataDatabaseScope can be forged without trusted-root provenance.  
**Finding:** existing `WSA-2026-020`.

### C-A2.4-004

**Source A:** Connections setup binds one installation system ID.  
**Source B:** canonical connection/execution state can use another system ID.  
**Finding:** existing `WSA-2026-030`.

### C-A2.4-005

**Source A:** MCP bearer credentials are origin scoped and cross-origin reuse is blocked on add.  
**Source B:** reauth can replace a credential handle without the same origin-binding check.  
**Finding:** existing `WSA-2026-031`.

### C-A2.4-006

**Source A:** Dashboard architecture calls for an authenticated local control/read gateway.  
**Source B:** current scratch Dashboard Gateway accepts unauthenticated local read clients.  
**Finding:** existing `WSA-2026-040`.

### C-A2.4-007

**Source A:** Dashboard systemId/workspaceId are intended stable authority/context boundaries.  
**Source B:** registered root replacement can rebind a systemId and WebSocket resubscribe can retain the prior workspace listener.  
**Findings:** existing `WSA-2026-038`, `WSA-2026-039`.

### C-A2.5-001

**Source A:** Memory exact-source retrieval revalidates current source version and fails stale.  
**Source B:** Gateway external exact fallback revalidates source fingerprint and fails stale.  
**Source C:** Gateway repeated deep-context request cache returns the prior result without owner/fingerprint revalidation.  
**Finding:** new `WSA-2026-045`.

### C-A2.5-002

**Source A:** Dashboard is projection-only.  
**Source B:** current Health/Inbox read models synthesize owner-like semantics.  
**Finding:** existing `WSA-2026-042`.

### C-A2.5-003

**Source A:** Data native reads require TrustedDataRoot-derived scope.  
**Source B:** public client accepts structurally forgeable scope provenance.  
**Finding:** existing `WSA-2026-020`.

### C-A2.5-004

**Source A:** Skills execution pins an immutable generation.  
**Source B:** retention can remove a generation while a live execution still relies on it.  
**Finding:** existing `WSA-2026-018`.

### C-A2.6-001

**Source A:** Automations supplies stable invocation identity and reuses it on retry.  
**Source B:** Gateway concurrent first-claim idempotency admission can create duplicate runs.  
**Finding:** existing `WSA-2026-008`.

### C-A2.6-002

**Source A:** pause/cancel are authenticated privileged Gateway controls.  
**Source B:** asynchronous stale execution state can overwrite a newer persisted pause/cancel.  
**Finding:** existing `WSA-2026-008`.

### C-A2.6-003

**Source A:** Multiple Bots transport authentication is not domain authority.  
**Source B:** sensitive operator controls authorize caller-supplied actor identity.  
**Finding:** existing `WSA-2026-022`.

### C-A2.6-004

**Source A:** managed Worker execution is tightly workspace-bound.  
**Source B:** generic Worker delegation/message paths can persist cross-workspace state before rejection.  
**Finding:** existing `WSA-2026-023`.

### C-A2.6-005

**Source A:** Automations forbids dual scheduler authority.  
**Source B:** a legacy definition appearing after setup does not continuously fence canonical scheduler execution.  
**Finding:** existing `WSA-2026-027`.

### C-A2.7-001

**Source A:** Token defines ACTUAL as trusted provider/runtime real-charge truth.  
**Source B:** generic ingest can submit syntactically valid actual_charge without mandatory trusted-source-registry proof.  
**Finding:** existing `WSA-2026-024`.

### C-A2.7-002

**Source A:** pricing refresh is one source observation whose accepted snapshots should be coherent.  
**Source B:** sequential immutable snapshot writes can leave an earlier subset committed when a later write fails.  
**Finding:** existing `WSA-2026-025`.

### C-A2.7-003

**Source A:** Connections final authority includes current component lifecycle and rate/call budget.  
**Source B:** final provider edge does not recompute the complete lifecycle/budget intersection.  
**Finding:** existing `WSA-2026-032`.

### C-A2.7-004

**Source A:** Distribution sanitizes child stdout/stderr for user-facing diagnostics.  
**Source B:** ProcessError can embed the raw child output in the unsanitized top-level message.  
**Finding:** existing `WSA-2026-036`.

### C-A2.8-001

**Source A:** Invisible Intelligence candidate is an explicitly installable released candidate with later qualification evidence.  
**Source B:** nested Distribution acceptance metadata still says qualification-pending.  
**Finding:** existing `WSA-2026-001`.

### C-A2.8-002

**Source A:** Agent compatibility and executable preflight require Python 3.11 and Node 22.5.  
**Source B:** ordinary Distribution README says Python 3.9+ and Node 22+.  
**Finding:** existing `WSA-2026-035`.

### C-A2.8-003

**Source A:** Agent public beta is already an admitted immutable released set.  
**Source B:** Full compatibility blocker text still says Agent lacks an admitted immutable release set.  
**Finding:** existing `WSA-2026-037`.

### C-A2.8-004

**Source A:** later candidate/component release evidence is accepted.  
**Source B:** System current release/meta surfaces do not consistently reflect those accepted states.  
**Finding:** existing `WSA-2026-044`.

### C-A2.8-005

**Source A:** several frozen current component trees are newer than their component-level immutable release identity surfaces.  
**Source B:** version/bootstrap/descriptor surfaces still name older accepted artifacts.  
**Findings:** existing `WSA-2026-011`, `WSA-2026-015`, `WSA-2026-019`, `WSA-2026-021`.

### C-A2.8-006

**Source A:** Video Editor is a 100% complete canonical Skills release and member-facing capability at `8c321c...`.  
**Source B:** every admitted Distribution release set pins an older Skills ref; newest candidate uses `71264af6...`.  
**Source C:** exact Video Editor package is absent at `71264af6...` and present at `8c321c...`.  
**Finding:** new `WSA-2026-046`.

### C-A3.1-001

**Source A:** ordinary Distribution prerequisites state Python 3.9+.  
**Source B:** executable Agent compatibility/preflight requires Python 3.11.  
**Finding:** existing `WSA-2026-035`.

### C-A3.1-002

**Source A:** explicit child stdout/stderr fields are sanitized.  
**Source B:** ProcessError string can retain raw child output in the top-level CLI message.  
**Finding:** existing `WSA-2026-036`.

### C-A3.1-003

**Source A:** Video Editor is accepted/member-facing at current Skills head.  
**Source B:** the ordinary Distribution Agent path contains older Skills refs.  
**Finding:** existing `WSA-2026-046`.

### C-A3.2-001

**Source A:** semantic migration-drop is current user-facing behavior and OS hosted QC passes.  
**Source B:** OS migration tests stub workspace/Memory/Data owner calls and Gateway tests use migration fixtures.  
**Source C:** reviewed Distribution cross-owner acceptance does not execute semantic migration through real sibling owners.  
**Finding:** new `WSA-2026-047`.

### C-A3.2-002

**Source A:** Memory migration law requires singular writable authority after handoff.  
**Source B:** target complete is published before durable source/writer retirement with no cross-root transaction journal.  
**Finding:** existing `WSA-2026-014`.

### C-A3.2-003

**Source A:** migration-required state is intended to block normal canonical writes.  
**Source B:** native Memory mutation does not enforce lifecycle attachment/enable/setup/migration state.  
**Finding:** existing `WSA-2026-013`.

### C-A3.2-004

**Source A:** existing-system lifecycle must stay physically inside the selected AI-Verse root.  
**Source B:** Memory lifecycle parent symlinks can redirect supported writes/deletes outside it.  
**Finding:** existing `WSA-2026-012`.

### C-A3.2-005

**Source A:** Brain adoption must stay inside the selected native root/scope.  
**Source B:** native destination parent containment is incomplete.  
**Finding:** existing `WSA-2026-009`.

### C-A3.3-001

**Source A:** client retry/idempotency contract says one key binds one request.  
**Source B:** concurrent first claims can both become new runs.  
**Finding:** existing `WSA-2026-008`.

### C-A3.3-002

**Source A:** pause/cancel are authenticated privileged durable controls.  
**Source B:** stale asynchronous execution state can overwrite newer persisted pause/cancel state.  
**Finding:** existing `WSA-2026-008`.

### C-A3.3-003

**Source A:** Gateway lifecycle exposes enable/disable/status semantics.  
**Source B:** Gateway does not own a real service manager, so lifecycle state can diverge from a live process.  
**Finding:** existing `WSA-2026-007`.

### C-A3.3-004

**Source A:** exact-source reads are required to revalidate source freshness.  
**Source B:** repeated per-run deep-context cache replay can bypass a new source read.  
**Finding:** existing `WSA-2026-045`.

### C-A3.4-001

**Source A:** real J2/Memory exact-source retrieval revalidates source fingerprint/version and fails stale.  
**Source B:** Gateway per-run deep-context dedupe can replay a prior identical exact result without executing that owner/source revalidation again.  
**Finding:** existing `WSA-2026-045`.

### C-A3.5-001

**Source A:** current architecture supports Goal-bound runs plus governed Skills learning.  
**Source B:** clean-machine Goal acceptance does not exercise learning.  
**Source C:** real OS/Brain/Skills learning acceptance does not begin from a Goal-bound Gateway user run.  
**Source D:** Gateway learned-Skill user journey uses a fixture host rather than real owners.  
**Finding:** new `WSA-2026-048`.

### C-A3.5-002

**Source A:** Skills lifecycle mutation is intended to be serialized.  
**Source B:** stale lock recovery is age-based and can reclaim a live long-running holder.  
**Finding:** existing `WSA-2026-017`.

### C-A3.5-003

**Source A:** a capability execution pins one immutable generation for its lifetime.  
**Source B:** explicit retention can remove a generation without accounting for live execution pins.  
**Finding:** existing `WSA-2026-018`.

### C-A3.5-004

**Source A:** Brain Goal operation IDs are intended to bind replay.  
**Source B:** cross-Goal concurrent operation-ID admission is not fully serialized.  
**Finding:** existing `WSA-2026-010`.

### C-A3.6-001

**Source A:** sensitive Multiple Bots operator controls require trusted operator authority.  
**Source B:** caller-supplied actor identity can satisfy that authority on affected paths.  
**Finding:** existing `WSA-2026-022`.

### C-A3.6-002

**Source A:** managed Team Run Workers are strictly bound to Task/run/workspace.  
**Source B:** generic Worker delegation/message paths can cross workspace before execution rejection and can mutate the foreign Worker.  
**Finding:** existing `WSA-2026-023`.

### C-A3.7-001

**Source A:** Automations retries/replays with one stable invocation identity.  
**Source B:** Gateway simultaneous first claims can both create runs.  
**Finding:** existing `WSA-2026-008`.

### C-A3.7-002

**Source A:** Automations scheduler SQLite is canonical owner state.  
**Source B:** owner lifecycle can adopt/mutate a foreign SQLite without proving Automations ownership.  
**Finding:** existing `WSA-2026-026`.

### C-A3.7-003

**Source A:** one canonical scheduler authority is required.  
**Source B:** a legacy definition appearing after setup does not fence the active Automations scheduler.  
**Finding:** existing `WSA-2026-027`.

### C-A3.7-004

**Source A:** OS attachment metadata should reflect Automations lifecycle state.  
**Source B:** component enable/disable/uninstall and OS registration can diverge.  
**Finding:** existing `WSA-2026-028`.

### C-A3.8-001

**Source A:** Connections setup binds one installation system ID.  
**Source B:** connection registration/execution can use another system ID.  
**Finding:** existing `WSA-2026-030`.

### C-A3.8-002

**Source A:** one MCP bearer handle must remain origin-bound.  
**Source B:** reauth can assign an existing foreign-origin credential handle.  
**Finding:** existing `WSA-2026-031`.

### C-A3.8-003

**Source A:** final provider edge should recompute the complete current authority intersection.  
**Source B:** lifecycle readiness and shared budgets are not rechecked atomically at that edge.  
**Finding:** existing `WSA-2026-032`.

### C-A3.8-004

**Source A:** Generic API effect must remain within admitted path prefixes.  
**Source B:** raw-prefix checking occurs before URL normalization, allowing normalized escape.  
**Finding:** existing `WSA-2026-033`.

### C-A3.8-005

**Source A:** exact-head hosted tests are required for strong release evidence.  
**Source B:** frozen Connections Actions jobs terminate without executing steps.  
**Finding:** existing `WSA-2026-003`.

### C-A3.9-001

**Source A:** Token monetary truth requires trusted real-charge evidence for ACTUAL.  
**Source B:** generic collector/direct canonical ingest can attach syntactically valid actual_charge without mandatory trusted-source proof.  
**Finding:** existing `WSA-2026-024`.

### C-A3.9-002

**Source A:** a failed pricing refresh should not alter usable accepted pricing evidence.  
**Source B:** earlier immutable snapshots from a later-failing sequential batch can remain visible and usable.  
**Finding:** existing `WSA-2026-025`.

### C-A3.10-001

**Source A:** normal owner uninstall/reinstall is intended to preserve canonical state and remain inside owned roots.  
**Source B:** Gateway, Memory, Skills and Connections retain destructive path-containment defects.  
**Findings:** existing `WSA-2026-006`, `012`, `016`, `029`.

### C-A3.10-002

**Source A:** lifecycle status/attachment should fence runtime/write authority.  
**Source B:** Gateway live process, Memory native writes and Automations OS attachment can diverge from lifecycle state.  
**Findings:** existing `WSA-2026-007`, `013`, `028`.

### C-A3.10-003

**Source A:** lifecycle/recovery effects require one serialized truth.  
**Source B:** Gateway, Skills and Distribution retain stale/concurrent-writer races.  
**Findings:** existing `WSA-2026-008`, `017`, `034`.

### C-A3.10-004

**Source A:** Memory migration requires one writable authority after handoff.  
**Source B:** target-complete and source-retirement are not one failure-atomic transaction.  
**Finding:** existing `WSA-2026-014`.

### C-A3.10-005

**Source A:** A3.10 explicitly requires two-system A/B isolation.  
**Source B:** exhaustive Distribution product acceptance contains only one-root Agent/Core acceptance scripts.  
**Finding:** new `WSA-2026-049`.

### C-A4.1-001

**Source A:** Gateway exposes a principal-scoped request rate limiter.  
**Source B:** bearer verification performs synchronous scrypt before the limiter and invalid credentials never enter the limiter.  
**Finding:** new `WSA-2026-050`.

### C-A4.1-002

**Source A:** Connections blocks private/reserved network destinations by DNS/IP policy.  
**Source B:** policy DNS resolution and actual global fetch resolution are separate, after trusted credentials are attached.  
**Finding:** new `WSA-2026-051`.

### C-A4.1-003

Existing destructive/path confinement findings remain active across Gateway, Brain, Memory, Skills, Connections and Dashboard.  
**Findings:** `WSA-2026-006`, `009`, `012`, `016`, `029`, `033`, `039`.

### C-A4.1-004

Existing trusted-authority/isolation defects remain active in Data, Multiple Bots, Connections and Dashboard.  
**Findings:** `WSA-2026-020`, `022`, `023`, `030`, `032`, `038`, `040`.

### C-A4.1-005

Existing credential/failure-path findings remain active alongside the new DNS-rebinding path.  
**Findings:** `WSA-2026-031`, `036`, `051`.

### C-A4.2-001

**Finding:** existing `WSA-2026-008`.

### C-A4.2-002

**Finding:** existing `WSA-2026-010`.

### C-A4.2-003

**Finding:** existing `WSA-2026-017`.

### C-A4.2-004

**Finding:** existing `WSA-2026-025`.

### C-A4.2-005

**Finding:** existing `WSA-2026-032`.

### C-A4.2-006

**Finding:** existing `WSA-2026-034`.

### C-A4.2-007

**Source A:** migration source identity is intended to suppress re-execution under classifier-plan variation.  
**Source B:** the same-source check is not reserved/serialized before owner effects, and subaction keys differ by plan-derived import key.  
**Finding:** new `WSA-2026-052`.

### C-A4.2-008

**Source A:** automatic structured truth expects one canonical record for one natural key.  
**Source B:** OS query-before-create plus candidate-specific idempotency and generated record IDs allow concurrent duplicate natural-key rows.  
**Finding:** new `WSA-2026-053`.


### C-A4.3-001

**Finding:** existing `WSA-2026-007`.

### C-A4.3-002

**Finding:** existing `WSA-2026-014`.

### C-A4.3-003

**Finding:** existing `WSA-2026-025`.

### C-A4.3-004

**Finding:** existing `WSA-2026-026`.

### C-A4.3-005

**Finding:** existing `WSA-2026-034`.

### C-A4.3-006

**Source A:** Connections canonical state mutations are intended to serialize through one write lock.  
**Source B:** the directory lock has no crashed-holder recovery and survives process termination.  
**Finding:** new `WSA-2026-054`.

### C-A4.3-007

**Source A:** a pre-effect pending receipt is intended to make an external-effect idempotency key replay-safe.  
**Source B:** process death after provider-edge entry has no durable unknown-effect transition and leaves the key permanently pending.  
**Finding:** new `WSA-2026-055`.

### C-A4.3-008

**Source A:** Connections status/doctor can project ready/healthy from lifecycle, registry, credential and live-verification checks.  
**Source B:** one malformed receipt line can make execution receipt reads fail, and doctor does not inspect the receipt store.  
**Finding:** new `WSA-2026-056`.

### C-A4.3-009

**Finding:** existing `WSA-2026-052`.

### C-A4.4-001

Memory progressive exact-source descent revalidates the evidence scope against current allowed scopes before serving canonical content.  
**Finding:** none.

### C-A4.4-002

Token normal projections remove sensitive provenance identifiers, while raw provenance export is explicit opt-in behind the read authorization boundary.  
**Finding:** none.

### C-A4.4-003

**Finding:** existing `WSA-2026-038`.

### C-A4.4-004

**Finding:** existing `WSA-2026-040`.

### C-A4.4-005

**Finding:** existing `WSA-2026-020`.

### C-A4.4-006

**Finding:** existing `WSA-2026-036`.

### C-A4.4-007

**Source A:** Connections keeps credentials behind opaque handles, minimizes normal terminal effect receipts and proves the ordinary Generic API bearer does not persist in registry/receipt state.  
**Source B:** MCP provider error message/details cross the adapter unsanitized; the message is persisted in a terminal failure receipt and the full RPC error object can be emitted by CLI diagnostics.  
**Finding:** new `WSA-2026-057`.

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

### A1.8 evidence IDs

| Evidence ID | Short description | Canonical source packet |
|---|---|---|
| `E-A1.8-001` | frozen Token tree/repository metadata | `repos/ai-verse-token.md` |
| `E-A1.8-002` | README/package/provenance identity | same |
| `E-A1.8-003` | architecture/ownership reconstruction | same |
| `E-A1.8-004` | usage protocol and validation | same |
| `E-A1.8-005` | immutable ledger schema/triggers | same |
| `E-A1.8-006` | ingest/dedupe/checkpoint transaction | same |
| `E-A1.8-007` | collector SDK/runner enforcement | same |
| `E-A1.8-008` | actual-cost registry/trusted sources | same |
| `E-A1.8-009` | provider/Hermes actual-cost adapters | same |
| `E-A1.8-010` | ACTUAL/CALCULATED/UNKNOWN cost engine | same |
| `E-A1.8-011` | pricing source registry/source assessment | same |
| `E-A1.8-012` | pricing synchronizer source stamping/freshness | same |
| `E-A1.8-013` | immutable pricing store/batch writes | same |
| `E-A1.8-014` | identity resolver exact-match behavior | same |
| `E-A1.8-015` | read authorization/filter floor | same |
| `E-A1.8-016` | privacy-safe read/export/MCP | same |
| `E-A1.8-017` | native filesystem/registry/lifecycle | same |
| `E-A1.8-018` | runtime setup/doctor behavior | same |
| `E-A1.8-019` | hardening audit provenance | same |
| `E-A1.8-020` | exact-head CI run 34778240376 | same |
| `E-A1.8-021` | six exact-head successful jobs | same |
| `E-A1.8-022` | packed release acceptance | same |
| `E-A1.8-023` | alpha.1/beta.1/beta.2 tag lineage | same |
| `E-A1.8-024` | beta.3 current-head provenance/version | same |
| `E-A1.8-025` | live pre-write ref/open-PR recheck | same |

### A1.9 evidence IDs

| Evidence ID | Short description | Canonical source packet |
|---|---|---|
| `E-A1.9-001` | frozen Automations tree/repository metadata | `repos/AI-Verse-Automations.md` |
| `E-A1.9-002` | README/manifest/package ownership identity | same |
| `E-A1.9-003` | architecture/owner contract | same |
| `E-A1.9-004` | schedule parser/DST/misfire behavior | same |
| `E-A1.9-005` | canonical SQLite schema | same |
| `E-A1.9-006` | database initialize/connect/integrity implementation | same |
| `E-A1.9-007` | automation/trigger store validation | same |
| `E-A1.9-008` | atomic definition creation/idempotency | same |
| `E-A1.9-009` | due-claim transactional concurrency | same |
| `E-A1.9-010` | definition/version kill fences | same |
| `E-A1.9-011` | OS permission binding/retry reauthorization | same |
| `E-A1.9-012` | crash recovery/unknown retry | same |
| `E-A1.9-013` | event replay/source/type binding | same |
| `E-A1.9-014` | webhook HMAC/replay window | same |
| `E-A1.9-015` | target credential/network validation | same |
| `E-A1.9-016` | Brain owner adapter | same |
| `E-A1.9-017` | Multiple Bots projection/payload | same |
| `E-A1.9-018` | Gateway owner adapter/stable envelope | same |
| `E-A1.9-019` | setup/status/doctor/enable/disable/update/uninstall | same |
| `E-A1.9-020` | live legacy-definition discovery | same |
| `E-A1.9-021` | OS extension registry/owner bridge | same |
| `E-A1.9-022` | OS extension attachment tests | same |
| `E-A1.9-023` | exact-head CI run 34875408692 | same |
| `E-A1.9-024` | nine exact-head successful CI jobs | same |
| `E-A1.9-025` | accepted marker to current 10-commit comparison | same |
| `E-A1.9-026` | live pre-write ref/open-PR recheck | same |

### A1.10 evidence IDs

| Evidence ID | Short description | Canonical source packet |
|---|---|---|
| `E-A1.10-001` | frozen Connections tree/repository metadata | `repos/AI-Verse-Connections.md` |
| `E-A1.10-002` | README/component/package ownership identity | same |
| `E-A1.10-003` | security/research trust and final-edge laws | same |
| `E-A1.10-004` | credential manager/vault implementation | same |
| `E-A1.10-005` | canonical state-store/lifecycle implementation | same |
| `E-A1.10-006` | generic connection registration/verification | same |
| `E-A1.10-007` | MCP registration/origin credential reuse guard | same |
| `E-A1.10-008` | capability admission/connection approval | same |
| `E-A1.10-009` | revoke/reauth implementation | same |
| `E-A1.10-010` | system/workspace/delegated policy | same |
| `E-A1.10-011` | final-edge execution/idempotency/receipts | same |
| `E-A1.10-012` | rate/call budget implementation | same |
| `E-A1.10-013` | generic API path/header policy | same |
| `E-A1.10-014` | MCP discovery/execution adapter | same |
| `E-A1.10-015` | bounded HTTP/network controls | same |
| `E-A1.10-016` | repository-local core integration tests | same |
| `E-A1.10-017` | repository-local limits integration tests | same |
| `E-A1.10-018` | repository-local MCP/idempotency tests | same |
| `E-A1.10-019` | Node URL encoded-dot-segment normalization reproduction | same |
| `E-A1.10-020` | exact-head CI run 34775251071 | same |
| `E-A1.10-021` | six exact-head no-step hosted jobs | same |
| `E-A1.10-022` | implementation/founding commit history | same |
| `E-A1.10-023` | live pre-write ref/open-PR recheck | same |


### A1.11 evidence IDs

| Evidence ID | Short description | Canonical source packet |
|---|---|---|
| `E-A1.11-001` | frozen Apps repository metadata/head/history | `repos/AI-Verse-Apps.md` |
| `E-A1.11-002` | exact one-file tracked-tree reconstruction | same |
| `E-A1.11-003` | README product identity / research-seed status | same |
| `E-A1.11-004` | intended ownership and non-ownership boundaries | same |
| `E-A1.11-005` | planned lifecycle and trust model | same |
| `E-A1.11-006` | planned security and multi-system isolation laws | same |
| `E-A1.11-007` | outbound sibling relationship claims | same |
| `E-A1.11-008` | research/inspiration provenance | same |
| `E-A1.11-009` | negative-space proof: no executable/package/test/CI surface | same |
| `E-A1.11-010` | current-head combined status with no contexts | same |
| `E-A1.11-011` | A0 snapshot Full-profile/research-seed classification | same |
| `E-A1.11-012` | live pre-write head/open-PR recheck | same |

A1.11 opened no finding IDs. The next unused finding ID remains `WSA-2026-034`.


### A1.12 evidence IDs

| Evidence ID | Short description | Canonical source packet |
|---|---|---|
| E-A1.12-001 | frozen Distribution repository metadata/head/open-PR state | repos/ai-verse-distribution.md |
| E-A1.12-002 | merged PR history and canonical file inventory | same |
| E-A1.12-003 | README/package/version/product identity | same |
| E-A1.12-004 | architecture and release-set contracts | same |
| E-A1.12-005 | profiles and compatibility model | same |
| E-A1.12-006 | current immutable release manifests | same |
| E-A1.12-007 | executable catalog validation | same |
| E-A1.12-008 | StateStore receipt implementation | same |
| E-A1.12-009 | exact source and staging enforcement | same |
| E-A1.12-010 | install and incremental receipt lifecycle | same |
| E-A1.12-011 | setup/workspace/start/safe-reconcile behavior | same |
| E-A1.12-012 | owner-backed status and doctor | same |
| E-A1.12-013 | component lifecycle and update/rollback | same |
| E-A1.12-014 | trusted owner adapter revision allowlists | same |
| E-A1.12-015 | shell-false subprocess and ProcessError behavior | same |
| E-A1.12-016 | redaction and support bundle implementation | same |
| E-A1.12-017 | state/orchestrator unit tests | same |
| E-A1.12-018 | catalog/manifest mirror tests | same |
| E-A1.12-019 | CLI/bootstrap tests | same |
| E-A1.12-020 | Core clean-machine acceptance | same |
| E-A1.12-021 | Agent clean-machine acceptance | same |
| E-A1.12-022 | post-merge Distribution CI 34998241632 | same |
| E-A1.12-023 | PR #8 final-head eight-workflow acceptance matrix | same |
| E-A1.12-024 | final PR head -> merge tree zero-file-diff proof | same |
| E-A1.12-025 | immutable System contract qualification snapshot | same |
| E-A1.12-026 | history/roadmap release-status evidence | same |
| E-A1.12-027 | stale-writer lifecycle concurrency trace | same |
| E-A1.12-028 | ProcessError redaction bypass trace | same |
| E-A1.12-029 | Agent Python-floor contradiction | same |
| E-A1.12-030 | final live pre-write recheck | same |


### A1.13 evidence IDs

| Evidence ID | Short description | Canonical source packet |
|---|---|---|
| E-A1.13-001 | frozen Dashboard repository metadata/head/open-PR state | repos/AI-Verse-Dashboard.md |
| E-A1.13-002 | Dashboard commit/PR evolution | same |
| E-A1.13-003 | README ownership/isolation law | same |
| E-A1.13-004 | architecture blueprint | same |
| E-A1.13-005 | Mission Control PRD and current tracker | same |
| E-A1.13-006 | baseline preservation report | same |
| E-A1.13-007 | protocol enforcement | same |
| E-A1.13-008 | OS registry implementation | same |
| E-A1.13-009 | server-side path containment | same |
| E-A1.13-010 | Markdown/SQLite read boundaries | same |
| E-A1.13-011 | local HTTP/WebSocket Gateway server | same |
| E-A1.13-012 | loopback Origin implementation | same |
| E-A1.13-013 | WebSocket resubscribe/subscription lifecycle trace | same |
| E-A1.13-014 | query router supported reads | same |
| E-A1.13-015 | unauthenticated local read trace | same |
| E-A1.13-016 | registered root substitution trace | same |
| E-A1.13-017 | synthetic read-model semantics | same |
| E-A1.13-018 | repository shadow-authority acknowledgment | same |
| E-A1.13-019 | live session/runtime scaffolding | same |
| E-A1.13-020 | client/web shell model | same |
| E-A1.13-021 | Gateway tests and coverage gaps | same |
| E-A1.13-022 | registry/isolation tests and coverage gaps | same |
| E-A1.13-023 | Phase 1 gate | same |
| E-A1.13-024 | Mission Control MC1 automation | same |
| E-A1.13-025 | third-party provenance | same |
| E-A1.13-026 | cross-platform Dashboard CI definition | same |
| E-A1.13-027 | PR #8 runtime-proof CI 34994307940 | same |
| E-A1.13-028 | PR #10 pause-head CI 34997395259 | same |
| E-A1.13-029 | current merge-head hosted status limitation | same |
| E-A1.13-030 | final live pre-write recheck | same |


### A1.14 evidence IDs

| Evidence ID | Short description | Canonical source packet |
|---|---|---|
| E-A1.14-001 | frozen System product ref and audit-only drift classification | repos/AI-Verse-System.md |
| E-A1.14-002 | Living Specification Protocol propagation law | same |
| E-A1.14-003 | immutable Agent release evidence | same |
| E-A1.14-004 | completed Context Ladder immutable release handoff | same |
| E-A1.14-005 | incomplete propagation after Context Ladder closure | same |
| E-A1.14-006 | stale OS/Brain/Memory component authority records | same |
| E-A1.14-007 | missing first-class Gateway component record | same |
| E-A1.14-008 | Token current-state contradiction | same |
| E-A1.14-009 | Blueprint/current-state release drift | same |
| E-A1.14-010 | inherited Connections System-spec drift | same |
| E-A1.14-011 | Component Release Descriptor contract | same |
| E-A1.14-012 | Whole-Release Preservation contract | same |
| E-A1.14-013 | preservation Schema/validator mismatch | same |
| E-A1.14-014 | missing optional-evidence regression | same |
| E-A1.14-015 | private System hosted CI no-step limitation | same |
| E-A1.14-016 | external exact contract qualification 34997085576 | same |
| E-A1.14-017 | qualified contract code equals frozen contract code | same |
| E-A1.14-018 | Safe Update remains truthfully incomplete | same |

### A2.1 evidence IDs

| Evidence ID | Short description | Canonical source packet |
|---|---|---|
| E-A2.1-001 | live frozen-ref/open-PR drift recheck across all 14 repos | seams/A2.1-RELATIONSHIP-MATRIX-RESOLUTION.md |
| E-A2.1-002 | completed 14-packet A1 claim set | same |
| E-A2.1-003 | Gateway -> OS focused host-adapter check | same |
| E-A2.1-004 | Gateway -> Brain Goal-owner check | same |
| E-A2.1-005 | Gateway owner-routing policy | same |
| E-A2.1-006 | Automations owner adapters | same |
| E-A2.1-007 | Automations -> Gateway idempotency contradiction | same |
| E-A2.1-008 | Multiple Bots <-> Token ownership boundary | same |
| E-A2.1-009 | Data integration adapter boundaries | same |
| E-A2.1-010 | Connections credential/effect owner boundary | same |
| E-A2.1-011 | Dashboard projection/non-ownership boundary | same |
| E-A2.1-012 | Distribution revision-bounded owner lifecycle adapters | same |
| E-A2.1-013 | Apps plan-only/current-forbidden write boundary | same |
| E-A2.1-014 | System meta/release boundary | same |
| E-A2.1-015 | sensitive NONE pair validation | same |
| E-A2.1-016 | mechanical 182-pair / 2,184-cell matrix validation | same |

A2.1 opened no new finding ID. The next unused finding ID remains `WSA-2026-045`.

### A2.2 evidence IDs

| Evidence ID | Short description | Canonical source packet |
|---|---|---|
| E-A2.2-001 | live A2.2 ref/open-PR freeze | seams/A2.2-CANONICAL-OWNERSHIP-WRITE-PATHS.md |
| E-A2.2-002 | A2.1 resolved relationship matrix | same |
| E-A2.2-003 | OS host action and write-command boundary | same |
| E-A2.2-004 | Brain direction handover/handback and policy intersection | same |
| E-A2.2-005 | Gateway runtime action admission and non-owner negative space | same |
| E-A2.2-006 | Memory canonical/derived state and write boundary | same |
| E-A2.2-007 | Skills immutable generation owner boundary | same |
| E-A2.2-008 | Data adapters and trusted-scope write admission | same |
| E-A2.2-009 | Multiple Bots coordination and Token boundary | same |
| E-A2.2-010 | Token canonical telemetry/pricing/cost boundary | same |
| E-A2.2-011 | Automations owner bridge/adapters/projection | same |
| E-A2.2-012 | Connections final-edge effect/credential ownership | same |
| E-A2.2-013 | Dashboard read-only/shadow-semantics evidence | same |
| E-A2.2-014 | Distribution revision-bounded owner adapters | same |
| E-A2.2-015 | System vs Distribution meta/release split | same |
| E-A2.2-016 | direct cross-owner write inventory | same |
| E-A2.2-017 | duplicate-ledger/shadow-cache classification | same |
| E-A2.2-018 | Brain/model security-authority check | same |

A2.2 opened no new finding ID. The next unused finding ID remains `WSA-2026-045`.

### A2.3 evidence IDs

| Evidence ID | Short description | Canonical source packet |
|---|---|---|
| E-A2.3-001 | fresh A2.3 frozen-ref/open-PR gate | seams/A2.3-LIFECYCLE-DISCOVERY-ADOPTION-RECONCILE.md |
| E-A2.3-002 | A2.1 relationship matrix | same |
| E-A2.3-003 | A2.2 ownership/write graph | same |
| E-A2.3-004 | OS lifecycle/install-order/discovery/reconcile | same |
| E-A2.3-005 | Brain install/adopt/migrate/update/detach | same |
| E-A2.3-006 | Memory lifecycle/readiness/migration | same |
| E-A2.3-007 | Skills immutable-generation lifecycle | same |
| E-A2.3-008 | Data native lifecycle/state preservation | same |
| E-A2.3-009 | Multiple Bots bounded native lifecycle | same |
| E-A2.3-010 | Token lifecycle/state preservation | same |
| E-A2.3-011 | Automations owner/OS attachment and legacy authority | same |
| E-A2.3-012 | Connections lifecycle/preserve/purge boundary | same |
| E-A2.3-013 | Gateway lifecycle and recovery | same |
| E-A2.3-014 | Distribution lifecycle completeness and adapters | same |
| E-A2.3-015 | Dashboard registration/future lifecycle | same |
| E-A2.3-016 | Apps PLAN-ONLY lifecycle boundary | same |
| E-A2.3-017 | adoption/migration graph | same |
| E-A2.3-018 | discovery/readiness graph | same |
| E-A2.3-019 | disable/detach/uninstall preservation graph | same |
| E-A2.3-020 | update/rollback support boundary | same |
| E-A2.3-021 | restart/recovery graph | same |

A2.3 opened no new finding ID. The next unused finding ID remains `WSA-2026-045`.

### A2.4 evidence IDs

| Evidence ID | Short description | Canonical source packet |
|---|---|---|
| E-A2.4-001 | fresh A2.4 frozen-ref/open-PR gate | seams/A2.4-IDENTITY-SCOPE-ISOLATION-AUTHENTICATION.md |
| E-A2.4-002 | Gateway bearer verifier/principal derivation | same |
| E-A2.4-003 | Gateway session/run system-workspace-principal binding | same |
| E-A2.4-004 | Gateway principal-owned run controls and approval | same |
| E-A2.4-005 | Gateway trusted-field stripping and OS request construction | same |
| E-A2.4-006 | OS action-permission v1 strict scope/policy contract | same |
| E-A2.4-007 | OS workspace physical isolation/permission floor | same |
| E-A2.4-008 | Brain operator/workspace scope + host permission intersection | same |
| E-A2.4-009 | Memory workspace/operator visibility | same |
| E-A2.4-010 | Data trusted-root model + structurally forgeable scope | same |
| E-A2.4-011 | Multiple Bots managed Worker identity/scope | same |
| E-A2.4-012 | Multiple Bots transport-vs-operator authority defect | same |
| E-A2.4-013 | Token host authorization envelope/filter floor | same |
| E-A2.4-014 | Automations OS scope reauthorization + adapter identity | same |
| E-A2.4-015 | Connections delegated authority/final-edge scope model | same |
| E-A2.4-016 | Connections system/credential-origin identity defects | same |
| E-A2.4-017 | Dashboard identity/auth/isolation defects | same |
| E-A2.4-018 | Distribution non-authority identity role | same |
| E-A2.4-019 | end-to-end trust-chain synthesis | same |
| E-A2.4-020 | single-operator-model classification | same |

A2.4 opened no new finding ID. The next unused finding ID remains `WSA-2026-045`.

### A2.5 evidence IDs

| Evidence ID | Short description | Canonical source packet |
|---|---|---|
| E-A2.5-001 | fresh A2.5 frozen-ref/open-PR gate | seams/A2.5-READ-RETRIEVAL-CONTEXT-DATA-FLOWS.md |
| E-A2.5-002 | OS current-context/direction-owner read boundary | same |
| E-A2.5-003 | Gateway progressive owner-context assembly | same |
| E-A2.5-004 | Gateway context governor/fold/raw-tail preservation | same |
| E-A2.5-005 | Gateway deep-context trusted-field rejection | same |
| E-A2.5-006 | Memory progressive recall and exact-source freshness | same |
| E-A2.5-007 | Memory digest/raw-transcript authority separation | same |
| E-A2.5-008 | Gateway external exact-source visibility/fingerprint checks | same |
| E-A2.5-009 | direct Gateway deep-context cache implementation | same |
| E-A2.5-010 | test proving equivalent repeated read skips owner | same |
| E-A2.5-011 | no exact-source cache invalidation regression | same |
| E-A2.5-012 | Brain bounded retrieval/current-context semantics | same |
| E-A2.5-013 | Skills exact generation/digest read binding | same |
| E-A2.5-014 | Data bounded query/read adapters/provenance | same |
| E-A2.5-015 | Dashboard projection/path/read-model behavior | same |
| E-A2.5-016 | Apps plan-only read relationships | same |
| E-A2.5-017 | provenance truth-class synthesis | same |
| E-A2.5-018 | scope/visibility synthesis | same |

### A2.6 evidence IDs

| Evidence ID | Short description | Canonical source packet |
|---|---|---|
| E-A2.6-001 | fresh A2.6 frozen-ref/open-PR gate | seams/A2.6-RUNTIME-TASK-BOT-AUTOMATION-EVENT-FLOWS.md |
| E-A2.6-002 | Gateway run/session/event state machine | same |
| E-A2.6-003 | Gateway action/approval/control flow | same |
| E-A2.6-004 | Gateway idempotency/control concurrency defect | same |
| E-A2.6-005 | Brain Goal continuation/evaluation/action receipts | same |
| E-A2.6-006 | Automations occurrence identity/scheduler claim transaction | same |
| E-A2.6-007 | Automations permission-on-retry/crash uncertainty | same |
| E-A2.6-008 | Automations -> Gateway stable invocation contract | same |
| E-A2.6-009 | Automations -> Brain idempotency handoff | same |
| E-A2.6-010 | Multiple Bots automation wake ingress implementation | same |
| E-A2.6-011 | Multiple Bots automation replay/source-binding tests | same |
| E-A2.6-012 | Multiple Bots Task/Worker/Team Run recovery | same |
| E-A2.6-013 | Data mutation event/idempotency/receipt atomicity | same |
| E-A2.6-014 | permanent Bot consent composition | same |
| E-A2.6-015 | recurring Automation consent composition | same |
| E-A2.6-016 | restart/recovery graph | same |
| E-A2.6-017 | event ownership map | same |

A2.6 opened no new finding ID. The next unused finding ID remains `WSA-2026-046`.

### A2.7 evidence IDs

| Evidence ID | Short description | Canonical source packet |
|---|---|---|
| E-A2.7-001 | fresh A2.7 frozen-ref/open-PR gate | seams/A2.7-TELEMETRY-TOKEN-COST-AUDIT-RECEIPTS.md |
| E-A2.7-002 | Token ownership/truth model | same |
| E-A2.7-003 | immutable usage ledger/correlation semantics | same |
| E-A2.7-004 | Token runtime/provider/model identity resolution | same |
| E-A2.7-005 | trusted actual-cost source registry | same |
| E-A2.7-006 | generic ACTUAL admission bypass | same |
| E-A2.7-007 | immutable pricing/freshness/source authority | same |
| E-A2.7-008 | pricing batch failure atomicity defect | same |
| E-A2.7-009 | Token read projection privacy | same |
| E-A2.7-010 | Gateway operational usage/audit boundary | same |
| E-A2.7-011 | Multiple Bots Token non-ownership boundary | same |
| E-A2.7-012 | Brain external action receipts | same |
| E-A2.7-013 | Data mutation events/receipts | same |
| E-A2.7-014 | Skills execution receipt v2 | same |
| E-A2.7-015 | Automations wake/replay receipts | same |
| E-A2.7-016 | Connections idempotency/effect receipts | same |
| E-A2.7-017 | Connections final-edge budget contradiction | same |
| E-A2.7-018 | Distribution diagnostic redaction boundary | same |
| E-A2.7-019 | global receipt/provenance ownership map | same |

A2.7 opened no new finding ID. The next unused finding ID remains `WSA-2026-046`.

### A2.8 evidence IDs

| Evidence ID | Short description | Canonical source packet |
|---|---|---|
| E-A2.8-001 | fresh A2.8 frozen-ref/open-PR gate | seams/A2.8-VERSION-COMPATIBILITY-RELEASE-INSTALL-ORDER.md |
| E-A2.8-002 | Distribution profile definitions/dependency graph | same |
| E-A2.8-003 | Distribution compatibility matrix | same |
| E-A2.8-004 | default Agent immutable release manifest | same |
| E-A2.8-005 | Invisible Intelligence explicit candidate manifest | same |
| E-A2.8-006 | Context Ladder explicit candidate manifest | same |
| E-A2.8-007 | Full blocked manifest | same |
| E-A2.8-008 | release channel catalog | same |
| E-A2.8-009 | executable Catalog validation | same |
| E-A2.8-010 | catalog tests for defaults/candidates/custom/Full/transitions | same |
| E-A2.8-011 | A1.12 Distribution acceptance/clean-machine evidence | same |
| E-A2.8-012 | frozen current Agent refs vs Context candidate comparison | same |
| E-A2.8-013 | accepted Skills Video Editor final release evidence | same |
| E-A2.8-014 | current Skills README member-facing Video Editor claim | same |
| E-A2.8-015 | Skills compare 71264af6 -> 8c321c03, 98 commits | same |
| E-A2.8-016 | Video Editor SKILL.md absent at candidate ref, present at accepted current ref | same |
| E-A2.8-017 | Distribution runtime-floor/public-requirement contradiction | same |
| E-A2.8-018 | self-only candidate update/rollback transition enforcement | same |
| E-A2.8-019 | component release identity drift findings | same |
| E-A2.8-020 | System current release propagation drift | same |

### A3.1 evidence IDs

| Evidence ID | Short description | Canonical source packet |
|---|---|---|
| E-A3.1-001 | fresh A3.1 frozen-ref/open-PR gate | journeys/A3.1-CLEAN-INSTALL-FIRST-USE.md |
| E-A3.1-002 | current aiverse start CLI dispatch | same |
| E-A3.1-003 | Orchestrator fresh-start implementation | same |
| E-A3.1-004 | release-specific preflight/runtime enforcement | same |
| E-A3.1-005 | exact source verification/install receipts | same |
| E-A3.1-006 | owner setup ordering/composed OS reconciliation | same |
| E-A3.1-007 | product bootstrap unit tests | same |
| E-A3.1-008 | real Agent first-run acceptance assertions | same |
| E-A3.1-009 | persisted first-run/authority assertions | same |
| E-A3.1-010 | Clean Machine Agent run 34997085354 | same |
| E-A3.1-011 | Windows job 104477919264 | same |
| E-A3.1-012 | macOS job 104477921127 | same |
| E-A3.1-013 | Ubuntu job 104477975938 | same |
| E-A3.1-014 | tested final PR tree to frozen head file-equivalence | same |
| E-A3.1-015 | fail-closed first-run status/reconcile behavior | same |
| E-A3.1-016 | first-use prerequisite contradiction | same |
| E-A3.1-017 | first-use diagnostics redaction contradiction | same |
| E-A3.1-018 | accepted Video Editor composition limitation | same |

A3.1 opened no new finding ID. The next unused finding ID remains `WSA-2026-047`.

### A3.2 evidence IDs

| Evidence ID | Short description | Canonical source packet |
|---|---|---|
| E-A3.2-001 | fresh A3.2 frozen-ref/open-PR gate | journeys/A3.2-EXISTING-SYSTEM-ATTACH-ADOPT-MIGRATION.md |
| E-A3.2-002 | migration-drop current capability contract | same |
| E-A3.2-003 | direct migration-import trusted OS transport | same |
| E-A3.2-004 | OS migration owner-routing/idempotency tests | same |
| E-A3.2-005 | OS semantic clarification/resume tests | same |
| E-A3.2-006 | OS Repository QC run 34988213763 | same |
| E-A3.2-007 | OS QC job 104445713230 migration steps | same |
| E-A3.2-008 | OS migration test owner-method stubbing proof | same |
| E-A3.2-009 | Gateway migration fixture-based acceptance | same |
| E-A3.2-010 | Distribution cross-owner workflow negative-space check | same |
| E-A3.2-011 | Brain standalone-to-native adoption semantics | same |
| E-A3.2-012 | Brain destination containment defect | same |
| E-A3.2-013 | Memory snapshot-bound migration contract | same |
| E-A3.2-014 | Memory handoff ordering | same |
| E-A3.2-015 | Memory lifecycle write-authority defect | same |
| E-A3.2-016 | Memory lifecycle containment blocker | same |
| E-A3.2-017 | Memory exact-head run 34983522129 | same |
| E-A3.2-018 | Memory Ubuntu public-beta migration evidence | same |
| E-A3.2-019 | Data schema migration and restore/import safety | same |
| E-A3.2-020 | Distribution bounded existing-install safe reconcile | same |
| E-A3.2-021 | existing profile/root/release lock refusal | same |
| E-A3.2-022 | global no-data-loss/singular-authority assessment | same |

### A3.3 evidence IDs

| Evidence ID | Short description | Canonical source packet |
|---|---|---|
| E-A3.3-001 | fresh A3.3 frozen-ref/open-PR gate | journeys/A3.3-GATEWAY-CHAT-RUN-RESTART.md |
| E-A3.3-002 | Gateway auth/server request boundary | same |
| E-A3.3-003 | session/run identity binding | same |
| E-A3.3-004 | context assembly/runtime tool boundary | same |
| E-A3.3-005 | Gateway run state machine | same |
| E-A3.3-006 | Distribution real prove_gateway_goal acceptance | same |
| E-A3.3-007 | real chat completion ID/run retrieval assertions | same |
| E-A3.3-008 | real Brain Goal event/binding preservation | same |
| E-A3.3-009 | default Agent clean-machine run 34997085354 | same |
| E-A3.3-010 | default Agent hosted Gateway/restart summary | same |
| E-A3.3-011 | Context Ladder candidate clean-machine run 34994419265 | same |
| E-A3.3-012 | Context candidate Ubuntu job 104467441328 exact current Gateway evidence | same |
| E-A3.3-013 | Context candidate Windows/macOS job success | same |
| E-A3.3-014 | current Gateway exact-head CI 34992616000 | same |
| E-A3.3-015 | current restart recovery unit test | same |
| E-A3.3-016 | completed-run/digest restart separation | same |
| E-A3.3-017 | Gateway concurrency/idempotency/control defect | same |
| E-A3.3-018 | Gateway lifecycle service-truth defect | same |
| E-A3.3-019 | deep-context cache freshness limitation | same |

A3.3 opened no new finding ID. The next unused finding ID remains `WSA-2026-048`.

### A3.4 evidence IDs

| Evidence ID | Short description | Canonical source packet |
|---|---|---|
| E-A3.4-001 | fresh A3.4 frozen-ref/open-PR gate | journeys/A3.4-CONTEXT-MEMORY-CONTEXT-LADDER.md |
| E-A3.4-002 | Gateway Context Ladder Integrated Acceptance run 34990219367 | same |
| E-A3.4-003 | job 104452629493 exact current Gateway/OS/Memory composition | same |
| E-A3.4-004 | real OS Alpha/Beta workspace preparation | same |
| E-A3.4-005 | real Memory installation/index/doctor in OS | same |
| E-A3.4-006 | ordinary conversation catalog-only behavior | same |
| E-A3.4-007 | progressive catalog/summary/detail/source descent | same |
| E-A3.4-008 | exact Memory source retrieval | same |
| E-A3.4-009 | session-digest external Gateway source fallback | same |
| E-A3.4-010 | Gateway source fingerprint revalidation/stale fail-closed | same |
| E-A3.4-011 | durable-only Memory promotion | same |
| E-A3.4-012 | correction/supersession behavior | same |
| E-A3.4-013 | long-context fold plus exact recent raw tail | same |
| E-A3.4-014 | Alpha/Beta Memory and fold scope isolation | same |
| E-A3.4-015 | derived Memory rebuild preserves canonical state | same |
| E-A3.4-016 | restart preserves fold/durable context state | same |
| E-A3.4-017 | branch catalog rejection remains safe | same |
| E-A3.4-018 | exact evidence reference requirement | same |
| E-A3.4-019 | A2.5 repeated deep-context cache defect | same |

A3.4 opened no new finding ID. The next unused finding ID remains `WSA-2026-048`.

### A3.5 evidence IDs

| Evidence ID | Short description | Canonical source packet |
|---|---|---|
| E-A3.5-001 | fresh A3.5 frozen-ref/open-PR gate | journeys/A3.5-GOAL-SELF-LEARNING-SKILLS.md |
| E-A3.5-002 | Brain Goal/evaluation journey from A3.3 | same |
| E-A3.5-003 | current Brain Skills learning-candidate gate | same |
| E-A3.5-004 | Brain gate byte-equivalence between accepted and frozen current refs | same |
| E-A3.5-005 | current OS production skills.learning-candidate route | same |
| E-A3.5-006 | OS Four Repo Acceptance run 34988213651 | same |
| E-A3.5-007 | job 104445712220 real Brain/Skills owner composition | same |
| E-A3.5-008 | initial propose-mode learning + replay | same |
| E-A3.5-009 | trivial/unsafe candidate rejection | same |
| E-A3.5-010 | real auto-promotion to immutable Skills generation | same |
| E-A3.5-011 | fresh-host learned capability rediscovery/bound use | same |
| E-A3.5-012 | real Skills quarantine and rollback | same |
| E-A3.5-013 | Skills accepted-to-current changed-file comparison | same |
| E-A3.5-014 | current Skills governed-learning tests | same |
| E-A3.5-015 | Distribution Invisible Intelligence A-F run 34997085620 | same |
| E-A3.5-016 | job 104475921027 C/D learning evidence | same |
| E-A3.5-017 | Gateway learned-Skill persistence fixture proof | same |
| E-A3.5-018 | real clean-machine Goal journey does not invoke learning | same |
| E-A3.5-019 | negative-space search for one Goal-to-Skills composed acceptance | same |
| E-A3.5-020 | Skills lifecycle/retention findings affecting learned generations | same |

### A3.6 evidence IDs

| Evidence ID | Short description | Canonical source packet |
|---|---|---|
| E-A3.6-001 | fresh A3.6 frozen-ref/open-PR gate | journeys/A3.6-MULTIPLE-BOTS-TEAM-EXECUTION.md |
| E-A3.6-002 | Context candidate exact current Multiple Bots pin | same |
| E-A3.6-003 | candidate Ubuntu durable Bot collaboration/restart | same |
| E-A3.6-004 | Distribution G-M run 34997085437 | same |
| E-A3.6-005 | G-M job 104475920006 exact current Multiple Bots | same |
| E-A3.6-006 | exact-current Multiple Bots npm test, 513 passes | same |
| E-A3.6-007 | real two-durable-Bot HTTP Artifact handoff | same |
| E-A3.6-008 | real managed temporary Worker Task execution | same |
| E-A3.6-009 | Worker identity preservation | same |
| E-A3.6-010 | run-scoped automatic Worker execution/cleanup | same |
| E-A3.6-011 | Team Run aggregate/absolute budget enforcement | same |
| E-A3.6-012 | Team Run live cancellation | same |
| E-A3.6-013 | stale/restart Worker execution recovery | same |
| E-A3.6-014 | Room/Thread discussion execution/restart | same |
| E-A3.6-015 | Handoff ownership transfer/reopen | same |
| E-A3.6-016 | adaptive collaboration topology | same |
| E-A3.6-017 | verifier/disagreement resolution | same |
| E-A3.6-018 | final synthesis/idempotent settlement | same |
| E-A3.6-019 | Task Memory bounded recall/non-persistence | same |
| E-A3.6-020 | operational usage vs canonical Token boundary | same |
| E-A3.6-021 | G-M Gateway temporary Worker consent/authority boundary | same |
| E-A3.6-022 | WSA-022 operator identity defect | same |
| E-A3.6-023 | WSA-023 generic Worker workspace defect | same |

A3.6 opened no new finding ID. The next unused finding ID remains `WSA-2026-049`.

### A3.7 evidence IDs

| Evidence ID | Short description | Canonical source packet |
|---|---|---|
| E-A3.7-001 | fresh A3.7 frozen-ref/open-PR gate | journeys/A3.7-AUTOMATION-CONSENT-SCHEDULE-REPLAY.md |
| E-A3.7-002 | Gateway Automation Recommendation Boundary run 34990219479 | same |
| E-A3.7-003 | recommendation job 104452631004 no schedule/trigger | same |
| E-A3.7-004 | recurring-consent job 104452630613 | same |
| E-A3.7-005 | exact current Automations ref caaed83b in composition | same |
| E-A3.7-006 | direct consent creates one canonical Automation/trigger | same |
| E-A3.7-007 | no-consent repetition suppressed | same |
| E-A3.7-008 | actual owner run_now trigger firing | same |
| E-A3.7-009 | scheduled Gateway run completion/provenance | same |
| E-A3.7-010 | Gateway restart exact wake replay -> same run | same |
| E-A3.7-011 | changed wake replay -> HTTP 409 | same |
| E-A3.7-012 | canonical schedule/trigger provenance verification | same |
| E-A3.7-013 | OS Automation Consent run 34987737337 | same |
| E-A3.7-014 | OS job 104444093471 exact owner schedule creation | same |
| E-A3.7-015 | Distribution installed Agent Automations -> Multiple Bots wake | same |
| E-A3.7-016 | exact current Automations CI 34875408692 | same |
| E-A3.7-017 | stable retry/unknown recovery semantics | same |
| E-A3.7-018 | event/webhook replay binding | same |
| E-A3.7-019 | WSA-008 concurrent Gateway replay defect | same |
| E-A3.7-020 | WSA-026 store ownership defect | same |
| E-A3.7-021 | WSA-027 legacy dual-authority defect | same |
| E-A3.7-022 | WSA-028 OS attachment/lifecycle divergence | same |

A3.7 opened no new finding ID. The next unused finding ID remains `WSA-2026-049`.

### A3.8 evidence IDs

| Evidence ID | Short description | Canonical source packet |
|---|---|---|
| E-A3.8-001 | fresh A3.8 frozen-ref/open-PR gate | journeys/A3.8-CONNECTION-EXTERNAL-EFFECT-APPROVAL.md |
| E-A3.8-002 | Connections canonical owner/effect model | same |
| E-A3.8-003 | opaque vault credential boundary | same |
| E-A3.8-004 | core integration secret non-persistence check | same |
| E-A3.8-005 | registration/verification/admission/approval separation | same |
| E-A3.8-006 | system/workspace rejection tests | same |
| E-A3.8-007 | final-edge connection revocation test | same |
| E-A3.8-008 | Generic API provider path/credential boundary | same |
| E-A3.8-009 | MCP discovery/admission/approval/tool execution | same |
| E-A3.8-010 | MCP capability drift revokes approval | same |
| E-A3.8-011 | same-key concurrent idempotency reservation | same |
| E-A3.8-012 | terminal receipt replay without re-execution | same |
| E-A3.8-013 | rate/call limits test | same |
| E-A3.8-014 | private-network default deny | same |
| E-A3.8-015 | WSA-030 lifecycle-system binding defect | same |
| E-A3.8-016 | WSA-031 MCP credential-origin defect | same |
| E-A3.8-017 | WSA-032 final-edge lifecycle/budget defect | same |
| E-A3.8-018 | WSA-033 normalized-path authorization defect | same |
| E-A3.8-019 | WSA-029 purge blocker | same |
| E-A3.8-020 | hosted run 34775251071 no-step evidence limitation / WSA-003 | same |
| E-A3.8-021 | current Distribution release graph excludes Connections/Full | same |

A3.8 opened no new finding ID. The next unused finding ID remains `WSA-2026-049`.

### A3.9 evidence IDs

| Evidence ID | Short description | Canonical source packet |
|---|---|---|
| E-A3.9-001 | fresh A3.9 frozen-ref/open-PR gate | journeys/A3.9-TOKEN-USAGE-COST-TRUTH.md |
| E-A3.9-002 | exact current Token identity/version | same |
| E-A3.9-003 | Token exact-current CI run 34778240376 | same |
| E-A3.9-004 | six OS/Node matrix jobs execute ci/release acceptance | same |
| E-A3.9-005 | Context candidate exact Token ref | same |
| E-A3.9-006 | candidate Ubuntu token_collection_projection | same |
| E-A3.9-007 | Distribution Agent runtime-work ordering before Token collection | same |
| E-A3.9-008 | Distribution prove_token owner/no-error/projection assertions | same |
| E-A3.9-009 | collector/runtime normalization suite | same |
| E-A3.9-010 | immutable usage ledger/dedupe/correlation | same |
| E-A3.9-011 | runtime/provider/model identity | same |
| E-A3.9-012 | trusted actual-cost source tests | same |
| E-A3.9-013 | WSA-024 generic ACTUAL admission bypass | same |
| E-A3.9-014 | authoritative pricing/CALCULATED tests | same |
| E-A3.9-015 | historical effective-tariff test | same |
| E-A3.9-016 | pricing source/freshness authority | same |
| E-A3.9-017 | WSA-025 partial pricing-batch publication | same |
| E-A3.9-018 | UNKNOWN/zero/missingness tests | same |
| E-A3.9-019 | Gateway/Brain/Dashboard projection tests | same |
| E-A3.9-020 | lifecycle preservation across uninstall/reinstall | same |
| E-A3.9-021 | release story preserves ACTUAL/CALCULATED/UNKNOWN | same |
| E-A3.9-022 | privacy-safe read/transport behavior | same |

A3.9 opened no new finding ID. The next unused finding ID remains `WSA-2026-049`.

### A3.10 evidence IDs

| Evidence ID | Short description | Canonical source packet |
|---|---|---|
| E-A3.10-001 | fresh A3.10 frozen-ref/open-PR gate | journeys/A3.10-LIFECYCLE-RECOVERY-TWO-SYSTEM-ISOLATION-CROSS-PLATFORM.md |
| E-A3.10-002 | A2.3 whole-system lifecycle/recovery graph | same |
| E-A3.10-003 | Distribution real Agent lifecycle acceptance | same |
| E-A3.10-004 | Context candidate run 34994419265 | same |
| E-A3.10-005 | Ubuntu candidate job 104467441328 | same |
| E-A3.10-006 | Windows candidate job 104467441640 | same |
| E-A3.10-007 | macOS candidate job 104467441767 | same |
| E-A3.10-008 | disable/enable composed lifecycle | same |
| E-A3.10-009 | all-component uninstall/reinstall preservation | same |
| E-A3.10-010 | same-release update/rollback | same |
| E-A3.10-011 | changed cross-release transitions fail closed | same |
| E-A3.10-012 | Gateway restart/recovery | same |
| E-A3.10-013 | Memory recovery/lifecycle | same |
| E-A3.10-014 | Skills update/rollback/recovery | same |
| E-A3.10-015 | Data transaction/quarantine/recovery | same |
| E-A3.10-016 | Multiple Bots queue/lease/restart recovery | same |
| E-A3.10-017 | Automations retry/unknown recovery | same |
| E-A3.10-018 | Token lifecycle preservation | same |
| E-A3.10-019 | exact current owner cross-platform matrices | same |
| E-A3.10-020 | Distribution acceptance inventory contains exactly two scripts | same |
| E-A3.10-021 | Agent acceptance creates one root only | same |
| E-A3.10-022 | profile acceptance creates one root only | same |
| E-A3.10-023 | A2.4 component identity/isolation graph | same |
| E-A3.10-024 | destructive lifecycle BLOCKER set | same |
| E-A3.10-025 | lifecycle/concurrency/recovery HIGH findings | same |

### A4.1 evidence IDs

| Evidence ID | Short description | Canonical source packet |
|---|---|---|
| E-A4.1-001 | fresh 14-repo A4.1 freeze | adversarial/A4.1-SECURITY-PATH-SECRET-REMOTE.md |
| E-A4.1-002 | Gateway loopback/remote bind guard | same |
| E-A4.1-003 | Gateway request order, bearer before rate limiter | same |
| E-A4.1-004 | Gateway synchronous scrypt verifier | same |
| E-A4.1-005 | no pre-auth invalid-bearer limiter/test found | same |
| E-A4.1-006 | Gateway path/auth/permission A1 evidence | same |
| E-A4.1-007 | Brain symlink/permission boundary | same |
| E-A4.1-008 | Memory lifecycle/path/secret boundary | same |
| E-A4.1-009 | Skills lifecycle path boundary | same |
| E-A4.1-010 | Data trusted-scope provenance finding | same |
| E-A4.1-011 | Multiple Bots operator/Worker authority findings | same |
| E-A4.1-012 | Connections private-network screening | same |
| E-A4.1-013 | Connections shared boundedFetch implementation | same |
| E-A4.1-014 | Generic API credential-bearing fetch | same |
| E-A4.1-015 | MCP credential-bearing fetch | same |
| E-A4.1-016 | no DNS-rebinding protection/test found | same |
| E-A4.1-017 | Connections path/origin/final-edge findings | same |
| E-A4.1-018 | Distribution secret-redaction finding | same |
| E-A4.1-019 | Dashboard local-auth/root/subscription findings | same |
| E-A4.1-020 | whole-system A2.4 identity/auth graph | same |

### A4.2 evidence IDs

| Evidence ID | Short description | Canonical source packet |
|---|---|---|
| E-A4.2-001 | fresh A4.2 frozen-ref/open-PR gate | adversarial/A4.2-CONCURRENCY-IDEMPOTENCY-REPLAY.md |
| E-A4.2-002 | Gateway concurrency/idempotency WSA-008 | same |
| E-A4.2-003 | Brain Goal replay WSA-010 | same |
| E-A4.2-004 | Skills lifecycle lock WSA-017 | same |
| E-A4.2-005 | Token pricing publication WSA-025 | same |
| E-A4.2-006 | Connections final-edge budget WSA-032 | same |
| E-A4.2-007 | Distribution lifecycle receipt race WSA-034 | same |
| E-A4.2-008 | Memory canonical mutation lock/recovery | same |
| E-A4.2-009 | Automations BEGIN IMMEDIATE occurrence claim | same |
| E-A4.2-010 | Automations unique invocation/event receipt | same |
| E-A4.2-011 | Multiple Bots message idempotency/restart | same |
| E-A4.2-012 | Multiple Bots stale execution/lease recovery | same |
| E-A4.2-013 | OS migration source/plan/import-key construction | same |
| E-A4.2-014 | OS pre-effect exact/same-source receipt checks | same |
| E-A4.2-015 | OS plan-dependent migration subaction keys | same |
| E-A4.2-016 | OS late migration receipt publication | same |
| E-A4.2-017 | migration sequential-only replay tests | same |
| E-A4.2-018 | Brain Data candidate identity/natural-key contract | same |
| E-A4.2-019 | OS Data query-then-create path | same |
| E-A4.2-020 | candidate-derived Data create idempotency key | same |
| E-A4.2-021 | Data transactional record.create/idempotency | same |
| E-A4.2-022 | Data storage key lacks semantic natural-key uniqueness | same |
| E-A4.2-023 | OS >1 natural-key match becomes ambiguous | same |
| E-A4.2-024 | no competing-candidate natural-key race test found | same |


### A4.3 evidence IDs

| Evidence ID | Short description | Canonical source packet |
|---|---|---|
| E-A4.3-001 | fresh A4.3 frozen-ref/open-PR gate | adversarial/A4.3-PARTIAL-FAILURE-CORRUPTION-RECOVERY.md |
| E-A4.3-002 | Gateway lifecycle setup publication ordering | same |
| E-A4.3-003 | Gateway run restart/recovery | same |
| E-A4.3-004 | Memory same-root lock/journal/effect recovery | same |
| E-A4.3-005 | Memory cross-root handoff WSA-014 | same |
| E-A4.3-006 | Skills immutable generation/active pointer | same |
| E-A4.3-007 | Skills stale-lock WSA-017 | same |
| E-A4.3-008 | Data corruption inspection/staged recovery | same |
| E-A4.3-009 | Data quarantine write block | same |
| E-A4.3-010 | Automations transactional occurrence/event behavior | same |
| E-A4.3-011 | Automations unknown-delivery recovery fence | same |
| E-A4.3-012 | Automations DB ownership/format WSA-026 | same |
| E-A4.3-013 | Multiple Bots stale execution recovery | same |
| E-A4.3-014 | Multiple Bots atomic recovery preconditions | same |
| E-A4.3-015 | Token pricing failure atomicity WSA-025 | same |
| E-A4.3-016 | Distribution atomic receipt file writer | same |
| E-A4.3-017 | Distribution owner effect / receipt gap WSA-034 | same |
| E-A4.3-018 | no admitted changed cross-release Distribution transition | same |
| E-A4.3-019 | OS migration deterministic subaction idempotency | same |
| E-A4.3-020 | OS late final migration receipt | same |
| E-A4.3-021 | Connections directory lock lacks crash recovery | same |
| E-A4.3-022 | Connections doctor omits state-lock validation | same |
| E-A4.3-023 | Connections pending reservation / terminal receipt flow | same |
| E-A4.3-024 | Connections budget counts attemptedExternal true only | same |
| E-A4.3-025 | Connections all-or-nothing NDJSON receipt parser | same |
| E-A4.3-026 | Connections doctor omits receipt-store validation | same |
| E-A4.3-027 | same-key tests have no abandoned-pending recovery | same |
| E-A4.3-028 | no stale-lock or receipt-corruption recovery test found | same |
| E-A4.3-029 | A4.2 migration source reservation finding WSA-052 | same |
| E-A4.3-030 | inherited failure/recovery finding matrix | same |

### A4.4 evidence IDs

| Evidence ID | Short description | Canonical source packet |
|---|---|---|
| E-A4.4-001 | fresh A4.4 frozen-ref/open-PR gate | adversarial/A4.4-PRIVACY-VISIBILITY-PROVENANCE.md |
| E-A4.4-002 | Gateway bearer/run-principal ownership | same |
| E-A4.4-003 | Gateway session/system/workspace/principal binding | same |
| E-A4.4-004 | Gateway audit request-digest minimization | same |
| E-A4.4-005 | Memory normal allowed-scope model | same |
| E-A4.4-006 | Memory progressive exact-source scope revalidation | same |
| E-A4.4-007 | Memory relationship projection scope filter | same |
| E-A4.4-008 | Data trusted-scope provenance WSA-020 | same |
| E-A4.4-009 | Token read authorization immutable scope floor | same |
| E-A4.4-010 | Token default export/projection privacy | same |
| E-A4.4-011 | Brain minimal durable action receipts | same |
| E-A4.4-012 | Automations wake/run/wake-receipt storage model | same |
| E-A4.4-013 | Automations local-only ordinary read surfaces | same |
| E-A4.4-014 | Multiple Bots inbound bearer authentication | same |
| E-A4.4-015 | Multiple Bots workspace-filtered Dashboard projections/events | same |
| E-A4.4-016 | Dashboard local unauthenticated read WSA-040 | same |
| E-A4.4-017 | Dashboard stale subscription WSA-038 | same |
| E-A4.4-018 | Distribution failure-path redaction WSA-036 | same |
| E-A4.4-019 | Connections normal credential/receipt minimization | same |
| E-A4.4-020 | Connections MCP JSON-RPC error propagation | same |
| E-A4.4-021 | Connections terminal failure receipt errorMessage persistence | same |
| E-A4.4-022 | Connections CLI error details serialization | same |
| E-A4.4-023 | Connections Generic API secret non-persistence regression | same |
| E-A4.4-024 | no MCP secret-like error redaction regression found | same |
| E-A4.4-025 | A2.4 identity/scope/isolation graph | same |
| E-A4.4-026 | A2.7 receipt/provenance ownership/privacy graph | same |
| E-A4.4-027 | A3.4 Context/Memory journey | same |
| E-A4.4-028 | A3.8 Connections external-effect journey | same |
| E-A4.4-029 | A3.10 two-system isolation journey | same |

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
| `WSA-2026-024` | allocated A1.8 |
| `WSA-2026-025` | allocated A1.8 |
| `WSA-2026-026` | allocated A1.9 |
| `WSA-2026-027` | allocated A1.9 |
| `WSA-2026-028` | allocated A1.9 |
| `WSA-2026-029` | allocated A1.10 |
| `WSA-2026-030` | allocated A1.10 |
| `WSA-2026-031` | allocated A1.10 |
| `WSA-2026-032` | allocated A1.10 |
| `WSA-2026-033` | allocated A1.10 |
| WSA-2026-034 | allocated A1.12 |
| WSA-2026-035 | allocated A1.12 |
| WSA-2026-036 | allocated A1.12 |
| WSA-2026-037 | allocated A1.12 |
| WSA-2026-038 | allocated A1.13 |
| WSA-2026-039 | allocated A1.13 |
| WSA-2026-040 | allocated A1.13 |
| WSA-2026-041 | allocated A1.13 |
| WSA-2026-042 | allocated A1.13 |
| WSA-2026-043 | allocated A1.14 |
| WSA-2026-044 | allocated A1.14 |
| WSA-2026-045 | allocated A2.5 |
| WSA-2026-046 | allocated A2.8 |
| WSA-2026-047 | allocated A3.2 |
| WSA-2026-048 | allocated A3.5 |
| WSA-2026-049 | allocated A3.10 |
| WSA-2026-050 | allocated A4.1 |
| WSA-2026-051 | allocated A4.1 |
| WSA-2026-052 | allocated A4.2 |
| WSA-2026-053 | allocated A4.2 |
| WSA-2026-054 | allocated A4.3 |
| WSA-2026-055 | allocated A4.3 |
| WSA-2026-056 | allocated A4.3 |
| WSA-2026-057 | allocated A4.4 |
| WSA-2026-058 | **NEXT UNUSED** |

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
