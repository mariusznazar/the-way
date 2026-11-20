# Author report — correction 2 (change of scope)

**Status:** done

## The remarks, as made, and how each was met

1. **A limit for the whole entry (600 words, all the paragraphs together, counted as a paragraph's words are).**
   - The check (`elements/common/foundation_check.py`): `check_length` adds the words of all the paragraphs of a decision's binding sentences (runs of characters between spaces, as for a paragraph); over `ENTRY_LIMIT = 600` it is an error naming the decision and the measure with its value (`` `ABC-03` is added or changed by this change: its binding sentences have 601 words in all (at most 600) ``) in a decision a change adds or whose paragraphs differ from those at the base (a different division included), and a `listed:` line in any other. A decision over both a limit of a paragraph and the whole gets one line for each. The description at the head of the script carries it.
   - WAY-05 carries the limit in its binding sentences (first and second paragraph), *Verification* names it in the `tests:` clause, *Rationale* gives its reason, *Rejected* gets both ways not chosen of the remark (no limit for the whole entry; a limit on the number of paragraphs).
   - The template gives it in the entry form, in "Binding sentences" and in the row "binding sentences" of the table of readers; `README.md` and `agent-instructions/README.md` name it in the same places as before.
2. **A paragraph for a part of the entry's own question.** WAY-05 now says the entry "may carry a further such paragraph for a part of its own question", each within the limits of a paragraph; its pair of examples gives a complying entry with a second paragraph for a part of its own question; *Rejected* gets both ways not chosen of the remark (keep the rule for another question's part only and divide anyway; rewrite or split every such entry). The template's "Binding sentences" says it, and the entry form too.

The entries over a limit today are not changed; the check lists them (WAY-344 now has two `listed:` lines, the 300-word one and the 600-word one). WAY-05 itself: paragraph 1, 3 sentences and 225 words; paragraph 2, 1 sentence and 72 words; 297 words in all (counted with the script's own functions); `python -B elements/common/foundation_check.py` reports no line for it.

## Commits (from the head `b0bba24d`)

1. `02bf399d` Give WAY-05 a limit of 600 words for all the binding sentences and a paragraph for a part of the entry's own question — the entry.
2. `63436978` Report binding sentences over 600 words in all their paragraphs — the check and six tests.
3. `fa5d349e` Give the limit of 600 words and the paragraph for a part of the entry's own question in the template and the descriptions of the check — the template, `README.md`, `agent-instructions/README.md`.

The worktree is clean. `foundation_check.py` stands at 1115 lines (limit 1200); no function reaches 110 lines (the size test passes).

## Entries written or changed (marks of the foundation step)

| Entry | Mark | Meaning in English | Znaczenie po polsku |
|---|---|---|---|
| WAY-05, the limit for the whole entry | `the cycle's` | The binding sentences of one decision, all their paragraphs together, have at most 600 words, and the check reports an excess as an error in a decision a change adds or alters, a different division included, and lists any other. | Zdania wiążące jednej decyzji, wszystkie akapity razem, mają najwyżej 600 słów, a sprawdzenie zgłasza przekroczenie jako błąd w decyzji dodanej lub zmienionej (także przy innym podziale na akapity), a w pozostałych tylko wypisuje. |
| WAY-05, a paragraph for a part of the entry's own question | `the cycle's` | An entry may carry a further paragraph for a part of its own question, within the limits of a paragraph. | Wpis może mieć dodatkowy akapit dla części własnego pytania, w granicach limitów akapitu. |

The two settlements come from the human's remarks on the request (correction 2), not from a row of *Settlements to record*, so each is marked `the cycle's`. No new pair of examples was added: the existing pair was brought to the two items. The wording of *Rationale* (one sentence on the whole limit and one on a part of the own question) is mine, from the "Why" of each remark. The *Rejected* variants are the four "Not chosen" of the remarks, each with its reason, with no count of entries (the remark's "about half of the entries" is left out as a count).

## WAY-19, WAY-05 and the template — what each says now, and what changed

- **WAY-05** now says: a paragraph for each part of *another* question the entry answers, and a further paragraph, allowed, for a part of the entry's *own* question; every paragraph within three sentences and 300 words, all together within 600.
- **WAY-19** (read whole, its *Rejected* too): its binding sentence says that "a part of the question an existing entry answers is a sentence of that entry where it cannot change without changing that entry". It states where such a part stands (in the entry, not under a number of its own) and says nothing of paragraphs or of how many sentences the part has, so it does not say the opposite of either item; I left WAY-19 unchanged. Its words, "the question an existing entry answers", name a rule that cannot change apart from the entry, which the template calls "a part of another question that the entry answers (WAY-19)" and which has a paragraph of its own; WAY-05's new permission for the entry's own question is a different case and is not WAY-19's. If the reviewer reads the "a sentence" of WAY-19 as exactly one sentence, that reading is a separate finding on WAY-19 (the review of correction 1 reported it outside the task); I did not widen the change to rewrite an approved decision's wording the remarks do not name.
- **The template, "Binding sentences"**, the first bullet: it now defines both cases in one place — "A part of another question that the entry answers, which cannot change without the entry (WAY-19), has its own paragraph after that one, one paragraph for each part. A part of the entry's own question, the question of its heading, may also have a paragraph of its own after the first." — and the total limit. The second bullet counts the limits of a paragraph and of all together.
- **The template, "Changing a decision"**, the bullet that cites WAY-19: it said a part of the question an existing entry answers stands "in a paragraph of its own ("Binding sentences")", which read as a rule for every part; it now reads "in a paragraph of its own as "Binding sentences" gives", pointing to the section that says when. This is the one place besides WAY-05 whose wording I changed to avoid a contradiction; name it in the request.
- No other entry or file says that a part of an entry's own question has no paragraph of its own: a search of the repository for "paragraph of its own", "own paragraph", "part of another question", "part of the question" and "paragraph for each" found WAY-05, WAY-19 (as above), the template, and no other text that holds the rule.

