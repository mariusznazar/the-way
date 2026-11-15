# Report: the fix of the whole-change review's findings, task `decision-log-reading-index`

- **Status:** done with concerns (one concern, below; nothing blocks)
- **Variant:** the fix of a review's findings (`task-cycle/change/SKILL.md`, `task-cycle/change/fix.md`)
- **Range:** `55f1a24..e82cbab` on `task/decision-log-reading-index`

## Commits and files

| Commit | Findings | Files (added / removed lines) |
|---|---|---|
| `d6599c7` | I1 | `foundations/decisions.md` +12 −10 (WAY-150 only); `elements/common/way_of_working.md` +5 −5 |
| `e82cbab` | m1–m5 | `task-cycle/cycle_measures.py` +33 −18; `task-cycle/test_cycle_measures.py` +72 −3; `elements/common/decision_index.py` +17 −5; `elements/common/test_decision_index.py` +14 −0; `task-cycle/skill/SKILL.md` +3 −1; `project-level/lead/answering.md` +2 −1; `project-level/lead/skill/SKILL.md` +3 −3 |

## Each finding

### I1 — fixed, variant (a)

- **Choice:** the reviewer's variant (a). WAY-150's second sentence now opens "Of the decisions it finds by
  *Scope*, by a line `decision:` or as the task or the work's source names them, whoever selects reads the index
  and opens whole only …", and its reading-whole clause reads "each other entry it selects — an invariant, an
  entry of the map of a touched part, or an entry, a decision included, that these or the decisions of the index
  link to as far as the work needs — it reads whole". So the index and "opens whole only" govern the decisions
  found by *Scope* (or, in a sectioned log, by section, as the third paragraph gives), by a test's `decision:`
  line and by name; a decision reached by a link of a selected entry is read whole, as far as the work needs.
- **Why (a):** it is the smaller change, it brings WAY-150 back into line with step 3 of "Reading the
  foundation" and with the complying example ("reads whole the invariants naming `gate` or `every` and the
  entries they link to") without touching either, and it keeps the plan's sentence for slice 3 true.
  **Way rejected:** (b), adding linked decisions to the index through `--decision` and rewriting step 3 and the
  example — a larger change of the rule file and of WAY-150's pair; its cost if (a) is wrong is that agents
  read whole a few more decisions than the index alone would give (for this task, WAY-21, WAY-33, WAY-148
  linked from WAY-150).
- **Rows kept:** row 1 (the index of the selection; opening whole only the named kinds; the reviewer reads the
  index of its whole selection and counts what it read whole), row 2 (paragraph 2 unchanged), row 3 (paragraph
  3 unchanged), row 5 (`decision:` decisions still selected and opened whole), row 6 (paragraph 3 unchanged).
- **`elements/common/way_of_working.md`, step 2**, kept in step: "Read the index. Of its decisions, open whole
  only those …" and "The log beyond the index, the entries opened and the decisions step 3 reaches by a link is
  not read." Step 3 stands as it was.
- **Verification examples:** neither pair of WAY-150 stops holding the sentence (WAY-12): the complying example
  already reads the linked entries whole; no violating example concerns linked decisions. No example changed.
  No test holds a sentence of WAY-150 (search `decision: WAY-150`: no match).
- **Check:** `python -B elements/common/foundation_check.py` → `0 errors`, exit 0.

### m1 — fixed

`json_lines` now parses each line through `line_object` and keeps the number of the line being read or parsed;
a `MemoryError`, while reading a line from the file or while parsing it, ends the reading with
`Error: <file>:<line>: the line is too large to read into memory`, exit 2. Within the same trust boundary,
two more places that parse transcript-side JSON now catch `MemoryError` too: the subagent's meta file
(`read_subagent_name`, exit 2 naming the file, as for its other errors) and the arguments of a Codex function
call (searched as their text alone, uncounted as parsed values, as for arguments that are no JSON). The
docstring's exit-code paragraph says both.

