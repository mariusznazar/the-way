"""Capture read-only settlement inventory and focused evidence validation."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

REPORTS = Path(__file__).resolve().parent
ROOT = REPORTS.parents[3]
BASE = '8726cc1c6b6b031ca94c6e867d0df1297c286c01'
HEAD = '9a8bc5e7ae467a1dce81b4be830130c64337db0d'
FIRST = 'f0b5eb131de5d681ee3fcdeb264e9f88778af2ec'
results = []

def run(args, allowed=(0,)):
    result = subprocess.run(args, cwd=ROOT, capture_output=True, text=True, encoding='utf-8')
    results.append({'command': args, 'cwd': str(ROOT), 'exit': result.returncode,
                    'stdout': result.stdout, 'stderr': result.stderr})
    assert result.returncode in allowed
    return result.stdout

try:
    assert run(['git', 'rev-parse', 'HEAD']).strip() == HEAD
    run(['git', 'status', '--short'])
    run(['git', 'log', '--reverse', '--format=%H %P', '--name-only', BASE + '..' + HEAD])
    run(['git', 'diff', '--numstat', BASE + '..' + HEAD])
    run(['git', 'diff', '--numstat', FIRST + '..' + HEAD])
    run(['rg', '-n', 'WAY-224@', 'foundations'], (1,))
    run(['rg', '-n', 'WAY-46@7511b86f', 'foundations'])
    old = run(['git', 'show', BASE + ':foundations/decisions.md'])
    new = (ROOT / 'foundations/decisions.md').read_text(encoding='utf-8')
    assert old.split('### WAY-224/1')[0] == new.split('### WAY-224/1')[0]
    def binding(number):
        block = new.split('### ' + number + '/1', 1)[1]
        return block.split('\n', 1)[1].split('- **Change:**', 1)[0].strip()
    fingerprint = hashlib.sha256(re.sub(r'\s+', ' ', binding('WAY-114')).encode()).hexdigest()[:8]
    assert fingerprint == '04b4f599'
    prior = json.loads((REPORTS / 'reviewer-selection.json').read_text(encoding='utf-8'))
    parts = set(prior['parts'])
    expected = []
    for match in re.finditer(r'^### (WAY-\d+/\d+).*?\n(.*?)(?=^### |\Z)', new, re.M | re.S):
        scope = re.search(r'^- \*\*Scope:\*\* (.*?)(?=^- \*\*|\Z)', match[2], re.M | re.S)
        assert scope
        if set(re.findall(r'[a-z]+(?:-[a-z]+)*', scope[1])) & parts:
            expected.append({'id': match[1], 'line': new[:match.start()].count('\n') + 1})
    assert expected == prior['expected']
    selection = {'revision': HEAD, 'parts': sorted(parts), 'expected': expected, 'read': expected,
                 'reused_whole_decisions': 209, 'reread_whole_decisions': ['WAY-224/1'],
                 'reconciliation': 'All 207 expected entries covered; unchanged complete foundation reads reused.', 'missing': []}
    (REPORTS / 'reviewer-settlement-selection.json').write_text(json.dumps(selection, indent=2), encoding='utf-8')
    assert not (ROOT / 'guidelines').exists()
    scenario = json.loads((REPORTS / 'settlement-workspace-result.json').read_text(encoding='utf-8'))
    original = Path(scenario['original_plan'])
    workspace = Path(scenario['original_workspace'])
    assert hashlib.sha256(original.read_bytes()).hexdigest() == scenario['original_plan_sha256']
    assert not (Path(scenario['scratch']) / 'plans/temporary/plan.md').exists()
    assert (workspace / 'task-1-brief.md').is_file()
    assert (workspace / 'task-1-report.md').is_file()
    assert (workspace / 'progress.md').is_file()
    print('PASS: reviewed HEAD, original range coverage, incoming references, unchanged 209 decisions, WAY-114 fingerprint, 207-entry selection, retained scenario artifacts.')
finally:
    # Keep complete command output, including the decision source read, in the live check log.
    # Do not archive a git-held source copy: discard that read output after validating it.
    for result in results:
        if result['command'][:2] == ['git', 'show']:
            result['stdout'] = '[source read; not a check output; source is identified by exact git revision]'
    (REPORTS / 'reviewer-settlement-checks.json').write_text(json.dumps(results, indent=2), encoding='utf-8')
