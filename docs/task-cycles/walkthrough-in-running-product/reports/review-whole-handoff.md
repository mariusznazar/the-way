# Handoff to the reviewer of the whole change — task `walkthrough-in-running-product`

You review the whole change of a task cycle of the-way as an agent that did not make it, with the
method `review-change`. You are read-only: you change no file of the worktree, commit nothing and
return PASS or FAIL with graded findings and the checks you ran. You never run the product's full
gate (its run is CI's), never start another stage and never ask the human anything; a question goes
to the orchestrator as your report's status `questions` gives it.

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator; none of
its answers is the human's approval. Write your report in English.

## What you review

- Worktree: `the task's worktree`, branch
  `task/walkthrough-in-running-product`. Work from its root.
- Range: base `9cffc9bad7f9b8ebfa8091a24a49c9de81c6ac53` to head `940893de` (confirm
  `git rev-parse HEAD`), one commit; compute the diff and the log yourself.
- Method: read `task-cycle/review/SKILL.md` whole and, as it says, `task-cycle/review/whole_change.md`
  and follow it; read any other file it names only when its step comes. Your variant: **the whole
  change** (no spec, no plan, no slice: one author without a plan).
- Frozen task, read whole: `.runs/task-cycles/walkthrough-in-running-product/task.md` (Polish; the
  files of the change are English). Check every *To do* item 1-8, every row of *Settlements to
  record* 1-11 and the *Out of scope* list, and the fidelity of the author's wording to the
  task's (the task is the only authority; an invented requirement, criterion or decision is a
  finding, and so is a task requirement left out).
- The author's report, a set of claims to verify and not evidence:
  `.runs/task-cycles/walkthrough-in-running-product/reports/author-report.md`. It names its own
  uncertain points: the split of rows 1-5 into three decisions (WAY-406, WAY-407, WAY-408), the
  adoption of the `test-run` and course practices stated in the *Rationale* of WAY-406 and the
  *Rejected* it carries (whether any of it is "a way the writer derives", WAY-134), the pairs of
  examples it wrote (`the cycle's`), and the references in the task that do not match the files
  (WAY-140, the paragraph "Where a change alters what a screen shows").
- Trust boundary: no. Irreversible operation: no.
- Task cycle facts you may need: the change is text only (no script, no test changed); the
  author ran the focused tests of `task-cycle`, `project-level`, `elements/common` and
  `agent-instructions` and the foundation check (all exit 0, per its report); no full gate ran
  yet. The request is not written yet.

## What you select yourself

You alone among the reviewers select your own foundation and guidelines (WAY-150, WAY-213): the
entries of the parts the change touches by "Reading the foundation" in
`elements/common/way_of_working.md`, and the guidelines of those parts by
`product-guidelines/reading.md`. The change touches the parts `task-cycle`, `decisions`, `glossary`
(the entry in `foundations/glossary.md`) and `project-level`, and writes entries of the decision
log, including changes to WAY-121 and WAY-319. Write the index of your whole selection with
`elements/common/decision_index.py` in your directory below and state in your report how many
decisions you read whole. Check among other things: the form of the new entries against
`elements/decisions/template.md`, `elements/common/rules.md` and the decision element's skill; that
each new or changed binding sentence is one the task settles (no widening); that the foundation's
other entries still agree with them (WAY-33); that `python -B elements/common/foundation_check.py`
is clean; the new method file against `task-cycle/change/ui_check.md` as its model, and against
every point of the task's items 1-2 (preparation, scope, plan of cases in the order of conditions,
execution, verdict per case with the layer, "what I did not check", comparison of two
measurements, the rules of the walk); that the readers are named as the task says (the one author
and the executor of a slice; not the fix); that no file the change commits holds an absolute path
or a note title of a private source.

## Your report

Write it to `.runs/task-cycles/walkthrough-in-running-product/reports/review-whole-report.md`. Its
first line is `PASS <sha>` or `FAIL <sha>` (the head you reviewed), then as the method gives:
graded findings (with, for each blocking finding, a mark `Contradiction: yes` where it is a
contradiction with the settlements of the task or the foundation; the slice it comes from is
`none`: there is no plan), the Minor findings within the task and those outside its scope kept
apart, the checks you ran with command and exit code, the number of decisions you read whole,
**Unread material** (what this handoff names or your own selection that stayed unread or was read
in part, or `none`) and **Searches not found or unclear** (each thing you looked for and did not find
or found unclear, or `none`), and your working copies. Return: the first line of the report, the
changed files with their line counts, the checks, and the report's path.

Your directory for working copies: `.runs/review-whole/`.

The files of the cycle's record directory `.runs/task-cycles/walkthrough-in-running-product/`
other than the two this handoff names, `cycle.md` among them, are not yours to read.

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
