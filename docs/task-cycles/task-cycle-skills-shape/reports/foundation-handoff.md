# Handoff — foundation entries, task `task-cycle-skills-shape`

You write the foundation entries of a planned change, before its slice 1. The person who requested
this cycle has delegated intermediate choices to the orchestrator; send questions to the
orchestrator in your report, never to the human.

## Where you work

- Worktree, your working directory: `C:/Storage/repos/the-way-wt/task-cycle-skills-shape`, branch
  `task/task-cycle-skills-shape`, base and slice 1's base `cf11541f039649db3a76aa5aaa2d7cce2cc48f34`.
  Nothing has been committed on the branch yet.
- **Method:** `make-change`, read whole from the base copy of the-way,
  `.runs/the-way-base/task-cycle/change/SKILL.md`. Read also, whole, the paragraph of the cycle that
  holds this stage: in `.runs/the-way-base/task-cycle/skill/SKILL.md`, the paragraph opening "The
  foundation step writes the entries the task carries" (lines 259–277), and the element skill it
  names for decisions, `.runs/the-way-base/elements/decisions/skill/SKILL.md`, with the files it
  names — each from `.runs/the-way-base/`. The task requires every agent of this cycle to read the
  methods of its stage from that copy at the base commit (its To do 7), because the task rebuilds
  them.
- The foundation you write into is the worktree's: `foundations/decisions.md`, checked by
  `python -B elements/common/foundation_check.py`.
- Your report: `.runs/task-cycles/task-cycle-skills-shape/reports/foundation-report.md`.

## What you make

The plan's *Foundation entries*, copied word for word from
`.runs/task-cycles/task-cycle-skills-shape/plan.md` (lines 7–24):

> | Entry | Kind | From | What depends on it |
> |---|---|---|---|
> | 1 — a stage agent reads its method's `SKILL.md` whole and a file beside the skill only at the step or in the variant that names it (change of WAY-125) | decision (change) | *Settlements to record* row 1 | Slice 11, which writes it into step 3 of "Inputs and authority" and the handoffs of `implement-task`; Slices 7–11, whose moves gain nothing without it |
> | 2 — an entry point of a the-way skill has a file the skill names read from the same checkout or worktree when the step that names it comes, not all at the start (change of WAY-127) | decision (change) | *Settlements to record* row 2 | Slice 2 (the generator's sentence, its test, `AGENTS.md`), Slices 3–6 (the regenerated entry points) |
> | 3 — a fragment of a step or variant that is one instruction stays in `SKILL.md` where its pointer would stand, since the pointer is an instruction too (exception in WAY-256) | decision (change) | *Settlements to record* row 3 | Slice 1 (`instruction-files/kind_skill.md`), Slices 7–11 (each judgment applies it) |
>
> The three are written before slice 1, through the base copy's `record-decision`
> (`.runs/the-way-base/elements/decisions/skill/SKILL.md`), into the worktree's
> `foundations/decisions.md`. Their search of the whole foundation (WAY-33) will find, outside the
> foundation, texts that this plan's slices bring in line, not the writer: `AGENTS.md:9-11` and the
> generator's sentence (row 2) — Slice 2; `instruction-files/kind_skill.md` (row 3) — Slice 1; the
> restatement of WAY-125 in `task-cycle/skill/SKILL.md:66-70` and `:128-137` (row 1) — Slice 11. A
> finding inside the foundation (for example WAY-148, which derives from WAY-125, or WAY-258, which
> cites WAY-256) is the writer's, as WAY-33 gives. No invariant, glossary term, environment fact or
> part-map entry is written: every file the slices create lies under `task-cycle/**`, which the part
> map already assigns, and the invariant `skill-entry-points` does not change (task, *Context*).

Each row's meaning is the settlement row's in the task; the wording is yours. The task's rows are
in Polish; the entries are in English, as the log is. Change no file outside `foundations/`: the
texts outside the foundation that the search finds are the slices' work — list them in your report
with `file:line`, and any the plan above does not name.

## What you read

- The frozen task: `.runs/task-cycles/task-cycle-skills-shape/task.md` — lines 17–33 (*Need*, *To
  do*), 40–56 (*Questions to settle*, whose answers bound the rows' meaning), 58–64 (*Context*),
  75–93 (*Decisions in play*, *Settlements to record*). Its source note, for row 1's and row 3's
  wording and named risks: `.runs/task-cycles/task-cycle-skills-shape/sources/seria_skilli.md`,
  lines 37 and 61.
- Foundation entries, whole, from the worktree's `foundations/`: WAY-125, WAY-127, WAY-256 (the
  three you change); WAY-257, WAY-258, WAY-128, WAY-129, WAY-35, WAY-148, WAY-150 (linked or
  restating); invariant `skill-entry-points` (it derives from WAY-127 and must still hold — the
  task's *Context* says it does not change). `record-decision` selects any further reading the
  entries need.
- Guidelines: none — the-way has no `guidelines/` (the task's second question settles it).

## Answers of the orchestrator's start

- Trust boundary: no. Irreversible operation: no.
- No open design choice: rows 1–3 settle each entry's meaning.
- The cycle wrote no spec; the route is planned slices.

## Your boundary

Commit the entries on the task branch (one commit is enough), keep the worktree clean, and return
before any slice. Run `python -B elements/common/foundation_check.py` and `git diff --check`; report
each with its command and exit code. Do not run `gate/run_tests.py` as a whole; that run is the
orchestrator's. Your report gives, for each entry, its identifier, one sentence of its meaning in
Polish (for the request), and what the WAY-33 search found and did. A question for the human arises
only as the foundation-step paragraph names it; then return `blocked` with it.
