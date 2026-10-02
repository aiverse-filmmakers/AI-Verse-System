# WSA-2026-051 Closure - Connections DNS Rebinding Containment

**Finding:** `WSA-2026-051`  
**Severity / confidence:** HIGH / PROVEN  
**Owner:** `AI-Verse-Connections`  
**Repair wave:** R1.9  
**Closure date:** 2026-10-02  
**State:** **CLOSED**

## 1. Finding

Connections screened a target with one standalone DNS lookup and then used ordinary global `fetch()`, which could independently resolve the same hostname again after trusted credentials had been attached.

That created a DNS-rebinding window where:

1. policy lookup returned a public address;
2. the request later resolved the hostname again;
3. the second resolution could point at loopback/private/reserved space;
4. the credential-bearing request could reach that private target.

Canonical contradictions: `C-A4.1-002` and `C-A4.1-005`.

Required closure evidence:

- resolve once under policy and pin the outbound connection to an approved address or equivalent non-rebinding transport;
- validate IPv4/IPv6 answers and normalized hostname/origin;
- preserve TLS hostname/SNI verification against the registered hostname;
- reject connected remote addresses outside the approved set;
- apply the same defense to Generic API and MCP;
- add deterministic rebinding regressions;
- prove credentials are never sent on a rebound connection.

## 2. Baseline and repair identity

**Pre-repair Connections ref:** `5759425fcf3692ce64f4834aaa1b101c483c8a34`  
**Open Connections PRs before repair:** 0

**Repair branch:** `repair/wsa-2026-051-dns-rebinding-containment`  
**Repair PR:** `AI-Verse-Connections#6`  
**Final tested PR head:** `0fceea60789e5145a90570000288c18e67443cfd`  
**Merged Connections ref:** `63f8698545d731654f76684bf6ba40248996fc6a`  
**Tested/merged product tree:** `67413e50942816a15c08b0da5cd2d07c538c1dfa`

The final tested PR head and merged `main` commit have the same product tree.

Open Connections PRs after merge: **0**.

## 3. Final implementation contract

### 3.1 One policy resolution

The shared network boundary now resolves a DNS hostname once before transport creation.

The policy resolution:

- normalizes the hostname;
- rejects localhost forms by default;
- validates every DNS answer as an IPv4 or IPv6 address;
- rejects malformed or family-mismatched answers;
- rejects any private/reserved answer unless private-network access was explicitly enabled;
- retains the approved address set;
- selects one approved address as the pinned transport target.

Literal IP targets pass through the same private/reserved classification.

### 3.2 Expanded private/reserved IP validation

The repaired network policy covers the existing private/local ranges plus reserved/documentation/link-local/multicast ranges relevant to SSRF containment.

Both IPv4 and IPv6 DNS answer sets are validated before any transport is created.

Mixed answer sets fail closed if even one returned address is private/reserved while private-network access is disabled.

### 3.3 Pinned transport

The old `assertNetworkTargetAllowed() -> global fetch()` sequence is removed from the credential-bearing edge.

The shared HTTP(S) transport now:

1. receives the approved DNS result;
2. installs a pinned lookup callback that can only return the selected approved IP;
3. disables connection pooling/reuse for that request;
4. opens the socket using the original registered URL/hostname;
5. verifies the actual connected remote address belongs to the approved DNS set;
6. only then sends request bytes.

A transport that ignores or bypasses the pinned resolver still fails closed at the remote-address verification step.

### 3.4 TLS hostname and SNI preservation

For HTTPS DNS hostnames, the transport keeps the original normalized hostname as TLS `servername`.

Therefore address pinning does not replace certificate verification with IP-based trust.

The connection is pinned to the approved IP while TLS identity remains bound to the registered hostname.

### 3.5 Credentials are withheld until remote verification

The request object may already contain trusted Authorization/header values in memory, but `req.end()` is deliberately delayed.

No HTTP request bytes are sent until:

- TCP/TLS connection establishment completes;
- the actual remote address is verified against the approved set;
- HTTPS peer authorization has not failed.

If the connected address is outside the approved set, the request is destroyed with `REMOTE_ADDRESS_MISMATCH` before `req.end()`.

This closes the credential exfiltration path proven by the finding.

### 3.6 Shared defense for Generic API and MCP

Both Generic API health/execute traffic and MCP RPC traffic use the same repaired `boundedFetch` transport.

The fix is therefore centralized at the common credential-bearing provider edge rather than duplicated per provider.

## 4. Permanent regressions

Dedicated coverage was added in:

`test/connections-dns-rebinding.integration.test.js`

The suite proves:

