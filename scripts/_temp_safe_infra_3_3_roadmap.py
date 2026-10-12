from pathlib import Path
import subprocess

path = Path('docs/SAFE-INFRASTRUCTURE-UPGRADE-AND-RECOVERY-IMPLEMENTATION-PLAN.md')
text = path.read_text(encoding='utf-8')
message = subprocess.check_output(['git', 'log', '-1', '--pretty=%s'], text=True).strip()

if message != 'TEMP run Safe Infrastructure Slice 3.3 task list':
    raise SystemExit(f'unexpected trigger for task-list helper: {message}')

old = '''## Slice 3.3 - Implement cross-provider capability scope semantics and managed Skills generation alignment

**Status:** NOT STARTED  
**Dependencies:** 2.3 plus canonical Identity Hardening scope-transfer contract  
**Adaptive tasks:** derive from current OS provider resolver and Skills managed-provider lifecycle
'''
new = '''## Slice 3.3 - Implement cross-provider capability scope semantics and managed Skills generation alignment

**Status:** IN PROGRESS  
**Dependencies:** 2.3 plus canonical Identity Hardening scope-transfer contract  
**Adaptive tasks:** 2/6 COMPLETE

### Refreshed refs

- `aiverse-filmmakers/AI-Verse-System@e6c20a1cd7c60d17095f4f24bd3745848667e924`
- `aiverse-filmmakers/AI-Verse-OS@88ce41a95554e1323ba34aa71b536b9e98475808`
- `aiverse-filmmakers/AI-Verse-Skills@afde5c06307fba7d074de2929c2eb6c3dc6bdab8`

### Derived task list

- [x] **3.3-T1** Refresh System, OS and Skills refs and re-read the canonical identity/provider law, current OS resolver/provider contract and current Skills immutable-generation integration.
- [x] **3.3-T2** Freeze evidence-backed placement semantics: project-only user capabilities target the trusted active Workspace; reusable capabilities intended across projects or a practical domain target the user-owned local provider; OS built-ins and managed `aiverse-skills` are never writable user-authoring targets.
- [ ] **3.3-T3** Implement an OS-owned practical placement planner that accepts member-level reuse intent without asking for provider IDs or storage paths, preserves current qualified identity forms, and refuses project-only placement when no trusted active Workspace exists.
- [ ] **3.3-T4** Add focused acceptance tests and architecture documentation proving wider reusable intent is not forced into Workspace-private storage, managed Skills generation ownership is unchanged, and any cross-provider promotion remains a separately admitted migration with provenance/reference-repair requirements rather than silent identity continuity.
- [ ] **3.3-T5** Run exact-ref OS validation and reverify Skills generation/lifecycle alignment without modifying Skills unless current evidence exposes a real owner gap.
- [ ] **3.3-T6** Record exact implementation/evidence refs, close every Slice 3.3 acceptance criterion, update the canonical roadmap, and stop before Slice 3.4.
'''
if text.count(old) != 1:
    raise SystemExit(f'Slice 3.3 start guard failed: expected exactly one untouched block, found {text.count(old)}')
text = text.replace(old, new, 1)
path.write_text(text, encoding='utf-8')
