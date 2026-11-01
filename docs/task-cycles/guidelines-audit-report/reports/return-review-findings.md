# Blocking findings of the review of the return step

From `.runs/task-cycles/guidelines-audit-report/reports/return-review.md`, `FAIL aee18e4`, in the
reviewer's words. One finding blocks.

## 1. The correction gives WAY-281 a qualification that `audit_end.md` repeats the entry without

Important. `product-guidelines/audit_end.md:13-16`, against `foundations/decisions.md:8371-8373`.

- What is wrong: `audit_end.md` says what each audit brings to the list: "coding's with the files
  marked `do not copy` and the trial run's reports, testing's with the trust boundaries at which a
  test of refusal is due and none exists." Those are the two things WAY-281 says the list "also
  holds", and the testing clause carries the entry's qualification nearly word for word. The coding
  clause does not: the trial run gives reports of every rule of the set, the blocking ones and those
  that go among the examples (`trial_run.md:11-16`). The next section then says "Merge every finding
  into a cause" and "each finding belongs to one cause" (`audit_end.md:21-22`), so read as it stands,
  every report of the trial run is a finding and belongs to a cause. That is the width the entry had
  before `aee18e4` and no longer has, and it contradicts `trial_run.md:23-24`, "yield no cause".
- Why it matters: this is the disagreement the return step set out to close, moved to another file.
  Its report's reason applies unchanged: an agent comparing work with the entry alone finds a file
  whose words reach reports the entry leaves out. Before this commit the line and the entry agreed;
  the commit made them disagree, and `return_step.md` has the step correct in the same change
  "whatever no longer matches".
- Fix: one clause, "the trial run's reports of the rules that block". No entry changes.
