# Handoff — review of the whole change

You are a fresh reviewer of the whole change of task `installer-preview-ignores-line-endings`, as
`the-way-stage`. You made none of it. The person who requested this cycle delegated the
intermediate choices to the orchestrator; nothing here is that person's approval.

## Where you work

- Worktree (work from its root): `the task's worktree`,
  branch `task/installer-preview-ignores-line-endings`.
- Range to review: base `9cc26f3eb5121c19be28e647170019982d2b08c7` to head `b2c31cc2` (one commit,
  `installation/install.py`, `installation/test_install.py`, `installation/README.md`).
- The directory for your working copies: `.runs/review-whole/` of the worktree.
- Your report: `.runs/task-cycles/installer-preview-ignores-line-endings/reports/review-whole-report.md`
  (its first line is `PASS <sha>` or `FAIL <sha>`).

## Working copies (word for word from the cycle's skill)

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

## Method

- Method: `task-cycle/review/SKILL.md` in this worktree (`review-change`), the variant of the review
  of the whole change. Read that `SKILL.md` whole, and a file it names, one beside it included, only
  when the step or variant that names the file comes.
- `cycle.md` and the other files of the cycle's record directory (other agents' handoffs, reports and
  findings) are not yours to read unless this handoff names them. Named here: the author's report,
  `reports/author-report.md`, beside this handoff.
- The review is read-only: change no tracked file. Run no full gate (`python -B gate/run_tests.py`
  with no directory); the orchestrator and CI run it. You may run the tests of one directory,
  `python -B gate/run_tests.py installation`, and focused checks of your own in your directory.
- Select your own foundation and guidelines by the parts of the change (`installation`), as
  `elements/common/way_of_working.md` "Reading the foundation" gives; write and read the index of your
  whole selection and state in the report how many decisions you read whole (WAY-150).

## What you review against

- The frozen task: `.runs/task-cycles/installer-preview-ignores-line-endings/task.md`, read whole.
  Its one *To do* item: a file the installer writes in a product that differs from the new content only
  in line endings (CRLF instead of LF) gets `KEEP` in the preview, with no diff beneath it, is not
  rewritten, and where no file changes and the pin does not move, the installer answers "Already
  installed; no changes". Out of scope: a file with a real change is still written with LF; the git
  setting on the author's computer stays.
- No spec and no plan: the task leaves no open design choice and the change fits one author.
- Foundation: the task's *Decisions in play* names WAY-34 and WAY-328; WAY-328 is withdrawn (replaced
  by WAY-379 · WAY-392), so the-way's own coding and testing guidelines apply (`guidelines/coding.md`,
  `guidelines/coding-repository-changer.md`, `guidelines/testing.md`).
- The author's report: `reports/author-report.md` (its choices 1–9, its before/after test runs and
  its note that the linter reports 8 blocking rules on the installation part that predate the change).
  Treat its claims as claims; check them.

## Answers of step 4 that bind your review

- Trust boundary: **yes** — `installation/install.py` is the boundary the part map names for
  `installation`. Check crafted input at it: a file in the product with CRLF, lone CR, mixed endings, a
  file that is not UTF-8, an empty file, a file reached through a link, a file whose last line ending is
  missing — what the new comparison does with each, and that nothing that was refused or replaced
  before is now kept wrongly (a file whose text really differs must never be `KEEP`).
- Irreversible operation: **no**; the change makes no such operation.
- The change adds no line to `run()` (already over WAY-385's threshold); check that, and the size
  thresholds for the changed files.
- The change adds a sentence to `installation/README.md`, a file the handoff to the author did not
  name; judge whether it is true, needed, and whether the README holds another sentence the change
  makes false.
- Judge the tests against the testing guidelines: the level chosen, the break each test names, whether
  the expected values are literals and no value is computed by the code under test, and whether the new
  tests fail on the old code (run them against `9cc26f3e` in a working copy of your own to see it).
- A finding you grade and scope yourself; the orchestrator moves none. Report each blocking finding
  with the reviewer's mark of contradiction with the settlements (`Contradiction: yes` or `no`).

## Report

As the method gives: first line `PASS <sha>` or `FAIL <sha>`; graded findings with `file:line`; the
checks you ran, each with its command and exit code; **Unread material**; **Searches not found or
unclear** (each `none` where there is none); the line on your working copies.
