# Handoff — slice 7

The person who requested this cycle delegated its intermediate choices to the orchestrator; no answer
here is that person's approval. You never ask the human: a question goes back to the orchestrator in
your report.

- Worktree (work only from its root): `the task's worktree root`, branch `task/cycle-technology-decisions-batch`. This is the-way itself; there is no pinned process.
- Your method and variant: `make-change` — read `task-cycle/change/SKILL.md` whole; your variant is **a slice, or the retry of a slice**, so read `task-cycle/change/slice.md` when the method sends you there. Read `agent-instructions/README.md` too.
- Stage and boundary: slice 7 of `.runs/task-cycles/cycle-technology-decisions-batch/plan.md` only. Change only the files of the slice's *Change* line; commit them with `git add <path>` (no `git add -A`); commit messages in English. Run the slice's *Checks* yourself (focused; never the full `python -B gate/run_tests.py` without a directory). The slice's *Model* sets your class.
- Frozen task (read whole): `.runs/task-cycles/cycle-technology-decisions-batch/task.md` (Polish). Plan: `.runs/task-cycles/cycle-technology-decisions-batch/plan.md` (your slice section is copied below word for word; the plan's *Foundation entries* and *Choices* are in the plan). No spec.
- Foundation entries already written in this cycle (commits `85c5395` .. `f3b90d5` on this branch, in `foundations/decisions.md`; the report is `.runs/task-cycles/cycle-technology-decisions-batch/reports/02-foundation-entries-report.md`): read the plan's *Foundation entries* table, then read the decisions your slice depends on in their current text. Row 1 is the **new decision WAY-322** (current range in the list below if your slice reads it); it covers every matter of an agent's way to the running product that the step lists — the base holds a fifth matter beyond the task's four, the place of the screenshots — and the failure notice; word your files to agree with it. WAY-165, WAY-166 and WAY-139 were reworded in place.
- Answers of step 4: trust boundary — no file of this slice is named as a trust boundary (the change as a whole touches one, in slice 3); irreversible operation — no.
- **Drift:** the task's line numbers and the plan's cite older commits; find each place by its content. Where the current text of a place already says what the item asks, change nothing there and say so in your report.
- Report path: `.runs/task-cycles/cycle-technology-decisions-batch/reports/10-slice-7-report.md` (full report as the method gives it, with the own-work check, **Searches not found or unclear**, reaches beyond this handoff, and each check with its command and exit code).
- Return: status, your commits, a one-line check result naming what failed or did not run, and the report path.

## The slice (plan section, word for word)

### Slice 7 — Two files named settle.md, and the order of step 2 of find-foundation-entries

- **Goal:** (item 14) the two files named `settle.md` — the technology step's `project-level/technology/settle.md` and the critique's `elements/common/critique/settle.md` — no longer share a name: the critique's file is renamed with `git mv` to `elements/common/critique/settle_review.md` and the one place that names it, the last section of `elements/common/critique/SKILL.md`, names the new file; the technology step's file and the references to it stay. (item 26) in `elements/common/skill/build_table.md` the rule that a settlement an entry read in step 1 already states is no candidate stands before the table is written and shown, so that such a candidate is excluded first, as `task_variant.md` and `definition_variant.md` (the lines that write and show the table) expect; the rule that a candidate which collides with such an entry is shown beside it stays. Skill entry points do not change (no description of a skill changes); run `python -B agent-instructions/skill_entry_points.py` without `--write` and expect it to report no change. Prose and one rename.
- **Change:** `elements/common/critique/settle.md` · `elements/common/critique/settle_review.md` · `elements/common/critique/SKILL.md` · `elements/common/skill/build_table.md`
- **Read:** `.runs/task-cycles/cycle-technology-decisions-batch/task.md:50-50` To do, item 14 · `.runs/task-cycles/cycle-technology-decisions-batch/task.md:71-71` To do, item 26 · `project-level/technology/SKILL.md:56-62` 2. Settle the open choices · `elements/common/skill/SKILL.md` · `elements/common/skill/task_variant.md` · `elements/common/skill/definition_variant.md` · `foundations/decisions.md:2668-2707` WAY-115 · `foundations/decisions.md:2799-2826` WAY-120 · `foundations/decisions.md:3445-3540` WAY-134 · `foundations/decisions.md:7704-7814` WAY-256 · `foundations/decisions.md:8042-8069` WAY-265
- **Model:** cheaper
- **Risk:** none
- **Checks:** `python -B agent-instructions/skill_entry_points.py` (expects no change reported) · `python -B gate/run_tests.py elements/common` · `python -B gate/run_tests.py agent-instructions` · `python -B elements/common/foundation_check.py --skip-test-citations` · `git diff --check`
- **Depends on:** none

## Passages the slice reads

#### Task passage: To do, item 14 (task.md:50-50)

```text
14. Jeden z dwóch plików `settle.md` — kroku technologii albo krytyki (`elements/common/critique/settle.md`) — dostaje inną nazwę, tak że agent kroku technologii, czytając w krytyce „the author reads `settle.md` beside this skill”, nie otworzy swojego pliku (theway#059-3; `elements/common/critique/SKILL.md:37`).
```

#### Task passage: To do, item 26 (task.md:71-71)

```text
26. Krok 2 find-foundation-entries wyłącza kandydata, którego wpis z kroku 1 już ustala, zanim tabela zostanie zapisana i pokazana (theway#032-6; `elements/common/skill/build_table.md:12-15` po `:3`; pokazanie tabeli w `task_variant.md:31` i `definition_variant.md:27-28`).
```

## Entries and files the slice reads, with current ranges

- `project-level/technology/SKILL.md:56-62` 2. Settle the open choices
- `elements/common/skill/SKILL.md`
- `elements/common/skill/task_variant.md`
- `elements/common/skill/definition_variant.md`
- `foundations/decisions.md:2671-2710` WAY-115 (current range)
- `foundations/decisions.md:2802-2829` WAY-120 (current range)
- `foundations/decisions.md:3449-3544` WAY-134 (current range)
- `foundations/decisions.md:7752-7862` WAY-256 (current range)
- `foundations/decisions.md:8090-8117` WAY-265 (current range)
