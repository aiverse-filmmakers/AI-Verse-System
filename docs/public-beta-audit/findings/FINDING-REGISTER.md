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
10. The A0-A6 audit is complete. Dashboard MC1.4 and owner dogfood remain paused under the final NO-GO verdict until the ordered repair, re-audit, closure and bounded final independent recheck gates explicitly release the intended scope.

**Next unused finding ID:** `WSA-2026-064`.

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
| `WSA-2026-006` | BLOCKER | PROVEN | CLOSED | destructive lifecycle / filesystem safety | `AI-Verse-Gateway` | A1.2 |
| `WSA-2026-007` | HIGH | PROVEN | OPEN | setup/disable/uninstall/status lifecycle truth | `AI-Verse-Gateway` | A1.2 |
| `WSA-2026-008` | HIGH | PROVEN | OPEN | concurrency / idempotency / session binding / run control | `AI-Verse-Gateway` | A1.2 |
| `WSA-2026-009` | HIGH | PROVEN | OPEN | filesystem containment / scope isolation | `AI-Verse-Brain` | A1.3 |
| `WSA-2026-010` | MEDIUM | PROVEN | OPEN | Goal concurrency / replay safety | `AI-Verse-Brain` | A1.3 |
| `WSA-2026-011` | LOW | PROVEN | OPEN | release/version identity | `AI-Verse-Brain` | A1.3 |
| `WSA-2026-012` | BLOCKER | PROVEN | CLOSED | destructive lifecycle / filesystem containment | `AI-Verse-Memory` | A1.4 |
| `WSA-2026-013` | HIGH | PROVEN | OPEN | lifecycle authority / canonical writes | `AI-Verse-Memory` | A1.4 |
| `WSA-2026-014` | HIGH | PROVEN | OPEN | migration / canonical authority transfer | `AI-Verse-Memory` | A1.4 |
| `WSA-2026-015` | LOW | PROVEN | OPEN | release/version/bootstrap reproducibility | `AI-Verse-Memory` | A1.4 |
| `WSA-2026-016` | BLOCKER | PROVEN | CLOSED | lifecycle controller containment | `AI-Verse-Skills` | A1.5 |
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
| `WSA-2026-029` | BLOCKER | PROVEN | CLOSED | destructive lifecycle / filesystem containment | `AI-Verse-Connections` | A1.10 |
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
| WSA-2026-058 | MEDIUM | PROVEN | OPEN | long-lived runtime state scale / idempotency indexing | AI-Verse-Gateway | A4.5 |
| WSA-2026-059 | MEDIUM | PROVEN | OPEN | external-effect history scale / receipt indexing / budget lookup | AI-Verse-Connections | A4.5 |
| WSA-2026-060 | LOW | PROVEN | OPEN | machine-readable release compatibility / blocker truth | ai-verse-distribution | A5.2 |
| WSA-2026-061 | LOW | PROVEN | OPEN | release-acceptance documentation / version and CI status truth | ai-verse-token | A5.3 |
| WSA-2026-062 | LOW | PROVEN | OPEN | profile composition documentation / release scope truth | AI-Verse-Multiple-Bots | A5.3 |
| WSA-2026-063 | MEDIUM | PROVEN | OPEN | product runtime release evidence / supported runtime boundary | AI-Verse-Gateway, ai-verse-distribution | A5.4 |

Current counts:

| Dimension | Count |
|---|---:|
| BLOCKER | 4 |
| HIGH | 24 |
| MEDIUM | 22 |
| LOW | 12 |
| INFO | 1 |
| PROVEN | 63 |
| STRONG | 0 |
| POSSIBLE | 0 |
| UNVERIFIED | 0 |
| OPEN | 59 |
| CLOSED | 4 |

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
**State:** CLOSED  
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


#### Post-audit closure - 2026-09-17

**State transition:** `OPEN -> CLOSED`  
**Repair PR:** `AI-Verse-Gateway#32`  
**Repair PR head:** `94a1416724f076f06783385c4df07cf18bdbd788`  
**Merged repair ref:** `5347a0b7e3f3f302f4570e9bc37d515192753610`  
**Closure packet:** `../repairs/WSA-2026-006-GATEWAY-DESTRUCTIVE-PURGE.md`

