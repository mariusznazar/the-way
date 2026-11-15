# Handoff — correction 1, for the human's remarks on the request

You are the one author, resumed, for a correction after the review of the request (WAY-289). The
person who owns the task answered the request through the day's advisor, who acts for them; the
remarks bind. Nothing you or the orchestrator say is that person's approval.

- Worktree: `.` (the root of the repository; your working directory), branch
  `task/cycle-after-foundation-review`, head `bd50b60` (the commits `6727b67` and `cfda61e` carry the
  change; `d6cc543` and `bd50b60` add and remove the record's copy; the target branch `foundations`
  has not moved from `739c813`, so no merge came in).
- Method: `task-cycle/change/SKILL.md`, variant **"a correction for the human's remarks"**; read
  what it names for it. The foundation step: read `task-cycle/skill/foundation_step.md` whole, and the
  `SKILL.md` of the decisions element at the path it gives, since you change a decision.
- The remarks, word for word: `.runs/task-cycles/cycle-after-foundation-review/reports/correction-1-remarks.md`.
  Remark 1 binds this correction: write down which of two decisions prevails — for a screenshot
  shown to the human, the rule that keeps it where the product's foundation settles it
  (WAY-316) prevails over WAY-373, and WAY-373 keeps its reach over every other screenshot and every
  copy made to check something — in the foundation's own form for one rule narrowing another, as WAY-25
  and the decisions template ask (the remark leaves open whether that is the relation on the
  narrowing rule or an exception in WAY-373: take the form they ask for, and name in your report the
  passages that settle it). Remark 2 (the missing source of WAY-138 let through) asks for no change: do
  not touch WAY-138.
- The frozen task: `.runs/task-cycles/cycle-after-foundation-review/task.md` (the correction does not
  widen it: it carries out only the remark). The request is
  `.runs/task-cycles/cycle-after-foundation-review/request.md` and its item 1 of *Fix or let through* is
  what the remark answers; the reviewer's words on the finding stand in
  `.runs/task-cycles/cycle-after-foundation-review/reports/review-whole-report.md`, Minor 3.
- What to read whole: in `foundations/decisions.md` WAY-25, WAY-316 and WAY-373 (each from its `###`
  heading to the next heading), and any decision that names either of them in *Relations* or
  *Verification*; the decisions template and rules the element's skill names; `task-cycle/change/ui_check.md`
  and the first paragraph of "Working copies" in `task-cycle/skill/SKILL.md` (the exception for a
  screenshot shown to the human that this change added, which must stay true beside the new entry).
  The invariants whose *Part* is `every` or `task-cycle`, and the glossary, as in your first dispatch.
- Do the search of the foundation once for the entries the changed entry touches (WAY-33) and correct
  them in this correction: for example whether WAY-373's *Rejected* or the skill's paragraph needs a
  word to agree; do not widen beyond what the remark and that search require. Two decisions that
  narrow each other are an error: check that none narrows WAY-316 and that WAY-373 narrows nothing.
- Run again the checks the correction affects: `python -B elements/common/foundation_check.py` (full,
  without `--skip-test-citations`), and `python -B gate/run_tests.py` for the directories your
  change reaches (at least `elements/common` and `task-cycle`; `agent-instructions` if a file it checks
  changes), each with command and exit code. Do not run the whole gate (`python -B gate/run_tests.py`
  without a directory): it is the orchestrator's run.
- Commit by path; lines within 100 columns; no absolute path in a file of the repository;
  leave the worktree clean. The record is the orchestrator's; do not touch `docs/` or `.runs/task-cycles/`
  other than writing your report.
- Agent directory for working copies: `.runs/author/`.
- Report path: `.runs/task-cycles/cycle-after-foundation-review/reports/author-correction-1-report.md`.
  It holds each remark as made and how it was carried out, the foundation entry you wrote or changed
  with its meaning sentence and its mark, the checks with command and exit code, the own-work check,
  reaches, **Unread material**, **Searches not found or unclear**, working copies.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
in the system's temporary directory, in the scratch directory of a session or in the main checkout
of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by
itself under its session's directory is moved into the agent's directory and the original removed.
The files that a product's own tools and tests make by themselves are no working copy of the agent
and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a
worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside
its report what the report needs, and states in the report where each copy stood and that it was
removed. Where a removal fails, the agent finishes all the same and names in the report the
remainder, with its full path and the reason it stayed.
