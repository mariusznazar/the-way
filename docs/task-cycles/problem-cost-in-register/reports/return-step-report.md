# Return step — problem-cost-in-register

**Status:** done. **Head reached:** the commit listed below, on `task/problem-cost-in-register` (the range to review is `e6d05e2..HEAD`).

## Commits

- One commit, by path: "Name the cost of an occurrence among the reasons a row is refused in the text of Problems by cycle" (`git log -1` on the branch). File: `process-audit/audit_count.py`, 4 lines added and 4 removed, in the paragraph the result prints above the table *Problems by cycle*; no logic changed.

## Foundation compared with the code (WAY-11)

Method: read `task-cycle/skill/return_step.md`, `task-cycle/skill/foundation_step.md`; compared each entry below with the code, template and skill at `e6d05e2`; searched tracked files (`git grep -i`, excluding `.runs`) for `four tables`, `class and weight`, `class or a weight`, `class, weight`, `four levels`, `table of the register is`.

| Entry | Compared with | Result |
|---|---|---|
| WAY-345 (scale, five levels, highest reached, user adapts only meanings) | `COST_LEVELS` and `check_cost_level` in `process-audit/audit_count.py`; the table `## Costs of an occurrence` of the template; tests of refused costs and of the table of levels | matches. Its *Verification* says the count refuses a table of levels that does not name each of the five once, and a row whose cost is none of the five: both true. It says nothing on exit codes, so it does not disagree with Minor 4 |
| WAY-346 (cost shown by issue, none by cycle) | section `## Cost of an occurrence by issue`; *Problems by cycle* has no cost column; the skill's steps 2 and 3 quote the row beside each issue | matches |
| WAY-330 (register holds the cost; audit gives none itself) | template, command (reads cost from the row, assigns none), skill | matches |
| Glossary `cost of an occurrence` and its *Not* (`WAY-337`) | the word's uses in `process-audit/` (the template, the skill, the docstring, the result text) | matches; every use of "cost of an occurrence" means the level, and "cost of a cycle" / section *Cost* means the money of WAY-337 |
| WAY-333 (weight scale of four levels, class list) | unchanged `LEVELS`, `check_weight`, table *Weights* | still true; the remaining "four levels" in the code are the weight scale |
| WAY-336 (frequency is material, no priority) | skill rule on the cost, order of the new section (register order) | matches |
| WAY-337 (cost of a cycle, two numbers) | section *Cost* untouched | matches |
| WAY-339 (series) | no change to the price list, stage report, classes or reviewer instructions | matches; it names no series start for a changed meaning of a cost level, and the task asks for none |
| WAY-344 (missing field) | register reading: heading, table and column missing give exit 2; level tables (a level is a "row label") give exit 1 as *Weights* did | the entries I wrote say nothing about exit codes, so no entry disagrees with the code; the difference between WAY-344's "row label" and the task's wording stays the reviewer's Minor 4, outside the task's scope, for the request's list. No code and no foundation entry changed for it |
| WAY-328 (*Scope* of every part) | no part added | matches |
| Part map entry `process-audit` | files `process-audit/**`, trust boundary `audit_count.py`; its text (template of the register, price list, counting command, skill) | still true; no change |

What did not match, and was corrected: the paragraph the command prints above *Problems by cycle* listed "a class, weight or issue the register lacks" as the reasons a row is refused. A cost that is no level refuses a row too (and the row counts in that cycle as a refused row). Corrected in the code's text to "a class, weight, cost of an occurrence or issue". Evidence: `git grep -n "refused for a class"` found only that line. The tests do not assert that text (`git grep` shows no test of it).

## Decisions written or changed

None in this step. (The foundation step's WAY-345, WAY-346 and the edit of WAY-330 stand.)

## Invariants

None written. The task, the decisions and the human set no rule for the return step to make into an invariant. No invariant of `process-audit` or `every` is affected: no import or subprocess added, and `tracked_private_paths_check.py` listed 0 at the last run.

## Environment facts, glossary terms, part-map changes, projected entries

None. No source outside the product was used. The only term the change uses in a meaning of its own is `cost of an occurrence`, written in the foundation step. The task has no projected entry.

## Rows of *Settlements to record*

Rows 1, 2 and 3 were written in the foundation step (row 1 WAY-345, row 2 WAY-346, row 3 the glossary term). The other three candidates were not accepted (the task: 3 accepted of 6 shown). No row missed.

## Choices that bind after the merge (WAY-36)

None new: the choices of the change (the header word, the column order, the separate section, the exit code of a missing field) are in `author-report.md` as choices of how to make what the task settles, and bind through WAY-345, WAY-346 and WAY-330 where they bind.

## Checks (command and exit code)

| Check | Command | Exit |
|---|---|---|
| Foundation check | `python -B elements/common/foundation_check.py` | 0 (0 errors) |
| Tests of the directory changed | `python -B gate/run_tests.py process-audit` (background, 354 s) | 0 (129 tests OK) |

Not run: the whole gate (the orchestrator runs it once).

## Unread material

- `reports/review-whole-report.md` and `reports/review-fix-report.md`: not read; the handoff and the coordinator's message give their outcome (both passed) and the Minor 4 content.
- `foundations/part_map.md`: only the entry `process-audit` and its neighbours, as in the first report.
- `task-cycle/record_template.md`: the *Return step* section was not read whole; this report follows the handoff's list of sections.
- Everything else the handoff names I read whole: `return_step.md`, `foundation_step.md`, the task, the entries WAY-345, WAY-346, WAY-330, WAY-333, WAY-336, WAY-337, WAY-339, WAY-344, WAY-328 (all read in the earlier stages of this session).

## Searches not found or unclear

- No test asserts the text above *Problems by cycle*, so the correction has no test of its own (it is prose the command prints; the full `process-audit` run still passes).
- The `record_template.md` section names for this report were taken from the handoff's list; I did not check them against the template.
