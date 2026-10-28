# Author report — instruction-files-router

**Status:** `done with concerns`

**Commit:** `634fa3b` — Give the skill of instruction files its criterion, a file per kind of text and the
judging of skills (on `task/instruction-files-router`, base `0b8c1bd`).

## Files changed (added / removed lines)

| File | + | − |
|---|---|---|
| `instruction-files/SKILL.md` | 215 | 55 |
| `instruction-files/judging.md` (new) | 107 | 0 |
| `instruction-files/kind_main_file.md` (new) | 53 | 0 |
| `instruction-files/kind_skill.md` (new) | 28 | 0 |
| `instruction-files/kind_path_rule.md` (new) | 12 | 0 |
| `instruction-files/principles.md` (deleted) | 0 | 316 |
| `instruction-files/check_instructions.py` (module docstring only) | 2 | 2 |
| `product-guidelines/template.md` | 1 | 1 |
| `foundations/decisions.md` | 131 | 12 |
| `foundations/environment_facts.md` | 8 | 2 |
| `.claude/skills/the-way-maintain-instruction-files/SKILL.md` (generated) | 1 | 1 |
| `.agents/skills/the-way-maintain-instruction-files/SKILL.md` (generated) | 1 | 1 |

All files LF, as before (`git ls-files --eol`); new files written LF.

## Checks run

