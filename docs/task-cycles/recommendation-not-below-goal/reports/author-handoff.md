# Handoff — the one author of the change (`make-change`)

## Delegation

The person who requested this cycle has delegated the intermediate choices of the cycle to the
orchestrator. No answer or go-ahead in this handoff is that person's approval. The human reviews the
request, not the steps.

## Where and what

- Worktree (your working directory, the process root): `the task's worktree`, branch `task/recommendation-not-below-goal`, base `301e4eae1111310ccd80e466f62ea01838b9ff88` (`foundations`). The process is the-way itself: there is no `.the-way` submodule, every path below is a path in this worktree. Write only here, never in the main checkout `the main checkout of the repository`.
- Method: `task-cycle/change/SKILL.md`. Read that `SKILL.md` whole, and a file it names, one beside it included, only when the step or variant that names the file comes. Variant: **the whole change as the one author**.
- Stage and boundary: you make the whole change, the foundation step with it, commit it on the task branch and return before any review. The foundation step is `task-cycle/skill/foundation_step.md` — read it whole. The orchestrator runs the product's gate; you do not (WAY-160). You do run the checks your change calls for (below).
- Frozen task: `.runs/task-cycles/recommendation-not-below-goal/task.md` — read it whole, it is the whole task (*Need*, *To do* 1–3, the answered questions 1–4, *Decisions in play*, *Settlements to record* rows 1 and 2, *Out of scope*). It was approved as `Status: ready for cycle`, relation independent. There is no spec and no plan.
- `cycle.md` and the other files of `.runs/task-cycles/recommendation-not-below-goal/` — other agents' handoffs, reports and findings — are not yours to read, save the frozen task and this handoff.

## Answers of the start (step 4)

- Trust boundary: no. Irreversible operation: no.
- Open design choice: none. The settlement rows and the four answered questions of the task fix what the rule says and where it stands. Choosing the words, and dividing WAY-113's binding sentences into paragraphs so that `elements/common/foundation_check.py` stays quiet, are yours to do and to name in the report.
- Class: `same` as the orchestrator's.

## What to read

