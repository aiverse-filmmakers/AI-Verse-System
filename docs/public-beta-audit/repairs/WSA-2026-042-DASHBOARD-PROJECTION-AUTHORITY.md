# WSA-2026-042 — Dashboard owner-declared Health, Inbox and Task truth

**Transition:** `ACTIVE -> CLOSED`  
**Severity / confidence:** MEDIUM / PROVEN, unchanged  
**Owner:** `AI-Verse-Dashboard`  
**Audited baseline:** `005c781111418cdde6cc6b1082efeaf8010fd880`  
**Original evidence:** AI-Verse-System A1.13 / WSA-2026-042  
**Repair PR:** [AI-Verse-Dashboard #15](https://github.com/aiverse-filmmakers/AI-Verse-Dashboard/pull/15)  
**Final tested owner head:** `8ab1743ad8108df47250511ade5546d5f209dff4`  
**Merged owner main:** `2c1d1a57f7cb27eec166d4fea10dbb335250c518`  
**Tested / merged product tree:** `da80a0159b10c0addd3ce8ebf1affc0bea29549c`

## Finding and accepted closure law

The audit found that generic workspace-file presence and Markdown headings were being converted into Health judgments, inbox filenames into synthetic review items with generated `createdAt`, and missing owner task data into an apparently available empty task list. These were Dashboard-authored interpretations without owner-declared Health, Inbox or Task records.

Health, Inbox and Task/Now now explicitly report unavailable when the canonical owner projection is absent. Health remains `unknown` with no invented dimensions; Inbox returns no fabricated items; Task summary marks `available: false`, and Now marks work, inbox and health unavailable. Owner-backed live session/run routes remain unchanged.

## Permanent regression coverage

- Workspace files, even when present and populated, do not create healthy/warning/critical owner health dimensions.
- Inbox filenames are not converted to approvals, review items, severities or timestamps.
- Missing task-owner data is distinguished from an available empty task list.
- Now reports unavailable flags and does not imply there are no running or attention items.
- Cross-system/workspace isolation and live owner-backed session/run routes remain covered by the existing suite.

## Owner validation

| Gate | Exact tested PR head | Merged main |
|---|---:|---:|
| Dashboard CI / Node 22 | `37167214458` — Ubuntu, macOS, Windows 3/3 PASS | `37167268099` — Ubuntu, macOS, Windows 3/3 PASS |

The first exact-head CI attempt caught stale adapter wiring in the Gateway projection call; that call was removed and the corrected final head passed all platforms. The exact tested head and merged main have identical tree `da80a0159b10c0addd3ce8ebf1affc0bea29549c`. All six changed-file blobs are identical. Dashboard has zero open PRs after merge.

System Contract Validation passed on the exact closure PR head in run `37167492113` (Python 3.11 and 3.13), and on merged System main in run `37167593426` (Python 3.11 and 3.13). The closure record was merged in System PR #149 at `a8579e83171f37a6013e075a4c9e4c9414d37c9a`.

## Outcome

The WSA-2026-042 shadow Health/Inbox/Task semantics are closed for AI-Verse-Dashboard. This finding-specific closure preserves the whole-system `NO-GO` verdict and existing release pauses.
