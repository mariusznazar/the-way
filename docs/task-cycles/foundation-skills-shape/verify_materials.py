from pathlib import Path
import subprocess,re,json,html
RUN=Path('.runs/task-cycles/foundation-skills-shape'); BASE='745a6e53ec5c8eab3e078a32a61aa6a583a61a93'
rows=json.loads((RUN/'assessment_rows.json').read_text(encoding='utf-8')); moves=json.loads((RUN/'relocations.json').read_text(encoding='utf-8'))
def norm(s): return ' '.join(s.split())
old={p:subprocess.check_output(['git','show',BASE+':'+p]).decode('utf-8') for p in {r['path'] for r in rows}}
report=(RUN/'reports/assessment.md').read_text(encoding='utf-8')
for p,source in old.items():
    lines=source.splitlines(); covered=[]
    for r in [r for r in rows if r['path']==p]:
        assert r['quote']=='\n'.join(lines[r['start']-1:r['end']]), (p,r['start'],'source quote mismatch')
        escaped=html.escape(r['quote'],quote=False).replace('|','&#124;').replace('\n','<br>')
        assert '<code>'+escaped+'</code>' in report
        covered.extend(range(r['start'],r['end']+1))
    assert len(covered)==len(set(covered)), (p,'overlap')
    assert set(i for i,line in enumerate(lines,1) if line.strip()) <= set(covered), (p,'gap')
for r in moves:
    expected=r['quote']; target=Path(r['target'])
    if r['target'].endswith('decisions/skill/projected.md'):
        expected=expected.replace('`way_of_working.md` gives it for projected mode','`elements/common/projected_mode.md` gives it')
    if r['target'].endswith('environment-facts/skill/projected.md'):
        expected=expected.replace('runs as above','runs as step 4 of this skill gives it')
    if r['target'].endswith('part-map/skill/first_map.md'):
        expected=expected.replace('by the steps above','by the steps of this skill')
    if r['target'].endswith('common/projected_mode.md'):
        expected=expected.replace('The steps above run with these','The steps of `way_of_working.md` run with these').replace('by "Reading the foundation";', 'by "Reading the foundation" in `way_of_working.md`;')
    if r['target'].endswith('critique/settle.md'):
        boundary='The critic does not write files; the workflow that\ncalled this skill makes accepted changes.'
        assert norm(boundary) in norm(Path('elements/common/critique/SKILL.md').read_text(encoding='utf-8'))
        expected=expected.replace(' '+boundary,'')
    assert norm(expected) in norm(target.read_text(encoding='utf-8')), (r['target'],r['start'],'moved text missing')
    assert Path(r['path']).exists()
# Every unchanged source fragment remains readable, allowing only the explicit projected pointer replacement.
for r in rows:
    if any(m['path']==r['path'] and m['start']==r['start'] for m in moves): continue
    expected=r['quote'].replace('Projected mode runs as `elements/common/way_of_working.md` gives it,','In projected mode, read `elements/common/projected_mode.md`,')
    assert norm(expected) in norm(Path(r['path']).read_text(encoding='utf-8')), (r['path'],r['start'],'retained text missing')
for target in {m['target'] for m in moves}:
    p=Path(target)
    owner=p.parent/'SKILL.md' if p.parent.name in {'skill','critique'} else p.parent/'way_of_working.md'
    assert p.name in owner.read_text(encoding='utf-8'), (target,'not reachable from owner')
# External named sections are unchanged, including all existing anchors.
common='elements/common/way_of_working.md'; current=Path(common).read_text(encoding='utf-8')
for section in ['How a skill asks','Reading the foundation','Critique before collective review']:
    pattern=r'^## '+re.escape(section)+r'\n.*?(?=^## |\Z)'
    assert re.search(pattern,old[common],re.M|re.S).group(0)==re.search(pattern,current,re.M|re.S).group(0)
assert 'For a project definition, also read `elements/common/projected_mode.md`' in Path('elements/common/skill/SKILL.md').read_text(encoding='utf-8')
changed=subprocess.check_output(['git','diff','--name-only',BASE]).decode().splitlines()
assert not any(p.endswith('.py') for p in changed)
assert not any('/template.md' in p or p=='elements/common/rules.md' for p in changed)
routes=json.loads((RUN/'routes.json').read_text(encoding='utf-8'))
counts=(RUN/'reports/word-counts.md').read_text(encoding='utf-8')
totals={m[0]:tuple(map(int,m[1:])) for m in re.findall(r'^\| ([^|]+? / [^|]+?) \| (\d+) \| (\d+) \| ([+-]\d+) \|$',counts,re.M)}
missing='elements/common/missing_element_file.md'
missing_move=next(m for m in moves if m['target']==missing)
assert missing_move['quote'] in Path(missing).read_text(encoding='utf-8')
assert missing_move['pointer'] in current
assert missing_move['quote'] not in current
missing_row=next(r for r in rows if r['path']==common and r['start']==47)
assert missing_row['end']==56 and 'never in projected mode' in missing_row['need']
assert Path('elements/common/projected_mode.md').read_bytes()==subprocess.check_output(['git','show','78e47ee:elements/common/projected_mode.md'])
for name,before,after in routes:
    assert len(after)==len(set(after)),name
    for p in after: assert Path(p).exists(),(name,p)
    assert (missing in after)==('first element file' in name or 'first map' in name),name
    before_count=sum(len(old[p].split()) for p in set(before))
    after_count=sum(len(Path(p).read_text(encoding='utf-8').split()) for p in after)
    assert totals[name]==(before_count,after_count,after_count-before_count),name
    inventory=re.search(r'^- \*\*'+re.escape(name)+r'\*\*: (.*)$',counts,re.M).group(1)
    assert re.findall(r'`([^`]+)`',inventory)==after,name
assert len(totals)==len(routes)
print(f'PASS: {len(rows)} literal quote rows; complete nonblank source coverage; relocated and retained text; {len(set(m["target"] for m in moves))} companion pointers; 3 unchanged external sections; {len(routes)} route inventories and rendered totals; missing-file trigger and projected exclusion; no tracked Python/template/rules change')
