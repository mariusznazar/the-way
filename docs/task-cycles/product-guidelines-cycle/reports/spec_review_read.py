from pathlib import Path
import re
import sys

parts = {'product-guidelines', 'task-cycle', 'project-level', 'agent-instructions', 'instruction-files'}
name = sys.argv[1]
s = Path('foundations', name).read_text(encoding='utf-8')
pattern, field = (r'^### (WAY-\d+/\d+)', 'Scope') if name == 'decisions.md' else (r'^## ([^\n]+/\d+)', 'Part')
headers = list(re.finditer(pattern, s, re.M))
rows = []
for i, m in enumerate(headers):
    b = s[m.start():headers[i+1].start() if i+1 < len(headers) else len(s)]
    f = re.search(r'(?ms)^- \*\*' + field + r':\*\* (.*?)(?=^- \*\*|\n\n|\Z)', b)
    assert f, m.group(1)
    words = set(re.findall(r'[a-z]+(?:-[a-z]+)*', f.group(1)))
    if sys.argv[2] == 'ids':
        wanted = set(sys.argv[3].split(','))
        if m.group(1).split('/')[0] in wanted:
            print(b)
    if parts & words or 'every' in words:
        rows.append((m.group(1), s.count('\n', 0, m.start())+1, b))
if sys.argv[2] == 'ids':
    pass
elif sys.argv[2] == 'inventory':
    print('Population:', len(headers), 'Selected:', len(rows))
    for ident, line, _ in rows:
        print(f'{ident} foundations/{name}:{line}')
else:
    print('\n'.join(b for _, _, b in rows[int(sys.argv[2]):int(sys.argv[3])]))
