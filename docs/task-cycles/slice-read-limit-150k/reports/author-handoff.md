# Handoff — the one author of the change

You are the one author of a change in a task cycle of the-way, without a plan. The person who
requested the cycle delegated intermediate choices to the orchestrator; no answer here is that
person's approval.

- Worktree (work only here, from its root): `the task's worktree root`, branch `task/slice-read-limit-150k`, base `f04f046d5220913a4ae399faf59683129e81c936`.
- Method: read `task-cycle/change/SKILL.md` whole; your variant is "the whole change as the one author". Read a file it names only when the step or variant that names it comes. You have no skill tool: a skill a file names by name alone is the `SKILL.md` whose frontmatter `name:` is that name, read as a file.
- Foundation step: read `task-cycle/skill/foundation_step.md` whole and write the entries the task carries as it gives. Return step: read `task-cycle/skill/return_step.md` when you reach it; take it after your code and entries, before you return.
- Frozen task (read whole): `docs/task-cycles/slice-read-limit-150k/task.md`. It is the whole of your task: *To do* 1–3, *Questions to settle* (the answers bind), *Decisions in play*, *Settlements to record* rows 1 and 2.
- Report: write it to `docs/task-cycles/slice-read-limit-150k/reports/author-report.md`, as `task-cycle/change/SKILL.md` gives, with **Unread material** and **Searches not found or unclear** (each `none` where nothing).

## Answers of the cycle's start

- Trust boundary: no. Irreversible operation: no. No open design choice, no reserved choice, no spec, no plan.
- The product has no guidelines of its own: WAY-328 departs for the-way's own code and tests from the general coding guidelines and the testing guidelines. Follow the style of `task-cycle/slice_size.py` and `task-cycle/test_slice_size.py`.
- The checks failing on the base: none.

## What you read (selected by the orchestrator, WAY-150)

- Decisions, whole: WAY-136 (the one the task changes), WAY-229, WAY-27, WAY-328, WAY-33; plus every decision whose *Scope* names `task-cycle` or `decisions` that you need for your search under WAY-33. The `task-cycle` and `decisions` parts of `foundations/part_map.md`; the invariants whose *Part* names `task-cycle`, `decisions` or `every`.
- Element for the entries you write: `elements/decisions/skill/SKILL.md` with its `template.md`, `elements/common/rules.md` and `elements/common/way_of_working.md`, as `foundation_step.md` and that skill give.
- Code: `task-cycle/slice_size.py`, `task-cycle/test_slice_size.py`, `task-cycle/plan/SKILL.md` (the paragraph around the size script), `task-cycle/skill/planning.md`, `task-cycle/plan/too_large.md`: look for anything that states the old limit, a quarter of the window or 250 000.

## Binding choices of the orchestrator (record in your report as ones you made)

1. The report line printed by `slice_size.py` (`report()`, "Too large: more than … estimated tokens to read, a quarter of a … context window …") states the old reasoning and would be false after the change: rewrite it to state the limit without "a quarter", keeping the form of the table, and make the test of that text, if any, follow.
2. Row 2 of *Settlements to record* (the limit is 150 000 tokens, not 175 000 or 125 000) is written as a decision entry of its own, with the rejected values and their numbers from *Questions to settle* in its *Rejected*, unless your search of the whole foundation (WAY-33) finds it already stated: then tie the row to that entry and say so in your report. Row 1 is the change of WAY-136's *Rejected* (*To do* 3). Mark each entry `row <n>`.
3. WAY-27: nothing you write in the repository (code, docstring, entry, comment) names or links a private note, a file of the author's disk or a source its readers cannot reach. The measurement is described in words and numbers taken from the frozen task's *Need* and *To do*; use no number the task does not give. The description of the script stays English; the entries are English.
4. The first sentence's claim of the script ("the limits start with a wide margin and are corrected as cycles bring data") may be kept in the form the task's point 2 allows; replace only what no longer holds. `CONTEXT_WINDOW_TOKENS` and `CHARACTERS_PER_TOKEN` and their source stay.
5. The test `test_read_at_the_limit_fits_and_one_character_more_is_too_large` moves to the new boundary (150 000 tokens at 2.5 characters a token); do not weaken what it checks.

## Checks you run (not the full gate: the orchestrator runs it)

- `python -B gate/run_tests.py task-cycle` (exit code and count in your report) and `python -B elements/common/foundation_check.py` (exit code in your report), and any test of another directory your search shows reads the changed text. Report each with its command and exit code.
- Commit on the task branch; add files by path, never `git add -A`. Do not touch `.runs/`. Commit messages in English, imperative.
