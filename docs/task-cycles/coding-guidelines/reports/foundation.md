# Foundation step — coding guidelines

## F1a

Author: foundation author A (general-purpose subagent, claude-opus-5-5), turn 1. Skill
`the-way-record-decision` (`elements/decisions/skill/SKILL.md` of this checkout). Worktree
`/home/user/the-way`, branch `claude/gallant-albattani-3k15lc`. Python 3.13.16 (the repository
declares 3.14; cycle choice O3).

**Status:** done. One commit, `a45956f`. No question needs the human.

### Inputs read

- Handoff `reports/foundation-handoff.md` (common part and "Stage F1a").
- Frozen task `task-frozen.md` whole: Q1–Q18, K1–K3, rows 1–25, *Decisions in play*, *Out of
  scope*.
- Spec `spec.md` whole (with §2, §8, §10); rulings C1–C21 `reports/design-rulings.md` whole; plan
  `plan.md` "Foundation entries" and "Foundation stages"; `cycle.md`; the passages of
  `reports/design.md` and `reports/spec-review.md` on WAY-167, WAY-168 and WAY-195.
- `agent-instructions/README.md`; `elements/decisions/skill/SKILL.md`, `elements/decisions/template.md`,
  `elements/decisions/examples.md` (WAY-03, read in the log), `elements/common/rules.md`,
  `elements/common/way_of_working.md`, all whole; `product-guidelines/template.md` whole.
- Foundation at `235b0b4` (= HEAD before the commit), by "Reading the foundation" (WAY-150):
  - part map whole. Touched parts: `product-guidelines` (all entries), `decisions` (the log),
    `invariants` (WAY-168, WAY-196, WAY-197 governance), `task-cycle` (WAY-197), `installation`
    (WAY-167's existing *Scope*), `gate` (WAY-168's new level 1 invariant).
  - *Scope* of all 178 decisions inspected by script; 151 name a touched part. Binding sentences of
    all 178 read (dump in the scratchpad). Read whole: WAY-167..WAY-192 (every `product-guidelines`
    decision), WAY-03, WAY-08, WAY-22, WAY-58, WAY-69, WAY-86, WAY-100, WAY-113, WAY-114, WAY-139,
    WAY-161, WAY-164.
  - invariants: `guidelines-*` (all eight), `gate-fork-point-evidence`, `invariant-test-break`,
    `level-one-decision-invariants`, `verification-invariant-derivation`.
  - glossary: every term and *Avoid* listed; whole entries of element, format guard, gate, clock,
    guidelines, invariant, invariant test, part, result, verdict, surface, debt, slice, user
    interface, binding part, binding sentence.
- Public sources of WAY-195, read on 2026-10-18 with curl 8.5.0, git 2.43.0 (a blob-less fetch of
  the commit, for its file list only) and pdftotext 24.02.0, each into its own scratchpad directory:
  Open Mercato at `4374c48def1654927805c4b760f0e7f8648280f2` — `AGENTS.md`,
  `packages/core/src/modules/customers/AGENTS.md`, `apps/mercato/src/modules/example/README.md`,
  `.github/workflows/audit.yml`, `.github/workflows/ci.yml`, `.ai/docs/agent-instructions.md`,
  `.ai/runs/2026-06-30-ts-morph-module-fact-sheets/PLAN.md`; the paper's public copy
  `https://storage.googleapis.com/gweb-research2023-media/pubtools/4365.pdf` (9 pages = CACM 61(4)
  pages 58–66). Nothing was taken from the task's private research; every quotation was checked
  by script, whitespace-normalised, against the downloaded text (all present; the two YAML-comment
  quotations span two comment lines, checked with the `#` markers removed).

### Entries written

| Entry | Meaning (pl, WAY-114) | Relations (fingerprints) | Verification | Fingerprint |
|---|---|---|---|---|
| WAY-167/1 edited in place | Wytyczne kodowania stoją w `guidelines/coding.md` (stali strażnicy, reguły całego kodu, tabela plików rodzajów z warunkiem, kiedy czytać każdy) i w `guidelines/coding-<rodzaj>.md` dla każdego rodzaju kodu ze wzorcem, z identyfikatorem rodzaju z decyzji, która wyznacza wzorzec. | derives from WAY-44@2f2b6227 · WAY-04@29a75d2c (unchanged) | level 1 `guidelines-check-kind-index` (new); level 2 with coding cases | `681d47ff` → `052adf27` |
| WAY-168/1 edited in place | Dla każdego niezmiennika, który reguła nazywa (poza niezmiennikiem formy wytycznych), dobry i zły przykład to całe pliki pod ścieżką produktu: metoda niezmiennika przechodzi z dobrym i oblewa ze złym (dla niezmiennika z listy naruszonych: dobry nie dodaje błędu, zły dodaje), a uruchamia się je tylko przy zmianie zdania niezmiennika albo przykładu, nigdy przy każdym uruchomieniu bramki. | unchanged | level 1 `guidelines-check-carrier` · `guidelines-check-example-files` (new) · `gate-guidelines-example-evidence` (new); level 2 | `47d9d53e` → `dc4a98a1` |
| WAY-193/1 | To, co niesie szablon wytycznych kodowania i co proponuje skill `maintain-coding-guidelines`, wiąże produkt dopiero decyzją produktu, która to przyjmuje; odejście tylko decyzją z uzasadnieniem. | derives from WAY-168@dc4a98a1 · WAY-100@e7a74a18 | level 2 | `1ae9ba7c` |
| WAY-194/1 | Skill wytycznych kodowania pyta człowieka o każdy wybór, także rekomendowany, pokazuje go przez skutek dla produktu, nigdy nazwami reguł lintera ani wartościami konfiguracji; pyta o decyzje, nie o pojedyncze reguły; tu wygrywa z WAY-114. | derives from WAY-113@d3e5cbfa · narrows WAY-114@04b4f599 | level 2 | `9b92a246` |
| WAY-195/1 | Wytyczne kodowania biorą z Open Mercato wzorzec wyznaczony decyzją z tabelą plików do kopiowania, status plików po audycie, audyt zależności zmiany wobec bazy i tabelę „praca → pliki do przeczytania”, a z badania Google blokadę tylko przy regule, której każde zgłoszenie prowadzi do wartej zmiany kodu, i miarę zgłoszenia; zostawiają resztę (wymienioną), w tym warunki Google „poprawność, nie styl” i „naprawa w całej bazie przed włączeniem” oraz próg 10% z przeglądu kodu. | derives from WAY-100@e7a74a18 | level 2 | `17cf3942` |
| WAY-196/1 | Każda reguła wytycznych kodowania ma co najmniej jeden niezmiennik — skrypt, a gdzie skrypt nie da rady, agent k z n, nigdy sędzia „czy nowy kod idzie za wzorcem”; reguła, której nikt nie sprawdzi, jest przykładem; tu wygrywa z WAY-168. | narrows WAY-168@dc4a98a1 · derives from WAY-08@2343e09f | level 1 `guidelines-check-carrier`; level 2 | `0e714a05` |
| WAY-197/1 | Zły przykład pisze autor wytycznych; to przypadek dodatkowy obok celowego złamania recenzenta, nigdy zamiast niego; do czasu bramki recenzent uruchamia też metodę z oboma przykładami. | derives from WAY-168@dc4a98a1 · WAY-69@7051f884 | level 3 (who wrote what) · level 2 | `44197f0a` |
| WAY-198/1 | Decyzja produktu wyznacza jeden plik wzorcowy dla rodzaju kodu (ścieżka i rodzaj w backtickach); to, co sprawdzi skrypt, staje się regułami z niezmiennikami, reszta wzorca jest przykładem. | derives from WAY-22@dcf291ea · WAY-193@1ae9ba7c | level 1 `guidelines-check-exemplar`; level 2 | `4dca82c6` |
| WAY-199/1 | Wskazanie innego pliku i zmiana reguły sprawdzanej ze wzorca to zmiany decyzji zatwierdzane jak WAY-172; edycja zachowująca te reguły nie wymaga zatwierdzenia; plik rodzaju podaje status (`exemplar`, `copy`, `do not copy`) przy ścieżce i decyzję przy wzorcu. | derives from WAY-172@45806b6e · WAY-198@4dca82c6 | level 1 `guidelines-check-exemplar`; level 2 | `9d0c758c` |
| WAY-200/1 | Bez plików danego rodzaju wzorzec wyznacza zadanie, które tworzy pierwszy; gdy produkt już je ma, skill ocenia każdy, porównuje i proponuje wzorzec ze statusem pozostałych, a decyzję zatwierdza człowiek. | derives from WAY-198@4dca82c6 | level 2 | `02f168d5` |
| WAY-201/1 | Audyt produktu z kodem kończy się propozycją wzorca dla każdego rodzaju z jednym zdaniem o zysku i plikami „do not copy” z `plik:linia` miejsca łamiącego regułę. | derives from WAY-200@02f168d5 | level 2 | `70344859` |
| WAY-202/1 | Szablon wymaga trzech stałych strażników — lintera, formatera i audytu zależności — a produkt odchodzi od każdego tylko decyzją z uzasadnieniem; wiążą od zadania wytycznych kodowania, które jest kompletne dopiero z decyzją przyjmującą albo odchodzącą dla każdego z trzech. | derives from WAY-193@1ae9ba7c | level 1 `guidelines-check-form`; level 2 | `e0fb6a51` |

