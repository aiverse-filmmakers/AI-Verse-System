# A1.7 - Independent Repository Audit: AI-Verse-Multiple-Bots

**Audit date:** 2026-09-15  
**Frozen ref:** `c600e2bc014351a61e1c0e2673fc63f5d5fa54ec`  
**System baseline:** `e881cc2759583fd7727848bf3be5f6da6449c047`  
**Status:** COMPLETE  
**Standalone verdict:** DOGFOOD BLOCKED  
**R-a:** COMPLETE / PASS  
**R-b:** COMPLETE / MATERIAL FAILURES FOUND  
**R-c:** COMPLETE / BLOCKED  
**Findings:** `WSA-2026-022`, `WSA-2026-023`  
**Next:** A1.8 ai-verse-token

## Independence and drift control

A1.7 used only the frozen Multiple Bots repository, its own tests, workflows, package metadata, history and documentation.

Pre-task and pre-write checks confirmed:

- Multiple Bots main remained `c600e2bc014351a61e1c0e2673fc63f5d5fa54ec`;
- System main remained `e881cc2759583fd7727848bf3be5f6da6449c047`;
- no open scoped PR existed;
- no Multiple Bots product file was modified;
- Dashboard MC1.4 remained paused.

The frozen repository tree contains **234 tracked entries**.

## Reconstructed ownership

Multiple Bots is the canonical coordination layer for persistent Bots and bounded temporary Workers.

It owns:

- durable Bot coordination identity;
- Bot relationships;
- Rooms and Threads;
- Messages and delivery state;
- Tasks and delegation;
- Handoffs and work ownership;
- Team Runs;
- temporary Workers;
- capability/environment coordination leases;
- coordination Approval lifecycle;
- coordination Artifact references;
- coordination Events;
- execution queue/recovery state;
- coordination budgets and runtime settlement evidence.

It does not claim canonical ownership of:

- OS workspace truth or outer policy;
- Brain goals/strategy;
- Memory durable historical knowledge;
- Skills trust authority;
- Data structured canonical records;
- Connections credentials;
- Automations scheduling;
- Dashboard presentation truth;
- Token normalized telemetry, pricing evidence or canonical cost truth.

## Durable Bots and temporary Workers

Managed Team Run creation binds Workers to their Team Run/workspace and the execution runner verifies:

- Task owner/assignee;
- workspace;
- run ID;
- Worker Task binding;
- capability lease;
- environment lease;
- lease expiry;
- execution ownership;
- budget inheritance.

This managed path is strong.

For durable Bots, coordination policy verifies active registration, exact workspace, peer permissions, requested tool/connection authority, declared Skill refs, hop limits, inherited constraints, deadlines, budgets and loop/duplicate limits.

Handoffs preserve immutable constraints and transfer leases rather than widening them.

## Remote execution authority

Remote capability/environment leases are fail-closed and narrower than local authority:

- remote expiry cannot exceed local expiry;
- remote tools/connections must be subsets;
- destructive-action policy cannot widen;
- remote environment must match local environment authority;
- receipts must bind the exact grant;
- recovery replacement must preserve effective authority.

No remote-authority expansion defect was found.

## Execution, concurrency and recovery

Canonical coordination state is SQLite-backed with explicit queue ownership and lease state.

Verified properties include:

- claimed execution ownership;
- atomic Task/queue transitions where required;
- Handoff retarget checks;
- runner-ownership checks before complete/fail/cancel;
- replay-safe stale execution may be requeued;
- other stale execution dead-letters;
- Team Run cancellation/budget exhaustion fences the run and performs bounded cleanup;
- dead-letter retry is explicit.

No higher-severity concurrency or recovery defect was found in the standalone repository.

## Token ownership boundary

Multiple Bots does **not** create a second canonical Token owner.

Executable observability code declares:

- `canonical_telemetry_owner = ai-verse-token`;
- `canonical_cost_truth_owner = ai-verse-token`;
- `token_projection_interface = @ai-verse/token/gateway`;
- `prices_model_usage_here = false`;
- `writes_token_telemetry_here = false`;
- `runtime_usage_is_canonical_token_truth = false`.

Runtime monetary evidence is labeled `runtime_reported_cost_evidence`.

Multiple Bots retains execution-local usage only for coordination budgets, limits, settlement and operational observability. Canonical normalized telemetry and pricing/cost truth remain delegated to Token.

## Other owner boundaries

- OS canonical writes use the owner-controlled write-command boundary.
- Brain integration consumes Brain-owned objective state rather than becoming goal owner.
- Memory integration is recall/projection oriented.
- Skill references are capability references rather than competing Skills ownership.
- Automation ingress consumes invocation state rather than becoming the scheduler.
- Channel bridges map verified provider ingress into canonical coordination without becoming credential owner.

