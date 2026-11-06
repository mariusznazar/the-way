"""Tests of task-cycle/review_reminder.py on small git repositories built for each case."""

from __future__ import annotations

import io
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import review_reminder  # noqa: E402

IDENTITY = ["-c", "user.name=Test", "-c", "user.email=test@example.com",
            "-c", "commit.gpgsign=false", "-c", "tag.gpgsign=false"]


class Repository:
    """A repository whose history the test builds commit by commit, with no working tree files."""

    def __init__(self, directory: Path) -> None:
        self.directory = directory
        self.git("init", "--quiet", "--initial-branch=main")
        self.tree = self.git("mktree", stdin="").strip()

    def git(self, *arguments: str, stdin: str | None = None) -> str:
        done = subprocess.run(["git", *IDENTITY, "-C", str(self.directory), *arguments],
                              input=stdin, capture_output=True, text=True, check=True)
        return done.stdout

    def commit(self, message: str, *parents: str) -> str:
        arguments = ["commit-tree", self.tree, "-m", message]
        for parent in parents:
            arguments += ["-p", parent]
        return self.git(*arguments).strip()

    def move(self, branch: str, commit: str) -> None:
        self.git("update-ref", f"refs/heads/{branch}", commit)

    def tag(self, name: str, commit: str) -> None:
        self.git("tag", "-a", "-m", "review", name, commit)

    def merge_into_main(self, head: str, number: int) -> str:
        """A merge of a side commit into the main branch, as a pull request's merge is."""
        side = self.commit(f"work {number}", head)
        merged = self.commit(f"Merge pull request #{number}", head, side)
        self.move("main", merged)
        return merged


def run(repository: Repository, *arguments: str) -> tuple[int, str, str]:
    out, err = io.StringIO(), io.StringIO()
    with redirect_stdout(out), redirect_stderr(err):
        code = review_reminder.main([*arguments, "--repository", str(repository.directory)])
    return code, out.getvalue(), err.getvalue()


class ReviewReminderTest(unittest.TestCase):
    def setUp(self) -> None:
        self.holder = tempfile.TemporaryDirectory()
        self.addCleanup(self.holder.cleanup)
        self.repo = Repository(Path(self.holder.name))
        self.head = self.repo.commit("root")
        self.repo.move("main", self.head)

    def merges(self, count: int, start: int = 1) -> None:
        for number in range(start, start + count):
            self.head = self.repo.merge_into_main(self.head, number)

    def test_without_a_tag_every_merge_since_the_start_of_history_counts(self) -> None:
        self.merges(3)
        code, out, _ = run(self.repo, "main")
        self.assertEqual(0, code)
        self.assertIn("tag: none\n", out)
        self.assertIn("merges: 3\n", out)
        self.assertIn("reminder: no\n", out)

    def test_only_the_merges_after_the_nearest_review_tag_count(self) -> None:
        self.merges(2)
        self.repo.tag("foundation-review/2026-01-10", self.head)
        self.merges(1, start=3)
        self.repo.tag("foundation-review/2026-01-10-2", self.head)
        self.merges(4, start=4)
        code, out, _ = run(self.repo, "main")
        self.assertEqual(0, code)
        self.assertIn("tag: foundation-review/2026-01-10-2\n", out)
        self.assertIn("merges: 4\n", out)

    def test_a_tag_that_is_no_review_tag_does_not_start_the_count(self) -> None:
        self.merges(2)
        self.repo.tag("v1.0", self.head)
        self.repo.tag("foundation-review-notes", self.head)
        self.merges(1, start=3)
        _, out, _ = run(self.repo, "main")
        self.assertIn("tag: none\n", out)
        self.assertIn("merges: 3\n", out)

    def test_a_merge_of_the_main_branch_into_a_task_branch_does_not_count(self) -> None:
        self.merges(1)
        self.repo.tag("foundation-review/2026-01-10", self.head)
        branch_point = self.head
        side = self.repo.commit("task work", branch_point)
        self.merges(1, start=2)                       # main moves on: one merge counts
        main_tip = self.head
        side = self.repo.commit("main merged into the task branch", side, main_tip)
        self.head = self.repo.commit("Merge pull request #3", main_tip, side)
        self.repo.move("main", self.head)             # the task branch itself merges: counts
        _, out, _ = run(self.repo, "main")
        self.assertIn("merges: 2\n", out)

    def test_the_reminder_starts_at_thirty_merges_and_not_at_twenty_nine(self) -> None:
        self.merges(29)
        _, out, _ = run(self.repo, "main")
        self.assertIn("merges: 29\n", out)
        self.assertIn("reminder: no\n", out)
        self.merges(1, start=30)
        _, out, _ = run(self.repo, "main")
        self.assertIn("merges: 30\n", out)
        self.assertIn("reminder: yes\n", out)

    def test_the_count_after_a_tag_restarts_the_reminder(self) -> None:
        self.merges(31)
        self.repo.tag("foundation-review/2026-01-10", self.head)
        self.merges(2, start=32)
        _, out, _ = run(self.repo, "main")
        self.assertIn("merges: 2\n", out)
        self.assertIn("reminder: no\n", out)

    def test_a_branch_that_does_not_exist_is_an_error(self) -> None:
        code, out, err = run(self.repo, "no-such-branch")
        self.assertEqual(2, code)
        self.assertEqual("", out)
        self.assertTrue(err.startswith("Error: "))

    def test_a_branch_name_that_looks_like_an_option_is_an_error(self) -> None:
        code, _, err = run(self.repo, "--output=x")
        self.assertEqual(2, code)
        self.assertTrue(err.startswith("Error: "))

    def test_a_directory_that_is_no_repository_is_an_error(self) -> None:
        with tempfile.TemporaryDirectory() as empty:
            out, err = io.StringIO(), io.StringIO()
            with redirect_stdout(out), redirect_stderr(err):
                code = review_reminder.main(["main", "--repository", empty])
        self.assertEqual(2, code)
        self.assertTrue(err.getvalue().startswith("Error: "))


if __name__ == "__main__":
    unittest.main()
