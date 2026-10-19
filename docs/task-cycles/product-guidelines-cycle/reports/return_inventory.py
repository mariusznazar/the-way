from pathlib import Path
import json
import re
import subprocess

reports = Path('.runs/task-cycles/product-guidelines-cycle/reports')
parts = {'product-guidelines', 'project-level', 'task-cycle', 'instruction-files', 'agent-instructions'}
original = json.loads((reports / 'foundation-completed-read-inventory.json').read_text())
read = {row['entry'] for row in original['entries'] if row['whole_read_completed']}
read.update(f'WAY-{number}/1' for number in range(213, 223))
terms = r'guideline|styleguide|exemplar|screenshot|appearance|visual|checklist|Applies to|When to read|waiting for human|waits for task|plan change|Minor|Important|script-unchecked|first file|first code|order of work|WAY-2(?:1[2-9]|2[0-2])|product-guidelines@'
rows = []
search = []
for name in ['decisions.md', 'invariants.md', 'part_map.md', 'glossary.md', 'environment_facts.md']:
    source = Path('foundations', name).read_text(encoding='utf-8')
    pattern = r'^### (WAY-\d+/\d+) .*' if name == 'decisions.md' else r'^## (.+)'
    headings = list(re.finditer(pattern, source, re.M))
    for index, match in enumerate(headings):
        block = source[match.start():headings[index+1].start() if index+1 < len(headings) else len(source)]
        ident = match[1]
        line = source.count('\n', 0, match.start()) + 1
        hits = sorted(set(item.lower() for item in re.findall(terms, block, re.I)))
        whole_read = ident in read if name in ['decisions.md', 'invariants.md'] else True
        if hits:
            search.append({'entry': ident, 'source': f'foundations/{name}:{line}', 'terms': hits, 'whole_read_completed': whole_read})
        if name not in ['decisions.md', 'invariants.md'] or not re.search(r'/\d+$', ident):
            continue
        field = 'Scope' if name == 'decisions.md' else 'Part'
        found = re.search(r'(?ms)^- \*\*' + field + r':\*\* (.*?)(?=^- \*\*|\n\n|\Z)', block)
        assert found, ident
        words = set(re.findall(r'[a-z]+(?:-[a-z]+)*', found[1]))
        selected = bool(parts & words or 'every' in words)
        rows.append({'entry': ident, 'source': f'foundations/{name}:{line}', 'field': found[1].replace('\n', ' '), 'scope_match': selected, 'whole_read_completed': whole_read})
target = subprocess.check_output(['git', 'rev-parse', 'origin/foundations'], text=True).strip()
head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip()
data = {'target': target, 'head': head, 'parts': sorted(parts), 'reading_basis': 'foundation-completed-read-inventory.json and ten whole new entries read in foundation stage; no source changes since those reads', 'entries': rows, 'search_matches': search}
(reports / 'return-source-inventory.json').write_text(json.dumps(data, indent=2), encoding='utf-8')
for name in ['decisions.md', 'invariants.md']:
    subset = [row for row in rows if f'/{name}:' in row['source']]
    print(name, 'population', len(subset), 'scope_matches', sum(row['scope_match'] for row in subset), 'whole_reads', sum(row['whole_read_completed'] for row in subset))
print('Semantic search matching entries:', len(search))
print('Unread matching entries:', ', '.join(row['entry'] for row in search if not row['whole_read_completed']) or 'none')
assert all(row['whole_read_completed'] for row in rows if row['scope_match'])
assert all(row['whole_read_completed'] for row in search)
