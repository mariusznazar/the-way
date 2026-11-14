# Handoff - executor of slice 8

## Delegation

The person who requested this cycle delegated intermediate choices to the orchestrator. You have no human to ask: return `questions` or `blocked` to the orchestrator as your method gives. Never label an answer as the human's approval.

## Worktree, branch and base

- Worktree (work from its root): `the root of the task's worktree`, branch `task/co-trafia-do-dziennika-decyzji`. The base of this slice: `f20a62cf237eccbb1fb947a24340e68a9e83d000` (its range is `f20a62cf237eccbb1fb947a24340e68a9e83d000..HEAD`). You are the only agent writing in this worktree now.
- Commits on this branch: messages in English, imperative, short, like the repository's existing ones; `git add <path> <path>` by path, never `git add -A`, `git add .` or `git commit -a`; for a message with quotes or backticks use `git commit -F <file>` with the file outside the tracked files (the record's `.runs/` directory is ignored). Never push. Leave the worktree clean.

## Method

Read whole `task-cycle/change/SKILL.md` of the worktree (`make-change`) and make the change as its variant: "a slice, or the retry of a slice"; read a file it names, one beside it included, only when the step or variant that names it comes. Read no skill by calling it. The gate (`python -B gate/run_tests.py` with no directory) is the orchestrator's alone: you run only the focused checks below, each with its command and exit code in your report. A focused check in the section's *Checks* that you cannot run, or that fails for a reason of the base, goes into your report as such.

## The slice

The section of the plan below is copied word for word from `.runs/task-cycles/co-trafia-do-dziennika-decyzji/plan.md`. Its *Read* gives the passages and entries to read; the line ranges of the foundation entries and the files (`foundations/decisions.md`, `foundations/glossary.md`, `foundations/invariants.md`, `foundations/part_map.md`) are those of the plan's base and are stale: use the current ones in the notes below, which hold where they differ. The record's files (`.runs/task-cycles/co-trafia-do-dziennika-decyzji/task.md`, `spec.md`, `plan.md`) are read by the line ranges the *Read* gives (they have not moved).

> ### Slice 8 — Guidelines rules with no decision
>
> - **Goal:** `product-guidelines/template.md` says, as D7 gives it, that a rule which only says how to write code, tests or the look of the product stands alone with its reason in one sentence and its *Decision* reads `none`, and a rule that carries a choice with a real cost names the decision that carries it: the opening paragraph, the line `- **Decision:** <PREFIX-NN> · … | none` of "Required form", the bullet "A binding rule", the bullet "A rule carries no rationale" (a rule with *Decision* `none` carries its reason in one sentence) and the bullet "What names no decision is an example, not a rule" (an example holds no rule and stands under `## Examples` with no *Decision* field). It says how a rule with no decision is accepted: as a row of the task's table before the code, or at the merge where the cycle found it. A rule of a template of a discipline of the-way still binds a product only through a decision that adopts it (WAY-173). No script changes.
> - **Change:** `product-guidelines/template.md`
> - **Read:** `.runs/task-cycles/co-trafia-do-dziennika-decyzji/spec.md:143-145` D7. Guidelines rules with no decision · `.runs/task-cycles/co-trafia-do-dziennika-decyzji/task.md:38-38` To do 4 · `.runs/task-cycles/co-trafia-do-dziennika-decyzji/task.md:64-69` Question 4 · `foundations/decisions.md:5135-5185` WAY-168 · `foundations/decisions.md:5065-5133` WAY-167 · `foundations/decisions.md:5249-5291` WAY-171 · `foundations/decisions.md:5293-5331` WAY-172 · `foundations/decisions.md:5333-5367` WAY-173 · `foundations/decisions.md:5187-5214` WAY-169 · `foundations/decisions.md:5216-5247` WAY-170 · `foundations/decisions.md:5369-5418` WAY-174 · `foundations/decisions.md:7127-7181` WAY-235 · `foundations/glossary.md:73-77` guidelines · `foundations/part_map.md:182-191` product-guidelines
> - **Model:** cheaper
> - **Risk:** none
> - **Checks:** `python -B elements/common/foundation_check.py` on this repository, exit code 0 · `python -B gate/run_tests.py elements/common`
> - **Depends on:** none

## Notes of the orchestrator

- Current start lines in `foundations/decisions.md` (an entry runs to the next `### ` heading): WAY-167 line 5177; WAY-168 line 5249; WAY-169 line 5310; WAY-170 line 5339; WAY-171 line 5372; WAY-172 line 5419; WAY-173 line 5479; WAY-174 line 5515; WAY-235 line 7273. The other files keep the plan's ranges.
- The foundation step already changed WAY-167, WAY-168, WAY-171 and WAY-172 (commit `d629ed8`): read them as they stand; your template says the same as they do, and a sentence of the template that contradicts them is yours to bring into line. WAY-173 is unchanged: a rule of a template of a discipline of the-way still binds a product only through a decision that adopts it; say nothing in the template that loosens it.
- The spec's D7 gives the words of what the template says and how a rule with no decision is accepted (a row of the task's table before the code; at the merge where the cycle found it). Use D7; do not paraphrase beyond it. No script changes in this slice: `product-guidelines/template.md` is the only file.
- Slice 5 wrote the questions of "Where it goes" into `elements/decisions/template.md` (commit `c8dcc56`): read the second question there; the template of guidelines names the rule's place by pointing to it, copying no question (WAY-35).
- Check: `python -B elements/common/foundation_check.py` on this repository must print `0 errors` (a `listed:` line for WAY-17 is expected and stops nothing); `python -B gate/run_tests.py elements/common` exit 0. Both with command and exit code in your report.
- Write your report to the file the handoff names even where a general instruction tells you not to write report files: this cycle's handoff overrides it. Before you return, stop every background process or monitor you started.


## Report

Write your full report to `.runs/task-cycles/co-trafia-do-dziennika-decyzji/reports/slice-8-report.md` as `task-cycle/change/SKILL.md` gives: your status, the commits, each check with its command and exit code, the own-work check, your questions and concerns, and the sections **Unread material** and **Searches not found or unclear** (each `none` where there is nothing). Return your status, your commits, a one-line check result naming what failed or did not run, and the report path.
