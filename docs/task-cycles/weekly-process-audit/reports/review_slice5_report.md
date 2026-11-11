FAIL c2a016909936be7a3b53ccb28b81d838c71a58de

# Review of slice 5 — problems and issues from the register (`9cf2633..c2a0169`)

`git rev-parse HEAD` = `c2a016909936be7a3b53ccb28b81d838c71a58de`, confirmed. One commit, `c2a0169`: `process-audit/audit_count.py` and `process-audit/test_audit_count.py`.
Worktree read only (`git status --short` empty after every check). Read: `task-cycle/review/SKILL.md` whole, the review handoff, the executor's handoff (current ranges, the slice, the entries, binding choices 1-7), the executor's report (claims),
the task passages it names, `process-audit/problem_register.md`, WAY-334 to WAY-336 and the script invariants as the handoff names them, the whole diff and the new code.
Counts: 1 blocking (Important), 3 Minor, 0 out of scope.

## Blocking finding

### 1. Important — a refused row of the register is invisible in the figures it belongs to: the cycle shows `0`, an open issue shows `—` ("no problem yet")

Place: `process-audit/audit_count.py` `analyse` (the lines that build `cycle_rows`, `members` and `open_rows`; counts are taken from `register.problems` only, refused rows go to `unknown` only)
and `read_register` (a row refused for its class, weight or issue is dropped from `register.problems`).

What is wrong. Binding choice 1 says a refused row gives "`unknown` for what depends on it, never an abort"; the slice says a problem that cannot be placed "gives `unknown` with its reason". The code lists the refused row in *Unknown values*
and leaves every count it belongs to as if the row did not exist:
- Scratch A: one cycle, one open issue `open-one`, one problem row for that cycle and issue with the weight `Blocker`. The row is refused (listed in *Unknown values*), and the result gives
  *Problems by cycle* `none 0 0 0 0` for the cycle and *Open issues* `open-one 0 0 0 —` — "`—` where the issue has no problem yet", in the table's own wording. The issue has a problem; the days of waiting, which the human weighs, are not "none".
- The executor's own tests pin this: `test_a_class_named_in_two_rows_refuses_both_and_its_problems_with_it` asserts `none 0 0 0 0` for a cycle whose only problem was refused, and `test_crafted_rows...` asserts a count of 1 for a cycle with seven problem rows of which six are refused.
- The same holds for a fixed issue: a refused problem of a fixed issue is in neither "holds" nor "lacks" nor any `unknown` column.
A row refused for a cause that still names its cycle (valid Repository and Record, bad class or weight or issue) is a known cycle with an incomplete count.

Why it matters. WAY-335 asks that the weighing of an issue be the human's, on material the audit gives; slice 6 and the weekly session read these tables. A zero that means "unreadable" and `—` that means "none yet" are figures that look measured, the class of defect the
reviews of slices 3 and 4 failed on ("`unknown`, never zero"). A typo in a user's register (one weight, one class) silently shortens a cycle's count and can shorten an issue's waiting. The listing in *Unknown values* is there, but the tables a reader and the next slice use do not point to it.

