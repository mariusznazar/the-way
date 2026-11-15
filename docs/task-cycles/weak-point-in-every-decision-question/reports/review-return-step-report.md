PASS 028b528107501af90c16b6498ceab785ead3e6ff

# Review of the return step — range `d542af0..028b528`

`git rev-parse HEAD` in the worktree is `028b528107501af90c16b6498ceab785ead3e6ff`, the head given. One commit,
`process-audit/SKILL.md` only (13 insertions, 14 deletions).

## Findings

Blocking: none. Minor: none. Out of scope: none.

## What was judged

1. **Is the removal right by the part map?** Yes. The part map's `process-audit` entry
   (`foundations/part_map.md:124-134`) gives *Depends on:* `task-cycle · project-level · gate`.
   `elements-common` is not in it, and neither is `decisions`. The glossary's "dependency of a part"
   (`foundations/glossary.md:37-39`) is "any reach of that part to another part ... a skill of it that calls
   a skill or a file of the other ... a path"; the template of the part map ("Allowed dependencies",
   `elements/part-map/template.md:88-94`) says *Depends on* covers every such reach and "is never rewritten
   to fit what the code reaches for today" (WAY-225). A skill that tells the agent to read the named file
   `elements/common/way_of_working.md` is such a reach, so the path was a dependency the map does not
   allow, and removing it (rather than widening the map) is the course the template gives; widening the
   map would go to the human. The part map is unchanged by the commit (`git diff` shows the one file). At
   the base `bfb2e10`, `process-audit/SKILL.md` named no file of `elements-common`
   (`git show bfb2e10:process-audit/SKILL.md` has no `way_of_working` or `elements/`), so the removal
   restores the base's standing, not a new one. The skill still cites decision ids (WAY-113 and many
   others) although `decisions` is not in its *Depends on*; that was so at the base and is the foundation's
   general practice (every part cites WAY-ids), so I do not read an id as a reach. The author's
   narrower reading (a named file is a reach) is the one that stays within the map either way.
   No other path of the skill reaches a part outside `task-cycle`, `project-level`, `gate` (grep of
   `elements/`, `foundation-review`, `product-guidelines`, `installation/` in `process-audit/SKILL.md`: none).
2. **Does the audit's text carry *To do* 7 fully?** Yes, at `process-audit/SKILL.md:157-168`: before the
   question the agent names from the rows what they show as broken or out of date and a step can change,
   with the three examples of the task (old version of the process, a count that did not succeed, an issue
   with no task), and puts each as a question of decision "as 'How a skill asks' gives it (WAY-113)"; the
   recommendation rests on what the rows show as broken, never on how often, how long or the level of the
   cost; "the rules of working on those two stand as they are", and both rules stand untouched at lines 40
   and 45 ("never a priority"); where the rows show nothing, one sentence and an open question of
   assessment with no recommendation; three outcomes (weighs further, decides on a step, sets aside). The
   note's *Decided* entry stands at line 260 (earlier range, already judged). Nothing of the task's sentence
   is lost by the commit.
3. **Did the rewrap change any wording?** No. `git diff --word-diff` of the range shows only two removals:
   the words "in `elements/common/way_of_working.md`" (step 1) and "`elements/common/way_of_working.md`"
   (step 3); the rest is line breaks. Each sentence otherwise reads word for word as at `d542af0`.
4. **Is the pointer "as 'How a skill asks' gives it (WAY-113)" enough to find the section?** Yes, with a
   small reading cost. The phrase is unique: the section heading `## How a skill asks` stands once in
   `elements/common/way_of_working.md:20`, and `### WAY-113` stands at `foundations/decisions.md:1414`, so a
   search for either string finds it (a grep of the tracked Markdown for "How a skill asks" returns that
   heading among the uses). It is the form most sibling texts use already: `project-level/lead/answering.md:36`
   ("in the shared workflow"), `process-audit` at the base, `foundation-review/with_the_human.md:4`,
   `product-guidelines/*/SKILL.md`. The audit's agent works in the-way's checkout, where both are found
   by one search. I do not grade the missing path a finding.

## Declined to judge

- Whether the other texts of the change that name `elements/common/way_of_working.md` by path (for example
  `project-level/technology/task_run.md:15`, `task-cycle/skill/request_template.md`) stand within their
  parts' *Depends on*: outside the return step's range, and the author's report says each stands in a part
  that names `elements-common`. I did not verify each of them.
- The two Minor lines of the fix review (`project-level/lead/skill/route_changes.md:19`,
  `task-cycle/skill/request_template.md:425`): outside this range, left by the handoff.

## Checks

- `git rev-parse HEAD` → `028b528...`, as given.
- `git diff d542af0..028b528` and `git diff --word-diff=porcelain d542af0..028b528` → read whole; two
  removed phrases, rest rewrap.
- `python -B elements/common/foundation_check.py` → exit 0, `0 errors`.
- `python -B gate/run_tests.py process-audit` → exit 0, `Ran 234 tests`, `OK`
- Not run: the full gate (the orchestrator's).
- Search of `process-audit/` for `way_of_working`, `elements/` → none at head; at `d542af0^` none; at `d542af0`
  two.

## Reaches beyond the dispatch

- `foundations/decisions.md` WAY-113 (the head of the entry, lines 1414-1425), to confirm the identifier and
  the heading a reader searches for; `foundations/glossary.md:37-39` "dependency of a part" and
  `elements/part-map/template.md:88-94`, the rule the judgment of the part map rests on (named by the
  handoff as "the template of the part map's Allowed dependencies"). Task rows read: *To do* 7 and the
  questions 9 and 7's settlements it needs.

## Foundation I selected

Selected by "Reading the foundation" for this one-file change of the `process-audit` part: the part-map
entry of `process-audit` (whole), WAY-113 (the entry's body), the glossary entry "dependency of a part"
and the part map template's "Allowed dependencies". I did not select guidelines, since the change is
Markdown text of a skill and the handoff names none.

## Working copies

None made. `.runs/review-return-step/` was not created.

## Unread material

- Whole `foundations/decisions.md` and whole `foundations/part_map.md` and `foundations/glossary.md`: read
  only the entries named above (the handoff selects by entry; WAY-113 body read, its *Verification*,
  *Rationale*, *Rejected* not re-read, judged in the earlier ranges).
- `reports/review-whole-report.md` and `reports/review-fix-report.md`: not read; the handoff states their
  results (PASS, PASS), and this range is the one commit after them.
- `elements/common/way_of_working.md` "Reading the foundation" and "How a skill asks" read only as to the
  heading and the section's existence, not whole.

## Searches not found or unclear

- A foundation rule that says whether a pointer by a section's name, with no path, to another part's file is
  a reach: not found; the glossary lists "a path" among the reaches, and a name alone is not a path. The
  judgment above does not depend on it, since the commit leaves the audit at its base's standing.
- Whether a decision id cited from a part not listing `decisions` is a reach: not found as a rule; the
  practice of every part is to cite ids.
