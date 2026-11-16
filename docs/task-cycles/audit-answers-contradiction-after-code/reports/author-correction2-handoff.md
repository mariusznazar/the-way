# Handoff to the one author — correction 2 for the human's remarks

You are a fresh author of the type `the-way-author`: the author of the earlier rounds belonged to another
session and cannot be resumed. You did not write the earlier code; read it as a reader. Ask the human
nothing; a question goes to the orchestrator in your report as `questions`. Do not run the product's full
gate (its run is the orchestrator's or CI's, WAY-160).

## What this is

The human answered the open request (https://github.com/mariusznazar/the-way/pull/138) through the day
advisor. The remarks bind and stand word for word in
`.runs/task-cycles/audit-answers-contradiction-after-code/reports/correction-2-remarks.md` — read them
whole. Method: `task-cycle/change/SKILL.md`, variant "a correction for the human's remarks", read whole,
and a file it names only when the step that names it comes; for the entries of the foundation you change,
`task-cycle/skill/foundation_step.md` and the `SKILL.md` of the element (`elements/decisions/skill/SKILL.md`
or the path `foundation_step.md` gives).

Worktree and branch: `the root of the task's worktree`,
`task/audit-answers-contradiction-after-code`. The code to correct is the head of the branch after the
merge of the target branch, `2e31b74b1a0dd3c9c787ed79a025bb7f372615a6` (the merge of `foundations` at
`30c947f`, PR #140, into the earlier head `7ef5b13`, whose code is `1d7d105`); your range starts there.
Your directory for working copies: `.runs/author-correction-2/`. Your report:
`.runs/task-cycles/audit-answers-contradiction-after-code/reports/author-correction2-report.md`.
Another agent, a reviewer, reads the merge commit meanwhile in a worktree of its own; do not rewrite
history, commit on top.

The frozen task: `.runs/task-cycles/audit-answers-contradiction-after-code/task.md` (for what the audit
must answer).

## What the remarks ask of you

**Remark 1 — the blocking finding N-1 of the review of the fix of the return step**, in
`.runs/task-cycles/audit-answers-contradiction-after-code/reports/review-return-fix-report.md` (read it
whole; its *Important* section is the finding). The sentence of WAY-405 (`foundations/decisions.md`; the
binding sentence), its *Verification* clause and two comments in the code
(`process-audit/audit_count.py`, the docstring near the line that says "gives the answer unknown unless it
opens with `reason: ` and one marker and holds no other"; `process-audit/record_items.py`, the docstring
at the top of the file) say an item whose lines are not entries at one indent alone gives `unknown` unless
it opens with `reason: ` and one marker; they leave out `none`, which the code (`discarded_reason`) reads
as "no attempt" and answers `no`. The human's remark: add "unless it reads `none` or opens with ..." in
those four places, so the sentence says what the code does. Search the whole repository for any other place
that says the same sentence (the record template's item *Discarded attempt*, `process-audit/SKILL.md`,
`task-cycle/skill/*.md`) and bring it in line, by WAY-33 of the foundation step. Code and tests do not
change for this remark.

**Remark 2 — the small remarks of the reviewers, in the same round.** The human's words: "the rare shapes of
a record listed in item 2 (a second reason word in a detail line, a second attempt with a malformed
reason word, a continuation at the left margin, and the two places where the rule is silent). Where a fix
would change what the audit answers, make the rule say what the code does and add the test; do not widen
the change beyond these." The six items stand in the request's description as *Minor findings* 1 to 6 and
in the reviewers' reports; their wording, word for word, is in
`.runs/task-cycles/audit-answers-contradiction-after-code/request.md`, section *Minor findings*, and
the margin case in the section *Findings outside the task's scope* of the same file (O-1). The reports
hold the probes:

1. a second reason word in an entry's detail line is not read (M-1 of
   `reports/review-correction-report.md`; `process-audit/record_items.py`, the reading of the entries);
2. a second attempt with a malformed reason word is read as a detail of the first (M-2 of the same
   report);
3. the docstring of `process-audit/audit_count.py` that says only the start of the item is read (M-3 of
   the same report; the return step rewrote some docstrings, check what stands now);
4. N-1 of `reports/review-correction-fix-report.md`: it concerns a sentence in an earlier author's report,
   not a file of the repository; check whether any file of the repository says what that report claimed
   (a first entry shallower than the later ones gives `unknown`) and correct it there; where none does,
   write "nothing to change" in your report;
5. WAY-404's *Verification* gives overlapping `yes` and `unknown` without saying which wins (M-1 of
   `reports/review-return-report.md`): the code gives `yes`;
6. WAY-405 is silent on an item with text after its colon and entries under it (M-1 of
   `reports/review-return-fix-report.md`): the code reads the whole as one attempt;
7. a line at the margin ends an item, so a continuation of an entry written there is not read (O-1 of
   `reports/review-correction-report.md`; `item_texts` in `process-audit/record_items.py`).

For each of the seven, choose per the human's words: where fixing the code would change an answer the
audit gives today, do not change the code — make the rule (WAY-404 or WAY-405, their *Verification*, the
template's item, `process-audit/SKILL.md` or a comment, whichever says it) state what the code does, and
add a test that holds it (a test of `process-audit/test_record_items.py` or `test_audit_count.py`,
through `read_contradiction` or the command, as the neighbouring tests are written, with the decision's
`tests:` clause where the decision's *Verification* cites it); where a fix would change no answer the
audit gives (a docstring, a sentence), make it and add a test only where behaviour is held. Where the
human's two instructions pull apart for a shape — the code gives a wrong `yes` or `no` that the rule
cannot honestly describe as intended — do not decide: return `questions` with the shape and the two ways.
Name, for each of the seven, which way you took and why, in your report.
This is the trust boundary `process-audit/record_items.py` (records are read from git history and are
untrusted): crafted input — deeper and shallower indents, tabs, a bare CR, very long or very many lines —
must give no hang and no crash, and no new wrong `yes` or `no`.

Do not widen the change beyond these. Items 3 of the request (the narrowing of WAY-344), 5 and the rest
are accepted by the human: do not change them.

## Reading

The files above, whole where you change them; WAY-404, WAY-405, WAY-337, WAY-344 of
`foundations/decisions.md` (use `python -B elements/common/decision_index.py` or the log as
`elements/common/way_of_working.md` gives for finding them), the invariants and guidelines
`guidelines/coding.md`, `guidelines/testing.md` and the guideline files of the parts you touch
(`process-audit`, `task-cycle`, the decision log); the reports named above. The merge brought in PR #140
(CI is now the final gate, WAY-160): your own checks stay focused.

## Checks

Run the affected focused checks, each with its command and exit code, a command through a pipe included:
`python -B gate/run_tests.py process-audit`, `python -B gate/run_tests.py task-cycle`, the directory of any
other file you change that holds tests, and `python -B elements/common/foundation_check.py` without
`--skip-test-citations`. Commit by path, messages in English, one commit for remark 1 and one for remark
2 where they separate cleanly.

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

## The report

As `make-change` gives it for a correction, with **Unread material**, **Searches not found or
unclear**, the own-work check and the correction's range from `2e31b74b1a0dd3c9c787ed79a025bb7f372615a6`.
Return its status, commits, a one-line check result and the report's path.
