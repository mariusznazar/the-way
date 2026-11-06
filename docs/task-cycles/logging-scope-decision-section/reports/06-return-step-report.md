# Return step — logging-scope-decision-section

**Status:** done
**Worktree:** `C:\Storage\repos\the-way\.runs\worktrees\logging-scope-decision-section`, branch `task/logging-scope-decision-section`, reviewed head `f604e93`.
**Commits:** `87377b2` docs: the request template states that the own-sections heading is the one heading omitted (`task-cycle/skill/request_template.md`, 4 added / 2 removed).

## Foundation compared with code

Entries the change writes or changes and those the task names, each compared with the files of the change:

- **WAY-287** (row 1, written by the foundation step as the cycle's record gives, confirmed, not written twice). Binding sentence lists "the additions a change makes to a product's logging scope" — matches template item 10 (`task-cycle/skill/request_template.md`, "For you to decide", item 10). *Rejected* holds B, C and the general item as the task's *Questions to settle* 1 gives them, with the word-search qualification from the fix. Consistent with the code: the section is the one the template and `request_check.py` read. No change needed.
- **WAY-274**: unchanged, as the task requires. Its "the human sees it at the merge" matches WAY-287's new kind. No change.
- **WAY-286** (skeleton and lower-part order). Its *Verification* says "a section with nothing in it is left out" is a violation. The own-sections heading is omitted only where the task has no own sections, which the task settles (item 5); I judged it is not "a section with nothing in it", since WAY-286 lists the task's own sections among the lower part's contents and never requires them. Judgment, not an edit. If the human reads it otherwise, WAY-286 needs a narrower wording by decision; that is a choice for Mariusz, not a return-step correction.
- **WAY-290** (form check). Lists headings order and level, content or `none`, and the block's language; "the script judges no content". The placeholder rejection is a heading-form check, and the BOM read is file handling; both fit the listed scope. No change.
- **WAY-10**: no change.
- **Template prose** (`task-cycle/skill/request_template.md`): the rule "A section with no content reads `none`, and never disappears" and "Every variant keeps every heading" were unqualified and contradicted the omitted own-sections heading. Corrected in this change: the exception is named in both places (commit `87377b2`).

## Decisions

- Changed: WAY-287 (row 1, earlier in this cycle; confirmed here).
- Written here: none. No decision follows from the change beyond WAY-287.

## Invariants

- Written here: none. The task, a decision or the human sets no new rule: the BOM read and the placeholder rejection are form behaviour that WAY-290 covers, and the script-level invariants (`script-language`, `script-imports`, `script-subprocesses`) are unchanged: no new import, no subprocess, Python file only.

## Environment facts

- Written here: none. The UTF-8 byte order mark that PowerShell may write is named in a code comment (`task-cycle/request_check.py`, `read()`). No entry rests on it: no decision's *Based on* and no invariant's *Rests on* cites it, and `utf-8-sig` gives the same result with or without the mark. The existing `utf-8` environment fact (`foundations/environment_facts.md`) is not contradicted.

## Glossary terms

- Written here: none. "placeholder" and "the task's own sections" are used in their ordinary sense in the template and the script; no entry of `foundations/glossary.md` holds them, and no word is used against an entry.

## Part-map changes

- Written here: none. `task-cycle` (Files `task-cycle/**`, dependencies, trust boundary) and `decisions` (Files `elements/decisions/**` and `foundations/decisions.md`) still describe what the change touches; no file moved, no part split.

## Projected entries

- none (the change is independent; no project definition projects an entry into it).

## Rows of *Settlements to record* written

- Row 1 (decision): written earlier as WAY-287; confirmed here, not written again.

## Checks

| Check | Command | Exit | Result |
|---|---|---|---|
| Task-cycle tests (before template edit, after it) | `python -B gate/run_tests.py task-cycle` | 0 | `Ran 94 tests`, `OK` (twice) |
| Foundation check | `python -B elements/common/foundation_check.py` | 0 | `0 errors` (twice) |

Not run: the whole gate. Not touched: `.runs/gate-check`.

## Searches not found or unclear

- Whole-foundation search for WAY-287 references and for the touched words (`placeholder`, `own sections`, `byte order`, `BOM`, `request_check`, `PowerShell`, `utf-8`): found the expected references (WAY-161 derives from WAY-287; WAY-286 and WAY-287 describe the section's contents); nothing else needed a change. The search is by words, not a reading of every entry.
- WAY-286's "a section with nothing in it is left out" against the omitted own-sections heading: judged compatible, but it is a reading. Flagged above as a choice for Mariusz.
- Whether the BOM comment in `request_check.py` is an environment fact that should be written: judged no (no entry rests on it).
- The reviewer's aside about WAY-114 and WAY-172 (the human seeing something at the merge) was not checked in this stage; it does not bear on the return step's entries.

## Addendum — repair of the report (no code, no commit)

Added on the branch head `23bb052` (the target merged in). Nothing above this addendum was changed. The item numbers in this report's earlier text refer to the numbering before the merge: after it, the target's item 10 ("A listing of the remarks check held wrong") stays 10, and the logging-scope item is 11 in `task-cycle/skill/request_template.md`.

### Own-work check (section 3 of the make-change skill)

- **Requirement most likely unmet:** the two changed template sentences (the rule under the skeleton, and the note under `## <…>`) state an exception the script does not enforce, or the script's placeholder message contradicts the template.
- **Checks and what they showed:**
  - `grep -n "never disappears\|omit this heading\|^## <…>\|keeps every heading" task-cycle/skill/request_template.md`: the rule at lines 48-49 says the own-sections heading is "the one exception ... omitted where the task has none"; the skeleton note at lines 104-105 says "omit this heading altogether: it is not written with `none`"; line 252 says "save the heading of the task's own sections where the task has none". All three agree.
  - `python -B task-cycle/request_check.py <description with the placeholder heading and none under it> --task .runs/task-cycles/logging-scope-decision-section/task.md`: exit 1; the placeholder line reads "omit the heading where the task has no sections of its own, or write in its place the heading of the task's own section", which matches the template note.
  - The same description with the placeholder heading and its `none` deleted (`sed` on the `## <…>` line and the two lines after it): zero placeholder messages. The script does not require the own-sections heading, as the template says.
  - `python -B gate/run_tests.py task-cycle` at head `23bb052`: exit 0, `Ran 139 tests`, `OK`. The 94-test runs above were at the heads before the merge. The template's skeleton test and the placeholder tests pass at this head.
  - `python -B elements/common/foundation_check.py`: exit 0, `0 errors`.
- **Files changed:** `task-cycle/skill/request_template.md` in commit `87377b2`: 4 added, 2 removed. Unchanged by the repair.
- **Reaches beyond the dispatch:** none.
- **Choices, with the way rejected and its cost if wrong:**
  - Qualified the rule "never disappears" with the one exception. Rejected: leave it unqualified and count the omitted heading as a violation. Cost if wrong: the template contradicts itself, and an agent may write the placeholder with `none` to satisfy it.
  - Left WAY-286 unchanged; its "a section with nothing in it is left out" stays a judgment (see the body of this report). Rejected: narrowing WAY-286 by an edit. Cost if wrong: an entry changed without the human's decision.
- **Searches not found or unclear:**
  - The user's script rule was read only during this repair, after the earlier Python edits in the cycle. The line endings of the edited files were unchanged, as the diff sizes show.
  - The reviewer's aside on WAY-114 and WAY-172 is still not checked; it does not bear on these sentences.
  - An earlier append went to the worktree root by mistake; it was an untracked file holding only this addendum, and it was removed.
  - Nothing else new.
