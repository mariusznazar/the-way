Author report — the fix of the review's findings, round 1 (`make-change`, "the fix of a review's findings").

**Status:** done. All five findings (I1–I4, M1) fixed; none contested.

Range: from the reviewed head `ae37fca3310ce6efe7e7939413b8b7a1205b0ead`; commits `96f87086`, `b3ffef2b`, `041d11f5`, `d1b8f520`, `41921006`.

## I1 — the orchestrator's duties of the tests a plan leaves failing (no contradiction)

Changed (commit `041d11f5`):
- `task-cycle/skill/planning.md`, "A slice's handoff": a new paragraph — the handoff of each later slice also lists the tests the plan leaves failing at its base, with their owners, as the *Goal* of each earlier slice names them, so that its executor reports a listed test that fails as expected; where a report names a failing test no *Goal* names, give it an owner by editing the plan before the next slice is dispatched.
- `task-cycle/skill/SKILL.md`, step 9: sub-step 2 adds the listed tests to what the handoff carries; sub-step 3 sends a failing test that no *Goal* names to `planning.md` (the duty stands once, there, WAY-256); sub-step 4 reads "reports a failing check of its slice — a listed test that fails as the plan says is none (WAY-136)".
- The quoted sentences in `task-cycle/plan/SKILL.md` and WAY-136 are untouched. No decision needed a new word; the sentences stay within WAY-136 (a failure so named is no failing check) and WAY-229 (the retry is for "a failing check of its slice").

Check: `python -B gate/run_tests.py task-cycle` exit 0, `... agent-instructions` exit 0, `... product-guidelines` exit 0. A search of `task-cycle/skill/` for `failing at its base|tests the plan` now finds the three places.

## I2 — `decision_index.py` reads the withdrawn list by column names (contradiction, WAY-344)

Changed (commit `96f87086`): `withdrawn_numbers` reads the table by the names `Identifier`, `Why`, `Successors` of its header, wherever the columns stand; a missing or renamed column, a row with no cell or an empty cell in `Why` or `Successors`, ends the script with exit code 2 and `Error: foundations/decisions.md: ...` naming the field (and the identifier of the row). The neighbouring reads of the same change had the same fault: `chain` took a successor that is neither a decision nor a withdrawn identifier nor `none` as "no successor"; it now ends the script with exit code 2 naming the successor and the withdrawn identifier. The list is read only where `--decision` is given (the other switches need no field of it). The docstring's exit-code paragraph names the new cases.

Tests (`elements/common/test_decision_index.py`, six new): the table without `Successors` (with the line `decision: WAY-344 "Each reading of a file that the rule covers has one test"`), a column under another name (`Reason`, `Replaced by`; line `decision: WAY-344 "A script of the-way that reads a file an agent or a human writes checks"`), a row without a cell and with an empty cell in each needed column, a successor the log does not hold, the columns found whatever their order, and the list unread by `--section`.

Checks: failing before the code — the new tests run against the head's script: `cd elements/common && python -B -m unittest test_decision_index` exit 1 (5 failures); after: exit 0 (31 tests). Every withdrawn number of the real log run through `--decision` still ends with exit code 0 (179 runs, 0 failures). `python -B gate/run_tests.py elements/common` exit 0.

## I3 — text in quotation marks is no path (no contradiction)

Changed (commit `b3ffef2b`, `instruction-files/check_instructions.py`, docstring, tests). The rule: a token is no path where it holds a typographic quotation mark anywhere (`“ ” „ ‚ ‘ ’ « »`), or begins or ends with an ASCII apostrophe (so the shell idiom `'\''` and `'text'` go out), besides the ASCII `"` that the first round took. An apostrophe inside a name (`O'Brien/notes.md`) leaves it a path. Price: a real file name that holds a typographic mark or begins or ends with an apostrophe is not looked up any more (rare; none known on this disk); a name with an apostrophe inside stays looked up. `instruction-files/SKILL.md` names no such characters, so it needed no change.