Every new or changed entry: *Approved by* `Mariusz, merge of <request link>`; *Origin* `none`;
*Based on* `none` except WAY-195. *Review when*: WAY-197 `a gate of the-way reports for an
invariant how its method meets the uses of the rules that name it · check by: 2027-03-31` (C7);
all others `none`, as spec §8.2 gives them for WAY-193..WAY-202.

### Renewals (WAY-31)

`WAY-168@47d9d53e` → `@dc4a98a1` in WAY-171, WAY-173 and WAY-188, each read against the new binding
part: WAY-171 still holds (its four fields do not exclude the uses' files in a rule's body);
WAY-173 still holds (adoption is untouched); WAY-188 still holds (WAY-168 still lets a rule naming
its decision bind with `Invariant: none`, which WAY-188 narrows for the styleguide). Their own
fingerprints do not change (only *Relations* moved), so nothing further follows from them.
`guidelines-check-carrier/1`'s *Derives from* `WAY-168@47d9d53e` is **not** renewed here: it is an
invariant, renewed at F3 through `record-invariant` with its edit. WAY-167's old fingerprint
`681d47ff` is carried by nothing (checked by grep over the repository's `.md` and `.py` files).
A script over the whole log confirms that every relation fingerprint matches the current binding
part (0 stale).

### Search of the whole foundation (WAY-33)

Searched, at `235b0b4` and again on the written change: the binding sentences of all 178
decisions; the whole entries listed above; `foundations/invariants.md`, `glossary.md`,
`environment_facts.md`, `part_map.md` for: exemplar, standing check, lint, formatter, vulnerab,
advisor, false positive, false alarm, use that follows, use that breaks, deliberate break, test
case, reference implementation, kind of code, copy from, do not copy, audit of dependencies, Open
Mercato, Google, style; and the new text for glossary words used loosely (element, part, result,
verdict, surface, debt, slice, pattern, guard, checker, clock, watch, probe).

Found and settled:

- WAY-171, WAY-173, WAY-188 and `guidelines-check-carrier` carry WAY-168's fingerprint — renewed
  (decisions) or left to F3 (invariant), above.
- WAY-114 collides with WAY-194 — `narrows WAY-114` and the area stated, as WAY-174 does.
- WAY-168 collides with WAY-196 in the coding discipline — `narrows WAY-168`, area stated, as
  WAY-188 does.
- WAY-69, WAY-149, WAY-164, WAY-58, `invariant-test-break`, `gate-fork-point-evidence` — read
  against WAY-197 and WAY-168: the author's breaking use never replaces the reviewer's break; no
  change needed.
- WAY-61 ("a check fed input made up for it is the method of a sentence about that check") — the
  uses are run against the method as evidence about the check, never as the product invariant's
  method; WAY-168 says "run against that method", the gate invariant (F3) reports it. No change.
- WAY-65 — the uses' files stand in guidelines, not named by `data:`, so they are no invariant
  tests. No change.
- WAY-169 — references inside fenced code are not checked, so references inside the uses' files
  raise nothing. No change.
- WAY-161 — cited in WAY-195's rationale (a style remark, Minor, never blocks), as Q18 gives it.
- WAY-139 — its rejected "the list in a template alone" is WAY-202's ground; cited.
- WAY-04 ("a rule copied from it turns one into law") — WAY-198/WAY-200 rationale.
- WAY-82, WAY-63, WAY-128, WAY-171 — cited in WAY-195's rationale for what is left.
- WAY-179 uses "pattern" for a non-binding model; no entry of mine uses "pattern" outside
  quotations, so no `record-glossary-term` question arises here beyond F2's two terms.
- Glossary: loose uses fixed before the commit — "part of the rules" → "some of the rules"
  (WAY-196), "guards against" → "keeps that out" (WAY-197), "the audit's result" → "what the audit
  found" (WAY-201). "gate", "clock", "result" and "verdict" stand in their term meanings.
- Environment facts: none touched; WAY-195's citations are of a fixed commit and a published
  edition, which cannot stop being true, so none becomes a fact (WAY-90), as WAY-175 did.
- No collision needing a human.

### Choices I made (rejected way, cost if wrong)

1. **WAY-168 *Scope* gains `gate`** — its new level 1 invariant `gate-guidelines-example-evidence`
   lies in `gate`, and a gate task must find WAY-168 from its *Scope*. Rejected: Scope unchanged
   (spec silent). Cost if wrong: one extra decision selected for gate changes.
2. **WAY-168's three binding sentences**: the old two merged into the first with a semicolon, the
   uses as files with C19's relative reading in the second, the timing in the third (WAY-05's
   limit). The exempt invariant is named "the invariant of guidelines that checks their form"
   (= `guidelines-form`, C11), not "one checking the guidelines themselves", so the form check's
   identifier-based exemption and the decision agree. Cost if wrong: a reviewer reads
   `guidelines-reference-current` as exempt too — it is not.
3. **"use", not "test case", in binding sentences** — "test case" sits close to the glossary term
   "invariant test" (a file a check names as data); "use" is WAY-168's own word. F2 may still weigh
   "test case" for the template and the gate invariant. Cost: none for F1a.
4. **WAY-195 quotes only what I read in the public sources.** The spec's left list names three
   items I did not verify in a passage — agents' hooks, the evaluation harness of instructions —
   and they are **left out of WAY-195**; "fact sheets generated from the code" is named, from
   `PLAN.md:20`. Rejected: naming them unread (they come from the private research). Cost if
   wrong: a later agent could adopt hooks or an instruction-eval harness without a decision naming
   them as left; WAY-100 still requires a decision to adopt either.
5. **WAY-195 also leaves Google's code-review threshold** ("up to 10% effective false positives",
   page 62), from K1's rejected way. Rejected: leaving it unnamed (spec §8.3 lists only Q18's two).
   Cost if wrong: one clause more.
6. **The paper's wording.** The task's private research cites "**zero** effective false
   positives"; the public copy reads "produce no effective false positives (the analysis should
   never stop the build for correct code)" (page 62). WAY-195 quotes the paper; the meaning is the
   same. Note for the request, no question.
7. **WAY-195's binding sentences use plain words** for the effective false positive ("every report
   of which leads to a change of code worth making"; "whether it is technically right or not"),
   per C2; the term appears only in *Based on* quotations. F2 applies WAY-95 to WAY-203/WAY-204.
8. **WAY-200: "where it already holds files of that kind"** for the task's "gdy ma ich kilka", so
   a product with exactly one file of a kind is covered by the audit rather than by neither branch.
   Rejected: "several" literally (leaves the one-file product undetermined). Cost if wrong: a
   one-file product gets an audit proposal instead of waiting for a second file.
9. **WAY-198 binds "naming in backticks its path and the kind's identifier"** — what
   `guidelines-check-exemplar` (spec §5.2 item 4) reads off the designating decision's binding
   sentences; without it the level 1 invariant would check a form no decision sets. Cost if
   wrong: a longer sentence.
