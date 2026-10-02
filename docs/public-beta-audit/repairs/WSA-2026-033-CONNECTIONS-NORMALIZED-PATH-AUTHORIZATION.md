# WSA-2026-033 Closure - Connections Normalized Path Authorization

**Finding:** `WSA-2026-033`  
**Severity / confidence:** HIGH / PROVEN  
**Owner:** `AI-Verse-Connections`  
**Repair wave:** R1.8  
**Closure date:** 2026-10-02  
**State:** **CLOSED**

## 1. Finding

Generic API execution authorized the caller's raw path string before WHATWG URL construction.

That allowed a path such as:

`/v1/%2e%2e/admin`

to satisfy a raw `/v1` prefix check while URL normalization produced:

`/admin`

The provider edge then rechecked only origin, so the normalized request could leave the admitted path prefix while still carrying trusted connection credentials.

Canonical contradiction: `C-A1.10-005`.

Required closure evidence:

1. construct/canonicalize the URL before path authorization;
2. validate the normalized pathname against canonical admitted prefixes;
3. reject dot-segment and encoded path-confusion forms;
4. cover percent-encoded dot segments, mixed-case encodings, plain dot segments, encoded separators and query-only variations;
5. recheck the final outbound pathname immediately before fetch.

## 2. Baseline and repair identity

**Pre-repair Connections ref:** `78a9843e338f2e301e7a8c7c3153d5b43cb69ea4`  
**Open Connections PRs before repair:** 0

**Repair branch:** `repair/wsa-2026-033-normalized-path-authorization`  
**Repair PR:** `AI-Verse-Connections#5`  
**Final tested PR head:** `5104ba8412374af69842b86e49b2bbc5235d59c4`  
**Merged Connections ref:** `5759425fcf3692ce64f4834aaa1b101c483c8a34`  
**Tested/merged product tree:** `100bf2d82f6935c745dd33aa5174fb300b3974a2`

The final tested PR head and merged `main` commit have the same product tree.

Open Connections PRs after merge: **0**.

## 3. Final implementation contract

### 3.1 Canonical admitted path prefixes

A dedicated internal path-policy module now canonicalizes every configured Generic API allowed path prefix.

Allowed prefixes:

- must be pathname-only values;
- must begin with `/`;
- cannot contain query or fragment policy text;
- cannot contain raw backslash separators;
- cannot contain encoded slash or backslash separators;
- cannot contain plain or percent-encoded dot-segment traversal forms.

The canonical pathname produced by the URL parser is the value used for authorization.

### 3.2 Path-confusion forms fail closed

Generic API request paths are inspected before URL construction for path-confusion forms.

The guard rejects:

- plain `.` and `..` path segments;
- percent-encoded dot segments;
- mixed-case percent encodings;
- mixed raw/encoded dot-segment forms;
- raw backslash separators;
- percent-encoded slash separators;
- percent-encoded backslash separators;
- nested percent-encoded traversal/separator forms.

Malformed percent encoding also fails before provider use.

### 3.3 URL normalization happens before authorization

The request target is now constructed with the WHATWG URL parser before path authorization.

After construction:

1. registered origin equality is enforced;
2. the normalized `target.pathname` is compared with the canonical admitted prefixes;
3. prefix matching preserves path-boundary semantics, so `/v1` does not authorize `/v10`.

The raw caller string is no longer the security authority for path scope.

### 3.4 Query-only data does not alter path authorization

Path-confusion validation is applied to the pathname portion, not query values.

A permitted request such as:

`/v1/item?next=%2e%2e%2Fadmin`

remains permitted because the normalized outbound pathname is still `/v1/item`.

This proves query data cannot either expand or unnecessarily narrow the path authorization decision.

### 3.5 Final provider-edge pathname recheck

Immediately before `boundedFetch`, after credential-header preparation, the adapter:

1. re-reads/canonicalizes the connection's current admitted prefixes;
2. reparses the final request target;
3. rechecks exact origin;
4. rechecks path-confusion safety;
5. rechecks the normalized outbound pathname against the current admitted prefixes.

Therefore a path that was valid during initial request construction but is no longer admitted at the final outbound edge fails before any HTTP request.

## 4. Permanent regressions

Dedicated coverage was added in:

`test/connections-normalized-path.integration.test.js`

The suite proves:

