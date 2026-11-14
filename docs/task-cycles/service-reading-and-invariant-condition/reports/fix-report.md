# Fix report: findings of the review of 8680824

**Status:** done

**Commits** (from the reviewed head `8680824`): `4f26b6b` Fix the review's findings: drop the cut-afterwards rule on a reading's output, keep binding paragraphs to three sentences, state the whitespace the pending-marker test reads, correct claims and wrapping

Files changed: `foundations/decisions.md` (WAY-35 *Verification*, WAY-60, WAY-80, WAY-84), `foundations/invariants.md` (one sentence), `elements/environment-facts/template.md`, `elements/common/test_elements_pending_marker.py`, `elements/common/test_foundation_check.py` (comment only). 23 insertions, 21 deletions before the one-character pattern change.

## Findings

- **B1 — fixed.** Dropped "nothing is cut from the output afterwards, and no marker stands in its place" from `elements/environment-facts/template.md` (the bullet now ends "so that a token or a password never enters the output (WAY-80)") and "and nothing is cut from the result afterwards" from the *Rationale* of WAY-80. The template now says no more than WAY-80's binding sentence and row 3: the command reads only the fields the sentence rests on, and the quoted output holds no secret. The ban on a marker stays where it was a decision: WAY-80's *Rejected* and the `violates` example. Check: the three passages the reviewer named read side by side no longer conflict; `grep -n "cut from" ` over the template and WAY-80 finds nothing.
- **M1 — fixed, both decisions.** WAY-80: the first paragraph holds three sentences (source forms; the reading; the output holds no secret), a second paragraph holds the other two (the sentence says no more than its source; a fact resting on a whole section), the second part of the entry, as WAY-05 allows. This removes the four-sentence departure that stood before the change as well. WAY-60: first paragraph holds the two sentences on where a condition stands and how it is named; the second holds the two on branches, `{fork-point}` and measured quantities (the title's second question). No sentence was changed. Check: `python -B elements/common/foundation_check.py` exit 0, `0 errors`.
- **M2 — fixed by dropping the claim.** The comment of `test_fact_source_with_a_command_of_several_lines_in_a_code_block` now says what it does hold: the form the template gives for a reading whose command has several lines is read as a fact, and the test fails if the script began to reject that form (a bug against the template's promise). I agree with the reviewer's five mutations: the test does not catch a mutation of `blocks` or `fields`, and my first report's claim that it does was wrong. I kept the test and its content, since the form the template promises is otherwise unpinned. The claim in `author-report.md` ("the break it catches: a change of `blocks` or `fields`...") is withdrawn by this report.
- **M3 — fixed by wording the sentence, and the pattern narrowed to the sentence.** The sentence of `elements-no-pending-marker` now reads: `No file git tracks under `elements/` holds the text "decision pending", every run of spaces and line breaks counting as one space.` The test pattern is `decision[ \n]+pending` (it was `decision\s+pending`, which also matched tabs): spaces and line breaks, the sentence's own words. Rejected: narrowing to one literal space, since lines of Markdown wrap and a wrapped marker would pass. Evidence: seeded `decision` + line break + `pending` appended to the tracked `elements/common/rules.md` fails the test (`['elements/common/rules.md:92']`, exit 1), a tab between the words passes, restored with `git checkout -- elements/common/rules.md`, never committed.
- **M4 — fixed.** Dropped the citation `(WAY-80)` from the rule on code under a fixed commit (`elements/environment-facts/template.md`, the bullet of item 6).
- **M5 — fixed.** Rewrapped the four places: WAY-84 binding paragraph, WAY-60 (the long line went with the paragraph split), `elements/environment-facts/template.md` (the *Which facts are written* bullet on settings) and WAY-35 *Verification*. The wrap of the lines is not checked by any rule.

## Checks (command, exit code)

| Check | Command | Exit |
|---|---|---|
| Foundation check | `python -B elements/common/foundation_check.py` | 0 (`0 errors`) |
| Invariant's test, passing | `python -B -m unittest elements/common/test_elements_pending_marker.py` | 0 |
| Invariant's test, failing on a seeded text (never committed) | same command, after appending `decision` + line break + `pending` to `elements/common/rules.md` | 1 |
| Private paths | `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` | 0 |
| Gate of the directory | `python -B gate/run_tests.py elements/common` | 0 (201 tests, OK) |

Not run: the full gate (the orchestrator runs it).

## Own-work check

Requirement most likely unmet after the fix: the template must say no more about secrets than WAY-80 and row 3, and the invariant's sentence and test must mean the same text. Checks: `grep` of the template and the decision for "cut from" finds nothing; the seeded wrapped marker fails and a tab between the words passes, as the sentence says.

## Unread material

none (the findings file, the handoff, `task-cycle/change/fix.md`, WAY-35, WAY-60, WAY-80 and WAY-84 in their current text, the template and the two test files were read; the full review report was not opened, since the findings file carried its evidence).

## Searches not found or unclear

none
