# Report 07 — fix of the whole-change review, round 1

**Status:** done

## Commits

- One fix commit on `task/cycle-remarks-batch-3`, from reviewed head `7841f00`: "docs: WAY-298 restarts a correction only where something came in, as the correction file says" (`git log --oneline -1` after the commit). Only `foundations/decisions.md` changed.

## Finding 1 (Important): fixed

- How: the orchestrator's choice, followed — the entry follows the file. In WAY-298 (`foundations/decisions.md`, from line 9028):
  - the first binding sentence now mirrors step 4 of `SKILL.md`: "it fetches and, where the checkout stands behind that branch, fast-forwards it when it is on that branch with a clean tree and no local commits, and then starts again from the entry point that started the cycle; where it cannot fast-forward, it stops and says so";
  - the correction sentence reads "…merges the remote target branch into it, and, where something came in, starts again from the entry point";
  - *Verification* "complies": a correction in the request's worktree "starts again from the entry point where the merge brought something in; a correction that fetched and found nothing new goes on without starting again"; "violates": "a correction that found nothing new starts again from the entry point all the same, and so never ends".
  - `task-cycle/skill/correction.md` and the step 4 sentence of `task-cycle/skill/SKILL.md` are unchanged (the latter is the task's sentence word for word; it restarts only after a fast-forward, which happens only "where it stands behind").
- Other places that say the restart: `rg`-style search `grep -n "start again\|starts again" task-cycle/skill/*.md foundations/decisions.md` shows `SKILL.md:116-120` (conditional by its structure), `correction.md:9` (conditional), and four places in WAY-298 (all now conditional). Nothing else needed an edit.
- The *Rationale* and *Rejected* of WAY-298 say nothing of the restart's condition and did not change.

## Meaning of the entry after the change (for the human)

- **Adds a condition the task row does not state:** the task's row 1 says the correction "zaczyna od nowa od punktu wejścia" without condition; the entry now restarts it only where something came in (a fast-forward or a merge brought commits). Reason: an unconditional restart reads the same paragraph again and never ends.
- English: In the-way itself the cycle fetches and, where the checkout stands behind the remote target branch, fast-forwards it and restarts from the entry point, stopping where it cannot fast-forward; a correction does the same, merging the remote target branch into the request's worktree, restarts only where something came in, and takes the remote branch in a product as well.
- Polish: Na samym the-way cykl pobiera zmiany i, gdy kopia stoi za zdalną gałęzią docelową, przewija ją do przodu i zaczyna od nowa od punktu wejścia; gdy przewinąć się nie da, staje. Korekta robi to samo, w worktree requestu scala do niego zdalną gałąź docelową, zaczyna od nowa tylko wtedy, gdy coś przybyło, a w produktach także scala gałąź zdalną. (Adds the condition above; mark: `row 1`, with the added condition.)

## Checks

- `python -B elements/common/foundation_check.py` -> exit 0, `0 errors`.
- `python -B gate/run_tests.py task-cycle` -> exit 0 (142 tests OK).
- Not run: the product's full gate, as the handoff says.

## Own-work check

- Requirement most likely not met: one wording of the restart across the entry, step 4 and `correction.md`. Check: searched every "start again" / "starts again" in `task-cycle/skill/*.md` and `foundations/decisions.md` (command above) and read each place against the others; all five say the restart follows a fast-forward or a merge that brought something in, none restarts unconditionally. Shown: consistent.

## Searches not found or unclear

- none
