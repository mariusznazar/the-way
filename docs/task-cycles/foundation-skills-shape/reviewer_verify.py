from pathlib import Path
import re,subprocess,html
root=Path.cwd()
run=root/'.runs/task-cycles/foundation-skills-shape'
base='745a6e53ec5c8eab3e078a32a61aa6a583a61a93'
report=(run/'reports/assessment.md').read_text(encoding='utf-8')
pattern=r'\| \[(elements/[^\]]+?):(\d+)-(\d+)\]\(([^)]+)\): <code>(.*?)</code> \|'
rows=re.findall(pattern,report)
assert len(rows)==125,len(rows)
coverage={}
for path,start,end,url,quoted in rows:
 start,end=int(start),int(end)
 source=subprocess.check_output(['git','show',f'{base}:{path}']).decode('utf-8').splitlines()
 assert html.unescape(quoted.replace('<br>','\n'))=='\n'.join(source[start-1:end]),(path,start)
 assert f'/blob/{base}/{path}#L{start}-L{end}' in url
 coverage.setdefault(path,[]).extend(range(start,end+1))
for path,covered in coverage.items():
 source=subprocess.check_output(['git','show',f'{base}:{path}']).decode('utf-8').splitlines()
 assert len(set(covered))==len(covered)
 assert {i for i,line in enumerate(source,1) if line.strip()} <= set(covered)
assert len(coverage)==7
print('PASS: 125 literal quotes, anchors and nonblank source coverage across seven files')
counts=(run/'reports/word-counts.md').read_text(encoding='utf-8')
totals={m[0]:tuple(map(int,m[1:])) for m in re.findall(r'^\| ([^|]+? / [^|]+?) \| (\d+) \| (\d+) \| ([+-]\d+) \|$',counts,re.M)}
for route,files in re.findall(r'^- \*\*([^*]+)\*\*: (.*)$',counts,re.M):
 files=re.findall(r'`([^`]+)`',files)
 assert len(files)==len(set(files)),route
 after=sum(len((root/f).read_text(encoding='utf-8').split()) for f in files)
 kind=route.split(' / ')[0]
 before_files=['elements/common/critique/SKILL.md'] if kind=='critique' else [f'elements/{kind}/skill/SKILL.md','elements/common/way_of_working.md']
 before=sum(len(subprocess.check_output(['git','show',f'{base}:{f}']).decode('utf-8').split()) for f in before_files)
 assert totals[route]==(before,after,after-before),(route,totals[route],before,after)
assert len(totals)==14
for kind,template_count,rules_count,addition in re.findall(r'^\| ([a-z-]+): `elements/[^`]+/template.md` \| (\d+) \| (\d+) \| (\d+) \|$',counts,re.M):
 tc=len((root/f'elements/{kind}/template.md').read_text(encoding='utf-8').split())
 rc=len((root/'elements/common/rules.md').read_text(encoding='utf-8').split())
 assert (tc,rc,tc+rc)==tuple(map(int,(template_count,rules_count,addition)))
print('PASS: 14 route inventories/counts and five fixed template/rules additions')
old=subprocess.check_output(['git','show',f'{base}:elements/common/way_of_working.md']).decode('utf-8')
new=(root/'elements/common/way_of_working.md').read_text(encoding='utf-8')
for heading in ['Critique before collective review','How a skill asks','Reading the foundation']:
 rx=r'(?ms)^## '+re.escape(heading)+r'\n.*?(?=^## |\Z)'
 assert re.search(rx,old).group()==re.search(rx,new).group()
print('PASS: three external named sections unchanged')
changed=subprocess.check_output(['git','diff','--name-only',base+'..HEAD']).decode().splitlines()
assert len(changed)==30
assert all(p.endswith('.md') and not p.endswith('template.md') and p!='elements/common/rules.md' and not p.startswith('foundations/') for p in changed)
print('PASS: 30 Markdown changes, no Python, template, common-rules, foundation entry or invariant test changes')
