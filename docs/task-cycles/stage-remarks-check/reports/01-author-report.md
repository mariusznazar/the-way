# Report of the one author — task stage-remarks-check

**Status:** done

**Commits** (branch `task/stage-remarks-check`, base `b96cfff`):

- `2a4847e` task-cycle: remarks check lists stage-report items missing from the process remarks
- `5e90498` foundations: WAY-294 to WAY-296, the remarks check and the one form of the process remarks

Worktree clean after both commits.

## Files changed (added / removed lines, `git diff --numstat b96cfff HEAD`)

| File | + / - |
|---|---|
| `task-cycle/remarks_check.py` (new) | 354 / 0 |
| `task-cycle/test_remarks_check.py` (new) | 428 / 0 |
| `task-cycle/record_template.md` | 13 / 2 |
| `task-cycle/skill/SKILL.md` | 47 / 3 |
| `task-cycle/skill/correction.md` | 3 / 1 |
| `task-cycle/skill/blocked_finding.md` | 2 / 1 |
| `task-cycle/skill/reserved_return.md` | 2 / 1 |
| `task-cycle/skill/request_template.md` | 9 / 1 |
| `foundations/decisions.md` | 95 / 0 |

## What was made

1. **Script** `task-cycle/remarks_check.py RECORD` (standard library only). Reads `reports/*report.md`
   in name order, takes the **Searches not found or unclear** section in both forms (a heading of
   any level, or a bold label whose colon is inside, outside or absent, at line start or as a list
   item), splits it into items, drops items that read `none`, and lists each other item that the
   `cycle.md` process remarks do not hold word for word, as `<report path>: <item>` plus a last line
   `checked: ...`. Exit 0 / 1 / 2. It only lists and writes nothing.
2. **Process text.** New section "The process remarks check" in `task-cycle/skill/SKILL.md`
   (run, append each listed item word for word with stage name and full report path, run again until
   exit 0, record the run under *Verification*; and "A listing you hold wrong": script not changed,
   archive written, case entered in the remarks, item in *For you to decide*, check named in
   *Checks*). Step 12, step 9.4 stop, `correction.md`, `blocked_finding.md` and `reserved_return.md`
   each point to it before the commit that adds the record. `request_template.md` gets item 10 of
   *For you to decide*, a *Checks* mention and a variant row.
3. **Template** `task-cycle/record_template.md`: the block is the list item
   `- Process remarks on the-way: ...` with one entry `- <stage name>, <full report path>: <item>`
   indented under it (and an `<the orchestrator>: ...` entry for its own remarks), last item of the
   record, nothing at its level after it.
4. **Foundation** WAY-294 (row 1), WAY-295 (row 2, narrows WAY-294), WAY-296 (row 3), written by
   hand in the form of `elements/decisions/template.md` through the steps of the decisions skill.

## Checks (command, exit code)

- Tests written first: `python -B gate/run_tests.py task-cycle` against a stub `remarks_check.py`
  (functions returning empty values): exit 1, 34 failures and 1 error, each on an assertion or on
  the empty output of the stub, not on a missing module.
- `python -B gate/run_tests.py task-cycle` after the implementation, the final run on the commits:
  exit 0, 137 tests OK (the earlier run after the first implementation: exit 0, 136 tests).
- `python -B elements/common/foundation_check.py` after the three decisions: exit 0, `0 errors`.
- Acceptance run (below): `python -B task-cycle/remarks_check.py <dir>` on the four extracts:
  exit 1 on each, as expected.
- Mutations run by hand on copies of the script in the scratchpad (the test file and template copied
  beside it): flipping the repeated-item count, the `none` test (emphasis/full stop stripping), the
  list-label end, the heading detection, the `*report.md` filter, the cut of the remarks block, the exit
  code, fenced-code handling and `utf-8-sig`: all caught after I added the byte-order-mark test (that
  mutation first survived). Not caught: removing `sorted` over the report names (Windows lists
  files in name order, so no test can tell); I left it.
- Not run: the product's gate `python -B gate/run_tests.py` (the orchestrator's, per the handoff).

## Own-work check (WAY-164)

