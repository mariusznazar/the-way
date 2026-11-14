# Report - slice 7 (The column *Goes to* in the table of a task)

## Status

`done`

## Commits

- `f20a62c` Put the column Goes to in place of Kind in the task settlements table (on `task/co-trafia-do-dziennika-decyzji`, on top of base `64cd4ad`). Not pushed.

## Files changed

| File | Added | Removed |
|---|---|---|
| `project-level/task/template.md` | 9 | 4 |
| `elements/common/skill/task_variant.md` | 7 | 4 |
| `elements/common/skill/build_table.md` | 4 | 2 |
| `task-cycle/skill/foundation_step.md` | 2 | 2 |

What changed:

- `project-level/task/template.md`: the header of *Settlements to record* reads `| # | Settlement | Goes to | Source | What the cycle would otherwise guess |` (the *Kind* column is replaced). The paragraph under "What each section carries" now says *Goes to* names the place the settlement goes, as the questions of "Where it goes" in `elements/decisions/template.md` give it, names the values by place only (no question copied), and says a settlement the questions answer "nothing" is a rejected row.
- `elements/common/skill/task_variant.md`: step 1 also reads the **Where it goes:** bullet of `elements/decisions/template.md`; step 2 replaces the kind list with "a settlement that the questions of 'Where it goes:' place", a decision passes the questions in order and its first "yes" gives *Goes to*; step 5 says rows are counted per place (*Goes to*) instead of per kind.
- `elements/common/skill/build_table.md`: the sentence that gives a row's kind keeps *Kind* for the definition variant and says that in task mode the task variant's lines give the column *Goes to*.
- `task-cycle/skill/foundation_step.md`: the sentence that wrote a row "as an entry of its kind" now writes it in the place its column *Goes to* names, as an entry of its kind where the column names an entry. The rest of the file is unchanged.

## Checks

| Check | Command | Exit code | Result |
|---|---|---|---|
| Foundation check | `python -B elements/common/foundation_check.py` | 0 | `0 errors`; one `listed:` line for `WAY-17` (expected, stops nothing) |
| Project-level tests | `python -B gate/run_tests.py project-level` | 0 | Ran 275 tests, OK (run on the final text) |
| Agent-instructions tests | `python -B gate/run_tests.py agent-instructions` | 0 | Ran 25 tests, OK (run on the final text) |
| Whitespace check | `git diff --check` | 0 | clean |

Notes on the runs:

- The first pass of the project-level and agent-instructions runs (before a whitespace-only reflow of two lines in `build_table.md` and `foundation_step.md`) also gave exit 0, 275 tests OK and 25 tests OK. The final rerun on the committed text is the one above.
- The project-level suite is slow in this environment: about 7 to 8 minutes wall clock on the rerun. It was run in the background, and I waited for it.
- No test was written or changed. This slice has no invariant and no failing-first test: its change is prose in the process files, and the checks above are the ones the slice names.

## Own-work check

Requirement: the four files must carry the column *Goes to* in place of *Kind*, each pointing to the questions of "Where it goes" and copying none of their words, and the definition variant must keep *Kind*.

Check: `grep -n "Goes to"` over the four files, and a search for `| Kind |` and `*Kind*` in `project-level/task/template.md` and `elements/common/skill/task_variant.md`.

Result: the header line reads `| # | Settlement | Goes to | ...`; no `| Kind |` or `*Kind*` remains in the two task files; each of the four files names *Goes to* at the place its change requires. The four files do not repeat the five questions. The task template's paragraph names the values only by place. The definition table `project-level/definition_template.md` still has *Kind* (line 288), as D5 requires.

## Choices made

- The paragraph in `project-level/task/template.md` lists the place values (`decision`, `invariant`, `glossary term`, `environment fact`, a sentence of an entry, a skill or instruction file, the guidelines of a discipline, the product's data or code) but gives no question wording. Rejected: a bare "as the questions give it" with no list, because the header's values would then be unnamed in the template. Cost if wrong: a value list that drifts from the questions; the list is short and names places only.
- `build_table.md` keeps *Kind* for the definition variant in words and gives the task-mode column by pointer, as the handoff says. Rejected: rewriting the definition variant's table. Cost if wrong: none found.
- Step 5 of `task_variant.md` changed "how many rows of each kind" to "of each place (*Goes to*)". Rejected: leaving "kind". Cost if wrong: the count is by place, not by kind, which is what the column now carries.

## Reaches beyond the dispatch

- Read whole the four target files and `elements/decisions/template.md` (the bullet "Where it goes:" and the template's sections read by the step).
- Read `task-cycle/change/slice.md` (named by my variant) and `task-cycle/change/SKILL.md`.
- Read the spec passages D5 (lines 113-127) and D6 (lines 129-139), the task passages `task.md` lines 30-40 and 92-100.
- Read WAY-134 in `foundations/decisions.md` from line 3611 down to the start of its *Rejected* field (the entry continues past line 3700; see Unread material).
- Grepped `*.md` for *Kind* and "its kind" to find mismatches outside the four files (see concerns).

## Unread material

- `foundations/decisions.md`: WAY-115 (line 2833), WAY-113 (line 2733), WAY-114 (line 2787), WAY-126 (line 3296), WAY-124 (line 3205), WAY-315 (line 10547), WAY-11 (line 390), WAY-33 (line 987). Not read by me. The slice's change follows D5 and D6 and WAY-134, which I read in part, so the unread entries were not needed for the wording. The slice named them for context.
- WAY-134: read from line 3611 through the start of *Rejected*; the rest of the entry (*Rejected*, *Origin*) was not read.
- `foundations/glossary.md` lines 61-65 (foundation step) and `foundations/part_map.md` lines 65-75, 77-91, 93-103: not read. Not needed for the four files' wording.
- `task.md` lines 36 and 94-98: read at lines 30-40 and 92-100, which cover them.
- `elements/decisions/template.md`: read whole.

## Searches not found or unclear

- None of my own searches came up empty. The handoff's *Read* line for `foundations/decisions.md` used stale ranges; I used the current start lines the handoff gives in its notes (WAY-134 at line 3611).
- Unclear: the handoff said "the sentence of `elements/common/skill/build_table.md` that gives a row's kind". The file has one such sentence (line 7). I took that as the sentence to change.

## Concerns

- `project-level/definition_template.md` (line 288) still has the column *Kind*. D5 says the definition variant keeps *Kind*, so this is intended. Stated only so the orchestrator sees the two tables still differ by one header, as D5 names as its cost.
- `foundations/decisions.md` WAY-115 (line 2836) still says the table shows "its kind". D5 says WAY-115 needs no change because in task mode the new column carries the kind for the entries. Not changed.
- The handoff's "Questions carried to cycle" in `task.md` asks whether *Goes to* replaces *Kind* or stands beside it. My change follows D5: it replaces it in the task table. This answers that question for the task; it is the orchestrator's to confirm.
- The gate's project-level suite runs about 7 to 8 minutes here; it was run in the background and waited for.
- Background processes: the monitors and the background check command I started are all stopped (TaskStop reported success for each still running; one had already completed).
