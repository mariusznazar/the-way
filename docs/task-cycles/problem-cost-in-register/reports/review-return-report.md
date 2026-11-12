PASS ba2f0dc8b56b474ef3dd62297b9a6c5db7d722df

# Review of the return step's commit — problem-cost-in-register

Range `e6d05e2..ba2f0dc`; `git rev-parse HEAD` is `ba2f0dc8b56b474ef3dd62297b9a6c5db7d722df`, as given. One commit, one file
(`process-audit/audit_count.py`, 4 lines added, 4 removed), only in the
string the result prints above *Problems by cycle* (line 2090 onward). No logic, no test, no foundation entry changed.

Blocking findings: 0. Minor: 1. Out of scope: 0.

## Findings

### Critical

none

### Important

none

### Minor

**M1. The rewrapped paragraph leaves one line 120 characters long, where the file had none above 103.**
`process-audit/audit_count.py:2094`: `"records of more than one cycle: it counts in none of them. Problems whose cycle no named repository holds, or "`.
Adding "cost of an occurrence," to line 2091 pushed the words down; the commit rewrapped lines 2091 to 2093 but left the
following line 2094 as it was, so it now carries the end of the sentence from the line above plus its old tail. At
`e6d05e2` the longest line of the file was 103 characters (13 lines over 100); this is the only line at 120. No test or
gate check fails on it (`process-audit` tests pass), and the printed text is unchanged by wrapping, so the effect is
polish only; the file's own convention, which the foundation step's earlier fix also followed (commit `e6d05e2`
"the wrap of WAY-330"), is a rewrap of the rest of the paragraph. Evidence: `awk 'length($0)>=120'` on the file prints
only line 2094; the same count on `e6d05e2` has no line at or above 110.

## Does the commit do what the return step says, and only that

Yes. The report says one commit, one file, 4 lines each way, text only. `git diff e6d05e2..ba2f0dc --stat` shows exactly that.
The words of the paragraph differ only by the inserted "cost of an occurrence," (the rest is a changed wrap); I compared
the old and the new sentences by eye and found no other word moved.

## Is the corrected text true of the code

