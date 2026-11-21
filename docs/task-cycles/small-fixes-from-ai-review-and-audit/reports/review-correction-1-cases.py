"""Reads hand-built gate outputs with four versions of Times and prints each result against the
expected one. Run: python -B -I cases.py <dir of the rule files>"""

import importlib.util
import sys
from pathlib import Path

RULES = Path(sys.argv[1])
RULE = "-" * 70
FAILURE_RULE = "=" * 70
SUMMARY_TWO = "2 tests in 2 directories; every directory passed\n"


def load(name):
    spec = importlib.util.spec_from_file_location(name, RULES / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def passing(d, s):
    return f"== {d}\n.\n{RULE}\nRan 1 test in {s}s\n\nOK\n"


def failing_dir(d, s, assert_line="    assert x == y"):
    return (
        f"== {d}\nF\n{FAILURE_RULE}\nFAIL: test_b (test_b.B.test_b)\n{RULE}\n"
        f"Traceback (most recent call last):\n{assert_line}\nAssertionError\n\n"
        f"{RULE}\nRan 1 test in {s}s\n\nFAILED (failures=1)\n"
    )


def failing_with(nested, s, d="gate", sep="AssertionError: 0 != 5 : "):
    return (
        f"== {d}\nF\n{FAILURE_RULE}\n"
        f"FAIL: test_nested (test_nested.N.test_nested)\n{RULE}\n"
        "Traceback (most recent call last):\n"
        '  File "gate/test_nested.py", line 6, in test_nested\n'
        f"    self.assertEqual(0, 5, done.stdout)\n{sep}{nested}\n\n{RULE}\n"
        f"Ran 1 test in {s}s\n\nFAILED (failures=1)\n"
    )


CASES = []


def case(name, text, expected):
    CASES.append((name, text, expected))


case(
    "A two dirs each print nested run",
    passing("other", "0.002")
    + failing_with(passing("x1", "0.001") + passing("y1", "0.003") + SUMMARY_TWO, "0.500", "gate1")
    + failing_with(passing("x2", "0.004") + passing("y2", "0.005") + SUMMARY_TWO, "0.600", "gate2")
    + "5 tests in 3 directories; failed: gate1 (exit code 1), gate2 (exit code 1)\n",
    [ ["other", "0.002"], ["gate1", "0.500"], ["gate2", "0.600"]],
)
case(
    "C whole beside cut-off",
    passing("other", "0.002")
    + failing_with(passing("x1", "0.001") + passing("y1", "0.003") + SUMMARY_TWO, "0.500", "gate1")
    + failing_with(passing("x2", "0.004") + passing("y2", "0.005"), "0.600", "gate2")
    + "5 tests in 3 directories; failed: gate1 (exit code 1), gate2 (exit code 1)\n",
    [ ["other", "0.002"], ["gate1", "0.500"], ["gate2", "0.004"], ["y2", "0.005"]],
)
N1_NESTED = (
    passing("a", "0.001")
    + failing_dir("b", "0.002")
    + passing("c", "0.003")
    + "3 tests in 3 directories; every directory passed\n"
)
case(
    "N1 confirmed input",
    failing_with(N1_NESTED, "0.500") + "1 tests in 1 directories; failed: gate (exit code 1)\n",
    [ ["gate", "0.500"]],
)
case(
    "T marker in enclosing traceback before failure message",
    passing("other", "0.002")
    + "== gate\nF\n    assert 0 == 5\n"
    + f"AssertionError: 0 != 5 : {passing('x', '0.001')}{passing('y', '0.003')}{SUMMARY_TWO}"
    + f"\n{RULE}\nRan 1 test in 0.539s\n\nFAILED (failures=1)\n"
    + "4 tests in 2 directories; failed: gate (exit code 1)\n",
    [ ["other", "0.002"], ["gate", "0.539"]],
)
case(
    "T2 marker in enclosing traceback, nested of 3",
    passing("other", "0.002")
    + "== gate\nF\n    assert 0 == 5\n"
    + "AssertionError: 0 != 5 : "
    + passing("x", "0.001") + passing("y", "0.003") + passing("z", "0.004")
    + "3 tests in 3 directories; every directory passed\n"
    + f"\n{RULE}\nRan 1 test in 0.539s\n\nFAILED (failures=1)\n"
    + "5 tests in 2 directories; failed: gate (exit code 1)\n",
    [ ["other", "0.002"], ["gate", "0.539"]],
)
case(
    "N1 + A: two dirs print nested runs, the second's middle dir prints assert",
    passing("other", "0.002")
    + failing_with(passing("x1", "0.001") + passing("y1", "0.003") + SUMMARY_TWO, "0.500", "gate1")
    + failing_with(N1_NESTED, "0.600", "gate2")
    + "6 tests in 3 directories; failed: gate1 (exit code 1), gate2 (exit code 1)\n",
    [ ["other", "0.002"], ["gate1", "0.500"], ["gate2", "0.600"]],
)
case(
    "N1 with m=2: assert in the last nested dir",
    failing_with(passing("a", "0.001") + failing_dir("b", "0.002") + SUMMARY_TWO, "0.500")
    + "1 tests in 1 directories; failed: gate (exit code 1)\n",
    [ ["gate", "0.500"]],
)
case(
    "assert in the first nested dir (after text)",
    failing_with(failing_dir("a", "0.001") + passing("b", "0.002") + SUMMARY_TWO, "0.500")
    + "1 tests in 1 directories; failed: gate (exit code 1)\n",
    [ ["gate", "0.500"]],
)
case(
    "fix-1 case: assert a == b after the nested first line",
    passing("other", "0.002")
    + "== gate1\nF\nAssertionError: 0 != 5 : == x\n    assert a == b\n.\n"
    + f"{RULE}\nRan 1 test in 0.001s\n\nOK\n"
    + passing("y", "0.003") + SUMMARY_TWO
    + f"\n{RULE}\nRan 1 test in 0.500s\n\nFAILED (failures=1)\n"
    + "4 tests in 2 directories; failed: gate1 (exit code 1)\n",
    [ ["other", "0.002"], ["gate1", "0.500"]],
)
case(
    "G nested at start of a line, no marker",
    failing_with(passing("x", "0.001") + passing("y", "0.003") + SUMMARY_TWO, "0.500",
                 sep="AssertionError: 0 != 5 :\n")
    + "3 tests in 1 directories; failed: gate (exit code 1)\n",
    [ ["gate", "0.500"]],
)
case(
    "X author's case: nested at start of line, assert in first nested dir",
    "== gate\nF\n" + failing_dir("x", "0.001", "    assert p == q").replace("F\n", ".\n", 0)
    + passing("y", "0.003") + SUMMARY_TWO
    + "Ran 1 test in 0.5s\n\nFAILED (failures=1)\n"
    + "3 tests in 1 directories; failed: gate (exit code 1)\n",
    [ ["gate", "0.5"]],
)
case(
    "X1 nested of one dir at start of line whose test prints assert",
    "== gate\nF\n" + failing_dir("x", "0.001") + "1 tests in 1 directories; failed: x (exit code 1)\n"
    + "Ran 1 test in 0.5s\n\nFAILED (failures=1)\n"
    + "2 tests in 1 directories; failed: gate (exit code 1)\n",
    [ ["gate", "0.5"]],
)
case(
    "X with the outer marker elsewhere (earlier dir traceback)",
    failing_dir("other", "0.002")
    + failing_with(passing("x", "0.001") + passing("y", "0.003") + SUMMARY_TWO, "0.500",
                   sep="AssertionError: 0 != 5 :\n")
    + "4 tests in 2 directories; failed: gate (exit code 1)\n",
    [ ["other", "0.002"], ["gate", "0.500"]],
)
case(
    "crafted: summary with 0 directories after a marker",
    "== a\n x == y\nRan 1 test in 0.1s\n0 tests in 0 directories; every directory passed\n"
    + "== b\nRan 1 test in 0.2s\n1 tests in 1 directories; every directory passed\n",
    None,
)
case(
    "crafted: huge directory count after a marker",
    "== a\n x == y\n== b\n1 tests in 999999999 directories; every directory passed\n"
    + "== c\nRan 1 test in 0.2s\n1 tests in 1 directories; every directory passed\n",
    None,
)


def read(module, text):
    times = module.Times()
    for line in text.encode("utf-8").split(b"\n"):
        if line:
            times.line(line)
    blocks, _ = times.result()
    return blocks


for name, text, expected in CASES:
    print(f"## {name}  expected={expected}")
    for rule in ("gt_orig", "gt_base", "gt_head", "gt_direction", "gt_lastmark", "gt_firstmark", "gt_noclear"):
        got = read(load(rule), text)
        mark = "" if expected is None else ("ok" if got == expected else "WRONG")
        print(f"  {rule:13} {mark:5} {got}")
