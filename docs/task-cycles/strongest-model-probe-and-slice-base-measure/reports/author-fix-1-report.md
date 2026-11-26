Status: done

# Author report — fix 1 (findings I-1, I-2, M-1 to M-4)

**Commit:** `15bf941a` (range from the reviewed head `60561fba`), branch `task/strongest-model-probe-and-slice-base-measure`.
Files: `foundations/decisions.md`, `task-cycle/skill/SKILL.md`, `task-cycle/change/slice.md`, `task-cycle/plan/SKILL.md`,
`task-cycle/record_template.md`, `task-cycle/skill/blocked_finding.md`, `task-cycle/skill/reserved_return.md` (72 insertions, 61 deletions).
No code or test changed; no skill name or description changed.

## What I did for each finding (none held wrong)

- **I-1.** The probe now runs again in every later session of the orchestrator, a correction's included, before that
  session's first dispatch of the strongest class, and the sentence that had a continuing session read the earlier
  model is gone. WAY-229 paragraph 2 ("in every cycle, and again in every later session of its orchestrator, before
  that session's first dispatch...", every dispatch "in the session"), its *Verification* (complies: a later session
  probes again; violates: a later session dispatches on the model an earlier one fixed with no probe), the paragraph
  before step 9 of `task-cycle/skill/SKILL.md` (also "never ... from the model an earlier session fixed", tries written
  "of the session"), and the *Strongest class* item of `task-cycle/record_template.md` (tries per session, a correction's
  included).
- **I-2.** The exception is narrowed to "a test that an earlier slice's *Goal* announces and the slice's own *Checks*
  hold" in WAY-136's binding paragraph 3, in its *Verification* (complies and violates), in
  `task-cycle/change/slice.md` and in step 9 sub-step 4 of `task-cycle/skill/SKILL.md`. A search of the tracked files
  for the old wording ("a test of the slice's *Checks*") finds nothing left.
- **M-1.** `task-cycle/skill/SKILL.md`: where the tool does not name the row by the description, the probe's row is the one
  whose start, in the table's section of start times, is that of its dispatch; the row's model matches the candidate
  where it is a model of the candidate's family, an older version included, and only a model of another family is a
  substitution.
- **M-2.** `task-cycle/plan/SKILL.md`: "its *Goal* names each such test file and the slice that makes it pass; the plan
  writes the same test into the *Checks* of that slice, and no slice between the two holds it in its *Checks*."
- **M-3.** WAY-136's binding sentence and its *Verification* both say the *Checks* of the repairing slice "hold the tests
  of that file".
- **M-4.** The sentence setting the models from `stages.md` now reads "here and in each stop that runs the script", and
  each stop names it: step 9 sub-step 4 (slice failed twice), the paragraph on a question about a test, and
  `task-cycle/skill/blocked_finding.md` and `task-cycle/skill/reserved_return.md`.

## Foundation entries

WAY-229 (`row 1`) and WAY-136 (`row 2`, `row 3`) keep their marks and meanings; the changes narrow them to the task's words.
WAY-229 still has the meaning of my first report with the probe per session; WAY-136 the exception limited to the owner's
announced test. No pair of examples added.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` — exit 0, "0 errors".
- `python -B instruction-files/check_instructions.py .` — exit 0, "0 error, 0 warn, 5 info".
- `python -B gate/run_tests.py task-cycle` — exit 0; `elements/common` — exit 0; `project-level` — exit 0.
- Not run: the full gate.

## Own-work check

Requirement likeliest not met: the exception of WAY-136 limited to the owner's announced test, in every place. Checked by
a search of all tracked files for the old wording (none left) and for `reads them there` (none left); the foundation
check passes with the word limits (the paragraphs stay under 300 words).

## Reaches, working copies, unread material, searches

- Reaches beyond the handoff: none.
- Working copies: none made; test logs stand in `.runs/author/` (ignored).
- **Unread material:** none.
- **Searches not found or unclear:** none
