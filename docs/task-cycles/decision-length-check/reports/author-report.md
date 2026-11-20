# Author report — decision-length-check

**Status:** done with concerns (two points for the orchestrator, under "Concerns"; no question is open).

## Commits (branch `task/decision-length-check`, base `1b6fe1c1`)

1. `0f738707` Move the readers of an entry's text out of foundation_check.py into foundation_text.py — the first commit that changes code, a move with no change of behaviour (see Choices).
2. `58f9937d` Give WAY-05 a limit of 300 words and the error for a paragraph over a limit — the foundation entry.
3. `9dc811af` Report a paragraph of binding sentences over 3 sentences or 300 words — the check and its tests.
4. `e8b76178` Describe the check of the length of a decision in the template, the README and the guide to the-way's foundation.

The worktree is clean (`git status --short` empty).

## Files changed (added / removed lines, `git diff --numstat 1b6fe1c1 HEAD`)

| File | + | - |
|---|---|---|
| `elements/common/foundation_check.py` | 73 | 103 |
| `elements/common/foundation_text.py` (new) | 112 | 0 |
| `elements/common/test_foundation_check.py` | 158 | 0 |
| `elements/decisions/template.md` | 14 | 7 |
| `foundations/decisions.md` (WAY-05 only) | 40 | 17 |
| `README.md` | 5 | 4 |
| `agent-instructions/README.md` | 5 | 3 |

`foundation_check.py` stands at 1111 lines (limit 1200, WAY-385), `foundation_text.py` at 112; the size test passes.

## What was made

- `foundation_check.py`: `check_length` reports, for each unversioned decision, each paragraph of its binding sentences over 3 sentences or over 300 words. In a decision the change adds, or whose paragraphs (words or division into paragraphs) differ from those at the base, it is an error at the heading line, naming the decision, the paragraph and each exceeded measure with its value (`` `WAY-405` is added or changed by this change: paragraph 1 of its binding sentences has 5 sentences (at most 3) and 344 words (at most 300) ``); in any other decision it is a `listed:` line at the heading. Where the base is unknown nothing is added or changed, so all are listed. A sentence is counted by the existing `begins_sentence` (start of the paragraph, or after a full stop and a space outside a passage between quotation marks); a word is a run of characters between spaces. `base_sentences` (used by the check of what holds a decision, which keeps its joined-text comparison, as the task says) now wraps the new `base_paragraphs`. The description at the head of the script carries the new report.
- `elements/decisions/template.md`: the limit of 300 words in the entry form (two lines), in the first bullet of "Binding sentences", a new bullet after it (both limits counted by `foundation_check.py` in a decision a change adds or alters, so an older entry meets them when next altered; a sentence counted as the point on `decision:` in "Verification" gives its start), and the row "binding sentences" of "Fields and their readers".
- `agent-instructions/README.md` ("The form of the foundation") and `README.md` (the sentence opening "`elements/common/foundation_check.py` checks that every identifier stands once") name the new report and the new list.
- WAY-05 as the task's *Decisions in play* gives: (1) at most 300 words per paragraph, in the first sentence; (2) a second paragraph, as a part of another question, with the error for an added or altered decision (a different division included) and the list for any other; (3) *Verification* starts with a `tests:` clause and the pair "For whether a part of another question has a paragraph of its own" keeps only that part; (4) *Rejected* gains the ways not chosen of the two questions, the old "a higher fixed limit" now reading "a higher fixed limit of sentences"; (5) WAY-05 meets both limits: paragraph 1 has 3 sentences and 199 words, paragraph 2 has 1 sentence and 64 words (counted by the script).

## Foundation entries (foundation step)

