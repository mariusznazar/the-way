"""One-off check (WAY-402): writes each of the changes (i), (ii), (iii), (v) once into a copy of
task-cycle/gate_times.py under .runs/author/, runs NestedRunTest on the copy, prints the result.

Run from the worktree root: python -B -I .runs/author/mutate.py
"""

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path.cwd()
CYCLE = ROOT / "task-cycle"
WORK = ROOT / ".runs" / "author"
SOURCE = (CYCLE / "gate_times.py").read_text(encoding="utf-8", newline="")

OPENED = "opened = any(self.count - mark == directories - 1 for mark in self.marks)"
DEDUP = "if BLOCK in text and (not self.marks or self.marks[-1] != self.count):"
CLEAR_AFTER = "        self.segment = self.count\n"

MUTANTS = {
    "current": [],
    "i": [(OPENED, "opened = bool(self.marks)")],
    "ii": [
        (
            OPENED,
            "opened = bool(self.marks) and self.count - self.marks[-1] == directories - 1",
        )
    ],
    "iii": [
        (
            OPENED,
            "opened = bool(self.marks) and self.count - self.marks[0] == directories - 1",
        )
    ],
    "v": [(DEDUP, "if BLOCK in text:")],
}


def build(name: str, replacements: list[tuple[str, str]], restore_clear: bool) -> Path:
    text = SOURCE
    for old, new in replacements:
        assert text.count(old) == 1, (name, old)
        text = text.replace(old, new)
    if restore_clear:
        assert text.count(CLEAR_AFTER) == 1
        text = text.replace(CLEAR_AFTER, CLEAR_AFTER + "        self.marks.clear()\n")
    folder = WORK / f"{'withclear' if restore_clear else 'final'}_{name}"
    if folder.exists():
        shutil.rmtree(folder)
    folder.mkdir(parents=True)
    (folder / "gate_times.py").write_text(text, encoding="utf-8", newline="")
    shutil.copy(CYCLE / "test_gate_times.py", folder / "test_gate_times.py")
    return folder


def run(folder: Path) -> tuple[int, list[str]]:
    done = subprocess.run(
        [sys.executable, "-B", "-m", "unittest", "test_gate_times.NestedRunTest"],
        cwd=folder,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    failing = [
        line.split(" ")[1]
        for line in done.stderr.splitlines()
        if line.startswith(("FAIL: ", "ERROR: "))
    ]
    return done.returncode, failing


for restore_clear in (False, True):
    label = "code with `self.marks.clear()` restored" if restore_clear else "code of the change"
    print(f"## base: {label}")
    for name, replacements in MUTANTS.items():
        if restore_clear and name == "current":
            continue
        code, failing = run(build(name, replacements, restore_clear))
        print(f"mutant {name}: exit {code}; red: {failing}")
