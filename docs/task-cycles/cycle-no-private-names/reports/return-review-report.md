PASS b241bb02b6046add59e96e3953ad2cd071ae7029

# Review of the return step's commits (a5ea36f..b241bb0), cycle-no-private-names

Range: `git log a5ea36f..b241bb0` is one commit, `b241bb0`; `git rev-parse HEAD` is `b241bb02b6046add59e96e3953ad2cd071ae7029`. The commit touches `foundations/decisions.md` only (+13 / -9). Code was not re-reviewed (orchestrator's note).

## Findings

Blocking: none. Critical: none. Important: none.

### Minor (within the task, not blocking)

M1. `foundations/decisions.md`, WAY-309 *Verification* (about lines 9575-9590). The binding sentence now fixes an order (the check of WAY-294 on the original first, one rewriting, a second run on the copy). The *violates* list names a case only for the second run (an entry appended for an item listed on the cleaned copy). It names no case for the order itself (the remarks check run only after the copy is cleaned, or the cleaning done as several rewritings that leave a report and the remarks in different words). The *complies* list does show the second run. A reader comparing a cycle with the entry can still see the rule from the binding sentence, so this is polish. WAY-263 grades a forbidden/required departure of the files, and here the files (`SKILL.md` steps 1-5) do match the sentence.

## Verification of the claims

1. Correction to WAY-308 (the request tells the human of a cleaned relation line). The new sentence: "a line it lists is cleaned like any other, and the request tells the human, since the reader of a plan's state may then report a conflict". Compared with the files: `task-cycle/skill/SKILL.md` section "The record before it is committed", step 3 (third bullet: "A line the check lists is cleaned like any other, and the reader may then report a conflict with exit 1 for this task, which the human sees in the request") and step 4 (last sentences: "the request tells the human, as item 12 of *For you to decide* ... gives"); `task-cycle/skill/request_template.md` item 12 (which line it was, never its text, that the reader may now report a conflict, "Merge as it stands?"); `task-cycle/record_template.md` lines 7-9 (the cleaning leaves `Task relation:` unless the check lists it). They agree. The entry's *Verification* and *Rationale* already said the same at `a5ea36f` ("a relation line the check lists is cleaned, and the request tells the human ..."; "a cleaned relation line is left out of what the request tells the human" is a violation); the commit makes the binding sentence match them. Not a new rule: the sentence only brings the binding text up to what the entry's own Verification already bound.
2. Correction to WAY-309 (order of the two checks, single rewriting). New sentence: "The check of WAY-294 runs on the original before the copy is made, the cleaning is one rewriting of every text file of the copy, and the check runs once more on the cleaned copy, where an item it lists is made to read the same in the report and in the remarks, not appended again." Compared with `SKILL.md` steps 1 (remarks check on the original, "each item reaches the remarks once, before any word is changed"), 2 (copy), 3 ("one rewriting, applied to every text file of it"), 5 (second run on the copy; an item listed there is made to read the same, "append no second entry") and with the section "The process remarks check" ("run twice: on the original in `.runs/`, and again on the cleaned copy"). They agree. The new *Rationale* sentences ("the check of WAY-294 runs first on the original because the original holds the words the reports gave ... one rewriting so that a report's item and its entry in the remarks keep reading alike") match step 1 and step 3. The *Verification* reflow in `complies` ("the same") changes no meaning.
3. Not beyond the task. The task's carried question says the cycle chooses the order of the two steps and that the cleaning must give the same words in reports and remarks; the entry now says the choice. The relation-line cleaning is an addition beyond row 1 (which said the lines stay unchanged), already in the entry before this commit and in the files; the return report marks both additions `the cycle's`. The return report states these as choices that bind after the merge (WAY-36), which `return_step.md` asks the return step to write. No new rule is introduced by the commit that is not in the files.
4. Consistency with the other entries.
   - WAY-309 "Relations: derives from WAY-308 · narrows WAY-294" holds: the sentence adds an order and a second-run rule to WAY-294's "runs before every commit" and does not contradict WAY-294's "word for word" (the cleaning is one rewriting, so both places read alike).
   - WAY-295 (a listing the orchestrator holds wrong) is not touched; the second-run listing on a cleaned copy is explained as different words and made to read the same, a different case from a script error. No conflict.
   - WAY-308 and WAY-309 agree with each other: both say a relation line stays unless the check lists it; WAY-309 names the unit of the check and its order, WAY-308 names what the cleaning does to a listed line and who is told.
   - WAY-27 / `outbound-link-reach`: the new text holds no link and no path. WAY-153 / `project-plan-state-evidence`: the new sentence in WAY-308 says only that the reader may report a conflict; the *Rationale* of WAY-308 (unchanged) already says it reports `unchecked` and proposes nothing it cannot prove; consistent with the invariant.
5. Style: no added line exceeds 100 columns (`git diff a5ea36f..b241bb0 | grep '^+' | awk 'length>101'` prints nothing).

## Notes for the orchestrator (not findings; outside the reviewed range)

- `.runs/task-cycles/cycle-no-private-names/request.md` line 86 (section "Foundation entries", WAY-308 row 1) still reads that the lines `Task relation:` and `Project relation:` "stay unchanged", and lists neither the cleaned-relation-line addition nor the order of the checks as `the cycle's` entries; `request_template.md` line 257 asks for the mark `the cycle's` for each such entry. The request should be brought in line when the orchestrator updates it for this commit.

## Declined to judge

- The code and tests at `a5ea36f` (previous reviews passed them; orchestrator's note).
- Whether the `Task source:` path cleaning's cost for the plan-state reader is acceptable (settled in WAY-308 *Rationale* by the earlier cycle; unchanged by this commit).

## Checks run (all in the worktree, no file changed)

| Command | Exit | Result |
|---|---|---|
| `git rev-parse HEAD` | 0 | `b241bb02b6046add59e96e3953ad2cd071ae7029` |
| `git log --format='%h %s' a5ea36f..b241bb0` | 0 | one commit, `b241bb0` |
| `git diff a5ea36f..b241bb0 --stat` | 0 | `foundations/decisions.md`, 13 insertions, 9 deletions |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `python -B task-cycle/private_paths_check.py foundations/decisions.md` | 0 | `checked: 1 files, 0 listed` |
| `python -B task-cycle/remarks_check.py .runs/task-cycles/cycle-no-private-names` | 0 | `checked: 7 reports, 11 items other than none, 0 not in the process remarks` |
| `git status --short` | 0 | clean (empty) before this report was written |

Not run: the full gate and the parts' tests (the cycle's own run; no code changed in the range).

## Reach beyond the dispatch

- None beyond the dispatch's list. I also read `.runs/task-cycles/cycle-no-private-names/cycle.md` and `request.md` (grep for the mark `the cycle's` and for the relation-line wording) to check where the marks stand; this produced the note above.

## Searches not found or unclear

- The mark `the cycle's`, which the handoff says the additions carry, does not stand in the committed foundation text or in `request.md` for the return step's two additions; it stands only in the return report (and the request template asks for it in the request's *Foundation entries* section). Not a defect of the range: the request had not yet been updated for this commit. See the note above.