1. Generic API policy lookup sees a public IP;
2. the simulated fetch-time/rebound socket is private;
3. the transport remains pinned to the original public IP;
4. TLS SNI remains the registered hostname;
5. the Generic API bearer header is present in request metadata but zero request sends occur to the rebound socket;
6. MCP receives the same defense;
7. the MCP bearer header is never sent to the rebound socket;
8. mixed public/private IPv4 DNS sets fail before transport creation;
9. mixed public/private IPv6 DNS sets fail before transport creation;
10. normalized localhost hostname forms fail before DNS lookup.

Existing live local/private-network integration coverage also continued to pass when `allowPrivateNetwork: true`, proving the new transport does not break the explicitly permitted local mode.

## 5. Validation evidence

### PR-head acceptance

Final PR-head Actions run:

`37002450798`

On exact final head `0fceea60789e5145a90570000288c18e67443cfd`:

- Ubuntu / Node 20: **PASS**
- Ubuntu / Node 22: **PASS**
- macOS / Node 20: **PASS**
- macOS / Node 22: **PASS**
- Windows / Node 20: validation harness failure before tests
- Windows / Node 22: validation harness failure before tests

Representative successful exact-head suite:

- tests: **33**
- passed: **33**
- failed: **0**

All four dedicated WSA-2026-051 regression tests passed.

An earlier intermediate PR-head run failed one localhost-normalization test because its expected-origin fixture omitted the URL's trailing dot. The product correctly rejected that call earlier at origin matching. The test was corrected to use the actual URL origin, and the final exact-head run above is fully green on Linux/macOS.

### Post-merge acceptance

Post-merge Actions run:

`37002566149`

On merged `main` ref `63f8698545d731654f76684bf6ba40248996fc6a`:

- Ubuntu / Node 20: **PASS**
- Ubuntu / Node 22: **PASS**
- macOS / Node 20: **PASS**
- macOS / Node 22: **PASS**
- Windows / Node 20: validation harness failure before tests
- Windows / Node 22: validation harness failure before tests

Representative merged-main suite:

- tests: **33**
- passed: **33**
- failed: **0**

### Windows CI limitation

The Windows jobs still fail before `npm test` because the existing package script contains shell globs:

`node --check src/*.js && node --check src/providers/*.js && node --check bin/*.js && npm test`

PowerShell passes those globs literally, causing Node to fail on `src/*.js` with `MODULE_NOT_FOUND`.

This is the same pre-existing validation-harness issue recorded during WSA-2026-031 and WSA-2026-033. No Windows product-test failure is attributed to WSA-2026-051.

## 6. Finding-specific recheck

### C-A4.1-002

**RESOLVED for WSA-2026-051.**

The private-network deny decision and the actual connection no longer depend on independent DNS resolutions.

### C-A4.1-005

**RESOLVED for WSA-2026-051.**

Trusted provider credentials cannot be transmitted until the actual remote socket address is proven to belong to the DNS-approved set.

### DNS rebinding seam

**PASS.**

The transport cannot re-resolve outside the approved set, and an unexpected connected address is rejected before request transmission.

### IPv4/IPv6 seam

**PASS.**

Both address families are validated, and mixed public/private answer sets fail closed.

### TLS identity seam

**PASS.**

Pinned IP transport preserves the registered DNS hostname for TLS SNI/certificate verification.

### Generic API seam

**PASS.**

Deterministic rebound regression proves zero bearer transmission.

### MCP seam

**PASS.**

Deterministic rebound regression proves zero bearer transmission.

## 7. Adjacent findings remain open

This closure is limited to `WSA-2026-051`.

The following Connections finding remains **OPEN** and was intentionally not repaired here:

- `WSA-2026-032` - complete final-edge lifecycle and budget authority.

Later Connections findings also remain open in their ordered waves.

No lifecycle-ready recheck, usage-budget reservation, crash recovery, receipt scaling, provider-error redaction or unrelated CI behavior was changed.

## 8. Closure verdict

Required WSA-2026-051 closure behavior is present on merged Connections `main`:

- hostname and origin inputs remain normalized;
- DNS is resolved once under policy;
- all IPv4/IPv6 answers are validated;
- private/reserved answers fail closed by default;
- the transport lookup is pinned to the approved address;
- TLS SNI/certificate identity remains the registered hostname;
- the actual remote socket address is rechecked against the approved set;
- request bytes are withheld until remote-address verification succeeds;
- Generic API and MCP share the same protection;
- deterministic rebinding tests prove zero credential transmission to the rebound socket;
- exact-head and post-merge Ubuntu/macOS Node 20/22 checks pass;
- representative exact-head and merged-main suites are 33/33;
- tested and merged product trees are identical;
- open owner PRs are zero.

The pre-existing Windows glob-expansion validation-harness defect remains outside this repair.

**WSA-2026-051: CLOSED.**
