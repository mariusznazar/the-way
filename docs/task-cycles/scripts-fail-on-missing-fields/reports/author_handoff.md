# Handoff — the one author of the change

Delegation: the person who requested this cycle delegated every intermediate choice to the
orchestrator; your questions go to the orchestrator, never to the human. Nothing here is the human's
approval.

Worktree (work only here, from its root): `the task's worktree (the repository's root)`
Branch: `task/scripts-fail-on-missing-fields`; base commit `e9a0f926dc9758f6554e8c0a30925d3e4d68cfed`.
Process: the-way itself, no pin; the-way's own skills are the project skills `the-way-<name>`.

Method and variant: read `task-cycle/change/SKILL.md` of this worktree whole (the entry point is
`.claude/skills/the-way-make-change/SKILL.md`). Your variant is "the whole change as the one author".
Read a file the method names only when the step or variant that names it comes. Also read
`agent-instructions/README.md` (the-way's own rules of a change, which apply here).

Stage and boundary: you make the whole change — the foundation step with its code (there is no
code; the change is one foundation entry) — and return before review. You run no review, do not run
the product's gate (`gate/run_tests.py` is the orchestrator's); run
`python -B elements/common/foundation_check.py` (or the invocation the record-decision skill and
`agent-instructions/README.md` give) as your own check and report its command and exit code.
For the foundation step read `task-cycle/skill/foundation_step.md` whole, and the skill of the
element — `.claude/skills/the-way-record-decision/SKILL.md` — when you write the decision. The
return step is a later stage; do not take it.

Task (frozen, read whole; copy of the task document): `docs/task-cycles/scripts-fail-on-missing-fields/task_frozen.md`
— read from its line `# Skrypty the way sprawdzają dane wejściowe…` on; the part above it is the
author's backlog note. Its *Settlements to record* rows 1–4 are the decision's content; its
*Questions to settle* give the answers and the *Not chosen* ways, which belong in the decision's
*Rejected*. *Out of scope*: review and repair of existing scripts.

Answers of step 4 (recorded in the cycle record):
- Trust boundary: no (the change is one entry in `foundations/decisions.md`, part `decisions`).
- Irreversible operation: no.
- Open design choice: none. Reserved choice: none. Route: one author, no plan, no spec.

What to read (selected by "Reading the foundation", `elements/common/way_of_working.md`):
- decisions by identifier: WAY-328 (the entry beside which the new one stands; its *Scope* list and
  its sentence that a new part joins the *Scope* is the pattern to follow), WAY-38, WAY-217,
  WAY-173, WAY-12, WAY-294, WAY-51; plus any other decision your WAY-33 search of the foundation
  finds;
- invariants `script-language`, `script-imports`, `script-subprocesses` in `foundations/invariants.md`
  (the family the new rule belongs to; the task says no invariant is written);
- `foundations/part_map.md` whole (16 parts, the *Scope* must list every one); `foundations/glossary.md`
  whole;
- `task-cycle/skill/SKILL.md` line 502 (exit code 2 reading), `task-cycle/remarks_check.py` and
  `task-cycle/request_check.py` as the two scripts the exit-code rule is judged against (read-only).

Boundary notes: the decision claims nothing about existing scripts. Do not edit scripts, tests,
skills or the part map unless the WAY-33 search finds an entry that the new decision makes false —
then correct it in the same change and name it in the report. Write the decision in English like the
other entries; quotes from the task stay as given.

Report: write the full report to
`docs/task-cycles/scripts-fail-on-missing-fields/reports/author_report.md`
as the method gives it, with the sections **Unread material** and **Searches not found or unclear**
(each `none` where empty) and your own-work check with command and exit code. Commit the work on
the branch (path-based `git add`). Return: status, commits, a one-line check result, the report
path, questions and concerns.
