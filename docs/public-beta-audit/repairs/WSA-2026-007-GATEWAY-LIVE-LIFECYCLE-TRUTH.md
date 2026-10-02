# WSA-2026-007 Closure - Gateway Live Lifecycle Truth

**Finding:** `WSA-2026-007`  
**Severity / confidence:** HIGH / PROVEN  
**Owner:** `AI-Verse-Gateway`  
**Repair wave:** R2.1  
**Closure date:** 2026-10-02  
**State:** **CLOSED**

## 1. Finding

Gateway lifecycle state was persisted on disk but was not operationally authoritative for a process that had already started.

The audited implementation allowed several contradictions:

- setup wrote `config.json` before config validation and host verification had completed;
- failed setup could therefore leave a configuration that later CLI status interpreted as ready;
- disable changed `config.json` only, while an already-running server continued serving from its startup snapshot;
- live `/status` used the stale in-memory config;
- doctor did not represent an intentional disabled state;
- normal uninstall removed integration/config files but did not stop or fence an already-running listener;
- the existing clean-install test closed the server before disable/uninstall and therefore did not test the live seam.

Canonical contradiction: `C-A1.2-001`.

Required closure evidence:

- validate configuration and host compatibility before publishing ready setup state, or rollback transactionally;
- establish one authoritative live lifecycle mechanism;
- make disable/uninstall stop or fence an already-running server from further operational requests;
- align CLI status, doctor and live status around disabled/absent/ready lifecycle truth;
- test live disable/uninstall, failed setup rollback, invalid remote setup and restart behavior.

## 2. Baseline and repair identity

**Pre-repair Gateway ref:** `5347a0b7e3f3f302f4570e9bc37d515192753610`  
**Open Gateway PRs before repair:** 0

**Repair branch:** `repair/wsa-2026-007-live-lifecycle-truth`  
**Repair PR:** `AI-Verse-Gateway#33`  
**Final tested PR head:** `8f19c4e70a4014c6e1ab164753999be85e9e3fd4`  
**Merged Gateway ref:** `b27cebe11e536aa5a0f9bad707f38b0c2471879d`  
**Tested/merged product tree:** `f25d6483395416affdf55fe8c05933163594740e`

The exact tested PR head and merged `main` commit have the same product tree.

Open Gateway PRs after merge: **0**.

## 3. Final implementation contract

### 3.1 One authoritative lifecycle reader

Gateway now has one shared lifecycle-state reader used by lifecycle commands and the live server.

It derives operational state from current owner files, not from an old process snapshot:

- `absent` when the install marker is absent;
- `setup-required` when installed but no config is published;
- `unhealthy` when current config cannot be loaded/validated;
- `disabled` when current config is valid but disabled;
- `ready` when current config is valid and enabled.

A live process additionally evaluates its setup generation. If disk setup has been replaced since that process started, the process reports:

- `restart-required`

and refuses operational traffic.

### 3.2 Setup validates before ready publication

`setupComponent()` no longer publishes canonical ready configuration before its own validation finishes.

The repair now:

1. constructs the candidate host/runtime/config state;
2. validates the full Gateway config, including remote-bind safety;
3. verifies the candidate OS host adapter through `describe`;
4. requires the host to prove `metadata.canonical_state_owned === false`;
5. publishes verified host/goal adapter config;
6. publishes `config.json` last as the ready-state edge.

A failed candidate host verification does not replace an existing ready configuration.

A failed first-time setup leaves the component in `setup-required`, not `ready`.

### 3.3 Invalid remote setup cannot publish ready state

Unsafe remote configuration is rejected by `validateConfig()` before canonical ready publication.

For example, a non-loopback host without both explicit remote permission and trusted TLS-proxy declaration fails with `REMOTE_BIND_UNSAFE`.

The permanent regression proves no canonical config or host adapter is published on that failed setup.

### 3.4 Setup generation fences stale live processes

Every successful new setup now receives an opaque `service_generation`.

Disable/enable preserves the same generation.

A new setup or uninstall/reinstall setup produces a new generation.

A running server captures the generation it was admitted under. Every request re-reads disk lifecycle state and compares the current setup generation with that captured generation.

If generation changed, the old process becomes `restart-required` and cannot resume operational service merely because a new ready config appeared at the same home path.

This prevents stale-process resurrection after uninstall/reinstall or live re-setup.

Legacy configs without a generation remain readable; a subsequent repaired setup moves them onto the generation-fenced contract.

### 3.5 Server start uses current owner lifecycle truth

`startServer()` no longer trusts a previously loaded config as sufficient lifecycle authority.

