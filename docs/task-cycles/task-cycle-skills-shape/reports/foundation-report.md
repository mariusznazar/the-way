# Report — foundation entries, task `task-cycle-skills-shape`

**Status:** done with concerns (one choice of wording in WAY-125 that the orchestrator should
confirm; see *Choices*).

## Files and commits

- `foundations/decisions.md` — +58 −26.
- Commit `40f0fd357deadc3818cfc77cf251c2a983db687f` on `task/task-cycle-skills-shape`, on base
  `cf11541f039649db3a76aa5aaa2d7cce2cc48f34`. Not pushed. Worktree clean after the commit.

Method read whole from the base copy: `.runs/the-way-base/task-cycle/change/SKILL.md`; the
foundation-step paragraph of `.runs/the-way-base/task-cycle/skill/SKILL.md:259-277`;
`.runs/the-way-base/elements/decisions/skill/SKILL.md` with `elements/decisions/template.md`,
`elements/decisions/examples.md`, `elements/common/rules.md` and `elements/common/way_of_working.md`
of the base copy.

## Entries

All three are changes of existing decisions, edited in place under their numbers (template,
"Changing a decision"). No new number, no withdrawn number. No invariant, glossary term,
environment fact or part-map entry written (handoff; confirmed by the search below).

### 1 — WAY-125 (row 1)

- Binding sentence now: "Each agent reads the `SKILL.md` of its stage's method whole, and a file the
  method names, one beside that `SKILL.md` included, only when the step or variant that names the
  file comes, while the orchestrator reads no method it does not conduct."
- Relations gain `derives from WAY-256`. Verification gains one complies and one violates example.
  Rationale states why (a fragment WAY-256 places beside a method would gain nothing if read at the
  start), where the gain is largest (variants not taken), and the named risk of a missed moment with
  WAY-257's second question against it. Rejected gains "reading the method and every file it names
  at the start".
- **Znaczenie (PL):** Agent etapu czyta w całości `SKILL.md` swojej metody, a każdy plik, który metoda
  wymienia — także plik obok skilla — dopiero wtedy, gdy przychodzi krok albo wariant, który ten plik
  wymienia; orkiestrator nadal nie czyta metod, których sam nie prowadzi.

### 2 — WAY-127 (row 2)

- Binding sentence now: "An entry point reads its skill, and each file the skill names when the step
  that names that file comes rather than all of them at the start, from the checkout or worktree the
  session works in — …". The rest of the entry's binding part is unchanged (one line reflowed).
- Relations gain `derives from WAY-256`. Verification gains a pair for when an entry point has the
  files read; `invariants: skill-entry-points` stays. Rationale and Rejected gain one clause each.
- **Znaczenie (PL):** Plik wejściowy skilla the way każe czytać plik wymieniony przez skill z tego
  samego checkoutu albo worktree dopiero wtedy, gdy przychodzi krok, który go wymienia — nie
  wszystkie pliki naraz na starcie.

### 3 — WAY-256 (row 3)

- The exception is written into the second binding sentence (the template allows three binding
  sentences and wants a foreseen exception in them): "a fragment of one step or variant that is one
  instruction, which would otherwise stand in a file beside the skill, stays in `SKILL.md` where its
  pointer would stand, since the pointer is an instruction too; beyond that, a fragment's place
  follows from …".
- Verification gains one complies and two violates examples (a file holding one instruction behind a
  pointer; several short instructions kept as "each is short" — the loophole the source note names).
  Rationale gains the reason and the countable boundary (one instruction against one pointer).
  Rejected gains "every fragment moved out, one instruction included".
- **Znaczenie (PL):** Fragment kroku albo wariantu, który jest jedną instrukcją i inaczej stałby w
  pliku obok skilla, zostaje w `SKILL.md` w miejscu, w którym stałby odsyłacz do niego, bo odsyłacz
  też jest instrukcją; fragment z więcej niż jedną instrukcją nie zostaje tylko dlatego, że każda jest
  krótka.

## Search of the whole foundation (WAY-33)

Searched `foundations/*.md` for `WAY-125`, `WAY-127`, `WAY-256`, and for "files it names", "what it
names", "method of its stage", "whole", "beside", "pointer", "entry point", "one instruction",
"at that step", "step names"; read each entry found whole.

