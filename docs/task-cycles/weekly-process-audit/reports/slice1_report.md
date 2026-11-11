# Report — executor of slice 1 (`make-change`: a slice)

**Status:** done with concerns

## Files changed and commits

| File | Added | Removed |
|---|---|---|
| `process-audit/problem_register.md` (new) | 100 | 0 |
| `foundations/part_map.md` | 10 | 0 |

Commit: `4443973ab89d8d2aea76abe650c6090eb8ddddba` — "Add the part process-audit with the template of the register of problems", on `1adca16`.

## Checks

| Command | Exit | Result |
|---|---|---|
| `python -B elements/common/foundation_check.py` (on `1adca16`, before the change) | 1 | 16 errors, each "`process-audit` names no part" (decisions.md:256, 1034, 2005, 10341, 10644 … 10892) — the expected failing run |
| `python -B elements/common/foundation_check.py` (entry written, files not yet committed) | 1 | 1 error: the pattern `process-audit/**` matches no file git tracks — expected until the commit |
| `python -B elements/common/foundation_check.py` (after commit `4443973`) | 0 | 0 errors |
| `python -B gate/run_tests.py elements/part-map` | 0 | 39 tests OK |
| `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` | 0 | checked 276 files, 0 listed |

No test was written: the slice adds prose and a map entry, no behaviour (`make-change` §2, "prose for people gets no test"). The full suite was not run (the cycle's run before the request).

## Own-work check

- Requirement most likely unmet: the template must be "in a form that the counting command reads" without
  ambiguity, the list of classes and its changes included.
- Check: a throwaway script, `a scratch file outside the repository`,
  that reads the committed template only by the rules the template states (table found by its `##` heading and its header row,
  rows until the first line not starting with `|`, names `[a-z0-9-]+` and unique, *Added* `start` or a date, *Withdrawn* `none`
  or a date, weights exactly the four levels).
  - `python -B -I …\parse_register.py process-audit/problem_register.md` → exit 0: 7 classes, 4 weights, empty *Issues* and
    *Problems*, 0 errors.
  - Against a mutated copy (a `|` inside a class's meaning, a class named `Foundation_gap`) → exit 1, 4 errors naming both — the
    check catches the breaks it is for.
- Also scanned the committed template for a drive path, a note link and a person's name: none.

## The shape of the template

`process-audit/problem_register.md` is a Markdown document of four tables, each under a fixed `##` heading with a fixed header
row; text outside the tables is not read, so the user may rewrite it. The rules of reading stand in the template's section
"What the counting command reads": rows follow the header and separator with no blank line, a table ends at the first line not
starting with `|`, a cell holds no `|` and no line break, dates `YYYY-MM-DD`, commits as the full 40-character hash, class and
issue names lower-case letters, digits and hyphens, unique in their table.

| Heading | Header row | Values |
|---|---|---|
| `## Classes` | `\| Class \| Meaning \| Added \| Withdrawn \|` | seven starting classes: `confirmation`, `check-not-run-or-uncertain`, `ambiguity-settled-by-agent`, `foundation-gap`, `known-problem-left`, `stale-reference`, `process-remark`; *Added* `start` or a date; *Withdrawn* `none` or a date |
| `## Weights` | `\| Weight \| Meaning \|` | `no problem`, `Minor`, `Important`, `Critical`; fixed levels, the meanings adaptable |
| `## Issues` | `\| Issue \| What \| Fate \| Fix \|` | *Fate* `open` · `fixed` · `dropped`; *Fix* the-way commit for `fixed`, else `none` |
| `## Problems` | `\| Repository \| Record \| Stages \| What \| Class \| Weight \| Issue \|` | *Record* the commit adding the record's copy; *Stages* joined by ` · `; *Issue* a name or `none` |

How a change of the list of classes shows (row 10, WAY-336): a class withdrawn keeps its row with a *Withdrawn* date; a class
added carries its *Added* date; a change of a class's meaning is a withdrawal and an addition under a new name on the same date.
Each date in *Added* or *Withdrawn* starts a new series. The template states this; it does not say how the command places a cycle
in a series — that is Slice 5's.

## Choices made

| Choice | Way rejected | Cost if wrong |
|---|---|---|
| Two tables, *Issues* and *Problems*, with a problem naming its issue; the fate and the fix stand once per issue | fate and fix columns on every problem row — two rows of one issue could disagree | Slice 5 parses a join instead of one table; a user's tool must keep both tables |
| The list of classes carries its own change dates (*Added*, *Withdrawn*) | a separate log of changes of the list; a version number of the list on every problem row | if Slice 5 needs to place a cycle in a series by something other than a date, the form needs another column |
| *Fate* is the closed set `open` · `fixed` · `dropped` | only `open` and `fixed` — an issue decided against would count as open and waiting for ever | a user wanting another fate has to change the command too; Slice 5 must accept exactly these |
| *Repository* is the repository's name as the user's locations file keys it (WAY-320: the keys are repository names) | the record's *Product repository* line, which may be a remote address | if Slice 3/5 finds repositories another way, this column's sentence changes |
| *Record* is the full hash; where a cycle committed its copy more than once (a correction repeats the pair, `task-cycle/record_template.md`), the commit of the copy that holds the report the problem was found in | the first copy's commit always | two commits may name one cycle; see concerns |
| Added a *What* column (one line) to *Problems* and *Issues* | no description — the human in the weekly session could not tell what a row is | one more column for the tool to fill |
| Weight meanings taken from the grades of `task-cycle/review/SKILL.md` §3 (reach below) | the levels with no meaning | none beyond wording |
| The counting command is named in words, not by `process-audit/audit_count.py` | the path the plan gives — the file does not exist yet and Slice 3 may name it | none |
| Part entry placed after `foundation-review`; *Depends on* `task-cycle · project-level` as the plan gives (record form; `project-level/backlog_place.md` reads a locations entry) | — | — |

The part-map entry was written through `the-way-update-part-map` (`elements/part-map/skill/SKILL.md`, `decide_entry.md`, `write.md`,
`template.md`, `examples.md`, `elements/common/rules.md`, `way_of_working.md`, the whole map). Meaning in one sentence: the-way gains
a part `process-audit`, owning `process-audit/**`, that answers for the audit of whether the process gets better, cheaper and faster
across cycles. Files claimed: `process-audit/problem_register.md`; taken from another part: none. Step 2 search of the foundation for
`process-audit`, "register of problems", `problem_register`: WAY-09, WAY-38, WAY-89, WAY-320, WAY-327…WAY-338 — each already names the
part, none needs a change; no invariant names the part; the glossary holds no entry for the words used (see concerns).

## Concerns

1. A cycle may commit its record's copy more than once (a correction after review repeats the pair). Two *Record* commits can then
   name one cycle; Slice 5 should treat the commits whose copy lies under the same `docs/task-cycles/<task-slug>/` of one repository
   as one cycle, or the count of cycles grows.
2. Task *To do* item 3 asks, for an open issue, "the number of days of waiting". The template keeps no date of an issue; Slice 5 can
   take it from the date of the earliest *Record* commit among the issue's problems. If that is not the intended start, *Issues*
   needs an `Opened` column.
3. A fix that lies outside the-way (in a user's own agent setup) has no the-way commit, so such an issue cannot be `fixed` in this
   form. Not asked by the slice; noted for the audit's skill.
4. The word "issue" is used in a meaning WAY-327 defines ("the one matter that like problems of several cycles make"), which a reader
   could take for a tracker ticket; the glossary has no entry. Possibly a WAY-95 entry for the return step; not in this slice's
   *Change*.
5. Plan/handoff mismatch, small: none found; the ranges of the handoff held.

## Reaches beyond the dispatch

- `task-cycle/review/SKILL.md:105-127` (§3 Grade) — to write what Minor, Important and Critical mean in the *Weights* table.
- `foundations/decisions.md` WAY-38 (1025-1050), WAY-89 (1998-2022), WAY-329 (10690-10711), WAY-332…WAY-335, WAY-337 (10866-10885),
  WAY-338 (10886-10907) — found by the foundation search of `update-part-map` step 2 for the part `process-audit`.
- `foundations/glossary.md` headings — to see whether the words of the template have entries.
- Search for `locations.json` in tracked files — to confirm `project-level/backlog_place.md` is where a locations entry is read,
  backing the plan's *Depends on* `project-level`.
- The skill files of `update-part-map` named above — the handoff told me to write through that skill.

## Unread material

none — every passage, entry and file the handoff names was read whole at its current range (task.md 23-108, WAY-09, WAY-40, WAY-41,
WAY-42, WAY-44, WAY-45 in passing, WAY-48, WAY-103, WAY-320, WAY-327, WAY-328, WAY-330, WAY-331, WAY-336, the three invariants,
`task-cycle/record_template.md`).

## Searches not found or unclear

- Which entry name under `the-way` in the locations file names the register: the task (*To do* item 6) and the slice say "an entry",
  none names it. The template says "an entry under `the-way`" without a name; the slice that writes the command and the skill must
  name it.
- How the counting command identifies a product's repository (task *To do* item 3: "repositories the user points to") is not settled
  in what this slice reads; the template ties *Repository* to the locations file's keys as a choice (above).

## Questions

none