1. plain `..` rejection;
2. plain `.` rejection;
3. lower-case encoded `%2e%2e` rejection;
4. mixed-case encoded dot-segment rejection;
5. mixed raw/encoded dot-segment rejection;
6. lower/upper-case encoded slash rejection;
7. lower/upper-case encoded backslash rejection;
8. raw backslash rejection;
9. double-encoded dot-segment rejection;
10. double-encoded separator rejection;
11. `/v1` does not authorize `/v10`;
12. rejected paths generate zero external requests;
13. query-only encoded traversal text remains permitted when the pathname is admitted;
14. ambiguous dot-segment prefix configuration is rejected;
15. ambiguous encoded-separator prefix configuration is rejected;
16. query-bearing prefix configuration is rejected;
17. the final outbound pathname is rechecked after request construction and before fetch;
18. narrowing the current prefix at that final edge produces `PATH_NOT_ALLOWED` with zero external requests.

## 5. Validation evidence

### PR-head acceptance

Final PR-head Actions run:

`36995438983`

On exact final head `5104ba8412374af69842b86e49b2bbc5235d59c4`:

- Ubuntu / Node 20: **PASS**
- Ubuntu / Node 22: **PASS**
- macOS / Node 20: **PASS**
- macOS / Node 22: **PASS**
- Windows / Node 20: validation harness failure before tests
- Windows / Node 22: validation harness failure before tests

Representative successful exact-head suite:

- tests: **29**
- passed: **29**
- failed: **0**

All three dedicated WSA-2026-033 regression tests passed.

### Post-merge acceptance

Post-merge Actions run:

`36995525131`

On merged `main` ref `5759425fcf3692ce64f4834aaa1b101c483c8a34`:

- Ubuntu / Node 20: **PASS**
- Ubuntu / Node 22: **PASS**
- macOS / Node 20: **PASS**
- macOS / Node 22: **PASS**
- Windows / Node 20: validation harness failure before tests
- Windows / Node 22: validation harness failure before tests

Representative merged-main suite:

- tests: **29**
- passed: **29**
- failed: **0**

### Windows CI limitation

The Windows jobs fail before `npm test` because the existing package script contains shell globs:

`node --check src/*.js && node --check src/providers/*.js && node --check bin/*.js && npm test`

PowerShell passes those globs literally, causing Node to fail on `src/*.js` with `MODULE_NOT_FOUND`.

This is the same pre-existing validation-harness issue recorded during WSA-2026-031. No Windows product-test failure is attributed to WSA-2026-033, and the repair does not modify the unrelated CI harness.

## 6. Finding-specific recheck

### C-A1.10-005

**RESOLVED for WSA-2026-033.**

Raw pre-normalization string-prefix authorization is no longer the path security decision.

### Normalization seam

**PASS.**

URL construction occurs before authorization and the normalized pathname is the authorized object.

### Path-confusion seam

**PASS.**

Plain, encoded, mixed-case, nested and separator-based confusion forms covered by the finding fail closed.

### Prefix-boundary seam

**PASS.**

Canonical path-boundary matching prevents sibling-prefix expansion such as `/v1` to `/v10`.

### Query-only seam

**PASS.**

Query content does not influence normalized pathname authorization.

### Final outbound seam

**PASS.**

The normalized target pathname is checked again against current admitted prefixes immediately before fetch.

### A4.1 path-authorization branch

**RESOLVED for WSA-2026-033.**

The audited encoded dot-segment escape path is closed.

## 7. Adjacent findings remain open

This closure is limited to `WSA-2026-033`.

The following Connections findings remain **OPEN** and were intentionally not repaired here:

- `WSA-2026-051` - DNS/private-network rebinding containment;
- `WSA-2026-032` - complete final-edge lifecycle and budget authority;
- later Connections findings in the ordered program.

No DNS resolution/pinning, socket destination verification, lifecycle-ready authority, rate-budget reservation or unrelated networking behavior was changed.

## 8. Closure verdict

Required WSA-2026-033 closure behavior is present on merged Connections `main`:

- admitted prefixes are canonicalized;
- ambiguous path-policy configuration fails closed;
- request URL normalization precedes path authorization;
- normalized pathname, not raw caller text, is authorized;
- dot-segment and encoded-separator confusion forms fail closed;
- prefix boundaries are enforced;
- query-only variations are handled correctly;
- the final normalized outbound pathname is rechecked immediately before fetch;
- permanent regressions are present;
- exact-head and post-merge Ubuntu/macOS Node 20/22 checks pass;
- representative exact-head and merged-main suites are 29/29;
- tested and merged product trees are identical;
- open owner PRs are zero.

The pre-existing Windows glob-expansion validation-harness defect remains outside this repair.

**WSA-2026-033: CLOSED.**
