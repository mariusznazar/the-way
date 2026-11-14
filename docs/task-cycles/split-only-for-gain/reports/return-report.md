# Return step report: task `split-only-for-gain`

**Status:** `done`. **Commits:** none (the comparison found nothing that no longer matches). Head stays `edf1699`.

## Return step

- **Foundation compared with code:** none to correct. Compared, each against the files of the worktree at `edf1699`:
  - **WAY-372** (written) against `project-level/task/skill/read_sources.md` (three reasons, the proposer names the reason, silence on size, the human's own request), `project-level/plan/skill/cut_tasks.md` (the plan's cut by WAY-143 and the reasons, size alone no reason) and `project-level/task/skill/resolve_gaps.md` (no offer of a split): the same three reasons and the same silence stand in all three; its *Relations* (WAY-13, WAY-140, WAY-143) name entries the log holds (`foundation_check.py` 0 errors).
  - **WAY-13** (edited) against `task-cycle/skill/SKILL.md` ("Two questions at start", "whatever its size, gets the product's tests and a review"), `task-cycle/plan/SKILL.md:167` and the slice rules: no file of `task-cycle` says a task's size is a signal to split it; what WAY-13 keeps (the two questions, the checks whatever the size) still matches.
  - **WAY-146** (edited) against `project-level/plan/skill/critique_plan.md`, `project-level/plan/template.md`, `project-level/plan_check.py` and its tests, and the invariants `project-plan-form` and `project-plan-check`: none holds a judgment of a task's size any more; the script's checks and the critique's four other judgments match the entry word for word. The entries that derive from it (WAY-151 at lines 4585-4600 of the log, WAY-144 and WAY-230 by their reference) lean on its critique and script, not on the removed judgment.
  - **WAY-139** (named by the task) against `resolve_gaps.md:60-64` and `:85-87`: its "or the human splits that work into a task of its own" matches the line "offer no split; the human may split that work"; stays as it was. **WAY-143** against `cut_tasks.md`: its rule stands in the first sentence of the paragraph. **WAY-113**: unaffected (the questions of refinement are asked as before).
  - A search of the whole foundation (decisions, invariants, glossary, part map, environment facts) for `split`, `too large`, `size alone`, `its size`, `merged before the others`, `signal`: the remaining hits are the slices of a change (WAY-136, WAY-371), the other uses of "split" in the form rules of the elements, and WAY-372's own *Rejected*; nothing contradicts WAY-372 or WAY-13.
  - **Part map**, parts `project-level` and `decisions` (and `task-cycle` for WAY-13): no file was added, moved or removed and no responsibility changed (the refinement of a task, the breakdown into a plan and the check of that plan stay what the part's text says); no change.
- **Decisions written or changed:** WAY-372 (written); WAY-13 and WAY-146 (edited in place). No further decision.
- **Invariants written or changed:** none.
- **Environment facts:** none (WAY-372's *Based on* is `none`; no source outside the product is cited).
- **Glossary terms:** none (no word the change uses is in a meaning for which WAY-95 gives it an entry, and no term was used against its entry).
- **Part-map changes:** none.
- **Projected entries written whole or in part:** none (the task carries none).
- **Rows of *Settlements to record* written:**
  - rows 1, 2 and 6, and the silence half of row 3: **WAY-372**;
  - the other half of row 3: **WAY-13** (edited in place);
  - rows 4 and 5: lines of the skill `project-level/task/skill/resolve_gaps.md` (`:62-64` for row 4, `:85-87` for row 5), with **WAY-139** beside them, as the entry that holds the human's own split, not as the entry that states the rows; no entry written for them;
  - also changed, no row of its own: **WAY-146** (`the cycle's`: the removal of the plan critique's size judgment that question 5 and row 6 carry, put before the human by the request).

## Check (command, exit code)

- `python -B elements/common/foundation_check.py` — exit 0, `0 errors` (on the unchanged tree at `edf1699`; `git status --short` empty).
- The focused tests ran in the fix step on the same tree (`agent-instructions`, `instruction-files`, `elements/common`, `project-level`, each exit 0; see `fix-report.md`); this step changed no file and ran no further test. Not run: the whole gate (the orchestrator runs it).

## Unread material

- The decisions of the scopes `project-level` and `task-cycle`, beyond those read whole in the earlier reports, remain unread, as the first report names. For this step I read WAY-372 whole again and the passages named above (WAY-151 lines 4585-4600, `task-cycle/skill/SKILL.md:90-112`).
- `reports/whole-change-review-report.md` and `reports/fix-review-report.md`: not read; I took the two Minor findings of the fix review from the handoff (a 126-column line at `critique_plan.md:19` and one short line inside WAY-372's *Rationale*) and left them for the request, since the comparison showed no mismatch they carry.

## Searches not found or unclear

- None: every search of this step found what it looked for. One note: no test or script cites WAY-372 or the removed judgment of WAY-146 (grep over the repository), so nothing of code holds either entry beyond the instruction files compared above.
