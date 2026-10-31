# Slice 1 — The technology step runs at a task document

**Status:** `done`

## Commit

`6fb58f6` — docs: run the technology step at a task document (on `task/unsettled-technology-returns`, not pushed)

## Files changed (added / removed lines, against the slice's base `2dbf1e7`)

| File | Added | Removed |
|---|---:|---:|
| `project-level/technology/SKILL.md` | 20 | 11 |
| `project-level/technology/task_run.md` (new) | 93 | 0 |
| `project-level/technology/research.md` | 19 | 15 |
| `project-level/technology/settle.md` | 7 | 6 |
| `project-level/task/template.md` | 52 | 6 |
| `elements/decisions/template.md` | 7 | 3 |
| `.claude/skills/the-way-settle-technology/SKILL.md` (generated) | 1 | 1 |
| `.agents/skills/the-way-settle-technology/SKILL.md` (generated) | 1 | 1 |

The generator reported no obsolete output path, so nothing was removed. All files keep `i/lf`.

## Checks, on the committed tree

| Command | Exit code | Result |
|---|---:|---|
| `python -B agent-instructions/skill_entry_points.py` | 0 | `entry points are current` |
| `python -B gate/run_tests.py agent-instructions` | 0 | 18 tests, OK |
| `python -B gate/run_tests.py gate` | 0 | 18 tests, OK |
| `python -B gate/run_tests.py project-level` | 0 | 267 tests, OK |
| `python -B instruction-files/check_instructions.py . --file project-level/technology/task_run.md` | 0 | 0 errors, 1 warning, on `AGENTS.md:21` (`_zadania\`), not a file of this slice |
| `git diff --exit-code 2dbf1e7 -- project-level/technology/start.md project-level/technology/list.md project-level/technology/close.md project-level/technology/running_product.md project-level/definition_template.md` | 0 | no difference |

Not run: the full suite, which is the cycle's run (WAY-160). No test was written: the slice changes
no script, as its *Checks* say. No agent was run at a real task document, so what an agent does with
these texts is not tested.

The first run of the instruction check warned that `.runs/technology/` in `task_run.md` does not
exist. The sentence now names `.runs/technology/<choice>.md`, as the other files do, and the warning
is gone.

## Own-work check (section 3)

- **Requirement:** spec decision 4, "Neutral wording, not a copy", with the *Start* to *Orchestrated*
  differences: `research.md`'s reader never sees `task_run.md`, and a run at a task must not fall
  into a definition's rule. This is the requirement the text most likely misses.
- **Checks:**
  - `grep -n "definition"` on `research.md` and `settle.md`. It shows the word only where a sentence
    names both documents, in the path `definition_template.md`, and in sub-step 7, which a run at a
    task replaces.
  - A throwaway script, `python -B own_check.py`, exit code 0. It looked for each required marker,
    field, pointer and rule in its file, with 0 missing, and for the description's form: one line,
    neither `: ` nor ` #`, 500 characters. This shows that nothing was left out, not what an agent
    does with it.
  - A hand trace of a run at a task through `SKILL.md`, `start.md`, `list.md`, `settle.md` and
    `close.md`, looking for each definition-only instruction. All are overridden in `task_run.md`:
    - `Projected foundation changes` and the look of `running_product.md`;
    - the status line and the bullet on a decision the project changes;
    - sub-step 7 and the readiness check.
- **Result:** nothing missing. No check failed and passed on a rerun.

## Reaches beyond the dispatch

- `plan.md:1-30`, read by mistake while confirming the slice's place. Nothing was taken from it that
  the handoff does not carry.
- `git`, `scripts` and `knowledge_artifacts`, the session's global rule files, read as the session's
  instructions ask.
- `agent-instructions/README.md`, read because the root `AGENTS.md` asks for it.
- `installation/install.py:34` and `installation/README.md`, a search for `settle-technology`, to see
  whether a new file beside the skill needs a listing. It does not.
- A search of `*.py` for `Questions to settle`, `task/template` and `decisions/template`, to see
  whether a script parses the sections the template gains. None does.
- `task-cycle/change/slice.md`, named by the method.

Each foundation entry the handoff names was read whole, at the handoff's current ranges.

## Searches not found or unclear

- `orchestrated_mode.md` has no routing for a run yet, and `resolve_gaps.md` and `find_settlements.md`
  have no text for it. `task_run.md` and `SKILL.md` point to them as the plan gives; until the later
  slices land these pointers lead to nothing specific.
- `reserved_choices.md` does not exist yet. This slice names only the glossary term, not the file.
- Unclear: the spec names no field or list that gives the research agent the decision a human opened.
  See *Observations*.

## Choices made

| Choice | Way rejected | Cost if wrong |
|---|---|---|
| *Close* sets `Status: refining`; the spec says only that the document reads `waiting for human` while the human owes a choice | leaving the status as it stands, so steps 4 to 6 would run under `waiting for human` | one line to change |
| `waiting for human` runs from the showing of the list until the human has settled what the run lists | switching it at each list and table | one line; research between tables then shows as waiting |
| Head line is `task documents: <path> · <path>`, opening the report, in lower case like `critique: passed` | a heading, or a field at the end | a reused report would need rereading |
| A settled choice goes into the question that already asks it, otherwise a new one | always a new question | a question could stand twice |
| *Answer* of a human-opened choice names the decision it changes, beside the nested item | the nested item alone | the row-writing step has less to read |
| Labels `Note, YYYY-MM-DD:`, `Preference:`, `Waits for:`, `Changes:` in English, as structure | document-language labels | a resumed run reads them less surely |
| The template shows a second sample question for a run's fields, with an inline `(hypothesis)` mark | the three fields added to the general sample | none beyond length |
| `research.md` and *Settle* say the leader gives the path of each affected task's document where one run serves several | leaving that to the orchestrated slice | the head line could not be written without it |
| *Rejected*'s path stands in the second rule of `decisions/template.md`, with the other two fields | splitting it between the two rules | a reader of the first rule alone misses *Not chosen*; it already sends that reader to the question |
| Title `# Settle technology` | `# Settle technology for a project or a task` | none |

Every choice is of wording or form, as *Left to the maker* gives; none is a design choice left open.

## Adaptations

None. The plan and the code agreed. The handoff's ranges were used where they differ from the plan's.

## Foundation entries

WAY-121, WAY-122, WAY-123, WAY-137, WAY-138, WAY-265 and the glossary term *reserved choice* hold
against the text; no entry differs.

## Observations

- `settle.md` sub-step 1 gives the research agent the binding sentences of each decision the list
  names `held by`. A choice the human opened stands `— open` with the decision nested under it, so
  that decision's sentences are not among what the leader gives. The agent sees only its number, and
  the task document quotes it only once *Decisions in play* is filled. No spec passage asks for this,
  so nothing was added. A later slice or the orchestrator may want one clause in *Settle*.
- A first attempt to make the edits in `SKILL.md`, `research.md` and `settle.md` by a shell script
  stopped on a shell quoting error and changed nothing. The edits were made one by one. Cause not
  looked into.