Closure evidence proves that Gateway destructive purge now requires persistent ownership bound to the canonical real root, refuses broad/root/symlink/foreign targets, refuses to claim unrelated non-empty directories, deletes only known Gateway-owned entries and preserves unknown entries.

PR-head CI run `35152574719` passed all six Ubuntu/macOS/Windows Node 20/22 jobs. The observed Ubuntu Node 22 suite reported 104 passed / 0 failed, including the new lifecycle-containment regressions. Four composed Gateway workflows also passed. PR-head to merged-main comparison contained zero file changes, proving the tested product bytes are the merged bytes.

Finding-specific rechecks:
- A1.2: WSA-006 failure mechanism no longer exists at the repaired ref;
- A3.10: Gateway branch of destructive lifecycle contradiction C-A3.10-001 resolved; other lifecycle blockers remain;
- A4.1: Gateway branch of owner-root contradiction C-A4.1-003 resolved; other security findings remain.

Overall system verdict remains **NO-GO**. Remaining open BLOCKERs are WSA-2026-012, WSA-2026-016 and WSA-2026-029.

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
**State:** CLOSED  
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


#### Post-audit closure - 2026-09-17

**State transition:** `OPEN -> CLOSED`  
**Repair PR:** `AI-Verse-Memory#30`  
**Final tested PR head:** `acbe3e22d9b12c0fc1b0dcd95eeea393a57a69f2`  
**Merged repair ref:** `7a1ed5777fd11616375501d730fcbd488beff8b8`  
**Closure packet:** `../repairs/WSA-2026-012-MEMORY-LIFECYCLE-CONTAINMENT.md`

Memory now routes target-root lifecycle writes and removals through one shared physical-containment helper. Existing path components must remain inside the selected canonical target root, POSIX symlinks and Windows junction/reparse components fail closed, and destructive uninstall preflights runtime/adapter targets before registration or filesystem mutation.

Permanent regressions attack `scripts`, `scripts/ai-verse-memory`, `.claude`, `.claude/skills`, the Claude Memory adapter, `.agents`, `.agents/skills`, and the Agents Memory adapter. External sentinel data must survive rejected install/setup/uninstall operations.

Final workflow run `35155708095` passed all 12 jobs across Ubuntu, macOS and Windows. Windows public-beta acceptance job `104994513236` created real directory junctions with `mklink /J`, passed both new containment tests, and reported 17 tests / OK. The final tested PR head and merged main have zero product-file differences.

Finding-specific rechecks:
- A1.4: the WSA-012 parent-redirection mechanism is closed at the repaired exact ref;
- A3.10: the Memory branch of destructive lifecycle contradiction C-A3.10-001 is resolved; Skills and Connections blockers remain;
- A4.1: the Memory branch of owner-root/path contradiction C-A4.1-003 is resolved; other security/path findings remain.

This closure does not alter WSA-2026-013, WSA-2026-014 or WSA-2026-015.

Overall system verdict remains **NO-GO**. Remaining open BLOCKERs are WSA-2026-016 and WSA-2026-029.

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
**State:** CLOSED  
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

#### Post-audit closure - 2026-09-17

**State transition:** `OPEN -> CLOSED`  
**Repair PR:** `AI-Verse-Skills#15`  
**Final tested PR head:** `62b49d6420a6034fd08c47c2070ec473f128a392`  
**Merged repair ref:** `3541d2a7af1b20ca12736ed7454d119295d8e193`  
**Closure packet:** `../repairs/WSA-2026-016-SKILLS-CONTROLLER-CONTAINMENT.md`

Skills now derives controller, generation, active-pointer, setup/integration and learning state through one physical controller-containment law. POSIX symlink and Windows junction/reparse indirection fail closed, and destructive generation purge validates confined generation paths before recursive deletion.

Final PR-head evidence is green across Validate, Full E2E, six-leg Runtime Readiness and six-leg Lifecycle Controller Containment. Windows Python 3.9 job `105107547111` ran all 10 lifecycle/controller tests including real `mklink /J` junction attacks and reported OK. The reviewed PR head and merged main share product tree `3e5f72ed405aec0cc015afb52a98505178cf0c3f`.

