"""Own-work check of the CI file: the Windows job is built to run the tests Linux skips.

Run from the worktree root: python -B -I .runs/author/check_ci_file.py
Exit code 0 when every assertion holds, 1 with the failed assertion otherwise.
"""

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent.parent
workflow = yaml.safe_load((ROOT / ".github/workflows/tests.yml").read_text(encoding="utf-8"))
text = (ROOT / ".github/workflows/tests.yml").read_text(encoding="utf-8")
jobs = workflow["jobs"]

assert workflow[True] == {"pull_request": {"branches": ["foundations"]}}, "trigger"
assert workflow["permissions"] == {"contents": "read"}, "permissions"
assert {job["name"] for job in jobs.values()} == {"tests", "tests-windows"}, "names"
assert jobs["tests"]["runs-on"] == "ubuntu-latest"
assert jobs["tests-windows"]["runs-on"] == "windows-latest"
assert "pull_request_target" not in text.replace("never `pull_request_target`", "")

linux = jobs["tests"]["steps"]
windows = jobs["tests-windows"]["steps"]
# The same actions at the same commits in both jobs.
uses = lambda steps: [step["uses"] for step in steps if "uses" in step]  # noqa: E731
assert uses(linux) == uses(windows), "actions differ"
for action in uses(windows):
    assert re.fullmatch(r"[\w./-]+@[0-9a-f]{40}", action), f"not pinned: {action}"
# The gate step is the one command with no directory, in both jobs.
for steps in (linux, windows):
    assert steps[-1] == {"run": "python -B gate/run_tests.py"}, steps[-1]
# The venv lies where the test looks for the program on Windows: Scripts/ruff.exe of
# .runs/quality-venv, and pip is the venv's own interpreter.
venv = [step["run"] for step in windows if "quality-venv" in step.get("run", "")][0]
assert "python -m venv .runs/quality-venv" in venv
assert ".runs/quality-venv/Scripts/python.exe -m pip install --require-hashes -r " \
       "requirements-quality.txt" in venv
test = (ROOT / "agent-instructions/test_linter_invariant.py").read_text(encoding="utf-8")
assert '"Scripts/ruff.exe" if os.name == "nt"' in test and '".runs" / "quality-venv"' in test
assert jobs["tests-windows"]["defaults"]["run"]["shell"] == "bash"
print("the CI file holds: two jobs, the Windows one makes the venv the Windows tests look for")
sys.exit(0)
