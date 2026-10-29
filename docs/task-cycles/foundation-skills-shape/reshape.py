from pathlib import Path
import subprocess, re, json, html
ROOT=Path.cwd()
RUN=ROOT/'.runs/task-cycles/foundation-skills-shape'
BASE='745a6e53ec5c8eab3e078a32a61aa6a583a61a93'
paths=[f'elements/{p}/skill/SKILL.md' for p in ['decisions','invariants','glossary','environment-facts','part-map']]+['elements/common/critique/SKILL.md','elements/common/way_of_working.md']
original={p:subprocess.check_output(['git','show',f'{BASE}:{p}']).decode('utf-8') for p in paths}
texts=dict(original)
rows=[]
newfiles={}
def cut(path,start,end,target,pointer,reason):
    lines=original[path].splitlines(keepends=True)
    fragment=''.join(lines[start-1:end]).rstrip('\n')
    assert fragment in texts[path], (path,start,end)
    texts[path]=texts[path].replace(fragment,pointer,1)
    if target:
        newfiles.setdefault(target,[]).append(fragment)
    rows.append(dict(path=path,start=start,end=end,target=target,pointer=pointer,reason=reason,quote=fragment))
for part,begin,end in [('decisions',30,40),('invariants',28,46),('glossary',28,42),('environment-facts',29,45),('part-map',27,38)]:
    cut(f'elements/{part}/skill/SKILL.md',begin,end,f'elements/{part}/skill/decide_entry.md',
        'At step 2, read `decide_entry.md` beside this skill to decide what the entry is and what\nthe search of the foundation adds for this element.', 'Several instructions for deciding and searching at step 2; WAY-256. Template references keep entry rules at their source (WAY-35).')
for part,begin,end in [('decisions',22,26),('glossary',22,24),('environment-facts',22,25)]:
    cut(f'elements/{part}/skill/SKILL.md',begin,end,f'elements/{part}/skill/read.md',
        'At step 1, read `read.md` beside this skill for the reading this entry needs.', 'Several reading or initialisation actions at step 1; WAY-256.')
for part,begin,end in [('invariants',70,76),('glossary',55,64),('environment-facts',58,67),('part-map',62,66)]:
    cut(f'elements/{part}/skill/SKILL.md',begin,end,f'elements/{part}/skill/write.md',
        'At step 4, read `write.md` beside this skill for what to check, show and write, and what\nfollows from the entry.', 'Several actions at step 4 and its handoff; WAY-256. Rules stay referred to their template.')
# Drafting operations whose entry rules remain in the template; leave form-bearing paragraphs unchanged.
cut('elements/invariants/skill/SKILL.md',53,58,'elements/invariants/skill/draft.md',
    '- At step 3, read `draft.md` beside this skill to check the parts and the facts the invariant\n  rests on.', 'Two drafting actions: justify each part and apply the template test to facts; WAY-256.')
cut('elements/environment-facts/skill/SKILL.md',49,54,'elements/environment-facts/skill/draft.md',
    'At step 3, read `draft.md` beside this skill to obtain and check the source material.', 'Source retrieval, host reading and archive selection are distinct drafting actions; WAY-256.')
# Projected procedural guidance; entry forms remain unchanged in SKILL.md, outside authorised template edits.
cut('elements/decisions/skill/SKILL.md',67,68,'elements/decisions/skill/projected.md',
    'In projected mode, read `projected.md` beside this skill for the plan test and\nwhat follows from the decision.', 'Prefix handling and the plan-test workflow are steps of projected writing; WAY-117, WAY-256.')
cut('elements/decisions/skill/SKILL.md',71,75,'elements/decisions/skill/projected.md','',
    'Technology handover follows the template and sends the following invariant through the projected workflow; WAY-117, WAY-256.')
cut('elements/glossary/skill/SKILL.md',71,73,'elements/glossary/skill/projected.md',
    'In projected mode, read `projected.md` beside this skill for choosing the words and\nrewriting their uses.', 'Choose candidate words and rewrite uses within the definition, projected workflow; WAY-117, WAY-256.')
cut('elements/glossary/skill/SKILL.md',75,75,'elements/glossary/skill/projected.md','',
    'Same projected workflow file as candidate selection; the two actions share the mode trigger.')
