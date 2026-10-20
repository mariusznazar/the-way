"""Capture the repository's required checks without losing process exit codes."""

import json
import subprocess
import sys
from pathlib import Path


report_dir = Path(__file__).resolve().parent
repo = report_dir.parents[3]
target = sys.argv[1]
prefix = sys.argv[2] if len(sys.argv) > 2 else "final"
commands = [
    ("gate", ["python", "-B", "gate/run_tests.py", "gate"]),
    ("decisions", ["python", "-B", "gate/run_tests.py", "elements/decisions"]),
    ("invariants", ["python", "-B", "gate/run_tests.py", "elements/invariants"]),
    ("part-map", ["python", "-B", "gate/run_tests.py", "elements/part-map"]),
    ("elements-common", ["python", "-B", "gate/run_tests.py", "elements/common"]),
    ("project-level", ["python", "-B", "gate/run_tests.py", "project-level"]),
    ("task-cycle", ["python", "-B", "gate/run_tests.py", "task-cycle"]),
    ("agent-instructions", ["python", "-B", "gate/run_tests.py", "agent-instructions"]),
    ("decision-form", ["python", "-B", "elements/decisions/format_guard.py", "--base", "none", "--merge-onto", "none"]),
    ("invariant-form", ["python", "-B", "elements/invariants/format_guard.py", "--base", "none", "--merge-onto", "none"]),
    ("decision-relations", ["python", "-B", "elements/decisions/format_guard.py", "--base", "none", "--merge-onto", target]),
    ("invariant-relations", ["python", "-B", "elements/invariants/format_guard.py", "--base", "none", "--merge-onto", target]),
    ("whitespace", ["git", "diff", "--check", target + "..HEAD"]),
]
results = []
for name, command in commands:
    result = subprocess.run(command, cwd=repo, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = report_dir / (prefix + "-" + name + ".txt")
    header = ("Command: " + subprocess.list2cmdline(command) + "\nExit code: " + str(result.returncode) + "\n\n").encode("utf-8")
    output.write_bytes(header + result.stdout)
    results.append({"name": name, "command": command, "exit": result.returncode, "output": output.name})
    print(name + ": exit=" + str(result.returncode), flush=True)
(report_dir / (prefix + "-checks.json")).write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
sys.exit(1 if any(row["exit"] for row in results) else 0)
