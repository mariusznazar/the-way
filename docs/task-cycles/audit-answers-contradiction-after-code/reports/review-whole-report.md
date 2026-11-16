FAIL ab2c8c801b2ba9170a00ed6056b8b7c56b062868

# Review of the whole change — audit-answers-contradiction-after-code

- Range: base `aba5ee92a0734c2e775cc69662af669bf6455795` to head
  `ab2c8c801b2ba9170a00ed6056b8b7c56b062868` (`git rev-parse HEAD` in the reviewed worktree gives the
  head). Three commits: `6867078` (the move), `19f7003` (code, tests, WAY-403, WAY-404, WAY-337),
  `ab2c8c8` (instruction texts). One-author route, no spec, no plan; no slice to name for a finding.
- Method: `review-change` as it stands at the base (`git show aba5ee92:task-cycle/review/SKILL.md`) and
  `task-cycle/review/whole_change.md`; the head's text of `task-cycle/review/SKILL.md` is reviewed as
  part of the change. The base method asks for no mark of contradiction; for the record the change
  introduces, each blocking finding below also carries the mark the head's method gives.
- Counts: 1 blocking (Important), 2 Minor within the task, 0 out of scope; 3 lines of Declined to judge.

## Findings

### Important

**I-1. The reworked reading of the cycle record reads a missing item as `unknown` with exit code 0,
which WAY-344 does not allow for that file.**

- Places: `process-audit/record_items.py:90-91` (no item *Review rounds*: `None` with the reason
  "the record holds no item `Review rounds`: an earlier form"), `process-audit/record_items.py:228-230`
  (no item *Discarded attempt*: `None` with `item_count_reason`), `process-audit/audit_count.py:1182-1184`
  (the reason goes to *Unknown values* only: no missing field is put on the cycle, so no `Error:` line
  and no exit code 1); the tests that hold this behaviour as the required one:
  `process-audit/test_audit_count.py:3788`
  (`test_a_record_without_the_item_discarded_attempt_or_review_rounds_gives_q1_unknown`, which asserts
  exit code 0 through `run_versions`) and `process-audit/test_record_items.py:89-95`, `:238-242`.
- What is wrong: WAY-344 (`foundations/decisions.md:2843`) binds, in a script a change changes, "the
  whole reading of each file whose way of reading the change reworks — every field of that file"
  (`foundations/decisions.md:2850`). This change reworks how `audit_count.py` reads `cycle.md` (the
  items *Discarded attempt* and *Review rounds*), so every item of `cycle.md` the command reads comes
  under the rule. For the command that counts the audit the rule is: "in a file of a cycle's record
  that it reads from git history, gives the values that need a missing field as unknown, writes its
  result and ends with exit code 1 and a line `Error:` that names the file and the field"
  (`foundations/decisions.md:2854-2856`). Its exception for an earlier form names the cases where the
  command reads a file as that form — three forms of a stage report — and no form of `cycle.md`. Its
  *Verification* lists as a violation "a change that reworks the reading of a file checks the field it
  added and leaves the other fields of that file unchecked", and its *Rejected* says of a case left out
  of the decision's sentence: "the code departs from this decision and the departure returns at the
  next review" (`foundations/decisions.md:2999`). The precedent in the same script is explicit: "Every
  field of `stages.md` is under this check, since this reading of the file is reworked"
  (`process-audit/audit_count.py:205-206`), with each earlier form of `stages.md` written into WAY-344.
  The change does neither for `cycle.md`: it reads a missing item as an earlier form on its own
  authority.
