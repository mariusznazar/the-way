# Return step, second run — what the correction `9703d0b` reaches

Head compared: `9703d0bf55d54a1e8b6b45ec6ebd4fd717e86381`. Commits of this run: none. Nothing needed correcting.

## Return step (fields of `task-cycle/record_template.md`)

- **Foundation compared with code:**
  - WAY-172 against the changed paragraph and the "Never writes" row of `coding/SKILL.md` (lines 45-52) and `testing/SKILL.md` (lines 44-51): both now give the two ways (the task document; approval at a blocked draft request where the document does not settle the meaning), the exception clause in the row, and "Using a meaning that a decision ... already carries takes no approval" (WAY-172). Matches; the wording equals the styleguide skill's. `grep "only through the task document"` over the repository finds nothing.
  - WAY-124 (cited in the paragraph for the human's acceptance of the whole document): the sentence "the human's acceptance of the whole document before the cycle approves every new or changed meaning" is unchanged and still agrees with it.
  - WAY-265 against `testing/SKILL.md` step 2 ("read `research.md` beside this skill too", same condition as `starting_set.md:11-12`) and step 4 ("read `new_tools.md` beside this skill too", as `settle.md:3-4`); `coding/SKILL.md` already complied. Both names stand in `SKILL.md` and in the step file, as WAY-265 asks. Matches.
  - WAY-256 (variant files named by the step, one level deep): the three skills now name `research.md`, `new_tools.md` (and `staged_cleaning.md`, `trial_run.md` where they exist) from the step; matches.
  - WAY-216, WAY-240, WAY-282, WAY-310, WAY-311 as far as the two skills restate them: `coding/SKILL.md` "A new kind" and step 4 restate WAY-216; the "Where the skill works" sentence of both restates WAY-282's hand-back rule (corrected in `f5ae96f`, untouched by the correction); the correction touched no line that restates WAY-240, WAY-310 or WAY-311. Matches.
  - Part map entry of `product-guidelines`: the correction edits two files inside `product-guidelines/**`; responsibility, files, dependencies unchanged. Matches.
- **Decisions written or changed:** none.
- **Invariants written or changed:** none.
- **Environment facts:** none.
- **Glossary terms:** none.
- **Part-map changes:** none.
- **Projected entries written whole or in part:** none.
- **Rows of *Settlements to record* written:** none in this run (rows 1-5 were written by the foundation step).

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` — 0 errors, exit 0 (no commit; run to confirm the log is as it was).
- Earlier, on the correction itself (report `correction-report.md`): the installation unittest modules for the coding and testing skills, exit 0; `check_instructions.py`, exit 0. Not re-run, since no file changed in this run.
- Not run: the full gate.

## Reaches beyond the dispatch

- `grep` for "only through the task document" and for WAY-172/WAY-265/WAY-256/WAY-124 citations in the two skills; `WAY-124` read whole (it was not in my earlier reads).

## Choices

- Judged the correction's choices (copy of the styleguide wording; the "Where the skill works" prose left as it was) against `return_step.md`: skill text only, no entry; they stay rows of the questions table.

## Searches not found or unclear

none
