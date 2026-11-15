FAIL 3eacbc139401085914940f54bcc60723aa537c9f

# Review of the merge of `origin/foundations` into `task/ci-on-merge-requests` (correction 1)

Range: the merge commit `3eacbc1` (first parent `351ffb1`, the task branch; second parent `7f5c5a5`,
the target `foundations`; merge base `21ecb62`). `git rev-parse HEAD` in my worktree:
`3eacbc139401085914940f54bcc60723aa537c9f`, the head given. Read from a detached worktree of
`3eacbc1`, never from the task's working tree.

Method: `task-cycle/review/SKILL.md` and `task-cycle/review/fix.md` at `3eacbc1`. This review is of
the reconciliation only, so `fix.md`'s list of remarks does not apply here: the human's remarks are
answered by the correction's own diff, which is not this range.

## Summary of what holds

- **Everything outside the decision log is the task's change, unaltered.** The diff `7f5c5a5..3eacbc1`,
  taken without context and without hunk headers and leaving out `foundations/decisions.md`, is the
  same byte for byte as `21ecb62..351ffb1`, taken the same way (`diff` exit 0). Both cover the same 17
  files. So the merge resolved `agent-instructions/README.md` by keeping both paragraphs, with the
  task's paragraph first, and dropped nothing from either side.
- **The decision log: the four entries were applied again correctly.**
  - `compare_log_entries.py target merged` reports exactly WAY-09, WAY-16, WAY-160 and WAY-206, so
    every other entry and the withdrawn list are byte-identical to the target's.
  - `compare_log_entries.py base target` reports 18 entries the target changed (WAY-13, 18, 21, 24,
    51, 107, 150, 153, 167, 225, 261, 287, 289, 300, 316, 339, 375, 376). None of them is one of the
    four, so the two sides changed disjoint entries.
  - `compare_log_entries.py task merged` reports those 18 plus WAY-09 and WAY-206. WAY-16 and
    WAY-160 are byte-identical to the task branch's.
  - A word-by-word comparison of the four entries, with all whitespace treated as equal, finds the
    same words in each, task copy against merged copy: WAY-09 824 words, WAY-16 704, WAY-160 952,
    WAY-206 861. So WAY-09 and WAY-206 differ only by rewrapping.
  - Every hunk of `git diff 7f5c5a5 3eacbc1 -- foundations/decisions.md` lies inside one of the
    four entries.
- **No trust-boundary file changed in the merge.**
  `git diff 351ffb1 3eacbc1 -- installation/install.py .github/workflows/tests.yml` is empty.
- **No record copy or screenshot is in the tree.** `docs/` holds no file at `3eacbc1`, and no image
  is among the changed files.
- **The part map has no textual conflict.** The task added the line `.github/workflows/**` to
  `agent-instructions`. The target added `foundation-review · process-audit` to the same part's
  *Depends on* and changed other parts' entries. Both stand side by side.
- **The task-cycle files read as one consistent whole on the points the handoff names:**
  - Step 13's reading of the backlog for the reminder (WAY-300) and the CI wait in step 12 do not
    meet. The reminder stays in every rewritten description, and the CI edit is one such rewrite.
  - The removal of working directories (WAY-375) agrees with step 12's "keep the worktree".
  - The answer "fix it in this request" to an item of *Fix or let through* (target, in
    `agent-instructions/README.md:111-116`) now follows the CI paragraph (`:106-109`). Its "checked
    as above" thus also covers the CI wait on the fixed head, which agrees with "after each
    correction".
  - No item number that the task's text cites changed. The task's additions cite steps 10 and 12
    and WAY-160 / WAY-309, and the item-17 mention in `correction.md` is the target's own context.
  - Items 4, 16 and 17 of `request_template.md` kept their numbers.

## Findings

### Important — within the task

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

### Minor — within the task

**3. Two further reaches of the change, under the same definition, that no *Depends on* allows.**

