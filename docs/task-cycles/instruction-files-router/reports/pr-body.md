The skill of `instruction-files` now gives the criterion for where a rule stands in `SKILL.md`, with the rules every kind of text shares. Each step names the one file it needs: one file per kind of text (main file, skill, path-scoped rule) and one per mode (judge, change, place, write). It judges skills too: each fragment of a skill is asked whether every use needs it or only one step or variant. Every verdict now shows when the rule is needed and whether the agent will recognize that moment. `principles.md` is gone; its content stands in those files.

Source: the task "Skill do plików instrukcji podaje przy każdym werdykcie kryterium miejsca reguły i ocenia także skille" (independent; `Status: ready for cycle`, 2026-10-28), frozen in the cycle record. Base `foundations` at `0b8c1bd`. Process pin: none — this is the-way itself (route of `agent-instructions/README.md`).

## Cycle

- Spec: none. The task's seven settlement rows and nine To do items settle every meaning. File names and the distribution of the old `principles.md` were the author's choices of how to make them.
- Route: one author without a plan, class `same` (Opus), because the change runs across five parts. Whole-change review by another agent: `PASS 634fa3b`. Return step: `524d9b8` corrected three places where the new text contradicted entries this change writes, and one more of the same kind. A fresh agent reviewed that step: `PASS 524d9b8`.
- Correction after review (Mariusz's remarks R1–R6, 2026-10-28): every rule of the skill now stands in one file only (WAY-258); the kind file is read before the mode's procedure is followed; the two dropped tool-documentation sources are cited again; the fact's scope is restored; leftover line breaks are reflowed. Review of the correction: `FAIL 44475cf` with two blocking findings — the correction lost WAY-133's second half (an instruction carries what the check cannot catch), and two restatements were left. The one fix `2ba7a47` met both and corrected two more of the same kind; its review: `PASS 2ba7a47`.
- Commits: `634fa3b` (change and foundation entries), `524d9b8` (return step), `44475cf` (correction), `2ba7a47` (fix of the correction's review). `8eec20a`/`f4bbf06` and the later pair only add and remove the cycle record. Please merge with a merge commit that keeps them; the record link below holds only then.

## What changed

- `instruction-files/SKILL.md`: the criterion ("Where a rule stands": when an agent needs a rule, and whether it will recognize that moment; reword the pointer's condition first, a whole rule in the main file only after recorded misses), shared rules, the conclusion on length that replaces "Length has no threshold", and the one-level rule with its new source. Its `description` now names skills, and the two entry points were regenerated.
- New files beside it, each named directly by the step that needs it: `kind_main_file.md`, `kind_skill.md`, `kind_path_rule.md`, `judging.md`, `changing.md`, `placing.md`, `writing.md`.
- `instruction-files/principles.md`: removed; every section lands in the files above. Its *Sources* list was dissolved into citations beside each principle.
- `instruction-files/check_instructions.py`: module docstring only (it pointed at section 6 of `principles.md`). The file is the part's trust boundary; the review confirmed that no handling of the files it reads changed.
- `product-guidelines/template.md:127`: points to where the rule on emphasis now stands.
- Words read at every use of the skill: about 5 900 now (`SKILL.md` + `tool_loading.md`), against 8 100 before, plus the mode's file and kind file at their step.

## What this request settles

- **WAY-256** (new; carries settlement row 1 and row 4 — the number for the lesson map) — Fragment skilla potrzebny tylko na jednym kroku albo w jednym wariancie stoi w pliku obok, który ten krok wskazuje (reguły wpisów zostają tam, gdzie kładzie je WAY-35), a `SKILL.md` trzyma obraz całości, zasady i odsyłacze; miarą jest to, czy krok fragmentu potrzebuje, nie liczba słów ani linii — dotyczy tego, co proponuje skill do plików instrukcji, i każdej zmiany skilla the way, która fragment dopisuje albo przeredagowuje.
- **WAY-257** (new; row 3 and the asking part of row 2) — Skill do plików instrukcji pyta przy każdej regule, kiedy agent jej potrzebuje i czy rozpozna tę chwilę, a każdy wiersz jego oceny, przy każdym werdykcie, pokazuje obie odpowiedzi.
- **WAY-258** (new; row 5) — Skill do plików instrukcji ma osobny plik na każdy rodzaj tekstu, wskazany przez krok, który nad tym rodzajem pracuje; reguła nie stoi w dwóch plikach, regułę wspólną kilku rodzajom trzyma `SKILL.md` (albo jeden plik wspólny, gdy takich reguł jest za dużo), a plik rodzaju nie odsyła do innego pliku.
- **WAY-128** (changed; rows 1 and 2) — Linia pliku ładowanego w każdej sesji może też nieść całą regułę czynności, ale dopiero gdy zapisy pracy pokażą, że agenci przegapili odsyłacz, którego warunek najpierw przeredagowano tak, jak spotykają tę chwilę; linie skilli procesu podlegają odtąd także WAY-256.
- **claude-skill-nested-references** (new environment fact; row 6) — Przewodnik Anthropic dla autorów skilli mówi, że Claude może przeczytać tylko część pliku, do którego prowadzi odsyłacz z innego pliku z odsyłaczem, i zaleca odsyłacze jeden poziom od `SKILL.md`.
- **instruction-density-accuracy** (changed environment fact; row 7) — Fakt mówi też, słowami badania, że trafność spada, gdy instrukcji naraz przybywa od 10 do 500, w trzech wzorcach (u dwóch najlepszych modeli dopiero po progu ok. 150 instrukcji).

Rows 1–5 of the task are one decision by intent. The log's form (one decision answers one question, WAY-19) split them into WAY-256, WAY-257, WAY-258 and the change to WAY-128.

Invariant tests altered: none. Surfaces altered: none. *Violated* marks set or cleared: none.

## Checks

- `python -B gate/run_tests.py` on `2ba7a47` (final tree), Windows — exit 0; 613 tests in 8 directories, every directory passed (5 platform skips in `instruction-files`). Also exit 0 on `634fa3b`, `524d9b8` and `44475cf`.
- `python -B elements/common/foundation_check.py` — exit 0, 0 errors (author and both reviewers).
- `python -B agent-instructions/skill_entry_points.py` — exit 0, entry points current.
- `python -B instruction-files/check_instructions.py . --file …` on the skill's files — exit 0; 0 errors, 5 `dead-path` warnings, all on example paths in the text.
- `git diff --check` — exit 0.

Not checked: no fresh agent session has used the rebuilt skill. Whether an agent follows the new route (reading the mode's file and the kind file at their step) is untested.

## Review findings not fixed

Minor findings, in the reviewers' words (full text in the reports linked from the record):

- Whole-change review, Minor 4 — "WAY-256 and the reading rule of WAY-125 are not reconciled": stage agents read "the method of its stage, and what it names, whole", which handoffs apply at the start. Read that way, moving step fragments beside a process skill cuts nothing. The reviewer recommends settling it in the task that rebuilds the process skills, or with a clause in WAY-125 (a change of meaning, the human's call). Left out of the correction on purpose.
- Correction review, M1 — "the rule on the words of a file narrows to one mode": the row "headings and wording taken from the principles — surroundings, way in, route, trigger | the words the file's readers use for the product" left *Mistakes* of `SKILL.md`; what remains is `writing.md:14-15`, for section names in the mode write only. "Restoring the point once in 'How to write a single rule' would cover every mode."
- Correction review, M2 — "'step 1' reads two ways": `judging.md:8-9` "the way step 1 searches session records" means `SKILL.md` § "1. Read", but the file's own numbered list starts at line 13; "as section '1. Read' searches session records" would match the other pointers.
- Correction review, M3 — `kind_skill.md:3-4` "is a sentence without a verb": "What is particular to skills — every skill, the skills of a process the repository works by included." E.g. "This file holds what is particular to skills — …".
- Correction review, M4 — "the emphasis citation widens and hardens its source": `SKILL.md:231-232` "piled-on emphasis makes a current model over-apply the rule"; the page says "piling on emphasis mostly makes Claude over-apply the rule". "mostly makes current Claude models over-apply the rule" keeps the source's reach.
- Review of the fix, M1 — "two items of the check-script list are hard to parse" (`SKILL.md:271-273`): "the pointing line the layout of files loaded with some files gives an `AGENTS.md` in a subdirectory" and "the pointer or copy the layout of skills gives a skill needed in Codex"; e.g. "an `AGENTS.md` in a subdirectory has the pointing line its layout gives". Wording only.

Fixed in this request: the whole-change review's Minor 1, 2 and 6 (return step, `524d9b8`), its Minor 3 and 5 and the return-step review's Minor 1–4 (correction `44475cf` and its fix `2ba7a47`).

Findings marked outside the task's scope:

- Correction review, O1 — "`tool_loading.md` repeats the positive control": `tool_loading.md:185-187` "One file in every variant must load — the positive control" and `judging.md:59` "always with a positive control, a file that must load". A rule of measurement, outside the remark R2 as worded; "Noted for the task that rebuilds the-way's skills."

## Questions

None.

## Other choices

13 other choices of the cycle stand in the questions table of the cycle record (`docs/task-cycles/instruction-files-router/cycle.md`, linked by the SHA of the commit that adds it).

## Human actions

None. Outside this request (task's *Out of scope*): after the merge, the lesson session points rows E16 and E17 of section s01e02 of the lesson map to **WAY-256**. The global copy (`the-way-global`) picks the change up the night after the merge.
