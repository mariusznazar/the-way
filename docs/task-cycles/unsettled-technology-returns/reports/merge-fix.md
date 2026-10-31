# Report — the fix of the reconciliation's findings

**Status:** done

## Files and commits

Range from the reviewed head `c69e355` to `9ea5fff`, one commit:
`9ea5fff docs: name the reserved rule and the task run in the skills' SKILL.md`

| File | Added | Removed |
|---|---|---|
| `project-level/task/skill/SKILL.md` | 7 | 3 |
| `task-cycle/skill/SKILL.md` | 3 | 1 |
| `task-cycle/spec/SKILL.md` | 4 | 1 |

Nothing pushed. No frontmatter changed, so no entry point changed. No check or rule moved: only the
pointers were added (WAY-256).

## Findings

All three are fixed; none is contested.

1. **`refine-task` does not name the reserved rule or the run's file — fixed.** Step 3 of
   `project-level/task/skill/SKILL.md` now says that when the task's outcome needs what
   `resolve_gaps.md` lists, that file points to `project-level/technology/reserved_choices.md`. The
   section *Orchestrated mode* says that for a run of the step that settles technology (WAY-267),
   whether `refine-task` starts it for a reserved choice or the human asked for it, the file
   `orchestrated_mode.md` points to `project-level/technology/task_run.md`. Both follow the form of
   step 1 of the same skill. Shown by the checks `condition-refine`, `condition-orchestrated` and
   the `git grep` below.
2. **`write-spec` does not name the reserved rule — fixed.** Step 2 of `task-cycle/spec/SKILL.md`
   now carries the condition of `design.md` and the file in the two-path form of the sister methods.
   Shown by `condition-spec` and the `git grep` below.
3. **`implement-task` names the file that reads the rule, not the rule — fixed.**
   `task-cycle/skill/SKILL.md:218-220` now reads: read `task-cycle/skill/reserved_return.md`, which
   checks the choice against `project-level/technology/reserved_choices.md` of the pinned the-way,
   and follow it. The condition is the sentence's own, so it covers both files. The check stays in
   `reserved_return.md`. Shown by `condition-cycle` and the `git grep` below. The reviewer's reading
   to weigh was taken: fixing costs one clause, and it reaches the case either way.

## Checks

Each ran with no pipe. Those marked *after the commit* ran on `9ea5fff`; the two test runs ran on
the same tree before the commit, which changed no file.

| Check | Command | Exit code |
|---|---|---|
| foundation (before the commit) | `python -B elements/common/foundation_check.py .` | 0, `0 errors` |
| entry points (before the commit) | `python -B agent-instructions/skill_entry_points.py` | 0, `entry points are current` |
| whitespace | `git diff --check` | 0 |
| task-cycle tests | `python -B gate/run_tests.py task-cycle` | 0, 42 tests OK |
| project-level tests | `python -B gate/run_tests.py project-level` | 0, 268 tests OK |
| foundation (after the commit) | `python -B elements/common/foundation_check.py .` | 0, `0 errors` |
| entry points (after the commit) | `python -B agent-instructions/skill_entry_points.py` | 0, `entry points are current` |
| names present (after the commit) | `git grep -n "reserved_choices\|task_run" HEAD -- project-level/task/skill/SKILL.md task-cycle/spec/SKILL.md task-cycle/skill/SKILL.md` | 0, five lines |
| `condition-refine` (after the commit) | `rg -U -c 'needs\s+a\s+language, ... that\s+no\s+decision,\s+approved\s+definition\s+or\s+accepted\s+answer\s+settles' project-level/task/skill/SKILL.md project-level/task/skill/resolve_gaps.md` | 0, one match in each |
| `condition-orchestrated` (after the commit) | `rg -U -c 'whether\s+`refine-task`\s+starts\s+it\s+for\s+a\s+reserved\s+choice\s+or\s+the\s+human\s+asked\s+for\s+it' project-level/task/skill/SKILL.md project-level/task/skill/orchestrated_mode.md` | 0, one match in each |
| `condition-spec` (after the commit) | `rg -U -c 'needs\s+a\s+language, ... that\s+the\s+task\s+and\s+the\s+foundation\s+do\s+not\s+settle' task-cycle/spec/SKILL.md task-cycle/spec/design.md` | 0, one match in each |
| `condition-cycle` (after the commit) | `rg -U -c 'needs\s+a\s+language, ... that\s+the\s+task,\s+the\s+spec\s+and\s+the\s+foundation\s+do\s+not\s+settle' task-cycle/skill/SKILL.md task-cycle/skill/reserved_return.md` | 0, one match in each |

