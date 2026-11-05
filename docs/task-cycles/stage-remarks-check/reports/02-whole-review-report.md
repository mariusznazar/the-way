PASS 5e90498974fd8f627e16191f4f03245acd1f554b

# Review of the whole change — task stage-remarks-check

Range `b96cfff..5e90498` (2 commits: `2a4847e`, `5e90498`); `git rev-parse HEAD` in the worktree is
`5e90498974fd8f627e16191f4f03245acd1f554b`. Counts: blocking 0, Minor 3, out of scope 0.
No spec, no plan (one author); no slice reviews existed, so I judged the whole range as section 2 gives.

## Findings

### Critical
none

### Important
none

### Minor

**M1. The match is a substring match over all remark blocks, so a short item can be masked by longer text of another entry.**
`task-cycle/remarks_check.py:315` and `:328` (`remarks.count(item)`), `:330`.
The remarks are one joined string and an item is "held" when it occurs anywhere in it as a substring, with no
boundary at the start or end of an entry. An item of one report that is a substring of another entry's text counts as held.
Evidence (scratch record, outside the worktree): `cycle.md` holds one entry
`stage a, <path>: A source outside the product: none found.`; report a gives that item, report b gives the bare item
`none found.`; `python -B task-cycle/remarks_check.py <record>` prints `checked: 2 reports, 2 items other than none, 0 not in the
process remarks`, exit 0, although no entry for report b exists. In the real archives there are short items
(`reset-hasla`: eight items below 60 characters, e.g. `Otherwise none.` in seven reports), so the case can occur.
Why it matters: a missing item hides, which is the failure the task fights; but it needs a short item, the task asks for
"word for word inside the block" (a containment reading), and the repeat count already covers identical items. Not blocking.
A fix, if wanted, is to require the item to stand at the end of an entry line (after `: ` or at a line start) in new-form records.

**M2. A listing held wrong leaves the request state unchanged, where the task's row 2 says "as with `request_check.py`".**
`task-cycle/skill/SKILL.md` ("A listing you hold wrong"), `task-cycle/skill/request_template.md` variant row "A remarks listing held wrong".
WAY-291, which row 2 points to, makes the request a draft whose human-decision section names the error. The change copies the
rest of that rule (script not changed, archive written, case in the remarks, item in *For you to decide* with "Merge as it stands?",
*Checks* names the check) but keeps the request's state "unchanged", as the author's report states and gives the cost of. The task's
words for the rule (row 2 and *To do* 2) name the three steps the change does and no draft state, so this is within the task; it is a
choice the human may want to see. Equality with row 2 otherwise holds (see Checks of the task below).

**M3. `display()` escapes non-printable characters in the printed item, but the orchestrator is told to copy the printed item word for word.**
`task-cycle/remarks_check.py:85-87`, `:347`. A report item with a character that `str.isprintable` rejects and `str.split`
does not treat as whitespace (for example U+200B) is printed as an escape (`\u200b`); the copy would not match the original and the
script would list it again for ever. Whitespace-like characters (NBSP included) are collapsed to a space first, so the real archives
are not affected (I saw no such character in the listed items of the three archives, but did not scan every item). Rare; the held-wrong rule is the way out.

## Task checks

- **Script listing against *To do* 1 and the acceptance criteria.** Both forms (heading at any level; bold label with colon inside,
  outside or absent, at line start or as list item), items other than `none`, ordering by report name, path of the report printed, only
  `*report.md` files read (handoffs, findings, logs not read). The script only lists. Verified by reading the code, by 137 tests in
  `task-cycle`, and by running it myself on fresh extracts of the three archives (below).
- **Match inside the block the digest cuts.** `remark_blocks` / `opens_block` in the script are a port of `extract_remark_blocks` /
  `_opens_block`. I imported the real `cycle_remarks_digest.py` (read-only, no bytecode written) and compared the blocks it cuts with the
  script's blocks on `plomyk`, `reset-hasla` and `kopia-bazy` `cycle.md` and on `task-cycle/record_template.md`: equal in all four. An item
  outside the block does not count (test `test_an_item_that_stands_outside_the_remarks_block_does_not_count`).
- **Acceptance 2 (loop2 archives, `git show`, never checked out).** `plomyk@31ac651`: lists `06-return-step-report.md` "Unclear: whether D-175's
  last sentence …" (plus 6 more: 3 of `04-whole-review-report.md` outside the digest's cut, 3 `none found`-style lines of 06). `reset-hasla@b311814`:
  lists the reconciliation report 37 (3 items) and its review 38 (3 items); the task says two each, the script finds three each, and none of them stands in
  `cycle.md`, so the criterion holds (see Searches). `kopia-bazy@d79c8e4`: lists `slice-6-fix-report.md` ("None unresolved. Unclear: `rsync` …") and
  `correction-2-report.md` ("Head `e69034c` …"). Summary lines: 7 / 6 / 8 not in the remarks. Matches the author's report.
- **Acceptance 1, template form against the digest's cut.** The template block is the list item `- Process remarks on the-way: …` with entries indented
  under it. I built a record in that form (blank line between two entries included) and ran the real digest function: one block, all entries
  inside; the script reads the same record and reports 0 missing for an item in each report form. A test of the template
  (`TemplateTest`) exists. The template item is the last item of the record template, and the explanatory paragraph under it is at indent 0 so it ends the block.
- **Process text leaves no commit adding the record without the check.** The commits that add the record: step 12 (check placed before the
  description, again before the commit if a report or remark changed), step 9.4 stop (SKILL.md line ~308), `blocked_finding.md`, `reserved_return.md` step 1,
  `correction.md` (also reached by `reserved_return.md` "After a correction", which repeats the pair "as `correction.md` gives"). `grep` for
  `docs/task-cycles`, "pair of commits", "adds the record", "its removal" over `task-cycle/`, `elements/`, `agent-instructions/` finds no other site. The README
  integration route (`agent-instructions/README.md`) names no record commit.
