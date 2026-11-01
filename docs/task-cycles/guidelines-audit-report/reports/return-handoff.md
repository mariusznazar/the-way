# Handoff — the return step

The review of the whole change returned `PASS 0ee0cd9`
(`.runs/task-cycles/guidelines-audit-report/reports/whole-review.md`), and the gate on `0ee0cd9`
has finished. Take the return step, step 11 of the cycle, as the author of this change, in the
worktree `C:/Storage/repos/the-way/.runs/worktrees/guidelines-audit-report`.

Read `task-cycle/skill/return_step.md` whole and follow it; it writes as
`task-cycle/skill/foundation_step.md` gives, which you already read. Compare with the files the
entries the change writes or changes (WAY-280 to WAY-285, WAY-187, WAY-201, WAY-250), those the task
names and those your search of the foundation found, and the part map of `product-guidelines`,
`project-level` and `decisions`, and correct in the same change whatever no longer matches.

The review's Minor findings are not fixed by this cycle: they go to the request with the reviewer's
words. Do not act on one as a finding. Where your own comparison shows an entry and a file disagree,
that is the return step's duty whatever a finding says; say so in your report, with the comparison.
Name in the report the outcome for the part map's sentence on `product-guidelines`, which the review
of the whole change raises under *Searches not found or unclear*, and for "weight" in WAY-13, which
your report raised.

Commit by path, in English, and leave a clean tree; no commit at all is a sound result. Do not push.
No agent else commits or runs tests in this worktree while you work. After your last commit, run
`python -B elements/common/foundation_check.py .`, and any focused directory your change bears on,
with no commit landing during a run, and report each with its command and exit code. Do not run the
full gate.

Write `.runs/task-cycles/guidelines-audit-report/reports/return-step.md`, with the *Return step* items
of the cycle's record: foundation compared with code; decisions, invariants, environment facts,
glossary terms and part-map changes written or changed; rows written, by row number and identifier;
each entry's sentence of meaning in Polish where the step changes its meaning; and **Searches not
found or unclear**. Return only your status, your commits, a one-line check result and the report's
path.
