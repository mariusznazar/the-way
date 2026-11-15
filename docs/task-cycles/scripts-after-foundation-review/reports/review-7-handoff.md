# Handoff — reviewer of slice 7, task `scripts-after-foundation-review`

You review one range of commits in a task cycle of the-way (`implement-task`) as an agent that did
not make the change. The person who requested the cycle has delegated intermediate choices to the
orchestrator; nothing here is the human's approval. Ask no human; a question goes to the orchestrator
as section 4 of the method gives. You are read-only: you change no file of the worktree.

## What and where

- Reviewed: slice 7. Worktree (work from its root): `the root of the task's worktree`, branch `task/scripts-after-foundation-review`. Range: **base `4c03086723435b286e1a94c92c5b12e3028be12d` to head `f1d632396d25f47cddf7efee7d4659a2e7e47e7c`** (`git diff 4c03086723435b286e1a94c92c5b12e3028be12d..f1d632396d25f47cddf7efee7d4659a2e7e47e7c` and `git log 4c03086723435b286e1a94c92c5b12e3028be12d..f1d632396d25f47cddf7efee7d4659a2e7e47e7c`, computed by you; confirm that `git rev-parse HEAD` is the head). Slice 7 alone. Information from the orchestrator (not a finding): the test Cost.test_the_stage_report_cycle_stages_writes_gives_the_share was red since Slice 3 (the audit refused the eleven-column header) and has to be green at the end of this slice; run the whole test_audit_count.py and the test_audit_series_scripts.py and say what you saw. Check the price list of Slice 4 (process-audit/price_list.md) against what the audit now requires of it.
- Method, read whole: `task-cycle/review/SKILL.md` (`review-change`); variant: the review of a slice (read nothing of `whole_change.md` or `fix.md`). A file the method names only when its step or variant comes. You have no skill tool.
- Report path: `.runs/task-cycles/scripts-after-foundation-review/reports/review-7-report.md`; its first line is `PASS f1d632396d25f47cddf7efee7d4659a2e7e47e7c` or `FAIL f1d632396d25f47cddf7efee7d4659a2e7e47e7c` (the full head), or `questions`. Graded findings and the checks you ran with command and exit code, **Unread material**, **Searches not found or unclear** and the working copies line as the method gives.
- Frozen task, whole: `.runs/task-cycles/scripts-after-foundation-review/task.md`; judge the change against the passages of the task, not the plan alone. Reviewed spec: `.runs/task-cycles/scripts-after-foundation-review/spec.md` (only the passages below). Plan: `.runs/task-cycles/scripts-after-foundation-review/plan.md` (only what is copied below).
- Answers of step 4: trust boundary **yes** — check crafted input at the boundary the slice touches: a transcript, a register, a locations file, a copy of a record from git history, a price list, a session record: a crash with a stack trace, a write outside the places the script writes, a command run, text of the input reaching a result unescaped. Irreversible operation: none (a change that only prepares one is checked as such; this one holds none).
- The executors' work is checked by the commands of the slice's *Checks* and your own; you run **no run of the whole gate** (WAY-160). Run focused tests you need, from `.runs/review-7/` for working copies only.
- Directory for your working copies: `.runs/review-7/`.
- WAY-03: a changed invariant test, or a test holding a sentence of a decision by a line `decision:`, is named in your report.

## The slice and the reports to verify

### Slice 7 — The cost prices the cache writes of each lifetime at its own price

