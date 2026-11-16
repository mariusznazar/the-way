PASS d7323f17d77b6037a7bd0b163496b1aad77d4099

# Review of correction 1 — readiness-approval-rename

Range: `4d7ad7960b10399ff64d67ca1b98b15e97dac375..d7323f17d77b6037a7bd0b163496b1aad77d4099`, one
commit (10 files, +219 −176). `git rev-parse HEAD` in the worktree gives `d7323f17…`. The human's
remarks (`reports/correction-1-remarks.md`) stand in place of a findings file.

## The remarks

1. **Item 1 (let through)** — no work asked; none done. Made.

2. **Item 2 ("entry" for an item of a list in the description of a cycle's record)** — made, with
   the two qualifications below.

   **What was done.** Every prose use I found of "entry"/"entries" for an item of a list nested
   under an item of a cycle's record now says "sub-item". These uses were in:
   - `task-cycle/record_template.md`, `task-cycle/skill/SKILL.md`, `task-cycle/skill/correction.md`
     and `task-cycle/skill/reserved_return.md`;
   - `process-audit/SKILL.md`, and the docstrings, comments and messages of
     `process-audit/audit_count.py` and `process-audit/record_items.py`;
   - WAY-309, WAY-337, WAY-404 and WAY-405, and the comments and expected messages of the two test
     files.

   I searched by WAY-97 myself (`git grep -i -w "entry|entries"` over every tracked file but the
   generated entry points, then read each hit outside plainly foundation-entry contexts). Apart from
   the two places named under Minor 1 and 2, every use left is of another kind.

   **The word chosen.** The remark asks for "row" where it fits. "Row" does not fit here: these are
   bullet lists nested under an item of the record (`- Review rounds:`, `- Discarded attempt:`,
   `- Process remarks on the-way:`), not lines of a table. The record's tables (Slices, Events, the
   questions table) already say "row". "Item" is taken by the record's own top-level lines ("the
   record's item *Review rounds*"), so "an item of the item" would be ambiguous. "Sub-item" names
   exactly what is meant. The author's reason holds, and the word is used the same way in all ten
   files.

   **Qualification a — the glossary.** The remark says "add the word to the glossary if it is new
   there". "Sub-item" is new to the glossary, and the author added no entry. Its reason is WAY-95:
   a word takes an entry only where the-way means by it something other than what a reader who knows
   the field takes it to mean, and "sub-item" means here exactly what it means anywhere. WAY-95's own
   *Verification* gives "every noun of the decision log takes an entry" as a violation. Writing the
   entry would therefore make the change do what a foundation entry forbids (WAY-263). Leaving it out
   follows the foundation and the purpose the remark states ("keep it consistent with the glossary"),
   but not the remark's literal words. That is a choice for the human, not a defect of the code. The
   request's description has to say plainly that no glossary entry was added and why, so that the
   human can ask for it (and for the change of WAY-95 it would need) instead of finding it silently
   left out.

   **Qualification b — the claim the remark wants true.** The remark wants "entry means only a
   foundation entry" to be true after the change. That holds for the prose that describes a cycle's
   record. It still fails in four places:
   - the test method names (Minor 2);
   - the plan's log of changes: WAY-145 (`foundations/decisions.md:3814`, "an entry in the plan's log
     of changes") and `project-level/lead/skill/SKILL.md:81` ("their change-log entries"). This is the
     same "item of a list" meaning, in a project plan rather than a cycle's record;
   - the registry of runs of the gate: `task-cycle/gate_times.py:183`, `:194`, `:202` and `:317`, the
     invariant `gate-times-refuses-impossible-entry`, and the passage on the registry in
     `foundations/decisions.md`;
   - the generic "file/entry/section": `project-level/lead/conversation_template.md:77` and
     `project-level/lead/answering.md:23`.

   The last three are outside what the remark binds: item 2 named the record, and so did my own
   finding that it answers, which missed these three. They are listed below as outside the scope.
   The description should name them, as the author proposes, because the remark's stated purpose is
   not met while they stand.

## Findings

**Critical / Important:** none.

