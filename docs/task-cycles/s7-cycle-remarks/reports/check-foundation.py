from pathlib import Path
import subprocess
import sys

root = Path.cwd()
reports = root / '.runs/task-cycles/s7-cycle-remarks/reports'
sys.path.insert(0, str(root / 'relation-model'))
from fingerprint import fingerprint

path = root / 'foundations/decisions.md'
with path.open(encoding='utf-8', newline='') as stream:
    text = stream.read()
entry = text.replace('\r\n', '\n').split('### WAY-46/1', 1)[1].split('### WAY-47/1', 1)[0]
binding = entry.split('\n\n', 1)[1].split('- **Change:**', 1)[0].strip()
fp = fingerprint(binding)
for filename in ('foundations/decisions.md', 'foundations/invariants.md'):
    path = root / filename
    with path.open(encoding='utf-8', newline='') as stream:
        content = stream.read()
    with path.open('w', encoding='utf-8', newline='') as stream:
        stream.write(content.replace('WAY-46@4b001fd2', 'WAY-46@' + fp))
print('WAY-46 ' + fp)

commands = [
    ('post-decisions', ['python', '-B', 'elements/decisions/format_guard.py', '--base', 'none', '--merge-onto', 'none']),
    ('post-invariants', ['python', '-B', 'elements/invariants/format_guard.py', '--base', 'none', '--merge-onto', 'none']),
    ('post-part-map', ['python', '-B', 'elements/part-map/format_guard.py', '--base', 'none']),
    ('tests-decisions', ['python', '-B', 'gate/run_tests.py', 'elements/decisions']),
    ('tests-invariants', ['python', '-B', 'gate/run_tests.py', 'elements/invariants']),
    ('tests-part-map', ['python', '-B', 'gate/run_tests.py', 'elements/part-map']),
    ('tests-gate', ['python', '-B', 'gate/run_tests.py', 'gate']),
]
for name, command in commands:
    result = subprocess.run(command, capture_output=True)
    with (reports / (name + '.txt')).open('w', encoding='utf-8', newline='') as stream:
        stream.write('Command: ' + ' '.join(command) + '\nExit: ' + str(result.returncode) + '\n\nSTDOUT:\n')
        stream.write(result.stdout.decode('utf-8', errors='replace'))
        stream.write('\nSTDERR:\n')
        stream.write(result.stderr.decode('utf-8', errors='replace'))
    print(name + ': exit ' + str(result.returncode), flush=True)
