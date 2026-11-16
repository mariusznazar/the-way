# Handoff — the one author of the change

## Delegation

The cycle's orchestrator runs this task for the human, who delegated every intermediate choice to
it. Nothing you are told here or answered later is the human's approval. Do not ask the human
anything; send questions to the orchestrator in your report with the status `questions`.

## Where you work

- Worktree: `the root of the task's worktree`, branch
  `task/renumber-decisions-on-merge`, base `1feb483cbb5a6538a475d6e42629441ba563d7f8`. Work from the
  worktree's root only. No other agent writes in it while you work.
- Your directory for working copies: `.runs/author/` of the worktree.
- Your report: `.runs/task-cycles/renumber-decisions-on-merge/reports/author-report.md`.

## Your method and variant

Read `task-cycle/change/SKILL.md` (`make-change`) of this worktree, whole, and take its variant
"the whole change as the one author". Read a file it names only when the step or variant that names
the file comes. You have no skill tool: read a method by its path.

## The stage and its boundary

Make the whole change of the task, with its foundation entries (the foundation step:
`task-cycle/skill/foundation_step.md`, read whole; and the `SKILL.md` of an element, named there,
when you write an entry of that element). Commit your work on the task branch, by path
(`git add <file> <file>`, never `git add -A`; commit messages in English). Return before any review.
You do not run the product's gate (`python -B gate/run_tests.py` with no directory); it is the
cycle's, and its final run is CI's. Run focused checks of the directories you touch only.
You do not take the return step now; the cycle resumes you for it.

## The task

The frozen task is `.runs/task-cycles/renumber-decisions-on-merge/task.md`; read it whole. It is
`Project relation: independent`. *Human actions*: none. *Questions carried to cycle*: none.

## Answers of the orchestrator's step 4

- Trust boundary: no. Irreversible operation: no.
- Open design choice: none. Reserved choice: none. Route: one author, no plan. No spec was written.
- Your class: `same` as the orchestrator's (sonnet), because the change writes a decision entry whose
  form `elements/common/foundation_check.py` holds, with rejected ways and its verification, and
  asks for the search of the whole foundation (WAY-33).

## What the orchestrator found that the task does not say

1. The task's *Decisions in play* names WAY-306, WAY-357 and WAY-328. They are withdrawn in the log
   since the task was accepted (table of withdrawn identifiers at the end of
   `foundations/decisions.md`): WAY-306's rule now stands in `task-cycle/skill/correction.md`,
   WAY-357's in `task-cycle/record_template.md`, and WAY-328 ended and WAY-379 and WAY-392 stand
   after it. Do not link a withdrawn number as a live decision; the new decision's *Relations*, and
   any text you write, name only entries the log holds. Where the task's *Rejected* wording leans on
   a withdrawn decision, take its meaning from the task, not from the log.
2. The next free decision number is WAY-403 (the highest in the log is WAY-402). Another running
   cycle may be taking numbers too; renumbering is the very case the new decision serves. Use the
   next free number of the base you work on.
3. WAY-293 says that in the log of the-way a rule that stands in one skill stands there with one
   sentence of its reason, and is an entry of the log only where it carries a choice with a real
   cost; the skill then names the decision. *Settlements to record* row 1 settles that this rule is
   an entry (question 4 of the task), so write it, and let step 12 and `correction.md` name it.

## What to read

The whole frozen task above. The foundation, selected by "Reading the foundation" in
`elements/common/way_of_working.md`; the orchestrator's selection:

- Parts touched: `task-cycle` (`task-cycle/skill/SKILL.md`, `task-cycle/skill/correction.md`) and
  `decisions` (`foundations/decisions.md`); a part-map line only if you find one that no longer
  matches.
- Decisions, open whole: WAY-19 (numbering), WAY-02 (references by identifier), WAY-05 (form of an
  entry), WAY-12 (how a decision is checked, and when it is held), WAY-18 (the log), WAY-22, WAY-36,
  WAY-293, WAY-294 (process remarks), WAY-11, WAY-150, WAY-161, WAY-162, WAY-135.
- The index of the orchestrator's selection, for the rest:
  `.runs/orchestrator/index.md` (written by `elements/common/decision_index.py`); write and read
  your own for what you add.
- The decisions' element: `elements/decisions/template.md`, `elements/decisions/examples.md` and
  `elements/decisions/skill/SKILL.md`; and `elements/common/rules.md`.
- Guidelines: the change as planned is text only. If you find it must touch code, read
  `guidelines/coding.md` first, and `guidelines/testing.md` before a test.
- The text you change: step 12 of `task-cycle/skill/SKILL.md` (the paragraph that begins "Otherwise
  merge the remote target branch into the task branch"), `task-cycle/skill/correction.md` (the
  paragraph that begins "In the-way itself, before anything else" and the one that begins "Take a
  link to the request"), and `task-cycle/record_template.md` only if the *Events* wording needs a
  line for the renumbering row; do not widen the task beyond its *To do* 1–4.

## Working copies (word for word)

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

## What your report must hold

As `task-cycle/change/SKILL.md` gives it, and, as the cycle requires of every report: status, your
commits, a one-line check result with the command and exit code of every check, the **Unread
material** and the **Searches not found or unclear** sections (each `none` or the items), your
own-work check, and the working copies. For each foundation entry you write: one sentence of its
meaning in English and one in Polish, and its mark (`row <n>`, `projected` or `the cycle's`).
Also state how the change makes the rule hold for the target-branch merges of both the one-author
and the planned route, and which text of the skill you changed, by file and heading.
