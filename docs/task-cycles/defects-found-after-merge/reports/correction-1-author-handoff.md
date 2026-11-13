# Handoff — the author of correction 1, `defects-found-after-merge`

## Delegation and place

The person who requested this cycle has delegated intermediate choices to the orchestrator; nothing
here is that person's approval. Work only in the worktree `the task's worktree, which is the repository's root`
(branch `task/defects-found-after-merge`, head `716b22a`; the target branch `foundations` is at
`6814c6f`, the branch's base, so nothing was merged in). Start every command from its root. Write
nothing outside it. Never commit the `.runs/` directory (it is ignored). Commit with `git add <path>`
by explicit paths, in one commit, the message in English in the form of the repository's existing
commits (`git log --oneline -10`).

## Stage and method

Stage: make the correction for the human's remarks. Variant of the method, in the words of its row:
"a correction for the human's remarks". Method: `task-cycle/change/SKILL.md` of this worktree. Read it
whole; read a file it names only when the step or variant that names it comes. Also read
`agent-instructions/README.md` (the repository's route for changing the-way itself). The request is
open, already reviewed and passed; this is its first correction.

Boundary: do not run the full gate (`python -B gate/run_tests.py` with no argument) — the
orchestrator runs it. Run the tests of the directories you touch with `python -B gate/run_tests.py
<directory>`, and `python -B elements/common/foundation_check.py --skip-test-citations .` where you
touch `foundations/`. Do not start the return step or any review.

## The human's remarks (they bind)

The file with the remarks word for word:
`.runs/task-cycles/defects-found-after-merge/reports/correction-1-remarks.md`. Their content:

> Fix in this request: Item 3 of "Fix or let through": "One sentence of the new kind of item for
> corrections is left to the writer. When a correction is only a refresh of the target branch, the
> description still has to carry the one sentence with its pair `target-branch · none`, and the
> template does not say what to write there, so the agent writing the description improvises the
> sentence." — Decision: fix it in this request. Add to the request template the sentence (or an
> example of it) that a refresh-only correction carries with its pair `target-branch · none`, so
> that the writer does not improvise it.

The two items of *Needed from you* are done outside the repository; do not touch them, the user's
register or the locations file.

## What to make

In `task-cycle/skill/request_template.md`, kind 17 ("The cause of a correction") gives the sentence
for a correction made for the human's remarks or answer, and says nothing of the sentence of a
correction that only refreshes the target branch, whose pair is `target-branch · none` (the kind is
`none`, the cycle judges nothing — see WAY-356 and `task-cycle/skill/correction.md`, the paragraph
that gives the line of a correction). Write into that kind the sentence, or an example of it, that a
refresh-only correction carries, so that the writer does not improvise it: in plain words that the
branch was only refreshed from the target branch at the human's request, that nothing else changed,
and, since the kind is `none`, that the cycle made no judgment of whether the task required anything.
It follows the template's own rules for the top part (plain words, no file names, no identifiers of
entries). Keep the wording as short as the kind's other sentences. Where a correction has two
sources, one of them `target-branch`, say in the same place how the one sentence carries both pairs
(WAY-356: each pair once), only if the kind's text does not already say it.

Make no other change. In particular:

- Do not change a decision unless the sentence you write contradicts one (then return `questions`
  with the collision, and change nothing). WAY-287 and WAY-356 already say that the description
  shows the pairs in one sentence and that `target-branch` takes the kind `none`; the new text must
  agree with them.
- Check that the tests which read the template still pass: the form check of a description and the
  tests of `task-cycle` that name the kinds; add a test only where the sentence is a rule a script
  reads (probably not). If the new text would need a test to stay true, say so in the report.
- The foundation step: search the foundation once for entries that the new sentence touches (WAY-33)
  and say in the report that you did, naming what you found; write none unless it must.

## What to read (selection by the orchestrator, WAY-150, WAY-213)

Decisions, each whole: WAY-287, WAY-356, WAY-355, WAY-286, WAY-289, WAY-306, WAY-337. Files:
`task-cycle/skill/request_template.md` (whole), `task-cycle/skill/correction.md` (whole),
`task-cycle/record_template.md` (the item *Corrections after the request opened*). The frozen task
for background, only if you need it: `.runs/task-cycles/defects-found-after-merge/task.md` (Polish;
no private path or note link enters a committed file).

## Report

Write the full report to `.runs/task-cycles/defects-found-after-merge/reports/correction-1-author-report.md`
in the form the method gives for a correction: status, commits, each remark as made and how, the
own-work check with its commands and exit codes, the checks you ran with command and exit code,
questions, concerns, reaches beyond this handoff, **Unread material** and **Searches not found or
unclear** (each `none` where none). Return only the status, the commits, a one-line check result and
the report's path.
