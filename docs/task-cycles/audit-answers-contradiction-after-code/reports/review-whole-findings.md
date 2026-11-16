# Findings of the review of the whole change, for the fix

Cut word for word from `reports/review-whole-report.md` (head `ab2c8c801b2ba9170a00ed6056b8b7c56b062868`): the blocking finding, then the Minor findings within the task (WAY-161). The blocking finding carries the reviewer's mark of contradiction.

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
