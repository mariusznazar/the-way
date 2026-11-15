# Handoff — the fix of the review's findings (the one author, resumed)

You fix the findings of the review of the whole change. Your method is `task-cycle/change/SKILL.md`,
variant **the fix of a review's findings** (read `task-cycle/change/fix.md`, as the skill says). The
findings file is `reports/review-whole-findings.md` (in the record directory
`.runs/task-cycles/ci-on-merge-requests/reports/`), the reviewer's words: three blocking findings
(I-1, I-2, I-3, Important) and four Minor findings within the task (M-1 to M-4). Fix all seven in one
fix, as one range of commits after `345b6bd`. Your report: `reports/author-fix-report.md` in the
same directory, with the sections the first report had (checks with command and exit code,
own-work check, **Unread material**, **Searches not found or unclear**, working copies, and for each
finding what you changed and where). Working copies: `.runs/author-fix/`, removed before you return.
Run no whole gate. The delegation, the worktree and the rules of the first handoff
(`reports/author-handoff.md`) stand.

## The orchestrator's answers (they bind the fix)

- **I-1** (*Based on* of WAY-16 and WAY-206). Take the reviewer's third way as the floor and the first
  as the aim: write an environment fact, through the method of
  `elements/environment-facts/skill/SKILL.md` (as `task-cycle/skill/foundation_step.md` gives), for
  what a source a reader can open states — the page of GitHub's own documentation on the alerts of
  vulnerable dependencies (Dependabot alerts: that a repository's owner turns them on in its settings
  and that they read the repository's dependencies without a change) and the page on rules for
  branches (a rule can require a status check to pass before a merge; the check can be chosen only
  after it has run; a bypass list lets chosen people past the rule). Read the pages with a web tool
  (search for a fetch tool if you do not hold one) at their current address and take every value from
  what the page says, never from memory; give the address and the date read. Name the facts in
  WAY-206's and WAY-16's *Based on*. Where a page cannot be read, or what you need is a reading of
  the-way's own repository (the branch is not protected today and the rule is the human's action,
  so no reading of it exists), write `TODO — <what is missing, with its source>` in that *Based on*
  as the decision template gives, so that WAY-287 puts it before the human. Name each of your
  choices and its price in the report.
- **I-2** (the correction route and the blocked requests). WAY-160 and the routes of the cycle say:
  the wait for CI, the treatment of red as a failed gate and the CI result in the description apply
  to every push to a request that is open for review or waits only for human actions in the cycle —
  the correction after review included (`correction.md`: wait for the run on the corrected head,
  write its result into *Checks*, a red result is a failed gate: a fix and its review, the gate, the
  pair of commits again, the wait again). A request the cycle leaves blocked for a remaining
  blocking finding, a slice that failed twice or a reserved choice (`blocked_finding.md`,
  `reserved_return.md`, step 9 sub-step 4) is out of the wait: its code is unfinished, CI may run and
  its result stands on the request's page for the human to read, and the description says so
  where it names the CI. Write that in WAY-160 (sentence and *Verification*/*Rationale* as they need)
  and in the three places.
- **I-3** and **M-4** (the installer's block). One edit of the same sentence in
  `installation/install.py` `product_guidance`: the bypass of the owner is named, and the claim
  that CI runs the one command is made true where a product has not yet written its CI file (the
  reviewer's clause "where this repository has a CI file", or the like, with a fallback in the same
  way as the block gives for the two checks). Change the tests of the block that hold the fragments.
- **M-1**: say in one sentence which holds (a read-only credential for the submodule is the one
  secret the job may hold, and then a request from a fork cannot be checked), or the like, in
  `installation/README.md`.
- **M-2**: the clause the reviewer proposes (the row stands in the ignored original, and in the
  committed copy only for the runs before its own head) in `task-cycle/record_template.md` and
  `task-cycle/skill/SKILL.md`.
- **M-3**: the edit of the description for the CI result in step 12, and in the correction's new
  step, takes the checks of the template, the check of private paths included, before it is
  published.

After the fix, run the focused checks of what you changed (single directories, one at a time),
`python -B elements/common/foundation_check.py`, and the search of the foundation of
`foundation_step.md` for the entries you now write or change. The files you change, each whole
before you change it.

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

Your directory is `.runs/author-fix/`.
