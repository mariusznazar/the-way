# Return step fix — report

**Status:** done

**Commit:** `8e6f4e9` on `task/audit-numbers-mechanism-measures` (from reviewed head `a1b2d471b96479ab9e26d5e3cfdcaad20f90a23b`). One file: `foundations/decisions.md`, WAY-344 only (+8 −7 lines before reflow; the three edited paragraphs wrapped to 100 columns).

## Finding fixed

**I1 — fixed.** I checked the code first, as the ruling asks:
- `process-audit/audit_count.py:938-941` (`section_table`): "the column *Files named* is never one [a missing field]: a section without it is the earlier form of the section"; line 957 sets `named` from the header row; the header may be `STAGE_COLUMNS` with or without `Files named`.
- `audit_count.py:1357-1358` (`fix_rounds_share`): without the column the share of fix rounds is unknown, with the reason "`stages.md` has no column `Files named`: an earlier form", and no `Error:`.
- `process-audit/test_audit_count.py:1342` `test_the_column_files_named_is_never_a_missing_field` (class `StagesForms`): exit 0, no `Error:` in stderr, a cost of 0.003000. I ran it: `python -B -m unittest test_audit_count.StagesForms.test_the_column_files_named_is_never_a_missing_field` from `process-audit/`, exit 0, 1 test OK.

The reviewer is right: the third reading exists in the code and its test, and my commit dropped it when it narrowed the earlier whole-change wording. The clause is now in the three places, and the paragraph stays at three binding sentences:
- binding paragraph, second sentence: the cases now read "a stage report that has no heading of its detailed section and holds a table of tokens by model, for one that has neither of its two time lines, and for one whose detailed section has no column *Files named*";
- *Verification*, *complies*: "one whose detailed section has no column *Files named*" added to the stage reports the count meets;
- *Rationale* price: "or the column *Files named* of that section" added to what a stage report may lose and be read as the earlier form.

Checks (command, exit code):
- `python -B elements/common/foundation_check.py` (the full check): exit 0, `0 errors`.
- `python -B instruction-files/check_instructions.py .`: exit 0, `0 error, 0 warn, 3 info`.
- The test above: exit 0.
- The product's gate was not run.

## What I searched for other earlier-form readings (the ruling's second request)

I listed every place where `process-audit/audit_count.py` gives "an earlier form" or reads an absent part as unknown with no `Error:` (`grep -n "earlier form|older form"`, and every `missing.append` and `missing_in.append`), and compared each with the diff of the range for whether the change reworked that reading (`git diff -U0 2292f33..a1b2d47`):
- reworked by the change, and covered by the entry now: the older table of tokens by model without the section heading (`stage_table`, `older_table`); neither time line (`fill`, `stages_time`); a section without the column *Files named* (`section_table`, `fix_rounds_share`).
- reworked by the change, and no field of a file: a record with no `mechanism_measures.md` or no `gate_times.md` at all (`read_optional`, reason "the copy holds no `<name>`: an earlier form"). WAY-344 speaks of a field in a file the script reads, and a file that is absent is none, so the entry says nothing and needs nothing. The same holds for an absent `cycle.md` or `stages.md`, unchanged since the base.
- not reworked by the change: the readings of `cycle.md`, `process_pin`, `remarks_count` ("an earlier form" for a record with no item *Process remarks on the-way*), `review_rounds` (no item *Review rounds*) and `process_questions`. None of them has a hunk in the range's diff, and WAY-344 binds the whole reading of a file only where a change reworks it. They give unknown with a reason and no `Error:`, and the entry does not need to list them.
- inside the two new files and the older table: a column or label that is missing there is a missing field with an `Error:` (`read_measures`, `read_gate`, `older_table` for `Input`, `Cached input`, `Output`), as the entry says; nothing in them is read as an earlier form.

I found no further reading that the entry omits.

## WAY-344 as it now stands, the sentence of its meaning

English: In a file of a cycle's record read from git history, a missing field gives unknown values, a written result and exit code 1 with an `Error:` line naming file and field, except that a stage report with no heading of its detailed section and a table of tokens by model, one with neither of its two time lines, and one whose detailed section has no column *Files named* are read as the earlier form, with unknown values, no `Error:` line and no change of the exit code.

Polski: Gdy w pliku zapisu cyklu czytanym z historii gita brakuje pola, wartości są nieznane, wynik zapisany, a kod wyjścia 1 z linią `Error:` nazywającą plik i pole; wyjątkiem jest raport etapów bez nagłówka sekcji szczegółowej z tabelą tokenów według modelu, bez obu linii czasu albo z sekcją szczegółową bez kolumny *Files named* — liczenie czyta go jako starszą formę, z wartościami nieznanymi, bez linii `Error:` i bez zmiany kodu wyjścia.

## Choices

- **The clause stays limited to the stage report and lists the three cases**, as the ruling says. Rejected: restore the earlier general wording ("where the file's other signs name that form"), which would cover any further case but is wider than the carve-out needs and was the sentence the first review found not to match the time lines. Cost if wrong: a fourth earlier-form reading, added to the code later, needs a new clause in the entry.
- **No change to the other two places of my first commit** (the part map, the trust boundary): the finding does not touch them.

## Unread material

- `process-audit/audit_count.py`: read again `section_table`, `fix_rounds_share`, the `older_table` and `stage_table` docstrings, `remarks_count`, `review_rounds`, `process_pin` and `process_questions`; the rest not read again (see my first report).
- `process-audit/test_audit_count.py`: read the test at line 1342 and the helper `newer()`; not whole.
- `reports/return-step-review-report.md` (the reviewer's whole report) was not read; the handoff and the findings file were read whole.

## Searches not found or unclear

none
