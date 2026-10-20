from pathlib import Path
import json
import os
import subprocess
import tomllib

reports = Path('.runs/task-cycles/s7-cycle-remarks/reports')
command = ['python', '-B', 'instruction-files/check_instructions.py', '.']
result = subprocess.run(command, capture_output=True)
output = 'Command: ' + ' '.join(command) + '\nExit: ' + str(result.returncode) + '\n\nSTDOUT:\n' + result.stdout.decode('utf-8', errors='replace') + '\nSTDERR:\n' + result.stderr.decode('utf-8', errors='replace')
(reports / 'instructions-before.txt').write_text(output, encoding='utf-8')
print('instructions-before exit ' + str(result.returncode))
for name in ['C:/Users/Mariusz/.claude/settings.json', '.claude/settings.json', '.claude/settings.local.json']:
    path = Path(name)
    if not path.exists():
        print(name + ': absent')
        continue
    data = json.loads(path.read_text(encoding='utf-8-sig'))
    print(name + ': claudeMdExcludes=' + json.dumps(data.get('claudeMdExcludes', '(absent)')))
    value = data.get('pluginConfigs', {}).get('cc-plugin-agents-md@builtin', {}).get('instructionFiles', '(absent)')
    print(name + ': instructionFiles=' + json.dumps(value))
codex_home = Path(os.environ.get('CODEX_HOME', 'C:/Users/Mariusz/.codex'))
for path in [codex_home / 'config.toml', Path('.codex/config.toml')]:
    if not path.exists():
        print(str(path) + ': absent')
        continue
    data = tomllib.loads(path.read_text(encoding='utf-8-sig'))
    for key in ['project_doc_max_bytes', 'project_doc_fallback_filenames']:
        print(str(path) + ': ' + key + '=' + json.dumps(data.get(key, '(absent)')))
print('CODEX_HOME=' + str(codex_home))
