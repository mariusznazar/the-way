"""Tests of the invariant `function-and-file-size` (WAY-385, WAY-361).

The first test checks the counting on made-up source text. The second test is the test of the
invariant: it counts the lines of every function and every file of a script that git tracks in the
parts with Python code, and fails while a function has more than 80 lines or a file more than 1000.
That invariant reads `Violated: yes` (WAY-51), so the second test is marked as an expected failure;
it stays apart from the first test so that the counting is checked even while the expected failure
stands. The change in which the last function and file are divided removes the marking and the mark
of the invariant: an expected failure that passes ends the run as an unexpected success.

The count runs in this file, outside the run of the linter (WAY-385). A function counts from its
`def` line to its last line, the functions nested in it included; a method is a function; a file
counts its lines. Test files, whose names begin `test_`, stand outside the rule (WAY-385).

Run from the root of the-way: python -B gate/run_tests.py agent-instructions
"""

import ast
import subprocess
import sys
import unittest
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent.parent
# The parts with Python code, as the directories that hold it.
PARTS = (
    "agent-instructions",
    "elements",
    "gate",
    "installation",
    "instruction-files",
    "process-audit",
    "product-guidelines",
    "project-level",
    "relation-model",
    "task-cycle",
)
FUNCTION_LIMIT = 80
FILE_LIMIT = 1000


def function_sizes(source: str) -> list[tuple[str, int, int]]:
    """Every function of the source as (name, first line, lines), counted with the functions
    nested in it."""
    sizes = []
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            sizes.append((node.name, node.lineno, node.end_lineno - node.lineno + 1))
    return sizes


def file_lines(source: str) -> int:
    """The number of lines of a file."""
    return len(source.splitlines())


def script_files() -> list[Path]:
    """The Python files git tracks in the parts with Python code, except the test files."""
    done = subprocess.run(
        ["git", "ls-files", "-z", "--", *PARTS],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    names = [name for name in done.stdout.split("\0") if name.endswith(".py")]
    return [ROOT / name for name in names if not Path(name).name.startswith("test_")]


class Counting(unittest.TestCase):
    def test_a_function_counts_the_functions_nested_in_it_and_a_method_is_a_function(self) -> None:
        # decision: WAY-385 "A function of a script of the-way has at most 110 lines, counted with the functions nested in it"
        source = (
            "def outer():\n"
            "    x = 1\n"
            "    def inner():\n"
            "        return x\n"
            "    return inner\n"
            "\n"
            "class Holder:\n"
            "    def method(self):\n"
            "        return 2\n"
        )
        self.assertEqual(
            sorted(function_sizes(source)), [("inner", 3, 2), ("method", 8, 2), ("outer", 1, 5)]
        )

    def test_a_file_counts_its_lines(self) -> None:
        self.assertEqual(file_lines("x = 1\n\n# note\n"), 3)


class Coverage(unittest.TestCase):
    def test_every_python_file_git_tracks_lies_in_a_part_the_check_reads(self) -> None:
        done = subprocess.run(
            ["git", "ls-files", "-z"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        outside = [
            name
            for name in done.stdout.split("\0")
            if name.endswith(".py") and name.split("/")[0] not in PARTS
        ]
        self.assertEqual(
            outside,
            [],
            "a tracked Python file lies in no directory of PARTS: add "
            "its directory to PARTS and to the Scope of WAY-379",
        )


class Size(unittest.TestCase):
    @unittest.expectedFailure
    # invariant: function-and-file-size
    def test_no_function_or_file_of_a_script_is_over_its_threshold(self) -> None:
        too_long = []
        too_big = []
        for path in script_files():
            source = path.read_text(encoding="utf-8")
            name = path.relative_to(ROOT).as_posix()
            for function, line, lines in function_sizes(source):
                if lines > FUNCTION_LIMIT:
                    too_long.append(f"  {name}:{line} {function}: {lines} lines")
            if file_lines(source) > FILE_LIMIT:
                too_big.append(f"  {name}: {file_lines(source)} lines")
        if too_long or too_big:
            self.fail(
                f"{len(too_long)} functions over {FUNCTION_LIMIT} lines and {len(too_big)} "
                f"files over {FILE_LIMIT} lines:\n" + "\n".join(too_long + too_big)
            )


if __name__ == "__main__":
    unittest.main()
