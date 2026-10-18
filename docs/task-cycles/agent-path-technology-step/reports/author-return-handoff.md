# Return step handoff — author, turn 3

Worktree and branch as before. Input commit: `2fabc67`. Cycle record: `.runs/task-cycles/agent-path-technology-step/cycle.md` (questions table C1–C10). The whole-change review ([review.md](review.md)) gave Yes with 5 Minor findings; Minor findings are not fixed (WAY-161) — do not act on them in this turn; they go to the request.

## What this stage does

Read `task-cycle/skill/SKILL.md` step 11 (first paragraph) and perform the return step of WAY-11 on the real diff `77c8a8b..2fabc67` and the cycle's choice log:

- Refresh the foundation selection by "Reading the foundation" for the real diff and current foundation; first fetch and compare with `origin/foundations` (base `77c8a8b`) and say whether it moved.
- Identify newly learned decisions, rules, uncovered behaviour, environment facts, glossary terms and part-map changes; compare the touched parts of the foundation with the text. For uncovered behaviour ask: would changing it in a later task violate a requirement or a settled rule? If yes, an invariant; if no, a replaceable detail kept in ordinary tests and the description of the change. Record only the candidates actually found, with their supporting requirement or reason. In particular consider: a `project-level` failure mode in `foundations/part_map.md` for the three matters (WAY-46); whether "development data", "logs", "interface" or "agent's way to the running product" need glossary entries (a word used in a meaning a reader of the field would not give it); whether any rule needs an invariant.
- Rows 1–4 of *Settlements to record*: confirm each is written and agrees with the text; write any the foundation step missed. No projected entries (independent task).
- Write resulting entries that bind after the merge (WAY-36) as the foundation step writes them, with the element skill of their kind read whole. Every other choice stays one line in the choice table. No entry is deferred or proposed for later.
- If you find a new invariant, stop before writing it and report it: its sentence and its check come from two other agents (WAY-69).
- Second whole-foundation search (WAY-33) against the current `origin/foundations` tip; record what it searched and found.
- Name any question the foundation step allows for the human (no recommendation, a change to the meaning of an approved decision, a row whose meaning cannot hold, or a value nobody gives), each with options and your recommendation.

## Checks

If you change anything: the affected tests and format guards (no-main options), entry points, `git diff --check`, with full output under `reports/` (prefix `return-`) and exit codes. Count fingerprint links and confirm none stale.

## Write boundary

As before: only this worktree, line endings preserved, commit by explicit paths with an English message, never `.runs/`, no push, no agents.

## Output

Full report `.runs/task-cycles/agent-path-technology-step/reports/author-return.md`: foundation selection refresh; each candidate found and its classification with reason; entries written (identifier, row, one sentence of meaning in Polish) or none; rows 1–4 check; second search domain, terms, findings; questions for the human with options and recommendation, or none; commands, exit codes, output paths; changed files and line counts for any commit; unresolved concerns. Short return message as before.