Tests: `test_text_in_apostrophes_or_in_typographic_quotation_marks_is_no_path` (the shell idiom, five typographic forms, an apostrophe at either end) and `test_an_apostrophe_inside_a_name_leaves_it_a_path` (warn where missing, sound where it exists). Failing before: the first one run against the head's script: exit 1; after: `cd instruction-files && python -B -m unittest test_check_instructions` exit 0 (122 tests, 5 skipped as before).

Crafted input again at this trust-boundary file: the change only widens what is taken out of the lookup, by text rules; no new read of a file and no new lookup; the existing tests of network paths, links and non-regular files pass (`python -B gate/run_tests.py instruction-files` exit 0). Result on loop2 (read only): warnings 22 at the end of round 0, 15 now — the 15 real ones the task lists as out of scope, none with a quotation mark; `python -B instruction-files/check_instructions.py .` on the-way: 0 warn.

## I4 — the walk (contradiction, WAY-406)

Read `task-cycle/change/walkthrough.md` whole. The section "Walkthrough" of `reports/author-report.md` is replaced in place: the judgment (the change alters what five commands print and how they end), the finding that the foundation settles no way to the-way as a running product, so the walk is not performed, the account of what the change alters in the user's words, what I did not check, and the plan of eight cases plus the side-observation row, each marked unchecked with that reason. The rest of that report stands; its "Unread material" line on `walkthrough.md` is corrected. No commit (the report is not tracked).

## M1 — `task-cycle/review/whole_change.md` (Minor, within the task)

Changed (commit `d1b8f520`, `41921006`): the sentence now tells the reviewer to run the check of the product's instruction files itself on the head, in the reviewed worktree (the script changes nothing), with the command `installation/README.md` gives for it, in a product `.the-way/installation/README.md` with the script's path starting with `.the-way/`. I did not write the script's own path (`instruction-files/check_instructions.py`) into the sentence: the part map gives `task-cycle` no dependency on `instruction-files`, and the README (a part `task-cycle` depends on) gives the command. If the review wants the path itself in `task-cycle/review/whole_change.md`, the map needs the dependency first.

## Checks run in this round

| Check | Command | Exit |
|---|---|---|
| I2 tests, before the code | `cd elements/common && python -B -m unittest test_decision_index` (head's script) | 1 |
| I2 tests, after | the same | 0 |
| I3 test, before the code | `cd instruction-files && python -B -m unittest test_check_instructions.TextThatIsNoPath` (head's script) | 1 |
| directories after all commits | `python -B gate/run_tests.py instruction-files` · `elements/common` · `agent-instructions` · `product-guidelines` · `task-cycle` | 0 each |
| foundation check on the finished change, no switch | `python -B elements/common/foundation_check.py` | 0 (`0 errors`) |
| instruction check on the-way | `python -B instruction-files/check_instructions.py .` | 0 (0 warn) |
| ruff 0.17.1 format and lint of `elements instruction-files task-cycle gate` | `.runs/author-fix-1/venv/Scripts/ruff format --check ...` and `ruff check ...` | 0 |

No new file was created by this fix, so no run was needed after a `git add` of a new file. The gate with no argument was not run.

## Unread material

none beyond round 0's list: this round I read the handoff, the findings file, `task-cycle/change/fix.md`, `task-cycle/change/walkthrough.md` and `task-cycle/skill/planning.md` whole, WAY-344 whole, and did not open the reviewer's probe directories (the findings carried what I needed).

## Searches not found or unclear

- WAY-406's third paragraph says the description of the request states the reason the walk was not performed; the foundation search for a way to the running product of the-way itself (I looked for a decision or skill that settles logs, interface, development data or screenshot place for the-way) found none, which I took as "settles no way" as the reviewer did.
- Whether a successor token in the withdrawn list should be matched case-insensitively (`None`): the log writes `none` only; I match `none` exactly.

## Working copies

`.runs/author-fix-1/` stood with a virtual environment `venv/` (ruff 0.17.1), a copy of my own script (`di_new.py`), temporary outputs and the outputs of the directory runs; removed with the directory by its full path before I returned; no remainder. No git worktree or clone was made.
