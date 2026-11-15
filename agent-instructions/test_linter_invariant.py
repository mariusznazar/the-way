"""Tests of the linter that checks the Python code of the-way (WAY-380, WAY-381).

The first test fails where the pinned Ruff cannot be found or cannot run, so that a missing Ruff
turns the gate red. The second test is the test of the invariant `ruff-blocking-rules`: it runs the
same Ruff over every part with Python code and fails while a file breaks a blocking rule. That
invariant reads `Violated: yes` (WAY-51, WAY-205), so the second test is marked as an expected
failure; it is kept apart from the first so that a missing Ruff cannot pass as the expected
failure. The change in which the last report is cleaned removes the marking and the mark of the
invariant: an expected failure that passes ends the run as an unexpected success.

Ruff comes from the environment `.runs/quality-venv` of the main checkout of the repository, found
through the common directory of git, so that one installation serves every working directory of
the repository (README, "Installing the linter"). The tests check no version of their own: Ruff
refuses to run in a version other than the one `required-version` of `ruff.toml` names.

Run from the root of the-way: python -B gate/run_tests.py agent-instructions
"""

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent.parent
# The parts with Python code, as the directories that hold it.
PARTS = ("agent-instructions", "elements", "gate", "installation", "instruction-files",
         "process-audit", "product-guidelines", "project-level", "relation-model", "task-cycle")
CLEAN_FILE = '"""A file that breaks no rule of the linter."""\n\nVALUE = 1\n'


def main_checkout() -> Path:
    """The main checkout of the repository this file stands in, found through the common
    directory of git, which is the same from a working directory of a worktree."""
    done = subprocess.run(["git", "rev-parse", "--git-common-dir"], cwd=ROOT, check=True,
                          capture_output=True, text=True, encoding="utf-8")
    # The common directory is relative to ROOT in a main checkout and absolute in a worktree.
    return (ROOT / done.stdout.strip()).resolve().parent


def ruff_program() -> Path:
    """Where the installed Ruff stands in the environment of the main checkout."""
    relative = "Scripts/ruff.exe" if os.name == "nt" else "bin/ruff"
    return main_checkout() / ".runs" / "quality-venv" / relative


def run_ruff(*arguments: str, cwd: Path) -> subprocess.CompletedProcess[str]:
    """Runs the pinned Ruff with the configuration of the repository and no cache."""
    program = ruff_program()
    if not program.is_file():
        raise AssertionError(f"Ruff is not installed at {program}; install it as the README of "
                             "the-way tells under \"Installing the linter\"")
    return subprocess.run([str(program), "check", "--config", str(ROOT / "ruff.toml"),
                           "--no-cache", "--output-format", "concise", *arguments],
                          cwd=cwd, capture_output=True, text=True, encoding="utf-8")


class Linter(unittest.TestCase):
    def test_the_pinned_ruff_runs_and_passes_a_clean_file(self) -> None:
        with tempfile.TemporaryDirectory(prefix="the-way-linter-") as directory:
            clean = Path(directory) / "clean.py"
            clean.write_text(CLEAN_FILE, encoding="utf-8")
            done = run_ruff(str(clean), cwd=Path(directory))
        self.assertEqual(done.returncode, 0, done.stdout + done.stderr)

    def test_every_python_file_git_tracks_lies_in_a_part_the_check_reads(self) -> None:
        done = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, check=True,
                              capture_output=True, text=True, encoding="utf-8")
        outside = [name for name in done.stdout.split("\0")
                   if name.endswith(".py") and name.split("/")[0] not in PARTS]
        self.assertEqual(outside, [], "a tracked Python file lies in no directory of PARTS: add "
                         "its directory to PARTS and to the Scope of WAY-379")

    @unittest.expectedFailure
    def test_no_file_of_a_part_breaks_a_blocking_rule(self) -> None:
        # invariant: ruff-blocking-rules
        done = run_ruff("--ignore-noqa", *PARTS, cwd=ROOT)
        self.assertEqual(done.returncode, 0, done.stdout + done.stderr)


if __name__ == "__main__":
    unittest.main()
