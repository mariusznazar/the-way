# Handoff — review of the whole change (review-change), task `glossary-three-questions`

## Delegation

You review the whole change of one the-way task as an agent that did not make it. The person who
requested this cycle has delegated intermediate choices to the orchestrator. You grade and scope
yourself; nothing in this handoff calls a finding wrong, Minor or out of scope. Do not seek human
approval, do not dispatch subagents, do not change the reviewed worktree, its index or branch.

## Where

- Worktree to read: `C:\Storage\repos\the-way\.runs\worktrees\glossary-three-questions` (the-way itself; the process root).
- Range: base `61c72fb6347649a9bd61a71f0d2695f2e91e8b6a` .. head `24e092c` (confirm `git rev-parse HEAD`; the full sha is what `git rev-parse 24e092c` prints). Compute the diff yourself: `git diff 61c72fb..24e092c`, `git log 61c72fb..24e092c`.
- If a check needs files changed, run it in a separate worktree of the head commit under the system temp directory, never in the reviewed worktree.

## Method and variant

Method: `task-cycle/review/SKILL.md` of this worktree — read it whole. Variant: **the review of the whole change**. When the method tells you to, read `task-cycle/review/whole_change.md`. You alone select your own foundation and guidelines (the parts the change touches: `decisions`, `glossary`, `task-cycle`, and `elements-common` for `elements/common/way_of_working.md`; the-way keeps no `guidelines/`), by "Reading the foundation" in `elements/common/way_of_working.md`, each entry whole.

## What you are given

- The frozen task, whole: `docs/task-cycles/glossary-three-questions/task.md` (copy of the accepted task document; *Settlements to record* rows 1–5 and *To do* 1–5 are the requirements; the answers under *Questions to settle* are the human's and are settled). No spec, no plan: one author, no slices.
- The author's report (a set of claims to verify, not evidence): `docs/task-cycles/glossary-three-questions/reports/author.md`. It names placement choices (a)–(f), the files it changed beyond the task's list (WAY-11, `elements/common/way_of_working.md`, `elements/glossary/skill/decide_entry.md`, `task-cycle/record_template.md`, `task-cycle/skill/return_step.md`) with its reason, and what it left alone (WAY-240 and the like). Judge each against the task and the foundation.
- Answers of the orchestrator at start: trust boundary — no; irreversible operation — no; open design choice — none; reserved choice — none; route — one author without a plan.
- Orchestrator's reading of one ambiguous instruction, recorded as an answer for you to check against the task: in *To do* 2 "z powodem, dla którego jego koszt jest teraz do przyjęcia" means the cost of the variant "reported as a warning rather than an error".
- The foundation entries the change writes or changes: WAY-11, WAY-95, WAY-97, WAY-99, WAY-104 and the new WAY-293 in `foundations/decisions.md` (read each whole at the head). Per the grading rule WAY-263, compare what the entries say with the change's other files and with the task's rows.
- No check outputs are given: the full gate is the orchestrator's run (step 10). The author ran `elements/common/foundation_check.py .` and `gate/run_tests.py` on `task-cycle` and `elements/common`, exit 0 each — verify what you need yourself; do not repeat the full suite.

## What to check besides the method's own sections

- Coverage of every *To do* item (1–5) and every settlement row (1–5), item by item, with where each lies in the diff; source fidelity — the *Answer* texts of the task against the wording of the entries (WAY-134, "Dyscyplina źródła": nothing added that the task does not settle, nothing the task settled left out), including the *Rejected* lists, which take the ways not chosen from the task and a reason the task commands.
- That the test of 1b and of question 2 works in both directions and only on sentences the files already hold, in each place it stands.
- That WAY-263's text and its paragraph are untouched, that the WAY-99 renaming finding is still graded as before, and that WAY-293's rule fits the grading rules of `task-cycle/review/SKILL.md` section 3 and WAY-161.
- Leftover places stating the old rule: grep the repository (outside `.runs`, `.claude`, `.agents`) for the old phrases and for every mention of WAY-95/97/99/104/161/263/293.
- The decisions' form (`elements/decisions/template.md`), the identifiers and references (`python -B elements/common/foundation_check.py .` in a separate worktree of the head), and the task's *Out of scope* (no product's foundation touched).

## Report

Write the full report to:
`docs/task-cycles/glossary-three-questions/reports/review-1.md`
in the form `task-cycle/review/SKILL.md` section 4 gives (first line `PASS <head sha>` or `FAIL <head sha>`; findings by grade with place, reasoning and evidence; Declined to judge; checks with command and exit code; reaches beyond the dispatch; **Searches not found or unclear**). Return to the orchestrator only the first line, the counts of blocking, Minor and out-of-scope findings, and the report path.