## Secure remote transport

Direct non-loopback Gateway HTTP binding is rejected.

Managed remote access uses Tailscale Serve to a loopback Gateway plus bearer authentication.

The repository's own security contract states that transport authentication grants Gateway access but **does not grant domain authority**.

That contract is contradicted by the operator-control implementation described below.

## Native install/update/uninstall

The native OS lifecycle is strongly bounded.

Verified controls include:

- compatible host required;
- extension-owned files only;
- traversal rejection;
- symlink-chain rejection for owned paths;
- malformed/foreign same-key registry state fails closed;
- exclusive registry lock;
- registry re-read under lock;
- compare-before-replace registry writes;
- user-disabled state preserved;
- unknown registry metadata preserved;
- unrelated extensions preserved;
- uninstall removes only registered regular files inside the owned extension root;
- unknown files are not recursively scavenged;
- coordination DB is preserved;
- canonical host/workspace state is preserved.

No destructive-lifecycle finding is opened for Multiple Bots.

## C-A1.7-001 - transport authentication and operator domain authority are not bound together

**Source A:** the security contract states that Gateway transport authentication does not grant domain authority.

**Source B:** sensitive mutation surfaces accept an operator actor identifier from request input, while core operator validation is only syntactic rather than bound to trusted authenticated identity.

**Higher-authority source:** executable server, Gateway, recovery and control implementation.

**Finding:** `WSA-2026-022`.

## WSA-2026-022 - operator/domain authority is not bound to trusted authenticated identity

**Severity:** HIGH  
**Confidence:** PROVEN  
**State:** OPEN  
**Root area:** approval/operator/domain authority binding  
**Affected repo:** `AI-Verse-Multiple-Bots`

### Summary

The remote-transport contract distinguishes Gateway access from domain authority, but sensitive operator actions are authorized using caller-supplied actor identity rather than trusted authenticated operator identity.

Affected control classes include:

- durable Bot lifecycle;
- external-managed Bot rebinding;
- Approval decisions;
- dead-letter retry;
- Task/Team Run cancellation and related operator controls.

### Impact

A caller that legitimately reaches the Gateway transport can be treated as an operator by domain logic without a second trusted identity binding.

The repo does not need hosted multi-user RBAC to close this. It does need operator authority to come from trusted host/session identity rather than caller-selected provenance.

### Required closure evidence

After repair authorization:

- bind operator authorization to trusted host/authentication state;
- keep provenance actor IDs separate from authorization;
- define which authenticated principals may perform operator controls;
- add negative tests proving Gateway access alone cannot satisfy operator-only mutations.

## C-A1.7-002 - generic Worker policy does not preserve the managed Worker workspace invariant

**Source A:** architecture/release law says temporary Workers are Team Run/workspace scoped and authority may narrow but not expand.

**Source B:** generic coordination workspace policy is Bot-specific, so Worker principals can bypass the same pre-persistence workspace check.

**Source C:** the runner later detects the mismatched Worker/Task workspace, but its generic failure path can still update the resolved Worker state.

**Higher-authority source:** executable policy, public delegation path, store/queue behavior and principal runner.

**Finding:** `WSA-2026-023`.

## WSA-2026-023 - generic Worker delegation can cross workspace scope and mutate the foreign Worker

**Severity:** HIGH  
**Confidence:** PROVEN  
**State:** OPEN  
**Root area:** Worker workspace isolation / canonical coordination authority  
**Affected repo:** `AI-Verse-Multiple-Bots`

### Summary

Managed Team Run Worker creation is correctly workspace-bound, but the generic coordination path does not apply equivalent Worker scope checks before persisting delegation/message state.

A Worker from one workspace can therefore be targeted by generic coordination state declared under another workspace.

The execution runner correctly refuses to run a mismatched Task, but its generic failure handling can still update the real Worker's canonical status after that rejected foreign-workspace Task is claimed.

Direct Worker message delivery has a related scope-validation weakness.

### Impact

This is a canonical cross-workspace coordination corruption/denial path.

A1.7 does **not** classify it as external tool/credential takeover because runtime execution is blocked once the runner detects the mismatch.

### Required closure evidence

After repair authorization:

- make Workers first-class principals in generic workspace checks;
- reject foreign-workspace Worker delegation before Task/lease/queue persistence;
- validate Worker message target workspace;
- ensure runner failure/cancel paths cannot mutate a Worker until Task/Worker/run scope binding is proven;
- add two-workspace adversarial regressions.

## Release identity and exact-head acceptance

Original beta.1 release merge:

`9bffdffd07fb8abcea848213642936a23ecf4ecf`

