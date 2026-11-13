"""Tests of task-cycle/gate_times.py on made-up gate output: each command here prints the lines the gate
prints, never the real gate.

The expected rows and counts are worked out by hand from the output written here, not by the script.
"""

from __future__ import annotations

import ast
import os
import re
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPT = HERE / "gate_times.py"

HEADING = "# Gate runs of the cycle"
TABLE_HEADER = ("| Started (UTC) | Exit code | Total seconds | Other gate runs at the same time "
                "| Directory | Directory seconds |")
STARTED = re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}$")
TOTAL = re.compile(r"^\d+\.\d{3}$")
ENDED = re.compile(r"^(\d+)_(\d+)_([A-Za-z0-9]+)\.run$")
HOUR = 3600 * 1000
DAY = 24 * HOUR


def now_ms() -> int:
    return time.time_ns() // 1_000_000


def printed(text: bytes, code: int = 0) -> list[str]:
    """A command that writes `text` to its output exactly, as bytes, and exits with `code`. The text
    comes in hex in the arguments, so that the code of the command stays a literal."""
    return [sys.executable, "-c",
            "import sys; sys.stdout.buffer.write(bytes.fromhex(sys.argv[1])); sys.exit(int(sys.argv[2]))",
            text.hex(), str(code)]


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

    def run_gate(self, command: list[str], options: list[str] | None = None,
                 end_options: bool = True) -> subprocess.CompletedProcess:
        """Runs the script with the command after `--`, from the folder of the test."""
        if options is None:
            options = ["--output", str(self.output), "--registry", str(self.registry)]
        args = [sys.executable, "-B", str(SCRIPT), *options]
        if end_options:
            args.append("--")
        return subprocess.run([*args, *command], capture_output=True, cwd=self.root, env=self.env)

    def rows(self) -> list[list[str]]:
        """The rows of the table in the output file, each as its cells."""
        text = self.output.read_bytes().decode("utf-8")
        body = [line for line in text.split("\n")
                if line.startswith("| ") and line != TABLE_HEADER and not line.startswith("| ---")]
        return [[cell.strip() for cell in line.strip("|").split("|")] for line in body]


class RowsTest(GateTimesTest):

    def test_rows_follow_the_order_the_gate_printed_them(self) -> None:
        # Made-up output with the directories out of alphabetical order.
        result = self.run_gate(printed(b"== zeta\nRan 3 tests in 0.010s\n\nOK\n"
                                       b"== alpha\nRan 1 test in 0.002s\n\nOK\n"))
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
        result = self.run_gate(printed(b"== first\nno timing here\n== second\nRan 2 tests in 0.5s\n"))
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
        result = self.run_gate(printed(b"Ran 9 tests in 9.9s\nstray\n== only\nRan 1 test in 0.100s\n"))
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


