# WSA-2026-034 closure packet - Distribution lifecycle receipt concurrency

**Finding:** R3.8 / WSA-2026-034  
**Severity/confidence:** HIGH / PROVEN, unchanged  
**Owner:** `ai-verse-distribution`  
**Audited Distribution baseline:** `31888c74235cc262910fb094335fd3a994f0ecf1`  
**Repair PR:** [ai-verse-distribution#9](https://github.com/aiverse-filmmakers/ai-verse-distribution/pull/9)  
**Final tested PR head:** `51710800675d0d85cfea404056d14966b5988155`  
**Merged Distribution ref:** `c67ffbdda38717da6f19811b07421f0293285778`  
**PR head and merged changed-file blobs:** identical across all six changed paths  
**Status:** **CLOSED**

## Audited failure and repair

The original A1.12 finding (contradiction C-A1.12-004; evidence E-A1.12-008, -010, -012, -013, -017 and -027) found that atomic replacement of individual receipt files did not serialize complete mutating lifecycle operations. Competing processes could perform different owner effects and commit stale snapshots, resurrecting or erasing receipt truth.

The repair places complete mutating lifecycle commands behind a cross-process kernel-owned lock (POSIX `flock`, Windows `msvcrt`), adds monotonic receipt generations and stale-writer CAS rejection, and journals each pending owner effect durably before mutation. Receipt commit precedes journal cleanup. Status/doctor surface unresolved crash windows as `recovery-required`; only the exact pending operation may resume, and recovery fast-forwards to the exact interrupted setup substep.

## Permanent adversarial regressions

- Real cross-process writers serialize, and the second writer reloads the first committed generation.
- A live holder cannot be stolen merely because its lock file is old.
- Explicit stale receipt generations fail closed.
- A crash after owner effect releases the kernel lock, fences unrelated mutations, and allows only the exact operation to resume.
- A crash after receipt commit finalizes the journal without replaying the owner effect.
- The audited setup/uninstall interleaving cannot resurrect stale receipt truth.
- Multi-step setup recovery resumes at the exact pending substep without replaying earlier committed effects.

All seven regressions are in the canonical dedicated test suite and passed on the exact PR head and merged main.

## Validation

- PR-head Lifecycle Receipt Concurrency run `37155613833`: Ubuntu/macOS/Windows, 3/3 PASS.
- PR-head Distribution CI run `37155613864`: Ubuntu/macOS/Windows × Python 3.9/3.12, 6/6 PASS.
- PR-head composed workflows: Core `37155613873`, Agent `37155613855`, Invisible Intelligence Candidate `37155613822`, and Scenarios A-F `37155613838`; all final PR-head workflow groups green.
- Post-merge Lifecycle Receipt Concurrency run `37158461626`: PASS on `main`.
- Post-merge Distribution CI run `37158461640`: PASS on `main`.
- Merged-main Core clean-machine acceptance `37158621979`: Ubuntu/macOS/Windows, 3/3 PASS.
- Merged-main Scenarios A-F `37158676435`: both jobs PASS.
- Merged-main Invisible Intelligence Candidate `37158659570`: Ubuntu/macOS/Windows, 3/3 PASS.
- Merged-main Agent clean-machine acceptance `37158642893`: Ubuntu/macOS passed. The first Windows attempt failed in the downstream Gateway owner during a composed chat run: Windows reported `EPERM` replacing a Gateway run-state file, then Gateway returned `RUN_NOT_COMPLETED`. Distribution installation had succeeded before this unrelated owner failure. A failed-job-only Windows retry was started; its outcome is recorded below when complete.
- Exact PR-head review verified all 20 required GitHub Actions jobs green on the tested head. The six changed-file blobs are byte-identical between tested head and merged main.
- Open Distribution PRs after merge: 0.

### Composed Agent Windows retry

<!-- Update this subsection from the failed-job-only retry before merging this packet. -->

## Closure boundary

This closes WSA-2026-034 only. It does not close adjacent Distribution findings WSA-2026-035, -036 or -037, nor Connections findings WSA-2026-054/-055. The owner transaction requirement is satisfied by the cross-platform dedicated workflow and the regression suite; the separate Gateway Windows acceptance error is retained above as an unrelated composed-acceptance observation, not represented as a Distribution pass.
