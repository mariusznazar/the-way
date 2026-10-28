The skill of `instruction-files` now gives the criterion for where a rule stands in `SKILL.md`, with the rules every kind of text shares. Each step names the one file it needs: one file per kind of text (main file, skill, path-scoped rule) and one per mode (judge, change, place, write). It judges skills too: each fragment of a skill is asked whether every use needs it or only one step or variant. Every verdict now shows when the rule is needed and whether the agent will recognize that moment. `principles.md` is gone; its content stands in those files.

Source: the task "Skill do plików instrukcji podaje przy każdym werdykcie kryterium miejsca reguły i ocenia także skille" (independent; `Status: ready for cycle`, 2026-10-28), frozen in the cycle record. Base `foundations` at `0b8c1bd`. Process pin: none — this is the-way itself (route of `agent-instructions/README.md`).

## Cycle

- Spec: none. The task's seven settlement rows and nine To do items settle every meaning. File names and the distribution of the old `principles.md` were the author's choices of how to make them.
- Route: one author without a plan, class `same` (Opus), because the change runs across five parts. Whole-change review by another agent: `PASS 634fa3b`. Return step: `524d9b8` corrected three places where the new text contradicted entries this change writes, and one more of the same kind. A fresh agent reviewed that step: `PASS 524d9b8`.
- Commits: `634fa3b` (change and foundation entries), `524d9b8` (return step). Please merge with a merge commit that keeps them; the record link below holds only then.

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

- `python -B gate/run_tests.py` on `524d9b8` (final tree), Windows — exit 0; 613 tests in 8 directories, every directory passed (5 platform skips in `instruction-files`). Also exit 0 on `634fa3b`.
- `python -B elements/common/foundation_check.py` — exit 0, 0 errors (author and both reviewers).
- `python -B agent-instructions/skill_entry_points.py` — exit 0, entry points current.
- `python -B instruction-files/check_instructions.py . --file …` on the skill's files — exit 0; 0 errors, 5 `dead-path` warnings, all on example paths in the text.
- `git diff --check` — exit 0.

Not checked: no fresh agent session has used the rebuilt skill. Whether an agent follows the new route (reading the mode's file and the kind file at their step) is untested.

## Review findings not fixed

Minor findings, in the reviewers' words (full text in the reports linked from the record):

- Whole-change review, Minor 3 — "two tool-documentation sources disappeared with the *Sources* list of `principles.md`": `https://code.claude.com/docs/en/best-practices` and `https://learn.chatgpt.com/guides/best-practices` now stand nowhere in `instruction-files/` or the facts. Principles that rested on them, e.g. "Matching by description fails in two situations" (`instruction-files/SKILL.md`), show no source.
- Whole-change review, Minor 4 — "WAY-256 and the reading rule of WAY-125 are not reconciled": stage agents read "the method of its stage, and what it names, whole", which handoffs apply at the start. Read that way, moving step fragments beside a process skill cuts nothing. The reviewer recommends settling it in the task that rebuilds the process skills, or with a clause in WAY-125 (a change of meaning, the human's call).
- Whole-change review, Minor 5 — "reflow leftovers": a short line in WAY-128 *Rejected* ("stand today — every"), and `instruction-files/check_instructions.py:4` at 123 characters.
- Return-step review, Minor 1 — `instruction-files/SKILL.md:88-89`: "the step now reads the kind file after the mode's procedure is followed". Suggested: "Read in full the mode's file and the file of each kind of file the mode works on …, then follow the mode's file."
- Return-step review, Minor 2 — "the move puts rules into two files, against WAY-258": `placing.md:12-13` vs `SKILL.md:253-255` (search for an existing rule and replace it); `changing.md:5` vs `SKILL.md:236-238`; `placing.md:8-11` vs `SKILL.md:117` and `:180-182` (the WAY-133 mechanism list); `judging.md:32-35` vs `SKILL.md:244-247` (WAY-130 threshold). The fix: the mode file names the `SKILL.md` section instead of restating it.
- Return-step review, Minor 3 — `instruction-files/placing.md:5-7`: "'A rule with neither is not placed' reads against the wrong antecedent and drops the threshold from the step's own text"; suggested "none of these" and keeping "found more than once" or relying on the pointer alone.
- Return-step review, Minor 4 — `instruction-files/SKILL.md:144-147`: the citation of `single-rule-compliance` "still leaves out the fact's scope" (Claude Code sessions); add "in Claude Code sessions" after "target annotation".

The whole-change review's Minor 1, 2 and 6 were contradictions of entries this change writes, so the return step corrected them in `524d9b8`.

Findings marked outside the task's scope: none.

## Questions

None.

## Other choices

12 other choices of the cycle stand in the questions table of the cycle record (`docs/task-cycles/instruction-files-router/cycle.md`, linked by the SHA of the commit that adds it).

## Human actions

None. Outside this request (task's *Out of scope*): after the merge, the lesson session points rows E16 and E17 of section s01e02 of the lesson map to **WAY-256**. The global copy (`the-way-global`) picks the change up the night after the merge.
