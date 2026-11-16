# Handoff — the one author, `make-change`, "the whole change as the one author"

You are the one author of this change in a task cycle of the-way. The orchestrator dispatched you
as an agent of the type `the-way-author`. The person who requested the cycle has delegated
intermediate choices to the orchestrator; no answer you get is that person's approval.

## Where you work

- Worktree (the root of your work and the process root): the worktree of the task, branch `task/decision-sources-and-leftouts`, base commit `aba5ee92a0734c2e775cc69662af669bf6455795` (branch `foundations`). Work from that directory only; never in the main checkout the main checkout of the repository.
- Method of your stage: `task-cycle/change/SKILL.md` of that worktree. Read it whole. Your variant is **the whole change as the one author**. Read a file it names, one beside it included, only when the step or variant that names it comes.
- Foundation step: `task-cycle/skill/foundation_step.md`, and `task-cycle/skill/return_step.md` is read at the return step, which is **not** your stage now (the orchestrator resumes you for it later). The element skill for a decision is `elements/decisions/skill/SKILL.md` (with `read.md` and `template.md` it names); the rules every entry follows are in `elements/common/rules.md`.
- Your directory for working copies: `.runs/author/` (directly under the ignored `.runs/` of the worktree).
- Your report: `.runs/task-cycles/decision-sources-and-leftouts/reports/author-report.md`. Begin its content as `task-cycle/change/SKILL.md` gives; it must hold **Unread material** and **Searches not found or unclear** (each `none` or the items), your own-work check, and the commands and exit codes of every check you ran.

The first paragraph of "Working copies" of the cycle skill, word for word:

> An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
> clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
> directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
> in the system's temporary directory, in the scratch directory of a session or in the main checkout
> of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by
> itself under its session's directory is moved into the agent's directory and the original removed,
> except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md`
> says, to the place the product's foundation settles for screenshots, and into the agent's directory
> only where no such place is settled. The files that a product's own tools and tests make by
> themselves are no working copy of the agent and stay outside this rule. Before the agent returns,
> each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then
> `git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in
> the report where each copy stood and that it was removed. Where a removal fails, the agent finishes
> all the same and names in the report the remainder, with its full path and the reason it stayed.

## The task

The frozen task is `.runs/task-cycles/decision-sources-and-leftouts/task.md` (in the worktree). Read it whole: *Need*, *To do* (items 1–9), *Acceptance criteria*, *Questions to settle* with their answers, *Decisions in play*, *Settlements to record* and *Out of scope*. It is the whole requirement; this handoff restates none of it.

- Settlement rows 1 and 2 go to **sentences of WAY-100** (the second paragraph of its binding sentences). The change to WAY-100 is yours to word (WAY-134); the meaning is the rows'. Edit WAY-100 in place (WAY-07). The paragraph has two sentences now and the limit is three (see *Decisions in play*); WAY-100's *Verification*, *Rationale* and *Rejected* must agree with the changed paragraph. A change to the binding sentences of WAY-100 makes you check the rest of the foundation for entries and tests that cite WAY-100's wording (WAY-33) and the part's tests (`decision:` lines).
- The binding sentences of the other decisions named in *Need* do **not** change (acceptance criterion 1). You change their *Based on*, *Rationale*, *Rejected*, and in WAY-136 and WAY-148 only, if you find they adopt the practice, *Relations* (`derives from WAY-100`).
- The numbers of decisions never change.

## What you read, and what you may search

