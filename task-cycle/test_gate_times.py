"""Tests of task-cycle/gate_times.py on made-up gate output: each command here prints the lines the gate
prints, never the real gate.

The expected rows and counts are worked out by hand from the output written here, not by the script.
"""

from __future__ import annotations

import ast
import io
import os
import re
import signal
import subprocess
import sys
import tempfile
import textwrap
import tracemalloc
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parent
SCRIPT = HERE / "gate_times.py"

sys.path.insert(0, str(HERE))

import gate_times

HEADING = "# Gate runs of the cycle"
TABLE_HEADER = (
    "| Started (UTC) | Exit code | Total seconds | Other gate runs at the same time "
    "| Directory | Directory seconds |"
)
STARTED = re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}$")
TOTAL = re.compile(r"^\d+\.\d{3}$")
ENDED = re.compile(r"^(\d+)_(\d+)_([A-Za-z0-9]+)\.run$")
HOUR = 3600 * 1000
DAY = 24 * HOUR
# The instant the script's clock gives in the tests of the registry: 2025-10-09 08:53:20.123 UTC.
NOW = 1_760_000_000_123
NOW_STAMP = "2025-10-09 08:53:20.123"


def printed(text: bytes, code: int = 0) -> list[str]:
    """A command that writes `text` to its output exactly, as bytes, and exits with `code`. The text
    comes in hex in the arguments, so that the code of the command stays a literal."""
    return [
        sys.executable,
        "-c",
        "import sys; sys.stdout.buffer.write(bytes.fromhex(sys.argv[1])); sys.exit(int(sys.argv[2]))",
        text.hex(),
        str(code),
    ]


class GateTimesTest(unittest.TestCase):
    """Each test runs the script in a folder of its own, removed afterwards."""

    def setUp(self) -> None:
        self.folder = tempfile.TemporaryDirectory()
        self.root = Path(self.folder.name)
        self.output = self.root / "out" / "gate_times.md"
        self.registry = self.root / "registry"
        self.env = dict(os.environ)
        self.env["USERPROFILE"] = str(self.root / "home")
        self.env["HOME"] = str(self.root / "home")

    def tearDown(self) -> None:
        self.folder.cleanup()

    def run_gate(
        self, command: list[str], options: list[str] | None = None, end_options: bool = True
    ) -> subprocess.CompletedProcess:
        """Runs the script with the command after `--`, from the folder of the test."""
        if options is None:
            options = ["--output", str(self.output), "--registry", str(self.registry)]
        args = [sys.executable, "-B", str(SCRIPT), *options]
        if end_options:
            args.append("--")
        return subprocess.run([*args, *command], capture_output=True, cwd=self.root, env=self.env)

    def run_gate_at(self, now: int, command: list[str]) -> subprocess.CompletedProcess:
        """Runs the script's `main` in this process with its clock fixed at `now` milliseconds, so
        that the run starts and ends at that instant; the registry and the output are the ones of the
        test. The home directory is the test's own, as for a run of the script in a process."""
        stdout = io.TextIOWrapper(io.BytesIO(), encoding="utf-8")
        stderr = io.StringIO()
        arguments = ["--output", str(self.output), "--registry", str(self.registry), "--", *command]
        with (
            mock.patch.object(gate_times, "now_ms", return_value=now),
            mock.patch.dict(os.environ, self.env),
            redirect_stdout(stdout),
            redirect_stderr(stderr),
        ):
            code = gate_times.main(arguments)
        stdout.flush()
        return subprocess.CompletedProcess(
            arguments, code, stdout.buffer.getvalue(), stderr.getvalue().encode("utf-8")
        )

    def rows(self) -> list[list[str]]:
        """The rows of the table in the output file, each as its cells."""
        text = self.output.read_bytes().decode("utf-8")
        body = [
            line
            for line in text.split("\n")
            if line.startswith("| ") and line != TABLE_HEADER and not line.startswith("| ---")
        ]
        return [[cell.strip() for cell in line.strip("|").split("|")] for line in body]


