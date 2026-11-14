# Report of the return step — decision-log-second-round

**Status:** done (one correction made; two matters left to the orchestrator, named below, neither blocks).

Worktree `the task's worktree`, branch `task/decision-log-second-round`.
Head reviewed `0364c08`; head after this step `9c24d0d`. Nothing pushed; the product's whole gate not run.

## Commits

| Commit | Change |
|---|---|
| `9c24d0d` Name in the Why of WAY-200 the skill file where the rule for the first file of a kind now stands | `foundations/decisions.md`, one row of *Withdrawn identifiers* (+1 -1) |

## The lines of the record's *Return step*

- **Foundation compared with code:** one mismatch found and corrected, the rest equal (the comparison
  is listed below).
  - Corrected: the row WAY-200 of *Withdrawn identifiers* said its rule, "who designates a product's
    exemplar for a kind of code, and when", stands in `product-guidelines/coding/kinds.md` alone. The fix
    of the review (`d55625e`, finding 9) removed from `kinds.md` the sentence "Where the product holds no
    file of a kind, the exemplar of that kind is designated by the task that creates its first file"
    because it stands in `product-guidelines/coding/SKILL.md`, "A new kind" (line 133: "Where the task
    creates the first file of a kind of code, that file is the kind's exemplar"). The comparison half of
    WAY-200 stands in `kinds.md` (route of one kind, proposal of the exemplar, `copy` / `do not copy`).
    The row now names both files, as the fix agent's addition `0364c08` did for WAY-115, WAY-156 and
    WAY-184 and, by oversight, not for WAY-200.
  - Compared and found equal (what, against what):
    - WAY-100 and its pointers: the second paragraph, *Verification*, *Rationale* and *Rejected* against
      `elements/decisions/template.md:42-45` (points to WAY-100, no wording of its own) and
      `elements/common/skill/read.md:9-11` (directs to the rule on the question of a decision, no wording
      of its own).
    - WAY-29: the third binding sentence, *Verification*, *Rationale* against
      `elements/decisions/template.md:298-300` (Recovered decisions) and `task-cycle/spec/design.md:27-30`.
    - The 22 entries that have `derives from WAY-100` on one line (the count of the wrapped relations is
      higher; the decisions of the pattern were read in the review of the whole change): each names the
      practice, what it takes and a source or `TODO`, and none states a place in a file.
    - WAY-288 against `task-cycle/request_check.py` (a block `none` where the task is English; the check
      holds the block to `none`).
    - WAY-309 (the merged paragraph of WAY-323) against `task-cycle/private_paths_check.py`: the twelve
      POSIX class names, the left-neighbour rule for `[[`, the escape sequences `\n`, `\t`, `\r` after a
      drive letter, the Git Bash path, the link after a space; every item is in the code and its
      docstring.
    - WAY-316 (the case of no place for screenshots) against `task-cycle/change/ui_check.md:15-16` and
      `task-cycle/skill/request_template.md:184, 328`.
    - WAY-339 (the measures of context and cache in a script and a file of their own) against
      `task-cycle/cycle_measures.py` (its docstring); WAY-368 (the types start with the instruction files)
      against `task-cycle/agent-types/the-way-author.md` and `the-way-stage.md` (fields `name`,
      `description`, `disallowedTools`, `experimental.cacheTtl` for the author only; no field that drops
      the instruction files).
    - WAY-312 against `product-guidelines/template.md:90-97` (the sentence the entry now leaves to the
      template stands there with its reason).
    - WAY-09 against `foundations/part_map.md` (every directory of the root has a part; `README.md` is the
      one file the map leaves out on purpose, as at the base; the sentences of `installation`, `gate`,
      `instruction-files` and `project-level` hold what the fix added) and against the root listing.
    - WAY-02 (*Verification* names `map-reference-target`; the invariant derives from WAY-02, its test is
      cited at `elements/common/test_foundation_check.py:1527`); WAY-19, WAY-293 (second paragraph),
      WAY-27 (`## Backlog` of the root `AGENTS.md`), WAY-90, WAY-33 read whole against the templates and
      the part map; no statement in them names a place or a count that changed.
    - The four invariants the foundation agent edited (`project-definition-form`, `map-reference-target`,
      `cross-part-imports`, `tracked-file-private-paths`) against the code they name: the files of the
      last one exist; `elements/part-map/template.md:106` names `cross-part-imports`; the readiness check
      cites `project-definition-form`.
    - The part map of the touched parts (`foundations/part_map.md` lines 7-196: decisions, part-map,
      invariants, glossary, environment-facts, elements-common, project-level, task-cycle,
      foundation-review, process-audit, gate, repository, agent-instructions, instruction-files,
      installation, product-guidelines) against the directories and files that exist.
    - The search of the foundation for the changed rules (WAY-33): every `` `path` `` in the log, the
      invariants, the glossary and the part map exists (a script over all of them; the only ones that do
      not are product examples and the `tools/` of a ban); no live entry holds a count of entries or of
      citations that the change made stale (a search of the log for numbers of entries); every
      environment fact of `foundations/environment_facts.md` (43) is still named by a live decision's
      *Based on* or an invariant's *Rests on*, so no fact lost its last entry by the withdrawals (WAY-73);
      every kept entry that WAY-293 requires a skill or template to name (WAY-93, 94, 97, 263, 287, 294,
      295, 297, 363, 364) is named in a file outside the log.
    - The places of *Withdrawn identifiers*: a script found no row naming a path that does not exist; I read
      the rows of WAY-37, 117, 200, 201, 207, 338, 351, 357, 358, 366, 371 against the files they name. Only
      WAY-200 differed.
- **Decisions written or changed:** none. (The row of WAY-200 in the list of withdrawn numbers changed; it
  is no decision.)
- **Invariants written or changed:** none by this step. The four the foundation agent edited stand as
  written (see above); each of their rules is set by a decision or by the task (`tracked-file-private-paths`
  by WAY-309, WAY-320, WAY-324; `map-reference-target` by WAY-02; `cross-part-imports` by WAY-44;
  `project-definition-form` by `none`, as the orchestrator's answer 5 gave). The listing of the foundation
  check for `tracked-file-private-paths` stands as expected.
- **Environment facts:** none. The change rests on no source outside the product that the foundation did not
  hold; the sources named in the 7 entries whose *Based on* reads `TODO` are the human's to supply and are
  no fact of this step.
- **Glossary terms:** none. A word the change uses against its entry: none found (the words "withdrawn
  identifier", "successor" and "kept" stand in `elements/decisions/template.md`, not in the glossary).
- **Part-map changes:** none by this step. (`foundations/part_map.md` changed in the foundation step and in
  the fix: `process-audit`, `project-level`, `gate`, `instruction-files`, `installation`, and one withdrawn
  row; each read above.)
- **Projected entries written whole or in part:** none; the task projects none.
- **Rows of *Settlements to record* written:** none by this step. The task's *Settlements to record* reads
  `TODO`; the plan's rows F1 to F8 are written by the foundation step (`reports/foundation-report.md`).

## The two choices the handoff asks about

Neither is written as an entry; each stays a row of the questions table of the cycle record.

1. **"An entry that `narrows` a staying decision stays in the log, because it is the one record of the
   precedence (WAY-25)."** `return_step.md` writes an entry for "a choice that binds after the merge
   (WAY-36)" and sends it to the place the questions of the decisions template give it. Here:
   - The plan test (`elements/decisions/template.md`, "Plan test") asks whether the rule still binds
     after the merge. The rule here is WAY-25's own: the precedence is recorded in the decision that
     prevails (`narrows`), so withdrawing that decision would drop the record. WAY-25 states it already
     ("the decision that prevails holds the record"). By the fifth question ("Does an entry of the log
     already answer the question it answers, in whole or in part?") the answer is yes, and a sentence
     added to WAY-25 or WAY-293 would only restate it.
   - Cost of writing it anyway: a second statement of WAY-25 to keep in step. Cost of not writing it: none
     beyond today, since the next round that applies WAY-293 meets WAY-25 in the same log.
2. **"The choice of the ten kept entries."** It is the result of this change's work on a table (which
   entries stay), not a rule: by WAY-36 a rule that ends with a piece of work stays in the choices of the
   cycle record. The rule that decides each case is already in the log (WAY-293 second paragraph, WAY-25).
   A later round may apply those two rules to the ten again and withdraw one; an entry saying "these ten
   stay" would make that round contradict the log. Not written.

   Left to the orchestrator: finding 6 of the review of the whole change (WAY-287 kept, WAY-202 withdrawn)
   is the orchestrator's choice and I did not touch it.

## Checks (focused; command and exit code)

| Command | Exit |
|---|---|
| `python -B elements/common/foundation_check.py` (after the change, at `9c24d0d`) | 0 (`0 errors`; the one expected `listed:` line for `tracked-file-private-paths`) |
| `python -B gate/run_tests.py elements/common` (the directory whose tests read `foundations/decisions.md`) | 0 (201 tests OK) |
| `python -B gate/run_tests.py foundations` (the directory of the file I changed) | 1 (`no test found in foundations`: the directory holds no test; the tests that read its files stand in `elements/common`, run above) |

## Own-work check (WAY-164)

- Requirement most likely unmet: a rule left in a place the log's row no longer names, after the fix
  removed sentences the plan had added. Check: the files the fix of finding 9 changed (`kinds.md`,
  `route_changes.md`, `build_table.md`, `starting_rules.md`), each against the withdrawn row naming it.
  Result: WAY-115, WAY-156 and WAY-184 were already corrected in `0364c08`; WAY-200 was not and is
  corrected in `9c24d0d`. The row of WAY-201 (the end of the coding audit) names `kinds.md`, which still
  holds that rule.

## For the orchestrator (not changed)

- The review of the fix (`reports/review-fix-report.md`) holds one Minor finding that no agent has acted on:
  `product-guidelines/styleguide/starting_rules.md:3` is a reason with no rule in its file
  ("A first screen built with no rules is the screen every later one copies" now stands beside no timing
  sentence). It blocks nothing and is a matter of the reviewed change, so I did not touch it.
- Finding 12 of the review of the whole change (empty directories `.runs/executor-3`, `-6`, `-11`, `-14`,
  `-15`, `-16`, `-17`, `-22`, `-23` and the file `.runs/fc.txt`, left by earlier agents) is still true at
  this head; I did not remove what I did not make.
- WAY-173's *Rationale* still says the template of a discipline binds a product only through its own
  decision "(WAY-100)", while its relation to WAY-100 was removed by the task's rule (foundation report,
  "For the human", point 1). Unchanged; it is the human's to see in the request.

## Reaches beyond the handoff

- `elements/decisions/template.md` ("Where it goes", "Changing a decision", "Withdrawn numbers") whole in
  part and WAY-36 and WAY-25 whole: to answer the question of the two choices.
- `foundations/environment_facts.md` headings and `foundations/invariants.md` fields (by script): the
  search for a fact left without an entry that rests on it.
- `task-cycle/private_paths_check.py`, `task-cycle/cycle_measures.py`, `task-cycle/request_check.py`,
  `task-cycle/agent-types/*.md`, `task-cycle/slice_size.py`, `gate/run_tests.py`,
  `task-cycle/change/ui_check.md`: the code the merged entries describe (read in the parts named above).
- `the task's note in the author's backlog` and `git.md`: named by the harness's hooks before a
  script and a commit.

## Unread material

- `plan.md`: not read; the handoff names it, and the foundation and review reports quote what I needed
  (slices and F rows).
- `reports/review-whole-findings.md`, the executor reports and handoffs: not read.
- WAY-93, 94, 97, 297, 363, 364, 263, 287, 294, 295 (the ten kept) and the 22 entries of the pattern: read
  by diff and by the fields named above, not whole; none of them states a place that changed.
- The 137 withdrawn entries at the base: read only WAY-200 whole (`git show`); the others by their question in
  the *Why* row.
- The part map from line 215 (the surfaces and commands) was not read; the change did not touch it.
- `task.md` from line 490 (the note before refinement) was not read, as the handoff bounds it at 1-490.

## Searches not found or unclear

- Where the cycle record's questions table lies for this task: I did not open `cycle.md`; the two choices
  are named here for the orchestrator to put there.
- Whether a check lists the rows of *Withdrawn identifiers* against the files they name: none found, so
  the comparison of those rows was by script (existence) and by reading (content).

## Working copies

`.runs/return-step/` of the worktree held `paths.py`, `paths.out`, `logdiff.txt`, `added.txt`, `fc.out`,
`rt.out`, `rt2.out`. No worktree or clone was made. Removed file by file by path before returning, then the
empty directory; remainder: none.
