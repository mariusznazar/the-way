# Handoff — the one author of the change `review-structure-form-class`

## Delegation

You make the whole change of one the-way task as the one author, with no plan. The human who asked for this
cycle has delegated intermediate choices to the orchestrator, who is the one you ask; there is no human to ask
during the cycle. Your work is reviewed afterwards by an agent that did not make it.

## Where

- Worktree (work from its root, and nowhere else): `the worktree's root`
- Branch `task/review-structure-form-class`, base commit `65b6d7007ec4fffad998612e5c521eee93c7b8b5` (the target branch `foundations`).
- This is the-way itself, so the process root is that worktree. No other the-way checkout is read. The directory `.runs/` inside the worktree
  is the orchestrator's: do not read or change it except your report and the frozen task named below.
- Report path (write your full report there): `docs/task-cycles/review-structure-form-class/reports/author-report.md`

## Method

Read `task-cycle/change/SKILL.md` in the worktree whole and follow it, in its variant "the whole change as the one author".
Read a file it names only when the step or variant that names it comes. Where it, or the task, names another skill of the-way —
`record-decision` — use the project skill with the `the-way-` prefix, whose entry point leads to `elements/decisions/` of the worktree.
The change includes the foundation step: read `task-cycle/skill/foundation_step.md` whole and follow it for the entries below.
The return step comes later, as a separate resumption; do not take it now.

## The task

The frozen task document is `docs/task-cycles/review-structure-form-class/task.md`. Read it whole. It is in Polish; the entries and files
you write are in English, as the-way's files are. The document governs; its eight items of *To do* in one line each:

1. `task-cycle/review/whole_change.md` gets a point: the reviewer of the whole change judges what the change leaves in the structure of the
   code — growth of a function or a file, code that has no user after the change, a name that stopped being true.
2. The reviewer gets numbers for that point: a new script of the-way in `task-cycle/`, with tests, that gives for a range of commits the
   number of lines of each changed file before the change and after it (pattern: `task-cycle/slice_size.py` with `task-cycle/test_slice_size.py`).
   Functions and files over a threshold come from the product's test of the size rule (item 3), which the reviewer runs on the state before the
   change and after it.
3. `product-guidelines/coding/template.md` gets a required rule of the size of a function and a file: a rule of its own with its own invariant
   and its own test, outside the linter's set of rules; the test, when it fails, names every function and file over a threshold with its size.
   `product-guidelines/coding/settle.md` gets the question about the thresholds, asked after a trial run on the product's existing code, and
   about exceptions written in a decision. A product that already has guidelines gets the rule by an extension of them, as the rules on
   failures and logs (WAY-278).
4. `task-cycle/review/SKILL.md`, section 3: a finding about the structure of code below the product's threshold is Minor, and the reviewer judges
   its scope as for any finding. A new decision narrows WAY-161 as WAY-297 does.
5. `task-cycle/plan/SKILL.md`: where a slice adds to a function or a file over the product's threshold, the plan begins with a slice that moves
   a part of that function or file out without a change of behaviour, and writes it in the plan's table of choices; `task-cycle/change/SKILL.md`:
   the author of a change without a plan makes that move the first commit.
6. `task-cycle/review/SKILL.md`, section 3: a finding that a foundation entry departs from the form of its template, where the entry's content
   agrees with the code, is Minor, unless the reviewer names a sentence a reader would read wrongly through the departure; with such a sentence it is
   graded as any other. A new decision narrows WAY-161 as WAY-297 does. A mismatch of content with the code stays Important (WAY-263).
7. WAY-229, through `record-decision`, no change of its binding sentences: *Rationale* gets the result of a measurement with its conditions;
   *Rejected* gets the variant "two runs of a reviewer of a cheaper class instead of one run of the lead's class" with its result. The wording of
   both is in item 7 of the task's *To do*; copy the numbers and conditions from there.