class RowsTest(GateTimesTest):
    def test_rows_follow_the_order_the_gate_printed_them(self) -> None:
        # Made-up output with the directories out of alphabetical order.
        result = self.run_gate(
            printed(b"== zeta\nRan 3 tests in 0.010s\n\nOK\n== alpha\nRan 1 test in 0.002s\n\nOK\n")
        )
        self.assertEqual(0, result.returncode, result.stderr)
        rows = self.rows()
        self.assertEqual(2, len(rows))
        self.assertEqual(["zeta", "0.010"], rows[0][4:])
        self.assertEqual(["alpha", "0.002"], rows[1][4:])
        self.assertEqual(rows[0][:4], rows[1][:4])
        self.assertRegex(rows[0][0], STARTED)
        self.assertRegex(rows[0][2], TOTAL)
        self.assertEqual(["0", "0"], [rows[0][1], rows[0][3]])

    def test_block_without_a_ran_line_gives_unknown(self) -> None:
        result = self.run_gate(
            printed(b"== first\nno timing here\n== second\nRan 2 tests in 0.5s\n")
        )
        self.assertEqual(0, result.returncode, result.stderr)
        rows = self.rows()
        self.assertEqual(["first", "unknown"], rows[0][4:])
        self.assertEqual(["second", "0.5"], rows[1][4:])

    def test_first_ran_line_after_its_own_block_counts(self) -> None:
        # The Ran line after `== b` belongs to b; a has none before the next block. A second Ran
        # line in b does not replace the first.
        result = self.run_gate(printed(b"== a\n== b\nRan 1 test in 0.1s\nRan 5 tests in 7.7s\n"))
        self.assertEqual(0, result.returncode, result.stderr)
        rows = self.rows()
        self.assertEqual(["a", "unknown"], rows[0][4:])
        self.assertEqual(["b", "0.1"], rows[1][4:])

    def test_text_before_the_first_block_belongs_to_no_directory(self) -> None:
        result = self.run_gate(
            printed(b"Ran 9 tests in 9.9s\nstray\n== only\nRan 1 test in 0.100s\n")
        )
        self.assertEqual(0, result.returncode, result.stderr)
        rows = self.rows()
        self.assertEqual(1, len(rows))
        self.assertEqual(["only", "0.100"], rows[0][4:])

    def test_run_with_no_block_gives_one_row_with_dashes(self) -> None:
        result = self.run_gate(printed(b"no directory printed\n"))
        self.assertEqual(0, result.returncode, result.stderr)
        rows = self.rows()
        self.assertEqual(1, len(rows))
        self.assertEqual(["—", "—"], rows[0][4:])

    def test_directory_cell_is_one_line_with_each_bar_replaced(self) -> None:
        result = self.run_gate(printed(b"== a|b  c\nRan 1 test in 0.1s\n"))
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual(["a/b c", "0.1"], self.rows()[0][4:])


RULE = "-" * 70
FAILURE_RULE = "=" * 70
SUMMARY_TWO = "2 tests in 2 directories; every directory passed\n"


def passing(directory: str, seconds: str) -> str:
    """The report `gate/run_tests.py` prints for a directory whose one test passes, under its line."""
    return f"== {directory}\n.\n{RULE}\nRan 1 test in {seconds}s\n\nOK\n"


def failing_with(nested: str, seconds: str, directory: str = "gate") -> str:
    """The report of the directory `directory` whose one test fails and prints, in its failure
    message, the output of a nested run of the runner (`nested`, ending with its summary line and a
    line end), as the unittest of Python prints it: the first line of `nested` stands after the
    text of the message, the rest at the start of their lines, and the directory's own `Ran` line
    comes after it."""
    return (
        f"== {directory}\nF\n{FAILURE_RULE}\n"
        f"FAIL: test_nested (test_nested.N.test_nested)\n{RULE}\n"
        "Traceback (most recent call last):\n"
        '  File "gate/test_nested.py", line 6, in test_nested\n'
        f"    self.assertEqual(0, 5, done.stdout)\nAssertionError: 0 != 5 : {nested}\n\n{RULE}\n"
        f"Ran 1 test in {seconds}s\n\nFAILED (failures=1)\n"
    )