Tests (running out of memory is not reproduced; `json.loads` is replaced to raise `MemoryError` for a text that
begins with a marker, and for the read case `Path.open` of the transcript gives one line then raises):
`test_a_line_too_large_to_parse_in_memory_ends_with_exit_2_naming_the_file_and_line`,
`test_a_line_too_large_to_read_into_memory_ends_with_exit_2_naming_the_file_and_line`,
`test_a_meta_file_too_large_to_parse_in_memory_ends_with_exit_2_naming_it`,
`test_arguments_too_large_to_parse_in_memory_are_searched_as_their_text`.

- Failing first, on the script as at `55f1a24` (the tests in place):
  `python -B -m unittest -q task-cycle/test_cycle_measures.py -k too_large` → `FAILED (errors=4)`, exit 1, each
  a `MemoryError` raised out of `main` (the finding's traceback).
- Passing, on the new script: same command → `OK`, exit 0.
- Mutation: with `reading = number + 1` removed, `python -B -m unittest -q task-cycle/test_cycle_measures.py -k
  too_large_to_read` → `FAILED (failures=1)`, exit 1 (the error named line 1, not 2); restored.

### m2 — fixed

`None` dropped from the tuple of `test_an_output_that_is_no_text_is_not_counted`, with its `continue`; both
remaining values assert. The missing output stays tested in
`test_a_missing_field_of_a_call_or_an_output_ends_with_exit_2_naming_it`.

### m3 — fixed

Step 12 of `task-cycle/skill/SKILL.md` now says that `cycle_measures.py` counts the context and the prompt cache
of the cycle's agents "and, for each agent, the bytes of the decision log and of the index of decisions that
entered its context and how many times each entered it, which show what the reading of the foundation costs
(WAY-339)". WAY-339 checked as the entry holding that paragraph (heading `### WAY-339` above it).

### m4 — fixed as the finding gives, not as an error

`decision_index.py` writes, after the line of counts, `Parts that no Scope names: <part>, <part>.` where a part
given by `--part` is named by no decision's *Scope*; no line where every part is named; exit 0 either way. The
docstring says it, and that such a part is no error.

The handoff reads "follow the finding; the error is exit 2 with the message form of WAY-344"; the finding says
"An error would be wrong (a new part may have no decision yet), but a line in the index or on stderr naming
each given part that no *Scope* names would show the typo." The two disagree; I followed the finding, since an
exit 2 would leave an agent whose work touches a new part with no index at all, and WAY-344 concerns a missing
field of a file, which a part absent from every *Scope* is not. The line stands in the index, not on stderr,
because the index is what the reading rule has the agent read. Cost if wrong: an orchestrator wanting a hard
stop on a typo would need the exit 2 added in a later change.

Test `test_a_part_that_no_scope_names_is_named_in_the_index` (`core`, the misspelled `core-engin` beside the
named `core-engine`, and `sound`, named by no decision): failing first, `python -B -m unittest -q
elements/common/test_decision_index.py -k no_scope` → `FAILED (failures=1)`, exit 1 (the line absent); passing
after the code with the whole file → `Ran 16 tests … OK`, exit 0.

### m5 — fixed

`project-level/lead/answering.md` line 9 rewrapped; `project-level/lead/skill/SKILL.md` lines 35–38 rewrapped so
no short line stays; `task-cycle/cycle_measures.py` docstring line 83 rewrapped. Words unchanged. A check of the
added lines of both commits found none over 100 characters. Other lines of `cycle_measures.py` measure 101–104
by `awk` (bytes, likely the `—` and similar); not named by the finding, not touched.

## Checks

| Command | Exit |
|---|---|
| `python -B elements/common/foundation_check.py` (after I1, and again after all fixes) | 0, `0 errors` |
| `python -B gate/run_tests.py elements/common` | 0, 232 tests OK |
| `python -B gate/run_tests.py task-cycle` | 0, 478 tests OK |
| `python -B gate/run_tests.py project-level` | 0, 275 tests OK |
| failing runs of the tests written first | as given under m1 and m4 |

Not run: `python -B gate/run_tests.py process-audit` (no file of `process-audit/` touched, as the handoff
gives); the product's full gate (the orchestrator's).

## Own-work check

