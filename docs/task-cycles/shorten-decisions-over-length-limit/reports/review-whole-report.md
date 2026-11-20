PASS ef8aa061051d3dbaf8dbc105465057833273a542

# Review of the whole change — shorten-decisions-over-length-limit

Range: `bafe3904a80f3f74e6a722dc3d8dc8be1ed882cc..ef8aa061` (two commits, `2f31b30f` and `ef8aa061`),
route "one author without a plan". `git rev-parse HEAD` = `ef8aa061051d3dbaf8dbc105465057833273a542`,
as dispatched. No plan, so no slice is named for any finding.

## Findings

### Critical

none

### Important

none

### Minor

1. **`elements/decisions/template.md:210-213` — the template's "Changing a decision" still states WAY-19
   with the old name of the part (outside the task).** The bullet reads "A part of the question an
   existing entry answers is a sentence of that entry, in a paragraph of its own as "Binding
   sentences" gives, where it cannot change without changing that entry … (WAY-19)". After this
   change WAY-19 (`foundations/decisions.md:879-886`) names the two kinds: "a part of another question
   that an existing entry answers, or a part of its own question that it sets apart". The template
   points to "Binding sentences", which tells the two kinds apart, so a reader is not misled about
   what to do, and in effect the two texts agree: the next sentence of WAY-19, "A new answer to a
   question the log holds rewrites that question's entry", covers a part of the entry's own question
   that is not set apart. But the template still uses the name that PR #152, "Fix or let through"
   1(a), called unclear. The decision skill reads the template whole, so it keeps that wording in
   front of agents. **Outside the task:** the task's *Out of scope* gives the decision template's
   rules to #152 and lets this task touch the template only for To do 13. A later change could
   repeat WAY-19's two kinds in this bullet. (The author observed the same.)

2. **`process-audit/test_audit_count.py:2036` — the docstring of `StagesForms` cites "the settlement 6
   of the task" (outside the task).** This is the task document of an earlier cycle. A reader of the
   repository cannot open it, and the number of the decision beside it now does the citing alone.
   The change only replaced `WAY-344` with `WAY-416` on that line, and the citation was already
   there at the base. Outside the task. The cost is one phrase removed in a later change.

3. **`foundations/decisions.md:1669-1670, 3410-3411, 4478-4480, 5466-5468, 5653-5655, 5669-5671,
   6227-6229, 6329-6330, 7689-7691, 7854-7856, 8596-8598, 8822-8824` — the raw text of the new
   paragraph breaks is not rewrapped (within the task).** The ten entries were split by inserting a
   blank line inside an existing line. This leaves short lines such as "Of the" (1672), "Where"
   (8824) and "Agent turns, questions" (5671). The two lines of WAY-287 at 7689 and 7691 run past
   100 columns, while the log wraps at 100 elsewhere. Rendered Markdown is unaffected, and the narrow
   diff makes the word-for-word check easy, which the author chose on purpose. The only consequence
   is a ragged raw file for the next editor. Polish only.

### Considered, no finding

- **WAY-416's sentence of precedence ("For the command that counts the audit this decision prevails
  over WAY-344 …") is held by no test and carries no pair of examples.** The author raised this.
  WAY-12 is met, because the decision is held by 21 `decision:` lines on its other sentences, and
  the check reports no error. The template makes a pair optional. The task's settlement on the
  violating example says that the new decision "nie potrzebuje [przykładu], bo trzymają ją testy". A
  test cannot assert precedence apart from the cases themselves. No finding.
- **The `decision:` lines `WAY-344 "Each reading of a file that the rule covers has one test"` at the
  count's tests of the cycle's record (`process-audit/test_audit_count.py:5012`,
  `process-audit/test_record_items.py:514,680,762`).** These tests exercise behaviour that WAY-416's
  sentence on the cycle's record now gives. The sentence they quote, however, is WAY-344's sentence
  that requires one test per reading. That sentence stayed in WAY-344, and nothing in WAY-416
  overrides it ("in every other case WAY-344 binds that command"). The moved sentence is held
  separately at `test_audit_count.py:475`. To do 7 and 8 are met. No finding.
