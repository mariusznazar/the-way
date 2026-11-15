# Author fix report — fix 1, decisions-list-in-refinement

**Status:** done

**Fix range:** `51f2590..b084a4a` (one commit, `b084a4a`, staged by explicit paths; I amended my own unpushed commit once to rewrap one line that stayed over 100 characters).

Files: `foundations/decisions.md` (WAY-377, WAY-378), `project-level/task/skill/final_review.md`, `project-level/task/skill/orchestrated_mode.md`, `project-level/task/skill/SKILL.md`. The table of foundation entries in `reports/author-report.md` is updated for WAY-378 (its meaning sentence now says the check covers the guesses kept from the human too); WAY-377's meaning sentence is unchanged.

## Findings

- **I1 (blocking), fixed, the orchestrator's chosen direction.** `final_review.md` step 3 now reads "For each matter you will show and each guess the critique keeps from the human by judging it already settled in the repository or most likely right, open the file the critique quotes from and check the quotation word for word, then write one explicit verdict … A quotation that does not hold voids the critique's verdict on that matter; settle the matter from what the file says, or count it open." WAY-378's binding sentence now says the agent checks the quotations "before it shows a matter, and before it keeps a guess from the human on the critique's verdict that the repository already settles it or that it is most likely right"; its *Verification* "violates" line, *Rationale* and *Rejected* follow; the *Rationale* price now names the cost (one file opened for each guess kept from the human, bounded by the list) and the remaining gap (a quotation that holds but does not settle). The *complies* example needed no change: it now happens under the skill's text. `orchestrated_mode.md` points to `final_review.md` for the check, so its words follow without a change of their own. Check: reading the skill step, the orchestrated bullet and WAY-378 side by side (own-work check below); `foundation_check.py` exit 0.
- **M1, fixed.** `orchestrated_mode.md`: "You end your turn with `questions`; the project orchestrator writes the *List* and the *Critique* …".
- **M2, fixed.** The request the refiner writes now names the list and the critique as steps 1 and 2 of `final_review.md`, which the project orchestrator takes the method from, says both agents run on a class of model cheaper than the refiner's, named in general terms, and that the first gets the complete task document and the full entries *Decisions in play* names and nothing of the conversation.
- **M3, fixed in *Rationale* of WAY-377.** It now says what the decision leaves out of the practice: "the count of how many guesses the human would settle otherwise and the minutes of reading the list, which the notes keep for the trial". I read the card (D8) in the author's notes to word it; the entry still names no file or path of them. *Rejected* is unchanged (only the ways the task keeps, WAY-134).
- **M4, fixed.** `final_review.md` step 5: "as sections 4 and 5 of `SKILL.md` give".
- **M5, fixed.** `SKILL.md` section 6 rewrapped to 100 characters.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` — 0 errors, exit 0 (before and after the commit).
- `python -B instruction-files/check_instructions.py .` — 0 error, 0 warn, exit 0.
- `python -B gate/run_tests.py project-level` — 278 tests OK, exit 0.
- `python -B gate/run_tests.py elements/common` — 242 tests OK, exit 0.
- Not run: the whole gate (forbidden); `agent-instructions` and `instruction-files` test directories (no skill's entry point, description or place changed, and no instruction-file check changed since the run in the first report).
- No failing-first run: prose only, no test exists or was written.

## Own-work check

Requirement most likely not met: that the skill, the orchestrated bullet and WAY-378 say the same thing about what the quotation check covers (the cause of I1) and that WAY-378's meaning sentence is kept. Check: I read the three texts together after the change. `final_review.md` step 3 covers the matters shown and the guesses judged settled or most likely right; `orchestrated_mode.md` defers to `final_review.md` for the check and, for M2, now names steps 1 and 2 and the class and input that WAY-377 binds; `SKILL.md` section 6 names no check and stays true; WAY-378's binding sentence, example, *Rationale* and *Rejected* all name both groups. The first example of WAY-378 (a quotation of one of the 6 "settled" guesses fails and the guess counts open) is now produced by the skill's own step 3. Reading check, not a run.

## Choices

- A guess the critique judges "most likely wrong" or "truly open" needs no quotation check for the human's sight, since it is shown; only guesses kept from the human are added to the check. Rejected: checking every guess — more files opened with no change in what the human sees. Cost if wrong: a wrong "most likely wrong" verdict shows one matter too many.
- M3 closed in *Rationale*, not in *Rejected*, as the finding suggests; WAY-134 keeps *Rejected* to the task's ways.

## Reaches beyond the handoff

- the author's notes on the AI Tech Leaders course, the card D8 (lines 516-523 and 684-703), to word what the practice includes (M3). The path is not in any tracked file.
- the user's rules for writing scripts (read through the hook, before a script I then did not use; I made the edits with the editing tool).

## Working copies

`.runs/author/` held the output of the two test runs; removed (`.runs/` holds only `orchestrator/` and `task-cycles/`).

## Unread material

- `reports/review-whole-report.md`: not read; the findings file holds the findings in the reviewer's words and the handoff said the fix needs only it.
- `task-cycle/change/fix.md`: read whole. Findings file: read whole.
- The rest of the dispatch's reading (decisions, invariants, glossary) is as in `reports/author-report.md`.

## Searches not found or unclear

- none
