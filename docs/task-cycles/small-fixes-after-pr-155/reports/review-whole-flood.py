"""Reviewer's one-off check at the trust boundary: time and peak memory of Times on crafted floods,
for gate_times.py of the base and of the head. Usage: python -B -I flood.py BASE_FILE HEAD_FILE"""

import importlib.util
import sys
import time
import tracemalloc


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def summaries_after_marks(n):
    # 100 different places of lines with `== ` after text, then n summary lines.
    for index in range(100):
        yield f"== d{index}".encode()
        yield b"    assert x == y"
    for _ in range(n):
        yield b"1 tests in 1 directories; every directory passed"
    yield b"3 tests in 3 directories; every directory passed"


def alternating(n):
    # A place, a line `== ` after text and a summary line, n times.
    for index in range(n):
        yield f"== d{index}".encode()
        yield b"    assert x == y"
        yield b"2 tests in 2 directories; every directory passed"
    yield b"3 tests in 3 directories; every directory passed"


modules = {"base": load("gt_base", sys.argv[1]), "head": load("gt_head", sys.argv[2])}
for label, make in (("summaries_after_marks", summaries_after_marks), ("alternating", alternating)):
    for name, module in modules.items():
        times = module.Times()
        tracemalloc.start()
        start = time.perf_counter()
        for line in make(300_000):
            times.line(line)
        result = times.result()
        elapsed = time.perf_counter() - start
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"{label} {name}: {elapsed:.2f}s peak {peak} blocks {len(result[0])} rest {result[1]}")
