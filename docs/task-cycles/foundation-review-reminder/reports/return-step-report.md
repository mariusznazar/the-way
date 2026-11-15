# Return step report — foundation-review-reminder

**Status:** done. One commit: `e5ae875` (from head `31f7507`).

## Foundation compared with code

Compared at `31f7507`: WAY-24, WAY-300 (written by the change); WAY-140, WAY-161, WAY-107, WAY-22, WAY-36, WAY-293, WAY-328, WAY-344 (named by the task); the part map entries `decisions`, `task-cycle`, `foundation-review`; and the entries of the search made in the foundation step (WAY-24's other references; WAY-33, WAY-12, WAY-05 for form), against `task-cycle/review_reminder.py` and its test, step 13 of `task-cycle/skill/SKILL.md`, `request_template.md`, `README.md` and the four files of `foundation-review/`.

- **No longer matching, corrected (one):** WAY-300 carried a pair of examples for a rule whose count and threshold sentences tests hold. The return step's rule asks that a part a test holds leave the pair and be named by the clause `tests:`. Done:
  - lines `decision: WAY-300 "…"` stand at five tests of `task-cycle/test_review_reminder.py` (comment lines only, no code): the three tests of the count since the nearest review tag, the one of the main branch's merges into task branches, and the threshold test hold the quotation "At the end of every task cycle the orchestrator counts the merges"; the no-tag test and the threshold test hold "The reminder blocks nothing, the threshold is one number";
  - WAY-300 *Verification* now begins with `tests:` naming the count since the nearest review tag (from the start of history where none stands, merges of the main branch into task branches left out), the reminder line turning to yes at the threshold and not one merge before it, and the one threshold; the pair stays only for the cycle's and the request's part, and its example "the count leaves out the merges of the main branch into task branches" left the pair because a test holds it.
  - I also rewrapped the ragged lines of the second binding paragraph of WAY-300 (no change of words).
- **Everything else matched:** the script gives 60 and exit 2 as WAY-300 and the template say; step 13, the template and WAY-300 say the same of the two forms, the unreadable backlog, the name of the repository, and that below the threshold nothing is written; WAY-24's binding sentences match `foundation-review/SKILL.md` (the review is a run of the skill, a line may stand, a human adds it); WAY-140, WAY-161 and WAY-107 are kept (the cycle only reads the backlog and takes the meaning of "open" from the task place); WAY-22/WAY-36/WAY-293 are applied (the number stands in code with test and comment, none in the log); the part map entries describe their parts as the files stand; WAY-328 and WAY-344 are not touched by the code (no new file read by the script).
- Not corrected, by the handoff: the lines of WAY-300 *Rejected* over 100 columns (the fix review's new Minor finding) — left to the request's list.

## Decisions written or changed

WAY-24 and WAY-300 (foundation step); in this step WAY-300's *Verification* only, as above.

## Invariants written or changed

none. No rule here is set by the task, a decision or the human as a rule a commit can break and a test check by itself; the existing invariants named in the handoff (`skill-entry-points`, `tracked-file-private-paths`, `script-*`, `test-method-citation`, `cross-part-imports`, `return-step-record`) hold, shown by the `task-cycle` gate run below.

## Environment facts

none. The change rests on no source outside the product.

## Glossary terms

none. No word is used in a meaning WAY-95 gives an entry (the words "reminder", "line of the review", "threshold" carry their ordinary meaning).

## Part-map changes

none. The files of the change lie in `decisions`, `task-cycle`, `foundation-review` and the root `README.md`, which the map leaves out on purpose; no part or dependency was added.

## Projected entries written

none.

## Rows of *Settlements to record*, and where each went

Each row stands as the foundation step wrote it; this step found no row missed.

- row 1 → sentence (second paragraph) of WAY-300.
- row 2 → sentence of WAY-24.
- row 3 → skill files of `foundation-review/` (`SKILL.md`, `weak_points.md`, `proposals.md`, `with_the_human.md`); no entry.
- row 4 → code and test: `THRESHOLD = 60` with its comment in `task-cycle/review_reminder.py`, held by `test_the_reminder_starts_at_sixty_merges_and_not_at_fifty_nine`; no entry.
- row 5 → sentence (first paragraph) of WAY-300.

**Choices that bind after the merge, placed by the questions of the decisions template** (the orchestrator's answers of record rows Q4 and Q5); each is an instruction for how an agent works that stands in one skill step with one sentence of its reason, so, as WAY-293 gives for this repository's log, no entry is written:
- the source of the repository's name (last segment of the `origin` address, else the main checkout's directory name) — `SKILL.md` step 13, reason in its sentence ("the same in every cycle and in every worktree"); the template and WAY-300 point to it;
- the reaction to exit code 2 of the script (record the message, write no reminder, put the count among the checks not run) — step 13, reason "since the count is unknown";
- the sentence about marking an open line done — `foundation-review/SKILL.md` step 7, reason in the sentence ("an open line makes the next reminder point to it instead of asking for a new one").
- the cycle's own: none.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` — 0 (`0 errors`). With one quotation altered by a letter it gave `4 errors` ("the quotation stands in no binding sentence of `WAY-300`"), so it reads the new lines; I restored the text.
- `python -B task-cycle/test_review_reminder.py` — 0, 11 tests OK.
- `python -B gate/run_tests.py task-cycle` — 0, 480 tests OK.
- Not run: the full gate, as asked.

## Unread material

none.

## Searches not found or unclear

none.

## Working copies

none left; the one backup file and one output file I made in `.runs/author/` were removed.
