"""Tests of task-cycle/slice_size.py on small plans and the files they name."""

from __future__ import annotations

import io
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import slice_size  # noqa: E402


class SliceSizeTest(unittest.TestCase):
    def setUp(self) -> None:
        directory = tempfile.TemporaryDirectory(prefix="the-way-slice-size-test-")
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name) / "product"
        self.root.mkdir()

    def file(self, name: str, text: str) -> None:
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="")

    def run_plan(self, plan: str) -> tuple[int, str, str]:
        path = self.root.parent / "plan.md"
        path.write_text(plan, encoding="utf-8")
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            code = slice_size.main([str(path), "--root", str(self.root)])
        return code, out.getvalue(), err.getvalue()

    def row(self, output: str, ident: str) -> list[str]:
        for line in output.splitlines():
            cells = [cell.strip() for cell in line.strip("|").split("|")]
            if cells[0] == ident:
                return cells
        self.fail(f"no row for slice {ident} in:\n{output}")

    def test_slice_within_limits_fits(self) -> None:
        self.file("src/app.py", "a" * 100)
        self.file("docs/guide.md", "b" * 50)
        code, output, _ = self.run_plan(
            "# Plan\n\n## Slices\n\n### Slice 1 — Add the flag\n\n- **Goal:** the flag works\n"
            "- **Change:** `src/app.py` · `src/new.py`\n- **Read:** `docs/guide.md`\n"
            "- **Checks:** `python -B -m unittest`\n")
        self.assertEqual(code, 0)
        self.assertEqual(self.row(output, "1"), ["1", "2", "150", "60", "fits", "—"])

    def test_changed_file_named_again_in_read_counts_once(self) -> None:
        self.file("a.md", "x" * 10)
        code, output, _ = self.run_plan(
            "### Slice 1\n- **Change:** `a.md`\n- **Read:** `a.md` · `a.md:1-1`\n")
        self.assertEqual(code, 0)
        self.assertEqual(self.row(output, "1")[1:4], ["1", "10", "4"])

    def test_range_counts_only_its_lines(self) -> None:
        self.file("log.md", "one\ntwo\nthree\nfour\n")
        code, output, _ = self.run_plan(
            "### Slice 2a — Read part of a log\n- **Change:** none\n"
            "- **Read:** `log.md:2-3` · `log.md:3-3`\n")
        self.assertEqual(code, 0)
        self.assertEqual(self.row(output, "2a")[1:5], ["0", "10", "4", "fits"])

    def test_paths_on_continued_lines_count(self) -> None:
        self.file("a.txt", "1234")
        self.file("b.txt", "56")
        code, output, _ = self.run_plan(
            "### Slice 1\n- **Read:** `a.txt` ·\n  `b.txt`\n- **Checks:** `c.txt`\n")
        self.assertEqual(code, 0)
        self.assertEqual(self.row(output, "1")[2], "6")

    def test_read_at_the_limit_fits_and_one_character_more_is_too_large(self) -> None:
        self.file("at.txt", "a" * 625_000)
        self.file("over.txt", "a" * 625_001)
        code, output, _ = self.run_plan(
            "### Slice 1\n- **Read:** `at.txt`\n\n### Slice 2\n- **Read:** `over.txt`\n")
        self.assertEqual(code, 1)
        self.assertEqual(self.row(output, "1")[3:5], ["250000", "fits"])
        self.assertEqual(self.row(output, "2")[3:6], [
            "250001", "too large", "reads about 250001 tokens, more than 250000"])

    def test_more_than_ten_files_to_change_is_too_large(self) -> None:
        ten = " · ".join(f"`f{number}.py`" for number in range(10))
        code, output, _ = self.run_plan(
            f"### Slice 1\n- **Change:** {ten}\n\n### Slice 2\n- **Change:** {ten} · `g.py`\n")
        self.assertEqual(code, 1)
        self.assertEqual(self.row(output, "1")[1:5], ["10", "0", "0", "fits"])
        self.assertEqual(self.row(output, "2")[4:6], [
            "too large", "changes 11 files, more than 10"])

    def test_missing_read_file_leaves_the_slice_unchecked(self) -> None:
        code, output, _ = self.run_plan("### Slice 1\n- **Read:** `absent.md`\n")
        self.assertEqual(code, 1)
        self.assertEqual(self.row(output, "1")[2:6], [
            "unknown", "unknown", "unchecked", "`absent.md` names no file under the root"])

    def test_path_outside_the_root_leaves_the_slice_unchecked(self) -> None:
        (self.root.parent / "secret.txt").write_text("x", encoding="utf-8")
        code, output, _ = self.run_plan(
            "### Slice 1\n- **Read:** `../secret.txt`\n- **Change:** `../elsewhere.py`\n")
        self.assertEqual(code, 1)
        self.assertEqual(self.row(output, "1")[4], "unchecked")
        self.assertIn("`../secret.txt` names no file under the root", output)
        self.assertIn("`../elsewhere.py` names no file under the root", output)

    def test_range_beyond_the_file_leaves_the_slice_unchecked(self) -> None:
        self.file("short.md", "one\ntwo\n")
        code, output, _ = self.run_plan("### Slice 1\n- **Read:** `short.md:2-5`\n")
        self.assertEqual(code, 1)
        self.assertEqual(self.row(output, "1")[4:6], [
            "unchecked", "`short.md:2-5` goes beyond the file's 2 lines"])

    def test_plan_without_a_slice_is_an_error(self) -> None:
        code, output, error = self.run_plan("# Plan\n\n- **Change:** `a.py`\n")
        self.assertEqual(code, 2)
        self.assertEqual(output, "")
        self.assertEqual(error, "Error: the plan holds no heading `### Slice <id>`\n")

    def test_two_slices_of_one_name_are_an_error(self) -> None:
        code, _, error = self.run_plan("### Slice 1\n### Slice 1 — again\n")
        self.assertEqual(code, 2)
        self.assertEqual(error, "Error: two slices are named 1\n")


if __name__ == "__main__":
    unittest.main()
