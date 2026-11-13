# Return step — report

**Status:** done

**Commit:** `a1b2d47` on `task/audit-numbers-mechanism-measures` (head before: `1e2c028`; base `2292f334d5499f45b68b00c477cd76a2effd7537`).
Files changed: `foundations/decisions.md` (WAY-344 only: +26 −21), `foundations/part_map.md` (+2 −1). No code file was changed.

## Checks

| Command | Exit | Result |
|---|---|---|
| `python -B elements/common/foundation_check.py` (the full check, after the edit of the log, and again after the edit of the part map) | 0 | `0 errors` |
| `python -B -m unittest discover -s elements/part-map -p "test_cross_part_imports.py"` | 0 | 39 tests OK |
| `python -B instruction-files/check_instructions.py .` | 0 | 0 error, 0 warn, 3 info |

The product's gate was not run. No script was changed, so no focused test of a script was run.

## Foundation compared with code

Read whole: `task-cycle/cycle_measures.py`, `task-cycle/gate_times.py`; of `process-audit/audit_count.py` the readers of both forms of `stages.md` (lines 915-1026), `add_cost`, `fix_rounds_share`, `read_measures`, `read_gate`, `fill` (1280-1672) and the series and median code (2277-2462); the diff of `process-audit/SKILL.md`, `price_list.md`, `problem_register.md`, `task-cycle/record_template.md`, `task-cycle/skill/SKILL.md`, `blocked_finding.md` and `reserved_return.md`.

