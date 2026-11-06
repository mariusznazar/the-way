# Remarks 2 — the human's remarks on the corrected request

Request: https://github.com/mariusznazar/the-way/pull/77 (draft, head `5a84a30`; reviewed tree `ef083d1`, final tree `990950b`).
Given by Mariusz in the orchestrator's session on 2026-11-06, in answer to the orchestrator's
summary of correction 1, which recommended making item 4 of *For you to decide* a separate small
task before the loop2 task. Not posted on the request; quoted here word for word.

> "nie lubię dodatkowych drobnych zadań
> drobne rzeczy powinny być robione przy okazji, żeby potem nie zostawały na dodatkowe zadania i dodatkowe sesje
> dociągnij e drobne luki w teście i przy okazji można też te M3 i M4 dorzucić"

## What the remarks ask, as the orchestrator reads them

1. **Close the small gaps of the test** (item 4 of *For you to decide* of the corrected request, and the
   review of correction 1, `reports/14-review-correction-1-report.md`):
   - **-c code** (review 14, M1): "code given with `-c` is not read, so a run or import inside it passes
     unseen … the code string is a constant the check could parse with `ast` as it parses files."
   - **Python's import functions and `exec`** (the author's named limits, `reports/13-correction-1-report.md`,
     "Limits"): `importlib.import_module`, `__import__`, and `exec` (also `eval`/`compile` where they run
     code) are not read.
   - **Two claimed branches without a fixture with teeth** (review 14, M2): "treating a run into a
     temporary directory like any other path (`:420`, `elif target != TEMPORARY` → `elif True`), and
     allowing a path outside the root (`:373`, `relative()` returning `../…`) … leaves the docstring's
     "a path outside the repository's root … is no dependency" (:18) with no test."
2. **M3** (review 04): "a Python file the map lists under "Files left out on purpose" fails the test,
   though WAY-44 and `foundation_check` allow it. … the copy of the pattern extraction (the author's
   concern 1) already diverges".
3. **M4** (review 04): "`elements/part-map/template.md:97` is 122 characters, where the surrounding
   paragraph wraps at 100 … `foundations/decisions.md:1083` — the re-wrap of WAY-44 leaves the short
   line "another. For a file that" before the old line continues."
