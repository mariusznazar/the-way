PASS 34170588d1169fb09c681df112173ad413d34e5f

# Review of the second correction (`410113b..3417058`)

`git rev-parse HEAD` = `34170588d1169fb09c681df112173ad413d34e5f`, confirmed. One commit, `3417058`: `process-audit/audit_count.py`, `process-audit/test_audit_count.py`, `process-audit/SKILL.md`.
Method: `task-cycle/review/fix.md` (the human's answer and the two findings take the findings file's place) and section 2 of `task-cycle/review/SKILL.md` for the diff. Read: `correction2_handoff.md`, `correction2_report.md` (claims), the whole diff, WAY-335 (the decision the code cites for the fixed issues; the correction calls the frequency decision WAY-336, which in the log as it stands is the decision on cost, see Searches).
Worktree read only (`git status --short` empty after every check). Counts: 0 blocking, 3 Minor, 0 out of scope.

## (a) The guard of the first question — MADE

`read_contradiction` no longer looks for a denying word anywhere in the item: for each occurrence of "open design choice" it reads at most 60 characters before it, cuts them after the last clause mark (`; : , . — – ( ) [ ] ! ? "`) and looks for a denying word (`no not none nor never without neither nothing`) among the last four words of what is left, or a contracted `n't` in that clause. Linear: `str.find`, a bounded slice, a backwards character scan, `[a-z]+`.

Before/after, run on `3417058` (`scratch9.py`; the previous head's behaviour is by the guard's code, a denial word anywhere in the item gave `unknown`):
- My example from the earlier review and the template's own form, `10:32, open design choice found in the auth flow; report reports/x.md; foundation entries none; reset to abc1234; next route: spec`: **`yes`** (was `unknown`). Also `10:32, open design choice, report reports/x.md`: `yes`.
- Negated forms, all `unknown`: `a time overrun; no open design choice`, `it was not an open design choice`, `discarded without an open design choice`, `found no evidence of an open design choice`, `reserved choice, not an open design choice`, `neither a size problem nor an open design choice`, `it wasn't an open design choice`, `NO OPEN DESIGN CHOICE`, `no reserved choice or open design choice`.
- Crafted: the phrase 20,000 times (0.14 s), `no ` 200,000 times before the phrase (0.003 s), 500,000 characters with no clause mark (0.002 s), ESC / `|` / control characters: each answers at once, no exception; the test also runs five such items through the command and finds no non-printable character in the result.

## (b) The open issue's count of cycles — MADE

`analyse`: the column is `max(len(hit) - 1, 0)`, `hit` the distinct cycles (a cycle copied again once) holding a problem of the issue; it reads `at least n` where `refused + not_read` is above zero; the header is `Cycles its problems came back in`. Run (`scratch11.py`, temporary repositories):

| Case | Before (cycles in which problems stand) | After |
|---|---|---|
| one problem in one cycle | 1 | `0` |
| three cycles | 3 | `2` |
| three cycles, four problems (two in one) | 3 | `2`, problems `4` |
| two cycles and a problem of an unread repository | 2 | `at least 1`, days `unknown` |
| one cycle and a refused row | 1 | `at least 0`, problems `at least 1`, days `unknown` |
| no known cycle, one problem of an unread one | 0 | `at least 0` |

Days of waiting: the block that computes them is untouched by the diff (`days` lines unchanged); the runs show the same `398` days in the exact cases and `unknown` where a cycle is unread or a row refused, as before. The order of the issues stays the register's; the open-issue and dropped-issue columns other than this one are unchanged. `process-audit/SKILL.md` says in its matter 3 that the first cycle does not count and `0` is a problem seen once;
`python -B agent-instructions/skill_entry_points.py` reports "entry points are current" (exit 0). The module docstring and the paragraph above the table say the same.

## The executor's concerns