Direction (the author's choice): give each cycle row, each fixed issue row and each open or dropped issue row a count of refused rows that belong to it (known by Repository + Record, or by Issue name), and write the cycle's count as `unknown`, or "at least n", where that count is above zero; an open issue whose
rows are refused gets `unknown` days, not `—`. Rows with no usable Record or issue name stay in *Unknown values* only.

Evidence: scratch `scratch6.py` scenario A (`a scratch file outside the repository`), and the two tests named.

## Minor findings

### 2. Minor — the days of waiting count from the first commit of the cycle, not from the commit the *Record* column names (binding choice 5)

Place: `analyse`, `first = min(cycle.committed ...)`. Binding choice 5 says "the days from the date of the earliest commit named in the *Record* column among the issue's problems"; the template says *Record* is, for a cycle committed again, the commit of the copy that holds the report the problem
was found in. The code uses the cycle's *Committed* date (its first copy). Scratch B: a cycle first committed 2025-10-09, a later copy 2025-11-01 named by the problem, run day 2025-11-11: the result says `33` days, the binding choice gives `10`. The executor's report states the source of the date, not that it departs from the choice. The cycle's first date is the earlier,
so the figure is longer, never shorter, and a case of a corrected cycle only; Minor. Either the code follows the choice (date of the named commit, which the command can read with `git log -1 --format=%ct` or from the cycle's copies) or the orchestrator confirms the cycle's date.

### 3. Minor — nothing bounds the work or the output by the register's size

(a) Output: 300,000 refused rows (`| a |`, a 2.1 MB register) give a 19.4 MB result in 5 s (scratch D); one refused row writes about 60 bytes into *Unknown values* from 6, so the cap on a read (4 MiB) and on a copied text (200 characters) hold but the count of rows copied is unbounded.
(b) Time: `analyse` scans all problems for every issue (`members = [... for problem, cycle in found if problem.issue == name]`): 8,000 issues x 8,000 problems took 4.3 s (scratch C, 1,000: 0.9 s, 4,000: 1.6 s), so a register of the largest size (tens of thousands of each) is quadratic, a minute or more, not a hang.
(c) Git: every distinct (pin, fix) pair costs a `merge-base` call and each distinct commit text two `rev-parse` calls, each with a 120 s timeout; a register of many fixed issues over many pins makes thousands of calls. Real registers are small; a cap or an index by issue (one pass) and a limit on refused rows listed ("and n more") would close it.
The slice-3 lesson asked for a cap on every read and on texts copied; the new read is capped, the work after it is not. Minor because the register is the user's own file and the cost grows only with a register far larger than any real one.

### 4. Minor — untested branches the figures depend on

The executor names the ambiguous short hash (`resolve`, `len(names) > 1`) as untested; I could not build a 7-character collision either. Also untested: the *Problems whose cycle is not read* columns of *Fixed issues* and *Dropped issues* (the stdin run only), a pin of the-way that is a short hash resolved by `--disambiguate`, a shallow clone of the-way (`shallow` turns "lacks" into `unknown`), a doubled heading of a table (exit 1) and a doubled header row inside a table. By reading, the code does the right thing in each: a name that matches two objects is `unknown`,
a shallow answer "lacks" is `unknown`, a doubled heading is a register error. Minor.

## Checks of the brief (no finding where none is stated)

- **Exit of a missing table.** Binding choice 1: "a table missing altogether is an `Error:` of the register (exit 2 only where the register itself cannot be read at all, as for the other entries)". The code writes the result and exits 1 with `Error: the register of problems: ...` on stderr; exit 2 only for an unreadable, oversized or non-UTF-8 register. That follows the parenthetical, so it is not a departure from choice 1. It is not a defect: the result is written with the missing table's problems `unknown`
  and a scheduler sees a non-zero exit. The cost is that exit 1 now also means "register table missing" beside "repository could not be read" (documented in the docstring).
- **Trust boundary, hostile input.** Control characters, escape sequences and a bar: names are validated by `NAME` (lower-case letters, digits, hyphens, at most 80 characters, length tested before the pattern, hyphens between runs so the pattern cannot backtrack), texts copied into the result are cut at 200 characters, every cell of the new tables and of the
  unknown rows passes `cell()` (the test asserts the result holds no non-printable character; I read `table()` and the render). Dates: `date.fromisoformat` after a fullmatch, in `try`. Numbers: counts only; no conversion of register text. A 4 MiB table: the read is capped at 4 MiB + 1 and refuses with exit 2 and nothing written. A doubled header: a heading that appears twice is a register error; a repeated header row in a table is a row refused for its class name. A `Fix` not in the-way's
  history: the issue's holding columns are `unknown` with the reason; a `Fix` that is no 40-hex commit refuses the issue and then its problems. A pin `unknown`: counted under "unknown pin". An issue name in no row: the problem is refused. A problem whose *Record* is a commit of another repository (or of an unread one): not found among the cycles, `unknown`, not dropped. Failure of a row never aborts: each refusal is a row of *Unknown values*; I found no path that raises on the inputs I tried.
- **Git (`script-subprocesses`).** The new calls are `merge-base --is-ancestor`, `rev-parse --disambiguate`, `rev-parse --verify`: git only, read only, the docstring lists them. No value of the register reaches git unvalidated: the pin and the fix are lower-case hexadecimal of 7 to 40 characters (`SHORT_HASH`, `FULL_HASH` lowered), so none begins with `-`; `merge-base` gets the full hashes git returned. `--end-of-options` is not used, and is not needed given the pattern.
  A short hash that matches several objects is `unknown` (conservatively, also when the other object is no commit). A checkout of the-way that git cannot read, or that is shallow, makes the answers `unknown`.
- **Binding choices.** 1 (parse by heading and header; refusals): kept except finding 1; 2 (cycle by repository and record; later copies are the same cycle): `index` maps the first and the later commits, tested; 3 and 7 (count rows, a corrected cycle once): kept; 4 (ancestry in the-way's checkout): kept; 5: the fixed and open figures are by pin and by cycle, the days by finding 2; 6 (register order, no ranking): see below.
- **No ranking.** Issues are listed in the register's order in *Fixed*, *Open* and *Dropped issues*, classes in the register's order inside a cycle, cycles in the existing order (repository, date, folder); nothing is sorted by count or waiting. The test sorts nothing and mutation by sorting fails it (the executor's mutation; I read the test and the code). Confirmed.
- **Deterministic result.** `--today` is parsed by `day_of` (a date or a clear error, exit 2); the day of the run is only used for the days and the dated file name, taken from `--today` or the UTC day; no register value reaches the file name. The *Unknown values* order is the order of
  first appearance (`dict.fromkeys`), the result is built from lists, so the same input and `--today` give the same bytes. I ran the stdin run in the executor's check only; I read the code path.
- **Which repository answers whether a pin holds a fix; from what date the days count:** named in the report as asked: the checkout of the-way (the `repository` entry under `the-way`, or the script's own); from the cycle's first commit date (see finding 2) to the `--today` day.
- **Foundation.** No foundation file is touched; WAY-329 to WAY-335 compared with the code: the audit counts problems by row (333), by pin holding the fix and never by date (334), no priority from the count (335), classes and weights as the template gives them (332). The docstring says it.

## Declined to judge

- The names of the register's sections in the result and the choice that issues are counted by problems for fixed issues and by cycles for open ones (the executor's choice 4; the task asks "the problems of that issue" and "the number of cycles").
- Slice 6's use of the new tables.
- The change of the dated file name from the local day to the UTC day (executor's choice 9): the binding choice gives `--today` the default of today in UTC.
- Whether the-way checkout `repository` entry must now be valid on every run (executor's choice 10; a user with a wrong entry and `--repository other` now gets exit 2).

## Checks run

| Command | Exit |
|---|---|
| `git rev-parse HEAD`; `git log 9cf2633..c2a0169`; `git diff 9cf2633..c2a0169` (read whole) | 0 |
| `python -B gate/run_tests.py process-audit` (worktree, bytecode off) | 0 — 85 tests OK, 293 s |
| `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` | 0 |
| `python -B elements/common/foundation_check.py` | 0 — 0 errors |
| scratch `scratch6.py` (outside the worktree, temporary repositories through the tests' helpers): A refused row of an open issue, B later copy named by the problem, C scaling 1,000/4,000/8,000 issues x problems, D 300,000 refused rows | A: cycle `none 0 0 0 0`, open `—`; B: 33 days; C: 0.9 / 1.6 / 4.3 s; D: 2.1 MB in, 19.4 MB out, 5.1 s |
| `git status --short` after the checks | empty |

Not run: the full suite; the run on this repository with stdin closed (the executor's, exit 0 reported; not repeated); a real 7-character hash collision (could not be built cheaply).

## Reaches beyond the handoff

- `process-audit/problem_register.md` whole (named by the slice) and `task.md` lines 20-65 (the passages the slice names).
- `task-cycle/remarks_check.py` (`split_lines`, `fenced_flags`) by name only, as the executor used them.
- Nothing else.

## Unread material

- `plan.md` (the handoff gives the slice and the rows); the reports of slices 3, 4 and the correction (shapes only, as the earlier reviews of this cycle read them).
- `audit_count.py` lines 140-955 (the code of earlier slices) read only where the new code calls it (`cell`, `table_cells`, `is_separator`, `Cycle`, `Read`); the diff and the new section read whole.
- Foundation entries WAY-38, WAY-48, WAY-89, WAY-320, WAY-329, WAY-332 to WAY-336 and the three script invariants: read in the earlier reviews of this cycle and here as far as the comparison needed (WAY-333 to WAY-336 and the invariants); WAY-320, WAY-332 not read again in full.

## Searches not found or unclear

- An ambiguous 7-character hash: not found in any repository at hand, not built.
- Whether *Record* in real registers names the first commit of the copy or a later one: not found; the template allows both, so finding 2 is a case the register may produce.
- Whether the weekly skill (slice 7) will read *Problems by cycle* with the `none` row as "no problem": unclear; it bears on finding 1.
