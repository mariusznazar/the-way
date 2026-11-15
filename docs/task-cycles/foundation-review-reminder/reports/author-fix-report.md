# Author fix report — foundation-review-reminder

**Status:** done. All five Minor findings fixed; none contested.

## Commits (from reviewed head `b7ec371`)

1. `9638c91` — Fix the Minor findings of the whole-change review: `task-cycle/skill/SKILL.md`, `task-cycle/skill/request_template.md`, `foundation-review/proposals.md`, `foundation-review/weak_points.md`, `foundations/decisions.md`.
2. `31f7507` — Rewrap the lines of WAY-24 and WAY-300 that the fix left over 100 columns: `foundations/decisions.md` (the first commit's own new lines were long; I rewrapped them).

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` — 0 (`0 errors`), run after the last edit of the log.
- `python -B gate/run_tests.py task-cycle` — 0, 480 tests OK; run after the edits of `task-cycle/skill/` and before the two rewraps of `proposals.md` and `decisions.md`, which are no files of that directory.
- `python -B task-cycle/test_review_reminder.py` — not run: the script and its test are untouched.
- Not run: the full gate, as asked.
- Line width: `awk 'length>100'` over `foundation-review/proposals.md`, `weak_points.md`, `with_the_human.md` — no line over 100 columns left of mine.

## Findings

1. **`weak_points.md`, "own piece of work" vs "own change" — fixed.** The sentence now reads "A rule that ends with its own change fails the plan test and gets no line here, as it gets none above (WAY-36)." It uses the same words as the transitional section and sends the entry to no list. Shown by reading the two sections side by side.
2. **WAY-24 and WAY-300 *Rejected* — fixed.**
   - Both entries now reject "a sentence that asks for no line and says nothing of the backlog, the human's own setup adding the line" in place of "only the setup of one user, with the wording of this decision as it was"; the history is gone.
   - WAY-24: the second kept way is now "a task of the review made ready for a cycle and copied into the backlog — three steps where one command does", so it no longer rejects the line a human adds as a mark. The first kept way ("run by a cycle …") stays as the reviewer found it saved by those words. `foundation_check.py` 0 errors.
3. **Source of "the name of the repository" — fixed.** Choice: step 13 now says the name is the last segment of the address of the remote `origin` of the repository the request merges into, without `.git`, or, with no such remote, the name of the directory its main checkout stands in; it is the same in every cycle and every worktree "whatever the `## Backlog` section names". The qualifier "as the `## Backlog` section names the product" is gone. The template says "taken as `SKILL.md` step 13 gives it", and WAY-300's second paragraph says the name "is the same in every cycle", so the three texts agree. For this repository the rule gives `the-way` (origin `…/the-way.git`), and for a product whose section names a directory or a public tracker it gives its own name. Rejected: the name of the directory of the checkout alone (a worktree's directory, as this task's `foundation-review-reminder`, would give a different name in each cycle, the very harm the reviewer names); the name the section gives (fails for a section with no name, as the reviewer finds); leaving "the name of the repository" bare (no source, so two cycles may pick two names). Cost if wrong: a product whose remote is renamed changes its line's expected name once; the sentence the cycle writes always states the name it expects, so the human sees it.
4. **Failed count among the checks not run — fixed.** Step 13 now adds to the exit-2 clause "and put the count among the checks not run in the section for the human's decisions (WAY-287)". My choice 6 stays otherwise as it was.
5. **Two lines over width — fixed.** `proposals.md` paragraph and `weak_points.md` line 4 rewrapped at 100; no lines of those files of mine exceed 100 now. (Lines over 100 columns that already stood in `foundation-review/SKILL.md` and `remarks.md` are not mine and untouched.)

## Own-work check

- **Requirement most likely unmet:** the fixed name has to be a name the orchestrator can really compute in a worktree and a product. Check: `git remote get-url origin` in this worktree gives `https://github.com/mariusznazar/the-way.git`, so the last segment without `.git` is `the-way`, the same in the worktree as in the main checkout. It showed the rule holds here; I did not test a product with a `.the-way` submodule, where the remote of the product (not of `.the-way`) is the one meant, which the sentence says by "the repository the request merges into".
- The three texts (step 13, template, WAY-300) say the same of the name; read side by side.

## Reaches beyond the handoff

- `git remote get-url origin` — to check the name rule against this repository.
- `foundations/decisions.md` WAY-287 (lines near 6467), read to the *Verification* line, for finding 4.

## Unread material

none beyond what the handoff names read in part: `reports/review-whole-report.md` was not read; the findings file was enough. `task-cycle/change/fix.md` read to its end.

## Searches not found or unclear

- None new. The earlier open point (source of the repository's name) is the one finding 3 closes.

## Working copies

None made in this fix; `.runs/author/` holds nothing (the one output file of the gate run was removed).
