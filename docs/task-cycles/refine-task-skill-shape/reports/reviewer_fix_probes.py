"""Read-only probes for the reviewed fix; tracked files remain unchanged."""
from pathlib import Path
import ast
import re
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / 'installation'))
import install
import test_install

assert len(install.SKILLS) == len(test_install.NAMES) == 20
assert dict(test_install.NAMES) == {path: name for name, path in install.SKILLS.items()}
tree = ast.parse((ROOT / 'installation/test_install.py').read_text(encoding='utf-8'))
checks = [node for node in ast.walk(tree) if isinstance(node, (ast.Expr, ast.Assign)) and node.lineno in (81, 84, 85)]
assert len(checks) == 3
compiled = compile(ast.fix_missing_locations(ast.Module(body=checks, type_ignores=[])), '<current-assertions>', 'exec')
commit = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
rejected = 0
for path, name in test_install.NAMES:
    text = install.skill_wrapper(path, name, commit)
    scope = {'self': unittest.TestCase(), 'path': path, 'text': text}
    exec(compiled, scope)
    mutants = [text.replace('in full and follow it,', 'partially,'),
               text + '\nRead the files it references inside `.the-way`.']
    for mutant in mutants:
        try:
            exec(compiled, {'self': unittest.TestCase(), 'path': path, 'text': mutant})
        except AssertionError:
            rejected += 1
        else:
            raise AssertionError(f'Broken instruction passed for {name}')
assert rejected == 40
print('20 generated skills pass; 40 partial-read/old-wording mutations rejected')

skill = ROOT / 'project-level/task/skill'
common = ['SKILL.md', 'read_sources.md', 'draft.md', 'resolve_gaps.md', 'carry_foundation.md', 'find_settlements.md', 'final_review.md']
extras = ['project_plan_task.md', 'source_only_task.md', 'orchestrated_mode.md', 'guideline_findings.md']
assert {p.name for p in skill.glob('*.md')} == set(common + extras)
counts = {name: len((skill / name).read_text(encoding='utf-8').split()) for name in common + extras}
base = sum(counts[name] for name in common)
assert base == 2007
assert base + counts['project_plan_task.md'] == 2212
assert base + counts['project_plan_task.md'] + counts['orchestrated_mode.md'] == 2782
assert base + counts['source_only_task.md'] == 2172
assert counts['guideline_findings.md'] == 453
assert len((ROOT / 'project-level/task/template.md').read_text(encoding='utf-8').split()) == 1580
for target in re.findall(r'\]\(([^)]+\.md)\)', (skill / 'SKILL.md').read_text(encoding='utf-8')):
    assert (skill / target).is_file(), target
print('All 11 skill files accounted for; counts 2007 / 2212 / 2782; conditional +453; template 1580')
