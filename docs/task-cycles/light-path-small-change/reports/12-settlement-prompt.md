You apply the orchestrator's settlement of an independent assessment in one the-way task cycle. Mariusz
delegated intermediate choices to the orchestrator; questions go to it. Worktree
C:/Storage/repos/the-way-light-path, branch task/light-path-small-change, HEAD 70f6bda. Edit with the Edit
tool (files are LF); no subagents; no push.

Two edits, nothing else:
1. foundations/decisions.md, WAY-125/1 *Rationale* (follow `record-decision`,
   elements/decisions/skill/SKILL.md, for form only): delete from "; a change that outgrows that finding
   starts again rather than having a spec and a plan" through "without the shape of\nits code" so the
   paragraph ends "...while the checks on the finished change and the final review stay\n(WAY-13)." —
   keep the period; rewrap only the line holding the cut, lines ≤ 100 characters. The binding part must
   not change: confirm WAY-125's binding paragraph still hashes to f4d471cc (write it to a UTF-8 file,
   `python -B relation-model/fingerprint.py < file`).
2. task-cycle/record_template.md lines 9–10: the Foundation route line becomes exactly
   `- Foundation route: <unchanged | entry or invariant-test change; affected entries>` (one line, as at
   c64a607).

Checks: decisions guard `python -B elements/decisions/format_guard.py foundations/decisions.md --base none
--merge-onto none --record .runs/decisions.jsonl` (expect 0 errors, 7 warnings, 5 unchecked);
`python -B gate/run_tests.py elements/decisions`; `python -B gate/run_tests.py gate`;
`python -B gate/run_tests.py task-cycle` (expect NO TESTS RAN).
Commit: `git add foundations/decisions.md task-cycle/record_template.md` and
`git commit -F C:/Users/Mariusz/AppData/Local/Temp/claude/C--Storage-repos-the-way/f1c4ac63-3b4e-4e88-81d3-69c0173d41d5/scratchpad/commit-msg-settlement.txt`
— use that message file unchanged. Check `git log -1 --format='%h %ae'` shows <author email>.

Write your report to docs/task-cycles/light-path-small-change/reports/12-settlement-report.md
and return: commit hash, fingerprint, check one-liners.
