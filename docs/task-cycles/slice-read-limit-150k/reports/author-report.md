# Author report: slice reading limit to 150 000 tokens

Status: done with concerns (see Problems as observed and Choices made)

Worktree: `the task's worktree root`, branch `task/slice-read-limit-150k`, base `f04f046d5220913a4ae399faf59683129e81c936`.

## Commits

- `92e7576` Lower the slice reading limit to 150 000 tokens (code and test)
- `888eb61` Record the slice reading limit and the rejected size route (foundation entries)

## Files changed

| File | Added | Removed |
|---|---|---|
| `task-cycle/slice_size.py` | 9 | 6 |
| `task-cycle/test_slice_size.py` | 4 | 4 |
| `foundations/decisions.md` | 36 | 1 |

What changed:

- `READ_LIMIT_TOKENS = 150_000` in place of `CONTEXT_WINDOW_TOKENS // 4` (task To do 1).
- The paragraph of the limits in the docstring: the sentence "READ_LIMIT_TOKENS is a quarter of that window..." is replaced by the measurement described in words and numbers taken from the task's Need, with no source pointer (To do 2, WAY-27). The first sentence "The limits start with a wide margin..." and the `CONTEXT_WINDOW_TOKENS` and `CHARACTERS_PER_TOKEN` bullet with its source are kept.
- The report line now reads "Too large: more than 150000 estimated tokens to read at 2.5 characters a token, or more than 10 files to change." The table form is unchanged.
- The boundary test moves to 375 000 characters (150 000 tokens, fits) and 375 001 characters (150 001 tokens, too large), with the expected values updated. No assertion was weakened.
- `WAY-136`: a new rejected route appended to *Rejected* (To do 3, row 1).
- `WAY-371`: new decision for row 2 (150 000 tokens limit), with the rejected 175 000 and 125 000 values.

## Checks run

Each run from the worktree root, `the task's worktree root`.

