# WSA-2026-030 Closure — Connections Installation/System Binding

**Finding:** `WSA-2026-030`  
**Severity / confidence:** HIGH / PROVEN  
**Owner:** `AI-Verse-Connections`  
**Repair wave:** R1.6  
**Closure date:** 2026-09-18  
**State:** **CLOSED**

## 1. Finding

Connections setup claimed to bind one Connections installation/home to an explicit AI-Verse system ID, but that lifecycle binding was not authoritative.

Before repair:

- lifecycle setup stored `lifecycle.systemId`;
- Generic and MCP connection registration accepted any caller-supplied `systemId`;
- verify/admit/approve state transitions trusted the connection record without checking the installation binding;
- execution compared request system ID only with connection system ID;
- provider-edge execution reloaded the connection but did not require its system ID to equal the installation lifecycle system ID;
- rerunning setup could replace the lifecycle system ID without reconciling existing connections.

Therefore one Connections home could hold and execute external authority for a system other than the system to which setup claimed the installation was bound.

Canonical contradiction: `C-A1.10-002`.

Primary evidence: `E-A1.10-005`, `E-A1.10-006`, `E-A1.10-010`, `E-A1.10-011`.

Required closure law:

1. exact lifecycle-system binding at connection creation;
2. exact lifecycle-system binding across authority-raising connection state transitions;
3. lifecycle-system binding rechecked at the provider edge;
4. ordinary setup cannot silently rebind an existing installation;
5. an explicit migration/rebind workflow exists;
6. two-system negative regressions cover add/verify/admit/approve/execute and setup rebind.

## 2. Baseline and repair identity

**Audited/live pre-repair Connections ref:** `a04f655c6f0c9b57d17e64b5c1ff8eb88aab4016`  
**Open Connections PRs before repair:** 0

**Repair branch:** `repair/wsa-2026-030-installation-system-binding`  
**Repair PR:** `AI-Verse-Connections#3`  
**Final reviewed head:** `8f724c74aef5b8dc22d138f9115f0b1d8de55cb7`  
**Merged Connections ref:** `ac8e34cffeaaa0417aaf5011a2379af1b044bf96`  
**Reviewed/merged product tree:** `0c32b64c87338f708990cc37f218b1c8a86669a5`

The reviewed PR tree and merged `main` tree are byte-identical.

Open Connections PRs after merge: **0**.

## 3. Final implementation contract

### 3.1 Setup system ID is now canonical

A shared installation-system guard now treats lifecycle `systemId` as the canonical installation binding.

A connection system ID that differs from that lifecycle binding fails with:

`SYSTEM_BINDING_MISMATCH`

Missing installation binding fails with:

`SYSTEM_BINDING_REQUIRED`

### 3.2 Connection creation is bound under the canonical state lock

Both Generic and MCP registration now check the requested connection system ID against lifecycle `systemId` inside the registry mutation lock before persistence.

This closes the original supported path:

`setup(sys-a) -> add connection(sys-b)`

The foreign connection is rejected before it enters canonical registry state.

### 3.3 Authority-raising state transitions recheck the installation binding

The following paths now require the connection's system ID to match lifecycle `systemId`:

- live verification;
- capability admission;
- connection approval;
- reauthentication.

Verification checks the binding before the provider health/discovery request and rechecks it again before committing successful verification state.

Revocation remains available as a narrowing/safety operation even for malformed legacy state.

### 3.4 Execution checks binding at planning and provider edge

Execution still performs the existing lifecycle-ready check at entry.

Connection lookup was changed to an installation-bound snapshot for:

1. initial planning; and
2. the mandatory final provider-edge authority reload.

The final binding snapshot reads lifecycle and registry state under the same Connections state lock.

This closes the audited case where request `sys-b` and connection `sys-b` agreed while the installation itself was bound to `sys-a`.

This repair intentionally checks **system identity only** at the final edge. It does not close WSA-2026-032's separate lifecycle-ready/budget recheck requirements.

### 3.5 Ordinary setup cannot silently rebind

Calling `setup` with a different system ID after a lifecycle binding already exists now fails with:

`SYSTEM_REBIND_REQUIRED`

Setup also inspects the registry under the same state lock and refuses to bind when any existing connection belongs to another system, including legacy state where lifecycle `systemId` is missing.

Repeated setup with the same system ID remains supported.

### 3.6 Explicit system migration/rebind workflow

A new explicit workflow is available:

`rebind-system --from-system <old> --system <new>`

Programmatic equivalent:

`rebindSystem({ fromSystemId, systemId })`

The operation requires the caller to state the expected current system ID. A mismatch fails with:

`SYSTEM_REBIND_SOURCE_MISMATCH`

Connections outside the declared source/target pair fail with:

`SYSTEM_REBIND_FOREIGN_CONNECTION`

The workflow is advertised in the component descriptor and README.

### 3.7 Rebind invalidates authority in the new system

Under the canonical state lock, rebind migrates every eligible connection to the target system and clears:

- live verification;
- health;
- authorization;
- approval;
- last verification timestamp;
- capability admission.

Capabilities are marked review-required and any stored approval record is removed.

Therefore external authority is not silently transferred to the new AI-Verse system. Each migrated connection must be freshly verified, re-admitted and approved.

### 3.8 Interrupted rebind is fail-closed and retryable

The explicit migration writes the registry before lifecycle.

If the process stops after the registry commit but before the lifecycle commit:

- migrated connection IDs already point to the target system;
- lifecycle still points to the old system;
- all installation-bound connection operations reject the mismatch;
- no migrated connection can execute.