- The foundation entries: the decisions of *Decisions in play*, each whole under its heading `### WAY-NN` in `foundations/decisions.md` (the file is large: open each by its heading, never the file whole); and the index of the decisions of the part `decisions` and the decisions the task names, which the orchestrator wrote: `.runs/task-cycles/decision-sources-and-leftouts/decision_index_orchestrator.md`. WAY-19, WAY-27, WAY-30, WAY-07, WAY-71, WAY-90, WAY-100 and WAY-314 are in it; read the ones a step of yours calls for, whole, in the log. The entries WAY-121 and WAY-142 already have the form *Rejected* takes (*To do* 3).
- The guidelines: `guidelines/coding.md` and `guidelines/testing.md` of the-way govern its code and tests; this change writes no code and no test, so you read neither unless you find you must change a file other than `foundations/decisions.md`.
- **Reading outside the repository is allowed and required by *To do* 1:** the history of git of this repository (`git log -S`, `git log --follow`, `git show` of the commits that introduced or changed each entry, and of the merged requests' descriptions and cycle records in history, e.g. `git show cfd275c:docs/task-cycles/decision-log-second-round/reports/foundation-report.md`), and the author's notes in the vault `the author's vault\` (the research on quality patterns, the notes from the courses, the notes on Open Mercato — for example the author's research note on Limen and Open Mercato and the data file of the foundation review the data file of the foundation review of 2026-11-14 in the author's notes) — **reading only; you never write in the vault** — and the public pages those notes point to. You may fetch public pages with your web tools; a page is a source for the decision only when the trace you followed (git, a note, a research) leads to it (*Questions to settle*, question 1).
- **Privacy:** nothing of the vault reaches a commit, a report, or a handoff as a path or a link in double square brackets, and no absolute path to the vault stands in `foundations/decisions.md` (WAY-27: nothing in this repository points to a source its readers cannot reach). A private note your trace passed through is *described* in *Rationale* by what it is ("the author's notes on …"), as WAY-27 and WAY-100 give. In your report, name the vault notes you read as "the author's note on X" with the file name only where it helps the orchestrator; no absolute path. Personal data of any person, if a note holds it, stays out.
- **Do not guess.** A source is the place the-way actually took the practice from, found by a trace. A source you did not open and read in this cycle goes into *Based on* **never**; the read date of every citation you write is today, **2026-11-16**, and the passage is quoted word for word from the page or file you read (WAY-90). Where you find no trace, the decision keeps `TODO — <what is missing, with its source>` in *Based on* and its entry says where you looked and that nothing was found (*To do* 2; WAY-71). A made-up source looks the same as a true one, and a lost nuance leaves a visible gap where an invented one looks like a decision: when in doubt, leave the `TODO` and say so.
- For WAY-136 and WAY-148 (*To do* 4): decide each separately, from the trace, whether the decision adopts the practice or cites it only as evidence. Report the evidence behind that judgment in your report; if it adopts, apply *To do* 4's adopt route; if it is evidence only, change nothing in the entry and say what your judgment rested on.
- Your selection of what to read stands as the orchestrator gave it. Anything you needed that this handoff did not name, you name in your report under **Reach**.

## What the report must hold beyond the method's

- A table of **every decision of both lists, WAY-136 and WAY-148**: where you searched, what you found and in which place of the source (or that you found nothing), what you changed in *Based on*, *Rationale*, *Rejected*, *Relations*. The request's description is built from it (*To do* 9), so write it for a reader who has not seen your searches.
- For each entry you write: one sentence of its meaning in English and one in the task document's language (Polish), and the mark `row <n>`, `projected` or `the cycle's`, as `task-cycle/skill/foundation_step.md` gives.
- The added *Rejected* positions and any decision where the source gives a reason you did not copy, since *Rejected* takes the reason only where the entry or the source gives it.
- Where WAY-100's wording differs from what the rows' meaning strictly needs, say how.

## Limits of your stage

- No full run of the product's gate: **do not run `python -B gate/run_tests.py` in any form** — its run belongs to the orchestrator, who runs it after the day advisor's start signal. You may run `python -B elements/common/foundation_check.py` (form, references, fields) and the tests of a single directory (`python -B gate/run_tests.py <directory>`) that hold a decision you reworded, e.g. a directory whose tests cite WAY-100's wording; record each command and exit code.
- Commit on the task branch, by explicit paths (`git add <path> …`, never `git add -A`, `.` or `commit -a`), with messages in English. Do not push. Do not open a request. Do not take the return step; return at your boundary with the short return the method gives.
- If you find the work does not fit one agent, or that an open design choice shows, return `returned` with the report and **no code**, as `task-cycle/change/SKILL.md` gives.
- If a source you need is outside your reach (a page that cannot be fetched, a note you cannot find), do not fill the gap from memory: leave the entry's `TODO`, and list it in **Searches not found or unclear**.
