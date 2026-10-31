# Return-step handoff — maintain-coding-guidelines in the WAY-256 shape

Same worktree, branch, cycle directory (`<cycle>`) and rules of commits and scripts as your first
handoff, `<cycle>/reports/author-handoff.md`. Head `088717a`, reviewed, `PASS`. Questions come back to
the orchestrator; never ask the human. Do not push.

## Stage

You take the return step of the cycle: read `task-cycle/skill/return_step.md` whole, and
`task-cycle/skill/foundation_step.md` with it, since the return step writes as the foundation step
writes. Read the skill of an element only where you write an entry of that element.

Compare with the files at the head: WAY-216 and WAY-266 as they now stand; the decisions of the
task's *Decisions in play*, each read whole in `foundations/decisions.md` for this comparison, those
you did not read whole so far included; the entries your search of the foundation found; and the part
map's entry `product-guidelines`, whose `product-guidelines/**` must still cover the ten new files.
Correct in the same change whatever no longer matches. Say which entries you compared and what each
comparison showed.

A correction of an entry's meaning beyond what the task carries returns as a question, not as an
edit. The Minor findings of the reviews are not foundation entries and are not yours to fix.

Keep the task's limits: no new entry is expected, and `description`, Python and the entry points stay
unchanged. Where you change a counted file, regenerate `<cycle>/reports/word-counts.md` and run
`verify_counts.py` after the last change.

## Report

Full report: `<cycle>/reports/return.md`, filling each line of *Return step* in
`task-cycle/record_template.md`, with each check's command and exit code, your commits or the
statement that there are none, and **Searches not found or unclear**. Return: your status, your
commits, a one-line check result naming what failed or did not run, and the report's path.