Inside the foundation (the writer's):

- WAY-148 (derives from WAY-125): "The handoff names what the agent reads, as the orchestrator selects
  it (WAY-150, WAY-213)" concerns foundation and guideline material, not the method's files. No
  restatement of "what it names, whole". No change.
- WAY-150: "every other agent of the cycle reads what its handoff names" — foundation material; "the
  whole reading of templates, rules and examples keep their domain" agrees, since an element skill
  names its template at its step 1. No change.
- WAY-213: guideline files are read whole when a handoff names them — other files than a method's.
  No collision. No change.
- WAY-35: element skills read the template and shared part "from there" — read at the step that names
  them. The new WAY-256 wording limits the exception to fragments that would otherwise stand beside
  the skill, so a one-instruction rule of an element's entries still goes to its template. No change.
- WAY-258 (derives from WAY-256): "such a rule stands in its `SKILL.md`, or in a file a step names as
  WAY-256 gives" — consistent with the exception. No change.
- WAY-128: "the lines of process skills and their entry points answer to WAY-35, WAY-127 and WAY-256
  instead" — still true. No change.
- WAY-257: now cited by WAY-125's rationale. No change.
- Invariant `skill-entry-points` (derives from WAY-127): requires the entry point to lead the session
  to `SKILL.md` in its checkout or worktree; says nothing of when the files are read. Still holds; no
  change, as the task's *Context* says.
- Environment fact `claude-skill-nested-references` (no written link): Claude may read a file reached
  through another referenced file only in part. An entry point is itself a skill file pointing to the
  real `SKILL.md`, which points to the files beside it — two levels. This held before the change
  too; the changed entries do not rest on the fact and do not contradict it, so no link and no
  change. Flagged as a risk for the slices' judgments, not a question.
- Glossary: no entry for "fragment", "pointer", "variant", "entry point" or "method"; the entries
  use them in the meaning WAY-256 and WAY-127 already use. Nothing for `record-glossary-term`.
- No collision between decisions with precedence missing (WAY-25) found.

Outside the foundation (the slices' work; nothing changed):

- `AGENTS.md:10-11` — "each reads its skill and the files it names from the checkout or worktree" —
  Slice 2 (named by the plan as `:9-11`).
- `agent-instructions/skill_entry_points.py:175-176` — "read the files it names under the same root"
  — Slice 2; its test `agent-instructions/test_skill_entry_points.py:53` — Slice 2.
- Every generated entry point, e.g. `.claude/skills/the-way-make-change/SKILL.md:13` and
  `.agents/skills/the-way-make-change/SKILL.md:13` (21 directories under each) — Slices 2–6 by
  regeneration.
- `instruction-files/kind_skill.md:13-14` — "only one step or one variant needs it — it stands in a
  file beside the skill" has no one-instruction exception — Slice 1.
- `task-cycle/skill/SKILL.md:68-69` — "Each stage agent reads the method of its stage, and what it
  names, whole" — Slice 11.
- `task-cycle/skill/SKILL.md:132-133` — the foundation/return-step handoff "which the agent reads
  whole, with the element skills it names" — Slice 11.
- Not named by the plan, checked and found consistent: `task-cycle/plan/SKILL.md:116` and `:170`
  ("*Read* is the whole reading of the slice's agent") concern the passages of task, spec and plan,
  not the method's files; a reader of Slice 9 may still want to keep that sentence from being read
  as "nothing outside *Read*, the method's step files included". `instruction-files/SKILL.md:22`
  ("the files it names lie beside this `SKILL.md`") says where, not when. No other text found.

## Checks

- `python -B elements/common/foundation_check.py` — exit 0 ("0 errors"). Positive control: with
  `derives from WAY-9999` put into WAY-125 for a moment it reported
  "`WAY-9999` names no decision of the log", exit 1; restored, exit 0.
- `git diff --check` — exit 0.
- `python -B -m pytest -q elements/common/test_foundation_check.py` — exit 0 (90 passed); it tests the
  checker on fixtures, so it says nothing about these entries beyond the script still working.
- Not run: `gate/run_tests.py` — the orchestrator's run (handoff, WAY-160).
- Binding sentences counted by hand: WAY-125 two, WAY-127 three, WAY-256 three (template: one to
  three).

## Own-work check

- Requirement most likely missed: row 3's meaning colliding with WAY-35 (a one-instruction rule of an
  element's entries kept in an element skill's `SKILL.md`). Check: read WAY-35 against the new WAY-256
  sentence. Found the first draft ("a fragment of one step or variant that is one instruction stays
  in `SKILL.md`") would have collided; narrowed it to fragments "which would otherwise stand in a file
  beside the skill". The row's meaning — the pointer it replaces implies a file beside — is kept.
- Second: that WAY-127's change still lets `skill-entry-points` hold. Read the invariant whole: it
  constrains where the entry point leads, not when files are read. Holds.

## Choices

- **WAY-125 covers every file the method names, not only one beside it.** Row 1 says "plik obok
  skilla"; *To do* 1 says `implement-task` stops telling stage agents to read at the start "wszystko,
  co metoda wymienia". The stage methods also name files elsewhere (`product-guidelines/reading.md`
  in `plan-task` and `review-change`, `elements/common/way_of_working.md` in `review-change`). Removing
  "and what it names, whole" with only files beside covered would leave those unruled, and row 2
  (entry points) already speaks of every file the skill names. Rejected: "a file beside the skill"
  alone — its cost if this was wrong: the entry says more than the row by those few files, which the
  orchestrator can narrow with a one-word edit. Recommendation: keep; confirm that *To do* 1 carries
  it, or narrow.
- **WAY-127 says "step", not "step or variant"**, as row 2 does; a variant is chosen at a step, so
  nothing is lost.
- **`derives from WAY-256` added to WAY-125 and WAY-127** as the link the search finds: both changes
  serve where WAY-256 places fragments. Not precedence.
- **WAY-256's exception is narrowed to fragments that would otherwise stand beside the skill**, see
  the own-work check.

## Reaches beyond the handoff

- WAY-33, WAY-13 heading, WAY-213 (whole) and `foundations/glossary.md` headings — for the WAY-33
  search and the collision check.
- `foundations/environment_facts.md` entries `claude-skill-nested-references`,
  `single-rule-compliance`, `claude-code-project-skills` — to see whether the changed entries rest
  on or contradict them.
- Base copy `task-cycle/{spec,plan,change,review}/SKILL.md` grepped for the files they name — to
  decide the WAY-125 choice above.
- Plan lines 1–24 and greps of the plan for "WAY-125", "beside", "whole" — to see what Slices 2 and
  11 expect of the entries.

## Problems

None observed.
