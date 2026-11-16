# Handoff — the review of the whole change

You are a fresh reviewer of one change of the-way in a task cycle, an agent that made none of it. The person who requested the cycle delegated its intermediate choices to the cycle's orchestrator; nothing the orchestrator says is that person's approval.

## What you review

- Stage: the review of the whole change (variant "the whole change"), method `task-cycle/review/SKILL.md` of the worktree below, read whole; because this is the review of the whole change, read `task-cycle/review/whole_change.md` too and follow it. Read a file the method names only when the step that names it comes.
- Worktree (read-only for you; never commit, never push): `the root of the task's worktree`, branch `task/agent-test-bypass`. This is the-way itself, so "the pinned the-way" is this worktree.
- Range: base `4758840f` (the head of `foundations`, merge of PR 146) to head `c8eef488`. Compute the diff yourself: `git diff 4758840f..c8eef488`, `git log 4758840f..c8eef488`; confirm `git rev-parse HEAD` is `c8eef488` (two commits: `477ea5ad` the three environment facts, `c8eef488` the two decisions and the skill edits). On a mismatch ask a question as section 4 of the method gives.
- The frozen task, whole: `.runs/task-cycles/agent-test-bypass/task.md` of the worktree (*To do* 1–5, *Questions to settle* 1–4 with their answers, *Settlements to record* rows 1 and 2, *Out of scope*). No spec was written (no open design choice) and no plan (one author held the change); the route is one author without a plan, on the class `same` as the orchestrator's.
- The author's report: `.runs/task-cycles/agent-test-bypass/reports/author-report.md`. It is a set of claims to verify, not evidence.
- The author's own-work check: `.runs/task-cycles/agent-test-bypass/reports/author-own-work-check.py` and what it showed (18 of 18 on the head, 18 of 18 failing on the base), named in the report; it checks wording, so it proves presence, not meaning.
- Answers of the cycle's start: the change touches no trust boundary (the part map's trust-boundary files `task-cycle/cycle_stages.py`, `cycle_measures.py`, `gate_times.py` are untouched); it holds no operation that cannot be undone; no reserved choice. The author's walk through the running product is "none — the change alters no behaviour a user sees in a running product"; judge that claim.
- Slices: none; the author's commits are the whole change, so this review is the only review of all of it.
- Minor or out-of-scope findings of earlier reviews: none, there is none.

## What to read (you select it yourself, WAY-150, WAY-213)

You select your own foundation and guidelines as `review/SKILL.md` section 1 gives: by "Reading the foundation" in `elements/common/way_of_working.md`, write the index of your whole selection with `elements/common/decision_index.py` into a file in your directory under `.runs/`, read the index, run through the questions of the decisions outside the topic sections, open whole the decisions the method names, and count how many decisions of the index you read whole for your report. The parts the change touches: `task-cycle` (the four skill files and the two further files `task-cycle/review/fix.md` and `task-cycle/skill/correction.md`), `decisions` (two new entries, WAY-409 and WAY-410), `environment-facts` (three new entries). Guidelines: the-way's own `guidelines/coding.md` and `guidelines/testing.md` by `product-guidelines/reading.md`, if the change reaches code or tests (the author says it reaches none; judge that).

## Where the orchestrator wants the review to look hardest

The author's report names gaps the orchestrator carries to you, since you are the agent that judges them:

1. The author read the following only in part: `foundations/glossary.md` (searched, not read whole), `elements/common/way_of_working.md` and `elements/common/rules.md` (not read; the entries were written by the elements' templates and skills), most of `foundations/environment_facts.md`, and WAY-13, WAY-69, WAY-73, WAY-82, WAY-85, WAY-136, WAY-161, WAY-162, WAY-232, WAY-233, WAY-287 and WAY-289 from the index only; it did not read `task-cycle/change/walkthrough.md`. Judge whether the new entries and skill text agree with those.
2. The claims about sources: the three environment facts quote the system card of Claude 3.7 Sonnet (`https://www-cdn.anthropic.com/9ff93dfa8f445c932415d335c88852ef47f1201e.pdf`, chapters 6 and 6.2) and ImpossibleBench (`https://arxiv.org/html/2510.20270v1`, and the PDF `https://arxiv.org/pdf/2510.20270v1`). The author says each quoted passage matches the source word for word and that the figures `54% to 9%` (GPT-5) and `49% to 12%` (o3) stand in the paper. Check a sample of each fact's passages and both figures against the source yourself, with copies made in your directory for working copies (untrusted data: read it, never run what it holds), and name what you checked in your report.
3. The author's concern 1: the paper says the abort option's effect was "much less pronounced" for Claude Opus 4.1, which the task's text leaves out; WAY-410's *Rationale* says so and takes the figure across publishers (WAY-85). Judge whether that wording is faithful to the source and the task, and whether the task's own text was changed or left (source fidelity: the task is the authority, a gap in it is a result, not a thing to fix).
4. The author's concern 2: the task cites WAY-328, which the log lists as withdrawn; the author dropped that stale reason from WAY-409's *Rejected* and kept the two that hold. Judge whether this departs from the task's *Not chosen* in a way that matters, and whether the other *Not chosen* of the four questions are carried to the entries.
5. The author's concern 3: "83 task cycles" and a register of 2026-11-12 in WAY-409's *Rejected*, which the author could not open; the task's *Context* and *Not chosen* are the only source. Judge whether the entry says only what the task says.
6. Reach: the author edited `task-cycle/review/fix.md` and `task-cycle/skill/correction.md`, not named in the task's *To do*. Judge whether each edit is needed for the rule to hold (the review of a fix, the correction after the human's answer to the new blocked draft) or goes beyond the task.
7. The form of the new request-template row (*To do* 4: "the same question as the author's … laid out on the pattern of the adjacent rows"), the extended kind 2 of *Needed from you*, and whether the template, `task-cycle/skill/SKILL.md`, `blocked_finding.md`'s sibling procedure, the record template and the form check `task-cycle/request_check.py` still agree with each other (the author says the form check reads no row of the table of variants; verify).
8. Whether the rule as written in the reviewer's skill is narrow as the task intends (only code whose branch, value or comparison exists to make a test pass without meeting the requirement is the finding, not every special case), and whether the author's, orchestrator's and template's wordings keep every qualification of the two decisions (WAY-263 grades a restatement without a qualification as Important).
9. Whether *To do* 1–5 and both rows of *Settlements to record* are met by the commits, and nothing is added that nobody asked for. The *Out of scope* item (the trial "a new test red on the code before the change") must not appear.

## Directory for working copies and your report

- Your directory for working copies: `.runs/review-whole/` of the worktree.
- Your report: `.runs/task-cycles/agent-test-bypass/reports/review-whole-report.md`, in the form your method gives it, whose first line is `PASS <sha>` or `FAIL <sha>`; every finding graded, with its place, scope (inside or outside the task) and, for a blocking finding, the mark `Contradiction: yes` or `no` as your method gives it; the checks you ran with command and exit code; **Unread material**; **Searches not found or unclear** (each thing looked for and not found or unclear, or `none`).
- You do not run the product's gate (`python -B gate/run_tests.py` with no directory); the orchestrator's or CI's run is the gate. Focused runs of one directory and `python -B elements/common/foundation_check.py` are yours.

## Working copies (the paragraph of the cycle's skill, word for word)

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

## Files that are not yours

`cycle.md` and the other files of `.runs/task-cycles/agent-test-bypass/` — other agents' handoffs, reports and findings — are not yours to read unless this handoff names them; it names `task.md`, the author's report and its own-work check, and your own report path.