cut('elements/environment-facts/skill/SKILL.md',76,77,'elements/environment-facts/skill/projected.md',
    '- In projected mode, read `projected.md` beside this skill for reading the source and\n  checking the proposal.', 'Reading the source and mechanical check are two actions of projected writing; WAY-117, WAY-256.')
cut('elements/part-map/skill/SKILL.md',82,86,'elements/part-map/skill/first_map.md',
    'When writing the first map of a product, read `first_map.md` beside this skill.',
    'The first-map variant has a first-entry write, no recursive invocation and repetition to complete coverage; WAY-28, WAY-256.')
cut('elements/common/way_of_working.md',156,185,'elements/common/projected_mode.md',
    'When writing an entry projected into a project definition, read `projected_mode.md` beside\nthis file for the differences from the steps above (WAY-117).',
    'Only projected writing needs these changes to the shared steps; WAY-117, WAY-256.')
# Keep common entry-form rules out of element companion files by relying on their template sources.
for p in paths[:5]:
    texts[p]=texts[p].replace('Projected mode runs as `elements/common/way_of_working.md` gives it,',
        'In projected mode, read `elements/common/projected_mode.md`,')
# Critique: role-specific handoff and settlement, checks shared by both roles.
cut('elements/common/critique/SKILL.md',23,25,'elements/common/critique/prepare.md',
    'When invoking a critique, read `prepare.md` beside this skill to start a fresh critic and\nhandle the case where none is available.', 'Only the invoking author prepares an independent critic; WAY-120, WAY-256.')
cut('elements/common/critique/SKILL.md',29,34,'elements/common/critique/prepare.md',
    'When giving the critic its material, follow `prepare.md` beside this skill.', 'Handoff actions are performed by the invoking author; WAY-120, WAY-256.')
cut('elements/common/critique/SKILL.md',38,61,'elements/common/critique/check.md',
    'At the independent check, the author and the critic each read `check.md` beside this skill.',
    'Both roles use these checks at the independent-check step; WAY-120, WAY-256.')
cut('elements/common/critique/SKILL.md',65,70,'elements/common/critique/settle.md',
    'When settling the review, the author reads `settle.md` beside this skill.',
    'Only the author verifies observations and settles the verdict; WAY-120, WAY-256.')
# Non-writing is a role boundary the critic must see too.
texts['elements/common/critique/SKILL.md']=texts['elements/common/critique/SKILL.md'].replace('This skill advises; it does not approve a proposal or change a human settlement.',
    'This skill advises; it does not approve a proposal or change a human settlement.\nThe critic does not write files; the workflow that called this skill makes accepted changes.')
for target,fragments in newfiles.items():
    title=Path(target).stem.replace('_',' ').capitalize()
    body='\n\n'.join(fragments)
    if target.endswith('critique/settle.md'):
        body=body.replace(' The critic does not write files; the workflow that\ncalled this skill makes accepted changes.','')
    if target.endswith('decisions/skill/projected.md'):
        body=body.replace('`way_of_working.md` gives it for projected mode','`elements/common/projected_mode.md` gives it')
    if target.endswith('part-map/skill/first_map.md'):
        body=body.replace('by the steps above', 'by the steps of this skill')
    if target.endswith('environment-facts/skill/projected.md'):
        body=body.replace('runs as above','runs as step 4 of this skill gives it')
    if target.endswith('common/projected_mode.md'):
        body=body.replace('The steps above run with these','The steps of `way_of_working.md` run with these').replace('by "Reading the foundation";', 'by "Reading the foundation" in `way_of_working.md`;')
    Path(target).write_text('# '+title+'\n\n'+body.rstrip()+'\n',encoding='utf-8',newline='\n')
for path,text in texts.items():
    # Existing files preserve their checkout newline convention.
    old=Path(path).read_bytes()
    newline='\r\n' if b'\r\n' in old else '\n'
    Path(path).write_bytes((text.rstrip()+'\n').replace('\n',newline).encode('utf-8'))
RUN.joinpath('relocations.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
print('wrote',len(texts),'existing and',len(newfiles),'companion files')