- `.github/workflows/tests.yml:41` (`agent-instructions`) reads `/.python-version`. That file is of
  the part `repository` (`foundations/part_map.md:149-151`), and `agent-instructions` does not list
  `repository` (`foundations/part_map.md:168-170`).
- `installation/README.md:143` and `:158` name `.github/workflows/tests.yml` (`agent-instructions`)
  and `.the-way/.python-version` (`repository`).

I grade these Minor, not Important, for two reasons:
- The target's own tree already holds an unlisted reach of the same kind: `installation/README.md:14`
  names `.python-version`, and no part of the merged map lists `repository` in its *Depends on*.
  So whether `repository` and a README's mention count is unsettled in the foundation itself.
- No reader is led into a wrong action by it.

Handled together with finding 2, it costs one or two more items.

## Remarks of the correction

Not judged here: this review covers the reconciliation with the target branch, not the correction's
own diff (which another agent is still making in the working tree).

## Declined to judge

- The handling of a CI run that does not report as only "named under *Checks*"
  (`task-cycle/skill/SKILL.md:599-600`), against item 4 of `request_template.md:233-237` and WAY-287
  ("the checks not run" in the section for the human's decisions). It predates the merge: neither
  item 4 nor that clause of WAY-287 changed between `21ecb62` and `7f5c5a5`. So it is the first
  cycle's change, which its reviews judged, and no seam of the merge. Step 13's new route for the
  reminder count (target) only makes the asymmetry visible beside it.
- The descriptive `TODO` in WAY-16's *Based on* (`foundations/decisions.md:2552-2555`), which item 16
  puts before the human. It came from the first cycle unchanged by the merge. The orchestrator writes
  it into the request.
- Line widths of 101 characters in WAY-160 and WAY-206. The target log holds 367 lines over 100
  characters, and the merged log holds fewer such lines than the task branch's log (373 against 377).
  The short line "in; such" in WAY-206's rationale (`foundations/decisions.md`, at the end of the
  rewrapped paragraph) is cosmetic and changes no word.

## Checks

| Check | Command (from the worktree of `3eacbc1`) | Exit code / result |
|---|---|---|
| Head | `git rev-parse HEAD` | 0; `3eacbc139401085914940f54bcc60723aa537c9f` |
| Non-log diff equals the task's change | `git diff -U0 21ecb62 351ffb1 -- . ':!foundations/decisions.md'` and `git diff -U0 7f5c5a5 3eacbc1 -- . ':!foundations/decisions.md'`, `@@` and `index` lines dropped, then `diff` | 0 (identical) |
| Target log against merged log | `python -B elements/common/compare_log_entries.py <7f5c5a5 log> <3eacbc1 log>` | 1; 4 reports: WAY-09, WAY-16, WAY-160, WAY-206 |
| Task log against merged log | `python -B elements/common/compare_log_entries.py <351ffb1 log> <3eacbc1 log>` | 1; 20 reports: the 18 target-changed entries plus WAY-09, WAY-206 |
| Base log against task log | `python -B elements/common/compare_log_entries.py <21ecb62 log> <351ffb1 log>` | 1; 4 reports: WAY-09, WAY-16, WAY-160, WAY-206 |
| Base log against target log | the same, `<21ecb62 log> <7f5c5a5 log>` | 1; 18 reports (listed above), none of the four |
| Words of the four entries, task against merged | a scratch Python script `.runs/review-merge/cmp/words.py` (blocks as the comparison script cuts them, whitespace-split words compared) | 0; same words in all four |
| Trust-boundary files untouched | `git diff 351ffb1 3eacbc1 -- installation/install.py .github/workflows/tests.yml` | 0; empty |
| Foundation check | `python -B elements/common/foundation_check.py` | 0; `0 errors` |
| Tests | `python -B gate/run_tests.py elements/common` | 0; 235 tests, OK |
| Tests | `python -B gate/run_tests.py installation` | 0; 61 tests, OK |
| Tests | `python -B gate/run_tests.py agent-instructions` | 0; 25 tests, OK |
| Tests | `python -B gate/run_tests.py instruction-files` | 0; 105 tests, OK (5 skipped) |
| Tests | `python -B gate/run_tests.py task-cycle` | 0; 483 tests, OK |
| Index of the decisions the merge changed | `python -B elements/common/decision_index.py --output ../cmp/index_merged_in.md --decision WAY-13 … --decision WAY-376 .` (the 18 numbers) | 0 |

