# Author report — ai-review-fixes-from-24-11

**Status:** done

**Commit:** `225bf1c5` on `task/ai-review-fixes-from-24-11` (base `07aa55df`), one commit for the whole change.

## Files changed (commit `225bf1c5`: 10 files, +282 −23)

| File | + / − | What |
|---|---|---|
| `task-cycle/skill/request_template.md` | +4 −1 | item 1: the two sentences end item 6, after "(*Description*)." (Question 4), wording as accepted, re-wrapped |
| `elements/invariants/skill/write.md` | +3 −2 | item 2: step 4.4 as given |
| `elements/invariants/skill/decide_entry.md` | +3 −3 | item 5: the sentence as given, rest unchanged |
| `elements/common/foundation_check.py` | +78 | item 3: `entry_texts`, `Foundation.check_linked`, the call in `run`, the docstring bullet; 1115 → 1193 lines (limit 1200) |
| `elements/common/test_foundation_check.py` | +129 | item 3: tests of both cases and of the edges (below) |
| `foundations/decisions.md` | +54 −12 (approx.) | WAY-12 and WAY-30 (new paragraph, *Verification*, *Rationale*, *Rejected* each); *Verification* of WAY-48, WAY-235, WAY-368 (item 4) |
| `elements/decisions/template.md` | +1 −1 | the *Verification* row of "who reads it" now says what the script reports for an unnamed invariant |
| `elements/invariants/template.md` | +1 −1 | the *Derives from* row, the same |
| `agent-instructions/README.md` | +3 −1 | "The form of the foundation": the new error and listed line |
| `README.md` | +5 −3 | the paragraph on what `foundation_check.py` reports: same (reach, see below) |

## The rule of item 3, as made

`check_linked` runs after `check_held`. For each unversioned invariant not of the earlier form it reads the decision numbers of *Derives from* the way `check_foundation_references` does (`known_part` then `unquoted`: a `TODO` tail is cut, a number inside a quoted source is no link). For each such decision of the log that has a *Verification*, it takes the identifiers after `invariants:` (`VERIFIED`, `@fingerprint` suffix dropped) and, where the invariant is not among them, reports at the first line of that decision's *Verification*:

- error where the whole entry of the invariant, or of the decision (heading, fields, sentence, rationale, rejected, every run of spaces and line breaks made one space), differs from the base commit's or is absent from it: `` `X` derives from `D`, whose *Verification* does not name it, and this change adds or alters one of the two entries: add `X` to the *Verification* of `D`, after `invariants:` ``;
- otherwise a `listed:` line with the same message without the middle clause. A file whose base is unknown counts as unchanged (the same convention as `check_held`: "Where the base is unknown no decision is added or changed"), so a gap there is listed.
- A reference to a decision the log does not hold, a decision with no *Verification* and an entry of the earlier form are left to the reports that already exist.

## Foundation entries (foundation step)

Written by following `elements/decisions/skill/SKILL.md` (with `read.md`, `decide_entry.md`; WAY-33 search made, see below). Each marked as the step gives.

1. **WAY-30**, new third paragraph — `row 1`.
   - English: a change to a decision's *Verification* that adds, removes or renames the identifier of a derived invariant, and alters none of its binding sentences, needs no approval before the code; the human accepts it at the merge with the request's list of entries (WAY-114) and the agent asks no question.
   - Polish: dopisanie, usunięcie albo zmiana nazwy niezmiennika w *Verification* decyzji, bez zmiany jej zdań wiążących, nie wymaga zgody przed kodem — człowiek przyjmuje to przy scaleniu, razem z listą wpisów prośby, a agent nie pyta.
   - Also edited in WAY-30: *Verification* (one more complies example and two violates examples for the new paragraph; these are the pair for this paragraph, the writer's addition, see Concerns), *Rationale* (one sentence), *Rejected* (two options, the second is the task's "not chosen" of Question 1).