class NestedRunTest(GateTimesTest):
    """The output of a gate run whose failing test printed the output of a nested run of the runner:
    the lines `== <directory>` of the nested run are no directories of the run, and the directory in
    which the test failed gets its own time.

    The outputs are written out by hand, as the runner and unittest print them; the rows expected are
    worked out from them by hand."""

    def read(self, text: str, code: int = 1) -> list[list[str]]:
        result = self.run_gate(printed(text.encode("utf-8"), code=code))
        self.assertEqual(code, result.returncode, result.stderr)
        return [row[4:] for row in self.rows()]

    def test_the_directories_a_nested_run_opened_are_no_directories_of_the_run(self) -> None:
        # The nested run has two directories: `tests/one` stands in the failure message after text
        # and opens no block; `tests/two` stands at the start of its line. Three lines open a block
        # and the run's own summary counts 2 directories (`other`, `gate`), so one line is the
        # nested run's: the one directly before the nested summary line.
        text = (
            passing("other", "0.002")
            + failing_with(
                passing("tests/one", "0.001") + passing("tests/two", "0.003") + SUMMARY_TWO,
                "0.539",
            )
            + "4 tests in 2 directories; failed: gate (exit code 1)\n"
        )
        self.assertIn("AssertionError: 0 != 5 : == tests/one\n", text)
        self.assertEqual([["other", "0.002"], ["gate", "0.539"]], self.read(text))

    def test_a_nested_run_of_three_directories_gives_two_lines_that_open_no_block(self) -> None:
        # The first of the three directories stands after text, the other two at the start of a
        # line. Four lines open a block and the run's own summary counts 2, so two are nested.
        nested = (
            passing("tests/three", "0.000")
            + passing("tests/one", "0.001")
            + passing("tests/two", "0.003")
            + "3 tests in 3 directories; every directory passed\n"
        )
        text = (
            passing("other", "0.002")
            + failing_with(nested, "0.539")
            + "5 tests in 2 directories; failed: gate (exit code 1)\n"
        )
        self.assertEqual([["other", "0.002"], ["gate", "0.539"]], self.read(text))

    def test_two_nested_runs_in_one_block_give_that_block_the_time_after_the_last(self) -> None:
        # Two failing tests of `gate`, each with a nested run of two directories whose first line
        # stands after text. Four lines open a block (`alpha`, `gate`, `b`, `d`) and the run's own
        # summary counts 2, so two are nested: `b`, before the first nested summary, and `d`,
        # before the second. The Ran line after the second nested summary is the block's.
        text = (
            passing("alpha", "0.010")
            + "== gate\nFF\n"
            + f"{FAILURE_RULE}\nFAIL: test_one (test_nested.N.test_one)\n{RULE}\n"
            + f"AssertionError: 0 != 5 : {passing('a', '0.001')}{passing('b', '0.002')}"
            + f"{SUMMARY_TWO}\n\n"
            + f"{FAILURE_RULE}\nFAIL: test_two (test_nested.N.test_two)\n{RULE}\n"
            + f"AssertionError: 0 != 5 : {passing('c', '0.004')}{passing('d', '0.005')}"
            + f"{SUMMARY_TWO}\n\n"
            + f"{RULE}\nRan 2 tests in 0.700s\n\nFAILED (failures=2)\n"
            + "6 tests in 2 directories; failed: gate (exit code 1)\n"
        )
        self.assertEqual([["alpha", "0.010"], ["gate", "0.700"]], self.read(text))

    def test_a_nested_run_in_a_block_that_is_not_the_first_leaves_the_blocks_around_it(
        self,
    ) -> None:
        # `alpha`, then `gate` with a nested run of two directories (`x` after text, `y` at the
        # start of a line), then `omega`. Four lines open a block and the run's own summary counts
        # 3, so one is nested: `y`.
        text = (
            passing("alpha", "0.010")
            + failing_with(passing("x", "0.001") + passing("y", "0.003") + SUMMARY_TWO, "0.539")
            + passing("omega", "0.004")
            + "4 tests in 3 directories; failed: gate (exit code 1)\n"
        )
        self.assertEqual(
            [["alpha", "0.010"], ["gate", "0.539"], ["omega", "0.004"]], self.read(text)
        )

    def test_two_directories_that_each_print_a_nested_run_each_keep_their_own_time(self) -> None:
        # Two failing directories, each with a nested run of two directories (`x1`, `x2` after
        # text, `y1`, `y2` at the start of their lines). Five lines open a block (`other`, `gate1`,
        # `y1`, `gate2`, `y2`) and the run's own summary counts 3, so two are nested: `y1` and
        # `y2`, each the one line that follows the text with a directory after it. `gate1` and
        # `gate2` stay blocks and take the first Ran line after their nested summary.
        text = (
            passing("other", "0.002")
            + failing_with(
                passing("x1", "0.001") + passing("y1", "0.003") + SUMMARY_TWO, "0.500", "gate1"
            )
            + failing_with(
                passing("x2", "0.004") + passing("y2", "0.005") + SUMMARY_TWO, "0.600", "gate2"
            )
            + "5 tests in 3 directories; failed: gate1 (exit code 1), gate2 (exit code 1)\n"
        )
        self.assertEqual(
            [["other", "0.002"], ["gate1", "0.500"], ["gate2", "0.600"]], self.read(text)
        )

    def test_a_whole_nested_run_beside_one_cut_off_is_read_by_the_one_with_a_summary_line(
        self,
    ) -> None:
        # `gate1` prints a whole nested run, `gate2` one cut off before its summary line. Five lines
        # open a block and the run's own summary counts 3, so two are nested in all, but only the
        # whole run is known: `y1`, the line that follows the text with `x1` after it. The cut-off
        # run is read as before: `y2` is a block, and `gate2` takes the first Ran line of its text,
        # the nested run's.
        text = (
            passing("other", "0.002")
            + failing_with(
                passing("x1", "0.001") + passing("y1", "0.003") + SUMMARY_TWO, "0.500", "gate1"
            )
            + failing_with(passing("x2", "0.004") + passing("y2", "0.005"), "0.600", "gate2")
            + "5 tests in 3 directories; failed: gate1 (exit code 1), gate2 (exit code 1)\n"
        )
        self.assertEqual(
            [["other", "0.002"], ["gate1", "0.500"], ["gate2", "0.004"], ["y2", "0.005"]],
            self.read(text),
        )

    def test_a_line_with_a_comparison_in_a_nested_failing_test_cuts_no_lines_taken(self) -> None:
        # The nested run has three directories: `a` stands after text, `b` and `c` at the start of
        # their lines, and the failing test of `b` prints the line `    assert x == y`, which holds
        # `== ` after text but opens no directory. Three lines open a block (`gate`, `b`, `c`) and
        # the run's own summary counts 1, so two are nested: `b` and `c`.
        nested = (
            passing("a", "0.001")
            + f"== b\nF\n{FAILURE_RULE}\nFAIL: test_b (test_b.B.test_b)\n{RULE}\n"
            + "Traceback (most recent call last):\n    assert x == y\nAssertionError\n\n"
            + f"{RULE}\nRan 1 test in 0.002s\n\nFAILED (failures=1)\n"
            + passing("c", "0.003")
            + "3 tests in 3 directories; every directory passed\n"
        )
        text = (
            failing_with(nested, "0.500") + "1 tests in 1 directories; failed: gate (exit code 1)\n"
        )
        self.assertEqual([["gate", "0.500"]], self.read(text))

    def test_a_line_with_a_comparison_before_the_failure_message_cuts_no_lines_taken(self) -> None:
        # The traceback of the enclosing test holds `    assert 0 == 5` before the failure
        # message that carries the nested run, whose `x` stands after text and `y` at the start of
        # its line: `y` is nested, and `gate` keeps the time after the nested summary.
        text = (
            passing("other", "0.002")
            + "== gate\nF\n    assert 0 == 5\n"
            + f"AssertionError: 0 != 5 : {passing('x', '0.001')}{passing('y', '0.003')}{SUMMARY_TWO}"
            + f"\n{RULE}\nRan 1 test in 0.539s\n\nFAILED (failures=1)\n"
            + "4 tests in 2 directories; failed: gate (exit code 1)\n"
        )
        self.assertEqual([["other", "0.002"], ["gate", "0.539"]], self.read(text))

    def test_a_nested_run_cut_off_before_its_summary_line_is_read_as_before(self) -> None:
        # The nested output ends before its summary line, so the run holds one summary line, its
        # own, and is read as it was: `tests/two` is a block, and `gate` takes the first Ran line
        # of its text, which is the nested run's.
        text = (
            failing_with(passing("tests/one", "0.001") + passing("tests/two", "0.003"), "0.539")
            + "2 tests in 1 directories; failed: gate (exit code 1)\n"
        )
        self.assertEqual([["gate", "0.001"], ["tests/two", "0.003"]], self.read(text))

    def test_a_nested_run_that_passes_gives_the_directory_the_time_after_it(self) -> None:
        # A passing test of `gate` prints a nested run whose first line stands after the dot of the
        # test; `tests/two` is nested, and the Ran line after the nested summary is the
        # directory's own.
        text = (
            passing("other", "0.002")
            + f"== gate\n.== tests/one\n.\n{RULE}\nRan 1 test in 0.001s\n\nOK\n"
            + passing("tests/two", "0.003")
            + SUMMARY_TWO
            + f".\n{RULE}\nRan 1 test in 0.050s\n\nOK\n"
            + "3 tests in 2 directories; every directory passed\n"
        )
        self.assertEqual([["other", "0.002"], ["gate", "0.050"]], self.read(text, code=0))

    def test_a_block_that_holds_a_nested_summary_and_no_ran_line_after_it_gives_unknown(
        self,
    ) -> None:
        # `gate` was cut off after the nested summary: no Ran line follows it in the block, and the
        # Ran lines of the nested run give it none.
        text = (
            "== other\nRan 1 test in 0.002s\n== gate\nF\nAssertionError: 0 != 5 : x\n"
            + passing("tests/two", "0.003")
            + SUMMARY_TWO
            + "3 tests in 2 directories; failed: gate (exit code -9)\n"
        )
        self.assertEqual([["other", "0.002"], ["gate", "unknown"]], self.read(text))

    def test_a_later_ran_line_after_the_nested_summary_does_not_replace_the_first(self) -> None:
        # Only the first Ran line after the nested summary line is the block's time.
        text = (
            "== gate\nF\nAssertionError: 0 != 5 : x\n"
            + passing("tests/two", "0.003")
            + SUMMARY_TWO
            + "Ran 1 test in 0.539s\n\nFAILED (failures=1)\nRan 9 tests in 9.9s\n"
            + "3 tests in 1 directories; failed: gate (exit code 1)\n"
        )
        self.assertEqual([["gate", "0.539"]], self.read(text))

    def test_the_lines_taken_are_those_before_a_summary_line_and_no_more_than_it_counts(
        self,
    ) -> None:
        # The run's own summary counts 1 directory, so three of the four lines `== …` are surplus.
        # The nested summary counts 2 directories, so it takes `c` and `b`, and `a` stays a block;
        # `d` is not before a summary line that is not the last, so it stays a block as well. `a`
        # holds the nested summary line and no Ran line follows it in its text: unknown.
        text = (
            "== a\nRan 1 test in 0.001s\n== b\nRan 1 test in 0.002s\n== c\nRan 1 test in 0.003s\n"
            + SUMMARY_TWO
            + "== d\nRan 1 test in 0.004s\n"
            + "4 tests in 1 directories; every directory passed\n"
        )
        self.assertEqual([["a", "unknown"], ["d", "0.004"]], self.read(text, code=0))

    def test_summary_lines_with_numbers_no_run_prints_are_no_summary_lines(self) -> None:
        # Crafted: numbers of five thousand digits, which a parse into a number would refuse, and
        # a count of directories beyond the lines shown. No line is nested, and the script
        # neither fails nor changes the exit code of the command.
        huge = "9" * 5000
        text = (
            "== a\nRan 1 test in 0.001s\n"
            f"{huge} tests in {huge} directories; every directory passed\n"
            "== b\nRan 1 test in 0.002s\n"
            "2 tests in 1000 directories; every directory passed\n"
        )
        self.assertEqual([["a", "0.001"], ["b", "0.002"]], self.read(text, code=0))

    def test_a_summary_line_of_digits_no_run_prints_is_no_summary_line(self) -> None:
        # Crafted: the digits are Arabic-Indic ones (three of each), which the runner never prints.
        # Three lines open a block and the run's own summary counts 2; were the crafted line a
        # summary line, `b`, the line before it, would be taken as nested.
        text = (
            "== a\nRan 1 test in 0.001s\n== b\nRan 1 test in 0.002s\n"
            "٣ tests in ٣ directories; every directory passed\n"
            "== c\nRan 1 test in 0.003s\n"
            "3 tests in 2 directories; every directory passed\n"
        )
        self.assertEqual([["a", "0.001"], ["b", "0.002"], ["c", "0.003"]], self.read(text, code=0))

    def test_a_ran_line_with_a_time_no_run_prints_is_no_time(self) -> None:
        # Crafted: a time of five thousand digits stands in no real run; the next line is the time.
        text = "== a\nRan 1 test in " + "9" * 5000 + "s\nRan 1 test in 0.5s\n"
        self.assertEqual([["a", "0.5"]], self.read(text, code=0))

    def test_a_flood_of_lines_with_a_comparison_between_blocks_keeps_the_memory_bounded(self) -> None:
        times = gate_times.Times()
        tracemalloc.start()
        try:
            for index in range(100_000):
                times.line(f"== directory {index}".encode("utf-8"))
                times.line(b"    assert x == y")
            _, peak = tracemalloc.get_traced_memory()
        finally:
            tracemalloc.stop()
        # A hundred places of such lines and fifty blocks take well under a megabyte; one place
        # for each of the hundred thousand lines would take several.
        self.assertLess(peak, 2_000_000)

    def test_a_flood_of_blocks_with_huge_times_keeps_the_memory_bounded(self) -> None:
        times = gate_times.Times()
        huge = b"Ran 1 test in " + b"9" * 100_000 + b"s"
        tracemalloc.start()
        try:
            for index in range(300):
                times.line(f"== directory {index}".encode("utf-8"))
                times.line(huge)
            _, peak = tracemalloc.get_traced_memory()
        finally:
            tracemalloc.stop()
        # Each line is a time of a hundred thousand digits; a hundred of them kept, each as printed,
        # would take ten megabytes.
        self.assertLess(peak, 2_000_000)

    def test_a_flood_of_summary_lines_and_blocks_keeps_the_memory_bounded(self) -> None:
        times = gate_times.Times()
        tracemalloc.start()
        try:
            for index in range(100_000):
                times.line(f"== directory {index}".encode("utf-8"))
                times.line(b"Ran 1 test in 0.1s")
                times.line(b"1 tests in 1 directories; every directory passed")
            times.line(b"3 tests in 3 directories; every directory passed")
            _, peak = tracemalloc.get_traced_memory()
        finally:
            tracemalloc.stop()
        # The 50 listed blocks and what the script keeps of the summaries take well under a
        # megabyte; 200000 blocks and 200000 summary lines kept would take tens.
        self.assertLess(peak, 2_000_000)
        blocks, _ = times.result()
        self.assertLessEqual(len(blocks), 50)


