# Handoff — correction 1 for the human's remarks

The person who requested this cycle delegated intermediate choices to the orchestrator; the human's remarks bind (they are the day advisor's words for the human). You are a fresh agent that makes the correction; no one author of the change exists on this planned route.

## Where you work

- Worktree (work from its root): `the root of the worktree`, branch `task/the-way-coding-and-testing-guidelines`, head `db0c5f8` (the final tree is that of `3cf54a5`; `db0c5f8` only adds and removes the record). Nobody else writes in the worktree.
- Method: `task-cycle/change/SKILL.md` (`make-change`), variant **"a correction for the human's remarks"**; read it whole, and the file it names for that variant where it names it. A skill named by its name alone is the `SKILL.md` whose frontmatter `name:` is that name; you have no skill tool, read it as a file.
- Remarks: `.runs/task-cycles/the-way-coding-and-testing-guidelines/reports/correction-1-remarks.md` (word for word). Only the two items marked **Fix** bind; items marked **Let through** and answer 1 need no change and you change nothing for them.
- Frozen task: `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md`; the request's description and its Minor findings: `.runs/task-cycles/the-way-coding-and-testing-guidelines/request.md` (Minor findings 3 and 4 are the two you fix); the reports of the stages in `reports/` beside (the reviews that gave the findings: `review-return-report.md`).
- Your directory for working copies: `.runs/correction-1/`. Your full report: `.runs/task-cycles/the-way-coding-and-testing-guidelines/reports/correction-1-report.md`.
- Trust boundary: yes for the change as a whole, none in the files you touch. Irreversible operation: no. You never run the full gate (`python -B gate/run_tests.py` with no directory); the orchestrator runs it after the day advisor's start signal.
- Commit by path (`git add <path>…`), messages in English; the range of your correction starts at `db0c5f8`.

## What to do

1. **Minor finding 4 (WAY-395).** The decision says the tests give the time "as the option `--today` gives it"; the script `task-cycle/gate_times.py` has no such option and the tests of the-way replace the clock function in process (and give a fixed time where a script takes one). Correct the wording of WAY-395 in `foundations/decisions.md` to what the tests do, and correct each place that quotes the same phrase (search the whole foundation and `guidelines/` once, as the foundation step gives: WAY-33), `guidelines/testing.md` among them if it quotes it. Do not change a test or a script.
2. **Minor finding 3 (pairs of examples).** In WAY-380 and WAY-388 to WAY-391 remove the examples (the pair of *complies* and *violates* lines of *Verification*) that repeat what an invariant holds, since the template of decisions (`elements/decisions/template.md`, "Verification") allows a pair only for the part of the sentences that no invariant and no test checks. Read the review's words in `reports/review-return-report.md` (its Minor finding 1) and the template; keep an example only where it covers a part no invariant holds; where nothing remains, write *Verification* in the form the template gives for a decision with no such part (its invariants and tests named). The return step also noted the same for WAY-380 only because it names tests alone; check each of the five decisions.
3. Run `python -B elements/common/foundation_check.py` (whole, exit 0 expected) and `python -B gate/run_tests.py elements/common` and `python -B gate/run_tests.py agent-instructions` (focused); name each command and exit code in the report. Search once more that no other entry quotes what you changed (WAY-33).

## Working copies (word for word from the orchestrator's skill)

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
in the system's temporary directory, in the scratch directory of a session or in the main checkout
of the repository. The files that a product's own tools and tests make by
themselves are no working copy of the agent and stay outside this rule. Before the agent returns,
each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then
`git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in
the report where each copy stood and that it was removed. Where a removal fails, the agent finishes
all the same and names in the report the remainder, with its full path and the reason it stayed.

## What you return

Status, commits, a one-line check result with command and exit code, the report path, questions and concerns, **Unread material**, **Searches not found or unclear** (`none` is an answer; a missing section is returned to you), the working-copies line.
