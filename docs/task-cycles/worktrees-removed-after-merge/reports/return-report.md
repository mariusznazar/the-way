# Return step report — worktrees removed after merge

**Status:** done

**Commit:** `eb5d28e` (Keep in the pair of WAY-375 only the part no test holds). Head before the step: `b8a16cc`.
Range of the whole change: `835344f..HEAD`.

## What I compared, and what I found

| Entry or file | Compared with | Result |
|---|---|---|
| WAY-298 (row 1) | `task-cycle/skill/SKILL.md` step 4 and the exception paragraph; `correction.md` | Matches. The sentence says the fast-forward (the-way only) and the removal at each new cycle's start (WAY-375) are the two changes outside the task's worktree; step 4 runs the script after the fast-forward, before the branch is created, and says a correction does not run it. |
| WAY-375 (rows 2, 4, 5) | the script as fixed, its docstring, its tests | Matches: clean as git's own check reads it (`--ignore-submodules=none`), commits on the remote, second parent of a first-parent merge, a branch `task/…` or holding `.runs/task-cycles/` or a detached base copy, nested detached checkouts only where clean and pushed, only `git worktree list` checkouts, never the main checkout, the directory the script runs in or holds, no branch removed. |
| WAY-375 pair of examples | the tests | One correction made: the *complies* line named the removal of a directory beside the repository's own, which tests hold (`tests:` clause); I kept in it only what no test holds (the cycle's run before the branch, going on without a word to the human, the list reaching record and request). |
| WAY-376 (row 6) | the script and tests | Matches: ignored files do not count, ignored paths outside `.runs/` listed per directory marked, known caches left out. |
| Row 3 | `SKILL.md` step 4/5/14, `record_template.md`, `request_template.md` | Written and consistent with the code: the list lines are `- <name> | <branch> | <reason>`, no absolute path (reasons are fixed texts, test-held); record item *Directories of earlier tasks kept*; *Cost* sentence and *Checks* lines. |
| WAY-373 | skill and decision text | No change needed: the remainder of an agent's working copy goes with the task's directory, which the script now removes after the merge; its route (record and description) is the one the new item follows. |
| WAY-140 | WAY-375 second paragraph, SKILL exception paragraph | No change needed: the script's removal is a change to the repository's state, not a server, DNS, key or account. |
| WAY-153 | script reasons | A closed-unmerged request's directory is kept with the reason "no merge git can see… or its request open or closed": as the decision brings it to the human. |
| WAY-269 | script | No conflict: it removes no branch; a returned, unmerged cycle's directory stays because its branch is not merged. |
| Part map, `task-cycle` | the new files | No change. The files fall under `task-cycle/**`; the script and test import nothing of another part (the test imports the script of its own part), so *Depends on* needs nothing; the script is **not** added to the trust boundary, as the orchestrator answered (it takes in only git's output about the product's own repository). The *External context* rows (git trusted, a user's places outside every repository) already cover what it reads and removes; I changed nothing there. |
| Invariants | `foundation_check.py` | No invariant written: no row or decision sets a rule an invariant would state. |
| Glossary | the change's terms | No entry: "merged branch", "base copy", "belongs to a cycle" are defined in WAY-375's own sentences (WAY-95). |
| Environment facts | WAY-375, WAY-376 | None written. The decisions rest on the structure of merge commits, which is not a cited source whose change would call them into question (WAY-90); the details of git the code reads (`worktree list --porcelain -z`, the wording of git's refusal for a submodule) are held by tests, not by the decisions. |

The fix review's new Minor (the glossary's "human action" against WAY-375's "needs no human action"): the same
wording stands nowhere else. The skill's exception paragraph names the removal as an exception to "changes nothing
outside the product repository" and does not use "human action"; no other file says it. Not changed, as the
handoff says.

## Foundation entries for the request (*Foundation entries*)

- WAY-298 — `row 1` — The fast-forward, made only in the-way itself, and the removal of finished tasks' working directories that every new cycle runs at its start are the two changes the cycle makes to checkouts outside the task's worktree.
- WAY-375 — `row 2` (carrying rows 4 and 5) — At its start a cycle removes an earlier task's working directory only when its tree is clean, its commits are on the remote, its branch is merged and it belongs to a cycle, touching only checkouts git names and never a branch, and that removal is no effect outside the repository in the sense of WAY-140.
- WAY-376 — `row 6` — A file git ignores does not count against a clean tree, and the script lists each removed directory's ignored paths outside `.runs/`, known caches left out.
- Row 3 — no entry: written in `task-cycle/skill/SKILL.md`, `task-cycle/record_template.md` and `task-cycle/skill/request_template.md`.
- Return step record: decisions written or changed: WAY-298, WAY-375, WAY-376; invariants: none; environment facts: none; glossary terms: none; part-map changes: none; projected entries: none.
- Marked `the cycle's`: none (the first-parent reading and the nested-checkout and cycle-record rules in WAY-375 are the writer's wording of rows 2 and 5 and are stated in the entry).

## Checks (command, exit code)

| Command | Exit | Result |
|---|---|---|
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` (after the one edit) |
| `python -B gate/run_tests.py task-cycle` | 0 | 440 tests OK |

Not run: the full gate (the orchestrator's); no `--apply` anywhere.

## Unread material

- none beyond the handoff's: `task-cycle/skill/return_step.md` and `foundation_step.md` read whole; the fix
  review's new Minor read from `reports/fix-review-report.md` (its lines on the Minor and the checks), the rest
  of that report not read.

## Searches not found or unclear

- none

## Working copies

None made in this step (no throwaway repository; `.runs/` holds only `task-cycles/`). Remainder: none.
