# Report 11 — foundation step 1.7, check author (saved by the orchestrator from the returned text)

Wrote `gate/test_skills_reach_the_way_sessions.py` only; committed nothing. Gate exit 1: 98 tests, the control passes, the
test citing `skill-entry-points/1` fails (no entry points yet); no import or syntax errors.

File: docstring in the form of `test_wording_reaches_dependants.py`, then `# flow: skills-reach-the-way-sessions`; `ROOT`
the folder above `gate/`; imports nothing from `agent-instructions/` and nothing that computes entry points. Fixed values
written out from the sentence: `.claude/skills`, `.agents/skills`, prefix `the-way-`, the four required phrases, the
prefix words, the generator command, the two control paths.
- `discover(root)`: the brief's `git ls-files -z --cached --others --exclude-standard -- ':(glob)**/SKILL.md'` in
  `root`; duplicates removed; paths under root `.claude/`/`.agents/` dropped; the glob also catches a root `SKILL.md`.
- `frontmatter(text)`: own YAML-header reader (plain values with indented continuation, quoted values over lines, `>`/`|`).
- `sentences(text)`: sentence split (reading 4).
- `problems(root)`: one line per failed property naming the file — skill with no name or no description; missing
  `.claude` / `.agents` file; copies not byte-identical; per distinct copy (`entry_problems`): header names
  `the-way-<name>`, description starts with the skill's (whitespace collapsed), path in backticks, the four phrases, a
  sentence holding the prefix words and naming every skill in backticks; every `the-way-*` folder matches a skill.
- `test_every_skill_reaches_a_session_on_the_way`: `# invariant: skill-entry-points/1` alone inside the method; positive
  control (`discover` finds `elements/decisions/skill/SKILL.md`, `task-cycle/skill/SKILL.md`); `problems(ROOT) == []`
  with a message naming `python -B agent-instructions/skill_entry_points.py --write`.
- `test_problems_reports_a_skill_the_session_does_not_see`: cites nothing; temporary `git init`, no commit, git env vars
  cleared, files untracked: `alpha` no entry points (two lines), `beta` only `.claude` (the `.agents` line), `gamma` copies
  differing only in line endings (byte-identity line only), `delta` correct (nothing), `.claude/skills/the-way-orphan`
  (reported); exact lines asserted, exactly 5 problems.

Run: exit 1; `FAIL: test_every_skill_reaches_a_session_on_the_way`; `Ran 98 tests`; `FAILED (failures=1)`. Verdict line:
`{"check": "gate/test_skills_reach_the_way_sessions.py::SkillsReachTheWaySessions.test_every_skill_reaches_a_session_on_the_way", "verdict": "fail", "invariant": "skill-entry-points/1", …}`
— 22 problems, two missing files for each of 11 skills; no "gives no name", no orphan line.

Readings of the sentence: 1 the names in the prefix sentence are `<name>` without the prefix (`<name>` = "the name its
frontmatter gives"); 2 the four phrases need not stand in backticks (only the path is required "in backticks"); 3 the
properties apply to each entry-point copy, a byte-identical second copy skipped; 4 a sentence ends at `.`, `!`, `?` +
whitespace, or a blank line; 5 the working tree is checked, only folders directly inside the skills folders count; 6 a
skill with no name/description is a problem; 7 `# flow:` placed after the docstring as the reference file does.

Question: prefixed or unprefixed names in the prefix sentence? The test requires unprefixed.
Orchestrator answer (from the sentence only): unprefixed — `<name>` is defined as the name the frontmatter gives; no
change.