| Entry | Marked | Meaning in English | Znaczenie po polsku |
|---|---|---|---|
| WAY-05, settlement row 1 | `row 1` | A paragraph of the binding sentences of a decision has at most three sentences and at most 300 words. | Akapit zdań wiążących decyzji ma najwyżej trzy zdania i najwyżej 300 słów. |
| WAY-05, settlement row 2 | `row 2` | The check of the foundation reports as an error a paragraph over a limit in a decision a change adds or whose binding sentences it alters, a different division into paragraphs included, and only lists any other decision over a limit. | Sprawdzenie fundamentu zgłasza jako błąd akapit ponad limit w decyzji, którą zmiana dodaje albo której zdania wiążące zmienia, także gdy zmienia tylko podział na akapity, a każdy inny wpis ponad limit tylko wypisuje. |
| WAY-05, one sentence of *Rationale* | `the cycle's` | "A limit in words beside the one in sentences keeps a paragraph short when its sentences are joined to stand under the count." | Limit w słowach obok limitu w zdaniach pilnuje, żeby akapit nie rósł, gdy zdania sklejono, by zmieścić się w liczbie. |

The sentence of *Rationale* is mine, drawn from the reason the task keeps under "Czym mierzyć długość" (not chosen: only sentences); the entry needs a reason for the word limit and no row gives it in so many words. The *Rejected* variants (six: sentences alone, words alone, 200 words, error only for a new or lengthened entry, lists and no error, a division counted as no change) are each from the *Not chosen* under the two questions, with the cost kept beside it; I dropped the counts the task quotes (30 and 45 paragraphs, "one in ten") because WAY-05 forbids a count in prose, and the 478-word measure because it goes false when the next task shortens WAY-134 (replaced by "three sentences can run to several hundred words"). No pair of examples was added; the pair was cut down (above). No *Relations* link was written.

The pair's part the test holds is already removed (the test of the same change holds it), so the return step has no pair to remove; what stays in the pair is whether a part of another question has its own paragraph, which no test holds.

## Choices (with the way rejected and the cost if wrong)

1. **Where the new check lives — the move of the readers of an entry's text into `elements/common/foundation_text.py`.** The file stood at 1141 lines; the addition (description at the head, constants, `excess`, `check_length`, the base reading, one call) came to about 65 lines, which would have landed at about 1206 over the 1200 of WAY-385. I made the first commit that changes the code a move, with no change of behaviour: `blocks`, `fields`, `located`, `binding`, `begins_sentence`, `table`, `items` and the patterns `FIELD`, `ITEM`, `QUOTED`, moved unchanged (the `begins_sentence` docstring unchanged). The module only defines functions and constants, reads no file and asks no git, as `foundation_source.py` does beside it. Rejected: (a) squeezing the addition into the 59 lines left — leaves no room for the next check and turns the description into a stub; (b) moving the file-and-part-map check (`check_files`, about 70 lines, a method that uses the state of `Foundation`) — it is less coherent as a part and would have touched a method that this change does not concern. Cost if wrong: a later reader looking for `binding` in `foundation_check.py` finds an import; the move is undone by moving the block back.
2. **Importers kept as they are.** `decision_index.py` imports `binding, blocks, fields, located` from `foundation_check`, and `test_cross_part_imports.py` imports `EMPTY, ENTRY, INVARIANTS, LEFT_OUT, PART_MAP, WORDS, blocks, fields, git, items, read, table` from it. All the moved names stay importable from `foundation_check`, which imports them and still uses each (the linter reports no unused import); no importer changed. The docstring of `foundation_check.py` says that `foundation_text.py` is imported through it. Rejected: changing the two importers to import from `foundation_text` — a wider change with nothing it gains for this task. Cost if wrong: another script that imports the names from `foundation_check` keeps depending on the re-export. **This enters the questions table of the record as a choice of the author, not a question for the human.**
3. **The error names the decision, the paragraph and the measure in one line per paragraph** (`paragraph N of its binding sentences has 4 sentences (at most 3) and 320 words (at most 300)`), one message for both measures of a paragraph; the listed line has the same body with a shorter lead. Rejected: one line per measure. Cost if wrong: a message wording only.
4. **Division into paragraphs and the base.** `check_length` compares the list of paragraphs with the base (each paragraph normalised as `binding` gives it), so a change of words, of division or of both is a change; a change of spacing alone is none. The check of what holds a decision keeps its comparison of the joined text.

