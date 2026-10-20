from pathlib import Path
import json
import re
import subprocess

reports = Path('.runs/task-cycles/s7-cycle-remarks/reports')
base = 'f0b5eb131de5d681ee3fcdeb264e9f88778af2ec'
for element in ('decisions', 'invariants'):
    command = ['python', '-B', 'elements/' + element + '/format_guard.py', '--base', 'none', '--merge-onto', base]
    result = subprocess.run(command, capture_output=True)
    (reports / ('relations-' + element + '.txt')).write_text('Command: ' + ' '.join(command) + '\nExit: ' + str(result.returncode) + '\n\nSTDOUT:\n' + result.stdout.decode('utf-8', errors='replace') + '\nSTDERR:\n' + result.stderr.decode('utf-8', errors='replace'), encoding='utf-8')
    print(element + ': exit ' + str(result.returncode))

selection_path = reports / 'foundation-selection.json'
data = json.loads(selection_path.read_text(encoding='utf-8'))
for key, filename, prefix in [('decisions', 'foundations/decisions.md', '###'), ('invariants', 'foundations/invariants.md', '##')]:
    content = subprocess.run(['git', 'show', base + ':' + filename], capture_output=True, check=True).stdout.decode('utf-8')
    headers = list(re.finditer('^' + prefix + r' ([^\n]+)', content, re.M))
    data[key + '_whole_read_locations'] = [{'heading': match.group(1), 'source': filename, 'first_line': content[:match.start()].count('\n') + 1, 'last_line': content[:headers[index + 1].start()].count('\n') if index + 1 < len(headers) else len(content.splitlines())} for index, match in enumerate(headers)]
selection_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print('whole decision entries: ' + str(len(data['decisions_selected_and_read'])))
print('whole invariant sections: ' + str(len(data['invariants_selected_and_read'])))
