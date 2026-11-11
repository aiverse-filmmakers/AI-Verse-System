# Portable local chat history and progressive recall

## Product direction and authority

Bogdan's November 2026 clarification requires preserving the visible local
conversation independently of deciding which facts deserve curated Memory.
Local tools that operate in the selected OS folder are the first target. Hosted
browser conversations are outside this scope. A copied OS folder must retain
original chat evidence that another assistant can inspect without the original
provider's local history. Native continuation inside a provider's own thread is
a separate provider capability.

This supplements the selective-learning direction in OWNER-PRODUCT-INTENT.md.
It does not promote every utterance into curated facts, current truth, goals or
instructions. Summaries navigate; exact local sources provide evidence. Old
chat instructions do not grant current permission or override current owners.

## Canonical owners

* OS owns the private original chat archive, native capture, physical folder and
  workspace binding, consent, placement, direct reading and move recovery.
* Memory consumes the archive as a typed scoped source through its existing
  catalog, summary, detail and exact-source depths. Search/derived views never
  rewrite original text or become another transcript owner.
* Brain, Data and Skills retain their established domains. Current file facts
  still resolve to the applicable current canonical file or owner record.
* Distribution adopts owner-accepted exact revisions, qualifies preservation and
  compatibility, refreshes installed helpers through the owner API and promotes
  only through its normal gate. System records architecture and scoped State.

The archive uses private, gitignored user storage under
`archives/private-chat-history/v1/`. Ordinary note/digest admission remains
selective. The archive writer does not publish raw chats or sync them remotely.
Provider execution and authorized contextual reads retain their existing
permissions; archiving grants no new connection or cross-project authority.

## Implemented handoff under qualification

OS PRs #129 and #130, Memory PR #39 and Distribution PR #97 implement the current handoff.
Those implementation PRs have merged; OS acceptance and the
unified member release remain separate gates. Exact accepted revisions and
current release observations belong to owner descriptors and Repository State,
not independently maintained version tables in this document.

The implementation uses existing approved native local lifecycle integration,
not a new Gateway or Dashboard. The first capture targets are version-qualified
Claude Code and Codex on macOS/Linux. Native Windows capture, T3, Hermes imports
and arbitrary browser/desktop adapters are not established by those proofs.
Cross-platform archive/Memory reading does not imply every capture host works.
Registration or a settings file is not evidence that callbacks execute.

Recording is explicit opt-in and starts at an observed authorized new-session
boundary. Switching it off and back on requires a new chat; private intervals
cannot be backfilled. Unverified old history is not attributed to today's
workspace. Native sources stream through no-follow descriptors and identity
checks; hidden reasoning and tool bulk are excluded. Exact visible text,
ordering, timestamps and exposed lineage metadata remain in canonical records.
Attachments are explicitly marked not embedded rather than silently copied.
Credential-like visible content blocks capture for operator review; it is not
silently claimed saved. Current status distinguishes saved-through-checkpoint,
pending, partial, blocked and unverified.

The native application may not flush its submitted prompt until after answering.
A real approved UserPromptSubmit therefore saves the exact current user words
first in an OS owned private recovery journal below that chat home's `.pending/`
directory. This is provisional observed input, not a fabricated native message,
source byte offset or Memory atomic. Existing consent, physical project,
private session and secret checks still apply. It is not a second curated store.

After native transcript messages commit durably, the OS matches observations
once, in order and after their original saved message checkpoints. Matching raw
text is removed from the journal; content free replay hashes remain. Repeated
identical prompts are distinct observations. Unmatched text stays explicitly
incomplete and is readable from the copied OS folder without provider history
or runtime session state. Recovery reads require current OS project permission.
Chats with unreconciled prompts cannot move and strand words in their old home.
Never describe incomplete observations as a completed conversation or invent a
reply the application did not produce. The durability invariant applies to any
future local adapter: receiving input must not depend on a later provider flush.

Each chat has one home. General root conversations use Personal; project chats
use the physical workspace. Tidying reviews both through bounded rotating
previews. Mixed conversations stay in their restricted home until reviewed.
Moves require an exact content-bound preview and an original user confirmation.
The OS denies both homes during an interrupted move, requires verified recovery,
retains stable message references, and prevents the old collector recreating
history in its old home. A move closes that native chat to further recording;
start a new chat to record more. Source application files are never moved.

Memory resolves old references through the current placement, rechecks the
currently permitted destination and immutable source evidence, and denies old
project access. Archive IDs reused in unrelated projects retain independent
namespaces. Search pages are bound to the query/current visibility and retain
per-page content budgets. Page-local counts are not a claim that the complete
history was searched; continue until complete. Individual source-record and
archive capacity limits remain explicit fail-closed limits.

## Evidence and release boundary

The owner CI includes actual native executables with isolated homes, synthetic
loopback providers and no personal credentials. It proves observed source
formats, real approved callbacks, replay, resumed processes, exact copied-folder
reads and scoped placement/recovery. Native process death checks also kill a
resumed app before its model response and require the exact submitted prompt
to survive a copied folder with the original app history removed. Claude
normalizes its observation identity once for learning and transcript capture;
an identity local to only one consumer cannot support durable prompt replay.
The cross-native proof additionally requires
the next native model request to receive the earlier exact archived reply through
Memory after the original provider home is removed, in both directions.

Passing a focused proof is not member release acceptance. Owner descriptor gates,
System Core refresh, exact Distribution qualification, preservation/rollback and
normal promotion must all pass. No emergency promotion, synchronization debt,
skipped gate or edits to historical evidence are permitted for this handoff.
The personal installation remains separate and is not updated by release work.
