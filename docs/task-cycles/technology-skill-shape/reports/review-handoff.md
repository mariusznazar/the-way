# Whole-change review handoff

The user invoked the-way-implement-task and delegated intermediate stages; the human reviews the request. You made none of this change. Read-only: edit no tracked file; write only your report. Do not read `cycle.md`. Questions go to the orchestrator.

- Worktree: `C:/Storage/repos/the-way/.runs/worktrees/technology-skill-shape`; run every command there.
- Method: `task-cycle/review/SKILL.md` in this worktree; read it whole, and a file it names when the step or variant that names it comes. Stage: the review of the whole change.
- First, as the user's own instructions require before a review: `C:\Storage\The Brain\The Brain\Notes\Areas\(A) Claude code\playbook_code_review.md`.
- Range: `525cde1dd53c474f56ea0ece289cb60e868aa90d..c2e70f9` (one commit; `git rev-parse c2e70f9` gives the full name). Seven Markdown files under `project-level/technology/`, +203 -132.
- Frozen task, read whole: `.runs/task-cycles/technology-skill-shape/task.md`. No spec, no plan: one author. No slice had a review of its own.
- Author's report: `.runs/task-cycles/technology-skill-shape/reports/author.md`, with `reports/assessment.md` and `reports/word-counts.md` beside it. These two are required outcomes of the task (To do 4, 5, 6) and go into the request: review them as part of the change. The author's own check scripts and outputs are under `.runs/task-cycles/technology-skill-shape/checks/`.
- Your report: `.runs/task-cycles/technology-skill-shape/reports/review.md`.

Answers of step 4: trust boundary no; irreversible operation no; no open design choice at start; one author, class cheaper, model sonnet. Select your own foundation and guidelines by the parts of the change. Read `agent-instructions/README.md`. Guidelines selection is empty under the task's question 6 (the-way has no `guidelines/`; Markdown only).

Evidence the orchestrator's mechanical check found, as information:

- Clean worktree; non-empty range; only Markdown; every line of the seven files LF; author address private.
- Stale figures in `author.md` and its short return: `research.md` is given as 446 words and `close.md` as 102, and the research route's saving as 1676. The files at `c2e70f9` hold 467 and 96 words, and `reports/word-counts.md` gives 467, 96 and -1655, which match the files. `reports/word-counts.md` is what goes into the request.
- The author's report says it did not read as files the environment facts and the glossary its handoff named. Whatever that affects is yours to judge.

The full gate is the orchestrator's: do not run `python -B gate/run_tests.py` over all directories. Focused checks as your method calls for, each with its exact command and exit code.

What a review of a move cannot take on trust, and the author's checks were written by the author:

- Check independently of `checks/preservation.py` that no rule of the old `SKILL.md` was lost or changed in meaning, the 20 rewordings included, apart from To do 2 and 3. The 9 changes of person in `research.md` and every gloss added there count as rewordings.
- Each acceptance criterion by name, against what each reader actually reads on each of the five routes, including a file read by its path with no entry point. The task's criteria 2, 3 and 4 are about reach, not about the presence of text somewhere in the directory.
- Whether every pointer's condition is one an agent recognises, and whether the division obeys WAY-256 as worded: each file beside the skill more than one instruction, and no fragment of one instruction moved out; no fragment needed by every step moved out.
- Whether the literal quotations and line ranges of `assessment.md` match `525cde1`, every non-blank line belongs to a row, and every row shows both answers WAY-257 asks for.
- Whether the counts of `word-counts.md` follow To do 4 and 5, each route's file list being what that route's reader is really told to read, recount included.
- Whether To do 6's proposals stand as proposals, unapplied, and whether the author's claim of 387 words against the task's "ok. 800" holds.

Grade and scope are yours alone; Minor and out-of-scope findings go to the request word for word. Complete the report as your method gives it, first line `PASS <sha>`, `FAIL <sha>` or `questions`, with **Searches not found or unclear** (`none` where none). Short return: the report's first line, a one-line check result naming what failed or did not run, the report's path. Do not push and do not publish anything.
