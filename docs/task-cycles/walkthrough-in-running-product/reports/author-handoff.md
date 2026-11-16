# Handoff to the one author — task `walkthrough-in-running-product`

You are the one author of this change, without a plan. You do the code, the foundation step and
nothing else; you return at your boundary. You never start the next stage, never run the product's
full gate (its run is the orchestrator's or CI's), and never ask the human anything: questions go to
the orchestrator in your report with status `questions`.

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator. The
orchestrator answers your questions from the task, its sources, the foundation and the code; none of
its answers is the human's approval. Write every file of the repository in English (the task
document is in Polish; the files you change are not).

## Where you work

- Worktree: `the task's worktree` — work from its root, never
  in the main checkout `the main checkout of the-way`.
- Branch: `task/walkthrough-in-running-product`, base commit `9cffc9bad7f9b8ebfa8091a24a49c9de81c6ac53`
  (target branch `foundations`).
- Your directory for working copies: `.runs/author/` (see the paragraph "Working copies" below).
- Your report: `.runs/task-cycles/walkthrough-in-running-product/reports/author-report.md`.
- Commit by path (`git add <path> ...`, never `git add -A`, `git add .` or `git commit -a`), with
  commit messages in English. Never commit anything under `.runs/`.
- The files of the cycle's record directory `.runs/task-cycles/walkthrough-in-running-product/`,
  other agents' handoffs, reports and findings and `cycle.md` are not yours to read. The only file
  of it you read is the frozen task named below.

## Your method and variant

Read `task-cycle/change/SKILL.md` of this worktree whole, and a file it names — one beside it
included — only when the step or variant that names the file comes. Your variant, in the words of
its row: **"the whole change as the one author"**.

For the foundation step, read `task-cycle/skill/foundation_step.md` whole; and, when you write an
entry of an element, read that element's `SKILL.md` at the path `foundation_step.md` gives, whole.
For your return before review, nothing more is asked of you than your method gives: the return step
comes later, as a separate dispatch.

## The task

