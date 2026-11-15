# Report of the fix — whole-change review of `af76148`

**Status:** done with concerns (M-3 fixed in part; see below).

**Commit:** `1b5aba9` on `task/part-map-dependencies-task-line`, from `af76148`.

## Findings

- **I-1 — fixed.** `foundations/part_map.md`, the second sentence of `project-level` now reads "…,
  for when the line of a task in the product's backlog is written, given its dependencies and moved
  to ready, and for the derivation of the identifier of a task of a plan, but not for the rest of
  how a line is made, which the rules of the task place say (WAY-107)." Two sentences stay. Shown by
  `python -B elements/common/foundation_check.py`, exit 0, `0 errors`; the text agrees with WAY-107,
  `task_line.md` and `backlog_place.md`.
- **M-1 — fixed.** `elements/part-map/template.md` ("Allowed dependencies") no longer lists the
  kinds of reach; it says what counts as a dependency of a part is what the glossary gives that
  term, any reach and not only an import. One definition stands, in the glossary.
- **M-2 — fixed by a split.** `blocked-request-line` became two invariants, each one rule:
  `blocked-request-wording` (the wording in backticks in the two skill files of `task-cycle`) and
  `blocked-request-label` (a line of `task-cycle/record_template.md` begins with the label). The
  identifier never reached the main branch. Both are `Method: test`, `Derives from: WAY-153`; WAY-153's
  *Verification* names both; each test of `project-level/test_blocked_request_line.py` cites its own
  (`invariant:` lines). Seen failing, each alone:
  - `sed` of the wording in `task-cycle/skill/blocked_finding.md` to "that commit":
    `python -B -m unittest project-level/test_blocked_request_line.py`, exit 1, only the wording
    test fails; restored with `git checkout --`.
  - `sed` of the label line in `task-cycle/record_template.md`: same command, exit 1, only the label
    test fails; restored.
  - Passing: `python -B gate/run_tests.py project-level`, exit 0.
- **M-3 — fixed in part.** "Dependency of a part" is now written where the finding names the part
  map's own text: `foundations/part_map.md:4` ("which dependencies of a part are allowed"),
  `elements/part-map/skill/SKILL.md` (the description on line 3, and the *Depends on* step), and in
  `elements/part-map/template.md` the line on fields of a part, the paragraph on a dependency the
  code holds that *Depends on* does not allow, and "no list of such dependencies of a part". The
  description changed, so `python -B agent-instructions/skill_entry_points.py --write` (exit 0) rewrote
  the two entry points `.claude/skills/the-way-update-part-map/SKILL.md` and
  `.agents/skills/the-way-update-part-map/SKILL.md`.
  **Not changed, contested with evidence:** the binding sentence of WAY-225
  (`foundations/decisions.md`, "a dependency the code holds that the part map does not allow … never
  by rewriting the allowed dependencies to fit the code"). The frozen task
  (`task.md`, *Decisions in play*) says of WAY-225 "Bez zmiany", so I did not change its sentence,
  and left the pair of examples and the prose of WAY-225 and WAY-51 (`Rejected`), which restate it,
  as they are, since a changed example beside an unchanged sentence would split one decision. Cost
  if the reviewer holds it must change: one sentence and its examples, edited with the task's
  consent. The title of the withdrawn row WAY-299 and the docstring of
  `test_cross_part_imports.py` ("is no dependency") are left too: the first is history, the second
  speaks of imports.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` (no skip switch): exit 0, `0 errors`.
- `python -B gate/run_tests.py project-level`: exit 0.
- `python -B gate/run_tests.py elements/part-map`: exit 0 (`cross-part-imports` included).
- `python -B gate/run_tests.py elements/common`: exit 0.
- `python -B gate/run_tests.py agent-instructions`: exit 0 (the entry points of skills).
- Not run: the whole gate (the orchestrator's); `task-cycle`, `process-audit` (no file of them
  changed).

## Own-work check

Requirement most likely missed: the split leaves each rule with its own test failing alone. Checked
by the two breaks above; each failed only its own test.

## Reach beyond the handoff

None beyond `task-cycle/change/fix.md`, which the method names.

## Unread material

none (the findings file, the handoff and `fix.md` read whole; the files edited read before editing,
in this session).

## Searches not found or unclear

- The finding M-3 says "and the like" without a list; I searched the part map, `elements/part-map/`,
  `elements/invariants/examples.md` and the decision log for the bare words and changed those that
  speak of the part map's dependency, leaving the decisions' prose as above.

## Working copies

`.runs/author-fix/` held only outputs of runs and the commit message; removed before return.
