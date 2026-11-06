# Handoff — the one author, the whole change

You are the one author of this change. The person who requested the cycle delegated every
intermediate choice to the orchestrator; no answer here is that person's approval.

- Worktree (work only here, from its root): `C:\Storage\repos\the-way\.runs\worktrees\logging-scope-decision-section`
  on branch `task/logging-scope-decision-section`, base `61c72fb6347649a9bd61a71f0d2695f2e91e8b6a`.
  The cycle's record directory `.runs/task-cycles/logging-scope-decision-section/` is ignored by git;
  you never read `cycle.md` there and never commit anything under `.runs/`.
- Method: `task-cycle/change/SKILL.md` of this worktree. Read it whole; read a file it names only
  when the step or variant that names it comes. Your variant, in the words of its row: **"the whole
  change as the one author"**.
- Stage and boundary: make the change, do the foundation step with it, run your own-work check, commit
  and return. You do not review, run the whole gate, take the return step or open a request. Return at
  that boundary; send any question to the orchestrator in your report.
- Frozen task, read whole: `.runs/task-cycles/logging-scope-decision-section/task.md` (a copy of the
  approved task document). It has no spec and no plan.
- Report: write it to `.runs/task-cycles/logging-scope-decision-section/reports/02-author-report.md` as the method
  gives it, with every check as its command and exit code. Under **Searches not found or unclear** list
  each thing you looked for and did not find or found unclear, or `none`. Return your status, your
  commits, a one-line check result and the report path.

## Answers of the start

- Trust boundary: no. Irreversible operation: no. Open design choice: none — the task settles the way
  (A), the consent stays on the general route and M-2 is closed both in the script and in the template.
- Route: one author without a plan. Your class of model is `cheaper`.

## What the change is

The five items of the task's *To do*:
1. `task-cycle/skill/request_template.md`: a new last item in the list of *For you to decide* about
   additions to a product's logging scope; existing numbers unchanged.
2. `foundations/decisions.md`: WAY-287's list of kinds gains "additions to a product's logging scope";
   WAY-274 does not change. This is row 1 of *Settlements to record* (kind decision), accepted at the
   task document: write it by the foundation step below, whole, in its place.
3. `task-cycle/request_check.py`: a description saved with a leading UTF-8 BOM passes the state check
   as the same description without it.
4. `task-cycle/request_check.py`: a description that keeps the placeholder heading `## <…>` fails the
   check; the message says to omit the heading or to write the heading of the task's own section.
5. `task-cycle/skill/request_template.md` — the sentence under the skeleton's `## <…>` heading (lines
   101–104) says plainly that the heading is omitted where the task has no sections of its own.

Tests for 3 and 4 belong in `task-cycle/test_request_check.py`; it already pins the skeleton's headings
against the script (`TemplateTest`), so the skeleton keeps its `## <…>` line and only its sentence
changes. The script's module docstring describes what it reads and checks: bring it into line with the
change.

## Foundation step

Read `task-cycle/skill/foundation_step.md` whole, and the skill of the decisions element through
`.claude/skills/the-way-record-decision/SKILL.md` (it sends you to `elements/decisions/` and to
`elements/common/way_of_working.md`) when you write the entry. The source of row 1's *Rejected* is
the task's *Questions to settle* 1: the ways not chosen that it keeps. Return the report with, for the
entry, one sentence of its meaning in English and one in Polish, marked `row 1`. Run
`python -B elements/common/foundation_check.py` from the worktree root after writing it.

## What to read

- Foundation entries, each whole, by identifier in `foundations/decisions.md`: WAY-287 (the entry the
  change edits), WAY-274, WAY-286, WAY-288, WAY-290, WAY-291, WAY-292, WAY-10, WAY-114, WAY-134 and
  WAY-36 (what a decision carries). The part map entries of `task-cycle` and `decisions` in
  `foundations/part_map.md`. Invariants of `foundations/invariants.md` whose part is `every` and that
  touch a script or a foundation file: `script-language`, `script-imports`, `script-subprocesses`,
  `return-step-record`.
- Guidelines: the-way has no guidelines of its own for code or tests; the task document says the task
  goes on as the earlier tasks of the-way did. `agent-instructions/README.md` gives how a change to the-way is
  made and checked ("Make the change", "Check the change"): read it.
- Files: `task-cycle/request_check.py`, `task-cycle/test_request_check.py`,
  `task-cycle/skill/request_template.md`, whole.

## Checks you run

Focused only: `python -B gate/run_tests.py task-cycle` and
`python -B elements/common/foundation_check.py`. Do not run the whole gate (the orchestrator does).
Tests for the two script changes are seen failing before they pass (WAY-08 applies to invariant tests;
the same practice serves these tests — report the failing and the passing run).

## Git

Commit on the task branch, by explicit paths (`git add <file> …`, never `-A`, `.` or `commit -a`), in
English messages shaped like the repository's (`docs: …`, `fix: …`). Check
`git log --format='%h %ae'` after your first commit; the address must be the private one
(the private address or the repository's usual noreply address of the earlier commits). Do not push.
Do not touch the user's notes or any file outside the worktree. Do not rewrite the task document.
