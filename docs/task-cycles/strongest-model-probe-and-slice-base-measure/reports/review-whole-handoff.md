# Handoff — review of the whole change (task cycle of the-way)

## Delegation and place

The person who requested this cycle has delegated intermediate choices to the orchestrator; no
answer of the orchestrator is that person's approval. You have no contact with a human: send a
question to the orchestrator by returning `questions`.

- Worktree: `the task's worktree`, branch
  `task/strongest-model-probe-and-slice-base-measure`. Read only; you change no tracked file.
- Method: `task-cycle/review/SKILL.md` (`review-change`) in the worktree. Read it whole, and a file
  it names only when the step or variant that names it comes. Your stage: the review of the whole
  change, by one reviewer that made none of it.
- Range to review: base `b502011f53225451ddf121e2b772a903b87492db` to head
  `60561fba` (one commit by the one author, no spec, no plan, no slices). Read the full diff of
  the range.
- Frozen task, read whole (under the worktree):
  `.runs/task-cycles/strongest-model-probe-and-slice-base-measure/task.md`. Check every item of its
  *To do* (points 1–5), the three rows of *Settlements to record*, the *Questions to settle* with
  their *Not chosen* lists and *Out of scope* against the change, and the fidelity of the
  entries to those sources.
- The author's report: `.runs/task-cycles/strongest-model-probe-and-slice-base-measure/reports/author-report.md`.
- Answers of the start: trust boundary — no (`task-cycle/cycle_stages.py` and the other
  trust-boundary files of the part map are not changed); irreversible operation — no.
- Selection: you select your own foundation and guidelines by "Reading the foundation" in
  `elements/common/way_of_working.md` and `product-guidelines/reading.md`, writing the index of your
  whole selection into your directory below, and state in the report how many decisions you read
  whole. The author's report names what it did not read: it did not run
  `elements/common/decision_index.py` (it read WAY-229, WAY-136, WAY-227, WAY-160, WAY-125 whole and
  searched the rest by `grep`), and did not read `elements/decisions/examples.md`,
  `guidelines/coding.md` or `guidelines/testing.md` (the change is prose and no code or test).
  Judge whether those gaps hid a collision or a wrong form.
- Particular care: the probe's procedure in `task-cycle/skill/SKILL.md` must be workable as written
  (the orchestrator can read the actual model of a probe agent from `task-cycle/cycle_stages.py`;
  every dispatch of the strongest class then uses the model fixed); the rule that replaces the
  list of tests must leave no place that still speaks of the list; WAY-136's and WAY-229's binding
  sentences must say what the task's settlements say, no more and no less (the *Not chosen* lists
  bind); the limits of the foundation check on binding sentences hold; no other file restates the
  old rule.

## Your report

- Report path: `.runs/task-cycles/strongest-model-probe-and-slice-base-measure/reports/review-whole-report.md`
  (under the worktree). First line `PASS <sha>` or `FAIL <sha>` (the head) or `questions`. This
  file is the input of the cycle's scripts (`task-cycle/remarks_check.py` reads it); the note that a
  subagent returns findings as text is no reason not to write it. If the harness refuses the
  write, return the report whole as your answer.
- Return: the report's first line, a one-line check result, and the report's path. The report holds,
  as `review-change` gives: grades (blocking, Minor, outside the task's scope), for each remark its
  place as `file:line`, its full wording and its reasoning, whether a blocking finding contradicts
  the settlements (`Contradiction: yes|no`), the checks you ran with command and exit code,
  **Unread material** (what this handoff names, or your own selection, that stayed unread or was
  read in part, or `none`) and **Searches not found or unclear** (or `none`).
- `cycle.md` and the other files of the record directory beyond those named above are not yours to
  read.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
in the system's temporary directory, in the scratch directory of a session or in the main checkout
of the repository. In a product, a worktree or checkout made to run checks gets its `.the-way`
populated, and the dependencies those checks need installed as the product's own rules give,
before they run; otherwise they fail for that reason. The screenshot that a screenshot tool, such as the Playwright server, saves by
itself under its session's directory is moved into the agent's directory and the original removed,
except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md`
says, to the place the product's foundation settles for screenshots, and into the agent's directory
only where no such place is settled. The files that a product's own tools and tests make by
themselves are no working copy of the agent and stay outside this rule. Before the agent returns,
each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then
`git worktree prune` — keeps in `reports/` beside its report what the report needs, the input and
command of a probe that shows a finding among them, and states in
the report where each copy stood and that it was removed. Where a removal fails, the agent finishes
all the same and names in the report the remainder, with its full path and the reason it stayed. It
removes a copy, as any directory, by its path written out in full in the command, never through a
shell variable: an empty variable turns the removal on the directory the shell stands in.

Your directory for working copies: `.runs/review-whole/`.
