from pathlib import Path
import json
import subprocess
import sys

reports = Path('.runs/task-cycles/s7-cycle-remarks/reports')
phase = sys.argv[1]
target = 'f0b5eb131de5d681ee3fcdeb264e9f88778af2ec'
commands = {
    'foundation': [
        ('decisions', ['python', '-B', 'gate/run_tests.py', 'elements/decisions']),
        ('decision-form', ['python', '-B', 'elements/decisions/format_guard.py', '--base', 'none', '--merge-onto', 'none']),
        ('decision-relations', ['python', '-B', 'elements/decisions/format_guard.py', '--base', 'none', '--merge-onto', target]),
        ('invariant-relations', ['python', '-B', 'elements/invariants/format_guard.py', '--base', 'none', '--merge-onto', target]),
        ('selection', ['python', '-B', str(reports / 'settlement-selection.py')]),
        ('incoming', ['rg', '-n', 'WAY-224@', 'foundations']),
        ('incoming-control', ['rg', '-n', 'WAY-46@7511b86f', 'foundations']),
        ('whitespace-foundation', ['git', 'diff', '--check']),
    ],
    'operational': [
        ('task-cycle', ['python', '-B', 'gate/run_tests.py', 'task-cycle']),
        ('agent-instructions', ['python', '-B', 'gate/run_tests.py', 'agent-instructions']),
        ('workspace-scenario', ['python', '-B', str(reports / 'check-settlement-workspace.py')]),
        ('whitespace-operational', ['git', 'diff', '--check']),
    ],
}[phase]
results = []
for name, command in commands:
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = 'settlement-' + name + '.txt'
    (reports / output).write_bytes(result.stdout)
    results.append({'name': name, 'command': command, 'exit': result.returncode, 'output': output})
    print(name + ': exit ' + str(result.returncode))
(reports / ('settlement-checks-' + phase + '.json')).write_text(json.dumps(results, indent=2) + '\n', encoding='utf-8')