## Checks (command, exit code)

All from the worktree root unless named.

- Failing run, before the code (the ten new tests that fail; the two others, a paragraph at the limits and a full stop inside quotation marks, passed because no check exists yet): `cd elements/common && python -B -m unittest test_foundation_check -k over_a_limit -k four_sentences -k 301_words -k both_measures -k counted_by_itself -k binding_sentences_a_change_alters -k different_division -k listed_decision_stands -k three_sentences_and_300 -k full_stop_inside_quotation_marks_ends_no_sentence` — exit 1, `Ran 12 tests`, `FAILED (failures=10)`; each failure an assertion (an exit code 0 where 1 was expected, or the expected line missing), no error on a missing name; output kept in `.runs/task-cycles/decision-length-check/reports/author-red-run.txt`. The whole directory then, `python -B gate/run_tests.py elements/common`, ran 283 tests and ended `FAILED (failures=10)` (its exit code was not captured, a pipe took it).
- Passing run, the same command after the code: exit 0, `Ran 12 tests`, `OK`.
- `python -B gate/run_tests.py elements/common` — exit 0, 283 tests, OK (after the move, 271 tests, exit 0 shown by the output `OK`; after the tests and code, 283, exit 0).
- `python -B gate/run_tests.py elements/part-map` — exit 0, 40 tests, OK.
- `python -B gate/run_tests.py agent-instructions` — exit 0, 52 tests, OK (the linter, the formatter and the size tests are among them).
- `python -B gate/run_tests.py product-guidelines` — exit 0, 14 tests, OK.
- `python -B gate/run_tests.py installation` — exit 0, 73 tests, OK.
- `python -B gate/run_tests.py elements/decisions` — exit 1, `no test found in elements/decisions`: the directory has no tests; not a failure of the change.
- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`, with twelve `listed:` lines for WAY-134, 136, 139, 148, 150, 154, 256, 287, 289, 339, 344 and 405, as the task counts them.
- `.runs/quality-venv/Scripts/ruff.exe check .` — exit 0, `All checks passed!`; `ruff.exe format --check .` — exit 0, `86 files already formatted`.
- Not run: the full gate (`python -B gate/run_tests.py` with no directory), as the handoff and WAY-160 give.

## Own-work check

The requirement most likely not met: that a decision a change *alters* — not only one it adds — turns an excess into an error, and an unchanged one only into a line, on the real repository and not only on the small products of the tests. The check: with the real foundation of the worktree, I added one word to the first paragraph of WAY-405 (an unaltered entry over the limits that stands as `listed:` today), ran `python -B elements/common/foundation_check.py`, and got exit 1 with `foundations/decisions.md:8853: \`WAY-405\` is added or changed by this change: paragraph 1 of its binding sentences has 5 sentences (at most 3) and 344 words (at most 300)` while the other eleven entries stayed as `listed:` lines; I then restored the file with `git checkout -- foundations/decisions.md` and the tree was clean. (The same run also reported four citations whose quotation the inserted word broke, which is expected from the edit and unrelated.) The tests also hold the boundary (3 sentences and exactly 300 words, whose words include hyphenated and comma-ended tokens, pass; 301 words fails), a full stop inside quotation marks, a division of paragraphs changing in both directions, spacing alone, the unknown base, and the order of errors and listed lines.

Mutations considered: `>` for `>=` on either limit (the boundary test fails); counting words by `\w+` (the hyphen tokens fail the boundary test); counting every `. ` (the quotation test fails); comparing the joined text instead of the list (the test of a different division fails); treating an unknown base as known (the unknown-base test fails). Not protected by a test: the single wording of the message, which the requirement does not fix (the tests hold the decision, the paragraph number and the measure with its value).

Each test of the new check carries a line `decision:` with the start of a sentence of WAY-05 as the entry now stands: "A decision entry opens with one to three binding sentences that answer its question" for the limits, and "The check of the foundation reports as an error a paragraph of binding sentences" for the error/list behaviour; the script accepts both (`0 errors`).

