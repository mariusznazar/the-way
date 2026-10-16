"""Run available repository checks and retain complete UTF-8 output."""
from pathlib import Path
import subprocess, os, json, re
root = Path(__file__).resolve().parents[4]
reports = Path(__file__).resolve().parent
commands = [
    ('task-cycle-tests', ['python', '-B', 'gate/run_tests.py', 'task-cycle']),
    ('decision-tests', ['python', '-B', 'gate/run_tests.py', 'elements/decisions']),
    ('critical-flow-tests', ['python', '-B', 'gate/run_tests.py', 'gate']),
    ('decision-guard', ['python', '-B', 'elements/decisions/format_guard.py', 'foundations/decisions.md', '--base', 'none', '--merge-onto', 'none']),
    ('invariant-guard', ['python', '-B', 'elements/invariants/format_guard.py', 'foundations/invariants.md', '--base', 'none', '--merge-onto', 'none']),
    ('part-map-guard', ['python', '-B', 'elements/part-map/format_guard.py', 'foundations/part_map.md', '--base', 'none']),
    ('whitespace', ['git', 'diff', '--check', '41cfbe55c17981500490ffddd24fc1fe0ec1c6ef..HEAD']),
]
rows = []
for name, command in commands:
    env = dict(os.environ, PYTHONIOENCODING='utf-8')
    result = subprocess.run(command, cwd=root, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    path = reports / ('final-' + name + '.txt')
    path.write_bytes(result.stdout)
    output = result.stdout.decode('utf-8', errors='replace')
    selected = [line for line in output.splitlines() if re.search(r'(?i)(error|fail|warning|unchecked|^Ran |^OK$|summary)', line)]
    rows.append(dict(name=name, command=command, exit_code=result.returncode, log=path.name, summary=selected))
(reports / 'final-checks.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding='utf-8')
for row in rows:
    print(row['name'] + ': exit=' + str(row['exit_code']))
    for line in row['summary']:
        print(line.encode('ascii', 'backslashreplace').decode())
raise SystemExit(int(any(row['exit_code'] != 0 for row in rows)))
