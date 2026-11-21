"""Writes each mutant of gate_times.py into the head worktree in turn, runs the NestedRunTest tests,
and restores the file. Run: python -B -I mutate.py <head worktree> <rules dir>"""

import subprocess
import sys
from pathlib import Path

HEAD = Path(sys.argv[1])
RULES = Path(sys.argv[2])
TARGET = HEAD / "task-cycle" / "gate_times.py"
ORIGINAL = TARGET.read_bytes()
SOURCE = ORIGINAL.decode("utf-8")

OPENED = "opened = any(self.count - mark == directories - 1 for mark in self.marks)"
MUTANTS = {
    "base rule (54b28445)": (RULES / "gt_base.py").read_text(encoding="utf-8"),
    "no clear at summary": SOURCE.replace("        self.marks.clear()\n", ""),
    "no dedup": SOURCE.replace(
        "if BLOCK in text and (not self.marks or self.marks[-1] != self.count):",
        "if BLOCK in text:",
    ),
    "opened never (orig rule)": SOURCE.replace(OPENED, "opened = False"),
    "opened whenever a mark (direction)": SOURCE.replace(OPENED, "opened = bool(self.marks)"),
    "only the last mark": SOURCE.replace(
        OPENED, "opened = bool(self.marks) and self.count - self.marks[-1] == directories - 1"
    ),
    "only the first mark": SOURCE.replace(
        OPENED, "opened = bool(self.marks) and self.count - self.marks[0] == directories - 1"
    ),
    "unbounded marks": SOURCE.replace(
        "self.marks: deque[int] = deque(maxlen=SUMMARIES_KEPT)", "self.marks: deque[int] = deque()"
    ),
    "directories not less one": SOURCE.replace(
        "directories - 1 if opened else directories, surplus", "directories, surplus"
    ),
}

try:
    for name, text in MUTANTS.items():
        if text == SOURCE:
            print(f"{name}: NOT APPLIED")
            continue
        TARGET.write_bytes(text.encode("utf-8"))
        done = subprocess.run(
            [sys.executable, "-B", "-m", "unittest", "test_gate_times.NestedRunTest"],
            cwd=HEAD / "task-cycle",
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        failed = [
            line.split("(")[0].replace("FAIL: ", "").replace("ERROR: ", "").strip()
            for line in done.stderr.splitlines()
            if line.startswith(("FAIL: ", "ERROR: "))
        ]
        print(f"{name}: exit {done.returncode}; failing: {failed}")
finally:
    TARGET.write_bytes(ORIGINAL)
