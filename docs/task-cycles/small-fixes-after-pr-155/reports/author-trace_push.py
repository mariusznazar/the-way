"""One-off check: pushes into origin.git of the Fixture with GIT_TRACE on and prints the trace lines
that start `git maintenance` or `git gc`, the lines about origin.git, and their count.

Run from the worktree root: python -B -I .runs/author/trace_push.py <directory holding the test file> <trace file>
"""

import re
import sys
import time
from pathlib import Path

directory, trace_file = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
sys.path.insert(0, str(directory))
import test_remove_merged_worktrees as module  # noqa: E402

trace_file.unlink(missing_ok=True)
module.ENVIRONMENT["GIT_TRACE"] = str(trace_file)
fixture = module.Fixture()
try:
    fixture.task("merged")
    unmerged = fixture.add("unmerged", "task/unmerged")
    fixture.commit(unmerged)
    fixture.push("task/unmerged")
    time.sleep(3)  # a maintenance run left in the background has started by now
    text = trace_file.read_text(encoding="utf-8", errors="replace")
finally:
    fixture.close()
lines = text.splitlines()
runs = [line for line in lines if re.search(r"(run_command|start_command|built-in|exec): git (maintenance|gc)\b", line)]
receive = [line for line in lines if "receive-pack" in line]
print(f"trace lines: {len(lines)}")
print(f"lines naming git-receive-pack: {len(receive)}")
print(f"lines that run git maintenance or git gc: {len(runs)}")
for line in runs:
    print("  " + line)
