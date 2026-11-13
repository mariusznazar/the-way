PASS c04d9cc

# Review of correction 1 — review-structure-form-class

Range `24cbe61..c04d9cc` (one commit, `c04d9cc`; 5 files, +31 / -16). `git rev-parse HEAD` =
`c04d9cc821800959f982fea28e01e84c4d9c6b5e`, the head given. Method: `task-cycle/review/fix.md`, variant "a correction for the
human's remarks", with `reports/correction-1-remarks.md` in the place of a findings file.

## Each remark

- **Remark 1 — made.** Where a product has no rule of size, a finding about the structure of its code is now Minor, in every
  place that grades it:
  - `task-cycle/review/SKILL.md:126-130`: "…is Minor, and so is every such finding where the product has no rule of size — it
    departed from the rule by a decision, or it has no coding guidelines at all — and you judge its scope as for any finding".
  - WAY-363, binding sentence (`foundations/decisions.md:12097-12101`), edited in place (WAY-07): "…and one in a product that has
    no rule of size — it departed from the rule by a decision, or has no coding guidelines at all — and judges its scope as for any
    finding (WAY-161)." *Relations* still `narrows WAY-161`; *Verification* gains a complying case (a script of this repository,
    WAY-328, and a product that departed) and a violating one; *Rationale* gains the reason (no threshold, no test); *Rejected*
    gains the way not taken with its price: "the finding graded as any other where the product has no rule of size — with no
    threshold a finding of structure can block the change on the reviewer's impression and give a round of correction". The entry
    still reads as a decision: one question, binding sentences that a change can be compared with, the fields whole
    (`foundation_check.py` 0 errors).
  - Made to agree: `task-cycle/review/whole_change.md:46-48`, `product-guidelines/coding/settle.md:89-90` (said to the human with the
    departure) and `product-guidelines/coding/template.md:76-78`.
  - No other grade or rule changed: the over-threshold sentence only moves from "that threshold" to "a threshold", which is the
    same where there is a rule; the scope judgment, WAY-364's form grade and the orchestrator's ban on regrading stay as they were.
- **Remark 2 — not made, as the remark asks.** The diff touches no measurement of WAY-229, WAY-164 or WAY-364.

## What the correction itself broke or widened

Nothing Critical or Important. The search of the branch (below) found no sentence that still grades a finding of structure
otherwise where there is no rule.

### Minor

**C1. `task-cycle/review/SKILL.md:127-128` and WAY-363 binding (`foundations/decisions.md:12098-12099`)** — "where the product has no
rule of size — it departed from the rule by a decision, or it has no coding guidelines at all —". The clause between dashes reads
as the list of cases, and it leaves out a third: a product whose coding guidelines predate the rule and do not yet hold the heading
(the game this task names stands there until its own adoption task, which the task puts out of scope). `whole_change.md:46`
covers it ("or the product's guidelines hold no such rule … a finding of structure is Minor"), and the head term "has no rule of
size" covers it too, so a reviewer reading the whole review has the answer; but the list in the entry and the skill is narrower
than that sentence. The clause follows the human's own remark word for word, so the fix is the human's call: add "or its
guidelines do not hold the rule yet", or make the clause read as examples. Minor: no grade goes wrong for a reviewer who reads
`whole_change.md`, which the review of the whole change always reads.

**C2. `foundations/decisions.md:12131`** — WAY-363 *Rationale*, a line of 163 characters ("structure Minor and not blocking. The
reviewer still judges the scope of each finding, so a restructuring of code from before the change reaches the request's list"):
the inserted sentence was not rewrapped. Polish.

## Declined to judge

- WAY-360 *Rejected* (`foundations/decisions.md:12025-12027`), "no rule in the template, only the question about the structure of
  code in the review — nothing blocks, and the assessment of structure depends on the reviewer, with the same chance in the grade as
  today": with WAY-363 now making every such finding Minor where there is no rule, "the same chance in the grade" describes the
  grade before this branch. It is question 4's way not chosen in the human's words, kept as WAY-134 gives, and outside this
  correction's remark.

## Checks

| Command | Exit | Result |
|---|---|---|
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `python -B gate/run_tests.py task-cycle` | 0 | 385 tests, OK |
| `git status --porcelain` in the reviewed worktree after the runs | 0 | empty |

Search once over the branch at `c04d9cc` (all tracked files but `.runs`):
`git grep -n -i -E "below the threshold|below its threshold|under the threshold|finding(s)? (about|of) (the )?structure|structure of (the )?code"`
— 21 hits; each read: the grade where there is no rule is Minor in every place that states it, and the rest are the
over-threshold case, the review's question (WAY-362, `whole_change.md:29-31`), the script's docstring, settle.md's weak point and
WAY-360's *Rejected* (Declined above).

Not run: the whole gate (the orchestrator's run).

## Unread material

none — `fix.md`, the remarks, the correction's report and the whole diff read whole; WAY-360 to WAY-364 read in the passages the
search found.

## Searches not found or unclear

none
