# Handoff — the review of the whole change, `review-change`

You review, as an agent that did not make it, the whole change of one task of the-way. The person
who requested the cycle has delegated intermediate choices to the orchestrator; nothing you are told
here is that person's approval of the change. You are read-only: you change no file of the
repository.

## Where you work

- Worktree: the worktree of the task, branch `task/decision-sources-and-leftouts`. Work from that directory.
- Method of your stage: `task-cycle/review/SKILL.md` of that worktree. Read it whole; a file it names, one beside it included, only when the step or variant that names it comes. Your variant is **the whole change**.
- Range to review: from the task's base `aba5ee92a0734c2e775cc69662af669bf6455795` to the head `05b4648` (one commit; it changes `foundations/decisions.md` only: 199 added, 88 removed lines). Read the full diff of the range: `git diff aba5ee9 05b4648`.
- Your directory for working copies: `.runs/review-whole/` (directly under the ignored `.runs/` of the worktree). Its first paragraph of "Working copies" of the cycle skill:

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

- Your report: `.runs/task-cycles/decision-sources-and-leftouts/reports/review-whole-report.md`, whose first line is `PASS <sha>` or `FAIL <sha>` as the method gives; it holds the checks you ran with command and exit code, **Unread material** and **Searches not found or unclear** (each `none` or the items), and for each blocking finding the place in the code or the diff.

## What you review against

- The frozen task: `.runs/task-cycles/decision-sources-and-leftouts/task.md` (in the worktree), read whole — *Need*, *To do* 1–9, *Acceptance criteria*, *Questions to settle* with answers, *Decisions in play*, *Settlements to record* (rows 1 and 2, which go to sentences of WAY-100), *Out of scope*. There is no spec and no plan.
- The author's report: `.runs/task-cycles/decision-sources-and-leftouts/reports/author-report.md`, whole. It has a table of what was searched, found and changed for each decision.
- The answers of step 4: the change touches no trust boundary (the part `decisions`, boundary `none`) and holds no operation that cannot be undone. There was no open design choice and no reserved choice.
- Foundation and guidelines: you select your own, by the parts of the change (`foundations/part_map.md`: the part `decisions`). The decisions that govern what is checked here include WAY-100 (the rule this change applies and rewords), WAY-27, WAY-71, WAY-90, WAY-19, WAY-07, WAY-30, WAY-134 and WAY-33; the form and template of an entry: `elements/decisions/template.md` and `elements/common/rules.md`. The change writes no code and no test, so `guidelines/coding.md` and `guidelines/testing.md` are not needed unless you find a changed file other than `foundations/decisions.md`.

## What the review must test beyond reading the diff

1. **Source fidelity, the task's main risk (a made-up source looks the same as a true one).** For every *Based on* citation the change adds or changes (WAY-164 Limen `templates/worker.md` line 25 at `e746877e8ef195ab9a34a070bdd3b000d0b6cf10`; WAY-199 `customers/AGENTS.md` line 7 at `4374c48`; and each other address the diff touches — WAY-167, 199, 203, 206, 212, 228, 233, 236): open the source (you may fetch public pages) and compare the quoted passage word for word, the place in it, and that the date read is **2026-11-16** (acceptance criterion 2; WAY-90). A passage you cannot open is a finding of its own, not a pass.
2. **Source versus decision for each *Rejected* position added.** Each is an element of the practice that the decision does not take, with a reason only where the entry or the source gives it (*To do* 3). Check, against the source or the trace the author names, that the element is really in the practice, is really not taken by the decision, and that no reason was invented. Where the source is the author's private vault, or a note read from a local archive (the author's report names them as a **Reach**), you may read those too — reading only; nothing of the vault reaches the report as an absolute path or a double-bracket link, and the report need not quote private text.
3. **Acceptance criterion 1.** The binding sentences of no decision of *Need* change, WAY-100 excepted. Verify by comparing the text before `- **Scope:**` of every decision at base and head; do not rest on the author's claim.
4. **WAY-100's change** against rows 1 and 2 word for word in meaning; its *Verification*, *Rationale* and *Rejected* agree with the new paragraph; its pair of examples; that the paragraph has no more than the limit of sentences; that no other entry or test of the foundation now contradicts the new wording (WAY-33). The foundation check (`python -B elements/common/foundation_check.py`) and the tests of a single directory you judge relevant (`python -B gate/run_tests.py <directory>`) you may run; **do not run the full gate** (`python -B gate/run_tests.py` with no directory), which is the orchestrator's.
5. **Privacy and form.** No absolute path, vault path or note link in double square brackets in the diff; each *Based on* form follows WAY-90; no `TODO` in *Based on* is left where the task expected a source, and where a `none` stands for a closed source, *Rationale* says what was seen there and that the source is not open to a reader (WAY-27, the new sentence of WAY-100).
6. **Coverage of every task item.** *To do* 1–8 item by item, both lists of *Need* (the seven decisions with `TODO`, and the seventeen with no *Rejected*), WAY-136 and WAY-148 each judged separately (adopts or evidence only: examine the author's evidence, which lies in the research and plan notes of the author's vault, and judge whether the conclusion — WAY-136 evidence only, WAY-148 adopts — is the one the evidence supports), the eight lessons decisions' sentence (WAY-121, 237, 256, 268, 270, 273, 280, 374), WAY-199 and WAY-203. *To do* 9 (the request's list of where the agent searched) is the orchestrator's, built from the author's report.
7. **Unread material of the author, which you may judge.** The author did not open the data file of the foundation review of 2026-11-14 (the data file of the foundation review of 2026-11-14 in the author's notes in the author's vault, section "Fundament" → "Propozycje", P7), which holds what the review said about WAY-136; the task's *Context* quotes its conclusion. The author read the map of the course and the lesson notes partly. Judge whether anything in what the author left unread bears on a finding of yours; if so, read it.
8. The author reports that WAY-145 has the same gap WAY-136 had (the map of the course says it takes a practice "in changed form"; it has no `derives from WAY-100`) and that it stands on no list of the task. This is **outside the task's scope** unless you find the change itself broke something; do not grade it blocking. Give your own view in the report if the evidence in the diff or in what you read says otherwise.

You alone grade and scope your findings (Critical, Important, Minor, outside the task's scope); no one moves a finding from one kind to another. Return with the short return the method gives: the first line, the checks, the report's path, the blocking findings, the Minor findings, those outside the scope, **Unread material** and **Searches not found or unclear**.
