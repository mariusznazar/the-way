PASS 168b055e5152030e0618e50f02cc6ec0bed51643

# Review of the whole change — decision-heading-level

Range `2f51e6c..168b055`, one commit; `git rev-parse HEAD` gives the head named in the dispatch.
Route: one author without a plan, so no finding comes from a slice. No invariant test changed.

## Findings

### Critical

None.

### Important

None.

### Minor

1. `task-cycle/change/SKILL.md:34` and `elements/common/way_of_working.md:75`. The re-wrap of the
   two passages is uneven: line 34 of the skill is 101 characters wide, while the prose around it
   keeps to 100 (lines 32 and 33 are 99 and 98), and in `way_of_working.md` the text stops at 63
   characters on line 75 and goes on at line 76, with no paragraph break between them. It matters
   only to someone editing the file: no word changes, the rendered text is the same, and no check
   of the repository holds line width. Evidence: `awk` widths of those lines; a whitespace-blind
   comparison with the base (see Checks) shows the wrap is the only other difference.

## Coverage of the task

- *To do* 1: met. After "Read each decision found whole, as the range of lines from its heading to
  the next heading" stands exactly "(`###` in the decision log, `##` in the other foundation
  files)". It stands before the comma of ", with its rationale and *Rejected*", as the author's
  report says; the sentence stays grammatical and its tail is not cut off.
- *To do* 2: met. After "The foundation entries the dispatch names by identifier, each whole"
  stands exactly ", an entry running to the next heading (`###` in the decision log, `##` in the
  other foundation files)", and the base's ", and the guideline files it names" follows it.
- *Need*: met. Both places an agent reads a foundation entry from, as the task chose them, now name
  the level of each file.
- *Questions to settle*: the answer "two insertions" is kept; `task-cycle/review/SKILL.md`,
  `task-cycle/spec/SKILL.md` and `task-cycle/plan/SKILL.md` are not in the diff.
- *Out of scope*: no script for taking entries out was added; the range changes two files.
- *Settlements to record*: `none`, 0 accepted; nothing to write. No projected entry is carried.
- *Questions carried to cycle* and *Human actions*: `none`.

## Against the foundation

- The claim most likely to be false was that the levels the insertion names hold everywhere. They
  do: `foundations/decisions.md` has 237 `###` entries, no `####`, and one `##`, which is
  `## Withdrawn identifiers`; `environment_facts.md`, `glossary.md`, `invariants.md` and
  `part_map.md` have `##` and no `###`. The task's addresses hold: `foundation_check.py:252` reads
  decisions by `### `, `:288` and `:313` read the others by `## `. So the levels also bind products,
  where the installer seeds `decisions.md` with `# Decision log` alone (`installation/install.py:88`).
- Other names under `foundations/` in the repository (`violated_invariants.md`, `human_verdicts.md`,
  `known_violations.md`) are files of the earlier form, which `migrate_foundation.py` removes, so
  "the other foundation files" misses no current file (invariant `foundation-file-kinds`).
- An entry's end: `blocks()` in `foundation_check.py:133` ends a block at a heading of any level,
  which agrees with "to the next heading". The last decision, WAY-279, ends at
  `## Withdrawn identifiers`, not at a `###`; an agent that stops only at `^### ` reads the withdrawn
  table too and nothing false, so this is no finding.
- WAY-150: the method keeps its selection; the insertion says how far an entry runs and changes no
  selection or reading rule. WAY-256: each insertion is a clause in place, in the text that already
  carries the rule, so no fragment moves. WAY-127: the description of `make-change` is unchanged and
  the entry points are current. WAY-125, WAY-35: neither is reached; `change/SKILL.md` is no
  element's skill, and the copy of the sentence is the task's own choice, with its cost stated there.
- No foundation entry is written or changed, so WAY-263 and the search of WAY-33 are not reached.
- Invariants reached: the 13 that name `every`; no invariant names `elements-common` or `task-cycle`.
  No file is added, moved or generated, no script changes, and the inserted text holds no link and
  no `@`. `return-step-record` falls to the later return step and to a `{merge-onto}` that does not
  yet exist.
- Guidelines: the repository has no `guidelines/`, as the handoff says; there is nothing to select.
- Reserved choice, trust boundary, operation that cannot be undone, user interface: none reached.
  Neither file lies in a *Trust boundary* of the part map.

## The author's own-work check

The author named the placing and wording of the two insertions, and checked it by reading. For a
change that is two given insertions, that is where it is weakest, and a reading would catch a
mismatch. The comparison below gives the same result by another route. The report's other claims
hold: file counts (+2/-1, +3/-2), the 42 tests, the foundation check. Its choice of placing the first
insertion before the comma is right.

## Declined to judge

None.

## Checks

| Check | Result |
|---|---|
| `git diff --check 2f51e6c..168b055` | exit 0 |
| `git ls-files --eol` on both files | `i/lf w/lf`, line endings unchanged |
| `python -B elements/common/foundation_check.py .` | exit 0, "0 errors" |
| `python -B gate/run_tests.py task-cycle` | exit 0, 42 tests OK |
| `python -B gate/run_tests.py agent-instructions` | exit 0, 18 tests OK |
| `python -B -m unittest discover -s gate -p "test_skills_reach_the_way_sessions.py"` | exit 0, 2 tests OK |
| `python -B agent-instructions/skill_entry_points.py` (no `--write`) | exit 0, "entry points are current" |
| Scratch script over `git show` of base and head, whitespace normalized: the task's anchor stands once in the base, anchor plus the task's insertion once in the head, and the head minus the insertion equals the base | all true for both files, exit 0 |
| `git grep` over `*.py` for `way_of_working` and `change/SKILL.md` | no test reads the prose of `way_of_working.md`; `installation/test_install.py:282` only appends to the description of a temporary copy of the skill |
| `git grep` for `way_of_working.md:<n>` and `change/SKILL.md:<n>` | no citation of a line number to go stale |
| Heading counts per foundation file, by `grep -c` | as given above |
| `git status --short` after every run | empty; the reviewed worktree is unchanged |

Not run: the full gate, which is the orchestrator's by the handoff and WAY-160. The test
directories of `elements/common` and `installation` were not run: no test there reads the changed
prose.

## Reaches beyond the dispatch

- `elements/common/foundation_check.py:133-143`, `:235-321`: to confirm the task's addresses and how
  a block ends.
- `installation/install.py:88` and the top of `foundations/decisions.md`: what a product's log
  starts from.
- `elements/common/migrate_foundation.py:36-37`: what the three other file names are.
- `installation/test_install.py:275-300`: whether a test reads the changed skill's text.
- `agent-instructions/README.md`: root `AGENTS.md` sends work on the-way there.
- `foundations/invariants.md` read whole, 307 lines, where the method gives a search of *Part*. Part
  map and glossary were read whole as the method allows. The 95 decisions whose *Scope* names
  `elements-common` or `task-cycle` were each read whole, WAY-150 and WAY-256 of *Decisions in play*
  among them.

## Searches not found or unclear

- `task-cycle/review/SKILL.md`, section 4, has the reviewer return the first line, the counts of
  blocking, Minor and out-of-scope findings and the report path, citing WAY-148, while the handoff
  and WAY-148 itself ask for a one-line check result naming what failed or did not run. The return
  gives both.
