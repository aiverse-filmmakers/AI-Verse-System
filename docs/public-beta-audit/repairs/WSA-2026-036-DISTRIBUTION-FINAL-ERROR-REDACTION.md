# WSA-2026-036 — Distribution final error redaction

**Transition:** `ACTIVE -> CLOSED`  
**Severity / confidence:** MEDIUM / PROVEN, unchanged  
**Original evidence:** E-A1.12-015 and E-A1.12-019  
**Owner:** `ai-verse-distribution`  
**Audited baseline:** `c67ffbdda38717da6f19811b07421f0293285778`  
**Repair PR:** [ai-verse-distribution #10](https://github.com/aiverse-filmmakers/ai-verse-distribution/pull/10)  
**Final tested owner head:** `1e8f0253bd648fde69ec0e6220e844e3e85f9e78`  
**Merged owner main:** `36a670ff263c9a16fbf6b7ab4a464cc4ef35efa9`  
**Tested / merged product tree:** `14c1d9e66c9ddbf5f1b6da8acfef441253fb4315`

## Finding and accepted closure law

The original audit found that `ProcessError` embedded raw child stdout/stderr and the CLI surfaced `str(exc)` in its top-level error message even when separate output fields were sanitized. It also found no ProcessError-to-CLI secret regression.

The closure law requires one final minimization/redaction boundary for child/provider output before it reaches exceptions, direct API results, structured JSON, terminal output or captured diagnostics. Secret-bearing argv values must also be covered.

## Repair

Distribution sanitizes structured and plain-text child output, argv (including split and inline secret arguments), process exception fields/messages, command result serialization, CLI JSON and human output, and errors returned by status/doctor. Credential coverage includes labeled secrets, environment-key forms, bearer values and common opaque token formats.

Permanent regressions cover process failures, serialized command results, nested structured errors, split/inline argv credentials, CLI human and JSON output, and direct status/doctor consumers.

## Owner validation

| Gate | Exact tested PR head | Merged main |
|---|---:|---:|
| WSA-036 Final Error Redaction | `37165501648` — 6/6 Ubuntu/macOS/Windows × Python 3.9/3.12 | `37165826622` — 6/6 PASS |
| Distribution CI | `37165501622` — PASS | `37165826606` — 6/6 PASS |
| Lifecycle Receipt Concurrency | `37165501618` — PASS | `37165826610` — 3/3 PASS |
| Invisible Intelligence Scenarios A-F | `37165501624` — PASS | — |
| Clean Machine Core Acceptance | `37165501620` — 3 OS PASS | — |
| Clean Machine Agent Release Gate | `37165501616` — 3 OS PASS | — |
| Clean Machine Invisible Intelligence Candidate | `37165501617` — 3 OS PASS | — |

All seven exact-head gates passed. The exact tested PR tree and merged product tree are identical, all changed-file blobs match, and Distribution has zero open PRs after merge.

System Contract Validation on the exact closure PR head and merged System main is recorded after both validations complete.

## Outcome

The WSA-2026-036 secret-leak path is closed for Distribution. WSA-2026-037 remains OPEN. This finding-specific closure does not change the whole-system `NO-GO` verdict or existing release pauses.