Before starting it:

- preserves the existing early remote-bind security rejection for unsafe serve-time host overrides;
- re-reads current on-disk lifecycle;
- requires current state to be `ready`;
- uses the authoritative current config;
- rejects a stale supplied config whose setup generation no longer matches.

The remote-bind policy is then checked again against the authoritative disk config before listen.

### 3.6 Every live request rechecks lifecycle state

The live server re-reads lifecycle state for every request.

The listener may remain bound so operators can inspect diagnostics, but only `ready` state may reach normal operational routes.

The following are fenced before operational route handling:

- `absent`;
- `setup-required`;
- `unhealthy`;
- `disabled`;
- `restart-required`.

This means disable/uninstall do not depend on separately discovering and killing a service process in order to become operationally authoritative.

### 3.7 Live diagnostic semantics

`GET /health` now reports current lifecycle state.

- ready: HTTP 200, `ok: true`;
- non-ready lifecycle states: HTTP 503, `ok: false`.

Authenticated `GET /status` remains available on the already-running process so an operator can see its current lifecycle state even after disable/uninstall.

Operational routes such as model, chat, run, Automation wake and run-control surfaces are rejected while non-ready.

### 3.8 Disable/enable is live

While a server is already running:

- `disable` changes owner state to disabled;
- CLI `status` reports disabled;
- CLI `doctor` reports disabled;
- live `/status` reports disabled;
- live `/health` reports disabled / 503;
- operational requests receive `GATEWAY_DISABLED`;
- a new server start while disabled is rejected.

Re-enable with the same setup generation returns both disk and the already-running process to ready state.

### 3.9 Uninstall is live

While a server is already running:

- normal uninstall removes live setup/install authority while preserving Gateway-owned canonical state as designed;
- CLI `status` reports absent;
- CLI `doctor` reports absent;
- live `/status` reports absent;
- live `/health` reports absent / 503;
- operational requests receive `GATEWAY_ABSENT`;
- a new server start from stale pre-uninstall config is rejected.

The listener may remain bound only as a fenced diagnostic process until explicitly closed.

### 3.10 Reinstall requires a fresh process

After uninstall + reinstall + setup:

- owner status/doctor return ready for the new setup;
- a previously running process detects the new generation and reports `restart-required`;
- that stale process returns `GATEWAY_RESTART_REQUIRED` for operational traffic;
- starting from the old config is rejected;
- starting from the newly loaded config succeeds;
- the fresh process serves ready traffic normally.

This is the required restart/recovery behavior for the live lifecycle seam.

## 4. Permanent regressions

Dedicated coverage was added in:

`test/live-lifecycle-authority.test.mjs`

It proves:

1. successful setup reaches ready;
2. an incompatible host candidate fails before replacing an existing ready setup;
3. existing config remains byte-identical after failed host verification;
4. existing host config remains byte-identical after failed host verification;
5. failed first-time host setup leaves status at setup-required;
6. failed first-time host setup publishes neither config nor canonical host adapter;
7. invalid remote setup fails with `REMOTE_BIND_UNSAFE`;
8. invalid remote setup leaves status and doctor at setup-required;
9. invalid remote setup publishes neither config nor canonical host adapter;
10. live CLI status and doctor start at ready;
11. live `/status` and `/health` start at ready;
12. disable while live immediately changes CLI status/doctor to disabled;
13. live `/status` changes to disabled;
14. live health changes to 503/disabled;
15. live operational requests fail with `GATEWAY_DISABLED`;
16. starting another process while disabled fails;
17. re-enable restores the same live process to ready;
18. operational traffic resumes after enable;
19. uninstall while live changes CLI status/doctor to absent;
20. live `/status` changes to absent;
21. live health changes to 503/absent;
22. operational requests fail with `GATEWAY_ABSENT`;
23. server start from the pre-uninstall config fails;
24. reinstall/setup creates a new service generation;
25. the old live process reports restart-required instead of silently reviving;
26. the old live process rejects operational traffic with `GATEWAY_RESTART_REQUIRED`;
27. the stale pre-uninstall config cannot start against the new generation;
28. a server started with the new authoritative config succeeds and serves ready traffic.

The existing remote-bind regression also remains green, proving lifecycle admission did not weaken the earlier serve-time host override security boundary.

## 5. Validation evidence

### Final PR-head CI

Final PR-head CI run:

`37032145023`

On exact final head `8f19c4e70a4014c6e1ab164753999be85e9e3fd4`:

