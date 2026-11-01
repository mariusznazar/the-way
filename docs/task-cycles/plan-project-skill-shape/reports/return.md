# Return step - plan-project in the WAY-256 shape

**Status:** done. No commit (no entry and no file needed a change). Head stays `1fa823e`; the worktree is clean.

Read whole: `task-cycle/skill/return_step.md`, `task-cycle/skill/foundation_step.md`, `task-cycle/record_template.md` (Return step), and in `foundations/decisions.md` each of WAY-13, 35, 106, 113, 120, 125, 126, 127, 142, 143, 144, 145, 146, 147, 150, 151, 152, 156, 200, 218, 230, 242, 247, 256, 257, 259, 265, 266; the part-map entry `project-level`; the invariants project-plan-form, project-plan-check, skill-entry-points, instruction-file-imports, repository-file-location, outbound-link-reach; the environment fact `claude-skill-nested-references`. The glossary was searched for the words the change uses, not read whole.

## Return step (lines of `task-cycle/record_template.md`)

- **Foundation compared with code:**
  - WAY-256: every fragment is placed by what it is. The picture of the whole, the rules across steps (the originals are authoritative; a new breakdown covers everything) and the pointers stand in `SKILL.md`; the delegated variant, the work on an existing plan, the guidelines tasks and each step's procedure stand in files that the step or variant names; the one-instruction fragments (step 0's reading of the template and "Otherwise begin with step 1") stay. Matches.
  - WAY-265: the variant files pointed to from a step file (`delegated_mode.md`, `guideline_tasks.md`, `existing_plan.md`, `reading_definition_and_plan.md`) are named in `SKILL.md` at that step with their condition. Matches.
  - WAY-257: the table of `assessment.md` shows both answers in every row. Matches.
  - WAY-125, WAY-127, WAY-259 and the invariant skill-entry-points: the skill still names its files "beside this skill", read when the step or variant comes; the 11 new files are not named `SKILL.md`, so no new entry point is due; `skill_entry_points.py --write` changes nothing. Matches.
  - WAY-150, WAY-151, WAY-218, WAY-266: reading of the foundation and the guidelines (`read.md`), the inventories and the whole-original checks (`reading_definition_and_plan.md`, `SKILL.md`) and the critique reading the whole plan (`critique_plan.md`) are the base's text, moved; a sentence comparison found every base sentence verbatim except three pointers reworded. Matches.
  - WAY-142, 143, 144, 145, 146, 147, 230, 247, 242, 200, 152, 106, 120, 113, 156: the sentences that carry them stand unchanged in the files (checked sentence by sentence); step numbers 0-7 and the heading "Delegated work while leading a plan" are kept, so "plan-project step 0" of WAY-156 and the lines of `project-level/lead/skill/SKILL.md` and `project-level/skill/SKILL.md` still resolve. Matches.
  - WAY-35: the files restate rules of `project-level/plan/template.md` exactly as the base did; the rebuild neither adds nor removes such a restatement (proposals 2-5 of `assessment.md` stand for the request, not for an edit). No new mismatch.
  - WAY-13: nothing in the change depends on a count of words or lines. Matches.
  - Invariants project-plan-form and project-plan-check: their scripts and the plan template do not change. instruction-file-imports: no `@` in the new files. repository-file-location and outbound-link-reach: all new files lie in `project-level/plan/skill/`, no link outside.
  - Part map `project-level`: `project-level/**` covers the 11 new files (13 files changed, all under `project-level/`); the trust boundary (`readiness_check.py`, `plan_check.py`, `plan_state.py`) is untouched. No change due.
  - Environment fact `claude-skill-nested-references`: the files stand one level deep from `SKILL.md`, as the fact asks.
  - A search of `foundations/` for "Reading the definition and plan", "plan/skill", "plan-project" found WAY-151, WAY-156 and WAY-218 only; none names the moved section or file. What no longer matched: nothing; corrections: none.
  - The cycle's choice C4 ("goes through `read.md`"): it follows WAY-256's clause that a later step has a file read unless an earlier step did, and WAY-150's selective reading, and contradicts neither. It binds one thing the foundation does not state elsewhere: a session on an existing plan carries step 1 (the readiness check, the foundation, the guidelines) before it edits, where the base's text sent a resumed draft past step 1. That binding stands in the skill's text and rests on the accepted answer of task question 3, which gives no row of *Settlements to record*. Neither WAY-256 nor WAY-150 states it, so it binds beyond them as the skill's own rule; I wrote no entry for it, as the task excludes one and the return step writes a decision only for a choice that binds after the merge beyond the text it is in. If the human wants it a decision, that is a new entry and a question for the request, not an edit by me.
- **Decisions written or changed:** none.
- **Invariants written or changed:** none.
- **Environment facts:** none.
- **Glossary terms:** none (the words used - step, variant, pointer, dispatched turn - are used in their usual meaning or have no entry).
- **Part-map changes:** none.
- **Projected entries written whole or in part:** none (the task has no projected entry).
- **Rows of *Settlements to record* written:** none (the task has no row).

## Checks (worktree at `1fa823e`)

- `python -B elements/common/foundation_check.py` exit 0 (0 errors)
- `python -B instruction-files/check_instructions.py .` exit 0 (0 error, 1 warn - the base's dead path in `AGENTS.md` -, 3 info)
- `python -B agent-instructions/skill_entry_points.py --write` exit 0 ("entry points are current"; changed nothing)
- `python -B .runs/task-cycles/plan-project-skill-shape/tools/verify_counts.py .runs/task-cycles/plan-project-skill-shape/reports/word-counts.md` exit 0 (279 figures, 0 differ); no counted file changed in this step, so the file was not regenerated.
- Not run: the whole gate (the orchestrator's).

## Searches not found or unclear

- No glossary entry holds "step", "variant" or "pointer"; I judged them as used in their usual meaning.
- Whether the human wants the C4 binding recorded as a decision is unclear; the task says no row (see above).
