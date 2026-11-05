# Handoff — the return step

You are the one author of this change, resumed for the return step (step 11 of `implement-task`).
Read `task-cycle/skill/return_step.md` whole and follow it; it sends you to
`task-cycle/skill/foundation_step.md` for how an entry is written — read that again where you write
or correct an entry, with the mark `the cycle's` and the two sentences of meaning it asks for. The
same worktree, branch and rules as your first handoff (`reports/author-handoff.md`): commit on
`task/pr-description-schema`, never push, nothing under `.runs/` committed, no full gate run, no
commit while one of your test runs is going. No other agent works in the worktree now.

The change under the return step: `f45ca40..4327974`, reviewed `PASS 4327974`
(`reports/whole-review.md`, then `reports/whole-review-2.md` for the fix). The entries it writes or
changes: WAY-286 to WAY-292 written; WAY-114, WAY-134, WAY-10 changed in place; WAY-161, WAY-33,
WAY-126, WAY-97 corrected by the search of the whole foundation. The task names WAY-03, WAY-10,
WAY-49, WAY-51, WAY-114, WAY-134, WAY-140, WAY-161, WAY-162, WAY-219, WAY-227, WAY-256, WAY-261 and
WAY-269 in its *Decisions in play*. The touched parts: `task-cycle`, `agent-instructions`,
`decisions`, `elements-common`, `glossary`; compare their part-map entries with the files, the new
`task-cycle/request_check.py` and `task-cycle/skill/request_template.md` included.

Unfixed findings of the reviews stand as they are; they are no foundation entries and none is
yours to fix: M-1 to M-4 in `reports/whole-review.md` and M-5 in `reports/whole-review-2.md`. Where
your comparison finds an entry that no longer matches the code, correct it, whatever a finding says.

Write your report to `docs/task-cycles/pr-description-schema/reports/return-step.md`: what you
compared, each mismatch and its correction by commit, each entry written or corrected with its
identifier, its mark and its meaning sentence in English and in Polish, the lines of the record's
*Return step* filled (decisions, invariants, environment facts, glossary terms, part-map changes,
projected entries, rows written with their identifiers), your checks with command and exit code,
reaches, and **Searches not found or unclear**, or `none`. Return your status, your commits (or
none), a one-line check result and the report's path.
