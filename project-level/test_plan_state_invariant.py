"""Independent black-box evidence checks, with real disposable Git repositories.

Each test names the unsupported-progress or lost-evidence bug it catches. Expected
transitions are literals; no reader code or helper supplies the oracle.
"""

import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


READER = Path(__file__).resolve().with_name("plan_state.py")
DEFINITION_BODY = """## Goal

Readers can download a saved report.

## Background

Readers cannot download reports today.

## In scope

- Download a saved report.

## Out of scope

none

## Inputs and constraints

none

## Deliverables

- A downloadable saved report.

## Success

A reader downloads a report.
**FALSIFIED IF:** a saved report cannot be downloaded.

## Risks

none

## Open questions

none

## Touched parts and decisions

none

## Technology

- Existing application language — held by: APP-01/1

## Projected foundation changes

Candidates: 0 shown, 0 accepted — 2026-10-01

none

"""
# Independently calculated once from the literal body under WAY-02, not from the reader.
FINGERPRINT = "a3b6ab99"

PLAN = """# Report download

Status: handed over 2026-10-02
Definition: definition.md — fingerprint {fingerprint}

## Tasks

| # | Task | Goal | Depends on | In scope | Preparatory | State | Document |
|---|---|---|---|---|---|---|---|
| 1 | report-download | Readers download a saved report. | — | 1 | no | {state} | [task](tasks/report-download.md) |

## Projected entries

none

## Open questions

none

## Phases

none

## Change log

- 2026-10-02 — written from the definition at fingerprint {fingerprint} — initial plan
"""

TASK = """# Download a report

Status: ready for cycle
Project relation: plan item: ../plan.md — report-download

## Description

### Need

- Readers need a copy of their saved report.

### To do

1. Let a reader download a saved report.

## Context

none

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

none

## Settlements to record

Candidates: 0 shown, 0 accepted — 2026-10-01

none

## Out of scope

none
"""

CYCLE_RECORD = """# Cycle record — Download a report

- Task source: {source} — approved 2026-10-01
- Task relation: plan item
- Product repository: {repository}
- Process pin: 0123456789abcdef
- Target branch and base: delivery, 0123456789abcdef
- Task branch: task/report-download
- Foundation route: unchanged
- Status: complete

## Sharpness at start and after the final diff

none

## Spec and plan

none

## Events

none

## Questions and autonomous choices

none

## Artifacts

| Kind | Path or commit | Author or agent | Review result |
|---|---|---|---|
| frozen task | [{frozen}]({frozen}) | Fixture | accepted |

## Verification

none

## Return step

none

## Independent assessment

none

## Request handoff

none
"""


