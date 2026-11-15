PASS 6727b67a34c54c9b6b6c7cae793c2e2681b9cdc9

# Review of the whole change: cycle-after-foundation-review

Range `739c8139bc7f2e74ef0f4c2f0a76a4352614cfd6..6727b67` (one commit, one author, no plan, no slices).
`git rev-parse HEAD` in the worktree is `6727b67a34c54c9b6b6c7cae793c2e2681b9cdc9`, the head given. The
worktree stayed unchanged (`git status --short` empty after my runs).

Counts: blocking 0, Minor 3 (2 within the task, 1 outside it), out of scope 1 (the same outside one).

## Against the task

Each item of *To do* and each row of *Settlements to record*, checked against the diff:

| Item or row | Met | Where |
|---|---|---|
| 1, row 1: clause on the first clearing removed from WAY-375 | yes | `foundations/decisions.md` WAY-375 second paragraph; grep finds "first clearing" only in the *Rejected* where the way not chosen is named |
| 2, row 3: WAY-376 sentence and *Rationale* give the list to the dry run a human starts | yes | WAY-376 binding sentence, *Rationale*, *Rejected*; the script prints the list under each `remove` with and without `--apply` (`task-cycle/remove_merged_worktrees.py` docstring, lines 48-53), so the text is true; the step of the cycle is unchanged |
| 3, row 4: base copy the script does not assign stays for the human; contradicting *Rejected* item removed | yes | WAY-375 first paragraph, *Rationale*, *Rejected*; matches the script (`inspect_state`, lines 346-353: branch not found; named for no task) |
| 4, row 2: `narrows WAY-13` in *Relations* and the area in the binding sentence | yes | WAY-375 *Relations* and last sentence of the second paragraph; WAY-13 binding sentence unchanged; no chain (WAY-13 *Relations* `none`) |
| 5: subject in the WAY-13 *Verification* example | yes | WAY-13 *Verification*, "an agent treats a large task …" |
| 6, rows 5-6: first red run of the gate stays the gate's result | yes | `task-cycle/skill/SKILL.md` step 10 paragraph (lines 489-493) and WAY-261 second paragraph; WAY-243 and the testing template untouched, as row 6 says |
| 7, row 7: "fix it" on a manual request | yes | `agent-instructions/README.md` "Integrate into `foundations`" |
| 8: kind 16 in the three lists | yes | `task-cycle/skill/correction.md` list; row "A correction" of `task-cycle/skill/request_template.md`; WAY-289 binding sentence and *Rationale*. The task places the list "An answer to do it in this request … other than item 8" in WAY-289; it stands in `correction.md` (author's problem 1, confirmed by me: WAY-289 holds no such text). The author changed both places, which meets the item's purpose |
| 9: example of kind 17 cannot be read as "the task required a defect" | yes | `request_template.md` kind 17, the sentence now reads "your remark, and the cycle judged that the task required what the remark asked to change" |
| 10: state line names what started the correction | yes | `request_template.md` row "A correction": three phrases, one for each source of the pairs of kind 17; no script reads the phrases (`git grep` finds them only there) |
| 11: exception for the screenshot shown to the human | yes | `SKILL.md` "Working copies", first paragraph; agrees with `task-cycle/change/ui_check.md` and WAY-316 |

Nothing added that nobody asked for beyond the items; WAY-289's *Rationale* and WAY-261's *Rationale* and *Rejected*
sentences carry the rows' own reasons and rejected ways (WAY-134). The wording of both
new *Rejected* ways follows the *Not chosen* of the task's questions.

No invariant, no test and no part of the part map changed; no changed invariant test to name. No reserved choice is
taken. The change touches no trust boundary and holds no operation that cannot be undone (it words rules about a script and does not change it).

## Findings

### Critical

none

### Important

none

### Minor

1. **Within the task.** `task-cycle/skill/request_template.md`, paragraphs **Checks** (line 466) and **Findings outside the task's scope** (line 500), against WAY-261's new second paragraph and `SKILL.md` step 10 (line 492). The sentence binds the request to name the flaky test and the task that fixes it, or to propose one. The place that the template gives for such a test, *Findings outside the task's scope*, asks only for its file path, its rerun's result and its counts, and *Checks* only for the counts and the rerun's result; neither says where the fixing task or the proposal stands. The orchestrator that writes the description will do it from the skill's step, since it can put the words beside the check, but the form that the description is checked against does not carry the new part, so different requests will word or omit it differently, the pattern of nine requests the task cites. The task's *To do* 6 names no change to the template (the author's problem 3 says the same), so no blocking claim; the fix is one clause in the sentence of *Findings outside the task's scope*. Evidence: `grep -n "task that" task-cycle/skill/request_template.md` shows no clause for it.
2. **Within the task.** `foundations/decisions.md` WAY-375, third sentence of the first paragraph ("… a copy of a base that the script does not assign to a task — one named for no task, or for a branch it does not find — among them, and a detached checkout nested in a directory that is removed goes with it …"). The script keeps a base copy named for no task only where it *stands alone*; nested in a directory that is removed it goes with it (docstring of `remove_merged_worktrees.py`, lines 36-38: "a copy named for no task never stands alone"; `inspect_state` lines 352-353). The sentence has no "stands alone" for the copy named for no task, and the skill's own `.runs/base/` copy is such a copy nested in a task's directory. The next clause ("a detached checkout nested … goes with it, whatever its name") covers the nested case, so a careful reader reaches the right answer; a reader of the first clause alone reads that the usual base copy stays. Add "standing alone" after "a copy of a base". Not tested by any test (the tests quote only the sentence's start).
3. **Outside the task.** `task-cycle/skill/SKILL.md` "Working copies" first paragraph (new exception for a screenshot shown to the human) against WAY-373, whose binding sentence lists "a screenshot" among the working copies that stand in the agent's directory under `.runs/` with no exception, and against WAY-316, which says where a screenshot shown to the human lies but has no `narrows WAY-373`. The skill now carries a precedence that no decision records; WAY-25 requires the precedence to stand in the decision that prevails. The author read the two as compatible (a screenshot shown to the human is no copy made "to check something"), and that reading is reasonable; the task's item 11 names the skill only. A later reader who reads WAY-373 alone gets the old rule. Proposed fix, for a later task: in WAY-373 say that a screenshot shown to the human is outside the sentence (or record `narrows WAY-373` in WAY-316). This lies outside the task.

### Out of scope

The Minor finding 3 above (graded Minor, outside the task).

## Declined to judge

- `task-cycle/skill/request_template.md` row "A correction": the new state-line phrases ("corrected for your answer to an item", "refreshed from the target branch at your request") are the author's words, since the task fixes only "corrected for your remarks"; I judged them to follow the task's own instruction ("to, co ją uruchomiło, z tych samych par źródeł"), and no script reads them. Whether the human wants other words is his taste.
- `ui_check.md` holds both "keep none" and "move it … where none is settled into your directory" (author's problem 4): untouched by the change and outside the task.
- WAY-289's *Verification* does not name the answer for kind 16: the task did not ask for it; WAY-289's binding sentence and the three lists carry it.
- The two loose base copies and `agent-path-to-running-product`: the task puts them out of scope.

## The structure of the code the change leaves

`python -B task-cycle/change_file_sizes.py 739c8139bc7f2e74ef0f4c2f0a76a4352614cfd6 6727b67`, exit 0:
`agent-instructions/README.md` 102 to 109 (+7), `foundations/decisions.md` 9485 to 9522 (+37),
`task-cycle/skill/SKILL.md` 747 to 753 (+6), `task-cycle/skill/correction.md` 88 to 91 (+3),
`task-cycle/skill/request_template.md` 538 to 539 (+1); +54 lines in all. The change holds no code
(no function, no script), and the-way has no coding guidelines with a rule of size, so there is no test of the invariant of the rule of size to run in worktrees of the base and head; the numbers above and the diff are my material. No code has lost its user; no name stopped being true (the clause of WAY-375 that used "human action" is gone and the glossary entry stays unchanged, as the task says). The row "A correction" of the variants table in `request_template.md` grew to a very long single line (the author's problem 5; a table row cannot be wrapped); a structure finding there would be Minor and I make none.

## Checks I ran

| Command | Exit | Result |
|---|---|---|
| `git rev-parse HEAD` | 0 | `6727b67a34c54c9b6b6c7cae793c2e2681b9cdc9` |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors`, no `listed:` line |
| `python -B gate/run_tests.py task-cycle` | 0 | 483 tests OK (the directory that holds `test_remove_merged_worktrees.py`, which cites the sentences of WAY-375 and WAY-376) |
| `python -B gate/run_tests.py agent-instructions` | 0 | 25 tests OK |
| `python -B task-cycle/private_paths_check.py foundations/decisions.md` | 0 | `checked: 1 files, 0 listed` |
| `python -B task-cycle/change_file_sizes.py <base> <head>` | 0 | table above |
| `python -B elements/common/decision_index.py --sections` and `--section/--part/--decision` selection | 0 | index in `.runs/review-whole/index.md` |

Manual checks: compared the docstring and `inspect_state` of `task-cycle/remove_merged_worktrees.py` with the new sentences of WAY-375 and WAY-376 (they agree); `git grep` for "first clearing", "gathered before", "hand clearing", "corrected for your" over the tracked files (hits only in *Rejected* entries and in the one template row). Not run: the whole gate (the orchestrator's), `installation` and `process-audit` directories (no file they check changed).

## Reaches beyond the dispatch

- `task-cycle/remove_merged_worktrees.py` (lines 1-130 and the `inspect_state` region by grep, lines 340-370 read through grep context): to check that WAY-375 and WAY-376 state what the script does; the task asks the wording to be true.
- `task-cycle/change/ui_check.md` (whole) and `task-cycle/skill/SKILL.md` lines 125-165, 440-520 and 305-335 (read): to check items 6, 11 and the step of removal.
- WAY-160 and WAY-316 (whole), WAY-243 (whole): to check the new text of step 10 and WAY-261 against them.
- `agent-instructions/README.md` lines 40-125 (read): the section the item 7 sentence joins.
- `foundations/part_map.md` (whole) to name the parts.

## Unread material

Decisions of the index of my selection read whole: **9** of the 32 listed in full (WAY-13, WAY-25, WAY-243, WAY-261, WAY-289, WAY-316, WAY-373, WAY-375, WAY-376); and WAY-160, which the index lists by heading alone, I opened whole as well (10 in all). I read the index of the whole selection (the 32 in full and the 111 by heading alone) and ran through the 111 headings: none of them, beyond WAY-160, bears on the change.

The other 23 decisions listed in full I read by their binding sentences in the index, not whole: WAY-14, WAY-24, WAY-30, WAY-114, WAY-313, WAY-314, WAY-315, WAY-11, WAY-125, WAY-135, WAY-136, WAY-148, WAY-229, WAY-164, WAY-255, WAY-260, WAY-365, WAY-227, WAY-287, WAY-288, WAY-294, WAY-295, WAY-300. Each reaches the change only as a neighbour in the same part or section; WAY-287 (cited by WAY-289 and by kind 16) and WAY-30 bear on the request's items for the human, which the change does not rewrite. WAY-164 I read through the author's own-work check.

No guideline file: the-way has no `guidelines/` directory (`product-guidelines/reading.md` read whole to confirm the selection). The invariants file (`foundations/invariants.md`), the glossary (`foundations/glossary.md`) and `foundations/environment_facts.md` I did not open whole; the change changes none of them and I found no invariant that cites a sentence the change edits (the foundation check lists none). WAY-140 and WAY-153, which WAY-375 derives from, I did not open: the change rewrote neither of them.

## Searches not found or unclear

- The list "An answer to do it in this request, to an item of *Fix or let through* other than item 8, …" which the task's *Decisions in play* places in WAY-289: not in WAY-289; it stands in `task-cycle/skill/correction.md` (lines 75-87). Not found where the task says; found elsewhere.
- Where the request names the flaky test and the task that fixes it (item 6): the template has no clause for it (Minor 1).
- Any rule that a request's state line depends on a red gate: searched `SKILL.md` and `request_template.md` for "red", "gate fails", "gate failed"; found none, so the new sentence of step 10 contradicts no other step.

## Working copies

None remain except the index of my selection, which the handoff asks for: `.runs/review-whole/index.md`. I made no worktree and no clone. The logs of my test runs and the list of sections stood in `.runs/review-whole/` and were removed. The reviewed worktree is unchanged.
