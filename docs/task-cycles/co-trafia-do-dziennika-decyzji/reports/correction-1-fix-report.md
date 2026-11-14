# Report of the fix of the blocking findings I1 and I2 of the review of the unread decisions

**Status:** done

Range: `7a5fea4..HEAD`. Commit: `8571691` "Restate the check and the named tests with their qualifications in the READMEs and the request template". The worktree is clean.

## I1 — fixed

- `README.md` (the paragraph on `foundation_check.py`): "each decision that a change adds or rewords and that nothing holds" became "each decision that a change adds or whose binding sentences it alters and that nothing holds"; "each invariant whose sentence a change rewords while no file citing it changes" became "each invariant that reads `test` whose sentence a change rewords while no file citing it changes".
- `agent-instructions/README.md` ("The form of the foundation"): "the invariants whose sentence a change rewords ..." became "the invariants that read `test` whose sentence a change rewords ...". The sentence "it reports the decisions that nothing holds" there says nothing of what makes one an error, so it needed no further qualification (the finding names only the invariant half for this file); I left it.
- The lines were reflowed to the 100-character width; no other word changed.

## I2 — fixed, widened (the reviewer's first way, as ruled)

All three places now name each test that holds a sentence of a decision by a line `decision:` where the change adds, drops or alters the test or its line:
- `task-cycle/skill/request_template.md`, kind 7: "Each test that holds a sentence of a decision by a line `decision:`, where the change adds, drops or alters the test or its line, is named as a changed invariant test is (WAY-03)."
- `task-cycle/skill/request_template.md`, lower part *Foundation entries*: "each test that holds a sentence of a decision by a line `decision:`, where the change adds, drops or alters the test or its line (WAY-03, WAY-12)".
- `foundations/decisions.md`, *Verification* of WAY-03: *complies* reads "a change that adds, drops or alters a test that holds a sentence of a decision by a line `decision:`, or alters its line, names that test in its request"; *violates* now reads "a change weakens a test that holds a sentence of a decision by a line `decision:`, or drops its line, and its request is silent" (it named only the dropped line before, which is the narrowing the reviewer found).

Decision changed: WAY-03, its *Verification* only. Its binding sentences are untouched, so no human acceptance is needed and the check reports no changed decision; WAY-03 stays held by its invariant tests (lines `decision:`) and its pair of examples. Every heading, group name and kind number of the request template stays.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` : exit 0, `0 errors` (run after the last edit).
- `python -B gate/run_tests.py elements/common` : exit 0, 199 tests OK (run after the last edit; an earlier run before a final reflow of one WAY-03 line also exit 0).
- `python -B gate/run_tests.py task-cycle` : exit 0, 394 tests OK.
- `python -B gate/run_tests.py agent-instructions` : exit 0, 25 tests OK.
- These two were first run before the final reflow of one *Verification* line of WAY-03 (a line break, no word). At the coordinator's request I ran both again on the tree as it stands at `8571691` (`git status` clean, HEAD `8571691`): `python -B gate/run_tests.py task-cycle` exit 0, 394 tests OK; `python -B gate/run_tests.py agent-instructions` exit 0, 25 tests OK.
- The gate with no directory: not run (the orchestrator's alone).

## Own-work check

The requirement most likely not met: that no place still says the request names only the changed line `decision:`, and that the widened places match WAY-03's binding sentence ("a change that alters an invariant test, or a test that holds a sentence of a decision by a line `decision:`, names that test in its request"). An earlier version of this report said a grep confirmed this; that grep (`grep -rn` for the phrases "whose line `decision:`" and "the line `decision:` of a test") found only two lines that state the form of the line, so it did not show it. What I checked after that:

- A search of every `*.md` file of the worktree (outside the record) for "decision:`", and a second for the phrases "names that test", "changed invariant test", "test whose line", and "adds/drops/alters" beside "line `decision:`", then a reading of each hit's lines.
- `foundations/decisions.md`, WAY-03 whole: the first binding sentence (lines 85-87) names a test that holds a sentence of a decision by a line `decision:` and alters it; *Verification* *complies* (lines 101-105) is widened ("adds, drops or alters a test that holds ... or alters its line"); *violates* (lines 108-110) is widened ("weakens a test that holds ... or drops its line"); the *Rationale* ("A test that holds a sentence of a decision checks that sentence as an invariant test checks its own, so it is named and read in the same way") already matches. No place of the entry says only the line.
- `task-cycle/skill/request_template.md`: kind 7 (lines 303-306) and the lower part *Foundation entries* (lines 457-458) are the only two places that name such a test, and both read "each test that holds a sentence of a decision by a line `decision:`, where the change adds, drops or alters the test or its line". The top part's other kinds name none.
- Other places that say a request names a test: `elements/invariants/template.md:68`, `elements/invariants/skill/write.md:9`, `task-cycle/review/SKILL.md:70` and `task-cycle/change/SKILL.md:154` say "invariant test" only. They do not say "only the line" and do not contradict the ruling; they speak of invariant tests, as they did before the change, and I left them (the ruling names three places). The other hits of the search (the other entries of `foundations/decisions.md` at lines 45-62, 444-467, 590-597 and 697-729, the decisions template, the decision skill, the invariants skill) state the form of the line, how a test holds a sentence, or the derived invariant, not what a request names.
- Result: no place still says "only the line"; nothing changed in this repair, no new commit. `git diff 7a5fea4..HEAD` shows the four files and nothing else.

## Questions and concerns

none. The reviewer's Minor findings (m1-m5) and o1 were not touched.

## Reach beyond the dispatch

none.

## Unread material

`reports/unread-review-report.md` (the findings file was enough).

## Searches not found or unclear

none
