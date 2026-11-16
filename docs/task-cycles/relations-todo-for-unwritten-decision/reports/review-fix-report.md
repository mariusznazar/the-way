PASS 68d8645c78e55bf751161fedd26dedf31cb43dbc

# Review of the fix — relations-todo-for-unwritten-decision

Range: `452f123d65de88143c91fe37b5633ecd341d88ee..68d8645` (one commit, `68d8645`). `git rev-parse HEAD`
in the worktree gave `68d8645c78e55bf751161fedd26dedf31cb43dbc`, the head of the dispatch. Bounded by
`reports/review-whole-findings.md` (I1, M1, M2, M3), as `task-cycle/review/fix.md` gives. Trust
boundary: no; irreversible operation: no.

## The findings, one by one

- **I1 — fixed.** `todo_item` now takes `typed`, and for *Relations* only (`known_part`,
  `elements/common/foundation_check.py:550`) treats an item that begins with `derives from` or
  `narrows` before the word `TODO` (`TYPED_TODO`, `:170`) as the `TODO` item. `known_part` reports it
  with one message that says the `TODO` item takes no relation type and gives the form (`:556-559`), and
  cuts the value there, so a number in the description is no longer read as a reference. Evidence:
  four new tests (`test_foundation_check.py:748-770`) cover the bare form, the form after a known
  relation and the described form with `ABC-77` in it, each asserting the message at line 22 and
  `1 error`; the author saw them fail before the fix (`FAILED (failures=7)`). My scratch runs on the
  real log at the fix head, WAY-71's *Relations* (`foundations/decisions.md:617`) replaced in turn:
  `derives from WAY-01 · derives from \`TODO — WAY-9999, later\`` → the type message, 1 error;
  `derives from WAY-01, derives from TODO — x` → the type message, 1 error; `narrows WAY-01 · TODO —
  the decision on saves, expected later` (the right form) → `0 errors`. The template sentence
  (`elements/decisions/template.md:75-77`), WAY-71's *violates* line (`foundations/decisions.md:633-634`)
  and the docstring (`foundation_check.py:50-51`) say what the script now does.
- **M1 — fixed.** WAY-126's second paragraph (`foundations/decisions.md:3737-3739`) now reads that the
  `TODO` is replaced by a reference "in a decision's *Relations* as `derives from <number>`, and in an
  invariant's *Derives from* as the number"; its complying example (`:3752-3754`) says the same. The
  paragraph stays one sentence (WAY-05), and the entry stays held by its pair (WAY-12). `derives from`
  is right here: WAY-71 opens the *Relations* `TODO` only for a decision the entry derives from.
- **M2 — fixed.** `test_relations_a_decision_on_a_second_line_is_still_checked`
  (`test_foundation_check.py:772-775`): a *Relations* value over two lines with no `TODO` and
  `narrows ABC-77` on the second, expecting the error at line 23 and `1 error`. The author broke the
  loop to `lines[:1]` and saw this test alone fail, which is the mutation the finding named.
- **M3 — fixed.** The docstring paragraph (`foundation_check.py:40-53`) is wrapped at 100 columns; no
  line of it runs past.

## New findings in the fix diff

### Critical

none

### Important

none

### Minor

**N1 — A relation type written with a capital or with two spaces still hides a bare `TODO` (within the task; blocks nothing).**
`elements/common/foundation_check.py:170`: `TYPED_TODO = re.compile(r"(?:derives from|narrows)[ \t]+(?=…TODO…)")`
matches the types only in lower case with one space between `derives` and `from`. Scratch runs at the
fix head: `- **Relations:** Derives from TODO` → `0 errors`; `- **Relations:** derives from WAY-01 ·
derives  from TODO` → `0 errors`. The template writes the types in lower case with one space, and
the script checks the spelling of no relation type anywhere else (`Derives from WAY-01` passes too),
so these values are typos the check of types would catch if one existed, not the form I1 named; that
keeps it Minor. A case-insensitive match with `\s+` between the words would close it at no cost.

**N2 — Two of the new tests overlap (within the task; blocks nothing).**
`test_relations_derives_from_todo_is_an_error` (`test_foundation_check.py:756-757`) asserts for
`derives from TODO` what `test_relations_a_bare_todo_behind_a_type_is_an_error` (`:751-754`) asserts
for `narrows TODO` and `derives from TODO —`; the value could be a subtest of the latter. The testing
guidelines name a duplicating test only under *Examples*, which binds nothing.

## M4 and M5

Not touched: the fix diff changes no line of WAY-287 and no row of the template's table of readers
(`elements/decisions/template.md:116`), as the handoff required.

## Against the task

The fix stays inside To do 3 and 4 (the template sentence, the script and its tests) and To do 1 and
5 (WAY-71's *violates* and WAY-126's sentence); nothing it adds checks a description against a
project definition (*Out of scope*), and *Origin* is unchanged. The *Questions to settle* answers
stand: the form is still `TODO — <the decision, and where it is expected>`, for any unwritten
decision.

## Structure of the code

`python -B task-cycle/change_file_sizes.py 452f123 68d8645` (exit 0): `foundation_check.py` 992 → 999,
`test_foundation_check.py` 1719 → 1748, `elements/decisions/template.md` 320 → 321,
`foundations/decisions.md` 10761 → 10762. `wc -l` of `foundation_check.py` gives 999: the author's
figure holds, one line under the 1000-line threshold of WAY-385. The size test, unmarked, in a
worktree of `68d8645` lists the same 11 functions and 2 files as on the base of the whole change, none
in `elements/common/`: the fix pushed nothing over a threshold. The next addition to this file must
begin with a move out of it (WAY-365); the author's report says so.

## Declined to judge

none

## Checks

- `git rev-parse HEAD` — `68d8645c78e55bf751161fedd26dedf31cb43dbc`.
- `python -B gate/run_tests.py elements/common` — exit 0, 257 tests OK (111.1 s).
- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`.
- `python -B task-cycle/change_file_sizes.py 452f123 68d8645` — exit 0.
- `python -B -m unittest agent-instructions.test_size_invariant` in a worktree of `68d8645`, the
  expected-failure mark taken off — exit 1, the same list as on the base, no file of this change in it.
- Scratch runs of `foundation_check.py` in that worktree with WAY-71's *Relations* replaced: the five
  values named under I1 and N1, results as given there; the file restored after each.
- Not run: `ruff` — still not installed (`ruff: command not found`, `No module named ruff`); I read the
  added lines for unused or undefined names and found none. The full gate — the orchestrator's
  (WAY-160).

## Reach beyond the dispatch

none — the fix diff, the findings file, the fix report, my own report of the whole change and
`task-cycle/review/fix.md`.

## Working copies

- `.runs/review-whole/head` — a git
  worktree of `68d8645` for the size test and the scratch runs; removed with
  `git worktree remove --force`, then `git worktree prune`; the directory `.runs\review-whole\` removed.
- `.runs/review-fix-tests.txt` — the
  output of the test run; removed. The reviewed worktree is unchanged (`git status --short` empty).

## Unread material

none — the handoff, the findings file, the fix report and the whole fix diff were read whole; the
decisions the fix touches (WAY-71, WAY-126) were read whole in the review of the whole change, and
their changed lines in this diff.

## Searches not found or unclear

none
