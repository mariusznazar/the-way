# Report of the one author — hide the entry points of the-way's skills from the model

**Status:** `done with concerns` (concerns: the generator carries a list of paths I chose, a clause of
WAY-127 and of the invariant that the rows do not give; the check in a real session ran on a probe
repository, not on loop2; see "Questions and concerns").

Branch `task/hide-the-way-skills-from-models`, base `19e5774aed6d1d628042e23deccc110ed9f112c0`.

## Commits

1. `f9cae3a6` — Hide the entry points of the-way's skills from the model and list each skill's file in them
   (generator, its tests, the end-to-end test, the 46 regenerated entry points)
2. `f3188faa` — Say that a skill of the-way reaches another by its file in the-way itself
   (the paragraphs of 15 skills, `AGENTS.md`, `README.md`)
3. `7d063ef2` — Record that the entry points of the-way's skills are hidden from the model
   (WAY-127, the invariant, the new fact, the part map)

## Files changed (added / removed lines, against the base)

- `agent-instructions/skill_entry_points.py` 17 / 12
- `agent-instructions/test_skill_entry_points.py` 30 / 8
- `gate/test_skills_reach_the_way_sessions.py` 51 / 32
- 46 entry points, `.claude/skills/the-way-*/SKILL.md` and `.agents/skills/the-way-*/SKILL.md`: 1196 / 46 in all
- Skill paragraphs "where the-way lies" (each 5–6 / 2): `elements/common/skill/SKILL.md`,
  `elements/decisions/skill/SKILL.md`, `elements/environment-facts/skill/SKILL.md`,
  `elements/glossary/skill/SKILL.md`, `elements/invariants/skill/SKILL.md`,
  `elements/part-map/skill/SKILL.md`, `foundation-review/SKILL.md`,
  `product-guidelines/coding/SKILL.md`, `product-guidelines/styleguide/SKILL.md`,
  `product-guidelines/testing/SKILL.md`, `project-level/lead/skill/SKILL.md`,
  `project-level/plan/skill/SKILL.md`, `project-level/skill/SKILL.md`,
  `project-level/task/skill/SKILL.md`, `project-level/technology/SKILL.md`
- `AGENTS.md` 13 / 10, `README.md` 8 / 4
- `foundations/decisions.md` 40 / 14 (WAY-127), `foundations/environment_facts.md` 6 / 0,
  `foundations/invariants.md` 1 / 1, `foundations/part_map.md` 2 / 2

`installation/install.py` and its test are unchanged: the product's hand-over stays as it is.

## What the change does

- The generator writes `disable-model-invocation: true` in the header of each entry point (one constant,
  `HIDING_FIELD`); both copies stay byte-identical. The docstring of the script says so.
