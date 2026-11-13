# Return step of correction 1 — `defects-found-after-merge`

**Status:** done. No commit (nothing needed a correction). Head stays `a3152c9`.

## Foundation compared with code

Compared with the changed sentence of kind 17 (`task-cycle/skill/request_template.md`, the text for
`target-branch · none` and for a correction with two sources):

- WAY-287: says the description after a correction shows the pairs of the cause in one sentence in
  *You accept by merging*, and its *complies* case says the sentence tells that the correction
  answered the remark and whether the cycle judged the task required what it changed. The new text
  is that sentence for the refresh-only case and for two sources; matches. No correction.
- WAY-355: a refresh-only correction leaves a line and a file of remarks in the record; the sentence
  of the description is not its subject. The new text does not touch it; matches. No correction.
- WAY-356: `target-branch` takes only `none`; each pair once; the description shows the pairs in one
  sentence. The new text says the cycle judged nothing for `target-branch · none` and carries each
  pair once; matches. No correction.
- Part map, `task-cycle` (`foundations/part_map.md`): files `task-cycle/**`, dependencies and trust
  boundary unchanged by the correction (one prose file changed inside the part, no file added or
  moved). Matches. No correction.
- Code that reads the template: `grep` of `task-cycle/*.py` and `process-audit/*.py` (non-test) for
  `target-branch`, `kind 17`, `cause of a correction` found no script that reads the sentence;
  `task-cycle/request_check.py` judges no content. Nothing to bring in line.

## Decisions written or changed

none

## Invariants written or changed

none

## Environment facts

none

## Glossary terms

none (the new sentence uses no word in a meaning WAY-95 gives an entry for)

## Part-map changes

none

## Projected entries written whole or in part

none

## Rows of *Settlements to record* written

none (no row is new, as the handoff says)

## Checks

- `git status --short` — clean, exit 0 (nothing to commit; no file changed by this step).
- No test run: no file changed. The earlier checks of the correction stand in
  `correction-1-author-report.md`. The full gate was not run (the orchestrator's).

## Unread material

none (read whole: `return_step.md`, `foundation_step.md`, WAY-287, WAY-355, WAY-356 as in the
earlier report, the *Return step* section of `record_template.md`, the `task-cycle` entry of the
part map)

## Searches not found or unclear

none
