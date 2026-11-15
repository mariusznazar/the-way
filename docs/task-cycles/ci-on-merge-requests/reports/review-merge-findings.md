# Findings of the review of the merge (blocking), for the fix

Source: `reports/review-merge-report.md`, review of the merge `3eacbc1`, first line `FAIL 3eacbc139401085914940f54bcc60723aa537c9f`. The two blocking findings, in the reviewer's words. The Minor finding 3 of that report is not fixed (a Minor finding of the review of a reconciliation goes to the request's list).

## Important — within the task

**1. A red CI result on a flaky test outside the task's scope gets two opposite rules in the merged
tree.**

Places:
- `foundations/decisions.md:2683-2688` (WAY-160, the task's sentence: CI red is "a failed gate — a
  fix and its review").
- `task-cycle/skill/SKILL.md:596-599` (step 12: "A red result is a failed gate (step 10): its
  failures are fixed, the fix reviewed …, and the wait repeated on the new head").
- `task-cycle/skill/correction.md:59-61` (the same).
- `agent-instructions/README.md:107-108` ("a red result is a failure of the gate, which the change
  fixes before the request goes to Mariusz").

These meet the second paragraph of WAY-261 that the merge brought in:
- `foundations/decisions.md:5960-5963`: "The red result of the first run of the gate on the final
  tree stays the result of the gate, also where the check that failed is one outside the task's
  scope that passes when run again; the cycle does not stop for it, and the request names that check
  and the task that fixes it, or proposes that task where none exists". Its *Violated* example reads
  "the cycle stops … because a test outside the task's scope failed and passed when run again".
- Its copy in step 10, `task-cycle/skill/SKILL.md:490-494`, added by the target.

What goes wrong: the CI run is the one place where the POSIX-only tests run (WAY-16, the
`agent-instructions/README.md:71-73` paragraph). A flaky test there, outside the task's parts, makes
CI red.

- Under the task's text, the orchestrator must fix it within this request, and wait again before the
  request goes to the human. That means fixing outside the task's scope (WAY-161 keeps such findings
  unfixed), or rerunning CI until it is green (WAY-243 forbids rerunning to make a gate pass).
- Under WAY-261, which calls itself the rule for a failed gate and to which step 12 points with
  "(step 10)", the cycle goes on, keeps the red result and names the test and its task.

Neither side shows this alone: the task branch was written before WAY-261 gained its second
paragraph. The target never had a CI wait. WAY-261 also lists `derives from WAY-160` among its
*Relations*, so the two entries are meant to agree.

Why it matters: the same red result now has two answers in the cycle's own skill and log, and the
handoff's question is exactly "no step now contradicting another". It is a rule the change writes
(WAY-160), restated more broadly than the foundation allows: WAY-263 grades that Important.

Evidence: the quoted lines above. `compare_log_entries.py base target` lists WAY-261 as changed by
the target. `git diff 21ecb62 7f5c5a5 -- task-cycle/skill/SKILL.md` shows the WAY-261 sentences of
step 10 as added by the target.

Repair, for the author: make the CI rule defer to WAY-261 for that case, in WAY-160, step 12,
`correction.md` and the README paragraph. A possible wording: "a red result is a failed gate, handled
as step 10 gives — a fix and its review, save a check outside the task's scope that passes when run
again, which WAY-261 governs".

**2. The installation part now reaches `instruction-files`, which its *Depends on* does not allow,
under the definition of a dependency that the merge brought in.**

The rule the merge brought in:
- The new glossary entry "dependency of a part" (`foundations/glossary.md:37-39`): "any reach of
  that part to another part … a skill of it that calls a skill or a file of the other, a script of
  it that reads a file of the other, … a path or a git tag of the other, or code of it that imports
  the other".
- The part-map template (`elements/part-map/template.md:91-93`): "What counts as a dependency of a
  part is what the glossary gives that term, any reach and not only an import, so *Depends on*
  covers every such reach".
- WAY-225 (`foundations/decisions.md:2486-2493`) and WAY-11 (through the template: "A change of the
  code that changes … what it may depend on … rewrites the entry in the same change").

The task's reaches:
- Installation's code writes into every product's guidance
  `python -B .the-way/instruction-files/check_instructions.py` and states that script's exit-code
  contract (`installation/install.py:200-202`).
- Its README says the same (`installation/README.md:61`, `:82-84`).
- Its test checks that the path exists at the pinned commit (`installation/test_install.py:145-146`,
  `:161-168`).

That is a reach of `installation` to `instruction-files`. Yet `installation`'s *Depends on*
(`foundations/part_map.md:192-193`) reads "decisions · invariants · glossary · part-map ·
environment-facts · elements-common · project-level · product-guidelines · task-cycle ·
foundation-review", without `instruction-files`. Before the task, no file of `installation/` named
`instruction-files` (`git grep instruction-files 7f5c5a5 -- installation/` finds nothing).

Why it matters: the merged map contradicts the merged code by the merged map's own rule. A later
change to `instruction-files` (renaming the script, changing its exit codes) would be judged against
a map that says installation does not depend on it. A later return step on either part would find
the reach and have to take it to the human as a violated invariant (WAY-225, WAY-51), when it is a
reach this task meant.

It is within the task (the change made the reach), and the change already edits the part map. The
fix is one item, `instruction-files`, in `installation`'s *Depends on*. Or, if the human is not to
allow it, the route WAY-225 gives.

Evidence: the lines above, and `git diff 7f5c5a5 3eacbc1 -- foundations/part_map.md` (only the
`.github/workflows/**` line).
