# Handoff — the return step

Stage: the return step of the task, taken by the one author who made the change (resumed). It is
neither a variant of `make-change` nor a fix; its handoff names its stage.

## Delegation and place

The person who requested this cycle has delegated intermediate choices to the orchestrator. Ask no
human. Same worktree and branch (`the worktree root`,
`task/precedence-between-decisions`), head now `baa07f44472de3d3c86cc61cb681c43ecb1bfd41`. Commit by
explicit paths, ending with the line
`Claude-Session: https://claude.ai/code/session_01GQhooaBqva1kjAzReLoCHk`. Do not push. Do not run the
whole gate. Write no absolute path and no title or link of a private note into a file of the repository.

## What to do

Read `task-cycle/skill/return_step.md` whole and follow it; it writes as the foundation step writes, so
read `task-cycle/skill/foundation_step.md` whole as well, and the skill of an element when you write an
entry of that element. The task is the frozen
`docs/task-cycles/precedence-between-decisions/task.md`. The change is the range
`294af7f..baa07f4`: your commit `9b44856` and the fix `baa07f4`. The whole-change review (first
`FAIL`, then `PASS` of the fix) and the whole gate on `baa07f4` (exit 0, 804 tests) are done.

Compare the foundation entries the change edits (WAY-25, WAY-134 and WAY-293 by the fix), those the task
names and those your search found, and the part map of the touched parts, with the files of the
repository, as the return step gives. Correct in the same change whatever no longer matches; commit a
correction. If nothing no longer matches, make no commit and say so.

The review put one thing in front of the return step that it graded outside the task's scope, and it is
not for you to fix: `foundations/decisions.md`, WAY-25 *Scope* is `decisions, task-cycle` and does not
name `agent-instructions`, while `agent-instructions/README.md` now carries the rule and cites WAY-25.
Name it in your report as a mismatch you found, with your judgment whether it is one the return step
corrects; do not edit WAY-25's *Scope* unless `return_step.md` tells you that this kind of mismatch is
corrected in the same change.

## Report

Write the full report to `docs/task-cycles/precedence-between-decisions/reports/return_report.md` in the
form `return_step.md` gives, with, for the record's *Return step*, each of its items (foundation
compared with code, decisions, invariants, environment facts, glossary terms, part-map changes,
projected entries, rows of *Settlements to record*), the sentences of meaning for each entry you write or
change, and **Searches not found or unclear** (`none` is an answer). Return the status, your commit if
any, a one-line check result and the report's path.
