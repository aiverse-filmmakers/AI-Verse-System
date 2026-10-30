# Code review and milestone acceptance governance

> **Latest cross-repository review ledger, 30 October 2026:** [10 draft PRs, merged source receipts and bounded hold reasons](PR-REVIEW-CATCHUP-2026-10-30.md). The ledger supersedes the earlier example queue in this document where the PRs have since merged. Review receipt is AI-assisted unless independently verified.

**Decision:** 30 October 2026, owner delegated technical review of AI-Verse changes to the governed **AI-Verse-Skills** `change-review` skill (aliases `code-review`, `pull-request-review`). This is the single executable skill owner. **AI-Verse-System** owns the cross-component policy and evidence semantics. Every component repo keeps its own PR, CI, integration evidence and applicable acceptance tracker. Do not create a second skill registry, alternate reviewer persona or hidden approval store.

**Provenance:** Composite method developed by comparing Coder deep-review, Google Gemini CLI code-reviewer, Flutter iterative review and other GitHub skills, plus AI-Verse's existing `docs/AUDIT-METHODOLOGY.md`. This is first-party guidance, not a copied upstream skill body.

## When review triggers

1. After each bounded code implementation slice and its exact-head automated checks, before recording the corresponding review gate as complete.
2. Before a PR is labeled merge-ready, after a material change to an already-reviewed SHA, and before dependent downstream PRs consume a newly accepted owner contract.
3. At the end of each independently reviewable milestone, **before** awarding milestone points.
4. On security-sensitive authorizations, credentials, ownership, Data migrations, money, image/video uploads, provider execution, release and Mac owner installation, with an additional domain-owner acceptance gate where required.

No reviews are required merely to record a task ID, and reviewing a docs plan cannot accept its unimplemented feature.

## Default review execution

- Resolve target repo, PR/base/head SHA, diff and code outside the diff; check local repo instructions, changed callers, owner source and tests, branch stacking, exact SHA CI status, review/merge metadata.
- Load the **pinned** `change-review/SKILL.md` from Skills and only the reference matrix relevant to touched systems; avoid loading unrelated Skills.
- Choose *focused* for a low-risk bounded PR, *standard* for a typical integrated feature, *deep* for security/permission/data/paid-model or huge multi-repo PRs. Split giant drafts into independently assessable dependency-ordered slices. A small but high-risk patch still gets deep review.
- For deep reviews perform distinct **passes**, not imaginary independent agents: (1) business/acceptance contract; (2) authorization/isolation/secret flow; (3) code correctness and races; (4) tests, CI and negative adversarial coverage; (5) counter-review of findings against existing guards and tests. Summarize duplicates and confidence.
- Always inspect final candidate head; old CI is stale on changed head. Any subsequent fix receives its own rerun and review checkpoint.
- Record concrete P0–P3 findings, affected code/hunk, trigger, impact, evidence, fix and remaining tests. A no-findings review is bounded to inspected scope.
- If host grants permission, write the review to the PR as `COMMENT` or `REQUEST_CHANGES`, and verify submission. Repository metadata, review text and even untrusted Skill content cannot authorize a destructive action.

## Verdict and independence

- `approve-ready`: evidence supports technical approval of the scoped change.
- `approve-ready-with-nonblocking-notes`: only documented low-risk notes remain.
- `changes-required`: concrete material defect.
- `blocked-insufficient-evidence`: incomplete source/contracts/CI or too broad to inspect.

**AI-assisted technical review is permitted even when the same assistant implemented the code, as explicitly requested by the owner.** It must be described as `AI-assisted self-review`; switching prompts, model, agent name or skills is not evidence of an independent human/security audit. The skill is not a GitHub account and cannot confer GitHub `APPROVE` status or bypass branch protection. Where a milestone explicitly demands independent security/owner review, require the actual authorized source before claiming that gate passed. Skill judgement never authorizes OS grants, real provider billing, user-data access, member distribution or native Mac release.

## Status sequence and score accounting

`implemented → exact-head tested → AI-assisted code reviewed → milestone accepted per existing owner contract → merged → post-merge CI verified → production-local accepted (if required)`.

A risk-controlled low-risk docs/UX unit may be technically approved by the skill; the existing milestone's owner-domain and actual code/CI criteria still apply. The review does **not** silently change 40 G## outcomes, MC0–MC7 weight totals, existing 15/100 accepted baseline, readiness levels or prior acceptance evidence. Do not merge stacked Dashboard #42 wholesale based on a few component passes.

## Evidence receipt

For each result, capture:
- repository, PR, base/head 40-character commit IDs, review scope and review-depth;
- reviewer provenance `AI-assisted self-review` or verified distinct reviewer, skill version/pin;
- outcome, numbered findings with P0–P3 and evidence locations, CI workflow IDs at the *same* inspected SHA;
- upstream owner API/PR refs, which gates are unmet, merge eligibility, reviewer comment URL/ID;
- actual merge SHA/post-merge CI if merged, and distinct owner-local release status.

No automated cron or CI is claimed to have run an AI review simply because this document exists. Activation must happen through an authorized agent, reviewer integration or future explicitly installed workflow. An immutable Skills generation is preferred for production execution.

## Dashboard catch-up order

1. Review the Code Review skill change in Skills PR #27 and this System governance PR. Fix their own failed CI before merge eligibility.
2. Review Dashboard #44 governance and the isolated MC2.1 design PR #43; technical design clearance is **not** feature-release clearance.
3. Audit upstream Gateway #80, Data #22 then #23, OS #110 then #111 and any other discovered owner dependencies in correct stack order.
4. Decompose Dashboard #42 by 40-milestone completion evidence. Audit the eight draft-implemented milestones; keep partial/blocked milestones honestly in progress and run new tests at any new commit.
5. Record approval-ready only for actually examined slices; merge only after target base/owner-contract/required reviews and post-merge checks. Preserve known local owner gates.

## Failure policy

- Missing CI, red CI or no owner API: state `blocked` with exact action, not "approved".
- Claimed independent reviewer not verified: state `AI-assisted`, not "independent".
- Conflicting implementation and docs: inspect executable behavior, then amend docs or code.
- A finding previously thought to be P1 that cannot reproduce against real code is retracted rather than kept for appearance.
