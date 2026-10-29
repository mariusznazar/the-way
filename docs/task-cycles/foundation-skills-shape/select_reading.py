from pathlib import Path
import re
parts={'decisions','invariants','glossary','environment-facts','part-map','elements-common'}
extra={'125','127','150','256','257','259'}
text=Path('foundations/decisions.md').read_text(encoding='utf-8')
entries=re.split(r'(?=^### WAY-)',text,flags=re.M)[1:]
selected=[]
for entry in entries:
    scope=re.search(r'^- \*\*Scope:\*\* (.*(?:\n  [^\n]+)*)',entry,re.M)
    items=set(re.split(r',\s*',scope.group(1))) if scope else set()
    num=re.search(r'WAY-(\d+)',entry).group(1)
    if items & parts or num in extra:
        selected.append(entry)
for index in range(0,len(selected),25):
    Path(f'.runs/task-cycles/foundation-skills-shape/reports/reading-{index//25}.md').write_text(''.join(selected[index:index+25]),encoding='utf-8')
print('selected',len(selected))