The full gate was not run, as the handoff and the method give.

## Reaches beyond the dispatch

- The glossary entry "dependency of a part" (`foundations/glossary.md:37`) and the section "Allowed
  dependencies" of `elements/part-map/template.md`: to judge item 3 of the handoff, the part map
  against what the target changed in it. Both came with the merge.
- The part-map entries `installation`, `repository` and `agent-instructions`
  (`foundations/part_map.md`), whole: for findings 2 and 3.
- WAY-225 whole and WAY-261 whole: WAY-225 because the template cites it, WAY-261 because the index
  showed that its new paragraph bears on the CI rule.
- Item 4 and item 16 of `task-cycle/skill/request_template.md`: to check the item numbers the
  change's text could cite, and for the lines under Declined to judge.
- `installation/test_install.py:161-168`: the test that pins the path of finding 2.

## Selection of the merged-in decisions

The index of the 18 decisions the target changed (no decision was added or withdrawn between base
and target) was read whole. I opened whole those bearing on the change:
- WAY-261 and WAY-225 (above), and WAY-160 (the task's own, merged).
- WAY-09, WAY-16 and WAY-206, through the diff and the comparisons.

The rest were judged by their binding sentences in the index, against the merged skill files:
- WAY-18: the change adds no entry, so no section is opened.
- WAY-150: no reading rule is touched.
- WAY-21 and WAY-24.
- WAY-300: the reminder and the CI edit agree.
- WAY-287 and WAY-289: items unchanged in number. The checks-not-run line is under Declined.
- WAY-339: the measures. The CI wait adds no measure.
- WAY-375 and WAY-376: the worktree is kept, consistent.
- WAY-316, alongside WAY-373: no screenshot.
- WAY-13, WAY-51, WAY-107, WAY-153 and WAY-167: no bearing.

## Working copies

- A detached worktree of `3eacbc1` at
  `.runs/review-merge/wt`: removed with
  `git worktree remove --force` (exit 0), then `git worktree prune`; `git worktree list` names it no
  more.
- Scratch files (log copies, the diffs, the index, the words script, the test outputs) in
  `.runs/review-merge/cmp`: removed (exit 0).
  Nothing was kept in `reports/`: the report quotes what it needs. No remainder.

## Unread material

The method's other beside files (`whole_change.md`) were not read, since this is no review of the
whole change.

Read in part:
- Of `task-cycle/skill/SKILL.md`, steps 10 to 14 and "The end of a code review", plus the diffs of
  both sides.
- Of `correction.md`, `request_template.md`, `record_template.md`, `blocked_finding.md` and
  `reserved_return.md`, the diffs of both sides and the passages cited above.
- Of `foundations/decisions.md`, the four entries through the diff, WAY-160, WAY-225 and WAY-261
  whole, and the 18 merged-in entries by the index.
- Of `elements/common/way_of_working.md`, "Reading the foundation".
- Of `elements/common/compare_log_entries.py` and `decision_index.py`, the docstrings.

## Searches not found or unclear

- Whether a reach to a file of the part `repository` (`/.python-version`), or a mere mention of
  another part's path in a README, counts as a dependency of a part. The glossary's words cover it,
  but the target's own tree leaves such a reach unlisted (`installation/README.md:14`), and no part
  lists `repository` in its *Depends on*. Unclear, which is why finding 3 is Minor.
