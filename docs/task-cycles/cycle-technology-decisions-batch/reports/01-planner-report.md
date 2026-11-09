# Planner report — cycle-technology-decisions-batch

Status: done with concerns

- Plan: `.runs/task-cycles/cycle-technology-decisions-batch/plan.md` (11 slices; 12 foundation entries)
- Size report: `.runs/task-cycles/cycle-technology-decisions-batch/plan-size.md`
- Size script: `python -B task-cycle/slice_size.py .runs/task-cycles/cycle-technology-decisions-batch/plan.md`, last exit code 0, every slice `fits` (largest: Slice 6, about 40,000 tokens to read, 7 files to change). The first runs exited 1: single-line ranges were written `:32` and not `:32-32`, and Slices 9 and 10 changed `foundations/decisions.md` (see concern 1).
- Design choice: none open, none reserved. No spec.

## Concerns

1. **Items 17 to 23 are not slices; the plan names them as foundation entries.** The handoff said to leave them to the slices. The size script counts a changed file whole, and `foundations/decisions.md` is about 755,000 characters, which alone exceeds the limit of one slice (about 625,000); a slice with it in *Change* reported `too large` and cannot be split, and a range in *Change* leaves a slice `unchecked`. `task-cycle/skill/foundation_step.md` has the foundation step write "each entry a reviewed spec or the plan names", so the plan lists seven rewordings (items 17 to 23) as entries beside rows 1 to 5, each with its subject and no wording. Cost: the writer of the foundation step carries twelve entries and their searches of the whole foundation (WAY-33) instead of five. Gain: it works with the size script and runs on the class WAY-229 gives the writer of a plan's entries. The orchestrator should confirm this reading of `foundation_step.md` or send the plan back. The sentence of item 17 in `project-level/definition_template.md` stays in a slice (Slice 6), which depends on the entry for item 17.
2. **Drift since the task's line numbers (46 commits).** Items 10 to 13, 15, 16, 18 to 23, 26, 28 to 30 stand at base. Item 17's second point (the reservation "which opens only on the human's word") is not in the current WAY-165, whose sentence now says the step may open a decision of the foundation (WAY-313); the plan tells the writer to change nothing there if so. Item 25's sentence in the task template ("A lasting exclusion belongs in a projected or current decision, or in a row of *Settlements to record*") may already be enough; item 27's first point may too. Both are marked "change nothing where already so and say it".
3. **Item 28, second point needs a page outside the repository.** The sentence on emphasis cites https://code.claude.com/docs/en/best-practices § "What you can stop doing"; no environment fact holds its passage. The plan has the executor read the page and, if it cannot, return the item as a question. I did not read it.
4. **Slice 3 (item 7) has a design inside it.** The task says the reader "shows the task as blocked" and fixes no output. I chose one added evidence line and no new proposal, state, conflict or exit code (listed in *Choices* with the way rejected). If the human meant a proposal or a state, the slice is wrong.
5. **Two checks I could not name cheaply.** The test for item 9 (the installer test racing a commit in the live repository) has no obvious failing-first form; Slice 5 asks the executor to show the failure with a throwaway copy and say how.

## Guidelines

The-way has no `guidelines/` directory (task question 6); there were no product guidelines to read. Nothing found missing or uncertain beyond that.

## Order against a styleguide example

No styleguide applies (no screens). Order: Slice 1 before Slice 4 (same file); Slice 6 after the entries for rows 1, 2 and item 17; Slice 8 after row 3.

## Reaches beyond the handoff

Invariants reached, by `- **Part:**` and by `invariant:` lines of tests the slices alter:

| Slice | Invariants |
|---|---|
| 1, 2, 4, 6, 7, 8, 9, 10, 11 (prose) | `tracked-file-private-paths` (every): checked by `task-cycle/test_tracked_files_private_paths.py`; `test-method-citation`, `map-reference-target` through `foundation_check.py` |
| 3 | `project-plan-state-evidence`, `project-plan-state-subprocesses` (part `project-level`; tests `project-level/test_plan_state_invariant.py`, `test_plan_state_subprocesses_invariant.py`, run by `python -B gate/run_tests.py project-level`); surface `project-plan-state-command` of the part map |
| 5 | `installation-claude-guidance` (cited by `installation/test_install.py`, six lines; the slice must keep those citations) |
| 6 | `project-technology-record`, `project-definition-form`, `project-readiness-gate` (readiness check reads the definition template's rules; run through the `project-level` tests) |
| 7 | `skill-entry-points` (rename of a non-`SKILL.md` file; checked by `python -B agent-instructions/skill_entry_points.py` with no `--write`) |
| 11 | `cross-part-imports`, `map-reference-target` |

Reaches (what, where, why):

- Decision ranges of WAY-153, WAY-163, WAY-269 (Slice 3), WAY-274, WAY-287 (Slice 2), WAY-296 (Slice 4), WAY-26 (Slice 8), WAY-44 and WAY-299 (Slice 11), WAY-115, WAY-120, WAY-134, WAY-256, WAY-265 (Slice 7), WAY-123 (Slice 6), WAY-130 and WAY-133 (Slice 10): read whole, found by the part map's Scope and by the decisions the task text names; not in the handoff's list.
- `foundations/decisions.md` Scope search over all decisions for `installation`, `instruction-files`, `part-map` and `elements-common` (a script, to see which decisions name those parts); the result was too broad (the part-map scope appears in dozens of decisions) and I took only the decisions bearing on each item; the orchestrator may widen.
- Code read to cut slices: `project-level/plan_state.py` and `project-level/test_plan_state.py` (setUp, helpers and the tests of the record), `task-cycle/remarks_check.py`, `task-cycle/test_remarks_check.py` (test names and the filename test), `installation/test_install.py` (first 260 lines), `task-cycle/slice_size.py` (limits and the Change/Read forms), `agent-instructions/skill_entry_points.py` (head only).
- I ran two existing test files, to see how long they take: `task-cycle/test_remarks_check.py` (45 tests, 0.1 s) and `project-level/test_plan_state.py` (40 tests, 48 s). Nothing was changed.

## Searches not found or unclear

- The line "how to read the logs" of WAY-139 does not appear as a string anywhere in the repository outside `foundations/decisions.md`; `project-level/task/skill/resolve_gaps.md` names only two items of WAY-139's list (the record's life and a failure), so the third has no place to be "tied" to yet; item 16 and row 3 will add it.
- The passage of https://code.claude.com/docs/en/best-practices § "What you can stop doing" that `instruction-files/SKILL.md` and `instruction-files/kind_main_file.md` cite is not held by any file of the repository (no environment fact); not read by me.
- Item 7: the task names no output form for "blocked"; I chose one (concern 4).
- Item 14: which of the two `settle.md` files to rename is not fixed by the task; I chose the critique's (one reference) over the technology step's (six files) — Choices.
- Item 17, second point and item 22's description of the template: the current text of WAY-165 (reservation) is no longer what the task quotes; whether WAY-293's *Rationale* still describes what the request template does today I did not decide, the writer will.
- The planner has no way to measure how long `python -B gate/run_tests.py <directory>` takes for `task-cycle`, `elements/common`, `instruction-files` or `elements/part-map`; I did not run them. Only the two test files above were timed.
- `foundations/part_map.md` has the part `installation` depend already on `task-cycle`; whether a mutual dependency of two parts meets any rule of WAY-299 besides the import test I did not find stated (the task's answer to question 4 accepts it).

## Open questions with proposed answers

- Concern 1: may the plan name items 17 to 23 as entries of the foundation step? Proposed: yes, by `foundation_step.md` ("each entry a reviewed spec or the plan names"); alternative, a split of the cycle's rule that bars a slice from naming `foundations/decisions.md` — not available in the size script.
- Concern 4: one evidence line for the blocked draft. Proposed: keep; the surface `project-plan-state-command` promises its proposals, observations and exit codes and an added line breaks none.