Merged-main recheck is also fully green:
- Containment run `35201821336`;
- Runtime Readiness run `35201821346`;
- Full E2E run `35201821359`;
- Validate run `35201821414`.

Finding-specific rechecks:
- A1.5: the WSA-016 controller-redirection mechanism is closed at the repaired exact ref;
- A3.10: the Skills branch of destructive lifecycle contradiction C-A3.10-001 is resolved; Connections WSA-029 remains;
- A4.1: the Skills branch of owner-root contradiction C-A4.1-003 is resolved; other security/path findings remain.

This closure does not alter WSA-2026-017, WSA-2026-018 or WSA-2026-019.

Overall system verdict remains **NO-GO**. The only remaining open BLOCKER is WSA-2026-029.

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
**State:** CLOSED  
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

#### Post-audit closure - 2026-09-17

**State transition:** `OPEN -> CLOSED`  
**Repair PR:** `AI-Verse-Connections#2`  
**Final tested/reviewed PR head:** `c4bb77f680298d91ce619db91a39d69daaaa76a8`  
**Merged repair ref:** `a04f655c6f0c9b57d17e64b5c1ff8eb88aab4016`  
**Closure packet:** `../repairs/WSA-2026-029-CONNECTIONS-DESTRUCTIVE-PURGE.md`

Connections now requires durable exact-realpath ownership before destructive purge. Broad filesystem/user/system homes, foreign non-empty homes, missing/wrong/copied ownership markers and an exact-home symlink/junction target fail closed. Purge removes only known Connections-owned children and preserves unexpected/unowned entries rather than recursively erasing the selected root.

Permanent regressions cover unrelated non-empty homes, legacy-state ownership migration, missing/foreign/copied markers, broad roots, safe custom owned purge, unknown sentinel preservation and exact-home symlink/Windows-junction rejection.

Exact repaired destructive-boundary validation reported **10 / 10 PASS**, and the actual lifecycle `install -> setup -> uninstall({purge:true})` path passed. Final PR head and merged product files have zero differences and there are no open Connections PRs after merge.

Hosted cross-platform execution is **not claimed** for this repair. Connections workflow run `35219295977`, unchanged-main run `35218943165` and post-merge run `35219652570` all produced the inherited private-repository no-runner condition: jobs have `steps: []` and `runner_id: 0`. This remains separately OPEN as WSA-2026-003 and is not a product-test failure.

Finding-specific rechecks:
- A1.10: the arbitrary configured-root recursive purge mechanism is closed at the repaired exact ref;
- A3.10: all four destructive lifecycle containment branches in C-A3.10-001 are now resolved; A3.10 remains PARTIAL overall because other lifecycle/recovery and two-system findings remain;
- A4.1: the WSA-029 Connections purge branch of owner-root contradiction C-A4.1-003 is resolved; other security/path findings remain.

This closure does not alter WSA-2026-003, WSA-2026-030 through WSA-2026-033, WSA-2026-051, WSA-2026-054 through WSA-2026-057, or WSA-2026-059.

All four historical BLOCKER findings are now CLOSED. Phase R0 is **4 / 4 complete**. Overall system verdict remains **NO-GO** pending later repair phases and the bounded final independent recheck.

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

### WSA-2026-058 - Gateway idempotency state has unbounded whole-file growth on supported recurring paths

**Severity:** MEDIUM  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A4.5  
**Root area:** long-lived runtime state scale / idempotency indexing  
**Affected repo:** AI-Verse-Gateway

**Summary:**  
Gateway stores every idempotency record in one JSON object. Each claim and commit reads/parses and rewrites the whole file. Supported recurring Automations generate a unique invocation ID on every occurrence, so ordinary always-on operation grows this hot-path state indefinitely.

**Contradiction:** C-A4.5-001.

**Primary evidence:** E-A4.5-005 through E-A4.5-009.

**Impact:**  
Idempotency request latency, memory use and write amplification grow with lifetime key count. This can degrade recurring Automation delivery and other idempotent Gateway operations even when individual requests are small and valid.

**Required closure evidence:**  
Move hot-path idempotency to an indexed transactional or equivalently bounded design, define safe replay retention/compaction, preserve changed-payload rejection, benchmark realistic 100k+ key histories, and re-run Gateway/Automation replay acceptance.

