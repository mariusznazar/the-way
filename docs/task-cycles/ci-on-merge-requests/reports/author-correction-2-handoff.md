# Handoff: author, correction 2 (the human's answer to the blocking item)

You are the author of corrections 1, resumed for correction 2, on your class. The orchestrator's go-ahead is provisional, never the human's approval.

## Where and what

- Worktree `the worktree of the task`, branch `task/ci-on-merge-requests`, the-way itself, head `9a00830` (its tree equals `dcb1a19`, your fix). `origin/foundations` has not moved from `7f5c5a5`, so no merge precedes you. Your directory for working copies: `.runs/author-correction-2/`. Your report: `.runs/task-cycles/ci-on-merge-requests/reports/author-correction-2-report.md`.
- Method: `task-cycle/change/SKILL.md`, variant **"a correction for the human's remarks"**; `task-cycle/skill/foundation_step.md` for the entries you change.

## The remark you carry out, word for word

> 1. (a) Allow the dependency: remove the debt record (the invariant `installation-instruction-files-dependency`) and add the instruction-file checker's part to the installer part's list of allowed dependencies in the part map, citing settlement 5 of the task. Then run what has not run on the final code: the comparison of the foundation with the code, a merge with the target branch if it moved, and the wait for the CI run.

Only the first sentence is yours; the rest the orchestrator runs (the return step comes to you separately later).

## What to do

1. Remove the entry `installation-instruction-files-dependency` from `foundations/invariants.md` whole (the file keeps no list of withdrawn identifiers; check how `elements/invariants/skill/SKILL.md` and `elements/invariants/template.md` handle the removal of an invariant, and follow them). Search the tracked files for any reference to that identifier or to its sentence, and correct or report each.
2. Add `instruction-files` to the *Depends on* of the part `installation` in `foundations/part_map.md`, keeping the file's order and form (read `elements/part-map/skill/SKILL.md` and `elements/part-map/template.md`, "Allowed dependencies", by the step that names them). The human allows this dependency because the task asked for it: settlement 5 of the frozen task `.runs/task-cycles/ci-on-merge-requests/task.md` ("Jedno polecenie testów produktu uruchamia też `check_instructions.py`", the human's choice). The part map has no field for a citation: write the citation in the commit message, and in your report give the settlement's line number and its words; say whether the map's own form calls for the citation anywhere in the file, and where.
3. Check that the allowance creates no dependency cycle or other error of the map, and that `elements/part-map/test_cross_part_imports.py` and the foundation check still pass.
4. Change nothing else. Do not fix the Minor findings of the reviews (they stand in the request's list), do not touch the installer, its README or its test, and do not edit the request's description. A Minor finding of this correction's review goes to the list too.

## Checks

`python -B elements/common/foundation_check.py` without `--skip-test-citations`, and `python -B gate/run_tests.py <directory>` for single directories (`elements/part-map`, `elements/common`, and any directory a changed file belongs to), one at a time. Never the full gate: it is the orchestrator's and waits for the day's advisor's signal.

## Reading

WAY-225, WAY-51, WAY-11, the glossary entry "dependency of a part", `elements/part-map/template.md` ("Allowed dependencies") and its skill, `elements/invariants/template.md` and its skill (for the removal), and what `elements/common/way_of_working.md` ("Reading the foundation") selects for the parts `part-map` and `invariants`.

## Working copies (word for word from the cycle's skill)

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never in the system's temporary directory, in the scratch directory of a session or in the main checkout of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by itself under its session's directory is moved into the agent's directory and the original removed, except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md` says, to the place the product's foundation settles for screenshots, and into the agent's directory only where no such place is settled. The files that a product's own tools and tests make by themselves are no working copy of the agent and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in the report where each copy stood and that it was removed. Where a removal fails, the agent finishes all the same and names in the report the remainder, with its full path and the reason it stayed.

## Your report

Status, commits, what was changed place by place, the place each entry went to as `foundation_step.md` gives, checks with command and exit code, the own-work check, reach beyond the handoff, **Unread material**, **Searches not found or unclear**, working copies and their removal. No secrets or personal data.
