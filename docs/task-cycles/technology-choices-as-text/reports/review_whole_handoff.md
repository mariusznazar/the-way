# Handoff — review of the whole change, `review-change`

Variant of the method: **the whole change** (it reads `task-cycle/review/whole_change.md` when the method names it).

## Delegation

The person who requested this cycle delegated intermediate choices to the orchestrator. You are an agent that did not make the change. You are read-only: change no file, make no commit. You grade and scope your own findings.

## Where

- Worktree: `the root of the task's worktree`, branch `task/technology-choices-as-text`.
- Method: read `task-cycle/review/SKILL.md` of the worktree whole; read a file it names only when the step or variant that names it comes.
- Range: base `a3206c17932cac9bc6ac33ecfe026a2a50fbe9d5` to head `78c32c7` (one commit, 9 files). Nothing is pushed.
- Route: one author without a plan, no spec, no slices. There is no slice review; you judge the whole change.
- Frozen task (read whole; Polish, with English quotations the change must carry word for word): `.runs/task-cycles/technology-choices-as-text/task_frozen.md`.
- The author's report: `docs/task-cycles/technology-choices-as-text/reports/author.md`.

## Answers to the two questions at start

- Trust boundary: no (markdown only; none of `readiness_check.py`, `plan_check.py`, `plan_state.py` is touched).
- Irreversible operation: no.
- The task did not move a pin of the-way (it is the-way itself).

## What to check, in addition to your method

- Coverage of every item of the task's *To do* (points 1–5), of *Questions to settle* 1–3 as settled, and of *Settlements to record* rows 1–3, and source fidelity: the sentences of points 1, 2 and 5 must stand word for word; the rows' meanings must be what the entries say, with nothing added that the task does not settle (the task's dyscyplina źródła: an entry that says more than its row is invented content).
- Point 3 changes the meaning of an accepted decision (WAY-123): check that the change goes no further than "table" → "message" plus the rows' content.
- Point 4: every site where "table" names what the human receives is changed, and no ordinary table is (the task lists those to leave). The author searched `project-level/` and `foundations/decisions.md` and lists left-alone and ambiguous sites in its report; do your own search, do not rely on its list. Treat WAY-137's "table of consequences" and WAY-166 (not on the task's list) as sites to judge.
- Foundation form: the entry templates (`elements/decisions/template.md`): binding part at most three sentences, *Verification*, *Rationale*, *Rejected*; foundation search for contradictions with other entries (WAY-33) — e.g. whether other decisions or files still say "table" of the showing, or contradict the new text.
- The foundation entries you read: select by "Reading the foundation" in `elements/common/way_of_working.md` for the parts `project-level` and `decisions`, the task's *Decisions in play* included.
- Whether the commit holds only the change (no stray file).

Run no gate: the orchestrator runs it. Focused checks are yours to run as you see fit (`python -B gate/run_tests.py <directory>`, `python -B elements/common/foundation_check.py`, from the worktree root); give each with command and exit code.

## Report

Write the full report to `docs/task-cycles/technology-choices-as-text/reports/review_whole_report.md`. Its first line is `PASS <sha>` or `FAIL <sha>` (or `questions`). Return that line, the report's path, the checks you ran with commands and exit codes, and the section **Searches not found or unclear** (`none` is an answer).