- **Rule for a listing held wrong equals row 2.** Script not changed in the cycle; archive written; case entered in the process remarks (as an
  entry of the orchestrator, not an item of its stage); item in *For you to decide* with "Merge as it stands?"; *Checks* names it. The one additional
  condition "with evidence you can name" is copied from WAY-291 and narrows only the orchestrator's licence; see M2 for the request state.
- **WAY-294 to WAY-296 against rows 1-3.** WAY-294 = row 1 (every adding commit; copy, correction repetition, blocked copies; list-append-rerun until nothing listed; the
  two not-chosen ways under it as *Rejected*). WAY-295 = row 2, `narrows WAY-294`. WAY-296 = row 3 (one form given by the template, read by the check, no section or file of
  its own). *Rejected: unknown* in WAY-296 is allowed by `elements/decisions/template.md` and the row's source names no way not chosen. No contradiction with WAY-260
  (copy every item word for word, keep repeats apart: the script counts repeats), WAY-148, WAY-290/291 (the pattern, not their draft state; see M2) or WAY-38/89
  (standard library, `from __future__ import annotations` with Python 3.14). `foundation_check.py`: 0 errors. The change writes no invariant and the invariant tests
  are untouched. No part-map change needed (`task-cycle/**`).
- **Tests.** I ran four mutations on a copy of the script and test file in the scratchpad: remarks taken as the whole `cycle.md` (1 failure), `none` test turned into
  `startswith` (3 failures), exit code always 0 (7 failures), block cut to its first line (11 failures). All caught. Tests state expected values by hand
  (fixtures in the test file), not from the code's own output. The tests do not cover M1.
- **Own-work check (WAY-164).** The requirement the author named (every item of the real reports, in the forms agents write) is the weakest spot, and the check
  (an independent count against the script on real archives, plus a BOM test written after it showed a gap) would catch a missed item. I repeated the idea: every report
  of the three archives (3 + 38 + 41) contains the section name, the forms seen are the heading (77) and the bold label (several, one list-item form); the script finds the section in all.
- **Reserved choice.** The change settles no language, framework, library, store, login or place to run.
- **Unrequested additions.** `request_template.md` item 10, the *Checks* mention and the variant row, and the calls in `blocked_finding.md` and
  `reserved_return.md`: follow from "the blocked variants" of *To do* 2 and from "stawia go w opisie requestu". Not out of scope.

## Declined to judge

- The wording quality of the Polish/English meanings in the author's foundation step: outside the task's code, the entries are in English and consistent.
- How `cycle_remarks_digest.py` itself treats the old-form `plomyk` second entry (`- From stage review-change …`, outside its cut): the digest is outside the repository and out of the task.
- The record template's Verification rule "each failing run remains in the record" against SKILL.md's "record the last run … with the number of runs" for the remarks check
  (the form check uses the same last-run-and-count pattern): left as the existing pattern.

## Checks I ran

- `git rev-parse HEAD` in the worktree: `5e90498974fd8f627e16191f4f03245acd1f554b`; `git log b96cfff..5e90498`, `git diff b96cfff..5e90498`: read whole.
- `python -B gate/run_tests.py task-cycle`: exit 0, 137 tests OK.
- `python -B elements/common/foundation_check.py`: exit 0, `0 errors`.
- `python -B task-cycle/remarks_check.py <scratch extract>` for `plomyk`, `reset-hasla`, `kopia-bazy` (extracts from `git show` of `31ac651`, `b311814`, `d79c8e4` in `C:\Storage\repos\loop2`,
  in `C:\Users\Mariusz\AppData\Local\Temp\claude\6b84451ec494cdda\821349a6-1a76-4a81-8e07-c83682a50609\scratchpad\rev\`): exit 1 each, 7 / 6 / 8 listed.
- Parity of the script's `remark_blocks` with the real `cycle_remarks_digest.extract_remark_blocks` on four texts: equal (scratch script `…\scratchpad\rev\cmp.py`, `-B`).
- Scratch record for M1 (`…\scratchpad\rev\t1`): exit 0 with a missing item (demonstrates M1). Scratch record in the template form (`…\scratchpad\rev\t2`): exit 0, 0 missing; digest cut shows one block holding all entries.
- Four mutations in `…\scratchpad\rev\mut2` (see Tests): each run of `python -B -m unittest test_remarks_check` exit 1 (caught).
- The full gate `python -B gate/run_tests.py`: not run, the orchestrator's.

## Reaches beyond the handoff

- `agent-instructions/README.md` lines 55-100 and `foundations/part_map.md` (task-cycle entry, grep): to see whether the integration route or the part map names the record commits or the scripts; neither needed a change.
- `elements/decisions/template.md` (grep for `unknown`) and `foundations/decisions.md` (grep of WAY-29x and the count of `*Rejected:* unknown`): to judge the `Rejected` line of WAY-296.
- `task-cycle/record_template.md` lines 115-185 (Verification, Request handoff): to check where the check's run is recorded and the template's block.

## Searches not found or unclear

- A guideline for the-way's own scripts and tests (WAY-215): not found, as the handoff says (no `guidelines/` directory); I judged the tests against the existing tests of `task-cycle/`.
- Where the task's count "two items each" for `reset-hasla` reports 37 and 38 comes from: unclear; the script finds three each, and all three of each are real, unheld bullets.
- Whether "as with `request_check.py`" in row 2 was meant to include the draft state of WAY-291: unclear from the task (M2).
- A way to check the script's port against the live digest inside the repository's own tests: not found (the digest lies outside the repository); I compared them by hand once, as above.
