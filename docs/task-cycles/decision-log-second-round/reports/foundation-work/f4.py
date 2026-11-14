import json
import re

p = 'foundations/decisions.md'
text = open(p, encoding='utf-8', newline='').read()
lines = text.split('\n')

places = json.load(open('.runs/foundation/f4_places.json'))
HELD = {'WAY-93', 'WAY-94', 'WAY-97', 'WAY-297', 'WAY-363', 'WAY-364'}
d_rows = {
    'WAY-292': ('its rule, that the collapsed block of the description of a request of an English task holds `none`, is a paragraph of WAY-288', 'WAY-288'),
    'WAY-317': ('its rule, what a cycle does where the foundation settles no place for screenshots, is a paragraph of WAY-316', 'WAY-316'),
    'WAY-323': ('its rule, what the script of WAY-309 takes for an absolute path and for a note link, is a paragraph of WAY-309', 'WAY-309'),
    'WAY-347': ('its rule, that the measures of context and cache use are counted by a script and into a file of their own, is a paragraph of WAY-339', 'WAY-339'),
    'WAY-358': ('its rule, what causes the line of a correction gives, is a part of the question that WAY-357 answered, and both stand in `task-cycle/record_template.md`', 'WAY-357'),
    'WAY-369': ('its rule, that the agent types of a task cycle start with the instruction files, is a paragraph of WAY-368', 'WAY-368'),
}

# index entries
heads = {}
for i, l in enumerate(lines):
    m = re.match(r'### (WAY-\d+) — (.*)$', l)
    if m:
        heads[m.group(1)] = (i, m.group(2))
wd_start = [i for i, l in enumerate(lines) if l == '## Withdrawn identifiers'][0]

remove = [k for k in places if k not in HELD] + list(d_rows)
assert len(remove) == 131 + 6, len(remove)
new_rows = {}
for k in places:
    if k in HELD:
        continue
    q = heads[k][1]
    assert '|' not in q, k
    new_rows[k] = 'its rule, the answer to "%s", stands in `%s`' % (q, places[k])
for k, (why, succ) in d_rows.items():
    new_rows[k] = (why, succ)

# remove spans (from the bottom up)
spans = []
for k in remove:
    s = heads[k][0]
    j = s + 1
    while not lines[j].startswith('### ') and not lines[j].startswith('## '):
        j += 1
    spans.append((s, j))
spans.sort(reverse=True)
for s, j in spans:
    del lines[s:j]

# rewrite the table
wd = [i for i, l in enumerate(lines) if l == '## Withdrawn identifiers'][0]
hdr = [i for i in range(wd, len(lines)) if lines[i].startswith('|---')][0]
rows = []
k = hdr + 1
while k < len(lines) and lines[k].startswith('| WAY-'):
    rows.append(lines[k])
    k += 1
tail = lines[k:]
existing = {}
for r in rows:
    num = re.match(r'\| (WAY-\d+) \|', r).group(1)
    existing[num] = r
for num, v in new_rows.items():
    assert num not in existing, num
    if isinstance(v, tuple):
        existing[num] = '| %s | %s | %s |' % (num, v[0], v[1])
    else:
        existing[num] = '| %s | %s | none |' % (num, v)
ordered = [existing[n] for n in sorted(existing, key=lambda n: int(n[4:]))]
lines[hdr + 1:k] = ordered
open(p, 'w', encoding='utf-8', newline='').write('\n'.join(lines))
print(len(rows), len(ordered), len(spans))
