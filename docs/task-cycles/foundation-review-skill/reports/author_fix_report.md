# Fix report — foundation-review-skill (the fix of a review's findings)

**Status:** done

**Commit:** `34a206f` docs: the review tag's message gives the number of items checked, in WAY-301 and in the skill alike (range from `02ca017`)

## The finding

**Important 1** (the skill said the tag message counts "entries and remarks" and adds "of a person";
WAY-301 said "entries") — **fixed**. I hold the finding right.

How: the task's *Context* says "Opis tagu podaje tylko liczbę sprawdzonych pozycji" — one number, of
items checked. I chose that, the smaller reading, for both texts, which now read the same: "the
number of items checked and no title of a task or of a private note".

- `foundations/decisions.md` WAY-301: binding sentence ("number of entries checked" became "number of
  items checked"); *Verification* "violates" (now "the message gives more than the number of items
  checked, such as the titles of the tasks the review made"); *Rationale* ("holds counts" became
  "holds the number of items checked").
- `foundation-review/SKILL.md` step 7: "The message gives the number of items checked and no title of
  a task or of a private note: the repository may be public." (removed the second count and "of a
  person" / "of a note").
- `foundation-review/weak_points.md` (a third restatement the search found): "takes no line beyond the
  number of items checked that the tag message gives."

Search for other restatements: `grep -rn -i "entries checked\|entries and remarks\|message gives\|message
holds\|message names\|tag's message\|tag message\|number of entries\|holds counts\|counts only\|of a
person"` over `*.md` and `*.py` outside `.runs`, `.claude`, `.agents`. The hits were those three files;
after the fix the same search for "entries checked", "entries and remarks" and "count the tag" finds
nothing. The skill's entry points copy only the description, so they did not change. My earlier report
(`author_report.md`) still says "entries and remarks" in a table row and in the commit-message-level
notes; it is a report, not a file of the change, and I left it.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`
- `python -B agent-instructions/skill_entry_points.py` — exit 0, `entry points are current`
- `python -B gate/run_tests.py agent-instructions` — exit 0, 18 tests OK
- `python -B gate/run_tests.py elements/common` — exit 0, 109 tests OK
- Not run: the whole gate (the orchestrator's); `foundation-review/` holds no test.

## Own-work check

Requirement most likely unmet by the fix: WAY-301 (binding sentence, *Verification*, *Rationale*) and
every text that restates the message agree. Check: the search above, run after the fix, finds no
remaining "entries checked" / "entries and remarks"; the three passages read side by side say "the
number of items checked" and "no title of a task or of a private note" (the skill and weak_points say
it in their own words, without adding a count or a kind of title). Showed: they agree. Not checked:
that a human running the skill puts such a message; the skill has not been run on a repository.

## Searches not found or unclear

none
