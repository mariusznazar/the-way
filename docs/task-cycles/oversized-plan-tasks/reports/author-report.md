# Author report: oversized-plan-tasks

**Status:** done (the orchestrator answered the three questions; see Answers received)

**Commits:** `0ed5ad7` Judge task size in the project plan critique, not by a script; `44c1d99` Name the size judgment in the plan template's critique paragraph (branch `task/oversized-plan-tasks`, base `5a24ac9`).

## Answers received

- Q1 (template echo): yes. Done in `44c1d99`, see below.
- Q2 (`plan_check.py` docstring): leave untouched. Done; not changed.
- Q3 (third *Rejected* item, author splits after the critique's remark): keep. Done; kept.

## Files changed

| File | Added | Removed |
|---|---|---|
| `project-level/plan/skill/cut_tasks.md` | 7 | 2 |
| `project-level/plan/skill/critique_plan.md` | 7 | 6 |
| `foundations/decisions.md` (entry WAY-146 only) | 28 | 5 |

Added in `44c1d99`:

| File | Added | Removed |
|---|---|---|
| `project-level/plan/template.md` (paragraph "The plan's independent critique judges…", lines 184–189) | 4 | 2 |

The clause is the decision's size test in its binding-sentence words: a task is too large when its goal joins two or more effects that can each be checked alone in the running product and merged before the others. Nothing else in the paragraph changed.

No code and no tests changed. The edits are prose of the plan skill and one decision entry, so no test was written first.

## What changed

1. `cut_tasks.md`, first bullet (task To do 1): the size test is stated (a task is too large when its goal joins two or more effects, each checkable alone in the running product and mergeable before the others). A task that gathers clearly more open questions, projected entries or In scope items is only a signal, with no number. "A large task is split" became "a task too large is split", and the author never splits for size alone; the critique judges size and the human settles any split (WAY-146).
2. `critique_plan.md`, "Ask it to judge" bullet (To do 2): the critic also judges each task's size by the test in `cut_tasks.md`.
3. `critique_plan.md`, "Verify each observation" bullet (To do 3): a split the critique asks for because of size goes to the human as a question before the plan is handed over, with the split and the choice to keep the task.
4. `decisions.md`, WAY-146, edited in place (WAY-07): binding sentences (still 3), Verification (one complies and one violates example in words, no link to private notes), Rationale (size sentences), Rejected (threshold; per-task count printout; author splitting after the critique's remark). The entry has no version and no new number.

Settlements to record: both rows are settled by this one edit of WAY-146, so there is no new entry.
- row 1 (EN): a task is too large by a test of its goal, with no numeric threshold in a script. (PL: zadanie jest za duże wg testu celu, bez progu liczbowego w skrypcie.)
- row 2 (EN): the author never splits a task for size alone; a size split goes to the human with the choice to keep the task. (PL: autor planu nie dzieli zadania sam z powodu wielkości; podział idzie do człowieka z wariantem zostawienia.)

## Checks run

After `44c1d99`:
- `python -B elements/common/foundation_check.py` (repo root): exit 0, "0 errors".
- `python -B -m unittest discover -s project-level -p "test_*.py"`: exit 0, 275 tests, OK. Output in `a file in the session's scratchpad, not kept`.

Earlier, after `0ed5ad7`:
- `python -B elements/common/foundation_check.py`: exit 0, "0 errors".
- `python -B -m unittest discover -s project-level -p "test_*.py"`: exit 0, 275 tests, OK (output `...\scratchpad\ut_project_level.txt`).
- Private-reference scan of the commit: `git show 0ed5ad7 | grep -i -n "loop2\|mariusz\|notatk\|brain\|prywat"`: exit 0, one hit, the author line of the commit header (git metadata, not text). No private reference in the diff.

Not run:
- `python -B project-level/plan_check.py <plan>`: no plan file was in the change; plan_check.py is not touched (task Out of scope). A check on the task document was attempted and not completed; it is not a valid check and I do not report it.
- `instruction-files/check_instructions.py`: not run. I judged the edited files as product skill prose outside its checked kinds; this is unverified.
- The gate (`gate/run_tests.py`): the orchestrator's, not run per handoff.

## Own-work check (section 3)

- Requirement most likely missed: that the new size clause reaches every place the critic or the author reads it, and that no statement in the entry contradicts another. Check: read the three files after the edit for the size clause, and for any "large task is split" or "A check a script can make" conflict. Result: the clause is in cut_tasks (bullet 1), critique_plan (two bullets) and WAY-146 (binding, Rationale, Verification, Rejected); the old "A large task is split" wording is gone from cut_tasks; no contradiction found with WAY-13 ("size serves only as a signal to split"), WAY-120 (author verifies each observation), WAY-143 or WAY-145.
- Requirement: the entry's Rationale and Rejected name no file, script or count (template rule). Check: read the edited Rejected and Rationale. Result: no file name; the threshold is "one third" (a rejected option, not a count of foundation entries); the one count (eight of fourteen questions) is in Verification as the decision's example, which the template allows.

## Reaches beyond the dispatch (section 1)

- `elements/decisions/skill/SKILL.md`, `read.md`, `decide_entry.md`, `template.md`, `elements/common/rules.md`, `elements/common/way_of_working.md`: to write the decision (handoff gave a wrong path, `elements/decisions/SKILL.md`; the real one is `elements/decisions/skill/SKILL.md`).
- `project-level/plan/template.md` lines 170–190 and `project-level/plan_check.py` lines 40–50: read to find stale echoes of WAY-146 (see Problems).
- `instruction-files/changing.md`: read to see whether the instruction-files method applies to editing a skill file. It concerns the human's judgement in mode change; not applied.
- Decision entries at `foundations/decisions.md` ~4396 (a decision that derives from WAY-146, about plan reading, heading not read) and ~6962–7002 (a decision deriving from WAY-144 and WAY-146, about collisions): read as WAY-33 search finds, for conflicts with the size rule. No conflict.

## Unread material

- `foundations/decisions.md`: only the entry WAY-146 and the reads listed above. WAY-13: read to "Size does tell how much" (line ~440); its tail not read. WAY-33: read to line ~909; its tail not read. WAY-143: read to line ~4090; its tail not read. WAY-07, WAY-27, WAY-120: read whole.
- `foundations/invariants.md` project-plan-form and project-plan-check: read whole. Not changed: both are tests and neither judges size.
- `foundations/part_map.md` project-level entry: read whole.
- `elements/decisions/examples.md`: not read (the way_of_working step 1 names it). Not needed for a prose edit of an existing entry, but unread.
- `elements/common/critique/SKILL.md`, `elements/common/projected_mode.md`, `project-level/plan/skill/SKILL.md`: not read; not needed (projected mode is not in this change; the critique step is `critique_plan.md`, read whole).
- `task-cycle/skill/foundation_step.md`, `cut_tasks.md`, `critique_plan.md`, `task.md`, `task-cycle/change/SKILL.md`: read whole.

## Searches not found or unclear

- The handoff's decisions SKILL.md path (`elements/decisions/SKILL.md`): not found there; found at `elements/decisions/skill/SKILL.md`.
- WAY-33 search for WAY-146 references (grep over the repo): found `foundations/decisions.md` (the WAY-146 entry itself and the two derived entries above), `foundations/invariants.md` lines 238 and 257 (derives from WAY-146; tests; no change needed), `project-level/definition_template.md` line 98, `project-level/plan/skill/critique_plan.md` line 8, `project-level/plan/template.md` lines 6, 123, 181, 187, 188, `project-level/plan_check.py` line 2.
- Search for "too large", "large task", "tells apart": the other hits concern slices (WAY-?? slice size), audit counts or unrelated "large task" senses; none touches plan tasks.
- Unclear: whether WAY-146 should gain a *Relations* link to WAY-13 (the size signal). I did not add one; the field is a closed list of two types and WAY-13 is not a higher decision it serves in the strict sense. The cost is small.

## Choices made

1. Rejected holds a third item beyond the two named in To do 4: the author splitting a task after the critique's remark (the not-chosen way of settlement row 2, under the answer to question 3). The template requires the ways not chosen that each row's source keeps, and row 2's source is question 3. Cost if wrong: one extra item in Rejected; it can be struck.
2. `cut_tasks.md` bullet changed beyond the literal To do 1 wording: "A large task is split" would contradict question 3 (the author does not split for size), so it became "A task too large is split ... the author never splits a task for its size alone". Cost if wrong: a reader of cut_tasks sees a rule the decision does not carry; low.
3. Verification example uses the decision's example in words, with the count "eight of the fourteen open questions" from the loop2 case, as the task asks. It is a count of a plan's questions, not of the foundation. Cost: none expected; the rule against counts applies to Rationale and Rejected.
4. Relations unchanged (see Searches).

## Problems and open questions

None open. The three questions were answered (see Answers received). Resolved in `44c1d99`: the template echo, which the orchestrator approved. Left as is: the `plan_check.py` docstring (answer 2); its list of what the check judges nothing about omits size, which is still true. The critic is still guided by `critique_plan.md`, so the effect is small, but the template now misstates the critique. Recommendation: add one clause naming the size test to that paragraph (a one-line edit of a product file, not named in the task). Cost of leaving it: the plan's author reads a template that omits the new judgment; it stays wrong until someone edits it. Should I make that edit in this cycle?
Struck (already answered): the old docstring item: the list of what the check judges nothing about omits size. The docstring is still true (the check does not judge size), only incomplete. The task says plan_check.py is not touched; I left it. Recommendation: leave it, or fold it into the same edit as question 1 with the orchestrator's consent.
Struck (already answered): question 3 of the Rejected list; the third item is kept (Q3 answer).

No commit was pushed; the branch is local. Working tree is clean after the commit.
