# Report of the fix of the review of the whole change — task `small-fixes-after-prs-117-121`

**Status:** done. Reviewed head `e9aea95`; fix range `e9aea95..eaf815c`.

## Commits

| Commit | What |
|---|---|
| `b23275b` | I1 (code, docstring, template, test), m6 (test) |
| `eaf815c` | m1, m2, m3 (`foundations/decisions.md`, `task-cycle/skill/SKILL.md`), m4, m5 (`task-cycle/plan/SKILL.md`), m7 (`agent-instructions/README.md`, `elements/invariants/template.md`), m8 (`project-level/task/skill/resolve_gaps.md`) |

I2 changes no commit (see the corrected table). `o1` was not touched.

## Findings

**I1 — fixed.** `QUOTED` in `elements/common/foundation_check.py` is now `"…"`, `[“„]…”` (opening U+201C or U+201E, closing U+201D). The docstring of the script and the point of `elements/decisions/template.md` name the three pairs. The test `test_a_full_stop_inside_a_quoted_string_ends_no_sentence` loops over a third pair. Failing run before the code: `python -B -m unittest discover -s elements/common -p test_foundation_check.py -k full_stop` — exit 1 (`FAILED (failures=1)`), `0 != 1`: the check passed a quotation that begins inside a `„…”` string. After: exit 0. Side effect named: `QUOTED` is shared, so `todo_item` and `unquoted` now also mask `„…”` text (a ` · ` or a `TODO` inside `„…”` joins or begins nothing, as for `“…”`); the whole `elements/common` run passes.

**I2 — corrected table below** (no commit).

**m1 — fixed.** WAY-60 *Verification*: the first example is restored as it stood; the added one is "an invariant of the-way whose sentence reads "as WAY-309 names them", the condition standing in that decision of its own log, has WAY-309 also in its *Derives from*, the link WAY-17 requires". It follows the task's own case and carries no the-way/product tension.

**m2 — fixed.** WAY-229's binding sentence: "(in Claude Code the setting `availableModels`; where the session has no such list, every model it offers)"; the two steps of `task-cycle/skill/SKILL.md` say "from the list `availableModels` in Claude Code or, with no such list, every model the session offers".

**m3 — fixed.** WAY-229's rationale: "A request for a model outside that list got another model, in the one session observed the session's own"; the *Rejected* item: "a request for it got another model".

**m4, m5 — fixed.** The plan sentence: the check is `elements/common/foundation_check.py` (in a product `.the-way/elements/common/foundation_check.py`), run with the switch "as the run right after the entry is written that WAY-321 exempts".

**m6 — fixed.** New test `test_reworded_invariant_lacking_a_field_at_base_is_listed_though_its_citing_file_changed` (touches `tests/test_saving.py`, expects one listed line naming *Method*). Mutation seen failing: I made the listing conditional on no file under `tests/` having changed; the run `-k lacking` gave exit 1 (`0 != 1 : []`); the code was restored from a copy and the run gave exit 0.

**m7 — fixed.** README: "…whose sentence a change rewords while no file citing them changes, both against the commit the branch left the main branch from; where such an invariant's copy at that commit lacks *Method* or *Part*, it lists it naming the field." Template row: "and, naming the field, one of them whose copy at the base lacks *Method* or *Part* (WAY-344)".

**m8 — fixed.** The list of the three items again ends "(WAY-139):" and the bullets follow; the pointer sentence stands after the list as its own paragraph ("names the guide as the item of the first paragraph of this check does").

## Corrected table "Entries written" (I2)

The three entries are marked `the cycle's`; the row each carries stays beside the mark. The pairs are the clauses added to each entry's existing pair, word for word, as the files stand at `eaf815c`.

