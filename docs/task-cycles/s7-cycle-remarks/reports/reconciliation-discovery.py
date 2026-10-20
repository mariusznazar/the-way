from pathlib import Path
import json
import re
import subprocess

reports = Path('.runs/task-cycles/s7-cycle-remarks/reports')
revision = subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True, check=True).stdout.decode().strip()
prior = json.loads((reports / 'foundation-selection.json').read_text(encoding='utf-8'))
parts = {'decisions', 'invariants', 'part-map', 'task-cycle', 'elements-common', 'project-level', 'agent-instructions', 'environment-facts', 'product-guidelines'}
decision_text = Path('foundations/decisions.md').read_text(encoding='utf-8')
entries = list(re.finditer(r'^### (WAY-\d+)/(\d+)[^\n]*\n.*?(?=^### |\Z)', decision_text, re.M | re.S))
latest = {}
for match in entries:
    number, version = match.group(1), int(match.group(2))
    if number not in latest or latest[number][0] < version:
        latest[number] = (version, match)
expected = []
for number, (version, match) in latest.items():
    scope = re.search(r'^- \*\*Scope:\*\* (.*?)(?=\n- \*\*)', match.group(0), re.M | re.S)
    if scope is None:
        raise ValueError('Missing Scope: ' + number)
    matches = parts.intersection(re.findall(r'[a-z]+(?:-[a-z]+)*', scope.group(1)))
    if matches:
        expected.append({'identifier': number, 'version': version, 'source': 'foundations/decisions.md', 'line': decision_text[:match.start()].count('\n') + 1, 'parts': sorted(matches)})
read_ids = set(prior['decisions_selected_and_read']) | {'WAY-224'}
missing = sorted(set(row['identifier'] for row in expected) - read_ids)
data = {'revision': revision, 'parts': sorted(parts), 'expected_decisions': expected, 'read_decisions': sorted(read_ids, key=lambda value: int(value.split('-')[1])), 'unread_expected': missing, 'read_evidence': 'Same author read all baseline foundation files whole, then read/wrote whole changed entries WAY-30, WAY-46, WAY-172 and WAY-224; WAY-224 was reread and amended for explicit precedence in this settlement; other foundation entries remain unchanged since those stages. Whole-read location evidence is in foundation-selection.json; current source lines are above.'}
inv_text = Path('foundations/invariants.md').read_text(encoding='utf-8')
invariants = []
for match in re.finditer(r'^## ([^\n]+)\n.*?(?=^## |\Z)', inv_text, re.M | re.S):
    part = re.search(r'^- \*\*Part:\*\* (.*?)(?=\n- \*\*)', match.group(0), re.M | re.S)
    if part and (part.group(1).strip() == 'every' or parts.intersection(re.findall(r'[a-z]+(?:-[a-z]+)*', part.group(1)))):
        invariants.append({'identifier': match.group(1), 'source': 'foundations/invariants.md', 'line': inv_text[:match.start()].count('\n') + 1, 'part': part.group(1).strip()})
data['expected_invariants'] = invariants
data['read_invariants'] = prior['invariants_selected_and_read']
patterns = {'approval': r'approved|approval|approver|accept|meaning|contradict|narrows', 'failure_candidate': r'failure mode|criticality|candidate|deferred|question|counterargument', 'operational': r'return step|commit message|chronicle|fingerprint|brief|cycle record|plan|workspace|operational error|cannot read|unchecked'}
data['search_patterns'] = patterns
data['search_hits'] = {}
data['foundation_blobs'] = {}
for filename in ['foundations/decisions.md', 'foundations/invariants.md', 'foundations/part_map.md', 'foundations/glossary.md', 'foundations/environment_facts.md']:
    content = Path(filename).read_text(encoding='utf-8')
    findings = {}
    heading = '(preamble)'
    for line_no, line in enumerate(content.splitlines(), 1):
        if re.match(r'^#{2,3} ', line):
            heading = line.lstrip('# ')
        for label, pattern in patterns.items():
            if re.search(pattern, line, re.I):
                findings.setdefault(label, {}).setdefault(heading, []).append(line_no)
    data['search_hits'][filename] = findings
    data['foundation_blobs'][filename] = subprocess.run(['git', 'rev-parse', revision + ':' + filename], capture_output=True, check=True).stdout.decode().strip()
