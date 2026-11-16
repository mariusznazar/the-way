# Author report — the return step after correction 2

**Status:** done

**Range:** `5a39a328346ad9a8d12e37732f52a86a164e3d17..9547acd4` — one commit, `9547acd4` ("Bring the audit skill, the record template and two docstrings in line with how Q1 is read"). Files (added / removed): `process-audit/SKILL.md` 11/6, `task-cycle/record_template.md` 1/1, `process-audit/audit_count.py` 3/1, `process-audit/record_items.py` 3/3. No code changed: the syntax trees of `process-audit/record_items.py` and `process-audit/audit_count.py` with docstrings left out equal those at `5a39a328`.

## What I compared, against the final code (`process-audit/record_items.py`)

- **WAY-337, new paragraph** (the item *Review rounds* takes an entry `review ..., PASS`; no fix round for the cost; read as a round with no contradiction): matches `REVIEW_ENTRY`, `round_of` (a review entry gives mark `no`) and `review_rounds` (gives no file for it). No change.
- **WAY-344 narrowing** (a record that lacks the line `Process pin` or `Target branch and base` or the item `Process remarks on the-way`, `Discarded attempt`, `Review rounds`, `Plan` or `Slices returned too large` is of an earlier form: unknown with a reason that names it, no `Error:`, no change of the exit code): matches `rounds_item` and `item_count_reason`, which return a reason naming the missing item, and the tests `test_a_missing_or_doubled_item_gives_unknown_with_its_reason`, `test_a_record_without_the_item_gives_none_with_its_reason`. No change.
- **WAY-404** (binding sentence and *Verification*, as correction 2 and its fix left them): matches `read_contradiction` order (a round's yes first; the item once and the marker `open design choice`; a doubled item gives unknown before any marker). No change.
- **WAY-405** (binding sentences and *Verification*, as the fix left them): matches `discarded_entries`, `discarded_reasons`, `discarded_reason`, `item_texts` for the `none` clause, the second `reason: ` followed by a backtick, text beside the colon, a deeper line of an entry, an entry with no marker and the margin line. No change.
- **Part map**, `process-audit`, field *Trust boundary*: names `process-audit/audit_count.py` and `process-audit/record_items.py`; the part's *Files* `process-audit/**` hold the module. No change.
- **Record template**, item *Review rounds*: matches (`none` or nothing after the colon and entries; the two forms; the mark at the colon or the end). No change. Item *Discarded attempt*: corrected, below.
- **`task-cycle/skill/SKILL.md`, `reserved_return.md`, `correction.md`** (a second attempt written as an entry, the earlier one rewritten as an entry too), **`task-cycle/review/SKILL.md`** (the reviewer's mark and where the audit reads it): match the code. No change.
- **Docstrings** of `process-audit/audit_count.py` (the Q1 passage) and `process-audit/record_items.py` (module, `discarded_reason`, `discarded_reasons`, `item_texts`, `read_contradiction`): two corrected, below.

## What I corrected

1. `process-audit/SKILL.md` (the matter of the version series, Q1): it said `unknown` only "where an entry of a round carries no mark or *Discarded attempt* gives no reason", and `no` "where no entry says so"; the code also gives `unknown` where *Review rounds* is missing, doubled or in neither form, where *Discarded attempt* is missing or doubled, and where a text of one attempt holds a second `reason: ` followed by a backtick, and gives `no` only where every entry gives its mark. It now lists those, and says a `yes` stands over the `unknown` of any other part of the record save that the reason of a doubled *Discarded attempt* does not (only the mark of an entry does), as WAY-404's *Verification* says.
2. `task-cycle/record_template.md`, item *Discarded attempt*: the writer is now told the text of one attempt holds no other `reason: ` followed by a backtick (a second one gives `unknown`), beside the clause on the margin line that correction 2 added.
3. `process-audit/audit_count.py` docstring of Q1: the `no` clause says each entry does, where the item holds several, and a sentence says which yes stands over which unknown.
4. `process-audit/record_items.py`, docstring of `read_contradiction`: "held once by the record" for the marker, and "unknown otherwise, with the reason".

Left alone, as the handoff says: M-1 of `reports/review-correction2-report.md`, m-1 and m-2 of `reports/review-correction2-fix-report.md`.

## Entries written

None. No row of *Settlements to record*, projected entry, environment fact, glossary term or choice that binds after the merge is new; the entries the change writes (WAY-337, WAY-344, WAY-404, WAY-405, the part-map line) stand as they were. No pair of examples to reduce (none of the four carries one for this change).

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` (without `--skip-test-citations`) — exit 0, `0 errors`.
- `python -B gate/run_tests.py process-audit` — exit 0, `Ran 276 tests in 494.310s`, `OK`.
- `python -B gate/run_tests.py task-cycle` — exit 0, `Ran 534 tests in 147.973s`, `OK (skipped=2)`.
- Not run: the product's full gate (by the handoff).

## The own-work check

- **Requirement most likely unmet:** WAY-11 — each sentence that says how the audit reads *Discarded attempt* or *Review rounds* says what the code does; the likeliest miss is a place the earlier rounds did not touch (the skill, the template).
- **Check:** I read each such sentence in `foundations/decisions.md`, `foundations/part_map.md`, `process-audit/SKILL.md`, `task-cycle/record_template.md`, `task-cycle/skill/*.md`, `task-cycle/review/SKILL.md` and the docstrings, found by a search for `Discarded attempt`, `Review rounds`, `contradiction`, `second reason`, and compared each with `read_contradiction`, `discarded_reasons` and `read_rounds`.
- **What it showed:** the skill's Q1 sentence was narrower than the code on the unknowns and wider on `no` (corrected); the rest agree.

## Reaches beyond the handoff

None.

## Working copies

`.runs/author-correction-2-return/` (`.runs/author-correction-2-return/`) held the outputs of the two test runs; removed before this return. No worktree or clone.

## Unread material

none — `task-cycle/skill/return_step.md` and `foundation_step.md` whole, the handoff, WAY-337, WAY-344, WAY-404, WAY-405, the part-map entry, the template's items, the Q1 passages of `process-audit/SKILL.md` and `audit_count.py`, and `record_items.py` were read; the rest of `process-audit/SKILL.md` and `audit_count.py` only where the search named them.

## Searches not found or unclear

none.