Frozen current main:

`c600e2bc014351a61e1c0e2673fc63f5d5fa54ec`

Frozen current is **19 commits ahead** and includes newer temporary-Worker and durable-Bot owner entrypoints.

A1.7 does not open a standalone version-drift finding because:

- beta.1 is explicitly a source candidate;
- the repo explicitly does not claim immutable Git tagging or npm publication;
- frozen current-head CI reruns the component release evaluation successfully;
- immutable/composed release truth belongs to A5.

A5 must still re-evaluate this evidence.

## Exact-head CI

Frozen head:

`c600e2bc014351a61e1c0e2673fc63f5d5fa54ec`

CI run:

`34872178884` - **SUCCESS**

Job:

`104070507325` - **SUCCESS**

Executed and passed:

- checkout;
- Node setup;
- dependency install;
- `npm test`;
- `npm run eval:phase4`;
- `npm run pack:check`;
- `npm run eval:release`.

This is real executed CI, not a no-step runner artifact.

## Negative-space checks

A1.7 found no evidence that Multiple Bots:

- creates a second canonical Token telemetry/pricing ledger;
- independently prices model usage as canonical truth;
- opens Data storage as a competing structured-data engine;
- takes Brain or Memory canonical ownership;
- stores Connections credentials as its own authority;
- becomes the Automations scheduler;
- lets Dashboard become coordination truth;
- widens remote leases beyond local authority;
- silently promotes Workers into durable Bots;
- lets normal Handoff drop immutable constraints;
- executes approval-gated Tasks before approval;
- auto-retries non-replay-safe stale execution;
- recursively purges unknown extension files;
- deletes coordination history during OS uninstall;
- steals another installer registry lock;
- permits direct non-loopback Gateway binding.

## Evidence limitations

- A1.7 does not validate sibling implementations.
- Token itself is not audited here.
- Whole-system permission composition belongs to A2.
- Release/tag/npm evidence belongs to A5.
- No product repair or reproduction test was added during A1.7.

## Evidence IDs

- `E-A1.7-001` frozen repository tree and metadata.
- `E-A1.7-002` ownership reconstruction.
- `E-A1.7-003` Bot/Worker distinction and managed Team Run Worker binding.
- `E-A1.7-004` durable Bot coordination policy.
- `E-A1.7-005` remote lease narrowing and receipt checks.
- `E-A1.7-006` operational budget enforcement.
- `E-A1.7-007` Token observability ownership boundary.
- `E-A1.7-008` execution queue/concurrency/recovery implementation.
- `E-A1.7-009` Handoff ownership/lease transfer.
- `E-A1.7-010` secure remote Gateway contract.
- `E-A1.7-011` bearer/loopback implementation.
- `E-A1.7-012` public operator-control routes.
- `E-A1.7-013` operator validation implementation.
- `E-A1.7-014` release acceptance security interpretation.
- `E-A1.7-015` generic Worker policy scope behavior.
- `E-A1.7-016` generic delegation route.
- `E-A1.7-017` Worker execution workspace validation.
- `E-A1.7-018` runner failure Worker update path.
- `E-A1.7-019` Worker mailbox/delivery scope behavior.
- `E-A1.7-020` OS write-command owner boundary.
- `E-A1.7-021` Brain/Memory/Skills/Automations boundary evidence.
- `E-A1.7-022` native registry/materialization/lifecycle.
- `E-A1.7-023` uninstall ownership/preservation tests.
- `E-A1.7-024` exact-head CI run `34872178884`.
- `E-A1.7-025` exact-head CI job `104070507325`.
- `E-A1.7-026` beta.1 release merge to frozen-current comparison.
- `E-A1.7-027` current release-evaluation source.
- `E-A1.7-028` live pre-write frozen-ref/open-PR recheck.

## Verdict and progress

**AI-Verse-Multiple-Bots at `c600e2bc014351a61e1c0e2673fc63f5d5fa54ec`: AUDIT COMPLETE, DOGFOOD BLOCKED.**

New findings:

1. `WSA-2026-022` HIGH - operator/domain authority binding.
2. `WSA-2026-023` HIGH - Worker workspace isolation/canonical mutation.

No Multiple Bots product repair is made during A1.7.

After acceptance:

- weighted audit: **19 / 100 = 19%**
- remaining: **81%**
- tasks: **12 / 51 complete**
- tasks remaining: **39 / 51**
- phases fully complete: **1 / 7**
- phases incomplete: **6 / 7**
- A1 repositories: **7 / 14 complete**
- A1 repositories remaining: **7 / 14**
- A1 weight: **14 / 28**
- next task: **A1.8 ai-verse-token**
