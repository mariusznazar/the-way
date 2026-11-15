# Handoff — the return step after correction 1

You are the one author, resumed, for the return step that repeats after correction 1 (step 11 of
`implement-task`, repeated as `correction.md` gives). Nothing you or the orchestrator say is the
human's approval.

- Worktree: `.` (the root of the repository; your working directory), branch
  `task/cycle-after-foundation-review`, head `f92d9dd` (the correction's review returned `PASS`). The
  range the correction changed: `bd50b60..f92d9dd` (WAY-316 only: a third paragraph of binding
  sentences, `narrows WAY-373` in *Relations*, one sentence of *Rationale*). The target branch
  `foundations` stands at `739c813`.
- Stage: the return step. Read `task-cycle/skill/foundation_step.md` whole and
  `task-cycle/skill/return_step.md` whole by their paths in this worktree, and the `SKILL.md` of an
  element when you write an entry of that element.
- What to compare with the code: the entry the correction wrote (WAY-316), the entries it names
  (WAY-373, WAY-25), the entries the first return step compared that the correction could touch,
  the part map of `task-cycle`, with the files of the repository: `task-cycle/skill/SKILL.md` ("Working
  copies", first paragraph), `task-cycle/change/ui_check.md`, `task-cycle/skill/request_template.md`
  (the places that say where a screenshot lies), and the invariants `record-copy-image-check` and
  `record-copy-image-files` with their tests (WAY-316's *Verification* names them). The correction's
  review noted one Minor finding (WAY-316's *Verification* has no complies/violates line for the new
  precedence); that review finding is no foundation entry: do not write it, defer nothing, and do
  not list it for later. Correct in the same change whatever no longer matches; where nothing does,
  commit nothing.
- Do not run the whole gate (the orchestrator's run); run `python -B elements/common/foundation_check.py`
  (full, without `--skip-test-citations`) and the directory checks your correction reaches.
- Agent directory for working copies: `.runs/author/`.
- Report path: `.runs/task-cycles/cycle-after-foundation-review/reports/return-step-2-report.md`; its
  content as the record's *Return step* gives it (what was compared and what no longer matched,
  decisions written or changed, invariants, environment facts, glossary terms, part-map changes,
  projected entries, rows written), with the checks (command and exit code), reaches,
  **Unread material**, **Searches not found or unclear** and working copies.

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
