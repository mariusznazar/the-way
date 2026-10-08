# Report 15 — scoped re-review, Task 3 fix round 1 (saved by the orchestrator from the returned text)

Range c12d4dd..c61cebc (972e9ad foundation context only; c61cebc under re-review).

- Important 1 (root after `/cd`) — ADDRESSED: generator text `agent-instructions/skill_entry_points.py:~166-171` matches
  spec §10 word for word (second check "run in the session's working directory, prints a line: …"; root paragraph "…the
  checkout or worktree the session works in: … when run in the session's working directory — the directory the session
  was started in, or the one it was last moved to (Claude Code's `/cd`) — not in the shell's current directory, which
  moves with `cd`. …"); all 22 entry points carry it, one bullet line and one paragraph line per file.
- New breakage: none — copies byte-identical (pre/post index hashes in identical pairs); frontmatter, title, intro, first
  bullet, sibling sentence untouched; `DECISION_ENTRY` in `agent-instructions/test_skill_entry_points.py:~45-52` carries
  the same strings.
- Out of scope: the part-map failure mode in 972e9ad reworded beyond §10 (cites `${CLAUDE_SKILL_DIR}`); settled by the
  orchestrator.
- Tests: fix report names covering tests with output — RED 12 tests, 2 failures (difference from 1 not explained); GREEN
  after generator edit 1 failure (committed entry points), after `--write` 12 OK, dry run `entry points are current`;
  gate 98 OK with `skill-entry-points/1` pass; part-map guard 0 errors; installation 16 OK.
- Verdict: all findings addressed, no new Critical/Important breakage.
