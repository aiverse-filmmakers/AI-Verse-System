from pathlib import Path
import re
import subprocess

path = Path('docs/SAFE-INFRASTRUCTURE-UPGRADE-AND-RECOVERY-IMPLEMENTATION-PLAN.md')
text = path.read_text(encoding='utf-8')
message = subprocess.check_output(['git', 'log', '-1', '--pretty=%s'], text=True).strip()

if message != 'TEMP run Safe Infrastructure Slice 3.3 closure':
    raise SystemExit(f'unexpected trigger for closure helper: {message}')

old_header = '''**Status:** PAUSED - PHASE 3 IN PROGRESS; SLICE 3.2 COMPLETE  
**Canonical planning repo:** `aiverse-filmmakers/AI-Verse-System`  
**Primary orchestration repo:** `aiverse-filmmakers/ai-verse-distribution`  
**Initial owner repos:** `aiverse-filmmakers/AI-Verse-OS`, `aiverse-filmmakers/AI-Verse-Skills`  
**Started:** 2026-10-12  
**Planning method:** `docs/ADAPTIVE-IMPLEMENTATION-PLANNING-SKILL.md`  
**Program size:** 18 slices  
**Completed:** 9  
**Remaining:** 9  
**Overall progress:** 50.0%  
**Current phase:** Phase 3 - Implement canonical owner migrations for proven motivating problems  
**Current phase progress:** 2/4  
**Slices until Phase 4:** 2  
**Next:** Slice 3.3 - Implement cross-provider capability scope semantics and managed Skills generation alignment  
**Next slice task list:** STOP - derive only when Slice 3.3 starts'''
new_header = '''**Status:** PAUSED - PHASE 3 IN PROGRESS; SLICE 3.3 COMPLETE  
**Canonical planning repo:** `aiverse-filmmakers/AI-Verse-System`  
**Primary orchestration repo:** `aiverse-filmmakers/ai-verse-distribution`  
**Initial owner repos:** `aiverse-filmmakers/AI-Verse-OS`, `aiverse-filmmakers/AI-Verse-Skills`  
**Started:** 2026-10-12  
**Planning method:** `docs/ADAPTIVE-IMPLEMENTATION-PLANNING-SKILL.md`  
**Program size:** 18 slices  
**Completed:** 10  
**Remaining:** 8  
**Overall progress:** 55.6%  
**Current phase:** Phase 3 - Implement canonical owner migrations for proven motivating problems  
**Current phase progress:** 3/4  
**Slices until Phase 4:** 1  
**Next:** Slice 3.4 - Implement admitted capability promotion/re-scoping and reference repair  
**Next slice task list:** STOP - derive only when Slice 3.4 starts'''
if text.count(old_header) != 1:
    raise SystemExit(f'header guard failed: found {text.count(old_header)}')
text = text.replace(old_header, new_header, 1)

old_phase = '''**Phase size:** 4 slices  
**Status:** IN PROGRESS  
**Phase progress:** 2/4'''
new_phase = '''**Phase size:** 4 slices  
**Status:** IN PROGRESS  
**Phase progress:** 3/4'''
if text.count(old_phase) != 1:
    raise SystemExit(f'Phase 3 guard failed: found {text.count(old_phase)}')
text = text.replace(old_phase, new_phase, 1)

pattern = re.compile(
    r'## Slice 3\.3 - Implement cross-provider capability scope semantics and managed Skills generation alignment\n.*?(?=\n---\n\n## Slice 3\.4 - Implement admitted capability promotion/re-scoping and reference repair)',
    re.S,
)
matches = pattern.findall(text)
if len(matches) != 1:
    raise SystemExit(f'Slice 3.3 closure guard failed: found {len(matches)} blocks')
if '**Status:** IN PROGRESS' not in matches[0] or '**Adaptive tasks:** 2/6 COMPLETE' not in matches[0]:
    raise SystemExit('Slice 3.3 closure guard found unexpected state')

