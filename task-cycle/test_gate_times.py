"""Tests of task-cycle/gate_times.py on made-up gate output: each command here prints the lines the gate
prints, never the real gate.

The expected rows and counts are worked out by hand from the output written here, not by the script.
"""

from __future__ import annotations

import ast
import io
import os
import re
import subprocess
import sys
import tempfile
import textwrap
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parent
SCRIPT = HERE / "gate_times.py"

sys.path.insert(0, str(HERE))

import gate_times

HEADING = "# Gate runs of the cycle"
TABLE_HEADER = ("| Started (UTC) | Exit code | Total seconds | Other gate runs at the same time "
                "| Directory | Directory seconds |")
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

    def run_gate_at(self, now: int, command: list[str]) -> subprocess.CompletedProcess:
        """Runs the script's `main` in this process with its clock fixed at `now` milliseconds, so
        that the run starts and ends at that instant; the registry and the output are the ones of the
        test. The home directory is the test's own, as for a run of the script in a process."""
        stdout = io.TextIOWrapper(io.BytesIO(), encoding="utf-8")
        stderr = io.StringIO()
        arguments = ["--output", str(self.output), "--registry", str(self.registry), "--", *command]
        with (mock.patch.object(gate_times, "now_ms", return_value=now),
              mock.patch.dict(os.environ, self.env),
              redirect_stdout(stdout), redirect_stderr(stderr)):
            code = gate_times.main(arguments)
        stdout.flush()
        return subprocess.CompletedProcess(arguments, code, stdout.buffer.getvalue(),
                                           stderr.getvalue().encode("utf-8"))

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


class RunnerOutputTest(GateTimesTest):
    """The output of the gate's own test runner, whose directories run at the same time and whose
    reports come whole, in the order the directories end, are read as the blocks of the script's
    form."""

    @staticmethod
    def waiting_for(path: Path) -> str:
        """The source of a loop that goes on once `path` exists and fails after two minutes."""
        return (f"for _ in range(6000):\n    if os.path.exists({str(path)!r}):\n        break\n"
                "    time.sleep(0.02)\nelse:\n    raise RuntimeError('a file never came')\n")

    def test_directories_that_end_out_of_the_order_of_their_names_each_get_their_own_time(self) -> None:
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
            + textwrap.indent(self.waiting_for(b_reported), "        "), encoding="utf-8")
        # b waits for a to have started before the module is imported, so that b's own time begins
        # after a's, and a's time, which ends after b's report, holds b's.
        (repo / "b" / "test_b.py").write_text(
            "import os, time, unittest\n\n"
            + self.waiting_for(a_started)
            + "\n\nclass B(unittest.TestCase):\n"
            "    def test_b_one(self):\n        pass\n\n"
            "    def test_b_two(self):\n        pass\n", encoding="utf-8")
        for command in (["init", "-q"], ["add", "--", "a/test_a.py", "b/test_b.py"]):
            subprocess.run(["git", *command], cwd=repo, check=True, capture_output=True)
        runner = HERE.parent / "gate" / "run_tests.py"
        gate = [sys.executable, "-B", str(runner), "--slowest", "1"]
        with subprocess.Popen(
                [sys.executable, "-B", str(SCRIPT), "--output", str(self.output), "--registry",
                 str(self.registry), "--"] + gate, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                cwd=repo, env=self.env) as process:
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
        made = {
            "stale": f"{NOW - 7 * HOUR}_running_stale.run",   # running, over six hours old: deleted
            "old": f"{NOW - 3 * DAY}_{NOW - 2 * DAY}_old.run",  # ended over a day ago: deleted
            "before": f"{NOW - 120000}_{NOW - 100000}_before.run",  # ended before this run: not counted
            "touching": f"{NOW - 60000}_{NOW}_touching.run",  # ended as this run started: not counted
            "running": f"{NOW - 60000}_running_runa.run",     # still running: counted
            "other": f"{NOW - 60000}_running.run",            # another form: counted for nothing
            "notes": "notes.txt",                              # another form: counted for nothing
        }
        for name in made.values():
            (self.registry / name).touch()
        # The command makes the entry of a run that ended after this run started: started a minute
        # before it, ended 5 seconds after the instant the clock gives, which is the run's start. The
        # entry appears while the command runs, so that a count taken before the command would miss it.
        inside = f"{NOW - 60000}_{NOW + 5000}_inside.run"
        result = self.run_gate_at(NOW, [sys.executable, "-c",
                                        "import os, sys; "
                                        "open(os.path.join(sys.argv[1], sys.argv[2]), 'w').close(); "
                                        "sys.stdout.buffer.write(b'== a\\nRan 1 test in 0.1s\\n')",
                                        str(self.registry), inside])
        self.assertEqual(0, result.returncode, result.stderr)
        rows = self.rows()
        self.assertEqual(NOW_STAMP, rows[0][0])
        self.assertEqual("2", rows[0][3])
        listing = set(os.listdir(self.registry))
        self.assertNotIn(made["stale"], listing)
        self.assertNotIn(made["old"], listing)
        for kept in ("before", "touching", "running", "other", "notes"):
            self.assertIn(made[kept], listing)
        # The run's own entry is renamed to its end: an empty file in the ended form, started and
        # ended at the instant the clock gave.
        self.assertIn(inside, listing)
        own = listing - set(made.values()) - {inside}
        self.assertEqual(1, len(own))
        name = own.pop()
        self.assertIsNotNone(ENDED.match(name), name)
        self.assertTrue(name.startswith(f"{NOW}_{NOW}_"), name)
        self.assertEqual(0, os.path.getsize(self.registry / name))

    # invariant: gate-times-refuses-impossible-entry
    def test_entries_with_a_time_that_cannot_be_are_deleted_and_count_for_nothing(self) -> None:
        # Malformed: an end more than a minute after the present, an end before the start, a start
        # more than a minute after the present (ended or running). Each is deleted at the start of
        # a run; a valid run still going is counted, and a run that ends 30 seconds ahead is not
        # malformed and stays.
        self.registry.mkdir(parents=True)
        malformed = [f"{NOW - 1000}_{NOW + 3 * DAY}_farend.run",
                     f"{NOW + DAY}_{NOW + DAY + 1000}_farstart.run",
                     f"{NOW - 1000}_{NOW - 5000}_reversed.run",
                     f"{NOW + DAY}_running_farrunning.run",
                     f"{NOW - 1000}_{NOW + 2 * HOUR}_farend2.run"]
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
        # Counted: the valid running one, and the entry that ends 30 seconds ahead (its interval
        # met this run's); the malformed ones count for nothing.
        self.assertEqual("2", self.rows()[0][3])

    def test_a_malformed_entry_that_cannot_be_deleted_still_counts_for_nothing(self) -> None:
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
