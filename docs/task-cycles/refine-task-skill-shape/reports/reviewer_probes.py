"""Read-only review probes; no tracked file is changed."""
from pathlib import Path
import ast
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / 'project-level'))
sys.path.insert(0, str(ROOT / 'installation'))
import test_plan_check as fixtures
import readiness_check
import plan_check
import install
import test_install

valid = fixtures.definition()
assert not readiness_check.check(valid)
assert not plan_check.check(fixtures.PLAN, valid)
broken = '\n'.join(line for line in valid.splitlines() if not line.startswith('- Approved by:'))
plan_findings = plan_check.check(fixtures.PLAN, broken)
readiness_findings = readiness_check.check(broken)
assert not plan_findings
assert readiness_findings
print('CONTROL valid definition: both checks return no findings')
print('MISSING APPROVER: plan findings =', len(plan_findings), '; readiness findings =', len(readiness_findings))

tested_names = {name for _, name in test_install.NAMES}
missing = sorted(set(install.SKILLS) - tested_names)
print('INSTALLER SKILLS:', len(install.SKILLS), '; assertion loop:', len(tested_names))
print('NOT CHECKED BY CHANGED TEST:', ', '.join(missing))
assert missing == ['lead-project', 'maintain-styleguide', 'maintain-testing-guidelines']

commit = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
path = install.SKILLS['refine-task']
text = install.skill_wrapper(path, 'refine-task', commit)
sentence = f'Read `.the-way/{path}` in full and follow it, and read a file it names inside `.the-way` when the step or variant that names it comes, not all of them at the start.'
assert sentence in text
assert 'Read the files it references' not in text
tree = ast.parse((ROOT / 'installation/test_install.py').read_text(encoding='utf-8'))
checks = [node for node in ast.walk(tree) if isinstance(node, ast.Expr) and node.lineno in (97, 98, 100)]
assert len(checks) == 3
assertions = compile(ast.fix_missing_locations(ast.Module(body=checks, type_ignores=[])), '<unchanged-and-new-test-assertions>', 'exec')
exec(assertions, {'self': unittest.TestCase(), 'path': path, 'text': text})
mutant = text.replace(f'Read `.the-way/{path}` in full and follow it, ', f'Read `.the-way/{path}` partially, ')
assert sentence not in mutant
exec(assertions, {'self': unittest.TestCase(), 'path': path, 'text': mutant})
print('FULL-SKILL INSTRUCTION REMOVED: current path/wording assertions still pass')

old = text.replace(sentence, f'Read `.the-way/{path}` in full and follow it. Read the files it references inside `.the-way`.')
try:
    exec(assertions, {'self': unittest.TestCase(), 'path': path, 'text': old})
except AssertionError:
    print('CONTROL old wording: assertions reject it')
else:
    raise AssertionError('old wording unexpectedly passed')
