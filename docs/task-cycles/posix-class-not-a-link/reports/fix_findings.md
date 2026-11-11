# Findings for the fix (Minor findings of the review of the whole change, within the task)

Review: `reports/review_report.md`, first line `PASS 8fa6bac2a7af84c73f54d7c8320c9077592f955b`. No blocking findings.
The reviewer's words, cut from its report:

1. Within the task. `foundations/decisions.md`, WAY-323 *Rationale*, the sentence "Each of the twelve names is kept to, not matched by a
   pattern, so a text with another name between the colons stays listed": the code does match them by a pattern, an
   alternation of the twelve names (`POSIX_CLASS`). What the sentence means is that the names are listed one by one, not
   matched by a general shape such as `:[a-z]+:`. A reader could take it for a statement about the code and find it false.
   Reword to "The twelve names are listed one by one, not matched by a general shape, ...". Grade Minor: the binding
   sentence and *Verification* are right; only a clause of the rationale is loose.
