# WSA-2026-041 — Dashboard localhost Origin policy

**Transition:** `ACTIVE -> CLOSED`  
**Severity / confidence:** MEDIUM / PROVEN, unchanged  
**Owner:** `AI-Verse-Dashboard`  
**Audited baseline:** `359a19f683a15485299cb2bab4e844d8d05b4fd6`  
**Original evidence:** AI-Verse-System A1.13 / WSA-2026-041  
**Repair PR:** [AI-Verse-Dashboard #14](https://github.com/aiverse-filmmakers/AI-Verse-Dashboard/pull/14)  
**Final tested owner head:** `c7a77551ac35fef4e0de5db5593bae735dfa4778`  
**Merged owner main:** `005c781111418cdde6cc6b1082efeaf8010fd880`  
**Tested / merged product tree:** `75ab3f32f7916e7604f8a4b22f577209f28e96ca`

## Finding and accepted closure law

The audited allowlist compared full origins against only `http://localhost` and `http://127.0.0.1`, rejecting ordinary browser origins carrying a development port such as `http://localhost:5173`.

The accepted policy allows only HTTP origins on the exact `localhost` or `127.0.0.1` host, with a valid optional explicit port in 1–65535. Credentials, paths, queries, fragments, HTTPS and non-loopback hosts are rejected. Missing Origin remains allowed for non-browser clients. Authentication remains a separate mandatory gate.

## Repair and permanent regression coverage

The Gateway uses the validated loopback-host/HTTP policy consistently for RPC and WebSocket upgrades. Authenticated RPC tests cover localhost and 127.0.0.1 with representative ports and bare origins. Negative cases cover HTTPS, hostname suffix attacks, private LAN IPs, out-of-range ports, path-bearing origins and userinfo. Browser-style WebSocket handshakes exercise both localhost and 127.0.0.1 with explicit ports and valid Dashboard authentication. Existing WSA-040 auth-negative checks remain intact.

## Owner validation

| Gate | Exact tested PR head | Merged main |
|---|---:|---:|
| Dashboard CI / Node 22 | `37166508321` — Ubuntu, macOS, Windows 3/3 PASS | `37166552466` — Ubuntu, macOS, Windows 3/3 PASS |

The exact tested head and merged product tree are identical (`75ab3f32f7916e7604f8a4b22f577209f28e96ca`). Both changed-file Git blobs match between exact tested head and merged main. Dashboard has zero open PRs after merge.

System Contract Validation on the exact closure PR head and merged System main is recorded after both validations complete.

## Outcome

The WSA-2026-041 localhost browser-origin failure is closed for AI-Verse-Dashboard. WSA-2026-042 remains OPEN. This finding-specific closure preserves the whole-system `NO-GO` verdict and existing release pauses.