- Ubuntu / Node 20: **PASS**
- Ubuntu / Node 22: **PASS**
- macOS / Node 20: **PASS**
- macOS / Node 22: **PASS**
- Windows / Node 20: **PASS**
- Windows / Node 22: **PASS**

Representative Ubuntu Node 22 suite:

- tests: **107**
- passed: **107**
- failed: **0**
- skipped: **0**

All three WSA-2026-007 dedicated regressions passed.

The pre-existing `serve-time host override cannot bypass loopback security policy` regression also passed.

### Final PR-head composition workflows

On the same exact final head:

- Context Ladder Integrated Acceptance `37032144965`: **PASS**
- Invisible Intelligence Permanent Bot Composition `37032144825`: **PASS**
- Invisible Intelligence Temporary Worker Composition `37032145348`: **PASS**
- Invisible Intelligence Automation Recommendation Boundary `37032145079`: **PASS**

### Intermediate run note

The first implementation head produced one failure in the existing remote-bind security regression because lifecycle admission occurred before the test's expected unsafe-host rejection.

The product repair was corrected so an unsafe serve-time bind override is rejected first, and the same remote policy is rechecked again against authoritative disk config before listen.

That intermediate head is not the accepted/tested repair head.

### Post-merge CI

Post-merge Gateway CI run:

`37032364023`

On merged `main` ref `b27cebe11e536aa5a0f9bad707f38b0c2471879d`:

- Ubuntu / Node 20: **PASS**
- Ubuntu / Node 22: **PASS**
- macOS / Node 20: **PASS**
- macOS / Node 22: **PASS**
- Windows / Node 20: **PASS**
- Windows / Node 22: **PASS**

Representative merged-main Ubuntu Node 22 suite:

- tests: **107**
- passed: **107**
- failed: **0**
- skipped: **0**

The WSA-2026-007 dedicated suite passed after merge.

## 6. Finding-specific cross-audit recheck

### C-A1.2-001

**RESOLVED for WSA-2026-007.**

Disk lifecycle state and live operational admission no longer diverge for the audited setup/disable/uninstall/status seam.

### A2.3 Gateway lifecycle branch

**RESOLVED for WSA-2026-007 only.**

A2.3 previously recorded that the Gateway lifecycle surface existed but setup/disable/uninstall/status truth could diverge.

The repaired owner now makes its current lifecycle state operationally authoritative at live request admission.

Other A2.3 lifecycle findings remain independent and OPEN.

### A3.10 C-A3.10-002 Gateway branch

**RESOLVED for WSA-2026-007 only.**

A3.10 specifically recorded Gateway live process authority diverging from disk lifecycle under this finding.

The permanent suite now exercises disable, enable, uninstall, reinstall and restart while a server is live, across the same code accepted on Ubuntu/macOS/Windows.

Memory and Automations branches of C-A3.10-002 remain OPEN under their own findings.

### Restart/recovery branch

**PASS for this finding.**

An old process cannot silently inherit a later setup generation.

Sequential Gateway run-state recovery and WSA-2026-008 concurrency remain separate concerns.

## 7. Adjacent findings remain open

This closure is limited to `WSA-2026-007`.

The following are intentionally untouched:

- `WSA-2026-008` - Gateway concurrency / idempotency / stale control writers;
- `WSA-2026-013` - Memory write authority vs lifecycle;
- `WSA-2026-026` - Automations canonical store ownership;
- `WSA-2026-027` - Automations live legacy authority fence;
- `WSA-2026-028` - Automations attachment/component lifecycle divergence.

The whole-system verdict remains NO-GO and owner dogfood / Dashboard MC1.4 remain paused.

## 8. Closure verdict

Required WSA-2026-007 closure behavior is present on merged Gateway `main`:

- setup validates config before canonical ready publication;
- host compatibility is verified before ready publication;
- failed setup cannot falsely publish ready state;
- invalid remote setup cannot publish ready state;
- on-disk owner lifecycle is the live admission authority;
- disable immediately fences a running server's operational traffic;
- enable restores live readiness within the same setup generation;
- uninstall immediately fences a running server's operational traffic;
- status, doctor, live status and health expose consistent lifecycle semantics;
- stale processes cannot silently revive after re-setup/reinstall;
- fresh restart on the new setup succeeds;
- remote-bind security ordering remains intact;
- exact-head six-job Node 20/22 cross-platform CI passes;
- four PR-head composition workflows pass;
- post-merge six-job Node 20/22 cross-platform CI passes;
- representative suites report 107/107 pass;
- tested and merged product trees are identical;
- open Gateway PRs are zero.

**WSA-2026-007: CLOSED.**
