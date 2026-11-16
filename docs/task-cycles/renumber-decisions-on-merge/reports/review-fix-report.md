PASS 059b891f1dcb574fedaa690565513548dbc9abc9

# Review of the fix — renumber-decisions-on-merge

Range: `34db2685148207b901f8a19c2629b0e14af04c91..059b891f` (one commit, `059b891f`; files
`foundations/decisions.md` +18 / -12 and `task-cycle/skill/SKILL.md` +14 / -10). `git rev-parse HEAD`
is `059b891f1dcb574fedaa690565513548dbc9abc9`, the head given. Bound by the findings file
`reports/review-whole-findings.md` (I-1, I-2 blocking; M-1 Minor within the task), as
`task-cycle/review/fix.md` gives. Read whole: the handoff, the findings file, the fix report, its
own-work script `reports/author-fix-passcheck.py` and the full diff of the range.

## The findings

- **I-1 — fixed.** `task-cycle/skill/SKILL.md:701-703` now has the author count, before the pass,
  the references of each old number in the texts step 2 rewrites, and `SKILL.md:712-716` counts
  each new number after it against the old number that became it, demands zero of every old number
  that is no new number, and says outright that a search for an old number that is also a new one
  proves nothing. The check no longer fails a correct pass with an overlap, and it catches a missed
  reference: a missed old number that is also a new number makes that new number's count one too
  high, and a missed one that is not stands where it must stand zero times. Evidence: my scratch run
  over 20 000 random overlapping and non-overlapping maps accepted every correct pass and caught
  every single missed reference (below); the author's script shows the same on the entry's own map
  and also fails a pass made decision by decision.
- **I-2 — fixed, by the second way out the finding named.** `SKILL.md:709-711` leaves the rows of an
  earlier reconciliation's conversion as they are, "true as it was written", and `SKILL.md:721-722`
  keeps them beside the new row; the earlier rows are thereby among the texts left out of both counts
  of step 1 and step 3, as the finding asked ("step 3 then has to name the earlier rows among what
  keeps old numbers"). WAY-403 moved with the skill in the same commit
  (`foundations/decisions.md:6240-6247`): its first paragraph names those rows among what stays,
  its second says a reconciliation that renumbers again adds a row of its own, the complying
  example gives the second row and the violating one the corrupted row of my evidence, and
  *Rationale* names the price (a reader follows two rows). *Rejected* is unchanged, rightly: the
  rewrite of an earlier row's right side is no way the task's source keeps, and the decisions
  template does not let a derived way into a row's *Rejected*.
- **M-1 — fixed.** `SKILL.md:708` now reads "so that `35` is not found in `355`"; no `WAY-35` or
  `WAY-355` stands in the skill (grep, exit 1).

## Agreement of WAY-403, the skill and the task

- The skill and WAY-403 say the same: one pass, earlier conversion rows and the human's quoted
  remarks and later texts left as they are, a row of its own for each reconciliation that renumbers,
  no other note of the conversion. `task-cycle/record_template.md:98-101` ("the row of the
  reconciliation ... gives each old number and the new one it now bears") stays true of each row.
- The task: To do 2 lists two kinds of text that stay ("teksty zapisane później i uwagi Mariusza
  cytowane słowo w słowo"); the fix adds a third, the rows of an earlier conversion. Row 2 and
  question 2 keep the conversion so that an old number stays readable ("nigdzie — ... staje się
  nieczytelna"), and the chain of rows keeps every old number readable, while rewriting those rows
  is what broke it. So the addition serves the task's purpose and goes against none of its answers;
  it is a choice of the cycle beyond the task's text, which the request's section for the human's
  decisions should put under *You accept by merging* (the orchestrator's to place). Not a finding.
- WAY-403's form still holds (WAY-05): the first paragraph keeps three binding sentences, the second
  one. The foundation check reports 0 errors.

## New in the fix

### Critical / Important

none

### Minor

**N-1. The chain of rows does not say from which row a reader starts.** Within the task; blocks
nothing (`fix.md`), goes to the request's list.

- Place: `task-cycle/skill/SKILL.md:710-711` ("a reader follows the rows one after the other") and
  `foundations/decisions.md:6281-6282` ("the rows are read one after the other").
- What is wrong: after a second renumbering one number can stand on the left of both rows with two
  meanings. In the entry's own complying example, 502 is the first number of the third decision
  (row 1: 502 -> 504, then row 2: 504 -> 507) and the number the first decision bore between the two
  reconciliations (row 2: 502 -> 505). A reader who starts at the first row with a number written
  between the reconciliations goes 502 -> 504 -> 507 and lands on the wrong decision.
- Why it matters: little — the rows of *Events* carry their times, and a reader who knows when the
  number was written starts at the first row after it; the ambiguity belongs to any conversion over
  two renumberings, and the fix did not create it but it now relies on the reader resolving it. A
  half sentence ("starting at the first row after the number was written") would settle it.
- Evidence: the complying example of WAY-403, `foundations/decisions.md:6251-6260`, read with the two
  rows it gives.

### Out of scope

none

## Declined to judge

none

## Checks

- `git rev-parse HEAD` — `059b891f1dcb574fedaa690565513548dbc9abc9`; `git log` and `git diff
  34db2685..059b891f` — one commit, two files, read whole.
- `python -B -I .runs/task-cycles/renumber-decisions-on-merge/reports/author-fix-passcheck.py` —
  exit 0, `ok`.
- `python -B -I .runs/review-fix/scratch_count.py` (my own: random maps with 1-8 new decisions, the
  target branch taking 1 to n+3 numbers, 1-30 references; the count of steps 1 and 3 on a correct
  pass and on a pass that misses one reference) — exit 0, `trials 20000 correct passes accepted
  20000 single misses caught 20000`.
- `python -B elements/common/foundation_check.py --skip-test-citations` — exit 0, `0 errors`.
- `python -B gate/run_tests.py product-guidelines` — exit 0, OK.
- `grep -n "WAY-35\b\|WAY-355" task-cycle/skill/SKILL.md` — exit 1, none.
- Not run: the product's full gate (CI's), as the handoff gives; `task-cycle` and `elements/common`
  tests not rerun by me — the fix changes only text the author's runs of both passed on (534 and
  257, exit 0), and none of their tests reads the changed sentences beyond what the foundation check
  covers.

## Reaches beyond the dispatch

- `task-cycle/review/fix.md`, whole (the method's variant for a fix).
- `task-cycle/record_template.md:98-101`, to check that the *Events* sentence still agrees.

## Working copies

`.runs/review-fix/` of the worktree held `fc.txt`, `pg.txt` (check outputs) and `scratch_count.py`
(the scratch run quoted above). No worktree, clone or screenshot. The directory was removed whole
before the return; nothing is kept in `reports/`. Remainder: none.

## Unread material

0 decisions of an index read whole in this review: it is the review of a fix, bounded by the
findings file, and selects no foundation of its own; WAY-403 was read whole as the diff leaves it.
none.

## Searches not found or unclear

none