10. **WAY-202 "complete only once it holds…"** for Q17's "bez jednej z nich nie jest gotowe", since
    "ready" names the task's readiness for its cycle in the-way. Cost: none.
11. **WAY-197's level 3 for who writes the breaking use**, beside level 2, in WAY-69's form.

### Checks (Python 3.13.16; outputs in this directory)

| Command | Exit | Output | Result |
|---|---|---|---|
| `python3 -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none` | 1 | `foundation-F1a-guard-decisions.txt` | 8 errors (all expected, below), 17 warnings (5 pre-existing passed check-by dates as at baseline; 12 `merge of <request link>` placeholders, expected), 5 unchecked as at baseline |
| `python3 -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none` | 1 | `foundation-F1a-guard-invariants.txt` | 12 errors (all expected, below), 3 unchecked as at baseline |
| `python3 -B elements/glossary/format_guard.py foundations/glossary.md --base none --merge-onto none` | 0 | `foundation-F1a-guard-glossary.txt` | as baseline |
| `python3 -B elements/part-map/format_guard.py foundations/part_map.md --base none` | 0 | `foundation-F1a-guard-part-map.txt` | as baseline (the new *Scope* names are parts of the map) |
| `python3 -B gate/run_tests.py elements/decisions` | 1 | `foundation-F1a-tests-elements_decisions.txt` | 169 tests, 1 failure: `OwnLog.test_the_way_log_holds_no_error` (the guard's 8 expected errors) |
| `python3 -B gate/run_tests.py elements/invariants` | 1 | `foundation-F1a-tests-elements_invariants.txt` | 233 tests, 1 failure: `OwnFile.test_the_way_invariants_hold_no_error` (the guard's 12 expected errors) |
| `python3 -B gate/run_tests.py elements/glossary` | 0 | `foundation-F1a-tests-elements_glossary.txt` | 204 OK |
| `python3 -B gate/run_tests.py elements/part-map` | 0 | `foundation-F1a-tests-elements_part-map.txt` | 162 OK |
| `python3 -B gate/run_tests.py relation-model` | 0 | `foundation-F1a-tests-relation-model.txt` | 19 OK |
| `python3 -B gate/run_tests.py gate` (critical flows) | 0 | `foundation-F1a-tests-gate.txt` | 98 OK |
| `python3 -B gate/run_tests.py product-guidelines` (extra) | 0 | `foundation-F1a-tests-product-guidelines.txt` | 61 OK |

Not a pass of the full gate; relation fingerprints and `TODO` are `unchecked` with `--merge-onto
none` (checked by my own script instead: 0 stale).

### Expected reds, each by message

Until F1b writes WAY-203..WAY-212 (decisions guard, `log-reference-target`):
- `decisions.md:6541: the text names WAY-206, which does not exist`; `:6542 … WAY-212`;
  `:6547 … WAY-203`; `:6548 … WAY-204`; `:6550 … WAY-205` (WAY-195's binding sentences);
- `decisions.md:6610: *Rationale* names WAY-206` (twice) and `WAY-205` (WAY-195's rationale).

Until F3 writes the invariants (invariants guard, `level-one-decision-invariants`,
`verification-invariant-derivation`):
- `WAY-167 is in force and verified at level 1, but no entry of the file derives from it`; `the
  level 1 verification of WAY-167/1 names guidelines-check-kind-index, which is not an entry`;
- `WAY-168/1 names guidelines-check-example-files …` and `… gate-guidelines-example-evidence …,
  which is not an entry of the file`;
- `WAY-196 is in force and verified at level 1, but no entry of the file derives from it`;
- `WAY-198 …` and `WAY-199 …` (no entry derives; `guidelines-check-exemplar` not an entry);
- `WAY-202 is in force and verified at level 1, but no entry of the file derives from it`;
- `guidelines-check-form/1: the level 1 verification of WAY-202/1 names it, but its *Derives from*
  does not name WAY-202`;
- `guidelines-check-carrier/1: the level 1 verification of WAY-196/1 names it, but its *Derives
  from* does not name WAY-196`.

Not reported with `--merge-onto none` but stale until F3: `guidelines-check-carrier`'s *Derives
from* `WAY-168@47d9d53e` (now `dc4a98a1`).

### For later stages

- F2: the glossary terms "exemplar" and "standing check" are used throughout WAY-167, WAY-195..202;
  the conditional term of C2 is weighed on WAY-203/WAY-204 (F1b) — WAY-195 holds the meaning only
  in plain words and in quotations.
- F3: renew `guidelines-check-carrier`'s *Derives from* to `WAY-168@dc4a98a1` and add
  `WAY-196@0e714a05`; `guidelines-check-form` gains `WAY-202@e0fb6a51`; `guidelines-check-kind-index`
  derives from `WAY-167@052adf27` (and WAY-212); `guidelines-check-exemplar` from
  `WAY-198@4dca82c6` and `WAY-199@9d0c758c`; `guidelines-check-example-files` and
  `gate-guidelines-example-evidence` from `WAY-168@dc4a98a1`. Fingerprints are of this commit; F1b
  does not touch these entries.
- S1: `product-guidelines/template.md` "Where guidelines go" restates WAY-167 and must follow the
  edit (spec §3.1).
- Request: WAY-167 and WAY-168 change meaning and are shown for renewed acceptance (WAY-07); choice
  6 (the paper's wording) and choice 4 (two left items not named) are worth a line.

### Commit

`a45956f` — `docs(foundations): coding guidelines — edit WAY-167 and WAY-168, add WAY-193 to
WAY-202`. Changed: `foundations/decisions.md` (+497 −26). The message carries the WAY-33 search
record and the expected reds. Not pushed.

### Questions

None for the human. For the orchestrator: accept choices 1, 4, 5 and 8 above, or send them back.

## F1b

Author: foundation author B (fresh general-purpose subagent, claude-opus-5-5). Skill
`the-way-record-decision` (`elements/decisions/skill/SKILL.md` of this checkout). Worktree
`/home/user/the-way`, branch `claude/gallant-albattani-3k15lc`, base `a45956f` (F1a). Python 3.13.16
(the repository declares 3.14; cycle choice O3).

**Status:** done. One commit, `b03c5da`. No question needs the human.

### Inputs read

- Handoff `reports/foundation-handoff.md` (common part and "Stage F1b"); this file's F1a section,
  its choices (C28) and "For later stages".
- Frozen task `task-frozen.md` whole (Q1–Q18, K1–K3, rows 1–25, *Decisions in play*, *Out of
  scope*); spec `spec.md` whole (§2, §4.4, §8, §10 in particular); `reports/design-rulings.md` whole
  (C1–C21); plan `plan.md` "Foundation entries" and "Foundation stages"; `cycle.md` (choices and
  rulings C22–C29); passages of `reports/design.md` (§3 CQ6, §4, §8, revision) and
  `reports/spec-review.md` (I-2, Minors 4–7) on WAY-203..WAY-212.
- `agent-instructions/README.md`; `elements/decisions/skill/SKILL.md`, `elements/decisions/template.md`,
  `elements/decisions/examples.md` (WAY-03, read in the log), `elements/common/rules.md`,
  `elements/common/way_of_working.md`, all whole.
- Foundation at `a45956f`, by "Reading the foundation" (WAY-150). Touched parts:
  `product-guidelines` (all ten entries), `invariants` (WAY-205, WAY-206), `instruction-files`
  (WAY-212), `decisions` (the log). Read whole: WAY-167..WAY-202 (every `product-guidelines`
  decision, F1a's included), WAY-03, 04, 08, 12, 16, 22, 36, 38, 44, 51, 60, 61, 62, 63, 68, 69, 73,
  76, 80, 82, 86, 100, 107, 113, 114, 120, 122, 123, 128, 129, 130, 133, 136, 137, 138, 139, 161.
  Invariants: all eight `guidelines-*`, `gate-fork-point-evidence`. Glossary: every term and
  *Avoid* listed; whole entries of clock, debt, element, entry, format guard, gate, guidelines,
  invariant, invariant test, part, result, verdict, watch, probe, correction, mechanics, repository
  instruction file. Environment facts: headings (none on linters, formatters or audits). Part map:
  `product-guidelines` and the part names used in *Scope*.

### Entries written

| Entry | Meaning (pl, WAY-114) | Relations (fingerprints) | Verification | Review when | Fingerprint |
|---|---|---|---|---|---|
| WAY-203/1 | Reguła lintera blokuje zmianę tylko wtedy, gdy każde jej zgłoszenie na kodzie produktu prowadzi do zmiany kodu, którą warto zrobić — liczy się to, do czego zgłoszenie prowadzi, nie to, czy jest technicznie trafne; reguła, która dała choć jedno zgłoszenie bez takiej zmiany, nie jest regułą wytycznych, może stać wśród przykładów, a bramka jej nie uruchamia. | derives from WAY-202@e0fb6a51 | level 2 | none | `96f71a98` |
| WAY-204/1 | Skill dzieli zestaw lintera na reguły blokujące i przykłady z próbnego przebiegu na kodzie produktu, którego zgłoszenia ocenia agent, który tego kodu nie pisał; produkt bez kodu bierze reguły zalecane przez dokumentację narzędzia (blokują bez dowodu — słaby punkt); podział człowiek zatwierdza w decyzji przyjmującej zestaw, a regułę, na której później padnie zgłoszenie bez wartej zmiany, przenosi do przykładów zmiana tej decyzji zatwierdzona przez człowieka. | derives from WAY-203@96f71a98 | level 2 | pierwszy produkt bez kodu z regułami zalecanymi trafi na takie zgłoszenie albo scali dziesięć zmian bez niego · check by: 2027-03-31 | `f74de946` |
| WAY-205/1 | Gdy kod już łamie blokujące reguły lintera, skill proponuje pełny niezmiennik na liście naruszonych niezmienników do końca porządków i obok drugi, spełniony od pierwszego dnia: żaden plik nie ma więcej zgłoszeń niż na `{fork-point}`, a plik spoza `{fork-point}` nie ma żadnego (drugi znika, gdy pierwszy jest spełniony); formater wchodzi jednym przeformatowaniem całego kodu, bez drugiego niezmiennika. | derives from WAY-51@8bdac21a · WAY-60@6e862c88 | level 2 | none | `a0d255a1` |
| WAY-206/1 | Skill proponuje audyt zależności, który sprawdza zmianę i oblewa ją tylko wtedy, gdy wersja zależności wniesiona przez zmianę względem `{fork-point}` ma znaną podatność — wg bazy porad wskazanej w decyzji produktu, czytanej w chwili sprawdzenia — o progu ważności, który ustala ta decyzja („każda ważność” wśród dróg); dopóki zegar nie uruchamia niezmienników produktu, szablon nie niesie audytu całego drzewa zależności. | derives from WAY-202@e0fb6a51 · WAY-60@6e862c88 | level 2 | zegar uruchamia metody niezmienników produktu · check by: 2027-03-31 | `bc4a61b1` |
| WAY-207/1 | Szablon każe wytycznym kodowania mówić, że błąd jednego pliku poprawia się w tym pliku, nigdy wyłączeniem reguły lintera w całym produkcie ani zmianą wzorca dla tego pliku, a wyłączenie reguły w całym produkcie to zmiana decyzji przyjmującej zestaw, zatwierdzana przez człowieka jak w WAY-172. | derives from WAY-172@45806b6e · WAY-193@1ae9ba7c | level 2 | none | `243b0872` |
| WAY-208/1 | Skill proponuje wytyczne kodowania każdej części mapy produktu, która ma kod, także skryptom budowania i części małej, a plik ogólny wymienia te części w *Applies to*. | derives from WAY-193@1ae9ba7c | level 2 | none | `ed84e391` |
| WAY-209/1 | W produkcie bez kodu plik ogólny ze stałymi strażnikami powstaje przed pierwszym zadaniem, które pisze kod, a plik rodzaju — z zadaniem, które tworzy pierwszy plik tego rodzaju. | derives from WAY-193@1ae9ba7c | level 2 | pierwszy produkt z wytycznymi kodowania przed kodem scalił zadanie, które wniosło ten kod · check by: 2027-03-31 | `977f8982` |
| WAY-210/1 | Skill najpierw rozpoznaje części z kodem i to, co produkt ma (linter, formater, audyt, rodzaje kodu z plikami, nic) oraz czy ma wytyczne kodowania, i rozbudowuje to, co jest, zamiast stawiać drugie narzędzie obok; nowe narzędzie to pytanie zadania do człowieka, z domyślną rekomendacją narzędzia najczęściej używanego w technologii produktu według researchu ze źródłami. | derives from WAY-193@1ae9ba7c | level 2 | none | `f168ee97` |
| WAY-211/1 | Narzędzia stałych strażników i zestaw reguł lintera skill bierze z preferencji człowieka, a bez nich z researchu każdego strażnika ze źródłami ze stroną i wersją, z krytyką przed pokazaniem opcji człowiekowi (jak WAY-122), i powtarza research przy odświeżeniu lub rozszerzeniu wytycznych. | derives from WAY-122@b343277a · WAY-120@81f84997 | level 2 | none | `d70681ee` |
| WAY-212/1 | Główny `AGENTS.md` produktu, poza blokiem instalatora, wskazuje wytyczne kodowania jedną linią — ścieżką `guidelines/coding.md` z warunkiem „przed zmianą kodu” — i żadna jego linia nie wskazuje plików `guidelines/coding-<rodzaj>.md`; te wskazuje tabela pliku ogólnego, ścieżką z warunkiem, kiedy czytać. | derives from WAY-128@4dca37ca · WAY-129@1336c32b · WAY-167@052adf27 | level 1 `guidelines-check-kind-index`; level 2 for the pointer | none | `116bffdf` |

Every entry: *Change* new decision; *Approved by* `Mariusz, merge of <request link>`; *Origin*
`none`; *Based on* `none`. *Scope* `product-guidelines`, plus `invariants` for WAY-205 and WAY-206
and `instruction-files` for WAY-212 (spec §8.2).

### Renewals (WAY-31)

None: F1b changes no existing binding part. All relation fingerprints in the log match the current
binding parts (own script over the whole log: 0 stale). F1a's fingerprints for F3 are unchanged
(WAY-167 `052adf27`, WAY-168 `dc4a98a1`, WAY-196 `0e714a05`, WAY-198 `4dca82c6`, WAY-199
`9d0c758c`, WAY-202 `e0fb6a51`).

### Search of the whole foundation (WAY-33)

Searched, on `a45956f` and again on the written change: the text of every decision of the log for
lint, formatt, vulnerab, advisor, severit, false alarm/positive, trial run, recommended, suppress,
turn … off, whole tree, audit of dependencies / dependency audit, reformat, most used / widely used,
preference, `AGENTS.md`, worth making, scratch worktree; `foundations/invariants.md`,
`glossary.md`, `environment_facts.md`, `part_map.md` and `violated_invariants.md` for the same
words; my new text for glossary words used loosely (element, entry, result, verdict, surface, debt,
slice, pattern, guard, checker, clock, watch, probe, correction, mechanics, invariant test, quality
gate, reference). Every decision found read whole (list under "Inputs read").

Found and settled:

- WAY-195 (F1a) names WAY-203..WAY-206 and WAY-212 in its binding sentences and rationale — each
  meaning checked against what I wrote; WAY-195 attributes "whether it is technically right or not"
  to WAY-204, so WAY-204's binding sentence carries it as well as WAY-203's. Severity "every
  severity among the ways" (WAY-195 rationale) stands in WAY-206.
- WAY-190, WAY-183, WAY-184, WAY-185, WAY-186, WAY-178, WAY-191, WAY-192 — the styleguide's
  counterparts; cited in the rationales; no collision (different discipline). WAY-192 governs
  styleguides alone, so WAY-212 neither narrows nor is narrowed by it (spec §10).
- WAY-167 holds the table of kind files (C20); WAY-212 derives from it with its fingerprint, so a
  change of that table flags WAY-212.
- WAY-68 (flipping check), WAY-61 (same command every run), WAY-82 (the clock runs facts' methods
  only) — WAY-206 reads the database live, names both weak points and leaves WAY-68 unchanged (C10);
  its bounded clause and *Review when* name the clock.
- WAY-63 (no warning result) — WAY-203 cites it.
- WAY-86, WAY-76, WAY-73, WAY-60, WAY-191 — WAY-204's rationale states why one environment fact per
  edition of a set holds under WAY-76 and why WCAG differs (spec §4.4, review Minor 7).
- WAY-51, WAY-60 — WAY-205 derives from both, as WAY-190 does.
- WAY-172, WAY-114 — WAY-204's later move of a rule and WAY-207's turning a rule off are changed
  meanings of guidelines, approved before code under WAY-172 (which narrows WAY-114); no new
  collision.
- WAY-128, WAY-129, WAY-107, WAY-16, WAY-130, WAY-133 — WAY-212's pointer is a pointer with its
  condition, outside the installer's block, naming no command; consistent.
- WAY-122, WAY-120, WAY-137, WAY-138 — WAY-210/WAY-211 follow WAY-122's research and critique;
  WAY-137/138 concern a project's technology step, no collision.
- WAY-36 — WAY-206's clause bounded by the clock binds after the merge until then (spec §8.2 note).
- WAY-46 ("severity" of failure modes) and WAY-136 ("suppress") — other meanings, no link.
- Glossary: "clock", "gate", "debt", "result", "verdict" used in their term meanings; "patterns"
  only in "git's rule of path patterns" (WAY-76's example, git's meaning). "False alarm" is not
  used: the meaning stands in plain words in WAY-203/WAY-204 (C2). WAY-205's binding sentence says
  "already breaks the rules", as WAY-190 does, not "debt" (see choice 6).
- Environment facts: none touched; no fact is named (WAY-204's and WAY-206's predictions stand in
  *Review when*).
- Part map: the part `product-guidelines` holds the template and skill these decisions bind; F2's
  failure mode on blocking rules that flag sound code relates to WAY-203/WAY-204.
- No collision needing a human.

### Choices I made (rejected way, cost if wrong)

1. **WAY-212 derives from WAY-167@052adf27** besides WAY-128 and WAY-129 (spec lists only the two):
   WAY-212's second sentence speaks of the rows of WAY-167's table (C20), so a change of that table
   should flag it (WAY-31). Rejected: no relation (a reworded table in WAY-167 would not flag
   WAY-212). Cost if wrong: one relation to renew when WAY-167 changes.
2. **WAY-205 keeps WAY-190's "the second is withdrawn once the first holds"** — Q13 answers "linter
   jak w WAY-190", and WAY-190 says so. Rejected: leaving withdrawal unsaid (the companion invariant
   would outlive its purpose with no rule for it). Cost if wrong: a clause the row does not spell out.
3. **WAY-206's bounded clause**: "Until the clock runs the methods of a product's invariants, the
   template of the coding discipline carries no audit of the whole tree" — the spec's "no audit of
   the whole tree by the clock" written with the glossary's "clock", and the *Review when* names the
   same state (spec: "a gate or clock … runs a product's checks apart from a change"; the gate runs
   only a change's checks, by its term, so only the clock is named). Cost if wrong: the review waits
   for the clock alone.
4. **WAY-204's "one environment fact per edition" stays in *Rationale*** as spec §4.4 and the
   handoff give it; the binding force comes from WAY-86 and WAY-76, applied there. Rejected: a
   binding sentence (a meaning no row gives, and WAY-204 already holds three clauses). Cost if
   wrong: the assessment asks for it in a binding sentence of a decision the template cites.
5. **WAY-207 does not say "by changing its code"**: C3 keeps the suppression rule as template text
   citing WAY-203 and WAY-193, not a the-way decision, so WAY-207 stays at row 23's words. Cost: the
   review's reading that "in that file" might allow a per-file suppression remains for the template
   to settle (it does, by C3).
6. **"breaks the rules", not "debt", in WAY-205's binding sentence**, as WAY-190 words the same
   case; "debt" stands in its rationale. Cost if wrong: F2 or the critique may ask for the term in
   the binding sentence under WAY-97 (an editorial change of WAY-205, no dependent yet).
7. **WAY-203's binding sentence reads "stands as a rule … checked by an invariant that blocks a
   change breaking it"** for "blokujący niezmiennik dostają tylko…", and "no invariant checks it, so
   the gate does not run it" for "bramka jej nie uruchamia". Cost: none expected.
8. **WAY-205's heading** asks about "a linter and a formatter", since the audit's entry is WAY-206's
   (spec's question names all standing checks). Cost: none; the heading is not fingerprinted.

### Checks (Python 3.13.16; outputs in this directory, exit code on the last line)

| Command | Exit | Output | Result |
|---|---|---|---|
| `python3 -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none` | 0 | `foundation-F1b-guard-decisions.txt` | 0 errors; 27 warnings (5 pre-existing passed check-by dates as at baseline; 22 `merge of <request link>` placeholders, expected); 5 unchecked as at baseline |
| `python3 -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none` | 1 | `foundation-F1b-guard-invariants.txt` | 14 errors, all expected until F3 (below); 3 unchecked as at baseline |
| `python3 -B elements/glossary/format_guard.py foundations/glossary.md --base none --merge-onto none` | 0 | `foundation-F1b-guard-glossary.txt` | same as F1a |
| `python3 -B elements/part-map/format_guard.py foundations/part_map.md --base none` | 0 | `foundation-F1b-guard-part-map.txt` | same as F1a |
| `python3 -B gate/run_tests.py elements/decisions` | 0 | `foundation-F1b-tests-elements_decisions.txt` | 169 OK (F1a's red own-log test now passes) |
| `python3 -B gate/run_tests.py elements/invariants` | 1 | `foundation-F1b-tests-elements_invariants.txt` | 233 tests, 1 failure: `OwnFile.test_the_way_invariants_hold_no_error` (the guard's 14 expected errors) |
| `python3 -B gate/run_tests.py elements/glossary` | 0 | `foundation-F1b-tests-elements_glossary.txt` | 204 OK |
| `python3 -B gate/run_tests.py elements/part-map` | 0 | `foundation-F1b-tests-elements_part-map.txt` | 162 OK |
| `python3 -B gate/run_tests.py relation-model` | 0 | `foundation-F1b-tests-relation-model.txt` | 19 OK |
| `python3 -B gate/run_tests.py gate` (critical flows) | 0 | `foundation-F1b-tests-gate.txt` | 98 OK |
| `python3 -B gate/run_tests.py product-guidelines` (extra) | 0 | `foundation-F1b-tests-product-guidelines.txt` | 61 OK |

Not a pass of the full gate; relation fingerprints and `TODO` are `unchecked` with `--merge-onto
none` (checked by my own script instead: 0 stale).

### Expected reds, each by message

The decisions guard reports no reference to an unwritten decision (F1a's 8 errors are gone).

Until F3 (invariants guard, `level-one-decision-invariants`, `verification-invariant-derivation`):
F1a's 12 errors unchanged, plus two for WAY-212:
- `decisions.md:7237: WAY-212 is in force and verified at level 1, but no entry of the file derives
  from it`;
- `decisions.md:7237: the level 1 verification of WAY-212/1 names guidelines-check-kind-index,
  which is not an entry of the file`.

### For later stages

- F2: WAY-203 and WAY-204 carry the meaning of a report leading to no change of code worth making in
  plain words (C2); the glossary skill's WAY-95 test on them decides whether a term follows. Both
  use "standing check" (WAY-205 heading aside, WAY-208, WAY-209, WAY-210, WAY-211) and "exemplar"
  (WAY-207, WAY-209). Choice 6 (debt) is for F2's look as well. The failure mode "a blocking linter
  rule that gives false alarms" relates to WAY-203/WAY-204; its wording should follow C2.
- F3: `guidelines-check-kind-index` derives from `WAY-167@052adf27` and `WAY-212@116bffdf`.
- Request: no F1b entry changes an approved decision's meaning; WAY-206's two weak points (C10) and
  WAY-204's weak point (recommended rules blocking with no evidence) are worth a line for Mariusz.

### Commit

`b03c5da` — `docs(foundations): coding guidelines — add WAY-203 to WAY-212`. Changed:
`foundations/decisions.md` (+384 −0). The message carries the WAY-33 search record and the expected
reds. Not pushed.

### Questions

None for the human. For the orchestrator: accept choices 1, 2, 3 and 6 above, or send them back.

## F2

Author: foundation author B, resumed (turn 2). Skills `the-way-record-glossary-term`
(`elements/glossary/skill/SKILL.md`) and `the-way-update-part-map` (`elements/part-map/skill/SKILL.md`)
of this checkout, with their templates, `examples.md` and the common files. Base `b03c5da`; F1b
choices accepted provisionally (C30). Committed with F3 in `05e44b1` (see "Commit" under F3).

**Status:** done. No question needs the human.

### Inputs read

Handoff section "Stages F2 and F3"; spec §2, §8.5, §8.6; C2, C6, C11, C14, C18, C19; the glossary
template, skill and examples (`invariant`, `gate`, `foundation`); WAY-95, WAY-96, WAY-98, WAY-99
whole; the whole glossary; the part-map template (failure modes, scale) and skill; the part
`product-guidelines` and the map's flows; the uses of both terms listed by
`python3 -B elements/glossary/format_guard.py --uses <word>` (exemplar: every use in WAY-167,
WAY-194..WAY-201, WAY-207, WAY-209; standing check: 22 uses in WAY-167, WAY-194, WAY-202,
WAY-208..WAY-212), each read.

### Entries written

| Entry | Text | Meaning (pl, WAY-114) |
|---|---|---|
| glossary `exemplar` | "An exemplar is a file of a product that a decision of the product designates as the model after which later code of its kind is written." *Avoid:* reference implementation — same thing. *Not:* none | Wzorzec wdrożenia to plik produktu, który decyzja produktu wyznacza jako wzór, według którego pisze się kolejny kod tego rodzaju. |
| glossary `standing check` | "A standing check is a check that a tool makes of every change to a product's code for the whole of the product, rather than for one kind of code, as a linter, a formatter or an audit of dependencies does." *Avoid:* standing guard — same thing. *Not:* none | Stały strażnik to sprawdzenie, które narzędzie robi przy każdej zmianie kodu produktu dla całego produktu, a nie dla jednego rodzaju kodu — tak jak linter, formater albo audyt zależności. |
| part map `product-guidelines`, failure mode | "the form check passes a file of coding guidelines of a kind whose exemplar no decision designates — agents copy a file nobody approved — high — detected by guidelines-check-exemplar" | Skrypt formy przepuszcza plik rodzaju, którego wzorca nie wyznacza żadna decyzja — agenci kopiują plik, którego nikt nie zatwierdził; wysoka; wykrywa `guidelines-check-exemplar`. |
| part map `product-guidelines`, failure mode | "the skill proposes as blocking a rule of a linter's set that gives a report leading to no change of code worth making — the gate blocks sound code, and only a change of a decision lets it through — high — not detected" | Skill proponuje jako blokującą regułę lintera, której zgłoszenie nie prowadzi do wartej zmiany kodu — bramka blokuje dobry kod i przepuszcza go dopiero zmiana decyzji; wysoka; niewykrywane. |

The part keeps its sentence, files, *Depends on* and trust boundary; `product-guidelines/coding/**`
(the slices' new template and skill) is claimed by `product-guidelines/**`, and no other part
claims it.

### C2: the WAY-95 test

The plain-words meaning in WAY-203/WAY-204 is a phrase — a report that leads to no change of code
worth making, whether it is technically right or not — whose words ("report", "change of code",
"worth making", "technically right") carry the meanings a reader who knows the field gives them. No
word takes a meaning a reader would not give it, so WAY-95 asks for no entry, and **no third term
is written.** Also weighed and left without an entry: "kind" (plain, spec §2), "general file"
(WAY-208, WAY-209, WAY-212: read as `guidelines/coding.md` from WAY-167's text, plain), "trial run",
"advisory database", "use" (WAY-168's own word, already approved).

### Search of the whole foundation (WAY-33)

- Paraphrases of the new definitions in the binding parts and rationales of WAY-167..WAY-212
  ("model", "template for", "reference module/file", "check of the whole") — none outside quotations
  (WAY-195's quoted "reference module", "template"); WAY-198 and WAY-202 state what is required of
  the thing, using the term, so nothing is rewritten (WAY-95, WAY-97).
- *Avoid* candidates (spec §2) searched in `foundations/` and the elements' Markdown: "reference
  implementation", "standing guard", "baseline check", "template module", "reference file" have no
  use; "code guard" is rejected — WAY-126's rationale reads "the code guards it". "Baseline check"
  is left out (a reader may take it for the audit against a base); "pattern" cannot stand in
  *Avoid* (WAY-98: other uses).
- Terms against identifiers: "exemplar" reads unlike `guidelines-check-exemplar` (no equality with
  hyphens read as spaces); "standing check" matches no identifier.
- Part map: no flow or other failure mode touched; the first new mode names
  `guidelines-check-exemplar`, written in F3 of the same commit.

### Choices I made (rejected way, cost if wrong)

1. **"designates" stays in the definition of exemplar** (spec §2, review Minor 11): without it the
   entry would hold only the plain sense and have no ground (WAY-95). Weighed as a rule under WAY-96:
   a file nobody designates is no exemplar but a file an agent happened to copy, so the clause says
   what the word names, not a rule WAY-198 could change. Cost if wrong: the assessment calls it a
   rule.
2. **"required by the template" left out of standing check** — WAY-202 could change what the
   template requires while the word names the same checks, so it is a rule (WAY-96). The three are
   given as "as … does", which a fourth check would leave true.
3. **One *Avoid* word each** ("reference implementation"; "standing guard", the literal of "stały
   strażnik"); neither has a use. Cost: none.
4. **F2 and F3 in one commit**, since the failure mode's detecting invariant must exist for the
   part-map guard.

## F3

Skill `the-way-record-invariant` (`elements/invariants/skill/SKILL.md`), with its template,
`examples.md` (`decision-guard-overdue-review`, `return-step-record` read) and the common files;
WAY-56, WAY-57, WAY-58, WAY-61, WAY-62, WAY-69 read whole. I am the sentence author of every
invariant of this task; I wrote no check, no test and no code (WAY-69).

**Status:** done. No question needs the human.

### Entries

Method of the four `guidelines-check-*` entries below: `python -B gate/run_tests.py
product-guidelines --record .runs/product-guidelines-tests.jsonl`; *Part*: product-guidelines ·
decisions · invariants · part-map · elements-common · relation-model (as the other
`guidelines-check-*`); *Rests on* none; *Correction* none.

**`guidelines-check-carrier/1` — edited in place, version kept** (spec §8.5; pre-`main`, precedent
`guidelines-form` in `19d28f8`). Fingerprint `3b699a99` → `bde3cc86`; nothing carries the old one.
*Derives from*: WAY-168@47d9d53e → WAY-168@dc4a98a1, gains WAY-196@0e714a05 (WAY-188@73da8ecb,
WAY-189@a76a39fb kept). For the request (WAY-57), old and new sentence:

- old: The form check of guidelines, `product-guidelines/form_check.py`, reports as an error every rule under `## Rules` of a file `guidelines/<name>.md` whose *Decision* holds no decision number with the log's prefix followed by `@`, every such rule of a styleguide whose *Invariant* holds no identifier of the invariants file followed by `@`, and every decision the table of roles of a styleguide names that the rule `### Each role in its meaning` does not name, unless that rule is dropped.
- new: The form check of guidelines, `product-guidelines/form_check.py`, reports as an error every rule under `## Rules` of a file `guidelines/<name>.md` whose *Decision* holds no decision number with the log's prefix followed by `@`, every such rule whose *Invariant* holds no identifier of the invariants file followed by `@` in a file whose discipline's template requires an invariant in every rule, and every decision the table of roles of a styleguide names that the rule `### Each role in its meaning` does not name, unless that rule is dropped.
- pl: Skrypt formy zgłasza jako błąd każdą regułę bez decyzji z odciskiem, każdą regułę bez
  niezmiennika z odciskiem w pliku, którego szablon dyscypliny wymaga niezmiennika w każdej regule
  (dziś styleguide i wytyczne kodowania; wcześniej tylko styleguide), oraz każdą decyzję z tabeli
  ról styleguide'a, której nie nazywa reguła „Each role in its meaning”.

Checks citing it gain coding cases, so under WAY-57 this is a change of meaning, shown at the
merge, not a correction; with no main branch the version stays 1.

**`guidelines-check-form/1`** — sentence unchanged (`0ce1adc4`); *Derives from* gains
WAY-202@e0fb6a51.

| Identifier | Sentence | Derives from | Part | Method | Fingerprint | Meaning (pl) |
|---|---|---|---|---|---|---|
| `guidelines-check-kind-index/1` | The form check of guidelines, `product-guidelines/form_check.py`, reports as an error every file `guidelines/coding-<kind>.md` git lists that no row of the table under `## Kinds of code` in `guidelines/coding.md` names by its path in *File*, every row of that table whose *File* names no file git lists, whose *Kind* is not the `<kind>` of the file its *File* names or whose *When to read* is empty, and every file `guidelines/coding-<kind>.md` git lists where git lists no `guidelines/coding.md`. | WAY-167@052adf27 · WAY-212@116bffdf | as above | as above | `2a02b7c1` | Skrypt formy zgłasza plik rodzaju, którego nie wymienia tabela `## Kinds of code` pliku `guidelines/coding.md`, wiersz tej tabeli wskazujący plik, którego git nie zna, z *Kind* niezgodnym z nazwą pliku albo z pustym *When to read*, oraz plik rodzaju bez pliku ogólnego. |
| `guidelines-check-exemplar/1` | The form check of guidelines, `product-guidelines/form_check.py`, reports as an error every file `guidelines/coding-<kind>.md` whose table under `## Files of this kind` holds no row, or more than one, whose *Status* is `exemplar`, every row of that table whose *Status* is not `exemplar`, `copy` or `do not copy`, whose *File* is absolute, holds a `..` segment, a drive or a UNC prefix or names nothing git tracks, or which is not the `exemplar` row and whose *Decision* is not `—`, and every `exemplar` row whose *Decision* names no decision the log holds and has not repealed, or names one whose binding sentences, their whitespace collapsed, lack its *File* in backticks or the file's `<kind>` in backticks. | WAY-198@4dca82c6 · WAY-199@9d0c758c | as above | as above | `745ccafa` | Skrypt formy zgłasza plik rodzaju bez dokładnie jednego wiersza `exemplar`, wiersz ze statusem spoza listy, ze ścieżką niebezpieczną albo nieśledzoną przez git, wiersz inny niż wzorzec z decyzją, oraz wiersz wzorca, którego decyzja nie istnieje, jest uchylona albo w zdaniach wiążących nie podaje w backtickach ścieżki i rodzaju. |
| `guidelines-check-example-files/1` | The form check of guidelines, `product-guidelines/form_check.py`, reports as an error every rule under `## Rules` of a file `guidelines/<name>.md` whose *Invariant* names an invariant other than `guidelines-form` and whose text after its fields does not hold, for each such invariant, exactly one fenced block whose opening line's info string reads `good <identifier> <path>` and exactly one whose info string reads `bad <identifier> <path>`, `<identifier>` being that invariant's, and, in such a rule, every such block whose `<identifier>` its *Invariant* does not name or whose `<path>` is absolute, holds a `..` segment, a drive or a UNC prefix, every line inside such a block that would open a fence, every other fenced block, and every such block left open to the end of the file. | WAY-168@dc4a98a1 | as above | as above | `7389b884` | Skrypt formy zgłasza regułę, która nazywa niezmiennik inny niż `guidelines-form`, a nie ma dla niego dokładnie jednego bloku `good <identyfikator> <ścieżka>` i jednego `bad …`; w takiej regule także blok z obcym identyfikatorem albo niebezpieczną ścieżką, linię otwierającą płot wewnątrz bloku, każdy inny blok kodu i blok niezamknięty do końca pliku. |
| `gate-guidelines-example-evidence/1` | For every invariant entry that a rule of a file `guidelines/<name>.md` names with a file for the use that follows the rule and one for the use that breaks it, and whose sentence a change adds or alters against "{fork-point}" or one of whose two files the change alters, the gate's report states whether the entry's method, run on the commit checked with each file put in place at its path, passes with the first and fails with the second — for an entry on the list of violated invariants, whether the first adds no failure the commit does not already have and the second adds one — or that this could not be checked. | WAY-168@dc4a98a1 | gate · product-guidelines | `TODO` | `2d38e732` | Dla każdego niezmiennika, który reguła wytycznych nazywa z plikami dobrego i złego użycia, a którego zdanie albo jeden z tych plików zmiana dodaje lub zmienia, raport bramki mówi, czy jego metoda z dobrym plikiem przechodzi, a ze złym oblewa (dla niezmiennika z listy naruszonych: czy dobry nie dodaje błędu, a zły dodaje), albo że tego nie dało się sprawdzić. |

Every decision's level 1 identifier now stands in that invariant's *Derives from*: WAY-167, WAY-212
→ kind-index; WAY-168 → carrier, example-files, gate evidence; WAY-196 → carrier; WAY-198, WAY-199 →
exemplar; WAY-202 → check-form. My script: 0 stale fingerprints in the invariants' *Derives from*.

### Search of the whole foundation (WAY-33)

- Invariants, part map and facts for fence, info string, good, bad, exemplar, standing check,
  `Kinds of code`, `Files of this kind`: `guidelines-reference-current`,
  `guidelines-check-reference-target`, `guidelines-check-stale-reference` and
  `instruction-file-imports` read only outside fenced code, so references and paths inside the
  test-case blocks stay unchecked by them, as C12 intends — no change.
- `gate-fork-point-evidence/1` is the model of the gate invariant (Q12), unchanged;
  `invariant-test-break/1` unchanged (WAY-197); `guidelines-form/1` unchanged (C14).
- Decisions whose level 1 names a changed or new invariant: WAY-167, WAY-168, WAY-188, WAY-189,
  WAY-196, WAY-198, WAY-199, WAY-202, WAY-212 — each read against the sentence; the carrier's new
  wording still holds for the styleguide (WAY-188, WAY-189).
- Failure modes and flows naming these identifiers: only the new mode of F2. No collision.

### Choices I made (rejected way, cost if wrong)

1. **kind-index also reports a row whose *Kind* is not its file's `<kind>` or whose *When to read*
   is empty** — beyond spec §5.2 item 3 — so that WAY-212's level 1 covers its "with the condition"
   and §4.3's agreement of the table with the kind files. Rejected: the bare spec list (WAY-212's
   condition left to level 2 alone). Cost if wrong: S3 writes two more checks; the orchestrator may
   strike the clause before F4.
2. **exemplar reports a repealed designating decision** ("no decision the log holds and has not
   repealed"), following spec §5.3's crafted input and WAY-169's wording. Cost: none expected.
3. **The carrier's discipline condition is generic** ("a file whose discipline's template requires
   an invariant in every rule"), not a list of disciplines, as spec §8.5 gives it, so a third
   discipline needs no edit.
4. **The gate invariant speaks of "a file for the use that follows the rule and one for the use that
   breaks it"**, WAY-168's words, not "test case" (F1a choice 3), and quotes "{fork-point}" as
   `gate-fork-point-evidence` does (a sentence about a check, WAY-60, WAY-61).

### Checks (Python 3.13.16; outputs `foundation-F2F3-*.txt` in this directory, exit code last line)

| Command | Exit | Result |
|---|---|---|
| decisions guard `--base none --merge-onto none` | 0 | 0 errors, 27 warnings (5 old check-by dates, 22 `<request link>` placeholders), 5 unchecked |
| invariants guard `--base none --merge-onto none` | 0 | 0 errors, 3 unchecked as at baseline |
| glossary guard `--base none --merge-onto none` | 0 | 0 errors, 5 unchecked as at baseline |
| part-map guard `--base none` | 0 | 0 errors, 7 unchecked as at baseline |
| `gate/run_tests.py elements/decisions` | 0 | 169 OK |
| `gate/run_tests.py elements/invariants` | 0 | 233 OK (the own-file test, red since F1a, passes) |
| `gate/run_tests.py elements/glossary` | 0 | 204 OK |
| `gate/run_tests.py elements/part-map` | 0 | 162 OK |
| `gate/run_tests.py relation-model` | 0 | 19 OK |
| `gate/run_tests.py gate` (critical flows) | 0 | 98 OK |
| `gate/run_tests.py product-guidelines` | 0 | 61 OK |

No guard reports an error. Not a pass of the full gate: link fingerprints and `TODO` are unchecked
with `--merge-onto none` (my script: 0 stale), and nothing runs the new invariants' methods yet —
their checks are F4's and the form check's code the slices'; `product-guidelines` passes because no
check cites the new sentences yet. `gate-guidelines-example-evidence` stays `unchecked` (method
`TODO`).

### For later stages

- F4 (check author, not me): checks citing `guidelines-check-carrier/1`, `guidelines-check-form/1`,
  `guidelines-check-kind-index/1`, `guidelines-check-exemplar/1`,
  `guidelines-check-example-files/1`, from these sentences; choice 1 adds two kind-index cases.
- Request: the carrier's old and new sentence (above); the two terms and failure modes with their
  meanings; no third term (C2).

### Commit

`05e44b1` — `docs(foundations): coding guidelines — glossary terms, failure modes and invariants
(F2, F3)`. Changed: `foundations/glossary.md` (+14 −0), `foundations/invariants.md` (+43 −3),
`foundations/part_map.md` (+5 −0). The message carries the WAY-33 search record. Not pushed.

### Questions

None for the human. For the orchestrator: accept F3 choice 1 (two extra kind-index clauses) and F2
choice 1 ("designates" in the definition of exemplar), or send them back.

## Final-review fix (C38)

Author: foundation author A, turn 2. Finding I1 of `reports/final-review.md`: WAY-201's binding
sentence narrowed row 22 ("propozycją wzorca dla każdego rodzaju"; row 3, Q6). Base `2eabf42`.
Skill `the-way-record-decision`; WAY-201 edited in place (before `main`, WAY-07); every other clause
and field kept.

- Old: "The audit the skill `maintain-coding-guidelines` makes of a product that has code ends with a
  proposed exemplar for each kind of code it audits, each with one sentence of what the product gains
  by it, and with the files of that kind marked `do not copy`, each with the file and line of the
  place that breaks a rule."
- New: "The audit the skill `maintain-coding-guidelines` makes of a product that has code ends with a
  proposed exemplar for each kind of code the product holds files of, each with one sentence of what
  the product gains by it, and with the files of that kind marked `do not copy`, each with the file
  and line of the place that breaks a rule."
- Meaning (pl): Audyt produktu z kodem kończy się propozycją wzorca dla każdego rodzaju kodu, którego
  pliki produkt ma, każdą z jednym zdaniem o tym, co zyskuje produkt, oraz plikami tego rodzaju
  oznaczonymi „do not copy”, każdy z `plik:linia` miejsca, które łamie regułę.
- Fingerprint `70344859` → `d98d2f0e`. The old one was carried by no relation, guidelines file or code
  (grep over the repository outside `.git`; only the F1a table above names it). A script over the
  whole log finds no stale relation fingerprint. *Approved by* already reads
  `Mariusz, merge of <request link>`.

Checks (Python 3.13.16):

| Command | Exit | Output | Result |
|---|---|---|---|
| `python3 -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none` | 0 | `foundation-fix-guard-decisions.txt` | 0 errors; 27 warnings (5 pre-existing passed check-by dates, 22 `<request link>` placeholders); 5 unchecked as at baseline |
| `python3 -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none` | 0 | `foundation-fix-guard-invariants.txt` | 0 errors; 3 unchecked as at baseline |
| `python3 -B gate/run_tests.py elements/decisions` | 0 | `foundation-fix-tests-elements_decisions.txt` | 169 tests OK |

## Assessment settlement (I1)

Author: foundation author B, turn 3. Skill `the-way-record-decision`. Base `28b42a2`. Remark I1 of
`reports/assessment.md` read with `product-guidelines/coding/template.md:125-149, 225-236` and
WAY-204.

**Status:** done. One commit, `a677bc4` (`foundations/decisions.md` +12 −10). Not pushed. No
question needs the human.

### WAY-203/1, edited in place (row 7's meaning kept)

- old: A rule of a linter's set stands as a rule of a product's coding guidelines, checked by an
  invariant that blocks a change breaking it, only where every report it gives on the product's
  code leads to a change of code worth making, a report counting by whether it leads to such a
  change, whether it is technically right or not. A rule of the set that gives a report leading to
  no such change is no rule of the coding guidelines: it may stand among their examples, and no
  invariant checks it, so the gate does not run it.
- new: A rule of a linter's set stands among the rules that block a change in the product's
  decision adopting the set, and so is checked by the invariant of the one rule of the product's
  coding guidelines on its linter, only where every report it gives on the product's code leads to
  a change of code worth making, a report counting by whether it leads to such a change, whether it
  is technically right or not. A rule of the set that gives a report leading to no such change is no
  rule that binds the product's code: it may stand among the examples of the coding guidelines, and
  no invariant checks it, so the gate does not run it.
- pl: Reguła zestawu lintera stoi wśród reguł blokujących w decyzji produktu, która przyjmuje
  zestaw, i sprawdza ją niezmiennik jednej reguły wytycznych kodowania o linterze — ale tylko wtedy,
  gdy każde jej zgłoszenie na kodzie produktu prowadzi do zmiany kodu, którą warto zrobić (liczy się
  to, do czego prowadzi, nie techniczna trafność); reguła z choć jednym zgłoszeniem bez takiej zmiany
  nie wiąże kodu, może stać wśród przykładów, a bramka jej nie uruchamia.
- *Verification*: complies gains "stands among the rules that block in the decision adopting the
  set"; violates gains "each rule of the set that blocks stands as a rule of its own under
  `## Rules` of the coding guidelines".
- Fingerprint `96f71a98` → `45e40683`.

"is no rule of the coding guidelines" became "is no rule that binds the product's code", since under
the new first sentence no rule of the set is a rule of the guidelines; the meaning of row 7 ("nie
jest regułą") is kept. The heading `### Linter` is not named in the decision, so the template keeps
its heading free; the decision says "the one rule of the product's coding guidelines on its linter".

### Renewals (WAY-31)

WAY-204/1 `derives from WAY-203@96f71a98` → `@45e40683`, read against the new binding part: it
still holds (WAY-204's rationale already puts the blocking rules in the adopting decision); its own
fingerprint (`f74de946`) is unchanged. Nothing else carries `96f71a98` (grep over `.md` and `.py`
outside `.runs/`); no invariant derives from WAY-203. My script: 0 stale relations in the log.

### Search (WAY-33)

Every mention of WAY-203 in `foundations/` read against the new sentence: WAY-195 (blocking only by
a check every report of which leads to a change worth making — holds), WAY-204 (renewed), WAY-207's
rationale (a blocking rule gives no report leading to no change worth making — holds). The
template's citations of WAY-203 (`### Linter` invariant 1, inline suppressions) now agree with it.
No collision.

### Checks (Python 3.13.16; outputs in this directory, exit code last line)

| Command | Exit | Output | Result |
|---|---|---|---|
| `python3 -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none` | 0 | `foundation-assess-guard-decisions.txt` | 0 errors, 27 warnings (5 old check-by dates, 22 `<request link>` placeholders), 5 unchecked |
| `python3 -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none` | 0 | `foundation-assess-guard-invariants.txt` | 0 errors, 3 unchecked |
| `python3 -B gate/run_tests.py elements/decisions` | 0 | `foundation-assess-tests-elements_decisions.txt` | OK |