Foundation entries (by identifier, in `foundations/decisions.md`; the whole entry of each, including *Rejected*, for those marked *): WAY-113* (the decision the task changes), WAY-120 (the critique; the task does not change it), WAY-35 (one copy of a rule), WAY-33 (the search of the foundation once the entry is settled), WAY-166* (a decision whose rationale says "the human is owed a recommendation (WAY-113)" where no option can be used by an agent — the orchestrator's selection found it as the one entry likely to meet the new rule; judge whether it collides with "a way below the goal is never recommended; where no way reaches the goal the question recommends none", and if it does, follow `agent-instructions/README.md` "Make the change" for what you may correct yourself and what goes to the human), WAY-25 and WAY-114 (what a collision with an accepted decision lets you do). Select further by `elements/common/way_of_working.md` "Reading the foundation", as `foundation_step.md` gives for an author who writes entries; the rows' *Goes to* names the files.

Files to change and read whole: `elements/common/way_of_working.md` (rule "How a skill asks"), `elements/common/critique/prepare.md`, `elements/common/critique/SKILL.md` and `elements/common/critique/check.md` (read, to see that `check.md` stays as it is). The element's template and skill for a decision is `elements/decisions/template.md` and `elements/decisions/skill/SKILL.md`: read them before you edit WAY-113.

Guidelines: the change writes prose of the foundation and no code; if you add or change any test, first read `guidelines/testing.md` and the coding guideline of the part (`guidelines/coding.md`), each whole, and name that in the report as a reach.

## Facts the orchestrator found, to keep you from searching twice

- The first paragraph of WAY-113's binding sentences already has three sentences and about 140 words; the whole binding part about 310 words. `foundation_check.py` reports, for a decision the change alters, a paragraph over three sentences or 300 words and a binding part over 600 words in all, so the new sentences stand in a paragraph of their own (or the paragraphs are divided otherwise) and the check must be run on the result.
- WAY-113 has a *Verification* (complies / violates) that the task's row 1 changes together with its binding sentences; its *Rationale* and *Rejected* carry the reasons and the ways refused, which the settlements' *Not chosen* gives you.
- `elements/common/way_of_working.md` has the rule "How a skill asks" in prose and quotes WAY-113; row 1 puts the rule's sentence in the bullet that starts "A question of decision — a choice that settles something in a file —". A rule of the foundation stands once (WAY-35): do not restate the rule in `check.md`, in the skills that ask, or in the element templates; `prepare.md` carries only the one added requirement of row 2, in the paragraph that starts "Give the fresh agent the complete proposal or set".
- `.claude/skills/the-way-critique/` and `.agents/skills/the-way-critique/` are entry points generated from the skill's description; this change touches no skill's description or name, so no `skill_entry_points.py --write` run is needed. Say in the report if you find otherwise.
- No invariant is asked for: the task and its rows set none, so write none (the return step compares; it writes an invariant only for a rule the task, a decision or the human sets).

## Checks you run

`python -B elements/common/foundation_check.py` from the worktree's root, with `--skip-test-citations` as long as an invariant of yours reads `test` without its test (expected not to arise), and without it on the finished change; the tests of every directory your change reaches with `python -B gate/run_tests.py <directory>` (for `elements/common` at least, since the check and the templates are read there); any instruction-file check the change reaches (`python -B` the check named in `instruction-files/` for a file of the foundation that holds an instruction, if the files you edit are read by it — find it, do not guess). Record each with its command and exit code in the report.

Your own-work check (WAY-164): name the requirement the change is likeliest not to meet — for example that "no less than the goal" covers every goal the material sets and not only a goal with a pattern, or that the new sentence leaves the question of a goal not worth its cost as a separate question — and say what check you ran on it and what it showed.

## Report

Write the report in full to `.runs/task-cycles/recommendation-not-below-goal/reports/author-report.md` and return its status (`done`, `done with concerns`, `questions`, `returned`, `reserved` or `blocked`), your commits, a one-line check result and that path. The report file is the input of the cycle's scripts (`task-cycle/remarks_check.py` reads it): the harness's refusal of a file whose name starts with `report`, `summary`, `findings` or `analysis` does not apply to this name; if the write is refused all the same, return the report whole as your answer. Its first line is yours; it holds the sections the method gives, **Unread material** (what this handoff names that you left unread or read in part, or `none`) and **Searches not found or unclear** (each thing you looked for and did not find or found unclear, or `none`) among them, and the meaning sentences of each foundation entry you wrote or changed, in the human's language (Polish), as `foundation_step.md` gives.

Commit on the task branch, adding files by path (`git add <path> …`), with a message in English as the repository's earlier commits are.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
in the system's temporary directory, in the scratch directory of a session or in the main checkout
of the repository. In a product, a worktree or checkout made to run checks gets its `.the-way`
populated, and the dependencies those checks need installed as the product's own rules give,
before they run; otherwise they fail for that reason. The screenshot that a screenshot tool, such as the Playwright server, saves by
itself under its session's directory is moved into the agent's directory and the original removed,
except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md`
says, to the place the product's foundation settles for screenshots, and into the agent's directory
only where no such place is settled. The files that a product's own tools and tests make by
themselves are no working copy of the agent and stay outside this rule. Before the agent returns,
each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then
`git worktree prune` — keeps in `reports/` beside its report what the report needs, the input and
command of a probe that shows a finding among them, and states in
the report where each copy stood and that it was removed. Where a removal fails, the agent finishes
all the same and names in the report the remainder, with its full path and the reason it stayed. It
removes a copy, as any directory, by its path written out in full in the command, never through a
shell variable: an empty variable turns the removal on the directory the shell stands in.

Your directory for working copies: `.runs/author/`.
