PASS 10c0f9eed88d05b2cff8145d2c58227e94346c6d

# Review of the whole change — `defects-found-after-merge`

Range `6814c6f6c9ff2b29d34612fa5cc86945ec3a2812..10c0f9eed88d05b2cff8145d2c58227e94346c6d` (four commits of
the one author, one-author route). `git rev-parse HEAD` is the head given. Blocking findings: 0. Minor
findings: 5 (3 within the task, 2 outside it). Out-of-scope findings: 2 (both Minor, counted in the five).
No finding comes from a slice: the route has none.

## What I checked against the task

All four *To do* items are met by the commits:

1. `project-level/task/template.md:17` carries the header line `Defect introduced by:` under `Project
   relation:` in the form the task's answer gives (`none` | addresses joined by ` · ` | `unknown — <why>`),
   with the fixing-task rule, the commit address for a change without a request, the filler (the refining
   agent, never the cycle) and "a missing line means not assessed, never `none`" (`template.md:101-113`).
   `project-level/task/skill/draft.md:20-29` has the refining agent fill it in every task.
2. `task-cycle/record_template.md:190-211` has the item *Corrections after the request opened* in *Request
   handoff*, before `Process remarks on the-way`, which stays last. `task-cycle/skill/correction.md:33-35`
   writes the human's remarks word for word to `reports/correction-<n>-remarks.md`, also for remarks given
   in conversation and for a refresh of the target branch only. `correction.md:52-63` has the orchestrator
   add the line; `item <n>` is the number of a kind (stated in `record_template.md` and `correction.md`).
3. `task-cycle/skill/request_template.md:314-319`: kind 17 in *You accept by merging* after kind 15, in
   kind order (kinds in that group run 5, 6, 7, 10, 11, 12, 13, 15, 17); the correction row of the variants
   table names it (`:452`).
4. `process-audit/problem_register.md`: the two classes on the start list (`:52-53`), the `item · defect` to
   `known-problem-left` sentence (`:61-63`), *Record* and *Stages* sentences for both rows (`:119-130`). The
   counting command is untouched.

The eleven accepted rows each stand written whole in a decision, in these entries (the author's table, which I
verified against the entries): row 2 in WAY-353; rows 1, 3, 7, 8 in WAY-354; rows 4, 9 in WAY-355; rows 5, 10
in WAY-356; rows 6, 11 in WAY-357. I compared each entry with its rows and with the *Questions to settle*
answers: meaning, forms (`none`, ` · `, `unknown — <why>`, commit address), classes, `after the merge`, `at
the request`, `item <n>` as a kind number, `target-branch · none` only. No entry says more or less than its
rows. *Rejected* of each entry reproduces the *Not chosen* of the question the rows' *Source* names (WAY-134);
rows 7-11 name *To do* items, which keep no ways, so they add none. The two numbers the answer to the last
question names (`remark · defect`, `item · defect`) are in WAY-356's rationale.

Cross-file consistency (the handoff's first point): kind 17, the pair `source · kind`, `item <n>` as a number of
a kind, the line `Defect introduced by:` and its forms, the two class names, `after the merge` and `at the
request` read the same in the template, the skill, the record template, the request template, the register
and WAY-353 to WAY-357. I found no contradiction between the five new decisions, WAY-287 and the files.

**The sentence on documents written before the line** (second point): the answers say "has none, and no line
means not assessed, not `none`". WAY-354 and `template.md:111-113` state it with the qualifier. `draft.md:27-29`
says "keeps none, and its missing line means that it was not assessed", which carries the same meaning but is
open to a wrong reading (Minor 1).

**WAY-287 edit** (third gap): the diff of WAY-287 holds the pairs added to the binding sentence's list (with
WAY-356 cited), one *complies* example, one *violates* example and one rationale sentence. *Rejected* is
untouched, and so are *Scope*, *Relations* and the remaining text. The binding-sentence change is what the
task names; the example and rationale sentences follow from it and add no rule. I count it as only what the task
says.

**Tests** (fourth point). I ran the author's mutation myself on a copy of the head outside the repository
(`git archive` into the scratchpad): the corrections item moved after the process remarks in
`task-cycle/record_template.md`, then `python -B -m unittest -k corrections test_remarks_check` in `task-cycle/`:
1 error, `ValueError: substring not found` in `test_the_corrections_item_before_the_remarks_is_no_part_of_their_block`
(the intended break: the order; it errors, not asserts, but the test does not pass). The two other tests
(`CommandTest.test_a_corrections_item_and_a_file_of_the_humans_remarks_change_nothing`, `Remarks.test_the_corrections_item_before_the_remarks_item_is_not_among_its_entries`)
use hand-built fixtures, not the template, and pass on the code before and after the change; they protect the
reading of the new form against a later break of the readers (the remarks file read as a report: 2 reports
counted; the remarks count 1 beside a corrections item with two lines), and they assert real values
(`row[2]` is the *Value* column of *Unknown values*, so the `assertNotIn("Remarks", ...)` is not vacuous; I
checked `remarks_of` and the table rows). They test the form the readers accept, as the author says; no test
shows a reader that would break, because none does. No invariant test changed.

