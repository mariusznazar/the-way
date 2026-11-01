# Author report — decision-heading-level

**Status:** done

**Commits:** 168b055 (on `task/decision-heading-level`, base 2f51e6c)

**Files changed**
- `elements/common/way_of_working.md` (+2/-1): after "to the next heading" added "(`###` in the decision log, `##` in the other foundation files)"; line re-wrapped.
- `task-cycle/change/SKILL.md` (+3/-2): after "each whole" added ", an entry running to the next heading (`###` in the decision log, `##` in the other foundation files)"; line re-wrapped.

**Checks**
- `python -B elements/common/foundation_check.py .` exit 0 ("0 errors").
- `python -B gate/run_tests.py task-cycle` exit 0 (42 tests OK).
- Not run: the full gate (orchestrator's); `skill_entry_points.py` (description unchanged).

**Own-work check.** Requirement most likely missed: the insertions must sit after the exact words the task names and read as given. Check: read both edited passages against the task text; the wording is identical and placed after the named phrases. The comma after "each whole" was kept as the task's insertion starts with one. Tests for prose: none (prose for people).

**Reaches beyond the dispatch:** none. Read WAY-35, WAY-150, WAY-256 whole.

**Searches not found or unclear:** none. The task's line numbers (73, 32) matched.

**Choices:** the insertion in way_of_working.md goes before the comma following "next heading", keeping the sentence grammatical; the alternative (after the comma) would cut "with its rationale" off. No cost if wrong.

**Problems:** none.
