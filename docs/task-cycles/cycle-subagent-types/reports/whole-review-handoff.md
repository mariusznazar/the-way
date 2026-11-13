# Handoff — review of the whole change (cycle `cycle-subagent-types`)

You review the whole change of one task for the task cycle of the-way, as an agent that did not make it. Read-only: you change no tracked file and commit nothing.

## Where and what

- Worktree: the repository's root, the task's worktree (work from there; the process root is this worktree). Branch `task/cycle-subagent-types`.
- Method: `task-cycle/review/SKILL.md` of this worktree, read whole. Your variant: **the whole change**; read `task-cycle/review/whole_change.md` as the method says, and any other file the method names when the step that names it comes.
- Range: base `715ae20` to head `2245f08` (`git diff 715ae20..2245f08`, `git log 715ae20..2245f08`; confirm `git rev-parse HEAD` is `2245f08` first). Three commits by the one author: `07cb56a`, `1239ae2`, `2245f08`.
- Frozen task, read whole: `docs/task-cycles/cycle-subagent-types/task.md`. Its *To do* 1–6, the acceptance criterion, the four answers of *Questions to settle* and the three rows of *Settlements to record* are the standard. No spec and no plan: one author, no slices.
- The author's report (claims to verify, not evidence): `docs/task-cycles/cycle-subagent-types/reports/author-report.md`.
- Write your whole report to `docs/task-cycles/cycle-subagent-types/reports/whole-review-report.md` (its first line `PASS <sha>` or `FAIL <sha>`, or `questions`). The directory is git-ignored; never commit it.
- Do not run the product's full gate (`python -B gate/run_tests.py` with no directory): the orchestrator runs it. You may run focused checks of single directories and `python -B elements/common/foundation_check.py`. The full `installation` directory run takes about 8 minutes; the new file `installation/test_agent_types_installation.py` alone about 2 minutes.

## Answers of step 4 that bind your review

- **Trust boundary: yes.** `installation/install.py` is the part `installation`'s trust boundary (files from outside: what a product already holds in `.claude/agents/`). Check crafted input at that boundary yourself, in the review, besides reading the author's tests: a symlinked `.claude` or `.claude/agents`, a file at an owned path that is not the installer's, a directory at the file path, non-UTF-8 text, a header that names another type, a stale own file of a removed type next to the product's own agents. Where you try an input, name it and what it showed.
- **Irreversible operation: no.** The cycle never installs into a product; check that the change only prepares what it prepares.
- Open design choices: the cycle judged there was none; the author made the two *Questions carried to cycle* (source location and generator; names and wording of the two types) as choices of how to make what the task settles. Judge whether any of them is in truth an open design choice of the kind the task or a decision reserves, and whether the choices as made fit the foundation.

## Gaps of the author's selection that you carry (its report's **Unread material**)

Judge these yourself, since you select your own foundation; the orchestrator has decided nothing about them:

- `task-cycle/record_template.md` lines 130 to the end were not read by the author, which edited lines 1–129 (the *Author* line and the actor cell now speak of the agent type); check the rest of the file for any statement the new text contradicts.
- `task-cycle/review/SKILL.md`, `task-cycle/spec/SKILL.md` and `task-cycle/skill/planning.md` were read only in their first 30–40 lines, in a search for a skill named as a thing to call; the task's To do 5 asks that every method of a stage be pointed at by a file path in the pinned the-way, not by a skill name to call. Search them yourself.
- Invariants not read by the author: `foundation-file-kinds`, `foundation-change-merge-route`, `return-step-record`, `ci-checking-commands`, `map-reference-target`, `test-method-citation`, `python-version-declared`, the invariants of `project-level` and `relation-model`, `gate-exit-code`. Select by "Reading the foundation" and read those that bear on the change.
- The author did not read the last 16,972 characters of the Claude Code subagents page and the installation test files other than `test_install.py`, `test_coding_guidelines_installation.py` and its own new file.
- The author reports that the sources' conditions (the 10.5k-token figure, the cache probe's version and model) are not given in the task, and that the decisions state only what is given; check that no decision states more than the task gives (the task's own rule: a figure comes from its source, never from memory).

## What the orchestrator wants checked in particular

1. Source fidelity of the three new decisions (WAY-368, WAY-369, WAY-370) and of the edit of WAY-255, WAY-09 and WAY-34 against rows 1–3 of *Settlements to record*, the four answers with their *Not chosen*, and To do 6; a *Rejected* line must hold the ways of the row's source only, and the quotes of the documentation must be what the page says (WAY-05, WAY-27: results described in the entry, no pointer to a private note).
2. To do 5: the author kept the names `write-spec`, `plan-task`, `make-change`, `review-change` in the orchestrator's text as labels of the four method files and states the path of each at step 3; it did not replace the roughly 25 "dispatch … with `make-change`" clauses. Judge whether that fulfils "każdą metodę … wskazują ścieżką pliku … nie nazwą skilla do wywołania" for the three places the task names (`foundation_step.md`, `return_step.md`, `change/SKILL.md`) and the planner's text (`plan/SKILL.md`), and for the orchestrator's text.
3. To do 4: the instruction names, for Claude Code, the type of each stage and what the orchestrator does when the session has no such type, and writes it in the record.
4. The installer: own-file rule, REPLACE and DELETE only of its own, the preview before confirmation, `installation-command`'s part-map entry listing every file rewritten or deleted, `installation/README.md`.
5. The generator and its test of the tracked copies, the content checks of the definitions, and the part-map claim of the new files (`foundation_check.py`).
6. Privacy of what is committed: no path of the author's disk outside the repository, no private note name or title.

## Report

Return in your report and your short return: the first line (`PASS <sha>` / `FAIL <sha>` / `questions`), the changed files with added and removed line counts, your findings each with its grade (Critical, Important, Minor), whether it is outside the task's scope and, for each blocking finding, that no slice applies (one author), the coverage of every task item, every settlement row and source fidelity, the checks you ran with command and exit code, the reaches beyond this handoff, the number of decisions you read whole and by title only (WAY-150), **Unread material** (what this handoff names or you selected that stayed unread or read in part, or `none`) and **Searches not found or unclear** (or `none`). List the Minor findings within the task's scope together in one place of the report, so that the orchestrator can cut them from it.
