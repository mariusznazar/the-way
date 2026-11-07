# Handoff — the one author of the change

You are the one author of a change without a plan, in a the-way task cycle (`implement-task`).

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator. Do not
ask the human anything and do not stop for approval. Send a question to the orchestrator by
returning `questions` in your report; it answers from the task, its sources and the foundation. A
choice of how to make what the task and the foundation settle is none for the orchestrator: make it
and name it in your report. An open design choice (one the task and foundation leave open, with
more than one way and a different behaviour for the human) is not yours to settle: return
`returned` with a report and no code.

## Where you work

- Worktree (work only here, from its root):
  `.`, branch
  `task/cycle-no-private-names`, base `ad44b84`. Commit on that branch. Do not push. Do not touch
  any other checkout.
- Your method: `task-cycle/change/SKILL.md` in this worktree, variant **"the whole change as the
  one author"**. Read it whole; read a file it names when the step that names it comes.
- Frozen task, read whole: `.runs/task-cycles/cycle-no-private-names/task.md` (the task document
  as accepted). It holds the *Need*, the *To do*, the acceptance criterion, questions 1–5 with
  their answers, *Decisions in play*, *Settlements to record* (rows 1 and 2) and *Out of scope*.
- No spec and no plan exist. The cycle record (`cycle.md`) is the orchestrator's; do not read or
  write it.
- Report: write your full report to
  `.runs/task-cycles/cycle-no-private-names/reports/author-report.md` as your method gives it, and return
  your status, commits, a one-line check result, and the report's path. Your report has the
  sections your method requires, among them **Searches not found or unclear** (`none` is an
  answer) and your own-work check.

## Answers of the orchestrator at start

- Trust boundary: no. Irreversible operation: no.
- Open design choice: none. Route: one author without a plan.
- **Q1 — order of cleaning and the remarks check** (task, *Questions carried to cycle*): the
  orchestrator rules: the remarks check (`remarks_check.py`, WAY-294) keeps running as today on
  the original `.runs/task-cycles/<task-slug>` before the record is copied. The cleaning is then a
  single rewriting applied to every text file of the copy, so an item of a report and the same item
  in the process remarks come out in the same words. After cleaning, both the new script and
  `remarks_check.py` run on the cleaned copy (`docs/task-cycles/<task-slug>`) and each must list
  nothing before the commit is made. Write the rules of the steps so this order and its reason
  are plain; if you find it cannot work as written (for example `remarks_check.py` cannot read a
  copy), return `questions` with what you found instead of changing `remarks_check.py`.

## What the change must do (from the task; the task binds, this list only points)

- The new check script of `task-cycle/`, with its own test file beside it (a directory the gate
  runs is any directory with a git-tracked `test_*.py`; `git add` the new files). The script only
  **lists**, with the place of each hit (file and line), every absolute path (a drive letter,
  a home directory) and every note link in the form `[[...]]` it finds; it rewrites nothing and
  holds no list of private words (question 2, row 2). It reads a directory (the copy of the
  record) and a single file (a request description). Name, call and exit codes are yours to
  choose; follow the conventions of `task-cycle/remarks_check.py` and
  `task-cycle/request_check.py` (exit 0 nothing listed, 1 listed, 2 call error). Take care that the
  pattern does not list a URL or ordinary prose, and that it does list a drive path written with backslashes and with slashes, the
  forms of a home directory on Windows, Linux and macOS, and the POSIX form of a drive some shells
  show (a slash, the drive letter and a slash) — and say in the report which forms you chose and why.
