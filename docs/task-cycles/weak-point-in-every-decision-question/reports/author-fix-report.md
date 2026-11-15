# Author fix report — Minor findings of the whole-change review

**Status:** `done`. All five findings fixed; none held wrong. Reviewed head `a3c97df`.

Commit: see the last line of this report (the fix is one commit on `task/weak-point-in-every-decision-question`).

## Findings, as fixed

1. `process-audit/SKILL.md` (step 3, the sentence on the newest earlier note): now reads "which
   matters the human weighed, decided on a step or set aside". Checked again with a grep for
   "set aside" in the file: every place that names the outcomes now names the third.
2. `task-cycle/skill/request_template.md`, the example with the fifth part: the way that accepts the
   risk now reads "Letting it through accepts that risk; undoing it, a correction after someone has
   lost a change", so the example shows the word "nothing" on the other two ways and a real cost on
   the one that cannot be taken back cheaply. The first example (the restore instruction) keeps
   "nothing" on all three ways: for each of them undoing it is a later change of the instruction,
   which is cheap, so the word is true there.
3. `foundations/decisions.md`, WAY-113 *Verification*, `complies`: the line on the rounds of a
   project definition now also gives the reason move — a decision costly to reverse whose reason
   neither the person's words nor the material give draws one question asking the reason.
4. `project-level/skill/rounds.md`: (b) the "I do not know" item reads "to a question of decision,
   answer with a recommendation put as "How a skill asks" gives it", as the finding proposes;
   (a) the heading now reads "Three moves and one rule run through the rounds". The finding offered
   "Two moves ... and one rule or similar"; the list holds three moves (contradiction, implication,
   the reason) and one rule, so "Three moves and one rule" is the count that is true.
5. Wrapping: the WAY-378 binding sentence and the WAY-174 *Verification* line were re-wrapped to
   100 columns, and the line of 106 characters in `project-level/lead/skill/route_changes.md` was
   re-wrapped. No word changed.

## Files changed

`foundations/decisions.md`, `process-audit/SKILL.md`, `project-level/lead/skill/route_changes.md`,
`project-level/skill/rounds.md`, `task-cycle/skill/request_template.md` — five files, about 24 lines
added and 23 removed (`git diff --stat`).

## Checks (command → exit code)

- `python -B elements/common/foundation_check.py` → 0 (`0 errors`), run after the last edit.
- `python -B gate/run_tests.py task-cycle` → 0.
- `python -B gate/run_tests.py process-audit` → 0.
- `python -B gate/run_tests.py project-level` → 0 (278 tests).
- Not run: `product-guidelines` (no file of it changed in this fix), the full gate (the orchestrator's).

## Own-work check

- Requirement most likely not met: the fix must leave no place that still names only two outcomes
  of the audit or only the implication move of the rounds, since the review's findings 1 and 3 came
  from a sentence the first change did not update.
- Check: `git grep -n -E "set aside|weighed" -- process-audit/SKILL.md` and
  `git grep -n -E "implication|reason of a decision" -- foundations/decisions.md project-level elements/common`,
  each hit read in its place.
- Result: the audit lines (13, the step 3 introduction, the note's list) all name three outcomes
  after the fix; the rounds, `way_of_working.md` and WAY-113 name both moves in the binding
  sentence, in `complies` and in the list of the rounds. The heading count of `rounds.md` (finding
  4a) was counted from the list itself, which is how the "three" was found.

## Unread material

- `reports/review-whole-report.md`, the full report of the review: not read; the findings file was
  the source, as the handoff gives it.
- `task-cycle/change/fix.md`: not read — the handoff names it only "when the method names it" and
  the method of this fix (the findings file, no reserved choice, no finding held wrong) did not
  need it.

## Searches not found or unclear

- none. (The finding 2 line numbers `:424` and `:400-402` had moved by the earlier commit's own
  wrapping; found by the text of the sentence.)

## Working copies

- `.runs/author/` held the logs of the checks `fix_*.log`; no script was made (the edits were made
  with short inline scripts that left no file). The logs stay in the ignored directory; nothing
  else was made, and no worktree, clone or screenshot.
Commit: `d542af0`
