# Report — the agent of the plan's *Foundation entries*

**Status:** done with concerns (the concerns are in "Concerns and questions for the orchestrator").

## Commits (branch `task/code-order-formatter-linter-size`, base `d69fb20b`)

- `9c093516` — Write the foundation entries of the code-order task: the formatter, the thresholds on
  formatted code, two new invariants and four rewordings
- `00945f93` — Keep the Verification of WAY-382 to its invariant and WAY-385 to its present pair of
  examples (drops a pair of examples I had added in the first commit, so that no entry carries a part
  its row does not give)

Files changed in the two commits together, by `git diff --stat d69fb20b..HEAD`: `foundations/decisions.md`,
`foundations/invariants.md`, `agent-instructions/test_size_invariant.py` (one line). No other code, no test
beside that line, no change of `ruff.toml`, no reformatting.

## The entries

Where each stands: decisions in `foundations/decisions.md` (WAY-382, WAY-385, WAY-379, WAY-145, WAY-350,
WAY-339 and, as a consequence, WAY-09); invariants in `foundations/invariants.md`.

| Entry | Mark | Meaning in English | Znaczenie po polsku |
|---|---|---|---|
| F1 — WAY-382, in place | row 1, 4, 5 | The-way's code has Ruff's formatter in the version WAY-381 pins, at width 100 with every other setting at its default, covering `.py` files only, and a comment `fmt: off`, `fmt: on` or `fmt: skip` in a covered file is forbidden. | Kod the way ma formater ruffa w wersji, którą przypina WAY-381, z szerokością linii 100 i resztą ustawień domyślnych, obejmujący tylko pliki `.py`; komentarz `fmt: off`, `fmt: on` albo `fmt: skip` w pliku objętym regułą jest zakazany. |
| F2 — WAY-385, in place | row 2 | A function of a script has at most 110 lines and a file of a script at most 1200, counted on the code as the formatter leaves it. | Funkcja skryptu ma najwyżej 110 linii, a plik skryptu najwyżej 1200, liczone na kodzie w układzie formatera. |
| F3 — `own-foundation-check-report`, new | row 3 | `elements/common/foundation_check.py`, run with no switch on the-way's repository as a commit leaves it, reports no error. | `elements/common/foundation_check.py` uruchomiony bez przełączników na repozytorium the way w stanie danego commita nie zgłasza żadnego błędu. |
| F4 — `formatter-layout`, new | row 1, 4, 5 | Every `.py` file git tracks in the parts of WAY-379 stands as the pinned Ruff's formatter leaves it with `ruff.toml`, with no part of it left out by a `fmt:` comment. | Każdy plik `.py` w częściach z WAY-379, który śledzi git, stoi tak, jak zostawia go formater przypiętego ruffa z `ruff.toml`, i żaden jego fragment nie jest wyłączony komentarzem `fmt:`. |
| F5 — WAY-379, corrected | row 1 | The example of a compliant state no longer says the formatter's rule reads `none —`; it says the rule names the decision adopting the formatter and its invariant, and takes the dependency audit as the example of `none —`. | Przykład zgodnego stanu nie mówi już, że reguła formatera czyta `none —`; mówi, że reguła nazywa decyzję przyjmującą formater i jego niezmiennik, a przykładem `none —` jest audyt zależności. |
| F6 — WAY-145, reworded | the cycle's | "entry" in the plan's log of changes becomes "line" in the sentence and in the *Verification*; meaning unchanged. | W dzienniku zmian planu „entry” zastępuje „line” w zdaniu i w *Verification*; znaczenie bez zmian. |
| F7 — WAY-350, reworded | the cycle's | "an entry whose times cannot be" of the registry of running gates becomes "a file whose times cannot be"; meaning unchanged. | W rejestrze uruchomień bramki „an entry whose times cannot be” staje się „a file whose times cannot be”; znaczenie bez zmian. |
| F8 — `gate-times-refuses-impossible-entry`, reworded | the cycle's | The sentence speaks of a file of the registry ("deletes a file of its registry …, and counts that file as no other run"); the identifier stays. | Zdanie mówi o pliku rejestru („deletes a file of its registry …, and counts that file as no other run”); identyfikator zostaje. |
| F9 — WAY-339 and `audit-series-script-paths`, corrected | the cycle's | Where they name the script that measures the cost as `task-cycle/cycle_stages.py`, they name it with the module `task-cycle/stage_transcripts.py` that it imports, so a change of either starts a series of the cost; meaning unchanged. | Tam, gdzie nazywają skrypt liczący koszt `task-cycle/cycle_stages.py`, nazywają go razem z modułem `task-cycle/stage_transcripts.py`, który ten skrypt importuje, więc zmiana któregokolwiek zaczyna serię kosztu; znaczenie bez zmian. |