class PlanStateEvidence(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="plan evidence ")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.remote = self.root / "remote.git"
        self.repo = self.root / "product repository"
        self.env = dict(os.environ, GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull,
                        GIT_TERMINAL_PROMPT="0", GIT_AUTHOR_NAME="Evidence fixture",
                        GIT_AUTHOR_EMAIL="fixture@example.invalid", GIT_COMMITTER_NAME="Evidence fixture",
                        GIT_COMMITTER_EMAIL="fixture@example.invalid")
        self.git(self.root, "init", "--bare", "--initial-branch=delivery", str(self.remote))
        self.git(self.root, "clone", str(self.remote), str(self.repo))
        self.write(self.repo / "README.md", "Fixture product\n")
        self.git(self.repo, "add", "README.md")
        self.git(self.repo, "commit", "-m", "Initial product")
        self.git(self.repo, "push", "-u", "origin", "delivery")
        self.git(self.repo, "remote", "set-head", "origin", "-a")
        # Original project documents deliberately live outside the product repository.
        self.docs = self.root / "project notes"
        self.plan = self.docs / "plan.md"
        self.definition = self.docs / "definition.md"
        self.task = self.docs / "tasks/report-download.md"
        self.write(self.definition, "# Report download\n\nStatus: approved 2026-10-01\n\n" +
                   DEFINITION_BODY + "## Gate record\n\n- Approved by: Fixture, 2026-10-01\n"
                   "- Foundation searched at: 0123456789abcdef\n"
                   "- Definition fingerprint: " + FINGERPRINT + "\n")
        self.write(self.task, TASK)
        self.set_state("ready for cycle")

    def git(self, directory, *arguments):
        result = subprocess.run(["git", "-C", str(directory), *arguments], env=self.env,
                                capture_output=True, text=True, encoding="utf-8", timeout=30)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return result.stdout.strip()

    @staticmethod
    def write(path, text):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(text.encode("utf-8"))

    def set_state(self, state):
        self.write(self.plan, PLAN.format(fingerprint=FINGERPRINT, state=state))

    def cycle(self, directory, source=None, frozen_text=TASK, basename="record.md"):
        source = self.task if source is None else source
        self.write(directory / basename, CYCLE_RECORD.format(
            source=source, repository=self.repo, frozen="accepted-task.md"))
        self.write(directory / "accepted-task.md", frozen_text)

    def archive(self, slug="report-download", source=None, basename="record.md"):
        relative = "docs/task-cycles/" + slug
        self.cycle(self.repo / relative, source=source, basename=basename)
        self.git(self.repo, "add", relative)
        self.git(self.repo, "commit", "-m", "Record completed cycle")
        return self.git(self.repo, "rev-parse", "HEAD")

    def worktree(self, source=None, provenance=True):
        path = self.root / "cycle worktree"
        self.git(self.repo, "worktree", "add", "--no-track", "-b", "task/report-download", str(path))
        directory = path / ".runs/task-cycles/report-download"
        directory.mkdir(parents=True)
        if provenance:
            self.cycle(directory, source=source)
        return path

    def other_plan(self):
        directory = self.root / "another project"
        self.write(directory / "plan.md", PLAN.format(fingerprint=FINGERPRINT, state="ready for cycle"))
        self.write(directory / "definition.md", self.definition.read_text(encoding="utf-8"))
        self.write(directory / "tasks/report-download.md", TASK)
        return directory / "tasks/report-download.md"

    def commit_archive_files(self):
        self.git(self.repo, "add", "docs/task-cycles/report-download")
        self.git(self.repo, "commit", "-m", "Record provenance fixture")
        self.git(self.repo, "push", "origin", "delivery")

    def task_unchecked(self):
        rows = [line for line in self.output.splitlines()
                if line.startswith("unchecked 1 report-download:")]
        self.assertTrue(rows, self.output)
        self.assertTrue(all(line.split(":", 1)[1].strip() for line in rows), self.output)

    def task_conflict(self):
        rows = [line for line in self.output.splitlines()
                if line.startswith("conflict 1 report-download:")]
        self.assertTrue(rows, self.output)
        self.assertTrue(all(line.split(":", 1)[1].strip() for line in rows), self.output)

    def run_reader(self):
        before = {path: path.read_bytes() for path in (self.plan, self.definition, self.task)}
        result = subprocess.run([sys.executable, "-B", str(READER), str(self.plan), str(self.repo)],
                                env=self.env, capture_output=True, text=True, encoding="utf-8",
                                errors="replace", timeout=60)
        for path, original in before.items():
            self.assertEqual(path.read_bytes(), original, "Reader modified " + str(path))
        self.output = result.stdout + result.stderr
        self.assertNotIn("can't open file", self.output, "Missing reader: " + self.output)
        self.proposals = [line for line in result.stdout.splitlines() if line.startswith("propose ")]
        return result.returncode

    def proposals_are(self, *expected):
        self.assertCountEqual(self.proposals, expected, self.output)

    def evidence_has(self, *facts):
        rows = "\n".join(line for line in self.output.splitlines()
                         if line.startswith("evidence 1 report-download:"))
        self.assertTrue(rows, self.output)
        for fact in facts:
            self.assertIn(fact.replace(chr(92), "/"), rows.replace(chr(92), "/"), self.output)

    def unresolved(self, *reasons):
        rows = "\n".join(line for line in self.output.splitlines()
                         if line.startswith(("unchecked", "error:", "conflict")))
        self.assertTrue(rows, self.output)
        for reason in reasons:
            self.assertIn(reason.replace(chr(92), "/").lower(),
                          rows.replace(chr(92), "/").lower(), self.output)

    def test_git_listed_worktree_proves_start_without_completion(self):
        # invariant: project-plan-state-evidence/1
        # Break caught: ignoring a listed worktree, or treating it as merged completion.
        path = self.worktree()
        self.assertEqual(self.run_reader(), 0, self.output)
        self.proposals_are("propose 1 report-download: ready for cycle -> in cycle")
        self.assertIn("task 1 report-download: ready for cycle", self.output.splitlines())
        self.evidence_has(str(path), ".runs/task-cycles/report-download")

    def test_branch_only_archive_proves_start_but_not_done(self):
        # invariant: project-plan-state-evidence/1
        # Break caught: treating an unmerged cycle-record commit as integration evidence.
        self.git(self.repo, "switch", "-c", "task/report-download")
        commit = self.archive()
        self.assertEqual(self.run_reader(), 0, self.output)
        self.proposals_are("propose 1 report-download: ready for cycle -> in cycle")
        self.evidence_has("docs/task-cycles/report-download/", commit)

    def test_fresh_remote_record_composes_both_transitions(self):
        # invariant: project-plan-state-evidence/1
        # Break caught: using stale local integration refs, or dropping the first transition.
        producer = self.root / "publisher"
        self.git(self.root, "clone", str(self.remote), str(producer))
        self.cycle(producer / "docs/task-cycles/report-download")
        self.git(producer, "add", "docs/task-cycles/report-download")
        self.git(producer, "commit", "-m", "Record delivered cycle")
        commit = self.git(producer, "rev-parse", "HEAD")
        self.git(producer, "push", "origin", "delivery")
        self.assertNotEqual(self.git(self.repo, "rev-parse", "origin/delivery"), commit)
        self.assertEqual(self.run_reader(), 0, self.output)
        self.proposals_are("propose 1 report-download: ready for cycle -> in cycle",
                           "propose 1 report-download: in cycle -> done")
        self.evidence_has("docs/task-cycles/report-download/", commit, "origin/delivery")
        self.assertIn("integration: refs/remotes/origin/delivery " + commit, self.output.splitlines())

    def test_deleted_merged_branch_still_proves_done(self):
        # invariant: project-plan-state-evidence/1
        # Break caught: requiring the original task branch after integration.
        self.git(self.repo, "switch", "-c", "task/report-download")
        commit = self.archive()
        self.git(self.repo, "switch", "delivery")
        self.git(self.repo, "merge", "--ff-only", "task/report-download")
        self.git(self.repo, "branch", "-d", "task/report-download")
        self.git(self.repo, "push", "origin", "delivery")
        self.set_state("in cycle")
        self.assertEqual(self.run_reader(), 0, self.output)
        self.proposals_are("propose 1 report-download: in cycle -> done")
        self.evidence_has(commit, "origin/delivery")

    def test_neighbour_slug_does_not_prove_progress(self):
        # invariant: project-plan-state-evidence/1
        # Break caught: matching an archive or working directory by slug prefix.
        self.archive("report-download-extra")
        self.git(self.repo, "push", "origin", "delivery")
        (self.repo / ".runs/task-cycles/report-download-extra").mkdir(parents=True)
        self.assertEqual(self.run_reader(), 0, self.output)
        self.proposals_are()
        self.unresolved()

    def test_branch_name_and_message_do_not_prove_start(self):
        # invariant: project-plan-state-evidence/1
        # Break caught: inferring a started cycle from a branch name or commit message.
        self.git(self.repo, "switch", "-c", "task/report-download")
        self.write(self.repo / "ordinary.txt", "report-download\n")
        self.git(self.repo, "add", "ordinary.txt")
        self.git(self.repo, "commit", "-m", "docs/task-cycles/report-download/ completed")
        self.assertEqual(self.run_reader(), 0, self.output)
        self.proposals_are()
        self.unresolved()

    def test_unlisted_directory_cannot_prove_start(self):
        # invariant: project-plan-state-evidence/1
        # Break caught: scanning neighbouring directories instead of Git-listed worktrees.
        (self.root / "unlisted/.runs/task-cycles/report-download").mkdir(parents=True)
        self.assertEqual(self.run_reader(), 0, self.output)
        self.proposals_are()
        self.unresolved()

    def test_failed_fetch_never_yields_completion_from_cached_record(self):
        # invariant: project-plan-state-evidence/1
        # Break caught: continuing to done from cached integration after failed fetch.
        self.archive()
        self.git(self.repo, "push", "origin", "delivery")
        self.git(self.repo, "remote", "set-url", "origin", str(self.root / "absent.git"))
        self.set_state("in cycle")
        self.assertEqual(self.run_reader(), 2, self.output)
        self.proposals_are()
        self.unresolved()

    def test_missing_remote_exposes_unestablished_integration(self):
        # invariant: project-plan-state-evidence/1
        # Break caught: guessing an integration branch when no remote establishes it.
        self.archive()
        self.git(self.repo, "remote", "remove", "origin")
        self.set_state("in cycle")
        self.assertEqual(self.run_reader(), 0, self.output)
        self.proposals_are()
        self.unresolved()
        self.assertFalse(any(line.startswith("integration:") for line in self.output.splitlines()), self.output)

    def test_missing_remote_head_does_not_guess_delivery(self):
        # invariant: project-plan-state-evidence/1
        # Break caught: guessing the integration ref from the checked-out branch.
        self.archive()
        self.git(self.repo, "push", "origin", "delivery")
        self.git(self.repo, "symbolic-ref", "--delete", "refs/remotes/origin/HEAD")
        self.git(self.remote, "symbolic-ref", "HEAD", "refs/heads/absent")
        self.set_state("in cycle")
        self.assertEqual(self.run_reader(), 0, self.output)
        self.proposals_are()
        self.unresolved()

    def test_another_remote_does_not_obscure_declared_origin_integration(self):
        # invariant: project-plan-state-evidence/1
        # Break caught: losing valid origin completion evidence because another remote exists.
        commit = self.archive()
        self.git(self.repo, "push", "origin", "delivery")
        self.git(self.repo, "branch", "other-delivery")
        self.git(self.repo, "push", "origin", "other-delivery")
        other = self.root / "other.git"
        self.git(self.root, "clone", "--bare", str(self.remote), str(other))
        self.git(other, "symbolic-ref", "HEAD", "refs/heads/other-delivery")
        self.git(self.repo, "remote", "add", "other", str(other))
        self.git(self.repo, "fetch", "other")
        self.git(self.repo, "remote", "set-head", "other", "-a")
        self.git(self.repo, "config", "--unset", "branch.delivery.remote")
        self.git(self.repo, "config", "--unset", "branch.delivery.merge")
        self.set_state("in cycle")
        self.assertEqual(self.run_reader(), 0, self.output)
        self.proposals_are("propose 1 report-download: in cycle -> done")
        self.evidence_has(commit, "origin/delivery")
        self.assertIn("integration: refs/remotes/origin/delivery " + commit, self.output.splitlines())

    def test_unavailable_listed_worktree_is_visible(self):
        # invariant: project-plan-state-evidence/1
        # Break caught: silently dropping an unavailable worktree and claiming a complete reading.
        path = self.worktree()
        shutil.rmtree(path)
        self.assertEqual(self.run_reader(), 0, self.output)
        self.proposals_are()
        self.unresolved(str(path))

    def test_shallow_history_cannot_prove_done(self):
        # invariant: project-plan-state-evidence/1
        # Break caught: reporting completion from an incomplete shallow history.
        self.archive()
        self.git(self.repo, "push", "origin", "delivery")
        shallow = self.root / "shallow product"
        self.git(self.root, "clone", "--depth=1", self.remote.as_uri(), str(shallow))
        self.repo = shallow
        self.set_state("in cycle")
        self.assertEqual(self.run_reader(), 0, self.output)
        self.proposals_are()
        self.unresolved()

    def test_done_row_with_live_cycle_is_reported_as_conflict(self):
        # invariant: project-plan-state-evidence/1
        # Break caught: normalizing contradictory live-cycle evidence for a done task.
        self.worktree()
        self.set_state("done")
        self.assertEqual(self.run_reader(), 1, self.output)
        self.proposals_are()
        self.assertTrue(any(line.startswith("conflict 1 report-download:")
                            for line in self.output.splitlines()), self.output)

    def test_draft_plan_gives_no_progress_proposal(self):
        # invariant: project-plan-state-evidence/1
        # Break caught: proposing cycle progress before a plan has been handed over.
        self.worktree()
        self.write(self.plan, self.plan.read_text(encoding="utf-8").replace(
            "Status: handed over 2026-10-02", "Status: draft"))
        self.assertEqual(self.run_reader(), 1, self.output)
        self.proposals_are()

    def test_unapproved_definition_gives_no_progress_proposal(self):
        # invariant: project-plan-state-evidence/1
        # Break caught: proposing progress for a definition without approval.
        self.worktree()
        self.write(self.definition, self.definition.read_text(encoding="utf-8").replace(
            "Status: approved 2026-10-01", "Status: ready for gate"))
        self.assertEqual(self.run_reader(), 1, self.output)
        self.proposals_are()

    def test_invalid_plan_gives_no_progress_proposal(self):
        # invariant: project-plan-state-evidence/1
        # Break caught: proposing progress despite an unreadable task table structure.
        self.worktree()
        self.write(self.plan, self.plan.read_text(encoding="utf-8").replace("## Tasks", "## Missing tasks"))
        self.assertEqual(self.run_reader(), 1, self.output)
        self.proposals_are()

    def test_unreadable_definition_gives_no_progress_proposal(self):
        # invariant: project-plan-state-evidence/1
        # Break caught: proceeding with cycle evidence when the definition cannot be read.
        self.worktree()
        self.definition.unlink()
        # Preserve all inputs that remain readable; the missing source is intentional.
        before = (self.plan.read_bytes(), self.task.read_bytes())
        result = subprocess.run([sys.executable, "-B", str(READER), str(self.plan), str(self.repo)],
                                env=self.env, capture_output=True, text=True, encoding="utf-8",
                                errors="replace", timeout=60)
        self.assertNotIn("can't open file", result.stderr, "Missing reader: " + result.stderr)
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        self.assertFalse(any(line.startswith("propose ") for line in result.stdout.splitlines()))
        self.assertEqual((self.plan.read_bytes(), self.task.read_bytes()), before)

    def test_identity_bearing_archive_has_no_mandatory_record_basename(self):
        # invariant: project-plan-state-evidence/1
        # Break caught: rejecting valid provenance solely because its record has another basename.
        commit = self.archive(basename="delivery-notes.md")
        self.git(self.repo, "push", "origin", "delivery")
        self.assertEqual(self.run_reader(), 0, self.output)
        self.proposals_are("propose 1 report-download: ready for cycle -> in cycle",
                           "propose 1 report-download: in cycle -> done")
        self.evidence_has(commit, "docs/task-cycles/report-download/", "origin/delivery")

    def test_other_plans_integrated_same_name_cannot_start_current_task(self):
        # invariant: project-plan-state-evidence/1
        # Break caught: treating a plan-local slug as globally identifying an integrated cycle.
        other = self.other_plan()
        self.archive(source=other)
        self.git(self.repo, "push", "origin", "delivery")
        self.assertEqual(self.run_reader(), 1, self.output)
        self.proposals_are()
        self.task_conflict()

    def test_frozen_task_identity_does_not_require_current_content_equality(self):
        # invariant: project-plan-state-evidence/1
        # Break caught: discarding an owned historical cycle after a source-only editorial change.
        commit = self.archive()
        self.git(self.repo, "push", "origin", "delivery")
        self.write(self.task, TASK.replace("Readers need a copy of their saved report.",
                                           "Readers need a downloadable copy of their saved report."))
        self.assertEqual(self.run_reader(), 0, self.output)
        self.proposals_are("propose 1 report-download: ready for cycle -> in cycle",
                           "propose 1 report-download: in cycle -> done")
        self.evidence_has(commit, "origin/delivery")

    def test_other_plans_integrated_same_name_cannot_complete_current_task(self):
        # invariant: project-plan-state-evidence/1
        # Break caught: borrowing completion and commit evidence from another same-named task.
        other = self.other_plan()
        self.archive(source=other)
        self.git(self.repo, "push", "origin", "delivery")
        self.set_state("in cycle")
        self.assertEqual(self.run_reader(), 1, self.output)
        self.proposals_are()
        self.task_conflict()

    def test_other_plans_live_same_name_cannot_start_current_task(self):
        # invariant: project-plan-state-evidence/1
        # Break caught: using a Git-listed live cycle whose recorded source belongs to another plan.
        self.worktree(source=self.other_plan())
        self.assertEqual(self.run_reader(), 1, self.output)
        self.proposals_are()
        self.task_conflict()

    def test_live_directory_without_provenance_cannot_start_task(self):
        # invariant: project-plan-state-evidence/1
        # Break caught: using a bare same-named live directory as proof of task ownership.
        self.worktree(provenance=False)
        self.assertEqual(self.run_reader(), 0, self.output)
        self.proposals_are()
        self.task_unchecked()

    def test_archived_header_alone_cannot_prove_task_ownership(self):
        # invariant: project-plan-state-evidence/1
        # Break caught: accepting a cycle title and task slug without recorded provenance.
        self.write(self.repo / "docs/task-cycles/report-download/delivery-notes.md",
                   "# Cycle record — Download a report\n\n- Status: complete\n")
        self.commit_archive_files()
        self.assertEqual(self.run_reader(), 0, self.output)
        self.proposals_are()
        self.task_unchecked()

    def test_archived_content_without_provenance_cannot_complete_task(self):
        # invariant: project-plan-state-evidence/1
        # Break caught: treating any integrated file in the exact directory as an owned cycle.
        self.write(self.repo / "docs/task-cycles/report-download/notes.txt", "Delivered report-download.\n")
        self.commit_archive_files()
        self.set_state("in cycle")
        self.assertEqual(self.run_reader(), 0, self.output)
        self.proposals_are()
        self.task_unchecked()

    def test_unanchored_same_basename_provenance_remains_unchecked(self):
        # invariant: project-plan-state-evidence/1
        # Break caught: resolving ambiguous task/plan basenames by choosing a same-named project.
        self.other_plan()
        self.cycle(self.repo / "docs/task-cycles/report-download", source="tasks/report-download.md")
        self.commit_archive_files()
        self.assertEqual(self.run_reader(), 0, self.output)
        self.proposals_are()
        self.task_unchecked()


if __name__ == "__main__":
    unittest.main()
