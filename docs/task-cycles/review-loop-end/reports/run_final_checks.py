"""Run the available repository checks and retain complete UTF-8 output."""
from pathlib import Path
import subprocess, os, json, re, sys
root = Path(__file__).resolve().parents[4]
reports = Path(__file__).resolve().parent
prefix = sys.argv[1] if len(sys.argv) > 1 else 'final'
base = 'e7f7c3a15c3f80143f9ad582ec785c993cff3779'
commands = [
    ('task-cycle-tests', ['python', '-B', 'gate/run_tests.py', 'task-cycle']),
    ('decision-tests', ['python', '-B', 'gate/run_tests.py', 'elements/decisions']),
    ('agent-instructions-tests', ['python', '-B', 'gate/run_tests.py', 'agent-instructions']),
    ('critical-flow-tests', ['python', '-B', 'gate/run_tests.py', 'gate']),
    ('decision-guard', ['python', '-B', 'elements/decisions/format_guard.py', 'foundations/decisions.md', '--base', 'none', '--merge-onto', 'none']),
    ('invariant-guard', ['python', '-B', 'elements/invariants/format_guard.py', 'foundations/invariants.md', '--base', 'none', '--merge-onto', 'none']),
    ('part-map-guard', ['python', '-B', 'elements/part-map/format_guard.py', 'foundations/part_map.md', '--base', 'none']),
    ('skill-entry-points', ['python', '-B', 'agent-instructions/skill_entry_points.py']),
    ('whitespace', ['git', 'diff', '--check', base + '..HEAD']),
]
rows = []
for name, command in commands:
    env = dict(os.environ, PYTHONIOENCODING='utf-8')
    result = subprocess.run(command, cwd=root, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    path = reports / (prefix + '-' + name + '.txt')
    path.write_bytes(result.stdout)
    output = result.stdout.decode('utf-8', errors='replace')
    selected = [line for line in output.splitlines() if re.search(r'(?i)(error|fail|warning|unchecked|^Ran |^OK$|summary|stale|current)', line)]
    rows.append(dict(name=name, command=command, exit_code=result.returncode, log=path.name, summary=selected))
(reports / (prefix + '-checks.json')).write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding='utf-8')
for row in rows:
    print(row['name'] + ': exit=' + str(row['exit_code']) + ' lines=' + str(len(row['summary'])))
raise SystemExit(int(any(row['exit_code'] != 0 for row in rows)))
