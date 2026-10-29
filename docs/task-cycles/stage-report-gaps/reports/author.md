# Author report

Status: done

## Change

Commit: `e95be3b` — `Record missing and unclear task-cycle searches`

Changed files:

| File | Added | Removed |
|---|---:|---:|
| `foundations/decisions.md` | 29 | 0 |
| `task-cycle/change/SKILL.md` | 3 | 0 |
| `task-cycle/plan/SKILL.md` | 4 | 1 |
| `task-cycle/record_template.md` | 2 | 1 |
| `task-cycle/review/SKILL.md` | 3 | 0 |
| `task-cycle/skill/SKILL.md` | 6 | 3 |
| `task-cycle/spec/design.md` | 3 | 1 |
| `task-cycle/spec/review.md` | 3 | 1 |

`WAY-260` states that every task-cycle stage reports unsuccessful searches and unclear points, or
`none`, separately from its existing account of reaches beyond the dispatch. The orchestrator
copies every non-`none` item word for word into *Process remarks on the-way*, adding the stage name
and full report path without combining repeated items. Its rationale is that a gap an agent resolves
without asking the orchestrator still matters to later process improvement. Its rejected options
record the task's alternatives: limit the item to the-way instructions, expand the reach item,
limit participating stages to authors and reviewers, and combine repeats. The decision derives
from WAY-148.

The stage reports for authors, executors, fixes, corrections, reviewers, planners, spec designers
and spec reviewers now have the same **Searches not found or unclear** item, with `none` allowed.
The cycle instructions tell the orchestrator to copy each such item into the process remarks, and
the record template calls for verbatim text, stage and report path while preserving repeats.

## Checks

- `python -B elements/common/foundation_check.py` — exit code 0; `0 errors`.
- `git diff --check` — exit code 0.
- Not run: the whole product gate, as assigned to the orchestrator by the handoff.
- Not run: Python tests. The change adds process prose and a decision; it changes no executable
  behaviour or test contract.

## Own-work check

Weakest requirement: each stage's report must expose unsuccessful searches and unclear points, and
the cycle must preserve each item in a form reachable by the process-remarks extractor. I searched
all stage report instructions for `reach beyond` and report requirements, then checked that the
seven report methods now use the same item label and allow `none`. I inspected the named
`extract_remark_blocks` implementation in `C:/Storage/The Brain/The Brain/Notes/Areas/(A) Claude
code/scripts/cycle_remarks_digest.py`: a list item includes following lines indented deeper than its
marker, so the `Process remarks on the-way` bullet in the record template can contain indented
copied items and remain inside the extracted block. The check showed all stage methods are covered
and the record placement is extractable. This was a manual check; command and exit code: not
applicable.

## Foundation meaning

- `WAY-260` — każdy etap cyklu zapisuje, czego szukał i nie znalazł albo co było niejasne, a
  orkiestrator przenosi każde takie zgłoszenie dosłownie do uwag procesowych, bez łączenia powtórzeń.

## Choices

- Kept the new report item separate from the existing reach item because the task settles that
  they capture distinct evidence; changing the meaning of reach would introduce routine-reading
  noise and alter what the orchestrator reads there.
- Applied the item to every stage and kept repeated reports separate, as the accepted settlement
  requires. Limiting the stages or combining reports would lose the evidence the task asks to
  preserve.
- Wrote a new decision derived from WAY-148 rather than extending WAY-148, as the task settles.

## Reaches and questions

- No reach beyond the dispatch. I read the external `extract_remark_blocks` function because the
  dispatch names it as acceptance evidence.
- Questions or concerns: none.
- Return step: not performed, as directed by the dispatch.
