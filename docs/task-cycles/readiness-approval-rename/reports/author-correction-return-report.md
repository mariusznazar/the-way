# Return step after correction 1 — report

**Status:** done. **Commits:** none (the comparison found nothing that no longer matches).

## Foundation compared with code

Head `d7323f17`. Compared with the files of the repository:

- **The four decisions** (WAY-309, WAY-337, WAY-404, WAY-405, word only): their sentences use "sub-item" for an item of a list
  under an item of the record; the files that restate them say the same: `task-cycle/record_template.md` (*Discarded attempt*,
  *Review rounds*, *Process remarks on the-way*), `task-cycle/skill/SKILL.md`, `correction.md`, `reserved_return.md`,
  `process-audit/SKILL.md`, `process-audit/audit_count.py` and `record_items.py` (docstrings and messages). Each `# decision: WAY-… "…"`
  quote of a test equals the sentence of its decision as changed (`git grep` of the quote lines: none still holds "entry"; the
  tests of `process-audit` passed in the correction, and `foundation_check.py` gives 0 errors).
- **Invariants whose tests cite them**: `foundations/invariants.md` holds no sentence that describes the record's lists with
  "entry" (the uses in it are foundation entries, the projected entries of the plan check, the skill entry points and the registry
  of the gate, `gate-times-refuses-impossible-entry`, which stays as a kind left). The invariants of the audit that mention the
  record (`audit-count-refuses-record-links` and the like) name no list item. Nothing to change.
- **Glossary**: `entry` (unchanged, *Not:* none) is true for the record's lists too, apart from the kinds the correction report left
  (the plan's log of changes, the registry of runs, outputs of tools, a generic "file/entry/section"); `gate` and
  `projected entry` unaffected by the correction. Nothing to change.
- **Part map**, parts `process-audit` and `task-cycle` (and trust boundaries `process-audit/audit_count.py`,
  `process-audit/record_items.py`): the responsibilities and file lists say nothing about "entry" for the record's lists;
  `record_items.py` stands as a trust boundary and the correction changed only its words and messages, not what it accepts.
  Nothing to change.
- **Sentences still describing the record's lists with "entry"**: `git grep -w entry|entries` over the files above and over the log,
  filtered to `round|attempt|remark|record|stage report`: only foundation entries, code names and test variables.
- **WAY-95 and WAY-263 read whole now.** WAY-95: a word takes a glossary entry when it means in the product something other
  than a reader who knows the field takes it to mean, or is used more narrowly where the field's reading would make a sentence
  read wrongly. "Sub-item" is a word of the field (a list item nested under a list item) and is used in that meaning; no sentence
  reads differently for the field's reading, so it takes no entry. "Row" and "item" likewise. The reason the correction gave
  holds. WAY-263: a changed file that repeats an entry more broadly or without a qualification is Important; I compared the
  restating files with the four decisions as changed and found each repeats the same item and sub-item structure with the same
  qualifications (the tests and docstrings give the same forms as WAY-404/405 state). No departure.

## Does a decision or invariant need a sentence on the choice of the word?

No. WAY-95 gives no entry for "sub-item", WAY-99 and WAY-97 already hold the rule that one word does not carry two meanings and
that the author rewrites each use whose meaning moves; the choice of "sub-item" over "row" is the correction's choice among
equal ways and binds later wording only as a habit. The return step puts such a choice in the questions table of the record (a
row for the orchestrator), not in the log, and writes an invariant only for a rule the task, a decision or the human sets; the
human's remark sets none for the word itself. Nothing was written.

## Written or changed

- Decisions: none. Invariants: none. Environment facts: none. Glossary terms: none. Part-map changes: none. Projected entries: none.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` — 0, "0 errors".
- No directory touched in this step (no file changed), so no focused run; the correction's runs stand in its report.

## Unread material

- `task-cycle/skill/return_step.md` and `foundation_step.md`: read whole in the first return step of this cycle and applied here
  as it stood; I did not reopen them in this turn. WAY-95 and WAY-263: read whole now (above). WAY-99, WAY-97: read as the task
  quotes them; not reread whole now.

## Searches not found or unclear

- none

## Working copies

None made; `.runs/author-correction-return/` was not created.