class RunnerOutputTest(GateTimesTest):
    """The output of the gate's own test runner, whose directories run at the same time and whose
    reports come whole, in the order the directories end, are read as the blocks of the script's
    form."""

    @staticmethod
    def waiting_for(path: Path) -> str:
        """The source of a loop that goes on once `path` exists and fails after two minutes."""
        return (
            f"for _ in range(6000):\n    if os.path.exists({str(path)!r}):\n        break\n"
            "    time.sleep(0.02)\nelse:\n    raise RuntimeError('a file never came')\n"
        )

    def test_directories_that_end_out_of_the_order_of_their_names_each_get_their_own_time(
        self,
    ) -> None:
        repo = self.root / "repo"
        a_started = repo / "a_has_started"
        b_reported = repo / "b_is_reported"
        (repo / "a").mkdir(parents=True)
        (repo / "b").mkdir()
        # a sorts first and ends last: its test waits for the file this test makes once the report of
        # b has come out, so that a ends after b with no pause.
        (repo / "a" / "test_a.py").write_text(
            "import os, time, unittest\n\n\nclass A(unittest.TestCase):\n"
            "    def test_a(self):\n"
            f"        open({str(a_started)!r}, 'w').close()\n"
            + textwrap.indent(self.waiting_for(b_reported), "        "),
            encoding="utf-8",
        )
        # b waits for a to have started before the module is imported, so that b's own time begins
        # after a's, and a's time, which ends after b's report, holds b's.
        (repo / "b" / "test_b.py").write_text(
            "import os, time, unittest\n\n"
            + self.waiting_for(a_started)
            + "\n\nclass B(unittest.TestCase):\n"
            "    def test_b_one(self):\n        pass\n\n"
            "    def test_b_two(self):\n        pass\n",
            encoding="utf-8",
        )
        for command in (["init", "-q"], ["add", "--", "a/test_a.py", "b/test_b.py"]):
            subprocess.run(["git", *command], cwd=repo, check=True, capture_output=True)
        runner = HERE.parent / "gate" / "run_tests.py"
        gate = [sys.executable, "-B", str(runner), "--slowest", "1"]
        with subprocess.Popen(
            [
                sys.executable,
                "-B",
                str(SCRIPT),
                "--output",
                str(self.output),
                "--registry",
                str(self.registry),
                "--",
            ]
            + gate,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=repo,
            env=self.env,
        ) as process:
            lines = []
            for line in process.stdout:
                lines.append(line)
                if line.rstrip(b"\r\n") == b"== b":
                    b_reported.touch()
            stderr = process.stderr.read()
        stdout = b"".join(lines)
        self.assertEqual(0, process.returncode, stdout + stderr)
        # The times as the runner printed them, read here from each report with no help of the script.
        reported = {}
        directory = None
        for line in stdout.decode("utf-8").splitlines():
            if line.startswith("== "):
                directory = line[3:]
            else:
                matched = re.fullmatch(r"Ran \d+ tests? in ([0-9.]+)s", line)
                if matched and directory not in reported:
                    reported[directory] = matched.group(1)
        self.assertEqual({"a", "b"}, set(reported))
        rows = self.rows()
        self.assertEqual(["b", reported["b"]], rows[0][4:])
        self.assertEqual(["a", reported["a"]], rows[1][4:])
        self.assertGreater(float(reported["a"]), float(reported["b"]))


