PASS ba36539

# Review of the fix — task `locations-file`, fix 1

Range: `973ee64..ba36539`, one commit (`ba36539 Fix the findings of the review of the locations file
change`); `git rev-parse HEAD` gives `ba365394094cd1028a9bd635386cf9e360bd191a`, the head given. Bound
by `reports/findings-whole-1.md` (I-1, I-2 blocking; M-1, M-2 Minor within the task).

Changed files (`git diff --numstat 973ee64..ba36539`): `foundations/decisions.md` +20 −9,
`project-level/backlog_place.md` +8 −6.

Blocking findings remaining: 0. Minor remaining: 1 (M-1, left on purpose, non-blocking). New findings
in the fix diff: 0.

## Findings

**I-1 — fixed.** WAY-320's binding sentence now reads "No file the repository tracks holds an
absolute path or a note link, other than the files that the invariant `tracked-file-private-paths`
names, which write example paths in order to find or to test them; …"
(`foundations/decisions.md:10210-10213`). It carries the qualification of settlement row 3 and the
invariant, so the four listed files no longer do what the decision forbids. The *violates* bullet is
narrowed to match ("a tracked file the invariant does not name", `:10223-10226`). The *Rationale*
now carries question 2's price ("adding a file to it shows in the change; a real path pasted into a
file on the list passes", `:10236-10238`), and *Rejected* carries question 2's three not-chosen ways
with their costs (`:10250-10255`). I compared each word for word with question 2 of the frozen task:
marked lines only (lines to mark, code of the marks, a real path in a marked line passes); no
exceptions with rewritten examples (every example rewritten, tests and the script's description
harder to read, every later author must remember); skip all tests and both scripts (a path in any test
passes) — all three faithful. Leaving out the counts 98 / about 100 changes no meaning. The
rationale's "the list of those files stands in the invariant" is true; the test mirrors it and
`test_the_exempt_files_are_the_ones_the_invariant_names` keeps the two equal, which the sentence does
not need to say.

**I-2 — fixed.** `project-level/backlog_place.md:24-26` now reads "An agent that runs a task cycle
does not create or change the locations file (WAY-140): …". It no longer forbids the write of the
request link and state into the backlog entry, which WAY-140 and `task-cycle/skill/SKILL.md:76-78`
allow, and WAY-140 supports the narrower rule (an effect outside the repository on the user's file is
the human's).

**M-1 — remains, kept as Minor; I accept leaving it.** `project-level/backlog_place.md:21-22` still
counts "the path it holds does not exist" as a missing place, and WAY-107 is unchanged. As the
finding said, it contradicts nothing and is the operational reading of a missing place; it blocks
nothing (WAY-162). Widening WAY-107 by one phrase stays an option for a later change.

**M-2 — fixed.** `backlog_place.md:10-12` marks the example as the-way's own section and says that in
another product the product's name stands in place of `the-way`; `:29-30` now reads "those name the
entry, as "the entry `tasks` under <the product's name>", and say nothing more".

## New findings in the fix diff

None. The reflow of WAY-320's *Rejected* changes no words of the earlier ways (checked in the diff:
only line breaks moved in "the place described in words … global instructions").

Note outside the fix diff (no finding): `backlog_place.md` says "the product's name" where WAY-320
says the keys are "repository names"; `:9-10` already says the line names "the repository it stands
under", so a reader is not misled.

## Declined to judge

- Whether WAY-107 should name the dangling path (M-1) — left to the cycle as the finding allowed.

## Checks run

- `git rev-parse HEAD` → `ba36539…`, matches.
- `python -B elements/common/foundation_check.py` — exit 0, "0 errors".
- `python -B gate/run_tests.py task-cycle` — exit 0, OK (includes `test_tracked_files_private_paths`
  and the check that the exempt list equals the invariant's).
- `python -B gate/run_tests.py project-level` — exit 0.
- `python -B gate/run_tests.py elements/common` — exit 0.
- `git status --short` in the reviewed worktree — empty after the checks.
- Manual: word-by-word comparison of WAY-320's new *Rationale* and *Rejected* with question 2 of
  `.runs/task-cycles/locations-file/task.md` — faithful, as above.
- Not run: the full gate, the orchestrator's run.

## Reaches beyond the dispatch

- WAY-140 and WAY-107 as read in the review of the whole change (no re-read beyond the lines quoted),
  to judge I-2 and M-1.
- Question 2 of the frozen task, to judge the fidelity of I-1's fix.

## Searches not found or unclear

none
