# Author report — fix of the findings of the review of correction 2

**Status:** done

## Commit (range from the reviewed head `fa5d349e`)

One commit: Say the same in WAY-05 and the template of a paragraph for a part of the entry's own question (files `foundations/decisions.md`, `elements/decisions/template.md`). The worktree is clean.

## Finding 1 (blocking) — fixed, not contested

The finding is right: WAY-05 said "a further such paragraph for a part of its own question" (one), the template's "Binding sentences" said any part may have a paragraph (several), and the entry form gave a part of the heading's question the rule of another question's part ("one paragraph for each such part", no "may"). Item 2 of the remarks says "each such paragraph", so several, and item 1 left the number of paragraphs unlimited. The three places now say one thing:

- **WAY-05**: "…and may carry a further such paragraph for each part of its own question that it sets apart, no paragraph of binding sentences running past 300 words and the binding sentences of one decision together not running past 600, …" (the paragraph is reflowed to 100 columns; no other word changed).
- **Template, "Binding sentences"**: "Each part of the entry's own question, the question of its heading, that the entry sets apart may also have a paragraph of its own after the first. Each such paragraph has one to three sentences and at most 300 words, no limit stands on the number of paragraphs, and the binding sentences of one decision, all their paragraphs together, have at most 600 words (WAY-05)."
- **Template, the entry form**: the block for another question's parts is as it was before correction 2 (`<1–3 binding sentences, at most 300 words, for a part of another question this entry answers, one paragraph for each such part; none where there is no such part>`), and a block of its own keeps "may" for the other kind: `<optionally 1–3 binding sentences, at most 300 words, for a part of the question of the heading that the entry sets apart, one paragraph for each such part; all the binding sentences together at most 600 words>`.

None of the three limits the number of paragraphs; the 600 words of the whole keep the length. I restored none of the ways not chosen and changed neither WAY-19 nor the two Minor findings of the review (they go to the request's list, as the handoff gives).

WAY-05 stands within all three limits, counted with the script's own functions: paragraph 1, 3 sentences and 229 words; paragraph 2, 1 sentence and 72 words; 301 words in all. `python -B elements/common/foundation_check.py` has no line for WAY-05.

## Entries changed (mark)

| Entry | Mark | Meaning in English | Znaczenie po polsku |
|---|---|---|---|
| WAY-05, the sentence on a further paragraph | `the cycle's` (as in correction 2; its meaning is the human's item 2, its wording mine) | An entry may carry a further paragraph for each part of its own question that it sets apart, each within the limits of a paragraph, and no limit stands on the number of paragraphs. | Wpis może mieć dodatkowy akapit dla każdej wydzielonej części własnego pytania, każdy w granicach limitów akapitu, bez limitu liczby akapitów. |

No test quotes the changed text: the tests hold WAY-05 by the starts of the sentence "A decision entry opens with one to three binding sentences that answer its question" and of "The check of the foundation reports as an error a paragraph of binding sentences", both unchanged (`0 errors` of the check, which reads those lines).

## Checks (command, exit code)

- `python -B gate/run_tests.py elements/common` — exit 0, 289 tests, OK.
- `python -B gate/run_tests.py agent-instructions` — exit 0, 52 tests, OK.
- `python -B gate/run_tests.py product-guidelines` — exit 0, 14 tests, OK.
- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`.
- Linter: not run, no Python file changed. Not run: the full gate.

## Own-work check

The weakest point: that the three statements now say the same, and that "sets apart" does not read as a new limit. I read the three side by side against item 2 of the remarks ("each such paragraph stands within the limits of a paragraph") and the way not chosen under item 1 (a limit on the number of paragraphs): each allows a paragraph for each part, within the limits of a paragraph, and none counts paragraphs. "That it sets apart" names the parts the entry divides out; it is the reviewer's own wording and carries no number. The check of the foundation and the tests of the quotations confirm the quoted sentences still stand.

## Unread material

- `task-cycle/change/fix.md`, `task-cycle/skill/foundation_step.md` and `elements/decisions/skill/SKILL.md`: not re-read (read whole in earlier turns). The reviewer's report `review-correction-2-report.md` was not read; the findings file was enough.

## Searches not found or unclear

- none

## Working copies

- `.runs/author-correction-2-fix/` (outputs of the runs): removed. `.runs/quality-venv/` stays as before.
