"""Tests of task-cycle/change_file_sizes.py on git repositories made up for the tests."""

from __future__ import annotations

import io
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import change_file_sizes  # noqa: E402

IDENTITY = ["-c", "user.name=Test", "-c", "user.email=test@example.invalid",
            "-c", "commit.gpgsign=false"]


class ChangeFileSizesTest(unittest.TestCase):
    def setUp(self) -> None:
        directory = tempfile.TemporaryDirectory(prefix="the-way-change-file-sizes-test-")
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name) / "product"
        self.root.mkdir()
        self.git("init", "-q")

    def git(self, *arguments: str) -> str:
        run = subprocess.run(["git", *IDENTITY, *arguments], cwd=self.root, check=True,
                             capture_output=True)
        return run.stdout.decode("utf-8").strip()

    def write(self, name: str, content: bytes | str) -> None:
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content if isinstance(content, bytes) else content.encode("utf-8"))

    def commit(self, message: str = "change") -> str:
        self.git("add", "-A")
        self.git("commit", "-q", "-m", message)
        return self.git("rev-parse", "HEAD")

    def run_command(self, base: str, head: str, root: Path | None = None) -> tuple[int, str, str]:
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            code = change_file_sizes.main([base, head, "--root", str(root or self.root)])
        return code, out.getvalue(), err.getvalue()

    def rows(self, output: str) -> list[str]:
        return [line for line in output.splitlines() if line.startswith("| `")]

    def summary(self, output: str) -> str:
        return [line for line in output.splitlines() if line.startswith("Summary:")][0]

    def test_a_modified_file_gives_its_lines_before_and_after(self) -> None:
        self.write("src/app.py", "a\nb\nc\n")
        base = self.commit()
        self.write("src/app.py", "a\nb\nc\nd\ne\n")
        head = self.commit()
        code, output, _ = self.run_command(base, head)
        self.assertEqual(code, 0)
        self.assertEqual(self.rows(output), ["| `src/app.py` | 3 | 5 | +2 | modified |"])
        self.assertEqual(self.summary(output), "Summary: 1 files changed (0 added, 0 deleted, "
                         "0 renamed, 1 modified, 0 not measured); lines before 3, after 5, "
                         "change +2.")

    def test_an_added_and_a_deleted_file_have_no_number_on_the_side_they_lack(self) -> None:
        self.write("old.py", "1\n2\n3\n4\n")
        base = self.commit()
        (self.root / "old.py").unlink()
        self.write("new.py", "x\ny\n")
        head = self.commit()
        code, output, _ = self.run_command(base, head)
        self.assertEqual(code, 0)
        self.assertEqual(self.rows(output), ["| `new.py` | — | 2 | +2 | added |",
                                             "| `old.py` | 4 | — | -4 | deleted |"])
        self.assertEqual(self.summary(output), "Summary: 2 files changed (1 added, 1 deleted, "
                         "0 renamed, 0 modified, 0 not measured); lines before 4, after 2, "
                         "change -2.")

    def test_a_last_line_without_a_line_feed_counts_and_an_empty_file_has_none(self) -> None:
        self.write("a.txt", "one")
        self.write("b.txt", "")
        self.write("c.txt", "one\r\ntwo\r\n")
        base = self.commit()
        self.write("a.txt", "one\ntwo")
        self.write("b.txt", "\n")
        self.write("c.txt", "one\r\ntwo\r\nthree")
        head = self.commit()
        _, output, _ = self.run_command(base, head)
        self.assertEqual(self.rows(output), ["| `a.txt` | 1 | 2 | +1 | modified |",
                                             "| `b.txt` | 0 | 1 | +1 | modified |",
                                             "| `c.txt` | 2 | 3 | +1 | modified |"])

    def test_a_renamed_file_is_measured_at_its_old_path_before_the_change(self) -> None:
        text = "".join(f"line {number}\n" for number in range(20))
        self.write("old_name.py", text)
        base = self.commit()
        (self.root / "old_name.py").unlink()
        self.write("pkg/new_name.py", text + "one more\n")
        head = self.commit()
        code, output, _ = self.run_command(base, head)
        self.assertEqual(code, 0)
        self.assertEqual(self.rows(output), [
            "| `pkg/new_name.py` | 20 | 21 | +1 | renamed from `old_name.py` |"])
        self.assertIn("1 renamed", self.summary(output))
        self.assertIn("lines before 20, after 21, change +1.", self.summary(output))

    def test_a_binary_file_is_listed_and_adds_no_line_to_the_totals(self) -> None:
        self.write("shot.png", b"\x89PNG\r\n\x1a\n\0\0\0\rIHDR")
        self.write("a.py", "x\n")
        base = self.commit()
        self.write("shot.png", b"\x89PNG\r\n\x1a\n\0\0\0\rIHDR\0\0\0\0\0\0\0\0")
        self.write("a.py", "x\ny\n")
        head = self.commit()
        _, output, _ = self.run_command(base, head)
        self.assertEqual(self.rows(output), ["| `a.py` | 1 | 2 | +1 | modified |",
                                             "| `shot.png` | binary | binary | — | modified |"])
        self.assertEqual(self.summary(output), "Summary: 2 files changed (0 added, 0 deleted, "
                         "0 renamed, 1 modified, 1 not measured); lines before 1, after 2, "
                         "change +1.")

    def test_a_submodule_is_listed_with_no_lines(self) -> None:
        self.write("a.py", "x\n")
        base = self.commit()
        self.git("update-index", "--add", "--cacheinfo",
                 f"160000,{base},vendor/lib")
        self.git("commit", "-q", "-m", "add a submodule entry")
        head = self.git("rev-parse", "HEAD")
        code, output, _ = self.run_command(base, head)
        self.assertEqual(code, 0)
        self.assertEqual(self.rows(output), ["| `vendor/lib` | — | submodule | — | added |"])
        self.assertIn("lines before 0, after 0, change +0.", self.summary(output))

    def stage_entry(self, name: str, content: str, mode: str) -> None:
        """Puts an entry of any name and mode in the index, whatever the file system allows."""
        source = self.root.parent / "blob-source"
        source.write_bytes(content.encode("utf-8"))
        blob = self.git("hash-object", "-w", str(source))
        self.git("update-index", "--add", "--cacheinfo", f"{mode},{blob},{name}")

    def commit_index(self) -> str:
        self.git("commit", "-q", "-m", "change")
        return self.git("rev-parse", "HEAD")

    def test_a_file_that_becomes_a_symbolic_link_is_a_type_change_measured_on_both_sides(self) -> None:
        self.stage_entry("thing", "one\ntwo\n", "100644")
        base = self.commit_index()
        self.stage_entry("thing", "target", "120000")
        head = self.commit_index()
        code, output, _ = self.run_command(base, head)
        self.assertEqual(code, 0)
        self.assertEqual(self.rows(output), ["| `thing` | 2 | 1 | -1 | type changed |"])
        self.assertIn("1 modified", self.summary(output))

    def test_a_bar_in_a_name_is_escaped_so_that_the_row_keeps_its_cells(self) -> None:
        self.stage_entry("a|b.txt", "x\n", "100644")
        base = self.commit_index()
        self.stage_entry("a|b.txt", "x\ny\n", "100644")
        head = self.commit_index()
        _, output, _ = self.run_command(base, head)
        self.assertEqual(self.rows(output), ["| `a\\|b.txt` | 1 | 2 | +1 | modified |"])

    def test_a_backtick_in_a_name_gets_a_longer_delimiter_and_a_padded_edge(self) -> None:
        self.stage_entry("back`tick.md", "x\n", "100644")
        self.stage_entry("`lead.md", "x\n", "100644")
        base = self.commit_index()
        self.stage_entry("back`tick.md", "x\ny\n", "100644")
        self.stage_entry("`lead.md", "x\ny\n", "100644")
        head = self.commit_index()
        _, output, _ = self.run_command(base, head)
        self.assertEqual(self.rows(output), ["| `` `lead.md `` | 1 | 2 | +1 | modified |",
                                             "| ``back`tick.md`` | 1 | 2 | +1 | modified |"])

    def test_a_name_with_a_space_and_a_letter_outside_ascii_is_read_as_it_is(self) -> None:
        self.write("notes ł/zażółć gęślą.md", "a\nb\n")
        base = self.commit()
        self.write("notes ł/zażółć gęślą.md", "a\nb\nc\n")
        head = self.commit()
        code, output, _ = self.run_command(base, head)
        self.assertEqual(code, 0)
        self.assertEqual(self.rows(output), ["| `notes ł/zażółć gęślą.md` | 2 | 3 | +1 | modified |"])

    def test_the_range_is_between_the_two_commits_given_and_unchanged_files_stay_out(self) -> None:
        self.write("kept.py", "k\n")
        self.write("grows.py", "g\n")
        first = self.commit()
        self.write("grows.py", "g\ng\n")
        self.commit()
        self.write("grows.py", "g\ng\ng\n")
        self.write("later.py", "l\n")
        last = self.commit()
        _, output, _ = self.run_command(first, last)
        self.assertEqual(self.rows(output), ["| `grows.py` | 1 | 3 | +2 | modified |",
                                             "| `later.py` | — | 1 | +1 | added |"])
        _, output, _ = self.run_command("HEAD~1", "HEAD")
        self.assertEqual(self.rows(output), ["| `grows.py` | 2 | 3 | +1 | modified |",
                                             "| `later.py` | — | 1 | +1 | added |"])

    def test_the_same_commit_twice_gives_an_empty_table_and_a_summary_of_nothing(self) -> None:
        self.write("a.py", "x\n")
        head = self.commit()
        code, output, _ = self.run_command(head, head)
        self.assertEqual(code, 0)
        self.assertEqual(self.rows(output), [])
        self.assertEqual(self.summary(output), "Summary: 0 files changed (0 added, 0 deleted, "
                         "0 renamed, 0 modified, 0 not measured); lines before 0, after 0, "
                         "change +0.")

    def test_a_name_that_is_no_commit_ends_with_exit_two_and_an_error_line_naming_it(self) -> None:
        self.write("a.py", "x\n")
        head = self.commit()
        code, output, error = self.run_command("no-such-branch", head)
        self.assertEqual(code, 2)
        self.assertEqual(output, "")
        self.assertTrue(error.startswith("Error: `no-such-branch` names no commit in "), error)
        self.assertEqual(len(error.splitlines()), 1)

    def test_a_name_that_is_no_commit_but_a_tree_ends_with_exit_two(self) -> None:
        self.write("a.py", "x\n")
        head = self.commit()
        tree = self.git("rev-parse", "HEAD^{tree}")
        code, _, error = self.run_command(head, tree)
        self.assertEqual(code, 2)
        self.assertTrue(error.startswith(f"Error: `{tree}` names no commit"), error)

    def test_a_directory_that_holds_no_repository_ends_with_exit_two(self) -> None:
        with tempfile.TemporaryDirectory(prefix="the-way-change-file-sizes-empty-") as empty:
            code, output, error = self.run_command("HEAD", "HEAD", Path(empty))
        self.assertEqual(code, 2)
        self.assertEqual(output, "")
        self.assertTrue(error.startswith("Error: "), error)
        self.assertEqual(len(error.splitlines()), 1)

    def test_a_root_that_is_no_directory_ends_with_exit_two(self) -> None:
        code, output, error = self.run_command("HEAD", "HEAD", self.root / "absent")
        self.assertEqual(code, 2)
        self.assertEqual(output, "")
        self.assertIn("is not a directory", error)

    def test_the_script_run_as_a_command_writes_utf8_and_ends_with_the_exit_code(self) -> None:
        self.write("zażółć.md", "a\n")
        base = self.commit()
        self.write("zażółć.md", "a\nb\n")
        head = self.commit()
        script = Path(change_file_sizes.__file__)
        run = subprocess.run([sys.executable, "-B", str(script), base, head, "--root",
                              str(self.root)], capture_output=True)
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertIn("| `zażółć.md` | 1 | 2 | +1 | modified |", run.stdout.decode("utf-8"))
        failed = subprocess.run([sys.executable, "-B", str(script), "absent", head, "--root",
                                 str(self.root)], capture_output=True)
        self.assertEqual(failed.returncode, 2)
        self.assertEqual(failed.stdout, b"")
        self.assertTrue(failed.stderr.decode("utf-8").startswith("Error: `absent` names no commit"))

    def test_the_command_changes_nothing_in_the_repository(self) -> None:
        self.write("a.py", "x\n")
        base = self.commit()
        self.write("a.py", "x\ny\n")
        head = self.commit()
        before = self.git("status", "--porcelain=v1", "--ignored") + self.git("rev-parse", "HEAD")
        self.run_command(base, head)
        after = self.git("status", "--porcelain=v1", "--ignored") + self.git("rev-parse", "HEAD")
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()