- **WAY-19's new wording and a part of the entry's own question that the entry does not set apart.**
  Read alone, the excepting clause no longer names such a part. The next binding sentence ("A new
  answer to a question the log holds rewrites that question's entry") still keeps it in the entry,
  so what WAY-19 binds is unchanged, as To do 10 requires. No finding.

## Coverage of the task

- **To do 1** — met. My own word-for-word comparison (see Checks) gives no difference in the joined
  binding sentences of WAY-256, 148, 339, 289, 405, 136, 154, 139 and 134. In each, the new
  paragraph starts at the sentence the table names.
- **To do 2** — met: the only difference in WAY-150 is `first` → `second`
  (`foundations/decisions.md:1695`). The second paragraph is now "Of the decisions it finds by
  *Scope* …", the paragraph that holds the rule on opening whole.
- **To do 3, 4** — met. WAY-344 keeps the first sentence, the second sentence up to "… with exit code
  1", the sentence on a copy of a file at the base, and the sentence on one test per reading. The
  second sentence now ends "and except that the command that counts the audit is bound by WAY-416 in
  the cases that decision gives, where it prevails over this decision." WAY-416 holds the rest of the
  second sentence, now opening "The command that counts the audit, in a file of a cycle's record …"
  (only "and except that" dropped and "the" capitalised). It also holds the sentences on the table
  of weights, the cache-write columns, the cycle's record and the key `repository`, all word for
  word. The only words added are the sentence of precedence in WAY-416 and the words after "WAY-416"
  in WAY-344. WAY-416's *Scope* is `process-audit, task-cycle`, *Relations* is `narrows WAY-344`, and
  the entry stands at the end of "Process audit" (`foundations/decisions.md:8869`). The number is the
  next free one: the log and `origin/foundations` (= base) hold up to WAY-415. Paragraphs:
  WAY-344 210 + 131 words (2 + 2 sentences); WAY-416 257 + 195 words (3 + 3 sentences).
- **To do 5** — met, checked clause by clause against the diff. *Verification*: of the nine clauses
  of the base, clauses 1 and 8 are in WAY-344 and 2–7 and 9 are in WAY-416. The pair of examples
  stays whole in WAY-344, the violating example on "neither a check of form nor the count of the
  audit" unchanged, as settled. *Rationale*: 13 sentences of the base. Sentence 3 is cut at ", and
  apart from the count of the audit": the first part stays in WAY-344, and the second part in
  WAY-416 opens with "Exit code 2 says the file was not read, apart from the count of the audit,"
  and reads as a sentence. Sentence 7 is cut at its clauses: the clause on the stage report goes to
  WAY-416 under the head "The price:" and reads as a sentence. Sentences 4, 5 and 9–12 are in
  WAY-416; 1, 2, 6, 8 and 13 are in WAY-344. *Rejected*: 16 ways. Ways 1–8 and 14–16 are in WAY-344,
  9–13 are in WAY-416, and none is in both or dropped.
- **To do 6** — met. WAY-287's first sentence ends "… the foundation entries the human did not see at
  the task document." The second begins "The section stands in three groups, headed …". The
  paragraphs are 218 / 185 / 27 words, and the only words that differ are `document —` →
  `document. The section stands`.
- **To do 7** — met. `foundation_check.py` accepts every quotation. Of the 19 base lines quoting "The
  rule binds a script that a change adds and, in a script", 13 lines at tests of the count now quote
  WAY-416 "The command that counts the audit, in a file of a cycle's record". I checked each test
  name against that sentence: the earlier forms, the files of measures and gate times, the changed
  tool, and the missing columns. The remaining 6 are at tests of transcripts and generators (exit
  code 2) and stay on WAY-344. The quotations of the other moved sentences (2 + 3 + 1 + 2) moved to
  WAY-416.
- **To do 8** — met. `git grep WAY-344` over the whole tree outside `docs/task-cycles/` leaves
  references only to WAY-344's general rule, to a copy of a file at the base, or to the test per
  reading. Examples: the register's missing heading, table or column ends with exit code 2
  (`audit_count.py:274`, `problem_register.py:218,297`, `problem_register.md:34`,
  `test_audit_count.py:3195`). Also the guidelines, WAY-294, WAY-339 *Rejected* and WAY-388.
  `audit_count.py:268` now cites both decisions, each for its own half of the sentence. The comments
  and docstrings on the count's own way to end (`record_reading.py`, `audit_count.py:213,702,841`,
  `problem_register.py:203`, `process-audit/SKILL.md:188,191`) now name WAY-416.
