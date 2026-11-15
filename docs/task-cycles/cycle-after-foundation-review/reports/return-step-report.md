# Return step report

**Status:** done. The return step commits nothing; the head stays `cfda61e` and the worktree is clean.

## Return step (as the record's item gives it)

- **Foundation compared with code:** none found that no longer matched. What I compared:
  - WAY-375 (binding sentences, *Relations*, *Rationale*, *Rejected*) with `task-cycle/remove_merged_worktrees.py`
    (docstring, `inspect_state`, `describe_owner`, `judge`) and its tests: the script keeps a base copy named
    for no task only where it stands alone ("a copy named for no task never stands alone"), keeps a copy
    named for a task whose branch it does not find, and removes a nested detached copy with its
    directory only where clean and on the remote — as the sentence now says. The script's output lines
    `- <name> | <branch> | <reason>` carry the kept directories, as the sentence and `SKILL.md` step 4 say.
    The tests that cite WAY-375 and WAY-376 by `decision:` lines still find their quoted sentence starts
    (the foundation check passes).
  - WAY-376 with the script: it lists the ignored paths under each `remove` line, leaves out the known
    caches, and with `--apply` removes with the directory; the sentence says the list serves the dry run
    and the cycle's own run waits for no one. Nothing in the skill, the template or the README promises
    the human sees the list before a removal (`git grep` for the old promise finds only *Rejected*).
  - WAY-13 with `SKILL.md` step 4: step 4's second question concerns the operation the task's change holds
    and the cycle prepares and never performs; the cycle's own removal of merged directories is the
    area WAY-375 now claims by `narrows WAY-13` (WAY-25's form), so no skill sentence collides.
  - WAY-261 with `SKILL.md` step 10 and `request_template.md` (*Checks*, kind 4, *Findings outside the
    task's scope*): the skill, the decision's second paragraph and the template's clause say the same
    (first red result stays the gate's, the cycle goes on, the request names the test and its fixing
    task or proposes one).
  - WAY-289 with `correction.md` (list of kinds) and the variants row "A correction" of
    `request_template.md`: both name kind 16 beside 8, 4, 9 and 14; kind 16's own paragraph in the template
    already says what the answer runs. WAY-287, which lists what the human's section holds, names the
    descriptive `TODO` item already and needs no change.
  - WAY-13 *Verification* (subject added) with its binding sentence: unchanged meaning.
  - `agent-instructions/README.md` (fix in a manually made request) with WAY-289 (Scope names
    `agent-instructions`): one fix and one review, what stays goes only with the question of a task.
  - `task-cycle/request_check.py`: reads headings, groups and content, not the sentences I changed; its
    tests pass.
  - The part map entries `decisions`, `task-cycle` and `agent-instructions`: the files changed lie in the
    parts they were in; no dependency was added (no code imports changed), so no change.
  - A search over the tracked files for the removed or reworded statements ("first clearing", "hand
    clearing", "sees before", "loose copies", "incomplete reading", "not applied") found no entry or
    instruction left saying the old thing.
- **Decisions written or changed:** none in the return step. (The foundation step changed WAY-13's
  *Verification*, WAY-375, WAY-376, WAY-261 and WAY-289; see `author-report.md`.)
- **Invariants written or changed:** none.
- **Environment facts:** none (no source outside the product that the change rests on and the foundation
  lacks).
- **Glossary terms:** none. A term used against its entry: none found; "human action" no longer appears
  in WAY-375 and its entry is unchanged, as the task says.
- **Part-map changes:** none.
- **Projected entries written:** none.
- **Rows of *Settlements to record* written:** rows 1, 2 and 4 in WAY-375; row 3 in WAY-376; rows 5 and 6
  in WAY-261 and `task-cycle/skill/SKILL.md` (step 10); row 7 in `agent-instructions/README.md`. The
  foundation step wrote them; the return step found none missed. No choice that binds after the merge
  stayed outside an entry.

## Checks (command, exit code)

| Command | Exit |
|---|---|
| `python -B elements/common/foundation_check.py` (full) | 0 (`0 errors`) |

No test directory was run: the return step changed no file. The whole gate was not run, as instructed.

## Reaches beyond the handoff

- `foundations/decisions.md` WAY-287 (passages around the list of what the human's section holds), read
  by search, to see whether it lists the kinds that "do it in this request" runs; it does not.
- `task-cycle/test_request_check.py` (one grep hit on "not applied"), not read otherwise.

## Unread material

`task-cycle/request_check.py`, which the handoff names: not opened; I judged it by its tests, which
pass in the cycle's earlier runs of `task-cycle` (not rerun now, no file changed since), and by a search
for the changed sentences. Everything else the handoff names was read: `foundation_step.md` and
`return_step.md` whole, the handoff whole, the script `remove_merged_worktrees.py` in the parts named
under "Reaches" of my earlier report and its docstring.

## Searches not found or unclear

none

## Working copies

None made.
