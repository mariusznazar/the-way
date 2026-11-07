PASS 3601aba4d9277868e8291ffe190c49427bdeb4a6

# Review of the whole change — merge-review-questions

Range `52889bc700123b50258c4201835034f0529351df..3601aba` (`git rev-parse HEAD` = `3601aba4d9277868e8291ffe190c49427bdeb4a6`, matches the dispatch). Two commits, no plan, no spec, one author. Blocking findings: 0. Minor: 2 (both within the task). Out of scope: 0.

## Findings

### Critical
none

### Important
none

### Minor

1. `foundations/decisions.md` WAY-307 *Rationale* (the last sentence of its *Rationale*, "one more file kept with the spec, which reaches the record of the cycle with the rest of its directory") and WAY-306 *Rationale* ("no automatic check finds that"). `elements/decisions/template.md` ("Where entries go" bullets on *Rationale* and *Rejected*) bars a *Rationale* the author writes from naming a file or count, or "what the process's own tools do or lack today". "One more file" is close to a count of files, "reaches the record of the cycle" tells what the copy step of the record does today, and "no automatic check finds that" tells what the checks lack today. Each fact comes from the task's *Need*/*Context* and is true, and none is a binding sentence, so the effect is a slightly looser entry; the next change to the check or the record would leave the sentence stale. Lies within the task (the entries are part of the change). Evidence: `foundations/decisions.md` WAY-307 and WAY-306 *Rationale* paragraphs, compared with the template lines quoted above. Offered fix: drop "one more file kept with the spec, which reaches ... directory" to "the cost of keeping the copy", and "and no automatic check finds that" to a statement of the risk only.

2. `task-cycle/skill/spec_review.md:6-8` and WAY-307 *Verification*. WAY-307's `complies` example says the dispatch of the review of the revision "names both" and `violates` says it leaves the reviewer to find the earlier version. The orchestrator's file `spec_review.md` (the sentence the task fixes word for word: "keep the spec as `spec-reviewed.md` beside it; ... comparing the two") does not say that the copy goes into the dispatch; that is said only in the reviewer's method, `task-cycle/spec/SKILL.md:18-20` (the dispatch carries it). An orchestrator who follows only `spec_review.md` and not the reviewer's method may still omit the path, which is the exact gap question 3 of the task wanted to close for the reviewer. Not Important: the task fixed these words and "comparing the two" implies the reviewer gets both; the reviewer's method now says what the dispatch holds. Lies within the task, but fixing it needs words beyond the task's quoted sentence, so it is the cycle's call. Evidence: `spec_review.md` text above; `foundations/decisions.md` WAY-307 *Verification*.

## Coverage of the task (checked by reading the files at head, not by the author's script)

- *To do* 1, `task-cycle/skill/SKILL.md:415-420`: the sentence matches the task's quote word for word (wrapping aside). Pass.
- *To do* 2, `task-cycle/skill/return_step.md:10-11, 19`: "or a term used against its entry" removed, the rest of the PR #75 sentence unchanged (question 1's answer); "A term used against its entry takes the use corrected and no entry." added as the last line of the paragraph. A line rewrap moved "true that the foundation step missed" onto a new line; words unchanged. Pass.
- *To do* 3, `task-cycle/skill/spec_review.md:5-8`: matches. Pass.
- *To do* 4, `task-cycle/spec/SKILL.md:18-20` and `task-cycle/spec/review.md:18-20`: both match. Pass.
- *Out of scope*: `git diff 52889bc..HEAD -- task-cycle/review` is empty. Pass.
- *Settlements to record*: row 1 is carried by WAY-306 (question; entries named by the orchestrator, not the reviewer; range = commits of the merge; the accepted risk and the three rejected ways with their reasons, including the I-1 case of `loop2` in `Rejected`; the "13 of 17" count left out per the template). Row 2 by WAY-307 (copy kept, reviewer compares; both rejected ways with their reasons). Faithful to the rows; nothing added that the rows do not hold except the derivation of the binding sentence's closing clause "the review ends as WAY-162 gives" (task *Decisions in play*, WAY-162 line: "przegląd scalenia kończy się tak jak dotąd"), which the task supports.
- The entry for *To do* 2 is correctly not written (WAY-11 unchanged; task: "wpisu tu nie trzeba"); the part map needs no change (no file added, moved or removed).
- Nothing added that nobody asked for in the five skill files; the two entries are the only addition and both are asked for.

