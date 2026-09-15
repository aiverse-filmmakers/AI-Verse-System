# A1.9 - Independent Repository Audit: AI-Verse-Automations

**Audit date:** 2026-09-15  
**Frozen ref:** `caaed83b98026dd955640fc015d181529b91a1c6`  
**System baseline:** `c4d34dcd6837fca62bbbc7e9dba5343ebb23110d`  
**Status:** COMPLETE  
**Standalone verdict:** DOGFOOD BLOCKED  
**R-a:** COMPLETE / PASS  
**R-b:** COMPLETE / MATERIAL FAILURES FOUND  
**R-c:** COMPLETE / BLOCKED  
**Findings:** `WSA-2026-026`, `WSA-2026-027`, `WSA-2026-028`  
**Next:** A1.10 AI-Verse-Connections

## Independence and drift control

A1.9 used only the frozen Automations repository, its own executable code, tests, CI, package metadata, history and documentation.

At task start and pre-write recheck:

- Automations main remained exactly `caaed83b98026dd955640fc015d181529b91a1c6`;
- System main remained `c4d34dcd6837fca62bbbc7e9dba5343ebb23110d`;
- no open scoped PR existed;
- no Automations product file was modified;
- Dashboard MC1.4 remained paused.

The frozen repository tree contains **44 tracked entries**.

## Reconstructed ownership

AI-Verse Automations is the canonical owner of:

- schedule definitions;
- trigger definitions;
- scheduled occurrence identity;
- normalized event/webhook occurrence identity;
- trigger lifecycle;
- retry/backoff/dead-letter state;
- restart/recovery metadata;
- durable run/invocation lifecycle;
- wake-delivery receipts.

It explicitly does not own:

- Brain strategic goals or cognition;
- Memory;
- Skills;
- Bot Tasks, Team Runs, Workers or execution attempts;
- Connections credentials;
- canonical business Data;
- Gateway session/run state after accepted wake delivery.

The downstream owner owns the work created by a wake.

## Scheduling and occurrence identity

Supported trigger types are:

- one-time timestamp;
- fixed interval;
- five-field cron with IANA timezone;
- authenticated webhook;
- normalized local event ingress.

Scheduled invocation identity is stable from:

`automation_id + trigger_id + exact scheduled instant`

Event/webhook invocation identity is stable from:

`automation_id + trigger_id + stable source event ID`

Event replay additionally binds source kind, source, event type and bounded event body digest.

A repeated event ID returns the prior run only when the replay semantics are unchanged. Payload drift under the same event ID fails closed.

Cron scans UTC instants and tests local representations, avoiding nonexistent local DST times and preserving repeated fall-back instants as distinct occurrences.

Recurring misfires coalesce rather than replaying an unbounded backlog.

## Claim, concurrency and retry

Scheduled due-claim and trigger advancement happen inside one `BEGIN IMMEDIATE` transaction.

The invocation ID has a UNIQUE constraint.

Concurrent due ticks therefore converge on a single durable occurrence/run.

Definition and trigger versions are execution kill fences. A pause/edit/archive after claim cancels stale work before delivery.

Every retry re-enters the OS permission check.

Retry policy is bounded by:

- maximum attempts;
- initial delay;
- exponential backoff;
- maximum delay.

Unknown crash-recovery runs are never automatically replayed.

Explicit retry of an `unknown` run requires operator confirmation that the downstream owner honors the stable invocation ID idempotently.

## Crash uncertainty

Each live claim records a process owner.

A different process owner treats an in-flight claim from the previous owner as `unknown` immediately; legacy rows without claim owner use a time cutoff.

Within the stated public-beta scope of one local scheduler service, this is intentionally conservative.

A second simultaneously live scheduler process would treat the first process's in-flight work as abandoned. Because the repository explicitly limits public beta to one local scheduler service, A1.9 records this as an operational limitation rather than a standalone defect.

## OS authority boundary

Before every delivery attempt Automations calls the OS action-permission entrypoint with:

- exact action class;
- exact operator/workspace scope;
- immutable request fingerprint.

The permission response must bind back to all three exact values.

Unknown/malformed/unavailable permission results fail closed.

`approval_required` is not treated as approval.

The run becomes blocked until an explicit recovery path is invoked later, and retry re-checks current authority.

Automation/trigger attribution is not itself permission.

## Atomic consented-definition owner path

Frozen current head adds the OS owner bridge and atomic definition creation path.

One trusted caller supplies a stable idempotency key.

Automations derives deterministic automation/trigger IDs from that key and creates both records in one transaction.

Exact replay returns the existing definition.

Semantic drift under the same idempotency key fails closed.

A trigger insert failure rolls back the Automation insert.

The generated OS bridge accepts only:

- operation `create_definition`;
- a strict definition field set;
- one trigger object;
- one stable idempotency key.