| Entry | Compared with | Result |
|---|---|---|
| WAY-347 (measures of context and cache use: own script, own file, no column of the stage report) | `cycle_measures.py` writes `mechanism_measures.md`; `cycle_stages.py` is untouched since the base | matches |
| WAY-348 (count reads the measures and gate times, shows medians per version and whether each falls) | `read_measures`, `read_gate`, `mechanism_rows`, `gate_rows`, `falls_answer` | matches |
| WAY-349 (the gate runs through a script; times of the run and of each directory, in any order, into a file of the record) | `gate_times.py` (`Times.line` reads `== ` blocks and `Ran n tests in s`, in whatever order; the output passes through; the file holds times only); `task-cycle/skill/SKILL.md` steps 2, 4 and 10 name the script for every run | matches |
| WAY-350 (count of other runs from a registry in the user's directory; median only over runs with none alongside) | `gate_times.py` `prepare`, `count_others` (empty file per run, renamed on its end, running counts six hours, ended one is kept a day); `gate_values` and `gate_rows` (a version with every run in company gets no median and no comparison, its runs listed apart) | matches |
| WAY-351 (tokens written again) | `cycle_measures.rewrites`: `min(max(0, held − read), written)`, only above 2000, not where the context falls to 70% or less of the previous call's. I worked both examples of the entry by hand against it: 20,000 counted; the second, with context 36,000 against 55,000, counted none | matches |
| WAY-352 (cost from the table of tokens by model; share unknown) | `stage_table`, `older_table`, `priced_older`, `add_cost` (`OLDER_NO_TURNS`) | matches |
| WAY-339 (as changed) | `instrument_series` splits only on a change of `task-cycle/cycle_measures.py` or `task-cycle/gate_times.py`; `TREE_PATHS` is not in the range's diff; `task-cycle/cycle_stages.py`, `change`, `plan`, `review` and `spec` are untouched | matches |
| WAY-344 (as changed) | see below | **did not match; corrected** |
| WAY-337 | the cost formula `cost_at` and the share rules are as the entry says; for the older form the share is unknown with a reason, the number of rounds stays | matches |
| WAY-160 | `gate_times.py` does not change who runs the gate and keeps no output of it; the entry's *Rejected* names the file of full output | matches |
| WAY-331 | the scripts of points 2 and 4 stand in `task-cycle/`, their reading in `process-audit/` | matches |
| WAY-341 | the count's exit 1 with a result written fits the night run | matches |
| WAY-38, WAY-328 | the two new scripts import the standard library alone; `gate_times.py` starts only the command the product declares | matches |
| WAY-140 | see Choices 4 | no change |
| Part map `process-audit` | sentence, files, *Depends on* (`task-cycle`, `project-level`), trust boundary `audit_count.py` | matches; no import of `task-cycle` code was added (`test_cross_part_imports.py` passes) |
| Part map `gate` | `gate/` is untouched; `gate_times.py` reads the two line forms that `gate/run_tests.py` writes (line 94 `== %s`, and the `Ran` line of `unittest`) | no change (Choices 5) |
| Part map `task-cycle` | trust boundary | **changed** (below) |

### N1 settled: WAY-344 worded to what the code does

The code (`audit_count.py` `stage_table` and `fill`, lines 923-934 and 1657-1671) reads a stage report as the earlier form by two marks and no other sign: with no heading of the detailed section and one table of tokens by model, or with neither of the two time lines. A report with one time line and not the other lacks the other (tests `test_a_time_line_without_the_other_is_a_missing_field`, `test_neither_time_line_is_the_earlier_form_and_no_missing_field`). The entry said "the file's other signs name that form", which the code does not do for the time lines. I did not treat it as a code change: the code is as the task wants it (the task says a file of the older form is read by its own marks; neither time line is such a mark).

Corrections in `foundations/decisions.md` (WAY-344), all in place:
- the clause now names the two cases (the stage report with no heading of its detailed section and a table of tokens by model; the stage report with neither of its two time lines) and says that is the whole of what the count reads as an earlier form; the clause is limited to the count of the audit and no longer states a rule for every script, which is what the carve-out needs and no more;
- *Verification*: *complies* names those two cases; *violates* gains "a stage report that holds one of its two time lines and not the other is read as the earlier form, with no line `Error:`", and its other sentence says "stage report" instead of "file";
- *Rationale* price: names the effect of the rule as it is, that a stage report that lost its two time lines, or its detailed section while a table of tokens by model remains, is read as the earlier form and gives unknown where the rule alone would give an error. This is the corner the review found (N1), now stated instead of hidden.
- The binding paragraph had four sentences after the whole-change fix (the template's "Binding sentences" allows one to three; `foundation_check.py` does not count them, so it passed). The earlier-form clause is now part of the second sentence, as the log's first carve-out is, and the paragraph has three.

The remaining Minor findings N2 and N3 of the review, and M10, are no mismatch with an entry; I did not touch them.

## Decisions written or changed

Only WAY-344 changed in this step, in place, as above. No decision was written.

| Entry | Mark | English | Polski |
|---|---|---|---|
| WAY-344 (the earlier-form clause only) | the cycle's (the clause stands beside row 6; the human did not see it as worded; the whole-change fix wrote it and this step corrects it to the code) | In a file of a cycle's record read from git history, a field that an earlier form never had is no missing field where the count reads the file as that form: a stage report with no heading of its detailed section and a table of tokens by model, or with neither of its two time lines; its values are unknown, with no `Error:` line and no change of the exit code. | W pliku zapisu cyklu czytanym z historii gita pole, którego starsza forma nigdy nie miała, nie jest brakującym polem, gdy liczenie czyta plik jako tę formę: raport etapów bez nagłówka sekcji szczegółowej, z tabelą tokenów według modelu, albo bez obu linii czasu; jego wartości są nieznane, bez linii `Error:` i bez zmiany kodu wyjścia. |

The entries the foundation step wrote stand as written; marks, as it gave them:

| Entry | Mark | English | Polski |
|---|---|---|---|
| WAY-347 | row 1 | The measures of context and cache use are counted by a script of their own into a file of their own in the cycle's record, never as columns of the stage report. | Miary użycia kontekstu i pamięci podręcznej liczy osobny skrypt do osobnego pliku w zapisie cyklu, nigdy nowe kolumny raportu etapów. |
| WAY-348 | row 2 | The weekly count reads those measures and the gate times and shows each cycle's values, each version's median and whether it falls against the previous version of the same series. | Cotygodniowe liczenie czyta te miary i czasy bramki i pokazuje wartości każdego cyklu, medianę każdej wersji i to, czy spada względem poprzedniej wersji tej samej serii. |
| WAY-339 (changed) | row 3 | For those measures and the gate times only a change of the script that counts or records them starts a new series; the series of the cost stays as it was. | Nową serię tych miar i czasów bramki zaczyna tylko zmiana skryptu, który je liczy albo zapisuje; seria kosztu zostaje jak była. |
| WAY-349 | row 4 | The orchestrator runs the product's gate at every run through a script that records the time of the run and of each directory of tests into a file of the record. | Orkiestrator uruchamia bramkę produktu przy każdym przebiegu przez skrypt, który zapisuje do pliku w zapisie cyklu czas przebiegu i czas każdego katalogu testów. |
| WAY-350 | row 5 | The script records how many other gate runs by it were going; the audit compares gate times only over runs with none alongside and shows the rest apart. | Skrypt zapisuje, ile innych jego przebiegów bramki biegło obok; audyt porównuje czasy bramki tylko z przebiegów bez innego obok, resztę pokazuje osobno. |
| WAY-344 (changed, the exception for the count) | row 6 | A missing field in a file of a cycle's record read from git history gives unknown values, a written result and exit code 1 with an `Error:` line naming file and field. | Brakujące pole w pliku zapisu cyklu czytanym z historii gita daje wartości nieznane, zapisany wynik i kod 1 z linią `Error:` nazywającą plik i pole. |
| WAY-351 | row 7 | Tokens written again to the cache are what the previous call held and this one did not read, at most what this one wrote, above 2 thousand and with no shrink of the context by 30% or more. | Ponownie zapisane do pamięci tokeny to to, co poprzednie wywołanie miało w pamięci, a to nie odczytało, najwyżej tyle, ile zapisało, powyżej 2 tys. i bez skurczenia kontekstu o 30% lub więcej. |
| WAY-352 | row 8 | A cycle whose stage report has no detailed section is still counted: its cost comes from the table of tokens by model, and its share of fix rounds is unknown. | Cykl, którego raport etapów nie ma sekcji szczegółowej, też jest liczony: jego koszt idzie z tabeli tokenów według modelu, a udział rund poprawek jest nieznany. |

## Invariants

None written or changed. No task row, decision or human instruction sets one. The invariants that reach the new scripts (`script-language`, `script-imports`, `script-subprocesses`, `cross-part-imports`) hold: both new scripts are Python, import the standard library only, and start only the command the product declares; `test_cross_part_imports.py` passes.

## Environment facts

None written. Decided for each source named in the handoff, by `the-way-record-environment-fact` and the template's "Which facts are written":

- **Session records of Claude Code** (usage fields, `message.id`, the `subagents` folder, `agent-<id>.meta.json`) **and of Codex** (`session_meta`, `token_usage_record`, `parent_thread_id`): code detail, no fact. The template asks for a fact where a decision's *Based on* or an invariant's *Rests on* cites a source whose change would call it into question. WAY-347, WAY-351 and the others have `Based on: none` and cite no form of those records; they decide how the measures are counted, not what a record looks like. A change of the record form breaks the script, which ends with `Error:` naming the missing field and fails its tests (`cycle_measures.py` `member`, `whole`); it does not call a decision into question. The part map already holds the exchange (external context row "session records", untrusted). A source also has to be an edition, a page without editions or a reading of a host (template, "Source"), and "a text quoting the source" is no source: a transcript form read from the repository's own tests would be that. I found no public page that states those fields, and a reading would need a private transcript; so no entry could be written from a source I can read here.
- **The registry of running gates under `~/.the-way/gate_runs/`**: not a source outside the product. It is the product's own state, set by WAY-350 (a decision of the product, which says where it lies and how long an entry counts); the file names are code.
- **Cache behaviour** (a collapse of the conversation writes the cache anew): WAY-351 gives it as the reason in its *Rationale*, not as a citation its rule rests on; its *Based on* is `none`. WAY-255 already cites the documentation of the cache lifetime. No new entry.

## Glossary terms

None written. The words the handoff names, by the template's "List the word's uses" and WAY-95:
- "series": 22 uses in the decision log, 14 in `process-audit/SKILL.md`; used in the plain sense (a run of comparable versions) since WAY-339 before this change; the change uses it the same way. No narrower meaning that a reader who knows the field would read wrongly.
- "instrument": two uses, both in WAY-349's *Rationale*, in the plain sense of a measuring tool; it is in no binding sentence.
- "measure": the plain sense (a number the audit counts); used so before this change.
- "rewrite": WAY-351 uses it in *Verification* and *Rationale* for "tokens written again", while the binding sentence says "written again", and elsewhere in the log it is the verb for editing a text. A reader meets "rewrite of 1,500 tokens" next to the sentence that defines it, so no sentence reads wrongly; I wrote no entry and left the wording.

## Part-map changes

| Change | Mark | English | Polski |
|---|---|---|---|
| `task-cycle`: *Trust boundary* gains `task-cycle/gate_times.py` (beside `cycle_stages.py` and `cycle_measures.py`) | the cycle's | The trust boundary of `task-cycle` also holds the script that runs the gate, because it lists, creates and deletes files in a directory on the user's disk and reads the output of the gate. | Granica zaufania części `task-cycle` obejmuje też skrypt uruchamiający bramkę, bo wypisuje, tworzy i usuwa pliki w katalogu na dysku użytkownika i czyta wyjście bramki. |
| External context, row "a user's places outside every repository": gains "and the registry of running gates that the script of the gate keeps" | the cycle's | The registry of running gates is one of the user's places outside every repository, an exchange in both directions, untrusted. | Rejestr działających bramek to jedno z miejsc użytkownika poza repozytoriami, wymiana w obu kierunkach, niezaufana. |

The foundation step's addition of `task-cycle/cycle_measures.py` stands. The sentences, *Files* and *Depends on* of `task-cycle`, `process-audit` and `gate` are unchanged and match the code.

## Projected entries

None: the task has no source project definition (`Project relation: independent`).

## Rows of *Settlements to record* written

All eight rows are written, by the foundation step, none by this step: row 1 WAY-347; row 2 WAY-348; row 3 WAY-339; row 4 WAY-349; row 5 WAY-350; row 6 WAY-344; row 7 WAY-351; row 8 WAY-352. This step found no row missed and no row whose settlement the code does not make true.

## Search of the whole foundation (WAY-33)

Searched `foundations/*.md` for the names of the change: `cycle_stages`, `cycle_measures`, `gate_times`, `gate_runs`, `mechanism_measures`, `stages.md`, `audit_count`, `price_list`, `record_template`, `process-audit/`, "new series", "series of", "gate" with run, "cache", "starting state". Read whole: WAY-09 (lists what `process-audit/` and `task-cycle/` hold; the two scripts fit "what the design of the task cycle sets"), WAY-140, WAY-160, WAY-255 (cache lifetime, cites the docs; no clash with WAY-351), WAY-320, WAY-331, WAY-337, WAY-338, WAY-341, WAY-344, WAY-345 and WAY-346 (WAY-345 says a change to the list of levels "would break a series of measures"; WAY-339 now says that of the cost, and WAY-339's own sentence says "of measures, except …", so they agree), the invariants `return-step-record`, `script-*`, `gate-exit-code`, `cross-part-imports`, the whole part map. Decisions 4797, 4855-4866 (the blocked routes that "run the gate") are served by the step-10 text, which `blocked_finding.md` and `reserved_return.md` point to. No other entry needed a change.

## Choices (each with the way rejected and its cost if wrong)

1. **WAY-344 worded to the code, not the code to WAY-344.** Rejected: ask for a code change that makes the time lines look at the heading too (the review's other way); it is a change of a script's behaviour, which is not this step's, and the task wants earlier forms read by their own marks. Cost if wrong: the human may prefer the stricter reading; then a code change makes a stage report of the newer form with no time line an error, and the clause loses its second case.
2. **The earlier-form clause limited to the count of the audit and the stage report.** Rejected: the general sentence about "an earlier form of a file", which bound every script. Cost if wrong: another script that reads an earlier form of a file has no carve-out written; it gets one with its own change.
3. **Paragraph kept at three sentences** by folding the clause into the second. Rejected: leave four, as `foundation_check.py` does not count. Cost if wrong: a long sentence that a reader must parse; a later rewrite splits it.
4. **WAY-140 not changed.** `task-cycle/skill/SKILL.md` now says the cycle writes outside the repository only to the registry of running gates, a directory of empty files. WAY-140 concerns a task's effect (a server, DNS, keys, an external account) that a reset cannot undo; the registry is the script's own bookkeeping, as the record of the request, which WAY-140 already says is no effect of the task, and holds nothing of the task. Rejected: add the registry to WAY-140's exceptions, which would change the meaning of an approved decision. Cost if wrong: if the human reads the registry as such an effect, WAY-140 needs the clause and SKILL.md's sentence stands as the cycle's own statement of it.
5. **`gate` part and the `test-runner-command` surface not changed** to promise the lines `== <directory>` and `Ran … in …s`. The reading is tolerant: where the lines change, `gate_times.py` writes `—` for the directories and the total stays. Rejected: add the lines to the surface, which is a promise to products pinned to a commit that nobody asked for; the reader is a script of the same repository. Cost if wrong: a change to `gate/run_tests.py` output silently empties the directory times until someone sees a run with `—`.
6. **`gate_times.py` added to the trust boundary** (the foundation step recorded the orchestrator's choice that it is not one, "to be checked against the code the slices will write"). The code lists, creates and deletes files in a directory on the user's disk, which the template's "Trust boundary" gives as such an input ("files that come from outside the product, such as one on the user's disk"), and relays the output of the product's gate into a record. Rejected: keep it out; the audit re-reads the file as untrusted anyway. Cost if wrong: later changes to the script get a review aimed at crafted input that was not needed, one extra line to take out of the part map and a row of the external context to reword.
7. **The rule that a Codex agent's cache writes are unknown, never zero, is not written as an entry.** It stands in the task's *To do* point 2, in the script, its docstring and its tests. The task's table says 10 candidates were shown and 8 accepted, and I cannot see which two were not; adding a clause to WAY-347 might write what the human declined. Rejected: add it to WAY-347's *Verification*. Cost if wrong: a later change could count Codex as zero with no entry to hold it against; only the tests would catch it.
8. **No environment fact for the session records or the cache**, as above. Rejected: write facts from the transcript forms in the repository's tests, which the template does not accept as a source. Cost if wrong: if the human wants a decision to rest on the form of the records, the fact is a task of its own with a reading of a real transcript.

## Unread material

- `process-audit/audit_count.py`: read about 1,400 of its 2,942 lines (the readers of both forms of `stages.md`, the cost, `read_measures`, `read_gate`, `fill`, and the series and median code); not read: the register reader, `analyse`, the rendering (`render`, `measures_lines`, `gate_lines`, lines 2562-2942) and `main`. The whole-change review read them.
- The tests (`test_audit_count.py`, `test_cycle_measures.py`, `test_gate_times.py`): read by name (`grep`) for the cases of WAY-344; not read whole.
- The diff of `process-audit/SKILL.md` was read, not the file whole.
- `reports/whole-change-fix-review-report.md` and `reports/foundation-entries-report.md` read whole; the other reports of the cycle and `plan.md` were not.
- The decisions and the invariants listed in the search above were read whole; the rest of the log was not read.

## Searches not found or unclear

- A public page or a stable document that states the form of Claude Code's session records or of Codex's rollouts: not found (not searched on the web; the repository's own tests carry the forms). Settled as no fact (above).
- Which two of the ten candidates the human declined: the task shows only "Candidates: 10 shown, 8 accepted" and the eight rows. Unclear; it bears on Choice 7.
- Whether the task's "2 tys." means 2,000 or 2,048: the code and WAY-351 use 2,000 and the example "2,000 or fewer counts none"; the source script lies outside the repository and was not read (as in the foundation step's report). Unclear.
- N2 and N3 of the review (a table's trailing rows after a note line, which the code says it does not read; lines over 100 columns) and M10 (the double reason in *Unknown values*): not mismatches with an entry; not touched, for the request's list.