| Command | Exit |
|---|---|
| `python -B gate/run_tests.py instruction-files` | 0 (104 tests, OK, 5 skipped) |
| `python -B gate/run_tests.py agent-instructions` | 0 (18 tests, OK) |
| `python -B elements/common/foundation_check.py` (after each foundation edit and before commit) | 0 ("0 errors") |
| `python -B agent-instructions/skill_entry_points.py` (before `--write`) | 0, reported "would change" both entry points of `the-way-maintain-instruction-files` |
| `python -B agent-instructions/skill_entry_points.py --write` | 0, changed those two files |
| `python -B agent-instructions/skill_entry_points.py` (after, and before commit) | 0, "entry points are current" |
| `python -B instruction-files/check_instructions.py . --file instruction-files/SKILL.md --file instruction-files/judging.md --file instruction-files/kind_main_file.md --file instruction-files/kind_skill.md --file instruction-files/kind_path_rule.md` | 0 — 0 errors, 5 warnings, all `dead-path` on example paths (`.claude/rules/`, `x/AGENTS.md`, `.the-way/instruction-files/SKILL.md`, and `_zadania\` in the root `AGENTS.md`); the same kind of example paths stood in `principles.md` and `SKILL.md` before |
| `git diff --check` | 0 |

Not run: the full gate (`python -B gate/run_tests.py` without a directory) — the orchestrator's, as the
handoff says. The two focused test runs were made before the last two Markdown-only edits (removing
two rows of the *Mistakes* table of `SKILL.md` and one sentence of `kind_main_file.md`); no test reads
those files. No test was written: the change is prose and one docstring, which per `make-change` §2
gets no test.

## Own-work check (WAY-164)

Requirement most likely not met: To do 1 / row 5 — "między plikami nie ma powtórzeń, a plik rodzaju
nie odsyła do innego pliku", for the new files of the skill (now also WAY-258).

Check: a script listed every sentence over 40 characters (normalised) standing in two of
`SKILL.md`, `judging.md`, the three kind files and `tool_loading.md`, and every `.md` name in
backticks in `judging.md` and the kind files. Result: no sentence repeated across files; the `.md`
names in the kind files are the files under judgement (`AGENTS.md`, `CLAUDE.md`, `SKILL.md`,
`x/AGENTS.md`), none an instruction to read another file of the skill. A reading for repetitions in
other words found three: the *Mistakes* table of `SKILL.md` restated two rules of the main file
(repository description, repeating the README) and `kind_main_file.md` said twice that `@path` is
no pointer; I removed the two rows and the duplicate sentence. The control of the script is weak: I
did not run it on a planted duplicate.

## Reaches beyond the handoff

- `elements/common/way_of_working.md`, `elements/common/rules.md`, `elements/decisions/template.md`,
  `elements/decisions/examples.md`, `elements/environment-facts/template.md` — read whole, because the
  two element skills' step 1 names them.
- `foundations/decisions.md` WAY-21 (based on `instruction-density-accuracy`), WAY-167 rationale (cites
  WAY-128), and a grep of the log for rules on what a skill holds — the WAY-33 search.
- `agent-instructions/test_instruction_files.py` (head) and `test_check_instructions.py` (grep) — to
  see whether any test reads `principles.md` or the skill's text; none does.
- `README.md:105–130` — whether its description of `instruction-files/` stays true; it does.
- The Wayback CDX index for the Anthropic page, to pick the closest existing archived copy
  (20261022015600), as the environment-facts skill asks.

## Choices, each with the option rejected

1. **Files and names.** `kind_main_file.md`, `kind_skill.md`, `kind_path_rule.md` beside `SKILL.md`.
   Rejected: `skills.md`/`skill.md` (too close to `SKILL.md`; the `skill-entry-points` invariant
   counts files named `SKILL.md`, and a case-insensitive filesystem makes `skill.md` risky); a
   `kinds/` subdirectory (no gain, deeper path). Cost if wrong: renames only.
2. **`judging.md` — a fifth file, for the judge mode.** The handoff lists the distribution as
   `SKILL.md`, kind files and a shared file only if row 5's condition holds; it also says
   `SKILL.md` is bound by the new criterion for what I add or reword. The judging-only principles
   (typical defects, judging in operation, when to remove, mechanisms that clean up) and the reworded
   judge procedure (row 3's rows) are needed only in one variant (mode judge), so by WAY-256 they
   stand beside, named by the Judge step. Rejected: keeping them in `SKILL.md`'s Judge section
   (breaks the criterion the change writes, for fragments it rewords). Cost if wrong: a reviewer or
   Mariusz sees a file the task did not name; folding it back is a move of text. **This is the main
   concern**: please confirm or reject it at review.
3. **No shared file.** Row 5's condition does not hold: work on one kind reads its kind file plus
   rules common to all kinds, not mostly rules of other kinds.
4. **Distribution of `principles.md`:**
   - to `SKILL.md`: § 3 (criterion table, splitting, a rule leaving its file) and § 2's three
     conditions as "Where a rule stands", with the recognition question and its rewording rule
     (row 2) and the length conclusion (To do 6); § 1 whole except its main-file bullet ("Ways in
     and routes", with the one-level rule now citing the new fact, To do 7); § 4's intro, the two
     layers every kind shares and three shared pitfalls ("One layout for three tools"); § 5 whole;
     § 7 "When to add a rule"; § 6's mechanical checks ("What the check script settles");
   - to `kind_main_file.md`: § 2 (definition, three kinds of content, what it does not hold, global
     file), § 1's main-file bullet, § 4's main-file and global-file rows and the `@path` and
     `CLAUDE.local.md` pitfalls;
   - to `kind_skill.md`: § 3's paragraph on skills, the new per-fragment question (To do 2,
     WAY-256), § 4's skills row;
   - to `kind_path_rule.md`: § 4's row for rules of parts of the code;
   - to `judging.md`: the judge procedure from `SKILL.md` (rows now show the criterion, To do 4),
     § 6 static and in operation (minus mechanical checks and the main-file line), § 7 "When to
     remove" and "Mechanisms that clean up" (the "edit replaces the sentence" bullet reduced to its
     instruction-to-agents part, since § 5 already holds the rule);
   - the "Sources" list is dissolved: each fact and study is cited where its principle stands; tool
     documentation stays in `tool_loading.md`.
   Rejected: keeping `principles.md` as a shared file (it would be read whole at every use, which the
   task's answer to the router question removes).
5. **Place/Write/Change sections stay in `SKILL.md`** with only their section references updated and
   Place step 2 pointed at the two questions. Rejected: moving each mode to its own file now — the
   rebuild of skills by the new criterion is Out of scope; those fragments stand unchanged in meaning.
6. **Decision split (WAY-19).** Rows 1–5 became: WAY-256 (rows 1 and 4 — one question: where a
   fragment of a skill stands and by what measure), WAY-257 (row 3, with the asking part of row 2),
   WAY-258 (row 5), and a change to WAY-128 (row 2's placement case, row 1's last sentence).
   Rejected: one entry for rows 1–5 — it answers four questions (WAY-19); five entries — rows 1 and 4
   answer one question. **Row 1 is carried by WAY-256** (the number for the map of the lesson).
7. **Row 2 and WAY-130.** Row 2 lets a rule stand whole in the main file "gdy zapisy pracy pokażą,
   że agent przegapił już przeredagowany odsyłacz — ten sam próg dowodu, którego WAY-130 wymaga".
   WAY-128's new clause says "once records of agents' work show they missed the reworded pointer";
   putting the rule whole into the main file is adding a rule, so WAY-130's "more than once" applies
   by itself, and `SKILL.md` says so. No number is written into WAY-128.

## Foundation entries written or changed

- **WAY-128** (changed) — Linia pliku ładowanego w każdej sesji może też nieść całą regułę czynności,
  ale dopiero gdy zapisy pracy pokażą, że agenci przegapili odsyłacz, którego warunek najpierw
  przeredagowano tak, jak spotykają tę chwilę; linie skilli procesu podlegają odtąd także WAY-256.
- **WAY-256** (new) — Fragment skilla potrzebny tylko na jednym kroku albo w jednym wariancie stoi w
  pliku obok, który ten krok wskazuje (reguły wpisów zostają tam, gdzie kładzie je WAY-35), a
  `SKILL.md` trzyma obraz całości, zasady i odsyłacze; miarą jest to, czy krok fragmentu potrzebuje,
  nie liczba słów ani linii — dotyczy tego, co proponuje skill do plików instrukcji, i każdej zmiany
  skilla the way, która fragment dopisuje albo przeredagowuje.
- **WAY-257** (new) — Skill do plików instrukcji pyta przy każdej regule, kiedy agent jej potrzebuje
  i czy rozpozna tę chwilę, a każdy wiersz jego oceny, przy każdym werdykcie, pokazuje obie
  odpowiedzi.
- **WAY-258** (new) — Skill do plików instrukcji ma osobny plik na każdy rodzaj tekstu, wskazany
  przez krok, który nad tym rodzajem pracuje; reguła nie stoi w dwóch plikach, regułę wspólną kilku
  rodzajom trzyma `SKILL.md` (albo jeden plik wspólny, gdy takich reguł jest za dużo), a plik
  rodzaju nie odsyła do innego pliku.
- **claude-skill-nested-references** (new fact) — Przewodnik Anthropic dla autorów skilli mówi, że
  Claude może przeczytać tylko część pliku, do którego prowadzi odsyłacz z innego pliku z
  odsyłaczem, i zaleca odsyłacze jeden poziom od `SKILL.md`.
- **instruction-density-accuracy** (changed fact) — Fakt mówi też, słowami badania, że trafność
  spada, gdy instrukcji naraz przybywa od 10 do 500, w trzech wzorcach (u dwóch najlepszych modeli
  dopiero po progu ok. 150 instrukcji).

Mapping of *Settlements to record*:

| Row | Entry |
|---|---|
| 1 | WAY-256 (carries row 1); WAY-128's last sentence changed |
| 2 | WAY-128 (first sentence gains the case); the asking part in WAY-257 |
| 3 | WAY-257 |
| 4 | WAY-256 |
| 5 | WAY-258 |
| 6 | `claude-skill-nested-references` (named in WAY-258's *Based on*) |
| 7 | `instruction-density-accuracy` (named in WAY-256's *Based on*) |

The WAY-33 search: WAY-192, WAY-212, WAY-245 and WAY-167 cite WAY-128 for pointers and knowledge
needed now and then — unchanged by the new clause. WAY-21 rests on `instruction-density-accuracy` and
still holds. WAY-133 rests on `single-rule-compliance`, unchanged. WAY-35 and WAY-256 do not collide:
WAY-256's binding sentence leaves to WAY-35 the rules and way of working it places. WAY-125 ("reads
the method of its stage, and what it names, whole") fits a step file read when its step comes. No
glossary term, invariant or part-map entry needed a change: the part map's `instruction-files`
sentence (principles, loading account, skill, script) still matches the files.

## Problems observed

- **The saving is small in a full judgement.** Words read per use before: `SKILL.md` 1926 +
  `principles.md` 3933 + `tool_loading.md` 2246 = 8105. After: `SKILL.md` ~4030 + `tool_loading.md`
  2246, plus `judging.md` 1289 and one kind file (161–592) when judging — about 8000 for judging one
  kind, about 6600 for placing or writing. The gain is in the instructions the agent meets at each
  step, not in words, which is what the task's answer on length expects, and its stated weak point.
- **WAY-212 vs the one-level rule (preexisting, not changed):** WAY-212 leads a product's agent from
  `AGENTS.md` to `guidelines/coding.md` and from its table to `guidelines/coding-<kind>.md` — two steps,
  which the one-level principle the skill now cites a source for advises against. WAY-258 binds only
  the skill of `instruction-files`, so nothing collides; it may be worth a question later.
- The handoff names the distribution targets without a mode file; see choice 2.
