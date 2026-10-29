from pathlib import Path
import json
import subprocess

root = Path.cwd()
run = root / '.runs/task-cycles/foundation-skills-shape'
base = '745a6e53ec5c8eab3e078a32a61aa6a583a61a93'
source_path = 'elements/common/way_of_working.md'
lines = subprocess.check_output(['git', 'show', f'{base}:{source_path}']).decode('utf-8').splitlines()
target = 'elements/common/missing_element_file.md'
records = json.loads((run / 'relocations.json').read_text(encoding='utf-8'))
records = [record for record in records if record['target'] != target]
records.append(dict(
    path=source_path, start=47, end=56, target=target,
    pointer="- Outside projected mode, where the product has no file of the element's entries, read\n  `missing_element_file.md` beside this file before continuing.",
    reason='Only a missing element file outside projected mode needs the start-file choice, stop on refusal, map assignment and map-first ordering. These are several actions, not the one-instruction exception (WAY-256; task To do 2). The existing TODOs and first-map route remain unchanged.',
    need='At step 1, only when writing to the foundation and the product has no file of this element; never in projected mode',
    recognise='Yes: the step-1 pointer names both the missing-file condition and the projected-mode exclusion; the shared projected override remains unchanged',
    quote='\n'.join(lines[46:56]),
))
(run / 'relocations.json').write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding='utf-8')

path = run / 'report_materials.py'
with path.open(encoding='utf-8', newline='') as handle:
    text = handle.read()
text = text.replace('The first-map heading stays in update-part-map, so the common missing-map instruction still reaches the variant.', 'The missing-element-file procedure is read at step 1 only outside projected mode and only when that file is absent. It keeps the start-file choice, stop, map assignment and ordering unchanged. The first-map heading stays in update-part-map, so the extracted common missing-map instruction still reaches the variant.')
text = text.replace('- first_map.md is read only', '- Foundation-entry rows assume the element file already exists. first element file rows add common/missing_element_file.md; projected routes never read it. Its before cost was already included in the whole shared file. A first-file route that also needs a part map dispatches update-part-map first; add the first-map route with shared files counted once, as for other following entries.\\n- first_map.md is read only')
text = text.replace('2173 words before or 1782 after', "2173 words before or {count(common)} after")
text = text.replace("wc.append('''\\n## Conditional reading", "wc.append(f'''\\n## Conditional reading")
with path.open('w', encoding='utf-8', newline='') as handle:
    handle.write(text)
print('Updated missing-file relocation and route-report explanations')