The bridge refuses operation unless the Automations owner reports `ready`.

The bridge does not itself carry a user-consent proof. Its own contract says Gateway/OS performs consent/permission provenance before invoking the owner bridge. A1.9 records that as an inbound seam claim for A2 rather than treating another component's side as proven here.

## Event and webhook ingress

Webhook triggers require:

- environment or absolute-file secret reference;
- HMAC-SHA256;
- timestamp replay window;
- bounded event ID;
- persistent event receipt;
- optional exact event-type binding.

The built-in HTTP server is loopback-only.

Remote webhook exposure is explicitly delegated to a trusted TLS/authenticated reverse proxy or tunnel.

Local event triggers bind source and optional event type exactly.

Wake/event bodies are bounded to 64 KiB.

Credentials are not accepted inline in target configuration.

Bearer credentials use environment/file references.

## Owner adapters

### Brain

Brain wake delivery passes the stable invocation ID as the Brain idempotency key.

Automations does not take Brain goal/strategy ownership.

### Multiple Bots

The adapter:

- requires workspace scope;
- requires a bounded Bot/Team Run target;
- emits the exact current receive-side compatibility payload;
- generates a projection-only source file under the OS automation tree;
- stores IDs/digests, not the objective/prompt or credentials, in that projection;
- rejects symlink escape and conflicting pre-existing projection files.

Multiple Bots remains owner of resulting coordination state.

### Gateway

Gateway receives the common stable wake envelope.

The Automations-side contract defines `invocation_id` as downstream idempotency key.

No versioned Gateway-specific receive schema is implemented in this repo yet.

Automations auto-retries retryable network/HTTP failures using the same invocation ID.

A1.9 does not classify downstream idempotency as an Automations standalone defect because the owner contract explicitly requires the stable invocation ID; whether the Gateway side actually honors that contract belongs to A2.

## Durable SQLite store

The canonical scheduler store uses SQLite/WAL and contains:

- automations;
- triggers;
- runs;
- event replay receipts;
- wake receipts;
- component metadata.

Run wake bodies and receipts are bounded.

However, the store lacks a durable ownership/format identity gate. See `WSA-2026-026`.

## C-A1.9-001 - scheduler store can adopt/mutate foreign SQLite and health does not verify Automations schema ownership

**Source A:** architecture and README describe the SQLite database as the component-owned canonical scheduler store.

**Source B:** `connect()` opens/creates whatever `automations.db` exists at the selected state directory. `initialize()` runs `CREATE TABLE IF NOT EXISTS`, may alter `runs`, then `INSERT OR REPLACE` stamps `meta.schema_version=2`.

**Source C:** no application ID, format marker, immutable ownership marker or full required-schema comparison is verified before mutation.

**Source D:** `integrity_check()` runs only SQLite `PRAGMA integrity_check`; lifecycle `descriptor()` can therefore call a structurally foreign but SQLite-valid database healthy.

**Higher-authority source:** executable database and lifecycle implementation.

**Finding:** `WSA-2026-026`.

## WSA-2026-026 - Automations canonical store has no ownership/format identity gate and can mutate a foreign SQLite file

**Severity:** HIGH  
**Confidence:** PROVEN  
**State:** OPEN  
**Root area:** canonical store ownership / lifecycle safety / health truth  
**Affected repo:** `AI-Verse-Automations`

### Summary

Setup/update do not prove that an existing `automations.db` belongs to Automations before modifying it.

A valid foreign SQLite database at the configured state path can receive Automations tables/metadata.

If similarly named tables already exist with incompatible structure, initialization may also stamp metadata or partially alter state before failing.

Lifecycle health proves only generic SQLite integrity, not Automations format identity/schema.

### Impact

This breaks fail-closed canonical-store ownership.

A custom state path, stale file, restored wrong database or operator mistake can cause a foreign SQLite file to be modified or treated as valid owner state.

The path is bounded to the explicitly selected Automations state directory, so A1.9 classifies this HIGH rather than BLOCKER.

### Required closure evidence

After repair authorization:

- introduce a durable Automations SQLite identity/format marker;
- refuse non-empty foreign databases before any schema write;
- verify exact required tables/indexes/schema version before ready state;
- make update migrations conditional on known compatible prior formats;
- add tests for foreign valid SQLite, wrong schema version, weakened/missing tables and clean new database creation.

## C-A1.9-002 - post-setup legacy definitions are detected by doctor but do not disable the active scheduler

**Source A:** README says legacy OS automation definitions produce `migration-required` and execution stays disabled to prevent competing writable authorities.

**Source B:** setup scans legacy definition paths and stores the result in component config.

**Source C:** normal status/descriptor uses only stored migration flags and does not rescan live legacy definitions.

**Source D:** `doctor()` does rescan live legacy definitions and can report the handoff check failed while returning descriptor state `ready`.

