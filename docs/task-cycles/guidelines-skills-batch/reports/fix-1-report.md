# Report of the fix of the review's findings — guidelines-skills-batch

**Status:** `done`

**Commit:** `2c46cb7` Fix the findings of the review of the whole change (range from `e66e8e7`).

**Files changed (added / removed):** `foundations/decisions.md` 4/3; `instruction-files/judging.md` 1/1; `product-guidelines/coding/SKILL.md` 3/3; `coding/settle.md` 2/1; `coding/template.md` 1/1; `product-guidelines/styleguide/SKILL.md` 1/1; `product-guidelines/testing/new_level.md` 2/1; `testing/settle.md` 4/2 (net, see diff); `project-level/task/skill/guideline_findings.md` 9/8.

## Findings

**I1 (Important) — fixed.** The review is right: the base read `new_level.md` for any level and settled the exemplar there; after item 10 nothing settled the exemplar of a level whose recipe the task's extension adds.
- `product-guidelines/testing/settle.md`: the exemplar bullet now reads "for each level with tests, its exemplar test, and for a new level, whether of step 3 (`new_level.md`) or one the task's extension adds with its recipe, that the task's first test of it becomes the exemplar (WAY-242, WAY-251)". Step 4 reads `settle.md` for every task, so the extension path reaches it.
- `product-guidelines/testing/new_level.md`: the last sentence now says the extension takes step 2 as well "and step 4 settles there, as for a new level, that the task's first test of the level becomes the exemplar, as `settle.md` gives". This removes the contradiction the review named in `recognize.md` / `new_level.md`; `new_level.md` still writes no recipe.
- Own-work check: the requirement is that every route of a task whose outcome is the first test of a level ends with the designation settled. Paths checked by reading: level with recipe and empty *Exemplar* — step 3 `new_level.md`, step 4 `settle.md`; level without recipe — step 1 `recognize.md` gives the extension, step 2 and step 4 `settle.md` bullet; then `guideline_findings.md:44-48` ("the extension ... and that this test becomes the level's exemplar") is carried out by the same bullet. A grep for `exemplar` in `testing/*.md` now finds `settle.md` covering both. No contradiction left in `recognize.md:21-25`.

**M1 — fixed.** `coding/template.md` departure table: the row for `### Recording a failure` now has in *Goes with it* what the rule says (the way a failure is written, with its cause, once, where code handles it, and the last-resort handler — the sentences of the template for that rule), and in *Stays* "the rest; each rule that stays keeps the meaning of every word it takes from this one, in its own text, as `### Hiding a failure` keeps what a failure is and that an expected refusal is no failure". "nothing else" is gone from that row. Check: read the row against the item and the rule's own bullet in "What each section carries".

**M2 — fixed.** WAY-311 *Rationale*: "Its weak points: two more sentences in what is read at every judgement, and a departure from the order of the sections stays as it is." (the reviewer's proposal, without naming a file). Check: compared with the source weak point in the task's question 3; `foundation_check.py` passes.

**M3 — fixed.** `project-level/task/skill/guideline_findings.md`, both places: `project-level/task/skill/read_sources.md` in full. Check: the file exists at that path; paragraphs rewrapped.

**M4 — fixed, the reviewer's second reading (the smaller).** The clause "which are those whose tool reads the language of the kind's files" is removed from the "A new kind" bullet of `coding/SKILL.md`; "touches" is left to the agent's judgement, as WAY-216's binding sentence and *Rationale* have it. The extension trigger (a language no standing check reads) stays, since the row gives it. I did not add a criterion to WAY-216, which would be a new binding rule the sources do not give. Check: grep for "reads the language" in `product-guidelines/coding/` finds only the extension trigger in `recognize.md` and `SKILL.md`; WAY-216's *Verification* example speaks of the checks "that read the language of migrations" as an example, not as a definition — left, as it binds nothing.

**M5 — fixed.** WAY-240 *Scope* is now `product-guidelines, glossary`. `foundation_check.py` exit 0 (glossary is a part).

**M6 — fixed.** `instruction-files/judging.md`: "(WAY-311)" at the end of the new paragraph.

**M7 — fixed.** `product-guidelines/styleguide/SKILL.md` table row: "a meaning the task did not settle, except as a decision proposed at a blocked draft request (WAY-172)".

**M8 — fixed, the reviewer's reading (the smaller).** `coding/settle.md`: "run the trial again on the chosen one, as `trial_run.md` gives, for the split alone and before it is proposed". The audit's list of causes stays as step 3 left it; no rule for redoing it was added.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` — 0 errors, exit 0 (after the decision edits).
- `python -B gate/run_tests.py instruction-files` — exit 0 (104 tests, 5 skipped).
- `python -B gate/run_tests.py project-level` — exit 0 (271 tests).
- `python -B gate/run_tests.py elements/common` — exit 0 (109 tests).
- `python -B gate/run_tests.py agent-instructions` — exit 0 (18 tests).
- `python -B -m unittest installation.test_coding_guidelines_installation installation.test_testing_guidelines_installation` — exit 0 (4 tests).
- Not run: the full gate (reserved); directories I did not touch.
- No test first: prose and foundation entries only; no invariant added or changed.

## Reaches beyond the dispatch

None beyond the findings file and the files it names. For M5 I checked that `glossary` is a part of the part map (it is, read earlier).

## Searches not found or unclear

- The sources give no criterion for what a standing check "touches" (M4); I left it open on purpose, as the reviewer allowed. The open point about the audit of dependencies from the first report remains for whoever refines it.
- Nothing else unclear.

## Choices

- M4 and M8: took the reading that adds least (drop the clause; "for the split alone"). Cost if wrong: a reviewer wants a criterion for "touches" in WAY-216 (a decision edit accepted at the merge) or a rule for redoing the list of causes (a decision).
- M1: *Goes with it* holds the rule's own text as the template states it, not a new claim about consequences. Cost if wrong: one table cell.
- I1: the fix lives in `settle.md` (the bullet) plus one sentence in `new_level.md`, not in `SKILL.md` step 3, so the step-3 condition added by item 10 stays as the item asked.

## Problems as observed

None. While editing I once rewrapped a block with a helper that flattened a list bullet in `testing/settle.md`; I saw it in the diff before committing and restored the indentation, so the committed text is as intended (checked against `git diff`).