class CapTest(GateTimesTest):
    """A flood of blocks or a very long directory line keeps the record small and readable: no more
    than 50 directories are listed per run (the number the audit reads), a directory cell is cut at
    200 characters, and the cut is written in the record."""

    def flood(self, blocks: int) -> list[str]:
        """A command that prints `blocks` blocks, each with a line of its time, as a loop."""
        return [
            sys.executable,
            "-c",
            "import sys\nfor i in range(int(sys.argv[1])):\n"
            "    sys.stdout.write('== d%d\\nRan 1 test in 0.1s\\n' % i)",
            str(blocks),
        ]

    def test_blocks_beyond_the_fiftieth_are_not_listed_and_a_row_says_how_many(self) -> None:
        result = self.run_gate(self.flood(2000))
        self.assertEqual(0, result.returncode, result.stderr)
        rows = self.rows()
        self.assertEqual(51, len(rows))
        self.assertEqual(["d0", "0.1"], rows[0][4:])
        self.assertEqual(["d49", "0.1"], rows[49][4:])
        # The cut is the last row of the run: the number not listed, and no seconds, never 0.
        self.assertEqual(["… 1950 more directories not listed", "—"], rows[50][4:])
        self.assertEqual(rows[0][:4], rows[50][:4])
        self.assertLess(self.output.stat().st_size, 10000)

    def test_fifty_blocks_are_all_listed_with_no_cut_row(self) -> None:
        result = self.run_gate(self.flood(50))
        self.assertEqual(0, result.returncode, result.stderr)
        rows = self.rows()
        self.assertEqual(50, len(rows))
        self.assertEqual(["d49", "0.1"], rows[49][4:])

    def test_time_after_a_block_not_listed_is_not_given_to_the_last_listed_block(self) -> None:
        # d49 has no Ran line; the Ran line after d50, which is not listed, must not become its time.
        result = self.run_gate(
            [
                sys.executable,
                "-c",
                "import sys\nfor i in range(49):\n"
                "    sys.stdout.write('== d%d\\nRan 1 test in 0.1s\\n' % i)\n"
                "sys.stdout.write('== d49\\n== d50\\nRan 1 test in 9.9s\\n')",
            ]
        )
        self.assertEqual(0, result.returncode, result.stderr)
        rows = self.rows()
        self.assertEqual(["d49", "unknown"], rows[49][4:])
        self.assertEqual(["… 1 more directories not listed", "—"], rows[50][4:])

    def test_a_long_directory_line_is_cut_with_a_mark(self) -> None:
        result = self.run_gate(printed(b"== " + b"x" * 5000 + b"\nRan 1 test in 0.1s\n"))
        self.assertEqual(0, result.returncode, result.stderr)
        cells = self.rows()[0][4:]
        self.assertEqual("x" * 199 + "…", cells[0])
        self.assertEqual("0.1", cells[1])

    def test_a_directory_of_exactly_the_cap_is_kept_whole(self) -> None:
        result = self.run_gate(printed(b"== " + b"y" * 200 + b"\nRan 1 test in 0.1s\n"))
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual("y" * 200, self.rows()[0][4])


