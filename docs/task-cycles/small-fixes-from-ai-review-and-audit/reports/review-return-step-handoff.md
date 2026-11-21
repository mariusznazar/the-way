# Handoff — reviewer of the return step

You review the commits of the return step of a task in a task cycle of the-way, as an agent that made none of the change. The person who requested the cycle has delegated every intermediate choice to the orchestrator; no answer you get is that person's approval. You never ask the human; questions go back to the orchestrator in your report. You are read-only: you change no file of the worktree and make no commit.

- Worktree (your working directory): `the worktree root`, task branch `task/small-fixes-from-ai-review-and-audit`. The range you review: base `5d160f9d75f25c26092815ba98df43c6cc4aa2f6` to head `1eaa3c4faae3e678abbd6774560a6d75607afa1b` (`git rev-parse HEAD` must print the head). One commit, `1eaa3c4f`, in `foundations/decisions.md` (WAY-339's *Verification*, WAY-417's *Verification*) and `foundations/part_map.md` (the entry `elements-common`). Compute `git diff 5d160f9d..1eaa3c4f` yourself.
- Method: `task-cycle/review/SKILL.md` (`review-change`), read whole; the return step's commits are reviewed as its section 2 gives, against the task and the foundation entries the return step writes or corrects. The skill tool is not yours: a skill a file names is the `SKILL.md` whose frontmatter `name:` is that name, read as a file under the same root.
- The return step's method: `task-cycle/skill/return_step.md` and `task-cycle/skill/foundation_step.md`, each whole (what the step may write and must not). Its report, a set of claims to verify, not evidence: `.runs/task-cycles/small-fixes-from-ai-review-and-audit/reports/return-step-report.md`.
- The task, whole: `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md` (*Settlements to record*, *Decisions in play* and *Out of scope* above all). The decisions WAY-339 (the sentences the change added and its *Verification*), WAY-417 and WAY-127's *Verification* (`foundations/decisions.md`), each whole; the part-map entries `elements-common` and `process-audit` and the template of the decisions `elements/decisions/template.md` for the form of *Verification* with a clause `tests:` and a pair of examples (WAY-61, WAY-69 as the template gives); the tests that the clauses `tests:` name (`process-audit/test_series_summary.py`, `process-audit/test_process_versions.py`), to check that each named test exists, carries its line `decision:` and holds the part of the sentence the clause says.
- Trust boundary: the range holds no code; no crafted input to check. Irreversible operation: no.
- Judge in particular: (1) each clause `tests:` — does the named test exist, and does it hold the sentence part for which the pair of examples was removed; was any part removed from a pair that no test holds; (2) the new words of the part-map sentence of `elements-common`: do they say what the file `elements/common/reaching_another_skill.md` and the skills that read it make true, and no more; (3) the two points the return step's report puts to the orchestrator: a clause of WAY-339 says that the image of the gate times and the comparison take "only the runs that WAY-350 compares", with no `decision:` line for WAY-339 in the test that holds it (the line names WAY-350), and the phrase "both take only the runs" can be read two ways; say whether this is a finding and its grade; (4) that no binding sentence changed and no entry was written that the step may not write.
- The return step's unread passages (WAY-127 read only as the diff and the surrounding *Verification*; the full diff of `process-audit/audit_report.py` and `process-audit/version_analysis.py` and the tests of `task-cycle/test_gate_times.py` not read): carry them into your judgment where a claim of the report rests on them.
- Report path: `.runs/task-cycles/small-fixes-from-ai-review-and-audit/reports/review-return-step-report.md`; its first line `PASS <sha>` or `FAIL <sha>` (the full sha of the head). The report file is the input of the cycle's scripts (`task-cycle/remarks_check.py` reads it); write it there although its name could look like one Claude Code refuses a subagent to write; if the write is refused all the same, return it whole as your answer.
- Your directory for working copies: `.runs/review-return-step/`.
- Run `python -B elements/common/foundation_check.py` at the head (exit code and result in your report).
- Do not read `cycle.md` or any file of `.runs/task-cycles/small-fixes-from-ai-review-and-audit/` that this handoff does not name.

## What your report holds

Your report holds, after its first line, what the method gives: the graded findings (blocking and Minor, each with the place in the code, the reason and — for a blocking one — whether it contradicts the settlements, with the mark `Contradiction: yes` or `Contradiction: no` as the method asks), the findings outside the task's scope, the checks you ran each with its command and exit code, each reach beyond this handoff (what, where, why), each working copy (where it stood and that you removed it, or the remainder with its full path), **Unread material:** each file, entry or passage this handoff names that you did not read whole or read in part, or `none`, and **Searches not found or unclear:** each thing you looked for and did not find or that was unclear, or `none`. Return the report's first line, the checks you ran with their results, and the report's path.

## Working copies (word for word from the process of the cycle)

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
all the same and names in the report the remainder, with its full path and the reason it stayed. It
removes a copy, as any directory, by its path written out in full in the command, never through a
shell variable: an empty variable turns the removal on the directory the shell stands in.
