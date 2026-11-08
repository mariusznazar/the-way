# Handoff — the one author, `make-change`

Variant of the method: **"the whole change as the one author"**.

## Delegation

The person who requested this cycle delegated intermediate choices to the orchestrator. Nothing you
are told here is that person's approval. The cycle has one human contact, the pull request; you ask
no one for design or review answers. A question you cannot settle goes back to the orchestrator in
your report with status `questions` or `blocked`.

## Where to work

- Worktree (work only here): `the root of the task's worktree`
- Branch: `task/technology-choices-as-text`, base `a3206c17932cac9bc6ac33ecfe026a2a50fbe9d5` (target branch `foundations`)
- Method: read `task-cycle/change/SKILL.md` of this worktree whole; read a file it names (beside it or elsewhere) only when the step or variant that names it comes.
- Repository rules for the-way: `agent-instructions/README.md` (read it; it governs commits, the gate and the return step of the-way itself). Commit by explicit paths (`git add <path> ...`), never `git add -A`/`.`/`-a`. Commit messages in English. Do not push.
- Do not run the full gate (`python -B gate/run_tests.py`); the orchestrator runs it. Run focused checks only (`python -B gate/run_tests.py <directory>`, `python -B elements/common/foundation_check.py ...` as the repository documents it).

## Task

The frozen task: `.runs/task-cycles/technology-choices-as-text/task_frozen.md` (read it whole; it is in Polish — keep the sentences it gives word for word, they are English quotations).
Required outcome: its *To do* points 1–5, with its *Questions to settle* 1–3 as already settled, and its *Settlements to record* rows 1–3 written as entries by the foundation step.

Answers to the two questions at start: trust boundary — no; irreversible operation — no. No spec, no plan, no reserved choice.

### Stale line numbers (orchestrator's finding C1)

The task cites lines "@ 52889bc". Files under `project-level/**` are unchanged since then, so their numbers hold. `foundations/decisions.md` grew by 349 lines, so its numbers moved (WAY-123 now begins at line 2901). Find every site in `decisions.md` by decision heading and by the quoted words, not by the task's numbers.

### Foundation entries to read (by identifier, each whole, from heading to next `###`)

`foundations/decisions.md`: WAY-123, WAY-138, WAY-113, WAY-120, WAY-165, WAY-267, WAY-268, WAY-137 (the task asks you to judge whether its "table of consequences" is what the human gets or a comparison in a report), WAY-114 (WAY-123 prevails over it). Beyond these, select by "Reading the foundation" in `elements/common/way_of_working.md` for the parts `project-level` and `decisions`.
The files the foundation step and the return step name: `task-cycle/skill/foundation_step.md`; `task-cycle/skill/return_step.md` is the orchestrator's for the return step later, not yours now.
Write the decision entries through the pinned skill `elements/decisions/skill/SKILL.md` (and its template), as the foundation step says.

No product guidelines apply: the-way's own repository has no `guidelines/` directory (checked by the orchestrator).

### What the task asks, in one place

1. `project-level/technology/settle.md`: replace the sentence beginning "Then show the wave together, in one table:" with the text the task gives under point 1.
2. `settle.md`: in the sentence where a fresh agent looks, before showing, for contradictions between choices, add what point 2 gives.
3. WAY-123 in `foundations/decisions.md`: "in one table" → "in one message", "in separate tables" → "in separate messages", and *Rejected* "the tables come one choice at a time" reworded without "table". The meaning of an accepted decision changes: say so in your report so the request puts it before the human.
4. The other sites where "table" names what the human receives become "message" — the files and decisions the task lists. Leave alone the ordinary tables it lists (reserved_choices questions table, WAY-268's questions table, working table of `start.md` and `definition_template.md`, the marker table of `definition_template.md`). Where a site is ambiguous (WAY-137, others you find with your own search), decide by what the sentence is about — what the human receives, or a comparison inside a report — and record each ambiguous site and your decision in your report. Search the whole of `project-level/` and `foundations/` for further sites the task did not list, and name them in the report as found by your search; change them only if they plainly name what the human receives.
5. `project-level/technology/task_run.md`: the sentence about the list and the interjection "whatever `list.md` says of the matter it settles", as point 5 gives them word for word.

Settlements to record (task rows 1–3): write each whole as a decision entry or as the change of an existing decision, per `foundation_step.md`. The task's third column of each row names what the cycle would otherwise guess — your search settles it; where you tie a row to an existing entry (WAY-123, WAY-165, WAY-267 …), say which and why. Rationale and *Rejected* of WAY-123 take the form of text, the rejected table, the table with a plain paragraph beneath, and the rule "tool name only where it carries a consequence", as row 1 says; row 2 (the check by a fresh agent, which sees only the first message) and variant A of question 2 as the row says; row 3 as the row says. Do not widen beyond the rows.

### Source discipline

The task is the only authority for what the decisions say. Where it is silent, write `unknown`/`none considered` as the decisions' template gives, or return `questions`; do not fill from memory.

## Report

Write the full report to `docs/task-cycles/technology-choices-as-text/reports/author_report.md`. Return its status, commits, a one-line check result, the report's path, your questions and concerns, and the section **Searches not found or unclear** (`none` is an answer; a missing section is not). The report holds: each check with its command and exit code; the own-work check; for each foundation entry one sentence of its meaning in English and one in Polish, marked `row <n>`, `projected` or `the cycle's`; the list of changed sites and the ambiguous ones with your decision; the weakest-point check the method asks.
