# Handoff — the return step (task slug `small-fixes-after-prs-117-121`)

You are the one author of this change, resumed for the return step (step 11 of the cycle). The
orchestrator dispatches you; nothing here is the human's approval; ask the human nothing. The code
was reviewed: the whole-change review failed on `e9aea95` and the review of its fix passed on
`eaf815c`.

- Worktree: `the task's worktree`, branch `task/small-fixes-after-prs-117-121`, base `b6b3416`, head `eaf815c`. Your range for the comparison is `b6b3416..eaf815c`.
- Method: `task-cycle/skill/return_step.md` read whole, with `task-cycle/skill/foundation_step.md` (the return step writes as the foundation step writes) and, for each element you write an entry of, its `SKILL.md` as `foundation_step.md` gives. Method of making a change: `task-cycle/change/SKILL.md`.
- Task: `docs/task-cycles/small-fixes-after-prs-117-121/task.md` (frozen, read whole as before). It names no entry for the return step beyond rows 1–9 and *Decisions in play*; `agent-instructions/README.md` "The form of the foundation" is named by its *Context* for the comparison with item 8.
- What to compare with the files at `eaf815c`: every foundation entry the change wrote or changed (WAY-139, WAY-344, WAY-60, WAY-61, WAY-229, the rationale of WAY-160), the entries the search of the foundation found, and the part map of the touched parts (`gate`, `elements-common` — it now holds the new file `elements/common/foundation_source.py` —, `decisions`, `invariants`, `project-level`, `product-guidelines`, `task-cycle`, `agent-instructions`), against the code and the files. Correct in the same change what no longer matches. In particular compare: the sentence and *Verification* of WAY-344 with the code of `list_invariants` and its tests; the description of the listing in `agent-instructions/README.md` and `elements/invariants/template.md` (the review's remaining Minor finding n1: both read as if an invariant is listed only when no file citing it changed, while the code lists it either way — this finding is Minor and not fixed as a finding, but if your comparison finds the two descriptions no longer match the code, correct them as the return step does); the description of the part `elements-common` in the part map with the new module; WAY-229, the two steps of `task-cycle/skill/SKILL.md` and any place that repeats their sentence.
- Do not hunt for behaviour no invariant covers; write an invariant only for a rule the task, a decision or the human sets (the return step's own rule).
- The corrected table of entries written, marks included (`the cycle's` for WAY-139, WAY-344, WAY-60, WAY-61, WAY-229 and the rationale of WAY-160), is in `reports/author-fix-report.md`; keep it in your report's account of what the change wrote, and add what the return step itself writes or corrects.
- Commit what the return step changes, by explicit paths, English messages, no push. Where it changes nothing, say so; no commit then.
- Do not run the full gate (the orchestrator's run; it starts after the return step and its review). Run the focused checks of what you change, with command and exit code, and `python -B elements/common/foundation_check.py`.
- Report path: `docs/task-cycles/small-fixes-after-prs-117-121/reports/return-step-report.md`. Your directory for working copies: `.runs/author/`. The report holds, as before, **Unread material**, **Searches not found or unclear**, the own-work check and the working copies, and the items the record's *Return step* asks (foundation compared with code; decisions, invariants, environment facts, glossary terms, part-map changes written or changed; projected entries; rows of *Settlements to record* written, each with its place).

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
in the system's temporary directory, in the scratch directory of a session or in the main checkout
of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by
itself under its session's directory is moved into the agent's directory and the original removed,
except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md`
says, to the place the product's foundation settles for screenshots, and into the agent's directory
only where no such place is settled. The files that a product's own tools and tests make by
themselves are no working copy of the agent and stay outside this rule. Before the agent returns,
each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then
`git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in
the report where each copy stood and that it was removed. Where a removal fails, the agent finishes
all the same and names in the report the remainder, with its full path and the reason it stayed.