**1. The count and the ordering the handoff asked for (the executor did not order the cycles).** Sound. The number of cycles minus one does not depend on which cycle is excluded, so an order adds nothing to the count and would add a place for an unknown date to turn it to `unknown`. Where a refused row or an unread cycle is involved, the count is a lower bound and is written so: "known cycles less one" is never above the true count, because the true number of cycles is at least the known number (an unread cycle or the cycle of a refused row can only add cycles); with no known cycle, `max(…, 0)` gives `at least 0`. I ran each case (table above); the first cycle excluded is never needed to decide any figure shown. The days of waiting, which do use the earliest commit date, are unchanged and `unknown` where a cycle is unread, so they cannot be too short. Not a defect.
   One point only: for a problem of an unread cycle (or a refused row) the lower bound `at least n` of *Cycles ... came back in* can sit beside an exact-looking *Problems* count only in the case a row is counted, and the executor writes both with `at least` by the existing rule, so the table stays consistent.

**2. A denial after the phrase now reads `yes`; a comma ends the clause.** Both are consequences of the direction given to the executor ("look only at the words just before the phrase") and the human's answer; the correction follows it, and the template's own form reads `yes` as asked. They are not defects of the correction, but they are a limit that breaks "never a wrong `yes`" in forms that can be written, so I put them to the orchestrator as Minor 1 and 2 with a cheap closing.
   The comma end is right for the template's form (`10:32, open design choice, …`) and for `not found, open design choice at the start`; it fails for a negated list, Minor 2.

## Findings

### Minor 1 — a denial after the phrase, or more than four words before it, gives a wrong `yes`

Place: `denied_before` (`audit_count.py`), the window of four words before the phrase in the same clause. Run, all `yes`: `open design choice not found`, `open design choice: ruled out`, `reserved choice; an open design choice did not apply`, `found no evidence at all of an open design choice`, `there was no sign whatsoever that this was an open design choice`. The previous head, which looked for a denial anywhere in the item, gave `unknown` for each.
Why it matters: Q1's `yes` is the one answer the audit must not give wrongly (the executor's own rule). Triggering text is prose about an attempt that was *not* discarded for an open design choice; no archived record holds a *Discarded attempt* other than `none`, so the case is a reading rule, not a seen form. Direction: also look at the rest of the same clause after the phrase for a denial (`not`, `no`, `did not`, `n't`, `ruled out`): the template's form `open design choice found in the auth flow; …` has no denial in its clause, so it stays `yes`. Cheap, the same helper.

### Minor 2 — a denial that governs a comma-separated list is cut off at the first comma

Place: `denied_before`, `CLAUSE_MARKS` includes `,`. Run, all `yes`: `No attempt was discarded for a reserved choice, an oversized change or an open design choice.`, `No attempt discarded: reserved choice, oversized change, open design choice`, `Nothing was discarded, whether a reserved choice, a size problem or an open design choice.` The previous head gave `unknown`.
The template's own line lists the kinds in a comma list (`open design choice, reserved choice or oversized one-author change`), so a prose denial of the list is the natural wrong form. Direction: an item that begins with a denying word (`no`, `nothing`, `neither`, `not`) reads `unknown`, as `none …` already does (`reads_none_first`); together with Minor 1 this closes the wrong `yes` without hurting the template's form. The executor's choice of the comma is right for `not found, open design choice at the start`; the answer is to guard the item's start, not to move the comma.

### Minor 3 — the tests pin the two wrong-`yes` forms as the expected answer

Place: `test_a_denial_stands_only_where_it_comes_just_before_the_phrase`: `("not found, open design choice at the start", "yes")` and `("a time overrun; open design choice at the start; no code was kept", "yes")` are right readings; but no test covers a denial after the phrase or a denied list (Minors 1 and 2), so the suite cannot tell the gap from the intended behaviour. A subTest for each form, expected `unknown`, would fail today and pass with the closing above. Not a weakened test: no existing assertion was relaxed (see below).

## The four changed existing tests: none weakened

