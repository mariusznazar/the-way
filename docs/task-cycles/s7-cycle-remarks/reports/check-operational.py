from pathlib import Path
import subprocess

reports = Path('.runs/task-cycles/s7-cycle-remarks/reports')
commands = [
    ('instructions-after', ['python', '-B', 'instruction-files/check_instructions.py', '.']),
    ('operational-agent-instructions', ['python', '-B', 'gate/run_tests.py', 'agent-instructions']),
    ('operational-task-cycle', ['python', '-B', 'gate/run_tests.py', 'task-cycle']),
    ('operational-project-level', ['python', '-B', 'gate/run_tests.py', 'project-level']),
    ('operational-part-map', ['python', '-B', 'gate/run_tests.py', 'elements/part-map']),
    ('operational-elements-common', ['python', '-B', 'gate/run_tests.py', 'elements/common']),
    ('operational-diff-check', ['git', 'diff', '--check']),
]
for name, command in commands:
    result = subprocess.run(command, capture_output=True)
    (reports / (name + '.txt')).write_text('Command: ' + ' '.join(command) + '\nExit: ' + str(result.returncode) + '\n\nSTDOUT:\n' + result.stdout.decode('utf-8', errors='replace') + '\nSTDERR:\n' + result.stderr.decode('utf-8', errors='replace'), encoding='utf-8')
    print(name + ': exit ' + str(result.returncode), flush=True)
