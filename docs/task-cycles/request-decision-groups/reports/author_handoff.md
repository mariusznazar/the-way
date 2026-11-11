# Handoff — the one author, whole change

You are the one author of one change in a the-way task cycle. The person who requested the cycle has
delegated intermediate choices to the orchestrator; no answer here is that person's approval. You do
not start another stage, do not seek human approval and do not run the product's gate (the
orchestrator runs it).

- **Worktree (work only here, from its root):** `the repository's root (the task's worktree)`, branch `task/request-decision-groups`, base `e3825a82386a61930a86f8517fc0c5f422fc2833`. Commit to this branch, by explicit paths (`git add <path>…`, never `git add -A`, `.` or `commit -a`); commit messages in English. Never force-push; do not push.
- **Method:** this is the-way itself (no `.the-way` submodule). Your method is the project skill `the-way-make-change`, whose method file is `task-cycle/change/SKILL.md` in the worktree; read it whole, and each file it names only when the step or variant that names it comes. Your variant, in the words of its row: **"the whole change as the one author"**. Where the method names another skill, use this repository's project skill with the `the-way-` prefix (e.g. `the-way-record-decision`, entry `.claude/skills/the-way-record-decision/SKILL.md`, method `elements/decisions/skill/SKILL.md`).
- **Foundation step:** you also do the cycle's foundation step with your code: read `task-cycle/skill/foundation_step.md` whole and follow it; read the skill of an element (here: decisions) when you write an entry of that element. The task's *Settlements to record* (below) are what it carries.
- **Frozen task (read it whole):** `docs/task-cycles/request-decision-groups/task_frozen.md`. It is the whole requirement; do not widen it. No spec and no plan exist.
- **Report path (write your full report here, in the form your method gives):** `docs/task-cycles/request-decision-groups/reports/author_report.md`. The report has the sections your method requires, including **Unread material**, **Searches not found or unclear** and your own-work check. Every check you name carries its command and exit code.

## Answers of the orchestrator at start

- Trust boundary: no. Irreversible operation: no.
- Open design choice: none. Reserved choice: none. Route: one author without a plan. Your class: `same` as the orchestrator's.
- Checks already failing on the base: the orchestrator's base run of `python -B gate/run_tests.py` is still running while you start; its result will be sent to you if it shows a failing check. You run focused tests only: `python -B gate/run_tests.py task-cycle` (and `elements/common` or the directory a test you touch lives in). The whole gate is the orchestrator's.
- A new test file in a new directory runs only after `git add`.

## What you read (selected by the orchestrator)

- **Decisions, each whole:** WAY-286, WAY-287, WAY-288, WAY-289, WAY-290, WAY-291, WAY-292 (these are at `foundations/decisions.md`, from line 9017), WAY-114 (line 2625), WAY-161, WAY-162, WAY-295, WAY-150, WAY-33, WAY-36. Edit an existing decision in place (WAY-07). Task *Decisions in play* names WAY-287, WAY-289, WAY-286, WAY-290, WAY-114, WAY-288.
- **Invariants (whole, `foundations/invariants.md`):** `foundation-file-kinds`, `foundation-change-merge-route`, `return-step-record`, `derived-file-content`, `tracked-file-private-paths`, `script-language`, `script-imports`, `script-subprocesses`, `test-method-citation`, `cross-part-imports`, and any other whose *Part* names `task-cycle` or `every` that your own selection by "Reading the foundation" in `elements/common/way_of_working.md` adds.
- **Part map:** the entries `task-cycle` and `decisions` of `foundations/part_map.md`.
- **Files the change edits, whole:** `task-cycle/skill/request_template.md`, `task-cycle/request_check.py`, `task-cycle/test_request_check.py`, `task-cycle/skill/correction.md`, `task-cycle/skill/SKILL.md` (the lines that name items of the section: "item 12" near line 563; read the whole step that holds each).
- **Glossary:** read the terms the template uses where the glossary holds them.
- There are no `guidelines/` in the-way. Read `agent-instructions/README.md` for how the-way is changed (checks, request form).

## What the change must do

Carry out every item of the frozen task's *To do* 1–8 and settle *Settlements to record* rows 1–5:

- rows 1 and 2 → edit WAY-287 (three groups with criteria; headings; `none` per group and for the whole section; continuous numbering; the items of the group "You accept by merging" wait for no separate answer);
- row 3 → a decision of its own (what an item in which the human chooses carries, and that the agent writing the description checks it before publication); write it with the decisions skill (`elements/decisions/skill/SKILL.md`, its template `elements/decisions/template.md`);
- row 4 → edit WAY-289 (the answer "fix in this request" for items 4, 9 and 14, not only for review findings);
- row 5 → edit WAY-290 (the list of what the script checks includes the group headings; the ban on judging content stays).

Numbers in the task's *To do* 2 refer to the numbered kinds of items in `request_template.md` lines 170-247 at base `e3825a8`; re-read those lines to map them before editing, and keep every reference by number (`correction.md` "item 8", `SKILL.md` "item 12", the template's "item 4" at item 13) pointing at the same kind of item after the change — numbering is continuous through the groups, so renumbering is only allowed if the kind keeps its number or every reference is corrected in the same change.

Wording: the template is written in English; the groups' headings are `### Needed from you`, `### Fix or let through`, `### You accept by merging`; the block in the task's language (the Polish ones are in the task's *To do* 1) stands translated like every heading of the top part. Plain words in anything meant for the human; no names of process steps.

Tests: `task-cycle/test_request_check.py` gets tests for the new check (a section with `none` alone passes; three headings in order each with content or `none` pass; missing, reordered, a fourth, text before the first heading, empty group each fail; the block in the task's language is not checked for group headings); every test cites what its method requires (`invariant: <id>` lines where the invariants you read require them). Update the docstring of `request_check.py` (WAY-290 description) and any example description file its tests or the template contain, so that the template's own example passes the check.

Return before review: commit your work (code and foundation entries together or in the order you judge), leave the worktree clean, and return status, commits, one-line check result, report path, questions and reach beyond this handoff.
