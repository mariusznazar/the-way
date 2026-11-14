# Handoff — the review of the whole change

You review the whole change of the task `ci-on-merge-requests` as an agent that did not make it.

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator. You ask
no human anything; a question goes to the orchestrator as the status `questions`. Your grades and
your scope are yours alone: nothing in this handoff names a finding wrong, Minor or outside the
scope.

## Where and what

- The worktree: `the worktree of the task`; work from its root. You are
  read-only: you change no tracked file and commit nothing.
- The method of your stage: `task-cycle/review/SKILL.md` (the-way is the worktree), whole; and
  `task-cycle/review/whole_change.md`, as the skill tells. Read another file the skill names only
  when the step that names it comes.
- The range to review: base `21ecb627f885de438e2209d7ff5c137b1e1b9d83` to head
  `345b6bd` (confirm `git rev-parse HEAD` is `345b6bd...`; compute `git diff 21ecb62..345b6bd` and
  `git log 21ecb62..345b6bd` yourself). Ten commits, 13 files, 245 insertions and 50 deletions.
- The frozen task, which you read whole: `.runs/task-cycles/ci-on-merge-requests/task.md` — all of
  it: *To do* 1–7, *Acceptance criteria*, the six answers under *Questions to settle*, *Decisions
  in play*, *Settlements to record* rows 1–6, *Human actions*, *Out of scope*. Check the coverage of
  every *To do* item, of each settlement row and of the acceptance criterion, and the source
  fidelity of the foundation entries the change writes (WAY-16, WAY-206, WAY-160, WAY-09) against
  the task's rows: nothing added to what a row settles, nothing missing.
- The author's report, a set of claims to verify, not evidence:
  `.runs/task-cycles/ci-on-merge-requests/reports/author-report.md` (the Linux evidence beside it:
  `reports/author-linux-evidence.txt`).
- Your report: `.runs/task-cycles/ci-on-merge-requests/reports/review-whole-report.md`, first line
  `PASS <sha>` or `FAIL <sha>`, with the graded findings, the checks you ran with command and exit
  code, **Unread material** and **Searches not found or unclear** (`none` is an answer), the count of
  decisions read whole and by title only (WAY-150), and for each blocking finding the slice it comes
  from, or that it comes from none (here: no slice; one author without a plan).
- Your directory for working copies: `.runs/review-whole/`.

## The orchestrator's answers at the start

- Trust boundary: **yes** — check crafted input at it. The change touches `installation/install.py`
  (the trust boundary of `installation`; only the text of `product_guidance`) and adds a CI
  workflow, `.github/workflows/tests.yml`, that takes in the content of a pull request. Check the
  workflow's trigger (never `pull_request_target`), the permissions of its token, secrets, text of
  the pull request reaching a shell command, the pinned actions (compare each SHA with the version in
  its comment by `gh api repos/<owner>/<repo>/git/ref/tags/<tag>`, a read only call), and what a pull
  request that edits the workflow can do. The author's own check of this is in its report; it is a
  claim for you to verify.
- Irreversible operation: no. The branch rule that makes the check required is made by the human
  after the request opens (the task's *Human actions*); check that the change performs nothing
  outside the repository and only prepares it (the check exists under a stable name).
- Reserved choice: none (GitHub Actions is named by To do 4). No spec, no plan.

## What the orchestrator selected for you, and what it knows it left out

You select your own foundation and guidelines (WAY-150). The-way holds no `guidelines/` directory.
Besides what you select by the parts the change touches (`installation`, `agent-instructions`,
`task-cycle`, `product-guidelines`, `instruction-files`, `decisions` and the part map), read whole
these, which the author did not read and the orchestrator's selection left out: WAY-161, WAY-162,
WAY-287, WAY-288, WAY-289 and WAY-300 (the request's description, the fixes of a review and the
reminder, which the changed *Checks* paragraph of `request_template.md` and step 12 of
`task-cycle/skill/SKILL.md` touch), WAY-243 (flaky tests and a rerun), and WAY-254, WAY-202 and WAY-235
(found by the author's search and not read by the orchestrator).

Facts about what the author reports it left unread or found unclear — check each:

1. The sentences about GitHub (that it has alerts of vulnerable dependencies, Dependabot, which a
   human turns on in the repository's settings; that a branch rule can require a check that has run
   once, with a bypass for the owner) have no source in the task or the foundation, and the author
   wrote no environment fact for them. The return step, run after your review, decides about
   environment facts; say whether a decision or invariant now written rests on them in a way that
   a check of the foundation would call a gap.
2. The author added a Python-version line to the description of a product's CI file
   (`installation/README.md`, new section "Run the one command in CI", item 4) that To do 2 of the
   task does not list. Judge whether it is within the task.
3. The author fixed three tests of `instruction-files/test_check_instructions.py` that failed on
   Linux (the task asks the cycle to fix Linux failures that fit its scope). Judge that they fit, that
   they are test faults and not script faults, and that no test got weaker.
4. Two tests of `task-cycle/test_remove_merged_worktrees.py` fail only when the user is root; the
   author left them (a GitHub runner is not root). Say whether you hold that out of scope; do not
   fix.
5. The whole gate has not been run; it is the orchestrator's alone and it will be run after the
   review and the return step. You may run the tests of single directories, one at a time:
   `python -B gate/run_tests.py <directory>` on Windows, or in a container —
   `docker run --rm --memory 2g` with the image `python:3.14` (already pulled) as a non-root user,
   the worktree or a copy of it under `.runs/review-whole/` mounted read only — and remove each
   container and copy before you return. Never run the whole gate, on any system. A claim of a passing
   check in the author's report is read against what you can run yourself, not taken.
6. The acceptance criterion (the five tests run in the request's CI) can only be shown on GitHub after
   the request opens; check that the workflow's design makes it so and that nothing in it skips them.

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

Your directory is `.runs/review-whole/`.

## Return

Return the first line of your report (`PASS <sha>` or `FAIL <sha>`), the changed files you judged,
a one-line check result, and the report's path.
