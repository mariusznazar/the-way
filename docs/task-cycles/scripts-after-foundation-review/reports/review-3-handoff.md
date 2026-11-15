# Handoff — reviewer of slice 3, task `scripts-after-foundation-review`

You review one range of commits in a task cycle of the-way (`implement-task`) as an agent that did
not make the change. The person who requested the cycle has delegated intermediate choices to the
orchestrator; nothing here is the human's approval. Ask no human; a question goes to the orchestrator
as section 4 of the method gives. You are read-only: you change no file of the worktree.

## What and where

- Reviewed: slice 3. Worktree (work from its root): `the root of the task's worktree`, branch `task/scripts-after-foundation-review`. Range: **base `40559b68ba26673de95e7c8d369c60230f219b4e` to head `336ae16e1e5f8821a3fb800967da4e8c453b60c6`** (`git diff 40559b68ba26673de95e7c8d369c60230f219b4e..336ae16e1e5f8821a3fb800967da4e8c453b60c6` and `git log 40559b68ba26673de95e7c8d369c60230f219b4e..336ae16e1e5f8821a3fb800967da4e8c453b60c6`, computed by you; confirm that `git rev-parse HEAD` is the head). MECHANICAL-CHECK INFORMATION from the orchestrator (not a finding; grade and scope are yours): (1) the executor changed one file outside the slice's Change list, process-audit/test_audit_count.py (a fixture gained the two lifetimes of cache_creation, because the stage script now needs the field); (2) one existing audit test, test_the_stage_report_cycle_stages_writes_gives_the_share, is red after this slice because the audit refuses the new eleven-column header until Slice 7 (the plan names it; the orchestrator accepted it as autonomous choice Q3). Judge whether the cause is exactly that and nothing else.
- Method, read whole: `task-cycle/review/SKILL.md` (`review-change`); variant: the review of a slice (read nothing of `whole_change.md` or `fix.md`). A file the method names only when its step or variant comes. You have no skill tool.
- Report path: `.runs/task-cycles/scripts-after-foundation-review/reports/review-3-report.md`; its first line is `PASS 336ae16e1e5f8821a3fb800967da4e8c453b60c6` or `FAIL 336ae16e1e5f8821a3fb800967da4e8c453b60c6` (the full head), or `questions`. Graded findings and the checks you ran with command and exit code, **Unread material**, **Searches not found or unclear** and the working copies line as the method gives.
- Frozen task, whole: `.runs/task-cycles/scripts-after-foundation-review/task.md`; judge the change against the passages of the task, not the plan alone. Reviewed spec: `.runs/task-cycles/scripts-after-foundation-review/spec.md` (only the passages below). Plan: `.runs/task-cycles/scripts-after-foundation-review/plan.md` (only what is copied below).
- Answers of step 4: trust boundary **yes** — check crafted input at the boundary the slice touches: a transcript, a register, a locations file, a copy of a record from git history, a price list, a session record: a crash with a stack trace, a write outside the places the script writes, a command run, text of the input reaching a result unescaped. Irreversible operation: none (a change that only prepares one is checked as such; this one holds none).
- The executors' work is checked by the commands of the slice's *Checks* and your own; you run **no run of the whole gate** (WAY-160). Run focused tests you need, from `.runs/review-3/` for working copies only.
- Directory for your working copies: `.runs/review-3/`.
- WAY-03: a changed invariant test, or a test holding a sentence of a decision by a line `decision:`, is named in your report.

## The slice and the reports to verify

### Slice 3 — The stage report holds the cache writes of each lifetime for each stage and model

