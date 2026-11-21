"""Reviewer's one-off mutation check (WAY-402: no tool). Writes each change into
task-cycle/gate_times.py of the worktree given, runs NestedRunTest there, keeps the failure
messages, and restores the file. Usage: python -B -I mutate.py WORKTREE OUTPUT"""

import subprocess
import sys
from pathlib import Path

worktree = Path(sys.argv[1])
output = Path(sys.argv[2])
target = worktree / "task-cycle" / "gate_times.py"
original = target.read_bytes()
source = original.decode("utf-8")

OPENED = "        opened = any(self.count - mark == directories - 1 for mark in self.marks)\n"
GUARD = "        if BLOCK in text and (not self.marks or self.marks[-1] != self.count):\n"
SEGMENT = "        self.segment = self.count\n"
MUTANTS = {
    "current": [],
    "i": [(OPENED, "        opened = bool(self.marks)\n")],
    "ii": [
        (
            OPENED,
            "        opened = bool(self.marks) and self.count - self.marks[-1] == directories - 1\n",
        )
    ],
    "iii": [
        (
            OPENED,
            "        opened = bool(self.marks) and self.count - self.marks[0] == directories - 1\n",
        )
    ],
    "v": [(GUARD, "        if BLOCK in text:\n")],
    "iv_clear_back": [(SEGMENT, SEGMENT + "        self.marks.clear()\n")],
    "r1_no_minus_one": [
        (OPENED, "        opened = any(self.count - mark == directories for mark in self.marks)\n")
    ],
    "r2_never_opened": [(OPENED, "        opened = False\n")],
    "r3_marks_maxlen_10": [
        (
            "        self.marks: deque[int] = deque(maxlen=SUMMARIES_KEPT)\n",
            "        self.marks: deque[int] = deque(maxlen=10)\n",
        )
    ],
    "r4_mark_only_at_start_dedupe_any": [
        (GUARD, "        if BLOCK in text and self.count not in self.marks:\n")
    ],
}

lines = []
try:
    for name, edits in MUTANTS.items():
        text = source
        for old, new in edits:
            assert text.count(old) == 1, (name, old)
            text = text.replace(old, new)
        target.write_bytes(text.encode("utf-8"))
        done = subprocess.run(
            [sys.executable, "-B", "-m", "unittest", "test_gate_times.NestedRunTest"],
            cwd=worktree / "task-cycle",
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        red = [
            line.split("(")[0].split()[-1]
            for line in done.stderr.splitlines()
            if line.startswith(("FAIL:", "ERROR:"))
        ]
        lines.append(f"## mutant {name}: exit {done.returncode}; red: {red}")
        if name != "current":
            lines.append(done.stderr)
finally:
    target.write_bytes(original)
output.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
print("done", len(MUTANTS))
