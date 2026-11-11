# Handoff — correction for the human's remarks, cycle `cycle-remarks-batch-4`

You are the one author, resumed, for **a correction for the human's remarks**. Read the row of that
variant in `task-cycle/change/SKILL.md`. The orchestrator acts on the user's delegation; the remarks
below are the human's own words in substance and bind.

- Worktree (from its root): `.runs/worktrees/cycle-remarks-batch-4`, branch
  `task/cycle-remarks-batch-4`; head `14b7680750c48e0c173291fec8223dd7c30b0655` (its tree equals the
  reviewed and gated tree of `5841ed7`; the two commits above it only add and remove the record). Your
  correction range starts there.
- The remarks, whole: `docs/task-cycles/cycle-remarks-batch-4/reports/11-correction-remarks.md`
  (R1, R2, R3). The frozen task is `…\task.md` beside it. The report goes to
  `docs/task-cycles/cycle-remarks-batch-4/reports/13-correction-report.md`.
- A correction is a change to decisions the human accepted only through these remarks (WAY-114,
  WAY-30): this is the human's own act. Mark every entry you edit `the cycle's`.
- The foundation step applies: read `task-cycle/skill/foundation_step.md` and the skill
  `record-decision` (`elements/decisions/skill/SKILL.md`) again for the decisions you edit in place
  (WAY-71, WAY-160, WAY-287), and `elements/invariants/template.md` for *Derives from*.

## What to do, in the order of the remarks

1. **WAY-71, *Scope*:** add `task-cycle`.
2. **WAY-160, *Verification*:** add to the *violates* example the case "the gate fails, its fix changes
   code, and the return step does not compare the fix's range". Do not touch the *complies* sentence
   the task gives word for word.
3. **Route B (R2):** WAY-71's binding sentence and `elements/common/rules.md` carry one extended
   sentence for the three fields, in the shape the task's To do 6 gave, with each field's form: an
   invariant's *Rests on* as `TODO — <the fact, with its source>`, an invariant's *Derives from* as
   `TODO — <the decision, and where it is expected>`, a decision's *Based on* as
   `TODO — <what is missing, with its source>`. Rewrite WAY-71's *Rationale* (the reason is that of
   *Rests on*, now for the other two), add the rejected way "TODO only in *Rests on* — an author of a
   decision whose source is silent, or of an invariant whose decision is not written yet, would have to
   stop the cycle or write `none`, which is false", and keep the two *Rejected* lines already there.
   Check its *Verification* examples read true after the change; add a *violates* case for a bare
   `TODO` in *Based on* or *Derives from*, and for `TODO` in *Relations* or *Origin*.
4. **WAY-287 and item 15 of `task-cycle/skill/request_template.md`:** cover the three fields: each
   descriptive `TODO` of an invariant's *Rests on* or *Derives from* in the invariants file and of a
   decision's *Based on* in the decision log, on the tree after the change; one item in plain words
   for each gap (the rule or decision and what is missing), with "Merge with the gap?". Keep what the
   first fix settled (the whole tree after the change, not only edited entries) and the plain top-part
   wording rules of the template. Update WAY-287's examples to match.
5. **Templates:** `elements/decisions/template.md` gets the form for *Based on* (where a source is
   silent) and says *Relations* and *Origin* never read `TODO`; `elements/invariants/template.md` already
   holds the form for *Derives from* and for *Rests on* — make its *Links* bullet say the same for both
   (bare `TODO` is an error in each).
6. **`elements/common/foundation_check.py`:** read a *Based on* (decision) or *Derives from*
   (invariant) value that begins with `TODO` in whole, as `check_rests_on` does for *Rests on*; report a
   bare `TODO` in each with the hint to describe what is missing; report `TODO` in a decision's
   *Relations* or *Origin* as an error ("does not take"); keep the fields that already forbid `TODO`
   (*Scope*, *Part*, *Verification*, *Source*, a part's fields, *Method*) as they are. Update the docstring.
   Take care that `Based on` also holds quoted sources and fact identifiers: a value that does not begin
   with `TODO` is read as today. Tests: each new rule fails before the code and passes after, with the
   cases of the descriptive form with a comma and with ` · ` inside, the bare forms, and `TODO` in
   *Relations* and *Origin*.
7. Search the whole foundation once for the entries these changes touch (WAY-33): the glossary, the
   skills of the elements (`elements/*/skill/`), `project-level/` forms for projected entries (a
   projected entry in a definition is not the main branch: do not change projected mode, but read it and
   report any conflict), `product-guidelines/`, `foundations/*.md`. Run `python -B
   elements/common/foundation_check.py .` and also, read-only, `python -B
   elements/common/foundation_check.py <the loop2 checkout>` and report the counts of what each
   reports about *Based on*, *Derives from*, *Relations*, *Origin* and *Rests on* (the human was told
   the-way and loop2 hold no such entry).

## Boundaries

- Commit with `git add <paths>`, English messages; do not push; touch nothing under `.runs/` but your
  report. Focused checks only (`python -B gate/run_tests.py task-cycle`, `elements/common`,
  `instruction-files`, `agent-instructions`, `installation`, whatever else you affect); the orchestrator
  runs the full gate. Another process may use the machine: start no full gate.
- A remark you hold wrong, answer with evidence; a choice the remarks do not settle and the foundation
  leaves open, return as `returned` with the choice and no code (WAY-135).
- Report: own-work check, each check with command and exit code, **Unread material**, **Searches not
  found or unclear**, what you did for each of R1–R3. Return status, commits, a one-line check result,
  the report path.
