# Final fix wave — code findings for the generator's implementer

Source: final review `C:\Storage\repos\the-way-skills-self\.runs\task-cycles\the-way-skills-in-the-way\reports\report_16_final_review.md`
and spec amendment R13 (`…\spec.md` §11, end of file — read it). The foundation side is fixed by another agent; the gate's
check `gate/test_skills_reach_the_way_sessions.py` and the invariant stay unchanged (read-only; do not open the check).

1. Important 1 — `agent-instructions/skill_entry_points.py`: `discover` also stops with `GeneratorError` naming the file
   when a description is not a safe plain YAML scalar: it starts with one of `-` `?` `:` `,` `[` `]` `{` `}` `#` `&` `*`
   `!` `|` `>` `'` `"` `%` `@` or a backtick, or contains `: ` or ` #`, or ends with `:`. Keep the existing rejection of
   folded `>`/`|` values (it is covered by the "starts with" rule; one message is enough if you merge them, but keep every
   existing test green). Tests in `agent-instructions/test_skill_entry_points.py` (`FrontmatterErrors` or beside it):
   written-out cases for a double-quoted description, a single-quoted one, one containing `: `, one containing ` #`, one
   ending with `:`, and one starting with a backtick — each stops with a message naming the file and writes nothing; and a
   positive case: a description with a colon not followed by a space (e.g. `Use at 10:30.`) is accepted.
2. Minor 3 — entry point text (`skill_entry_points.py` around line 171) and the written-out expected text in the test: right
   after "…never a copy in another checkout or worktree." add the sentence "If `<path>` is absent there, stop and say so."
   (with `<path>` the skill's path in backticks, as the paragraph already writes it). Keep the paragraph on one line.
3. Ledger minor — `test_skill_entry_points.py` (around line 144-146): replace the literal U+FEFF character with the escape
   `"\ufeff"` so the byte-order-mark case is visible in the source.

Test-first: change the tests, see them fail, change the generator, see them pass; regenerate with
`python -B agent-instructions/skill_entry_points.py --write` (never edit entry points by hand); then
`python -B agent-instructions/skill_entry_points.py` (expect `entry points are current`). Covering checks:
`python -B gate/run_tests.py agent-instructions`, `python -B gate/run_tests.py gate --record .runs/gate-tests.jsonl`
(expect `skill-entry-points/1` pass), `python -B elements/part-map/format_guard.py foundations/part_map.md --base none`,
`python -B gate/run_tests.py installation`. Commit by explicit paths:
`git commit -m "fix(agent-instructions): Refuse a description the frontmatter cannot carry, and stop when the skill is absent" --
agent-instructions/skill_entry_points.py agent-instructions/test_skill_entry_points.py .claude/skills .agents/skills`.
Append a fix report to `C:\Storage\repos\the-way-skills-self\.superpowers\sdd\plan\task-2-report.md` (what changed, the
covering tests, the commands, their output) — or, if refused, put it in your reply.
