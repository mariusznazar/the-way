# Handoff — the one author, the whole change

You are the one author (`the-way-author`) of the change of one task of the-way, made without a plan.

## Delegation

The person who requested this cycle has delegated the intermediate choices to the orchestrator. Never
label an answer of yours as that person's approval. You return at your boundary: you start no later
stage and ask no human; a question goes to the orchestrator in your report.

## Where you work

- Worktree (the checkout you work in, from its root): `the root of the repository`, branch `task/cycle-instruction-seven-fixes`, base `0b43a27d`. The-way is this worktree itself; in the paths below, `<the-way>` is its root.
- Read from the worktree only, never a copy in another checkout.
- The directory for your working copies: `.runs/author/` of the worktree.
- Your report: `.runs/task-cycles/cycle-instruction-seven-fixes/reports/author-report.md`.

## Your method and your variant

Read `<the-way>/task-cycle/change/SKILL.md` whole. Your variant, in the words of its row: **the whole change as the one author**. Read a file that `SKILL.md` names only when the step or variant that names it comes.

## Your stage and its boundary

Make the whole change of the task, with the foundation step (the three rows of *Settlements to record*, which `<the-way>/task-cycle/skill/foundation_step.md` governs — read it whole), and return before any review. You write the code, the texts and the entries; you run no review of your own and you run no full gate. The product's full gate is run by the orchestrator or CI, never by you. Your focused checks are the tests of the directories you change (`python -B gate/run_tests.py <directory>`) and `python -B elements/common/foundation_check.py`, each with its command and exit code in your report.

## The task

The frozen task, to be read whole: `.runs/task-cycles/cycle-instruction-seven-fixes/task.md` (the task's `To do` points 1–7 with their sub-points, its *Questions to settle*, *Decisions in play* and *Settlements to record*). Its points give the wording of the change; keep that wording word for word where a point quotes it. The places the task names with a line number are a hint beside the quotation, which finds the place. The rejected variants under *Questions to settle* are not to be restored.

Where the task's quotation of a place no longer matches the file (the checkout stands at a later commit than the one the task was checked on), say so in your report and take the nearest place that serves the point; where the place is unclear, return `questions`.

Two further points follow from *Questions to settle* and are part of the task: the sentence of WAY-136 (point 2), the sentence of WAY-255 (point 6) and the sentence of WAY-134 (point 5) are written into the decisions — rows 1, 2 and 3 of *Settlements to record*; and the two additions of point 4, (b) in `task-cycle/plan/SKILL.md` and (c) in `task-cycle/change/SKILL.md`, are part of the task as its *To do* lists them. Point 4(a) changes `task-cycle/slice_size.py` and needs a test, as the task describes it: a plan whose slice changes a large decision log.

## The answers at start

- Does the change touch a trust boundary? **No.** None of the files the part map names as the trust boundary of the `task-cycle` part is among the files of the task.
- Does it hold an operation that cannot be undone? **No.**
- Open design choice: **none** (the orchestrator's finding; where you meet one while you make the change, return `returned` with a report and no code, as your method gives).
- Route: one author without a plan. Your class: `same`.

## What you read

You read what is named here, and whatever else you need by a selective reach that you name in your report.

Foundation entries, each whole (an entry of the decision log runs from its `###` heading to the next heading of any level):

- the decisions the change writes: **WAY-136**, **WAY-255**, **WAY-134**, each with its *Rejected*, in `foundations/decisions.md` — find each by its heading and read that entry only;
- the decisions the task names that stay unchanged and that the change must not contradict: **WAY-140**, **WAY-316**, **WAY-373**, **WAY-148**;
- the others of the orchestrator's selection (the decisions of the part `task-cycle` and `decisions`, and the sections *The course of a task cycle*, *The work of a cycle's agents* and *Review of a change*), as an index of their numbers, questions and binding sentences: `.runs/task-cycles/cycle-instruction-seven-fixes/orch_index.md`. Open whole of them only a decision your change goes against or one whose sentence leaves open what you have to do.
- never read `foundations/decisions.md` as a whole file: it is about 900 KB. Read it by the entries named above, by a search for a number or a word and the entry found.

Guidelines, each whole: `guidelines/coding.md`, `guidelines/coding-measuring-report.md` (`task-cycle/slice_size.py` is a measuring report), `guidelines/testing.md` (you change a test). A file `guidelines/coding-<kind>.md` other than that one only where its row in `guidelines/coding.md` matches the work.

The element's skill, where you write a decision: `elements/decisions/skill/SKILL.md`, and the files it reads (the template `elements/decisions/template.md`, which one of the points also changes, and the examples), as `task-cycle/skill/foundation_step.md` gives.

Files of the change, each whole before you change it: `task-cycle/skill/SKILL.md`, `task-cycle/plan/SKILL.md`, `task-cycle/change/SKILL.md`, `task-cycle/review/SKILL.md`, `task-cycle/slice_size.py` and `task-cycle/test_slice_size.py`, `elements/decisions/template.md`. Of `foundations/decisions.md` you read the three entries above, by their ranges, and not the file whole.

`task-cycle/skill/SKILL.md`, `task-cycle/plan/SKILL.md`, `task-cycle/change/SKILL.md` and `task-cycle/review/SKILL.md` are instruction files of the process. Where the work changes one, also read `instruction-files/` of the-way if its skill applies — the task gives exact wording for them, so only the form of a sentence is yours (a line break, a link), never its meaning.

`cycle.md` and the other files of the cycle's record directory — other agents' handoffs, reports and findings — are not yours to read unless this handoff names them. It names the frozen task and `orch_index.md`.

## Entry points and copies

A change to the description of a skill, or one that adds, renames or moves a skill, runs `python -B agent-instructions/skill_entry_points.py --write`; a change to a definition in `task-cycle/agent-types/` runs `python -B agent-instructions/agent_type_copies.py --write`. The task changes the body of four skills and no description, so neither is expected to be needed; where `python -B gate/run_tests.py agent-instructions` fails after your change on such a copy, do as the test says and say so in your report.

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

(Your directory is `.runs/author/`. Remove a copy by its path written out in full in the command, never through a shell variable: an empty variable turns the removal on the directory the shell stands in.)

## Commits

Commit on the task branch, in commits of your own, with messages in English as the history of the repository writes them. Add files by their paths, never `git add -A` or `git add .`. Commit nothing of `.runs/`.

## Your report

Write the report whole to the path above; its file name starts with the role (`author-report.md`), as the cycle names it. If a harness refuses the write of that file, return the report whole as your answer. Return, besides, your status, your commits, a one-line check result naming what failed or did not run, and the report's path. The report holds, as `task-cycle/change/SKILL.md` gives it: your checks with command and exit code, your own-work check (the weakest point of the change and the check of it), your reaches, **Unread material** (what this handoff names that stayed unread or was read in part, or `none`) and **Searches not found or unclear** (each thing looked for and not found or unclear, or `none`), and, for the foundation step, one sentence of the meaning of each entry in English and one in the language of the task document (Polish), marked `row 1`, `row 2`, `row 3` as `task-cycle/skill/foundation_step.md` gives.
