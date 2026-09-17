# WSA-2026-022 Closure — Multiple Bots Operator/Domain Authority Binding

**Finding:** `WSA-2026-022`  
**Severity / confidence:** HIGH / PROVEN  
**Owner:** `AI-Verse-Multiple-Bots`  
**Repair wave:** R1.3  
**Closure date:** 2026-09-17  
**State:** **CLOSED**

## 1. Finding

The audited Multiple Bots security contract correctly distinguished Gateway transport access from domain authority, but sensitive operator-control paths accepted caller-selected `actorId` values and treated syntactic `operator_*` identity as sufficient authority.

The proven contradiction was `C-A1.7-001`, supported by `E-A1.7-010` through `E-A1.7-014`.

Affected operator-control classes included:

- durable Bot lifecycle transitions;
- external-managed Bot rebinding;
- Approval decisions;
- dead-letter retry;
- operator override of Task cancellation;
- operator override of Team Run termination;
- related operator control surfaces.

The required closure law was:

1. transport authentication must not itself grant operator/domain authority;
2. operator authorization must bind to trusted host/session identity;
3. caller actor identity must remain provenance/domain identity rather than a self-granting permission source;
4. negative regressions must prove ordinary Gateway access cannot satisfy operator-only mutations.

## 2. Audited baseline and live pre-repair state

**Audited Multiple Bots baseline:** `c600e2bc014351a61e1c0e2673fc63f5d5fa54ec`

The live pre-repair `main` was exactly that audited ref and had no open pull requests. The audited defect therefore remained current with no product drift to reconcile before implementation.

## 3. Repair identity

**Branch:** `repair/wsa-2026-022-operator-authority-binding`  
**Repair PR:** `AI-Verse-Multiple-Bots#69`  
**Final reviewed/tested PR head:** `7c31c18fa789f5b4a7f377fa781db85764f1b7a9`  
**Merged Multiple Bots ref:** `cb20bfd014530a7faa26e6abc868d8f85226ec79`  
**Final tested/merged tree:** `4c2bd28712cd10c43af57ad1f9c1c5cf875e350b`

The final tested PR tree and merged `main` tree are byte-identical.

Open Multiple Bots PRs after merge: **0**.

## 4. Final implementation contract

### 4.1 Transport access is not operator authority

`gateway-security.ts` now maintains request-scoped authority separately from the bearer credential.

A normal bearer session establishes:

- authenticated Gateway transport access;
- no operator mutation authority;
- no authenticated operator principal.

This preserves the repository's original secure-remote contract: bearer access reaches the Gateway but does not silently become domain authority.

### 4.2 Explicit trusted operator-session binding

Host code can explicitly bind a bearer session to a trusted operator principal through `bindGatewayOperatorSession(...)`.

The binding is host-supplied rather than caller-selected request data.

Operator principals are validated as bounded `operator_*` identities.

### 4.3 Request authority is reset per inbound request

The request-scoped authority context is overwritten before routing every request, including failed bearer attempts.

An unauthenticated or transport-only request therefore cannot inherit operator capability from a prior request.

### 4.4 Provenance and authorization are separate

Sensitive operator paths still record `actorId` as canonical provenance/domain identity, but that value is no longer sufficient to grant operator authority.

For bearer-backed operator sessions:

- the session must carry explicit trusted operator authority; and
- the claimed operator provenance must exactly match the authenticated bound operator principal.

A mismatch fails with `OPERATOR_PRINCIPAL_MISMATCH`.

### 4.5 Operator-only controls are fenced

Trusted operator authority is enforced for the operator paths involved in this finding, including:

- Bot lifecycle and external-managed rebind;
- Approval approve/deny;
- dead-letter retry;
- Task cancellation when using the `operator_*` override;
- Team Run termination when using the `operator_*` override;
- Handoff rejection when using the `operator_*` override.

Canonical retry mutation also retains a final authority fence before recovery state can be committed.

### 4.6 Existing non-operator domain rights are preserved

The repair does **not** convert all cancellation/control behavior into operator-only RBAC.

Existing legitimate domain rules remain intact:

- Task creator / owner / assignee cancellation;
- same-workspace Team Run leader Task cancellation;
- Team Run leader termination;
- Handoff target rejection;
- internal/local trusted host orchestration and recovery paths.

This distinction was explicitly re-reviewed before merge so WSA-2026-022 did not overwrite valid coordination authority.

## 5. Permanent regression coverage

Dedicated regressions in `test/operator-authority-binding.test.ts` prove:

1. a valid ordinary bearer can still reach `/health`;
2. bearer transport alone cannot disable a Bot by claiming an `operator_*` actor;
3. a host-bound authenticated operator session can perform the operator mutation;
4. a bound operator session cannot claim a different operator provenance identity;
5. bearer transport alone cannot approve pending work by claiming operator identity;
6. bearer transport alone cannot use the operator Task-cancel override;
7. bearer transport alone cannot authorize dead-letter retry.

The wider existing suite continues to prove owner/assignee/leader cancellation and Team Run semantics.

## 6. Pre-merge review history

The repair was not accepted on first green-looking implementation.

### 6.1 Type-shim failure caught before behavioral acceptance

The first PR CI attempt failed compilation because the repository's custom Node declarations lacked `node:async_hooks`.

A minimal `AsyncLocalStorage` declaration was added. No product behavior was waived.

### 6.2 Adversarial test fixture race caught by CI

The next run reached the full test suite and produced **517 / 518 passing**.

The sole failure was a new cancellation-test fixture racing the live supervisor: the Task completed before the assertion.

The fixture was changed to an approval-gated Task so the authority test is deterministic.

### 6.3 Semantic overreach caught after a green intermediate run

An intermediate head then passed the repository gate, but manual diff/domain-law review found that the first cancellation fence would also deny legitimate Task owner/assignee/Team-leader cancellation.

That was not accepted.

The final repair was narrowed so:

- only the `operator_*` override requires authenticated operator authority;
- legitimate non-operator cancellation/leader semantics remain unchanged;
- generic queue cancellation is not incorrectly made operator-only.

Permanent tests were updated to test the actual operator override rather than impersonating a legitimate owner.

This final corrected design is what was tested and merged.

## 7. Exact acceptance evidence

### PR-head CI

**Run:** `35284371590`  
**Job:** `105413321754`  
**Head:** `7c31c18fa789f5b4a7f377fa781db85764f1b7a9`  
**Conclusion:** **SUCCESS**

Executed successfully:

- `npm test` — **519 / 519 PASS**
- `npm run eval:phase4` — **5 / 5 PASS**
- `npm run pack:check` — **PASS**
- `npm run eval:release` — **7 / 7 PASS**

### Merged-main CI

**Run:** `35284559449`  
**Job:** `105413902656`  
**Merged ref:** `cb20bfd014530a7faa26e6abc868d8f85226ec79`  
**Conclusion:** **SUCCESS**

Executed successfully:

- `npm test` — **519 / 519 PASS**
- `npm run eval:phase4` — **5 / 5 PASS**
- `npm run pack:check` — **PASS**
- `npm run eval:release` — **7 / 7 PASS**

## 8. Finding-specific recheck

### C-A1.7-001

**RESOLVED for WSA-2026-022.**

The secure-remote contract and executable operator-control implementation now agree:

- transport authentication permits Gateway access;
- ordinary bearer access does not grant operator authority;
- operator authority comes from explicit trusted host/session binding;
- caller-selected operator provenance cannot create or switch authority.

### Operator-control seam

**PASS.**

Bot lifecycle/rebind, Approval decisions, dead-letter retry and operator overrides are bound to trusted operator authority rather than request-selected identity.

### Adversarial identity spoofing

**PASS.**

Transport-only bearer plus forged `operator_*` identity fails closed. A bound operator session with mismatched claimed operator identity also fails closed.

### Cancellation/control semantics

**PASS.**

The final repair preserves existing legitimate Task creator/owner/assignee and Team Run leader control while fencing only operator overrides.

## 9. Adjacent findings and residual limits

This closure is intentionally limited to `WSA-2026-022`.

`WSA-2026-023` — Multiple Bots Worker workspace isolation / canonical coordination authority — remains **OPEN** and was not repaired, reclassified or implicitly closed here.

This repair also does not introduce hosted multi-user RBAC. The audit explicitly did not require that for this finding. Local loopback/in-process calls remain inside the trusted host boundary, while remote bearer transport requires an explicit trusted operator-session binding for operator controls.

## 10. Closure verdict

All required WSA-2026-022 closure evidence is satisfied:

- owner repair merged;
- exact tested and merged trees match;
- permanent negative regressions exist;
- full PR-head acceptance is green;
- full merged-main acceptance is green;
- provenance is separated from authorization;
- operator authority is bound to trusted host/session identity;
- legitimate non-operator domain rights were preserved;
- finding-specific seam/adversarial recheck passes;
- adjacent WSA-2026-023 remains untouched.

**WSA-2026-022: CLOSED.**
