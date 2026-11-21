"""One-off check: the code of the change and the same code with `self.marks.clear()` restored give
the same result() on random outputs. Run from the worktree root: python -B -I .runs/author/probe.py
"""

import importlib.util
import random
import sys
from pathlib import Path

SOURCE = Path("task-cycle/gate_times.py").read_text(encoding="utf-8")
ANCHOR = "        self.segment = self.count\n"
assert SOURCE.count(ANCHOR) == 1
WITH_CLEAR = SOURCE.replace(ANCHOR, ANCHOR + "        self.marks.clear()\n")
folder = Path(".runs/author/probe_copies")
folder.mkdir(parents=True, exist_ok=True)
(folder / "gt_current.py").write_text(SOURCE, encoding="utf-8", newline="")
(folder / "gt_clear.py").write_text(WITH_CLEAR, encoding="utf-8", newline="")


def load(name):
    spec = importlib.util.spec_from_file_location(name, folder / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


current, cleared = load("gt_current"), load("gt_clear")
TOKENS = [
    "== d",
    "== d",
    "    assert x == y",
    "text == d",
    "Ran 1 test in 0.1s",
    "2 tests in 2 directories; every directory passed",
    "3 tests in 3 directories; every directory passed",
    "1 tests in 1 directories; every directory passed",
    "4 tests in 4 directories; every directory passed",
    "plain",
]
random.seed(20261121)
different = 0
runs = 200_000
for _ in range(runs):
    lines = [random.choice(TOKENS) for _ in range(random.randint(1, 30))]
    results = []
    for module in (current, cleared):
        times = module.Times()
        for index, line in enumerate(lines):
            text = line if line != "== d" else f"== d{index}"
            times.line(text.encode("utf-8"))
        results.append(times.result())
    if results[0] != results[1]:
        different += 1
print(f"random outputs: {runs}; different results: {different}")
