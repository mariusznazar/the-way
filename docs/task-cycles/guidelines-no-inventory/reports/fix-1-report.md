# Fix report — review of the whole change, `FAIL 6df733c`

Saved by the orchestrator from the author's returned text (a subagent may not write report files).

Status: done. One new commit, `ae5dff6`, on top of `6df733c` (no amend, no reset). I1 and M1, M2, M3, M4 and M6 are fixed. M5 is untouched, as the orchestrator said, and no commit message was changed.

**Commit:** `ae5dff6` Fix the findings of the review of the guidelines-no-inventory change.

**Files changed** (added/removed lines, from `git diff HEAD~1 --numstat`):
- `foundations/decisions.md`: +27 −23
- `foundations/environment_facts.md`: +1 −1
- `product-guidelines/template.md`: +2 −2

## Per finding

**I1 (blocking), fixed.** WAY-312's second binding sentence had only the template and the skills as its subject. It now reads: "Nothing that edits a product's guidelines, whether the template, a skill of guidelines or a product's own task, replaces a sentence that names a practice a model knows with the name of the practice, or takes out a case that follows from a rule's purpose."
- Sentence 1 (state and repetition go out), sentence 3 (a product's own task cleans existing guidelines, skills get no search step) and the rest of the entry are unchanged, and the entry still has three binding sentences.
- *Verification* "complies" gains: a product's cleaning task removes a sentence restating a decision's *Decision* field and leaves a known-practice sentence and a case that follows from a rule's purpose as they were.
- *Verification* "violates" now reads: "the template, a skill or a product's task that cleans its guidelines replaces the sentence on an empty list with the words 'fail loudly', or takes out a case that follows from a rule's purpose". The search-step example stays.

**M1, fixed.** The fact `shorter-guidelines-trial` now says the 45 of 45 holds "on the model Sonnet 5.5". The clause "for every stage of the cycle that ran the trial" is gone, so the sentence is one fact with the model as its condition. The *Source* passages are untouched.

**M2, fixed.** The figures were left out and the point kept. *Rejected* now says the earlier trial "was a heavy one, hours of agent time and tens of millions of tokens". That is true under both the cited record (2 h 44 min, 95.2 million tokens) and the later corrected description (about 2¼ hours, 119.4 million tokens), so no reader of the fact sees a different cost. The 2¼ h and 119 million figures were not sourced, because the cited record does not hold them and the repository must not be named elsewhere.

**M3, fixed.** The *Rationale* now says "Two inferences from that result are the author's own, not the source's". They are that a passing no-file arm means the tests cannot tell whether the file is followed, and that a pass rate near 55% gives five of five in about one set of five runs in twenty (arithmetic, 0.55^5 ≈ 0.05). Both are kept because they are marked as derivations.

**M4, fixed.** The template bullet's last sentence is now: "The list of `### Logging scope`, which WAY-274 gives as the product's promise and no inventory of its code, is no such state (WAY-312, WAY-274)." The exemption no longer covers any list that is a product's promise.

**M6, fixed.** The two ragged lines in WAY-312 (the *Rationale* line "Its weak points: ..." and the *Rejected* line "refresh mode of coding guidelines ...") were reflowed. No wording changed apart from the M2 and M3 edits made in the same paragraphs.

**Correction of the earlier misattribution.** The author earlier said the template examples "endpoints the code has today" and "version of a tool" come from the task's Context. "Endpoints" is not in the task. It comes from WAY-225's "violates" line ("a hand-written list of the product's endpoints kept next to the code"). The text is valid; only the attribution was wrong. The version-of-a-tool example does come from the task.

## Checks

| Command | Exit |
|---|---|
| `python -B elements/common/foundation_check.py` (worktree root), after the edits and before `ae5dff6` | 0 ("0 errors") |

Not run: `gate/run_tests.py` (the orchestrator's) and focused tests (no changed file has tests).

## Own-work check (changed lines only)

- **Requirement most likely unmet:** I1's fix must not widen or narrow rows 1 and 2.
- **Check:** the new sentence 2 and the *Verification* lines compared with row 1 and *To do* 1 of the frozen task.
  - Known-practice sentences and derivable cases are neither replaced by a name nor taken out. This now applies to any editor.
  - The template guards new text.
  - A product's task cleans existing guidelines.
  - The skills get no search step.
- **Result:** sentences 1 and 3 are untouched, and no new "for that reason alone" qualifier was added.
- **Other fixes:**
  - The *Rationale* has no unmarked claim beyond the fact; derived statements are labelled as the author's inferences.
  - The fact has one subject, and its passages still match the local clone word for word (unchanged since the earlier check).
  - A `git grep` for "loop2" outside `.runs` still finds it only in the fact's *Source* line.

## Search of the foundation, repeated for the changed entries

- Re-read the places the fix touches. WAY-312 (relations: WAY-168, WAY-225, WAY-173) is consistent with WAY-100, WAY-172 and WAY-274.
- `git grep` for "fail loudly" and "endpoints the code" finds only WAY-312's *Verification* and the template bullet.
- Nothing else names `shorter-guidelines-trial` except WAY-312's *Based on*. No other entry or skill needs a change.

## Searches not found or unclear

- None remain open. The wording "tens of millions of tokens" is my paraphrase of both records, not a quoted figure. If the human wants the exact 2¼ hours and 119 million, they have to come from a source the fact cites.