Yes. `read_register` (`audit_count.py:1519-1530`) refuses a row of *Problems* when `cost not in COST_LEVELS` ("the cost of
an occurrence is not one of the five levels") and appends it to `register.refused_problems`, which the analysis turns into
the *Refused rows* column of *Problems by cycle* and `at least n` in that cycle's counts (lines 1683-1707). So "refused for a
class, weight, cost of an occurrence or issue the register lacks" is true of a cost that is no level. "The register lacks" is
loose for a cost (the levels are fixed in the code, the register holds only their table), but it is exactly as loose for the
weight in the same sentence and was so before the commit; I do not grade it.

The sentence still names only four of the reasons a row is refused: the code also refuses a row of a wrong width, one that
names no repository and one whose *Record* is no 40-character commit hash (lines 1512, 1519-1523). That was so before the
commit and the task did not ask to list them; set aside under Declined to judge.

## The report's comparison of the entries with the code

I read WAY-330, WAY-345 and WAY-346 whole, the glossary entry `cost of an occurrence` and the part-map entry `process-audit`,
and compared them with the code, `process-audit/SKILL.md` and `problem_register.md` by search. WAY-333, WAY-336, WAY-337,
WAY-339 and WAY-344 I read in the task's quotations only (see Unread material).

- WAY-345: the code has the five levels in `COST_LEVELS`; a row with another cost is refused (line 1521); a table of levels
  that does not name the five once is refused with an `Error:` (line 1493-1496). The entry's *Verification* is true. Report: matches. Agreed.
- WAY-346: *Cost of an occurrence by issue* is built at lines 1717-1721 and printed at line 2154 with the levels and *Refused
  rows*; *Problems by cycle* has no cost column (line 2099). SKILL.md steps 2 and 3 quote the row beside each issue (line 148-151).
  Report: matches. Agreed.
- WAY-330: the register holds the cost; the command reads it from the row and gives none (SKILL.md:24, problem_register.md:12
  agree). Report: matches. Agreed. The decision's heading was widened by the foundation step ("class, weight and cost of an
  occurrence"); the code's docstring and the result text now use the same triple.
- Glossary `cost of an occurrence` and its *Not* (WAY-337, money of a cycle): the uses I found in `audit_count.py`, SKILL.md
  and `problem_register.md` mean the level. Agreed.
- Part-map entry `process-audit`: files `process-audit/**`, trust boundary `audit_count.py`; the change touches only that
  part. Its text (template, price list, command, skill) is still true. Agreed.
- Mismatch search of my own: `git grep -n -i "four tables|class and weight or|class or a weight"` finds nothing outside `.runs`;
  `git grep "a class, weight"` finds only `process-audit/audit_count.py:2091` (the corrected line). SKILL.md lines 138 and 164
  speak of a row refused "for its class", which is true of that case only and is not a list of reasons. I found no further
  mismatch.

The comment on lines 133-137 of the docstring (the register's description) lists "an unknown class, weight or cost of an
occurrence, an issue in no row of *Issues*" and says the five tables are named: already correct, and the same list the
corrected result text now gives.

## Declined to judge

- The text above *Problems by cycle* does not list the other reasons a row is refused (wrong cell count, no repository, a
  *Record* that is no commit hash): present before the commit, not part of the task or the return step.
- Minor 4 of the review of the whole change (WAY-344's "row label" against the exit 1 of a level table that does not name its
  levels): carried by the cycle for the request's list, outside the task, not reopened.
- No test asserts the text above *Problems by cycle*; a test of printed prose is not asked by the task, and the report says
  so itself.

## Checks

| Check | Command | Exit |
|---|---|---|
| Foundation check | `python -B elements/common/foundation_check.py` | 0 (`0 errors`) |
| Tests of the part | `python -B gate/run_tests.py process-audit` (background, 435 s; "Ran 129 tests ... OK") | 0 |
| Diff of the range | `git show ba2f0dc`, `git diff e6d05e2..ba2f0dc --stat` | 0 |
| Search for the old wording | `git grep -n -i "four tables\|class and weight or\|class or a weight\|a class, weight" -- ':!.runs'` | only the corrected line |
| Line length | `awk` over the file at head and at `e6d05e2` | one line at 120 at head, none above 103 at base |

Not run: the whole gate (the cycle's own run).

## Reaches beyond the dispatch

- `foundations/decisions.md` WAY-330 (line 10947) and WAY-345 (line 11389), read whole; WAY-346 (line 11425) read in its
  *Verification* and *Rationale* part, which the output of my read showed; to compare the entries the dispatch lists.
- `foundations/glossary.md:181` and `foundations/part_map.md:114` (the entry `process-audit`), read whole.
- `process-audit/SKILL.md` and `process-audit/problem_register.md`, by search for the words of the text and the old wording.
- `process-audit/audit_count.py` lines 125-142 and 1476-1535, 2080-2100: the reading of the register and the printed text.
- `reports/review-fix-report.md`: only a search for the words Minor and wrap, to see what stays open.

## Unread material

- WAY-333, WAY-336, WAY-337, WAY-339, WAY-344 and WAY-328: not read whole; I know them from their quotation in the task's
  *Decisions in play*, which the change cannot touch since the commit only changes printed prose. I found no word in them that
  the new text would contradict.
- WAY-346: the first lines of its body (statement and relations) were cut from my output; I read its *Verification* and
  *Rationale* and the heading.
- `reports/review-whole-report.md`, `reports/review-fix-report.md`: not read beyond the search above.
- `task-cycle/skill/return_step.md`, `foundation_step.md`: not read; the dispatch did not ask for them.
- The method file `task-cycle/review/SKILL.md`: read whole; `whole_change.md` and `fix.md` not read (variants not mine).

## Searches not found or unclear

- The dispatch names the foundation to select "by the parts of the range (`process-audit`)"; it does not give a list of
  guidelines for the part. WAY-328 says the-way departs from the general coding guidelines for its own code in this part, so I
  checked no guideline file. Not unclear, but I did not search `product-guidelines/` for a line-length rule; the one search I ran
  (`git grep` for "line length", "120 char") found none for code, so M1 rests on the file's own practice, not on a rule.
- No test asserts the corrected text; a search of `process-audit/test_audit_count.py` for "lacks" found only unrelated tests.
