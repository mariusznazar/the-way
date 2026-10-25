# Handoff — reviewer of the whole change (review-change), task `testing-guidelines`

## Delegation and your boundary

The person who requested this cycle (Mariusz) delegated every intermediate choice of the cycle to
its orchestrator. You review the whole change and made none of it. Follow the project skill
`the-way-review-change` (read `task-cycle/review/SKILL.md` in this worktree whole, and what it
names) as the reviewer of the whole change. Read only; write only your report. Its first line is
`PASS <sha>`, `FAIL <sha>` or `questions`. Select your own foundation and guidelines by the parts of
the change ("Reading the foundation" in `elements/common/way_of_working.md`; the-way has no
`guidelines/`). Judge every slice that had no review of its own, and name for each blocking finding
the slice it comes from, or that it comes from none (a gap of the plan, or the foundation entries).
Questions go to the orchestrator, never to the human.

## Range and worktree

- Worktree: `C:/Storage/repos/the-way-wt/testing-guidelines`, branch `task/testing-guidelines`.
- Range: `4302f72..3bd9e37` (task base to head).
- Frozen task (read whole): `.runs/task-cycles/testing-guidelines/task.md`.
- Reviewed spec: `.runs/task-cycles/testing-guidelines/spec.md` (spec review FAIL, one revision,
  re-review PASS: `reports/spec-review.md`).
- Plan: `.runs/task-cycles/testing-guidelines/plan.md`, size report `plan-size.md`.
- Your report: `.runs/task-cycles/testing-guidelines/reports/whole-review.md`.

## Slices

| Slice | Range | Own review | Report of its maker | Mismatch the mechanical check passed on |
|---|---|---|---|---|
| Foundation entries | `4302f72..57917c3` (`4f207dd`, `57917c3`) | no (judged with slice 1 here) | `reports/foundation.md` | none |
| 1 testing template | `57917c3..083ab5d` | no | `reports/slice-1.md` | none |
| 2 coding discipline loses the rule | `083ab5d..87b600e` | no | `reports/slice-2.md` | the executor read only part of its *Read* (task and spec passages, WAY-231, WAY-247), not WAY-228 as edited |
| 3 skill, README, entry points | `87b600e..2b5b1c0` | no | `reports/slice-3.md` | 42 generated entry points named by two patterns (accepted, C7) |
| 4 reading and two project-level skills | `2b5b1c0..467a2af` | no | `reports/slice-4.md` | none |
| 5 installer | `467a2af..3bd9e37` | yes — `PASS 3bd9e37` (`reports/slice-5-review.md`) | `reports/slice-5.md` | none |

Minor and out-of-scope findings of the slice 5 review, in its words (`reports/slice-5-review.md`):
- Minor: the copied test comment at `installation/test_testing_guidelines_installation.py:151-152`
  is stale — the installer catches the decode error and stops with "Existing integration file
  differs" since commit `24f7f44`; because the test skips the message check for the non-UTF-8 case,
  it cannot tell a clean refusal from a crash.
- Out of scope: `installation/test_coding_guidelines_installation.py:149-155` has the same stale
  comment and exemption, predating this slice.

## Answers of step 4 and the cycle's rulings

- Trust boundary: yes — `installation/install.py` (slice 5, reviewed on its own). Check crafted
  input there as far as the whole change bears on it.
- Irreversible operation: no.
- C3: row 25 gets no decision; its pieces go to *Based on*/*Rejected*/*Rationale* of WAY-233,
  WAY-235, WAY-236, WAY-237, WAY-238, WAY-241, WAY-243 (`elements/decisions/template.md:40-42`,
  WAY-19); 10xDevs without a link (WAY-27).
- C4: WAY-242 carries WAY-200's split; one bullet in `product-guidelines/reading.md` like WAY-216's;
  the testing skill mirrors only the coding skill's "A new kind".
- C10: WAY-235 `narrows WAY-168` (refusal invariants named by the trust-boundary rule, though their
  test checks behaviour), within task Q2 and item 1.
- C11: an exclusion's return condition is part of what the product decision allows, not a review
  trigger (WAY-24); the AI tool's fact worded as the tool's behaviour in the version used (WAY-77).
- C12: WAY-250's three to five charges are per level (task row 24).

## What to check

Coverage of every *To do* item, every answered question, every row of *Settlements to record*
(row 25 per C3) and every entry of the spec's *Foundation entries*; fidelity to the task's sources
(no row written with another meaning, nothing widened, the Q14 cut list absent); contradictions
between the new or edited entries and the rest of the foundation; the templates, skill and reading
against the decisions they cite; the entry points current; checks that the reports claim, with
their commands and exit codes.

## Report

Return a short message: the report's first line, its path, and a one-line check result naming what
you ran with exit codes and what you did not run. Grade each finding as the method gives, with its
place in the code and its slice.
