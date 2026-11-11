"""Tests of task-cycle/tracked_private_paths_check.py on git repositories made up for the tests.

Each test runs the command as a product does, as a process started in the root of a repository
whose invariants file holds the invariant given to it. The expected lines are written out here. A
path or a note link written in this file would be a finding of the invariant itself, so every
fixture is assembled from pieces, and a backslash is written as `BS`.
"""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMMAND = HERE / "tracked_private_paths_check.py"
BS = chr(92)
INVARIANT = "tracked-file-private-paths"
DRIVE = "D" + ":/"
GIT_BASH = "/" + "c/work/alice"
OPEN, CLOSE = "[" + "[", "]" + "]"


def invariants_file(sentence: str, others: str = "") -> str:
    return ("# Invariants\n\n" + others + f"## {INVARIANT}\n\n{sentence}\n\n- **Method:** test\n"
            "- **Rests on:** none\n\n## after\n\nAnother sentence with `names.py` in it.\n")


class CommandTest(unittest.TestCase):
    def setUp(self) -> None:
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        subprocess.run(["git", "init", "-q"], cwd=self.root, check=True)

    def track(self, name: str, text: str) -> None:
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="")
        subprocess.run(["git", "add", "--", name], cwd=self.root, check=True)

    def invariant(self, sentence: str, others: str = "") -> None:
        self.track("foundations/invariants.md", invariants_file(sentence, others))

    def run_command(self, *arguments: str, cwd: Path | None = None) -> tuple[int, str, str]:
        run = subprocess.run([sys.executable, "-B", str(COMMAND), *arguments],
                             cwd=cwd or self.root, capture_output=True, encoding="utf-8")
        return run.returncode, run.stdout, run.stderr

    def listing(self, out: str) -> list[str]:
        return [line for line in out.splitlines() if not line.startswith("checked: ")]

    def test_a_clean_repository_exits_zero_with_only_the_summary(self) -> None:
        self.invariant("No file git tracks contains an absolute path or a note link.")
        self.track("src/a.py", "x = 1\n")
        code, out, err = self.run_command(INVARIANT)
        self.assertEqual((code, err), (0, ""))
        self.assertEqual(out, "checked: 2 files, 0 listed\n")

    def test_a_path_is_listed_with_its_file_and_line_and_exit_one(self) -> None:
        self.invariant("No file git tracks contains a path.")
        self.track("notes/plan.md", "first\nsecond\nsee " + DRIVE + "work/proj now\n")
        code, out, err = self.run_command(INVARIANT)
        self.assertEqual((code, err), (1, ""))
        self.assertEqual(self.listing(out), ["notes/plan.md:3: absolute path: " + DRIVE + "work/proj"])
        self.assertEqual(out.splitlines()[-1], "checked: 2 files, 1 listed")

    def test_a_path_is_listed_in_a_file_of_any_kind(self) -> None:
        self.invariant("No file git tracks contains a path.")
        self.track("deploy/run", "dir=" + DRIVE + "srv/x\n")
        self.track("src/a.py", "d = '" + DRIVE + "srv/y'\n")
        _, out, _ = self.run_command(INVARIANT)
        self.assertEqual(self.listing(out), ["deploy/run:1: absolute path: " + DRIVE + "srv/x",
                                             "src/a.py:1: absolute path: " + DRIVE + "srv/y"])

    def test_a_note_link_is_listed_in_a_markdown_file_only(self) -> None:
        self.invariant("No file git tracks contains a link.")
        link = OPEN + "Meeting notes" + CLOSE
        self.track("a.md", "see " + link + "\n")
        self.track("B.MD", "see " + link + "\n")
        self.track("deploy/run", "if " + OPEN + ": -f x " + CLOSE + "; then\n")
        self.track("src/a.js", "const rows = " + OPEN + "address, 1" + CLOSE + ";\n")
        self.track("src/b.py", "x = " + OPEN + "a, b" + CLOSE + "\nnote = '" + link + "'\n")
        self.track("report.txt", "see " + link + "\n")
        _, out, _ = self.run_command(INVARIANT)
        self.assertEqual(self.listing(out), ["B.MD:1: note link: " + link,
                                             "a.md:1: note link: " + link])

    def test_a_character_class_of_the_shell_in_a_markdown_file_is_no_note_link(self) -> None:
        self.invariant("No file git tracks contains a link.")
        cls = OPEN + ":alpha:" + CLOSE
        link = OPEN + "Meeting notes" + CLOSE
        self.track("a.md", "run `grep -E \"^" + OPEN + ":space:" + CLOSE + "*#\" f`, see " + link + "\n")
        self.track("b.md", "only the class " + cls + " here\n")
        _, out, _ = self.run_command(INVARIANT)
        self.assertEqual(self.listing(out), ["a.md:1: note link: " + link])

    def test_the_files_the_sentence_names_are_skipped_and_others_are_not(self) -> None:
        self.invariant("No file git tracks, other than `listed.py` and `tests/test_listed.py`, "
                       "contains a path.")
        self.track("listed.py", "p = '" + DRIVE + "dir'\n")
        self.track("tests/test_listed.py", "p = '" + DRIVE + "dir'\n")
        self.track("other.py", "p = '" + DRIVE + "dir'\n")
        code, out, _ = self.run_command(INVARIANT)
        self.assertEqual(code, 1)
        self.assertEqual(self.listing(out), ["other.py:1: absolute path: " + DRIVE + "dir"])
        self.assertEqual(out.splitlines()[-1], "checked: 2 files, 1 listed")

    def test_a_sentence_that_runs_over_several_lines_names_its_files_from_all_of_them(self) -> None:
        self.invariant("No file git tracks, other than `first.py`,\n`second.py` and\n"
                       "`third.py`, contains a path.")
        for name in ("first.py", "second.py", "third.py"):
            self.track(name, "p = '" + DRIVE + "dir'\n")
        code, out, _ = self.run_command(INVARIANT)
        self.assertEqual((code, self.listing(out)), (0, []))

    def test_only_the_sentence_of_the_named_invariant_names_files(self) -> None:
        others = "## other-invariant\n\nNo file, other than `skipped.py`, is wrong.\n\n"
        self.invariant("No file git tracks contains a path.", others)
        self.track("skipped.py", "p = '" + DRIVE + "dir'\n")
        self.track("names.py", "p = '" + DRIVE + "dir'\n")
        code, out, _ = self.run_command(INVARIANT)
        self.assertEqual(code, 1)
        self.assertEqual(self.listing(out), ["names.py:1: absolute path: " + DRIVE + "dir",
                                             "skipped.py:1: absolute path: " + DRIVE + "dir"])

    def test_the_command_reads_the_repository_it_is_started_in_from_a_subdirectory(self) -> None:
        self.invariant("No file git tracks, other than `skip.py`, contains a path.")
        self.track("skip.py", "p = '" + DRIVE + "dir'\n")
        self.track("deep/er/a.py", "p = '" + DRIVE + "dir'\n")
        code, out, _ = self.run_command(INVARIANT, cwd=self.root / "deep" / "er")
        self.assertEqual(code, 1)
        self.assertEqual(self.listing(out), ["deep/er/a.py:1: absolute path: " + DRIVE + "dir"])

    def test_a_file_git_lists_but_the_tree_lacks_is_not_read(self) -> None:
        self.invariant("No file git tracks contains a path.")
        self.track("gone.md", "text\n")
        (self.root / "gone.md").unlink()
        code, out, _ = self.run_command(INVARIANT)
        self.assertEqual((code, out), (0, "checked: 1 files, 0 listed\n"))

    def test_a_binary_file_is_counted_and_not_read(self) -> None:
        self.invariant("No file git tracks contains a path.")
        (self.root / "shot.png").write_bytes(b"\x89PNG\0\0" + DRIVE.encode() + b"x\0")
        subprocess.run(["git", "add", "--", "shot.png"], cwd=self.root, check=True)
        code, out, _ = self.run_command(INVARIANT)
        self.assertEqual((code, out), (0, "checked: 1 files, 0 listed, 1 binary files not read\n"))

    def test_the_shapes_of_a_product_with_code_give_only_the_real_findings(self) -> None:
        # The five shapes of false hits of code, the paths and the links a product really has.
        self.invariant("No file git tracks, other than `tests/support.py`, contains a path.")
        link = OPEN + "Notatka" + CLOSE
        self.track("web/form.js", "const m = new Map(" + OPEN + OPEN + "address, check(address)"
                   + CLOSE + CLOSE + ");\n")
        self.track("deploy/run", "while " + OPEN + OPEN + ":space:" + CLOSE + CLOSE + "; do :; done\n")
        self.track("foundations/facts.md", "slot p." + OPEN + "PromiseResult" + CLOSE + " of a promise\n")
        self.track("src/wait.py", 'print(f"... within {limit} s:' + BS + 'n")\n'
                   'print("done s:' + BS + 'n' + BS + 'n")\n'
                   "pattern = re.compile(r'" + BS + "d" + BS + "d:" + BS + "d" + BS + "d')\n")
        self.track("src/real.py", "root = r'C:" + BS + "new" + BS + "dir'\n"
                   "line = 'wait s:" + BS + "nWynik'\n")
        self.track("tests/support.py", "git_bash = '" + GIT_BASH + "'\nwin = 'C:" + BS + "x'\n")
        self.track("docs/note.md", "zob." + link + " i " + link + "\n")
        code, out, _ = self.run_command(INVARIANT)
        self.assertEqual(code, 1)
        self.assertEqual(self.listing(out), [
            "docs/note.md:1: note link: " + link,
            "src/real.py:1: absolute path: C:" + BS + "new" + BS + "dir",
            "src/real.py:2: absolute path: s:" + BS + "nWynik"])

    def test_a_posix_example_of_a_shell_is_listed_unless_its_file_is_named(self) -> None:
        self.invariant("No file git tracks, other than `tests/support.py`, contains a path.")
        self.track("tests/support.py", '"""Example: ' + GIT_BASH + '."""\n')
        self.track("tests/other.py", '"""Example: ' + GIT_BASH + '."""\n')
        _, out, _ = self.run_command(INVARIANT)
        self.assertEqual(self.listing(out), ["tests/other.py:1: absolute path: " + GIT_BASH])

    def test_a_missing_or_surplus_argument_exits_two(self) -> None:
        self.invariant("No file git tracks contains a path.")
        for arguments in ((), (INVARIANT, "extra"), ("--help",)):
            code, out, err = self.run_command(*arguments)
            self.assertEqual((code, out), (2, ""), arguments)
            self.assertTrue(err.startswith("Error: "), err)

    def test_an_invariant_the_file_does_not_hold_exits_two(self) -> None:
        self.invariant("No file git tracks contains a path.")
        code, out, err = self.run_command("tracked-file")
        self.assertEqual((code, out), (2, ""))
        self.assertTrue(err.startswith("Error: ") and "tracked-file" in err, err)

    def test_a_repository_without_an_invariants_file_exits_two(self) -> None:
        self.track("a.py", "x = 1\n")
        code, out, err = self.run_command(INVARIANT)
        self.assertEqual((code, out), (2, ""))
        self.assertTrue(err.startswith("Error: "), err)

    def test_a_sentence_that_names_a_file_git_does_not_track_exits_two(self) -> None:
        self.invariant("No file git tracks, other than `gone.py`, contains a path.")
        code, out, err = self.run_command(INVARIANT)
        self.assertEqual((code, out), (2, ""))
        self.assertTrue(err.startswith("Error: ") and "gone.py" in err, err)

    def test_a_directory_outside_every_repository_exits_two(self) -> None:
        with tempfile.TemporaryDirectory() as outside:
            code, out, err = self.run_command(INVARIANT, cwd=Path(outside))
        self.assertEqual((code, out), (2, ""))
        self.assertTrue(err.startswith("Error: "), err)

    def test_a_file_that_is_not_utf8_exits_two_with_nothing_listed(self) -> None:
        self.invariant("No file git tracks contains a path.")
        (self.root / "late.txt").write_bytes("zażółć".encode("cp1250"))
        subprocess.run(["git", "add", "--", "late.txt"], cwd=self.root, check=True)
        code, out, err = self.run_command(INVARIANT)
        self.assertEqual((code, out), (2, ""))
        self.assertTrue(err.startswith("Error: ") and "late.txt" in err, err)

    def test_the_command_rewrites_nothing(self) -> None:
        self.invariant("No file git tracks contains a path.")
        self.track("a.md", "see " + DRIVE + "x\n")
        before = {p.name: p.read_bytes() for p in self.root.iterdir() if p.is_file()}
        self.run_command(INVARIANT)
        after = {p.name: p.read_bytes() for p in self.root.iterdir() if p.is_file()}
        self.assertEqual(after, before)


if __name__ == "__main__":
    unittest.main()