## Against the foundation

- WAY-306 and WAY-307 compared with `elements/decisions/template.md` read whole: heading is a question; binding sentences are 2 and 1, present tense, no normative words; *Scope* `task-cycle` is a part of the map (the foundation check reports no unknown part); *Relations* use the closed list; *Verification* is a pair of examples, no invariants; *Origin* `none`; *Based on* `none` (no outside source rests on them); numbers are the next free ones (WAY-305 was last; nothing else holds 306/307; no withdrawn number holds them). Placement before *Withdrawn identifiers*. Pass.
- Restatement (WAY-263): WAY-306 binding sentences vs step 12: the skill sentence says "where that changes the reviewed code", "asks whether the two sides still hold together", "names the foundation entries the merge brought in that bear on the parts the change touches (WAY-150)". The decision says the same, narrower in no place; it adds "by identifier", the orchestrator's choice and the reviewer's range, all of which the task and WAY-150 give. WAY-307 binding sentence vs `spec_review.md` and the reviewer's method: same. No departure beyond Minor 2.
- WAY-150 and WAY-162 (read selectively, see reaches): the new decisions do not collide; `derives from` is right. No invariant is written or changed; no invariant test changed.
- Guidelines: the change writes no code and no product guidelines; no guideline of a touched part is reached beyond `elements/common/way_of_working.md` reading rules. A step-by-step read of `product-guidelines/reading.md` was not needed: the touched parts are `task-cycle` (prose of skills) and the foundation file; see Searches.

## Declined to judge

- Whether WAY-306's broad question will in practice make merge reviewers judge the change from the beginning: the human accepted the risk (task row 1, 2026-11-06); not a defect of this change.
- Whether `task-cycle/review/SKILL.md` should say that the dispatch of a merge review holds the question and the entries: the task puts it out of scope.
- The whole gate and its other tests: the orchestrator's run.

## Checks

| Check | Result |
|---|---|
| `git rev-parse HEAD` | `3601aba4d9277868e8291ffe190c49427bdeb4a6`, matches the dispatch |
| `git diff 52889bc..HEAD --stat` and `git diff 52889bc..HEAD -- task-cycle foundations/decisions.md`, read whole | six files, 84 insertions, 10 deletions |
| `git diff 52889bc..HEAD --stat -- task-cycle/review` | empty (exit 0) |
| `python -B elements/common/foundation_check.py` | `0 errors`, exit 0 |
| `python -B gate/run_tests.py task-cycle` | 151 tests OK, exit 0 |
| `git status --short` in the worktree | clean (nothing changed by the review besides this report in the ignored `.runs`) |
| Manual: each of the six quoted sentences of *To do* 1-4 read against the diff | all present word for word; wrapping differs |
| Manual: `git grep` for the old phrases ("revises the spec once", "term used against", "reconciliation", "review the merge") over the repo outside `docs/task-cycles` | no other file restates the changed sentences; WAY-162's mentions of the reconciliation stay valid |
| Manual: `grep -n "WAY-306\|WAY-307"` outside the two entries | no references (no referrers to renumber) |

Not run: the whole gate (the orchestrator's).

## Reaches beyond the dispatch

- `elements/decisions/template.md`, read whole: to judge the form of the two new entries (section 2, the foundation entries the change writes).
- `foundations/decisions.md` WAY-306/WAY-307 entries whole; `grep` for `^### WAY-30x`, `reconcil` and `WAY-306|WAY-307` in `foundations`, `elements`, `task-cycle`: to confirm numbering and that no other entry restates the changed sentences. WAY-150 and WAY-162 were not re-read whole: the task quotes their binding passages and I judged only that the new entries cite them correctly; the quoted passages and the entries' relations agree.
- `task-cycle/review/whole_change.md`, read whole: the method of this variant, named by section 1.

## Searches not found or unclear

- The handoff says the step-12 sentence is "now at `task-cycle/skill/SKILL.md:415-420`"; it is at 415-420. Clear.
- I did not read `product-guidelines/reading.md` or the guidelines of the `task-cycle` part: the change is prose of skills and two decision entries and writes no code or guidelines; whether a guideline of the `task-cycle` part exists that a skill sentence must meet was not searched beyond `git grep` of the changed phrases. Marked unverified, not found to be a gap.
- `elements/decisions/examples.md` not read (the template was enough to judge form). Unclear whether the author's report note on it matters; I found no consequence.
- Otherwise: none.
