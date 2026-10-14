from pathlib import Path
import json
import re
import subprocess

root = Path.cwd()
record = root / '.runs/task-cycles/selective-document-reading/reports'
base = subprocess.check_output(['git', 'rev-parse', 'origin/foundations'], text=True).strip()
head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip()
paths = [f'foundations/{name}.md' for name in
         ('decisions', 'invariants', 'environment_facts', 'part_map', 'glossary')]
patterns = {
    'topic': r'read|load|select|coverage|scope|candidate|whole|project plan|definition|pending.*(read|select|scope)',
    'wording': r'whole foundation|read.*full|read.*whole|selective|WAY-111|WAY-115|reading|pending.*(read|scope|select)',
    'incoming': r'WAY-(111|115|150|151)@',
}
rows = []
for revision in (base, head):
    for path in paths:
        source = subprocess.check_output(['git', 'show', f'{revision}:{path}'])
        for name, pattern in patterns.items():
            run = subprocess.run(['rg', '-n', '-i', pattern, '-'], input=source,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            assert run.returncode in (0, 1), run.stderr
            lines = [int(line.split(b':', 1)[0]) for line in run.stdout.splitlines()]
            rows.append({'revision': revision, 'path': path, 'pattern': name,
                         'matching_lines': lines})
data = {'target': base, 'task_head': head, 'patterns': patterns, 'searches': rows,
        'note': 'Whole-domain locators only. Matches locate candidates; semantic findings are in second-foundation-search.md.'}
(record / 'second-foundation-locators.json').write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')
changed = subprocess.check_output(['git', 'diff', '--name-only', f'{base}..{head}'], text=True).splitlines()
assert len(changed) == 14 and all(p.endswith('.md') for p in changed), changed
(record / 'assessment-source.diff').write_bytes(subprocess.check_output(['git', 'diff', f'{base}..{head}', '--', *changed]))
(record / 'assessment-files.json').write_text(json.dumps({'base': base, 'head': head, 'files': changed}, indent=2) + '\n', encoding='utf-8')
print('target', base, 'head', head, 'domain_files', len(paths), 'search_passes', len(rows))
print('source_only_files', len(changed), 'locator_count', sum(len(row['matching_lines']) for row in rows))
