# Report of the executor of slice 21

**Status:** done

**Commit:** `e94b13d` on `task/decision-log-second-round`: "Remove the withdrawn decision numbers from the task cycle skill files and record template and give each rule its reason".

**Files changed** (53 added, 32 removed lines in all):
- `task-cycle/skill/SKILL.md`
- `task-cycle/skill/blocked_finding.md`
- `task-cycle/skill/correction.md`
- `task-cycle/skill/spec_review.md`
- `task-cycle/record_template.md`

## Checks

| Command | Exit code | Result |
|---|---|---|
| `python -B elements/common/foundation_check.py` | 1 | Lines for the files of the slice's *Change*: none (`grep` of its output for the five paths found nothing). The exit code 1 comes from files of slices not yet made. Before my edit it listed 25 lines for these files. |
| `python -B gate/run_tests.py task-cycle` | 0 | 440 tests OK |
| `python -B gate/run_tests.py agent-instructions` | 0 | 25 tests OK |
| `python -B agent-instructions/skill_entry_points.py` | 0 | "entry points are current" |

The product's gate was not run (the cycle's run).

## Own-work check

Requirement most likely not met: a number that left the log stays in one of the five files, or a removal changes the sentence around it. Check: the foundation check's lines for the five files, before (25 lines) and after (none), and a read of `git diff -U0` for every removed bracket. Result: each number left with its brackets and the sentence kept its full stop; the reference numbers that stay (WAY-148, 150, 164, 260, 294, 295, 309, 316 and others) were left as they were.

## Reasons added (file and sentence, with the entry read at base `ec7929d`)

