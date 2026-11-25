# Handoff — the return step, `make-change`

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator; no answer in this handoff is that person's approval. The cycle has one ordinary human contact, the request.

## Where you work

- The same worktree and branch: `the task's worktree` (branch `task/ai-review-fixes-from-24-11`). The head is `2dca6873` (your fix; the whole-change review `PASS 225bf1c5`, the fix review `PASS 2dca6873`). Your directory for working copies: `.runs/author/`.
- Your report: `.runs/task-cycles/ai-review-fixes-from-24-11/reports/author-return-report.md`, with **Unread material**, **Searches not found or unclear**, and each check with command and exit code. The report file is the input of the cycle's scripts.

## Your stage

The return step of the cycle, not a variant of `make-change`'s table: read `task-cycle/skill/return_step.md` whole and follow it. It compares the entries the change writes or changes (WAY-12, WAY-30, WAY-48, WAY-235, WAY-368 and the entries of the files you edited), those the task names (*Decisions in play*, WAY-18, WAY-114), those your search of the foundation found and those your own search by the names and words the change's code adds (`check_linked`, `entry_texts`, the new message of the check) finds, and the part map of the touched parts, with the code, and corrects in the same change whatever no longer matches. Take the two reviews' reports into account: `.runs/task-cycles/ai-review-fixes-from-24-11/reports/review-whole-report.md` and `reports/review-fix-1-report.md` are yours to read for this step (the reviewer judged the root `README.md`, the two templates and the pair of examples you added to WAY-30 within scope; the pair of examples is to be carried to the request word for word, which is the orchestrator's). A pair of examples of a decision the change writes that a test holds part of: remove that part from the pair, as the file says (WAY-12's pair was not extended; check that WAY-30's pair holds nothing a test holds).

Name in the report, in the record's *Return step* form (`task-cycle/record_template.md`, section *Return step*): foundation compared with code, decisions written or changed, invariants written or changed, environment facts, glossary terms, part-map changes, projected entries, and the rows of *Settlements to record* written, with where each went. Do not run the full gate. Commit any correction by path, English message; where you find nothing to correct, commit nothing and say so.

## Working copies

Only in `.runs/author/`; remove before you return by the full path, and say so in the report.
