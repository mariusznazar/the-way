# Handoff — the one author of the change

You are the one author of the change of task `installer-preview-ignores-line-endings`, as
`the-way-author`. The person who requested this cycle delegated the intermediate choices to the
orchestrator; nothing here is that person's approval.

## Where you work

- Worktree (work from its root): `the task's worktree`
  on branch `task/installer-preview-ignores-line-endings`, base `9cc26f3eb5121c19be28e647170019982d2b08c7`.
- The directory for your working copies: `.runs/author/` of the worktree. Nothing of yours goes in
  the system's temporary directory, in a session's scratch directory or in the main checkout.
- Your report: `.runs/task-cycles/installer-preview-ignores-line-endings/reports/author-report.md`.

## Working copies (word for word from the cycle's skill)

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

## Method

- Method of your stage: `task-cycle/change/SKILL.md` in this worktree (`make-change`). Variant:
  **the whole change as the one author**. Read that `SKILL.md` whole, and a file it names, one beside
  it included, only when the step or variant that names the file comes.
- `cycle.md` and the other files of the cycle's record directory (other agents' handoffs, reports
  and findings) are not yours to read unless this handoff names them. It names none.
- Run no full gate (`python -B gate/run_tests.py` with no directory): its run is the orchestrator's
  or CI's. Run the tests of one directory while you work: `python -B gate/run_tests.py installation`.
  Where the method asks for your own-work check, run it as the method gives.
- Commit by path (`git add <file> …`), never `git add -A` / `.` / `commit -a`. Commit messages in
  English. Do not push.

## The task

The frozen task is `.runs/task-cycles/installer-preview-ignores-line-endings/task.md` (read it whole).
Its single *To do* item:

> 1. Plik, który instalator zapisuje w produkcie, a który różni się od nowej treści tylko końcówkami
> linii (CRLF zamiast LF), dostaje w podglądzie `KEEP`, bez różnicy pod spodem, i instalator go nie
> przepisuje; gdy żaden plik nie zmienia treści i wersja the way się nie przesuwa, instalator
> odpowiada „Already installed; no changes”. Miejsce zmiany: funkcja `file_action` w
> `installation/install.py`, zdanie `path.read_bytes() == content.encode("utf-8")` (około linii 515
> in this worktree).

Out of scope (task): a file with a real change in content is still written with LF endings, as
today; the git setting on the author's computer stays as it is.

## Answers of step 4

- Trust boundary: **yes** — `installation/install.py` is the boundary the part map names for part
  `installation`. The change touches it, so the review checks crafted input at that boundary: here,
  the bytes of a file in the product that the installer reads before deciding to keep or replace it
  (CRLF, lone CR, mixed endings, a file that is not UTF-8, an empty file, a file whose name is a
  link). Keep the existing behaviour for all of it except the one the task changes.
- Irreversible operation: **no**.
- Open design choice: **none**. Reserved choice: **none**.
- Route: one author without a plan, class `cheaper`. No spec, no plan.
- Findings of the orchestrator: `run()` in `installation/install.py` is already over the 80-line
  threshold of WAY-385; the task's place of change is the 6-line `file_action`, which is not over it,
  so the change adds nothing to `run()`. If you find that the change must touch `run()`, return it
  as a question rather than adding lines to it.
- The task's *Decisions in play* names WAY-34 and WAY-328. WAY-328 is withdrawn (the coding and the
  testing guidelines of the-way's own are written: WAY-379, WAY-392); the guidelines below apply.

## What you read (selected by the orchestrator)

- Foundation (index of the selection written by `decision_index.py`, `--part installation`,
  `--part installation-command`, `--decision WAY-34 --decision WAY-379 --decision WAY-392`, at
  `.runs/orchestrator/index.md` of the worktree — read it; open whole only what the change touches
  or what the index leaves open): decisions WAY-34, WAY-379, WAY-385, WAY-392, WAY-393, WAY-394.
- Part map: entries `installation` and `installation-command` (`foundations/part_map.md`).
- Invariants: `installation-paths-through-links`, `installation-claude-guidance`,
  `repository-changer-acts-only-when-told` (`foundations/invariants.md`), each whole.
- Guidelines, each whole: `guidelines/coding.md`, `guidelines/coding-repository-changer.md`,
  `guidelines/testing.md`.
- Code: `installation/install.py` (the function `file_action`, and where `run()` and `plan()` use its
  result) and `installation/test_install.py` (the test
  `test_preview_apply_rerun_and_preserve_foundation`, the tests of AGENTS.md blocks that already
  compare after normalising line endings, and the fixture helpers).
- Evidence for the cause, from the task's *Context*: `agents_change` already compares the block in
  `AGENTS.md` after `text.replace("\r\n", "\n")`; git stores a CRLF file in the repository as LF.

## What you do

1. Make the change the task's item gives, in `file_action`. Decide, and name in your report, how a
   line ending is normalised (only `\r\n`, as `agents_change` does, is the expectation; say what
   happens to a lone `\r` and why that is right).
2. Add the permanent test(s) the testing guidelines call for, at the level they give, naming for each
   the break it catches: at least (a) a file of the installer's own, written in the product with CRLF
   endings and the same content, is shown as `KEEP` with no diff under it, is not rewritten (its bytes
   stay CRLF) and, where nothing else changes, the installer answers "Already installed; no changes";
   (b) a CRLF file whose content really differs is `REPLACE` with a diff that shows only the real
   change, and when applied is written with LF as today. Check that the test of (a) fails on the
   code before your change and passes after it (record both runs in your report).
3. Do the foundation step as `task-cycle/skill/foundation_step.md` gives (the task carries no
   *Settlements to record* and no projected entry; search the foundation once for entries the change
   touches — for example any that says the installer compares bytes — and correct what no longer
   matches, as the method gives).
4. Run your own-work check and the focused tests of `installation`, and `ruff` as the coding
   guidelines require. Report as the method gives, with the command and exit code of every check, your
   **Unread material** and **Searches not found or unclear** (each `none` where there is none) and
   the line on your working copies.
5. Return: status, commits, a one-line check result, and the report's path.
