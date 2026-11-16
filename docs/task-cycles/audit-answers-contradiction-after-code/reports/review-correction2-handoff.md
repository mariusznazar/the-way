# Handoff to the reviewer of correction 2

You are a fresh reviewer: you did not make the change and did not write any earlier review of it.
Ask the human nothing; a question goes to the orchestrator in your report as `questions`.

## What you review

- The worktree (read-only for you): `the root of the task's worktree`.
- Method: `task-cycle/review/SKILL.md` (`review-change`), variant "the review of a correction for the
  human's remarks": read `task-cycle/review/fix.md` as the method says; the remarks stand in place of a
  findings file.
- The range: base `2e31b74b1a0dd3c9c787ed79a025bb7f372615a6` (the merge of the target branch, being reviewed
  by another agent, not by you) to head `17065c8b` (`git rev-parse 17065c8b` gives the full identifier).
  Two commits: `1fbb9cc4` (remark 1) and `17065c8b` (remark 2). The diff to review is
  `git diff 2e31b74b 17065c8b` (6 files).
- The remarks, word for word (they bind):
  `.runs/task-cycles/audit-answers-contradiction-after-code/reports/correction-2-remarks.md`.
- The handoff the author received (what it was asked, including the reading of the human's words on
  remark 2): `.runs/task-cycles/audit-answers-contradiction-after-code/reports/author-correction2-handoff.md`.
- The author's report (claims to verify, not evidence):
  `.runs/task-cycles/audit-answers-contradiction-after-code/reports/author-correction2-report.md`.
- The seven small remarks of remark 2 stand word for word in the section *Minor findings* and the section
  *Findings outside the task's scope* of `.runs/task-cycles/audit-answers-contradiction-after-code/request.md`
  and in the reports the author's handoff names (the review reports in the same `reports/`).
- The frozen task: `.runs/task-cycles/audit-answers-contradiction-after-code/task.md`.
- Your report: `.runs/task-cycles/audit-answers-contradiction-after-code/reports/review-correction2-report.md`.
  Your directory for working copies: `.runs/review-correction-2/`.

## What to judge

1. **Remark 1.** The sentence "unless it reads `none` or opens with ..." must now stand in the four places
   the remark names (WAY-405's binding sentence, its *Verification* clause, and the two comments in
   `process-audit/audit_count.py` and `process-audit/record_items.py`), and say what the code does
   (`discarded_reason` gives "no attempt" for `none`). Search the repository for any other place that
   still says the old, wider sentence (the template's item *Discarded attempt*, `process-audit/SKILL.md`,
   `task-cycle/skill/*.md`, other entries).
2. **Remark 2.** For each of the seven shapes: the author chose between fixing the code and making the rule
   say what the code does, by the human's words ("Where a fix would change what the audit answers, make
   the rule say what the code does and add the test; do not widen the change beyond these"). Judge each
   choice, that the rule's new text is true of the code (probe it), and that each new test holds what the
   rule says and fails when the code behind it is broken. The author's one flagged judgment call: the
   second attempt with a malformed reason word under a first attempt left as plain text, read as a detail
   of the first. Judge whether the rule states it honestly.
3. **Nothing widened, nothing lost.** The code's executable behaviour must be unchanged (the author claims
   the syntax trees without docstrings equal those at `2e31b74b`; verify). No earlier answer changes; the
   tests that held WAY-337, WAY-344, WAY-404 and WAY-405 still stand. Crafted input at the trust boundary
   `process-audit/record_items.py` (this task's *Two questions at start*: yes) gives no hang, no crash and
   no new wrong `yes` or `no`.

A finding is blocking where a sentence of the rule says more or less than the code does, or a remark is not
carried out; the human has named wider-than-the-code wording as the thing to remove. Say for each blocking
finding whether it contradicts an entry of the foundation or a settled answer of the task document.

## Checks

Focused checks only, in a worktree of the head in your directory: `python -B gate/run_tests.py process-audit`,
`python -B gate/run_tests.py task-cycle`, `python -B elements/common/foundation_check.py` without
`--skip-test-citations`. **Do not run the product's full gate.** Report each check with its command and
exit code.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
in the system's temporary directory, in the scratch directory of a session or in the main checkout
of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by
itself under its session's directory is moved into the agent's directory and the original removed,
except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md`
says, to the place the product's foundation settles for screenshots, and into the agent's directory
only where no such place is settled. The files that a product's own tools and tests make by
themselves are no working copy of the agent and stay outside this rule. Before the agent returns,
each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then
`git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in
the report where each copy stood and that it was removed. Where a removal fails, the agent finishes
all the same and names in the report the remainder, with its full path and the reason it stayed.

## The report

First line `PASS <sha>` or `FAIL <sha>` (or `questions`); graded findings with places in the code;
checks with commands and exit codes; **Unread material**; **Searches not found or unclear**; the line on
your working copies. Return the first line, a one-line check result and the report's path.
