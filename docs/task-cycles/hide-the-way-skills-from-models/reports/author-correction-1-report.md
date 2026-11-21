# Report of correction 1 — the human's remarks on the request

**Status:** `done`

Range of the correction: after `48e64f104b2a4f656f4be4606c98c0959ffa975e`.

## Commits

- `429cade1` — Say in the part map that Codex ignores the hiding field, and name every cause the invariant
  test reports (`AGENTS.md`, `foundations/part_map.md`, `gate/test_skills_reach_the_way_sessions.py`)

## The remarks as made, and how I met each

1. *"Codex still loads the entry files that carry the new setting — checked by hand, nothing to fix here. ...
   in Codex the skills stay visible to the model — Codex ignores the setting. Write this result into the
   record as the remark the item asks for."* No change of code: the result goes into the record, which is the
   orchestrator's. What it shows binds my texts; I searched the files of the change for a text that says or
   implies that the model is offered no skill of the-way in Codex. The texts that state the hiding are all
   qualified as Claude Code's: WAY-127 ("so that Claude Code offers the model no skill of the-way";
   *Rationale*: "what Claude Code offers the model", "in Claude Code a request ..."), the entry point text
   ("since Claude Code does not offer the entry points of the-way's skills to the model") and the 15 skill
   paragraphs (same clause), `AGENTS.md` ("which in Claude Code keeps the model from being offered a skill"),
   `README.md` ("a Claude Code session does not call a skill of the-way") and the generator's docstring ("in
   Claude Code"). Two texts implied it without the qualification and are corrected in the commit above: the
   part map sentence (remark 3) and the docstring of the invariant's test ("would be offered to the model",
   now "by Claude Code"). The sentence of `AGENTS.md` that said "or the model would be offered it" is replaced
   by the list of causes (remark 3). No other text needed a change.
2. *Let a fresh reviewer read whole the four decisions ...* — not mine (the orchestrator dispatches it). I
   did nothing for it.
3. *"Fix them here: the description of the part in the part map has to say that hiding from the model is
   Claude Code's behaviour, and that in Codex the skills stay visible to the model (see 1); the summary of
   the invariant test's failure message and the matching sentence in the instructions for agents name every
   cause the test reports, not three."* Met in three places:
   - `foundations/part_map.md`, entry `agent-instructions`: the entry points are those "through which a human
     starts the-way's skills in sessions on it, which Claude Code keeps from the model because of the field
     in their header while Codex ignores that field and the skills stay visible to the model there".
   - The failure message of `test_every_skill_reaches_a_session_on_the_way` and the matching sentence of
     `AGENTS.md` (`## Skills`) now list every cause `problems` and `entry_problems` report, read from the
     code: a skill file that cannot be read or has no name or description; an entry point that is missing, or
     a pair that differs in bytes; an entry point with no frontmatter, whose header does not name the skill,
     does not start with its description or lacks `disable-model-invocation: true`, whose text lacks the path
     of its skill, a command or sentence the invariant requires, or the line of another skill; a directory
     `the-way-*` that no skill produces. The test's checks are unchanged (no assertion, constant or helper
     changed; the diff of the file is its docstring and that message).
   - The docstring of the test says "by Claude Code" for what would be offered to the model.

Items 4–6 are accepted; nothing to do.

## Checks (command → exit code)

- `python -B gate/run_tests.py gate` → 0.
- `python -B gate/run_tests.py agent-instructions` → 0 (it holds the formatter test of the file I edited).
- `python -B elements/common/foundation_check.py` → 0, "0 errors".
- `python -B agent-instructions/skill_entry_points.py` (without `--write`) → 0, "entry points are current".
- Also `python -B gate/run_tests.py <directory>` → 0 for `instruction-files`, `elements/part-map` and
  `elements/common` (they read `AGENTS.md` and the part map).
- The full gate was not run. No test was failing before the change, so there is no failing run to report; no
  invariant's test changed in assertion.

## Own-work check

- Requirement most likely not met: the message and the sentence of `AGENTS.md` name *every* cause the test
  reports. Check: I read `entry_problems` (no frontmatter; name; description; field; path of the skill;
  `REQUIRED_WORDS`; one line for each skill) and `problems` (file cannot be read; no name; no description; no
  file in a copy; copies not byte-identical; directory with no skill) and matched each to a clause of the
  message; the `REQUIRED_WORDS` are named as "a command or sentence the invariant requires". The match is by
  reading, not by a test; no test pins the wording of a message.
- Second: that the part map's statement of Codex's behaviour has a source. It has none in the foundation: the
  remark gives it as a hand check by the human's adviser (codex-cli 0.163.0). I wrote it as the remark asks.
  See the concern below.
- The entry points stay current: generator without `--write` → "entry points are current".

## Choices

- The message of the test lists the causes in one sentence rather than naming them by the invariant's
  clauses; rejected: a shorter summary with "among other things", which would again name some causes only.
  Cost if wrong: the message must be reworded when a check of the test is added or removed.
- The part map sentence says "Claude Code keeps from the model because of the field ... while Codex ignores
  that field". Rejected: leaving "hidden from the model" and adding a note; the remark asks that the
  description say it.

## Questions and concerns

- The statement that Codex ignores the field rests on the comment of the request (a hand check, codex-cli
  0.163.0, a model of the adviser's account), not on a source in the foundation. I did not run Codex and did
  not write an environment fact: the template asks for a reading with its command, tool version and output,
  which I do not have. Recommended: the orchestrator decides whether the reading is to be written as a fact
  with the adviser's output; until then the part map sentence is the only place that says it.
- The text of WAY-127 and the entry points still say only what Claude Code does; they do not say that Codex
  ignores the field. The remarks do not ask for it.

## Reaches beyond the handoff

None.

## Working copies

None made; `.runs/author-correction-1/` was not created. `.runs/author/` holds nothing.

## Unread material

- The record's other files (`cycle.md` and the rest) and the request's comment itself: not read; the remarks
  file gives its words.
- WAY-127 and the other entries were not re-read whole; only the lines the remarks touch were changed, and the
  texts of the change were searched for the claim about Codex.

## Searches not found or unclear

- A search of the files of the change (`*.md`, `*.py`, outside `.runs/`, `.claude/`, `.agents/`) for "hidden
  from the model", "offered", "offers the model", "not offered" and "never calls" found no text left that says
  the model is offered no skill in Codex. The 46 entry points and the 15 skill paragraphs say "Claude Code does
  not offer ... to the model", which I read as qualified.
- No source in the repository states the behaviour of Codex with the field (see the concern).