- Requirement most likely not met: that the index's new line shows a misspelled part on the real log, also with
  `--section`, where the finding says the loss is silent. Check:
  `python -B elements/common/decision_index.py --part task-cycle --part no-such-part --output .runs/fix-whole/idx.md`
  → exit 0, "Listed in full: 96 … Parts that no Scope names: no-such-part."; the same with `--section <first
  section of the log> --part no-such-part` → exit 0, "Listed in full: 9 … Parts that no Scope names:
  no-such-part." Met.
- For I1: read WAY-150's new second sentence against steps 2 and 3 of "Reading the foundation" and WAY-150's
  complying example: the index and "opens whole only" cover the same decisions in both files, and the linked
  entries are read whole in both.

## Concerns

1. WAY-150's clause "the reviewer of the whole change reads the index of its whole selection" and its violating
   example "the reviewer of the whole change leaves decisions of its selection out of the index it reads" still
   say "selection", which the first sentence makes include linked entries. Read strictly, a reviewer that reads a
   linked decision whole without adding it to its index matches the violating example. I left both as row 1
   gives them ("czyta spis całego wyboru"), since a decision read whole is known better than from the index,
   and changing the reviewer's clause or the example goes beyond what the new wording needs. A reviewer of
   this fix may want "decisions it finds by *Scope*, by a line `decision:` or by name" written into the
   example.

## Entries changed

- **WAY-150** — row 1; the clause on linked decisions is the cycle's.
  - EN: Whoever selects reads the index of the decisions it finds by *Scope*, by a test's `decision:` line or by
    name and opens whole only those the work changes, contradicts, answers otherwise, names, tests or finds
    open, while the invariants, the part map's entries and every entry these or the indexed decisions link to,
    a decision included, it reads whole as far as the work needs.
  - PL: Wybierający czyta spis decyzji znalezionych po *Scope*, po linii `decision:` testu albo po nazwie i w
    całości otwiera tylko te, które praca zmienia, którym przeczy, na które odpowiada inaczej, które nazywa,
    których zdania pilnuje zmieniany test albo które zostawiają otwarte, co praca ma zrobić; niezmienniki,
    wpisy mapy części i każdy wpis, do którego one albo decyzje ze spisu linkują, decyzję też, czyta w całości,
    o ile praca tego potrzebuje.

## Reaches beyond the handoff

- `elements/decisions/skill/read.md`, `elements/decisions/skill/decide_entry.md`, `elements/decisions/template.md`
  sections "Binding sentences" to "Verification": read as `elements/decisions/skill/SKILL.md` names them, for
  the change of WAY-150.
- `foundations/decisions.md` WAY-150's *Rationale* and *Rejected* (read as part of the entry), WAY-19, WAY-22
  (in the same read range), WAY-148 and WAY-167's passages that cite WAY-150 (search `WAY-150` in
  `foundations/`), WAY-339's paragraph on the measures (for m3), WAY-297 (in the WAY-263 read range).
- `.runs/task-cycles/decision-log-reading-index/task.md` *Settlements to record* (named by the handoff);
  `reports/foundation-entries-report.md` "Fix 1" and `reports/executor-3-report.md` "Concerns" — to see what
  `dbdfdad` meant to change and why.
- `elements/common/way_of_working.md` read whole (the handoff named the section; I change the file).

## Working copies

`.runs/fix-whole/` held a copy of the new `cycle_measures.py` (used to restore it after running the tests on the
old one and after the mutation), two index files of the own-work check and the outputs of the test runs. The
directory was removed before return; nothing kept in `reports/`. The tests' own temporary directories are the
product's tests' and outside this rule.

## Unread material

- `task-cycle/test_cycle_measures.py`: read whole in two pages.
- `reports/review-whole-report.md`: only the passages the findings cite were searched (lines around I1 by the
  findings' quotations); not read whole, as the handoff gives.
- Otherwise none.

## Searches not found or unclear

- The handoff's m4 line, "follow the finding; the error is exit 2 with the message form of WAY-344", disagrees
  with the finding, which holds an error wrong for a part no decision names yet; I followed the finding (see m4).
- WAY-150's "its whole selection" for the reviewer is unclear after variant (a) as to decisions reached by a link
  (Concerns 1).
