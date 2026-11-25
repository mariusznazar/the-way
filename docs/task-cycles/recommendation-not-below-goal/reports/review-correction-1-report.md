PASS e08834e4317de5961519bed739b02f49b7a89d0f

# Review of correction 1 — recommendation-not-below-goal

Range: `e5a69f85..e08834e4317de5961519bed739b02f49b7a89d0f`, one commit (`e08834e4`). `git rev-parse
HEAD` gives `e08834e4317de5961519bed739b02f49b7a89d0f`, the head given. `git diff --stat
3130f1d9..e5a69f85` is empty, so `e5a69f85` carries the code I last reviewed. The correction changes
`foundations/decisions.md` only, inside WAY-166 (+23/−10). The human's remarks
(`reports/correction-1-remarks.md`) take the place of a findings file, as `task-cycle/review/fix.md`
gives.

## Each remark: made or not

- **Needed from you 1 — way a, with the relation the remarks word: made.** The remarks: WAY-166 "nie
  jest wyjątkiem od nowej reguły, tylko z góry przyjętą odpowiedzią na pytanie o zmianę celu"; where
  the goal is an agent's check and no option gives it, "cel zostaje jawnie zawężony do sprawdzenia
  przez człowieka — to jedno zdanie, które WAY-166 już każe napisać — i dopiero wobec tak zawężonego
  celu pytanie poleca wariant najtańszy". WAY-166's new third binding sentence
  (`foundations/decisions.md:4850-4854`) carries each clause: "that sentence narrows the goal openly,
  in the same question, to the check by the human, and the recommendation goes against the goal so
  narrowed; it is the answer, accepted in advance, to the question of changing the goal that WAY-113
  asks where no way reaches the goal". The recommendation keeps WAY-166's own words ("by the other
  consequences"), and the added *complies* case says "the one that wins by cost and upkeep", which
  is what "najtańszy" means here; no word the remarks do not give enters the rule.
- **Needed from you 2 — the correction makes the return step and the reconciliation:** not a change of
  files in this range; nothing to judge here.
- **Items 3 and 4 accepted:** no change was asked, and none was made (WAY-113's paragraph, its eleven
  words and the bullet of `way_of_working.md` are unchanged: `git diff e5a69f85..HEAD --stat` names
  only `foundations/decisions.md`, and its hunks lie in WAY-166 only).

Not widened: beside the binding sentence, the correction aligns the parts of the same entry that
would otherwise say the old rule — *Relations* (`narrows WAY-113`), one clause each in *complies* and
*violates*, one passage of *Rationale*, and the removal of "an exception to WAY-113" from the
*Rejected* way the remarks reframe. No way is added to *Rejected*, no other entry and no other file is
touched, and no step of way d (a step in `settle.md` for a choice with no recommendation) is written.

The relation word: the remarks say WAY-166 is no exception but an answer given in advance, while
the entry records `narrows WAY-113` and "prevails in this area over WAY-113's rule". WAY-25 gives
`narrows` with the area stated in the binding sentences as the one form of a precedence, and the
binding sentence says, in the remarks' own terms, why it prevails (it is the answer to WAY-113's
question). The two agree in effect; no finding.

## State of I1 after the correction

