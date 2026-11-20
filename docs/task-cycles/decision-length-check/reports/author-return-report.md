# Author report — the return step

**Status:** done. Nothing no longer matched, so nothing was changed and nothing was committed; the head stays `9c7f9b71`, the worktree is clean.

## Commits

none

## Return step (in the form of the record)

- **Foundation compared with code:** the entries the change writes or changes, those the task names, those the search found, and the part map of the touched parts, each against the code at `9c7f9b71`.
  - WAY-05 as it stands in `foundations/decisions.md:682-754`: the limits (3 sentences, 300 words per paragraph), the error for a decision a change adds or whose binding sentences it alters (a different division into paragraphs included), and the list for any other, match `check_length`, `excess` and `base_paragraphs` of `elements/common/foundation_check.py` and the 12 tests of `elements/common/test_foundation_check.py`. WAY-05 itself has 3 sentences and 199 words in paragraph 1 and 1 sentence and 64 words in paragraph 2.
  - The pair of examples (task point 6): *Verification* opens with the clause `tests:` naming what the tests hold (the limits, the error and the list, the counting); the pair left in it covers the fields, the rationale and whether a part of another question has its own paragraph — none of which a test holds — and what was held (a paragraph of five sentences; the folded part running past three sentences) is out of it.
  - WAY-12, WAY-02, WAY-22, WAY-385 (named by the task, unchanged): WAY-12's check of what holds a decision still compares the joined text, as the code does; WAY-02's line `decision:` and its counting of a sentence are the ones the new check reuses (`begins_sentence`); WAY-22 gives the sentences of WAY-05 that a test holds no derived invariant, and none was written; WAY-385 holds: `foundation_check.py` stands at 1111 lines, `foundation_text.py` at 112, and the size test passes.
  - Part map: the sentence of `elements-common` names both modules (`foundation_source.py` and `foundation_text.py`, written in the fix `9c7f9b71`) and `elements/common/**` claims the new file; the sentences of `decisions`, `repository` and `agent-instructions` stay true (the template, the log, the READMEs and the guide changed within what they already answer for). The surface `foundation-check-command` (path, argument, exit codes) is kept: the new report changes none of them. No *Depends on* needs a change: `foundation_text.py` is in the part that holds `foundation_check.py`, and the importers (`decision_index.py`, `test_cross_part_imports.py`) are unchanged.
  - Invariants: `own-foundation-check-report` (the check run with no switch reports no error) holds — `python -B elements/common/foundation_check.py` exit 0, `0 errors`; `function-and-file-size` holds. No invariant names the 3-sentence limit.
  - Glossary: "binding sentence" and "binding part" keep their meanings; the change uses no word in another meaning.
  - Texts that say "one to three binding sentences (WAY-05)" (the two product-guidelines templates, a decision about a table) stay true: the limit of sentences is unchanged.
- **Decisions written:** none in this step (WAY-05 was written in the foundation step, rows 1 and 2).
- **Invariants written:** none.
- **Environment facts written:** none (the change rests on no source outside the product).
- **Glossary terms written:** none.
- **Part-map changes:** none in this step (the sentence of `elements-common` was changed in the fix).
- **Projected entries written:** none (the task projects none).
- **Rows of *Settlements to record* written:** none in this step; rows 1 and 2 stand written in WAY-05 (foundation step, commits `58f9937d`).
- **The choices of the questions table, judged as `return_step.md` gives:** neither enters the log.
  - The move of the readers of an entry's text into `foundation_text.py`, with the names kept importable from `foundation_check`: WAY-385 and WAY-365 already bind what makes it necessary, and the split itself is where code lives — a single location of code, which the template's question 3 of "Where it goes" sends to the product's code with the test that holds it, not to the log; no cost is attached that someone could reasonably propose the rejected way for (WAY-293's condition for a choice in the log).
  - The wording of the check's message: a single text, question 3 of the same list, held in code with the tests that name the decision, the paragraph and the measure; it binds nothing after the merge.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` — exit 0, `0 errors` (12 `listed:` lines for the entries the next task shortens).
- No file changed, so no focused test run was repeated; the focused runs of the fix stand (`elements/common` 283 tests, `elements/part-map` 40, `agent-instructions` 52, `product-guidelines` 14, all exit 0; ruff check and format exit 0).
- Not run: the full gate (as handed).

## Unread material

- `elements/glossary/skill/SKILL.md`, `elements/part-map/skill/SKILL.md` for this step: not read again, since no entry was written (the part-map skill was read whole in the fix).
- The part map was read in the entries of the touched parts and the surfaces (`decisions`, `part-map`, `elements-common`, `repository`, `agent-instructions`, `foundation-check-command`), not whole; the invariants file by search (`foundation_check`, `own-foundation-check-report`, `function-and-file-size`), not whole.

## Searches not found or unclear

- none

## Working copies

- none made (`.runs/author-return/` was not needed). `.runs/quality-venv/` stays as before (the environment of Ruff).
