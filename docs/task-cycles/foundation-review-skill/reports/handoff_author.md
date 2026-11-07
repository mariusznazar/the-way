# Handoff: the one author — foundation-review-skill

**Stage and variant:** `make-change`, variant **the whole change as the one author**. You make the
whole change of the task, including its foundation entries (the foundation step), and return before
review. You do not run the product's full gate (the orchestrator does), and you do not start the
next stage.

**Delegation.** The user (Mariusz) asked the orchestrator to run this task's cycle and has delegated
intermediate choices to the orchestrator. Questions go to the orchestrator in your report with the
status `questions`; none of them is the human's approval.

**Worktree:** `C:\Storage\repos\the-way\.runs\worktrees\foundation-review-skill` (branch
`task/foundation-review-skill`, base `86cc21e876f27f5d7d3ffd811ba11b687ac04cc6`, target branch
`foundations`). Work from its root. This is the-way itself; there is no `.the-way` pin, so every
method is read from this worktree. Write only inside it. Never edit another worktree or the
checkout `C:\Storage\repos\the-way`.

**Method:** read `task-cycle/change/SKILL.md` whole, and a file it names only when the step or
variant that names it comes. For your foundation entries, read `task-cycle/skill/foundation_step.md`
whole when you get to that step (it is the foundation step of the cycle), and the skill of an
element when you write an entry of it (`the-way-record-decision` etc., by the path of its
`SKILL.md`).

**Task (frozen):** `C:\Storage\repos\the-way\.runs\worktrees\foundation-review-skill\.runs\task-cycles\foundation-review-skill\frozen_task.md`
— read it whole. It is in Polish; the repository is in English, so the skill and the entries you
write are English, and the task's quotes keep the meaning, not the language. It is the one source:
where it is silent, the gap is an open question for your report, not something to fill from what you
know. Its *Settlements to record* rows 1–7 are the entries you write (decisions); WAY-24 changes as
its *To do* point 3 and *Decisions in play* say.

**Answers of step 4 (the orchestrator's):**
- Trust boundary: no.
- Irreversible operation: no. The cycle creates no tag; the skill you write creates one only when a
  human runs it later.
- Open design choice: none. How to make what the task settles is yours: which part of the part map
  holds the skill's files (an existing part, or a new one if the part map's rules call for it —
  record it through `the-way-update-part-map`), how the skill's text is split into files, whether
  the reminder's count is a small script with a test or text for the orchestrator, the wording of
  the new decisions. Name each such choice in your report.
- Human action 2 of the task (moving the "nośnik" of row L7 in `mapa_artykulow.md`) is the human's
  at the merge. Do not touch files outside the repository.

**Foundation entries to read whole (by identifier, each whole in `foundations/decisions.md`):** the
task's *Decisions in play*: WAY-24, WAY-37, WAY-11, WAY-14, WAY-120, WAY-140, WAY-215, WAY-82,
WAY-161, WAY-289. The decisions whose *Scope* names `task-cycle`, `elements-common` or
`agent-instructions` are listed in
`docs/task-cycles/foundation-review-skill/reports/selected_decisions.txt` (in the worktree);
read those that bear on the request's description, the cycle's end and the skill entry points, not
all of them. Read the part-map entries of the parts you touch and the invariants whose *Part* names
them or `every`. Read the glossary entry of each term you use. The-way has no guidelines of its own
(the task's *Context*), so no guideline file is named.

**Other files to read:**
- `agent-instructions/README.md` (how a change to the-way is made and checked).
- `elements/common/critique/SKILL.md` — the skill the review skill hands its set to.
- Skills for shape: `task-cycle/skill/SKILL.md` (and the files it names at its steps 12–13),
  `task-cycle/skill/request_template.md` and `task-cycle/request_check.py` — the reminder lives in
  the request's description; check whether the template and the check need a place for it.
- The shape of what the skill hands over (task *To do* 1, question 12): the first review's data file
  `C:\Storage\The Brain\The Brain\Notes\Projects\(P) Proces pracy nad produktem\przeglad_fundamentu_dane\uwagi_z_pr_2026-11-06.md`
  and the list of the predictions of reviews
  `C:\Storage\The Brain\The Brain\Notes\Projects\(P) Proces pracy nad produktem\odchudzanie_radykalne_dane\przewidywania_review_when.md`
  — read them for the form only. The repository may be public: nothing of those files, no title of a
  private note and no personal data goes into what you commit.
- The codified rules for artifacts: `C:\Storage\The Brain\The Brain\.ai\rules\knowledge_artifacts.md`
  (skills, decisions and playbooks describe the current state, not the way to it) and
  `C:\Storage\The Brain\The Brain\.ai\rules\git.md` (commit messages in English; `git add` by
  paths, never `-A`/`.`/`commit -a`).

**What follows the skill (mechanical):** a change that adds a skill runs
`python -B agent-instructions/skill_entry_points.py --write` and commits what it writes. The gate's
tests report a skill a session would not see.

**Checks you run:** focused tests of the directories you change (`python -B gate/run_tests.py
<directory>`), `python -B elements/common/foundation_check.py` on the foundation if you edit it, and
your own-work check. Each check in your report with its command and exit code. Do not run the whole
gate: it takes about 16 minutes and the orchestrator runs it.

**Report:** write the full report to
`C:\Storage\repos\the-way\.runs\worktrees\foundation-review-skill\.runs\task-cycles\foundation-review-skill\reports\author_report.md`
as `make-change` gives it, with its **Searches not found or unclear** section (`none` is an
answer) and the own-work check. Return the status, your commits, a one-line check result, and the
report path.
