PASS baa07f44472de3d3c86cc61cb681c43ecb1bfd41

# Review of the fix - precedence-between-decisions

Range `9b44856..baa07f4` (one commit). `git rev-parse HEAD` printed `baa07f44472de3d3c86cc61cb681c43ecb1bfd41`.
Diff: `foundations/decisions.md` (+5 / -5), `task-cycle/skill/request_template.md` (+1 / -1). Nothing else.

## Findings of the findings file

- **I1 - fixed.** WAY-25 *Rejected*, last item, now reads "an outcome can come from two passages read
  together, and an agent reading the wording literally would stop where the outcome is given". The
  universal "only" is gone; the sentence matches the source (one case where two passages together gave
  the outcome) and the entry's *complies* example ("in one passage or in two read together").
- **M1 - fixed.** WAY-25 *Rejected*: "the outcome can follow from settlements that do not say so"; the
  frequency "often" is removed.
- **M2 - fixed.** WAY-293 *Rationale*: "may not settle it silently (WAY-25)", the same wording as WAY-25.
- **M3 - fixed.** `task-cycle/skill/request_template.md`, item 6: the passages are quoted "from the report
  of the step that wrote it (WAY-25)", which covers the foundation step and the return step.

No finding contested by the author.

## What the fix itself could have broken

The diff changes only the words named above. No new Critical or Important finding. The rest of WAY-25
(binding sentence, *Verification*, rationale, other *Rejected* items), WAY-134 and the other copies
are untouched in this range.

Minor note (non-blocking, formatting only): the edited lines in WAY-293 and in `request_template.md`
run past the wrap of the neighbouring lines (the reflow was not redone after the word change). No
check reads line length (`foundation_check.py` passes).

## Checks run (worktree root)

| Command | Exit |
|---|---|
| `git rev-parse HEAD`; `git log --oneline 9b44856..baa07f4`; `git diff 9b44856..baa07f4` | 0 |
| `grep -c "can come only\|often follows\|settle it (WAY-25)" foundations/decisions.md` (old wordings) | count 0 |
| `python -B elements/common/foundation_check.py` | 0 (`0 errors`) |
| `python -B task-cycle/private_paths_check.py foundations/decisions.md` | 0 (0 listed) |
| `python -B task-cycle/private_paths_check.py task-cycle/skill/request_template.md` | 0 (0 listed) |
| `python -B gate/run_tests.py task-cycle` | 0 (OK) |
| `git status --short` | 0, empty |

Not run: the whole gate (the orchestrator's). My earlier O1 (WAY-25 *Scope* and `agent-instructions`)
was not given to the author and stays for the request's list.

## Reaches

none beyond the range, the findings file, the fix report, `task-cycle/review/fix.md` and the changed
passages.

## Searches not found or unclear

none
