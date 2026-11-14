# Author report: task `resolve-gaps-two-meanings`

**Status:** done

## Commits

- `9c66ee1` Make the refinement of a task ask about a word its sources leave readable in two ways (branch `task/resolve-gaps-two-meanings`, base `f4af75d`)

## Files changed

- `project-level/task/skill/resolve_gaps.md` +17 -0: a paragraph "Look also for a word that can be read two ways (WAY-374)" after the first paragraph (To do items 1-4 and question 4's dictionary role).
- `project-level/task/skill/SKILL.md` +2 -2: section "## 3. Resolve the gaps" lists the check beside the questions and choices (To do item 5). The `description` is unchanged, so no entry-point regeneration.
- `foundations/decisions.md` +64 -0: the new entry WAY-374 (row 1).

## Foundation entry written

- **WAY-374**, mark `row 1`, kind decision, *Scope* `project-level`, *Relations* `derives from WAY-100`, *Based on* `none`, *Origin* `none`.
  - English: At the step that resolves the gaps, the refinement of a task asks the human which reading holds where a word of the task document or of the sentences its result rests on allows two readings that give different observable results inside the task's scope and no approved source settles it, and it says nothing where it finds no such word.
  - Polish: Przy kroku "Resolve the gaps" doprecyzowanie zadania pyta człowieka, który odczyt obowiązuje, gdy słowo z dokumentu zadania albo ze zdań, na których stoi wynik, dopuszcza dwa odczyty dające różny obserwowalny wynik w zakresie zadania, a żadne zatwierdzone źródło go nie rozstrzyga; gdy takiego słowa nie znajdzie, nic o tym nie mówi.
- Search of the whole foundation (WAY-33), once: for the course (`10xDEVS`, `10x-plan`, `m2l2`) and for the words two readings, two meanings, ambiguity, probe in `foundations/`. Found no entry that states this adoption: WAY-100 states only the rule that a borrowed practice binds through a decision; WAY-99 and WAY-95 concern the glossary and the renaming of a word, not a question in refinement; WAY-273, WAY-280 and the entry near line 8842 are adoptions of other lessons (the models for the form, which names the course and lesson in *Rationale* with *Based on* `none`). So row 1 became a new entry, not a tie.
- Collisions: none. WAY-113, WAY-95, WAY-99, WAY-118 are named by identifier in the binding sentences or *Rationale* and their meaning is unchanged.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` — exit 0, `0 errors` (run after the entry, and again after the last edit).
- `python -B gate/run_tests.py project-level` — exit 0 (275 tests OK).
- `python -B gate/run_tests.py elements/common` — exit 0 (201 tests OK).
- `python -B gate/run_tests.py instruction-files` — exit 0 (104 tests, 5 skipped).
- `python -B gate/run_tests.py agent-instructions` — exit 0 (25 tests OK).
- `python -B instruction-files/check_instructions.py .` — `0 error, 0 warn, 3 info`.
- Not run: `gate/run_tests.py task-cycle` (no file of `task-cycle/` touched), the whole gate (the orchestrator's).
- No test written first and no invariant test: the change is prose in two instruction files and one decision; no test cites the sentences changed (searched `test_*.py` for `refine-task`, `resolve_gaps`, `task/skill` and the sentences changed: no hit).

## Own-work check (section 3)

- Requirement most likely not met: the task's boundary against widening — the check must not add the trial of a list (card D8), must not leak private notes or counts into the repository, and the decision's *Rejected* must hold only the ways of the row's source (questions 1-4).
- Check: grep of the diff for `D8|trial|loop2|mapa|usprawnien|register|\.md\]\]`, exit 1 (no hit). Read of the entry against the task's *Questions to settle*: each *Rejected* item is a *Not chosen* of question 1, 2, 3 or 4; question 5's ways (wait for the trial, run the trial now) are left out, as it is out of the row's source and of scope. The *Rationale* says the plain words (a word read two ways reaches the code and shows only at review of the request or after it) without a path or a count.
- Result: no hit; the *Rejected* matches.

## Reaches beyond the dispatch

- `elements/decisions/template.md`, `elements/decisions/skill/read.md`, `decide_entry.md`, `elements/common/rules.md`, `elements/common/way_of_working.md` — read whole as `elements/decisions/skill/SKILL.md` names them (not a reach: the handoff names the skill).
- WAY-134 was named in the handoff; WAY-373 and WAY-372 (the last two entries of the log) read as the nearest examples of the present form; WAY-273 and WAY-280 (and the lines near 8842) read as models of an adoption from the course. Reason: form of an entry and of a citation of the course.
- `instruction-files/SKILL.md`, `writing.md`, `kind_skill.md`, `changing.md` read whole (the handoff names `instruction-files/`). I did not read `tool_loading.md`, `judging.md`, `placing.md`, `kind_main_file.md`, `kind_path_rule.md`: the change is a paragraph in a skill step file, not a judgement, a placement of a rule or a main file.

## Files read and left alone

`project-level/task/skill/carry_foundation.md`, `find_settlements.md`, `project_plan_task.md`, `orchestrated_mode.md` (a question already goes through the conversation file; no change needed), `project-level/technology/task_run.md` (passage near the WAY-118 line), `project-level/task/template.md` (*Questions to settle* rule, lines 128-155; it already holds the answer, the ways not chosen and the provenance). The glossary, WAY-95, the skill's `description` and the task template are not changed. Other places listing what the step does: `project-level/task/deployment_skill_guide.md` mentions only the deployment check in `resolve_gaps.md`; left alone, not read whole.

## Working copies

None made; `.runs/author/` not created. A temporary output file under `.runs/` made during the test runs was removed.

## Choices (way rejected, cost if wrong)

- *Based on* `none`, the course named in *Rationale*: following WAY-273 and WAY-280. Rejected: `TODO — the passage of the lesson word for word and the date read`, because the repository holds no passage of the course word for word and the task's *Context* gives only a paraphrase. Cost if wrong: the reviewer or the human wants a quoted passage, which needs the course's text.
- *Relations* `derives from WAY-100` only; WAY-113, WAY-95, WAY-99, WAY-118 stand in the text by identifier. Rejected: relations to each of them (a relation is for a higher decision this one serves). Cost if wrong: a link added later.
- The check's paragraph stands after the first paragraph of `resolve_gaps.md`, before the conflict paragraph. Rejected: after the paragraph on the approved definition (it refers to that paragraph, so it needed to come before it).
- The check paragraph names WAY-374 and refers to "the paragraph below on that definition" and to step 5 for the glossary candidate; it does not name `find_settlements.md` by file, since step 5 of `SKILL.md` already points to it.

## Unread material

- Whole foundation entries read whole: WAY-33, 95, 99, 100, 113, 114, 118, 134, 150, 313, 314, 315. Of WAY-134 I read lines 3700-3779 (the entry's rationale continues past that range; I did not read its last lines of *Rejected*). Of WAY-150 I read to the first lines of the *Rationale*'s end (4503-4562) and not the rest of *Rationale*/*Rejected*. The step 2-3 selection of "Reading the foundation" (decisions whose *Scope* names `project-level`, invariants whose *Part* names it or `every`) was not made in full: this change adds one decision and prose, and the whole-foundation search (WAY-33) found no collision; no invariant of `invariants.md` was read.
- `foundations/glossary.md` read whole; `foundations/part_map.md` read only its head and the `project-level` part (lines 77-92), not whole.
- `product-guidelines/reading.md`: not read (the-way has no `guidelines/` directory).

## Searches not found or unclear

- A passage of the course (lesson m2l2, `10x-plan` step 1.1.4) quoted word for word: not found in the repository; the task's *Context* holds a paraphrase and the private notes it cites are outside the repository. The decision therefore names the practice in words and carries no quotation (see *Based on* above).
- `elements/decisions/examples.md` names only WAY-03; I took WAY-372 and WAY-373 as the nearest form.

## Problems as observed

None. One thing to note for the orchestrator: the glossary candidate road (WAY-95, `find_settlements.md`) is described in the check as "step 5 finds it"; I verified that `find_settlements.md` takes the task document and the conversation as its source and has rows of kind glossary term (WAY-134), but did not run it.
