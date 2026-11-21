# Handoff to the reviewer of the whole change

You review the whole change of one task of the-way as an agent that did not make it. The person who
requested the cycle has delegated intermediate choices to the orchestrator; nothing here is that
person's approval.

## Where and what

- Worktree: `the root of the task's worktree` (branch
  `task/hide-the-way-skills-from-models`). Read-only for you: change nothing tracked.
- Method: `task-cycle/review/SKILL.md` of the worktree, read whole, and `task-cycle/review/whole_change.md`
  as it tells you. You are the reviewer of the whole change: you select your own foundation and
  guidelines as the method gives.
- Range: base `19e5774aed6d1d628042e23deccc110ed9f112c0`, head `7d063ef2` (confirm with
  `git rev-parse HEAD`; if `7d063ef2…` does not match, ask before going on). Three commits:
  `f9cae3a6` (generator, its tests, the end-to-end test, 46 regenerated entry points), `f3188faa`
  (the paragraphs of 15 skills, `AGENTS.md`, `README.md`), `7d063ef2` (WAY-127, the invariant
  `skill-entry-points`, the environment fact `claude-code-skill-model-hiding`, the part map).
- The frozen task, which you read whole: `.runs/task-cycles/hide-the-way-skills-from-models/task.md`
  (Polish; the code and the foundation are in English). It has no spec and no plan: the one-author
  route, no slices, so no slice had a review of its own; you judge the whole.
- The author's report (claims to verify, not evidence):
  `.runs/task-cycles/hide-the-way-skills-from-models/reports/author-report.md`. Two failing runs it
  mentions are beside it in `reports/`.
- The answers of the cycle's step 4: the change touches no trust boundary and holds no operation
  that cannot be undone.
- Your directory for working copies: `.runs/review-whole/`.
- Your report: `.runs/task-cycles/hide-the-way-skills-from-models/reports/review-whole-report.md`;
  its first line is `PASS <sha>`, `FAIL <sha>` or `questions`. The cycle's script
  `task-cycle/remarks_check.py` reads this report file; if the harness refuses the write, return the
  report whole as your answer.

## Working copies (word for word)

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
all the same and names in the report the remainder, with its full path and the reason it stayed. It
removes a copy, as any directory, by its path written out in full in the command, never through a
shell variable: an empty variable turns the removal on the directory the shell stands in.

`cycle.md` and the other files of the cycle's record directory — other agents' handoffs, reports and
findings — are not yours to read unless this handoff names them (it names the two above). You do not
run the product's whole gate (`python -B gate/run_tests.py` with no argument); you may run focused
checks of directories (`python -B gate/run_tests.py <directory>`) and
`python -B elements/common/foundation_check.py`.

## Things the orchestrator asks you to look at

- The author wrote a clause the rows of *Settlements to record* do not give: WAY-127's second paragraph
  and the invariant `skill-entry-points` say each entry point lists every skill with the path of its
  `SKILL.md`. Judge whether it contradicts the settlements (the task's rows, answers and *Not chosen*), and
  mark a blocking finding that comes from it `Contradiction: yes` if it does.
- Acceptance criterion 1 of the task asks for a check in a real Claude Code session; the author ran it on
  a probe repository (report, "Own-work check"). Judge whether the report's evidence meets the criterion and
  say what stays unchecked.
- Codex: both copies carry the field; nothing shows how Codex treats it. The cycle did not settle it; do
  not grade the unverifiable absence of a Codex check as a defect of the change, but name any text of the
  change that claims something about Codex.
- Every text that still tells a session of the-way (not a product) to call a skill of the-way, and every
  text that changed the product's hand-over (the product's entry points are written by
  `installation/install.py`, which the task does not change).