Why F6, F7 and F8 are marked `the cycle's` and not `row`: no row of the task's *Settlements to record* carries
them (rows 1-5 are the formatter, the thresholds, the check of the foundation, `.py` only, `fmt:`); To do 8
of the accepted task asks for them and their meaning does not change, so `foundation_step.md` gives
`the cycle's` for an entry no row carries whole. Your handoff names F9 as the one entry beyond the rows; I
did not find that F6-F8 follow from a row with no way left open, so I marked them as that file gives. If you
judge To do 8 enough, the three marks regroup with no change of text.

Why F5 is `row 1`: it is the corrected example of the decision whose neighbour row 1 changes; no way is left
open for it (the formatter's rule can no longer read `none —`).

### Choices I made, with the way rejected

- **Identifiers.** F4 `formatter-layout` (it names what the sentence constrains: the layout the formatter
  leaves); F3 `own-foundation-check-report` (the report of the check on the-way's own repository). Rejected:
  `formatter-invariant`, `foundation-check-passes` (they name a demand or the entry itself, which
  `elements/invariants/template.md` rules out).
- **F3 derives from WAY-09 only** ("The entries in `foundations/` are checked by
  `elements/common/foundation_check.py`"). WAY-09's *Verification* gained `own-foundation-check-report` after
  `invariants:` (the decision skill's step 4.4: a decision names the invariants derived from it). Rejected:
  WAY-16 as a second source (it makes the check run in the gate but does not say what the check reports) and
  WAY-321 (about the switch). Cost if wrong: one more `derives from`, no behaviour changes.
- **F3 and F4 `Rests on: none`.** `ruff-required-version` is the reason of WAY-381, so it stays in that
  decision's *Based on*; no environment fact holds a condition that decides F4. F3 reads the repository, no
  outside fact. Cost if wrong: an environment fact missing from a link, found by the review.
- **F4 is one sentence.** The `fmt:` ban is worded as the same rule ("with no part of it left out of the
  formatter by a comment"), since a `fmt:` comment makes `ruff format --check` skip a region; the task's
  To do 2 also takes it as one invariant. Cost if wrong: the review may split it (a new identifier, WAY-12).
- **F4 *Part*** = the parts of WAY-379's *Scope* and `repository`, as `ruff-blocking-rules` and the
  template's paragraph on the *Part* of a standing check give. **WAY-382 *Scope*** gained `repository` for the
  same reason WAY-380's has it (`ruff.toml` is the formatter's configuration and stands there). Cost if wrong:
  the decision reaches one more part's agents.
- **No pair of examples** in WAY-382's *Verification* (it reads `invariants: formatter-layout.`). The old pair
  spoke of a state without a formatter, so it went; a new pair would have been a part the rows do not give and
  would have made F1 `the cycle's`. The width 100 and the defaults stay with the review, which compares a change
  with the binding sentence as for any decision. I wrote one pair in the first commit and dropped it in the
  second. **No pair of examples was added anywhere**; the only pair touched is WAY-379's, a correction (F5).
- **WAY-385's rationale lost its sentences about the mark** (the invariant "is marked violated until … and
  until then only review keeps a cleaned or a new file from growing over it"), since the plan's Coverage gives
  "F2 (WAY-385's sentence on the mark)" to this entry. The marks of `ruff-blocking-rules` and
  `function-and-file-size` stand as they were (`Violated: yes`), as you told me. A sentence of WAY-385's
  *Rationale* says no more about a known violation.
- **WAY-385 has no `derives from WAY-382`.** The sentence names WAY-382 in the text only; `derives from` is "a
  higher decision this one serves" (the template), and the thresholds do not serve the formatter. Cost if
  wrong: one more link.
- **WAY-385's *Rejected*** takes the ways the row's source keeps (80/1000 kept; files only with the test of
  functions staying an expected failure; 100/1500), each with its reason, beside the earlier ways, whose "in
  the same run" now reads "in the run before the formatter" (the counts of the earlier run stand as a
  measurement of the code before the formatter). *Rationale* names the two runs as the product's own
  measurement with their conditions, as the decisions' template gives. Numbers 11 and 2 for 110/1200 come from
  the task's *Questions to settle* (result at `bec6c3d2` formatted at width 100).
- **WAY-382's rationale and *Rejected*** carry the widths 88/100/120 with their line and function/file counts
  (the product's own measurement, said so) and the ways the rows' sources keep (no formatter, 88, 120, the
  formatter over Markdown examples, no ban on `fmt:` comments). The earlier reason for waiting is not kept: an
  entry holds the present state (WAY-07). No file name stands in the *Rationale* or *Rejected*, as the
  template asks; so `.git-blame-ignore-revs` and the count of Markdown files are not there.
- **Word for "entry" in F6 and F7/F8:** "line" for the plan's log of changes (the plan template,
  `project-level/plan/template.md:148`, and another decision of the log already say "a line in the change
  log"); "file" for the registry of running gates, which holds "an empty
  file for each run". Slice 10 should use the same words: "line" in `project-level/lead/skill/SKILL.md`
  ("their change-log lines"), "file" in `task-cycle/gate_times.py` and `task-cycle/test_gate_times.py`.
- **F9 wording** in WAY-339: "the script that measures the cost, `task-cycle/cycle_stages.py` with the module
  `task-cycle/stage_transcripts.py` that it imports" — the later "the script that measures the cost" of that
  decision now means the pair. In the invariant, the same phrase after the dash. The opening of the first
  sentence stays word for word: "A new series of the cost of cycles, the two numbers of WAY-337".

### Pairs of examples added word for word

none (see the choice above).

## The lines brought along

- `agent-instructions/test_size_invariant.py:58`: `# decision: WAY-385 "A function of a script of the-way has
  at most 110 lines, counted with the functions nested in it"` (before: "… at most 80 lines, …"). The test that
  holds it, named for the request (WAY-03):
  `agent-instructions/test_size_invariant.py`, class `Counting`,
  `test_a_function_counts_the_functions_nested_in_it_and_a_method_is_a_function`. The thresholds
  `FUNCTION_LIMIT` and `FILE_LIMIT` and the module description are for Slice 19 and I did not touch them.
- The lines `decision: WAY-339 "…"` of `process-audit/test_audit_count.py` and `task-cycle/test_cycle_stages.py`
  stand as they were. The opening words of the first sentence of WAY-339 stay ("A new series of the cost of
  cycles, the two numbers of WAY-337"), and the other quoted sentences are untouched (checked by the foundation
  check: no error). The sentence the first quotation opens now reads differently in its latter part, so the
  request names the tests that quote it (the ones at `process-audit/test_audit_count.py:3351, 3407, 3427,
  3446, 3471, 3569, 3617, 4342`; none in `task-cycle/test_cycle_stages.py` quotes that sentence — its five lines
  quote "The one exception is that this report holds").
- Invariant tests whose sentence is reworded and that the foundation check lists (WAY-03), for the request to
  name once their slices change the files: `audit-series-script-paths` — `process-audit/test_audit_series_scripts.py`
  (Slice 17); `gate-times-refuses-impossible-entry` — `task-cycle/test_gate_times.py` (Slice 10).

## Own-work check (`make-change`, section 3)

Requirement most likely not met: every `decision:` quotation of a test still begins a binding sentence of its
decision, since I changed the first sentences of WAY-385 and WAY-339 and WAY-12 makes a quotation that stands
in no sentence an error.

- `python -B elements/common/foundation_check.py --skip-test-citations` → `0 errors`, exit 0 (final state, after
  both commits). It lists two reworded invariants whose tests do not change yet:
  `audit-series-script-paths` and `gate-times-refuses-impossible-entry` — expected; Slices 17 and 10 change those
  tests (WAY-03, to be named in the request).
- Negative control (so that the check is seen to catch the break): with the old quotation "… has at most 80
  lines, …" put back for a moment in `agent-instructions/test_size_invariant.py:58`, the same command reports
  `agent-instructions/test_size_invariant.py:58: the quotation stands in no binding sentence of WAY-385`,
  `1 error`, exit 1; the file was then restored to my edit (the foundation check ends with `0 errors`, exit 0,
  as above).
- `python -B agent-instructions/test_size_invariant.py` → `Ran 4 tests … OK (expected failures=1)`, exit 0: the
  counting tests pass and the invariant's test is still an expected failure, as the plan leaves it until Slice 19.
- Not run, with the reason: `python -B gate/run_tests.py` (the full suite is the cycle's run) and the tests of
  `elements/common` (no test cites F3 and F4 until Slices 4 and 3; WAY-321).

## Concerns and questions for the orchestrator

1. **The invariant `audit-series-script-paths` says "a script whose history `process-audit/audit_count.py`
   reads"**; Slice 16 moves `COST_SCRIPTS` and the other lists into `process-audit/version_analysis.py`. The
   command is still `audit_count.py` and imports the module, so the sentence stays true, but the plan has no
   entry that rewords it; recommend leaving as is, and to see it at Slice 17's review.
2. **`process-audit/SKILL.md:54`** names the script that measures the cost as `task-cycle/cycle_stages.py`
   ("at a change of `task-cycle/cycle_stages.py`, the script that measures the …"). F9 (decision and
   invariant) does not reach it; a skill file belongs to a slice (17 is the nearest, which changes
   `process-audit` files), or is left whole as one more name of the same script. Recommend adding it to Slice
   17's *Change* with the foundation check as proof.
3. **WAY-382's *Based on* stays `none`.** The decision rests on behaviours of Ruff's formatter (Markdown
   examples formatted by default, `fmt:` comments respected, the widths' effect). No environment fact holds
   them, and writing one was outside my handoff. If you want them, it is one fact for the formatter's
   documentation, written by `elements/environment-facts/skill/SKILL.md`.
4. **WAY-09's *Verification*** gained `own-foundation-check-report` (a consequence of F3 deriving from it; the
   handoff did not name WAY-09). It is one word in a list; the request should name WAY-09 among the changed
   entries.

## Unread material

- WAY-48, WAY-95 and WAY-233: not read whole (named in the handoff; no entry of mine touches a trust boundary,
  a glossary term or an expected value of a test: I read WAY-95's sentence in the task and the index). WAY-03:
  only its sentence in the index and the title, whole text not read.
- WAY-33, WAY-61, WAY-69, WAY-321, WAY-12, WAY-07, WAY-08, WAY-16, WAY-51, WAY-205, WAY-365, WAY-379-382, WAY-385,
  WAY-145, WAY-339 and WAY-350: read whole.
- `product-guidelines/coding/template.md`: read lines 1-70, 125-175 and 315-350 (the required form, the rule
  *Formatter* and its paragraph on *Part*, the section "The tools of the standing checks" whole), not the rest.
- `process-audit/test_audit_series_scripts.py`, `process-audit/test_audit_count.py`, `task-cycle/test_cycle_stages.py`:
  searched for lines `decision:`/`invariant:` and `COST_SCRIPTS`; the first file's header and its citation line
  only, the others not read.
- `elements/glossary/skill/SKILL.md` and `elements/part-map/skill/SKILL.md`: not read; I wrote no term and
  touched no part of the map.
- The plan: read *Foundation entries*, Slices 1, 2, 3, 4, 10, 13, 15, 16, 17 and 19 and all of *Choices*;
  the other slices not read.
- The vault rule files `knowledge_artifacts.md`, `git.md`, `scripts.md`: read.

## Searches not found or unclear

- No `decision:` line quotes WAY-382, WAY-145 or WAY-350 in any `.py` file (found none).
- No other entry of the foundation names the old state "no formatter" besides WAY-382 and WAY-379's *Verification*;
  `guidelines/coding.md` still reads `none — WAY-382` in `### Formatter` (Slice 3 changes it; the foundation
  check does not report it).
- Unclear: whether the part map should name `.git-blame-ignore-revs` now; it is To do 1 and Slice 3, so I left it.

## Reaches beyond this handoff

- WAY-09 (read whole; *Verification* edited) — to derive F3 and name it as the decision skill's step 4.4 gives.
- WAY-360 and `elements/common/foundation_check.py` (head of the docstring) — to see what the check reports for
  a reworded invariant, and which decisions bind the size rule.
- `process-audit/SKILL.md:54`, `project-level/plan/template.md` (the phrase "line in the change log"),
  `task-cycle/gate_times.py` (its description) — to choose the words of F6-F8 and F9 and to find the gap in
  concern 2.

## Working copies

None made. I made no directory under `.runs/foundation-entries/`; a one-off copy of
`agent-instructions/test_size_invariant.py` for the negative control stood at
`.runs/foundation-entries-backup.py` and was removed (`ls .runs` shows only `orchestrator/` and
`task-cycles/`).
