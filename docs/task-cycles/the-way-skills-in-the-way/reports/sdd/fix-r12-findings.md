# Fix round 1 (R12) — findings for the generator's implementer

Finding (Task 3 review, Important 1, ruled load-bearing; spec amendment R12 in
`C:\Storage\repos\the-way-skills-self\.runs\task-cycles\the-way-skills-in-the-way\spec.md` §10 — read it): the entry
point's root and second product check say "the session's start directory" / "the directory the session was started in";
after Claude Code's `/cd` that is the wrong root. The foundation is already corrected (commit 972e9ad); the invariant's
sentence is unchanged, so the gate's check stays as it is (read-only; do not open it).

Change, exactly as §10 gives it, in `agent-instructions/skill_entry_points.py` (the entry point text, around lines
166-167) and the expected text written out in `agent-instructions/test_skill_entry_points.py` (around lines 45, 48-49):

- the second check bullet: "`git ls-files --stage -- ':/.the-way'`, run in the session's working directory, prints a line:
  the session works in a product that pins the-way."
- the root paragraph: "The process root is the checkout or worktree the session works in: the directory
  `git rev-parse --show-toplevel` prints when run in the session's working directory — the directory the session was
  started in, or the one it was last moved to (Claude Code's `/cd`) — not in the shell's current directory, which moves
  with `cd`. Read `<path>` there in full and follow it, and read the files it names under the same root, never a copy in
  another checkout or worktree. If the skill tells you to resolve a link to find the-way, skip that: the root is the one
  above. Do not substitute a global skill."

Keep each paragraph on one line, as now. Then, test-first: change the expected text in the test, see it fail, change the
generator, see it pass; run `python -B agent-instructions/skill_entry_points.py --write` to regenerate the 22 entry points
(never edit them by hand), `python -B agent-instructions/skill_entry_points.py` (expect `entry points are current`).
Covering checks: `python -B gate/run_tests.py agent-instructions`, `python -B gate/run_tests.py gate --record
.runs/gate-tests.jsonl` (expect `skill-entry-points/1` pass), `python -B elements/part-map/format_guard.py
foundations/part_map.md --base none`, `python -B gate/run_tests.py installation`. Commit by explicit paths:
`git commit -m "fix(agent-instructions): Read the-way from the session's working directory, not its start" --
agent-instructions/skill_entry_points.py agent-instructions/test_skill_entry_points.py .claude/skills .agents/skills`.
Append a fix report to `C:\Storage\repos\the-way-skills-self\.superpowers\sdd\plan\task-2-report.md` (what changed, the
covering tests, the commands, their output) — or, if the write is refused, put it in your reply.