class CapTest(GateTimesTest):
    """A flood of blocks or a very long directory line keeps the record small and readable: no more
    than 50 directories are listed per run (the number the audit reads), a directory cell is cut at
    200 characters, and the cut is written in the record."""

    def flood(self, blocks: int) -> list[str]:
        """A command that prints `blocks` blocks, each with a line of its time, as a loop."""
        return [sys.executable, "-c",
                "import sys\nfor i in range(int(sys.argv[1])):\n"
                "    sys.stdout.write('== d%d\\nRan 1 test in 0.1s\\n' % i)", str(blocks)]

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
        result = self.run_gate([sys.executable, "-c",
                                "import sys\nfor i in range(49):\n"
                                "    sys.stdout.write('== d%d\\nRan 1 test in 0.1s\\n' % i)\n"
                                "sys.stdout.write('== d49\\n== d50\\nRan 1 test in 9.9s\\n')"])
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

    def test_exit_code_of_the_command_is_passed_on(self) -> None:
        result = self.run_gate(printed(b"== a\nRan 1 test in 0.1s\n", code=3))
        self.assertEqual(3, result.returncode, result.stderr)
        self.assertNotIn(b"Error:", result.stderr)
        self.assertEqual("3", self.rows()[0][1])

    def test_output_is_passed_on_unchanged_with_error_output_joined(self) -> None:
        data = "alpha é\r\n== a\nRan 1 test in 0.1s\n|bar \x00 end\n".encode("utf-8")
        result = self.run_gate([sys.executable, "-c",
                                "import sys; sys.stdout.buffer.write(bytes.fromhex(sys.argv[1])); "
                                "sys.stdout.flush(); sys.stderr.buffer.write(b'err line\\n'); "
                                "sys.stderr.flush()", data.hex()])
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
        t0 = now_ms()
        made = {
            "stale": f"{t0 - 7 * HOUR}_running_stale.run",   # running, over six hours old: deleted
            "old": f"{t0 - 3 * DAY}_{t0 - 2 * DAY}_old.run",  # ended over a day ago: deleted
            "before": f"{t0 - 120000}_{t0 - 100000}_before.run",  # ended before this run: not counted
            "running": f"{t0 - 60000}_running_runa.run",     # still running: counted
            "other": f"{t0 - 60000}_running.run",            # another form: counted for nothing
            "notes": "notes.txt",                             # another form: counted for nothing
        }
        for name in made.values():
            (self.registry / name).touch()
        # The command makes the entry of a run that ended inside this run: started a minute before
        # it, ended after this run started, which it did before the command began.
        result = self.run_gate([sys.executable, "-c",
                                "import os, sys, time; time.sleep(0.1); "
                                "now = time.time_ns() // 1000000; "
                                "open(os.path.join(sys.argv[1], '{}_{}_inside.run'.format("
                                "now - 60000, now)), 'w').close(); "
                                "sys.stdout.buffer.write(b'== a\\nRan 1 test in 0.1s\\n')",
                                str(self.registry)])
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual("2", self.rows()[0][3])
        listing = set(os.listdir(self.registry))
        self.assertNotIn(made["stale"], listing)
        self.assertNotIn(made["old"], listing)
        for kept in ("before", "running", "other", "notes"):
            self.assertIn(made[kept], listing)
        # The run's own entry is renamed to its end: an empty file in the ended form.
        own = listing - set(made.values()) - {next(n for n in listing if n.endswith("_inside.run"))}
        self.assertEqual(1, len(own))
        name = own.pop()
        self.assertIsNotNone(ENDED.match(name), name)
        self.assertEqual(0, os.path.getsize(self.registry / name))

    def test_entries_with_a_time_that_cannot_be_are_deleted_and_count_for_nothing(self) -> None:
        # Malformed: an end more than a minute after the present, an end before the start, a start
        # more than a minute after the present (ended or running). Each is deleted at the start of
        # a run; a valid run still going is counted, and a run that ends 30 seconds ahead is not
        # malformed and stays.
        self.registry.mkdir(parents=True)
        t0 = now_ms()
        malformed = [f"{t0 - 1000}_{t0 + 3 * DAY}_farend.run",
                     f"{t0 + DAY}_{t0 + DAY + 1000}_farstart.run",
                     f"{t0 - 1000}_{t0 - 5000}_reversed.run",
                     f"{t0 + DAY}_running_farrunning.run",
                     f"{t0 - 1000}_{t0 + 2 * HOUR}_farend2.run"]
        kept = [f"{t0 - 60000}_running_valid.run", f"{t0 - 1000}_{t0 + 30000}_nearend.run"]
        for name in malformed + kept:
            (self.registry / name).touch()
        result = self.run_gate(printed(b"== a\nRan 1 test in 0.1s\n"))
        self.assertEqual(0, result.returncode, result.stderr)
        listing = set(os.listdir(self.registry))
        for name in malformed:
            self.assertNotIn(name, listing)
        for name in kept:
            self.assertIn(name, listing)
        # Counted: the valid running one, and the entry that ends 30 seconds ahead (its interval
        # met this run's); the malformed ones count for nothing.
        self.assertEqual("2", self.rows()[0][3])

    def test_a_malformed_entry_that_cannot_be_deleted_still_counts_for_nothing(self) -> None:
        # A directory in the place of a file cannot be unlinked: a warning, and no count.
        self.registry.mkdir(parents=True)
        t0 = now_ms()
        stuck = self.registry / f"{t0 - 1000}_{t0 + 3 * DAY}_stuck.run"
        stuck.mkdir()
        result = self.run_gate(printed(b"== a\nRan 1 test in 0.1s\n"))
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual("0", self.rows()[0][3])

    def test_unusable_registry_gives_unknown_and_the_gate_still_runs(self) -> None:
        self.registry.write_text("not a folder", encoding="utf-8")
        marker = self.root / "ran.txt"
        result = self.run_gate([sys.executable, "-c",
                                "import sys; open(sys.argv[1], 'w').close(); "
                                "sys.stdout.buffer.write(b'== a\\nRan 1 test in 0.1s\\n')",
                                str(marker)])
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertTrue(marker.exists())
        self.assertTrue(result.stderr.decode("utf-8", errors="replace").startswith("Warning:"))
        self.assertEqual("unknown", self.rows()[0][3])

    def test_default_registry_is_under_the_home_directory(self) -> None:
        options = ["--output", str(self.output)]
        result = self.run_gate(printed(b"== a\nRan 1 test in 0.1s\n"), options=options)
        self.assertEqual(0, result.returncode, result.stderr)
        folder = self.root / "home" / ".the-way" / "gate_runs"
        entries = os.listdir(folder)
        self.assertEqual(1, len(entries))
        self.assertIsNotNone(ENDED.match(entries[0]), entries[0])
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
        result = self.run_gate([sys.executable, "-c", "open(sys.argv[1], 'w').close()", str(marker)],
                               options=["--registry", str(self.registry)])
        self.assertError(result)
        self.assertFalse(marker.exists())

    def test_output_that_cannot_be_appended_is_an_error_before_the_command_starts(self) -> None:
        folder = self.root / "a_folder"
        folder.mkdir()
        marker = self.root / "ran.txt"
        result = self.run_gate([sys.executable, "-c", "open(sys.argv[1], 'w').close()", str(marker)],
                               options=["--output", str(folder), "--registry", str(self.registry)])
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
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) \
                    and isinstance(node.func.value, ast.Name):
                owner, name = node.func.value.id, node.func.attr
                if owner == "subprocess" or (owner == "os" and name.startswith(
                        ("system", "popen", "exec", "spawn", "posix_spawn"))):
                    started.append(f"{owner}.{name}")
        self.assertEqual(["subprocess.Popen"], started)


if __name__ == "__main__":
    unittest.main()
