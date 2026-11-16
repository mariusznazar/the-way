# Fix report — renumber-decisions-on-merge (findings I-1, I-2, M-1)

**Status:** done

## Commits

- `059b891f` — Check the renumbering pass by counts and leave an earlier conversion row as written
  (WAY-403). On top of `34db2685`; no amend.

Files: `task-cycle/skill/SKILL.md` (+11 / -7 approx.), `foundations/decisions.md` (WAY-403 only).

## Findings and how each is fixed (no finding held wrong)

- **I-1** (`task-cycle/skill/SKILL.md`, "The renumbering of the task's decisions", items 1 and 3):
  the search for old numbers is replaced by a count. Item 1 now also has the author count, for each
  old number, its references in the texts item 2 rewrites (texts that stay as they are left out).
  Item 3 counts again, in the same texts, each new number: it stands as many times as the old
  number that became it stood before the pass; an old number that is no new number stands there no
  more; and the text says outright that a search for an old number that is also a new one finds
  correct references and proves nothing. Why it holds on an overlap: a new number inside the old
  range only receives the references of the number mapped to it, since all of its own references
  moved on. Why it still catches a miss: the last number of each chain (504 in 500..502 -> 502..504)
  is no old number, so nothing can compensate a missed reference there.
- **I-2**: I chose the second way out: **earlier conversion rows stay as written, and the
  conversion is read as a chain of rows.** Item 2 now leaves "the rows of an earlier
  reconciliation's conversion" as they are, with its reason ("true as it was written, and a reader
  follows the rows one after the other"); item 5 adds "the rows of earlier reconciliations stay
  beside it". Rejected: rewriting only the right side of an earlier row (reading first number ->
  present number in one row). Its cost: the pass must tell the two sides of a row apart in a free
  text table, a slip corrupts the one place that keeps the conversion readable, and the row would
  stop saying what was true when it was written (a reader holding a number from between the two
  reconciliations would meet a row that names it nowhere). The cost of the chosen way: a reader of
  an old number follows two rows after a second renumbering. Step 3 treats the earlier rows
  consistently: they are among the texts left out of both counts (item 1: "those that stay as they
  are left out").
  WAY-403 changed with it, in the same commit: paragraph 1 now says that "the rows that give the
  conversion of an earlier reconciliation" stay as they are; paragraph 2 adds that a reconciliation
  that renumbers again adds its own row beside the earlier ones; the complying example gives the
  second row (502 -> 505, 503 -> 506, 504 -> 507) and leaves the first as it is; the violating
  example now has the corrupt row of the reviewer's evidence (500 -> 505, 501 -> 506, 505 -> 507);
  *Rationale* says that the rows are read one after the other and carries the price (a reader
  follows two rows). *Rejected* is unchanged: the rewrite of the earlier row is not a way the task's
  source keeps, so it is not written there (WAY-134).
- **M-1**: `WAY-35`/`WAY-355` replaced by bare numbers, "so that `35` is not found in `355`".

## Checks

- `python -B .runs/author-fix/author-fix-passcheck.py` (kept as `reports/author-fix-passcheck.py`) —
  exit 0, prints `ok`.
- `python -B elements/common/foundation_check.py --skip-test-citations` — exit 0, `0 errors`
  (`reports/author-fix-foundation-check.txt`).
- `python -B gate/run_tests.py task-cycle` — exit 0, 534 tests, OK (skipped=2).
- `python -B gate/run_tests.py product-guidelines` — exit 0, 14 tests, OK.
- `python -B gate/run_tests.py elements/common` — exit 0, 257 tests, OK.
- Not run: the full gate (the cycle's); `installation` and `agent-instructions` not rerun, since the
  change touches no file they read beyond `foundations/decisions.md` and `SKILL.md` text that they
  passed on before this fix (installation 62 OK, agent-instructions 37 OK on `34db2685`).

One-line result: all focused checks pass; the full gate was not run.

## Own-work check

Requirement the first change most likely did not meet: that the check of the pass holds on an
overlapping map and that a second pass keeps the first conversion readable. The script
`reports/author-fix-passcheck.py` runs the pass of item 2 and the count of item 3 as the text gives
them:
- map 500..502 -> 502..504 on three texts (plus a longer number `5020` and a number `35` that must
  stay, and a human's remark kept out of the counts): the pass gives the expected texts, the count
  passes, and a search for old `502` still finds correct references (the reviewer's I-1 shown);
- the count fails for a text the pass missed, for a missed old 502 inside a rewritten text, and for
  a pass done decision by decision (the chain);
- second pass 502..504 -> 505..507: the old text's mechanism corrupts row 1 into `500 -> 505, 501 ->
  506, 505 -> 507`; with the row left alone, a reader holding 502 as first borne takes row 1
  (502 -> 504) and row 2 (504 -> 507), the chain gives `500 -> 505, 501 -> 506, 502 -> 507`; the
  count of the second pass passes with row 1 left out.
It showed all of the above (exit 0). What it does not test: the human running these steps; the text
is read by an agent and the script is the mechanism written out.

## Choices

- I-2 way out: leave earlier rows as written (above); rejected: rewrite only the right side.
- The count excludes the stay-as-is texts by saying so in item 1 and relying on "the same texts" in
  item 3, instead of a rule for each kind of text; cost if wrong: an author who counts a remarks
  file will see a wrong count and has the sentence to correct it.
- Kept the text short, as the handoff asks: item 3 grew by about two lines.

## Reaches beyond the dispatch

none beyond the two named files (`reports/review-whole-findings.md` read whole; the full
`reports/review-whole-report.md` was not read, the findings file holding the reviewer's words).

## Working copies

`.runs/author-fix/` (the edit scripts, the check script, the test outputs): removed whole before the
return (`ls .runs` shows `orchestrator`, `task-cycles`). Kept in `reports/`:
`author-fix-passcheck.py`, `author-fix-foundation-check.txt`. Nothing remains.

## Unread material

- `reports/review-whole-report.md` (the full review): not read; I read the findings file whole and
  the handoff whole.

## Searches not found or unclear

none