**Source E:** Engine tick/delivery never rechecks live legacy definition authority.

**Higher-authority source:** executable lifecycle/engine implementation.

**Finding:** `WSA-2026-027`.

## WSA-2026-027 - legacy definition conflict is not a live execution kill fence after setup

**Severity:** HIGH  
**Confidence:** PROVEN  
**State:** OPEN  
**Root area:** canonical schedule authority / migration handoff / readiness truth  
**Affected repo:** `AI-Verse-Automations`

### Summary

Automations correctly refuses enablement when legacy OS automation definitions exist during setup.

But that protection is snapshot-based.

If a legacy definition appears after a successful setup:

- component config remains migration-free;
- `status` can remain `ready`;
- `doctor` detects the conflict but reports the descriptor's `ready` state;
- the scheduler continues claiming/delivering Automations-owned work.

### Impact

The repo's own anti-dual-authority law is not continuously enforced.

A legacy scheduler definition introduced after setup can coexist with the active canonical Automations scheduler instead of forcing migration-required/disabled state.

A1.9 does not assume the sibling OS necessarily executes that legacy file; the standalone defect is that Automations itself recognizes the conflict in doctor but does not make it a runtime authority fence as its contract promises.

### Required closure evidence

After repair authorization:

- make live legacy-authority detection part of readiness and execution;
- status and doctor must agree;
- scheduler tick/delivery must fail closed when conflicting legacy definitions appear;
- define the explicit handoff state that clears the fence;
- add post-setup conflict injection/removal regressions.

## C-A1.9-003 - component lifecycle and OS extension registry lifecycle are unsynchronized

**Source A:** public lifecycle exposes enable, disable and uninstall; README describes uninstall/detach while preserving canonical SQLite state.

**Source B:** OS attachment records `installed:true` and an independent `enabled` flag in the OS extension registry.

**Source C:** `set_enabled()` and `uninstall()` mutate only Automations component config. No detach/removal/update path changes the OS registry entry or removes the two extension-owned bridge files.

**Source D:** the retained bridge fails closed after uninstall because owner descriptor is not ready, but host discovery can still see an installed/enabled extension.

**Higher-authority source:** executable lifecycle and OS-extension implementation.

**Finding:** `WSA-2026-028`.

## WSA-2026-028 - enable/disable/uninstall lifecycle does not synchronize attached OS extension state

**Severity:** MEDIUM  
**Confidence:** PROVEN  
**State:** OPEN  
**Root area:** native attachment lifecycle / host discovery truth  
**Affected repo:** `AI-Verse-Automations`

### Summary

Automations can attach an OS extension registry entry and owner bridge, but its main lifecycle commands do not manage that attachment afterward.

Examples:

- component `disable` can leave registry `enabled:true`;
- component `enable` can coexist with a registry entry preserved as `enabled:false`;
- `uninstall` leaves the registry entry and extension files present.

The bridge itself checks owner readiness and therefore fails closed after uninstall.

### Impact

This is primarily host lifecycle/discovery inconsistency rather than residual execution authority.

Operators and host discovery can disagree about whether Automations is installed/enabled, and lifecycle state can diverge until a manual reattachment/edit occurs.

### Required closure evidence

After repair authorization:

- either synchronize component enable/disable/uninstall with the attached registry under the existing lock/lost-update controls;
- or define a separate explicit attach/detach lifecycle and ensure status clearly represents both states;
- uninstall/detach must preserve canonical SQLite state while removing or disabling replaceable integration files/registry truth;
- add attached enable/disable/uninstall/reinstall tests.

## Native OS extension safety

The attachment implementation otherwise includes useful containment:

- fixed extension-owned paths;
- root containment;
- path segment validation;
- symlink-chain rejection;
- exclusive registry lock;
- no lock stealing;
- registry raw-text lost-update detection;
- atomic file replacement;
- preservation of unrelated registry fields/entries;
- existing disabled registration preservation;
- rollback of newly created bridge files when attachment fails.

No recursive destructive purge exists.

## Release/current-head evidence

Earlier hosted acceptance marker:

`494469a496d479cfec618bcd9511033c0cd3e815`

Frozen current head:

`caaed83b98026dd955640fc015d181529b91a1c6`

Frozen current is **10 commits ahead**.

Those commits add:

- atomic consented-definition creation;
- OS owner bridge attachment;
- associated safety/rollback tests.

Current version remains:

`ai-verse-automations 0.1.0`

The repository explicitly states it does not claim an immutable tagged public release yet.

A1.9 therefore does not open a standalone version/tag finding. A5 owns release-tag/pinning verification.

## Exact-head CI

Frozen head:

`caaed83b98026dd955640fc015d181529b91a1c6`

CI run:

`34875408692` - **SUCCESS**

All nine jobs executed and passed:

