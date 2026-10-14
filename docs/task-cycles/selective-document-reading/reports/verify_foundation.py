from pathlib import Path
import importlib.util
import re
import sys

root = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(root / 'relation-model'))
from fingerprint import fingerprint
spec = importlib.util.spec_from_file_location('decision_guard_verification', root / 'elements/decisions/format_guard.py')
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)
text = (root / 'foundations/decisions.md').read_text(encoding='utf-8')
entries = module.parse_log(text, 'WAY')
current = {}
for entry in entries:
    if entry.kind == 'version':
        current[entry.number] = entry
errors = []
count = 0
for entry in current.values():
    relation = entry.fields.get('Relations', [''])[0]
    for number, carried in re.findall(r'WAY-(\d+)@([0-9a-f]{8})', relation):
        count += 1
        actual = fingerprint(current[int(number)].binding)
        if actual != carried:
            errors.append((entry.number, number, carried, actual))
assert not errors, errors
assert not re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', text)
print('relations_checked', count)
for number in (111, 115, 134, 150, 151):
    entry = current[number]
    print('WAY-' + str(number), fingerprint(entry.binding))
print('control_characters', 0)
