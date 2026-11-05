# Handoff — the return step

You are the one author, resumed for the return step (step 11 of `implement-task`). The person who
requested this cycle has delegated intermediate choices to the orchestrator; nothing here is the
human's approval.

- Worktree: `C:\Storage\repos\the-way\.runs\worktrees\stage-remarks-check`, branch
  `task/stage-remarks-check`, head `5e90498`.
- Read whole: `task-cycle/skill/return_step.md` (it names the foundation step, which you already
  read; read `task-cycle/skill/foundation_step.md` again only for an entry you write now), and the
  skill of an element when you write an entry of that element.
- The whole-change review passed (`PASS 5e90498`): its report is
  `.runs/task-cycles/stage-remarks-check/reports/02-whole-review-report.md`. It has no blocking
  findings; its three Minor findings (M1–M3) are not fixed in this cycle and are not yours to fix.
  They go to the request's lists; do not change the script, the process text or the decisions for
  them.
- Report path: `.runs/task-cycles/stage-remarks-check/reports/03-return-step-report.md`.
- Do not run the product's gate. Run `python -B elements/common/foundation_check.py` and
  `python -B gate/run_tests.py task-cycle` if you commit anything.

Compare, with the code, the entries the change writes (WAY-294 to WAY-296), those the task names
(WAY-260, WAY-148, WAY-38, WAY-89, WAY-290, WAY-291) and those the search of the foundation found,
and the part-map entries of `task-cycle` and `decisions`; correct in the same change whatever no
longer matches. Apply "where the task or its spec explicitly excludes an entry": the task's
*Out of scope* excludes changes to `cycle_remarks_digest.py` and `/ai-review-cycles`. Write an
invariant only for a rule the task, a decision or the human sets; the task sets none. Commit any
change on the task branch.

The report holds, in the fields of the *Return step* section of `task-cycle/record_template.md`
(read that section): foundation compared with code; decisions, invariants, environment facts,
glossary terms and part-map changes written or changed, each by identifier or `none`; projected
entries; rows of *Settlements to record* written. It also states the own-work check (WAY-164)
where you commit code or text, each check with command and exit code, each reach beyond this
handoff, and **Searches not found or unclear**, each item or `none`. Return status, commits, a
one-line check result and the report path.
