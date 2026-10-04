# WSA-2026-045 — Gateway exact-source freshness cache

**Transition:** `ACTIVE -> CLOSED`  
**Severity / confidence:** MEDIUM / PROVEN, unchanged  
**Owner:** `AI-Verse-Gateway`  
**Audited/live pre-repair main:** `cd0789401ddf7c536558a27d84328e963b10c882`  
**Repair PR:** [AI-Verse-Gateway #35](https://github.com/aiverse-filmmakers/AI-Verse-Gateway/pull/35)  
**Final tested owner head:** `f7c415b20d8e6637cdc5f30cf04d6c56edda1053`  
**Merged owner main:** `3fd9618f693ec71e186cc47da66c2b2694837a17`  
**Tested / merged product tree:** `ab6cc47a3972f93acf9c2b5eba376b9adb3b0ca8`

## Finding and accepted closure law

The original A2.5 evidence found that repeated identical source-depth requests replayed a prior per-run result by request fingerprint alone, skipping Memory owner freshness checks and Gateway external-source fingerprint validation. Exact-source requests now always perform a fresh owner retrieval and external source validation; request deduplication remains for non-source summary/detail reads. Changed Memory evidence returns current owner content. Changed Gateway-held external evidence returns an explicit `stale` result with no source messages.

## Permanent regression coverage

- Memory exact-source drift between identical requests performs a second owner read and returns updated source content.
- Gateway external-source drift between identical requests performs a second owner read, detects `source_fingerprint_mismatch`, returns `stale`, and exposes no old source content.
- Existing equivalent summary/detail requests continue to deduplicate.

## Owner validation

| Gate | Exact tested PR head | Merged main |
|---|---:|---:|
| Gateway CI / Node 20 and 22 | `37167702013` — Ubuntu/macOS/Windows 6/6 PASS | `37167789207` — Ubuntu/macOS/Windows 6/6 PASS |
| Context Ladder Integrated Acceptance | `37167701999` — PASS | merged-main CI `37167789207` — 6/6 PASS |
| Temporary Worker Composition | `37167702199` — PASS | merged-main CI `37167789207` — 6/6 PASS |
| Permanent Bot Composition | `37167701980` — PASS | merged-main CI `37167789207` — 6/6 PASS |
| Automation Recommendation Boundary | `37167701923` — PASS | merged-main CI `37167789207` — 6/6 PASS |

The exact tested head and merged main have identical product tree `ab6cc47a3972f93acf9c2b5eba376b9adb3b0ca8`. Gateway has zero open PRs after merge.

System Contract Validation on the exact closure PR head and merged System main will be recorded after both validations pass.

## Outcome

WSA-2026-045 is closed for AI-Verse-Gateway. This finding-specific closure preserves the whole-system `NO-GO` verdict and existing release pauses.
