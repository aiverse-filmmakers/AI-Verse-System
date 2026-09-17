# WSA-2026-023 Closure — Multiple Bots Worker Workspace Isolation

**Finding:** `WSA-2026-023`  
**Severity / confidence:** HIGH / PROVEN  
**Owner:** `AI-Verse-Multiple-Bots`  
**Repair wave:** R1.4  
**Closure date:** 2026-09-17  
**State:** **CLOSED**

## 1. Finding

Managed Team Run Worker creation was workspace-bound, but generic coordination policy did not treat Workers as first-class workspace-scoped principals. That allowed foreign-workspace generic coordination state to target an existing Worker.

The runner later rejected mismatched execution, but its failure/cancel cleanup could still mutate the real Worker's canonical status or invoke its runtime merely because the foreign Task named that Worker.

Direct Worker message delivery had the same generic scope-validation gap.

The proven contradiction was `C-A1.7-002`, supported by `E-A1.7-015` through `E-A1.7-019`.

Required closure law:

1. existing Workers must be workspace-validated by generic coordination policy;
2. foreign-workspace delegation to an existing Worker must fail before canonical Task/lease/queue persistence;
3. direct Worker messaging must enforce Worker workspace scope;
4. failure and cancellation cleanup may mutate/invoke a Worker only after canonical Task <-> Worker <-> Team Run binding is proven;
5. two-workspace adversarial regressions must permanently cover the failure class.

## 2. Baseline and repair identity

**Live pre-repair Multiple Bots ref:** `cb20bfd014530a7faa26e6abc868d8f85226ec79`  
**Open owner PRs before repair:** 0

**Repair branch:** `repair/wsa-2026-023-worker-workspace-isolation`  
**Repair PR:** `AI-Verse-Multiple-Bots#70`  
**Final reviewed/tested PR head:** `c451e4a4065f4e5ecb9026a5a453cf7573ce2cef`  
**Merged Multiple Bots ref:** `e84090f932762316a985e30054859bb846bca963`  
**Final tested/merged tree:** `c01ede3789b38409438b6baf6aa0526c5ef1c4e7`

The final tested PR tree and merged `main` tree are byte-identical.

Open Multiple Bots PRs after merge: **0**.

## 3. Final implementation contract

### 3.1 Existing Workers are first-class generic workspace principals

`CoordinationPolicy.assertPrincipalWorkspace` now recognizes both durable `bot_*` and temporary `worker_*` principals.

For an existing Worker, policy requires:

- the Worker object's workspace to equal the requested coordination workspace;
- its `run_id` to resolve to a canonical Team Run;
- the Team Run workspace to equal both the Worker workspace and requested workspace.

A foreign-workspace existing Worker therefore fails with `WORKSPACE_DENIED` before delegation state is persisted.

### 3.2 Scope-only policy preserves valid Team Run planning/lifecycle

The final repair deliberately does **not** make generic policy the Worker lifecycle owner.

Two existing product behaviors are preserved:

- Team Run/fan-out planning may reserve a `worker_*` identity before the Worker record is persisted;
- a completed Worker may still publish its final bounded result while Team Run/runner lifecycle logic completes settlement.

If a `worker_*` identity has no existing Worker object yet, generic policy does not invent scope authority, but also does not reject valid pre-persistence planning. Once the Worker exists, its canonical workspace/Team Run scope must match.

Worker lifecycle availability remains owned by Team Run and runner logic.

### 3.3 Direct Worker message delivery is workspace checked

`CoordinationGateway.sendMessage` now invokes generic message policy for both Bot and Worker targets.

Because message policy validates both sender and target principals, this closes both directions:

- foreign Bot -> existing Worker;
- existing Worker -> foreign Bot.

Rejected messages do not create canonical message/mailbox delivery state.

### 3.4 Runner failure cleanup requires canonical Worker binding

A new runner binding predicate proves the exact relationship before Worker failure mutation:

- Worker workspace equals Task workspace;
- Team Run workspace equals Worker workspace;
- Task `run_id` equals the Worker Team Run;
- Worker `task_id` equals the Task;
- Task owner and assignee both equal the Worker;
- Team Run participants contain the Worker.

If this binding is not proven, the malformed/foreign Task may itself fail, but the real Worker is not marked failed and no Worker status-change event is emitted.

### 3.5 Cancellation/recovery uses the same Worker fence

Cancellation now applies the same canonical binding rule before:

