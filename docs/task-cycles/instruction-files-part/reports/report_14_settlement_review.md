# Report 14 — code review of the assessment's settlement (opus; returned as text, saved by the orchestrator)

Range 2d9c32e..2ada67c (3 commits). Verdict: **Ready.** No Critical, no Important.

Partial checks in the scratch clone at 2ada67c: `instruction-files` 104 OK (5 skipped); `agent-instructions` 18 OK; `gate` 98 OK; entry points current; the-way 0/1/3; 397 references, 0 stale; guards 0 errors (decisions 13 warnings: 8 placeholders, 5 overdue before the branch).

Strengths: settlement rows 1, 3, 4, 8, 11 applied one for one; rejected rows 5, 6, 9, 12 leave no trace. The rewritten check follows the new sentences only: population follows the widened term (`INSTRUCTION_NAMES` with `CLAUDE.local.md`), naming files stay the root `AGENTS.md` and `CLAUDE.md`; `counted_ats` is exactly "followed by a character other than whitespace"; the root-import test asserts only its sentence; written by a check author who wrote neither sentences nor code (two commits d87d74f, 2d10454). Text and code edits match their rows (proposals sentence; `-@` not established; docstring on the narrow `@` and on link targets off Windows; two tests stub `lexists`).

Minor: 1 `principles.md:9-10` says whole sections were adopted, while adoption is per principle; 2 `claude-code-agents-md` carries passages its sentence does not state (WAY-132 *Rejected* rests on them; the watch guards them) — controller's call; 3 the invariant reaches beyond WAY-129 (mentions) — recorded as Q33, must appear in the request; 4 `check_instructions.py:23` (111), `:35` (105) over 100 columns.

## Deliberate breaks (from the two sentences only; scratch clone; each run once, reverted)

| Break | Exit | IFI | RCI |
|---|---|---|---|
| control | 0 | pass | pass |
| `Ping @nothing here.` in `AGENTS.md` | 1 | fail | pass |
| `A line ending in @`, `An @ x alone.` in `AGENTS.md` | 0 | pass | pass |
| tracked `sub/CLAUDE.local.md` holding `[@x]` | 1 | fail | pass |
| tracked `.claude/CLAUDE.md` holding `@y` | 1 | fail | pass |
| `# Claude` above `@AGENTS.md` in `CLAUDE.md` | 1 | fail | fail |
| root `CLAUDE.md` untracked | 1 | fail (population control, kept by row 2) | pass (vacuous) |
| tracked root `CLAUDE.local.md` = `Text.\n@AGENTS.md` | 1 | fail | pass |
| `sub/CLAUDE.local.md` `[@x]` untracked | 0 | pass | pass |
| `a@example.com`, `-@dash.md`, `` `@code` ``, `<@angle>` in `AGENTS.md` | 0 | pass | pass |
| `“@q”` in `agent-instructions/README.md` | 1 | fail | pass |

No break that should fail passed; none that should pass failed.
