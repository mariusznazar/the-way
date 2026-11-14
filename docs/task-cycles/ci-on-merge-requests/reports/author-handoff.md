# Handoff — the one author of the change

You are the one author of the task `ci-on-merge-requests` in the task cycle of the-way. You make the
whole change, its foundation entries included, and return before review.

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator. You ask
no human anything; a question goes to the orchestrator as the status `questions` in your report.
Never label an answer or a choice as the human's approval.

## Where you work

- The worktree: `the worktree of the task`, branch `task/ci-on-merge-requests`,
  base `21ecb627f885de438e2209d7ff5c137b1e1b9d83` (the tip of `origin/foundations`). Work from its
  root. Edit nothing outside it. Commit with explicit paths (`git add <path> ...`, never
  `git add -A` or `git commit -a`), in English; commit messages are not checked.
- This is the-way itself, so the-way you read is the worktree. The method of your stage:
  `task-cycle/change/SKILL.md` — your variant: **the whole change as the one author**. Read it whole,
  and read a file it names only when the step that names it comes.
- The foundation step: `task-cycle/skill/foundation_step.md` — read it whole before you write a
  foundation entry, and the `SKILL.md` of an element, at the path it gives, when you write an entry
  of that element. The return step is not yours now: you are resumed for it later.
- The frozen task, which you read whole: `.runs/task-cycles/ci-on-merge-requests/task.md` (a copy of
  the task document; its *To do* items 1–7, *Acceptance criteria*, the six answers under *Questions
  to settle*, *Decisions in play* and *Settlements to record* — rows 1–6 — are your assignment;
  *Out of scope* binds).
- Your directory for working copies: `.runs/author/`.
- Your report: `.runs/task-cycles/ci-on-merge-requests/reports/author-report.md`, written as the
  method gives it, with **Unread material** and **Searches not found or unclear** (`none` is an
  answer).

## The orchestrator's answers at the start

- Open design choice: none. The six answers of the task settle every choice it leaves; what remains
  (where the description of a CI file for products lies, the wording of the sentences, the steps of
  the workflow) is how to make what is settled. Make it, and name each such choice with the way you
  rejected in your report; the orchestrator enters it in the questions table. If you meet an open
  design choice the task and the foundation do not settle, return `returned`, with no code.
- Reserved choice: none. The place to run is GitHub Actions, which To do 4 and the answer to
  question 2 name.
