# Report — the fix of the findings of the review of the whole change (`make-change`, the fix of a review's findings)

Saved by the orchestrator from the author's returned text; the author's Write tool refused the file
a second time and the author did not work around it. The words below are the author's.

**Status:** done
**Commit:** `ba36539` on `task/locations-file`, on top of `973ee64`. The worktree is clean.
**Check result:** `foundation_check.py`, `task-cycle`, `elements/common`, `project-level` and `agent-instructions` all exit 0. Not run: the full gate (the cycle's run), and `installation`, which is not affected by this fix.

## Files changed
- `foundations/decisions.md` (WAY-320)
- `project-level/backlog_place.md`

## Findings

- **I-1: fixed.**
  - **Binding sentence:** it now reads "No file the repository tracks holds an absolute path or a note link, other than the files that the invariant `tracked-file-private-paths` names, which write example paths in order to find or to test them…". This matches row 3 and the invariant, so the four listed files no longer do what the decision forbids.
  - **Price taken:** the *Rationale* now carries question 2's price. The list of exempt files stands in the invariant, so adding a file shows in the change, and a real path pasted into a listed file passes.
  - **Rejected ways:** *Rejected* now carries question 2's three not-chosen ways with their costs:
    - Skip only lines marked as examples: every example line has to be marked, there is code for the marks, and a real path in a marked line passes too.
    - Allow no exceptions and rewrite the examples: every example is rewritten, the tests and the script's description get harder to read, and every later author of a test has to remember it.
    - Skip all test files and both scripts: a path in any test passes.
  - **Counts:** I left out the task's exact counts (98 places, about 100 lines), because the entry template bars counts in author-written prose.
  - **Violates bullet:** it now says "a tracked file the invariant does not name".
  - **Check:** `foundation_check.py` exit 0, 0 errors; `python -B gate/run_tests.py task-cycle` exit 0.
- **I-2: fixed.** `backlog_place.md` now says "An agent that runs a task cycle does not create or change the locations file (WAY-140)". It no longer forbids writing the backlog entry, which WAY-140 and `task-cycle/skill/SKILL.md` allow.
- **M-1: left as the operational reading, no change.** A dangling path still counts as a missing place in `backlog_place.md`. The finding allows either option and says it contradicts nothing. I did not widen WAY-107 for it. If the orchestrator wants WAY-107 widened, that is one phrase.
- **M-2: fixed.** The example at `backlog_place.md:10` is now marked as the-way's own section, with "the product's name in place of `the-way`" for other products. The sentence at `:28` now reads "the entry `tasks` under <the product's name>".

## Checks

| Command | Exit |
|---|---|
| `python -B elements/common/foundation_check.py` | 0 (0 errors) |
| `python -B gate/run_tests.py task-cycle` | 0 |
| `python -B gate/run_tests.py elements/common` | 0 |
| `python -B gate/run_tests.py project-level` | 0 |
| `python -B gate/run_tests.py agent-instructions` | 0 |
| `python -B task-cycle/private_paths_check.py project-level` | 0 (0 listed) |

## Own-work check
- **Requirement most likely unmet:** the fixed WAY-320 must stay faithful to question 2 and must not contradict the invariant.
- **Check:** I compared the new sentence and the three *Rejected* ways word by word with question 2 of the frozen task, and checked that `foundation_check.py` and the `task-cycle` test still pass.
- **Result:** no contradiction. The `task-cycle` test, which checks that the exempt list equals the files the invariant names, still passes, because the invariant is unchanged.

## Choices
- **Rationale wording:** the added sentence says the list "stands in the invariant". The alternative was repeating the four file names in the decision. I did not, to avoid a third copy of the list.
- **Violates bullet:** I considered adding an example for a rewritten exempt file and dropped it. It would not be a case of code going against the decision, and the finding did not ask for it.

## Searches not found or unclear
- None.
