from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import json
import os
import re
import subprocess

root = Path.cwd()
record = root / '.runs/task-cycles/selective-document-reading/reports'
environment = dict(os.environ, PYTHONIOENCODING='utf-8')
commands = {
    'request-decision-guard': ['python', '-B', 'elements/decisions/format_guard.py',
                             'foundations/decisions.md', '--base', 'none', '--merge-onto', 'none',
                             '--record', str(record / 'request-decision-guard.jsonl')],
    'request-glossary-diagnostic': ['python', '-B', 'elements/glossary/format_guard.py',
                                  'foundations/glossary.md', '--base',
                                  '52b9d487efeafe37c46ad2b9f10d60c13a885e63', '--merge-onto', 'none'],
    'request-relations': ['python', '-B', str(record / 'verify_foundation.py')],
    'request-diff': ['git', 'diff', '--check', '52b9d487efeafe37c46ad2b9f10d60c13a885e63'],
}


def check(item):
    name, command = item
    run = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env=environment)
    (record / (name + '.txt')).write_bytes(run.stdout)
    return {'name': name, 'command': command, 'exit': run.returncode}


with ThreadPoolExecutor(max_workers=4) as pool:
    results = list(pool.map(check, commands.items()))
assert all(result['exit'] == 0 for result in results), results
source_paths = subprocess.check_output(['git', 'diff', '--name-only', '52b9d487efeafe37c46ad2b9f10d60c13a885e63'], text=True).splitlines()
assert len(source_paths) == 14
controls = []
for path in source_paths:
    if re.search(rb'[\x00-\x08\x0b\x0c\x0e-\x1f]', (root / path).read_bytes()):
        controls.append(path)
assert not controls, controls
data = {'source_head_before_url_commit': subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip(),
        'commands': results, 'control_characters': 0, 'source_files': source_paths,
        'mutations': 'Only four approval request URL substitutions after assessed/settled source.'}
(record / 'request-verification.json').write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')
print('commands_passed', len(results), 'controls', 0, 'source_files', len(source_paths))
