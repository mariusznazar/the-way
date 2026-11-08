# Handoff — the return step

You are the one author, resumed for the return step (step 11 of `implement-task`), same worktree
`the root of the worktree`, branch `task/guidelines-no-inventory`,
head `ae5dff6` (reviewed: whole-change review `PASS ae5dff6`). Variant: the task cycle's return step; read
`task-cycle/skill/return_step.md` whole (and `task-cycle/skill/foundation_step.md`, which it says it writes as).

Compare with the files of the repository, and correct in the same change whatever no longer matches:
- the entries the change writes or changes: WAY-312, the environment fact `shorter-guidelines-trial`,
  the bullet in `product-guidelines/template.md`;
- the entries the task names (*Decisions in play*: WAY-168, 169, 171, 172, 173, 213, 130, 100, 271) and
  those your search of the foundation found;
- the part map entries of the touched parts: `decisions`, `environment-facts`, `product-guidelines`.
Also: each source outside the product the change rests on that the foundation does not hold (the fact is
written); any word used in a meaning for which WAY-95 gives an entry (`record-glossary-term`); any row of
*Settlements to record* the foundation step missed (rows 1–3 are written — confirm that each is, with its
identifier); a choice that binds after the merge (WAY-36) — none expected, say so. Write an invariant only
for a rule the task, a decision or the human sets (none is set). Defer nothing: an entry this request does
not write is neither proposed nor listed for later; review findings are no foundation entries. The unfixed
Minor notes of the last review (a 130-character line 9822 of `foundations/decisions.md`; whether sentence 2
of WAY-312 should mention the WAY-173 route) are the request's list, not for this step — leave them.

If you change nothing, do not commit. If you commit, say so; a reviewer will review the range.
Run `python -B elements/common/foundation_check.py` (exit 0). Do not run the product's gate (the
orchestrator's).

Return, as text (the harness forbids a subagent to write the report file; the orchestrator saves it as
`reports/return-step-report.md`): the record's *Return step* items — Foundation compared with code;
Decisions written or changed; Invariants; Environment facts; Glossary terms; Part-map changes; Projected
entries; Rows of *Settlements to record* written — plus commits, checks with commands and exit codes, and
**Searches not found or unclear** (`none` is an answer).
