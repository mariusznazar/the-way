# Handoff — correction 1, for the human's remarks on the open request

You are the one author, resumed. Your variant of `<the-way>/task-cycle/change/SKILL.md`, in the words of its row: **a correction for the human's remarks**. Read it as its row gives: each remark binds, and your report holds each remark as made, and how.

## Where you work

- The request's worktree, as before: `the root of the repository`, branch `task/cycle-instruction-seven-fixes`; the head is `dcaa169c` (the commit that removes the record's copy). The request is https://github.com/mariusznazar/the-way/pull/151, open. Your correction's range runs from `dcaa169c`. The code you correct stands in the commits `2a0df03c`, `fc88ee2c`, `bcaddc2b`, `76b6b172`, `20210259`, `52801a69`.
- The directory for your working copies: `.runs/author-correction-1/`.
- Your report: `.runs/task-cycles/cycle-instruction-seven-fixes/reports/author-correction-1-report.md`; where the harness refuses the write, return it whole.

## The remarks, word for word (they bind)

The file: `.runs/task-cycles/cycle-instruction-seven-fixes/reports/correction-1-remarks.md` — read it whole. In short, its first two items ask for two changes inside this request; the rest only accepts items you do not touch.

The frozen task stays `.runs/task-cycles/cycle-instruction-seven-fixes/task.md`, and the reviewer's two findings outside the task's scope that these remarks answer are, word for word:

1. **Minor — "the lead" names the orchestrator by a word the-way uses nowhere else.** Place: `task-cycle/skill/SKILL.md:508`. The skill addresses its reader as "you", the decisions say "the orchestrator" (WAY-136 as this change writes it included), and a search of the task-cycle skills and the glossary finds "the lead" in this one sentence only; a reader can take it for another actor than the one the rest of the sub-step addresses. The word is the task's, given word for word and confirmed under its first question, so changing it goes beyond the task.
2. **Minor — the measure and the reading differ for a changed file that is no file of the foundation.** Place: `task-cycle/slice_size.py:194-196` against `task-cycle/change/SKILL.md:37-38`. The sentence of point 4(a) counts by its ranges every file of *Change* that *Read* names by ranges; the sentence of point 4(c) lets the agent read by ranges only "a file of the foundation", and every other file it changes whole. A plan that names in *Read* a range of a file of code the slice changes is now measured by the range while its agent reads the whole file. Evidence: a scratch run, a slice with `task-cycle/remove_merged_worktrees.py` in *Change* and `:1-10` in *Read* counts 548 characters at the head and 25 907 at the base. The task's answer on point 4(c) gives as its aim that the measure and the reading count the same; both sentences are the task's, so the difference is a gap of the task and its closing goes beyond it.

## What the correction does

1. **The word.** In the sentence about groups of reviews in `task-cycle/skill/SKILL.md` (sub-step 5 of step 9), put in place of "the lead" the name the process gives the agent leading the cycle: the skill opens with "You are the orchestrator" and the decisions say "the orchestrator". Read the sub-step around the sentence and use the name it uses for that agent; where the sub-step addresses its reader as "you", say which you chose and why. Do not touch the rest of the sentence. A copy of the sentence elsewhere (a record template, another skill, a decision) is corrected the same way where it holds the word; search the repository once for "the lead may dispatch" and for the sentence.
2. **The measure.** In `task-cycle/slice_size.py`, a changed file that *Read* names by ranges counts the lines of those ranges only where it is a file of the foundation — the files of decisions the task was about: a slice that names part of a large decision log. A file of *Change* that is no file of the foundation (a code file) counts whole, as its agent reads it, whatever ranges of it *Read* names. Settle from the repository what "a file of the foundation" is for the script (the foundation's own files — the decision log, the invariants file, the glossary, the environment facts and the part map — stand under `foundations/` of the repository, `elements/common/way_of_working.md` and the part map say so; take the rule from there and name where you took it), and write the docstring paragraph of the script to say it: the sentence the task gave for point 4(a) is narrowed only where the task did not intend it, so for a file of the foundation it reads as it did. The rest of the docstring and the code stay as they are. A file that *Read* names whole still counts whole, and a file named both whole and by ranges still counts whole (the choice the orchestrator accepted).
3. **Tests.** Keep the tests of the script that hold the case of the foundation file (a large log named by a range counts by the range) with the path adjusted where they use another place; add the test the remarks ask for: a plan whose slice changes a code file, names a range of it in *Read*, and counts the whole file (write the expected number out in the test with its derivation in a comment, as the guidelines for tests give). Run the new test red against the code as it stands now, and say so with its command in the report.
4. **What stays.** The sentence of 4(b) in `task-cycle/plan/SKILL.md` and the item of 4(c) in `task-cycle/change/SKILL.md` already speak of a file of the foundation; read them again and change them only where they disagree with the corrected measure. The three decisions and the template do not change.

## What you read

- The remarks file above, the frozen task whole, the two findings above, and your own earlier reports as needed (`reports/author-report.md`, `reports/author-fix-report.md`, `reports/author-return-report.md`) — they are yours.
- Whole before you change them: `task-cycle/skill/SKILL.md`, `task-cycle/slice_size.py`, `task-cycle/test_slice_size.py`, and any other file you change.
- Guidelines, each whole, as before: `guidelines/coding.md`, `guidelines/coding-measuring-report.md`, `guidelines/testing.md`.
- Foundation entries: those you read earlier; reach selectively for any other and name the reach in your report.
- `cycle.md` and the other files of the cycle's record directory — other agents' handoffs and reports — are not yours to read unless this handoff names them.

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

(Your directory is `.runs/author-correction-1/`. Remove a copy by its path written out in full in the command, never through a shell variable: an empty variable turns the removal on the directory the shell stands in.)

## Commits and checks

Commit on the branch by paths, in English. Run the affected checks again: the test file you change (with its command and exit code), `python -B gate/run_tests.py task-cycle`, `python -B gate/run_tests.py agent-instructions`, `python -B gate/run_tests.py instruction-files`, and `python -B elements/common/foundation_check.py`, and the own-work check of `task-cycle/change/SKILL.md` for the corrected measure (a plan against the real `foundations/decisions.md` and against a real code file, as you did before). No full gate. Your report holds, besides the remarks as made and how each was met: your checks with command and exit code, your own-work check, your reaches, **Unread material** and **Searches not found or unclear** (each `none` where there is nothing), and the working copies line.