class PassThroughTest(GateTimesTest):
    # invariant: command-runner-passes-exit-code
    def test_exit_code_of_the_command_is_passed_on(self) -> None:
        # 2 is also the script's own error code, and 255 the largest code a process gives: each is
        # the command's, passed on unchanged.
        for code in (2, 3, 255):
            with self.subTest(code=code):
                result = self.run_gate(printed(b"== a\nRan 1 test in 0.1s\n", code=code))
                self.assertEqual(code, result.returncode, result.stderr)
                self.assertNotIn(b"Error:", result.stderr)
                self.assertEqual(str(code), self.rows()[-1][1])

    # invariant: command-runner-passes-exit-code
    @unittest.skipIf(os.name == "nt", "Windows gives a killed process no signal number")
    def test_a_command_killed_by_a_signal_gives_128_plus_the_signal_number(self) -> None:
        result = self.run_gate(
            [sys.executable, "-c", "import os, signal; os.kill(os.getpid(), signal.SIGTERM)"]
        )
        self.assertEqual(128 + signal.SIGTERM, result.returncode, result.stderr)
        self.assertEqual(str(128 + signal.SIGTERM), self.rows()[-1][1])

    # invariant: command-runner-passes-exit-code
    def test_a_signal_number_of_the_child_gives_128_plus_it_on_any_platform(self) -> None:
        # The child is replaced by one that reports a signal, since only some platforms give a
        # process a signal number; the script's own mapping of that number is what is checked.
        read_end, write_end = os.pipe()
        os.close(write_end)
        child = mock.Mock()
        child.stdout = os.fdopen(read_end, "rb")
        child.wait.return_value = -signal.SIGTERM
        with mock.patch.object(gate_times.subprocess, "Popen", return_value=child):
            result = self.run_gate_at(NOW, ["gate-command-that-is-replaced"])
        self.assertEqual(128 + signal.SIGTERM, result.returncode, result.stderr)

    def test_output_is_passed_on_unchanged_with_error_output_joined(self) -> None:
        data = "alpha é\r\n== a\nRan 1 test in 0.1s\n|bar \x00 end\n".encode("utf-8")
        result = self.run_gate(
            [
                sys.executable,
                "-c",
                "import sys; sys.stdout.buffer.write(bytes.fromhex(sys.argv[1])); "
                "sys.stdout.flush(); sys.stderr.buffer.write(b'err line\\n'); "
                "sys.stderr.flush()",
                data.hex(),
            ]
        )
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual(data + b"err line\n", result.stdout)

    def test_heading_and_table_header_are_written_once_over_two_runs(self) -> None:
        for _ in range(2):
            result = self.run_gate(printed(b"== a\nRan 1 test in 0.1s\n"))
            self.assertEqual(0, result.returncode, result.stderr)
        text = self.output.read_text(encoding="utf-8")
        self.assertEqual(HEADING, text.split("\n")[0])
        self.assertEqual(1, text.count(HEADING))
        self.assertEqual(1, text.count(TABLE_HEADER))
        self.assertEqual(2, len(self.rows()))
        self.assertNotIn("\r", text)


