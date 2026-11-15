# Handoff — reviewer of slice 18 (its rework after the real run of the count), task `scripts-after-foundation-review`

You review one range of commits in a task cycle of the-way (`implement-task`) as an agent that did
not make the change. The person who requested the cycle has delegated intermediate choices to the
orchestrator; nothing here is the human's approval. Ask no human; a question goes to the orchestrator
as section 4 of the method gives. You are read-only: you change no file of the worktree.

## What and where

- Reviewed: slice 18 (its rework after the real run of the count). Worktree (work from its root): `the root of the task's worktree`, branch `task/scripts-after-foundation-review`. Range: **base `e8bef720a34924cb4b32bd0f136f51c006e2b504` to head `881c1ea6fd8e471545a01481bee8da954ba6dcf1`** (`git diff e8bef720a34924cb4b32bd0f136f51c006e2b504..881c1ea6fd8e471545a01481bee8da954ba6dcf1` and `git log e8bef720a34924cb4b32bd0f136f51c006e2b504..881c1ea6fd8e471545a01481bee8da954ba6dcf1`, computed by you; confirm that `git rev-parse HEAD` is the head). The range is one commit made after the real run of the count on the user's register: read reports/executor-18-rework-handoff.md first (it says why: the list Unknown values was 1605 lines on real data against 501 on the task's base, and the task's aim is to cut that flood, task To do 10 and Questions to settle 5). Judge the code change against To do 10, Questions to settle 5 and Settlements row 6, and against the earlier slice 9's review finding (its text is in reports/slice-9-findings.md: a claim 'the full list stays in the register' must be true for what it names): is every sentence about where a full list stands now true? You may re-run the count only through a copy of the locations file in .runs/review-18/, read only, with no path of the disk, user name or content in your report.
- Method, read whole: `task-cycle/review/SKILL.md` (`review-change`); variant: the review of a slice (read nothing of `whole_change.md` or `fix.md`). A file the method names only when its step or variant comes. You have no skill tool.
- Report path: `.runs/task-cycles/scripts-after-foundation-review/reports/review-18-report.md`; its first line is `PASS 881c1ea6fd8e471545a01481bee8da954ba6dcf1` or `FAIL 881c1ea6fd8e471545a01481bee8da954ba6dcf1` (the full head), or `questions`. Graded findings and the checks you ran with command and exit code, **Unread material**, **Searches not found or unclear** and the working copies line as the method gives.
- Frozen task, whole: `.runs/task-cycles/scripts-after-foundation-review/task.md`; judge the change against the passages of the task, not the plan alone. Reviewed spec: `.runs/task-cycles/scripts-after-foundation-review/spec.md` (only the passages below). Plan: `.runs/task-cycles/scripts-after-foundation-review/plan.md` (only what is copied below).
- Answers of step 4: trust boundary **yes** — check crafted input at the boundary the slice touches: a transcript, a register, a locations file, a copy of a record from git history, a price list, a session record: a crash with a stack trace, a write outside the places the script writes, a command run, text of the input reaching a result unescaped. Irreversible operation: none (a change that only prepares one is checked as such; this one holds none).
- The executors' work is checked by the commands of the slice's *Checks* and your own; you run **no run of the whole gate** (WAY-160). Run focused tests you need, from `.runs/review-18/` for working copies only.
- Directory for your working copies: `.runs/review-18/`.
- WAY-03: a changed invariant test, or a test holding a sentence of a decision by a line `decision:`, is named in your report.

## The slice and the reports to verify

### Slice 18 — The audit count run on the real register of problems, and corrected

- **Goal:** `process-audit/audit_count.py` is run on the user's real register of problems through a **copy** of the user's locations file, given by `--locations`, whose `audit_results` entry under `the-way` points to a directory in the executor's own directory under `.runs/` of this worktree; the original locations file, the register and the repositories are only read, and nothing is written outside `.runs/`. Where the count refuses a result directory that lies inside a checkout it reads, the executor reports that and does not choose another place; the orchestrator then decides. The executor reports **counts and facts only**: the exit code, the number of lines of *Unknown values* (it was about 830 on the template, which Slice 9 reduces) and of lines for each kind, whether the measures of the Codex cycle and of the nested Claude Code helper are present in *Mechanism measures*, and the number of `Error:` lines; **no absolute path of the user's disk, no user name, no name of a repository or product and no content of the register or of a cycle**. A result that is wrong or empty where the count should give it is a defect of this cycle: the executor fixes it in `process-audit/audit_count.py` with the test first in `process-audit/test_audit_count.py` and reports what it fixed; where nothing is wrong, it changes nothing. Where the locations file or the register cannot be opened, the executor reports it and does not guess. The copy of the locations file, the result and the executor's directory are removed before it returns.
- **Change:** `process-audit/audit_count.py` · `process-audit/test_audit_count.py`
- **Read:** `.runs/task-cycles/scripts-after-foundation-review/task.md:37-38` To do 10 and 11 · `.runs/task-cycles/scripts-after-foundation-review/task.md:75-84` Questions to settle 5 and 6 · `foundations/decisions.md:7309-7341` WAY-330 · `foundations/decisions.md:7183-7253` WAY-320 · `foundations/invariants.md:116-145` script-language, script-imports, script-subprocesses · `foundations/part_map.md:124-134` process-audit
- **Model:** same — it judges real data and may change a trust-boundary script on what it sees
- **Risk:** trust boundary — `process-audit/audit_count.py`
- **Checks:** the run above, with its counts in the report; where a defect is fixed, the new test red on the base and `python -B -m unittest discover -s process-audit -p "test_audit_count.py"` · `python -B -m unittest discover -s process-audit -p "test_audit_series_scripts.py"`
- **Depends on:** Slice 9 · Slice 17


Reports of the agents of the range (claims to verify, not evidence): `.runs/task-cycles/scripts-after-foundation-review/reports/executor-18-report.md`, `.runs/task-cycles/scripts-after-foundation-review/reports/executor-18-rework-report.md`, `.runs/task-cycles/scripts-after-foundation-review/reports/executor-18-rework-handoff.md`

## Foundation entries to read (named by the orchestrator, WAY-150)

- `foundations/decisions.md:7357-7390` WAY-330
- `foundations/decisions.md:7231-7302` WAY-320
- `foundations/invariants.md:116-125` script-language
- `foundations/invariants.md:126-135` script-imports
- `foundations/invariants.md:136-145` script-subprocesses
- `foundations/part_map.md:124-135` process-audit

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

Note of the orchestrator's mechanical check (information, not a finding): the commit also changes `process-audit/SKILL.md` (6 lines), a file outside the slice's *Change* (the prose that says what *Unknown values* is); judge whether it follows the code.
