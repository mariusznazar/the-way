# Findings for the fix — Minor findings of the whole-change review within the task

Source: `reports/review-whole-report.md` (PASS 038a330); cut word for word. No blocking finding. Minor 5 and 6 concern the text of the request, which the orchestrator writes; for them answer in your fix report that no code changes, or what you changed if you hold otherwise.

### Minor 1 — `foundations/decisions.md:7646–7647` and `:7685–7687` (WAY-256 *Rationale* and *Rejected*): the "five to fifteen percent more words" figure is an estimate of a layout nobody built, stated without what was measured

Within the task. The *Rationale* says "estimated from the files of one skill, that shape reads five to fifteen
percent more words in a typical session than keeping its steps in `SKILL.md`", and *Rejected* repeats "an
estimated five to fifteen percent more words read in a typical session". WAY-05 lets a rationale hold "a
measurement the choice rests on ... with what was measured and under which conditions". The figure is the
task's own estimate for the full shape of `lead-project` (task question 3, "pełny kształt ... +5 do +15%");
the full shape was not built, so nothing was measured, and the entry names neither the skill nor what was
counted (files of the skill, words). "Typical session" is a condition, so this is not the case WAY-05's
*violates* example gives (a bound with no conditions); the entry is not wrong, only thin. The author's report
(choice 7) already says the reviewer may want it out.

Evidence: WAY-05 text; the author's measured result for the chosen shape (skill text -3.8% to -21.1% on the six
roads, files together +277 words) does not test the unbuilt shape. A reading that stays within WAY-05: say it is
an estimate made before the rebuild, from the word counts of the files of `lead-project`, or drop the figure
from one of the two places. Not blocking: the figure comes from row 1's source and is labelled "estimated".

### Minor 2 — `project-level/lead/skill/SKILL.md:176–181` (step 5 pointer): the road "recovery of a pending gate or recheck in step 0" does not say whether `route_changes.md` is read

Within the task. The first sentence sends to `route_changes.md` "from a refiner's result `plan change` or from
a changed definition in step 0"; the second sends to `definition_change.md` for a change of the definition, its
gate or the plan recheck, "a gate or recheck found pending in step 0 included". A pending gate found at the
start is not obviously "a changed definition", so the first sentence may or may not apply. In the base the agent
read the whole of step 5 on this road. What `route_changes.md` bullet 1 holds that the recheck also needs: "Stop
your shared-plan writes until it returns ... Human questions and required critique requests return through the
file, for you to dispatch/present and record. Read its result and rerun the whole-plan check before resuming
state updates or affected refinement" (the recheck of `definition_change.md` bullet 3 dispatches the same kind
of `plan-project` agent). `definition_change.md` bullet 3 keeps "serialized shared-plan ownership", "readiness
writes blocked" and "logged corrections", and step 1 (`SKILL.md:73–75`) keeps "Run `plan_check.py` after plan
changes", so what can be lost is narrow: the rule that questions and critique requests of that agent come back
through the file, and the explicit rerun of the whole-plan check before resuming. Fix: either word the first
sentence to include the pending gate or recheck of step 0, or repeat nothing and let the second sentence say
"read `route_changes.md` too". Evidence: reading of the stub against base lines 190–219 (`git show a3206c1:project-level/lead/skill/SKILL.md`).

### Minor 3 — `project-level/lead/skill/definition_change.md:23`: "this route" has no antecedent in the new file

Within the task. The moved sentence "A check passing the old fingerprint or approval alone does not complete this
route" stood under the step heading "Route plan and definition changes"; the new file's heading is "Change of
the definition and its gate", and `route_changes.md` (the other half of that old heading) is a separate file.
The reading is easy (the route of the definition change), but the criterion asks for each demonstrative of a
moved sentence to be read alone and the author's own-work check (section 9 of the report) lists "its", "it",
"either mismatch", "the file" and "Left in place", not "this route". Meaning is not lost. Fix: "does not complete
this change" or "does not complete the recheck".

### Minor 4 — `foundations/decisions.md:7601, 7659, 7662, 7688, 7691, 7692, 7696`: the "reflow" commit left seven lines of the WAY-256 entry over 100 columns

Within the task. `038a330` is described as a reflow of the rationale and rejected ways; a word-level diff of
`e98f46b` against `038a330` (`git diff -w --word-diff=porcelain`) shows only line breaks moved, as claimed, but
`awk 'length($0)>101'` still finds seven long lines in the entry (103, 102, 119, 102, 103, 109, 123 characters);
the rest of the entry and the log wrap at 100. Cosmetic: noisy diff for the next editor.

### Minor 5 — the request's word-count columns "with the step-0 files" mix two bases

Within the task (acceptance criterion on the numbers). The "before" column uses 9833 (7253 of the side files at
`a3206c1` plus 2580), the "after" column 7255 of side files at the head, because `conversation_template.md`
grew by two words between `a3206c1` and `57795e4`. So "-96 (-1.0%)" on road 1 is the real -98 of the skill text
plus the two words of an unrelated merge. The author's report discloses it (section 5, last list). The request
should say so beside the table or give the side files at one commit in both columns; the skill-text columns are
exact and unaffected.

### Minor 6 — `project-level/lead/skill/technology_run.md:3`, `task_return.md:3–4`: two opening lines are given "no exclusion" or an exclusion that is the pointer itself

Within the task. The criterion asks the author to name what each new sentence excludes. For `technology_run.md`
the report says "nothing but orientation"; for `task_return.md` it says the line excludes "the transitions that
step 1 supports from evidence", which the condition of the same line ("when the human has said that the blocked
request of a task is closed") does. Both sentences are harmless (they restate the condition of the pointer in
`SKILL.md` and add no road; I compared them with the pointers: same conditions), so this is a matter of the
request giving the honest entry for each: "restates the pointer's condition, adds none".