Frozen task: `.runs/task-cycles/walkthrough-in-running-product/task.md` — read it whole. It is the
only authority for what to make: *To do* items 1–8, the answered *Questions to settle*, *Settlements
to record* rows 1–11 (all accepted by the task's owner at the readiness gate) and *Out of scope*.
`Project relation: independent`. No spec and no plan exist: the orchestrator found no open design
choice. The one choice the task leaves to you is the name of the new method file (the task says
only "a file beside the author's skill, on the model of `task-cycle/change/ui_check.md`");
recommended: `task-cycle/change/walkthrough.md`. A choice of how to make what the task settles is
yours: make it and name it in your report; the orchestrator enters it in its record.

Answers of the cycle's start:

- Trust boundary: no. The files changed are texts, the foundation and templates; none of the
  boundary files the part map names (`task-cycle/cycle_stages.py`, `installation/install.py`, …) is
  touched. If your work reaches one, say so in the report.
- Irreversible operation: no.
- Open design choice: none. Reserved choice: none.
- The move of the pin: not applicable (this is the-way itself); no check failing on the base is
  carried to you except the flaky `task-cycle/test_remove_merged_worktrees.py` test named in
  the earlier cycle's CI run, which this change does not touch.

## What to read, selected by the orchestrator

Foundation, by identifier — the decisions of the task's *Decisions in play*: WAY-164, WAY-121,
WAY-165, WAY-227, WAY-238, WAY-239, WAY-13, WAY-140, WAY-287, WAY-316, WAY-166, WAY-319, WAY-373,
WAY-125, WAY-256, WAY-293 and WAY-100, in `foundations/decisions.md`. The orchestrator wrote an index
of a wider selection (the parts `task-cycle`, `decisions` and `project-level` and seven sections of
the log) with the script `elements/common/decision_index.py`: `.runs/orchestrator/index.md`. Read it,
open whole only the decisions you change, go against or find open (WAY-121, WAY-319 and the decision
you write among them; of one you change or answer otherwise, the *Rejected* too), and add by the
same method what your own foundation step needs (`elements/common/way_of_working.md`, "Reading the
foundation"). Read the part map entries of the parts you touch (`foundations/part_map.md`:
`task-cycle`, `decisions`, `project-level`, and the parts of the glossary entry you edit), the
invariants whose *Part* names them and the glossary entry "agent's way to the running product" in
`foundations/glossary.md`.

Files you will change or model yours on (read each whole before you change it): the files the task
names — `task-cycle/change/ui_check.md` (model, stays unchanged), `task-cycle/change/SKILL.md`
(sections 3 and 6), `task-cycle/review/SKILL.md` ("The author's own-work check"),
`task-cycle/skill/request_template.md` (item 4, the paragraph beginning "Where a change alters what
a screen shows", item 8), `elements/decisions/template.md` ("Where it goes"), `foundations/decisions.md`
(WAY-121, WAY-319, and the new decision or decisions), `foundations/glossary.md`,
`project-level/technology/research.md`.

Guidelines of the-way's own code: read `guidelines/coding.md` before you change any code, and
`guidelines/testing.md` before you write or change a test. The change is expected to be text; if a
script of the cycle that reads the files you change (for example `task-cycle/request_check.py` on
`request_template.md`, or a test of the skills' entry points or of the size of a skill) is reached
by it, read the guidelines and keep that script and its tests consistent, and name the reach.

Sources outside the repository you read, because the task names them: the model for the method —
`the skill `test-run` of a team repository, which is not in this repository` (a team repository, not open to a reader
of the-way) — and, for the items of the 12.11.2026 addendum the task takes over, the sections named
in the task (D21 in `the author's private note on the practices of the first course`
and section U4 in `the author's private note on the practices of the second course`).
Take from them only what the task's settlements say is adopted, and nothing else
("the source is the only authority", the task's *Out of scope* included). **No file you commit
holds an absolute path or the path or title of a private note**: a decision that adopts the method
(WAY-100) describes in its *Rationale* what was seen in the source and says that the source is not
open to a reader of the repository (WAY-27).

## What to make — the task's items in the order of dependence

1. The foundation step: the *Settlements to record* of the task. Rows 1–5 go to the decision log as
   a decision or decisions (the number and the split are yours, by the decision element's skill and
   WAY-293); rows 6–8 go to the method file, and the practices taken from `test-run` and the courses
   bind the-way only through a decision that names what is adopted, where it applies and why
   (WAY-100) — one of your decisions says it; row 9 is a sentence of WAY-121 and the same sentence
   in the template of decisions (*To do* 6); row 10 is the glossary entry (*To do* 7); row 11 is a
   sentence of WAY-319 (*To do* 8). Where the decision log is divided into topical sections, put
   a new decision into the section whose sentence fits it.
2. The method file and the pointers (*To do* 1–3): the file; the point in section 3 of
   `task-cycle/change/SKILL.md` that names the readers (the one author and the executor of a slice;
   the fix of a review's findings reads nothing of it); the report's content in section 6.
3. The review's reading of the report (*To do* 4) and the request's pieces (*To do* 5).
4. The technology step (*To do* 8): `project-level/technology/research.md`, point 3.

After the foundation entries are settled, search the whole foundation once for entries your change
touches and correct them in the same change (WAY-33) — `foundation_step.md` gives how.

## Checks you run (focused, not the full gate)

`python -B elements/common/foundation_check.py` (as `elements/common/way_of_working.md`, step 4.3,
gives it); `python -B agent-instructions/skill_entry_points.py` without `--write` if you change a
skill description (and with `--write` only where the AGENTS.md says it is needed); a directory's
tests with `python -B gate/run_tests.py <directory>` for each directory whose files or inputs you
change; `python -B task-cycle/request_check.py` on a description you draft to try the template, if
you change the template. Name each command with its exit code in your report.

## Your report

Write the full report to the path above, as `task-cycle/change/SKILL.md` section 6 gives it, and
add: the choices of how to make what the task settles; your own-work check (WAY-164) — the
requirement of the task you most likely did not meet, the check you wrote or ran for it and what it
showed; **Unread material** — what this handoff names that stayed unread or was read in part, or
`none`; **Searches not found or unclear** — each thing you looked for and did not find or found
unclear, or `none`; and the working copies you made and their removal. Return: status, your
commits, a one-line check result naming what failed or did not run, and the report's path.

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
