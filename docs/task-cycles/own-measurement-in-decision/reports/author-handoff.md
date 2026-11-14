# Handoff to the one author — own-measurement-in-decision

You are the one author of the whole change of this task, with no plan. The person who requested
this cycle has delegated intermediate choices to the orchestrator; nothing you are told here is the
human's approval, and you do not ask the human: questions go back to the orchestrator in your
return, with the status `questions` or `blocked`.

## Where you work

- Worktree (work from its root, commit on its branch): `the root of the task's worktree`
- Branch: `task/own-measurement-in-decision`; base commit `3c572b95e86a1a4e6b0373b7fb11c3e7c6b00ead`
  (the-way itself, target branch `foundations`; the pin is not moved).
- Method: `task-cycle/change/SKILL.md` in the worktree, variant "the whole change as the one author".
  Read it whole; read a file it names only when the step that names it comes.
- Foundation step: `task-cycle/skill/foundation_step.md` (read whole). The element skill for a
  decision is `elements/decisions/skill/SKILL.md`; for an environment fact
  `elements/environment-facts/skill/SKILL.md`. Read the element's template and
  `elements/common/rules.md` and `elements/common/way_of_working.md` as that skill gives.
- Repository rules for this change: `agent-instructions/README.md` (read it; the check of a change is
  the gate, which the orchestrator runs — you do not run `python -B gate/run_tests.py`; you may run
  the focused check `python -B elements/common/foundation_check.py --skip-test-citations` and
  `python -B gate/run_tests.py <directory>` for a directory your edit touches).
- Commits: English messages; `git add` by explicit paths, never `-A`, `.` or `commit -a`; do not push.
  Before the first commit read `the author's git rules for agents`.

## The task

The frozen task: `.runs/task-cycles/own-measurement-in-decision/task.md` (in the worktree; read it
whole). Its status is `ready for cycle`, `Project relation: independent`, no human actions.
In short: where a measurement made by the product's own people has a record the readers of this
public repository cannot open, the decision log keeps the result in the decision's rationale, with
what was measured and the conditions, says there that the measurement is its own and its record is
not open to the reader, and writes no environment fact for it. The three items of *To do*
carry that out in WAY-90, the two templates and each decision whose rationale gives such a result;
the settlements are rows 1 and 2 of *Settlements to record* (accepted), and the answer to
question 3 is WAY-33. Wording is yours (WAY-134); the meaning is the rows'.

## Answers of step 4 (orchestrator)

- Trust boundary: no (parts `decisions`, `environment-facts`, `elements-common` and files named in
  the part map carry none).
- Irreversible operation: no.
- Open design choice: none — rows 1 and 2 settle it. Reserved choice: none.
- Route: one author without a plan. Do not write a plan or a spec.

## Reconciliation since the task was accepted (orchestrator)

After the task was accepted, merged request #114 added two more places where a decision's
rationale gives the result of such a measurement of one game product, so *To do* item 3 reaches them
too — it says "each decision whose rationale gives the result of such a measurement — among them":

- WAY-371 (new) — already says its source is "not reachable from this repository"; read it as a
  model of the sentence, and make it say the same as the rule you write, if it differs.
- WAY-136 — its rationale gained a measurement of cycles of one game product (cost per changed
  line, one author against a plan).

Your search of the whole foundation (WAY-33) finds the rest; each finding becomes a change to the
entry in this change, a link or a question to the orchestrator. Do not change a decision's binding
sentence, *Scope*, *Based on* or other fields in item 3 — only the rationale gets the sentence
(WAY-229, WAY-164, WAY-364, WAY-312, WAY-371, WAY-136 and any other the search finds). Edit WAY-90
in place (WAY-07).

## What to read (selected by the orchestrator, WAY-150)

Whole, from `foundations/decisions.md` — each by the range of lines from its heading to the next
heading: WAY-90, WAY-27, WAY-05, WAY-80, WAY-33, WAY-229, WAY-164, WAY-364, WAY-312, WAY-136,
WAY-371, and the decisions whose *Scope* names `decisions` or `environment-facts` that bear on the
form of an entry, found by the search of *Scope* the skill gives. Templates: `elements/decisions/template.md`
(the point opening "*Based on* names every source outside the product", about line 44) and
`elements/environment-facts/template.md` (section "Which facts are written", the point opening "A
decision's *Based on* names a fact entry", about line 45). Invariants whose *Part* names `decisions`,
`environment-facts` or `every`. The glossary entries of the terms you use. Everything else you need
you select as the element skill's step 1 gives.

## Return

Return before review: all work committed, a clean worktree. Write your full report to
`.runs/task-cycles/own-measurement-in-decision/reports/author-report.md` as `make-change` gives it,
including: the own-work check with commands and exit codes, **Unread material**, **Searches not found
or unclear**, for each foundation entry one sentence of its meaning in English and one in Polish and
its mark (`row <n>`, `projected` or `the cycle's`), the result of the whole-foundation search of
WAY-33 (what it found and what you did with each finding), and what you took the weakest point of
the change to be and how you checked it. Return the status, your commits, a one-line check result
and the report path.
