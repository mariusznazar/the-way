"""Run the available repository checks and retain complete UTF-8 output.

Usage: python -B run_checks.py <prefix> [tests|guards|all]
"""
from pathlib import Path
import subprocess, os, json, re, sys
root = Path(__file__).resolve().parents[4]
reports = Path(__file__).resolve().parent
prefix = sys.argv[1] if len(sys.argv) > 1 else 'final'
which = sys.argv[2] if len(sys.argv) > 2 else 'all'
base = '96623ed7710100fe6e11a0ce3c052fc44d4af52d'
test_dirs = ['gate', 'elements/decisions', 'elements/invariants', 'elements/glossary', 'elements/part-map',
             'elements/environment-facts', 'relation-model', 'agent-instructions', 'installation',
             'instruction-files', 'task-cycle', 'project-level', 'product-guidelines']
extra = [d for d in sys.argv[3:]]
tests = [('tests-' + d.replace('/', '-'), ['python', '-B', 'gate/run_tests.py', d]) for d in test_dirs + extra
         if (root / d).is_dir()]
guards = [
    ('decision-guard', ['python', '-B', 'elements/decisions/format_guard.py', 'foundations/decisions.md', '--base', 'none', '--merge-onto', 'none']),
    ('invariant-guard', ['python', '-B', 'elements/invariants/format_guard.py', 'foundations/invariants.md', '--base', 'none', '--merge-onto', 'none']),
    ('part-map-guard', ['python', '-B', 'elements/part-map/format_guard.py', 'foundations/part_map.md', '--base', 'none']),
    ('glossary-guard', ['python', '-B', 'elements/glossary/format_guard.py', 'foundations/glossary.md', '--base', 'none', '--merge-onto', 'none']),
    ('environment-facts-guard', ['python', '-B', 'elements/environment-facts/format_guard.py', 'foundations/environment_facts.md', '--base', 'none', '--merge-onto', 'none']),
    ('form-check', ['python', '-B', 'product-guidelines/form_check.py', '--record', '.runs/guidelines-form.jsonl']),
    ('form-check-merge', ['python', '-B', 'product-guidelines/form_check.py', '--merge-onto', 'none', '--record', '.runs/guidelines-reference.jsonl']),
    ('skill-entry-points', ['python', '-B', 'agent-instructions/skill_entry_points.py']),
    ('whitespace', ['git', 'diff', '--check', base + '..HEAD']),
]
commands = (tests if which in ('tests', 'all') else []) + (guards if which in ('guards', 'all') else [])
rows = []
for name, command in commands:
    env = dict(os.environ, PYTHONIOENCODING='utf-8')
    result = subprocess.run(command, cwd=root, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    path = reports / (prefix + '-' + name + '.txt')
    path.write_bytes(result.stdout)
    output = result.stdout.decode('utf-8', errors='replace')
    selected = [line for line in output.splitlines() if re.search(r'(?i)(error|fail|warning|unchecked|^Ran |^OK|summary|stale|current)', line)]
    rows.append(dict(name=name, command=command, exit_code=result.returncode, log=path.name, summary=selected))
(reports / (prefix + '-checks.json')).write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding='utf-8')
for row in rows:
    print(row['name'] + ': exit=' + str(row['exit_code']) + ' lines=' + str(len(row['summary'])))
raise SystemExit(int(any(row['exit_code'] != 0 for row in rows)))
