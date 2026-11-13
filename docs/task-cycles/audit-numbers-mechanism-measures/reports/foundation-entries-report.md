# Foundation entries — report

**Status:** done with concerns (one error of the foundation check stands until slice 1; see Check)

**Commit:** `a030dbf` on `task/audit-numbers-mechanism-measures` (base `2292f334d5499f45b68b00c477cd76a2effd7537`).
Files: `foundations/decisions.md` (+219 −16 lines before reflow; WAY-339 and WAY-344 edited in place, WAY-347 to
WAY-352 added before *Withdrawn identifiers*), `foundations/part_map.md` (+1).

## Entries

| Entry | Mark | English | Polski |
|---|---|---|---|
| WAY-347 (new) | row 1 | The measures of context and cache use are counted by a script of their own into a file of their own in the cycle's record, never as columns of the stage report. | Miary użycia kontekstu i pamięci podręcznej liczy osobny skrypt do osobnego pliku w zapisie cyklu, nigdy nowe kolumny raportu etapów. |
| WAY-348 (new) | row 2 | The weekly count reads those measures and the gate times and shows each cycle's values, each version's median and whether it falls against the previous version of the same series. | Cotygodniowe liczenie czyta te miary i czasy bramki i pokazuje wartości każdego cyklu, medianę każdej wersji i to, czy spada względem poprzedniej wersji tej samej serii. |
| WAY-339 (changed in place) | row 3 | For those measures and the gate times only a change of the script that counts or records them starts a new series; no change of the cycle's instructions does; the series of the cost stays as it was. | Nową serię tych miar i czasów bramki zaczyna tylko zmiana skryptu, który je liczy albo zapisuje; zmiana instrukcji cyklu jej nie zaczyna; seria kosztu zostaje jak była. |
| WAY-349 (new) | row 4 | The orchestrator runs the product's gate at every run through a script that records the time of the run and of each directory of tests the test runner reports into a file of the record. | Orkiestrator uruchamia bramkę produktu przy każdym przebiegu przez skrypt, który zapisuje do pliku w zapisie cyklu czas przebiegu i czas każdego katalogu testów, który wypisze program uruchamiający testy. |
| WAY-350 (new) | row 5 | The script records how many other gate runs by it were going; the audit compares gate times only over runs with none alongside and shows the rest apart. | Skrypt zapisuje, ile innych jego przebiegów bramki biegło obok; audyt porównuje czasy bramki tylko z przebiegów bez innego obok, resztę pokazuje osobno. |
| WAY-344 (changed in place) | row 6 | In a file of a cycle's record read from git history, a missing field makes the count of the audit give unknown values, write its result and end with exit code 1 and an `Error:` line naming file and field. | Gdy w pliku zapisu cyklu czytanym z historii gita brakuje pola, liczenie audytu daje wartości nieznane, zapisuje wynik i kończy kodem 1 z linią `Error:` nazywającą plik i pole. |
| WAY-351 (new) | row 7 | Tokens written again to the cache are what the previous call held and this one did not read, at most what this one wrote, above 2 thousand tokens and with no shrink of the context by 30% or more. | Ponownie zapisane do pamięci tokeny to to, co poprzednie wywołanie miało w pamięci, a to nie odczytało, najwyżej tyle, ile zapisało, powyżej 2 tys. i bez skurczenia kontekstu o 30% lub więcej. |
| WAY-352 (new) | row 8 | A cycle whose stage report has no detailed section is still counted: its cost comes from the table of tokens by model at the same price list, and its share of fix rounds is unknown. | Cykl, którego raport etapów nie ma sekcji szczegółowej, też jest liczony: jego koszt idzie z tabeli tokenów według modelu tym samym cennikiem, a udział rund poprawek jest nieznany. |
| part map: `task-cycle` | the cycle's (from the cycle's answer on the trust boundary; no row) | The trust boundary of `task-cycle` gains `task-cycle/cycle_measures.py`, which reads session records. | Granica zaufania części `task-cycle` obejmuje `task-cycle/cycle_measures.py`, który czyta zapisy sesji. |

Free number: WAY-347 was the first number no entry and no withdrawn identifier held (log ended at WAY-346).

## Check

`python -B elements/common/foundation_check.py --skip-test-citations` — exit 1, one error, the only one:
`foundations/part_map.md:102: the pattern task-cycle/cycle_measures.py in the Trust boundary of task-cycle matches
no file git tracks`. The file does not exist until slice 1 writes it; the error goes when it is tracked. No code
was written here by instruction. The run was made on the final tree, after the edits to the log and the part map
together, and the error above is its whole output; the log's edits gave no error of their own.

The product's gate was not run.

## Choices made (way rejected, cost if wrong)

- **WAY-339 *Scope* gains `task-cycle`.** The decision now binds a change of two scripts that stand in
  `task-cycle/`, so an agent changing them reads it by the part. Rejected: keep `process-audit` alone — an agent of
  `task-cycle` would not find the rule that its script change starts a series. Cost if wrong: one more decision read
  by `task-cycle` work; take the word out of *Scope*.
