# Handoff — review of the whole change

You are the reviewer of the whole change in a task cycle of the-way, an agent that did not make it.
The person who requested the cycle has delegated intermediate choices to the orchestrator; no human
is available during the cycle. Return `questions` to the orchestrator where you have one.

## What to review

- Worktree (work from its root): `the root of the worktree`,
  branch `task/weak-point-in-every-decision-question`.
- Method: `task-cycle/review/SKILL.md` (`review-change`), read whole; a file it names only when the
  step that names it comes. Variant: the review of the whole change.
- Range: base `bfb2e109735b5fff98802b8be0ff3c43c799262a` to head `a3c97df` (two commits, `a14b07f`
  for `foundations/decisions.md` and `a3c97df` for 19 other files). Read the full diff.
- Frozen task, read whole: `.runs/task-cycles/weak-point-in-every-decision-question/task.md`
  (Polish; the files of the-way are English). Check every item of *To do* 1–7, every row of
  *Settlements to record* 1–8 and the answers to *Questions to settle* 1–9 against the diff. The
  change has no spec and no plan (one author, no slices); the change was judged by the orchestrator
  to hold no open design choice.
- The author's report, read whole: `.runs/task-cycles/weak-point-in-every-decision-question/reports/author-report.md`.
  Its choices that go beyond the literal *To do* and need your judgment: WAY-155, WAY-174 and
  WAY-378 reworded and WAY-378 given a relation `derives from WAY-113`; `project-level/task/skill/final_review.md`
  changed; a new bullet on project definitions in "How a skill asks"; the refinement sentence of
  WAY-113 moved to a second paragraph; `foundation-review/with_the_human.md` items 1–4 shortened;
  the *Decided* outcome added to the audit note; `product-guidelines/{coding,styleguide}/settle.md`
  changed though not on the task's list. It also lists the places it looked at and left, in its
  section "To do 4 — places looked at and left": judge whether any of them restates the rule.
- Answers of step 4 of the cycle: the change touches no trust boundary and holds no operation that
  cannot be undone.
- Reach beyond the author's handoff, for you: the author read WAY-378 whole, found by the search of
  the whole foundation (WAY-33); the author left unread the part-map entries of the touched parts
  and the orchestrator's index of decisions — you select the foundation and the guidelines for your
  own review by "Reading the foundation" in `elements/common/way_of_working.md` (the-way has no
  product guidelines for these files).
- Checks run by the author (focused directories and `foundation_check.py`) are in its report. The
  product's full gate is the orchestrator's and has not run yet on this tree; do not run
  `python -B gate/run_tests.py` with no directory.
- The task asks the cycle to show the strongest argument against a proposal; judge, among other
  things, whether the changed texts are consistent with each other (WAY-113 *Verification*,
  "How a skill asks", the request template's item parts, the audit's step 3), whether the weak
  point and the cost of undoing are stated once and pointed to elsewhere, and whether the change
  contradicts any untouched decision or text.

## Where to write

- Directory for your working copies: `.runs/review-whole/`.
- Report path: `.runs/task-cycles/weak-point-in-every-decision-question/reports/review-whole-report.md`;
  its first line is `PASS <sha>` or `FAIL <sha>`, followed by what the method gives, with **Unread
  material** (for you, your own selection) and **Searches not found or unclear**.

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
