PASS b4bfca8992d115f26815ca8c9cf21cb82b50b297

# Review of the fix of the Minor findings — guidelines-departure

Range `7442841..b4bfca8` (`git rev-parse HEAD` = `b4bfca8992d115f26815ca8c9cf21cb82b50b297`; one commit; worktree clean). One file, `foundations/decisions.md`, entry WAY-327 only (+15 / -13). Method: `task-cycle/review/SKILL.md` and `task-cycle/review/fix.md`. Read: the findings file, the fix report, the diff, the frozen task's row 1 and row 2 (read whole in my earlier review), `elements/decisions/template.md` (read whole earlier in this session).

Counts: new Critical or Important 0 · my four Minor findings: 4 fixed, 0 remain · new Minor 1 (within the task) · out of scope 0 new.

## Each finding

1. Row 2's way not chosen missing from *Rejected* — **fixed.** `foundations/decisions.md` (end of *Rejected*) now ends "...; a decision with no sentence that adds a new part to its *Scope* — the first script in a new part would raise the question of missing guidelines again." It follows row 2's *Source* ("bez tego zdania pierwszy skrypt w nowej części znów stawia pytanie o brak wytycznych"), names no file and no count, and sits in the same semicolon list as the other rejected ways.
2. *Rationale* never states the reason — **fixed.** It now opens: the-way departs rather than writes its own guidelines "because that is a large task of its own whose gain lies mostly in code and tests that already exist and would have to be cleaned, while every task of the-way with code or tests waits for it." This is the task's *Not chosen* (a) (large task; gain mostly in existing code that would have to be cleaned; every task with code waits). "and tests" is not an addition: (a) names the audit of the 29 test files. No count or file name enters (template rule kept). The old reasons (whole-the-way scope, no stage, price) follow unchanged in meaning.
3. Exit clause only in prose — **fixed**, by a third binding sentence (below). The prose version, with its "or narrows", is removed; row 1 gives "withdraws" only.
4. Wrapping — **fixed.** The *Rationale* is re-wrapped to the width of the entry (longest line 103 characters in the binding sentences, the same as the entry had before; no stub line).

## The new third binding sentence

"A separate task that writes guidelines of the-way's own withdraws this decision."

- Against row 1: the row says "gdyby własne wytyczne zaczęły się opłacać, osobne zadanie je napisze i tę decyzję wycofa." The sentence keeps the separate task, the writing of own guidelines and the withdrawal; it drops the "if they come to pay" condition, which is the motive, not a state (the template's binding sentences describe a state). Meaning held.
- Against the template: three sentences (the maximum); present tense; no *should*, *will*, capitals or RFC words (grep for them over the entry: none); checkable (a task that writes the-way's guidelines either removes WAY-327 in the same change, with its number going to *Withdrawn identifiers*, or does not). It names no stage of the product. The plan test passes: the rule still binds after the change that brings it merges. It matches "A decision no longer needed leaves the log in the change that ends it". It does not clash with the *Rationale*'s "no time limit": that says no calendar or stage limit, and the sentence is a condition on events.
- Against the other binding sentences: no collision; the *Scope* sentence and this one do not touch.

### New finding (Minor, within the task)

6. `foundations/decisions.md:10634-10635`, the third binding sentence. "Guidelines of the-way's own" is wider than what the decision covers. The decision departs only from the general coding guidelines and the testing guidelines, and its *Rationale* excludes the styleguide. Read literally, a task that writes only a styleguide of the-way (not a thing the-way needs, as it has no screens), or only coding guidelines (leaving testing departed), "withdraws this decision". Row 1 says "własne wytyczne" in the context of the two disciplines, so the wider wording is the row's own, and a task that writes any of them can state in its change which part of the decision it withdraws. It blocks nothing; a reader who meets it can resolve it from the *Rationale*. Fix, if the human wants it: "A separate task that writes the coding guidelines and the testing guidelines of the-way's own withdraws this decision" (a choice of meaning for the human, since row 1 does not say whether one of the two is enough, so I did not grade it higher).

## Anything else new in the fix diff

- *Verification* examples are unchanged and still true; none contradicts the new sentence.
- *Relations*, *Scope*, *Based on*, *Origin* unchanged.
- The *Rationale* keeps "the departure covers the coding guidelines and the testing guidelines only", which the new sentence's "guidelines of the-way's own" does not repeat (finding 6).
- No Critical or Important finding.

## Declined to judge

- Whether one of the two disciplines' guidelines is enough to withdraw the decision: row 1 does not say; it is the human's choice (finding 6).
- The out-of-scope finding 5 of the earlier review (kinds of code under WAY-216): not to be fixed per the findings file.

## Checks run

| Check | Command | Exit |
|---|---|---|
| Foundation check | `python -B elements/common/foundation_check.py --skip-test-citations` | 0 ("0 errors") |
| Head and range | `git rev-parse HEAD`; `git log --oneline 7442841..b4bfca8`; `git status --short` | 0; head matches, one commit, clean |
| Diff | `git diff 7442841..b4bfca8`; `git diff --stat` | 0; `foundations/decisions.md` only |
| Forbidden words in the entry | grep for should, will, MUST, SHALL, MAY, REQUIRED over lines 10628-10680 | exit 1 (no match, as wanted) |
| Line widths of the entry | awk over lines 10628-10680 | no line over 103 characters except the heading (130) |

Not run: the product's gate (the cycle's), any test (the change holds no code).

## Reaches beyond the dispatch

None beyond the dispatch's files; the template and the frozen task were already read in this session's earlier review.

## Unread material

For this review the whole selection is the dispatch: the findings file, the fix report, the diff and the current text of WAY-327, all read whole. The frozen task's rows 1 and 2 and the template were read whole earlier in this session, not again. In the review of the fix there is no selection of foundation of my own, so no counts of decisions apply. `none` of the dispatch stayed unread.

## Searches not found or unclear

- none found missing.
- Unclear: whether row 1's "własne wytyczne" means both disciplines together or either one (finding 6).
