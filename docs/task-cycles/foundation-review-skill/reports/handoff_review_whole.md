# Handoff: review of the whole change — foundation-review-skill

**Stage and variant:** `review-change`, **the whole change**. You did not make it. You are read-only:
you change nothing in the worktree. Read `task-cycle/review/SKILL.md` whole, then
`task-cycle/review/whole_change.md` as it says; other files that `SKILL.md` names, when the step
that names them comes.

**Delegation.** The user (Mariusz) asked the orchestrator for this task's cycle. Questions go to the
orchestrator as the status `questions`; the orchestrator's answers are not the human's approval.

**Worktree:** `C:\Storage\repos\the-way\.runs\worktrees\foundation-review-skill` (the-way itself; no
pin, read every method from this worktree). Branch `task/foundation-review-skill`.
**Range:** base `86cc21e876f27f5d7d3ffd811ba11b687ac04cc6` .. head `02ca017cc5e7a6176f1f921f08d6eace43cd0ffd`
(five commits, one author, no plan, no slices). Confirm `git rev-parse HEAD` is the head; compute the
diff yourself with `git diff <base>..<head>`.

**Frozen task (read whole):**
`C:\Storage\repos\the-way\.runs\worktrees\foundation-review-skill\.runs\task-cycles\foundation-review-skill\frozen_task.md`
(Polish). Check coverage of every item of its *To do* (1–3), each answer of its *Questions to settle*
that the change has to carry, every row of *Settlements to record* (1–7) and every entry of *Decisions
in play*, and source fidelity: whether what the skill, the decisions and the reminder say follows the
task, widens it, or narrows it. Ask whether anything in the change reads as a decision the task did
not take. No spec and no plan exist.

**Answers of the orchestrator's step 4:** the change touches no trust boundary of the part map; it
holds no operation that cannot be undone (the cycle puts no tag; the skill puts one only when a human
runs it later). The task's *Human actions* item 2 (the "nośnik" of row L7 in a file outside the
repository) is the human's, at the merge; it is not part of the change.

**The author's report** (a set of claims to verify, not evidence):
`C:\Storage\repos\the-way\.runs\worktrees\foundation-review-skill\.runs\task-cycles\foundation-review-skill\reports\author_report.md`.
The repository may be public: look also for anything private (a title or text of a private note, a
personal name) in what the range commits.

**You select your own foundation and guidelines** by "Reading the foundation" in
`elements/common/way_of_working.md`. The-way has no guidelines of its own. Also see
`agent-instructions/README.md` for how a change to the-way is made, and the checks it lists. The
orchestrator runs the whole gate itself after your review; you may run focused checks and
`python -B elements/common/foundation_check.py`, each with its command and exit code in your report.

**Report:** write your full report to
`C:\Storage\repos\the-way\.runs\worktrees\foundation-review-skill\.runs\task-cycles\foundation-review-skill\reports\review_whole.md`
as `review-change` gives it (first line `PASS <sha>` or `FAIL <sha>`, graded findings with the
reason in full, the checks you ran, your reaches, and **Searches not found or unclear**). Return the
first line, the path, and a one-line result.
