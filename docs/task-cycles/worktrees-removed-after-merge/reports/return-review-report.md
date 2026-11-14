PASS eb5d28ec86091d2a125b66a6fbb6275e4cae51d3

# Review of the return step's commits (`review-change`, section 2)

Range: `b8a16cc2d40c703c3a6870e0af0973e38667c182..eb5d28e` (one commit, `Keep in the pair of WAY-375 only the part no test holds`). `git rev-parse HEAD` = `eb5d28ec86091d2a125b66a6fbb6275e4cae51d3`, as given. Reviewed worktree untouched (`git status --short` empty).

Counts: blocking 0, Minor 2, out of scope 0.

## The change

`foundations/decisions.md`, WAY-375, the *complies* line of the pair. Before: "a new cycle runs the script before it creates its task branch, and the directory of a merged, clean task that stands beside the repository's own directory is removed without a word to the human; each directory ... reaches the record and the request ...". After: "a new cycle runs the script before it creates its task branch and goes on without a word to the human where the script removed a directory that stands beside the repository's own; each directory ... reaches the record and the request with its name, branch and reason". The *violates* line, the `tests:` clause and the rest of the entry are unchanged.

## Is the corrected line true to the code and to the task

- True to the code. The part removed from *complies* ("the directory of a merged, clean task beside the repository's own is removed") is held by tests: `Fixture` makes the main checkout at `<root>/main` and the task directories at `<root>/wt/...` (`task-cycle/test_remove_merged_worktrees.py:60-63`, `add`), and `test_a_dry_run_removes_nothing_and_apply_removes_only_what_is_marked` (`:338`) and `test_a_merged_clean_pushed_task_directory_is_marked_remove` (`:224`) assert that such a directory is marked and removed. The entry's own `tests:` clause names this ("which directories the script marks for removal and which it keeps"), so the correction keeps in the pair only what no test holds. What stays is held by no test and by the skill: step 4 of `task-cycle/skill/SKILL.md:130-148` runs the script after the fast-forward and before the branch is created and says an exit code other than 0 stops nothing (`:141-143`); the list lines reach the record's item *Directories of earlier tasks kept* (`task-cycle/record_template.md:202-204`) and the request's *Checks* and its plain sentence (`task-cycle/skill/request_template.md:423-427`, `:459-460`). The list lines' format (`- <name> | <branch> | <reason>`, no absolute path) is held by `test_the_list_for_the_cycle_holds_name_branch_and_reason_and_no_absolute_path` (`:320`); that the cycle carries them on is the part no test holds. The skill nowhere has the cycle ask the human before the removal, so "goes on without a word to the human" is what the skill does.
- True to the task. Row 5 (checkouts git names, also outside the repository's directory, no effect in the sense of WAY-140, so no human) is what the line states and the first *violates* example forbids the opposite. Row 2 and the Answer under "Który katalog jest zbędny" are not narrowed or widened by the line: it names no condition of removal. Row 4 (no branch removed) stays in the third *violates* example. The line does not restate the entry's conditions more broadly.
- The line does not say the same as the `tests:` clause in a way that could drift: it holds the cycle's behaviour, the clause the script's.

## Whether the return step missed an entry

I compared each entry the dispatch names with the script (`task-cycle/remove_merged_worktrees.py`), the skill, the two templates and `task-cycle/skill/correction.md`.

- WAY-298 (`foundations/decisions.md:9991-10040`): the sentence "two changes ... outside the task's worktree" and the pair match `SKILL.md:77-81`, `:129-148` and `correction.md:7-12` (a correction fast-forwards or merges and runs no removal: step 4's removal paragraph says "a correction after review does not run it", `SKILL.md:140`). No mismatch.
- WAY-375 (`:12950-13040`): the conditions match the code: clean as git reads it (`--ignore-submodules=none`, `:334`), head on a remote-tracking ref (`pushed`, `:272`), tip the second parent of a merge on the first-parent history (`merged`, `:255`), owned by `task/` prefix or `.runs/task-cycles/` record or a detached base copy under `.runs/` (`describe_owner`, `:356`), only entries of `git worktree list`, never main, the directory run in or from, no branch removed (`remove_entry` runs only `git worktree remove`), nested detached checkouts only where clean and pushed (`judge`, `:373-392`). See Minor 1 for one rule the body does not state.
- WAY-376: matches (`list_ignored`, `:405-417`: paths outside `.runs/`, caches left out; ignored files do not enter the status check).
- WAY-373: no change needed. Its remark that an agent's remainder "stays until the task's directory is removed" is now true of the removal the script makes; the new list follows the same route to record and description.
- WAY-140: no change needed. Its text reserves effects on a server, DNS, keys and accounts for a human; WAY-375 rests on git's own list of checkouts being the repository's state, which the entry says.
- Part map, `task-cycle` entry (`foundations/part_map.md:93-103`): files fall under `task-cycle/**`; the script and its test import nothing of another part; no *Depends on* change is needed. I agree with the orchestrator's answer to leave the script off the trust boundary: it reads only git's output about the product's own repository. I found no invariant (`foundations/invariants.md`, `project-plan-state-evidence`, `:320-330`) or glossary line that the removal makes untrue; the invariant reads the move to *done* from merged history, not from a surviving directory.
- No file of the repository still says the worktree "stays" or is "removed by hand" in a way the change falsifies: `SKILL.md:568` is updated, `reserved_return.md:67` ("Keep the worktree", a returned unmerged cycle) stays true because the branch is not merged.

## Findings

### Critical

none

### Important

none

### Minor

1. `foundations/decisions.md:12952-12961` (WAY-375, first paragraph) — the rule for a loose copy of a base is not stated in the body. The task's Answer under "Który katalog jest zbędny" and *To do* point 4 say a loose `base-check-*` copy is removed only where its name points to a task whose branch is merged, and a nested one goes with its task directory. The body says a detached copy of a base "belongs to a cycle" and that removal needs "its branch is merged", but a detached copy has no branch; the code reads the branch `task/<task>` its name gives, local and remote, and keeps a copy named for no task unless it is nested (`inspect_state`, `remove_merged_worktrees.py:346-355`; `test_a_base_copy_goes_by_the_merge_of_the_task_its_name_gives`, `:307`). The Rationale holds half of it ("a base copy named for no task ... is not for the script to judge"). A reader of the entry alone cannot tell which loose copies go. Why it matters little: the code and tests hold the rule and the entry does not contradict it. Suggested repair: one sentence in the body that a loose copy of a base is removed only where the branch `task/<task>` its name gives is merged and a copy named for no task only with the directory that holds it. Grade Minor because the entry's sentences do not state anything the code does not do; the gap is an omission a reader would resolve by reading the code. This reaches before the return step's single commit; the return step's table lists WAY-375 as "Matches" without naming this rule.
2. `foundations/decisions.md:12978-12980` (WAY-375 pair) against `:10009-10011` (WAY-298 pair) — "runs the script before it creates its task branch" is now in both pairs (WAY-298 says "runs the removal of WAY-375 after its fast-forward ... and before it creates the task branch"). Harmless: the two agree. Repair, if any: let WAY-375's *complies* keep only "goes on without a word to the human ..." and the list reaching record and request.

## Declined to judge

- The fix review's Minor on the glossary's "human action" against WAY-375's "needs no human action" (`foundations/glossary.md:81`): already decided by the handoff of the fix; the return step found the same wording nowhere else and I found none either. Not changed, outside this single commit.
- The code of the script and the skill text of step 4 beyond what the entries state: reviewed by the earlier reviews of the cycle; I read them only to compare with the entries.

## Checks

| Command | Exit | Result |
|---|---|---|
| `git rev-parse HEAD` | 0 | `eb5d28ec86091d2a125b66a6fbb6275e4cae51d3` |
| `git show eb5d28e` (the whole diff of the range, one commit) | 0 | four lines of `foundations/decisions.md` |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `python -B -m unittest task-cycle.test_remove_merged_worktrees` | pipeline shown through `tail`, its own status line `OK` | 46 tests OK in 58 s (the exit code of the shell line is that of `tail`; the line `OK` is the unittest result) |

Not run: the full gate (the cycle's own); `remove_merged_worktrees.py --apply` against any repository.

## Reaches beyond the dispatch

- `task-cycle/remove_merged_worktrees.py`, whole: to compare WAY-375 and WAY-376 with the code.
- `task-cycle/skill/SKILL.md` (diff of the range for steps 4, 5, 12, 14 and the exception paragraph), `record_template.md` and `request_template.md` (diff), `task-cycle/skill/correction.md:1-12`: to check the line and WAY-298.
- `foundations/decisions.md` WAY-373 (`:12845-12880`) and WAY-140 (`:4137-4175`), `foundations/part_map.md:90-125`, `foundations/invariants.md:318-330`, and a grep of `foundations/invariants.md`, `glossary.md`, `environment_facts.md` for "fast-forward", "worktree", "outside": to check the entries named in the handoff for a mismatch after the fix.
- `task-cycle/test_remove_merged_worktrees.py:40-140, 215-230, 333-352` and the list of its test names: to judge what the tests hold.

## Working copies

None made; `.runs/review-return/` was not created. Remainder: none. The unittest run created and removed its own temporary directories.

## Unread material

- The dispatch: read whole (the handoff, `task-cycle/review/SKILL.md`, the frozen `task.md`, the return report). WAY-298, WAY-375 and WAY-376 read whole.
- Not read: `reports/fix-review-report.md` and the earlier reports of the cycle (the handoff does not name them); the tests of the script past the lines listed above, read by name only.

## Searches not found or unclear

- none
