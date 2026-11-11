# Fix report — the four Minor findings of the review of the whole change

**Status:** done. No finding contested.

## Commits

- `9d4bdcd` — `foundations/decisions.md`, `task-cycle/request_check.py`, `task-cycle/skill/correction.md`, `task-cycle/skill/request_template.md` (112 insertions, 103 deletions). On top of `ff77994`. The worktree is clean. Not pushed.

## Per finding

1. **"Let it through" against "only a task" after a correction — fixed.** One rule in all five places, kept to what WAY-289 settles (the loop ends after one correction; what stays goes with the task question or stays below): *what a correction left unfixed or undone, and whatever cannot be done in this request at all, carries only the question "Make a task of it?"; the human who makes no task lets it through by merging.* Where it stands now: the `### Fix or let through` paragraph of the template (no longer "offers only 'make a task of it' and 'let it through'"), kind 8 (adds "as anything else a correction left undone does"), the *A correction* row of the variants (now "what a correction left unfixed or undone, whether it ran on an answer to item 8, 4, 9 or 14, carries only 'Make a task of it?'"), `correction.md` (last paragraph: the same, "and so is an item that cannot be done in this request at all"), WAY-289 (third binding sentence: "like whatever cannot be done in the request at all ... which the human who makes none lets through by merging"). Evidence: reread the five passages side by side; `grep -n "Make a task of it"` in the template shows lines 196, 238, 432 agreeing. The answer "let it through" stays an answer only for items that can still be done in this request (before a correction).
2. **Where the stages of a blocked request stand — fixed.** Kind 1 now says that the stages the cycle did not run because it stopped (the return step, the reconciliation, the slices not made, the review of the whole change) stand under *Needed from you* and that kind 4 does not list them again; kind 4 says so from its side. Since the rule binds, WAY-287 says the same: its blocked-request sentence now reads "what the cycle needs, in plain words, and the stages it did not run because it stopped, under *Needed from you*", and its *Verification* (complies, blocked request) names the return step and the reconciliation under *Needed from you*. The state line: "for `ready`, whether any item of *Needed from you* or *Fix or let through* below waits for the human's answer; what the human only accepts by merging waits for nothing."
3. **WAY-289 title — fixed.** Now "Which things the cycle left unfixed or undone does a request put before the human for a decision?" (edited in place, number unchanged). `grep -rn "Which unfixed findings"` over `*.md` and `*.py` outside `.runs` and `.git` found only the entry's own heading, so nothing quotes the old title. This reverses my Choice 4 of the author report.
4. **Wrapping — fixed.** `request_check.py:50` (171 characters) rewrapped; the template: "Write, check, publish" step 5 and the "two parts" bullet (its line had lost its indent) rewrapped, and every kind entry `- **N.**` rewrapped to 100 columns; WAY-287's binding paragraph and WAY-327's *Rationale* reflowed. `awk 'length>100'` on `task-cycle/request_check.py` lists only lines 37, 250 and 559, none of them from this change (`git blame` shows the base commit); in the template the lines above 100 are the table rows of the variants and a few lines of 101-115 characters that were already in the base text.

## Checks

| Check | Command | Exit |
|---|---|---|
| Focused: task-cycle (includes the template-example test) | `python -B gate/run_tests.py task-cycle` | 0 (254 tests, OK) |
| Template-example test alone | `python -B task-cycle/test_request_check.py -k templates_example` | 0 (1 test, OK) |
| Foundation check | `python -B elements/common/foundation_check.py` | 0, `0 errors` |
| Private paths | `python -B task-cycle/private_paths_check.py <file>` for `request_template.md`, `correction.md`, `decisions.md`, `request_check.py` | 0 for each of the four |
| Instruction files | `python -B instruction-files/check_instructions.py .` | 0, `0 error, 0 warn, 3 info` |

Not run: the whole gate (the orchestrator's). No test changed in this fix; the change to the code is a docstring rewrap only.

Own-work check of the fix: the likeliest miss is a leftover of the old rule in a place I did not edit. I grepped `let it through|let through|carry only|carries only|offers only|only with the question` over the template, `correction.md` and `decisions.md`: the remaining hits are the group heading and name, kind 8's question (before a correction), the example item, WAY-287's description of the group, WAY-289's own three answers (before a correction) and WAY-289's leftover rule — all agree with the one rule.

## Reach beyond the findings file

- `task-cycle/change/fix.md` (whole): the method of this variant.
- Foundation text outside the findings file edited: WAY-287 (finding 2 requires it, per the direction), WAY-327's *Rationale* (rewrap only). A mistake of mine from the first change repaired in passing: the blank lines before "What an item carries" were lost when the kinds were rewrapped, noticed and restored before the commit.

## Unread material

- `reports/whole_change_review.md`: not read; only `reports/fix_findings.md`, as the coordinator's message gave it (the findings in the reviewer's words).
- The rest as in `author_report.md`.

## Searches not found or unclear

- A search for a quote of the old WAY-289 title found none (see finding 3).
- Unclear: the direction said to "make the state-line clause about what waits below unambiguous"; I read "waits" as waiting for the human's answer, not for the human's merge. If the reviewer meant the merge itself, the clause needs another word.