Retrying the same explicit source→target rebind accepts target-system connection records as an interrupted transition, reapplies authority invalidation, and completes the lifecycle write.

### 3.9 Doctor exposes corrupted/legacy binding state

Doctor now includes a structural `system-binding` check for each connection.

A foreign connection therefore prevents doctor from reporting an overall healthy/ready result even before that connection is used.

## 4. Permanent two-system regressions

`test/connections-system-binding.integration.test.js` contains dedicated WSA-2026-030 regressions for:

1. Generic add under `sys-b` after setup `sys-a`;
2. MCP add under `sys-b` after setup `sys-a`;
3. verify rejection before any network request for foreign legacy state;
4. capability-admission rejection for foreign legacy state;
5. approval rejection for foreign legacy state;
6. doctor detection of foreign system binding;
7. execution where request and connection agree on `sys-b` but installation is `sys-a`;
8. provider-edge lifecycle binding change after planning;
9. ordinary setup rebind rejection;
10. explicit source-system mismatch rejection;
11. explicit migration from `sys-a` to `sys-b`;
12. forced loss of verify/authorize/approve/admit state during migration;
13. old-system execution rejection after migration;
14. new-system execution only after fresh verify/admit/approve;
15. setup rejection against a legacy foreign registry when lifecycle binding is missing;
16. recovery from a registry-first interrupted migration;
17. rejection of undeclared third-system registry state.

## 5. Validation evidence and CI limitation

### Exact-head static syntax validation

Every changed JavaScript source/test file on final head `8f724c74aef5b8dc22d138f9115f0b1d8de55cb7` passed V8 syntax parsing:

- `src/cli.js`;
- `src/service-admission.js`;
- `src/service-execute.js`;
- `src/service-lifecycle.js`;
- `src/service-registry.js`;
- `src/state-store.js`;
- `src/system-binding.js`;
- `test/connections-system-binding.integration.test.js`.

### Exact-head structural recheck

The final head was programmatically inspected for every required binding edge.

All checked conditions were present:

- setup rebind guard;
- foreign-registry setup guard;
- explicit rebind workflow;
- source-ID binding;
- third-system rejection;
- authority invalidation;
- Generic add binding;
- MCP add binding;
- verify pre-network binding;
- verify pre-commit binding;
- admission/approval/reauth binding;
- initial execution binding;
- final-edge execution binding;
- all dedicated two-system/recovery regression cases.

Result: **all structural checks PASS**.

### Hosted CI infrastructure limitation

Final PR-head Actions run:

`35334960224`

Post-merge Actions run:

`35335199615`

Both runs created the expected six Ubuntu/macOS/Windows × Node 20/22 jobs, but every job returned:

- `steps: null`;
- no checkout step;
- no dependency install step;
- no test step.

Therefore the hosted runner did **not execute product code or regressions**.

This is the inherited private-repository/no-runner infrastructure condition already tracked separately as `WSA-2026-003`. It is not recorded as a Connections product-test failure, and this closure does not close or reclassify WSA-2026-003.

No passing hosted test count is claimed for this repair.

## 6. Finding-specific recheck

### C-A1.10-002

**RESOLVED for WSA-2026-030.**

The installation lifecycle system ID is now an enforced authority input rather than descriptive setup metadata.

### Creation seam

**PASS by exact-code recheck.**

Generic and MCP persistence require exact lifecycle-system equality while holding the canonical registry mutation lock.

### Verify/admit/approve seam

**PASS by exact-code recheck.**

Foreign legacy connection state cannot be verified, admitted or approved against another installation system.

### Execution seam

**PASS by exact-code recheck.**

A request cannot execute merely because it matches a foreign connection record; connection and installation binding must also match.

### Final-edge seam

**PASS by exact-code recheck.**

The connection is reloaded through an installation-bound snapshot immediately before provider execution.

### Setup/rebind seam

**PASS by exact-code recheck.**

Ordinary setup cannot change the binding. Explicit rebind is source-bound, registry-validated, authority-resetting and fail-closed under interrupted migration.

### Diagnostic seam

**PASS by exact-code recheck.**

Doctor detects connection/lifecycle system mismatch.

## 7. Adjacent findings remain open

This closure is limited to `WSA-2026-030`.

The following Connections findings remain **OPEN** and were intentionally not repaired here:

- `WSA-2026-031` — MCP credential-origin binding on reauth/verify;
- `WSA-2026-033` — normalized path authorization;
- `WSA-2026-051` — DNS/private-network containment;
- `WSA-2026-032` — complete final-edge lifecycle and budget authority;
- later Connections findings in the ordered program.

In particular:

- MCP cross-origin credential reuse logic is unchanged;
- Generic normalized path authorization is unchanged;
- DNS/private-network resolution logic is unchanged;
- execution does not newly re-read lifecycle ready/enabled state or atomically reserve rate budgets at the final edge.

## 8. Closure verdict

Required WSA-2026-030 product changes are present on the merged owner tree:

- lifecycle system binding is canonical;
- creation enforces it;
- verify/admit/approve/reauth enforce it;
- provider-edge execution rechecks it;
- setup cannot silently change it;
- an explicit source-bound migration/rebind workflow exists;
- migrated authority is invalidated;
- interrupted migration is fail-closed and retryable;
- two-system and recovery regressions are permanently present;
- doctor exposes corrupted binding state;
- reviewed and merged trees are identical;
- open owner PRs are zero.

Hosted regression execution remains unavailable because of separate open infrastructure finding WSA-2026-003; no green CI claim is made.

**WSA-2026-030: CLOSED.**
