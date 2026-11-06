# Return step — task `glossary-three-questions`

**Status:** done. **Commits:** none (head stays `049e84e9fdea1784f348b29e7f20f33491e02ec5`; `git status --short` empty).

- **Foundation compared with code:** compared the six entries the change writes or changes (WAY-11, WAY-95, WAY-97, WAY-99, WAY-104, WAY-293), the decisions the task names (WAY-161, WAY-263, WAY-226, WAY-72, WAY-171, which the change leaves as they are), and the part map entries of `decisions`, `glossary`, `task-cycle` and `elements-common`, against the files of the repository at the head:
  - `elements/glossary/template.md` states the same rules as WAY-95 (narrower meaning), WAY-99 (sentence test, English text, other-language files), WAY-97 ("A changed meaning": English text) and WAY-104 ("Two glossaries": both directions, bare use stays bare); the old `TODO — decision pending: which decision sets when two uses of a word carry two meanings` is gone and WAY-99 carries the rule.
  - `task-cycle/review/SKILL.md` section 3 states WAY-293 with the same grades and carve-outs; WAY-263's paragraph is unchanged. It says "a word should have a glossary entry" where WAY-293 says "needs"; the review of the fix judged the two wordings to mean the same and not a finding, so I made no edit.
  - `elements/common/way_of_working.md`, `elements/glossary/skill/decide_entry.md`, `task-cycle/record_template.md` and `task-cycle/skill/return_step.md` agree with WAY-95, WAY-99 and WAY-11 as changed.
  - Part map: the responsibilities, files and dependencies of the four parts still match what the change did; no file was added, removed or moved, so no entry moved. No invariant names WAY-95/97/99/104/293 (search of `foundations/invariants.md`), so none needed a change.
  - What no longer matched: nothing found. Correction: none.
- **Decisions written or changed:** WAY-293 (new); WAY-95, WAY-97, WAY-99, WAY-104 (edited in place); WAY-11 (one phrase: "a meaning other than the usual one" -> "a meaning for which WAY-95 gives it an entry").
- **Invariants written or changed:** none.
- **Environment facts:** none (the change rests on no source outside the product).
- **Glossary terms:** none. The change adds no glossary entry; "qualifier" is used in WAY-104 and the template as a phrase holding the word, defined where it is used, and WAY-95 as now written gives it no entry (no sentence reads it differently for a reader of the field).
- **Part-map changes:** none.
- **Projected entries written whole or in part:** none (the task has none).
- **Rows of *Settlements to record* written:** row 1 -> WAY-95; row 2 -> WAY-293; row 3 -> WAY-99; row 4 -> WAY-104; row 5 -> WAY-99 (with WAY-97 narrowed to English text).

## Checks
- `python -B elements/common/foundation_check.py .` -> `0 errors`, exit 0 (run for this report; nothing changed by the return step).
- `python -B gate/run_tests.py <directory>`: not run, nothing changed; the orchestrator ran the full gate on this head, exit 0.

## Searches not found or unclear
- The Minor and out-of-scope findings of `review-1.md` (M1-M6 and one out-of-scope) were read and left untouched (WAY-161); they are no foundation entries.
- Whether "qualifier" deserves a glossary entry is a judgment I took as "no"; the reviewer or the human may weigh it at the merge.
- The one-word difference between the skill sentence and WAY-293 ("should have" / "needs") is left, as the review of the fix put it, to the human; fixing it would add a commit and a review of that range.
