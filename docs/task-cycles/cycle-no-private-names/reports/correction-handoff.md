# Handoff — a correction for the human's remarks

You are the one author, resumed, making a correction after the human's decision on the open request.
Method: `task-cycle/change/SKILL.md`, variant **"a correction for the human's remarks"**; its
`fix.md` does not apply (no findings file). Same worktree and branch:
`.`, `task/cycle-no-private-names`.
Commit on the branch, do not push, do not run the full gate. The branch head is `acbcb15`; the
code is as at `4deb195` (the two commits after it only added and removed the record copy under
`docs/task-cycles/`, which is not yours to touch). Your correction's range starts at `acbcb15`.

## The human's remark (binds)

The request blocked on the finding N1 of the review of your fix (`reports/whole-review-2-report.md`,
"New findings in the fix diff", N1). The orchestrator put the finding to the human with two ways out
and recommended the first; the human answered, in his words: "Poprawimy zatem tak jak proponujesz"
("Let's fix it as you propose"). The first way, as the human was shown it: *rewrite such a line like
any other, so that nothing private is ever published, and the plan reader may then report a conflict
you can see.* The other way (keep the exception, write it into both decisions, stop before the
commit) is **not** chosen.

So, drop the exception. A `Task relation:` line of the record or a `Project relation:` line of the
task copy that the check of private paths lists is cleaned like any other line; nothing the check
lists is committed. The lines still stay as they are when the check does not list them (their form
names the plan by its file name, so they are not expected to hold a path), because the plan-state
reader reads them. A cleaned relation line can make the reader report a conflict with exit 1 (your
test 3 in `project-level/test_plan_state.py` pins it); say so as a known and visible consequence, not
as a loss to hide.

## What to change (smallest set that makes files, decisions and templates agree)

- `task-cycle/skill/SKILL.md`, section "The record before it is committed": step 3's bullet on the
  two relation lines (they stay as they are unless the check lists them) and step 4's last sentences
  of the exit-1 paragraph (the exception that commits the listed line is removed; the loop "until
  both exit 0" then holds without an exception). Add that when a relation line had to be cleaned, the
  request tells the human in *For you to decide*, in plain words: which kind of line (the record's or
  the task copy's, never its text), that the plan reader may now report a conflict for this task, and
  "Merge as it stands?". Keep it short.
- `task-cycle/skill/request_template.md`: the row "A draft for another reason" no longer carries the
  example of a listed line the cycle may not rewrite (remove that example and its check detail);
  give the item for a cleaned relation line its place, with the least new machinery — an item among
  those of *For you to decide* in the form that file uses, with its variant row or a sentence in the
  list of items, whichever the file's form takes (read how the other items are placed).
- `foundations/decisions.md`: WAY-308's binding paragraph and *Verification* (complies/violates)
  and *Rationale*, and WAY-309 where it repeats the exception, so the two entries say: the two lines
  stay as they are unless the check lists them, and a listed one is cleaned like any other; a cleaned
  relation line may make the plan reader report a conflict, which the human sees in the request. Add
  that consequence to WAY-308's "price taken". The lines you rewrite here: wrap them at the file's
  100 columns (the Minor finding N4 of the review of your fix concerns lines you edit anyway).
- Any other place that repeats the exception: search the repository outside `.runs/` and `docs/` for
  `Task relation` and `Project relation` and for the words of the exception, and correct each.
- Leave the Minor findings N2 and N3 as they are (the human did not ask for them).
- `project-level/plan_state.py` and the invariants stay unchanged. Run `foundation_check.py` on the
  foundation; run the focused tests of the parts you touch (`task-cycle`, `project-level`,
  `agent-instructions`); every check with command and exit code in your report.

## Report

Write it to `.runs/task-cycles/cycle-no-private-names/reports/correction-report.md`: each place changed
and why, the checks (command and exit code), your own-work check (name the requirement most likely
unmet — that no file still says a listed line is committed — and the search that shows it), the
**Searches not found or unclear** section (`none` is an answer), and any choice you made with the
way rejected. Return the status, the commits, a one-line check result and the report path.
