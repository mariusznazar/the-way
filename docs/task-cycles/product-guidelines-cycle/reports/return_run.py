from pathlib import Path
import json
import subprocess
import sys

directory = Path('.runs/task-cycles/product-guidelines-cycle/reports')
label, *command = sys.argv[1:]
result = subprocess.run(command, capture_output=True)
stdout = directory / f'return-{label}.stdout.txt'
stderr = directory / f'return-{label}.stderr.txt'
stdout.write_bytes(result.stdout)
stderr.write_bytes(result.stderr)
record = {'command': command, 'exit_code': result.returncode,
          'stdout': str(stdout).replace('\\', '/'), 'stderr': str(stderr).replace('\\', '/')}
with (directory / 'return-checks.jsonl').open('a', encoding='utf-8', newline='') as stream:
    stream.write(json.dumps(record, ensure_ascii=True) + '\n')
print(label, result.returncode)