- macOS Python 3.11: `104081254561`
- Windows Python 3.13: `104081254591`
- Ubuntu Python 3.12: `104081254613`
- Ubuntu Python 3.13: `104081254694`
- Windows Python 3.12: `104081254701`
- macOS Python 3.13: `104081254715`
- Ubuntu Python 3.11: `104081254743`
- macOS Python 3.12: `104081254781`
- Windows Python 3.11: `104081254842`

Each job executed:

- checkout;
- Python setup;
- pip upgrade;
- editable package + pytest install;
- compileall;
- full pytest suite;
- CLI install smoke.

This is real executed current-head cross-platform evidence.

## Negative-space checks

A1.9 found no evidence that Automations:

- becomes Brain goal/strategy owner;
- becomes Memory owner;
- becomes Skills owner;
- becomes Bot Task/Team Run/Worker owner;
- stores target bearer credentials directly;
- grants workspace/action authority from schedule state;
- treats `approval_required` as approval;
- skips OS permission re-check on retry;
- silently replays `unknown` crash deliveries;
- changes invocation ID during explicit unknown recovery;
- allows mutable remote schedule-control HTTP endpoints;
- binds its built-in HTTP server to non-loopback interfaces;
- accepts credential-bearing target URLs;
- lets event replay drift under the same event ID;
- replays an unbounded schedule backlog after outage;
- lets definition edits bypass version kill fences;
- writes Multiple Bots objective/prompt content into compatibility projection files;
- steals an existing OS extension registry lock;
- recursively purges canonical scheduler state during uninstall.

## Evidence limitations / A2 claims

A1.9 does not independently prove sibling behavior.

Claims carried into A2 include:

- OS permission responses are the current scope/action authority floor;
- Gateway/OS provides trusted consent provenance before invoking the atomic owner bridge;
- Brain honors the supplied idempotency key;
- Multiple Bots validates the projection/source binding and invocation ID;
- Gateway honors `invocation_id` as its downstream idempotency key.

The public-beta one-local-scheduler-process constraint is accepted as explicit scope for A1.9. Multi-live-process scheduler ownership remains a future hardening concern unless later whole-system evidence makes it reachable in the supported journey.

## Evidence IDs

- `E-A1.9-001` frozen Automations tree/repository metadata.
- `E-A1.9-002` README/manifest/package ownership identity.
- `E-A1.9-003` architecture/owner contract.
- `E-A1.9-004` schedule parser/DST/misfire behavior.
- `E-A1.9-005` canonical SQLite schema.
- `E-A1.9-006` database initialize/connect/integrity implementation.
- `E-A1.9-007` automation/trigger store validation.
- `E-A1.9-008` atomic definition creation/idempotency.
- `E-A1.9-009` due-claim transactional concurrency.
- `E-A1.9-010` definition/version kill fences.
- `E-A1.9-011` OS permission binding/retry reauthorization.
- `E-A1.9-012` crash recovery/unknown retry.
- `E-A1.9-013` event replay/source/type binding.
- `E-A1.9-014` webhook HMAC/replay-window implementation.
- `E-A1.9-015` target credential/network validation.
- `E-A1.9-016` Brain owner adapter.
- `E-A1.9-017` Multiple Bots compatibility projection/payload.
- `E-A1.9-018` generic Gateway owner adapter and stable envelope.
- `E-A1.9-019` lifecycle setup/status/doctor/enable/disable/update/uninstall.
- `E-A1.9-020` live legacy-definition discovery behavior.
- `E-A1.9-021` OS extension registry/owner bridge implementation.
- `E-A1.9-022` OS extension attachment tests.
- `E-A1.9-023` current-head CI run `34875408692`.
- `E-A1.9-024` nine exact-head successful CI jobs.
- `E-A1.9-025` accepted marker to frozen-current 10-commit comparison.
- `E-A1.9-026` live pre-write ref/open-PR recheck.

## Verdict and progress

**AI-Verse-Automations at `caaed83b98026dd955640fc015d181529b91a1c6`: AUDIT COMPLETE, DOGFOOD BLOCKED.**

New findings:

1. `WSA-2026-026` HIGH - canonical SQLite ownership/format identity is not enforced.
2. `WSA-2026-027` HIGH - post-setup legacy definition conflict is not a live scheduler kill fence.
3. `WSA-2026-028` MEDIUM - component lifecycle and attached OS registry lifecycle diverge.

No Automations product repair is made during A1.9.

After acceptance:

- weighted audit: **23 / 100 = 23%**
- remaining: **77%**
- tasks: **14 / 51 complete**
- tasks remaining: **37 / 51**
- phases fully complete: **1 / 7**
- phases incomplete: **6 / 7**
- A1 repositories: **9 / 14 complete**
- A1 repositories remaining: **5 / 14**
- A1 weight: **18 / 28**
- next task: **A1.10 AI-Verse-Connections**