---

### WSA-2026-059 - Connections performs unbounded lifetime receipt scans on every external execution

**Severity:** MEDIUM  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A4.5  
**Root area:** external-effect history scale / receipt indexing / budget lookup  
**Affected repo:** AI-Verse-Connections

**Summary:**  
Connections keeps one lifetime append-only receipt log and reparses the entire file on every external execution. Budget checks and idempotency lookup repeatedly scan all historical receipts, including records too old to affect current minute/day budgets.

**Contradiction:** C-A4.5-002.

**Primary evidence:** E-A4.5-023 through E-A4.5-028.

**Impact:**  
Normal valid lifetime growth increases disk read, parse, allocation and filtering cost for every provider call. Long-lived external-effect use can progressively degrade without corruption or hostile input.

**Required closure evidence:**  
Use indexed recent-window/idempotency state while retaining auditable historical receipts, define safe partition/archive semantics, benchmark 100k+ receipts, prove bounded hot-path latency/memory, and re-run budget/idempotency/recovery tests.

---

### WSA-2026-060 - Full compatibility metadata retains an obsolete “Agent not admitted” blocker

**Severity:** LOW  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A5.2  
**Root area:** machine-readable release compatibility / blocker truth  
**Affected repo:** ai-verse-distribution

**Summary:**  
The canonical compatibility record for `full-public-beta-pending` still says the Agent profile does not have an admitted immutable public-beta release set, while the same Distribution catalog contains and defaults to released `agent-public-beta-2026-09-14`. The Full release manifest itself correctly lists only the remaining Connections/Dashboard/Apps composition blocker.

**Contradiction:** C-A5.2-006.

**Primary evidence:** E-A5.2-036 through E-A5.2-039.

**Impact:**  
Machine consumers or maintainers reading compatibility metadata can derive a false reason for Full being blocked. Runtime Full selection still fails closed for the true remaining blocker, so no unsafe release admission is created.

**Required closure evidence:**  
Remove the obsolete Agent blocker, retain the real Connections/Dashboard/Apps blocker, define one authoritative blocker source or validate repeated blocker lists for consistency, and add a regression preventing a released Agent channel from coexisting with an “Agent not admitted” Full blocker.

---

### WSA-2026-061 - Token beta.3 release-acceptance document retains beta.1 and pre-CI status text

**Severity:** LOW  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A5.3  
**Root area:** release-acceptance documentation / version and CI status truth  
**Affected repo:** ai-verse-token

**Summary:**  
Token's current release-acceptance document declares public-beta.3 while its verification section still describes public-beta.1 evidence and says beta.3 hosted CI remains a future seal condition. Exact-head beta.3 CI has already passed all six configured cross-platform jobs.

**Contradiction:** C-A5.3-007.

**Primary evidence:** E-A5.3-015 through E-A5.3-017.

**Impact:**  
Release reviewers can derive the wrong answer about which version the listed test counts apply to and whether beta.3 hosted qualification is still pending. Runtime behavior is unaffected.

**Required closure evidence:**  
Make version labels internally consistent with beta.3, distinguish inherited beta.1 counts if intentionally retained, replace future CI wording with completed exact run/job evidence, and add bounded release-doc/version-status consistency coverage where practical.

---

### WSA-2026-062 - Multiple Bots release acceptance incorrectly places Connections in the Agent profile

**Severity:** LOW  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A5.3  
**Root area:** profile composition documentation / release scope truth  
**Affected repo:** AI-Verse-Multiple-Bots

**Summary:**  
The current Multiple Bots public-beta release-acceptance document says the Agent profile composition includes Connections. Distribution's canonical Agent profile excludes Connections; Connections belongs to Full.

**Contradiction:** C-A5.3-008.

**Primary evidence:** E-A5.3-012 through E-A5.3-014.

**Impact:**  
Maintainers can incorrectly infer that Connections is required for the current Agent release or was exercised by Agent composed acceptance. Distribution runtime composition is unaffected.

**Required closure evidence:**  
Correct the Agent profile sentence, preserve Connections only as the owner of external-connection authority where relevant, and regression-check repeated profile composition against canonical Distribution profile truth if composition is retained in component docs.

