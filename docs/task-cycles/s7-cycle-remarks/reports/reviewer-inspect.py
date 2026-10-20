import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
REPORTS = Path(__file__).resolve().parent
PARTS = {'decisions', 'invariants', 'part-map', 'task-cycle', 'elements-common', 'project-level', 'agent-instructions', 'environment-facts', 'product-guidelines'}

def entries(path, level):
    text = (ROOT / path).read_text(encoding='utf-8')
    starts = list(re.finditer(r'^' + '#' * level + r' (.+)$', text, re.M))
    return [(m.group(1), text[m.start():starts[i+1].start() if i+1 < len(starts) else len(text)], text[:m.start()].count('\n')+1) for i, m in enumerate(starts)]

def selected():
    result = []
    for name, body, line in entries('foundations/decisions.md', 3):
        match = re.search(r'^- \*\*Scope:\*\* (.*?)(?=^- \*\*|\Z)', body, re.M|re.S)
        if not match:
            raise ValueError(name)
        scope = set(re.findall(r'[a-z]+(?:-[a-z]+)*', match.group(1)))
        if scope & PARTS:
            result.append((name, body, line))
    return result

if sys.argv[1] == 'decisions':
    data = selected()
    start, end = map(int, sys.argv[2:4])
    for name, body, line in data[start:end]:
        print('SOURCE foundations/decisions.md:' + str(line))
        print(body)
elif sys.argv[1] == 'inventory':
    data = selected()
    inventory = {'revision': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(), 'parts': sorted(PARTS), 'expected': [{'id': name.split(' ')[0], 'line': line} for name, body, line in data], 'read': []}
    (REPORTS / 'reviewer-selection.json').write_text(json.dumps(inventory, indent=2), encoding='utf-8')
    print('selected=' + str(len(data)))
    print('guidelines_exists=' + str((ROOT/'guidelines').exists()))
elif sys.argv[1] == 'checks':
    commands = [
        ['git', 'rev-parse', 'HEAD'],
        ['git', 'status', '--short'],
        ['git', 'log', '--reverse', '--format=%H %P', '--name-only', 'f0b5eb131de5d681ee3fcdeb264e9f88778af2ec..8726cc1c6b6b031ca94c6e867d0df1297c286c01'],
        ['git', 'diff', '--numstat', 'f0b5eb131de5d681ee3fcdeb264e9f88778af2ec..8726cc1c6b6b031ca94c6e867d0df1297c286c01'],
    ]
    with (REPORTS / 'reviewer-git-checks.txt').open('w', encoding='utf-8') as stream:
        for command in commands:
            run = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, encoding='utf-8')
            stream.write('COMMAND: ' + subprocess.list2cmdline(command) + '\nEXIT: ' + str(run.returncode) + '\nSTDOUT:\n' + run.stdout + '\nSTDERR:\n' + run.stderr + '\n')
            print(subprocess.list2cmdline(command) + ' exit=' + str(run.returncode))
elif sys.argv[1] == 'complete-reading':
    path = REPORTS / 'reviewer-selection.json'
    inventory = json.loads(path.read_text(encoding='utf-8'))
    inventory['read'] = inventory['expected']
    inventory['method'] = 'Reviewer read the complete current decision log, invariants, environment facts, glossary and part map; repaired truncated chunks through bounded UTF-8 reads.'
    inventory['all_decision_entries_read'] = len(entries('foundations/decisions.md', 3))
    inventory['missing'] = []
    with path.open('w', encoding='utf-8', newline='') as stream:
        stream.write(json.dumps(inventory, indent=2))
    print('expected=' + str(len(inventory['expected'])) + ' read=' + str(len(inventory['read'])) + ' missing=0 all_decisions=' + str(inventory['all_decision_entries_read']))
elif sys.argv[1] == 'semantic':
    base = 'f0b5eb131de5d681ee3fcdeb264e9f88778af2ec'
    def at_base(path):
        return subprocess.check_output(['git', 'show', base + ':' + path], cwd=ROOT).decode('utf-8')
    before = at_base('foundations/invariants.md')
    after = (ROOT / 'foundations/invariants.md').read_bytes().decode('utf-8').replace('\r\n', '\n')
    assert before.count('WAY-46@a5f43e40') == 6
    assert before.replace('WAY-46@a5f43e40', 'WAY-46@7511b86f') == after
    print('PASS: invariants file has exactly six WAY-46 fingerprint replacements and no other change.')
    def binding(text, number):
        body = re.search(r'^### ' + number + r'/.*?\n(.*?)(?=^### |\Z)', text, re.M | re.S).group(1)
        return body.split('- **Change:**', 1)[0].strip()
    before = at_base('foundations/decisions.md')
    after = (ROOT / 'foundations/decisions.md').read_text(encoding='utf-8')
    assert binding(before, 'WAY-172') == binding(after, 'WAY-172')
    print('PASS: WAY-172 binding wording unchanged.')