- `task-cycle/skill/SKILL.md`, step 4, after "where it cannot fast-forward, stop and say so." (WAY-298 *Rationale*): "A cycle started from a copy that stands behind its remote reads an older skill and entry point with nothing to show it, so a copy that cannot be brought up to date is shown to the human instead of being worked from."
- `task-cycle/skill/SKILL.md`, step 4, after "If it is, do not run the gate on the base." (WAY-367 *Rationale*): "The final gate of the earlier cycle ran on the files the base now holds, so a run on the base would repeat it and add a full run of the gate to the wait of every cycle."
- `task-cycle/skill/SKILL.md`, stage reports, after "...saying why it bears on nothing the agent judged." (WAY-325 *Rationale*): "Going on at the status alone would let an unread decision pass through a stage that looks complete, and an error hidden in it would reach the request."
- `task-cycle/skill/SKILL.md`, stage reports, after "`none` is an answer, a missing section is not." (WAY-326 *Rationale*): "The section of unread material stands apart from the account of what the agent looked for, because that account goes into the process remarks word for word and an unread file usually concerns one change, not the process."
- `task-cycle/skill/SKILL.md`, step 9, after "...never to change a reviewer's grade or scope." (WAY-158 *Rationale*): "The independent reviewer already reads the change for correctness, so repeating that read in coordination costs attention." The missing part of the rule was added first: "The reviewer reads the full diff of the range it reviews." (WAY-158's first sentence; `task-cycle/review/SKILL.md` line 45 has the reviewer compute the diff).
- `task-cycle/skill/SKILL.md`, step 10, after "...by the agent that owns them." (WAY-159 *Rationale*): "Repeating a completed check for coordination spends time without checking another state, while a changed state or an unresolved failure needs new evidence."
- `task-cycle/skill/SKILL.md`, step 10, WAY-349 (*Rationale*): "A time that a script reads from the run cannot be copied wrongly, and a change to the script shows in the files, where a change to an agent's habit leaves no trace." Placed before "The gate's output passes through unchanged." and not after it: the rule of WAY-349 is that every run goes through the script, which the sentences before it give, and the unchanged output is a different part of it. This differs from the plan's placement, as a choice; cost if wrong: a reader moves one sentence.
- `task-cycle/skill/blocked_finding.md`, after "...on code its review has not accepted." (WAY-163 *Rationale*): "Work done on code its review has not accepted is done again once the fix the human's decision calls for is made, while a run of the gate costs little and shows the human where the code stands against the rest of the product's checks." The missing part of the rule was added first: "The request names each of these that has not run on that code."
- `task-cycle/skill/correction.md`, after "...run them again." (WAY-306 *Rationale*): "A merge can bring in a rule or code that the change goes against, or that meets the change at a seam neither side shows alone, which is why the dispatch asks whether the two sides still hold together." The missing part of the rule was added first: "The reviewer's range is the commits of the merge the dispatch gives."
- `task-cycle/skill/spec_review.md`, after "comparing the two." (WAY-307 *Rationale*): "The designer revises the spec in its own file, which no commit holds, so without the copy the reviewer of the revision would compare it with the earlier text from memory."
- `task-cycle/record_template.md`, end of the paragraph on the corrections (WAY-357 *Rationale*): "The cause stands in the record because the record is the cycle's only log and the place the nightly review of cycles reads, which the title of a commit is not." The missing part of the rule was added first: "The title of the commit that adds a copy of the record holds no cause."

## Numbers removed

SKILL.md: WAY-158, 159 (three places), 220, 221, 286, 290, 296, 298, 325, 326 (three places), 367. `blocked_finding.md`: WAY-163. `correction.md`: WAY-163, 306 (two places), 357 (two places), 358. `record_template.md`: WAY-317, 357, 358.

## Entries left under the "stay" rule

WAY-93, 94, 97, 263, 287, 294, 295, 297, 363 and 364: none was a reason to add or a number to remove in these five files by the foundation check's listing, and none was changed. WAY-287, 294 and 295 still stand in these files (for example `correction.md` and SKILL.md) and were left as they are.

## Beside the files: WAY-358

`task-cycle/record_template.md` already says what causes the line of a correction gives: each pair once, the source read and not judged with `item <n>`, `remark` and `target-branch`, and the kind judged by one test with `defect`, `not-required` and `none` only with `target-branch`. I added no sentence of the rule and no reason for WAY-358; I only removed its number there and in `correction.md`. Finding: the sentence of WAY-358 that the request's description after a correction shows the pairs in one sentence (WAY-287) stands in `correction.md` (kind 17), not in `record_template.md`; I took it to concern the description, not the causes of the line, and left it. A reason of WAY-358 (a pair keeps apart who raised a correction, which is read, from what was wrong, which is judged) stands in no file after the withdrawal; the plan's list asks for none, so I added none. Cost if the human wants one: one sentence in `record_template.md` after the paragraph on the corrections.

## Mismatches and choices

- The plan's section was truncated in several places by the copy ("the entry's 'the request na…", "SKILL.md:480-483 lists the reconciliation review under 'The end of…"). I read the missing part of each rule from the entry at the base: for WAY-163 the request names what has not run; for WAY-306 the range of the reviewer. Part of WAY-163 I did not add: that the work after the human's decision begins with the reconciliation with the target branch. `correction.md` already begins every correction with the merge of the target branch, so it stands there; cost if wrong: one clause in `blocked_finding.md`.
- The plan says the WAY-306 reason stands in `correction.md` and that step 12 of SKILL.md carries the same sentence; I added the reason to `correction.md` only, since SKILL.md's list of additions names none for WAY-306.
- A file `.runs/fc.txt` stands directly under `.runs/`; it is not mine (mine stood in `.runs/executor-21/` and is removed) and I left it.

## Reaches beyond the dispatch

`task-cycle/review/SKILL.md` line 45 (grep for "diff"), to see that the reviewer's reading of the full diff stands in the review method; `task-cycle/skill/request_template.md` (grep for "not run", line 508 names WAY-163 and is not in my slice).

## Unread material

none. Every file of my *Change* was read whole before I changed it; each entry of my *Read* was read whole at the base `ec7929d` (WAY-293 to its first rationale lines, lines 9771-9810 as the plan's range). `task.md` lines 25-55 were read, not 1-490.

## Searches not found or unclear

- The plan's section of slice 21 is cut in the middle of several items (see Mismatches); the full sentences of the rules were taken from the entries at the base.
- Whether WAY-349's reason belongs before or after "The gate's output passes through unchanged." is unclear in the plan; I placed it before (see above).

## Working copies

`.runs/executor-21/` held a copy of the base's `foundations/decisions.md` and the output of the foundation check; both files were deleted one by one and the directory removed. No remainder.
