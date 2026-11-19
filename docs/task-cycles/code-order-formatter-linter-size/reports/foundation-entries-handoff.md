# Handoff — the agent of the plan's *Foundation entries* (stage: foundation step)

## Delegation

The person who requested this cycle has delegated every intermediate choice of it to the orchestrator.
You work for the orchestrator. You never ask the human; a question goes back to the orchestrator in
your report. Never label an answer as the human's approval. The human accepts the entries you write at
the merge of the request (WAY-114).

## Where you work

- The worktree: `the worktree's root`, branch
  `task/code-order-formatter-linter-size`, at `d69fb20b`. Work from its root. The-way is the
  repository itself; there is no pin.
- Your directory for working copies: `.runs/foundation-entries/` of the worktree (rule below).
- Your report: `.runs/task-cycles/code-order-formatter-linter-size/reports/foundation-entries-report.md`.
- `cycle.md` and the other files of the record directory — other agents' handoffs, reports and
  findings — are not yours to read, except the files this handoff names.

## Your method and stage

- Stage: the foundation step for the plan's *Foundation entries*. Method: `task-cycle/change/SKILL.md`
  of the worktree (`make-change`), read whole — you take none of its variants' rows; this handoff names
  your stage — and `task-cycle/skill/foundation_step.md`, read whole. Read the `SKILL.md` of an element
  (`elements/decisions/skill/SKILL.md`, `elements/invariants/skill/SKILL.md`,
  `elements/glossary/skill/SKILL.md` where you write a term, `elements/part-map/skill/SKILL.md` where
  you touch the part map) when you write an entry of that element, together with the element's
  `template.md`, `elements/common/rules.md` and `elements/common/way_of_working.md`, as those skills give.
- Boundary: you write the nine entries below and the one line of a test named below; you write no other
  code, no other test and no change of `ruff.toml`, no reformatting. Commit on the task branch, by path
  (`git add <path> …`, never `git add -A`, `.` or `commit -a`), with English messages. Return when the entries stand,
  the check of the foundation (below) is green and you have run the own-work check `make-change` gives.
- The frozen task, read whole: `.runs/task-cycles/code-order-formatter-linter-size/task.md`. The
  plan: `.runs/task-cycles/code-order-formatter-linter-size/plan.md`, read its section *Foundation
  entries* (copied below) and, for what each entry later serves, the slices named in its last column
  and the *Choices* rows 7 and 16. There is no spec.
- Answers of step 4 of the cycle: a trust boundary is touched by the whole change (not by the entries);
  no operation that cannot be undone.

## What you write, and the rows that carry it

