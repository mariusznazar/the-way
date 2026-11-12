# Handoff — review of the whole change, `review-change`

You are a reviewer that did not make this change. Read-only: do not edit, commit or reset anything
in the worktree. Questions go to the orchestrator.

## Where, what, which method

- Worktree (process root; work from it): `the task's worktree`
- Method: the project skill `the-way-review-change`; its entry point sends you to
  `task-cycle/review/SKILL.md` in the worktree. Read that `SKILL.md` whole, and a file it names only
  when the step or variant that names it comes. Your variant: the review of the whole change.
- Range to review: base `55afa8e57aa1b83c77108576a36642722e0dda15` to head
  `18b4a3f` (`git diff 55afa8e..18b4a3f`); two commits, `f5e1d45` (code, tests, template, skill)
  and `18b4a3f` (foundation entries). The one-author route: no spec, no plan, no slices; so no
  slice had a review of its own — this review judges the whole change.
- Frozen task, read whole: `.runs/task-cycles/problem-cost-in-register/task.md`
  (`Project relation: independent`). The change carries out its *To do* 1–4, answers its
  *Questions to settle* and writes *Settlements to record* rows 1–3 (accepted: 3 of 6 candidates).
- The author's report, read it: `.runs/task-cycles/problem-cost-in-register/reports/author-report.md`
  (status `done with concerns`).
- Select your own foundation and guidelines, by the parts of the change (`process-audit`,
  and the foundation files `decisions`/`glossary`), as `elements/common/way_of_working.md`
  "Reading the foundation" gives; state in your report how many decisions you read whole and how many
  by title (WAY-150). The task's *Decisions in play* name WAY-330, 328, 333, 336, 339, 344 and 337 is
  the neighbour whose cost the new term must not be confused with. The-way's own code and tests are
  held to no general coding or testing guidelines (WAY-328).

## Answers of the orchestrator at start (WAY-13)

- Trust boundary: yes. `process-audit/audit_count.py` is a trust boundary of the part map, and the
  change edits it. Check crafted input at that boundary: the register is untrusted input
  (a cost cell that is no level, a level table with a level missing, doubled or extra, a register
  without the new column, table or headings, cells with `|`, line breaks, control characters),
  and that the output carries no cell text unprintable or unescaped.
- Irreversible operation: no.
- The change moved no process pin (the-way itself).
- Checks failing on the base: none (the whole gate passed on the base, exit 0, 1066 tests).
- The edits the task's *Human actions* place in the cycle (the user's own register copy, the rules of
  the nightly session) lie outside the repository; the orchestrator lists them in the request. Do not
  count their absence as a finding.

## Things the author reported that you should judge, not take as settled

(The orchestrator grades nothing. These are the author's own words from its report, handed to you.)

1. Exit code of a missing field. The author applied WAY-344 to the whole reading of the register:
   a missing heading, table or column now ends the run with exit 2 and nothing written, where before
   a missing table gave exit 1 with a written result. For row labels of the two level tables
   (*Weights* and the new table) the author kept exit 1, following the task's explicit words
   ("tak jak dziś tabelę wag bez czterech poziomów wagi"). Judge both against the task,
   WAY-344 and the decision log, and whether the changed exit code of old tables is within the task.
2. Where the result shows the cost. Task item 3 and *Questions to settle* ask that the result, for
   each issue fixed, open and dropped, give how many of its problems stand on each level of cost. The
   author made one new section `Cost of an occurrence by issue` (one row per issue with its fate)
   rather than extra columns in the three issue tables. Judge against the task's words.
3. Foundation entries: WAY-345 (row 1), WAY-346 (row 2), glossary term (row 3) and an in-place
   edit of WAY-330 (the task's *Decisions in play* lists WAY-330 with "Zmiana, którą wprowadza
   zadanie"). Judge the fit of each with the row it carries out and with `elements/common/rules.md` and
   the skills of the elements.
4. Unread material of the author: `process-audit/test_audit_count.py` lines 220–1099 and 1600–end,
   `foundations/part_map.md` beyond the `process-audit` entry and the other invariants beyond their
   headings were not read by the author. You judge the change that touches that file; read what you
   need of it.
5. Open points the author names unclear: whether WAY-339 wants a new series when the user adapts the
   meaning of a cost level; whether editing WAY-330's heading question goes beyond the task.

## Request

Write the full report to
`.runs/task-cycles/problem-cost-in-register/reports/review-whole-report.md`
as `review-change` gives it: the first line `PASS <sha>` or `FAIL <sha>`, graded findings (each
with its scope: in the task or outside), the checks you ran with command and exit code, **Unread
material** and **Searches not found or unclear**. Do not run the whole gate
(`python -B gate/run_tests.py` with no argument); the orchestrator runs it. Return your first line,
a one-line check result and the report's path.