## Walkthrough

The change alters no behaviour a user sees in a running product: it changes a check run from a terminal and its report, a decision of the foundation, and prose; the check's own report was run on the real foundation (above).

## Concerns

- A value of the task that does not pass my reckoning: none; the count "WAY-256 has 301 words" and the twelve entries all matched the script's output.
- The step 4.4 of the skill of decisions (an edit of a neighbour found in step 2): I found no entry that names WAY-05's limit as "one to three sentences" and now disagrees. Three texts say "one to three binding sentences (WAY-05)" — `product-guidelines/styleguide/template.md:168`, `product-guidelines/testing/template.md:196`, and a decision at `foundations/decisions.md` (a line reading "a decision holds one to three binding sentences and no table") — and stay true; none of them states the word limit. Say so in the request if the reviewer wants them changed.

## Reach beyond the dispatch

- `elements/part-map/test_cross_part_imports.py` lines 55–95 (the import list), `agent-instructions/test_size_invariant.py` whole, `elements/common/rules.md` and `elements/common/way_of_working.md` whole, `elements/decisions/skill/read.md` and `decide_entry.md` whole (named by the `SKILL.md`), and `guidelines/coding-shared-module.md` whole (named by the handoff for a split): read because the move and the foundation step needed them.
- `installation/install.py` lines 198–218 and excerpts of `installation/README.md`: a search for places where the description of the check stands; neither needed a change.
- A search of the whole repository for `WAY-05`, "binding sentences", "one to three", "three sentences" and "foundation_check" (the search of the foundation, WAY-33); the hits are above.
- `.runs/quality-venv` created as `README.md` gives, for the linter and the formatter.

## Working copies

- `.runs/author/` (my scripts and outputs): removed; the output of the failing run is kept in `reports/author-red-run.txt`.
- `.runs/quality-venv/` (the environment of Ruff, installed from `requirements-quality.txt` as `README.md` gives): left in place on purpose — the tests of the linter and the formatter in `agent-instructions` use it, so the orchestrator's or CI's gate needs it; it is under the ignored `.runs/` and is no tracked file.

## Unread material

- `foundations/decisions.md`: WAY-05 read whole with its *Rejected*; WAY-12 read from its heading to the first lines of its *Verification* (not its *Rationale* or *Rejected*), WAY-02, WAY-22 and WAY-385 by their binding sentences through `orch_index.md` and the task's quotation only — none of them changed.
- The selection of "Reading the foundation" for the parts I touched (the index of decisions and the invariants of `decisions`, `elements-common`, `agent-instructions`, `repository` by the part map) was not run: I read what the handoff names and made the search of step 2 by text (`WAY-05`, `binding sentences`, `foundation_check`, `one to three`) over the repository instead. No invariant of those parts was opened apart from what the tests that cite them exercise (`function-and-file-size`, the invariants of the formatter and linter, `own-foundation-check-report`: all pass).
- `elements/common/decision_index.py`: only its import line was read (it imports `binding, blocks, fields, located` from `foundation_check`); `elements/common/test_foundation_check.py` read in part (its head, the sections on `decision:` lines, the base, and what held a decision, and its tail), not whole.
- `elements/decisions/skill/projected.md`, `elements/common/projected_mode.md` and `missing_element_file.md`: not read (projected mode and a product without the file do not apply).

## Searches not found or unclear

- The task names "ok. linii 132–134" and "ok. linii 29–32" of the template: found (lines 130–134 and 29–32 at the base), no difference of substance.
- `elements/decisions/SKILL.md`, named in the handoff by that path, does not exist; the file is `elements/decisions/skill/SKILL.md` (found by the directory listing).

## Problems observed

- `python -B gate/run_tests.py elements/decisions` exits 1 with `no test found in elements/decisions`: the directory has no test, and the handoff lists it among the directories to run. Observed, not caused by this change.
