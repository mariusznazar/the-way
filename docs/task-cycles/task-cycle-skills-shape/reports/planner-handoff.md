# Handoff — planner, task `task-cycle-skills-shape`

You are the planner of one task's cycle on the-way itself. The person who requested this cycle has
delegated intermediate choices to the orchestrator; send your questions to the orchestrator in your
report, never to the human. Your go-ahead comes from the orchestrator and is provisional.

## Where you work

- Worktree (your working directory and the repository you plan for):
  `C:/Storage/repos/the-way-wt/task-cycle-skills-shape`, branch `task/task-cycle-skills-shape`,
  base `cf11541f039649db3a76aa5aaa2d7cce2cc48f34` (`foundations`).
- **Method:** `plan-task`, read whole from the base copy of the-way:
  `.runs/the-way-base/task-cycle/plan/SKILL.md`, with the files of the process it names, each from
  `.runs/the-way-base/` as well (for example its size script:
  `python -B .runs/the-way-base/task-cycle/slice_size.py ...`). The task requires this (its To do 7):
  every agent of this cycle reads the methods of its stage from the copy at the base commit, never
  from the task branch, because the task rebuilds those methods.
- The product's foundation, the files to change and the tests are those of the worktree
  (`foundations/`, `task-cycle/`, `instruction-files/`, `agent-instructions/`, `.claude/skills/`,
  `.agents/skills/`).
- Write `plan.md` and its size report `plan-size.md` in
  `.runs/task-cycles/task-cycle-skills-shape/`, and your full report to
  `.runs/task-cycles/task-cycle-skills-shape/reports/planner-report.md`. Write no code and commit
  nothing. Return before any slice is made.

## What you read

- The frozen task, whole: `.runs/task-cycles/task-cycle-skills-shape/task.md`. It is in Polish; write
  the plan in English, as the-way's files are, quoting the task's wording where a slice needs it.
- Its two sources, frozen beside it:
  - `.runs/task-cycles/task-cycle-skills-shape/sources/przyklad_make_change.md` — the judgment table
    of `make-change` and its layout after the rebuild (To do 5 follows it);
  - `.runs/task-cycles/task-cycle-skills-shape/sources/seria_skilli.md`, section „Ustalone” (lines
    34–63) — the settlements the series shares.
- Foundation entries, each whole (from the worktree's `foundations/`):
  - decisions the task changes or applies: WAY-125, WAY-127, WAY-256, WAY-257, WAY-258, WAY-128,
    WAY-35, WAY-148, WAY-150;
  - decisions whose *Scope* names `task-cycle`, which the rebuilt skills carry and must keep
    unchanged in meaning: WAY-13, WAY-37, WAY-135, WAY-136, WAY-158, WAY-159, WAY-160, WAY-161,
    WAY-162, WAY-163, WAY-164, WAY-220, WAY-227, WAY-229, WAY-255 — read those a slice's work needs
    and name them in that slice's *Read*;
  - WAY-33 (the search of the whole foundation once an entry is settled);
  - invariants: `skill-entry-points` (the generator's output), `derived-file-content` (cited by
    `agent-instructions/test_skill_entry_points.py:256`), `return-step-record`.
- Guidelines: none. the-way has no `guidelines/`; the task's second question under *Questions to
  settle* settles the selection as empty.

## Answers of the orchestrator's start (step 4 of `implement-task`)

- Trust boundary: no — no file the part map names as one is changed
  (`instruction-files/check_instructions.py` stays as it is).
- Irreversible operation: no. No slice is marked with either risk.
- Open design choice: none. The layout of each rebuilt skill follows from WAY-256 and WAY-257 applied
  to each fragment: a choice of how to make what the task settles, made and named by the executor
  that judges the skill.
- Route: planning — the change divides along the five skills.

## Choices of the orchestrator that bind the plan

- **C3 — carried question 1** (where the foundation step and the return step of `implement-task`
  stand): the executor that judges `implement-task` answers it by WAY-256 and WAY-257 like any
  fragment and names the answer in its table; the handoffs then name whatever file or paragraph holds
  them. Do not settle it in the plan.
- **C4 — carried question 2** (`task-cycle/record_template.md`): judged for its place only, as one
  row of `implement-task`'s table; its content is neither judged nor rebuilt. The request names it as
  not judged.
- **C5** — the five skills are judged with the base copy's `maintain-instruction-files`
  (`.runs/the-way-base/instruction-files/SKILL.md`, judging mode, kind "skill", with
  `judging.md` and `kind_skill.md` as it names them), with the exception of settlement row 3 applied
  (a fragment of a step or variant that is one instruction stays in `SKILL.md` where its pointer would
  stand), since the task settles it.
- Only "keep" and "move" verdicts and rewordings that change no meaning are carried out; "remove"
  and "reword" verdicts that change a rule's content are proposals in the report and the request,
  with no edit (task, *Questions to settle* 5).

## What the plan must cover

Every item of To do 1–7, both acceptance criteria and rows 1–3 of *Settlements to record*. Things
the orchestrator's reading found that the plan should place:

- The foundation entries (rows 1–3) are settled by the task: they are the plan's *Foundation
  entries*, written before slice 1 through the base copy's `record-decision` skill
  (`.runs/the-way-base/elements/decisions/skill/SKILL.md`) into the worktree's
  `foundations/decisions.md`. Their WAY-33 search will find, among others, `AGENTS.md:11` ("each
  reads its skill and the files it names from the checkout or worktree the session works in") and
  WAY-125's restatement in `task-cycle/skill/SKILL.md` (step 3 of "Inputs and authority" and the
  handoff paragraphs).
- The generator's sentence is `agent-instructions/skill_entry_points.py:175`; its test's assertion
  `agent-instructions/test_skill_entry_points.py:53`; after the change,
  `python -B agent-instructions/skill_entry_points.py --write` regenerates the 42 entry points, and
  `python -B agent-instructions/skill_entry_points.py` checks them. Per the acceptance criteria, no
  other Python changes.
- To do 6 needs, for each of the five skills, the judgment table (fragment, when it is needed and
  whether the agent recognises the moment, verdict) and the words each agent reads in each variant
  before and after. Each executor that rebuilds a skill writes that table and those counts in its
  report, so the request can carry them; the plan's *Checks* should require it.
- Acceptance criterion 2 — no rule disappears or changes meaning — is the weakest point of every
  rebuild slice; its *Checks* need a check that can actually run for it, which the executor names.
- `implement-task`'s handoffs name the stage methods' files; the stage skills' new layouts decide
  what those handoffs name, so order the slices accordingly.
- Choose each slice's *Model* by WAY-229 as the method gives; judging and rebuilding a skill is
  judgment, not ordinary implementation, so say why where you set a class other than `cheaper`.

Return with your status, the paths of `plan.md`, `plan-size.md` and your report, and a one-line
result of the size script with its command and exit code.
