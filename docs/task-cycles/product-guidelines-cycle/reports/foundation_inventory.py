from pathlib import Path
import json
import re

root = Path('foundations')
reports = Path('.runs/task-cycles/product-guidelines-cycle/reports')
parts = {'product-guidelines', 'project-level', 'task-cycle', 'instruction-files', 'agent-instructions'}
extra = {'WAY-' + str(n).zfill(2) for n in [2,4,5,7,8,12,14,17,18,19,20,22,29,31,35,40,41,49,52,53,54,56,60,61,64,71,72,85,86,95,97,104]}
terms = r'guideline|styleguide|exemplar|screenshot|screen|appearance|visual|checklist|plan order|first file|first code|waiting for human|waits for task|plan change|WAY-212'
rows = []
search = []
for name in ['decisions.md', 'invariants.md', 'part_map.md', 'glossary.md', 'environment_facts.md']:
    source = (root / name).read_text(encoding='utf-8')
    pattern = r'^### (WAY-\d+/\d+) .*' if name == 'decisions.md' else r'^## (.+)'
    headings = list(re.finditer(pattern, source, re.M))
    for index, match in enumerate(headings):
        block = source[match.start():headings[index+1].start() if index+1 < len(headings) else len(source)]
        ident = match.group(1)
        line = source.count('\n', 0, match.start()) + 1
        hits = sorted(set(x.lower() for x in re.findall(terms, block, re.I)))
        if hits:
            search.append({'entry': ident, 'source': f'foundations/{name}:{line}', 'terms': hits})
        if name not in ['decisions.md', 'invariants.md']:
            continue
        if name == 'invariants.md' and not re.search(r'/\d+$', ident):
            continue
        field = 'Scope' if name == 'decisions.md' else 'Part'
        found = re.search(r'(?ms)^- \*\*' + field + r':\*\* (.*?)(?=^- \*\*|\n\n|\Z)', block)
        assert found, ident
        words = set(re.findall(r'[a-z]+(?:-[a-z]+)*', found.group(1)))
        scope_match = bool(parts & words or 'every' in words)
        method_match = name == 'invariants.md' and bool(re.search(r'^- \*\*Method:\*\* .*foundations/(decisions|part_map)\.md', block, re.M))
        linked = ident.split('/')[0] in extra or ident == 'decision-guard-stale-reference/1'
        rows.append({'entry': ident, 'source': f'foundations/{name}:{line}', 'field': found.group(1).replace('\n', ' '), 'scope_match': scope_match, 'method_match': method_match, 'linked': linked, 'selected': scope_match or method_match or linked})
(reports / 'foundation-source-inventory.json').write_text(json.dumps(rows, indent=2), encoding='utf-8')
(reports / 'foundation-search-inventory.json').write_text(json.dumps(search, indent=2), encoding='utf-8')
for name in ['decisions.md', 'invariants.md']:
    subset = [row for row in rows if f'/{name}:' in row['source']]
    print(name, 'population', len(subset), 'scope', sum(row['scope_match'] for row in subset), 'selected', sum(row['selected'] for row in subset))
    if name == 'invariants.md':
        print('Additional method entries:', ','.join(row['entry'].split('/')[0] for row in subset if row['method_match'] and not row['scope_match']))
print('search entries', len(search))