2. **WAY-12**, new third paragraph — `row 2`.
   - English: the check of the foundation reports as an error an invariant whose *Derives from* names a decision that does not name it in *Verification*, where a change adds or alters either entry as a whole, with the identifier and the decision in the message; any other such invariant is only listed.
   - Polish: sprawdzenie fundamentu zgłasza jako błąd niezmiennik, którego *Derives from* wymienia decyzję, a jej *Verification* go nie wymienia, gdy zmiana dodaje albo zmienia któryś z tych dwóch wpisów w całości, i podaje w błędzie, który identyfikator dopisać do której decyzji; każdą inną taką lukę tylko wypisuje.
   - Also edited in WAY-12: the `tests:` clause of *Verification* (the new error and list), *Rationale* (the link written at both ends), *Rejected* (three options; two are the task's "not chosen" of Question 2). The decision is held by tests; tests carry `decision: WAY-12 "The check of the foundation reports as an error an invariant whose"` and `... "Any other such invariant stands in the list the check prints"`, both checked by the script. Its pair of examples is not extended.
3. **WAY-48**, **WAY-235** (the seven invariants) and **WAY-368** (`installation-paths-through-links`): *Verification* only, `invariants: … . For the rest, an agent compares … :` before the existing pair — `the cycle's` (item 4 of *To do*, no row carries it). English: each of these decisions names the refusal invariants derived from it. Polish: każda z tych decyzji wymienia niezmienniki odmowy, które z niej wynikają. No binding sentence of the three changed.

WAY-18 and WAY-114 are read and unchanged: WAY-18's "one exception … a decision's invariants" already states the link at both ends.

## Own-work check (section 3)

- Requirement most likely unmet: the acceptance criterion and item 3's "either entry as a whole, anywhere in the entry", which the code can fail by reading only a field.
- Checks: `python -B elements/common/foundation_check.py` (no switch) → `0 errors`, exit 0, and no `listed:` line. Before the entries were written, the same command with the new check listed exactly the 15 links of item 4 and no other (7 for WAY-48, 7 for WAY-235, 1 for WAY-368) — none found beyond the task.
- Tests of the whole entry: a change to the decision's rationale only, and to the invariant's *Part* only, each turn an old gap into an error; a spacing-only change keeps it a listed line.

## Tests written (`elements/common/test_foundation_check.py`, section "an invariant whose decision does not name it")

Break each catches: the check not running or ignoring a side of the change. Each expected message is written out; the line numbers are those of the small log (ABC-01 *Verification* at 10, ABC-02 at 23).

1. new invariant, decision does not name it → error with the add line, `1 error`;
2. new invariant named by the decision in the same change → `0 errors`;
3. old gap, decision's rationale altered → error;
4. old gap, invariant's *Part* altered → error;
5. old gap, untouched → one `listed:` line, `0 errors`;
6. old gap, invariant altered in spacing only → still listed;
7. base unknown (no commit) → listed;
8. *Derives from* of two decisions, neither names it → two errors, one line for each decision;
9. a decision number inside a quoted source is no link → `0 errors`;
10. a decision with no *Verification* is left to the fields check → one error, no new message.

Seen failing: with the call `foundation.check_linked()` replaced by `pass` in `run`, the command `python -B -m unittest -v -k … elements.common.test_foundation_check` (the tests above) ran 19 tests, `FAILED (failures=7)` — the seven tests that expect the error or the listed line (1, 3, 4, 5, 6, 7, 8); tests 2, 9, 10 pass with or without it by design (they hold what the check must not report). The call was restored; the first run of the same selection with the call in place passed (`Ran 19 tests … OK`), and the full run of the directory below passed after the restore. Mutation in the head: counting a number inside quotation marks would fail test 9; reading only *Derives from* and *Verification* for "changed" would fail tests 3 and 4; dropping whitespace normalisation would fail 6.

The note of the review about `test_foundation_check.py` ("many examples of an invariant with *Derives from* and no link back"): verified, not assumed. The whole file ran green with the new check and no example was completed: the good product's invariants are all named by their decisions, and the tests that add invariants only assert on exit code and parts of the report.

## Checks run (command, exit code)

- `python -B elements/common/foundation_check.py` → `0 errors`, exit 0 (no `--skip-test-citations`).
- `python -B gate/run_tests.py elements/common` → 314 tests OK, exit 0 (before the last edit to the root `README.md`, a file no test of that directory reads).
- `python -B gate/run_tests.py agent-instructions` → 53 OK, exit 0 (the size and formatter invariants; `foundation_check.py` stands at 1193 lines of 1200); run again after the last edit, exit 0.
- `python -B gate/run_tests.py task-cycle` → 570 tests OK (2 skipped on Windows), exit 0 (`request_template.md` is read there).
- `python -B gate/run_tests.py product-guidelines` → 14 OK, exit 0. `python -B gate/run_tests.py instruction-files` → 122 OK (5 skipped), exit 0, also after the last edit. `python -B gate/run_tests.py project-level` → 302 OK, exit 0.
- Linter and formatter, with the pinned Ruff of the main checkout's `.runs/quality-venv`: `ruff format --check --config ruff.toml elements/common` → 13 files already formatted; `ruff check --config ruff.toml --ignore-noqa elements/common` → all checks passed, exit 0.
- The full gate was not run (the orchestrator's or CI's).

## Choices made (the task and the foundation settle none that is open)

- The error line stands at the first line of the decision's *Verification* (not at the invariant's heading), since that is where the fix is written; rejected: the invariant's heading, which would point away from the edit. Cost if wrong: the line number in the message only.
- "Changed" is decided on the whole entry with its heading, whitespace-normalised, per file against the base; a file whose base is unknown counts as unchanged for it (the convention of `check_held`). Rejected: treating an unknown base as changed, which would turn old gaps into errors on every run without a git history.
- Item 2 and item 5 sentences are exactly the task's; item 1 is the accepted text, re-wrapped to the file's width.
- No move of code out first (WAY-365): the file stands under its threshold (1115 before, 1193 after).
- The new code reuses `known_part` and `unquoted` of the references check, so the reading of *Derives from* is the same as theirs.
- The kind file read: `guidelines/coding-check.md` (`foundation_check.py` is a check; its rules read `none — WAY-386`, and it lists the script as `copy`); `coding.md` and `testing.md` whole.

