# Handoff — the one author (`make-change`, "the whole change as the one author")

Delegation: the person who requested this cycle delegated intermediate choices to the orchestrator;
nothing below is that person's approval of an entry.

Worktree (work from its root, edit nothing outside it):
`C:\Storage\repos\the-way\.runs\worktrees\merge-review-questions`, branch `task/merge-review-questions`,
base `52889bc700123b50258c4201835034f0529351df`. Do not run `python -B gate/run_tests.py` (the
orchestrator runs the gate); run only focused checks you need, e.g. `python -B gate/run_tests.py task-cycle`
and `python -B elements/common/foundation_check.py` as its usage gives, if the foundation changes.

Method: `task-cycle/change/SKILL.md` of this worktree, variant "the whole change as the one author".
Read it whole; read a file it names only when the step that names it comes. The foundation step is
`task-cycle/skill/foundation_step.md` — read it whole; read the skill of an element
(`elements/decisions/` / `.claude/skills/the-way-record-decision/SKILL.md`) when you write a decision.

Frozen task (read whole): `C:\Storage\repos\the-way\.runs\worktrees\merge-review-questions\.runs\task-cycles\merge-review-questions\task.md`
(source path in `cycle.md` is not for you; the task is in Polish, its quoted replacement text is English).
No spec, no plan: the task's *To do* 1–4 give the exact wording. The step-12 sentence is now at
`task-cycle/skill/SKILL.md:415-418` (the task cites 389-391); the other four targets are where the task
says. Apply the wording of *To do* word for word.

Answers of step 4: trust boundary — no; irreversible operation — no; open design choice — none.

Foundation entries the task carries: both rows of *Settlements to record* (kind: decision). Write
each whole through the pinned `record-decision` skill; its meaning is the row's, its wording is yours
(WAY-134). Where the search of the whole foundation (WAY-33) finds the settlement already stated, tie
the row to that entry instead of writing a second one, and say so in the report. Where the rule is
better carried as an addition to an existing decision (e.g. WAY-162, WAY-135, WAY-150), the skill's
rules for changing a decision decide; name your choice and why in the report. A decision's
*Rejected* takes the ways not chosen that the row's source keeps (they stand in the row and in the
task's *Context*). The next free decision identifier is WAY-306 (last: WAY-305).

Foundation entries to read whole (by identifier, in `foundations/decisions.md`): WAY-01, WAY-11,
WAY-30, WAY-33, WAY-36, WAY-95, WAY-104, WAY-114, WAY-125, WAY-134, WAY-135, WAY-136, WAY-148,
WAY-150, WAY-161, WAY-162, WAY-293; the part-map entry of `task-cycle` (`foundations/part_map.md`);
the glossary whole (`foundations/glossary.md`) for the words you use. Guidelines: this repository has
none for the-way itself beyond `agent-instructions/README.md` (read it).

Task's *Decisions in play*: WAY-150, WAY-162, WAY-11, WAY-135.

Out of scope: `task-cycle/review/SKILL.md` stays unchanged.

If a change to a skill's description or an entry point is involved, follow `AGENTS.md` (not expected).
Commit by explicit paths (`git add <path> …`), English messages in the style of `git log`; never
`git add -A`. Do not push.

The report: write it in full to
`C:\Storage\repos\the-way\.runs\worktrees\merge-review-questions\.runs\task-cycles\merge-review-questions\reports\02-author-report.md`
as your method gives it, with each check's command and exit code, your own-work check, the foundation
entries with the marks and sentences `foundation_step.md` asks for, and the section **Searches not
found or unclear** (`none` is an answer). Return status, commits, a one-line check result, and the
report path.
