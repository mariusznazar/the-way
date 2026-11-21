# Report of the return step after correction 1

**Status:** `done` — the comparison found nothing to correct; no commit.

Head compared: `429cade12c23fb9053fec841094258b6fde4ffda`; the worktree is clean.

## What I compared (read at the head)

- **Part map, entry `agent-instructions`** (the sentence changed by the correction): it says the entry points
  are those through which a human starts the-way's skills, which Claude Code keeps from the model because of
  the field in their header, while Codex ignores that field and the skills stay visible to the model there.
  It agrees with the generator (the field in all 46 entry points, both copies identical: the generator without
  `--write` reports "entry points are current"), with `AGENTS.md` (the field "in Claude Code keeps the model
  from being offered a skill of the-way and from calling one"; `.agents/skills/` for Codex), and with the
  entries below.
- **WAY-127** (both paragraphs of the sentence, *Scope*, *Based on*, *Verification*, *Rationale*, *Rejected*):
  it states the hiding only as Claude Code's ("so that Claude Code offers the model no skill of the-way",
  "removes them from what Claude Code offers the model", "in Claude Code a request naming a skill without its
  command brings no skill"). Its only mentions of Codex (the entry point's own directory that Codex lists; how
  Claude Code and Codex settle two skills of one name; `codex-repository-skills` and `codex-skill-paths` in
  *Based on*) say nothing about the field, so none contradicts the part map sentence. The hand-over (file in
  the-way itself with the path from the entry point's list, product's own entry point in a product) is what
  the entry points and the 15 skill paragraphs say.
- **Invariant `skill-entry-points`**: the sentence (pair byte-identical, name, description start, the field,
  the text leading to the `SKILL.md`, "do not call it" and "read that skill's `SKILL.md`", a line with name
  and path for every skill, the directories) is what `gate/test_skills_reach_the_way_sessions.py` checks; the
  correction changed only the test's docstring and failure message, not a check. The invariant is cited by
  the test, and `gate` passes (the correction's run: exit 0).
- **Fact `claude-code-skill-model-hiding`**: unchanged by the correction; it states only Claude Code's
  behaviour and quotes the page; it names nothing about Codex, so it does not collide with the part map
  sentence. Per the handoff, no fact is written for the Codex result.
- **The sentence of `AGENTS.md` and the message of the test** (what the correction changed): both list the
  causes in the same words; the list matches the checks of `problems` and `entry_problems` as I read them in
  the correction (file that cannot be read, no name or description, an entry point missing, a pair that
  differs in bytes, no frontmatter, header does not name the skill, description does not start with the
  skill's, field missing, path of the skill missing, a required command or sentence missing, a skill's line
  missing, a directory with no skill). The review's Minor M1 on the wording of that list is left for the
  request, as the handoff says; it is a wording of the summary, not an entry that stopped matching the code.

No decision, invariant, fact, glossary term or part-map entry other than these bears on the correction's
texts; the search of the return step after the first review (`foundations/decisions.md`, `glossary.md`,
`part_map.md` for "project skill", "the-way-<name>", "`the-way-` prefix" and "entry point") stands, and the
correction added no text to those files except the part map sentence.

## What I wrote

Nothing; no entry, no correction, no commit. No choice of the correction binds after the merge in a way a
decision or an invariant is to carry: the wording of a message and of a sentence in `AGENTS.md` is not a rule
(the question of the decisions template's "Where it goes": an instruction for how an agent works, which stands
in the instruction file itself). The review's four Minor findings are not fixed here (M1 wording of the
summary, M2 the one hand check behind the part map sentence, M3 the repeated paragraph in 15 skills, M4 the
request's description); none shows an entry that no longer matches the code.

## Checks (command → exit code)

- `python -B elements/common/foundation_check.py` → 0 ("0 errors").
- `python -B agent-instructions/skill_entry_points.py` (without `--write`) → 0 ("entry points are current").
- Not run: tests of any directory and the full gate; nothing changed since the correction's runs (`gate` 0,
  `agent-instructions` 0, `instruction-files` 0, `elements/part-map` 0, `elements/common` 0).

## Working copies

None made; `.runs/author-correction-1-return/` was not created.

## Unread material

- `reports/review-correction-1-report.md`: not read; the handoff gives the four Minor findings.
- The task document, the record's other files, and the request's description: not read.
- The invariant and the fact were not opened again word for word; I compared the invariant with the test and
  the fact with the part map sentence from my earlier reading of both in this session.

## Searches not found or unclear

- A search of `foundations/decisions.md` for "codex" in the range of WAY-127 found three lines, all listed
  above, none about the field. No entry in the foundation states Codex's behaviour with the field besides the
  part map sentence; the handoff says no fact is to be written, so I record this as a gap, not a finding.
