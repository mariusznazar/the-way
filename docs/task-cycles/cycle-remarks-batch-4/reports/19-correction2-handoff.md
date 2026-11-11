# Handoff — second correction for the human's remarks, cycle `cycle-remarks-batch-4`

You are the one author, resumed, for **a correction for the human's remarks**. Read the row of that
variant in `task-cycle/change/SKILL.md` again. The orchestrator acts on the user's delegation; the
remarks are the human's and bind.

- Worktree (from its root): `.runs/worktrees/cycle-remarks-batch-4`, branch
  `task/cycle-remarks-batch-4`; head `98e2d86`, whose tree equals the reviewed and gated tree of
  `10d443f` (the two commits above `10d443f` only add and remove the record). Your correction range
  starts there.
- The remarks, whole: `docs/task-cycles/cycle-remarks-batch-4/reports/18-correction2-remarks.md`
  (S1, S2). The reviewer's finding they answer, with the evidence: N-1 in
  `…\reports\15-correction-review-report.md`. Frozen task: `…\task.md`. Report:
  `docs/task-cycles/cycle-remarks-batch-4/reports/20-correction2-report.md`.
- This is a change to decisions the human accepted only through these remarks (WAY-114, WAY-30): mark
  every entry you edit `the cycle's`. Read `task-cycle/skill/foundation_step.md` and the skill
  `record-decision` (`elements/decisions/skill/SKILL.md`) again for decisions you edit in place
  (WAY-71, WAY-287).

## What to do

1. **`elements/common/foundation_check.py`:** for each of the three fields (an invariant's *Rests on*
   and *Derives from*, a decision's *Based on*): the value is a list of items joined by ` · `; the first
   item that begins with `TODO` and everything after it is one description (so a comma or a ` · `
   inside it is no separator); the items before it are read as today (identifiers / quoted sources /
   fact names, with their reference checks). A `TODO` item with no description after it (bare, or
   `TODO —` with nothing after) is the error with the field's hint, as a bare whole value is today.
   Keep: a whole-value `TODO — …` passes; a value with no `TODO` item is read exactly as before; the
   fields that forbid `TODO` stay as they are. Update the docstring (the line you added in the first
   round about "only a value that begins with `TODO` is read as a missing fact" is superseded — fix
   it). Take care with *Based on*, whose items can be quoted sources containing ` · ` inside quotation
   marks and `TODO` words inside a quote: a `TODO` inside a quoted passage is no `TODO` item.
2. **Tests** in `elements/common/test_foundation_check.py`, for each of the three fields: a known
   entry followed by `TODO — <description>` passes, also with a comma and with ` · ` in the
   description; a known entry followed by a bare `TODO` fails with the hint; a known entry that does
   not exist, before a `TODO — …` item, still fails as a reference; `TODO` first and then more text
   reads as one description; `TODO` inside a quoted *Based on* source is not a `TODO` item. Each new
   test fails before the code and passes after.
3. **Words:** WAY-71's binding sentence and `elements/common/rules.md` (one sentence, kept equal in
   both): say that where an entry stands on several things and only some are missing, the missing one
   is the last item and reads as the form of its field. WAY-71's *Verification*: add a complies and a
   violates case for the mixed value; adjust *Rationale* in one or two sentences (why: WAY-17 says every
   link is written, so the known entry stays; the reference stays checked). Both templates
   (`elements/invariants/template.md`, `elements/decisions/template.md`) say it for their fields. The
   example of WAY-287 and item 15 of `task-cycle/skill/request_template.md`: a mixed value is one gap
   (one item), shown with the missing part only.
4. Search the whole foundation once for the entries these changes touch (WAY-33) and report what you
   found. Run `python -B elements/common/foundation_check.py .` and, read-only,
   `python -B elements/common/foundation_check.py <the loop2 checkout>`; report the counts (the human
   knows loop2 has one bare `TODO` in *Rests on*).

## Boundaries

- Commit with `git add <paths>`, English messages; do not push; touch nothing under `.runs/` but your
  report. Focused checks only (`task-cycle`, `elements/common`, `instruction-files`,
  `agent-instructions`, `installation`, whatever else you affect); the orchestrator runs the full gate.
  Another process may use the machine: start no full gate.
- A remark you hold wrong, answer with evidence; a choice the remarks do not settle and the foundation
  leaves open, return as `returned` with the choice and no code (WAY-135).
- Report: own-work check, each check with command and exit code, **Unread material**, **Searches not
  found or unclear**, what you did for S1 and S2. Return status, commits, a one-line check result and
  the report path.
