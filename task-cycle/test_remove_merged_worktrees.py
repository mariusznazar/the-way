"""Tests of task-cycle/remove_merged_worktrees.py on throwaway repositories.

Each repository is built in a temporary directory of its own, with a bare repository as its remote;
no test touches a directory outside it. A pull request's merge is made with `git merge --no-ff`
in the main checkout, which is what the script reads as a merge on the target branch.
"""

from __future__ import annotations

import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPT = HERE / "remove_merged_worktrees.py"
LINE = re.compile(r"^(remove|keep)\s+(.+?)  \[(.*?)\]  (.*)$")
LIST_HEADER = "Directories of cycles that stay for a human decision"

ENVIRONMENT = {
    **os.environ,
    "GIT_CONFIG_GLOBAL": os.devnull,
    "GIT_CONFIG_NOSYSTEM": "1",
    "GIT_AUTHOR_NAME": "Test", "GIT_AUTHOR_EMAIL": "test@example.com",
    "GIT_COMMITTER_NAME": "Test", "GIT_COMMITTER_EMAIL": "test@example.com",
}


def git(directory: Path, *arguments: str) -> str:
    done = subprocess.run(["git", "-c", "core.autocrlf=false", "-c", "protocol.file.allow=always",
                           "-C", str(directory), *arguments], capture_output=True, text=True,
                          encoding="utf-8", env=ENVIRONMENT, stdin=subprocess.DEVNULL)
    if done.returncode != 0:
        raise AssertionError(f"git {' '.join(arguments)} failed: {done.stdout}{done.stderr}")
    return done.stdout


def write(path: Path, text: str = "x\n") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


class Fixture:
    """A remote, a main checkout on the target branch and the working directories of tasks."""

    def __init__(self, target: str = "main") -> None:
        self.holder = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.root = Path(self.holder.name)
        self.target = target
        self.origin = self.root / "origin.git"
        self.main = self.root / "main"
        self.worktrees = self.root / "wt"
        self.files = 0
        git(self.root, "init", "--bare", "-b", target, str(self.origin))
        git(self.root, "init", "-b", target, str(self.main))
        git(self.main, "remote", "add", "origin", str(self.origin))
        write(self.main / ".gitignore", ".runs/\n__pycache__/\nnode_modules/\n"
                                        ".claude/settings.local.json\nlocal-notes/\n")
        write(self.main / "a.txt")
        git(self.main, "add", ".gitignore", "a.txt")
        git(self.main, "commit", "-m", "root")
        git(self.main, "push", "-u", "origin", target)

    def close(self) -> None:
        self.holder.cleanup()

    def add(self, directory: str, branch: str | None, start: str | None = None,
            where: Path | None = None) -> Path:
        path = (where or self.worktrees) / directory
        arguments = ["worktree", "add"] + (["-b", branch] if branch else ["--detach"])
        git(self.main, *arguments, str(path), start or self.target)
        return path

    def commit(self, path: Path, name: str | None = None) -> None:
        self.files += 1
        name = name or f"file{self.files}.txt"
        write(path / name, f"{name}\n")
        git(path, "add", name)
        git(path, "commit", "-m", f"add {name}")

    def push(self, branch: str) -> None:
        git(self.main, "push", "origin", branch)

    def merge(self, branch: str) -> None:
        git(self.main, "merge", "--no-ff", "-m", f"Merge pull request from {branch}", branch)
        git(self.main, "push", "origin", self.target)

    def task(self, name: str, directory: str | None = None, branch: str | None = None,
             where: Path | None = None) -> Path:
        """A working directory whose branch has a commit and is merged, as after a pull request."""
        branch = branch or f"task/{name}"
        path = self.add(directory or name, branch, where=where)
        self.commit(path)
        self.push(branch)
        self.merge(branch)
        return path

    def run(self, *arguments: str, cwd: Path | None = None, script: Path = SCRIPT,
            repository: Path | None = None) -> subprocess.CompletedProcess:
        command = [sys.executable, "-B", str(script), "--repository",
                   str(repository or self.main), *arguments]
        return subprocess.run(command, capture_output=True, text=True, encoding="utf-8",
                              env=ENVIRONMENT, cwd=cwd or self.root)

    def relative(self, path: str) -> str:
        return Path(os.path.relpath(path, self.root)).as_posix()

    def decisions(self, output: str) -> dict[str, tuple[str, str, str]]:
        """`remove` or `keep`, the branch and the reasons of each directory, by its path from the
        root of the fixture."""
        found = {}
        for line in output.splitlines():
            match = LINE.match(line)
            if match:
                found[self.relative(match.group(2))] = (match.group(1), match.group(3),
                                                        match.group(4))
        return found

    def kept(self, output: str) -> list[str]:
        lines = output.splitlines()
        start = next(i for i, line in enumerate(lines) if line.startswith(LIST_HEADER))
        return [line for line in lines[start + 1:] if line.startswith("- ")]

    def registered(self) -> list[str]:
        return [self.relative(line.split(" ", 1)[1]) for line in
                git(self.main, "worktree", "list", "--porcelain").splitlines()
                if line.startswith("worktree ")]


