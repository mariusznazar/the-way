# Word counts of lead-project

Cut from `reports/author-report.md`, section 5.

## 5. Word counts (`wc -w`, LC_ALL=C, made after the last change of a counted file)

Before: `a3206c1`. After: the worktree at `08e70be` (the skill files last changed in `08e70be`). Files read next to the skill in step 0 (unchanged by this task): `plan/template.md` 1855 (`57795e4`: 1855), `task/template.md` 2213 (2213), `lead/conversation_template.md` 1419 (`57795e4`: **1421**), `lead/answering.md` 775 (775), `way_of_working.md:20–38` 204 (204), `:52–91` 496 (496), `reading_definition_and_plan.md` 291 (291); together 7253 at `a3206c1` and 7255 at `57795e4`.

Skill files after: `SKILL.md` 2044, `route_changes.md` 176, `definition_change.md` 271, `task_return.md` 246, `technology_run.md` 129; together 2866 against 2580 before (+286). The estimate of the task was +170 to +370.

| Route | Skill text before | Skill text after (files read) | Change | With the step-0 files, before | With the step-0 files, after | Change |
|---|---|---|---|---|---|---|
| 1. steps 0–5, definition change and gate (SKILL.md + route_changes + definition_change) | 2580 | 2491 | -89 (-3.4%) | 9833 | 9746 | -87 (-0.9%) |
| 2. steps 0–5, plan change only (SKILL.md + route_changes) | 2580 | 2220 | -360 (-14.0%) | 9833 | 9475 | -358 (-3.6%) |
| 3. no step 5 (SKILL.md) | 2580 | 2044 | -536 (-20.8%) | 9833 | 9299 | -534 (-5.4%) |
| 4. return of a task, then steps 0–5 with a plan change (SKILL.md + task_return + route_changes) | 2580 | 2466 | -114 (-4.4%) | 9833 | 9721 | -112 (-1.1%) |
| 5. a round with a technology run, then steps 0–5 with a plan change (SKILL.md + technology_run + route_changes) | 2580 | 2349 | -231 (-9.0%) | 9833 | 9604 | -229 (-2.3%) |
| 6. a critic or refiner sent to the definition-change route (SKILL.md + route_changes + definition_change) | 2580 | 2491 | -89 (-3.4%) | 9833 | 9746 | -87 (-0.9%) |

The `before` skill text is the whole of `SKILL.md` at `a3206c1`, 2580 words, on every route. Route 6 counts the whole `SKILL.md` and the two files its pointers name; a critic that opens only the part named in its order reads less on both sides, and the step-0 files are read by the orchestrator, not by that critic, so the right-hand columns of route 6 are given because the task asks for two numbers on each route. The task's own estimates for the skill text (1: 2400–2550, 2: 2050–2250, 3: 1950–2100, 4: 2300–2500, 5: 2150–2350, 6: 2400–2550) all contain the measured number.

Where the new text lies: pointers in `SKILL.md` 174 words (step 0: 5, step 1: 53, 3.1: 33, 3.3: 22, step 5: 61); the rest is titles and opening lines of the four files. Moved out of `SKILL.md`: the return of a task 211 (the 29 words of the `fetch --prune` rule stay), the technology run 67 + 42, step 5 151 + 241 (+ the heading 7, which stays).

### Where `57795e4` differs from `a3206c1` for these files

- `project-level/lead/skill/SKILL.md` 2580 → 2581 (+1): lines 130–134 (3.3) read `its message on the choices` for `its table of choices`; the line numbers are unchanged. The table quotes `a3206c1`; the moved sentence in `technology_run.md` follows `57795e4`.
- `project-level/lead/conversation_template.md` 1419 → 1421 (+2): the field `Technology run` reads `the message on the choices with their consequences` for `the table of choices`. The side sum changes 7253 → 7255; `project-level/task/template.md` changed three lines and its count did not.
- `foundations/decisions.md` differs (WAY-123 and others); the line numbers of the log moved by about 30, as noted in section 1.

### Numbers of the task checked against the files

Agree with the files: `SKILL.md` 2580 words; `:61–77` 240; `:113–118` 67; `:189–219` 399 (it counts the heading at `:189`); the seven side files 7253 together (the task notes that the 7261 of the earlier question counted the headings of the following sections). Discrepancies: (1) the count of Codex files in *Context*: 37 stated, 31 found; (2) the task calls the lines `:7605`, `:7609` and `:7634` of the log sentences that contradict row 1: the first two do (the measure is the instructions in play, not the words; the shape with each step's guidance in a file beside it) and are reworded, while `:7634` (moving one-instruction fragments is rejected) does not contradict it and stays. Not checked, because they are no counts of the files: the 19 agents and the 2.4 million tokens of *Need* and *Context*.

