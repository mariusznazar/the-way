# Slice 9 report: the request template names what the new checks and tests show

## Status

`done`

## Commits

- `39d702a` Name the listed invariants and the decision tests in the request template

Base: `5c4db42a052e9e4836b833a9408199580bb0bdfc`. The worktree is clean after the commit. Nothing was pushed.

## Files changed

- `task-cycle/skill/request_template.md`: 12 lines added, 2 removed (`git diff --stat`). The two removed lines are the closing words of kind 6 and kind 7, each rejoined to new text. No heading, group name or kind number changed.

What changed:

1. **Kind 6** (*You accept by merging*): a guidelines rule with no decision that the cycle found itself is named there, as a rule whose *Decision* reads `none`, with one plain sentence of what it asks for; the human accepts it at the merge (WAY-172).
2. **Kind 7** (*You accept by merging*): the writer of the description runs `python -B elements/common/foundation_check.py` (in a product, `.the-way/elements/common/foundation_check.py`) on the finished change, without the switch, and reads its `listed:` lines. Each invariant listed for a corrected sentence is named in plain words (what the sentence now says, and that the test that checks it was left as it was). Each test whose line `decision:` the change adds, drops or alters is named as a changed invariant test is (WAY-03).
3. **Lower part, *Foundation entries***: the same listed invariants and the changed `decision:` tests are added there (WAY-03, WAY-12), pointing to the top part's *You accept by merging*.

## Checks

| Check | Command | Exit code | Result |
|---|---|---|---|
| Task-cycle gate | `python -B gate/run_tests.py task-cycle` | 0 | Ran 394 tests, OK |
| Foundation check on this repository | `python -B elements/common/foundation_check.py` | 0 | One `listed:` line for `WAY-17` (`foundations/decisions.md:578`, held by nothing), then `0 errors` |

No check failed or was left unrun.

## Own-work check

- **Requirement:** the description writer must find, in the template, the exact script to run, the rule to read its `listed:` lines, and the naming of changed `decision:` tests; and no heading, group name or kind number may move (the handoff's constraint, since `request_check.py` and its test read the headings).
- **Check:** `git diff -U0 task-cycle/skill/request_template.md | grep '^-'` shows only the two line-ends replaced (no heading removed). `git diff -U0 | grep -c '^+#'` gives 0, so no heading was added. The task-cycle gate, which includes `test_request_check.py`, passed (exit 0).
- **Result:** as expected. The prose itself is not tested (method: prose for people gets no test), so no invariant test was written or altered and no failing run was needed.

## Choices and departures

- I wrote the kind 6 addition as a sentence inside the existing kind 6 item, not as a new item (the handoff forbids a new kind).
- I put the pointer in the lower part as "as the top part's *You accept by merging* gives it", not as a kind number, because the template says a kind number is not an item number in a description.
- The lower-part addition names WAY-12 beside WAY-03, since the `decision:` line is WAY-12's attached rule (spec D8).

## Concern and question

1. The kind 7 text says "without the switch", as spec D4 gives it. The switch is `--skip-test-citations` (`elements/common/foundation_check.py`, line 11 and `main` at line 971). Nothing in the template names it, so a description writer may not know which switch is meant. Recommendation: name the flag in kind 7 (`without --skip-test-citations`), since that is what the writer must leave out. I have not made this change because the spec gives the words; the orchestrator decides.

## Unread material

- `.runs/task-cycles/co-trafia-do-dziennika-decyzji/plan.md`: not read; the handoff copies the slice section, and I used that copy.
- `.runs/task-cycles/co-trafia-do-dziennika-decyzji/spec.md`: read only lines 100–154 (D4–D9); D1–D3 not read.
- `.runs/task-cycles/co-trafia-do-dziennika-decyzji/task.md`: read only lines 36–43 (To do 4, 6–8 and the settlement lines around them), as the handoff's *Read* gives.
- `foundations/decisions.md`: WAY-03 read at lines 68–107 (its attached paragraph and *Verification*; the *Rationale* and *Rejected* after line 107 not read); WAY-12 read at lines 435–464 (its *Rationale* and *Rejected* not read); WAY-114 read at lines 2787–2836; WAY-172 read at lines 5419–5468.
- `foundations/part_map.md:93-103` (task-cycle): not read; the change alters no scope.
- `task-cycle/request_check.py` and `task-cycle/test_request_check.py`: not read; I relied on the gate's pass for them.
- `foundations/glossary.md`, `foundations/invariants.md`, `product-guidelines/template.md`: not read; the handoff names them only as context for stale ranges, and this slice does not change them.
- `task-cycle/change/slice.md` and `make-change` (`task-cycle/change/SKILL.md`): read whole.

## Searches not found or unclear

- My first attempt to read `spec.md` and `task.md` used a path relative to the repository root (`.runs/task-cycles/...` outside the worktree), so the read failed. The second attempt at the worktree path succeeded. No content was missed.
- The word "switch" in spec D4 and in the handoff's *Checks* is not defined in the spec. Found: `--skip-test-citations` in `elements/common/foundation_check.py`. See the concern above.
- A Bash hook (`rules-on-demand`) blocked my first commit call and asked me to read the git rules file. I read it and repeated the same commit (`git add` by path, `-m`, English message). The hook's content did not change the commit. The git rules file is at `the author's personal rule file on git`.

## Background processes

None started. Nothing needed stopping.
