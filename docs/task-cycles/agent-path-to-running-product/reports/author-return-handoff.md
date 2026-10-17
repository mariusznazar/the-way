# Return step handoff — author, turn 4

Worktree: `C:/Storage/repos/the-way-wt/agent-path-to-running-product`, at `0c1dfd5` (reviewed: [review.md](review.md), [review-fix.md](review-fix.md) — Ready to merge: Yes).
Target tip: `origin/foundations` refetched, still `77c8a8b` (the base).
Cycle record: `.runs/task-cycles/agent-path-to-running-product/cycle.md` — questions table C1–C12 is the cycle's choice log.

## Read first

- The return-step paragraph, step 11, of `task-cycle/skill/SKILL.md` (from "Have the one-author change's author resume for the return step" to "Run a check added here on the product and record its actual result, before its first acceptance deliberate break.").
- "Reading the foundation" in `elements/common/way_of_working.md` — refresh the selection for the real diff `77c8a8b..0c1dfd5`.
- The element skills of any entry kind you write (`.claude/skills/the-way-record-decision/`, `…record-invariant/`, `…record-glossary-term/`, `…record-environment-fact/`, `…update-part-map/`), whole, when you write that kind.

## What this stage does

Perform the return step of WAY-11 on the diff `77c8a8b..0c1dfd5` and the choice log C1–C12:

- Identify newly learned decisions, rules, uncovered behaviour, environment facts, terms and part-map changes; compare the touched parts of the foundation with the code. For uncovered behaviour ask: would changing it in a later task violate a requirement or a settled rule of the product? If yes, it needs an invariant; if no, record why the detail is replaceable and where it is covered (ordinary test or description of the change). Record only candidates actually found.
- Rows 1–6 of *Settlements to record*: confirm each is written (WAY-134); write any the foundation step missed.
- Part map (`foundations/part_map.md`, part `project-level`): the existing failure mode "a technology choice the project needs is missing from the definition's list — … — not detected" and your candidate failure mode from turn 1. Follow `update-part-map` for what an agent may write and what is the human's (WAY-46); what is the human's becomes a question for the request with your recommendation, not an entry.
- Choices that bind after the merge go into the foundation (WAY-36); every other choice stays a line in the choice table — report it, do not write it.
- An invariant found here needs separate sentence and check authors (WAY-69): do not write its sentence or check; report the need and stop that part; the orchestrator dispatches them.
- Second whole-foundation search (WAY-33) against the target tip `77c8a8b`, all five elements, for anything the final text collides with.
- Do not change the code, skills, template or tests in this turn; a needed change there is reported, not made.

## Checks

If you change a foundation file: its format guard (`--base none`, `--merge-onto none` where available), `python -B gate/run_tests.py elements/<element>`, `python -B gate/run_tests.py project-level`, `python -B gate/run_tests.py gate`, fingerprint links recount (0 stale). Outputs under `reports/` with prefix `return-`, exit codes recorded.

## Write boundary and output

Foundation files only, in this worktree; same rules as before (line endings, explicit paths, English message, no `.runs/`, no push, no agents, no human). Full report: `reports/author-return.md` — selection refresh; candidates found and how each was classified with its requirement or reason and test/description paths; rows 1–6 → entries; entries written or changed with one sentence of meaning in Polish; questions for the human (with options and recommendation); second search domain, terms and findings; commands, exit codes, outputs; changed files with line counts; commit or none; concerns. Return a short message.
