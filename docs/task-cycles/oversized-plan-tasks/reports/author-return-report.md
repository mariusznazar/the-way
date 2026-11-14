# Return step report: oversized-plan-tasks

**Status:** done (nothing needed correction)
**Commits:** none. Head stays `4e3c4cf`; the return step changed no file.
**Check:** no check run, since no file changed (the foundation check was run at `4e3c4cf`: 0 errors).

## Foundation compared with the code

Each entry the change writes or changes, the entries the task names, and the entries the search found, compared with the files of the repository at `4e3c4cf`.

- **WAY-146** (edited in place, `foundations/decisions.md`). Binding sentence, Rationale, Verification, Rejected compared with each other and with the two rows of *Settlements to record*:
  - row 1 (a task is too large by the goal test, no numeric threshold in a script): the binding sentence states the test and "no script judges a task's size"; Rejected names the threshold and the printout as ways not chosen. Agrees.
  - row 2 (a size split goes to the human, with the choice to keep the task; the author never splits for size alone): the binding sentence states it; Verification's violates example names the author splitting alone. Agrees.
  - Rationale carries the size reason; Verification's complies and violates examples use the same test. Agrees.
  - Nothing in the entry is a second entry: the two rows are settled by this one edit. Confirmed.
- **`project-level/plan/skill/cut_tasks.md`** (first bullet): "a task too large is put to the human to split", the test, the signal with no number, the author never splits for size alone. Agrees with WAY-146.
- **`project-level/plan/skill/critique_plan.md`**: the critic judges size by the test in `cut_tasks.md`; the author hands the test with the request; a size split goes to the human before hand-over. Agrees.
- **`project-level/plan/template.md`** (paragraph at lines 184–189): the critique judges size by the same test; a check a script can make is never left to the critique. Agrees.
- **WAY-13** (Decisions in play): "a task's size ... otherwise serves only as a signal to split it". The change names the human as the one who settles the split, which WAY-13 does not forbid. Consistent; no change.
- **WAY-143** (Decisions in play): not touched by the change; the criterion does not conflict. No change.
- **WAY-120** (Decisions in play): the critique gives observations, the author verifies each, and a human settlement stays with the human. The change routes size splits to the human and does not let the critic change a human settlement. Consistent; no change.
- **Entries that derive from WAY-146** found by the search (WAY-33): the decision at `foundations/decisions.md` ~4396 (the critic reads the whole plan) and the decision at ~6962–7002 (collisions, a script decides them). Neither conflicts with a size judgment by the critique. No change.
- **Invariants `project-plan-form` and `project-plan-check`** (derive from WAY-146): tests of form and of structure; neither mentions size and no script judges size. Consistent; no change.
- **`foundations/part_map.md` project-level entry**: "the breakdown ... and the check of that plan" still covers the critique's size judgment. No change.
- **`project-level/plan_check.py` docstring** (not in the change scope): its list of what the check judges nothing about omits size. The docstring stays true: the check judges no size. Left as decided (orchestrator answer 2).

## Environment facts

None. The change rests on no source outside the product: the size test and the routing come from the task's settlements, the human's answers and the foundation. Searched the foundation for a source the change uses: none new.

## Glossary terms (WAY-95)

None written. The term *preparatory task* already has an entry (`foundations/glossary.md`, "## preparatory task") and the change uses it in its existing meaning. "Too large" and "task too large" are defined inside WAY-146 and in `cut_tasks.md`; they are not terms of the field that a reader would not understand, so the glossary rule does not require an entry. This is a judgment; the orchestrator may decide otherwise.

## Invariants

None written. The task sets no invariant, and no rule of the task, a decision or the human requires one; the size judgment is a critique, not a test.

## Part-map changes

None (see the project-level entry above).

## Projected entries

None. The task is independent (*Project relation: independent*).

## Rows of *Settlements to record*

Both rows are written by the edit of WAY-146 at `44c1d99` / `0ed5ad7` (commit `0ed5ad7` made the edit; the later commits tightened wording and named the judgment in the template). No second entry. Each row marked:
- row 1: decision, written as the WAY-146 edit (`row 1`).
- row 2: decision, written as the WAY-146 edit (`row 2`).

Meaning, one sentence each:
- row 1 (EN): a task is too large by a test of its goal, with no numeric threshold in a script. (PL: zadanie jest za duże wg testu celu, bez progu liczbowego w skrypcie.)
- row 2 (EN): the author never splits a task for size alone; a size split goes to the human with the choice to keep the task. (PL: autor planu nie dzieli zadania sam z powodu wielkości; podział idzie do człowieka z wariantem zostawienia.)

## Unread material

- `foundations/decisions.md`: the WAY-146 entry is read whole; the entries derived from it are read as the search found them, in part; WAY-13, WAY-33 and WAY-143 are read in part (as recorded in the author report). The file is not read whole.
- `foundations/glossary.md`: read only the "preparatory task" entry and the grep hits; not read whole.
- `task-cycle/skill/foundation_step.md`, `task-cycle/skill/return_step.md`: read whole.
- The `SKILL.md` of an element (path in `foundation_step.md`): not read; no element entry was written or changed in this step.

## Searches not found or unclear

- Searched the glossary for "too large", "critique", "preparatory", "project plan": one hit for "preparatory task", none for the others. Unclear whether "task too large" needs an entry; decided none (see above).
- Searched the part map for "critique" and "the check of that plan": hits at lines 70 and 80, both consistent with the change.