## Reach beyond the handoff

- Root `README.md` (lines 83–93, the paragraph on what `foundation_check.py` reports): found by a search for "nothing holds" (WAY-33 search for what the change touches); it described the reports and had to include the new one. Edited.
- `elements/decisions/skill/read.md`, `decide_entry.md` and `elements/invariants/skill/SKILL.md` — read by following the `record-decision` skill and for the surroundings of step 4.4.
- Searches for "level 1", "4.4", "reports an invariant" across the repository to find other text that says what the check reports or the dead vocabulary; none other found.
- Ruff: the-way worktree has no `.runs/quality-venv`; I used `the pinned Ruff of the main checkout's quality virtual environment` of the main checkout, the one the linter test names.

## Concerns / for the human at the merge

- The pairs of examples I added to WAY-30's *Verification* (one complies, two violates, the text in the commit) are the writer's addition not given by row 1; by the foundation step they make WAY-30's edit partly `the cycle's` and the request should show them word for word. They are kept as the only check of that paragraph (no test can hold it).
- WAY-12's *Rationale* and *Rejected* additions and WAY-30's are my wording around the meaning of rows 1 and 2; the meaning is the rows'.

## Unread material

Read in part or not at all (the rest of the reading list was read): the frozen task whole, `task-cycle/change/SKILL.md` and `foundation_step.md`, `elements/decisions/skill/SKILL.md` with `read.md` and `decide_entry.md`, WAY-05, 12, 18, 30, 48, 114, 235, 368 whole; WAY-14, 33, 150, 02, 379, 382, 385 and the invariants named were not read whole as entries (WAY-385's limit is quoted in the handoff; the invariants' *Derives from* were read for the seven; the size test passes). Not read: the part map's entries for `elements-common`, `invariants`, `decisions`, `task-cycle`, the glossary and the invariants whose *Part* is `elements-common` or `every` (the change touches no file or claim of the map, and the foundation check reports no file left unclaimed), `elements/common/rules.md` and `way_of_working.md` beyond a search.

## Searches not found or unclear

- None unfound. Unclear: WAY-385 and WAY-379 "counted as the formatter leaves it": I counted the physical lines of the file after `ruff format` (1193), and the size test of `agent-instructions` passes with it.

## Working copies

None made. The directory `.runs/author/` held the output files of the test runs; it was removed.
