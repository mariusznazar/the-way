Global constraints for Slice 5:
- Spec §7 (one sentence in steps 10 and 11 of `task-cycle/skill/SKILL.md`, as amended by C18 and
  C19): for an invariant a rule of the product's guidelines names with test cases, whose sentence
  the change adds or alters or one of whose test cases it rewrites, the reviewer also runs the check
  in a scratch worktree of the commit once with that invariant's good file and once with its bad
  file in place (the pair whose info string names it), records that it passes and fails there — for
  an invariant on the list of violated invariants, that the good file adds no failure the commit
  lacks and the bad file adds one, the per-file companion taking the strict reading — and the check
  is not accepted otherwise; the bad file is a case beside the deliberate break, never the break
  (WAY-168, WAY-197, WAY-69); a test case is applied only in that scratch worktree. Nothing else in
  the cycle changes; no review of code against guidelines (Q5, out of scope).
- C8: one sentence; frontmatter unchanged; `skill_entry_points.py` prints `entry points are current`.
- No invariant's code is covered; no deliberate break.