## Tests

Six new tests in `elements/common/test_foundation_check.py`, each with a line `decision:` quoting the start of a sentence of WAY-05 as it stands ("A decision entry opens with one to three binding sentences that answer its question" for the limits; "The check of the foundation reports as an error a paragraph of binding sentences" for the error and the list):
- 600 words in all pass (three paragraphs of two sentences, 200 words each);
- 601 words in all are an error that names the decision and "601 words" and no paragraph;
- a decision over both a limit of a paragraph and the whole is reported for each (two paragraphs of 4 sentences and 320 words, 640 in all: three errors);
- a change that lengthens a decision from 502 to 601 words is an error;
- a decision over 600 whose rationale alone changed is listed, exit 0;
- a different division of the same 601 words (three paragraphs to four, no word changed) is an error.

The names the tests break on: `>` to `>=` on the limit (the 600 test fails); counting the words of the longest paragraph and not of all (the 601 test fails); comparing the joined text and not the paragraphs for the change (the division test fails); an unlisted case where the base is unknown is held by the earlier test of the paragraph limits.

## Checks (command, exit code)

- Failing run, before the code: `cd elements/common && python -B -m unittest test_foundation_check -k binding_sentences_of_60 -k both_the_limit -k lengthens_past_600 -k over_600_words -k division_of_binding_sentences_over_600` — exit 1, `Ran 6 tests`, `FAILED (failures=5)` (the sixth, 600 words in all pass, passes before the code, since no check refuses it); each failure an assertion (an exit code 0 where 1 was expected, or the expected line missing); output kept in `reports/author-correction-2-red-run.txt`.
- First passing run: the same tests and the earlier tests of the limits, with `-k paragraph -k limit` added: exit 1, `Ran 15 tests`, `FAILED (failures=1)` — my own mistake in a test (the expected count of errors for a decision over both limits, "2 errors", where its two paragraphs and the whole make three, as the report showed). I corrected the expectation, written out by hand as three lines, and ran again: exit 0, `Ran 15 tests`, `OK`.
- `python -B gate/run_tests.py elements/common` — exit 0, 289 tests, OK.
- `python -B gate/run_tests.py elements/part-map` — exit 0, 40 tests, OK.
- `python -B gate/run_tests.py agent-instructions` — exit 0, 52 tests, OK.
- `python -B gate/run_tests.py product-guidelines` — exit 0, 14 tests, OK.
- `python -B gate/run_tests.py installation` — exit 0, 73 tests, OK.
- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`.
- `.runs/quality-venv/Scripts/ruff.exe check .` — exit 0; `ruff.exe format --check .` — exit 0.
- Not run: the full gate.

## Own-work check

The weakest point: that WAY-05 stays within all three limits and that the whole-entry limit counts as the remarks say. Check: counted WAY-05 with the script's own `binding` and `begins_sentence` (3/225, 1/72, 297 in all) and ran the check on the real foundation (no line for WAY-05, `0 errors`); the real foundation also shows that only WAY-344 stands over 600 words (two `listed:` lines for it, none an error, since this change does not alter it). The tests hold the boundary (600 passes, 601 fails), a division change over 600, the list for an unaltered entry, and both measures at once.

## Concerns

- The reflow of WAY-05 to 100 columns moved lines of text I did not change (the *Rationale* and the first part of *Rejected*); only the words listed above differ in meaning.
- WAY-19's "a sentence of that entry" and WAY-05's "paragraph of one to three binding sentences" still use different words for what an entry holds of a part; see the section on WAY-19 above. It is the matter the review of correction 1 reported as outside the scope; I did not change WAY-19.

## Unread material

- `guidelines/coding.md`, `guidelines/coding-check.md`, `guidelines/testing.md`, `elements/decisions/skill/SKILL.md`, `task-cycle/skill/foundation_step.md`, `task-cycle/change/SKILL.md`: read whole in the first turn, not re-read.
- `elements/common/foundation_text.py` and the rest of `test_foundation_check.py`: not re-read; only the sections I changed and the code they call were read.
- The selection of "Reading the foundation": run with `decision_index.py` (sections "Decision entries and the decision log", "The foundation and its entries", "Scripts and the gate", the parts `decisions`, `elements-common`, `agent-instructions`, `repository` and the decisions WAY-05, 12, 02, 19, 22, 385); the index was read for the first 120 lines (to WAY-16), and the entries opened whole were WAY-05, WAY-12 and WAY-19; WAY-02, WAY-22 and WAY-385 were read in the index form (binding sentences) and earlier turns. The invariants of the parts were not opened again.
- `.runs/task-cycles/decision-length-check/orch_index.md` was not re-read.

## Searches not found or unclear

- none

## Working copies

- `.runs/author-correction-2/` (the index of the selection, scratch counts and outputs): removed. The output of the failing run is kept in `reports/author-correction-2-red-run.txt`. `.runs/quality-venv/` stays as before. The file `.runs/fc_final.txt` was there when I started and is not mine; I left it.
