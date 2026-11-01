# Handoff — one author, task `decision-heading-level`

**Delegation.** The person who requested this cycle has delegated intermediate choices to the
orchestrator. Send questions to the orchestrator; never to the human.

**Worktree.** `C:\Storage\repos\the-way\.runs\worktrees\decision-heading-level`, branch
`task/decision-heading-level`, base `2f51e6c`. Work only there. Every path below is relative to it.

**Method.** Read `task-cycle/change/SKILL.md` whole; it lies in this worktree. Your variant is "the
whole change as the one author". Read a file it names, one beside it included, only when the step
or variant that names the file comes.

**Stage and boundary.** Make the whole change, commit it and return before review. Do not start a
review, do not open a request, do not push. Do not run the full gate `gate/run_tests.py` with no
argument: its run is the orchestrator's.

**Frozen task.** `.runs/task-cycles/decision-heading-level/task.md`, read whole. It is a copy of the
task document as approved at `foundations` `2f51e6c`. Do not read other notes of the author.

**Answers of step 4.**

- Trust boundary: no. The change touches `elements/common/way_of_working.md` (part
  `elements-common`) and `task-cycle/change/SKILL.md` (part `task-cycle`); the part map names no
  trust boundary in either.
- Irreversible operation: no.
- Open design choice: none. The task gives both insertions word for word, and its *Questions to
  settle* records the human's answer that there are exactly these two.
- Foundation entries to write: none (*Settlements to record*: none).
- The skill's `description` does not change, so `agent-instructions/skill_entry_points.py` has
  nothing to write.

**Foundation to read, each whole.** WAY-150 and WAY-256 (the task's *Decisions in play*), WAY-35.
They stand in `foundations/decisions.md`, each under a `###` heading, running to the next heading.

**Guidelines.** None: this repository has no `guidelines/` directory, and the change writes no code
and no test.

**Focused checks.** `python -B elements/common/foundation_check.py .` and
`python -B gate/run_tests.py task-cycle`. Prefer the wait of `task-cycle/change/SKILL.md` section 3
for anything that may run long.

**Report path.** `.runs/task-cycles/decision-heading-level/reports/author.md`. Return your status,
your commits, a one-line check result naming what failed or did not run, and the report's path.
