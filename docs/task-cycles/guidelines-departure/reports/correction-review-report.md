PASS 062b772ef3430250fe9bd842b31e3c67d4bfce2d

# Review of the correction after the human's remark — guidelines-departure

Range `66cc61d..062b772` (`git rev-parse HEAD` = `062b772ef3430250fe9bd842b31e3c67d4bfce2d`; one commit; worktree clean). One file, `foundations/decisions.md`, WAY-328 only (+3 / -2, the third binding sentence). Method: `task-cycle/review/SKILL.md`, `task-cycle/review/fix.md` (a correction: each remark made or not, then the diff by section 2). Read: the remark file, the correction report, the diff, the current entry WAY-328 whole. The frozen task's rows 1 and 2 and the template were read whole earlier in this session.

Counts: new Critical or Important 0 · new Minor 1 (within the task) · out of scope 0.

## The remark

"Popraw w tym PRze" on my Minor finding 6 (the third binding sentence, "guidelines of the-way's own", is wider than the coverage). **Made:** the sentence now names the two disciplines the decision covers, so a styleguide of the-way, which the decision excludes, can no longer read as withdrawing it, and one discipline's guidelines no longer withdraws the other's departure.

The sentence as written:

"A separate task that writes the general coding guidelines of the-way's own takes the coding guidelines out of this decision, one that writes its testing guidelines takes the testing guidelines out of it, and once both are written the decision is withdrawn."

## Judgment of the sentence

- Row 1 of the frozen task: "gdyby kiedyś własne wytyczne zaczęły się opłacać, osobne zadanie je napisze i tę decyzję wycofa." The case where both are written is the row's case, and the sentence keeps it (a separate task writes; the decision is withdrawn). The row is silent on the case of one discipline; the sentence answers it per discipline. That answer is the orchestrator's choice, not the human's and not the source's, but it follows from WAY-217 (a departure covers the work it expressly covers) and it adds no value: a discipline whose guidelines exist is no longer "missing", so a departure from it has nothing left to say. The human accepts the meaning by merging the request, so the request should name this choice (Minor 7).
- Template: still three binding sentences (the maximum); present tense; no *must*, *should*, *will*, capitals or RFC words (grep over the entry: no match); names no stage, file or count; the plan test passes (the rule binds after the change merges); it is checkable on a commit (a change that writes a discipline's guidelines of the-way either takes that discipline out of the entry or leaves the entry as it was).
- Against the decision's other parts, all unchanged by the commit:
  - Binding sentence 1 says "neither is missing" for both disciplines; after a partial take-out the entry is edited, as the template's "Changing a decision" gives (edit in place). No conflict.
  - *Rationale* (the reason, scope, no time limit, price) does not speak of the withdrawal; "no time limit" means no stage or date, and the sentence is a condition on events. Agrees.
  - *Verification*: no example speaks of the withdrawal, and none contradicts the sentence. Agrees. (An example for it would be optional.)
  - *Rejected*: the rejected "the-way writing its own coding guidelines and testing guidelines, as every product does" is still the way not chosen now; this sentence says what follows if a later task takes it. Agrees.
- Part by part: a general coding file that omits an affected part is read for extension, not as an absent file (`product-guidelines/reading.md`), and the departure is per part by WAY-217, so guidelines written for some parts only do not need a clause here. No gap.

## Findings

### Blocking

None.

### Minor (within the task)

7. `foundations/decisions.md:10765-10767`, the third binding sentence. It is one 40-word sentence with three clauses, and "takes ... out of this decision" does not say how it is done. Reading "a separate task takes the coding guidelines out" as an edit of this entry (its first sentence, its *Scope* sentence and its examples then speak of one discipline) is the natural one, but the sentence does not say so, and the per-discipline meaning is the orchestrator's choice, not row 1's. Fix if the human wants it: state the choice in the request's *For you to decide* so that the merge accepts it, or, if the human reads row 1 as "both or nothing", return to the earlier wording "the coding guidelines and the testing guidelines". It blocks nothing.

## Declined to judge

- Whether the departure should be per discipline or both together: not given by row 1; the orchestrator chose, the human accepts at the merge.
- The WAY-216 question (a first file of a new kind of code): marked out of scope by the earlier review and by the correction's remark.

## Checks run

| Check | Command | Exit |
|---|---|---|
| Foundation check | `python -B elements/common/foundation_check.py --skip-test-citations` | 0 ("0 errors") |
| Head, range, tree | `git rev-parse HEAD`; `git log --oneline 66cc61d..062b772`; `git status --short` | 0; head matches, one commit, clean |
| Diff | `git diff 66cc61d..062b772`; `--stat` | 0; `foundations/decisions.md` only, +3 / -2, inside WAY-328 |
| Requirement words in the entry | grep for should, will, must, SHALL, MAY, REQUIRED over the entry (lines 10759-10813) | exit 1 (no match, as wanted) |
| Line widths | awk over the same lines | no line of the entry over 103 characters except the heading |

Not run: the product's gate (the cycle's), any test (prose of one entry).

## Reaches beyond the dispatch

`product-guidelines/reading.md` (read whole earlier in this session) for the per-part departure; WAY-217 (read whole earlier). Nothing new was opened.

## Unread material

For a later change to an open request the selection is the dispatch: the remark file, the correction report, the diff, and WAY-328 (read whole). `none` stayed unread. The decisions I selected in the earlier whole-change review (21 whole, 7 in part, the rest by title) were not selected again; the merge of the target branch (commit `66cc61d`) was reviewed by another reviewer and I did not review its other changes.

## Searches not found or unclear

- none found missing.
- Unclear: whether the human wants the per-discipline meaning or "both or nothing" (finding 7).