| Entry | Mark | English | Polish | Added examples |
|---|---|---|---|---|
| WAY-139 | `the cycle's` (its settlement is row 1; the pair of examples is not the row's) | Each item of the To do that writes into the skill the answer to how to read the logs, how long the record lives or how a human learns of a failure, or the record of the human's refusal, points to the guide too. | Każdy punkt *To do*, który wpisuje do skilla odpowiedź o czytaniu logów, o czasie życia zapisu albo o awarii (albo zapis odmowy człowieka), też wskazuje przewodnik. | *complies* (added clause): "the item that writes into the skill the answer a decision gives for how a human learns of a failure, or the record of the human's refusal to settle it, points to the guide as well"; *violates* (added clause): "an item that writes into the skill the answer for how to read the logs, how long the record lives or how a human learns of a failure names no guide" |
| WAY-344 | `the cycle's` (its settlement is row 3; the pair is not the row's) | A field missing from the copy of a file at the commit the branch left is listed by a `listed:` line naming the entry and the field, with no error and no change of the exit code. | Brak pola w kopii pliku z commita bazowego jest wypisany linią `listed:` z nazwą wpisu i pola, bez błędu i bez zmiany kodu wyjścia. | *complies* (added clause): "the same script, reading a copy of the file at the commit the branch left, lists an absent section of that copy on a line `listed:` and keeps its exit code"; *violates* (added clause): "a script that checks the form of a file ends with an error at a field missing from the copy at the commit the branch left, or passes over it without a word" |
| WAY-60 | `the cycle's` (its settlement is row 5; the pair is not the row's) | A decision identifier written into an invariant's sentence because the decision holds the condition is part of the condition, not a link WAY-17 requires; the link stands beside the sentence in its own field. | Identyfikator decyzji wpisany w zdanie niezmiennika, bo ta decyzja trzyma jego warunek, jest częścią warunku, a nie powiązaniem z WAY-17; powiązanie stoi obok zdania w swoim polu. | *complies* (added clause, changed by m1): "an invariant of the-way whose sentence reads "as WAY-309 names them", the condition standing in that decision of its own log, has WAY-309 also in its *Derives from*, the link WAY-17 requires"; *violates* (added clause): "an invariant whose entry has the link WAY-17 requires only as the identifier in its sentence, with no field of its own for it" |

Marks of the other entries stay as in `author-report.md`: WAY-61 *Scope*, WAY-229 and the rationale of WAY-160 `the cycle's`; their *Verification* changes (WAY-229's two clauses on the source of the strongest model; WAY-160 has none) are additions to existing examples of WAY-229, not a new pair. WAY-229's complies clause now reads "…the orchestrator taking it from the models the session's settings allow" and its violates clause "a review is asked for on the strongest model of the family while the session's settings keep that model out", the second added by `52b122b` — the orchestrator may show both with the entry. WAY-139's *Verification* also changed in the cycle's first commit by the pair above only.

## Checks (worktree root)

| Command | Exit | Result |
|---|---|---|
| `python -B -m unittest discover -s elements/common -p test_foundation_check.py -k full_stop` before the code | 1 | FAILED (failures=1), `0 != 1` |
| the same after | 0 | 1 test OK |
| `… -k lacking` with the mutation of m6 | 1 | FAILED (failures=1), `0 != 1 : []` |
| `… -k lacking` after restoring | 0 | 10 tests OK |
| `python -B gate/run_tests.py elements/common` | 0 | 246 tests OK |
| `python -B gate/run_tests.py task-cycle` | 0 | 534 OK (skipped=1) |
| `python -B gate/run_tests.py project-level` | 0 | 279 OK |
| `python -B gate/run_tests.py agent-instructions` | 0 | 37 OK (expected failures=2, as on the base) |
| `python -B gate/run_tests.py product-guidelines` | 0 | 14 OK |
| `python -B gate/run_tests.py elements/part-map` | 0 | 40 OK |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |

Not run: the full gate (the orchestrator's).

## Own-work check

Requirement most likely not met: I1's case, the quotation of loop2 — `„…”` with a full stop and a space inside. The test gives that form to the same function the check uses; the third pair fails before the code and passes after. Mutation in the head: a quotation whose opening is U+201E but whose closing is not U+201D is not matched (same as the existing `“` form); not tested, as the earlier pair was not.

## Reaches beyond the handoff

None beyond the findings file and the handoff; I read `foundations/decisions.md` at the entries I changed and `task-cycle/plan/SKILL.md` lines 168–182 and 200–212 for m5.

## Unread material

The reviewer's full report `review-whole-report.md` — not read; the findings file carried the places and evidence, and I checked each finding against the files.

## Searches not found or unclear

None.

## Working copies

`.runs/author/` held throw-away scripts and one saved copy of `foundation_check.py` for the mutation; all removed (`find .runs/author -mindepth 1 -delete`). Remainder: none.
