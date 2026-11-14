# Handoff — the agent of the plan's *Foundation entries*

## Delegation

The person who requested this cycle delegated intermediate choices to the orchestrator. You have no human to ask: return `questions` or `blocked` to the orchestrator as `task-cycle/skill/foundation_step.md` gives. Never label an answer as the human's approval.

## Worktree, branch and base

- Worktree (work from its root): `the root of the task's worktree`, branch `task/co-trafia-do-dziennika-decyzji`. Base of your work: `ac753401de0bfaae0b9b8175c10c17387736f8d8` (this is also slice 1's base; slice 1's range starts there, so its review covers your entries).
- You are the only agent writing in this worktree now. Commit on this branch: commit messages in English, imperative, short, like the repository's existing ones (`git log --oneline`); `git add <path> <path>` by path, never `git add -A`, `git add .` or `git commit -a`; for a message with quotes or backticks use `git commit -F <file>` with the file outside the worktree's tracked files (the record's `.runs/` directory is ignored). Never push.

## Method and stage

Stage: the foundation step of the plan's *Foundation entries* (no variant row of `make-change` applies). Read whole `task-cycle/skill/foundation_step.md`, and the `SKILL.md` of the element at the path it gives (`elements/decisions/skill/SKILL.md`) when you write a decision, and follow it with the way of working it names (`elements/common/way_of_working.md`, `elements/decisions/template.md` and `elements/common/rules.md`, whole). Read `task-cycle/change/SKILL.md` whole for the reading, the own-work check, the commits and the report. Boundary: you write the foundation entries below and nothing else; no code, no test, no change to any file outside `foundations/decisions.md`. You run no gate; the focused check is `python -B elements/common/foundation_check.py --skip-test-citations` from the worktree's root (exit 0 required; the script before slice 1 still has no new report).

## What to write

The plan's section *Foundation entries* (`.runs/task-cycles/co-trafia-do-dziennika-decyzji/plan.md`), copied word for word:

> The entries are written by one agent before slice 1, each edited in place with its pair of examples kept (spec, "Foundation entries"). A slice that quotes a sentence of an entry reads the entry as the foundation step leaves it; the line ranges below are its size at the plan's base.
>
> | Entry | Kind | From | What depends on it |
> |---|---|---|---|
> | WAY-11 (changed) | decision | row 1; spec "Foundation entries" | none |
> | WAY-293 (changed in part) | decision | row 2; spec "Foundation entries" | none |
> | WAY-134 (changed) | decision | row 3; spec "Foundation entries" | none |
> | WAY-168 (changed) | decision | row 4; spec "Foundation entries" | none |
> | WAY-167 (changed) | decision | row 4; spec "Foundation entries" | none |
> | WAY-171 (changed) | decision | row 4; spec "Foundation entries" | none |
> | WAY-172 (changed) | decision | row 5; spec "Foundation entries" | none |
> | WAY-19 (changed) | decision | row 6; spec "Foundation entries" | none |
> | WAY-05 (changed) | decision | row 7; spec "Foundation entries" | none |
> | WAY-12 (changed: the line `decision:` and *Verification*) | decision | row 8; spec "Foundation entries" | Slice 1 (its tests carry a `decision:` line quoting a sentence of it) |
> | WAY-12, attached paragraph for the report of decisions nothing holds (D2) | decision, part of WAY-12 (D8) | row 11; spec D2, D8 | Slice 3 (its tests carry `decision:` lines quoting the start of this paragraph's sentences) |
> | WAY-22 (changed) | decision | row 9; spec "Foundation entries" | none |
> | WAY-03 (changed: changes of a test with a line `decision:` are named) | decision | row 9; spec "Foundation entries" | none |
> | WAY-03, attached paragraph for the listing of an invariant whose sentence changed (D4) | decision, part of WAY-03 (D8) | row 12; spec D4, D8 | Slice 4 (its tests carry `decision:` lines quoting the start of this paragraph's sentences) |
> | WAY-02 (changed) | decision | row 10; spec "Foundation entries" | Slice 1 (the form of the quotation the script reads) |
>
> No invariant, glossary term, environment fact or part-map entry is written (spec, "Not written"). WAY-36, WAY-173, WAY-65 and WAY-26 are read and stay as they are.

Where a row is the source: the frozen task `.runs/task-cycles/co-trafia-do-dziennika-decyzji/task.md`, its table *Settlements to record* (row numbers above are its `#`), the sources each row names, and the spec `.runs/task-cycles/co-trafia-do-dziennika-decyzji/spec.md`, section "Foundation entries" (what each entry says after the change), D1–D9 and Constraints. The *Rejected* of an entry written from a row takes only the ways not chosen that the row's source keeps (the *Not chosen* of the question the row names), as `elements/decisions/template.md` gives (WAY-134); where an entry is edited in place, keep its existing *Rejected* and add the row's ways. Do not widen a row. The entries as they stand: `foundations/decisions.md` by the heading `### WAY-NN`; read each whole and edit it in place (WAY-07). Rulings of the orchestrator the spec carries: the switch `--skip-test-citations` is not changed (WAY-321 stays); a decision's "changed" is a change of its binding sentences; rows 11 and 12 are attached paragraphs of WAY-12 and WAY-03, each with its own one to three sentences; the pair-then-trim rule lives in `elements/decisions/skill/SKILL.md` step 3 and `task-cycle/skill/return_step.md` (not yours to write).

The sentences the later tests quote: write each sentence of WAY-12's and WAY-03's attached paragraphs and of the changed WAY-12 sentence about the line `decision:` so that it begins a sentence (after the start of the paragraph or after `. `) and has at least three words before any punctuation you would not want quoted, since Slices 1, 3 and 4 will quote their starts as the spec's D3 gives.

Each decision keeps its pair of examples (the plan's rule) except where the spec's "Foundation entries" says otherwise. A search of the whole foundation for the entries these touch (WAY-33) is yours, once: correct in the same change the entries it finds (those the task and spec name are in the table; any other the spec lists under "Other decisions of the log the change reaches" is read and corrected only where it contradicts a changed entry). Where your search finds an entry that would change beyond what the task carries, return `blocked` with the question.

## Report

Write your full report to `.runs/task-cycles/co-trafia-do-dziennika-decyzji/reports/foundation-entries-report.md` as `task-cycle/change/SKILL.md` and `foundation_step.md` give: for each entry one sentence of its meaning in English and one in the task document's language (Polish), marked `row <n>` (or `the cycle's`); the own-work check; the check with its command and exit code; the sections **Unread material** and **Searches not found or unclear** (each `none` where there is nothing). Return your status, your commits, a one-line check result, the report path and your questions.
