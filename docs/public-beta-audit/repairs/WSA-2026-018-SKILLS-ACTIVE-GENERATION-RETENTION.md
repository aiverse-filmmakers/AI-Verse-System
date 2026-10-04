# WSA-2026-018 — Skills active-generation retention

**Transition:** `ACTIVE -> CLOSED`  
**Severity / confidence:** MEDIUM / PROVEN, unchanged  
**Finding:** explicit generation retention purge could remove an immutable generation while an execution still held and used its path.  
**Original evidence:** `E-A1.5-013`  
**Owner:** `AI-Verse-Skills`  
**Accepted owner baseline:** `3817ba1e4c7ede85e36d968a737feb9de398d235`  
**Repair PR:** [AI-Verse-Skills #18](https://github.com/aiverse-filmmakers/AI-Verse-Skills/pull/18)  
**Final tested owner head:** `747cfc1bdde81ff4f06522ff8c9a9a816f97d13b`  
**Merged owner main:** `fa455961c17691862bd86b7e0f658690e9ecb86d`  
**Tested / merged product tree:** `c316450944dcdb4e2f60cb1f950b47c170734fb8`  
**System closure PR:** pending

## Accepted repair and closure law

A generation selected for execution remains protected from explicit retention purge for the whole execution, including after the active pointer changes. Lease acquisition, release and purge serialize under the same per-root lifecycle lock. The CLI returns a random lease ID and token; normal execution cleanup releases it. Hosts may pin either the current active generation or an exact generation they previously resolved. A requested package is validated before durable lease publication, so a failed pin cannot leave an orphan lease.

Purge preserves verifiably live local leases regardless of age or `--keep`. A dead local owner can be reclaimed only after process-death verification and a lease-identity reread. Foreign-host, malformed and otherwise unverifiable lease records fail closed and keep the referenced generation. Both the public purge and the controller-contained purge use this lease accounting.

## Permanent adversarial regressions

The lifecycle suite proves:

- an old generation remains available through purge while a lease is held, then becomes purgeable after explicit release;
- an exact previously selected generation can be leased after the active generation changes;
- invalid package selection fails before any lease is published;
- an aged but live process lease is never reclaimed;
- a dead local process lease is safely reaped and retention proceeds;
- foreign-host and unverifiable leases fail closed;
- unsafe lease-storage redirection fails closed;
- CLI pin/unpin, wrong-token rejection and release behavior remain covered.

## Owner validation and identity

| Gate | Exact tested head | Merged main |
|---|---:|---:|
| Validate AI-Verse Skills (registry, canonical unittest suite, CLI smoke) | Run 37164076308 — PASS | Run 37164305338 — PASS |
| Full E2E Install | Run 37164076087 — PASS | Run 37164305289 — PASS |
| Runtime Readiness | Run 37164076178 — PASS | Run 37164305362 — PASS |
| Lifecycle Controller Containment | Run 37164076072 — PASS, six OS/Python jobs | Run 37164305333 — PASS |
| WSA-018 Generation Lease Retention | Run 37164076127 — PASS, six OS/Python jobs | Run 37164305329 — PASS, six OS/Python jobs |

The WSA-018 matrix covers Ubuntu, macOS and Windows with Python 3.9 and 3.12. All six jobs passed on exact head and merged main. The full E2E journey passed install, pin, update, rollback, uninstall while a generation remained pinned, and recovery after uninstall.

All eight changed-file Git blobs match between the exact tested head and merged main. Skills main is `fa455961c17691862bd86b7e0f658690e9ecb86d`; it has zero open PRs after merge.

## Finding-specific outcome

The active-generation retention failure is resolved for AI-Verse-Skills. Generation bytes selected by a live execution are protected from explicit purge, and crash recovery does not use age as a substitute for process liveness. This finding-specific closure does not change the whole-system `NO-GO` verdict or close adjacent findings.

System Contract Validation on the closure PR head and merged System main is recorded after both validations complete.
