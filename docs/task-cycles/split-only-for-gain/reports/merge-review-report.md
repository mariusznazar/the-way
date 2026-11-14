PASS 50548bf40fcb9900589d3ff3b16ecbf08e23e5db

# Review of the reconciliation with the target branch (task `split-only-for-gain`)

Range: merge commit `50548bf` against first parent `1e807cc`. `git rev-parse HEAD` = `50548bf40fcb9900589d3ff3b16ecbf08e23e5db`, as dispatched.
Diff: three files, `foundations/decisions.md` (WAY-139 only), `project-level/task/deployment_skill_guide.md` (new), `project-level/task/skill/resolve_gaps.md` (the conflict).

## Findings

Blocking: none. Minor: none. Out of scope: none.

## What I judged

1. The conflict's resolution in `project-level/task/skill/resolve_gaps.md:61-68` keeps both sides.
   - The task's side (frozen task, *To do* items 4 and 5; settlements 4 and 5): the check adds an item to *To do* and "offer[s] no split"; the human may split the work off, "which step 1 then handles". The *Where the product has no deployment skill at all* bullet (line 94) reads "ask these questions before the human splits that work off". Both are kept as the target branch's text had no conflict with them except in wording.
   - The target side (WAY-139 as merged, and the guide at line 13): "that item and that task point to the guide, which an agent reads only when it writes or completes a deployment skill". The resolution has the item, and the task the human splits off, name `<the-way>/project-level/task/deployment_skill_guide.md`; only the agent that writes or completes the skill reads it, "and the refinement of any other task does not"; "the guide binds nothing: the list and this check do (WAY-139)". Each clause matches the entry's sentence and its Verification (*complies* and *violates* lines) word for word in meaning.
   - The only word that changed from the target's side is "offer the human to split it" -> "offer no split; the human may split ... of its own", which is exactly what the task changes and what WAY-139's own text ("or the human splits that work into a task of its own") already says. WAY-139 was not changed by this task and still holds.
2. WAY-139 against WAY-372 and the task: WAY-139 says the human splits, never that the agent offers; WAY-372 lets a split the human asks for stand without a reason and bans an agent's offer for size alone; the merged WAY-139 text does not make the agent offer a split. Its Verification line "the human splits writing one into a task of its own" is the human's act, consistent. WAY-372's three reasons name "a later step of the refinement offers a separate task"; `resolve_gaps.md` no longer is such a step for deployment work, and WAY-372 does not name it, so nothing there is stale.
3. WAY-13 and WAY-146 against what the merge brought in: the merge touched neither; WAY-13 (size decides nothing outside preparing and making the change, a split for size alone has no reason, WAY-372) and WAY-146 (critique no longer judges size) still match `critique_plan.md`, `cut_tasks.md` and `template.md` of the reviewed head. The guide's mentions of size (lines 203, 280, 294) are about a search string, a log's size and a rotated file, not a task's size. Its only mention of a split (line 13, "or for the task split off for it") agrees with the resolution: it says the task is one the human splits off, and names no offer.
4. No leftover of the old wording: `git grep` for "offer ... split", "deployment-work split", "A large task is split", "signal to split" finds only the resolution's "offer no split". No conflict markers in `project-level`, `foundations`, `task-cycle`.

## Declined to judge

- How the task the human splits off for deployment work comes to name the guide: that task has no deployment outcome and takes no check (resolve_gaps line 94), so the sentence "the task the human splits off ... name[s] the guide" has no stated step that writes the pointer. The target branch's own text (before the resolution) had the same shape and WAY-139 states it the same way; the task did not touch it. Set aside as outside this task and this merge.
- The new guide's content (352 lines, examples, placeholder addresses): the target branch's own reviewed work, not the task's; I read only its mentions of a split and its first 40 lines.

## Checks

- `git diff 1e807cc 50548bf`, `git show` of the conflict file and `git diff 14098ae 50548bf -- project-level/task/skill/resolve_gaps.md` (second parent against the merge): read both sides, as above. Done, no problem.
- `python -B elements/common/foundation_check.py`: exit 0, "0 errors".
- `git diff --check 1e807cc 50548bf`: exit 0.
- Conflict-marker search with `git grep -E` in `project-level foundations task-cycle`: no output.
- Not run: the gate (`python -B gate/run_tests.py`), which the orchestrator runs afterwards; no other focused tests, since the merge changed text only.

## Reaches beyond the dispatch

- `project-level/task/skill/read_sources.md:28-35` (the one-task check) and the diff `edf1699^..1e807cc` of `critique_plan.md`, `cut_tasks.md`, `template.md`: to confirm the target-side merge left the reviewed change's other files consistent with WAY-372, WAY-13 and WAY-146. Found consistent.
- `git grep` of the old wording across the repository (excluding `.runs`), to check no text still offers the deployment split.

## Unread material

- The guide `project-level/task/deployment_skill_guide.md`: read lines 1-40 and the lines that match "split|size|large"; the rest (parts and fragments from line 41) unread, as it does not bear on a split.
- Everything else the handoff named, read whole: WAY-13, WAY-146, WAY-372, WAY-139 (merged), `resolve_gaps.md` lines 50-95 (from the *Human actions* paragraph to the end; lines 1-49 unread, they precede the changed step), the frozen task `task.md`.

## Searches not found or unclear

none
