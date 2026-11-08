# Correction report — the human's remarks on request 90 (correction 1)

Status: `done`. Commit `c8bf864` (on head `ff395cf`); worktree clean. Changed file: `foundations/decisions.md` (WAY-113 only).

## Remarks, as made, and how

The human's words: "przyjmuję punkty 1–3, poprawmy punkt 4 w tym requeście". Items 1-3 accepted as they stand (nothing touched). Item 4 (the reviewer's Minor finding 1) to be fixed:

- **WAY-113 *Rationale* still said the full question stays "where an entry is written".** Fixed in place: "Where an entry is written outside such a refinement or a cycle runs, the answer is about to bind, so the question stays; the entries written during a refinement, such as the projected entries of a definition, wait for the person's acceptance of the whole document or at the gate, so they follow the rule of the refinement." The binding sentence is unchanged (the human accepted it).
- **WAY-113 *Verification* named only "the refinement of a task".** Fixed: both the *complies* and the *violates* clause now read "the refinement of a task or a project definition, the entries written during it included" / "for an entry written during it too".
- *Rejected* of WAY-113: read; it says "at refinement no question at all ... only where the answer changes a decision", true as it stands; unchanged.

## Other places with the same stale reading

Searched `grep -rn -i "where an entry is written"` over all Markdown outside `.runs/`: only `elements/common/way_of_working.md:40` ("...where an entry is written outside such a refinement", already correct) and WAY-113's binding sentence (correct) and its Rationale (fixed). `elements/common/skill/`, `project-level/`: no file holds the old reading. No other file changed.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` — exit 0 ("0 errors"), before and after the final rewrapping.
- `python -B gate/run_tests.py elements/common` — exit 0.
- `python -B gate/run_tests.py task-cycle` — exit 0.
- `git diff --check` clean; no added line over 100 characters.
- Not run: the full gate; `project-level` tests (no file there changed).

## Own-work check

Requirement most likely not met: that the correction changes no meaning of the binding sentence and touches nothing items 1-3 accepted. Check: `git diff ff395cf HEAD` holds only WAY-113's *Rationale* and *Verification* hunks; the binding sentence and every other entry are byte-identical.

## Reaches beyond the handoff

none

## Searches not found or unclear

- none