- The paragraph of the entry point that told a session to "use the project skill of the same name with the
  `the-way-` prefix" now says: do not call another the-way skill, read its `SKILL.md` under the same root in
  full and follow it, and lists every skill as ``- `name`: `path` `` (function `skill_list`, which replaces
  `sibling_names`). The first paragraph (stop in a product, use the product's own project skill) is unchanged.
- In the 15 skills that said "each the-way skill named below is the project skill with the `the-way-`
  prefix", the paragraph now distinguishes the two cases: in the-way itself a named skill is read as a file
  (the `SKILL.md` whose frontmatter has `name: <that name>`, which a search of the files named `SKILL.md`
  finds — the same convention as `task-cycle/plan/SKILL.md` and `task-cycle/skill/foundation_step.md`); in a
  product it is the project skill with the prefix.
- `AGENTS.md` `## Skills` and the `README.md` section "Using the skills" say that a human starts a skill with
  `/the-way-<name>` and a skill hands work on through its file; neither says anything about Codex hiding or
  showing a skill (the `README.md` cites only Claude Code's documented behaviour).

## Foundation entries

Each written by the `SKILL.md` of its element, read as a file. Marks as `foundation_step.md` gives.

| Entry | Mark | One sentence in English | Jedno zdanie po polsku |
|---|---|---|---|
| WAY-127 (sentence, *Rationale*, *Rejected*, *Verification*, *Based on* gains `claude-code-skill-model-hiding`) | `row 1` (with a clause of mine, below) | The entry points of the-way's skills carry `disable-model-invocation: true`, so the model is offered none; a human starts a skill with `/the-way-<name>`, a skill hands another on by reading its `SKILL.md` in the-way itself, and a product's hand-over stays through its own entry point. | Wejścia do skilli the way mają w nagłówku `disable-model-invocation: true`, więc model ich nie widzi; człowiek uruchamia skill przez `/the-way-<name>`, w samym the way skill przekazuje pracę innemu przez jego `SKILL.md`, a w produkcie przekazanie zostaje przez wejście produktu. |
| invariant `skill-entry-points` | `row 1` (derives from WAY-127; same clause of mine) | Each pair of entry points is byte-identical, holds the field `disable-model-invocation: true`, tells a session not to call another such skill but to read its `SKILL.md`, and lists every such skill with the path of its `SKILL.md`. | Każda para wejść jest identyczna bajt w bajt, ma pole `disable-model-invocation: true`, każe nie wywoływać innego takiego skilla, tylko czytać jego `SKILL.md`, i wylicza każdy taki skill ze ścieżką jego `SKILL.md`. |
| environment fact `claude-code-skill-model-hiding` | `row 2` | Claude Code removes a skill with `disable-model-invocation: true` from Claude's context, so its description is not in context and Claude does not invoke it on its own, while the user can still invoke it. | Claude Code usuwa z kontekstu modelu skill z `disable-model-invocation: true`, więc jego opis nie jest w kontekście i model nie wywołuje go sam, a użytkownik dalej może go uruchomić. |
| part map, `agent-instructions` responsibility sentence | `the cycle's` | The entry points are described as the way a human starts the-way's skills, hidden from the model, not as what makes them visible to sessions. | Wejścia opisano jako sposób, w jaki człowiek uruchamia skille the way, ukryte przed modelem, a nie jako to, co czyni je widocznymi dla sesji. |

- No pair of examples was added anywhere. The `complies`/`violates` examples of WAY-127 for the paragraphs of
  skills were reworded in place (they existed before).
- **Clause of mine, not given by the rows:** "each entry point giving the path of every skill" in the second
  paragraph of WAY-127, and "lists every such skill ... with the path of its `SKILL.md`" in the invariant. The
  rows say "przez jego plik czytany po ścieżce"; the list of paths is how I made the path reachable from the
  text (a name alone gives no path). If the orchestrator reads this as a part the rows do not give, the two
  entries become `the cycle's` and go before the human.
- *Rejected* of WAY-127 gained three ways, each from the task's *Not chosen* (settings written by the
  installer; a hand list of exclusions; the file hand-over in a product as well). The way "entry points
  untracked and generated locally" is already in the existing *Rejected* of WAY-127 ("entry points written per
  checkout and ignored by git"), so it was not added again. The cost of each is as the task gives it.
- The environment fact quotes the page of Claude Code documentation read on 2026-11-21. I read the live page
  (`https://code.claude.com/docs/en/skills`, its raw Markdown) and the archived copy of 2026-11-14 that the
  fact `claude-code-project-skills` already cites; both hold the sentence "Hide individual skills ... This
  removes the skill from Claude’s context entirely." and the table row `disable-model-invocation: true` with
  "Yes", "Not on its own", "Description not in context, full skill loads when invoked". The tool I have for
  reading pages refuses `web.archive.org`; I read the archived copy with `curl`. The sentence of the
  environment fact and the quoted passage are the page's. The archive's apostrophe is typographic (’), the
  live page's is straight; I wrote the typographic one in the quoted sentence.

## Checks (command → exit code)

- Invariant test, failing run before the entry points were regenerated:
  `python -B gate/run_tests.py gate` → 1 (copy in `reports/author-invariant-test-failing-run.txt`; the
  failing test is `test_every_skill_reaches_a_session_on_the_way`, 46 lines "its frontmatter does not hold
  `disable-model-invocation: true`"). Passing run after
  `python -B agent-instructions/skill_entry_points.py --write`: `python -B gate/run_tests.py gate` → 0.
- Generator tests, failing run (the test written first, with a stub `skill_list`):
  `python -B gate/run_tests.py agent-instructions` → 1, six assertions failing
  (copy in `reports/author-generator-tests-failing-run.txt`). Passing run: same command → 0, 53 tests.
- `python -B agent-instructions/skill_entry_points.py` (without `--write`) → 0, "entry points are current".
- `python -B elements/common/foundation_check.py` → 0, "0 errors" (run after the foundation commit content).
- Focused runs, `python -B gate/run_tests.py <directory>` → 0 each: `agent-instructions`, `gate`,
  `elements/common`, `elements/part-map`, `instruction-files`, `product-guidelines`, `project-level`,
  `task-cycle`, and `installation` (73 tests, 703 s when run alone; a first run in parallel with the others
  hit my 560 s timeout, exit 124, and was repeated alone).
- A fix of formatting: the first passing run of `agent-instructions` → 1 because
  `test_every_python_file_of_the_parts_stands_as_the_formatter_leaves_it` reported one expression of
  `gate/test_skills_reach_the_way_sessions.py` laid out against the formatter; I laid it out as the formatter
  prints it; rerun → 0.
- The full gate was not run (the orchestrator's or CI's).

The failing run of the end-to-end test failed for the expected reason; the test that checks the test
(`test_problems_reports_a_skill_the_session_does_not_see`) was written first against the old checker and
failed at its assertion on the `delta` skill (the old checker flagged the new text); after the checker was
changed it passes, with two new cases (`epsilon` with no field, `zeta` with no line for `alpha`), 7 findings
in all.

## Own-work check

- The requirement most likely not met: acceptance criterion 1, "after a read of a file in a subdirectory,
  none of the entries is on the list the model gets — checked once in a real session". Check: a probe
  repository under `.runs/author/probe/` with a nested `sub/.claude/skills/` holding one skill with
  `disable-model-invocation: true` and one without, and `claude -p --model haiku --allowedTools Read` started
  at the repository root, told to read `sub/file.txt` and then name every skill in its context whose name
  contains "probe". Claude Code 2.1.330. Result: it named only the skill without the field
  (`the-way-shown-probe`), so the nested skills did load (positive control) and the hidden one was not
  offered. This was a probe of the mechanism with the same field, not a session in loop2 with the real
  entry points; the measurement in loop2 stays the out-of-scope step. The probe directories are removed.
- Second most likely: a skill or a file that still tells a session to call a skill of the-way. Check: a
  search of the `SKILL.md` files and the files beside them for `the-way- prefix`, for `project skill` and for
  the 23 skill names in backticks. All 15 skills that carried the prefix sentence now carry the two cases;
  the skills of `task-cycle/` name other skills only as labels of methods that the handoff gives by path
  (`task-cycle/skill/SKILL.md` lines 253–256 already say so); `elements/common/way_of_working.md` and the
  files beside element skills say "through `record-invariant`" etc., which the paragraph of the skill that
  led the session there now reads as a file.
- What I did not check: that Codex loads a `.agents/skills/` copy with the field (the cycle's answer is to
  keep both copies identical; nothing was run on Codex).

## Choices (with the way rejected and its cost if wrong)

1. **The way the entry points and skills phrase the file hand-over.** Entry point: a list of every skill with
   the path of its `SKILL.md`, generated, and the sentence "do not call it ... read that skill's `SKILL.md`
   under the same root". Skill paragraphs: "its `SKILL.md` is the file under that root whose frontmatter has
   the line `name: <that name>`, which a search of the files named `SKILL.md` finds" (the convention of
   `task-cycle/plan/SKILL.md` and `foundation_step.md`). Rejected: a hand-kept table of paths in a skill —
   the list goes stale when a skill moves (WAY-127 already rejects lists by hand); only the search by name
   in the entry point — one more step for each hand-over, with a search that can match a copy in another
   place. Cost if wrong: each entry point is 23 lines longer (read only when a human starts the skill); the
   invariant and its test pin the list.
2. **Codex:** both copies carry the field and stay byte-identical, as the handoff gives. Cost if wrong: if
   Codex refuses a skill with an unknown field, the entry points do not load there and the copies must be
   split, which the invariant forbids today; a probe of `codex exec` was not possible.
3. **The first paragraph of the entry point** (stop in a product and use the product's project skill)
   stays as it was; it now matters only for a human who starts the nested entry point in a product.
4. **Part map:** I changed the sentence "make the-way's skills visible to sessions on it", which the change
   made false, to "through which a human starts the-way's skills in sessions on it, hidden from the model".
   Rejected: leaving it (it would say the opposite of WAY-127); cost if wrong: one sentence to reword.
5. **`instruction-files/tool_loading.md`** already holds the field; I did not cite the new fact there.
6. No move of code before the change (WAY-365): `skill_entry_points.py` (about 280 lines) and
   `entry_point_text` (about 40 lines) are under the thresholds of WAY-385.

## Reaches beyond the handoff

- `README.md` lines 125 and 156–162 and `foundations/part_map.md` line 170 were read and changed (the handoff
  names `README.md` and the entry of the part map; the lines of the README beyond the one of `the-way-<name>`
  were read to place the edit).
- `elements/part-map/skill/decide_entry.md`, `write.md` and `template.md` (part-map), the element skill files
  of environment facts (`read.md`, `decide_entry.md`, `draft.md`, `write.md`, `template.md`) and of
  invariants (`decide_entry.md`, `draft.md`, `write.md`, `template.md`), and `elements/decisions/template.md`
  were read to write the entries; `elements/common/rules.md` also, as those skills name it.
- `task-cycle/plan/SKILL.md` (lines 1–40) and `task-cycle/skill/SKILL.md` (lines 1–40, 71–76, 250–258) were read
  to find the convention for a skill read as a file; `foundations/decisions.md` WAY-385 for the size rule.
- `instruction-files/judging.md` and `instruction-files/tool_loading.md` (lines 40–50 and 50–64) were read for
  texts that say a session finds skills by calling them; none needed a change.
- Also the rules of the author's own environment (`scripts.md`, `git.md`) the harness hook asked for.

## Working copies

- `.runs/author/`: logs of runs and the message files of commits; the failing runs are kept in `reports/` as
  `author-invariant-test-failing-run.txt` and `author-generator-tests-failing-run.txt`; the rest was removed.
  `.runs/author/probe/` and `.runs/author/probe_copy/` (the probe repositories for the real-session check)
  stood under `.runs/author/` and were removed. `.runs/author/skills.md`, `arch.html` (the pages I read) were
  removed. Nothing remains.

## Unread material

- Decisions WAY-125, WAY-34, WAY-44, WAY-256: read in part. WAY-34 whole; WAY-125 whole (its entry); WAY-44 and
  WAY-256 not opened (WAY-127 only names them under *Relations*; the change touches neither's sentence).
- The environment facts `codex-repository-skills` and `codex-skill-paths`: read whole.
- The other element templates (`glossary`) and skills and the part map as a whole: not read; the part-map
  entry for `agent-instructions` was read in the lines 170–185 and the "Using the skills" area only.
- `elements/*/examples.md` of the three elements I wrote into: not read (the entries edited follow
  the entries around them).
- `installation/install.py` and `installation/README.md`: only the lines a search of `the-way-` prefix found;
  not read whole (the handoff: must not change).
- Pages: the page of Claude Code documentation read in the two passages above, not the whole page.

## Searches not found or unclear

- The task's *Context* gives the table "Control who invokes a skill" and says only that a human "can still
  invoke it by `/name`"; the page's table row says "You can invoke: Yes". I quoted the row, not a sentence
  about `/name`. The sentence of the fact says "the user can still invoke it".
- No test in the repository cites WAY-127 or `skill-entry-points` besides `gate/test_skills_reach_the_way_sessions.py`;
  none other had to change.
- Whether Codex loads a skill with an unknown field: not found in the sources named by the handoff; not probed.

## Questions and concerns

1. The clause of mine in WAY-127 and in the invariant (the list of paths). Recommended: keep it — without it
   a session reading a skill that names `critique` has only a name; the invariant's test pins it.
2. Acceptance criterion 1 was checked on a probe repository with Claude Code 2.1.330 and the model haiku, not on
   loop2. Recommended: the orchestrator or the step after the merge repeats it with loop2's script
   (`09_start_po_zmianie.py`) after the pin moves.
3. In a product, the hidden nested entry points can still be started by a human; their first paragraph tells
   the human's session to use the product's own project skill. Nothing to do; named for completeness.
