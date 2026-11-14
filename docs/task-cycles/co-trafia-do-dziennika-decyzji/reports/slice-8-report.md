# Slice 8 report: guidelines rules with no decision

## Status

`done`

## Commits

- `5c4db42` Let a guidelines rule with no decision read none in the template (branch `task/co-trafia-do-dziennika-decyzji`, base `f20a62cf237eccbb1fb947a24340e68a9e83d000`)

Worktree is clean after the commit. Nothing pushed.

## Files changed

- `product-guidelines/template.md`: 22 insertions, 11 deletions (from `git diff --shortstat f20a62c..HEAD`).

## What changed (against D7 and WAY-168/172/173)

- Opening paragraph: a binding rule says what to do and how; a rule executing a real-cost choice names its decision; a rule that only says how to write code, tests or the look of the product stands alone with its reason in one sentence and *Decision* reads `none`.
- "Required form" block: `- **Decision:** <PREFIX-NN> · … | none`.
- Bullet "A binding rule": *Decision* may read `none` where the rule only says how to write, test or style.
- Bullet "A rule carries no rationale and no rejected options": a rule with *Decision* `none` carries its reason in one sentence instead.
- Bullet "What names no decision is an example" reworded to "What holds no rule is an example": it stands under `## Examples` with no *Decision* field, and a rule with *Decision* `none` binds, so it is a rule.
- New bullet in "Rules of writing": a rule with *Decision* `none` is accepted by the human as a row of the task's table of settlements (*Goes to* `guidelines: <discipline>`) before the code; a rule the cycle finds itself is named in the request's description among what the human did not see in the task and accepted at the merge (WAY-172); a rule of a template of the-way binds a product only through a decision of the product's log that adopts it (WAY-173, not loosened).

## Checks

1. `python -B elements/common/foundation_check.py` (run in the worktree root), exit code 0. Output: `foundations/decisions.md:578: listed: WAY-17 is held by nothing ...` (the expected listed line, not a gate stop) then `0 errors`.
2. `python -B gate/run_tests.py elements/common`, exit code 0. Output: `Ran 198 tests in 237.664s`, `OK`.

No test was written or changed in this slice (prose only), so there is no failing-first run and no invariant test to see failing. No script changed.

## Own-work check

- Requirement most likely unmet: the template must now allow *Decision* `none` in every place D7 names, without loosening WAY-173 (a template rule binds a product only through a decision adopting it).
- Check: `grep -n` over `product-guidelines/template.md` for `reads \`none\``, `Decision\* \`none\``, `binds a product` and `What holds no rule`, plus reading `git diff` against D7 point by point. The `| none` on the *Decision* line was checked in the diff.
- Result: passed. Each D7 item is present, and the WAY-173 sentence is the only text on that rule and says it binds through a decision only. `git diff --check` exit code 0 (no whitespace errors).

## Reaches beyond the dispatch

- `.runs/task-cycles/co-trafia-do-dziennika-decyzji/spec.md` lines 140-147 and lines 45-71 (the questions and answers, to confirm points 4 and the D7 text): inside the spec file, read by the line ranges the handoff names plus the adjacent Questions to settle block, which the spec's D7 cites as its basis (WAY-172/173 answers).
- `foundations/decisions.md` read by line ranges beyond the handoff's current starts: 5065-5194 (WAY-166 end and WAY-167 whole, to see the guideline-file rules), 5523-5552 (WAY-174 rationale start), 7273-7342 (WAY-235 whole and the start of WAY-236, the trust-boundary rule that WAY-173's family relates to). Reason: to confirm the WAY-168/171/172/173 wording and the cross-references, not to change anything in them.
- `task-cycle/change/slice.md` read whole; the reserved-choices file and `ui_check.md` not read (no reserved choice, no UI change).

## Unread material

- `foundations/decisions.md` WAY-174 from line 5553 to its end; not needed for the template's wording.
- `foundations/invariants.md`, `elements/decisions/template.md`: not read. The slice names them only as the place WAY-35 and the decisions template govern; the template points to them and copies no question, so no reading was needed.
- The rest of the task document (`task.md`) beyond lines 36-71: not read, not named.

## Searches not found or unclear

- First attempt to read the spec used the main checkout path `.runs/task-cycles/...`, which does not exist; the correct path is under the worktree's `.runs\`. Resolved by re-reading from the worktree.
- The handoff says the foundation entries' line ranges are stale; I used the orchestrator's current starts (WAY-167 5177, WAY-168 5249, WAY-169 5310, WAY-170 5339, WAY-171 5372, WAY-172 5419, WAY-173 5479, WAY-174 5515, WAY-235 7273), which matched.
- A Bash commit call was blocked once by a `PreToolUse` hook that printed the git rules file (`.ai/rules/git.md`) and asked for a re-run; I re-ran the same command unchanged after reading it. No rule was violated; the commit is path-scoped and English.

## Questions and concerns

- None blocking.
- Not done in this slice, by design: D7's extension of the request's kind 6 list and of the *Foundation entries* of the lower part belongs to the request template, not to `product-guidelines/template.md`; the handoff named this file as the only file to change. The orchestrator should confirm another slice covers it.
- A small reflow of the opening paragraph left the word "and" on its own line in the template text; cosmetic only.

## Background processes

The `foundation_check` and gate run were started in the background; both completed (exit 0). The monitor (`bsdqg93vt`) that waited on the gate log ended on its own after the second `EXIT=0`. No background process is still running.
