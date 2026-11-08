PASS ae5dff6

Saved by the orchestrator from the reviewer's returned text (a subagent may not write report files).

No new Critical or Important finding, and I1 and M1–M4 are fixed. M6 is fixed except for one 130-character line the fix left behind. M5 is left alone as instructed.

## Per finding

- **I1: fixed.**
  - Sentence 2 of WAY-312 now reads "Nothing that edits a product's guidelines, whether the template, a skill of guidelines or a product's own task, replaces a sentence that names a practice a model knows with the name of the practice, or takes out a case that follows from a rule's purpose."
  - The *Verification* "complies" line now has a product's cleaning task that removes a sentence restating a decision's *Decision* field and leaves a known-practice sentence and a derivable case as they were.
  - The "violates" line now names a product's task that cleans its guidelines and either replaces the empty-list sentence with "fail loudly" or takes out a derivable case.
  - Sentences 1 and 3 are unchanged, and the entry still has three binding sentences. The row's meaning is now met: the template guards new text, a product's task cleans existing guidelines, and the skills get no search step.
- **M1: fixed.** The fact now has one subject: the 45 of 45 pass, "on the model Sonnet 5.5". The "for every stage" clause is gone. The *Source* line is unchanged, and the quoted § Cost passage still carries the model.
- **M2: fixed, with a Minor remark.** The 2¼ h / 119 million figures are gone from *Rejected*, so the decision no longer disagrees with the cited source. The replacement, "a heavy one, hours of agent time and tens of millions of tokens", is a paraphrase. Against the task's own 119 million, "tens of millions" understates by a little. This blocks nothing.
- **M3: fixed.** The *Rationale* now says "Two inferences from that result are the author's own, not the source's" and labels both: the no-file arm point and the 55% arithmetic ("by arithmetic").
- **M4: fixed.** The template bullet now exempts only "The list of `### Logging scope`, which WAY-274 gives as the product's promise and no inventory of its code". It no longer exempts any list that is the product's promise.
- **M6: fixed except one line.** The reflow in the *Rationale* and *Rejected* is done. Line 9822 of `foundations/decisions.md` ("tokens, and in a product such a rule may not exist, ... a one-off") is 130 characters. The fix's own edit left it that way. This is polish only.
- **M5:** not raised again.

## Minor notes on the fix diff (block nothing)

- The 130-character line above.
- Sentence 2 now says "Nothing that edits a product's guidelines ...". The WAY-173 route, where a product departs from a rule by a decision of its own log, is not mentioned. This is arguably right for this row, since the decision derives from WAY-173. A reader might still ask whether a product's decision can lift the ban.

## Checks run

| Check | Result |
|---|---|
| `git rev-parse HEAD` | `ae5dff654ed4396ccca45b2a2c456a527179380d`, matches the head given |
| `git diff 6df733c..ae5dff6` | read whole: 3 files, +30 −26 |
| `python -B elements/common/foundation_check.py` in the worktree | exit 0 ("0 errors") |
| `git grep -i -n loop2 -- . ':!.runs'` | one hit only, `foundations/environment_facts.md:208` (the *Source* line) |
| Line-length scan of WAY-312 (lines 9773–9832) | one line over 102 characters (9822, 130) |
| `git status --short` | clean, no change made |

Not run: the full gate (the orchestrator's) and any focused tests (no changed file has tests).

## Searches not found or unclear

none
