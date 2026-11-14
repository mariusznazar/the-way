PASS 4f26b6b62d49d3575e137ee7a610f2ace43d5635

# Review of the fix: range 8680824..4f26b6b

`git rev-parse HEAD` in the worktree is `4f26b6b62d49d3575e137ee7a610f2ace43d5635`; `git log 8680824..4f26b6b` holds the one commit `4f26b6b`. The worktree was clean before and after. Counts: blocking 0, Minor remaining or new 2, out of scope 0.

## Each finding of the findings file

- **B1 — fixed.** `elements/environment-facts/template.md` (the bullet of the secret) now ends "so that a token or a password never enters the output (WAY-80)"; the clause "nothing is cut from the output afterwards, and no marker stands in its place" is gone. The *Rationale* of WAY-80 no longer says "nothing is cut from the result afterwards". `git grep -n -i "cut from\|cut afterwards" -- elements foundations README.md` finds nothing (exit 1). The template now says what WAY-80's binding sentence and row 3 say, and the allowance "the lines of it the sentence rests on" no longer meets a contrary instruction. The ban on a marker stays in WAY-80's *Rejected* and in its `violates` example, where the task's row keeps it.
- **M1 — fixed (WAY-80 and WAY-60).** WAY-80: first paragraph, three sentences (forms of source; the reading; the output holds no secret); second paragraph, two sentences (the sentence says no more than its source; a fact resting on a whole section). WAY-60: first paragraph two sentences (where a condition stands; how it is named), second paragraph two sentences (branches, `{fork-point}`, `{merge-onto}`; measured quantities), which is the title's second question. No sentence was reworded. Every paragraph holds one to three sentences, as the decisions template and WAY-05 give; the split into a paragraph per part of the question is the form WAY-05 names.
- **M2 — fixed.** The comment of `test_fact_source_with_a_command_of_several_lines_in_a_code_block` (`elements/common/test_foundation_check.py:892-894`) no longer claims a break of `blocks` or `fields` is caught; it says the form the template gives is read as a fact and the test fails if the script began to reject it. The fix report withdraws the claim of the author's first report. The test's content is unchanged, as the finding proposed.
- **M3 — fixed.** The sentence of `elements-no-pending-marker` (`foundations/invariants.md:108`) now says "every run of spaces and line breaks counting as one space", and the pattern is `decision[ \n]+pending` (`elements/common/test_elements_pending_marker.py:17`), the sentence's own words; a tab no longer matches. My controls on `4f26b6b` in a scratch worktree: `decision` + LF + `pending` appended to the tracked `elements/common/rules.md` exit 1; `decision  pending` (two spaces) exit 1; `decision` + CRLF + `pending` exit 1 (the file is read in text mode, so CRLF counts as a line break); `decision` + tab + `pending` exit 0, as the sentence says. The scratch worktree is removed, nothing committed.
- **M4 — fixed.** `(WAY-80)` is gone from the rule on code under a fixed commit (`elements/environment-facts/template.md:152`).
- **M5 — fixed.** WAY-84's binding paragraph, WAY-60's paragraph (split), the template bullet on settings (`template.md:65-67`) and WAY-35 *Verification* are rewrapped evenly. The line of WAY-60 that was about 107 characters now reads under 100.

## What the fix itself broke

No new Critical or Important finding. The diff is 23 insertions and 21 deletions in wording, paragraph splits, one pattern character class, one sentence of the invariant and one comment; the foundation check reports `0 errors` and the directory gate passes, so no citation or quotation of a changed binding sentence is left stale. The invariant's sentence was reworded and its test file changed in the same commit (the foundation check's rule on a reworded sentence is met).

Minor, new in the fix diff, blocks nothing, within the task:
- `foundations/decisions.md` WAY-80, second paragraph: the line "quoting the source is no source. A fact resting on a whole section of rules quotes the sentence of its source that sets those rules and" is about 137 characters, and the rationale of WAY-80 ends with a one-word line (`it.`); the paragraph split left a hand-wrapped line unreflowed. Polish only, no rule limits line length (698 lines of the file are over 100 characters; 699 before).
- `foundations/invariants.md:108`: the invariant's sentence is one long line, as the file's other sentences are; no finding, noted because the sentence grew by a clause that pairs exactly with the test's pattern.

## Checks (command, exit code)

| Check | Command (from the worktree root) | Exit |
|---|---|---|
| Foundation check | `python -B elements/common/foundation_check.py` | 0 (`0 errors`) |
| Directory gate | `python -B gate/run_tests.py elements/common` | 0 (201 tests, OK, 259 s) |
| Invariant test | `python -B -m unittest elements/common/test_elements_pending_marker.py` | 0 |
| Private paths | `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` | 0 (`checked: 298 files, 0 listed`) |
| Whitespace in the fix range | `git diff --check 8680824..HEAD` | 0 |
| Cut-afterwards wording gone | `git grep -n -i "cut from\|cut afterwards" -- elements foundations README.md` | 1 (no match) |
| Negative controls of the pattern | scratch worktree of `4f26b6b`; LF, two spaces, CRLF fail with exit 1; tab exit 0 | as above |

Not run: the full gate (as dispatched).

## Unread material

The fix diff, the findings file's contents as the handoff gives them (the coordinator's message and my own whole-change report, which I wrote and have in context), the fix report, `task-cycle/review/fix.md`, the changed decisions (WAY-35 *Verification*, WAY-60, WAY-80, WAY-84) in their current text and the two test files' changed parts were read whole or in the parts changed. I did not re-read the entries of the whole-change selection beyond them, since this review is bounded by the findings file. `reports/whole-change-findings.md` itself I did not open separately: its findings are those of my whole-change report. Reread of the full task document: not repeated.

## Searches not found or unclear

none