**Minor (within the correction; go to the request's list):**

1. `process-audit/test_record_items.py:423` — a comment still says "a doubled item, an entry in
   neither form, a findings file named twice". Here "entry" is a sub-item of *Review rounds*, the
   meaning the correction renames everywhere else, including the neighbouring comment at line 422.
   It was missed. The fix is one word.

2. **Test method names still say "entry"/"entries" for a sub-item of the record:** about 24 names.
   Examples:
   - `process-audit/test_record_items.py:96` `test_one_entry_for_each_attempt_gives_yes_where_any_marker_is_an_open_design_choice`,
     `:112`, `:154`, `:166`, `:193`, `:353`, `:370`, `:387`, `:454`, `:491`, `:524`;
   - `process-audit/test_audit_count.py:480` `test_the_corrections_item_before_the_remarks_item_is_not_among_its_entries`,
     `:489` (whose test data the correction did change: "its own sub-item"), `:1205`, `:3828`.

   The author keeps "code names". The task's own rule (To do 9: `entry_path`, `REGISTER_ENTRY` stay)
   supports that for identifiers, so I do not grade it higher. But a test name in the-way is a
   sentence about the behaviour (`guidelines/testing.md`, recipe *unit*, *Shape*). The same change
   renamed test names for both earlier renames (the locations key in `test_audit_count.py`, and
   `GateRecord` → `ApprovalRecord` with its tests). So the claim of remark 2 stays false in the
   English an agent reads in these files. Renaming them is mechanical and touches no assertion. If
   they stay, the description should say that the claim holds for prose and not for identifiers.

3. **Ragged rewraps and one new line over 100 columns.**
   - `foundations/decisions.md`, WAY-309 *Verification* ("…appends a second sub-item to the remarks
     for / an item that the check of / WAY-294 lists…"), and similar short lines in WAY-337 and
     WAY-405.
   - `task-cycle/record_template.md:60` goes from about 98 to 101 characters.
   - The other long lines in the diff were over 100 before.

   No word changed. This is cosmetic.

**Outside the scope of the remarks (to the request's list):**

- The plan's log of changes (WAY-145, `project-level/lead/skill/SKILL.md:81`), the gate-run registry
  (`task-cycle/gate_times.py`, `gate-times-refuses-impossible-entry`, its decision), and
  "file/entry/section" (`project-level/lead/conversation_template.md:77`,
  `project-level/lead/answering.md:23`): "entry" in meanings other than an entry of the foundation,
  as described under remark 2b.

## Declined to judge

- The author's kinds 4, 5, 7 and 8. Kind 4 is the output of tools (`git worktree list`, git trees,
  session transcripts); kind 5 is the decision log in its scripts; kind 7 is "entry point"; kind 8 is
  test data that holds foundation entries. These are field meanings, foundation meanings or another
  word, outside the remark.

## Against the foundation and the guidelines

- **Decisions changed (WAY-309, WAY-337, WAY-404, WAY-405), each read whole.** Only the word
  changed: "entry" → "sub-item", and in WAY-309's rationale "a report's item and its entry in the
  remarks" → "its copy in the remarks". In WAY-309 the sub-item is the remark's copy of the report's
  item, so "copy" is exact. Each sentence keeps its meaning: binding sentences, *Verification*,
  *Rationale* and *Rejected* alike.
- **The `# decision:` quotes in the tests** (WAY-337 "…takes a sub-item for a review", WAY-404 "…into
  the sub-item of the round…", WAY-405 "Where the lines are sub-items at one indent alone…" and
  "…are not sub-items at one indent alone") equal the changed sentences. `foundation_check.py`
  reports 0 errors (below).
- **Trust boundary (`audit_count.py`; also `record_items.py`, which the part map names for
  process-audit).** Only docstrings, comments and messages changed; no regular expression,
  condition or exit path. I ran 23 crafted records through `read_contradiction`, `review_rounds`,
  `remarks_count` and `read_too_large`, in a worktree of the old head `4d7ad796` and in the reviewed
  worktree. The records covered:
  - *Process remarks*: none, two sub-items, no sub-items, text beside, wrong indent, a plain line;
  - *Review rounds*: none, marked no, marked yes, unmarked, no sub-items, text beside, neither form,
    wrong indent, the review form;
  - *Discarded attempt*: marker, two sub-items, a sub-item with no marker, wrong indent, text beside;
  - *Slices returned too large*: none, two, prose.

  Every verdict is the same at both heads. The only difference is the renamed word in the reasons
  (compared after mapping "entry" to "sub-item": 0 differences). Nothing is accepted or refused
  differently.
- **Changed tests, against "Changing an existing test" (`guidelines/testing.md:95-106`).** The
  expected values changed are the message substrings `BESIDE`, `SILENT`, "does not give its
  sub-items" and "beside its sub-items", and the contradiction reason. Each follows the renamed
  message word for word. The cause is on the side of the requirement (the human's remark 2), and the
  evidence is `reports/correction-1-remarks.md`. Both are stated in the author's report and the
  commit. No assertion is loosened (`assertIn` stays `assertIn`, `assertEqual` stays `assertEqual`),
  no test is removed or skipped. Two data texts changed ("belongs to the item above", "its own
  sub-item"); neither changes what the reading under test sees, since the content of a line is not
  what those tests read.
- **Rewraps.** Lines the rename lengthened were broken again with no word changed. See Minor 3 for
  the ones left ragged or long.

## Checks run

- Crafted records at `process-audit/record_items.py` and `process-audit/audit_count.py`:
  `python -B .runs/review-correction/crafted.py <checkout> <out.json>`, run on a worktree of
  `4d7ad796` (`.runs/review-correction/old`) and on the reviewed worktree — exit 0 both; JSON
  comparison after mapping the word — 0 differences.
- `python -B elements/common/foundation_check.py` — exit 0, "0 errors"
- `python -B gate/run_tests.py gate` — exit 0 (36 tests)
- `python -B gate/run_tests.py product-guidelines` — exit 0 (14 tests)
- `python -B gate/run_tests.py elements/common` — exit 0 (270 tests)
- `python -B gate/run_tests.py task-cycle` — exit 0 (534 tests, 2 skipped)
- `python -B gate/run_tests.py process-audit` — exit 0 (276 tests)
- Manual searches (`git grep -n -i -w -E "entry|entries"` over all tracked files except `.runs/`,
  `.claude/`, `.agents/`; the same for lines starting with the word, to catch a phrase split across
  lines; `def test.*entr` over the test files): results as under remark 2 and Minor 1–2.
- A scan of added lines over 100 characters in the correction's diff: results as under Minor 3.
- Not run: the full gate (handoff); `project-level`, `agent-instructions` (no file there changed).

## Working copies

- `.runs/review-correction/old`, a worktree of `4d7ad796` for the crafted comparison — removed with
  `git worktree remove --force`, then `git worktree prune`.
- `.runs/review-correction/` held the crafted script, its two outputs, the word diff, the search
  lists, the extract of the four decisions and the outputs of the test runs — removed before return.
  Nothing remains.

## Unread material

- WAY-309, WAY-337, WAY-404 and WAY-405 read whole. WAY-145 read in the earlier review whole; here
  only its sentence holding "entry". WAY-95 and WAY-263 read in the earlier review (WAY-95 whole).
- `process-audit/record_items.py` and `process-audit/audit_count.py`: read in the diff, with the
  crafted run standing for their behaviour, not read whole. The test files were read in the diff and
  by search.
- `task-cycle/gate_times.py`, `project-level/lead/answering.md`, `project-level/lead/conversation_template.md`:
  read only at the lines holding the word.

## Searches not found or unclear

- The remark says "about thirteen places". The renamed uses are about 120 lines, because the audit's
  scripts, their tests and four decisions name the same items. This agrees with the author's report;
  no place the remark means was found outside the ten files, except the comment of Minor 1 and the
  test names of Minor 2.
- The remark's clause "add the word to the glossary if it is new there" stands against WAY-95 for a
  plain word such as "sub-item" (qualification a). Which the human wants is unclear from the remark
  alone.