- The rules of the cycle (`task-cycle/skill/SKILL.md` and the files that repeat the
  "process remarks check" step): before every commit that adds the record — its copy for a
  request, the repetition in a correction after review, and the copy of a request blocked for any
  cause — the orchestrator cleans the copy (absolute paths become paths relative to the
  repository; paths and titles of private notes become a description of what they are; the line
  `Project relation:` of the copy of the task document stays unchanged, because the plan-state
  reader ties the record to the plan's task by it), runs the script on the copy and corrects what
  it lists until it lists nothing. Before every publication of a request description — the first
  and each later edit, the one that adds the link to the record included — the same script runs on
  the description file, including the block in the language of the task document. Commit messages
  are not checked (question 3). Find every place that now says "process remarks check" (search
  the repository outside `.runs/` and outside `foundations/decisions.md` for `remarks check` and
  `remarks_check`; the hits already known are in `task-cycle/skill/SKILL.md` lines 74, 315, 425,
  458–493, `correction.md`, `blocked_finding.md`, `reserved_return.md`, `request_template.md`,
  `record_template.md`) and make the new step stand wherever those commits are described, without
  repeating the same text in all of them where one reference serves.
- The record template: its first line asks for "an absolute path" of the task source; the
  template must stop asking for what the check lists (the published copy). Check the other places
  of `record_template.md` and `request_template.md` that ask for an absolute path, and the
  request template's own *Checks* rule for what the description names, so the check's command and
  exit code stand in the description as other checks do.
- Foundation entries (the foundation step): rows 1 and 2 of *Settlements to record* are decisions.
  Read `task-cycle/skill/foundation_step.md` whole and follow it; write them through
  `elements/decisions/SKILL.md` (the-way's `record-decision`), choosing one decision or two as
  that skill's rules give, with `Based on`/`Verification`/`Rejected` as the template requires. The
  *Not chosen* options of questions 1–3 are the *Rejected* material. Mind WAY-294 and WAY-295
  (their listing procedure runs before the same commits), WAY-27 and invariant
  `outbound-link-reach`, WAY-153 and invariant `project-plan-state-evidence`, WAY-288 and
  WAY-286/290/291 (the description and its check). Do not invent a new invariant; the task asks
  for none. Run `elements/common/foundation_check.py` on the foundation as your method and
  `foundation_step.md` give.
- Out of scope: what already stands in the published history. A rewriting mode in the script, a list
  of private words, a check of commit messages: none of them.

## What you read (selected by the orchestrator, WAY-150, WAY-213)

Foundation entries, each whole (from its heading to the next heading): decisions WAY-27, WAY-30,
WAY-36, WAY-147, WAY-148, WAY-153, WAY-162, WAY-163, WAY-286, WAY-288, WAY-290, WAY-291,
WAY-294, WAY-295, WAY-296, WAY-289 (found by heading in `foundations/decisions.md`; search for
`### WAY-<n> `); invariants `outbound-link-reach`, `project-plan-state-evidence`,
`return-step-record` (in `foundations/invariants.md`); the part map entries of `task-cycle`,
`decisions`, `agent-instructions` and `gate` (`foundations/part_map.md`, short, read it whole).
Every file you change, whole, before you change it. For the shape of the new script and test,
`task-cycle/remarks_check.py` and `task-cycle/test_remarks_check.py`. The product has no coding or
testing guidelines of its own (the task, question 4); follow the existing scripts of
`task-cycle/`.

Reach for anything else selectively and list each reach beyond this handoff in your report.

## Working rules of this repository

- Read `agent-instructions/README.md`. Commit messages in English, in the form of the recent
  commits (`git log --oneline -15`). Add files by path: `git add <path> <path>`, never `git add
  -A` or `git add .`.
- Console output of a script on this machine is ANSI, not UTF-8: keep stdout of your script and
  tests ASCII. Write paths in Python literals with `/`; write a backslash only in a raw string or
  from `chr(92)`, and in the tests check that the backslash patterns really match what you
  intend (a `\r`, `\t`, `\N`, `\U` in a plain literal silently becomes another character or breaks).
- Run the focused checks yourself and record the command and exit code of each in your report:
  `python -B gate/run_tests.py task-cycle`, `python -B elements/common/foundation_check.py` (the
  command as `foundation_step.md` gives), and, if the change touches an entry point or the
  description of a skill, `python -B agent-instructions/skill_entry_points.py --write` and the
  tests of `agent-instructions`. Do **not** run the full gate (`python -B gate/run_tests.py`
  without a directory); the orchestrator runs it.
- Run the new script on your own change's text files too, where useful — but the cycle's own
  record is the orchestrator's business, not yours.
- Keep all text you add to files of this repository in English, in plain language; the script's
  messages, its docstrings and comments are English too.
- Your own-work check: before you report, check your change against each item of the task (each
  *To do*, the acceptance criterion, each settlement row, each carried question) and name in your
  report the weakest point of the change and the check you made on it.
