# Findings for the fix — Minor findings of the review of the whole change within the task

Source: `reports/review-whole-report.md`, first line `PASS 18b4a3fb99df3d95e939d1c348fe84f2bc50e0c0`.
No blocking finding. The three Minor findings below are cut from the report in the reviewer's words;
they are the ones the reviewer lists and has not marked outside the task's scope. (Minor 4 of the
report is outside the task's scope and is not fixed: it goes to the request's list.)

1. **Stale count of tables in the template** (within the task). `process-audit/problem_register.md:39`
   still reads "Text outside the four tables is not read; write there what you like." The same file
   now says five tables six lines above (line 29: "reads the five tables below"). A user who adapts
   the template reads two counts in one section and may take the new table *Costs of an occurrence*
   for text outside the tables. Evidence: `grep -n "four tables" process-audit/problem_register.md`
   gives line 39 only. Fix: "five tables".

2. **A test whose name claims more than it checks** (within the task).
   `process-audit/test_audit_count.py`, `test_a_column_in_another_order_or_an_extra_one_is_refused_not_missing`
   (the test just after `test_every_field_missing_from_the_register_is_named_in_one_error`): it builds
   only the extra-column header (`| Issue | Note |`); no case puts the columns of *Problems* in
   another order. The behaviour is right (my scratch run `col_swapped`, Cost and Weight swapped:
   exit 1, table refused, result written, stderr `... does not have the header row the template
   gives`), but a change that turned a reordered header into exit 2 would pass this test. The test
   exists to guard exactly the line "no field is missing, so the table is refused". Add a reordered
   case to it, or rename it.

3. **Reflow damage in the edited WAY-330** (within the task). `foundations/decisions.md`, *Rationale*
   and *Rejected* of WAY-330 (about lines 10968-10985 at the head): after the in-place edit three lines
   run to 123, 109 and 110 characters ("cycles itself would repeat it every week, and could repeat it
   differently. A template lets another user of the-way keep the", "problem to its fix would have to
   be rebuilt each time; the-way taking over the review of the remarks of cycles") where the rest of the
   log wraps at about 100. Cosmetic only; the words are right. Evidence: `awk '{print length}'` on
   lines 10960-10972 and the diff of `18b4a3f`.