**Private paths** (fifth point): `git diff` of the range has no drive path, `[[ ]]` note link or note title in
any added line (grep over added lines: no match). No private path or note link in a committed file.

**Reader behaviour** (the author's Searches 1): I read `task-cycle/remarks_check.py` through its tests and
`process-audit/audit_count.py` `review_rounds` and the remarks reading. The remarks file name holds neither
`handoff` nor `findings`, so `remarks_check` reads it as a report (no section, no item; WAY-294) and the audit's
*Fix rounds* does not take it for a findings file. The corrections item stands at indent 0 before the remarks
item, so the remarks block ends where it starts and the audit counts its entries as before. The nightly review
itself is outside the repository; I could not check it (see Searches).

## Findings

### Critical

None.

### Important

None.

### Minor

1. `project-level/task/skill/draft.md:27-29` (and, in the same shape, `project-level/task/template.md:111` and
   WAY-354's last sentence, "has none"): "a document the refinement does not reopen keeps none, and its missing
   line means that it was not assessed". Written without backticks, "keeps none" can be read as "keeps the value
   `none`", the very reading the decision forbids; the next clause corrects it but a reader or an agent
   skimming the first clause may stop there. Suggest "keeps no line" in `draft.md` and "has no line" in the
   template and WAY-354. Within the task (it is the sentence of the task's own *Question settled*; the wording
   is the task's, so a change of it is a choice of the human). Grade Minor: the second clause states the
   meaning in the same sentence.
2. `task-cycle/skill/correction.md:56-57`: "as in item 8 above". The only mention of item 8 is below
   (`correction.md:65`); nothing above names it. A reader looks for an earlier passage that is not there.
   Suggest "as in item 8 below" or name `request_template.md` kind 8 in place. Within the task.
3. `project-level/task/template.md:112-113`: the sentence on `TODO` ("`TODO` marks a missing answer; never use
   it to make an unfinished task look ready.") was its own line before the change and is now joined at the end
   of the new paragraph's last line, a line longer than the rest of the paragraph. The sentence is unrelated to
   the new line and reads as part of it. Cosmetic; within the task (the author's edit made it).
4. `foundations/decisions.md` WAY-356 and the matching passages (`task-cycle/record_template.md`,
   `correction.md`): the word "kind" has two meanings in one rule: "the number of that item's kind in the
   template" (a kind of request item) and "the pair source · kind" (`defect`, `not-required`, `none`). The words
   come from the task's own answers (Polish "rodzaj" for both), and each use is explained at its place, so no
   reading is wrong today. Grade Minor; **outside the task** (the task's answers fix the word; renaming one of the
   two is a decision of the human, offered as a separate matter, not a defect of this change).
5. `task-cycle/skill/request_template.md:314-319`, kind 17: an item of *You accept by merging* "says what the
   cycle chose or wrote and why" (`request_template.md:337-338`, WAY-327's neighbour rule); kind 17 gives the
   sentence content but not the "why" or an alternative, and for `target-branch · none` it asks for a judgment
   ("whether the cycle judged that the task or the foundation required what the correction changed") that
   WAY-356 sets as `none`. A writer of the description must improvise the sentence for a refresh-only
   correction. Grade Minor; **outside the task** (the task's *To do* 3 says only "pokazuje pary tej poprawki
   jednym zdaniem").

### Declined to judge

- The author's Concern 1 (after correction n the description shows only that correction's pairs): *To do* 3 and
  row 5 say "pary tej poprawki"; the change follows the words. Whether the human wants every correction shown is
  a choice outside the task.
- The author's Concern 2 (item 17 makes *You accept by merging* non-empty after any correction, also a
  refresh-only one): the same words of the task give it; the decision WAY-287 now says so in its *violates* list.
- The human actions of the task (the user's register classes, the nightly review reading the new line): outside
  the repository (WAY-330); not part of this change.
- A correction made for the human's decision at a blocked request has no named source in the closed list of
  sources; it falls under `item 1` (an answer to an item of *Needed from you*), which `correction.md` does not say
  in so many words. I set it aside as the task's *Context* names three entries of a correction and its answers
  fix three sources, so the gap is the task's, not the change's.

## Checks run

All from the worktree root unless stated; the reviewed worktree, its index and branch were not changed
(`git status --short` empty at the end).

- `python -B gate/run_tests.py task-cycle` — exit 0 (367 tests OK).
- `python -B gate/run_tests.py process-audit` — exit 0 (180 tests OK).
- `python -B gate/run_tests.py project-level` — exit 0 (275 tests, the output's last lines `OK`).
- `python -B gate/run_tests.py agent-instructions` — exit 0 (18 tests OK).
- `python -B gate/run_tests.py instruction-files` — exit 0 (104 tests OK, 5 skipped).
- `python -B elements/common/foundation_check.py .` — exit 0, `0 errors` (also with `--skip-test-citations`, exit 0).
- Mutation run on a copy of the head in the scratchpad (not the repository): the corrections item moved after the
  process remarks item; `python -B -m unittest -k corrections test_remarks_check` in `task-cycle/` — the
  template test errors (`ValueError: substring not found`), `FAILED (errors=1)`; the shell's `echo $?` printed 0
  because it reported `tail`, not the test; the test did fail.
- Manual: `git diff 6814c6f..HEAD` read whole (all nine files); grep over added lines for drive paths, note links
  and private note names: no match; kind order of *You accept by merging* in `request_template.md` read.
- Not run: the full suite `python -B gate/run_tests.py` with no argument (the cycle's own run), `elements/common`
  tests (the author's run of 144 tests is the only one; no file of `elements/common` changed in the range).
  Not run, nothing in the repository to run: the nightly review of cycles.

## Reaches beyond the dispatch

- `task-cycle/skill/SKILL.md` lines 515-624 (the process remarks check, the cleaning of the record's copy), to
  check that the remarks file and the new item pass the cleaning and the remarks check; `task-cycle/skill/request_template.md`
  lines 190-360 and 440-460 (kinds, groups, variants table), `task-cycle/record_template.md` lines 160-215,
  `process-audit/problem_register.md` whole, `process-audit/audit_count.py` lines 60-95, 1025-1075 and a grep
  for `correction`, `Stages`, `reports`; `task-cycle/cycle_stages.py` by grep for `reports`;
  `foundation-review/with_the_human.md` lines 22-45 (it makes task documents by the template; the new line is
  left to the refinement, which `draft.md` now orders — a gap by nothing) and a grep over the repository for
  other readers of `Project relation`, `Request URL and status`, `Review rounds`, `task/template.md`: to find
  files that list the header lines or the items of the record and need the new one. None found.
- Invariants of the touched parts by header (`foundations/invariants.md`): read whole `project-plan-state-evidence`,
  `project-plan-form`, `project-definition-form`, `record-copy-image-check`; the part-map entries of
  `project-level`, `task-cycle`, `process-audit`, `foundation-review` (lines 77-125). Why: the parts the diff
  touches and the readers of the task document header.

## Unread material

- Decisions of my selection: 183 decisions have *Scope* naming `project-level`, `task-cycle` or `process-audit`
  (found by a search of the *Scope* lines of `foundations/decisions.md`), of which 5 are the change's own. I read
  **18 whole** (the five new ones, WAY-124, 134, 148, 287, 289, 290, 294, 296, 327, 330, 333, 335, 339) and ran
  through the other **165 by title only**.
- Decisions whose title I judged to have no bearing and did not open: WAY-331, 332, 336, 338, 340, 341, 347 to
  351 (the handoff's list, apart from WAY-344), WAY-342, 343, 345, 346, 352 (price list, schedule, results'
  place, cost and context measures). The change touches none of the files they concern.
- Decisions that may bear on the change and stayed unread (I did not open them; none of their text was needed to
  reach a finding, and the tests that cover their readers pass): WAY-286 (the form of a request's description:
  the kinds' place in it), WAY-288 (language), WAY-295 (a listing held wrong), WAY-306 (merge of the target
  branch in a correction), WAY-308 and 309 and 323 (private paths and their check: I checked the diff by grep,
  not by their rules), WAY-337 and 344 (cost and missing fields in the audit's reading), WAY-161 (the
  findings route). The handoff's WAY-344 is among them: I did not read it whole.
- Guidelines: the-way holds its own code to the general coding and testing guidelines of a product (WAY-328);
  I did not read the guideline files for the two Python tests added, and judged them by their own
  fixtures and the existing tests next to them. The glossary was not read whole; the terms the change uses
  (`correction`, `defect`, `kind`) have no entry (the author's third search).
- Invariants not read: only those named above; the invariants whose *Part* is `every` I did not read whole
  (`return-step-record`, `derived-file-content`, `tracked-file-private-paths` are the ones the change could
  touch; the checks show no change in a file one of them cites).

## Searches not found or unclear

- The nightly review of cycles (the user's tool) is outside the repository, so I could not check that it reads
  the new item and the remarks files as the task's *Human actions* ask; I checked only `remarks_check.py` and
  `audit_count.py`.
- No file lists the header lines of a task document, so `project-level/task/skill/draft.md` as the place that
  has the line filled is a judgment (the author's; I found no better place and accept it).
- "Fixing task" and "correction" have no glossary entry (the author's third search); no sentence in the files
  is read wrongly for lack of one, so it is no finding.
- The handoff's author note that the other three directories were not run again after the final test fix: I ran
  all of them on the head myself (see Checks).
