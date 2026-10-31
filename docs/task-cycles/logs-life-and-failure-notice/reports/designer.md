# Report — designer of the spec

Status: done

Spec: `.runs/task-cycles/logs-life-and-failure-notice/spec.md`

## Questions sent and answers

None. The handoff gave the two choices to settle, and no assumption changed the design past what a
source answers. Two readings the text left open are picked and written in the spec (D6, "Two readings
picked"), so that the orchestrator can overturn either; see *Worth the orchestrator's eye* below.

## Ways weighed

**The main choice: a list written before this change (spec D1).** Chosen: an entry holds a matter of
an agent's way only where it answers everything the matter asks as the template gives it, for a
decision and a projected decision, on a new list and on one already written. A silent item ends
`— open`, with the entry nested, and the list is shown again.

- Leave `held by` and `projected` alone. Lost: the result would depend on when the list was written,
  and a silent projected decision would enter the foundation already failing the next project's look.
- A second item beside the untouched one. Lost: one matter as two choices, research bound to a
  destination that may be why the record dies, and against the task's Context.
- Reopen `held by` but not `projected`. Lost: the only entry that is still a draft would stay silent.
- Add the failure item only to a new list. Lost: two regimes, though `start.md` takes the look at
  every resume anyway.

Reading the text showed two traps in `start.md` that any reopening meets, both closed in D1: the
bullet on open items turns a reopened `projected` item straight back, and it reuses a passed report
that says nothing of the record's life.

Who may open what: at a definition the agent opens nothing held, since a silent decision does not
settle the matter under WAY-121, and the human sees the change first. The rule of `task_run.md` binds
a run at a task and has no bearing at a definition. The answer binds after the merge, and WAY-165
carries it.

**Where the look stands (D2).** Chosen: a new file, `project-level/technology/failure_notice.md`.

- A second section in `running_product.md`. Lost: its subject is an agent's way, and a reader would
  apply WAY-166, which answer 1 rules out.
- A bullet each in `list.md` and `start.md`. Lost: the criterion applied in two places, and the
  skill's pattern for a look read on its own condition broken.

**One decision or two (D3).** Chosen: one new decision that narrows WAY-121 and WAY-122, plus a
pointer in WAY-121.

- Two decisions. Lost: two entries for one question, against answer 1's wording.
- Row 3 as a fourth sentence of WAY-121. Lost: breaks the limit of three sentences and WAY-19.

## The four checks

1. Placeholder, `TBD` or empty section: none.
2. Contradiction: none found. One apparent tension is intended and explained: at a definition one
   matter stays one item (D1), while at a task a projected decision of an approved definition leaves
   the record's life as an item of its own (D6), because the note bounds a run and no run reopens such
   a decision. The binding-sentence counts of WAY-121 and WAY-165 were counted against the entries:
   three each.
3. Several independent changes: no. The logs' life, the failure item and the deployment list share
   the same decisions and files, and the rows bind them together. The size is a matter for the
   orchestrator's choice of one author or a plan.
4. Requirements readable two ways: picked and written down in D4 (the criterion while the place to run
   is open, a project that runs nothing elsewhere) and D6 (the two readings).

## Reaches beyond the dispatch

- `agent-instructions/README.md`: AGENTS.md asks it be read before starting.
- `elements/decisions/template.md`, whole: the form of the entries, the limit of three binding
  sentences, *Rejected* from a row, `narrows`.
- `elements/decisions/skill/projected.md` and `elements/common/projected_mode.md`: whether a projected
  decision can be rewritten.
- `elements/glossary/template.md` and `elements/glossary/skill/decide_entry.md`: the test of a term,
  named by the handoff through `elements/glossary/`.
- `project-level/skill/SKILL.md`, the lines on `settle-technology`: when a definition resumes the step.
- `project-level/task/template.md`, the lines on Technology: the form of a settled question.
- `project-level/readiness_check.py`, `check_technology` and `items`: that nested items pass, so no
  file of the trust boundary changes.
- `foundations/decisions.md`, the opening of WAY-07, WAY-25, WAY-30, WAY-33, WAY-112, WAY-114, WAY-118,
  WAY-134, read as search hits with 14 lines of context, not whole: the rules they set on editing,
  collisions and approval.
- `foundations/part_map.md`, lines 1–130, beyond the two entries named, as part of the same read.
- `agent-instructions/test_instruction_files.py`, search only: whether a test pins files beside a
  skill. It does not.

Not read: the source note, which no choice needed. Not opened: anything the task's restriction names.

## Searches not found or unclear

- **The task's quoted boundary phrase** ("bez dotykania kodu aplikacji", "without touching"): found
  nowhere in the repository outside this cycle. The nearest text is WAY-165 *Rejected*, which agrees
  with answer 3 (spec D8). The search's positive control: the same pattern matched WAY-165.
- **Tests pinning the step's text:** a search of every `*.py` for the step's file names and "running
  product" found only `installation/install.py:34`, which maps the skill to its `SKILL.md`.
- **"Deliberate absence", "failure" in the foundation:** no use with a meaning of its own; the one hit
  in `foundations/invariants.md:158` is a failing test. Nothing stands in the way of D9.
- **`foundations/decisions.md`, what the fifth candidate was:** the task reads "Candidates: 5 shown, 4
  accepted", and the rejected candidate is not in the task. It may be the boundary of answer 3, which
  has no row. The spec writes no entry for the boundary, which fits either way.
- **Unclear, a matter the human strikes:** `start.md` adds each matter "it finds missing" at every
  resume, so a struck item comes back. This stands today for the three matters and now also for the
  failure item. The spec leaves it, because the way to refuse the failure item is to choose a deliberate
  absence, not to strike it.

## Worth the orchestrator's eye

- **D6, a refusal closes the check, not the look.** Row 4 says "pytanie nie wraca"; row 3's criterion
  reads only the foundation. The spec reads the first as the question of the deployment check, so the
  next project of that product lists the item once. The other reading needs the look to read the
  product's deployment skill.
- **D6, the check asks nothing where a decision or an approved definition already answers.** Row 4
  says refinement asks where the skill does not say. The spec applies `resolve_gaps.md`'s first
  paragraph before that, because a run could not reopen a projected decision of an approved definition.
- **WAY-121's compliant example** of a project that "records that the foundation holds every choice it
  needs" now holds only with the failure item settled where the criterion is met. The spec hands this
  to the maker.
