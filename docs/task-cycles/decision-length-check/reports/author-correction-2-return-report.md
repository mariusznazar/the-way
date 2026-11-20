# Author report — the return step after correction 2

**Status:** done. Nothing no longer matches, so I changed and committed nothing; the head stays `a8753bb8` and the worktree is clean.

## Commits

none

## Return step (in the form of the record)

- **Foundation compared with code:** the entries correction 2 wrote or changed, against `check_length`, `excess` and the constants in `elements/common/foundation_check.py`, its head description, `elements/common/foundation_text.py` and the tests.
  - **WAY-05** (read whole, *Rejected* too, `foundations/decisions.md:682-`):
    - The limits it states — a paragraph of at most three sentences and 300 words, all the binding sentences of a decision together at most 600 words — are `SENTENCE_LIMIT = 3`, `WORD_LIMIT = 300` and `ENTRY_LIMIT = 600` of the script; a word is a run of characters between spaces and a sentence is counted by `begins_sentence`, as the template says.
    - The second paragraph — an error in a decision a change adds or whose binding sentences it alters (a different division into paragraphs included), a list for any other — is what `check_length` does (`before.get(key) != paragraphs` decides "changed"; an unknown base adds and alters nothing).
    - The sentence on a further paragraph "for each part of its own question that it sets apart" is a permission the code does not and need not enforce (it counts no paragraphs); no test holds it.
    - *Verification*: the clause `tests:` names the limits, the error and the list and the counting, each held by tests carrying a line `decision:` that quotes the start of "A decision entry opens with one to three binding sentences that answer its question" or "The check of the foundation reports as an error a paragraph of binding sentences", both still true in the entry. The pair of examples now covers only whether a part of a question has a paragraph of its own, which no test holds (and the fields and the rationale), so the part a test holds is out of it, as the step requires.
    - WAY-05 meets its own limits: 3 sentences and 229 words, 1 sentence and 72 words, 301 words in all (counted with the script's functions in the fix); the check reports no line for it.
  - **The template `elements/decisions/template.md`**: the entry form (the block for another question's part, and the optional block for a part of the heading's question with the 600 words), "Binding sentences" (the two bullets), the row "binding sentences" of the table of readers and the bullet of "Changing a decision" say what WAY-05 and the code say. The description of the check in the script's head, `README.md` and `agent-instructions/README.md` name the same report as the code gives.
  - **WAY-12** (the check of what holds a decision, which keeps its comparison of the joined text) and **WAY-02** (the line `decision:` and the start of a sentence): the code of the check of what holds a decision is unchanged and `base_sentences` still wraps `base_paragraphs`; the counting of a sentence is the one WAY-02 gives. **WAY-22**: the sentences of WAY-05 that tests hold have no derived invariant, and none was written. **WAY-385**: `foundation_check.py` stands at 1115 lines (limit 1200), `check_length` at about 30 lines (limit 110); the size test passes. **WAY-19**: not changed, as the handoff says (its words and WAY-05's name a part differently; see below).
  - **Part map:** the sentences of `decisions`, `elements-common` (both modules named) and `agent-instructions` still hold; no file moved and no dependency changed in correction 2.
- **Decisions written:** none in this step (the settlements stand written in WAY-05 by correction 2 and its fix).
- **Invariants written:** none. **Environment facts written:** none. **Glossary terms written:** none. **Part-map changes:** none. **Projected entries written:** none.
- **Rows of *Settlements to record* written:** none in this step. The two settlements of the remarks stand written, in WAY-05 and in the template, both marked `the cycle's` in my report of correction 2 (no row of the task carries them; they come from the human's remarks on the request):
  1. the limit of 600 words for all the binding sentences of one decision, with the error for a decision a change adds or alters (a different division included) and the list for any other — in the first and second paragraphs of WAY-05, its *Verification* `tests:` clause, *Rationale* and *Rejected* (no limit for the whole entry; a limit on the number of paragraphs), and in the template's entry form, "Binding sentences" and the row of the table of readers;
  2. a further paragraph for each part of the entry's own question that it sets apart, within the limits of a paragraph, with no limit on the number of paragraphs — in the first paragraph of WAY-05, its pair of examples, *Rationale* and *Rejected* (the rule kept for another question's part alone with entries divided anyway; every such entry rewritten or split), and in the template's entry form and "Binding sentences".
  The two earlier settlements, rows 1 and 2 of the task, stand in WAY-05 marked `row 1` and `row 2` (foundation step), and the one sentence of *Rationale* marked `the cycle's`.
- **The choices of the questions table:** none new in this step; the choices named after the first return step (the module `foundation_text.py` and the wording of the check's message) stand as then judged: no entry.

## Findings of the reviews left as they stand (go to the request's list)

As the handoff gives, I left, and fixed none of:
- the name of a part in WAY-19 ("a part of the question an existing entry answers") against WAY-05 ("a part of another question" / "of its own question") — a Minor finding of the review of correction 2; WAY-19 is unchanged;
- "for this report alone" in `agent-instructions/README.md` — a Minor finding of the review of correction 2;
- the words "all the binding sentences together at most 600 words" inside the optional block of the entry form of the template, which belong to the whole entry and not to that kind of paragraph — the Minor finding of the review of the fix.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`.
- No file changed, so no focused test run was repeated; the runs of the fix stand (`elements/common` 289 tests, `agent-instructions` 52, `product-guidelines` 14, all exit 0).
- Not run: the full gate (as handed).

## Unread material

- `task-cycle/skill/return_step.md` and `task-cycle/skill/foundation_step.md`: read whole in earlier turns, not re-read. The reviews of correction 2 and of the fix were not read; the handoff names the findings.
- The part map and the invariants file were not read again; the entries named above are from the earlier return steps, and no file of a part moved in correction 2.
- WAY-12, WAY-02, WAY-22, WAY-385 and WAY-19 were compared through the index of the selection and the earlier turns, not re-read whole in this step.

## Searches not found or unclear

- none

## Working copies

- none made (`.runs/author-correction-2-return/` was not needed) and no file outside the worktree. `.runs/quality-venv/` stays as before.
