# Handoff — the one author, `make-change`

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator; no answer in this handoff is that person's approval. The cycle has one ordinary human contact, the request; do not stop for design questions that the sources below settle.

## Where you work

- The worktree: `the task's worktree` (branch `task/installer-foundation-check-full-path`, base `fad52af301db6fd6b831850e9bf69f6a11559a4a`, target branch `foundations`). Work from its root; the-way is this worktree (no product, no `.the-way` pin).
- Your directory for working copies: `.runs/author/` (directly under `.runs/` of the worktree).
- Your report: `.runs/task-cycles/installer-foundation-check-full-path/reports/author-report.md`. The report file is the input of the cycle's scripts (`task-cycle/remarks_check.py` reads it); the rule that a subagent may not write a file whose name starts with `report` does not apply to it. If the write is refused all the same, return the report whole as your answer.
- `cycle.md` and the other files of the cycle's record directory — other agents' handoffs, reports and findings — are not yours to read unless this handoff names them.

## Your stage and variant

You make the whole change as the one author, with no plan. Read `task-cycle/change/SKILL.md` whole and follow it: the variant is "the whole change as the one author". Read a file it names, one beside that `SKILL.md` included, only when the step or variant that names the file comes.

You also do the foundation step with your code, as `task-cycle/skill/foundation_step.md` gives: read it whole. The task carries one entry to write, the invariant of *Settlements to record* row 2; the `SKILL.md` of the element is `elements/invariants/skill/SKILL.md` (read it whole when you write the entry, with the files it names at the step that names them). You return before review; the review, any fix and the return step come after your report.

Do not run the product's full gate (`python -B gate/run_tests.py` with no argument): its run is the orchestrator's or CI's. Run the focused checks of your own work: the tests of the directories you touch (`python -B gate/run_tests.py installation`, `python -B gate/run_tests.py instruction-files` if you touch nothing there only as a control), `python -B elements/common/foundation_check.py` (without `--skip-test-citations` once your test exists), and the linter and formatter as the-way's guidelines give.

## The task

The frozen task: `.runs/task-cycles/installer-foundation-check-full-path/task.md` (the document as accepted; read it whole — you are the one author, so you read the whole frozen task).

Answers of the start (the orchestrator's, from the task):

- Trust boundary: **yes** — the part map names `installation/install.py` as the trust boundary of the part `installation`, and the change edits a literal of the block that file writes into a product's `AGENTS.md`. Add no new read of outside data; build the product of your test only in your own directory under `.runs/author/` and write nothing outside it.
- Irreversible operation: **no**.
- Open design choice: **none**. The task's *Settlements to record* row 1 (the sentence of the block carries the full path `{SUBMODULE}/elements/common/foundation_check.py`, in `product_guidance` in `installation/install.py`, with the test that pins the text of the block, `installation/test_install.py`) and row 2 (the invariant, Method `test`, with a test carrying the line `# invariant: <identifier>`, in the pattern of `installation-claude-guidance`) bind. Question 1's answer binds: the sentence about `.runs/` is not changed; the test builds the product by a full installation (`installation/install.py <product> --apply --url <the-way>` as the existing tests of `installation/test_install.py` do for a full installation — find how they make the remote and the product), before any skill ran (no `.runs/` directory), and runs the check of instruction files (`instruction-files/check_instructions.py`) on the product's main `AGENTS.md`, expecting zero warnings (the `info` lines are no warnings). A choice of how to make this that the task and the foundation settle is none; make it and name it in your report. If you meet an open design choice that the sources do not settle, return `returned` with a report and no code, as the method gives.
- In the task document's *Context*, the lines of `installation/install.py` and `instruction-files/check_instructions.py` are at `fad52af3`, which is your base: re-read them in the worktree, the line numbers there are approximate.

## What you read

Name the foundation entries by identifier; read each whole (an entry runs to the next heading). The orchestrator's index of its selection is not yours to read.

- Decisions in `foundations/decisions.md`: WAY-418 (the task's *Decisions in play*), WAY-141, WAY-129, WAY-321, WAY-392, WAY-393, WAY-394, WAY-395, WAY-401, WAY-38, WAY-89, WAY-344.
- Invariants in `foundations/invariants.md`: `installation-claude-guidance` (the pattern for row 2, with the tests that cite it in `installation/test_install.py`), `installation-paths-through-links`.
- The part map's entries for the parts `installation` and `instruction-files`, and the entries `installation-command` and `foundation-check-command` of `foundations/part_map.md`, in the part map's file as the ranges to its headings give.
- Glossary terms: whichever you use, from `foundations/glossary.md`, by search.
- The guidelines of the parts you touch (`installation`: `install.py` is a script of the kind `repository-changer`): `guidelines/coding.md` whole and `guidelines/testing.md` whole; of the kind files read the index in `coding.md` and open a kind file only where its row's *When to read* matches your work, and name which you read and why.
- The files you change, whole, before you change them: `installation/install.py` (the function `product_guidance` and what it calls), `installation/test_install.py` (the constants of the expected block and the tests that build a product by a full installation), `foundations/invariants.md` by the ranges of the section you add to and the entry you copy the pattern of. Read `instruction-files/check_instructions.py` where it bears on your test (how it decides `dead-path`, `looks_like_path`, `dead_path_note`), and the entry point of the check — how it is called and what it prints — not the whole file.
- `installation/README.md` where it says what the installer writes or what a test of it holds.

Where something the dispatch does not name matters to your work, reach for it selectively and name the reach in your report.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never in the system's temporary directory, in the scratch directory of a session or in the main checkout of the repository. In a product, a worktree or checkout made to run checks gets its `.the-way` populated, and the dependencies those checks need installed as the product's own rules give, before they run; otherwise they fail for that reason. The screenshot that a screenshot tool, such as the Playwright server, saves by itself under its session's directory is moved into the agent's directory and the original removed, except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md` says, to the place the product's foundation settles for screenshots, and into the agent's directory only where no such place is settled. The files that a product's own tools and tests make by themselves are no working copy of the agent and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside its report what the report needs, the input and command of a probe that shows a finding among them, and states in the report where each copy stood and that it was removed. Where a removal fails, the agent finishes all the same and names in the report the remainder, with its full path and the reason it stayed. It removes a copy, as any directory, by its path written out in full in the command, never through a shell variable: an empty variable turns the removal on the directory the shell stands in.

## What to return

Your report at the path above, as `task-cycle/change/SKILL.md` gives it, with its **Unread material** (what this handoff names that stayed unread or was read in part, or `none`) and **Searches not found or unclear** (each thing looked for and not found or unclear, or `none`), your own-work check with its command and exit code, and each check with its command and exit code. Commit your work on the branch by path (`git add <path> …`, never `git add -A`); commit messages in English. Return your status, your commits, a one-line check result naming what failed or did not run, and the report's path. Your questions and concerns, each reach beyond this handoff, go in the report.