- **To do 9** — not checkable on the range. The request's description is written later by the
  orchestrator. The author's report holds the map of *Verification*, *Rationale* and *Rejected* that
  the description needs, and I checked that map against the diff (To do 5).
- **To do 10** — met. WAY-19 (`foundations/decisions.md:881-883`) uses WAY-05's own words for both
  kinds of part and says nothing of paragraphs, so it cannot contradict WAY-05 on them. Its binding
  meaning stays (see "Considered, no finding").
- **To do 11** — met. WAY-391's *Scope* is `relation-model, process-audit, task-cycle,
  elements-common`, the same parts as *Applies to* of `guidelines/coding-shared-module.md`, as for
  WAY-386–390 and their guidelines (checked for all six).
- **To do 12** — met (`agent-instructions/README.md:17-18`, "for these two reports alone"). The
  paragraph was rewrapped and nothing else changed in it.
- **To do 13** — met (`elements/decisions/template.md:37`). The limit now stands on its own line in
  parentheses after the blocks of paragraphs, outside the "optionally" block. The author used
  parentheses rather than angle brackets because the angle-bracket lines of the form are
  paragraphs. That choice is sound.
- **Acceptance criteria** — all three met. `foundation_check.py` exits 0 with `0 errors` and prints no
  `listed:` line. No entry is over 600 words: the largest are WAY-150 592, WAY-134 583, WAY-339 488,
  WAY-416 452. The joined binding sentences of the ten entries match the base except one word in
  WAY-150.
- **Row 1 of *Settlements to record*** — met by WAY-416.
  - **Fidelity and mark.** The binding sentences are the moved sentences of WAY-344 plus the sentence
    of precedence. The task's *Decisions in play* gives that sentence's content ("poza tymi
    przypadkami komendę dalej wiąże reguła ogólna WAY-344"), and To do 4 and WAY-25 require it.
  - The *Rejected* adds exactly the two "Not chosen" ways of "Co zrobić z WAY-344", as *Decisions in
    play* orders, worded faithfully without the figures.
  - The one sentence the writer added to *Rationale* restates the source's reason ("to ten wpis
    rośnie z każdą zmianą komendy audytu"). Its last clause ("leaves the general rule of WAY-344 as
    it is") is a direct consequence of that reason, not a new meaning.
  - No pair of examples and no field was added beyond the row. I judge that nothing the writer added
    goes beyond the row and the task the human accepted, so the mark `row 1` stands and the entry is
    not `the cycle's`.

## Structure of the code the change leaves

`python -B task-cycle/change_file_sizes.py bafe3904 ef8aa061` shows that no Python file changed its
line count (`audit_count.py` 871 → 871, `record_reading.py` 1052 → 1052, `problem_register.py`
358 → 358, `test_audit_count.py` 5729 → 5729). Every Python change replaces one comment, docstring or
`decision:` line with another. No function grew, so I did not run the test of the size invariant
(`agent-instructions/test_size_invariant.py`) on base and head: its result cannot differ. No code
lost its user, and no name stopped being true. The gap the cycle carried was that the author did not
read the coding and testing guidelines whole. Judged by the diff, it does not matter: no rule of
`guidelines/coding.md` or `guidelines/testing.md` reaches a change of comments only. The one added
line over 100 columns (`test_audit_count.py:475`, 103 columns) is a comment of the same length as the
line it replaced. The formatter does not reflow comments, and no blocking linter rule counts line
length.

## Declined to judge

none

## Checks run

- `git rev-parse HEAD` — `ef8aa061051d3dbaf8dbc105465057833273a542`, exit 0.
- `python -B elements/common/foundation_check.py` (reviewed worktree) — exit 0, `0 errors`, no line
  `listed:`.
- `python -B task-cycle/change_file_sizes.py bafe3904 ef8aa061` — exit 0 (table above).
- `python -B gate/run_tests.py process-audit` — exit 0 (277 tests, OK).
- `python -B gate/run_tests.py elements/common` — exit 0.
- `python -B gate/run_tests.py agent-instructions` — exit 0.
- `python -B .runs/review-whole/cmp.py` (my own script) — exit 0. It reads `foundations/decisions.md` at
  the base and at HEAD, takes each entry's binding sentences (from the heading to the first field)
  and compares the words with difflib. Results:
  - the ten entries are identical except `first` → `second` in WAY-150;
  - paragraphs and totals of every entry are as given above, and no entry anywhere in the log is
    over 3 sentences or 300 words a paragraph, or 600 in all;
  - WAY-344 + WAY-416 against the base WAY-344 differ only by the added words named under To do 3–4;
  - WAY-287 differs only at the cut.
