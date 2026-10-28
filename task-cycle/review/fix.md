# Reviewing a fix or a correction

What the review of a fix of a review's findings, or of a correction made for the human's remarks on
the request, reads and what bounds it.

## Read

- For the review of a fix, the findings file — the blocking findings of the review it answers —
  and the fix report. For the review of a correction made for the human's remarks on the request,
  those remarks and the correction report.

## Review of a fix

The findings file bounds this review; it holds the blocking findings only, since Minor and
out-of-scope findings are not fixed (WAY-161). For each finding in it, say whether it is **fixed**
— the defect no longer exists on the new head; tried is not fixed — or **remains**, with evidence.
For a finding the author contests with evidence, say whether you keep it. Inspect the fix diff for
what the fix itself broke: a new Critical or Important finding there counts as one that remains.
An issue outside the fix diff is a Minor or out-of-scope note; it does not reopen the review.

For a correction made for the human's remarks, the remarks take the findings file's place: say for
each whether the correction makes it, then review the correction's diff as section 2 gives.
