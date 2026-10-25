# Slice 5 report

**Status:** done
**Commit:** 3bd9e37 (mariusznn@gmail.com)

Files: installation/install.py (+1), installation/README.md (+2/-2), installation/test_testing_guidelines_installation.py (new, copy of the coding one), installation/test_coding_guidelines_installation.py and installation/test_styleguide_installation.py (count 38 -> 40).

## Checks
- Failing first (SKILLS unchanged, new test and counts of 40 written): `python -B gate/run_tests.py installation` exit 1. The coding and styleguide tests failed on `38 != 40`; the new file's preview/apply test and its crafted-entry subtests failed (the crafted cases exit 0 with no refusal, as no wrapper path was owned yet).
- After the SKILLS entry: `python -B gate/run_tests.py installation` exit 0 (44 tests, 235 s).
- `python -B elements/common/foundation_check.py` exit 0.
- `git diff --check 4302f72 -- installation/` exit 0, empty.

## Own-work check
Weakest point: the refusal at the new entry-point path (foreign file, directory, non-UTF-8 file, in .claude and .agents, preview and --apply). The new test passes: non-zero exit, tree byte for byte as before, nothing staged. The README list of checks was updated; its line-ending style was preserved.

## C9
The non-UTF-8 case still stops on an uncaught UnicodeDecodeError; the new test copies the coding test's assertion (exit and untouched tree only). The installer's decoding is not changed.

## Reach beyond Read
None beyond task-cycle/change/SKILL.md, the coding installation test, install.py SKILLS and the README lines.

## Choices
Test file made by sed from the coding one (names, paths, strings renamed). README: both the table row (line 57) and the list of checks (line 172) name the skill.

## Concerns
None.
