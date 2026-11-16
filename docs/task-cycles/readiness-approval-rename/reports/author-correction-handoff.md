# Handoff to the author — correction 1, for the human's remarks

You are the one author, resumed. Same worktree `the task's worktree (the repository's root)`,
branch `task/readiness-approval-rename`; head `4d7ad796` (the code is that of `cef14df7` merged with the
target branch at `50bc1993`; the record's copy was added and removed above it). The delegation and your
earlier rules stand. Your variant: **a correction for the human's remarks**
(`task-cycle/change/SKILL.md`, row "a correction for the human's remarks"; the remarks bind, there is no
findings file). Your directory for working copies: `.runs/author-correction/` (removed before you
return; say where each stood). Do not run the full gate; run the affected focused checks and
`python -B elements/common/foundation_check.py`, with command and exit code.

**The remarks (word for word, in the file):** `.runs/task-cycles/readiness-approval-rename/reports/correction-1-remarks.md`.
Read it whole. Item 1 (let through) needs no work. **Item 2 binds:** fix, in this request, the use of
"entry" / "entries" for an item of a list in the description of a cycle's record, so that "entry" in
the-way's English text means only an entry of the foundation (the task's *To do* 10: "Po zmianach 9 i
10 „entry” w the way znaczy tylko wpis fundamentu"; frozen task: `.runs/task-cycles/readiness-approval-rename/task.md`).
The human's words: use the word the change already gives a line of a table where it fits (for a line of
the record's table, "row"); keep it consistent with the glossary; add the word to the glossary if it is
new there; if one of the places means something no plain word covers, say so in the report (the
description will say it) instead of choosing silently.

**Where the places are (the reviewer's list, at the old head; line numbers have moved since the merge
of the target branch, so search, do not trust numbers):** `task-cycle/record_template.md` (about 8 places:
the lines on *Discarded attempt* "an entry of its own", "one entry for each fix round", "entries" of
*Review rounds*, "entries under it" of the process remarks, the paragraph on the record's forms) and
`task-cycle/skill/SKILL.md` (about 5 places: "an entry of its own where the cycle discarded an attempt
before", "that attempt rewritten as an entry too", the process remarks "as an entry in the form", "each
item listed" lines). Search by WAY-97 the English text of every file git tracks for "entry"/"entries" in
that meaning — the record's lists: events, discarded attempts, review rounds, process remarks, the
questions table, the lists of a request's description — also in `task-cycle/skill/correction.md`,
`task-cycle/skill/request_template.md`, `task-cycle/skill/blocked_finding.md`,
`task-cycle/skill/reserved_return.md`, `task-cycle/skill/foundation_step.md`, `task-cycle/remarks_check.py`
(docstring and messages — but the code reads the form the template gives: change a script's text only
where it names the record's items, and keep every pattern it matches on; where a script *matches* the
word "entry" or a text copied from the template, change the match and its tests together or leave it and
say so), `task-cycle/test_*.py` that copy a line of the template, decisions of the log that use the word
for a record's item (a decision's sentence changes only in that word, and the meaning stays), and any
other file the search finds. The word in the record's items stays what it names today; the words you
choose are "row" for a line of a table, "item" for an item of a list, "line" or "report" where one of
these names the thing exactly. Do not widen the task: other non-foundation meanings of "entry" (for
example a list of the worktrees `git` prints in `task-cycle/remove_merged_worktrees.py`, or of the
transcripts in `task-cycle/cycle_stages.py`) are not the record's lists — name each kind you leave in the
report with the file and the reason, so that the orchestrator can tell the human; change none of them.
Names in code stay (`entry_path`, `REGISTER_ENTRY` and the like).

**Glossary.** Look at `foundations/glossary.md` and `elements/glossary/template.md` /
`elements/glossary/skill/SKILL.md`: whether "row" or "item" is a word the glossary holds, and whether WAY-95
gives it an entry (a word the product uses more narrowly than the field takes an entry only where a
reader who takes the field's meaning would read a sentence wrongly). The human's remark says "add the word
to the glossary if it is new there": follow it where the word is new and the rule allows; where WAY-95
says no entry, say so in the report with the reason and add none. Write an entry only by following
`elements/glossary/skill/SKILL.md`, as `task-cycle/skill/foundation_step.md` gives.

**Foundation to read.** The decisions you edit or that bear on the record's lists and on the glossary
rule: WAY-95, WAY-97, WAY-99 (each whole), and every decision whose sentence you change, whole;
`guidelines/coding.md` whole before you change a script; `guidelines/testing.md` whole before you change a
test (a changed expected value follows "Changing an existing test"). The trust boundary is untouched
unless the search leads you to one of the three files of the part map named earlier; if so, do not change
what it accepts.

**Report** to `.runs/task-cycles/readiness-approval-rename/reports/author-correction-report.md`: each
place changed (file, the word before and after, why this word), each kind of use of "entry" left and
why, the glossary decision, checks with command and exit code, own-work check (WAY-164: the requirement
most likely missed, and what you checked), **Unread material**, **Searches not found or unclear**
(`none` if nothing), working copies. Commit by path; message in English. Return only status, commits, a
one-line check result and the report path.

**Working copies (word for word from `task-cycle/skill/SKILL.md`).** An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
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
