from pathlib import Path
import subprocess

path = Path('docs/SAFE-INFRASTRUCTURE-UPGRADE-AND-RECOVERY-IMPLEMENTATION-PLAN.md')
text = path.read_text(encoding='utf-8')
message = subprocess.check_output(['git', 'log', '-1', '--pretty=%s'], text=True).strip()

if message != 'TEMP run Safe Infrastructure Slice 3.2 task list':
    raise SystemExit(f'unexpected trigger for task-list helper: {message}')

old = '''## Slice 3.2 - Implement admitted OS Workspace migration/reference repair only if required

**Status:** NOT STARTED  
**Dependencies:** 3.1  
**Adaptive tasks:** derive from proven OS/reference graph and canonical identity contract
'''
new = '''## Slice 3.2 - Implement admitted OS Workspace migration/reference repair only if required

**Status:** IN PROGRESS  
**Dependencies:** 3.1  
**Adaptive tasks:** 3/5 COMPLETE

### Refreshed refs

- `aiverse-filmmakers/AI-Verse-System@ed98c92028dc7b0659ffb11a237976e924705034`
- `aiverse-filmmakers/AI-Verse-OS@88ce41a95554e1323ba34aa71b536b9e98475808`
- `aiverse-filmmakers/AI-Verse-Data@f8978f8f7a1bc94edecddc2662112233289159a3`
- `aiverse-filmmakers/AI-Verse-Brain@69f7912eeb35f0178f6952ff0554aec8d7f2c496`
- `aiverse-filmmakers/AI-Verse-Memory@f1327be48ba2ee0043959021365e6dbb9dcb1d3a`

### Derived task list

- [x] **3.2-T1** Refresh System, OS, Data, Brain and Memory refs and re-read the canonical durable-identity/Workspace law plus Slice 3.1 generation contract.
- [x] **3.2-T2** Reverify every proven path-coupled Workspace consumer and determine whether any owner now exposes an alternate admitted Workspace location, locator/registry, source generation or relocation contract.
- [x] **3.2-T3** Decide from owner evidence whether a Workspace migration/reference-repair operation is actually required. If no alternate admitted source/target exists, explicitly classify relocation as not admitted and do not create mutation code merely to satisfy the roadmap example.
- [ ] **3.2-T4** Prove reference repair and writable-slot retirement are not required when no path changes, and prove unsupported nested/misplaced/custom layouts continue to fail closed through the OS structural detector rather than being auto-moved.
- [ ] **3.2-T5** Record exact evidence and conditional acceptance results, validate the unchanged owner contracts/current System state, close Slice 3.2, and stop before Slice 3.3.
'''
if text.count(old) != 1:
    raise SystemExit(f'Slice 3.2 start guard failed: expected exactly one untouched block, found {text.count(old)}')
text = text.replace(old, new, 1)
path.write_text(text, encoding='utf-8')
