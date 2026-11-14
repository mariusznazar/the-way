# Fix report: review of the whole change (task `agent-work-copies-in-task-directory`)

**Status:** done

**Commits:** `a300ee6` (range `5f01235..a300ee6`), on `task/agent-work-copies-in-task-directory`. Not pushed.

Files changed (added / removed vs `5f01235`): `foundations/decisions.md` 7/5, `task-cycle/plan/SKILL.md` 4/4, `task-cycle/review/SKILL.md` 3/2, `task-cycle/skill/SKILL.md` 62/60, `task-cycle/skill/request_template.md` 4/4 (`git diff 5f01235..a300ee6 --numstat`).

## Each finding

- **I-1 (Important), fixed.** The sentence in the first paragraph of "Working copies" (`task-cycle/skill/SKILL.md`) now reads: "The screenshot that a screenshot tool, such as the Playwright server, saves by itself under its session's directory is moved into the agent's directory and the original removed. The files that a product's own tools and tests make by themselves are no working copy of the agent and stay outside this rule." WAY-373's binding text got the same clause in its third sentence ("...while the files that a product's own tools and tests make by themselves are no working copy of the agent and stand outside it"), so the paragraph and the decision agree. I kept the out-of-scope clause in the rule (the guidance allowed it where it is the smallest way to keep the rule checkable): the paragraph is copied into every handoff and lists "a prepared input of a test" as a working copy, so without the clause an agent reads the rule as reaching its test runner's own files, which is the confusion the finding names. The other two places (`task-cycle/review/SKILL.md`, `task-cycle/change/ui_check.md`) were already narrow and are unchanged.
- **M-1 (Minor), fixed by moving the item to the lower part.** Chosen: kind 18 is deleted from `task-cycle/skill/request_template.md` (*You accept by merging*), and the leftover copy is shown in two places that the foundation already lets hold it: one plain sentence in **Cost** of the top part (that a copy of an agent's check stayed in the task's ignored working directory, that nothing waits for it, that it is removed by hand or goes with the task's directory; no path), and the path with the agent in **Checks** of the lower part (as it was). The second paragraph of "Working copies" in `task-cycle/skill/SKILL.md` now says "into the description under *Cost* and *Checks* as `task-cycle/skill/request_template.md` gives". Why: WAY-287's list of what the section for the human's decisions holds is closed and its `none` means nothing waits for a yes; a leftover copy needs no yes, so the item did not belong there. The other way (keep kind 18 and amend WAY-286 and WAY-287, link them from WAY-373) would have cost a change to two approved decisions, one of them a long closed list, and a `none` of that section that no longer says "nothing waits for you"; the saving would have been the human seeing the item in the decisions section, which the Cost sentence also gives. WAY-373's *Relations* stay `derives from WAY-148`: no link to WAY-286/287 is needed since neither is touched. WAY-286 was read (its form leaves **Cost** to "the cycle's cost", which a copy the human removes by hand fits); WAY-287 was read whole. `task-cycle/request_check.py` checks headings, groups and `none` in sections, not item kinds, and the two template tests passed unchanged.
- **M-2 (Minor), fixed.** In `task-cycle/skill/SKILL.md`, the list of what the orchestrator reads in every report now ends "its checks, reaches, unread material, searches and working copies", and the second paragraph of "Working copies" says "The report of every agent holds the line on its working copies, and you read it when the agent returns, as you read its **Unread material**." Step 14 stays as it was (it confirms the record lists each remainder a report names), consistent with that.
- **M-3 (Minor), fixed for the changed paragraphs.** Rewrapped to about 100 characters: `task-cycle/skill/SKILL.md` (step 2's paragraph, the boundary paragraph, step 4's paragraph on the base, the handoff paragraph, the paragraph on what is read in every report, step 14, the section "Working copies"), `task-cycle/review/SKILL.md` (the bullet on checks), `task-cycle/plan/SKILL.md` (the bullet on the size rule), `foundations/decisions.md` (WAY-373's *Rationale*), `task-cycle/skill/request_template.md` (the removed item). Each rewrap runs from the first line I had changed to the end of the paragraph, and in two paragraphs the older lines after my change were reflowed with it (diff noise in lines I had not changed; the alternative was a ragged short line). The title line of WAY-373 stays one line of 113 characters as a heading does; other headings of the log are that long. A check of the added lines after the fix, `git diff 671f470 -U0` filtered for added lines over 100 characters, lists only that heading.

## Checks (command and exit code)

| Command | Exit |
|---|---|
| `python -B elements/common/foundation_check.py` | 0 (`0 errors`) |
| `python -B gate/run_tests.py task-cycle` | 0 (394 tests OK) |
| `python -B gate/run_tests.py agent-instructions` | 0 (25 tests OK) |
| `python -B gate/run_tests.py instruction-files` | 0 (104 tests, 5 skipped) |
| `python -B gate/run_tests.py elements/common` | 0 (201 tests OK) |
| `git diff HEAD --check` (before the commit) | 0 |

Not run: the generators for `AGENTS.md` and skill entry points (no agent type or skill description changed); the whole gate.

## Own-work check

Requirement most likely unmet: the paragraph the handoffs copy and the decision say the same, and nothing still points at the deleted kind 18. Check: `grep -rn "kind 18\|writes by itself outside" task-cycle foundations/decisions.md`, exit 1 (no match), and `grep -n "no working copy of the agent" task-cycle/skill/SKILL.md foundations/decisions.md`, exit 0, one hit in each file. Result: no stale pointer; both files carry the clause. A second check, a scan of the added lines for an odd number of backticks, found one code span split over a line break in my first rewrap (`` `FAIL <sha>` ``), which I repaired before the checks above; the scan then printed nothing. What the check cannot show: whether an agent given the narrowed paragraph still removes its own copy; the next cycle shows that.

## Foundation search (WAY-33), once

One search after the fix: `grep -rn "kind 18\|Working copies left" task-cycle foundations` for the places my fix touches (kind 18 and the record item), and WAY-286 and WAY-287 read whole. Finding: the record item *Working copies left* in `task-cycle/record_template.md` stays as it was; WAY-286 and WAY-287 need no change. No other entry is touched.

## My own working copies

I made `.runs/author/` in this worktree to hold the output of the test runs, and removed it (`rm -rf .runs/author`) before the commit; `ls .runs` after shows only `task-cycles/`. Slips against the rule I wrote: (1) a command of mine ran `cat > <system temp>/null`, which created an empty file `null` in the system's temporary directory (it hung, was stopped, and I removed the file; the directory listing afterwards shows no `null`); (2) in the first round I wrote test output into a temp file, reported in the first report. Remainders: none.

## Unread material

Read whole this round: the findings file, the handoff, WAY-286, WAY-287, `task-cycle/skill/SKILL.md` (the paragraphs I changed, whole), `task-cycle/skill/request_template.md` (the changed parts), WAY-373 (mine). Not read: `reports/whole-change-review-report.md` (the handoff said to read its sections only if a finding needed them; none did), `task-cycle/change/fix.md` (read in the first round, not again).

## Searches not found or unclear

none

## Choices

- M-1, lower part against amending WAY-286/287: stated above; cost if wrong: the human misses the Cost sentence, and the copy stays until the task's directory goes.
- I-1, keeping the out-of-scope clause in the rule and in the decision: cost if wrong: one sentence more in every handoff.
- No questions.
