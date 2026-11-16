# Author return-step report — correction 1, decision-sources-and-leftouts

**Status:** done. The step commits nothing; head stays `d48638a`.

## Return step

- **Foundation compared with code:** the correction writes no code and changes no binding sentence;
  it changed *Rationale*, *Rejected* and *Relations* of WAY-139, WAY-145 and WAY-165.
  - Everything that names the three (search of every tracked file outside `.runs/` for
    `WAY-139`, `WAY-145`, `WAY-165`): the project-level files on where an open question is resolved
    (`project-level/plan/template.md:128-148`, `project-level/plan/skill/place_questions.md`,
    `write_and_check.md`, `cut_tasks.md`, `project-level/lead/skill/route_changes.md`,
    `project-level/task/skill/project_plan_task.md`, `project-level/definition_template.md:142`); the
    files on the deployment skill (`project-level/task/skill/resolve_gaps.md:82-107`,
    `project-level/task/deployment_skill_guide.md`); the files on the logs and the agent's way to the
    running product (`project-level/technology/start.md`, `running_product.md`, `task_run.md`,
    `project-level/definition_template.md:172-183`, `product-guidelines/coding/template.md:179`,
    `product-guidelines/styleguide/audit.md:6`); the invariant `project-plan-check`, which derives
    from WAY-145 (`foundations/invariants.md:267`); WAY-121, WAY-142, WAY-270 and WAY-100 in the log.
    Each cites what the binding sentences say, which did not change, so each still matches. WAY-270's
    *Rationale* ("they bind by this decision, by WAY-165 and by WAY-139, and nowhere else") now agrees
    with WAY-139's and WAY-165's own *Rationale*.
  - The relation `derives from WAY-100` in the three has the form `elements/decisions/template.md`
    gives ("Relations and precedence": `derives from WAY-x`, number alone, in the dependent entry);
    WAY-100 is a decision of the log. `elements/common/rules.md`: no `TODO`, no field word outside
    its template; no change.
  - Nothing in the repository names any of the three as adopting no practice: a search for "no
    practice", "adopts no", "evidence only", "as evidence", "not adopt" outside `.runs/` finds only
    unrelated lines (the record template and the cycle skill on evidence of checks; WAY-25x on a
    mutation tool). The statement to the contrary stood only in the frozen task's *Out of scope*
    (WAY-139) and in the history of the second round, which are no file of the tree.
  - Tests with a line `decision:` for WAY-139, WAY-145 or WAY-165: none.
  - Part map, part `decisions` (`foundations/part_map.md:7-15`): untouched and still matching.
- **Decisions written or changed in this step:** none.
- **Invariants:** none — the correction sets no new rule; `project-plan-check` still derives from
  WAY-145 with its meaning unchanged.
- **Environment facts:** none. The correction adds no citation outside the product: the three
  sources are course lessons a reader cannot open, described in *Rationale* with *Based on* `none`
  (WAY-100, WAY-90), so WAY-90's test has nothing to judge.
- **Glossary terms:** none; no word is used in a new meaning or against its entry.
- **Part-map changes:** none.
- **Projected entries:** none — the task carries none.
- **Rows of *Settlements to record*:** the correction wrote none; rows 1 and 2 stand in WAY-100.
- **Choices that bind after the merge:** none.
- The review's Minor findings M1–M6 are not mine to fix and are not touched.

## Checks

| Command | Exit | Result |
|---|---|---|
| `python -B elements/common/foundation_check.py` (on `d48638a`, tree clean) | 0 | `0 errors` |

Searches above were made with the search tool. Not run: the full gate (the orchestrator's).

## Working copies

None made in this step; `.runs/author/` does not exist.

## Unread material

- `reports/review-correction-report.md`: not read; the handoff states its result and that its
  findings are not mine.
- The files that name the three were read at the lines the search found, not whole; each cites a
  binding sentence that did not change.

## Searches not found or unclear

none
