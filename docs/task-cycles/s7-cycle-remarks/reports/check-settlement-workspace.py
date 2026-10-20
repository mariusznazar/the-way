"""Exercise the installed brief adapter in an isolated, retained scratch repository."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import tempfile

reports = Path('.runs/task-cycles/s7-cycle-remarks/reports').resolve()
scratch = Path(tempfile.mkdtemp(prefix='settlement-workspace-', dir=reports))
bash = 'C:/Program Files/Git/bin/bash.exe'
scripts = 'C:/Users/Mariusz/.claude/plugins/cache/claude-plugins-official/superpowers/6.4.1/skills/subagent-driven-development/scripts/'
commands = []


def run(args):
    result = subprocess.run(args, cwd=scratch, capture_output=True)
    stdout = result.stdout.decode('utf-8', errors='replace')
    stderr = result.stderr.decode('utf-8', errors='replace')
    commands.append({'command': args, 'cwd': str(scratch), 'exit': result.returncode,
                     'stdout': stdout, 'stderr': stderr})
    assert result.returncode == 0, commands[-1]
    return stdout.strip()


def native(path):
    match = re.match(r'^/([a-zA-Z])/(.*)$', path)
    return Path(match[1] + ':/' + match[2]) if match else Path(path)


def marker_target(marker):
    path = native(marker.decode().strip())
    return path.resolve() if path.is_absolute() else (scratch / path).resolve()


try:
    run(['git', 'init', '--quiet'])
    original = scratch / 'plans/original/plan.md'
    temporary = scratch / 'plans/temporary/plan.md'
    original.parent.mkdir(parents=True)
    temporary.parent.mkdir(parents=True)
    source = ('# Plan fixture\n\n### Slice 1: First\nKeep this exact requirement.\n'
              '```text\n### Task 88: Fenced example\n```\n\n'
              '### Slice 2: Second\nExclude the second slice.\n').encode('utf-8')
    original.write_bytes(source)
    original_relative = original.relative_to(scratch).as_posix()
    temporary_relative = temporary.relative_to(scratch).as_posix()
    workspace_text = run([bash, scripts + 'sdd-workspace', original_relative])
    workspace = native(workspace_text)
    marker_before = (workspace / 'plan-path').read_bytes()
    assert marker_target(marker_before) == original.resolve()
    ledger = workspace / 'progress.md'
    ledger_content = ('# SDD ledger - plan: ' + original_relative + '\nTask 1: fixture pending\n').encode()
    ledger.write_bytes(ledger_content)
    temporary.write_bytes(re.sub(rb'(?m)^### Slice ([0-9]+)', rb'### Task \1', source))

    # Expected negative control: successful extraction violates the workspace contract.
    run([bash, scripts + 'task-brief', temporary_relative, '1'])
    divergent_text = run([bash, scripts + 'sdd-workspace', temporary_relative])
    divergent = native(divergent_text)
    assert divergent.resolve() != workspace.resolve()
    assert marker_target((divergent / 'plan-path').read_bytes()) == temporary.resolve()
    assert (divergent / 'task-1-brief.md').is_file()
    assert not (workspace / 'task-1-brief.md').exists()
    print('NEGATIVE CONTROL: script exit 0; original-workspace contract FAIL (expected).')

    # Actual corrected instruction: original workspace resolved above, explicit third argument.
    out = workspace_text + '/task-1-brief.md'
    run([bash, scripts + 'task-brief', temporary_relative, '1', out])
    brief = workspace / 'task-1-brief.md'
    extracted = brief.read_text(encoding='utf-8')
    assert extracted.startswith('### Task 1: First\n')
    assert 'Keep this exact requirement.' in extracted
    assert '### Task 88: Fenced example' in extracted
    assert 'Exclude the second slice.' not in extracted
    # The borrowed method derives its report name beside the brief.
    report = brief.with_name('task-1-report.md')
    report.write_text('Fixture report beside the extracted brief.\n', encoding='utf-8')
    temporary.unlink()
    resolved_again = native(run([bash, scripts + 'sdd-workspace', original_relative]))
    assert resolved_again.resolve() == workspace.resolve()
    assert (workspace / 'plan-path').read_bytes() == marker_before
    assert ledger.read_bytes() == ledger_content
    assert report.parent == ledger.parent == brief.parent
    assert original.read_bytes() == source
    assert not temporary.exists()
    summary = {
        'scratch': str(scratch), 'original_plan': str(original),
        'original_plan_sha256': hashlib.sha256(source).hexdigest(),
        'original_workspace': str(workspace), 'divergent_workspace': str(divergent),
        'negative_control': 'FAIL (expected): two-argument temporary extraction leaves original workspace without brief',
        'corrected_route': 'PASS: explicit original-workspace output, original marker and ledger unchanged, brief/report colocated, original bytes unchanged, temporary copy removed',
        'report_fixture': str(report),
        'limit': 'Report naming is applied from the borrowed method; no real implementer or full cycle is dispatched.',
    }
    (reports / 'settlement-workspace-result.json').write_text(json.dumps(summary, indent=2) + '\n', encoding='utf-8')
    print('CORRECTED ROUTE: PASS; marker, ledger, plan and cleanup checked.')
finally:
    (reports / 'settlement-workspace-commands.json').write_text(json.dumps(commands, indent=2) + '\n', encoding='utf-8')
