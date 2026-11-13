# Reviewing the whole change

What the review of the whole change reads and what it checks besides section 2.

## Read

- For the review of the whole change: the frozen task document whole, the spec where the cycle
  wrote one and, on the planned route, the plan, each slice's range and whether it had a review of
  its own, the reports of the executors of the slices that had none with any mismatch the
  orchestrator's mechanical check passed on, the report of the agent that wrote the plan's
  *Foundation entries* where slice 1 had no review of its own, and the Minor and out-of-scope
  findings of the slice reviews the dispatch lists.

## Review of the whole change

Besides section 2, check the change against the whole task: every required outcome and item of
*To do*, and every row of *Settlements to record* and projected entry the task carries, met by the
commits; fidelity to the task's sources, with nothing the change takes from them altered or
invented. Judge every slice that had no review of its own as section 2 judges a slice, its
executor's own-work check included (WAY-164); this review is the only one it gets (WAY-136). In
the review of the whole change of a plan, name for each blocking finding the slice it comes from,
by the slice's number and the commit; or say that it spans slices and name them, or that it comes
from none — a gap of the plan, or the plan's *Foundation entries*. Grade each Minor and
out-of-scope finding of the slice reviews the dispatch lists as a finding of this review. List
each Minor finding with its place in the code and its own words, and say in them where a Minor
finding lies outside the task, so that the cycle can cut the Minor findings within the task from
the report into the findings file of the fix that follows them (WAY-161).

## The structure of the code the change leaves

Judge, besides the task, what the change leaves in the structure of the code: the growth of a
function or a file, code that has no user after the change, and a name that stopped being true
(WAY-357). Take your numbers from two runs of your own, none in the reviewed worktree:

- the lines of each changed file before the change and after it: from the root of the repository,
  `python -B task-cycle/change_file_sizes.py <base> <head>` on the dispatch's range, in a product
  `python -B .the-way/task-cycle/change_file_sizes.py <base> <head>`. The script ends with exit
  code 2 and an `Error:` line where it cannot read the range;
- the functions and files over a threshold: the test of the invariant that the rule
  `### Size of a function and a file` in the product's `guidelines/coding.md` names, run as an
  ordinary test of the product's suite in a separate worktree of the base and in one of the head
  (WAY-356). What the run on the head names and the run on the base does not is what the change
  pushed over a threshold. Where the rule's invariant is marked violated, its test stands marked as
  an expected failure (WAY-51); take the mark off in your separate worktrees, so that the test's
  message shows. Where that heading holds `none —`, or the product's guidelines hold no such rule,
  there is no such test, and the first numbers and the diff are your material.

Name a growth by those numbers, read the functions the diff reaches in the files that grew, and
grade each finding as section 3 of `SKILL.md` gives it (WAY-358).
