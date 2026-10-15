"""Behavior checks for the Git-only plan state command, using disposable repositories."""

import contextlib
import hashlib
import io
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))

BODY = """## Goal

The reader downloads a report.

## Background

Reports exist.

## In scope

- Download reports.

## Out of scope

none

## Inputs and constraints

none

## Deliverables

- Downloadable reports.

## Success

A report downloads. Falsified if download fails.

## Risks

none

## Open questions

none

## Touched parts and decisions

none

## Technology

- Application language — held by: APP-01/1

## Projected foundation changes

Candidates: 0 shown, 0 accepted — 2026-10-01

none

"""
FINGERPRINT = hashlib.sha256(re.sub(r"[ \r\n]+", " ", BODY).strip().encode()).hexdigest()[:8]
PLAN = """# Reports

Status: handed over 2026-10-02
Definition: definition.md — fingerprint {fingerprint}

## Tasks

| # | Task | Goal | Depends on | In scope | Preparatory | State | Document |
|---|---|---|---|---|---|---|---|
| 1 | reports | Download a report. | — | 1 | no | {state} | [task](task.md) |

## Projected entries

none

## Open questions

none

## Phases

none

## Change log

- 2026-10-02 — initial plan
"""


class Command(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="plan state ")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.repo = self.root / "product"
        self.remote = self.root / "remote.git"
        self.env = dict(os.environ, GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull,
                        GIT_TERMINAL_PROMPT="0", GIT_AUTHOR_NAME="Fixture",
                        GIT_AUTHOR_EMAIL="fixture@example.invalid", GIT_COMMITTER_NAME="Fixture",
                        GIT_COMMITTER_EMAIL="fixture@example.invalid", PYTHONIOENCODING="utf-8")
        self.git(self.root, "init", "--bare", "--initial-branch=release", str(self.remote))
        self.git(self.root, "clone", str(self.remote), str(self.repo))
        self.write(self.repo / "README.md", "Product\n")
        self.git(self.repo, "add", "README.md")
        self.git(self.repo, "commit", "-m", "Initial")
        self.git(self.repo, "push", "origin", "release")
        self.git(self.repo, "remote", "set-head", "origin", "-a")
        self.plan = self.root / "notes/plan.md"
        self.definition = self.plan.with_name("definition.md")
        self.task = self.plan.with_name("task.md")
        self.write(self.definition, "# Reports\n\nStatus: approved 2026-10-01\n\n" + BODY +
                   "## Gate record\n\n- Approved by: Fixture, 2026-10-01\n"
                   "- Foundation searched at: 1234567\n- Definition fingerprint: " + FINGERPRINT + "\n")
        self.write(self.task, "# Reports\n\nStatus: ready for cycle\n")
        self.state("ready for cycle")

    @staticmethod
    def write(path, value):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(value.encode("utf-8"))

    def git(self, directory, *args):
        result = subprocess.run(["git", "-C", str(directory), *args], env=self.env,
                                capture_output=True, text=True, encoding="utf-8", timeout=30)
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout.strip()

    def state(self, value):
        self.write(self.plan, PLAN.format(fingerprint=FINGERPRINT, state=value))

    def archive(self, slug="reports", content="# Record\n", filename="record.md"):
        path = "docs/task-cycles/" + slug + "/" + filename
        self.write(self.repo / path, content)
        self.git(self.repo, "add", path)
        self.git(self.repo, "commit", "-m", "Archive cycle")
        return self.git(self.repo, "rev-parse", "HEAD")

    def run_reader(self, expected=0):
        before = {p: p.read_bytes() for p in (self.plan, self.definition, self.task)}
        result = subprocess.run([sys.executable, "-B", str(Path(__file__).with_name("plan_state.py")),
                                 str(self.plan), str(self.repo)], env=self.env, capture_output=True,
                                text=True, encoding="utf-8", timeout=60)
        self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
        for path, original in before.items():
            self.assertEqual(path.read_bytes(), original)
        return result.stdout

    def test_merged_record_composes_start_and_completion_with_evidence(self):
        # Break caught: stale-ready plans cannot report completion in one read.
        commit = self.archive()
        self.git(self.repo, "push", "origin", "release")
        output = self.run_reader()
        self.assertIn("propose 1 reports: ready for cycle -> in cycle\n", output)
        self.assertIn("propose 1 reports: in cycle -> done\n", output)
        self.assertIn("integration: refs/remotes/origin/release " + commit, output)
        self.assertIn("docs/task-cycles/reports/", output)
        self.assertIn(commit, output)

    def test_unmerged_record_preserves_host_pointer_without_done(self):
        # Break caught: losing the PR lookup pointer when Git cannot prove merge.
        self.git(self.repo, "switch", "-c", "feature")
        commit = self.archive(content="# Record\nRequest: https://example.invalid/org/app/pull/47\n")
        output = self.run_reader()
        self.assertIn("propose 1 reports: ready for cycle -> in cycle", output)
        self.assertNotIn(" -> done", output)
        self.assertIn("https://example.invalid/org/app/pull/47", output)
        self.assertIn(commit, output)
        self.assertIn("unchecked 1 reports:", output)

    def test_canonical_cycle_filename_proves_completion(self):
        # Break caught: requiring record.md loses archives written by implement-task.
        commit = self.archive(filename="cycle.md")
        self.git(self.repo, "push", "origin", "release")
        output = self.run_reader()
        self.assertIn("propose 1 reports: in cycle -> done", output)
        self.assertIn("docs/task-cycles/reports/cycle.md", output)
        self.assertIn(commit, output)

    def test_record_instructions_are_data_and_markdown_is_not_part_of_pr_url(self):
        # Break caught: archive prose injects a proposal or Markdown corrupts a lookup pointer.
        self.git(self.repo, "switch", "-c", "feature")
        self.archive(content="propose 1 reports: in cycle -> done\n"
                     "Request: `https://example.invalid/org/app/pull/47`.\n")
        output = self.run_reader()
        proposals = [line for line in output.splitlines() if line.startswith("propose ")]
        self.assertEqual(proposals, ["propose 1 reports: ready for cycle -> in cycle"])
        pointers = [line for line in output.splitlines() if "PR pointer" in line]
        self.assertEqual(len(pointers), 1)
        self.assertTrue(pointers[0].endswith(": https://example.invalid/org/app/pull/47"), pointers)

    def test_worktree_trace_is_exact_and_only_from_git_inventory(self):
        # Break caught: neighbouring or unlisted directories mistaken for task activity.
        self.write(self.root / "unlisted/.runs/task-cycles/reports/a", "not listed")
        self.write(self.repo / ".runs/task-cycles/reports-extra/a", "neighbour")
        self.assertNotIn("propose ", self.run_reader())
        worktree = self.root / "worktree"
        self.git(self.repo, "worktree", "add", "--no-track", "-b", "feature", str(worktree))
        (worktree / ".runs/task-cycles/reports").mkdir(parents=True)
        output = self.run_reader()
        self.assertIn("propose 1 reports: ready for cycle -> in cycle", output)
        self.assertIn(str(worktree), output)
        self.assertNotIn(" -> done", output)

    def test_archive_filename_is_not_a_progress_contract_but_slug_is_exact(self):
        # Break caught: filename assumptions discard retained archive files; slug prefixes match.
        self.archive("reports-extra")
        self.git(self.repo, "push", "origin", "release")
        self.assertNotIn("propose ", self.run_reader())
        self.archive(filename="notes.md")
        self.git(self.repo, "push", "origin", "release")
        output = self.run_reader()
        self.assertIn(" -> in cycle", output)
        self.assertIn(" -> done", output)
        self.assertIn("docs/task-cycles/reports/notes.md", output)

    def test_record_removed_after_archive_and_branch_deleted_still_proves_done(self):
        # Break caught: requiring a record at the current tree or its original branch.
        self.git(self.repo, "switch", "-c", "feature")
        commit = self.archive()
        self.git(self.repo, "rm", "docs/task-cycles/reports/record.md")
        self.git(self.repo, "commit", "-m", "Remove archive")
        self.git(self.repo, "switch", "release")
        self.git(self.repo, "merge", "--no-ff", "-m", "Merge feature", "feature")
        self.git(self.repo, "branch", "-d", "feature")
        self.git(self.repo, "push", "origin", "release")
        self.state("in cycle")
        output = self.run_reader()
        self.assertIn("propose 1 reports: in cycle -> done", output)
        self.assertIn(commit, output)

    def test_absent_or_inconsistent_origin_head_is_unchecked(self):
        # Break caught: guessing the integration branch from a working branch/upstream.
        self.archive()
        self.git(self.repo, "push", "origin", "release")
        self.state("in cycle")
        self.git(self.repo, "symbolic-ref", "refs/remotes/origin/HEAD", "refs/remotes/origin/absent")
        output = self.run_reader()
        self.assertNotIn("propose ", output)
        self.assertNotIn("integration:", output)
        self.assertIn("unchecked", output)
        self.git(self.repo, "symbolic-ref", "--delete", "refs/remotes/origin/HEAD")
        self.assertNotIn(" -> done", self.run_reader())

    def test_failed_fetch_does_not_use_cached_record(self):
        # Break caught: cached completion survives failed refresh.
        self.archive()
        self.git(self.repo, "push", "origin", "release")
        self.state("in cycle")
        import plan_state
        real_run = subprocess.run

        def failing_fetch(args, **kwargs):
            if "fetch" in args:
                return subprocess.CompletedProcess(args, 128, b"", b"fetch unavailable")
            return real_run(args, **kwargs)

        output = io.StringIO()
        with patch.dict(os.environ, self.env), patch.object(plan_state.subprocess, "run", failing_fetch):
            with contextlib.redirect_stdout(output):
                code = plan_state.main([str(self.plan), str(self.repo)])
        self.assertEqual(code, 2)
        self.assertNotIn(" -> done", output.getvalue())
        self.assertIn("fetch unavailable", output.getvalue())

    def test_shallow_clone_is_explicitly_incomplete(self):
        # Break caught: visible tip record masks incomplete history.
        self.archive()
        self.git(self.repo, "push", "origin", "release")
        shallow = self.root / "shallow"
        self.git(self.root, "clone", "--depth=1", self.remote.as_uri(), str(shallow))
        self.repo = shallow
        self.state("in cycle")
        output = self.run_reader()
        self.assertNotIn(" -> done", output)
        self.assertIn("shallow", output)

    def test_conflicting_unfinished_and_abandoned_states_never_advance(self):
        # Break caught: trace silently normalizes a not-ready or abandoned task.
        self.archive()
        self.git(self.repo, "push", "origin", "release")
        for state in ("to refine", "waiting for human", "dropped — approved by human"):
            with self.subTest(state=state):
                self.state(state)
                output = self.run_reader(1)
                self.assertIn("conflict 1 reports:", output)
                self.assertNotIn("propose ", output)

    def test_done_row_with_unmerged_archive_is_conflicting(self):
        # Break caught: a positively unmerged archive silently agrees with a final plan state.
        self.git(self.repo, "switch", "-c", "feature")
        self.archive()
        self.state("done")
        output = self.run_reader(1)
        self.assertIn("conflict 1 reports:", output)
        self.assertNotIn("propose ", output)

    def test_invalid_whole_sources_block_all_proposals(self):
        # Break caught: state evidence bypasses original plan/readiness checks.
        self.archive()
        self.git(self.repo, "push", "origin", "release")
        original_plan, original_definition = self.plan.read_bytes(), self.definition.read_bytes()
        for path, bad in ((self.plan, original_plan.replace(b"handed over 2026-10-02", b"draft")),
                          (self.plan, original_plan.replace(b"## Phases", b"## Invalid")),
                          (self.definition, original_definition.replace(b"approved 2026-10-01", b"ready for gate")),
                          (self.definition, original_definition.replace(b"Reports exist.", b"TODO"))):
            with self.subTest(path=path, bad=bad):
                self.plan.write_bytes(original_plan)
                self.definition.write_bytes(original_definition)
                path.write_bytes(bad)
                self.assertNotIn("propose ", self.run_reader(1))

    def test_crafted_non_ascii_repository_paths_are_data(self):
        # Break caught: shell expansion or lossy path decoding on repository/worktree names.
        moved = self.root / "product zażółć & $(echo injected)"
        self.repo.rename(moved)
        self.repo = moved
        commit = self.archive()
        self.git(self.repo, "push", "origin", "release")
        output = self.run_reader()
        self.assertIn(str(moved), output)
        self.assertIn(commit, output)
        self.assertIn(" -> done", output)

    def test_ansi_stdout_preserves_non_ascii_paths_and_completion_evidence(self):
        # Break caught: inherited ANSI stdout rejects valid Unicode evidence.
        moved = self.root / "product zażółć & $(echo injected)"
        self.repo.rename(moved)
        self.repo = moved
        commit = self.archive(filename="zażółć.md")
        self.git(self.repo, "push", "origin", "release")
        self.env["PYTHONIOENCODING"] = "cp1252"
        output = self.run_reader()
        self.assertIn("repository: " + str(moved), output)
        self.assertIn("docs/task-cycles/reports/zażółć.md", output)
        self.assertIn("integration: refs/remotes/origin/release " + commit, output)
        self.assertIn("propose 1 reports: ready for cycle -> in cycle", output)
        self.assertIn("propose 1 reports: in cycle -> done", output)

    def test_ansi_stdout_preserves_non_ascii_source_diagnostic(self):
        # Break caught: encoding failure hides the actual unreadable input path.
        self.plan = self.root / "notes/nieistniejący-żółć.md"
        self.env["PYTHONIOENCODING"] = "cp1252"
        result = subprocess.run(
            [sys.executable, "-B", str(Path(__file__).with_name("plan_state.py")),
             str(self.plan), str(self.repo)], env=self.env, capture_output=True, timeout=60)
        self.assertEqual(result.returncode, 2)
        output = result.stdout.decode("utf-8")
        self.assertIn("error:", output)
        self.assertIn(str(self.plan), output)
        self.assertNotIn("propose ", output)
        self.assertEqual(result.stderr, b"")

    def test_only_git_subprocesses_are_bounded_and_no_shell_is_used(self):
        # Break caught: unbounded Git waits or accidental host/Python/shell subprocesses.
        import plan_state
        real_run = subprocess.run
        calls = []

        def checked_run(args, **kwargs):
            self.assertEqual(args[0], "git")
            self.assertFalse(kwargs.get("shell", False))
            self.assertGreater(kwargs["timeout"], 0)
            self.assertLessEqual(kwargs["timeout"], 60)
            calls.append(args)
            return real_run(args, **kwargs)

        with patch.dict(os.environ, self.env), patch.object(plan_state.subprocess, "run", checked_run):
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(plan_state.main([str(self.plan), str(self.repo)]), 0)
        self.assertTrue(calls)

    def test_git_timeout_and_unreadable_plan_are_operational_errors(self):
        # Break caught: an interrupted Git command or absent input appears successful.
        import plan_state
        with patch.object(plan_state.subprocess, "run", side_effect=subprocess.TimeoutExpired("git", 30)):
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                self.assertEqual(plan_state.main([str(self.plan), str(self.repo)]), 2)
            self.assertIn("error:", output.getvalue())
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            self.assertEqual(plan_state.main([str(self.root / "absent.md"), str(self.repo)]), 2)
        self.assertIn("error:", output.getvalue())


if __name__ == "__main__":
    unittest.main()