- Trust boundary: **yes**. The change touches `installation/install.py`, a file the part map names as
  the trust boundary of `installation` (the text the installer writes into a product's `AGENTS.md`),
  and it writes a CI workflow, which takes in the content of a pull request from outside. The
  reviews will check crafted input at it, so you check it yourself too: the workflow's trigger
  (`pull_request`, never `pull_request_target`), the permissions of its token (read only), no secret,
  no text of the pull request (title, branch name, body) in a shell command, and the actions it uses.
- Irreversible operation: no. Setting the check as required in the branch rules of `foundations` is
  an effect outside the repository, made only by the human after the request opens, through the
  *Human actions* item of the task. You prepare it and perform nothing outside the repository: no
  `gh api` call that changes anything, no push. Give the workflow's job a name that stays stable and
  state it in your report, since the branch rule will name it.
- No spec and no plan: one author without a plan.

## What to read, by identifier

The foundation entries, each whole (a decision runs from its `###` heading to the next heading, the
other files from their `##` heading):

- The decisions the task names in *Decisions in play*: WAY-16, WAY-206, WAY-34, WAY-160, WAY-133.
- The invariant `ci-checking-commands` in `foundations/invariants.md`, and the entries these
  decisions and it link to, as far as you need them.
- The decisions whose *Scope* names a part you write in: `installation` — WAY-09, WAY-27, WAY-34,
  WAY-38, WAY-89, WAY-100, WAY-102, WAY-107, WAY-127, WAY-141, WAY-167, WAY-321, WAY-324, WAY-328,
  WAY-344, WAY-368, WAY-370; and `repository` — WAY-09, WAY-55, WAY-89, WAY-100, WAY-102, WAY-328,
  WAY-344. For the parts `task-cycle`, `product-guidelines`, `agent-instructions` and `gate`, whose
  *Scope* lists are long, the file `.runs/task-cycles/ci-on-merge-requests/scopes.txt` gives the
  identifiers by part; read the ones that bear on the passage you change (WAY-206 and WAY-160 are
  yours already; for `task-cycle` start from WAY-148, WAY-160, WAY-243, WAY-286-family decisions about
  the request description and the final gate if the search shows them to bear on it).
- The part map, `foundations/part_map.md`, whole; `foundations/glossary.md`, whole.
- The files you change, each whole before you change it: at least `installation/install.py` (the
  function `product_guidance`) and its tests, `installation/README.md`,
  `product-guidelines/coding/settle.md` and the place of the skill that proposes the audit of
  dependencies, `task-cycle/skill/SKILL.md` (the part after the request opens; step 12 and 13) and
  `task-cycle/skill/request_template.md` where the description must carry the result of the CI.
- The-way holds no `guidelines/` directory, so there are no guideline files to read.

A reach beyond this list is named in your report: what, where and why.

## What the change is

All seven *To do* items of the frozen task and the single acceptance criterion; the six rows of
*Settlements to record* are written by this change (rows 1, 2, 4 and 6 as sentences of WAY-16,
WAY-206 and WAY-160; row 3 as the comment of the CI file; row 5 as the installer's block). Points
the orchestrator has settled for you:

1. **The CI file of the-way.** A GitHub Actions workflow in `.github/workflows/` that on every pull
   request to `foundations` runs, on Linux, exactly `python -B gate/run_tests.py` and no other
   checking command (the invariant `ci-checking-commands`). It takes the version of Python from the
   repository's `.python-version`. It fetches the history `foundation_check.py` needs to compare with
   the commit the branch left the target branch from; find out how the script finds it and write what
   it needs. The workflow's file is claimed by no part of the part map yet: put it in the part whose
   responsibility it fits and say why in your report.
2. **The five tests.** The five tests of `instruction-files/test_check_instructions.py` that Windows
   skips (links, loops of links, FIFO) must run in that CI instead of being skipped. This machine
   runs Windows; **Docker is present**, and you may run the tests of single directories on Linux:
   `docker run --rm --memory 2g` with a Python image of the version in `.python-version`, the worktree
   (or a copy of it in your directory under `.runs/`) mounted read only, and
   `python -B gate/run_tests.py <directory>` inside; remove each container and each copy before you
   return. **Never run the whole gate**, on Windows or in a container: the orchestrator alone runs it,
   and only on a signal of the day's advisor, since it takes much memory. A test that fails on Linux
   and is not yours to fix by a small correction within the task is no work of this change: name it in
   your report for the request (the task says a larger fix is set apart as a remark in the
   description).
3. **The description for products.** To do 2 asks for a description of what a product's CI file must
   contain: the one command on every merge request, `.the-way` at the commit the product pinned and
   never the latest (WAY-34), the history `foundation_check.py` needs, and the result set as a
   required check with a bypass for the owner. Choose its place (the installer's block points to it;
   `installation/README.md` is the file that already explains how a product uses the pinned version),
   keep it short, and write it so that a product's owner can follow it. Do not write a CI file for a
   product and do not make the installer insert one (settlement 1).
4. **The installer's block** (To do 3): change only the paragraph that begins "Before a merge, run
   every test of this repository with its one command", and its tests. The block's wording about the
   one command runs `check_instructions.py` too, a script error stopping the tests and a warning not.
   The wording says the command runs in CI on every merge request and points to the description of
   item 3. The installer's promise to products (which files it touches) does not change.
5. **The skill of coding guidelines** (To do 5): the point of `product-guidelines/coding/settle.md`
   about the audit of dependencies (about line 123) and the place where the skill proposes the audit
   of dependencies: a vulnerability found in a dependency the product already holds has a signal, the
   alerts of the service the repository lies on (on GitHub, Dependabot alerts); the skill proposes
   that the product turns them on, and the human turns them on. WAY-206 gets the matching sentence
   (settlement 4) and keeps its audit of a change and its sentence that the template carries no audit
   of the whole tree; its *Verification* and *Rationale* are brought in line.
6. **The cycle's skill** (To do 7): the part of `task-cycle/skill/SKILL.md` after the request opens
   tells the orchestrator, where CI runs on the open request, to wait for its result, to treat a red
   result as a failed final gate (a fix and its review) and to put the result into the description;
   WAY-160 gets the matching sentence (settlement 6). Where `task-cycle/skill/request_template.md`
   or `task-cycle/request_check.py` has to carry the CI result for the description, change it with
   its tests. The request template names no checks the CI cannot yet give; keep it short.
7. **WAY-16 and the invariants** (To do 1): the sentences of settlements 1 and 2. Check that
   `ci-checking-commands` and the other invariants still read true after it, and that the-way's own
   `agent-instructions/README.md` ("Check the change") and `AGENTS.md` say what is now true about CI.
8. **The part map:** add or correct what the change makes false (the CI file's place).

Where the foundation entries you write are at stake, the search of the whole foundation after the
entries are settled (WAY-33) is yours, as `foundation_step.md` gives.

## Checks

The focused checks of your work: `python -B gate/run_tests.py <directory>` for each directory you
change (for `installation`, `task-cycle`, `elements/common` and so on), and
`python -B elements/common/foundation_check.py` for the foundation. Every check you report has its
command and its exit code. Your own-work check (as `task-cycle/change/SKILL.md` gives it) is part of
the report. You run no more than one test directory at a time.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
in the system's temporary directory, in the scratch directory of a session or in the main checkout
of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by
itself under its session's directory is moved into the agent's directory and the original removed.
The files that a product's own tools and tests make by themselves are no working copy of the agent
and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a
worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside
its report what the report needs, and states in the report where each copy stood and that it was
removed. Where a removal fails, the agent finishes all the same and names in the report the
remainder, with its full path and the reason it stayed.

Your directory is `.runs/author/`.

## Return

Return the status (`done`, `done with concerns`, `questions`, `returned`, `reserved` or `blocked`),
your commits, one line of check results naming what failed or did not run, and the report's path.
