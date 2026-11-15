# Return step report — weak point in every decision question

**Status:** `done`. One correction, one commit: `028b528` (on `d542af0`). No entry written, no
invariant written.

## What was compared, and with what result

- **Entries the change edits**, read whole in the foundation at head `d542af0`: WAY-113 (edited in
  place), WAY-155, WAY-174, WAY-378 (reworded to point to WAY-113). Compared with the files: the text
  each entry now says (a decision question gives the ways, the cost of each with the cost of undoing,
  a recommendation and the weak point; the implication and reason moves for a project definition
  only) stands the same in `elements/common/way_of_working.md` ("How a skill asks"),
  `project-level/skill/rounds.md`, `elements/common/skill/definition_variant.md` (unchanged, as the
  task says), `task-cycle/skill/request_template.md` and `process-audit/SKILL.md`. Nothing
  disagrees. WAY-113's *Scope* names every part whose text carries the rule after the change
  (`task-cycle`, `foundation-review`, `process-audit`, `product-guidelines`, with the parts it had).
- **Entries the task names:** WAY-123 (the weak point of the option recommended; its *Rationale* says
  the weak point lets the choice stand without a question after it, which WAY-113 now says for every
  decision question) — consistent, unchanged by the task. WAY-100 — the practice taken from the
  Mega.DEV course is named in WAY-113's *Rationale* with what the recording showed and what is left
  out in *Rejected*, as WAY-100 gives; `Based on` stays `none` for a source a reader cannot open.
  WAY-327 stands in the table of withdrawn identifiers with its rule in
  `task-cycle/skill/request_template.md`, as the task says; no entry for it.
- **Search of the foundation for entries restating the rule:** `grep` over `foundations/*.md` for
  "ways open", "cost of each", "recommendation", "options", "weak point", "question of assessment",
  "How a skill asks" and for the audit's outcomes ("weigh", "set aside", "note"). Besides the four
  entries above, no decision, invariant, glossary or environment-fact entry restates the rule or
  the audit's two outcomes. The decisions that mention a recommendation without restating the
  rule (WAY-166's "owed a recommendation", WAY-114, the exceptions that narrow WAY-114) say nothing
  the change contradicts. No test holds a sentence of WAY-113, 155, 174 or 378 by a `decision:` line,
  and no invariant derives from them, so no pair of examples had a test to give way to.
- **Part map of the touched parts:** `elements-common`, `project-level`, `task-cycle`,
  `foundation-review`, `process-audit`, `product-guidelines`, `decisions`. Descriptions and *Files*
  still hold. *Depends on*: every new text pointer from these parts to "How a skill asks"
  (`elements/common/way_of_working.md`) stands in a part whose *Depends on* names `elements-common`
  (`project-level`, `task-cycle`, `foundation-review`, `product-guidelines`), or inside
  `elements-common` itself. The one exception is `process-audit`, below.
- **Glossary:** no word of the change is used in a meaning for which WAY-95 gives an entry; "weak
  point" and "question of decision" are plain words and the latter already stood in WAY-113. No
  glossary entry written.

## The correction: `process-audit` and `elements-common` (one of the two things left to this step)

The part map lets `process-audit` depend on `task-cycle`, `project-level` and `gate`. The glossary's
entry "dependency of a part" is any reach of the part to another, among them "a skill of it that
calls a skill or a file of the other"; the template of the part map says that *Depends on* names the
parts a part may depend on and "is never rewritten to fit what the code reaches for today"
(WAY-225), and that a dependency the map does not allow goes to the human or is removed. The
reviewers found no rule for text pointers, and none exists beyond those two; I decided by them:
a skill that tells an agent to read a named file of another part is a reach in the glossary's sense.

`process-audit/SKILL.md` as changed named `elements/common/way_of_working.md` twice (step 1 and
step 3). At the base it named no file of `elements-common`; it cited the decision (WAY-113) only.
That was a reach the map does not allow. The correction removes the path at both places and keeps
the pointer by the name of the section and the decision: "as "How a skill asks" gives it
(WAY-113)". The meaning of the audit's rule is unchanged, the part map is unchanged, and the audit
no longer reaches into `elements-common` by file.

*Cost if wrong:* a reader of the audit's skill finds the rule by its section name and the decision
number, not by a path; if the human wants the path in the skill, the right way is to add
`elements-common` to `process-audit`'s *Depends on*, which changes the meaning of the map and goes
through the human, not through this step. I did not propose that change.

## The other thing left to this step

The two lines of the fix review's new Minor finding (`project-level/lead/skill/route_changes.md:19`,
`task-cycle/skill/request_template.md:425`): left as the handoff says; my comparison did not need
those lines.

## Entries and invariants written

None. The task's settlements went to WAY-113 (rows 1, 2, 3, 7) and to files (rows 4, 5, 6, 8) in the
change; the return step found nothing the foundation step missed (no source outside the product to
write as an environment fact, no choice that binds after the merge outside the rows, no rule the
task or a decision sets for an invariant). The place of each settlement of this step: the
correction above went to `process-audit/SKILL.md`, the place of the rule it concerns; no entry.

## Checks (command → exit code)

- `python -B elements/common/foundation_check.py` → 0 (`0 errors`), run after the correction.
- `python -B gate/run_tests.py process-audit` → 0 (234 tests), the one directory changed.
- Not run: the full gate (the orchestrator's).

## Unread material

- The part-map entries of `decisions`, `gate`, `installation` and `instruction-files`, and the
  entries of the part map outside the touched parts: not read; I read the entries of the touched
  parts and their *Depends on* in full, and the template's sections "Allowed dependencies" and
  "Assigning files" (first lines).
- `reports/review-whole-report.md` and the fix-review reports: not read; the handoff gave their
  results.
- `elements/glossary/skill/SKILL.md` and the full glossary: only the entry "dependency of a part"
  and a search of the glossary for the words of the change were read.

## Searches not found or unclear

- A rule that governs text pointers between parts: none found beyond the glossary entry
  "dependency of a part" and the part-map template's "Allowed dependencies". The decision above
  rests on them.
- Whether a pointer by a section's name to another part's file, with no path, counts as a reach:
  unclear in the foundation; the correction takes the narrower reading (a named file is a reach)
  and leaves a pointer by name and decision number, as the base had it.

## Working copies

- `.runs/author/` holds the test logs of the earlier checks and of this one; the edit scripts were
  inline and left no file. No worktree, clone or screenshot was made.