class ClassificationTest(unittest.TestCase):
    """One dry run over a repository holding a directory for each case the script judges."""

    @classmethod
    def setUpClass(cls) -> None:
        fx = cls.fx = Fixture()
        fx.task("merged-clean")
        ignoring = fx.task("merged-ignored")
        write(ignoring / ".claude" / "settings.local.json")
        write(ignoring / "local-notes" / "n.txt")
        write(ignoring / "__pycache__" / "m.pyc")
        write(ignoring / "node_modules" / "p" / "i.js")
        write(ignoring / ".runs" / "x.log")
        write(fx.task("dirty-tracked") / "a.txt", "changed\n")
        write(fx.task("dirty-untracked") / "new.txt")
        unmerged = fx.add("unmerged-pushed", "task/unmerged-pushed")
        fx.commit(unmerged)
        fx.push("task/unmerged-pushed")
        extra = fx.task("extra-commit")
        fx.commit(extra, "later.txt")
        fx.add("fresh", "task/fresh")
        # A branch that merged the target in, merged in its turn, and a fresh branch at the commit
        # of the target that was merged in.
        sibling = fx.add("sibling", "task/sibling")
        fx.commit(sibling)
        fx.push("task/sibling")
        write(fx.main / "b.txt")
        git(fx.main, "add", "b.txt")
        git(fx.main, "commit", "-m", "target moves on")
        git(fx.main, "push", "origin", fx.target)
        git(sibling, "merge", "-m", "Merge main into task", "main")
        fx.push("task/sibling")
        fx.merge("task/sibling")
        fx.add("fresh-at-merged-in", "task/fresh-at-merged-in", start=fx.target + "~1")
        squashed = fx.add("squashed", "task/squashed")
        fx.commit(squashed)
        fx.push("task/squashed")
        git(fx.main, "merge", "--squash", "task/squashed")
        git(fx.main, "commit", "-m", "Squash the task")
        git(fx.main, "push", "origin", fx.target)
        recorded = fx.task("recorded", directory="recorded", branch="side/recorded")
        write(recorded / ".runs" / "task-cycles" / "slug" / "cycle.md")
        fx.task("plain", directory="plain", branch="feature/plain")
        locked = fx.task("locked")
        git(fx.main, "worktree", "lock", str(locked), "--reason", "in use")
        missing = fx.task("missing")
        shutil.rmtree(missing)
        gone = fx.task("gone", where=fx.main / "inner")
        (gone / ".git").unlink()
        alien = fx.root / "alien"
        git(fx.root, "init", "-b", "main", str(alien))
        git(alien, "commit", "--allow-empty", "-m", "alien root")
        git(alien, "worktree", "add", "-b", "other", str(fx.root / "alien-wt"))
        pointed = fx.task("pointed")
        pointer = (fx.root / "alien-wt" / ".git").read_text(encoding="utf-8")
        (pointed / ".git").unlink()
        write(pointed / ".git", pointer)
        fx.add("scratch", None)
        fx.task("odd", directory="-odd name ü")
        runs = fx.root / ".runs"
        fx.add("base-check-merged-clean", None, where=runs)
        fx.add("base-fix-merged-clean", None, where=runs)
        fx.add("base-check-unmerged-pushed", None, where=runs)
        fx.add("base-check-no-such-task", None, where=runs)
        fx.add("base-check", None, where=runs)
        fx.add("base-check-merged-clean", None, where=fx.root / "elsewhere")
        cls.result = fx.run("--no-fetch")
        cls.decided = fx.decisions(cls.result.stdout)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.fx.close()

    def decision(self, path: str) -> tuple[str, str, str]:
        self.assertIn(path, self.decided, self.result.stdout)
        return self.decided[path]

    def test_the_run_ends_with_exit_zero_and_changes_nothing(self) -> None:
        # Breaks if a dry run removes a directory or exits non-zero for a repository it judged.
        self.assertEqual(0, self.result.returncode, self.result.stderr)
        self.assertIn("Dry run: nothing was removed", self.result.stdout)
        self.assertTrue((self.fx.worktrees / "merged-clean").is_dir())

    def test_a_merged_clean_pushed_task_directory_is_marked_remove(self) -> None:
        # decision: WAY-375 "At the start of a new cycle the cycle runs a script of the-way that removes"
        self.assertEqual("remove", self.decision("wt/merged-clean")[0])

    def test_a_tracked_change_and_a_new_file_keep_the_directory(self) -> None:
        # Breaks if the clean tree test reads only tracked files, or only untracked ones.
        for name in ("dirty-tracked", "dirty-untracked"):
            decision = self.decision(f"wt/{name}")
            self.assertEqual("keep", decision[0])
            self.assertIn("uncommitted changes", decision[2])

    def test_ignored_files_do_not_keep_a_directory_and_are_listed_without_caches(self) -> None:
        # decision: WAY-376 "A file that git ignores does not count against a clean tree"
        self.assertEqual("remove", self.decision("wt/merged-ignored")[0])
        shown = [line.strip() for line in self.result.stdout.splitlines()
                 if line.strip().startswith("ignored:")]
        self.assertIn("ignored: .claude/settings.local.json", shown)
        self.assertIn("ignored: local-notes/", shown)
        self.assertEqual([], [line for line in shown
                              if ".runs" in line or "__pycache__" in line or "node_modules" in line])

    def test_a_commit_not_on_the_remote_keeps_the_directory(self) -> None:
        decision = self.decision("wt/extra-commit")
        self.assertEqual("keep", decision[0])
        self.assertIn("commits not on origin", decision[2])

    def test_an_unmerged_branch_is_kept_though_everything_is_pushed(self) -> None:
        decision = self.decision("wt/unmerged-pushed")
        self.assertEqual("keep", decision[0])
        self.assertNotIn("commits not on origin", decision[2])
        self.assertIn("no merge git can see", decision[2])

    def test_a_branch_with_no_commit_of_its_own_is_not_merged(self) -> None:
        # decision: WAY-375 "A branch is merged where its tip is the second parent of a merge commit"
        # Breaks if "merged" is read as "the tip is an ancestor of the target".
        self.assertEqual("keep", self.decision("wt/fresh")[0])

    def test_the_merge_of_the_target_into_a_task_branch_makes_no_branch_merged(self) -> None:
        # Breaks if the second parents of every merge count, not those of the first-parent history:
        # the commit of the target that a task branch merged in would then be a merged tip.
        self.assertEqual("remove", self.decision("wt/sibling")[0])
        self.assertEqual("keep", self.decision("wt/fresh-at-merged-in")[0])

    def test_a_squashed_branch_is_kept_with_the_reason_that_git_sees_no_merge(self) -> None:
        decision = self.decision("wt/squashed")
        self.assertEqual("keep", decision[0])
        self.assertIn("squash or rebase", decision[2])

    def test_a_branch_without_the_prefix_belongs_to_a_cycle_by_its_record(self) -> None:
        # Breaks if ownership is the prefix alone, which misses a task branch of another name.
        self.assertEqual("remove", self.decision("wt/recorded")[0])

    def test_a_branch_without_prefix_or_record_is_foreign_and_not_listed(self) -> None:
        # decision: WAY-375 "The script touches only the checkouts that"
        decision = self.decision("wt/plain")
        self.assertEqual("keep", decision[0])
        self.assertIn("not a cycle's directory", decision[2])
        self.assertFalse([line for line in self.fx.kept(self.result.stdout) if "plain" in line])

    def test_the_main_checkout_is_never_marked(self) -> None:
        decision = self.decision("main")
        self.assertEqual(("keep", "main", "the main checkout"), decision)

    def test_locked_missing_and_unreadable_directories_are_kept(self) -> None:
        self.assertIn("locked", self.decision("wt/locked")[2])
        self.assertIn("directory is missing", self.decision("wt/missing")[2])
        # Breaks if a checkout whose `.git` is gone is judged by the repository above it, or one
        # whose `.git` points into another repository by that repository.
        self.assertEqual("keep", self.decision("main/inner/gone")[0])
        pointed = self.decision("wt/pointed")
        self.assertEqual("keep", pointed[0])
        self.assertIn("does not read it as a checkout of this repository", pointed[2])
        self.assertTrue((self.fx.main / "a.txt").is_file())

    def test_a_directory_name_with_a_space_a_dash_and_a_letter_outside_ascii_is_handled(self) -> None:
        self.assertEqual("remove", self.decision("wt/-odd name ü")[0])

    def test_a_detached_checkout_that_is_no_base_copy_is_foreign(self) -> None:
        decision = self.decision("wt/scratch")
        self.assertEqual("keep", decision[0])
        self.assertIn("not a cycle's directory", decision[2])
        self.assertFalse([line for line in self.fx.kept(self.result.stdout) if "scratch" in line])

    def test_a_base_copy_goes_by_the_merge_of_the_task_its_name_gives(self) -> None:
        # decision: WAY-375 "At the start of a new cycle the cycle runs a script of the-way that removes"
        for name in ("base-check-merged-clean", "base-fix-merged-clean"):
            self.assertEqual("remove", self.decision(f".runs/{name}")[0], name)
        unmerged = self.decision(".runs/base-check-unmerged-pushed")
        self.assertEqual("keep", unmerged[0])
        self.assertIn("task/unmerged-pushed", unmerged[2])
        self.assertIn("is not found", self.decision(".runs/base-check-no-such-task")[2])
        self.assertIn("named for no task", self.decision(".runs/base-check")[2])

    def test_a_base_copy_outside_a_runs_directory_is_foreign(self) -> None:
        self.assertEqual("keep", self.decision("elsewhere/base-check-merged-clean")[0])

    def test_the_list_for_the_cycle_holds_name_branch_and_reason_and_no_absolute_path(self) -> None:
        # decision: WAY-375 "A directory of a cycle that the script does not remove stays"
        kept = self.fx.kept(self.result.stdout)
        self.assertTrue(kept)
        for line in kept:
            self.assertEqual(3, len(line[2:].split(" | ")), line)
            self.assertNotIn(str(self.fx.root), line)
            self.assertNotIn(self.fx.root.name, line)
        self.assertIn("- unmerged-pushed | task/unmerged-pushed | ", " ".join(kept).replace("\n", " "))
        self.assertTrue([line for line in kept if line.startswith("- base-check-unmerged-pushed | detached | ")])
        self.assertTrue([line for line in kept if line.startswith("- locked | task/locked | ")])


class ApplyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.fx = Fixture()
        self.addCleanup(self.fx.close)

    def test_a_dry_run_removes_nothing_and_apply_removes_only_what_is_marked(self) -> None:
        merged = self.fx.task("merged")
        unmerged = self.fx.add("unmerged", "task/unmerged")
        self.fx.commit(unmerged)
        self.fx.push("task/unmerged")
        dry = self.fx.run()
        self.assertEqual(0, dry.returncode, dry.stderr)
        self.assertTrue(merged.is_dir())
        applied = self.fx.run("--apply")
        self.assertEqual(0, applied.returncode, applied.stderr)
        self.assertFalse(merged.exists())
        self.assertTrue(unmerged.is_dir())
        self.assertNotIn("wt/merged", self.fx.registered())

    def test_apply_removes_no_branch_local_or_remote(self) -> None:
        # decision: WAY-375 "The script touches only the checkouts that"
        self.fx.task("merged")
        self.fx.run("--apply")
        self.assertIn("task/merged", git(self.fx.main, "branch", "--list", "task/merged"))
        self.assertIn("task/merged", git(self.fx.main, "ls-remote", "--heads", "origin"))

    def test_apply_removes_ignored_files_with_the_directory_and_the_dry_run_named_them(self) -> None:
        merged = self.fx.task("merged")
        write(merged / ".claude" / "settings.local.json")
        dry = self.fx.run()
        self.assertIn("ignored: .claude/settings.local.json", dry.stdout)
        self.fx.run("--apply")
        self.assertFalse(merged.exists())

    def test_the_main_checkout_stays_where_it_stands_on_a_merged_branch(self) -> None:
        # Breaks if the main checkout is judged like any other directory.
        git(self.fx.main, "checkout", "-b", "task/on-main")
        self.fx.commit(self.fx.main)
        self.fx.push("task/on-main")
        git(self.fx.main, "checkout", self.fx.target)
        self.fx.merge("task/on-main")
        git(self.fx.main, "checkout", "task/on-main")
        result = self.fx.run("--apply")
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertTrue((self.fx.main / "a.txt").is_file())
        self.assertEqual(("keep", "task/on-main", "the main checkout"),
                         self.fx.decisions(result.stdout)["main"])

    def test_the_directory_the_script_runs_in_is_not_removed(self) -> None:
        merged = self.fx.task("merged")
        result = self.fx.run("--apply", cwd=merged)
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertTrue(merged.is_dir())
        self.assertIn("runs in or from", self.fx.decisions(result.stdout)["wt/merged"][2])
        # A subdirectory of it counts as well, and so does the repository the script is given.
        (merged / "sub").mkdir()
        self.assertTrue(self.fx.run("--apply", cwd=merged / "sub").returncode == 0 and merged.is_dir())
        self.assertTrue(self.fx.run("--apply", repository=merged).returncode == 0 and merged.is_dir())

    def test_the_directory_that_holds_the_script_is_not_removed(self) -> None:
        # Breaks if a directory is removed under the very script that runs.
        merged = self.fx.task("merged")
        copy = merged / ".runs" / "copy" / SCRIPT.name
        copy.parent.mkdir(parents=True)
        shutil.copy(SCRIPT, copy)
        result = self.fx.run("--apply", script=copy)
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertTrue(merged.is_dir())

    def test_apply_removes_a_nested_base_copy_with_its_task_directory(self) -> None:
        # decision: WAY-375 "At the start of a new cycle the cycle runs a script of the-way that removes"
        merged = self.fx.task("merged")
        nested = self.fx.add("base-check", None, where=merged / ".runs")
        scratch = self.fx.add("scratch", None, where=merged / ".runs")
        result = self.fx.run("--apply")
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertFalse(nested.exists())
        self.assertFalse(scratch.exists())
        self.assertFalse(merged.exists())
        self.assertEqual(["main"], self.fx.registered())

    def test_a_nested_checkout_with_uncommitted_work_keeps_its_task_directory(self) -> None:
        merged = self.fx.task("merged")
        nested = self.fx.add("base-check", None, where=merged / ".runs")
        write(nested / "work-in-progress.txt")
        result = self.fx.run("--apply")
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertTrue((nested / "work-in-progress.txt").is_file())
        self.assertTrue(merged.is_dir())
        decision = self.fx.decisions(result.stdout)["wt/merged"]
        self.assertEqual("keep", decision[0])
        self.assertIn("holds base-check, which stays", decision[2])

    def test_a_nested_checkout_on_a_branch_keeps_its_task_directory(self) -> None:
        merged = self.fx.task("merged")
        nested = self.fx.add("side", "task/side", where=merged / ".runs")
        result = self.fx.run("--apply")
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertTrue(nested.is_dir() and merged.is_dir())

    def test_a_base_copy_nested_in_a_kept_directory_is_judged_by_its_own_name(self) -> None:
        unmerged = self.fx.add("unmerged", "task/unmerged")
        self.fx.commit(unmerged)
        self.fx.push("task/unmerged")
        nested = self.fx.add("base-check", None, where=unmerged / ".runs")
        self.fx.run("--apply")
        self.assertTrue(unmerged.is_dir() and nested.is_dir())

    def test_the_merge_pushed_by_another_clone_is_seen_after_the_fetch_only(self) -> None:
        # decision: WAY-375 "At the start of a new cycle the cycle runs a script of the-way that removes"
        branch = self.fx.add("late", "task/late")
        self.fx.commit(branch)
        self.fx.push("task/late")
        other = self.fx.root / "other"
        git(self.fx.root, "clone", str(self.fx.origin), str(other))
        git(other, "merge", "--no-ff", "-m", "Merge pull request from task/late", "origin/task/late")
        git(other, "push", "origin", self.fx.target)
        stale = self.fx.run("--apply", "--no-fetch")
        self.assertEqual("keep", self.fx.decisions(stale.stdout)["wt/late"][0])
        self.assertTrue(branch.is_dir())
        fresh = self.fx.run("--apply")
        self.assertEqual(0, fresh.returncode, fresh.stderr)
        self.assertFalse(branch.exists())

    def test_the_target_branch_comes_from_the_remote_head_or_from_the_option(self) -> None:
        fx = Fixture(target="trunk")
        self.addCleanup(fx.close)
        merged = fx.task("merged")
        git(fx.main, "remote", "set-head", "origin", "trunk")
        self.assertEqual(0, fx.run().returncode)
        self.assertTrue(merged.is_dir())
        git(fx.main, "branch", "decoy", "origin/trunk~1")
        git(fx.main, "push", "origin", "decoy")
        explicit = fx.run("--target", "decoy")
        self.assertEqual("keep", fx.decisions(explicit.stdout)["wt/merged"][0])
        self.assertEqual("remove", fx.decisions(fx.run("--target", "trunk").stdout)["wt/merged"][0])

    def test_a_symbolic_link_inside_a_worktree_is_removed_and_not_followed(self) -> None:
        # decision: WAY-375 "The script touches only the checkouts that"
        merged = self.fx.task("merged")
        outside = self.fx.root / "outside"
        write(outside / "keep.txt", "precious\n")
        link = merged / ".runs" / "link"
        link.parent.mkdir(parents=True, exist_ok=True)
        try:
            os.symlink(outside, link, target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest("this system makes no symbolic link")
        result = self.fx.run("--apply")
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertFalse(merged.exists())
        self.assertEqual("precious\n", (outside / "keep.txt").read_text(encoding="utf-8"))

    def test_a_listed_path_that_is_a_link_is_kept(self) -> None:
        merged = self.fx.task("merged")
        moved = self.fx.root / "moved"
        merged.rename(moved)
        try:
            os.symlink(moved, merged, target_is_directory=True)
        except (OSError, NotImplementedError):
            moved.rename(merged)
            self.skipTest("this system makes no symbolic link")
        result = self.fx.run("--apply")
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertTrue(moved.is_dir())
        self.assertIn("symbolic link or a junction", self.fx.decisions(result.stdout)["wt/merged"][2])

    def test_a_populated_submodule_does_not_keep_a_clean_directory(self) -> None:
        # The checkout of a product holds its `.the-way` submodule, which git removes only forced.
        sub = self.fx.root / "sub"
        git(self.fx.root, "init", "-b", "main", str(sub))
        write(sub / "s.txt")
        git(sub, "add", "s.txt")
        git(sub, "commit", "-m", "sub")
        git(self.fx.main, "submodule", "add", str(sub), ".the-way")
        git(self.fx.main, "commit", "-m", "add the submodule")
        git(self.fx.main, "push", "origin", self.fx.target)
        merged = self.fx.task("merged")
        git(merged, "submodule", "update", "--init")
        self.assertTrue((merged / ".the-way" / "s.txt").is_file())
        result = self.fx.run("--apply")
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertFalse(merged.exists())

    def test_a_removal_that_fails_is_reported_and_the_others_go_on(self) -> None:
        stuck = self.fx.task("stuck")
        other = self.fx.task("other")
        holder = self.hold_a_file(stuck)
        try:
            result = self.fx.run("--apply")
        finally:
            holder()
        if not stuck.exists():
            self.skipTest("this system lets a held file be removed")
        self.assertEqual(1, result.returncode, result.stdout + result.stderr)
        self.assertRegex(result.stdout, r"(?m)^failed\s")
        self.assertFalse(other.exists())
        kept = self.fx.kept(result.stdout)
        self.assertTrue([line for line in kept if line.startswith("- stuck | task/stuck | ")])
        self.assertFalse([line for line in kept if str(self.fx.root) in line])

    def test_a_nested_checkout_that_cannot_be_removed_keeps_the_directory_that_holds_it(self) -> None:
        # Breaks if the directory is removed over a nested checkout whose removal failed.
        merged = self.fx.task("merged")
        nested = self.fx.add("base-check", None, where=merged / ".runs")
        holder = self.hold_a_file(nested)
        try:
            result = self.fx.run("--apply")
        finally:
            holder()
        if not nested.exists():
            self.skipTest("this system lets a held file be removed")
        self.assertEqual(1, result.returncode, result.stdout + result.stderr)
        self.assertTrue(merged.is_dir())
        self.assertIn("inside it was not removed", result.stdout)

    def test_the_fetch_does_not_prune_the_remote_tracking_branches(self) -> None:
        # Breaks if the fetch prunes: the remote-tracking branch of a merged task, deleted on the
        # host, is the evidence that the state reader of a project plan still reads.
        self.fx.task("merged")
        git(self.fx.origin, "branch", "-D", "task/merged")
        result = self.fx.run()
        self.assertEqual(0, result.returncode, result.stderr)
        git(self.fx.main, "rev-parse", "--verify", "refs/remotes/origin/task/merged")

    def hold_a_file(self, worktree: Path):
        """Makes a file of the worktree that git cannot remove, and returns the call that undoes it."""
        held = worktree / ".runs" / "held"
        write(held / "file.txt")
        if os.name == "nt":
            handle = open(held / "file.txt", "rb")
            return handle.close
        held.chmod(stat.S_IRUSR | stat.S_IXUSR)
        return lambda: held.chmod(stat.S_IRWXU)


class ErrorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.fx = Fixture()
        self.addCleanup(self.fx.close)

    def test_a_directory_that_is_no_repository_exits_two_with_an_error(self) -> None:
        empty = self.fx.root / "empty"
        empty.mkdir()
        result = self.fx.run("--apply", repository=empty)
        self.assertEqual(2, result.returncode)
        self.assertTrue(result.stderr.startswith("Error: "), result.stderr)
        self.assertEqual("", result.stdout)

    def test_a_fetch_that_fails_judges_and_removes_nothing(self) -> None:
        merged = self.fx.task("merged")
        git(self.fx.main, "remote", "set-url", "origin", str(self.fx.root / "gone.git"))
        result = self.fx.run("--apply")
        self.assertEqual(2, result.returncode)
        self.assertIn("fetch", result.stderr)
        self.assertTrue(merged.is_dir())

    def test_a_target_that_is_missing_exits_two_and_removes_nothing(self) -> None:
        merged = self.fx.task("merged")
        for arguments in (["--target", "nosuch"], ["--target", "--apply"], ["--remote", "nosuch"]):
            result = self.fx.run("--apply", *arguments)
            self.assertEqual(2, result.returncode, arguments)
            self.assertTrue(merged.is_dir())

    def test_without_a_remote_head_the_target_falls_back_to_main(self) -> None:
        merged = self.fx.task("merged")
        git(self.fx.origin, "symbolic-ref", "HEAD", "refs/heads/nothing")
        git(self.fx.main, "remote", "set-head", "origin", "--delete")
        result = self.fx.run("--apply")
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertFalse(merged.exists())

    def test_no_target_on_the_remote_exits_two(self) -> None:
        fx = Fixture(target="trunk")
        self.addCleanup(fx.close)
        merged = fx.task("merged")
        git(fx.origin, "symbolic-ref", "HEAD", "refs/heads/nothing")
        git(fx.main, "remote", "set-head", "origin", "--delete")
        result = fx.run("--apply")
        self.assertEqual(2, result.returncode)
        self.assertIn("no target branch", result.stderr)
        self.assertTrue(merged.is_dir())

    def test_an_unknown_option_exits_two(self) -> None:
        result = self.fx.run("--force")
        self.assertEqual(2, result.returncode)
        self.assertTrue(result.stderr.startswith("Error: "), result.stderr)


if __name__ == "__main__":
    unittest.main()