- **Goal:** the detailed section of the report of `task-cycle/cycle_stages.py` (*Stages: start, waiting for tools and tokens by model*) gains, after *Files named*, the columns *Cache write (5 minutes)* and *Cache write (1 hour)* (D1): for each row and each model, the tokens the model's responses wrote to the cache at each lifetime, from `message.usage.cache_creation.ephemeral_5m_input_tokens` and `ephemeral_1h_input_tokens`, summed like the other counts, whole numbers in the form of the other token cells. *Input* keeps its meaning and its figure (input, cache writes and cache reads together); the line "Tokens in all", the whole-cycle table by model and the first table keep their figures and columns; the module description and the paragraph above the section say that *Input* holds the writes and what the two columns are. A Codex row writes `0` and `0`, with no warning and no `unknown`; a row with no token usage keeps the model `—` or `unknown` and zero counts. Where the two lifetimes of a response do not add up to its `cache_creation_input_tokens`, a `Warning:` line names the transcript, the figures stand as read and the exit code is 0. The new fields join the *Needed* list of Slice 2 (`message.usage.cache_creation` and its two lifetimes, absent or no whole number: exit 2 naming the field), under the same one test and the same pin. The tests: the detailed table of a Claude Code stage holds the two columns with the figures of the two lifetimes of its responses, a Codex row holds `0` and `0`, a row of one model with both lifetimes keeps them apart; and the test across the two scripts — the same Claude Code transcript given to `cycle_stages.py` and `cycle_measures.py` gives the same tokens written at each lifetime in the totals of both. `task-cycle/cycle_measures.py` and `mechanism_measures.md` do not change. After the slice the audit still reads the report: its reading ignores nothing it needs, and no other script changes here.
- **Change:** `task-cycle/cycle_stages.py` · `task-cycle/test_cycle_stages.py`
- **Read:** `.runs/task-cycles/scripts-after-foundation-review/spec.md:87-98` D1, the route · `.runs/task-cycles/scripts-after-foundation-review/spec.md:132-135` D1, the price of the route · `.runs/task-cycles/scripts-after-foundation-review/spec.md:169-174` D2, Codex rows · `.runs/task-cycles/scripts-after-foundation-review/spec.md:249-264` D4, new data, Codex row, the warning · `.runs/task-cycles/scripts-after-foundation-review/spec.md:308-324` D4, the test, the test across the two scripts, the series of the cost · `.runs/task-cycles/scripts-after-foundation-review/task.md:34-34` To do 7 · `foundations/decisions.md:7343-7382` WAY-337 · `foundations/decisions.md:7384-7469` WAY-339 · `foundations/decisions.md:2741-2852` WAY-344 · `foundations/invariants.md:116-145` script-language, script-imports, script-subprocesses · `foundations/part_map.md:101-111` task-cycle · `task-cycle/cycle_measures.py` the whole file, for the figures of the test across the two scripts
- **Model:** cheaper
- **Risk:** trust boundary — `task-cycle/cycle_stages.py`
- **Checks:** start from the new tests in `task-cycle/test_cycle_stages.py` (the two columns of a Claude Code stage, `0` and `0` of a Codex row, the two lifetimes of one model kept apart, the test across the two scripts, the transcript without `message.usage.cache_creation`), red on the base; `python -B -m unittest discover -s task-cycle -p "test_cycle_stages.py"`; `python -B -m unittest discover -s task-cycle -p "test_cycle_measures.py"`; `python -B -m unittest discover -s process-audit -p "test_audit_count.py" -k Cost -k StagesForms` (the audit still reads the report of the earlier forms)
- **Depends on:** Slice 2


Reports of the agents of the range (claims to verify, not evidence): `.runs/task-cycles/scripts-after-foundation-review/reports/executor-3-report.md`

## Foundation entries to read (named by the orchestrator, WAY-150)

- `foundations/decisions.md:7391-7431` WAY-337
- `foundations/decisions.md:7432-7585` WAY-339
- `foundations/decisions.md:2741-2901` WAY-344
- `foundations/invariants.md:116-125` script-language
- `foundations/invariants.md:126-135` script-imports
- `foundations/invariants.md:136-145` script-subprocesses
- `foundations/part_map.md:101-112` task-cycle

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