Each changed only the third cell, the cycle count of *Open issues*, to the new derived value, with the rest of the row unchanged:
- `test_open_issues_wait_from_the_cycle_commit_to_the_day_of_the_run` and `test_an_open_issue_waits_from_the_copy_its_problem_names`: `1` to `0` (one cycle holds the problem); the days (`10`) and the problems (`1`) are still asserted, so the days of waiting are pinned unchanged.
- `test_open_issues_are_listed_in_the_register_order_not_by_their_returns`: `1, 2` to `0, 1`; the order of the issues, which the test protects, is still asserted.
- `test_a_record_that_adds_the_records_of_two_cycles_names_neither`: `0` to `at least 0`: stricter than before (an unread cycle is now said).
The new tests cover the exact counts, the lower bounds for a refused row and an unread cycle, and a cycle copied again; I read them and recomputed their expected values by hand (`seen-thrice` 2, `cycle-lost` `at least 2`, `row-refused` `at least 1`).

## Hostile input in what the correction changed

(a): the scan is bounded to 60 characters per phrase and the phrases are found in one `str.find` pass, so the work is linear in the item (a 4 MiB item of phrases is 20,000 x in 0.14 s per 380 KB); no new pattern; no text of the item is copied into the result (the reasons are fixed sentences); the casefolded text is indexed consistently. A partial word at the left edge of the window can read as a denial (`…not` cut from a longer word) and then answers `unknown`, the safe side.
(b): the new code writes integers and the fixed word `at least` through `counted`, and the header and paragraph are constants; there is no conversion of register text, no date computation (the days block is untouched), and every cell still passes `cell()`. A register with many cycles is counted in the same dictionary pass.

## Declined to judge

- Whether the audit's wording of the decision on frequency should be edited (the executor read WAY-336 and left it; the log numbers: the decision on frequency is WAY-336 in the executor's words, but WAY-336 of the log is the decision on cost — see Searches); neither text is changed by this commit and none of its sentences is false after the change.
- The fixed issues' counting (problems that stand, not returns): outside the two items the human asked for.

## Checks run

| Command | Exit |
|---|---|
| `git rev-parse HEAD`; `git log 410113b..3417058`; `git diff 410113b..3417058` (read whole) | 0 |
| `python -B gate/run_tests.py process-audit` (worktree, bytecode off) | 0 — 124 tests OK, 152 s |
| `python -B elements/common/foundation_check.py` | 0 — 0 errors |
| `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` | 0 |
| `python -B agent-instructions/skill_entry_points.py` | 0 — entry points are current |
| scratch `scratch9.py` and `scratch10.py` (the guard on 21 + 3 forms, with timings), `scratch11.py` (six open-issue cases) in `a scratch file outside the repository` (outside the worktree; temporary repositories through the tests' helpers) | as above |
| `git status --short` after the checks | empty |

Not run: the executor's stdin-closed run on this repository (the template register holds no issue, so the table is empty; the tests run the command as a process).

## Reaches beyond the handoff

- `foundations/decisions.md` WAY-335 (read, `### WAY-335` to `### WAY-336`) — to check the text of the decision the docstring cites for the fixed issues. Nothing else.

## Unread material

- `process-audit/audit_count.py` and `test_audit_count.py` outside the diff and the code it calls; the executor's report read whole; WAY-336 (cost) known from the earlier reviews; `task-cycle/review/fix.md` read whole.

## Searches not found or unclear

- The numbering: the handoff and the executor call the decision on frequency WAY-336, and the docstring and the table paragraph cite WAY-336 for "never ranked by their counts"; in the log as it stands WAY-335 holds the decision on whether a fix works and WAY-336 the cost of a cycle, and the decision on frequency is not among the text I read. I did not find which number carries it; the citations in the code and the paragraph may be off by one and are not a finding of this correction (the code already cited them before it).
- A record with a *Discarded attempt* other than `none`: none in the archive, so the guard's forms are tested on text written for the tests.