- **Requirement most likely unmet:** the script must find every item of the real reports, in the
  forms agents really write, not only in my fixtures (task *To do* 1 and the second acceptance
  criterion).
- **Check:** ran the script on 4 extracts of the `loop2` archives and compared it with a second,
  independent count: (a) every report of the extracts has the section; (b) every report for which
  the script finds no item has a section that reads `none` (`None.`, `none`), listed by hand: 13
  entries over the four extracts, all `none`; (c) for each report using the heading form in the
  three main archives, the script's item count equals the count of `- ` lines other than `none` in
  the section, except five reports.
- **What it showed:** the five differences are all items the bullet count cannot see, and are
  correct: `none. Note: ...` and a trailing paragraph inside the section
  (`reset-hasla` 15, 29, 30 and `kopia-bazy` `slice-4-report.md`, one item each) and a closing
  paragraph (`reset-hasla` 33, 5 items against 4 bullets). No missed item found. The check showed
  one real gap in my tests: a BOM left in the text hides a first-line section; I wrote the test
  and the fix (`utf-8-sig`) was then caught by it.

## Acceptance run

The archives were taken with `git show` (never checked out) from `C:\Storage\repos\loop2` into the
scratchpad `C:\Users\Mariusz\AppData\Local\Temp\claude\6b84451ec494cdda\821349a6-1a76-4a81-8e07-c83682a50609\scratchpad\loop2\<slug>\`
(`cycle.md` and the files `reports/*report.md`, at `31ac651` plomyk, `b311814` reset-hasla,
`d79c8e4` kopia-bazy, `67620ff` first kopia-bazy). Command, per archive:

```
python -B task-cycle/remarks_check.py <scratchpad>\loop2\plomyk
python -B task-cycle/remarks_check.py <scratchpad>\loop2\reset-hasla
python -B task-cycle/remarks_check.py <scratchpad>\loop2\kopia-bazy
```

Exit 1 each. Output, the items the task's *Context* describes (paths shortened to the archive; item
text cut at about 110 characters here):

```
plomyk/reports/06-return-step-report.md: Unclear: whether D-175's last sentence („A character without nature energy has no spells and pays nothing for them”) needs code today. ...
reset-hasla/reports/37-reconciliation-report.md: „The numbers in `guidelines/` tables”: unclear whether the handoff means decision numbers or counts. I checked both.
reset-hasla/reports/37-reconciliation-report.md: The old numbers D-214 to D-219 still stand, in this task's meaning, outside the tracked files: ...
reset-hasla/reports/37-reconciliation-report.md: The vault's folder `Notes/Projects/(P) Loop` names none of D-214 to D-219; ...
reset-hasla/reports/38-reconciliation-review-report.md: `scripts/build.mjs --check` covers `tsconfig.browser.json` and `tsconfig.server.json` only, ...
reset-hasla/reports/38-reconciliation-review-report.md: A first search for the schema's version in `src/server/database.ts` by guessed names found nothing; ...
reset-hasla/reports/38-reconciliation-review-report.md: Which request lines the orchestrator will rewrite, and when: not stated in the handoff, so O1 names all nine.
kopia-bazy/reports/slice-6-fix-report.md: None unresolved. Unclear: `rsync` availability on a new host is not stated by any source; ...
kopia-bazy/reports/correction-2-report.md: Head `e69034c` named in the handoff was the head at start; commits since are mine only.
```

Summary lines: plomyk `checked: 3 reports, 13 items other than none, 7 not in the process
remarks`; reset-hasla `checked: 38 reports, 84 items other than none, 6 not in the process
remarks`; kopia-bazy `checked: 41 reports, 129 items other than none, 8 not in the process remarks`.

Full outputs: `...\scratchpad\loop2\plomyk.out`, `reset-hasla.out`, `kopia-bazy.out`,
`kopia-bazy-first.out` (same directory as above). Observations:

- The task says the two `reset-hasla` reports have two items each; the script lists three each
  (37 and 38). I checked them by eye: each is a separate bullet and none stands in `cycle.md`.
- `plomyk` also lists three items of `04-whole-review-report.md`. They stand in the record, but as a
  second top-level entry (`- From stage review-change ...`) that opens with no word the nightly
  digest cuts on, so by the digest's cut they are outside the remarks block. That is the old form
  failing the digest too, not a script error.
- `kopia-bazy` also lists `correction-2-review-report.md` (one item), three entries that begin
  `none. ...` or `none for the code; ...` (`slice-2-fix`, `slice-4`, `slice-7`) and two of
  `slice-2-fix-review-report.md`; by the literal rule "other than `none`" they are items. The first
  `kopia-bazy` archive (`67620ff`, run as `kopia-bazy-first`) lists 5 items: `slice-2-fix`,
  `slice-2-fix-review` (two), `slice-4` and `slice-6-fix`.

## Choices made (the way rejected and its cost if wrong)

- **Which files are reports:** `reports/*report.md`, so a handoff (it quotes the section name as an
  instruction), `*-findings.md` and logs are not read. Rejected: every `.md` in `reports/` (false
  items from handoffs). Cost if wrong: a stage report whose name does not end in `report` is not
  read; the cycle names its reports so (the real archives all do).
- **Item:** a list item with its continuation lines and sub-items joined into one line, or a paragraph
  where the section is no list; text after a bold label on its line is the first paragraph. Items are
  printed as one line (whitespace collapsed). Rejected: printing the original lines (the appended copy
  would then differ from the printed text only in whitespace anyway, and the match ignores whitespace).
- **`none`:** an item reads `none` when, after stripping `*`, `_`, backticks, spaces and full stops, it
  is `none` in any case. `none found`, `none.` followed by more text, and `None unresolved. ...` are items
  (the literal reading the task chose). Cost: noise in the nightly review, named in the task.
- **Matching:** only inside the blocks of `cycle.md` that open as `cycle_remarks_digest.py` cuts them
  (a port of its `_opens_block` and `extract_remark_blocks`; the script cannot import it, it lies
  outside the repository), whitespace collapsed, exact words and case. Rejected: matching anywhere in
  `cycle.md` (an item can stand in the Events table and still never reach the review). Cost if wrong:
  the port must follow the digest; a change to the digest's rules is not seen here.
- **Repeats:** an item that two reports give is listed again unless the block holds it twice. Not in the
  task's words; it follows WAY-260 ("without combining repeated items") and is bound in WAY-294. Cost
  if wrong: a repeated item the orchestrator rightly wrote once is listed again.
- **Section end for a bold label that is no list item:** the next heading, rule, or non-list line that
  starts with bold text. Cost: a section whose paragraphs start with bold text outside a list ends
  early and its tail is not read; the real archives hold none.
- **A listing held wrong:** the item is not appended; the case is entered in the remarks as an entry of
  the orchestrator's own and in *For you to decide*, and *Checks* names the check. The request's state
  is left as it is for its other causes (the task names no draft state; WAY-291's draft state is not
  copied). Rejected: draft state as for the form check. Cost if wrong: a request marked `ready` carries
  a decision item; its first line says whether anything waits below, as the template already allows.
- **Record in *Verification*:** the last run of the remarks check is recorded there, not in a new field
  of *Request handoff*.
- **Order in step 12:** the check runs right after `cycle_stages.py` and before the description is
  written, so that a listing held wrong reaches the description; again before the commit if a report
  or remark changed.
- **No `reports/` directory** gives no listing (exit 0); a missing `cycle.md` is exit 2.
- **Scope of edits beyond the three files named:** `blocked_finding.md` and `reserved_return.md` also
  commit a record (the handoff said "the blocked variants"), so each got the call; `request_template.md`
  got item 10, a *Checks* mention and a variant row.

## Reaches beyond the handoff

- `foundations/part_map.md` (the `task-cycle` entry and its neighbours, lines 85 to 130) and
  `foundations/glossary.md` (grep of headings and of "remark"): to see whether the part map or a
  glossary term changed. Neither needed a change: `task-cycle/**` covers the new files, and no glossary
  entry holds "process remarks" or "report".
- `elements/common/way_of_working.md`, `elements/common/rules.md`, `elements/decisions/template.md`,
  `elements/decisions/examples.md`, `elements/decisions/skill/read.md` and `decide_entry.md`: the
  skill of a decision names them; read whole for the three entries.
- `foundations/invariants.md` lines 90 to 125 (`script-language`, `script-imports`,
  `script-subprocesses`): to see that the new script meets them. It imports only standard-library
  modules and starts no program.
- Grep over the repository for "process remarks", "Searches not found", `cycle_stages`, `request_check`
  and `docs/task-cycles`: found the places that commit a record (SKILL.md, `blocked_finding.md`,
  `reserved_return.md`) and confirmed no other file names the remarks.
- `C:\Storage\repos\loop2` through `git show`/`git ls-tree` for the four archives, the 38 reports of
  `reset-hasla` and the files of `kopia-bazy`; `C:\Storage\The Brain\...\cycle_remarks_digest.py` as the
  handoff names it.

## Foundation step

- Written: WAY-294 (row 1), WAY-295 (row 2), WAY-296 (row 3), each marked `row <n>`; meaning in
  English: WAY-294 the cycle compares the reports with the remarks by script before every archive
  commit and appends what is missing until nothing is listed; WAY-295 a listing the orchestrator holds
  a script error neither stops the archive nor changes the script, and the case goes into the
  remarks and the request; WAY-296 the process remarks stand in one form, the one the template gives.
  Meaning in the task's language (Polish): WAY-294 przed każdym zapisaniem archiwum cyklu skrypt
  porównuje raporty z uwagami procesowymi, a orkiestrator dopisuje brakujące pozycje, aż skrypt
  niczego nie wymieni; WAY-295 zgłoszenie, które orkiestrator uważa za błąd skryptu, nie zatrzymuje
  archiwum ani nie zmienia skryptu, a przypadek trafia do uwag i do opisu requestu; WAY-296 uwagi
  procesowe stoją w jednej formie, którą ustala szablon zapisu.
- Search of the whole foundation (WAY-33): grep of `foundations/` for "process remark", "remarks",
  "Searches not found", "word for word", "request_check", "form check". Entries found and read whole:
  WAY-260 (the text that says where the items go: "into the cycle record's *Process remarks on the-way*"
  already names the item the template now fixes and needs no edit; its *Verification* already says
  the orchestrator may not omit, edit or combine an item, which the script now checks), WAY-148,
  WAY-290 and WAY-291 (the pattern), WAY-286. No collision, no entry changed, no new glossary term
  (no word is used in another meaning than its usual one), no part-map change, no invariant (none
  set by the task or a decision).
- Two rows had a `Rejected` with only the ways the source of the row keeps: WAY-294 has the two ways
  under question 1, WAY-295 the two under question 4, WAY-296 `unknown` (question 2 keeps no way not
  chosen).
- The "critique before collective review" step of `way_of_working.md` needs a fresh agent; I may not
  dispatch one, so it did not run on the three entries. They were accepted as rows with the task.

## Problems observed

- `plomyk/cycle.md` holds the second stage's items as a sibling entry the digest does not cut (see
  above). Evidence: `remark_blocks` on that file returns one block, ending before
  `- From stage review-change ...`.
- No test or code fault is known. `Counter[str]` in an annotation and `from __future__ import
  annotations` keep Python 3.14 as `.python-version` declares.

## Searches not found or unclear

- A test guideline for the-way's own scripts (WAY-215): not found, as the handoff says; I followed
  the existing tests of `task-cycle/` (unittest, fixtures written in the test file, expected values
  written out).
- The stage name for a report cannot be read from a path (a report path such as `37-reconciliation-report.md`
  does not give it reliably), so the script prints only the report path and the orchestrator takes the
  stage name from the Events; unclear whether the task wanted the script to print a stage name too.
- The task says `reset-hasla` 37 and 38 hold two items each; the script finds three each. Unclear
  where the count of two came from (a count of only the unclear items, or of the items other than
  `none found`).
- Whether a report with no recognised section (a form I did not see) should be listed: the task asks
  only for items, so the script lists nothing for it. A report that lacks the section is repaired
  by the orchestrator at the report's arrival (WAY-260), not by this script.
- Whether the "critique before collective review" step applies to three entries already accepted as
  rows of a task document: not run (no subagents for me).
