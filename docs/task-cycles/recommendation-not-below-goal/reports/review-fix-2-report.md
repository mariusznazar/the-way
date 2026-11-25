FAIL 3130f1d9d0802b07acc90fb798e9f5832a7996c7

# Review of the fix — recommendation-not-below-goal, fix 2

Fix range: `42298f2a81d8d4600b7a3769ab5ab6795510f0f6..3130f1d9d0802b07acc90fb798e9f5832a7996c7`, one
commit (`3130f1d9`). `git rev-parse HEAD` gives `3130f1d9d0802b07acc90fb798e9f5832a7996c7`, the head
given. The fix changes `elements/common/critique/prepare.md` (line breaks only),
`elements/common/way_of_working.md` and `foundations/decisions.md` (WAY-113, two lines each, the same
words). Bounded by the findings file `reports/review-whole-2-findings.md` (I1, M1, M2), as
`task-cycle/review/fix.md` gives.

The review fails only because I1 remains, as the handoff expects: it goes to the human and is not
asked of this fix. The fix introduces no new Critical or Important finding.

## State of each finding

**I1 — remains, unchanged.** The fix touches none of I1's places beyond WAY-113's last sentence:
WAY-113's sentence "A way that gives less stands among the ways [...] and is never recommended; where
no way reaches the goal, the question recommends none and says so" stands at
`foundations/decisions.md:1595-1597` as I found it; WAY-166 (`:4844-4849`, its *Verification*,
*Rationale* and *Rejected*), `project-level/technology/settle.md` and
`project-level/definition_template.md` are untouched (`git diff --stat 42298f2a..HEAD -- project-level
foundations` names only `foundations/decisions.md`, +2/−1, inside WAY-113's goal paragraph). No
`narrows` is recorded in either decision (WAY-113 *Relations*: none). The finding stands as worded in
the findings file and goes to the human; the author's fix report now puts the question with four
ways and, after reweighing, recommends the same way I recommended (d). Nothing of it is written.

Contradiction: yes — WAY-166 (binding sentence, *Verification* "violates", *Rejected*), with no
precedence recorded under WAY-25.

**M1 — fixed.** `elements/common/critique/prepare.md:7-13` re-wrapped: line lengths now 96, 99, 87, 100,
96, 98, 95; `git diff --word-diff=porcelain 42298f2a..HEAD -- elements/common/critique/prepare.md`
shows no added or removed word, only line breaks moved.

**M2 — fixed.** WAY-113's goal paragraph (`foundations/decisions.md:1599-1601`) and the bullet of
`elements/common/way_of_working.md:40-42` end: "the goal of an independent task with the human in the
same refinement, or in its cycle through a blocked draft request (WAY-227)". Judged:

- The route is what the foundation says. WAY-227 (read whole): "Decisions reserved to a human by the
  foundation remain reserved; when required code cannot proceed without one, the cycle opens a blocked
  draft request." A task's goal is the human's (the task document is accepted by the human), so a
  change of it is reserved to the human, and a blocked draft request is the cycle's way to put it
  before the human — the same route WAY-30 gives a contradiction found in implementation. It is the
  route my finding named.
- It changes nothing the task settles: *To do* 2 and the answer to question 4 name where the goal's
  question is settled for a refinement ("cel zadania niezależnego u człowieka w tym samym
  doprecyzowaniu"); the words add the place for the case the task does not cover, a question asked
  inside a cycle, and leave the refinement's place as it was. Row 1's "tam, gdzie cel stoi" holds.
- Limits: the paragraph stays at three sentences; `foundation_check.py` exits 0 with WAY-113 counted as
  changed; no added line of the whole change exceeds 100 columns.

## New finding in the fix diff

**N1 — Minor, within the task, non-blocking.** `foundations/decisions.md:1600-1601`,
`elements/common/way_of_working.md:41-42`. WAY-227, the decision cited, opens a blocked draft request
"when required code cannot proceed without" a decision reserved to the human. The new words send the
question of changing a goal through a blocked draft request in every case of a cycle, also where a
way that reaches the goal exists and code could proceed, so an agent of a cycle that only holds the
goal too dear would stop the cycle on its own opinion, a step WAY-227 does not give for that case. The
consequence is small: an agent in a cycle is already bound by the task as frozen (WAY-315) and the
case is rare; a wording such as "or, in its cycle, in the request, through a blocked draft request
where the code cannot proceed without the change (WAY-227)" would follow the cited decision exactly.
Polish of the citation's fit, not a defect of the rule.

## Declined to judge

- `product-guidelines/*/new_tools.md:4`, named again in the author's fix report — outside the fix diff
  and outside the task, as declined in the review of the whole change; they would follow the human's
  answer to I1.

## Checks

| Command / method | Exit / result |
|---|---|
| `git rev-parse HEAD` | `3130f1d9d0802b07acc90fb798e9f5832a7996c7`, the head given |
| `git log --oneline 42298f2a..HEAD`, `git diff 42298f2a..HEAD` | 0; one commit, 3 files |
| `git diff --word-diff=porcelain 42298f2a..HEAD -- elements/common/critique/prepare.md \| grep -c '^[-+][^-+]'` | 0 words changed (grep exit 1 on no match, the count printed is 0) |
| `awk '{print NR": "length($0)}' elements/common/critique/prepare.md` | lines 7–13: 96, 99, 87, 100, 96, 98, 95 |
| `python -B elements/common/foundation_check.py` | 0, `0 errors` |
| `python -B instruction-files/check_instructions.py` | 0, `0 error, 0 warn, 5 info` |
| `git diff 301e4eae..HEAD \| grep '^+' \| awk 'length($0)>101' \| wc -l` | 0 lines |
| `git diff --stat 42298f2a..HEAD -- project-level foundations` | only `foundations/decisions.md`, +2/−1 |
| Manual: WAY-227 read whole against the words of M2 | the route holds; N1 |

Not run: the gate (the cycle's own run).

## Reaches beyond the dispatch

- WAY-227, `foundations/decisions.md:7820-7840`, read whole — the decision the fix cites for M2.

## Working copies

None made. The outputs of the two checks went to `.runs/fc-fix2-review.txt` and
`.runs/ci-fix2-review.txt` in the worktree, outside my directory `.runs/review-whole-2/`; both are
removed before returning.

## Unread material

- The author's fix report, the findings file, `fix.md` and WAY-227: read whole. WAY-30: not reread in
  this review (read as its index line in the review of the whole change); its binding sentence is
  what M2's judgment relies on.
- Otherwise none.

## Searches not found or unclear

- A sentence of WAY-227, or another entry, that sends a question the cycle can work around — code that
  can proceed — to a blocked draft request: not found (the ground of N1).