- **Goal:** in `process-audit/audit_count.py`, the audit reads the newer form of the detailed section of `stages.md` and prices it, as the spec's D2 and D5 fix. **Form:** the header of the detailed table has three forms, each a prefix of the next — the columns the audit needs (`#`, `Stage`, `Start`, `Waiting for tools`, `Model`, `Input`, `Cached input`, `Output`); those and *Files named*; those, *Files named* and the two columns *Cache write (5 minutes)* and *Cache write (1 hour)*, in that order; a header of another form is refused with a reason, as today; the row type holds the two counts, zero for the earlier forms. **Missing field:** a table with neither write column is the earlier form, read as today (no `Error:`, the same cost, the same exit code, no new `unknown`); a table with one and not the other has a missing field: the cost is `unknown` with the reason, the result is written, the run ends with exit 1 and the `Error:` line names `stages.md` and the column that is missing; the pair is never missing when neither stands, as *Files named* is never. **Cost of a row of the newer form:** the input that is neither a cache read nor a write at *Input*, the cache read at *Cached input*, the writes of 5 minutes and of 1 hour each at its write price, the output at *Output*; a row whose cached input and writes together exceed its input is `unknown` with a reason; a row of an earlier form and the older table of tokens by model are priced exactly as today. **Price list:** `read_prices` reads both write columns of every table as it reads the other three; a table that lacks one ends the run with exit 2 and an `Error:` that names the option `--prices` and the column, never the path; a write cell is a number or `—`; a `—` in a write column is no price for that lifetime (a model so marked is priced while the row holds none of that lifetime and the cost is `unknown`, with the reason, where it holds some, never a price borrowed from another column), and a `—` in *Input*, *Cached input* or *Output* stays a model with no price at all; the price table keeps the two cases apart. **Codex:** a Codex row has `0` and `0` and is priced as today. The module description is changed where it says "Cache writes are inside *Input* … priced as input: an approximation" (it holds for the earlier forms, and says what the newer form does), the paragraph that lists the fields of `stages.md` under WAY-344 gains the two columns as a pair that is never missing when both are absent, and the description of the price list gains the new column and the rule for `—`; the text of the section *Cost* follows. The tests, each first red on the base: a copy of the earlier form without the write columns gives the cost it gave, no `Error:`, no new `unknown`, the same exit code; a copy with one write column only gives the cost `unknown`, writes the result, ends with exit 1 and the line that names `stages.md` and the column; a copy of the newer form prices a row with writes of both lifetimes at the two prices (figures that tell the 5-minute price from the 1-hour price), a Codex row with zero writes at the old price, a model with `—` in a write column and writes as `unknown`, a model with `—` and no writes as priced, and a row whose cached input and writes exceed its input as `unknown`; and the one test of the price list: a table without *Cache write (1 hour)* ends with exit 2 and an `Error:` naming `--prices` and the column. The existing tests that build a price list gain both write columns.
- **Change:** `process-audit/audit_count.py` · `process-audit/test_audit_count.py`
- **Read:** `.runs/task-cycles/scripts-after-foundation-review/task.md:34-34` To do 7 · `.runs/task-cycles/scripts-after-foundation-review/task.md:111-113` Context, cache writes, WAY-339 and the route · `.runs/task-cycles/scripts-after-foundation-review/task.md:147-147` Settlements to record, row 5 · `.runs/task-cycles/scripts-after-foundation-review/spec.md:137-178` D2, what the audit does with the columns · `.runs/task-cycles/scripts-after-foundation-review/spec.md:329-357` D5, form and reading, the module description, the tests · `foundations/decisions.md:7343-7382` WAY-337 · `foundations/decisions.md:2741-2852` WAY-344 · `process-audit/price_list.md` the price list as Slice 4 left it · the form of the stage report that Slice 3 wrote: the function report of the file task-cycle/cycle_stages.py, found by its name
- **Model:** same — it joins the writer of Slice 3, the price list of Slice 4 and the reading of three forms under WAY-344
- **Risk:** trust boundary — `process-audit/audit_count.py`
- **Checks:** start from the new tests of class `Cost` and of class `StagesForms`, and the test of the price list in class `Cost` or `Locations`, red on the base; `python -B -m unittest discover -s process-audit -p "test_audit_count.py" -k Cost -k StagesForms -k Locations -k PriceBoundary`; then the whole file `python -B -m unittest discover -s process-audit -p "test_audit_count.py"`; `python -B process-audit/audit_count.py --help` exits 0
- **Depends on:** Slice 3 · Slice 4 · Slice 6


Reports of the agents of the range (claims to verify, not evidence): `.runs/task-cycles/scripts-after-foundation-review/reports/executor-7-report.md`

## Foundation entries to read (named by the orchestrator, WAY-150)

- `foundations/decisions.md:7391-7431` WAY-337
- `foundations/decisions.md:2741-2901` WAY-344

## Working copies

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
