# Findings to fix — Minor findings of the review of the whole change (within the task)

Cut word for word from `review_whole_report.md` (first line `PASS afa43439b39b66fc1e737897b0c6b8b0e11aa129`). No blocking findings. Fix range runs from head `afa43439b39b66fc1e737897b0c6b8b0e11aa129`.

1. **"Closed on the way" is defined only in the template, not in the entry that binds it.**
   Place: `task-cycle/skill/request_template.md:240-248` against `foundations/decisions.md:9053-9059`
   (WAY-287's binding sentence, "and the gap was not closed on the way") and `:10552-10580` (WAY-325).
   What is wrong: the template narrows "closed" to "the reviewer or a fresh one reading what stayed
   unread"; WAY-287 says only "closed on the way", and WAY-325 gives the orchestrator a third way, an
   autonomous choice that the gap bears on nothing. A reader of the entries alone cannot tell whether
   that choice closes the gap for the request. Why it matters: a later reviewer comparing the template
   with the entries (WAY-263) or an orchestrator reading WAY-287 may put the item in or leave it out
   either way. Evidence: the three texts above. Suggested fix: one clause in WAY-287 saying a gap is
   closed on the way when the reviewer, or a fresh one, read what stayed unread.

2. **A title-screened decision is not said to be "no gap" where the orchestrator's rule is stated.**
   Place: `task-cycle/skill/SKILL.md:200-203` and `foundations/decisions.md:10552-10557` (WAY-325),
   `:10584-10590` (WAY-326), against `task-cycle/review/SKILL.md:149-154`. What is wrong: WAY-325 fires
   on a report that says something "stayed unread or was read in part"; the whole-change reviewer's
   section always opens with counts such as "40 whole, 111 by title only". Only the review method
   says what the section lists (decisions not run through, bearing decisions unread, guideline files),
   i.e. that a decision read by title is the practice and not a gap. WAY-287's rationale says so
   (`:9092-9099`), but WAY-325/326 and the orchestrator's sentence do not. Why it matters: an
   orchestrator reading the counts as "read in part" must decide (resume, carry, or record a choice) at
   every whole-change review, which is the cost the task set out to avoid. Evidence: the quoted places.
   Suggested fix: one clause in WAY-326 (or in the `SKILL.md` sentence) that a decision read by title
   under WAY-150 is no gap.

3. **The exception for a report returning `questions` was extended to the new section without being
   in the entry.**
   Place: `task-cycle/skill/SKILL.md:209-213` ("A report that lacks its **Unread material** (WAY-326) or
   its **Searches not found or unclear** (WAY-260), save one returning `questions`...") against
   `foundations/decisions.md:10586-10592` (WAY-326: "a report without it returns to its agent for
   repair"). What is wrong: the skill states the repair rule with a qualification the entry does not
   have. The same difference already holds between this sentence and WAY-260, so the author followed
   the existing shape, and the effect is benign (a `questions` report is resumed anyway), which is why
   it is Minor and not a WAY-263 Important; but the author's report does not name it as a choice.
   Suggested fix: say in WAY-326 that a report returning `questions` is not returned for the section, or
   drop the exception for the new section.

4. **Reverse order leaks an Unread line into the process remarks; the tests cover only the prescribed
   order.**
   Place: `task-cycle/remarks_check.py:16-23` (end of a bold-label section) and
   `task-cycle/test_remarks_check.py:143-165` (the two new tests). What is wrong: when a report writes
   **Searches not found or unclear** as a bold label outside a list and then **Unread material** as a
   list item (not as bold text starting a paragraph), the Unread line is read as an item of Searches.
   Reproduced (scratch run, `remarks_check.section_items`): `**Searches...:**\n\n- item one\n\n-
   **Unread material:** the file` gives `['item one', '**Unread material:** the file']`; the same with
   a `none` bold label followed by the Unread bullet gives `['**Unread material:** the file']`. The
   forms with Unread first, with a heading, with a bold label (not a list item) after Searches, and with
   the Searches label as a list item are all read correctly. Why it matters: WAY-326's *Verification*
   calls the gap standing among WAY-260's items a violation; the leak is limited to a report that breaks
   the order the methods give, so the author's recommendation (leave it, let a real listing decide) is
   reasonable. Suggested: add a test that records the reverse-order behaviour, or end the section at a
   bold label named `Unread material` as the author proposes.

5. **Long unwrapped lines and one clumsy sentence left by the edits.**
   Place: `foundations/decisions.md:4226` (159 characters; WAY-150, the sentence that joins "of the
   cycle reads what its handoff names and reaches for what is missing selectively — a search for an
   identifier or a word and a read of the passage found,"), `foundations/decisions.md:9059` (135
   characters, WAY-287), `task-cycle/skill/SKILL.md:213` (151 characters, "section is not. An agent
   that returns `questions` gets your answers as step 6 answers the designer's — ..."), and
   `elements/common/way_of_working.md:82-83` ("Read each decision found whole, save as the reviewer of
   the whole change reads them below, as the range of lines from its heading..." reads awkwardly: two
   "as" clauses). The files are wrapped near 100 characters elsewhere. Evidence: `awk 'length>100'` on
   the added lines; no test checks line length. Suggested: re-wrap the three lines and split the
   way_of_working sentence.