- calling Worker runtime cancellation/recovery;
- marking the Worker canceled;
- emitting Worker status-change events.

A foreign or unbound Task therefore cannot control the Worker's runtime or canonical lifecycle.

## 4. Permanent adversarial regressions

Dedicated `test/worker-workspace-isolation.test.ts` coverage proves:

1. a foreign-workspace generic delegation to an existing Worker is rejected before Task or capability-lease persistence and leaves the Worker unchanged;
2. foreign Bot -> Worker direct messaging is rejected before message/mailbox persistence;
3. Worker -> foreign Bot direct messaging is rejected before persistence;
4. a foreign-workspace Task targeted at a real Worker can fail without marking the Worker failed;
5. cancellation of a foreign/unbound Task cannot mark the Worker canceled, emit a Worker lifecycle event, or invoke the Worker runtime.

## 5. CI caught and prevented an over-broad repair

The first PR implementation was **not** accepted.

**Initial CI run:** `35285759155`  
**Job:** `105417593970`  
**Result:** FAIL at `npm test`; later gates correctly skipped.

The four new WSA-023 adversarial regressions all passed in that run, but 12 existing tests exposed two semantic overreaches:

- generic policy required reserved `worker_*` identities to already exist, breaking valid fan-out planning;
- generic policy treated completed Workers as unavailable before final result publication/settlement.

Several downstream Worker execution, Brain/Memory projection, fan-out and handoff tests therefore failed.

The repair was narrowed instead of weakening workspace isolation:

- only existing Workers are scope-validated;
- pre-persistence reserved Worker identities remain valid;
- lifecycle availability stays with Team Run/runner code;
- the runner's failure/cancel canonical-binding fence remains intact.

This corrected design is the one tested and merged.

## 6. Exact acceptance evidence

### Final PR-head CI

**Run:** `35285867694`  
**Job:** `105417927293`  
**Head:** `c451e4a4065f4e5ecb9026a5a453cf7573ce2cef`  
**Conclusion:** **SUCCESS**

Executed successfully:

- `npm test` — **523 / 523 PASS**
- `npm run eval:phase4` — **5 / 5 PASS**
- `npm run pack:check` — **PASS**
- `npm run eval:release` — **7 / 7 PASS**

### Merged-main CI

**Run:** `35286065219`  
**Job:** `105418541761`  
**Merged ref:** `e84090f932762316a985e30054859bb846bca963`  
**Conclusion:** **SUCCESS**

Executed successfully:

- `npm test` — **523 / 523 PASS**
- `npm run eval:phase4` — **5 / 5 PASS**
- `npm run pack:check` — **PASS**
- `npm run eval:release` — **7 / 7 PASS**

## 7. Finding-specific recheck

### C-A1.7-002

**RESOLVED for WSA-2026-023.**

Generic coordination can no longer use a foreign workspace to target an existing Worker before persistence.

### Delegation seam

**PASS.**

Foreign-workspace delegation to an existing Worker fails before Task/lease/queue creation.

### Direct-message seam

**PASS.**

Existing Worker sender/target workspace is validated before message persistence.

### Failure-path adversarial recheck

**PASS.**

A malformed/legacy foreign Task cannot use runner failure handling to change the real Worker's canonical status.

### Cancellation-path adversarial recheck

**PASS.**

A foreign/unbound Task cannot invoke Worker runtime cancellation or change Worker canonical lifecycle.

### Valid Worker flows

**PASS.**

The full 523-test suite confirms the repair preserves:

- fan-out pre-persistence Worker planning;
- normal manager Worker execution;
- final Worker result publication;
- Worker handoff/restart flows;
- Brain, Memory and workspace projection Worker integrations;
- existing Team Run lifecycle/settlement behavior.

## 8. Adjacent findings

This closure is limited to `WSA-2026-023`.

`WSA-2026-024` — Token trusted ACTUAL source authority — remains **OPEN** and was not implemented, reclassified or implicitly closed here.

## 9. Closure verdict

All required WSA-2026-023 closure evidence is satisfied:

- owner repair merged;
- final tested and merged trees match exactly;
- existing Workers are workspace-scoped in generic policy;
- foreign Worker delegation/message paths fail before persistence;
- failure/cancel Worker mutation is canonically fenced;
- permanent two-workspace regressions exist;
- full PR-head and merged-main acceptance are green;
- valid Worker planning, execution, publication and handoff flows remain intact;
- adjacent findings remain untouched.

**WSA-2026-023: CLOSED.**