The rows of *Settlements to record* of the task: row 1 → the sentence of WAY-382; row 2 → the sentence
of WAY-385; row 3 → an invariant (F3); row 4 → the sentence of WAY-382; row 5 → the sentence of WAY-382.
F4 (the formatter's invariant) is the invariant the task's *To do* 2 asks for; the part of it that no row
carries whole is `the cycle's` unless it follows from the rows with no way left open — decide as
`foundation_step.md` gives and mark each entry `row <n>`, `projected` or `the cycle's` in your report,
with one sentence of its meaning in English and one in Polish (the task document's language). F9 is
marked `the cycle's`: it is the one entry beyond the rows and the request puts it before the human; the
orchestrator judged it no open design choice because the meaning of WAY-339 stays and the only other
ways break the decision or the rule of size (plan *Choices* 16). If you find that it needs another
way, or that an entry collides with a current one with no precedence, return `blocked` with the question.

Where the next free number of a new decision is needed, take it from the log; the plan writes no new
decision, only changes WAY-382, WAY-385, WAY-379, WAY-145 and WAY-339 in place (WAY-07) and writes two new
invariants and rewords one. Name each new invariant's identifier as `elements/common/rules.md` gives
and cite the decisions it derives from. Both new invariants read *Method* `test`, with the test
written by a later slice (Slices 3 and 4): their *Verification* names that test by its file and the
check names the slice only in your report, not in the foundation. Run `python -B
elements/common/foundation_check.py --skip-test-citations` and fix what your entries break (WAY-321).
The invariants `ruff-blocking-rules` and `function-and-file-size` keep their marks *Violated* as they
stand: later slices clear them (WAY-51).

The paragraph that follows the plan's table in *Foundation entries* binds you too (it is copied with
the section below): the line `decision: WAY-385 "…"` of `agent-instructions/test_size_invariant.py`,
the opening words of each sentence of WAY-339 that a line `decision:` quotes in
`process-audit/test_audit_count.py` and `task-cycle/test_cycle_stages.py`, and the naming of the tests
for the request (WAY-03).

## What you read (named by me; select the rest as `way_of_working.md` gives)

- Decisions by identifier, each whole where you change it or where its text binds yours: WAY-382, WAY-385,
  WAY-379, WAY-205, WAY-380, WAY-381, WAY-51, WAY-16, WAY-08, WAY-03, WAY-233, WAY-95, WAY-145, WAY-350,
  WAY-339, WAY-07, WAY-12, WAY-33, WAY-61, WAY-69, WAY-321, WAY-365, WAY-48. The index of the first
  seven is at `.runs/orchestrator/index.md`.
- Invariants by identifier: `ruff-blocking-rules`, `function-and-file-size`, `map-reference-target`,
  `test-method-citation`, `gate-times-refuses-impossible-entry`, `audit-series-script-paths`,
  `cross-part-imports`.
- The part map (whole, short), the glossary (whole, short; the entry `entry` matters for entry F6–F8),
  the guidelines `guidelines/coding.md` whole and `product-guidelines/coding/template.md` (the rule
  *Formatter*; the section "The tools of the standing checks") whole.
- The files whose lines you bring along: `agent-instructions/test_size_invariant.py` (line ~58),
  `process-audit/test_audit_count.py` and `task-cycle/test_cycle_stages.py` (lines `decision:` of WAY-339),
  `process-audit/test_audit_series_scripts.py` as far as the invariant `audit-series-script-paths` needs.

## The plan's section *Foundation entries* (copied word for word from `plan.md`)

| Entry | Kind | From | What depends on it |
|---|---|---|---|
| F1 — WAY-382, changed in place: the-way's code gets Ruff's formatter, in the version WAY-381 pins, with line width 100 and the other settings at their defaults, brought in by one reformatting of the whole code (WAY-205); the formatter and its invariant cover `.py` files only, never Python examples in Markdown files; a comment `fmt: off`, `fmt: on` or `fmt: skip` in a file the rule covers is forbidden and the test of the formatter fails on it; its *Verification* names F4 | decision (changed) | rows 1, 4, 5; To do 1–2 | Slices 1, 2, 3 |
| F2 — WAY-385, changed in place: a function of a script has at most 110 lines and a file of a script at most 1200, counted on the code after formatting, the same sharpness as 80/1000 on the code before the formatter | decision (changed) | row 2; To do 4 | Slices 11, 12, 13, 15, 16, 19 |
| F3 — new invariant: `elements/common/foundation_check.py` run on the-way's own repository reports no error; *Method* `test`; check: the full test of the-way's foundation in `elements/common/test_foundation_check.py`, written by Slice 4 | invariant (new) | row 3; To do 6 | Slice 4 |
| F4 — new invariant of the formatter: every `.py` file of the parts WAY-379 names stands as the formatter of the Ruff WAY-381 pins, run with `ruff.toml`, leaves it, and holds no comment `fmt: off`, `fmt: on` or `fmt: skip`; *Method* `test`; *Part* the parts of WAY-379's *Scope* and `repository` (the configuration stands there), as the template's rule *Formatter* and its paragraph on *Part* give; *Violated* `no` (WAY-205); check: the test of the formatter in `agent-instructions/test_linter_invariant.py`, written by Slice 3 | invariant (new) | To do 2; rows 1, 4, 5 | Slices 1, 2, 3 |
| F5 — WAY-379, corrected: its *Verification*, which gives as compliant "the rule of the formatter reads `none —` with the decision that departs from it", follows F1 | decision (corrected) | Decisions in play (WAY-379); To do 2 | Slice 3 |
| F6 — WAY-145, reworded: "entry" in the plan's log of changes, in its sentence and in its *Verification*, takes a word that fits there; meaning unchanged | decision (reworded) | To do 8 | Slice 10 |
| F7 — WAY-350, reworded: "entry" of the registry of running gates takes the word Slice 10 uses for it; meaning unchanged | decision (reworded) | To do 8 | Slice 10 |
| F8 — `gate-times-refuses-impossible-entry`, reworded: its sentence speaks of the registry's files without "entry"; the identifier stays (`elements/common/rules.md`, Identifiers) | invariant (reworded) | To do 8 | Slice 10 |
| F9 — WAY-339 and the invariant `audit-series-script-paths`, corrected: where they name the script that measures the cost as `task-cycle/cycle_stages.py`, they name it as `task-cycle/cycle_stages.py` with the module `task-cycle/stage_transcripts.py` that Slice 13 moves out of it, so that a change of either starts a series of the cost; meaning unchanged; marked `the cycle's` | decision and invariant (corrected) | the cycle's: follows from dividing `task-cycle/cycle_stages.py` (To do 4), with no other way open (see *Choices*) | Slices 13, 17 |

The agent of these entries also brings the line `decision: WAY-385 "…"` of
`agent-instructions/test_size_invariant.py` (line 58 at the base) to F2's new wording in the same
commit, since the check of the foundation reports a quotation that stands in no binding sentence
(WAY-12), and names that test for the request (WAY-03). It keeps the opening words of each sentence
of WAY-339 that a line `decision:` quotes (in `process-audit/test_audit_count.py` and
`task-cycle/test_cycle_stages.py`), such as "A new series of the cost of cycles, the two numbers of
WAY-337". It leaves the marks *Violated* of `ruff-blocking-rules` and `function-and-file-size` as
they stand: Slices 8 and 19 clear them in the slice in which their tests start to pass (WAY-51).
Its own check of the foundation runs with `--skip-test-citations`, since the tests of F3 and F4 come
in Slices 4 and 3 (WAY-61, WAY-321); until Slice 4 no slice runs `elements/common`'s tests.

## Working copies (word for word)

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
in the system's temporary directory, in the scratch directory of a session or in the main checkout
of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by
itself under its session's directory is moved into the agent's directory and the original removed,
except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md`
says, to the place the product's foundation settles for screenshots, and into the agent's directory
only where no such place is settled. The files that a product's own tools and tests make by
themselves are no working copy of the agent and stay outside this rule. Before the agent returns,
each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then
`git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in
the report where each copy stood and that it was removed. Where a removal fails, the agent finishes
all the same and names in the report the remainder, with its full path and the reason it stayed.

Your directory is `.runs/foundation-entries/`.

## Your return

Return: your status (`done`, `done with concerns`, `questions`, `blocked`), your commits, a one-line check
result naming what failed or did not run, and the report's path. The report holds, for each entry, its
mark (`row <n>` or `the cycle's`) with one sentence of its meaning in English and one in Polish, any pair
of examples you added word for word, the lines you brought along (with the tests that hold them named for
the request), the own-work check, your **Unread material** (what this handoff names that stayed unread or
was read in part, or `none`), **Searches not found or unclear** (or `none`), your reaches beyond this
handoff, and your working copies. A check you ran carries its command and exit code.