The `...` in the commands stands for the same list of six kinds of choice, written out in the run,
each space as `\s+`.

**Not run:** the gate and the full suite, which are the orchestrator's (the handoff, WAY-160).

**No test written.** The change is text that instructs agents, and WAY-265's own *Verification* is
an agent's reading, so no test was written first and none failed first; no invariant's test is
touched. `gate/` and the two test directories ran as regression only.

## Own-work check

- **Requirement most likely not met:** "The condition has to read the same in both places" (WAY-265,
  *Rationale*, as the finding quotes it, and the handoff). A pointer with reworded conditions would
  pass a search for the path and still leave two conditions to keep equal.
- **Check:** the four `condition-*` searches above, ignoring only line breaks. Before the edit, the
  Grep tool with the same patterns found the first three conditions only in the step's file
  (`resolve_gaps.md`, `orchestrated_mode.md`, `design.md`); after it, one match in each of the two
  files. The fourth was not run before the edit: that sentence's condition was not edited.
- **Showed:** each condition reads word for word as in the step's file.

A second check, for the same defect elsewhere among the files this change adds: `git grep` over
`reserved_choices` and `task_run` outside the decision log shows each step's file that points to
them has a `SKILL.md` naming the file. `task_run.md` is named at `project-level/technology/SKILL.md:37`
and `project-level/lead/skill/SKILL.md:115`; `reserved_choices.md` at `task-cycle/change/SKILL.md:101`,
`task-cycle/plan/SKILL.md:65`, `task-cycle/review/SKILL.md:68` and now the three files fixed here.
`reserved_return.md` is named at `task-cycle/skill/SKILL.md`, which also covers the pointer at
`task-cycle/skill/planning.md:12`. This covered those three new files, not every pointer of the
change.

## Reaches beyond the dispatch

- `project-level/technology/reserved_choices.md` and `project-level/technology/task_run.md`, each
  whole: the pointers name them, and I checked that each is what the sentence says.
- `foundations/environment_facts.md`, the entry `claude-skill-nested-references`: the ground of
  WAY-265.
- `foundations/decisions.md`, WAY-267 and WAY-269, each whole: they stood in the range I read with
  WAY-265 and WAY-268.
- `agent-instructions/README.md`, as `AGENTS.md` asks of work on the-way.
- `C:\Storage\The Brain\The Brain\.ai\rules\git.md` and `knowledge_artifacts.md`, as the session's
  global instructions ask before a commit and a change to a skill.

## Searches not found or unclear

none

## Choices

- **"Points to" or "checks against", not "read".** Each pointer says that the step's file leads to
  the rule, rather than having it read in `SKILL.md` as well. Rejected: "read `X` and `Y`" — WAY-256
  names as a breach "a step names a file and has it read again though an earlier step read it", and
  the sentences in the step's files already order the reading. Cost if wrong: an agent that reads
  only `SKILL.md` sees the file and its condition but gets its order to read from the step's file,
  which it is told to follow anyway.
- **One path in `refine-task`, two in `write-spec`.** Finding 2 asks for the two-path form; finding 1
  does not, and `refine-task` writes the-way's paths singly (`SKILL.md:9`), with `SKILL.md:12-13`
  saying where the-way stands in a product, as do `resolve_gaps.md` and `orchestrated_mode.md`.
  Rejected: the two-path form there too — it would differ from the file it must be kept equal to.
  Cost if wrong: a reader in a product has to apply lines 12-13 to the path, as it does for the
  template named at line 9.
- **`of the pinned the-way` in `implement-task`**, the words of `reserved_return.md:14` and of the
  skill's own usage, rather than the two-path form. Finding 3 names no form. Cost if wrong: none
  that I can see; the same words stand in the file it points to.
- **Step 3 of `refine-task` rewrapped** so the added sentence keeps the file's line width; the
  sentences on `guideline_findings.md` are unchanged in words.

## Problems observed

None. No Minor finding was touched, and step 4 of `task-cycle/skill/SKILL.md` and step 4 of
`task-cycle/spec/SKILL.md` were left as they stand, outside the findings.