8. WAY-164, through `record-decision`, no change of its binding sentences: *Rejected* gets the variant "a review without the author's report"
   with its result; the conditions of the measurement are not repeated, one sentence points to WAY-229 (the task's question 7).

Settlements to record (rows of the task's *Settlements to record*, all accepted, all to be written whole by you in the foundation step), each a
new decision unless said otherwise. The next free decision number is WAY-355:

- Row 1 — item 4 (structure finding below the threshold is Minor). Row 2 — item 6 (form-of-entry finding). Row 3 — item 3 (the template requires
  the rule of size; a product settles thresholds after a trial run and exceptions in a decision, or departs from the rule by a decision with a reason;
  a product with guidelines gets it as an extension). Row 4 — the test names every function and file over the threshold with its size, the reviewer
  runs it before and after the change, and a product has no command of its own for function sizes. Row 5 — item 5. Row 6 — items 1 and 2.
- Items 7 and 8 are changes of WAY-229 and WAY-164, not new entries. Rows 1–6 may share a decision where one question is answered, but the task's
  rows are each a settlement to find in the log; decide how many entries and say in the report which row each holds.

Each decision's *Rejected* takes the ways the task records as not chosen under its questions 2–7 (the task is the source; invent no alternative).
A decision's *Origin* is `none` where the source is a private note (WAY-27); a measurement is written in the entry with what was measured and the
conditions (WAY-05). WAY-229 and WAY-164 are edited in place (WAY-07).

## Choices left to you (name each in the report as a choice, with the way you did not take)

- The command line and the output of the new script: it takes a range of two commits (and a repository directory if you judge it needed), prints
  for each changed file its number of lines before and after, and ends with a summary line. It runs on Python as the-way's scripts do (WAY-38, WAY-89),
  calls git with argument lists and never through a shell string, reads names with `-z` so that a file with a space or with non-ASCII letters is
  handled, and ends with exit code 2 and an `Error:` line where it cannot read what it needs (WAY-344). The reviewer runs it (cycle's choice Q3).
- Where among the required rules of the template of coding guidelines the rule of size stands and how its invariant reads. Fixed by the cycle:
  a heading of its own after the six rules on failures and logs (WAY-271), so that those six and their order stay; an invariant of its own
  and a test of its own; outside the linter's set (WAY-203); the test names each function and file over a threshold with its size; the invariant is
  marked violated while code exceeds (WAY-51); thresholds come from a trial run on the product's code; exceptions are written in a decision.
- Where else the word "structure of code" and the threshold must be said so that the skills agree (the review skill's section 2 reads the
  guidelines; `task-cycle/skill/` files that list what the reviewer of the whole change is given, if any).

## Answers of the cycle's start (step 4)

- Trust boundary: no. Irreversible operation: no. Open design choice: none. Reserved choice: none.
- The change touches the parts `task-cycle`, `product-guidelines`, `decisions`. Where a file you add needs an assignment in the part map, the return
  step handles it (`task-cycle/**` already covers the new script and its tests); tell the orchestrator in the report.
- Product guidelines: the-way has none and departs from them (WAY-328), so the new script and its tests wait for none.

## What you read

Foundation entries, each whole (a decision is the lines from its `###` heading to the next heading in `foundations/decisions.md`):

- the task's *Decisions in play*: WAY-229, WAY-164, WAY-161, WAY-297, WAY-263, WAY-51, WAY-135, WAY-16, WAY-271, WAY-278, WAY-168, WAY-173,
  WAY-203, WAY-05, WAY-27, WAY-328;
- selected by the orchestrator as bearing on the files you change: WAY-07, WAY-33, WAY-36, WAY-38, WAY-89, WAY-136, WAY-148, WAY-150, WAY-162,
  WAY-170, WAY-171, WAY-172, WAY-198, WAY-201, WAY-202, WAY-204, WAY-205, WAY-208, WAY-209, WAY-210, WAY-211, WAY-213, WAY-217, WAY-220, WAY-221,
  WAY-251, WAY-252, WAY-256, WAY-260, WAY-279, WAY-293, WAY-306, WAY-312, WAY-326, WAY-344;
- `foundations/part_map.md` whole, `foundations/glossary.md` whole, the invariants whose *Part* names a touched part or `every`
  (find them by a search of `foundations/invariants.md`);
- `product-guidelines/template.md`, `product-guidelines/coding/SKILL.md`, `settle.md`, `template.md`, `trial_run.md`, `starting_set.md`.

Beyond that, the foundation step selects as `task-cycle/skill/foundation_step.md` and the skills of the elements give. Search the whole
foundation once for the entries your new entries touch (WAY-33), and correct them in the same change. Every file you change, read whole first.
The product-guidelines reading (`product-guidelines/reading.md`) has the-way with no guidelines of its own; do not look for them.

## Boundaries

- Commit on the branch, naming files by path (`git add <file> ...`), never `git add -A`. Commit messages in English, the form of the existing log.
  Several commits are welcome: for example the script with its tests; the review skill with its decisions; the guidelines template and its question
  with their decisions; the plan and change skills with their decision; the two edits of WAY-229 and WAY-164. Do not push.
  Do not touch the main checkout of the repository or other worktrees.
- Do not run the whole gate (`python -B gate/run_tests.py` without a directory): the orchestrator runs it. Run the focused checks that your
  change calls for: `python -B gate/run_tests.py task-cycle` (the new script's tests included; `git add` a new test file first so that the runner
  sees it), `python -B elements/common/foundation_check.py` on the foundation, `python -B task-cycle/private_paths_check.py <file>` on each file
  you change, and, if the description of a skill changes, `python -B agent-instructions/skill_entry_points.py --write` and a commit (the no-argument form
  checks; there is no `--check`). Record each check's command and exit code in the report.
- Do not start the next stage; return at your boundary with the report. Questions go to the orchestrator as `questions`, not to a human.
  A change that proves too large for one agent returns `returned` with where the size lies, and no code.
- The report holds, as `make-change` gives it: status, commits, checks with command and exit code, the own-work check, your meaning sentences
  for each foundation entry written, **Unread material** and **Searches not found or unclear** (each `none` where there is nothing); and the list of
  your choices named above.
- Write the report to the path above only: a subagent's report file whose name starts with `report`, `summary`, `findings` or `analysis` is
  refused; `author-report.md` is fine.
