from pathlib import Path
import json
import re
import subprocess
import sys

sys.path.insert(0, 'relation-model')
from fingerprint import fingerprint

reports = Path('.runs/task-cycles/product-guidelines-cycle/reports')
inventory = json.loads((reports / 'foundation-source-inventory.json').read_text())
selected = {row['entry'] for row in inventory if row['selected']}
source = Path('foundations/decisions.md').read_text(encoding='utf-8')
headers = list(re.finditer(r'^### (WAY-\d+/\d+) .*', source, re.M))
blocks = {m[1]: source[m.end():headers[i+1].start() if i+1 < len(headers) else len(source)] for i, m in enumerate(headers)}
terms = r'Applies to|When to read|refin|readiness|waiting|blocked|depends|preparatory|review|finding|Minor|Important|states|running product|WAY-212|WAY-139|WAY-164|WAY-161'
unread = [key for key, block in blocks.items() if re.search(terms, block, re.I) and key not in selected and int(key.split('/')[0][4:]) < 213]
print('Additional search hits requiring whole reading:', ','.join(unread))
for key in ['WAY-212/1'] + [f'WAY-{n}/1' for n in range(213, 223)]:
    binding = blocks[key].split('- **Change:**')[0]
    print(key, 'binding fingerprint', fingerprint(binding))
for key, block in blocks.items():
    if int(key.split('/')[0][4:]) < 213:
        continue
    relation = re.search(r'(?ms)^- \*\*Relations:\*\* (.*?)(?=^- \*\*)', block)[1]
    for ident, carried in re.findall(r'(WAY-\d+)@([a-f0-9]+)', relation):
        actual = fingerprint(blocks[ident + '/1'].split('- **Change:**')[0])
        assert actual == carried, (key, ident, actual, carried)
print('New decision relation fingerprints match their current targets.')
base = subprocess.run(['git', 'show', 'f98ac2fed3ab6ecbc1701e0c5f9a694dc9d91624:foundations/decisions.md'], capture_output=True, check=True).stdout.decode('utf-8')
base_headers = list(re.finditer(r'^### (WAY-\d+/\d+) .*', base, re.M))
for i, m in enumerate(base_headers):
    old = base[m.end():base_headers[i+1].start() if i+1 < len(base_headers) else len(base)]
    assert fingerprint(old.split('- **Change:**')[0]) == fingerprint(blocks[m[1]].split('- **Change:**')[0]), m[1]
print('All 198 existing decision binding fingerprints remain unchanged.')