new_slice = '''## Slice 3.3 - Implement cross-provider capability scope semantics and managed Skills generation alignment

**Status:** COMPLETE  
**Dependencies:** 2.3 plus canonical Identity Hardening scope-transfer contract  
**Adaptive tasks:** 6/6 COMPLETE

### Refreshed refs

- `aiverse-filmmakers/AI-Verse-System@e6c20a1cd7c60d17095f4f24bd3745848667e924` at audit refresh;
- task-list commit: `aiverse-filmmakers/AI-Verse-System@6a3cc21215b66fbafae72121efaabb0c57983279`;
- starting OS ref: `aiverse-filmmakers/AI-Verse-OS@88ce41a95554e1323ba34aa71b536b9e98475808`;
- final OS implementation ref: `aiverse-filmmakers/AI-Verse-OS@01571824d18421ea71251556b47c3308bfef4446`;
- Skills ref: `aiverse-filmmakers/AI-Verse-Skills@afde5c06307fba7d074de2929c2eb6c3dc6bdab8`;
- detailed evidence: `docs/SAFE-INFRASTRUCTURE-SLICE-3.3-CAPABILITY-SCOPE-AND-SKILLS-ALIGNMENT.md` at `aiverse-filmmakers/AI-Verse-System@8e2f3f8d9317c62d808dd429330a6d9b803ba199`.

### Final derived task list

- [x] **3.3-T1** Refresh System, OS and Skills refs and re-read the canonical identity/provider law, current OS resolver/provider contract and current Skills immutable-generation integration.
- [x] **3.3-T2** Freeze evidence-backed placement semantics: project-only user capabilities target the trusted active Workspace; reusable capabilities intended across projects or a practical domain target the user-owned local provider; OS built-ins and managed `aiverse-skills` are never writable user-authoring targets.
- [x] **3.3-T3** Implement an OS-owned practical placement planner that accepts member-level reuse intent without asking for provider IDs or storage paths, preserves current qualified identity forms, and refuses project-only placement when no trusted active Workspace exists.
- [x] **3.3-T4** Add focused acceptance tests and architecture documentation proving wider reusable intent is not forced into Workspace-private storage, managed Skills generation ownership is unchanged, and any cross-provider promotion remains a separately admitted migration with provenance/reference-repair requirements rather than silent identity continuity.
- [x] **3.3-T5** Run exact-ref OS validation and reverify Skills generation/lifecycle alignment without modifying Skills unless current evidence exposes a real owner gap.
- [x] **3.3-T6** Record exact implementation/evidence refs, close every Slice 3.3 acceptance criterion, update the canonical roadmap, and stop before Slice 3.4.

### Implemented placement semantics

OS now maps practical member intent to the authorized user-owned provider without asking the member to choose folders, provider IDs or internal scope IDs:

- "only use this in this project" -> trusted active Workspace provider;
- "use this for all YouTube work" or equivalent related-work intent -> private reusable `local` provider;
- "use this everywhere" -> private reusable `local` provider.

OS built-ins and the managed `aiverse-skills` distribution are never user-authoring targets. Publishing into the managed distribution remains a separate reviewed Skills-owned action.

The placement planner is classification/planning only. It does not move an existing package. When a user-owned capability would cross providers, the result explicitly says that a separate migration is required, qualified identity is not assumed to survive, provenance/history must be preserved, and durable references require admitted repair. Actual promotion/re-scoping remains Slice 3.4.

### OS implementation

Final exact OS ref: `01571824d18421ea71251556b47c3308bfef4446`.

Added/updated:

- `scripts/capability-placement.mjs`;
- `scripts/capability-resolver.mjs`;
- `scripts/capability-resolver-cli.mjs`;
- `scripts/test-capability-placement.mjs`;
- `.github/workflows/capability-placement.yml`;
- `system/architecture/capability-resolution.md`.

Current qualified identities remain unchanged:

```text
os:<name>
aiverse-skills:<name>
local:<name>
workspace:<workspace-id>:<name>
```

### Skills alignment

No AI-Verse-Skills source change was required. Skills already owns immutable generations, the atomic active pointer, exact generation pinning, immutable update, pointer-only rollback, uninstall retention and recovery. User-owned local/Workspace capabilities remain outside managed distribution ownership.

OS consumes that provider contract but does not duplicate Skills lifecycle or write/publish into the distribution.

### Exact validation

OS `Capability Placement Contract` run `38291968753` at exact SHA `01571824d18421ea71251556b47c3308bfef4446`: **SUCCESS**.

Passed:

- placement/resolver/CLI syntax;
- practical placement acceptance;
- existing scoped discovery and managed-generation resolver regression.

OS `Repository QC` run `38291968646` at the same exact SHA: **SUCCESS** across `qc`, `adapter-integration` and `skills-provider-integration`. The provider integration installed a real immutable Provider-v1 Skills generation outside OS and successfully discovered/selected it through the OS resolver.

Skills `Full E2E Install` run `38246389751` at exact SHA `afde5c06307fba7d074de2929c2eb6c3dc6bdab8`: **SUCCESS**, including generation lifecycle validation, immutable update, pointer-only rollback, uninstall retention and recovery.

### Acceptance criteria

- OS owns provider scope/placement semantics: **PASS**;
- Skills continues owning managed provider package identity/lifecycle: **PASS**;
- current provider-qualified identity forms remain compatible unless explicitly versioned/amended: **PASS**;
- new reusable capabilities are not forced into a Workspace-private provider when wider user-owned reuse is clearly intended: **PASS**;
- provenance/history survives promotion according to the canonical identity contract: **PASS AT THE SLICE 3.3 BOUNDARY** because cross-provider change is explicitly classified as a separate unapplied migration requiring provenance/history preservation and reference repair; actual migration remains Slice 3.4;
- member never chooses storage folders or internal scope IDs: **PASS**.

### Completion report

```text
Completed: Slice 3.3 - Implement cross-provider capability scope semantics and managed Skills generation alignment
Tasks: 6/6
Overall: 10/18 slices (55.6%)
Phase: Phase 3 - Implement canonical owner migrations for proven motivating problems
Phase progress: 3/4
Until next phase: 1 slice
Next: Slice 3.4 - Implement admitted capability promotion/re-scoping and reference repair
Blockers/drift/amendments: none. Skills lifecycle ownership remains unchanged; actual cross-provider migration remains deliberately unimplemented until Slice 3.4.
```

### NEXT

**STOP after Slice 3.3 for the current one-at-a-time execution request.**

Next execution unit: Slice 3.4. Derive its adaptive task list only after fresh System/OS/provider-consumer refs are fetched. No Slice 3.4 promotion, copying or reference-repair mutation was started here.
'''
text = pattern.sub(new_slice, text, count=1)

