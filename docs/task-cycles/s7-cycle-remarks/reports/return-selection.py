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
data = {'revision': revision, 'parts': sorted(parts), 'expected_decisions': expected, 'read_decisions': sorted(read_ids, key=lambda value: int(value.split('-')[1])), 'unread_expected': missing, 'read_evidence': 'Same author read all baseline foundation files whole, then read/wrote whole changed entries WAY-30, WAY-46, WAY-172 and WAY-224; the accepted current diff is unchanged since those stages. Whole-read location evidence is in foundation-selection.json; current source lines are above.'}
inv_text = Path('foundations/invariants.md').read_text(encoding='utf-8')
invariants = []
for match in re.finditer(r'^## ([^\n]+)\n.*?(?=^## |\Z)', inv_text, re.M | re.S):
    part = re.search(r'^- \*\*Part:\*\* (.*?)(?=\n- \*\*)', match.group(0), re.M | re.S)
    if part and (part.group(1).strip() == 'every' or parts.intersection(re.findall(r'[a-z]+(?:-[a-z]+)*', part.group(1)))):
        invariants.append({'identifier': match.group(1), 'source': 'foundations/invariants.md', 'line': inv_text[:match.start()].count('\n') + 1, 'part': part.group(1).strip()})
data['expected_invariants'] = invariants
data['read_invariants'] = prior['invariants_selected_and_read']
patterns = {'approval': r'approved|approval|approver|accept|meaning|contradict|narrows', 'failure_candidate': r'failure mode|criticality|candidate|deferred|question|counterargument', 'operational': r'return step|commit message|chronicle|fingerprint|brief|cycle record|plan'}
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
(reports / 'return-selection.json').write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print('revision: ' + revision)
print('expected decisions: ' + str(len(expected)))
print('read decisions: ' + str(len(read_ids)))
print('unread expected: ' + str(len(missing)))
print('expected invariants: ' + str(len(invariants)))
print('read invariant sections: ' + str(len(data['read_invariants'])))
print('foundation search domains: ' + str(len(data['search_hits'])))
print('guidelines directory exists: ' + str(Path('guidelines').is_dir()))
