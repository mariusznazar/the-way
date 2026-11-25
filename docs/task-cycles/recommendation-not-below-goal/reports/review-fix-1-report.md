FAIL 42298f2a81d8d4600b7a3769ab5ab6795510f0f6

# Review of the fix 1 — recommendation-not-below-goal

Fix range: `7c2502a73f8360d9e47af85863c522392ec6c192` to `42298f2a81d8d4600b7a3769ab5ab6795510f0f6` (one commit, `git rev-parse HEAD` returned the fix head; one file, `foundations/decisions.md`, +17 / -17). The findings file is `reports/review-whole-findings.md` (I1, I2, M1); the fix report is `reports/author-fix-1-report.md`.

The first line is FAIL only because I1 remains, as the handoff expects: it goes to the human and I ask for no fix of it here. I2 and M1 are fixed and the fix brings no new finding.

## State of each finding

**I1 — remains, exactly as found.** The fix does not touch WAY-113's text on the case, WAY-166, `project-level/technology/settle.md` or `project-level/definition_template.md`: `git diff 7c2502a7..HEAD --stat` names `foundations/decisions.md` only, and within it only the move and re-wrap below. WAY-113's paragraph still says "where no way reaches the goal, the question recommends none and says so" (now `foundations/decisions.md:1592-1600`), WAY-166 still says "the recommendation goes by the other consequences" and its *Rejected* still refuses "the step recommending nothing where no option can be used by an agent — an exception to WAY-113", and no `narrows WAY-113` is recorded. I checked the author's reason for not settling it: the frozen task's answers 1, 2 and 4, its *Context*, *Decisions in play* and *Settlements to record* do not name WAY-166, the technology step or a goal that is an agent's check; read generally, "każdy cel" would reverse a *Rejected* line without saying so. So no passage of what the human accepted gives the outcome, and WAY-25 and `agent-instructions/README.md` "Make the change" send it to the human; I agree with returning it as a question. The author's options a, b and c are the three fix directions of my finding; I do not judge between them (the human's choice).
- Contradiction: yes — WAY-166 (its binding sentence "the recommendation goes by the other consequences" and its *Rejected* line on recommending nothing), and WAY-25 (a collision with no precedence recorded).

**I2 — fixed.** The new paragraph now stands after the paragraph on refinement, at the end of the binding sentences (`foundations/decisions.md:1592-1600`). The base's first two paragraphs and the paragraph between them stand byte for byte as at the base: the fix diff's first hunk removes the paragraph from between them and adds nothing there, and `git diff 301e4eae..HEAD` shows only the added paragraph after them. "That question" at `foundations/decisions.md:1582` again follows the sentence about the question against the human's choice, and its closing "the rule above" has no new paragraph above it. No existing binding sentence is restated (WAY-263). The moved paragraph still reads: "the way recommended" is the phrase the first paragraph defines, and it no longer says anything that the refinement paragraph's "that question" could be taken to cover. The entry is 4 paragraphs; the moved paragraph is 3 sentences (checked by the foundation check, below).

**M1 — fixed.** No line the whole change adds to `foundations/decisions.md` is over 100 characters (script count over `git diff 301e4eae..HEAD`: 0 lines; at the reviewed head it was 2). The old last line of *Rejected* is wrapped where the new text starts. The words are unchanged: the sorted word list of the whole WAY-113 entry at `7c2502a7` and at `42298f2a` is identical (`diff` printed no difference), so the fix re-wrapped and moved text and changed no word.

## What the fix itself broke

Nothing found. The fix diff is a move of one paragraph and a re-wrap of the *Rejected* tail; it changes no *Verification*, *Rationale* or *Scope* word, no other file, no code and no test. The foundation check passes with the paragraph in its new place. No Critical, Important or Minor finding is new.

## Checks

| Command (from the worktree) | Exit | Result |
|---|---|---|
| `git rev-parse HEAD` | 0 | `42298f2a81d8d4600b7a3769ab5ab6795510f0f6` |
| `git diff 7c2502a7..HEAD` and `--stat` | 0 | one file, +17 / -17 |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `python -B instruction-files/check_instructions.py .` | 0 | `0 error, 0 warn, 5 info` |
| manual: added lines over 100 characters in `git diff 301e4eae..HEAD` | n/a | 0 |
| manual: sorted words of the WAY-113 entry at `7c2502a7` against `42298f2a` (`diff`) | 0 | same words |

Not run: the full suite and `gate/run_tests.py` (the cycle's own; the author ran the tests of `elements/common`, 316 OK; the fix touches no code and no test).

## Working copies

None made. Two word-list files of the check above stand under the ignored `.runs/review-whole/` (`w113-7c2502a7.txt`, `w113-42298f2a.txt`), beside the earlier index files; not removed.

## Unread material

none. (Read whole: the handoff, the findings file, the fix report, `task-cycle/review/fix.md`, the fix diff, and WAY-113 at the new head as far as its binding sentences and the move touch it; the decisions and files of my earlier report were read as it says there.)

## Searches not found or unclear

none.
