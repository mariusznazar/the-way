from pathlib import Path
import hashlib
import re
import subprocess

reports = Path('.runs/task-cycles/s7-cycle-remarks/reports').resolve()
fixture = reports / 'brief-plan-fixture.md'
temporary = reports / 'brief-plan-temporary.md'
brief = reports / 'brief-task-1.md'
bash = 'C:/Program Files/Git/bin/bash.exe'
script = 'C:/Users/Mariusz/.claude/plugins/cache/claude-plugins-official/superpowers/6.4.1/skills/subagent-driven-development/scripts/task-brief'
fixture.write_text('''# Plan — illustrative documentation correction

- Task: illustrative frozen task
- Spec: none
- Base: illustrative base

## Foundation entries

none

## Slices

### Slice 1 — Clarify the accepted answer

- **Goal:** An accepted answer is carried without another question.
- **Change:** `instructions.md`
- **Read:** `decision.md`
- **Checks:** Compare both authorized and unapproved-answer scenarios.
- **Depends on:** none

### Slice 2 — Present an unanswered proposal

- **Goal:** A proposal awaits the human's answer.
- **Change:** `questions.md`
- **Read:** `instructions.md`
- **Checks:** Compare accepted and rejected proposal scenarios.
- **Depends on:** Slice 1

## Independence and execution

Sequential: the question uses the acceptance instruction.

## Coverage

| Requirement | Slice |
|---|---|
| Accepted answer | 1 |
| Unanswered proposal | 2 |

## Choices

none
''', encoding='utf-8', newline='')
original = fixture.read_bytes()
log = []

def run(label, plan):
    command = [bash, script, plan.as_posix(), '1', brief.as_posix()]
    result = subprocess.run(command, capture_output=True)
    log.extend([label, 'Command argv: ' + repr(command), 'Exit: ' + str(result.returncode), 'STDOUT:', result.stdout.decode('utf-8', errors='replace'), 'STDERR:', result.stderr.decode('utf-8', errors='replace')])
    return result

negative = run('Before adapting the temporary copy', fixture)
assert negative.returncode == 3
try:
    temporary.write_bytes(re.sub(rb'(?m)^### Slice ([0-9]+)', rb'### Task \1', original))
    positive = run('After adapting only the temporary copy', temporary)
    assert positive.returncode == 0
    actual = brief.read_text(encoding='utf-8')
    expected = original.decode('utf-8').split('### Slice 1', 1)[1].split('### Slice 2', 1)[0]
    assert actual == '### Task 1' + expected
finally:
    temporary.unlink(missing_ok=True)
assert fixture.read_bytes() == original
assert not temporary.exists()
log.extend(['Observation: original headings are Slice; original extraction exits 3.', 'Observation: converted copy yields exactly the whole first slice with only its heading renamed; no second slice.', 'Observation: authoritative fixture unchanged, SHA256=' + hashlib.sha256(original).hexdigest(), 'Observation: temporary copy removed; extracted brief retained.', 'Scenario result: PASS'])
(reports / 'brief-adapter.txt').write_text('\n'.join(log) + '\n', encoding='utf-8')
print('brief adapter PASS')