(reports / 'reconciliation-selection.json').write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print('revision: ' + revision)
print('expected decisions: ' + str(len(expected)))
print('read decisions: ' + str(len(read_ids)))
print('unread expected: ' + str(len(missing)))
print('expected invariants: ' + str(len(invariants)))
print('read invariant sections: ' + str(len(data['read_invariants'])))
print('foundation search domains: ' + str(len(data['search_hits'])))
print('guidelines directory exists: ' + str(Path('guidelines').is_dir()))

target = 'f0b5eb131de5d681ee3fcdeb264e9f88778af2ec'
expected_head = '9c2a87c28ff0359bb0a48425fa23c5d8119a63a0'
assert revision == expected_head
assert subprocess.run(['git', 'rev-parse', 'foundations'], capture_output=True, check=True).stdout.decode().strip() == target
searches = {'target': {}, 'head': {}}
snapshot_matches = {}
incoming = {}
for filename in data['foundation_blobs']:
    target_bytes = subprocess.run(['git', 'cat-file', 'blob', target + ':' + filename], capture_output=True, check=True).stdout
    head_bytes = subprocess.run(['git', 'cat-file', 'blob', revision + ':' + filename], capture_output=True, check=True).stdout
    assert Path(filename).read_bytes() == head_bytes, filename
    snapshot_matches[filename] = {'working_tree_matches_head': True, 'target_matches_head': target_bytes == head_bytes}
    for label, content in [('target', target_bytes.decode('utf-8')), ('head', head_bytes.decode('utf-8'))]:
        records = []
        heading = '(preamble)'
        for line_no, line in enumerate(content.splitlines(), 1):
            if re.match(r'^#{2,3} ', line):
                heading = line.lstrip('# ')
            labels = [key for key, pattern in patterns.items() if re.search(pattern, line, re.I)]
            if labels:
                records.append({'line': line_no, 'entry': heading, 'matched': labels})
        searches[label][filename] = records
    incoming[filename] = [{'line': n, 'text': line} for n, line in enumerate(head_bytes.decode('utf-8').splitlines(), 1)
                          if re.search(r'WAY-(30|46|172|224)@', line)]
all_foundation = '\n'.join(Path(name).read_text(encoding='utf-8') for name in data['foundation_blobs'])
assert 'WAY-46@7511b86f' in all_foundation
assert 'WAY-30@6924312f' not in all_foundation
assert 'WAY-46@a5f43e40' not in all_foundation
assert 'WAY-224@' not in all_foundation
read_invariants = set(data['read_invariants'])
unread_invariants = sorted({row['identifier'] for row in invariants} - read_invariants)
assert not unread_invariants, unread_invariants
data.update({'target': target, 'target_equals_original_base': True, 'snapshot_comparison': snapshot_matches,
             'target_and_head_searches': searches, 'incoming_changed_decisions': incoming,
             'unread_expected_invariants': unread_invariants,
             'stale_prior_fingerprints_found': False,
             'read_evidence': 'Original author whole reads of all five foundation elements and all current entries, with subsequent whole changed-entry reads; target is the unchanged original base, and final source snapshots match the reviewed working files. New R1 source rereads are recorded in final-assessment-settlement-report.md.'})
(reports / 'reconciliation-selection.json').write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print('target: ' + target)
print('target unchanged from original base: True')
print('working foundation snapshots match head: True')
print('unread expected invariants: ' + str(len(unread_invariants)))
print('stale prior fingerprints: 0; incoming WAY-224 fingerprints: 0')
print('incoming references: ' + str(sum(len(rows) for rows in incoming.values())))