---

### WSA-2026-063 - Agent clean-machine release evidence substitutes Gateway's deterministic test runtime for the supported runtime edge

**Severity:** MEDIUM  
**Confidence:** PROVEN  
**State:** OPEN  
**Opened by:** A5.4  
**Root area:** product runtime release evidence / supported runtime boundary  
**Affected repos:** AI-Verse-Gateway, ai-verse-distribution

**Summary:**  
Distribution's clean-machine Agent release gate uses the real `aiverse start` entrypoint, real owner lifecycles and real Gateway HTTP API, but configures Gateway with the `deterministic` zero-network runtime that Gateway itself labels for local testing. No reviewed default or candidate clean-machine Agent acceptance drives the documented non-test runtime boundary such as `openai-compatible`.

**Contradiction:** C-A5.4-002.

**Primary evidence:** E-A5.4-009 through E-A5.4-025.

**Impact:**  
A release can pass without proving the final member-facing model/runtime network edge: upstream URL handling, environment-backed bearer injection, model/tool-call mapping, usage mapping, timeout/error behavior and clean-machine runtime readiness can remain outside composed release evidence. This is an evidence gap, not proof that the adapter currently fails.

**Required closure evidence:**  
Add immutable clean-machine acceptance that begins through `aiverse start`, configures an admitted exact Agent set through a supported non-test runtime boundary, exercises the actual `openai-compatible` network adapter with a deterministic protocol-faithful local upstream if necessary, verifies credential/model/tool/usage/error handling, preserves runtime binding across restart, and passes on Ubuntu/macOS/Windows. Keep the deterministic runtime gate as supplemental coverage rather than the sole composed runtime proof.

---

## 5. Contradiction register