class RegistryTest(GateTimesTest):
    def test_other_runs_counted_from_the_registry(self) -> None:
        self.registry.mkdir(parents=True)
        made = {
            "stale": f"{NOW - 7 * HOUR}_running_stale.run",  # running, over six hours old: deleted
            "old": f"{NOW - 3 * DAY}_{NOW - 2 * DAY}_old.run",  # ended over a day ago: deleted
            "before": f"{NOW - 120000}_{NOW - 100000}_before.run",  # ended before this run: not counted
            "touching": f"{NOW - 60000}_{NOW}_touching.run",  # ended as this run started: not counted
            "running": f"{NOW - 60000}_running_runa.run",  # still running: counted
            "other": f"{NOW - 60000}_running.run",  # another form: counted for nothing
            "notes": "notes.txt",  # another form: counted for nothing
        }
        for name in made.values():
            (self.registry / name).touch()
        # The command makes the file of a run that ended after this run started: started a minute
        # before it, ended 5 seconds after the instant the clock gives, which is the run's start. The
        # file appears while the command runs, so that a count taken before the command would miss it.
        inside = f"{NOW - 60000}_{NOW + 5000}_inside.run"
        result = self.run_gate_at(
            NOW,
            [
                sys.executable,
                "-c",
                "import os, sys; "
                "open(os.path.join(sys.argv[1], sys.argv[2]), 'w').close(); "
                "sys.stdout.buffer.write(b'== a\\nRan 1 test in 0.1s\\n')",
                str(self.registry),
                inside,
            ],
        )
        self.assertEqual(0, result.returncode, result.stderr)
        rows = self.rows()
        self.assertEqual(NOW_STAMP, rows[0][0])
        self.assertEqual("2", rows[0][3])
        listing = set(os.listdir(self.registry))
        self.assertNotIn(made["stale"], listing)
        self.assertNotIn(made["old"], listing)
        for kept in ("before", "touching", "running", "other", "notes"):
            self.assertIn(made[kept], listing)
        # The run's own file is renamed to its end: an empty file in the ended form, started and
        # ended at the instant the clock gave.
        self.assertIn(inside, listing)
        own = listing - set(made.values()) - {inside}
        self.assertEqual(1, len(own))
        name = own.pop()
        self.assertIsNotNone(ENDED.match(name), name)
        self.assertTrue(name.startswith(f"{NOW}_{NOW}_"), name)
        self.assertEqual(0, os.path.getsize(self.registry / name))

    # invariant: gate-times-refuses-impossible-entry
    def test_files_with_a_time_that_cannot_be_are_deleted_and_count_for_nothing(self) -> None:
        # Malformed: an end more than a minute after the present, an end before the start, a start
        # more than a minute after the present (ended or running). Each is deleted at the start of
        # a run; a valid run still going is counted, and a run that ends 30 seconds ahead is not
        # malformed and stays.
        self.registry.mkdir(parents=True)
        malformed = [
            f"{NOW - 1000}_{NOW + 3 * DAY}_farend.run",
            f"{NOW + DAY}_{NOW + DAY + 1000}_farstart.run",
            f"{NOW - 1000}_{NOW - 5000}_reversed.run",
            f"{NOW + DAY}_running_farrunning.run",
            f"{NOW - 1000}_{NOW + 2 * HOUR}_farend2.run",
        ]
        kept = [f"{NOW - 60000}_running_valid.run", f"{NOW - 1000}_{NOW + 30000}_nearend.run"]
        for name in malformed + kept:
            (self.registry / name).touch()
        result = self.run_gate_at(NOW, printed(b"== a\nRan 1 test in 0.1s\n"))
        self.assertEqual(0, result.returncode, result.stderr)
        listing = set(os.listdir(self.registry))
        for name in malformed:
            self.assertNotIn(name, listing)
        for name in kept:
            self.assertIn(name, listing)
        # Counted: the valid running one, and the file that ends 30 seconds ahead (its interval
        # met this run's); the malformed ones count for nothing.
        self.assertEqual("2", self.rows()[0][3])

    # invariant: gate-times-refuses-impossible-entry
    def test_a_malformed_file_that_cannot_be_deleted_still_counts_for_nothing(self) -> None:
        # A directory in the place of a file cannot be unlinked: a warning, and no count.
        self.registry.mkdir(parents=True)
        stuck = self.registry / f"{NOW - 1000}_{NOW + 3 * DAY}_stuck.run"
        stuck.mkdir()
        result = self.run_gate_at(NOW, printed(b"== a\nRan 1 test in 0.1s\n"))
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual("0", self.rows()[0][3])

    def test_unusable_registry_gives_unknown_and_the_gate_still_runs(self) -> None:
        self.registry.write_text("not a folder", encoding="utf-8")
        marker = self.root / "ran.txt"
        result = self.run_gate(
            [
                sys.executable,
                "-c",
                "import sys; open(sys.argv[1], 'w').close(); "
                "sys.stdout.buffer.write(b'== a\\nRan 1 test in 0.1s\\n')",
                str(marker),
            ]
        )
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertTrue(marker.exists())
        self.assertTrue(result.stderr.decode("utf-8", errors="replace").startswith("Warning:"))
        self.assertEqual("unknown", self.rows()[0][3])

    def test_default_registry_is_under_the_home_directory(self) -> None:
        options = ["--output", str(self.output)]
        result = self.run_gate(printed(b"== a\nRan 1 test in 0.1s\n"), options=options)
        self.assertEqual(0, result.returncode, result.stderr)
        folder = self.root / "home" / ".the-way" / "gate_runs"
        files = os.listdir(folder)
        self.assertEqual(1, len(files))
        self.assertIsNotNone(ENDED.match(files[0]), files[0])
        self.assertEqual("0", self.rows()[0][3])


