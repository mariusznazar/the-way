# Handoff — the agent of the plan's *Foundation entries*

## Delegation

The person who requested this cycle (Mariusz) delegated every intermediate choice to the cycle's
orchestrator. You answer to the orchestrator, never to the human, and you ask no human.

## Where you work

- Worktree, your working directory for every command and read:
  `C:/Storage/repos/the-way/.runs/worktrees/unsettled-technology-returns`
- This is the-way working on itself; there is no `.the-way`, and the-way's files are read from this
  worktree, never from another checkout.
- Target branch `foundations`, task branch `task/unsettled-technology-returns`, slice 1's base
  `2dbf1e7`, which is the current head. Nothing else writes in this worktree while you work.
- Commit on the task branch by explicit paths (`git add <path>`, never `git add -A`, `git add .` or
  `git commit -a`). Commit messages are in English, in the form of the repository's log
  (`docs: ...`). Do not push.
- Your report: `.runs/task-cycles/unsettled-technology-returns/reports/foundation.md`

## Your stage

You are the agent of the plan's *Foundation entries*: you write the ten entries before any slice is
made. You take none of the rows of the table of variants in `make-change`; your stage is this one.
Read these files whole, in the worktree:

- `task-cycle/change/SKILL.md`, the method for how you read, commit and report;
- `task-cycle/skill/foundation_step.md`, the step you carry out.

When you write an entry, read the skill of its element whole and follow it: the project skill
`the-way-record-decision` for a decision and `the-way-record-glossary-term` for the term, in
`.claude/skills/`, each of which sends you to its source in this worktree. Your boundary: you write
entries, and you change no skill, template or test; those are the slices' work. You run no gate;
that run is the orchestrator's.

The session's global rule on knowledge artifacts applies to what you write: an entry says how things
are, with no history of attempts and no dates of events.

## What you write

Frozen task, read it whole: `.runs/task-cycles/unsettled-technology-returns/task.md`.
Reviewed spec, read it whole: `.runs/task-cycles/unsettled-technology-returns/spec.md`. Its section
*Foundation entries* names what you write, its *Decisions* carry the ways weighed, and its *Left to
the maker* leaves you each entry's wording, its *Scope*, its number and, for the entries the spec
names itself, its *Rejected* from the ways above.

The plan's *Foundation entries*, copied word for word from
`.runs/task-cycles/unsettled-technology-returns/plan.md`:

| Entry | Kind | From | What depends on it |
|---|---|---|---|
| (new) How does the step that settles technology run outside a project definition? | decision | row 1 | Slices 1, 2, 3 |
| (new) Who settles a technology choice that no decision or definition settles? | decision | row 2 | Slices 2, 4, 5 |
| (new) How does a task leave a cycle that met a reserved choice, and how does it come back? | decision | this spec | Slices 5, 6 |
| reserved choice | glossary term | this spec | Slices 1, 2, 4, 5, 6 |
| WAY-121 | decision, changed in place | row 3 | Slices 1, 2 |
| WAY-122 | decision, changed in place | row 3 | Slice 1 |
| WAY-123 | decision, changed in place | row 3 | Slice 1 |
| WAY-137 | decision, changed in place | row 3 | Slice 1 |
| WAY-138 | decision, changed in place | row 3 | Slice 1 |
| WAY-135 | decision, changed in place | row 3 | Slices 4, 5 |

The rows of *Settlements to record* are written whole, their meaning the row's and the wording
yours (WAY-134). For the decisions from rows 1 and 2, *Rejected* takes only the ways not chosen that
the row's source keeps, under the questions the row's *Source* names; `none considered` or `unknown`
as the decisions' template gives. For the third new decision and the term, which no row carries, the
meaning is the spec's and *Rejected* comes from the ways the spec gives under its decisions 2 and 5.

Three settlements of the orchestrator bind the wording, each already in the spec:

- no rule on doubt: a choice is under the rule or it is not, and the boundary rests on the agent's
  judgment with the examples;
- WAY-263 stays unchanged;
- a run reopens no choice a projected decision of an approved definition settles.

Decision 2 names what the row adopts from lesson m2l4 of 10xDEVS (WAY-100): a technical decision
that rests on a checkable source, not on the model's memory.

Where the entry names a mechanism a slice has yet to write, such as a file or a status, write it as
the spec gives it. All of it reaches the target branch in one merge (WAY-01).

## What to read of the foundation

Each of these whole, from its heading to the next heading, in `foundations/decisions.md`: WAY-01,
WAY-14, WAY-19, WAY-29, WAY-30, WAY-33, WAY-36, WAY-100, WAY-106, WAY-113, WAY-114, WAY-121, WAY-122,
WAY-123, WAY-124, WAY-134, WAY-135, WAY-136, WAY-137, WAY-138, WAY-147, WAY-153, WAY-155, WAY-165,
WAY-166, WAY-219, WAY-227. In `foundations/glossary.md` the entries `open design choice`, and in
`foundations/invariants.md` `project-technology-record`. The element's skill selects further as its
own step 1 gives. Your one search of the whole foundation (WAY-33) comes once the entries are
settled; the spec's list "Searched and left unchanged" says what its designer found, and does not
replace your search.

The-way has no directory `guidelines/`; no guideline file applies.

## What can stop you

A question goes to the human only as `task-cycle/skill/foundation_step.md` gives: return `blocked`
with it, and write no entry with another meaning. In particular, a correction your search finds that
would change an approved decision beyond what the task or the spec carries is such a question.

## Reporting

Write your full report to the path above as `make-change` gives it, with one sentence of each
entry's meaning in Polish, the document's language, for the request; your search of the whole
foundation and what it found; and **Searches not found or unclear** — each thing looked for and not
found or unclear, or `none`. Each check you name carries its command and exit code; run at least
`python -B elements/common/foundation_check.py .`.
Return your status, your commits, a one-line check result naming what failed or did not run, and
the report's path.