- **WAY-347 to WAY-352 *Relations*:** WAY-347 derives from WAY-339; WAY-348 from WAY-335 and WAY-339; WAY-349 from
  WAY-160; WAY-350 from WAY-349; WAY-351 from WAY-347; WAY-352 from WAY-337. The closed list has only `derives from`
  and `narrows`; none of these goes against another decision, so none narrows.
- **The counting of concurrent gate runs sits in WAY-350 (row 5), not WAY-349 (row 4).** Task point 4 puts it in the
  script of row 4, but row 5 is the row that makes it mean something and slice 3 serves both. Rejected: put it in
  WAY-349 — row 4's meaning would carry a number only row 5 uses. Cost if wrong: move one sentence.
- **Part-map sentence of `task-cycle` unchanged.** The entry's text names no script (not `cycle_stages.py` either), so
  it does not call for one on the two new scripts; `gate_times.py` is not a trust boundary, as the handoff records.
  *Depends on* unchanged: the audit reads the new files, it imports no code of `task-cycle`, and `task-cycle` gets no
  prices.
- **Row 8 *Rejected* reads `unknown`:** the row's source (point 1 of *To do*) keeps no way not chosen; the way the row
  guards against (dropping the older form) is derived, so by WAY-134 it does not enter.
- **Row 6:** the exception is written as a clause of the second sentence (the log's rule allows three binding
  sentences; the entry already had three, so no fourth was added). The *Rejected* gains the two ways the row's source
  keeps (exit code 2 with no result; the exception for the stage report alone).
- **WAY-350 *Rationale* keeps the task's measurement** (15 to 16 minutes on a free machine, 23 to 40 beside several
  sessions) with its condition, as the template allows, and no date, because the task gives none.

## Searches (WAY-33)

Read whole, as the handoff selected: WAY-337 to WAY-346 (all of them), WAY-330 to WAY-336, WAY-09, WAY-33, WAY-38,
WAY-89, WAY-07, WAY-140, WAY-147, WAY-148, WAY-158, WAY-159, WAY-160, WAY-229, WAY-260, WAY-294, WAY-296, WAY-308,
WAY-309, WAY-316, WAY-320, WAY-325, WAY-326, WAY-328; also WAY-255 and WAY-319 (found by the search for cache and
parallel runs); the whole part map, the whole glossary, the whole invariants file; `elements/decisions/` template,
`elements/common/rules.md`, `way_of_working.md`, the two skills' step files.

- Entries that name WAY-339 or WAY-344: only WAY-294 (narrows WAY-344 for reports without the section; its case is
  unaffected, as it concerns the list of remarks) and WAY-345 (names WAY-339 for the list of classes). Neither needs a
  change. WAY-337's last sentence says the share is unknown where the record and the stages cannot tie each round;
  WAY-352 is consistent with it.
- No invariant derives from WAY-339, WAY-344 or WAY-337. No invariant is written or changed (as the handoff says).
- Glossary: no new word entry — "series", "stage report" and "instrument" are used in the plain sense of the
  existing decisions; the entries use no term of the process the glossary lacks.
- No environment-fact entry holds the lifetime of the prompt cache or the form of session records; WAY-255 cites the
  documentation of the cache directly. The new scripts depend on the form of the session records of Claude Code and
  Codex (a fact an invariant or decision could rest on); no row asks for it, so none was written (see Questions).

## Unread material

none (the handoff's selection was read whole; the task document whole; the plan itself and the slices were not read,
as the handoff allowed, because no entry's wording needed them).

## Searches not found or unclear

- WAY-33 search for an entry that already states a row: none found for rows 1, 2, 4, 5, 7, 8; the rows are new
  decisions.
- The row 7 threshold "2 tys." is written `2 thousand tokens`; the task does not say whether it means 2,000 or 2,048,
  and the source script that the task names lies outside the repository and was not read (handoff: do not read the
  author's notes).
- WAY-140 says only a human makes "a task's effect outside the product's repository"; the registry of gate runs that
  row 5's count relies on lies in `~/.the-way/` and is an effect of the script's run, not of the task. WAY-320 keeps
  the places that files of the-way name in `~/.the-way/locations.json`, and the registry is a place outside every
  repository that the script names by a fixed path, no entry of that file. Neither decision names such a registry.
  Not stated in any entry (the file name is code).
- The external-context row "a user's places outside every repository … both | untrusted" is worded generally ("such
  as" the register and the results); it was not changed for the registry.

## Questions for the orchestrator

1. Is a registry of gate runs under `~/.the-way/gate_runs/` acceptable under WAY-320 as a fixed place with no entry in
   the locations file? Recommended: yes — it holds only empty files the script itself writes and no path of the user's
   disk; WAY-320 concerns places that files of the-way name for a *reader of the user's choice*; if the human
   disagrees, the slice should read the place from an entry, and no foundation entry changes (none names the registry).
2. Should the format of the session records (Claude Code, Codex) become an environment fact that WAY-347's measures
   rest on? Recommended: not in this task — no row asks, and the fact would need a cited source; leave for the return
   step if slice 1 finds the form fixed enough to cite.
3. The check stays red (one error) between this commit and slice 1; recommended: accept, since slice 1 adds the file.
   If a gate at the end of this stage is wanted green, move the trust-boundary line to slice 1's commit instead.