class ErrorTest(GateTimesTest):
    def assertError(self, result: subprocess.CompletedProcess) -> None:
        self.assertEqual(2, result.returncode, result.stdout)
        first = result.stderr.decode("utf-8", errors="replace").split("\n")[0]
        self.assertTrue(first.startswith("Error: gate_times.py:"), first)

    def test_no_command_is_an_error_before_anything_runs(self) -> None:
        result = self.run_gate([], end_options=False)
        self.assertError(result)
        self.assertFalse(self.output.exists())

    def test_no_output_is_an_error_before_the_command_starts(self) -> None:
        marker = self.root / "ran.txt"
        result = self.run_gate(
            [sys.executable, "-c", "open(sys.argv[1], 'w').close()", str(marker)],
            options=["--registry", str(self.registry)],
        )
        self.assertError(result)
        self.assertFalse(marker.exists())

    def test_output_that_cannot_be_appended_is_an_error_before_the_command_starts(self) -> None:
        folder = self.root / "a_folder"
        folder.mkdir()
        marker = self.root / "ran.txt"
        result = self.run_gate(
            [sys.executable, "-c", "open(sys.argv[1], 'w').close()", str(marker)],
            options=["--output", str(folder), "--registry", str(self.registry)],
        )
        self.assertError(result)
        self.assertFalse(marker.exists())

    def test_command_that_cannot_start_is_an_error(self) -> None:
        result = self.run_gate(["gate-command-that-does-not-exist-anywhere"])
        self.assertError(result)


class TextTest(GateTimesTest):
    def test_script_imports_no_repository_module_and_starts_no_other_program(self) -> None:
        tree = ast.parse(SCRIPT.read_text(encoding="utf-8"))
        imported = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported.update(alias.name.split(".")[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom):
                self.assertEqual(0, node.level)
                imported.add(node.module.split(".")[0])
        self.assertTrue(imported <= set(sys.stdlib_module_names), imported)
        started = []
        for node in ast.walk(tree):
            if (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and isinstance(node.func.value, ast.Name)
            ):
                owner, name = node.func.value.id, node.func.attr
                if owner == "subprocess" or (
                    owner == "os"
                    and name.startswith(("system", "popen", "exec", "spawn", "posix_spawn"))
                ):
                    started.append(f"{owner}.{name}")
        self.assertEqual(["subprocess.Popen"], started)


if __name__ == "__main__":
    unittest.main()
