# Executor report — slice 2: spec step asks for the reason of existing code

**Status:** done

## Commits

- `ebe9998` — Ask in the spec step for the reason of existing code before a design rebuilds it
  (branch `task/decision-log-second-round`, worktree `the task's worktree`). Not pushed.

## Files changed

- `task-cycle/spec/design.md` — 4 lines added, 0 removed. One bullet added in "Settle the design",
  after the bullet "Weigh two or three ways with their costs and recommend one."

Text of the bullet, as committed:

> Where the choice the spec settles rebuilds code that already exists, look in the description of the
> commit or of the merged request that brought the shape of that code for the reason of it, and quote
> what you find with the identifier of the commit. Where that description holds no reason, ask the
> orchestrator, as above; write no reason of your own for the code.

No other file changed. No frontmatter change, so no entry point was regenerated.

## Checks

| # | Command | Exit code | Result |
|---|---|---|---|
| 1 | `python -B elements/common/foundation_check.py` | 1 | Lists 509 lines across 105 files, all for files of other slices or of the existing withdrawn-number references the handoff says stand. Zero lines name `task-cycle/spec/design.md` (checked with a search of the output for `design.md`, count 0). Check passes for this slice's *Change* file. |
| 2 | `python -B gate/run_tests.py task-cycle` | 0 | Ran 440 tests, OK. |

No test was written for this change: it is prose for an agent, and make-change section 2 gives
no test for prose for people or for a text an agent reads that is not a script's output. No failing
run was therefore needed. The gate was not run without a directory (as the handoff forbids).

## Own-work check (make-change section 3)

- **Requirement most likely unmet:** the bullet has to sit inside "Settle the design" and say the
  same thing as the decisions template's *Recovered decisions* sentence (commit or merged request
  quoted with its identifier before `unknown`), with the question to the orchestrator where that
  description is empty, and no reason written by the designer.
- **Check:** read the `design.md` section as committed, against the goal and the template sentence.
  Plus check 1 above, that the foundation check names nothing in `design.md`.
- **Result:** the bullet is in "Settle the design"; it names the commit or merged request, the
  identifier, the question to the orchestrator, and the prohibition on an own reason. The foundation
  check reports nothing in the file.
- **Wording choice:** "ask the orchestrator, as above" refers to the batch-of-questions rule
  already in the same section (the bullet "Send your questions to the orchestrator in batches").
  I chose it to avoid restating that rule. Cost if wrong: a reader might take "as above" for a
  different rule; the batch rule is the only one it can point to in that section.

## Reasons added

No sentence of reason was added to any foundation entry. The bullet states a rule, not a reason
for an entry. Its source is the *Recovered decisions* section of `elements/decisions/template.md`
(as Slice 1 left it, sentence "The description of the commit, or of the merged request, that brought
the shape of the code is a source: the agent looks there before it writes `unknown`, and quotes
what it finds with the identifier of the commit") and WAY-29 in `foundations/decisions.md`
(*Rationale*: the description of the commit or of the merged request is where a reason stands).

## Entries left under the "stay" rule

None. This slice removed no number and changed no reference to a withdrawn number.

## Working copies

None made. No worktree, clone, script or prepared input was created; `.runs/executor-2/` was not used.

## Unread material

- `.runs/task-cycles/decision-log-second-round/plan.md` — not read; the handoff copies my section
  word for word, and I worked from the copy.
- `project-level/technology/reserved_choices.md` — not read. make-change section 5 and design.md
  send to it only where a language, framework, library, store, login or place to run is needed.
  This change makes no such choice.
- `agent-instructions/README.md` and the-way `AGENTS.md` — not read; the dispatch names neither.
- `task-cycle/spec/SKILL.md`, `elements/decisions/template.md`, `foundations/decisions.md` WAY-29,
  `task.md` lines 1-60 (including To do, lines 33-40) — read whole, as the handoff names them.

## Searches not found or unclear

- None not found. One point was unclear to me and I resolved it by reading: the handoff's "Read"
  line gives `foundations/decisions.md:908-941` for WAY-29, which is the base's range. I found the
  entry by its heading `### WAY-29` in the log as it stands (commit `8d04d89` already applied it);
  its text matches the commit's added lines.

## Concerns

- The foundation check's exit code is 1 at this commit, from lines of other slices' files. The
  handoff says this stands; I note it so the orchestrator does not read exit 1 as a failure of this
  slice.
