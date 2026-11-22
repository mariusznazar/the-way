# Handoff — the return step (the one author, resumed)

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator; no answer here is that person's approval.

## Where you work

- The same worktree and branch (`the task's worktree`, `task/installer-foundation-check-full-path`), at the head `674c93fe` (your fix); base of the cycle `fad52af301db6fd6b831850e9bf69f6a11559a4a`. Your directory for working copies: `.runs/author/`.
- Your report: `.runs/task-cycles/installer-foundation-check-full-path/reports/author-return-report.md` (the file is the input of the cycle's scripts; the rule against a subagent writing a file whose name starts with `report` does not apply to it; if refused, return the report whole as your answer).

## Your stage

Take the return step: read `task-cycle/skill/return_step.md` whole and follow it. It is not a row of `make-change`'s table; your stage is the return step. Compare with the code the entries you wrote or changed (the invariant `installation-agents-md-warnings`, WAY-418's *Verification*), those the task names, those the search of the foundation found and those your own search by the names and words the change's code adds finds (such as `foundation_check.py` as a bare name in other instruction texts of the-way, `installation-agents-md-warnings`, `looks_like_path`, and `ERROR`/`WARN` of the instruction check), and the part map of the touched parts (`installation`, `instruction-files`) and `installation/README.md`. Correct in the same change whatever no longer matches, and commit it. Where nothing needs correcting, commit nothing and say so.

The review of the whole change and the review of its fix returned (PASS at `674c93fe`); one Minor finding of the fix's review stays unfixed by the cycle's rule and goes to the request's list: the invariant's sentence says "no warning" while its test also refuses an error. It is not yours to fix in this step; if your own search finds that the sentence and the test disagree further, name that in your report.

Run no full gate. Report as `return_step.md` gives, with each check's command and exit code, **Unread material** and **Searches not found or unclear**, and the record's *Return step* items (what you compared, decisions, invariants, environment facts, glossary terms, part-map changes, projected entries and rows of *Settlements to record* written, each with its place). Return status, your commits (if any), one line on the checks and the report's path.
