# Handoff to the one author — decisions-list-in-refinement

You are the one author of this change, without a plan. The orchestrator of the cycle delegated the
intermediate choices to itself; none of its answers is the human's approval.

- Worktree (start from its root, write only there): `the task's worktree (the repository's root)`, branch `task/decisions-list-in-refinement`, base `9cbc6b2c46837c956f863843de0dd0bc3d32d8f1` (target branch `foundations`; the-way is the repository itself, no pin).
- Method: read `task-cycle/change/SKILL.md` whole; your variant is **"the whole change as the one author"**. Read a file the method names only when its step comes.
- Frozen task: `.runs/task-cycles/decisions-list-in-refinement/task.md` (read whole). It is in Polish; the change's texts of skills and decisions are English, as the files you edit are.
- Spec and plan: none (no open design choice; one author without a plan).
- Answers of step 4: trust boundary — no; irreversible operation — no.
- Your directory for working copies: `.runs/author/` (a working copy is made only there; remove it before each return and say so in the report).
- Report path: `.runs/task-cycles/decisions-list-in-refinement/reports/author-report.md`.

## What you do

Make the whole change of the task: its *To do* 1-8 and its two rows of *Settlements to record*
(both go to a decision), with the foundation step (`task-cycle/skill/foundation_step.md`, read it whole;
it names `elements/decisions/skill/SKILL.md` for a decision, and you read that whole when you write
a decision). Edit in place: `project-level/task/skill/final_review.md`,
`project-level/task/skill/orchestrated_mode.md`, `project-level/task/skill/SKILL.md` (section
"## 6. Review and hand off") and `foundations/decisions.md`. Read each file you change whole before
changing it. The task's *Questions to settle* are answered; its *Out of scope* binds you.

Notes from the orchestrator (checks, not restatements of the task):

- Where the new step's agents are dispatched, mind that the skill's own agent of refinement works in the
  same session as the human; the step must say who writes what file in `.runs/` of the product, as *To do* 5 states. Do not widen the task.
- `elements/common/foundation_check.py` and the tests of the foundation check the decision's form,
  the `decision:` lines of tests and the references; a new decision may need a test that holds its
  sentence (WAY-02) — judge by the decisions' skill and the tests that already hold neighbouring
  decisions; do not invent a test the method does not ask for.
- A skill's entry point, its description, or its place does not change, so `skill_entry_points.py` is not needed unless you find otherwise; say in the report what you checked.
- A skill file you change is an instruction file: read `instruction-files/SKILL.md` and, of the
  files it names, the ones its steps send you to (writing, placing, kind_skill) when the step comes.

## What you read (selected by the orchestrator; WAY-150, WAY-213)

- Foundation index of the decisions the work reaches, written by `decision_index.py`: `.runs/orchestrator/index.md` in the worktree (43 KB, 31 decisions: the sections *Task refinement and readiness*, *Accepting and applying decisions*, *How skills write and read the foundation*, *The request and the human*; the decisions whose *Scope* names the parts `project-level` and `decisions`; and WAY-374, WAY-120, WAY-113, WAY-229, WAY-100, WAY-134, WAY-124, WAY-154). Read the index. Open whole in `foundations/decisions.md` (an entry runs from its heading to the next heading of any level) those the task's *Decisions in play* names — WAY-374, WAY-120, WAY-113, WAY-229, WAY-100, WAY-134, WAY-124, WAY-154 — and each that your change goes against, answers otherwise or whose sentences leave open what you have to do.
- The invariants whose *Part* names `project-level` or `decisions` or is `every`, in `foundations/invariants.md`, and the entries they and the decisions link to, as far as your change needs them, each whole. The part map's entries for `project-level` and `decisions` (`foundations/part_map.md`).
- The glossary entries of the words you use in the new text (`foundations/glossary.md`); *gate* has two meanings in the process, so write nothing about "the gate" in the new text.
- Guidelines: the-way holds no `guidelines/` directory; there is none to read for this change.
- The orchestrator's reading of `elements/common/way_of_working.md` "Reading the foundation" is the method of selection; you select the further entries for the decisions you write as `elements/decisions/skill/SKILL.md` step 1 gives.

## Boundary

Make the change, commit it on the branch (stage by explicit paths, never `git add -A` or `.`; the
commit message is English), run the tests of the directories you change with
`python -B gate/run_tests.py <directory>` — the focused checks only, **never the whole gate** (`python
-B gate/run_tests.py` without a directory): the full run is the orchestrator's, and it waits for the
human's advisor to give a signal before it starts. Also run `python -B elements/common/foundation_check.py` and the own-work check
`task-cycle/change/SKILL.md` gives. Return at your boundary (status, commits, one-line check result,
report path). Do not start review, return step or any other stage, and do not ask the human. The
return step comes later: you are resumed for it.

## Working copies (word for word from the cycle's skill)

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
in the system's temporary directory, in the scratch directory of a session or in the main checkout
of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by
itself under its session's directory is moved into the agent's directory and the original removed,
except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md`
says, to the place the product's foundation settles for screenshots, and into the agent's directory
only where no such place is settled. The files that a product's own tools and tests make by
themselves are no working copy of the agent and stay outside this rule. Before the agent returns,
each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then
`git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in
the report where each copy stood and that it was removed. Where a removal fails, the agent finishes
all the same and names in the report the remainder, with its full path and the reason it stayed.