- `python -B elements/common/decision_index.py --sections` and the index of my selection (below) —
  exit 0.
- `git grep -n "WAY-344" HEAD` / `git grep "decision: WAY-344" bafe3904` / `git grep "decision: WAY-416"
  HEAD` outside `docs/task-cycles/` — counts of quotations before and after (To do 7).
- `gh pr view 152` — read "Fix or let through" 1 (a)–(e), the source of To do 10–13.
- Manual: read the whole diff of the range, WAY-344 and WAY-416 whole at HEAD, and the passages around
  each remaining reference to WAY-344.
- Not run: the full gate (WAY-160, the orchestrator's/CI's); `ruff check` / `ruff format --check`
  (ruff is not installed in this environment: `python -m ruff` reports no module); the size
  invariant test (no function or file grew, see above); `task-cycle` tests (the change touches no
  file of `task-cycle/`; the author ran them, exit 0).

## Reaches beyond the dispatch

- PR #152 description ("Fix or let through" 1), via `gh pr view 152`, to read the source of To do
  10–13.
- `guidelines/coding-measuring-report.md:30-36` and the *Applies to* lines of every
  `guidelines/coding-*.md`, to judge the reference to WAY-344 there and To do 11.
- `process-audit/test_record_items.py:505-770` and `process-audit/test_audit_count.py:3188-3200,
  5000-5015`, and `process-audit/audit_count.py:258-280`, `process-audit/problem_register.py:212-224,
  290-300`, `process-audit/problem_register.md:30-36`, `foundations/decisions.md:8712-8720` (WAY-339
  *Rejected*): the passages around the references to WAY-344 that remain.

## Working copies

`.runs/review-whole/` of the worktree held my script `cmp.py` and its output, the index of the
selection, the list of sections, the diff of the log and the logs of the three test runs. All were
removed after the report was written; the directory is left empty.

## Unread material

- **Decisions of the index of my selection read whole: 8 of 38 listed in full** (WAY-05, WAY-12,
  WAY-18, WAY-19, WAY-25, WAY-344, WAY-391, WAY-416).
  - **How I selected.** Sections "Decision entries and the decision log", "Scripts and the gate" and
    "Process audit". The parts `decisions`, `agent-instructions`, `process-audit`, `task-cycle`,
    `elements-common` and `relation-model`. The decisions of *Decisions in play* and the twelve
    changed entries. WAY-344's *Scope* names every part. I did not take that as touching every part:
    the change's files lie in the parts above.
  - **Questions run through.** I ran through all 139 decisions listed by heading. Those whose question
    bears on the change (WAY-07, WAY-14, WAY-263, WAY-294, WAY-386–390) I judged from what I read of
    them: the *Scope* lines of WAY-386–390, and WAY-294's link to WAY-344 through the grep hits.
- **Decisions that bear on the change and were not read whole:**
  - The ten entries of the table (WAY-256, 148, 339, 289, 150, 405, 136, 154, 139, 134): I read their
    binding sentences in the index and in the diff, not their fields, *Rationale* and *Rejected*. The
    change adds only a blank line inside their binding sentences, and the diff proves nothing else in
    them changed.
  - WAY-287: binding sentences, fields and the start of *Rationale*; the rest unread, for the same
    reason (only the cut changed).
  - WAY-02, WAY-30, WAY-114: binding sentences in the index only; they are unchanged and quoted in
    *Decisions in play*.
- **Guideline files:** `guidelines/coding.md` and `guidelines/testing.md` read whole.
  `guidelines/coding-shared-module.md`, `coding-generator.md` and `coding-measuring-report.md`: only
  their headers and the passages named above. No kind's *When to read* matches a change of comments
  only.
- **Other:** `elements/common/foundation_check.py` was not read beyond its imports, limits and
  `excess()`. Its result is used as evidence, and my own comparison confirms it independently.

## Searches not found or unclear

- `ruff`: not found in the environment (see Checks).
- The source of "the settlement 6 of the task" at `process-audit/test_audit_count.py:2036` (an
  earlier cycle's task document) is not in the repository; not looked for further (Minor 2).
