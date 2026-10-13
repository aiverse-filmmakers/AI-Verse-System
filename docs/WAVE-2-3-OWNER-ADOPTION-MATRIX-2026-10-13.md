# Wave 2/3 Owner Adoption Matrix

**Program:** Repository Network Governance, Release Safety and Self-Checking  
**Slice:** 4.3 - Wave 2/3 handoff governance  
**Task:** 4.3-T2  
**Recorded:** 2026-10-13  
**Scope:** Evidence/discovery only. No owner repository, Distribution release set, Repository State, generated ledger or member payload is changed by this task.

## Decision rule

A current owner head may be selected as the next owner-adoption candidate only when one designated native workflow exists and has passed on that exact immutable revision. Native CI success proves owner-local candidate fitness only. It does not create Distribution acceptance or release admission.

An accepted revision is recorded only when immutable Distribution evidence already admits that exact component revision. A newer green branch head does not replace an older admitted revision merely because it is newer.

## Active owner matrix

| Owner | Rollout/profile | Exact current candidate | Designated native workflow | Exact successful native run | Immutable Distribution accepted revision | Disposition for T3 |
| --- | --- | --- | --- | --- | --- | --- |
| Gateway | Wave 2 / Agent | `1772b75e2add73a524715f746e87b3a6b5561bf6` | `.github/workflows/ci.yml` (`CI`) | `37876089214` | `46c15ee58b028dd7fb8b310327ea705ef618805e` | Candidate passes. Current head is a descendant of the released Agent baseline, but is not itself Distribution-accepted. |
| Automations | Wave 2 / Agent | `287ce9d6718ef06e4589a2a3e767c6a9ba376755` | `.github/workflows/ci.yml` (`CI`) | `37050285820` | `caaed83b98026dd955640fc015d181529b91a1c6` | Candidate passes. Current head is a descendant of the released Agent baseline, but is not itself Distribution-accepted. |
| Multiple Bots | Wave 2 / Agent | `ddf70ac19736f6ca7f8d604901c20af9e46614fe` | `.github/workflows/ci.yml` (`CI`) | `37240126310` | `c600e2bc014351a61e1c0e2673fc63f5d5fa54ec` | Candidate passes. Current head is a descendant of the released Agent baseline, but is not itself Distribution-accepted. |
| Token | Wave 2 / Agent | `d36916323abb5f396bd8fd6b7f5c3ef84af519d0` | `.github/workflows/ci.yml` (`CI`) | `37239902766` | `23b7b8ecbc9d9ef267f5e10449f785eb11107dd4` | Candidate passes. Current head is a descendant of the released Agent baseline, but is not itself Distribution-accepted. |
| Connections | Wave 3 / Full | `602a1c52ab782cc9a8b7a4caa60ccb29efe403d1` | `.github/workflows/ci.yml` (`CI`) | `37182362458` | none | Candidate passes owner-local CI only. No admitted Full component revision exists. Fail closed on release acceptance. |
| Dashboard | Wave 3 / Full | `bd26986e202d4b911d0c5f64659db71363bfccfa` | `.github/workflows/ci.yml` (`Dashboard CI`) | `37859693102` | none | Candidate passes owner-local CI only. No admitted Full component revision exists. Fail closed on release acceptance. |

## Wave 2 immutable Distribution baseline

The newest applicable released Agent record inspected is:

- `ai-verse-distribution/release-sets/agent-video-editor-rc1-2026-10-04.json`
- blob `111342a54e7090494c9af958584c80868455ffc2`
- profile `agent`
- status `released`
- Distribution acceptance `qualification-passed`
- qualification head `84a706d8fcb2d7881cf459af2d364e7057a0bd8a`
- candidate run `37185675385`
- merged Distribution ref `c3055f8db13d744416032ac61ad65cf8344aef48`
- merged Distribution CI run `37186142306`

It admits the four Wave 2 revisions shown in the matrix. The earlier released `agent-context-ladder-rc1-2026-09-15.json` independently records the same four revisions and an accepted Distribution qualification, so the baseline is not inferred from branch recency.

## Wave 2 lineage proof

Each current Wave 2 candidate is a strict descendant of its immutable released Agent baseline:

- Gateway: accepted `46c15ee58b028dd7fb8b310327ea705ef618805e` -> candidate `1772b75e2add73a524715f746e87b3a6b5561bf6`, `ahead_by=113`, `behind_by=0`.
- Automations: accepted `caaed83b98026dd955640fc015d181529b91a1c6` -> candidate `287ce9d6718ef06e4589a2a3e767c6a9ba376755`, `ahead_by=3`, `behind_by=0`.
- Multiple Bots: accepted `c600e2bc014351a61e1c0e2673fc63f5d5fa54ec` -> candidate `ddf70ac19736f6ca7f8d604901c20af9e46614fe`, `ahead_by=4`, `behind_by=0`.
- Token: accepted `23b7b8ecbc9d9ef267f5e10449f785eb11107dd4` -> candidate `d36916323abb5f396bd8fd6b7f5c3ef84af519d0`, `ahead_by=20`, `behind_by=0`.

Lineage makes these exact current heads safe candidates for owner adoption work. It does not promote them to released Agent revisions.

## Wave 3 fail-closed finding

The only Full release-set record present is:

- `ai-verse-distribution/release-sets/full-public-beta-pending.json`
- blob `c8270e23654264f22655ad8d9d4a070f1421c304`
- profile `full`
- status `blocked`
- components `[]`
- blocker: `AI-Verse Connections, Dashboard, and Apps do not yet have one admitted compatible Full release set`

Therefore Connections and Dashboard have exact owner-local candidates but no Distribution-accepted Full revision. T3 may publish the owner-local governance pattern against the exact green candidates, but neither candidate may be described as an admitted Full release.

## Apps experimental gap

Apps remains outside the six-active-owner adoption path:

- exact head `db5b0115bf59d6eae9149137a40e891968f3a637`
- repository status in its own README: founding architecture / research seed
- implementation status: not started
- `.github/workflows` is absent at the exact head
- no native CI is available
- no admitted Full release revision exists

No readiness, CI or release claim is manufactured for Apps.

## T2 conclusion

T2 passes.

The six active owners each have one exact candidate revision bound to one designated successful native workflow. Wave 2 retains its older immutable released Agent revisions as the only accepted Distribution baselines. Connections and Dashboard remain candidate-only because Full is explicitly blocked and has no admitted component revisions. Apps remains an explicit no-CI experimental gap.

This matrix is evidence for the next task only. It does not itself publish Component Release Descriptors, add owner-local exact-revision gates, alter release composition, refresh Repository State/ledger, or begin owner adoption.