| Check | Command | Exit code | Result |
|---|---|---|---|
| Baseline, before any change | `python -B gate/run_tests.py task-cycle` | 0 | 394 tests, OK |
| Test written first, run before the code change | `python -B -m unittest test_slice_size.SliceSizeTest.test_read_at_the_limit_fits_and_one_character_more_is_too_large` from `task-cycle` | 1 | Fails at its assertion `self.assertEqual(code, 1)`: `0 != 1`, because 150 001 tokens fitted under the old 250 000 limit. Expected reason. |
| Size test module after the change | `python -B -m unittest task-cycle.test_slice_size` | 0 | 16 tests, OK |
| Task-cycle suite after the change | `python -B gate/run_tests.py task-cycle` | 0 | 394 tests, OK |
| Foundation check | `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| Sample report output | `python -B task-cycle/slice_size.py <probe plan> --root .` | 0 | Report header prints the new line; the table form is unchanged. |

Checks not run: the full gate (the orchestrator runs it). Tests of other directories: a search (`test_*.py` files naming `decisions.md`, `slice_size` or `WAY-136`) found only fixtures in `elements/common/test_foundation_check.py`, `elements/common/test_migrate_foundation.py` and `installation/test_*.py`, which do not read the real text of WAY-136 or the changed script. Not run for that reason.

No invariant test was changed or written: no invariant covers the slice size (the search of `foundations/invariants.md` for `slice_size`, the limit and the quarter found none).

The invariant break check does not apply.

## Own-work check (section 3)

- Requirement: the limit is exactly 150 000 estimated tokens, so a slice reading 150 000 tokens fits and one reading 150 001 is too large; the docstring and the report line state the same value.
- Check: the boundary test above, run before and after the code change.
- Showed: failing before the change (exit 1, expected reason), passing after (exit 0).
- Mutations considered: a constant of 150 001 or 149 999 fails the two halves of the boundary test; a `>=` in place of `>` fails the 150 000 case. Empty return and hostile input are outside this change: the logic is unchanged apart from the constant.
- Second requirement: nothing in the diff names a private note, a file of the author's disk or an unreachable source (WAY-27). Check: `git diff` grepped for `Mariusz`, `Brain`, `Obsidian`, `zadani`, `notat`, `note`: no match (exit 1).

## Reaches beyond the dispatch

- Searched the whole foundation (WAY-33 by search, read per hit) for `250 000`, `quarter`, `READ_LIMIT`, `context window`, `slice_size` and `tokens` across the repository outside `.runs/`. Hits: the two `slice_size.py` lines and the two test lines, all changed; the `process-audit` numbers are unrelated. No invariant, glossary term, part-map entry or decision (other than WAY-136 and the new WAY-371) states the old limit.
- Read `elements/decisions/examples.md` and `WAY-03` whole as the example it names.
- Read `WAY-135` whole (task-cycle scope, its rationale on specs and the size judgment).
- Read `task-cycle/plan/SKILL.md` lines 185 to 224 (the size-check section), `task-cycle/skill/planning.md`, `task-cycle/plan/too_large.md` and `task-cycle/skill/return_step.md` whole. None states the old limit; the plan's size paragraph says only what is measured, which still holds.
- Checked `foundations/glossary.md` for `slice` (present, line 145) and for `token` (none). The new entry uses `slice` and `estimated tokens` in the sense the entries already give; no new term was needed.
- Checked the coding guidelines of the product for a rule of size: WAY-328 departs from them for the-way's own code, so the move rule of WAY-365 does not apply, and the change adds no function or file that grows past a threshold.

## Foundation entries written (WAY-134 row marks)

- `WAY-136` edited in place, marked `row 1`. The *Rejected* gains the route of a change-size measure, with the cost of whole cycles on both routes from the task's To do 3. Binding sentences and other fields are unchanged; the judgment from the task document remains the route.
  - Meaning in English: a measure of change size deciding the route at the cycle's start is rejected, because a whole cycle with a plan costs more per changed line than a whole cycle with one author.
  - Meaning in Polish: miara rozmiaru zmiany rozstrzygająca drogę na starcie cyklu jest odrzucona, bo cały cykl z planem kosztuje więcej na zmienioną linię niż cykl jednego autora.
- `WAY-371` new, marked `row 2`. Question: "What reading limit does a slice of a plan have?". Binding sentence: a slice is too large when its agent reads more than 150 000 estimated tokens. Scope `task-cycle`. Relations derives from WAY-136. Verification: a complies and a violates example. Rejected: 175 000 and 125 000 tokens, each with its cost, from the task's *Questions to settle* (not chosen).
  - Meaning in English: a plan slice is too large for one agent when its agent reads more than 150 000 estimated tokens.
  - Meaning in Polish: kawałek planu jest za duży dla jednego agenta, gdy jego wykonawca ma przeczytać ponad 150 000 szacowanych tokenów.
- No other entry was needed: no invariant, glossary term, part-map entry or environment fact follows from the change. The return step found nothing further to write.

## Choices made

1. Row 2 written as a new decision `WAY-371`, not as an edit of an existing one: the search found no entry that already states the limit (choice of the orchestrator point 2, so no tie was needed).
2. `WAY-371` *Based on* is `none`. The measurement comes from the task's private sources, which WAY-27 forbids pointing to, so it is described in *Rationale* instead. Alternative: `TODO — <what is missing, with its source>`. Cost if wrong: a reader may take the decision for one resting on no outside source; the *Rationale* carries the measurement, so the reasoning is still complete.
3. `WAY-371` Verification gives an optional complies and violates pair, since no invariant derives from it yet. Cost if wrong: none for the checks; a later invariant would need a `Verification` change.
4. The report line drops the quarter and the window; the sentence "at 2.5 characters a token" keeps `CHARACTERS_PER_TOKEN` in use. Cost: see Problems, `CONTEXT_WINDOW_TOKENS`.
5. The docstring measurement includes the about 21 000 and 13 000 to 16 000 input tokens per changed line figures from the task's Need, as the cost evidence of the band. Alternative: leave them out. Cost if wrong: the docstring is longer by two lines.
6. No move of code under WAY-365, as explained above.

## Unread material

- `WAY-229` read by lines 6828 to 6867 only (decision, rationale-free part of the entry). Its rest is unread; the change does not touch it.
- `WAY-328` read by lines 10927 to 10956 only; the rest of its *Rationale* and *Rejected* unread. The change does not touch it.
- The decisions whose *Scope* names `task-cycle` or `decisions` (the list from the search of `foundations/decisions.md`): I read whole WAY-27, WAY-33, WAY-135, WAY-136 and the examples' WAY-03. The other decisions of that scope (for example WAY-13, WAY-25, WAY-30, WAY-125, WAY-148, WAY-150) were not read whole; they were located by the title and *Scope* search and by the grep for `slice`, `plan` and `tokens`, with the hits read in place.
- The invariants whose *Part* names `task-cycle`, `decisions` or `every`: not read; located only by the grep for the old limit, which found none.
- The part map entries of `task-cycle` and `decisions`: not read whole.
- `foundations/environment_facts.md`: not read; the change rests on no citation.
- `task-cycle/plan/SKILL.md`, the rest of it outside lines 185 to 224: not read.
- `elements/common/way_of_working.md`, `rules.md`, `elements/decisions/skill/SKILL.md`, `template.md`, `read.md`, `decide_entry.md` and `foundation_step.md`: read whole.
- `task-cycle/change/SKILL.md` and `task-cycle/skill/return_step.md`: read whole.
- `task.md` (frozen task): read whole.

## Searches not found or unclear

- An invariant on the slice size or the limit: not found (`foundations/invariants.md` searched for `slice_size`, `READ_LIMIT`, `quarter`, `tokens`).
- An existing decision stating the 150 000 limit or the rejected 175 000 and 125 000 values: not found; the search of the whole foundation hit only WAY-136 and the slice reading in the plan skill.
- A source for the `Based on` of `WAY-371` that the repository may cite: none; see choice 2.
- The task's line "Limit 150 tys. pochodzi z jednego produktu" and the "Context" section were not used as sources of entries; the entries carry only the numbers of Need and To do.

## Problems as observed

- `CONTEXT_WINDOW_TOKENS` is no longer used by any limit or message. The task says it and its source stay, so it stays, and its docstring bullet still describes it. Cost: a constant that feeds nothing and a bullet that reads as if the window still matters. Alternative: delete the constant and its bullet, which the task's point 4 forbids; a later cycle may decide to remove it. Not a failure of any check.
- The first sentence of the limits paragraph, "The limits start with a wide margin", was kept as the task's point 4 allows. With 150 000 the margin is narrower than with 250 000; a reviewer may judge the phrase no longer exact. Flagged, not changed.
- The foundation check and the task-cycle suite ran with the defaults; the foundation step's `--skip-test-citations` switch was not used because no invariant is written.

## Status

`done with concerns`: the concerns are the unused `CONTEXT_WINDOW_TOKENS` constant and the partial reading of the decisions listed above, both recorded.