The contradiction register below remains historical audit evidence. Post-audit finding closure is recorded in each finding's appended closure record and does not rewrite the original A0-A6 contradiction rows.

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
| C-A4.5-001 | A4.5 | Gateway replay safety vs unbounded whole-file idempotency state | yes | WSA-2026-058 | OPEN |
| C-A4.5-002 | A4.5 | Connections bounded request budgets vs lifetime receipt scans | yes | WSA-2026-059 | OPEN |
| C-A4.5-003 | A4.5 | Agent current-generation floor vs ordinary Python prerequisite UX | yes | WSA-2026-035 | OPEN |
| C-A4.5-004 | A4.5 | current supported platform claim vs clean-machine evidence | no | none | VERIFIED |
| C-A4.5-005 | A4.5 | Memory/Token/Data bounded read claims vs executable query limits | no | none | VERIFIED |
| C-A5.1-001 | A5.1 | private workflow failure label vs zero executed steps | yes | WSA-2026-003 | OPEN |
| C-A5.1-002 | A5.1 | final Agent success vs first-attempt Windows Gateway failure | no | none | RECORDED / RETRY PASSED |
| C-A5.1-003 | A5.1 | green exact-head standard CI vs specialized workflow absence | no | none | BOUNDED EVIDENCE |
| C-A5.1-004 | A5.1 | mutable-main compatibility jobs vs immutable composition evidence | no | none | SUPPLEMENTAL ONLY |
| C-A5.1-005 | A5.1 | Skills Video Editor acceptance head vs frozen current head | no | none | VERIFIED / ZERO FILE DIFF |
| C-A5.1-006 | A5.1 | Distribution qualification head vs current merge head | no | none | VERIFIED / ZERO FILE DIFF |
| C-A5.1-007 | A5.1 | current System hosted no-step failure vs external exact qualification | yes | WSA-2026-003 | OPEN |
| C-A5.2-001 | A5.2 | Invisible candidate qualification-pending metadata vs qualified merged candidate | yes | WSA-2026-001 | OPEN |
| C-A5.2-002 | A5.2 | current Skills accepted head vs newest admitted Agent candidate Skills ref | yes | WSA-2026-046 | OPEN |
| C-A5.2-003 | A5.2 | historical component release descriptors vs current main | no | existing version findings | INTENTIONAL RELEASE-METADATA BOUNDARY |
| C-A5.2-004 | A5.2 | Token beta.3 package identity vs absent beta.3 Git tag | no | none | EXACT DISTRIBUTION SHA VERIFIED |
| C-A5.2-005 | A5.2 | finalized manifest identity vs future anti-repointing enforcement | no | none | NEGATIVE SPACE / CURRENT MANIFESTS PRESERVED |
| C-A5.2-006 | A5.2 | Full release blocker vs stale compatibility blocker | yes | WSA-2026-060 | OPEN |
| C-A5.2-007 | A5.2 | System latest-candidate current truth vs Distribution | yes | WSA-2026-044 | OPEN |
| C-A5.3-001 | A5.3 | audit entrypoint says A0.1 vs tracker at A5.3 | yes | WSA-2026-004 | OPEN |
| C-A5.3-002 | A5.3 | System Connections spec says not started vs executable live Connections | yes | WSA-2026-002 | OPEN |
| C-A5.3-003 | A5.3 | System living spec vs latest accepted owner/release truth | yes | WSA-2026-044 | OPEN |
| C-A5.3-004 | A5.3 | Distribution Agent Python prose vs executable compatibility | yes | WSA-2026-035 | OPEN |
| C-A5.3-005 | A5.3 | Distribution architecture/roadmap release status vs machine truth | yes | WSA-2026-037 | OPEN |
| C-A5.3-006 | A5.3 | Full compatibility blocker vs released Agent | yes | WSA-2026-060 | OPEN |
| C-A5.3-007 | A5.3 | Token beta.3 acceptance status vs beta.1/pre-CI verification section | yes | WSA-2026-061 | OPEN |
| C-A5.3-008 | A5.3 | Multiple Bots Agent composition vs Distribution profile | yes | WSA-2026-062 | OPEN |
| C-A5.3-009 | A5.3 | component safety/readiness prose vs known executable defects | yes | existing technical findings | DEDUPED |
| C-A5.3-010 | A5.3 | dated historical snapshots vs later implementation | no | none | HISTORICAL / BOUNDED |
| C-A5.4-001 | A5.4 | clean-machine claim vs actual public Distribution entrypoint | no | none | VERIFIED REAL AIVERSE START PATH |
| C-A5.4-002 | A5.4 | real composed Agent claim vs deterministic test runtime edge | yes | WSA-2026-063 | OPEN |
| C-A5.4-003 | A5.4 | default Agent age vs later accepted explicit candidates | no | none | INTENTIONAL IMMUTABLE CHANNEL BOUNDARY |
| C-A5.4-004 | A5.4 | strongest candidate current refs vs current Skills/Video Editor | yes | WSA-2026-046 | OPEN |
| C-A5.4-005 | A5.4 | semantic migration current path vs composed owner acceptance | yes | WSA-2026-047 | OPEN |
| C-A5.4-006 | A5.4 | current self-learning path vs one composed release journey | yes | WSA-2026-048 | OPEN |
| C-A5.4-007 | A5.4 | multi-system isolation intent vs one-root clean-machine gates | yes | WSA-2026-049 | OPEN |
| C-A5.4-008 | A5.4 | public Agent prerequisites vs executable compatibility | yes | WSA-2026-035 | OPEN |
| C-A5.4-009 | A5.4 | final Agent PR attempt-1 Windows failure vs unchanged successful rerun | no | none | EVIDENCE LIMITATION |
| C-A5.4-010 | A5.4 | current model/provider generation vs hard-coded obsolete provider | no | none | VERIFIED ADAPTER/CONFIG DRIVEN |

### A6.5 final audit freeze

A6.5 freezes the final A0-A6 audit state at **100/100 complete**.

Final audit truth:

- product/distribution refs remain exactly on the A0 frozen snapshot;
- 63 findings remain PROVEN / OPEN;
- severities remain 4 BLOCKER / 24 HIGH / 22 MEDIUM / 12 LOW / 1 INFO;
- whole-system verdict remains **NO-GO**;
- nine root-cause families remain canonical;
- A6.4 repair program covers 63/63 findings exactly once;
- Dashboard MC1.4 and owner dogfood remain paused;
- post-repair bounded independent recheck remains mandatory.

Canonical final freeze:

`docs/public-beta-audit/synthesis/A6.5-FINAL-AUDIT-FREEZE.md`

