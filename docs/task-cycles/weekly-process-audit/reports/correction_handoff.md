# Handoff — the correction for the human's decision (`make-change`: "a correction for the human's remarks")

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator. Their decision below binds you.
Your questions go to the orchestrator, never to the human.

## Where you work

- Worktree (work from its root, read every file from it): `the worktree of the task`, branch
  `task/weekly-process-audit`, HEAD `5f2c155` (the target branch merged in; the decisions of the audit are now WAY-329…WAY-340).
- Method: `task-cycle/change/SKILL.md` whole (you make "a correction for the human's remarks"); then `task-cycle/review/fix.md` is
  how your work will be reviewed. The correction's range starts at `5f2c155`.
- Report path: `docs/task-cycles/weekly-process-audit/reports\correction_report.md`.

## The human's decision (their words, which bind)

On the blocked request, item 1 asked: fix the finding as the reviewer says or keep the code, and "make a task" of the tie of a subagent
turn to its round. The human answered:

> a co do tego 0.0% zgadzam się z propozycją, ale nie rozumiem idei żeby to zrobić osobnym zadaniem — jak wiemy co jest do zrobienia,
> to trzeba to zrobić, a nie wydzielać

That is: (1) the reviewer's direction is accepted — the share of fix rounds is `0.0%` only where the record plainly says there was no
round, otherwise it is not `0.0%`; (2) the tie of a subagent turn to the round it served is to be made in this request, not as a task of
its own. The share must therefore be a real figure in a cycle that follows the new form, `unknown` only where the cycle's records
cannot say.

## The blocking finding that remained (the reviewer's words)

Read `.runs/task-cycles/weekly-process-audit/reports/review_slice4_fix_report.md` (finding 1, "REMAINS", and the section "Whether the
outcome … is a defect of the fix or a limit for the human") and the fix report `slice4_fix_report.md`. In short: the command read a fix
round only from report paths that hold the words `report` and `fix`, but real records name their fix reports `reports/fix.md`,
`reports/review-fix.md` and so on, so a cycle with a fix round was given `0.0%`; and `stages.md` names the subagent that worked, not the
round a turn served, so no honest non-zero share could be computed.

## What to build (the orchestrator's design — the way of making what the human decided; name any part you cannot hold)

1. **The tie, without words.** A fix round has a *findings file*: the orchestrator writes it from a review's blocking findings, and both
   the fix's dispatch and the dispatch of the review of that fix name it by its path in `reports/` (the cycle's skill says the fix is
   given the findings file; see `task-cycle/skill/SKILL.md`, "The end of a code review", and `task-cycle/review/fix.md`). A stage (one
   turn of a subagent) belongs to a fix round exactly when its prompt or resuming message names the findings file of a round.
2. **`task-cycle/cycle_stages.py`:** for each subagent turn, read the `reports/<name>.md` file names that its prompt or resuming message
   names (safe characters only, a cap on count and length, text from the transcript is data) and write them in a new column of the
   per-stage table of `stages.md` ("Files named" or the name you choose, one cell, no bar). A turn that names none has an empty cell, not
   a failure. This changes the form of the stage report, which starts a new series (WAY-338, formerly numbered 336 in the plan): say so in
   the docstring and in the report. Tests for both transcript forms (Claude Code and Codex) as the slice 2 tests do.
3. **`task-cycle/record_template.md`:** *Review rounds* names, for each round, the findings file by its path in `reports/`, in one fixed
   form a script can read (choose it; keep `none` for no round). Mirror it in the line of the `Review rounds` in the template's text, and
   add to `task-cycle/skill/SKILL.md` the one rule that makes the tie hold: the dispatch of a fix and the dispatch of the review of that
   fix name the findings file by its path in `reports/`. Change nothing else in that skill; the target branch changed it recently, so read
   the passage in its current form.
4. **`process-audit/audit_count.py`:** the share of fix rounds is the cost of the turns that name a findings file of a round of the record,
   over the cost of all stages, from the new column. It is `0.0%` only where the record's *Review rounds* reads `none` (as
   `remarks_check.reads_none` reads the remarks item) and, in the new form, no turn names a findings file; it is `unknown` with the reason
   where the record's rounds name no findings file, where `stages.md` has no such column (the earlier form), where a named file is no
   turn's, or where the record and the stages disagree. Remove the word-based rule of the fix (`report` and `fix` in a path) and the
   `fix`/`review` words in stage names. A round count stays: the number of findings files the record names. Keep the lessons of the
   trust-boundary reviews: no backtracking pattern, no unguarded conversion, every cell through `cell()`, size caps, one cycle's failure is
   `unknown` for that cycle. Also fix, since you touch them: the tokenless *orchestrator* stretch must not make a whole cycle's cost
   `unknown` when subagent stages are priced (the reviewer's cheaper rule: `unknown` for a section with no priced row and for subagent rows
   with `—`; an orchestrator stretch with `—` counts as zero and the reason says so), and a doubled `- Review rounds:` line is read as
   a doubled line (unknown), as the pin and the remarks item are.
5. **The decision:** WAY-336 (cost of a cycle; edit in place, WAY-07, through the project skill `the-way-record-decision`) says what a fix
   round is and how the audit ties a turn to it, and its Verification; do not write a new number. WAY-338 (the series) already says a
   change of the stage report's form starts a new series; nothing to add unless a sentence there is now false.
6. **Tests first** where you can name the failing test in one sentence: a record with a fix round named `reports/fix.md`-style and a
   `stages.md` of the new form gives the real share; the same record with an old-form `stages.md` gives `unknown`; a record with
   `Review rounds` `none` gives `0.0%`; a turn that names a findings file of a round is counted once even if it names two; crafted file
   names in a prompt (control characters, a bar, a very long run, `..`) do not break a row or a pattern.

## Boundaries

- Do not make slices 5–7 (reading the register, the per-version measures, the skill): they run after your correction.
- Leave alone every other Minor finding of the earlier reviews.
- The foundation check must report 0 errors after your commits; the target branch's new WAY-328 holds the-way's own code and tests to no
  guidelines of their own.
- Commit with `git add <paths>`, messages in English.

## Checks (each as command and exit code in your report)

`python -B gate/run_tests.py process-audit`, `python -B -m unittest discover -s task-cycle -p test_cycle_stages.py`,
`python -B gate/run_tests.py task-cycle` if it covers the record template's tests, `python -B elements/common/foundation_check.py`,
`python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths`, and a run of `process-audit/audit_count.py` with stdin
closed on a temporary locations file naming this worktree and a temporary results directory. Run
`python -B task-cycle/cycle_stages.py b065500f-249b-4808-a8bf-172d19a2724a --output <a file outside the repository>` and say what the new column
shows for the turns of the fixes of slices 3 and 4 of this very cycle (they name `review_slice3_findings.md` and `review_slice4_findings.md`).

## Report

As `make-change` gives: status, commits, a one-line check result, questions, concerns, each reach beyond this handoff, **Unread material**,
**Searches not found or unclear**, the own-work check; and for each of the human's two points, how the correction makes it.