changelog = '''## 2026-10-12 - Slice 3.3 completed; practical capability placement aligned with managed Skills generations

- Added OS-owned practical placement planning for project-only, related-work and all-work reuse intent.
- Routed wider personal reuse to the user-owned local provider rather than trapping it in Workspace-private storage or writing into managed Skills.
- Preserved all existing provider-qualified identity forms.
- Classified any cross-provider promotion as a separate unapplied migration requiring provenance/history preservation and reference repair.
- Kept AI-Verse-Skills authoritative for immutable generations, active-pointer lifecycle, rollback, uninstall retention and recovery; no Skills code change was required.
- Qualified OS `Capability Placement Contract` run `38291968753` and `Repository QC` run `38291968646` at exact OS ref `01571824d18421ea71251556b47c3308bfef4446` as successful.
- Reverified Skills `Full E2E Install` run `38246389751` at exact Skills ref `afde5c06307fba7d074de2929c2eb6c3dc6bdab8` as successful.
- Recorded detailed evidence in `docs/SAFE-INFRASTRUCTURE-SLICE-3.3-CAPABILITY-SCOPE-AND-SKILLS-ALIGNMENT.md` at `8e2f3f8d9317c62d808dd429330a6d9b803ba199`.

'''
marker = '\n---\n\n# Current execution pointer\n'
if text.count(marker) != 1:
    raise SystemExit(f'changelog insertion guard failed: found {text.count(marker)}')
text = text.replace(marker, '\n' + changelog + '---\n\n# Current execution pointer\n', 1)

pointer_pattern = re.compile(r'# Current execution pointer\n.*\Z', re.S)
if len(pointer_pattern.findall(text)) != 1:
    raise SystemExit('current execution pointer guard failed')
pointer = '''# Current execution pointer

**Completed:** 10/18  
**Overall:** 55.6%  
**Phase:** Phase 3 - Implement canonical owner migrations for proven motivating problems  
**Phase progress:** 3/4  
**Until Phase 4:** 1 slice  
**Next:** STOP after Slice 3.3 under the one-at-a-time execution rule  
**Next Safe Infrastructure slice:** Phase 3 / Slice 3.4 - Implement admitted capability promotion/re-scoping and reference repair  
**Next task:** none until Slice 3.4 starts and its adaptive task list is derived from fresh System/OS/provider-consumer refs  
**Blockers/drift/amendments:** none. Slice 3.3 added practical OS placement semantics without changing managed Skills ownership or silently applying cross-provider migration.
'''
text = pointer_pattern.sub(pointer, text, count=1)

path.write_text(text, encoding='utf-8')