No finding is closed or changed by the freeze.

### A6.4 ordered repair program

A6.4 defines the dependency-safe post-audit repair sequence for **all 63 open findings**.

Repair waves:

- Wave 0 — 4 destructive-containment BLOCKERs;
- Wave 1 — 13 trusted authority/scope/identity/final-edge HIGHs;
- Wave 2 — 5 lifecycle/readiness authority findings;
- Wave 3 — 10 atomicity/concurrency/migration/crash-safety findings;
- Wave 4 — 10 remaining runtime MEDIUM correctness/privacy/scale findings;
- Wave 5 — 15 release/current-state/documentation synchronization findings;
- Wave 6 — 6 composed qualification/evidence findings.

Coverage is **63/63 unique findings** with no duplicate assignment.

The program requires a bounded final independent recheck after repair/requalification before any new readiness verdict or MC1.4/owner-dogfood release.

Canonical repair program:

`docs/public-beta-audit/synthesis/A6.4-ORDERED-REPAIR-PROGRAM.md`

Current verdict remains **NO-GO**.

### A6.3 whole-system verdict

A6.3 issues the system-level verdict:

# **NO-GO**

for owner dogfood, Dashboard MC1.4 resumption and any claim that the frozen audited whole-system snapshot is ready for controlled public-beta use.

Basis:

- 4 PROVEN / OPEN BLOCKER findings;
- 24 PROVEN / OPEN HIGH findings;
- canonical tracker rule requiring repair, re-audit, closure and bounded final recheck before dogfood;
- A6.2 concentration of all BLOCKER/HIGH findings in trusted-boundary binding, atomic canonical mutation and authoritative lifecycle truth.

This verdict opens no new finding and changes no finding state/severity/confidence.

Canonical verdict:

`docs/public-beta-audit/synthesis/A6.3-WHOLE-SYSTEM-VERDICT.md`

### A6.2 root-cause synthesis result

A6.2 groups the 63 stable findings into **9 primary architectural root-cause families** without merging or closing findings.

Primary assignment is exact:

- RC-01 trusted boundary binding: 17 findings — 4 BLOCKER / 13 HIGH;
- RC-02 atomic/serialized canonical mutation: 10 findings — 7 HIGH / 3 MEDIUM;
- RC-03 authoritative lifecycle/readiness truth: 6 findings — 4 HIGH / 2 MEDIUM;
- RC-04 long-lived state retention/freshness/indexing: 4 MEDIUM;
- RC-05 final diagnostics/receipt sanitization: 2 MEDIUM;
- RC-06 release/current-state synchronization: 15 findings — 3 MEDIUM / 12 LOW;
- RC-07 composed qualification completeness: 6 findings — 5 MEDIUM / 1 INFO;
- RC-08 Dashboard projection/browser semantics: 2 MEDIUM;
- RC-09 Gateway pre-auth resource admission: 1 MEDIUM.

All **4 BLOCKERs and all 24 HIGHs** are concentrated in RC-01/RC-02/RC-03.

Canonical graph:

`docs/public-beta-audit/synthesis/A6.2-ROOT-CAUSE-FINDING-GRAPH.md`

No finding state, severity, confidence or ID changed.

### A6.1 global deduplication result

A6.1 has completed the whole-system contradiction dedupe.

- source contradiction rows retained: **184**;
- material source observations: **165**;
- non-material / verified / historical / bounded rows: **19**;
- unresolved global contradiction families after dedupe: **63**;
- stable open findings: **63**;
- orphan findings: **0**;
- material unresolved families without a stable finding: **0**;
- one material umbrella row without exact IDs, `C-A5.3-009`, was already marked **DEDUPED** and creates no additional family.

Canonical deduped view:

`docs/public-beta-audit/synthesis/A6.1-GLOBAL-CONTRADICTION-REGISTER.md`

The raw phase-local contradiction rows below remain immutable audit history. A6.1 does not renumber, erase or rewrite them.

[The remainder of this file, including all historical contradiction detail, evidence ID registers, finding allocation ledger, negative-space checks, downstream rules and A0.3 task completion record, is unchanged from blob `f7648b3eb684b2fa0bed4fc439d096a1758b20d5`.]