**I1 — fixed.** The collision I found is settled with a precedence recorded as WAY-25 gives it:
WAY-166, the decision that prevails, names `narrows WAY-113` in *Relations* (`:4858`) and states the
area in its binding sentences ("Where the goal the material sets is that an agent checks the running
product [...] it prevails in this area over WAY-113's rule that such a question recommends none").
WAY-113 does not name WAY-166, so no two decisions narrow each other; WAY-166 also narrows WAY-123,
which derives from WAY-113 — no chain is relied on. In the case I found (a run of the technology step
at a task whose need is that an agent reads the logs, every option a panel only the human reads), the
two decisions now say one thing: the one sentence narrows the need to the human's reading, and the
step recommends the option that wins by cost and upkeep — the added *complies* clause states that
very case. The parts of WAY-166 I cited now agree: its *violates* still names "the step recommends
nothing" and adds leaving the goal unchanged beside the recommendation; its *Rationale* ("the human
is owed a recommendation (WAY-113)") holds, since against the narrowed goal a way reaches it and
WAY-113's first paragraph asks for a recommendation; its *Rejected* no longer calls the refused way
"an exception to WAY-113".

Neighbouring cases in WAY-166's area: `project-level/technology/settle.md:34-38` and
`project-level/definition_template.md:242-248` restate WAY-166's first two sentences, and an agent
that follows them writes the very sentence that, by the new third sentence, narrows the goal; so in
that area every choice keeps a recommendation, and the risk tests (`settle.md:39-41`, WAY-138) and
the answer "you choose" (`settle.md:61-62`) keep their object. Their missing third sentence is N1
below.

Contradiction: none remains — the contradiction with WAY-166 that I1 carried is settled by the
recorded precedence.

## New findings

**N1 — Minor, within the task, non-blocking.** `project-level/technology/settle.md:34-38`,
`project-level/definition_template.md:242-248`. Both restate WAY-166 without its new third sentence.
An agent that follows them behaves as WAY-166 now asks, since the sentence they require is the
narrowing; but a reader of these files alone does not learn that the sentence also narrows a goal
that is an agent's check, and cannot judge WAY-166's new *violates* clause ("leaves that goal as it
stands beside the option recommended") from them. The author weighed this and left them, since the
area is stated in the decision that prevails (WAY-25). One clause in each would close it.

**N2 — Minor, within the task, non-blocking; the remainder of the second paragraph of I1.** Outside
WAY-166's area — a technology choice where no option reaches a goal of the definition or the task
that is not an agent's check — WAY-113's new paragraph still gives a question with no recommendation,
and `settle.md` still has no step for it: the risk tests run on "the option recommended for every
choice of the wave" (`:39-41`, WAY-138) and "A human who answers "you choose" or "I do not know" takes
the recommendation" (`:61-62`). In the review of the whole change I wrote this inside I1, whose
ground for blocking was the collision with WAY-166 under WAY-25. With that collision settled, what
remains is no collision between decisions: WAY-123 derives from WAY-113 and is read under it, and a
risk test that has no recommended option simply has nothing to test. The one open act is the answer
"you choose" to a question that recommends none, which the agent can only meet by saying there is
no recommendation and asking again. The case is rare and the cost is one more exchange, so I grade it
Minor. The human, choosing a over d, also left out the `settle.md` step that d would have written.

## Declined to judge

- `product-guidelines/*/new_tools.md:4` — outside the correction and outside the task, as declined in
  the review of the whole change.

## Checks

| Command / method | Exit / result |
|---|---|
| `git rev-parse HEAD` | `e08834e4317de5961519bed739b02f49b7a89d0f`, the head given |
| `git log --oneline 3130f1d9..HEAD`; `git diff --stat 3130f1d9..e5a69f85` | 0; three commits, the first two add and remove the record; the code diff between `3130f1d9` and `e5a69f85` is empty |
| `git diff e5a69f85..HEAD` | 0; `foundations/decisions.md` only, all hunks in WAY-166 |
| `python -B elements/common/foundation_check.py` | 0, `0 errors` (WAY-166 counted as changed against base `301e4eae`) |
| `python -B instruction-files/check_instructions.py` | 0, `0 error, 0 warn, 5 info` |
| `git diff e5a69f85..HEAD \| grep '^+' \| awk 'length($0)>101' \| wc -l` | 0 lines |
| `python -B -c` count of WAY-166's binding paragraph | 0; 172 words, 3 sentences (limits 300 and 3; the whole binding part 172 of 600) |
| `grep -n "WAY-166" -r --include=*.md .` (outside `.runs`) | 0; `settle.md:35,38`, `definition_template.md:248`, `research.md:41`, `task_run.md:77-78`, decisions `:4559`, `:4577`, `:4593-4594`, `:5072` — read; none says anything the correction makes false |
| Manual: WAY-166 at head against each clause of the remarks; WAY-25 against the recorded relation | as above |

Not run: the gate (the cycle's own run).

## Reaches beyond the dispatch

- `project-level/technology/task_run.md:70-90`, `foundations/decisions.md:4552-4562` — places that cite
  WAY-166, read to check that the correction makes none of them false.

## Working copies

Directory `.runs/review-whole-2/` held only the outputs of the two checks (`fc.txt`, `ci.txt`); no
worktree, clone or probe. Removed before returning.

## Unread material

- WAY-166 read whole at head; WAY-25 and WAY-113 read whole in the review of the whole change, not
  reread whole here (WAY-113 is unchanged by the correction).
- `project-level/technology/settle.md` and `project-level/definition_template.md`: read in the parts
  cited (settle.md 1–75 in the earlier review; definition_template.md 234–263), not whole.
- Otherwise none.

## Searches not found or unclear

- A step in `project-level/technology/settle.md` for a choice whose question recommends none (risk
  tests, the answer "you choose"), outside WAY-166's area: not found (the ground of N2).
