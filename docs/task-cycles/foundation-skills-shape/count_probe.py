from pathlib import Path
import subprocess
for path in ['elements/decisions/skill/SKILL.md','elements/invariants/skill/SKILL.md','elements/glossary/skill/SKILL.md','elements/environment-facts/skill/SKILL.md','elements/part-map/skill/SKILL.md','elements/common/critique/SKILL.md','elements/common/way_of_working.md']:
    before=subprocess.check_output(['git','show','745a6e5:'+path]).decode('utf-8')
    print(path,len(before.split()),len(Path(path).read_text(encoding='utf-8').split()))
