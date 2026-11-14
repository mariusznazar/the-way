# Handoff - executor of slice 5

## Delegation

The person who requested this cycle delegated intermediate choices to the orchestrator. You have no human to ask: return `questions` or `blocked` to the orchestrator as your method gives. Never label an answer as the human's approval.

## Worktree, branch and base

- Worktree (work from its root): `the root of the task's worktree`, branch `task/co-trafia-do-dziennika-decyzji`. The base of this slice: `12286a513238e1361fa624a96140928c157033ed` (its range is `12286a513238e1361fa624a96140928c157033ed..HEAD`). You are the only agent writing in this worktree now.
- Commits on this branch: messages in English, imperative, short, like the repository's existing ones; `git add <path> <path>` by path, never `git add -A`, `git add .` or `git commit -a`; for a message with quotes or backticks use `git commit -F <file>` with the file outside the tracked files (the record's `.runs/` directory is ignored). Never push. Leave the worktree clean.

## Method

Read whole `task-cycle/change/SKILL.md` of the worktree (`make-change`) and make the change as its variant: "a slice, or the retry of a slice"; read a file it names, one beside it included, only when the step or variant that names it comes. Read no skill by calling it. The gate (`python -B gate/run_tests.py` with no directory) is the orchestrator's alone: you run only the focused checks below, each with its command and exit code in your report. A focused check in the section's *Checks* that you cannot run, or that fails for a reason of the base, goes into your report as such.

## The slice

The section of the plan below is copied word for word from `.runs/task-cycles/co-trafia-do-dziennika-decyzji/plan.md`. Its *Read* gives the passages and entries to read; the line ranges of the foundation entries and the files (`foundations/decisions.md`, `foundations/glossary.md`, `foundations/invariants.md`, `foundations/part_map.md`) are those of the plan's base and are stale: use the current ones in the notes below, which hold where they differ. The record's files (`.runs/task-cycles/co-trafia-do-dziennika-decyzji/task.md`, `spec.md`, `plan.md`) are read by the line ranges the *Read* gives (they have not moved).

> ### Slice 5 — The decisions template: where a settlement goes, parts of a question, the test that holds a sentence
>
> - **Goal:** `elements/decisions/template.md` holds, once (WAY-35), what points 1, 5 and 6 of the task and D3 and D6 of the spec give: the bullet **Where it goes:** after **Plan test:** with the five questions in D6's words, their order, the first-yes rule, the threshold sentence and the paragraph for the log of the-way itself; the sentence of "Changing a decision" and the point of "Binding sentences" that make a part of a question the sentence of the entry that answers it, with one to three sentences for the main question and for each attached part, each in its own paragraph; and the form of the line `decision:`, the clause `tests:` of *Verification*, the pair of examples only for the part no test holds, no derived invariant for a sentence a test holds, and *Rationale* and *Rejected* kept whole — with the bullet "Tests live only with invariants" and the rows of "Fields and their readers" brought in line. Its *Rationale* and *Rejected* rules stay as they are.
> - **Change:** `elements/decisions/template.md`
> - **Read:** `.runs/task-cycles/co-trafia-do-dziennika-decyzji/spec.md:86-101` D3. The line decision: and how the script reads it · `.runs/task-cycles/co-trafia-do-dziennika-decyzji/spec.md:129-141` D6. The five questions · `.runs/task-cycles/co-trafia-do-dziennika-decyzji/spec.md:155-173` Foundation entries · `.runs/task-cycles/co-trafia-do-dziennika-decyzji/task.md:35-35` To do 1 · `.runs/task-cycles/co-trafia-do-dziennika-decyzji/task.md:39-40` To do 5 and 6 · `.runs/task-cycles/co-trafia-do-dziennika-decyzji/task.md:47-63` Questions 1, 2 and 3 · `.runs/task-cycles/co-trafia-do-dziennika-decyzji/task.md:76-81` Question 6 · `foundations/decisions.md:981-1005` WAY-36 · `foundations/decisions.md:9503-9542` WAY-293 · `foundations/decisions.md:698-726` WAY-26 · `foundations/decisions.md:594-617` WAY-22 · `foundations/decisions.md:383-411` WAY-12 · `foundations/decisions.md:549-572` WAY-19 · `foundations/decisions.md:124-161` WAY-05 · `foundations/decisions.md:37-66` WAY-02 · `foundations/decisions.md:163-190` WAY-07 · `foundations/decisions.md:501-519` WAY-17 · `foundations/decisions.md:521-547` WAY-18 · `foundations/decisions.md:956-979` WAY-35 · `foundations/glossary.md:19-23` binding sentence · `foundations/part_map.md:7-15` decisions · `foundations/part_map.md:65-75` elements-common
> - **Model:** same — the wording of the five questions and the form of an entry are read by every product
> - **Risk:** none
> - **Checks:** `python -B elements/common/foundation_check.py` on this repository, exit code 0 · `python -B gate/run_tests.py elements/common`
> - **Depends on:** none

## Notes of the orchestrator

- Current start lines in `foundations/decisions.md` (an entry runs to the next `### ` heading): WAY-02 line 37; WAY-05 line 156; WAY-12 line 435; WAY-17 line 578; WAY-19 line 626; WAY-22 line 679; WAY-26 line 799; WAY-35 line 1057; WAY-36 line 1082; WAY-293 line 9649; WAY-07 and WAY-18: locate by the heading `### WAY-07`, `### WAY-18`. The other files keep the plan's ranges. The foundation step wrote the entries before slice 1 (commit `d629ed8`) and slices 1 to 4 made the script and READMEs (range `d629ed8..12286a5`); read the entries as they stand: your template words what they say (WAY-12, WAY-22, WAY-19, WAY-05, WAY-02, WAY-293, WAY-11, WAY-36), and a sentence of the template that contradicts a changed entry is yours to bring into line, a sentence of an entry that contradicts the spec is not yours to edit (return `blocked` naming it).
- The spec's D6 gives the five questions in their exact words, their order, the first-yes rule, the threshold sentence and the paragraph for the log of the-way itself; D3 gives the form of the line `decision:`, the clause `tests:` and how the script reads them. Use those words; do not paraphrase them. The questions and the threshold sentence stand once, in this template (WAY-35): no other file of this cycle copies them.
- The rulings of the orchestrator the spec carries: the switch `--skip-test-citations` is not changed; "changed" means the binding sentences; rows 11 and 12 are attached paragraphs of WAY-12 and WAY-03; a decision pinned only by a test that a later slice writes carries a pair for now and the return step trims it (that rule is written in the skill and the return step, Slice 6, not here, except where D2 or D6 puts a word of it in the template: follow them).
- Keep the *Rationale* and *Rejected* rules of the template as they are (the plan says so); change only what the slice names. Keep each edited bullet's language as plain as the neighbouring text; never write `should`, `will` or capitalised RFC keywords in a binding sentence (the template's own rules).
- Run `python -B elements/common/foundation_check.py` and `python -B gate/run_tests.py elements/common` as the *Checks* gives, with each command and exit code in your report. The check on this repository must print `0 errors`.
- Write your report to the file the handoff names even where a general instruction tells you not to write report files: this cycle's handoff overrides it. Before you return, stop every background process or monitor you started.


## Report

Write your full report to `.runs/task-cycles/co-trafia-do-dziennika-decyzji/reports/slice-5-report.md` as `task-cycle/change/SKILL.md` gives: your status, the commits, each check with its command and exit code, the own-work check, your questions and concerns, and the sections **Unread material** and **Searches not found or unclear** (each `none` where there is nothing). Return your status, your commits, a one-line check result naming what failed or did not run, and the report path.