- The author's evidence, weighed: its reading is the one WAY-344's *Rationale* supports ("A field that
  an earlier form of a file never had is no loss of the file ... read as missing, it would end every
  count in exit code 1 ... and an exit code that every run gives carries no signal"), and my own run
  over the archive confirms the scale: of the last copies of the 103 records of
  `docs/task-cycles/*/cycle.md` in history, 10 have no item *Discarded attempt* and 67 have no item
  *Review rounds* in its form, so an `Error:` per missing item would make every count end with exit 1.
  So the behaviour is likely right and the decision's text is what lacks the case. But that is a
  change of an approved decision the task does not carry, and WAY-30 (`foundations/decisions.md:1184`)
  gives the route: when a contradiction shows during implementation the agent "either brings the
  change into line, drops the change, or proposes on the task branch an edit of the decision, a new
  wording or a narrowing, and the code that needs it waits for that human"; "no exception lives only
  in a task document, plan or cycle record". The author's report raised the concern but the branch
  carries no proposed narrowing, and the exception now lives only in code and in the author's report.
- Why it matters: the merged code and WAY-344 would say two things about the same reading; the next
  reviewer of a change to `record_items.py` or `audit_count.py` meets the same departure, and a later
  author may "fix" it into `Error:` lines that fire on every run.
- Recommended fix (the orchestrator's and the human's to settle): propose on the task branch a
  narrowing of WAY-344 that names the items of a cycle record the count reads as of an earlier form
  where they are missing — at least *Discarded attempt* and *Review rounds*, and whichever other items
  of `cycle.md` the command reads (*Process pin*, *Plan*, *Slices returned too large*, *Process remarks
  on the-way*), since the rule now covers the whole file — giving `unknown` with a reason that names
  the item, no `Error:` line and no change of the exit code, with its *Verification* naming the tests
  that hold it; the merge then waits for the human's acceptance (WAY-30, WAY-14). The other way,
  `Error:` lines with exit 1 for a missing item, is the one WAY-344's own rationale argues against.
- Contradiction: yes — WAY-344 (mark of the head's method, for the record).

### Minor

**M-1 (within the task). A cycle that discards two attempts has no form in *Discarded attempt*, and the
count reads it as "no marker".** The skill allows two discards in one cycle: a discard for an open
design choice, then, after the spec, a one-author route judged again that proves too large
(`task-cycle/skill/SKILL.md:374-383`), or a correction that meets either again
(`task-cycle/skill/correction.md:42-43`). The template gives one item that opens with one reason
(`task-cycle/record_template.md:38-42`), and the two places that write it say only "Record it under
*Discarded attempt* with the reason `size`" (`task-cycle/skill/SKILL.md:382-383`). A leader that
replaces the first reason with the second leaves Q1 `no` for a cycle that had an open design choice;
one that adds a second reason gets `unknown` from `discarded_reason`
(`process-audit/record_items.py:214`, `text.count(REASON_START) != 1`) with the reason "the item
`Discarded attempt` holds no marker of its reason" (`process-audit/record_items.py:235-237`), which is
false for that text (my probe: `reason: `size`; then reason: `open design choice`` gives exactly that
reason). *To do* 3 makes Q1 `yes` where *Discarded attempt* has the marker `open design choice`. Fix:
give the template a form for a second discarded attempt (for example one marker per discarded attempt,
each opening its own line or entry) and read `yes` where any marker is `open design choice`, or at
least give two markers a reason of their own.

**M-2 (within the task). WAY-404 says an item with no marker gives `unknown`, which read alone takes in
`none`.** `foundations/decisions.md:7951-7952`: "so that an item with no marker, written in any earlier
form, gives the answer unknown". `none` carries no marker and gives `no` in the code
(`process-audit/record_items.py:211-212`, `:232-243`); the sentence before it ("the item reads `none`
where no attempt was discarded") and WAY-403's *Verification* make the intent readable, so the code and
the entry agree. Wording: "an item that reads neither `none` nor a marker".

## Coverage of the task

- *To do* 1: `task-cycle/review/SKILL.md` section 3 (head, lines 153-162) gives the mark, what counts
  (an entry of the foundation, the change's own included; an answer of *Questions to settle*, a row of
  *Settlements to record*, a decision of *Decisions in play*) and that an undone point of *To do* is
  none; section 4 carries it into the report. Met.
- *To do* 2: `task-cycle/skill/SKILL.md:219-227` (findings file with the mark; the round's entry says
  `yes`/`no`, a new finding of the fix review included) and `task-cycle/record_template.md:53-72`. Met.
  The author found no step naming the moment the entry is written; the task asks for the mark in the
  entry and names the template and the one paragraph, not a step, so none is required.
- *To do* 3: `process-audit/record_items.py:219-243`; no inference from the text of remarks or of the
  item; `denied_before`, `phrase_starts` and the denial constants are gone. Met (see M-1 for two
  markers).
- *To do* 4: review entry form in the template (`task-cycle/record_template.md:69-72`), in `round_of`
  and `review_rounds` (`process-audit/record_items.py:117-162`), not counted as a fix round
  (`test_audit_count.py` `test_reviews_that_passed_alone_say_the_cycle_had_no_fix_round`), `no` for Q1;
  an entry in neither form gives `unknown` with a reason. Met.
- *To do* 5 and settlement row 3: one reason for an unmarked round, old or new form, at
  `process-audit/record_items.py:241-242`, replacing `a review round names findings, and their content
  is not in the record`. The task gives the reason in Polish („wpis rundy nie mówi, czy była
  sprzeczność”, in Polish quotation marks, not as a literal in backticks as it gives the old English
  reason); the code gives it in English, "the entry of a round does not say whether there was a
  contradiction", as every other reason of the count is English. I take this as a faithful rendering,
  not an alteration. Met.
- *To do* 6: template (`task-cycle/record_template.md:38-42`), `task-cycle/skill/SKILL.md:374-376` and
  `:382-383`, `task-cycle/skill/reserved_return.md:35-37`; only the marker is read. The four examples
  of review #100, word for word as the task gives them, give `unknown` in
  `test_record_items.py:57-67` and through the command in `test_audit_count.py:3699`. Met.
- Questions to settle 1-5: answers 1 and 2 in the review method and WAY-403; 3 in the template, the
  code and WAY-337; 4 one reason; 5 the marker. Each *Not chosen* of 1, 2, 3 and 5 stands in a
  *Rejected* (WAY-403, WAY-337, WAY-404). Met.
- Settlements: row 1 → WAY-403, row 2 → the new paragraph of WAY-337, row 4 → WAY-404, each compared
  with its row, its question and the code: they agree (M-2 is wording). Row 3 is code. The part map's
  *Trust boundary* line for `process-audit/record_items.py` (`foundations/part_map.md:135`) follows
  WAY-48: the module takes the lines of records read from git history.

## Trust boundary: crafted input

Probes of my own against `record_items.read_contradiction` at the head (script and output in my
working directory, removed): an item *Review rounds* in a code fence beside one outside it, a quoted
`contradiction yes` on a continuation line, an entry quoted deeper or in another item, numbered and `*`
markers, a tab after the item's dash, `none` in backticks or bold, a marker inside a fenced block under
the item, a review and a findings entry with one path, CR and U+2028 line breaks, a no-break space
after the colon, an item indented off the margin, 50,000 doubled items over 100,000 entries (0.43 s),
an item of 200,000 lines (0.14 s), 2,000 items of 2,000 lines each (2.55 s, linear). No `yes` or `no`
the text does not state, no hang, no crash; every reason is a fixed string, so no text of a record
reaches a cell (the head's tests check control characters in cells,
`test_crafted_entries_of_review_rounds_break_no_cell_and_give_no_answer_they_do_not_state`). Over the
103 archived records: 4 `no`, 99 `unknown`, no `yes`, no crash.

## The move and the structure the change leaves

- `6867078` is the first commit that changes code and only moves: the 177 lines it removes from
  `process-audit/audit_count.py` and the 193 lines of the new `process-audit/record_items.py` differ, as
  multisets of non-blank lines, only by the new module's docstring and its imports; `audit_count.py`
  gains only the import of the nine names it uses; no other script imports a moved name from
  `audit_count` (search of the head). The process-audit tests pass on that commit (below). WAY-365 met.
- Sizes (`python -B task-cycle/change_file_sizes.py <base> <head>` in the reviewed worktree, exit 0):
  `process-audit/audit_count.py` 3310 → 3143, `process-audit/record_items.py` new, 243;
  `process-audit/test_record_items.py` new, 246; `process-audit/test_audit_count.py` 4224 → 4289.
- The test of `function-and-file-size` with its `expectedFailure` mark taken off, in my worktrees of
  the base and the head: both name 11 functions over 80 lines and 2 files over 1000; the only
  difference is `process-audit/audit_count.py` 3310 → 3143. The change pushed nothing over a threshold.
  `19f7003` adds to `audit_count.py` only docstring lines, after the move, with the file smaller than
  before. No code is left without a user; `reads_none_first` lives in `record_items.py` and is used by
  `audit_count.py` (`read_plan`, `read_too_large`).

## Tests

- Against `guidelines/testing.md`: unit tests at the lowest level for the reading
  (`test_record_items.py`), command-level tests for the cells and the series; inputs and expected
  values written out; the one reason written out in the test, not imported (`test_record_items.py:14`).
- Changed and deleted tests: the six named in the author's report go with the denial detection that
  *To do* 6 and question 5 remove (cause on the side of the requirement, the task as evidence);
  `test_the_crafted_discarded_attempts_break_no_cell_and_no_pattern` keeps its base assertions
  (`assertIn(answer, ("yes", None))` was the base's form too) on new inputs. Not weakened.
- The 100,000-entry test catches the quadratic reading only by time, as the author says; the
  guidelines give no time limit. Not a finding.
- The author's own-work check (*To do* 5 over the archive) fits a weak point and would catch an
  unmarked old entry read as `no`; it does not reach I-1, which the author raised separately.

## Declined to judge

- The field label `Discarded attempt` in *Unknown values* for a Q1 reason that concerns *Review
  rounds* (author's choice 6): the convention predates the change and the task does not touch it.
- `task-cycle/skill/request_template.md:441` ("the number of review rounds") may now be read as
  counting entries of reviews that passed: the request's figure is outside the task.
- `process-audit/record_items.py` stands in no table of a kind of the coding guidelines (it is a
  `shared-module`, whose file applies to `relation-model` only); three other modules stand in none
  either (`elements/common/compare_log_entries.py`, `decision_index.py`, `foundation_source.py`), and
  a change of the guidelines is outside the task.

## Checks run

- `python -B gate/run_tests.py process-audit`, worktree of the head — exit 0, 257 tests.
- `python -B gate/run_tests.py task-cycle`, worktree of the head — exit 0, 534 tests, 1 skipped.
- `python -B gate/run_tests.py elements/part-map`, worktree of the head — exit 0, 40 tests.
- `python -B gate/run_tests.py process-audit`, worktree of `6867078` (the move) — exit 0, 234 tests.
- `python -B elements/common/foundation_check.py`, worktree of the head — exit 0, `0 errors`.
- `python -B task-cycle/change_file_sizes.py aba5ee92a0734c2e775cc69662af669bf6455795 ab2c8c801b2ba9170a00ed6056b8b7c56b062868`,
  reviewed worktree — exit 0 (it left the worktree clean).
- `agent-instructions/test_size_invariant.py` class `Size` with `expectedFailure` removed, worktrees of
  the base and of the head — exit 1 in both (the failure the invariant's mark expects), same list but
  for `audit_count.py` 3310 → 3143.
- Ruff, the pinned `ruff.exe` of the main checkout's `.runs/quality-venv`, `check --config ruff.toml
  --no-cache --ignore-noqa process-audit` — exit 1 at the head with 4 reports (`UP037` at
  `audit_count.py` 2126, 2339, 2413; `F541` at `test_audit_count.py` 2424), exit 1 at the base with 5;
  none on a line the change wrote.
- Manual: the multiset comparison of the moved lines (script of mine); the crafted-input probe and the
  read of the 103 archived records (scripts of mine) — results above.
- `python -B elements/common/decision_index.py --output <my dir>/index.md` with the sections *Process
  audit*, *Review of a change*, *Scripts and the gate*, *The-way's own coding and testing guidelines*,
  *Coding guidelines*, the parts `process-audit`, `task-cycle`, `decisions`, `part-map`, and the
  decisions WAY-337, 339, 135, 263, 344, 33, 229, 260, 162, 294, 150, 161 — exit 0 (59 listed in full,
  111 by heading).
- Not run: the product's full gate, by the handoff (WAY-160).

## Reaches beyond the dispatch

- `foundations/invariants.md`: `audit-count-refuses-record-links`, `audit-series-script-paths`,
  `script-imports`, `cross-part-imports`, `script-language`, `test-method-citation` — for the new
  module at a trust boundary and its imports.
- `guidelines/coding-shared-module.md` (whole) — the new file is a module another script imports.
- `elements/decisions/template.md`, lines on *Relations* — to judge the relations of WAY-403/404.
- `elements/part-map/template.md`, section *Trust boundary* — for the part map line.
- `task-cycle/skill/correction.md:30-53` — for the second discarded attempt (M-1).
- `task-cycle/remarks_check.py` (`MARKER`, `split_lines`, `indent_of`, `fenced_flags`, `reads_none`) —
  what the reading relies on.

## Working copies

Under `.runs/review-whole/`: three
worktrees (`base` at `aba5ee9`, `head` at `ab2c8c8`, `move` at `6867078`), my scripts, the decision
index and the outputs of the runs. Each worktree was removed with `git worktree remove --force`
(exit 0 for all three), then `git worktree prune`, and the directory `.runs/review-whole/` was
deleted; `git worktree list` names none of them and the reviewed worktree is clean. Nothing of them is
kept in `reports/`: the evidence the report needs stands in it. No remainder.

## Unread material

- Decisions of my index read whole: 21 — WAY-403, 404, 337, 339, 135, 263, 344, 365, 385, 363, 48,
  161, 162, 294, 260, 229, 30, 164, 394, 136, 269. The other 38 listed in full I read by their binding
  sentences in the index; the 111 listed by heading I ran through by question and opened the six above
  whose question bore on the change (WAY-365, 48, 30, 164, 136, 269).
- Bearing on the change and not read: WAY-314 and WAY-315 (which act of the human consents to a change
  of a decision, and from when it binds) — they bear on the route of the fix of I-1, for which I relied
  on WAY-30; WAY-14 (who accepts a decision), likewise; WAY-19 (numbering), whose check
  `foundation_check.py` passed.
- Invariants of `task-cycle` and `every` not read whole: `record-copy-image-check`,
  `record-copy-image-files`, `blocked-request-wording`, `blocked-request-label`, `review-tag-pattern`,
  `cycle-*`, `gate-times-*`, `command-runner-passes-exit-code`, `repository-changer-acts-only-when-told`
  and the `every` invariants other than those named under reaches; their tests pass in the runs above.
- Glossary entries: not read beyond a search for "settlement" and "marker".
- Guideline files: all of the selection read whole (`guidelines/coding.md`,
  `guidelines/coding-measuring-report.md`, `guidelines/testing.md`, `product-guidelines/reading.md`,
  `guidelines/coding-shared-module.md`); `guidelines/coding-check.md` not read, as the change adds or
  changes no check.
- `process-audit/audit_count.py` and `process-audit/test_audit_count.py`: read where the change reaches
  them and their callers, not whole.

## Searches not found or unclear

- WAY-344 names no form of `cycle.md` as an earlier form and no item of it as a field read so; whether
  the reading of a missing item as `unknown` with exit 0 predates the rule or was ever weighed against
  it I could not find in the foundation (the audit clause of WAY-344 entered after the reading of
  *Review rounds* and *Discarded attempt*, 2026-11-11).
- The template and the skill give no form for a second discarded attempt in one cycle (M-1).
- The glossary holds no entry for "settlement" or "contradiction with the settlements", which the head's
  review method and WAY-403 use as a defined phrase; WAY-403 spells out its three sources, so I found no
  sentence a reader would read wrongly.
