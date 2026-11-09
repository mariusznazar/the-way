# Slice 1 report — The cycle skill's merge, base-check and exception sentences

**Status:** done
**Commit:** `361c9fb` on `task/cycle-technology-decisions-batch` (base `f3b90d5`)
**Worktree:** `the task's worktree root`
**Method:** `task-cycle/change/SKILL.md` (whole) and `task-cycle/change/slice.md`; `agent-instructions/README.md` read as the handoff names.

## Files changed

| File | Added | Removed |
|---|---|---|
| `task-cycle/skill/SKILL.md` | 9 | 6 |
| `task-cycle/skill/correction.md` | 8 | 3 |

Total: 17 added, 9 removed (`git show --numstat 361c9fb`).

## What changed, by item

Each place was found by its content; the line numbers of the handoff were from older commits and were not used.

- **Item 1 (correction merge, both places) — `task-cycle/skill/correction.md`.**
  - The first place (the start, "In the-way itself, before anything else", where the request's worktree gets the remote target branch merged) now says that where that merge changes code the cycle reviewed, it is reviewed and its affected checks run, as the merge in the paragraph below is (WAY-306).
  - The second place (the paragraph "First merge, never rebase, the remote target branch…") now says the full rule: a fresh reviewer reviews the merge with `review-change`, with a dispatch that asks whether the two sides still hold together and names the foundation entries the merge brought in that bear on the parts the change touches, "as step 12 of `implement-task` gives (WAY-306, WAY-150)", and the agents that own the checks the merge touches run them again.
- **Item 2 (step 12 merges the remote target branch) — `task-cycle/skill/SKILL.md`, step 12.** "merge the current target branch" → "merge the remote target branch". The branch creation at step 5 ("Create a task branch from the current target branch") is a different sentence not named by item 2, and was left as it is.
- **Item 3 (the exception) — `task-cycle/skill/SKILL.md`, the paragraph after "Inputs and authority".**
  - The sentence now reads "changes nothing outside the product repository, except the fast-forward of the checkout in step 4 and the account of the request named below".
  - The sentence "The one exception is the cycle's own account…" is now "The account of its request is the cycle's own: …". The paragraph no longer ends with two things each called "the one exception".
- **Item 5 (base-check copy) — `task-cycle/skill/SKILL.md`, step 4, second way of running the base checks.** Added: "In a product that checkout gets its dependencies installed, as the product's own rules give, and its `.the-way` populated before the checks run; otherwise they fail for that reason and not on the base."

No other rule was changed. No `description:` line changed, so `skill_entry_points.py` was not run.

## Checks

| # | Command | Exit code | Result |
|---|---|---|---|
| 1 | `python -B elements/common/foundation_check.py --skip-test-citations` | 0 | "0 errors" |
| 2 | `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` | 0 | Ran 9 tests, OK |
| 3 | `python -B gate/run_tests.py task-cycle` | 0 | Ran 209 tests, OK |
| 4 | `git diff --check` | 0 | no output (run before the commit) |

Failing checks: none. Checks not run: none. The prose has no test of its own; the checks above are the slice's *Checks*, run as named. No invariant test was changed, and no test was written, since the slice is prose only.

## Own-work check (section 3)

- **Requirement most likely missed:** that step 12 and the two correction places now say the same merge rule, so that a reader of `correction.md` alone finds the review and the checks without a second file. Check: `grep` of `task-cycle/skill/correction.md` for `WAY-306` and for `review-change`, and of `task-cycle/skill/SKILL.md` for `remote target branch`. Shows: `correction.md` has the review rule at both merge places; `SKILL.md` has `merge the remote target branch` at step 12 (grep count of "remote target branch" in `SKILL.md`: 2, the other being the existing sentence at step 4). Passed on first run.
- **Second requirement:** that no "one exception" phrasing is left in the paragraph. Check: `grep -rn "one exception" task-cycle/` — the only remaining hit is `task-cycle/skill/request_template.md:64`, a different file, not in this slice. Passed.

## Reaches beyond the handoff

- `task-cycle/skill/SKILL.md` and `task-cycle/skill/correction.md` read whole (both are changed files).
- `.runs/task-cycles/cycle-technology-decisions-batch/plan.md` read whole; `task.md` lines 20–40 read; the WAY-298 and WAY-306 entries and the invariant `tracked-file-private-paths` read at the handoff's current ranges.
- `project-level/technology/reserved_choices.md` was not read: no part of the slice needed a choice settled by the reserved list, so the reserve did not apply.

## Searches not found or unclear

- `task-cycle/skill/SKILL.md` step 4, the sentence "the one change the cycle makes outside the task's worktree" (about the fast-forward). Now the paragraph names a second exception (the backlog account), so step 4's "the one change" reads as contradicting it. It is outside this slice's *Change* and was left unchanged. Question for the orchestrator: should step 4's phrase be reworded in the slice that touches it, or in a later slice? The decision WAY-298 also has the sentence "The fast-forward is the one change the cycle makes outside the task's worktree", so the decision text and the skill's phrase are the same words.
- `task-cycle/skill/SKILL.md` step 5, "Create a task branch from the current target branch" — not named by any item of the slice; left unchanged. Noted for completeness.
- `task-cycle/skill/request_template.md:64`, "The one exception is the heading of the task's…" — a different file, not in this slice; left unchanged.

## Choices made

- **Correction merge wording.** Chose to state the full rule in both merge places rather than make the first place a cross-reference only. Rejected: the cross-reference alone, because the first place is read before the paragraph below and the reader would have to jump. Cost if wrong: the two copies can drift when step 12 changes; the next slice touching step 12 should compare them.
- **Exception wording.** Chose "The account of its request is the cycle's own" instead of keeping an enumeration with "The second exception". Rejected: the enumeration form, which reads as a list of two exceptions in the same paragraph. Cost if wrong: none expected; a reader can still see the account is the second exception from the first sentence.

## Problems observed

- The conflict of step 4's "the one change" with the new second exception (see *Searches not found or unclear*). Observed by reading the text; not a test failure.

## Adaptations of section 4

None. The plan matched the code: each place was found by its content and its text matched the item's description; no structural mismatch.
