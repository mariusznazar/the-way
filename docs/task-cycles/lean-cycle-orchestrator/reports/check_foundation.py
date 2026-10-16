from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding='ascii', errors='backslashreplace')
reports = Path('docs/task-cycles/lean-cycle-orchestrator/reports')
checks = [
    ('foundation-decisions', ['python', '-B', 'elements/decisions/format_guard.py', 'foundations/decisions.md', '--base', 'none', '--merge-onto', 'none']),
    ('foundation-invariants', ['python', '-B', 'elements/invariants/format_guard.py', 'foundations/invariants.md', '--base', 'none', '--merge-onto', 'none']),
    ('foundation-part-map', ['python', '-B', 'elements/part-map/format_guard.py', 'foundations/part_map.md', '--base', 'none']),
    ('foundation-task-cycle-tests', ['python', '-B', 'gate/run_tests.py', 'task-cycle']),
    ('foundation-decisions-tests', ['python', '-B', 'gate/run_tests.py', 'elements/decisions']),
    ('foundation-critical-flow-tests', ['python', '-B', 'gate/run_tests.py', 'gate']),
]
results = []
for name, command in checks:
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output_path = reports / (name + '.txt')
    output_path.write_bytes(result.stdout)
    results.append({'command': command, 'exit_code': result.returncode, 'output': str(output_path)})
    print(name, 'exit', result.returncode, flush=True)
    output = result.stdout.decode('utf-8', errors='replace')
    for line in output.splitlines():
        if re.search(r'(?i)error|fail|warning|unchecked|^Ran |^OK$|^passed|^summary|^\d+ ', line):
            print(line, flush=True)
(reports / 'foundation-checks.json').write_text(json.dumps(results, indent=2) + '\n', encoding='utf-8')

source = Path('foundations/decisions.md').read_text(encoding='utf-8')
entries = re.findall(r'(?ms)^### (WAY-\d+)/\d+[^\n]*\n\n(.*?)(?=^### WAY-|\Z)', source)
fingerprints = {key: hashlib.sha256(re.sub(r'[ \r\n]+', ' ', value.split('\n\n', 1)[0]).strip(' ').encode()).hexdigest()[:8] for key, value in entries}
checked = []
failures = []
for path in Path('foundations').glob('*.md'):
    for number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        for key, actual in re.findall(r'(WAY-\d+)@([0-9a-f]{8})', line):
            checked.append((str(path), number, key, actual))
            if actual != fingerprints.get(key):
                failures.append((str(path), number, key, actual, fingerprints.get(key)))
result = {'checked_references': len(checked), 'failures': failures, 'changed_fingerprints': {key: fingerprints[key] for key in ['WAY-125', 'WAY-148', 'WAY-157', 'WAY-158', 'WAY-159', 'WAY-160']}}
(reports / 'foundation-current-fingerprints.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print('current decision fingerprints:', len(checked), 'references;', len(failures), 'failures')
if failures:
    print(failures)
sys.exit(1 if failures or any(item['exit_code'] for item in results) else 0)
