# Foundation stage report — foundation author

Handoff: [foundation-handoff.md](foundation-handoff.md). Worktree
`C:/Storage/repos/the-way-wt/product-guidelines-styleguide`, branch
`task/product-guidelines-styleguide`, base `96623ed7710100fe6e11a0ce3c052fc44d4af52d`.
Skill: `elements/decisions/skill/SKILL.md` with `elements/decisions/template.md`,
`elements/decisions/examples.md` (WAY-03), `elements/common/rules.md`,
`elements/common/way_of_working.md`, read whole.

## Turn 1 — F1a

### Reading

- Read whole: frozen task (`task.md`, 27 rows), `spec.md`, `plan.md`, `cycle.md` (C1–C26),
  `agent-instructions/README.md`, `elements/common/rules.md`, `elements/common/way_of_working.md`,
  the decision skill, template and examples, `reports/design.md`, `reports/foundation-selection.md`,
  `reports/research-outside_sources.md`, spec-review findings 10–24.
- Foundation at `96623ed` (WAY-150): `foundations/decisions.md` read whole (WAY-01 … WAY-166, every
  entry); `foundations/glossary.md` and `foundations/part_map.md` read whole;
  `foundations/invariants.md` — every heading, the six WAY-09 dependants (`:146-202`) and every
  invariant whose sentence names templates, instruction files, approval, language, directories or
  `README.md` (searched, read whole where hit); `foundations/environment_facts.md` — every heading
  and `context-file-effect`.
- Touched parts: `decisions` (new entries, WAY-09/27/38 edits); prospective new part
  `product-guidelines` (in every *Scope* written; not yet in the map — F2). Scope selection: the
  design stage's complete *Scope* inspection (152 of 152 decisions) holds at `96623ed`; nothing
  changed on `foundations` since.

### Entries written or changed (commit `2181273`)

| Entry | Lines | Row / source | Relations (fingerprint recomputed) | Verification | Review when |
|---|---|---|---|---|---|
| WAY-09/1 (edit in place) | 234-316 | spec §2.1, root C10 | none | level 1 (six invariants) + level 2, gains `product-guidelines/` and a complying case | none |
| WAY-27/1 (*Scope* only) | 775-805 | spec §2.1, finding 21 | none | unchanged | unchanged |
| WAY-38/1 (*Scope* only) | 1114-1143 | spec §2.1, finding 21 | none | unchanged | unchanged |
| WAY-167/1 = G1 | 5439-5486 | row 1; C7 | derives from WAY-44@2f2b6227 · WAY-04@29a75d2c | level 2 | none |
| WAY-168/1 = G2 | 5487-5528 | row 2 | derives from WAY-22@dcf291ea · WAY-18@8c477ea2 | level 1 `guidelines-check-carrier` + level 2 | none |
| WAY-169/1 = G3 | 5529-5570 | row 3 | derives from WAY-02@3ffcbd46 · WAY-31@a14c616c | level 1 `guidelines-reference-current` · `guidelines-check-reference-target` · `guidelines-check-stale-reference` + level 2 | none |
| WAY-170/1 = G4 | 5571-5604 | row 4 | derives from WAY-04@29a75d2c · WAY-16@5c1d60d4 | level 1 `guidelines-form` · `guidelines-check-form` · `guidelines-check-code-path` + level 2 | none |
| WAY-171/1 = G26 | 5605-5656 | finding 24 (autonomous language rule) | derives from WAY-168@47d9d53e | level 1 `guidelines-form` · `guidelines-check-form` + level 2 | first product writing guidelines' text in another language merges a change to a restated decision · check by 2027-03-31 |
| WAY-172/1 = G5 | 5657-5700 | rows 24, 27 (approval before code); C19 | derives from WAY-30@6924312f · WAY-125@f3e6afcf · narrows WAY-114@04b4f599 | level 2 | a merged change of a product uses on a screen a meaning no decision carries · check by 2026-12-31 |
| WAY-173/1 = G6 | 5701-5735 | row 26 | derives from WAY-168@47d9d53e · WAY-100@e7a74a18 | level 2 | none |
| WAY-174/1 = G24 | 5736-5770 | rows 23, 27 (asking with a recommendation) | derives from WAY-113@d3e5cbfa · narrows WAY-114@04b4f599 | level 2 | none |
| WAY-175/1 = G25 | 5771-5833 | WAY-100 (*Decisions in play*), spec §9.1 | derives from WAY-100@e7a74a18 | level 2 | a product settles how an agent sees its screens and keeps a kitchen-sink page · check by 2026-12-31 |

Numbers: G1→167, G2→168, G3→169, G4→170, G26→171, G5→172, G6→173, G24→174, G25→175 (order of
writing; turn 2 continues at WAY-176 for G7–G23). New binding fingerprints: WAY-09 `ce6bd9c0` (was
`909e9c5c`), WAY-167 `681d47ff`, WAY-168 `47d9d53e`, WAY-169 `e2fb088c`, WAY-170 `c1b230d2`,
WAY-171 `2bc38c05`, WAY-172 `45806b6e`, WAY-173 `c423105b`, WAY-174 `c916835f`, WAY-175
`3174b1f3`. WAY-27 `fb27e458` and WAY-38 `6e10c3fd` unchanged (only *Scope* changed).

*Approved by* of every new entry and of WAY-09 reads `Mariusz, merge of <request link>`; WAY-27 and
WAY-38 keep `Mariusz, merge of https://github.com/mariusznazar/the-way/pull/8` and `Mariusz,
2026-09-26`, since their binding sentences and meaning are unchanged (a *Scope* widening makes the
decision findable for the new part; WAY-38 already covers every script of the-way).

### Meaning sentences for the request (Polish)

- **WAY-09** (zmiana znaczenia, do ponownej akceptacji, WAY-07): repozytorium the way ma nowy katalog
  `product-guidelines/` — szablon wspólny dla wytycznych każdego produktu, szablony dyscyplin, dla
  których the way daje szablon, ze skillem prowadzącym pracę nad nimi, oraz skrypt sprawdzający
  formę wytycznych z testami; katalog nie wejdzie na gałąź główną, zanim tego nie zawiera.
- **WAY-27, WAY-38** (bez zmiany znaczenia): decyzje o odsyłaczach poza repozytorium i o skryptach
  w Pythonie z samą biblioteką standardową obejmują też nową część `product-guidelines`.
- **WAY-167:** wytyczne produktu pisze się ręcznie, poza fundamentem, w katalogu `guidelines/` w
  korzeniu repozytorium — plik na dyscyplinę, a styleguide jako plik na każdy interfejs użytkownika,
  nazwany identyfikatorem części mapy, która ten interfejs rysuje; katalog należy do części, która
  kieruje pracą agentów.
- **WAY-168:** wiążąca reguła wytycznych wskazuje po identyfikatorze decyzję z dziennika produktu i
  niezmienniki, które ją sprawdzają, i mówi, co i jak robić, z przykładem dobrego i złego użycia;
  uzasadnienia i odrzucone warianty stoją tylko w decyzji, a to, co nie wskazuje ani decyzji, ani
  niezmiennika, jest przykładem, nie regułą.
- **WAY-169:** odsyłacz wytycznych do decyzji albo niezmiennika niesie odcisk wiążącego brzmienia
  wpisu, a zmiana, po której odcisk się nie zgadza albo wpis nie obowiązuje, trafia na gałąź główną
  dopiero wtedy, gdy ta sama zmiana poprawi wytyczne i odcisk.
- **WAY-170:** formę wytycznych i ich odsyłacze sprawdza przed scaleniem skrypt the way według
  szablonów z commita, którego używa repozytorium, a produkt z wytycznymi ma niezmienniki, których
  metody go uruchamiają, więc odpala go bramka.
- **WAY-171:** każdy plik wytycznych ma te same nagłówki i sekcje w stałej kolejności, reguły z polami
  *Decision*, *Invariant*, *Good*, *Bad*, w „Where in code” tylko ścieżki, a porzuconą wymaganą część
  — `none —` z decyzją produktu; słowa struktury są po angielsku, reszta w języku produktu, a reguła
  szablonów the way zmienia się tylko z decyzją the way, którą cytuje.
- **WAY-172:** nowe albo zmienione znaczenie w wytycznych to decyzja produktu, którą człowiek
  zatwierdza przed kodem, który jej używa — w dokumencie zadania albo przy zablokowanym projekcie
  requestu; użycie istniejącego znaczenia i zmiana wartości bez zmiany znaczenia nie wymagają
  zatwierdzenia; w tym obszarze decyzja ma pierwszeństwo przed WAY-114.
- **WAY-173:** treść szablonu styleguide'a i propozycje skilla wiążą produkt tylko przez jego własną
  decyzję przyjmującą, a produkt odchodzi od nich tylko własną decyzją z uzasadnieniem; decyzje the
  way o szablonie wiążą szablon i skill, nie ekrany produktu.
- **WAY-174:** skill styleguide'a pyta człowieka o każdy wybór, także tam, gdzie ma rekomendację, i
  pokazuje go przez to, co zobaczy użytkownik, a nie przez nazwy i wartości tokenów, tłumacząc
  prostymi słowami pojęcia dziedziny; w tym obszarze decyzja ma pierwszeństwo przed WAY-114.
- **WAY-175:** the way przejmuje z lekcji kursu i skilla `10x-ui` oraz ze skilli `om-ux-setup` i
  `om-ux-shape` wymienione elementy (tokeny nazwane rolą, para tło–tekst, audyt dwukierunkowy, stany,
  strona „kitchen sink”, reguła w pliku instrukcji, opis ekranów przez to, co widzi użytkownik itd.),
  a pomija ich polecenia, listy narzędzi, moment pracy po pierwszym ekranie, porównanie zrzutów (do
  powrotu, gdy produkt będzie miał drogę agenta do ekranów i stronę „kitchen sink”) i nazwę roli
  `surface`.

### Whole-foundation search (WAY-33) for these entries

Searched: every entry of `foundations/decisions.md` (read whole, WAY-01…WAY-166), the whole glossary
and part map, the invariants (headings; sentences matching translat/English/language/guid/style/
screen/user interface/README/approv/template/instruction file/directory, read whole where hit) and
the environment facts (headings, `context-file-effect`). Findings and how each was settled:

1. **WAY-04** (closed list; a hand-written document beside the map violates) — guidelines hold no
   rule of their own and point to code: link `derives from` in WAY-167 and WAY-170; the rationale of
   WAY-167 and WAY-171 says why no copy of derivable state is made.
2. **WAY-18, WAY-22** — one log; a choice is a decision: links in WAY-168.
3. **WAY-52** (rules generated for agents from the part map; rule files by hand rejected as a copy)
   — near-collision: a styleguide restates meanings of decisions scoped to its part. Settled: the
   human rejected a script-composed extract (task *Context*); guidelines carry what entries do not
   (how to apply, uses, pointers) and their restated meanings are held to the decisions by WAY-169;
   written into WAY-167 *Rejected*. No relation.
4. **WAY-114** (agent writes on recommendation; asks only without one) — collides with rows 24 and
   27: `narrows WAY-114` in WAY-172 (area: new or changed meanings of guidelines) and WAY-174 (area:
   the styleguide skill's questions). WAY-114's last clause "a translation never enters the
   foundation" meets WAY-171's language rule: settled in WAY-171's rationale (guidelines are outside
   the foundation; the decision stays the one binding wording; drift of a translation is caught by no
   fingerprint — the price shown at the request).
5. **WAY-134** (cycle writes kept rows; blocked draft where a meaning cannot hold) — no collision
   with WAY-172, which covers a meaning the task did not settle at all.
6. **WAY-30, WAY-125** — approval before code; reserved decisions open a blocked draft request:
   links in WAY-172.
7. **WAY-113, WAY-123** — how an agent asks; choices shown by consequences: WAY-174 derives from
   WAY-113, WAY-123 named in its rationale.
8. **WAY-02, WAY-31** — fingerprints and renewal: links in WAY-169; bare mentions stay unflagged.
9. **WAY-16** — one command, checks from methods: link in WAY-170 (the form check runs through
   invariants' methods; no lint command of a product's own).
10. **WAY-34, WAY-100, WAY-86** — WAY-173 derives from WAY-168 and WAY-100 (spec proposed WAY-34;
    see choice 3); WAY-34 named in its rationale; WAY-86 is the analogue for WCAG (turn 2, G22).
11. **WAY-108, WAY-72** — WAY-171's language rule follows WAY-108's split by analogy; WAY-72 binds
    the foundation only. Named in the rationale, no relation.
12. **WAY-128, WAY-130** — an instruction file leads to guidelines as knowledge needed now and then
    (WAY-167 rationale); a rule carrying a recorded decision is WAY-130's exception (WAY-168
    rationale).
13. **WAY-35, WAY-05** — templates' rules cite their decisions: carried into WAY-171's third
    sentence for the-way's templates of guidelines.
14. **WAY-09** — edited in place; its only incoming fingerprinted links are the six invariants
    (`grep "WAY-09@"`: `foundations/invariants.md:152-202`), renewed in F3; no decision relates to it.
15. **Glossary**: "foundation" (record of the rules) — guidelines hold no rule of their own, so they
    are outside it as WAY-167 says; to recheck when the term "guidelines" is written (turn 3).
    "repository instruction file" — a styleguide named from `AGENTS.md` becomes one, consistent with
    WAY-167. "surface" — kept out of role names (WAY-175). *Avoid* words "checker", "quality gate"
    not used. The singular "guideline" not used anywhere (it would be a second meaning of the term).
    "view", bare "token", bare "interface", "domain" not used in the new entries.
16. **Environment facts** — none holds a condition of these entries; `context-file-effect`
    (overviews do not help) does not apply: guidelines are instructions read on a condition.

Unlinked effects found that need another stage: none beyond F2/F3 work already planned.

### Choices, with evidence and cost if wrong

1. **WAY-27/WAY-38 approvals kept** — binding sentences and meaning unchanged; only *Scope*. Cost if
   the root rules a *Scope* widening a change of meaning: two *Approved by* lines become
   `merge of <request link>`.
2. **WAY-167 *Scope* adds `installation`** (spec: `product-guidelines` only) — the installer's product
   guidance names `guidelines/` (spec §8, S8), so a later change there finds this decision. Cost: one
   more decision selected for installer changes.
3. **WAY-173 derives from WAY-168 and WAY-100, not WAY-34** (spec proposed WAY-34) — the task's
   rejected option for row 26 rests on row 2 ("sprzeczne z wierszem 2"), and adoption of an offered
   practice by a decision naming it is WAY-100's rule; WAY-34 says which commit's decisions bind, not
   that every decision of the-way binds a product. Cost if wrong: one relation rewritten.
4. **WAY-170 also derives from WAY-16** — its second sentence relies on the gate taking checks from
   invariants' methods. Cost: a flag on WAY-170 if WAY-16 changes, which is what is wanted.
5. **WAY-172 also derives from WAY-125** (blocked draft route) and its *Scope* adds `project-level`
   and `task-cycle` — the approval happens in the task document (`refine-task`) and the stop in the
   cycle; the "cycle for view changes" task touches both parts and must find WAY-172. Cost: more
   decisions selected for those parts.
6. **WAY-172 sentence 2 includes "a value changed with its meaning kept takes no approval"** — root
   C23 (R1); placed here rather than in G9 (turn 2) so one question has one answer (WAY-19). G9 will
   refer to it, not restate it.
7. **WAY-171 sentence 3 binds the-way's templates of guidelines to cite their decisions** (spec §3
   opening; WAY-05 and WAY-35 by analogy). Without it nothing binds a later template edit to cite a
   decision. Cost: a template rule change needs a decision of the-way.
8. **Review when** set on WAY-171 (first use of another language), WAY-172 (a meaning reaching a
   screen with no decision — the weak detection until the view-change task) and WAY-175 (the
   screenshot comparison's return condition from m2l5 row 13); `none` elsewhere, as no other entry
   rests on a prediction.
9. **G1, G5, G6, G24, G25 at level 2**, as spec §9.3 gives; G2, G3, G4, G26 at level 1 with the
   invariants of the plan.

### Checks (turn 1)

| Command | Exit | Output |
|---|---|---|
| `python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none` | 0 | [foundation-f1a-decision-guard.txt](foundation-f1a-decision-guard.txt) — 0 errors, 15 warnings (5 pre-existing check-by dates WAY-03/21/52/55/69; 10 `merge of <request link>` placeholders: WAY-09, WAY-167…175), 5 unchecked (all from `--base none` / `--merge-onto none`, the last being "the fingerprints relations carry") |
| `python -B .runs/task-cycles/product-guidelines-styleguide/reports/foundation_fingerprints.py . --from 167` (hand recomputation through `relation-model/fingerprint.py`) | 1 | [foundation-f1a-fingerprints.txt](foundation-f1a-fingerprints.txt) — 468 relations and links; all 17 relations of WAY-167…175 current; the only stale links are the six invariants deriving from WAY-09@909e9c5c (now `ce6bd9c0`), renewed in F3 |
| `git diff --check` (before commit) | 0 | [foundation-f1a-diff-check.txt](foundation-f1a-diff-check.txt) |
| informational: `python -B elements/part-map/format_guard.py foundations/part_map.md --base none` | 1 | [foundation-f1a-part-map-guard-informational.txt](foundation-f1a-part-map-guard-informational.txt) — 12 errors, each a *Scope* naming `product-guidelines` (WAY-09, 27, 38, 167–175) not yet a part; expected until F2 |
| informational: `python -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none` | 1 | [foundation-f1a-invariant-guard-informational.txt](foundation-f1a-invariant-guard-informational.txt) — 13 errors, each a level-1 invariant of WAY-168…171 not yet written or derived; expected until F3; the stale WAY-09 links are not reported with `--merge-onto none` |

### Changed files (commit `2181273`)

`foundations/decisions.md` — 424 added, 16 removed.

### Unresolved concerns

- Between this commit and F2/F3 the part-map and invariants guards fail as listed above; the
  six WAY-09 dependants carry a stale fingerprint until F3.
- "form check" names a script in WAY-170 without a glossary entry; a reader of the field reads it as
  "a check of form", which is what it is. To weigh at F2 with the term "guidelines".
- The glossary term "guidelines" (turn 3, row 25) holds "hand-written" in its meaning, which WAY-167
  also binds; WAY-96 keeps rules out of definitions, so turn 3 may need the definition without
  "hand-written" or a reason that it is not a rule.
- Several new lines exceed 100 characters (headings of WAY-168 and WAY-175, a few prose lines), as
  older entries do; no check reads the width.

## Turn 2 — F1b

Root ruling C27: turn-1 departures accepted provisionally; G9 refers to WAY-172's clause on a value
kept with its meaning instead of repeating it. Foundation reread for these entries: the whole log as
of `2181273` (WAY-167…175 included), the glossary, the part map; invariants and facts as in turn 1.

### Entries written (commit `5fde846`)

| Entry | Lines | Row | Relations (fingerprint recomputed) | Verification | Review when | Fingerprint |
|---|---|---|---|---|---|---|
| WAY-176/1 = G7 | 5835-5874 | 5, 6 | derives from WAY-173@c423105b | level 1 `guidelines-check-colour-pair` + level 2 | none | e8801ae5 |
| WAY-177/1 = G8 | 5875-5902 | 7 | derives from WAY-173@c423105b | level 2 | none | 8c1571e5 |
| WAY-178/1 = G9 | 5903-5928 | 8 | derives from WAY-173@c423105b · WAY-172@45806b6e | level 2 | none | 7d0e002d |
| WAY-179/1 = G10 | 5929-5955 | 9 | derives from WAY-173@c423105b | level 2 | none | c619d448 |
| WAY-180/1 = G11 | 5956-5981 | 10 | derives from WAY-173@c423105b | level 2 | none | 3f7bd803 |
| WAY-181/1 = G12 | 5982-6007 | 11 | derives from WAY-173@c423105b · WAY-36@3ee8e19c | level 2 | none | fc13a0df |
| WAY-182/1 = G13 | 6008-6034 | 12 | derives from WAY-173@c423105b | level 2 | none | 84cb098f |
| WAY-183/1 = G14 | 6035-6058 | 13 | derives from WAY-173@c423105b | level 2 | none | a0357689 |
| WAY-184/1 = G15 | 6059-6087 | 15 | derives from WAY-173@c423105b | level 2 | first product with a styleguide written before its first screen merges that screen's task · 2027-03-31 | cdb363d5 |
| WAY-185/1 = G16 | 6088-6117 | 14 | none | level 2 | none | dbec4fbc |
| WAY-186/1 = G17 | 6118-6156 | 16 | derives from WAY-122@b343277a · WAY-120@81f84997 | level 2 | none | f2b98895 |
| WAY-187/1 = G18 | 6157-6195 | 17 | none | level 2 | none | d58726d5 |
| WAY-188/1 = G19 | 6196-6226 | 18 | narrows WAY-168@47d9d53e · derives from WAY-08@2343e09f | level 1 `guidelines-check-carrier` + level 2 | none | 73da8ecb |
| WAY-189/1 = G20 | 6227-6261 | 19 (+ role meaning, C16) | derives from WAY-188@73da8ecb · WAY-191@1f2ebdb9 | level 1 `guidelines-check-carrier` + level 2 | none | a76a39fb |
| WAY-190/1 = G21 | 6262-6297 | 20 | derives from WAY-51@8bdac21a · WAY-60@6e862c88 | level 2 | none | 6fe44697 |
| WAY-191/1 = G22 | 6298-6333 | 21 | derives from WAY-86@fa2a4251 | level 2 | none | 1f2ebdb9 |
| WAY-192/1 = G23 | 6334-6368 | 22 | derives from WAY-128@4dca37ca · WAY-129@1336c32b · WAY-133@d4f21514 | level 2 | none | deeb7733 |

Rows 5–13 and 15 are written as what the template of the styleguide discipline carries or what the
skill proposes, each deriving from WAY-173 (row 26). All *Approved by* read `Mariusz, merge of
<request link>`.

### Meaning sentences for the request (Polish)

- **WAY-176:** szablon styleguide'a daje tabelę ról nazwanych rolą, nie kolorem (`primary`, `muted`),
  rodzaju `background`, `text` albo `other`, ze zdaniem, co rola znaczy dla użytkownika, z decyzją,
  która to znaczenie niesie, i ze wskazaniem wartości w pliku tokenów bez jej przepisywania; rola tła
  stoi zawsze w parze z rolą tekstu na niej; nazwa roli omija słowa słownika the way, chyba że nadaje
  ją technologia produktu.
- **WAY-177:** styleguide wskazuje ścieżką katalog wspólnych komponentów i podaje stany każdej
  wspólnej kontrolki (domyślny, hover, widoczny fokus, wyłączony, błąd, pusty, ładowanie), pokazane
  na stronie stanów albo oznaczone jako nie dotyczy z powodem; spisu komponentów nie przepisuje.
- **WAY-178:** globalny token to znaczenie dla całego produktu, więc błąd jednego ekranu naprawia
  się w jego komponencie, nie zmianą wartości globalnego tokenu; co wymaga zmiana tokenu, mówi
  WAY-172.
- **WAY-179:** szablon niesie jako przykład, że makieta jest wzorem do porównania, nie specyfikacją —
  znaczenia biorą się z wytycznych, a wartości z pliku tokenów.
- **WAY-180:** styleguide wskazuje stronę „kitchen sink” produktu ze wszystkimi komponentami w
  każdym stanie, widoczną tylko w trybie deweloperskim; strona jest kodem produktu, nie treścią
  styleguide'a.
- **WAY-181:** kolejność planu zmiany interfejsu (środowisko i biblioteka → wartości w źródle →
  jeden ekran → stany) stoi w szablonie tylko jako przykład.
- **WAY-182:** każda wartość w pliku tokenów niesie obok informację, skąd pochodzi, a źródło dobiera
  skill dla danego produktu — the way nie trzyma listy narzędzi.
- **WAY-183:** skill proponuje styleguide każdemu interfejsowi użytkownika produktu, także prostemu
  panelowi administracyjnemu; produkt dostępny tylko przez API albo terminal go nie dostaje.
- **WAY-184:** skill proponuje, by styleguide powstał przed pierwszym ekranem, z regułami na start
  szerszymi niż pierwsze zadanie, które go użyje.
- **WAY-185:** skill najpierw rozpoznaje, co produkt już ma (tokeny czytane albo martwe, komponenty,
  nic), i rozbudowuje to zamiast nowego systemu; nową bibliotekę albo sposób stylowania zostawia
  człowiekowi jako pytanie zadania.
- **WAY-186:** reguły na start biorą się z preferencji człowieka dla technologii interfejsu, a bez
  nich z researchu ze źródłami ze stroną i wersją i z krytyką jak w kroku technologii, uzupełnionego
  o znaczenia zapowiadanych ekranów; research się powtarza przy odświeżeniu albo rozszerzeniu.
- **WAY-187:** produkt z ekranami dostaje audyt dwukierunkowy kończący się 3–5 zarzutami z
  `plik:linia` i skutkiem dla użytkownika w czterech kategoriach, ze stałym pytaniem „co zobaczy ktoś
  bez danych, prosto z linka, po odświeżeniu”; z drogą agenta do działającego produktu, gdy fundament
  ją rozstrzyga, a bez niej z kodu z oznaczeniem tego, czego nie widać.
- **WAY-188:** każda wiążąca reguła styleguide'a ma niezmiennik — skrypt, a gdzie się nie da, agent z
  k z n; reguła, której nie sprawdzi nawet agent, jest przykładem; tym styleguide zawęża WAY-168.
- **WAY-189:** skill proponuje na start niezmienniki sprawdzane skryptem — brak wartości na sztywno,
  widoczny fokus na każdej kontrolce, kontrast par tło–tekst liczony z pliku tokenów według przyjętego
  WCAG — oraz niezmiennik oceniany agentem, że każda rola jest używana tylko w swoim znaczeniu.
- **WAY-190:** przy porządkach stopniowych skill proponuje obok pełnego niezmiennika (na liście
  znanych naruszeń do końca porządków) drugi: żaden plik nie ma więcej wartości na sztywno niż na
  `{fork-point}`, a nowy plik nie ma żadnej; drugi znika, gdy pełny jest spełniony.
- **WAY-191:** progi kontrastu i wymóg widocznego fokusu skill bierze z WCAG przez decyzję produktu,
  o którą pyta z domyślną rekomendacją: najnowsza edycja nazwana numerem ze strony W3C, poziom AA,
  wszystkie ekrany; nic bez akceptacji człowieka; kryteria, na których opierają się niezmienniki, to
  fakty o otoczeniu.
- **WAY-192:** główny `AGENTS.md` produktu, poza blokiem instalatora, wskazuje każdy styleguide
  ścieżką z warunkiem „przed zmianą pliku tej części”, a zakaz wartości na sztywno stoi tam, gdzie
  skill `instruction-files` umieszcza reguły dla części plików, z informacją, że pilnuje go
  niezmiennik.

### Whole-foundation search (WAY-33) for these entries

Searched the same domain as in turn 1, now with the vocabulary of these entries (role, colour,
state, component, mockup, page, plan order, source of values, admin panel, first screen, research,
audit, invariant by an agent, k of n, list of violated invariants, fork point, WCAG, catalogue,
success criterion, pointer, instruction file, installer's block). Findings and how each was settled:

1. **WAY-104** (a word of the-way's glossary in a product's domain takes a qualifier) — WAY-176's
   role names; named in its binding sentence.
2. **WAY-04** (no hand-written copy of what code holds) — WAY-176 points to values, WAY-177 copies
   no component list, WAY-180's page is code; reasons in their rationales.
3. **WAY-172** — WAY-178 derives from it and points to its clause instead of restating it (C27).
4. **WAY-36** (plan rules stay in plans) — WAY-181 derives from it: the plan order is an example.
5. **WAY-121, WAY-122, WAY-120, WAY-123** — WAY-185 leaves a new library to the human (the task
   records that no route from an independent task to the technology step exists yet; no relation to
   WAY-121, whose step is a project's); WAY-186 derives from WAY-122 and WAY-120.
6. **WAY-143** (a task of a plan ends with something checkable; a preparatory task only where one
   depends on it) — a styleguide task before the first screen (WAY-184) is such a preparatory task
   or ends with the page of every state; no collision.
7. **WAY-165** and the glossary term "agent's way to the running product" — WAY-187 uses the term;
   the reliance goes through the term (WAY-94), no relation.
8. **WAY-28, WAY-29** — an audit of an existing product: existing state needs no justification and a
   kept choice is recovered with its rationale as WAY-29 gives; no change, the skill (S4) follows them.
9. **WAY-168, WAY-08, WAY-62, WAY-68** — WAY-188 narrows WAY-168 (area: the styleguide discipline),
   derives from WAY-08 (k of n); WAY-62 and WAY-68 named in its rationale as the bounds of agents'
   cost and flakiness (task question 4).
10. **WAY-51, WAY-60** — WAY-190 derives from both and fits them unchanged; the full invariant goes
    on the list only by a foundation change a human accepts (WAY-51), as its complying example says.
11. **WAY-86, WAY-73, WAY-76, WAY-77, WAY-80, WAY-46** — WAY-191 derives from WAY-86; the edition is
    read from the W3C's page (WAY-80), facts per criterion (WAY-76, WAY-73); a law or contract binds
    without adoption (WAY-86's last sentence, WAY-46) — in its rationale.
12. **WAY-128, WAY-129, WAY-130, WAY-133, WAY-16, WAY-107, WAY-132, WAY-141** — WAY-192 derives from
    WAY-128, WAY-129, WAY-133; WAY-130 is met by WAY-168 (the rule carries a decision); WAY-16 keeps
    a lint command out; WAY-107 keeps product paths out of the installer's block; WAY-132 and WAY-141
    leave the installer's files to the installer — no collision.
13. **Glossary** — "surface" kept as a product's own role only with a qualifier (WAY-176); no
    *Avoid* word used; "view", bare "token", "guideline", "domain", bare "interface" not used.

### Choices, with evidence and cost if wrong

1. **WAY-178 also derives from WAY-172** — it relies on WAY-172's clauses by reference (C27). Cost:
   a flag when WAY-172 is reworded, which is wanted.
2. **WAY-188 also derives from WAY-08** — k of n is WAY-08's rule. Cost: one more relation.
3. **WAY-189 derives from WAY-191 as well as WAY-188** — its contrast and focus invariants take their
   thresholds through the WCAG adoption. Cost: a flag on WAY-189 when WAY-191 changes.
4. **WAY-188 and WAY-189 phrase rows 18–19 so that they fit WAY-173** — the skill proposes and the
   template's required rules call for the first invariants; a product departs only by a `none —`
   decision; the meaning of the rows (which invariants, script vs agent) is kept.
5. **WAY-183 adds that a product reached only through an API or a terminal gets no styleguide** —
   root C14 ("user interface" means screens). Cost: low.
6. **WAY-185 and WAY-187 carry no relation** (spec "—"); WAY-192 adds WAY-129 to the spec's
   WAY-128 · WAY-133 because the pointer's form is WAY-129's rule.
7. **Review when** only on WAY-184 (the before-first-screen mode has no trial yet — task question 2,
   weak point).

### Checks (turn 2)

| Command | Exit | Output |
|---|---|---|
| `python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none` | 0 | [foundation-f1b-decision-guard.txt](foundation-f1b-decision-guard.txt) — 0 errors, 32 warnings (5 pre-existing check-by dates; 27 `merge of <request link>` placeholders: WAY-09, WAY-167…192), 5 unchecked (no-main options, incl. "the fingerprints relations carry") |
| `python -B .runs/task-cycles/product-guidelines-styleguide/reports/foundation_fingerprints.py . --show WAY-176 … WAY-192 --from 176` | 1 | [foundation-f1b-fingerprints.txt](foundation-f1b-fingerprints.txt) — 491 relations and links; all 23 relations of WAY-176…192 current, and all of WAY-167…175 still current; stale only the six WAY-09 dependants (F3) |
| `git diff --check` (before commit) | 0 | [foundation-f1b-diff-check.txt](foundation-f1b-diff-check.txt) |
| informational: part-map guard `--base none` | 1 | [foundation-f1b-part-map-guard-informational.txt](foundation-f1b-part-map-guard-informational.txt) — 29 errors, every one a *Scope* naming `product-guidelines` (F2) |
| informational: invariants guard `--base none --merge-onto none` | 1 | [foundation-f1b-invariant-guard-informational.txt](foundation-f1b-invariant-guard-informational.txt) — 19 errors, every one a level-1 invariant of WAY-168…171, 176, 188, 189 not yet written (F3) |

### Changed files (commit `5fde846`)

`foundations/decisions.md` — 535 added, 0 removed.

### Unresolved concerns

- Carried to turn 3 as the root asks: the definition of "guidelines" and "hand-written" (WAY-96);
  whether "form check" needs an entry.
- F3 must derive `guidelines-check-carrier` from WAY-168, WAY-188 and WAY-189, and
  `guidelines-check-colour-pair` from WAY-176, with the fingerprints above.
- A product's styleguide invariants (WAY-189, WAY-190) are proposals the skill (S4) writes into a
  task; nothing in the-way checks that a product took them, beyond the form check's demand of an
  invariant for every rule (WAY-188).

## Turn 3 — F2 and F3

Skills read whole: `elements/glossary/skill/SKILL.md`, `template.md`, `examples.md` (and the example
entries `invariant`, `gate`, `foundation`); `elements/part-map/skill/SKILL.md`, `template.md`,
`examples.md` (with `part-map`, `task-cycle`, `wording-reaches-dependants`, `content-fingerprint`,
`entry-format`); `elements/invariants/skill/SKILL.md`, `template.md`, `examples.md` (with
`log-entry-field-presence`, `decision-guard-overdue-review`, `file-part-assignment`,
`fingerprint-definition`, `return-step-record`). Foundation at `5fde846` (WAY-150): the whole
glossary and part map; every decision the new entries name; the invariants file whole for
identifiers, the six WAY-09 dependants and every invariant of the parts the new entries name;
root ruling on the held notes (after C27).

Commit `eb9ff1e`.

### F2 — glossary (`foundations/glossary.md:105-110`)

**guidelines** — "Guidelines are text a product keeps outside its foundation that tells agents what
to do and how in a discipline of work on the product." *Avoid* none, *Not* none. Fingerprint
`b59228a0` (no reference carries it, WAY-94).

- Uses (`format_guard.py --uses guidelines`): 70, all in WAY-09 and WAY-167…192, every one in this
  meaning; no use before this change, so no other meaning to rename (WAY-99) and nothing for *Not*.
  No other word for the same thing in the foundation, so *Avoid* is none; "guide" (WAY-128, 130,
  133) is not listed, as spec §9.2 requires.
- **Genus "text", not "a document"**: the uses say both "a product's guidelines" (all its files,
  WAY-167, WAY-170) and "the guidelines of the styleguide discipline" (one file); a definition as
  "a document" would be false of the first use, a second meaning (WAY-95). "Text … in a discipline"
  is true of both; one file per discipline stays WAY-167's rule.
- **"hand-written" left out** (root note 1): WAY-96 — a definition carries a rule when it holds
  something the decision setting it could change while the word names the same thing; WAY-167
  binds "written by hand", and a version of it allowing generated guidelines would leave the word
  naming the same text, so the clause is a rule and stays in WAY-167. "Outside its foundation" stays:
  it tells guidelines apart from the foundation's entries, the neighbouring term (WAY-96), and is
  what row 25 names them by.
- **"form check" takes no entry** (root note 2): it stands in binding parts (WAY-170 and the
  `guidelines-check-*` sentences), but each binding use names it as "the form check of
  guidelines" beside what it is — "a script of the-way" (WAY-170) or its path
  `product-guidelines/form_check.py` (the invariants) — and a reader of the field reads "form
  check" as a check of form, which it is; the foundation uses the phrase in no other meaning (its
  only other near use, "the check of form" in WAY-168's *Rejected*, means the same). Neither test of
  WAY-95 holds.
- Other words weighed, no entry: "styleguide" (a reader of the field gives it this meaning, and
  WAY-167 says which file it is); "design token", "user interface", "discipline", "screen" — field
  meanings.
- Term against identifiers (WAY-93): `read_alike("guidelines", …)` is false for `product-guidelines`,
  the eight new invariants and the surface (run by hand, as the guard's check is `unchecked` with
  `--base none`). No sentence of the foundation says what the word is, so nothing to rewrite.

### F2 — part map (`foundations/part_map.md`)

| Entry | Lines | Change |
|---|---|---|
| `product-guidelines` (new part) | 261-280 | responsibility (fingerprint `d09fece0`); *Files* `product-guidelines/**`; *Depends on* decisions · invariants · glossary · part-map · environment-facts · elements-common · relation-model · project-level · instruction-files · task-cycle; four failure modes of spec §9.4, all high, the first detected by `guidelines-check-stale-reference`, the rest not detected; *Trust boundary* `product-guidelines/form_check.py` |
| `agent-instructions` | 185-212 | *Depends on* gains `product-guidelines` |
| `installation` | 242-259 | *Depends on* gains `product-guidelines` |
| `skills-reach-the-way-sessions` (flow) | 291-301 | *Parts* gains `product-guidelines` |
| `guidelines-form-check-command` (new surface, root C25) | 355-360 | promise (fingerprint `e57c6ed8`); *Declared at* `product-guidelines/form_check.py · main` |

- The fourth failure mode gains the kind of damage the spec left out ("a user's files can leave the
  machine, or a merge rests on a check that never ran"), worded as `instruction-files`' failure mode
  of the same kind, since the template requires the field.
- The part's criticality computes high from its failure modes; `installation` and
  `agent-instructions` now inherit from it as dependants of a high part (they are high already).
- The external context's row "a product pinned to a commit | both | untrusted" already covers what
  the form check reads; no new row.
- Expected before the code, recorded, not stubbed (handoff): the part-map guard reports three errors
  — the pattern `product-guidelines/**` and the trust boundary match no file, and the surface's
  declaration does not exist — until S1 and S2.

Polish meaning sentences:
- **guidelines (słownik):** wytyczne to tekst, który produkt trzyma poza fundamentem i który mówi
  agentom, co i jak robić w jednej dziedzinie pracy nad produktem.
- **część `product-guidelines`:** nowa część the way odpowiada za wspólną formę wytycznych każdego
  produktu, szablony dziedzin wytycznych ze skillem, który prowadzi pracę nad nimi, i za skrypt
  sprawdzający formę wytycznych; jej awarie to m.in. przepuszczony nieaktualny odsyłacz, znaczenie
  nieprzyjęte przez człowieka i skrypt, który czytając spreparowany plik, wychodzi poza repozytorium.
- **`agent-instructions`, `installation`, przepływ `skills-reach-the-way-sessions`:** zależą od nowej
  części / przechodzą przez nią (nowy skill i jego punkty wejścia, instalator podający skill).
- **powierzchnia `guidelines-form-check-command`:** polecenie skryptu formy wytycznych zachowuje
  nazwę, argumenty i kody wyjścia, bo polegają na nim metody niezmienników produktów i wskazówki
  instalatora.

### F3 — invariants (`foundations/invariants.md`)

| Entry | Lines | Derives from | Part | Method | Fingerprint |
|---|---|---|---|---|---|
| `guidelines-form/1` | 2133-2141 | WAY-170@c1b230d2 · WAY-171@2bc38c05 | every | `python -B product-guidelines/form_check.py --record .runs/guidelines-form.jsonl` | 91ee4865 |
| `guidelines-reference-current/1` | 2143-2151 | WAY-169@e2fb088c | product-guidelines · decisions · invariants | `python -B product-guidelines/form_check.py --merge-onto {merge-onto} --record .runs/guidelines-reference.jsonl` | 0b831257 |
| `guidelines-check-form/1` | 2153-2161 | WAY-170@c1b230d2 · WAY-171@2bc38c05 | C13 set¹ | tests² | 21e7904e |
| `guidelines-check-carrier/1` | 2163-2171 | WAY-168@47d9d53e · WAY-188@73da8ecb · WAY-189@a76a39fb | C13 set | tests | 452551ec |
| `guidelines-check-colour-pair/1` | 2173-2181 | WAY-176@e8801ae5 | C13 set | tests | 174737ed |
| `guidelines-check-reference-target/1` | 2183-2191 | WAY-169@e2fb088c | C13 set | tests | 269a1196 |
| `guidelines-check-stale-reference/1` | 2193-2201 | WAY-169@e2fb088c | C13 set | tests | fee763b3 |
| `guidelines-check-code-path/1` | 2203-2211 | WAY-170@c1b230d2 | C13 set | tests | 86919ec9 |

¹ `product-guidelines · decisions · invariants · part-map · elements-common · relation-model`.
² `python -B gate/run_tests.py product-guidelines --record .runs/product-guidelines-tests.jsonl`.
Every entry: *Rests on* none, *Correction* none, version 1 (no main branch). The methods name a
script and a directory that do not exist yet, which the template allows for a Python command
(WAY-105). Authors (WAY-69, root C25): I am the sentence author of all eight; their checks are
`product-guidelines/form_check.py` run on the-way (the two form invariants, S2/S3 executors) and
`product-guidelines/test_form_check_invariants.py` (the six `guidelines-check-*`, the F4 author);
the code covered is `form_check.py` (S2, S3). Instruction for F4 (skill step 4.4): give the check
author the six `guidelines-check-*` entries above and their method only, as plan F4 gives it.

**Renewed (WAY-09 edited in place, WAY-31):** `repository-file-location`,
`element-directory-contents`, `relation-model-directory-contents`, `invariant-example-target`,
`map-example-target`, `glossary-example-target` — *Derives from* `WAY-09@909e9c5c` →
`WAY-09@ce6bd9c0`; each checked against WAY-09's new binding part: the new part adds a directory
`product-guidelines/` that `repository-file-location` now admits, and changes nothing the other
five say (element directories, `relation-model/`, the three examples files). Sentences and versions
unchanged.

Sentence choices, with cost if wrong:
1. `guidelines-form` adds to spec §3.3's sentence "with a name that agrees with its *Discipline*",
   because the form check records error 5a (spec §5.3) under this invariant; without it the check
   would give verdicts for what the sentence does not say. It speaks of "rules and rule fields that
   the templates require", which covers the role table and the carriers the styleguide template
   requires (S1 writes them). Cost: a word in the sentence.
2. `guidelines-reference-current` says "reference" where the spec said "token" — bare "token" is
   kept out of the new entries (WAY-84's secret, WAY-162's model tokens).
3. The six `guidelines-check-*` follow spec §9.3's shapes, each naming the script by its path, the
   value the check is given in quotation marks (`"{merge-onto}"`, template "The sentence"), and
   the form of references word for word as `guidelines-reference-current` gives it, so F4's tests
   have one definition of a reference. `guidelines-check-carrier` names the required heading
   `### Each role in its meaning` (spec §4.1), which ties the sentence to that heading: a rename of
   the heading in S1 is a change of this invariant. `guidelines-check-code-path` names "absolute, a
   `..` segment, a drive or a UNC prefix" from spec §5.3 item 6.
4. Level-1 links in both directions hold: every decision naming these invariants (WAY-168…171,
   176, 188, 189) is named in their *Derives from*.

Polish meaning sentences:
- **`guidelines-form`:** każdy plik `guidelines/<nazwa>.md` ma we właściwej kolejności nagłówki,
  sekcje, reguły i pola wymagane przez szablony (z commita the way, którego używa repozytorium),
  nazwę zgodną z dziedziną, porzucone części oznaczone `none —` z decyzją i odciskiem, części mapy,
  które istnieją, i ścieżki, które git śledzi.
- **`guidelines-reference-current`:** każdy odsyłacz w wytycznych poza blokami kodu wskazuje
  obowiązującą decyzję albo niezmiennik i niesie aktualny odcisk — na tym samym commicie i, gdy jest
  gałąź główna, po scaleniu na nią.
- **`guidelines-check-form`:** skrypt formy zgłasza jako błąd brakujące albo przestawione części
  wymagane przez szablony, porzucenie bez decyzji z odciskiem, część mapy, której nie ma, i plik,
  którego nazwa nie zgadza się z dziedziną.
- **`guidelines-check-carrier`:** skrypt zgłasza regułę bez decyzji, regułę styleguide'a bez
  niezmiennika i decyzję z tabeli ról, której nie wskazuje reguła „każda rola w swoim znaczeniu”.
- **`guidelines-check-colour-pair`:** skrypt zgłasza rolę tła bez wskazanej roli tekstu z tabeli.
- **`guidelines-check-reference-target`:** skrypt zgłasza odsyłacz do decyzji albo niezmiennika,
  których nie ma albo które nie obowiązują, oraz odsyłacz ze źle zapisanym odciskiem.
- **`guidelines-check-stale-reference`:** skrypt zgłasza odsyłacz z odciskiem innym niż aktualny —
  na tym samym commicie i, z `{merge-onto}`, po scaleniu.
- **`guidelines-check-code-path`:** skrypt zgłasza ścieżkę w „Where in code”, która wychodzi poza
  repozytorium albo wskazuje coś, czego git nie śledzi.
- **odnowienie sześciu niezmienników WAY-09:** te same zdania, nowy odcisk WAY-09; żaden nie zmienia
  znaczenia.

### Whole-foundation search (WAY-33), end of F3

Domain: all five elements at the working tree of this commit — decisions (WAY-01…WAY-192, every
*Scope*, every relation), invariants (every entry; every *Part* naming a part of the new entries or
`every`), glossary, part map, environment facts (headings and every fact a new sentence could rest
on). Searched for: the new term and its forms; the identifiers of the new part, surface and
invariants; "form check", "styleguide", "reference", "fingerprint", "fenced code", "template",
"discipline", "git tracks", "trust boundary", "network", "skill entry point". Findings:

1. **Identifiers** — `guidelines-form` (invariant) and `guidelines-form-check-command` (surface) are
   distinct in the one space of identifiers (`identifier-holders`, guard clean); no term reads alike
   any of them (checked by hand above).
2. **`file-part-assignment`, `path-pattern-reach`, `surface-declaration`** (*Part* `every` or the
   map) — fail until S1/S2 bring the files; recorded as expected, no stub.
3. **`skill-entry-points`** (*Part* `every`) — will need the new skill's entry points (S4–S7); the
   flow `skills-reach-the-way-sessions` now lists `product-guidelines`, so its test reaches changes
   there.
4. **`repository-file-location`** — holds for `product-guidelines/` only with WAY-09's edit, renewed.
5. **`script-language`, `script-imports`, `script-subprocesses`** (WAY-38, *Scope* now includes
   `product-guidelines`) — bind `form_check.py`; nothing to change in the entries.
6. **`invariant-citation-target`** — the form check will cite `guidelines-form/1` and
   `guidelines-reference-current/1`, both now entries (root C11).
7. **Environment facts** — no fact holds a condition of the eight sentences: they compute
   fingerprints through `relation-model` (whose facts `sha-256`, `utf-8` rest on
   `fingerprint-definition`), and "git tracks" asks git for a listing, not a pattern match
   (`git-path-patterns` stays with `file-part-assignment`). *Rests on* none for all.
8. **WAY-62** — the reach of each *Part* follows root C13; `guidelines-form` names `every` because a
   renamed tokens file, part or pin can make it false (spec §3.3).
9. **Glossary uses** — the new sentences use "foundation", "part", "invariant", "decision" in their
   terms' meanings; no *Avoid* word ("checker", "quality gate"); "guideline", "view", bare "token"
   not used.

No finding calls for another entry. Turn-1 and turn-2 searches are above; this is the search the
plan records at the end of F3. The search against the `foundations` tip before integration is the
root's later step.

### Checks (turn 3)

| Command | Exit | Output |
|---|---|---|
| `python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none` | 0 | [foundation-f3-decision-guard.txt](foundation-f3-decision-guard.txt) — 0 errors, 32 warnings (5 pre-existing check-by dates, 27 request-link placeholders), 5 unchecked (no-main options) |
| `python -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none` | 0 | [foundation-f3-invariant-guard.txt](foundation-f3-invariant-guard.txt) — 0 errors, 0 warnings, 3 unchecked: identifiers, versions, corrections and the violated list (`--base none`); `TODO` in the entries and the fingerprints the links carry (`--merge-onto none`); note: no `human_verdicts.md` |
| `python -B elements/glossary/format_guard.py foundations/glossary.md --base none --merge-onto none` | 0 | [foundation-f3-glossary-guard.txt](foundation-f3-glossary-guard.txt) — 0 errors, 0 warnings, 5 unchecked: the *Avoid* count, terms and identifiers that came to read alike, uses of changed definitions (`--base none`); `TODO` in the entries, terms with no use after the merge (`--merge-onto none`); note: the-way's glossary is no product's |
| `python -B elements/part-map/format_guard.py foundations/part_map.md --base none` | 1 | [foundation-f3-part-map-guard.txt](foundation-f3-part-map-guard.txt) — 3 errors, all expected before the code: `product-guidelines/**` and the trust boundary `product-guidelines/form_check.py` match no file, the surface's declaration does not exist; 7 unchecked: both flows' parts (no coverage file), change paths of promise levels, dependencies (no graph command), known violations, identifiers, criticality lowering (`--base none`) |
| `python -B elements/environment-facts/format_guard.py foundations/environment_facts.md --base none --merge-onto none` | 0 | [foundation-f3-environment-facts-guard.txt](foundation-f3-environment-facts-guard.txt) — 0 errors, 0 warnings, 3 unchecked (no-main options) |
| `python -B gate/run_tests.py elements/decisions` | 0 | [foundation-f3-tests-elements-decisions.txt](foundation-f3-tests-elements-decisions.txt) — 169 tests OK |
| `python -B gate/run_tests.py elements/invariants` | 0 | [foundation-f3-tests-elements-invariants.txt](foundation-f3-tests-elements-invariants.txt) — 233 tests OK |
| `python -B gate/run_tests.py elements/glossary` | 0 | [foundation-f3-tests-elements-glossary.txt](foundation-f3-tests-elements-glossary.txt) — 204 tests OK |
| `python -B gate/run_tests.py elements/part-map` | 1 | [foundation-f3-tests-elements-part-map.txt](foundation-f3-tests-elements-part-map.txt) — 162 tests, 1 failure: `OwnMap.test_the_way_map_holds_no_error`, failing on the same three expected errors of the part-map guard; passes once S1/S2 add the files (recorded, not suppressed) |
| `python -B gate/run_tests.py gate` | 0 | [foundation-f3-tests-gate.txt](foundation-f3-tests-gate.txt) — 98 tests OK (critical-flow tests included) |
| `python -B .runs/.../reports/foundation_fingerprints.py . --from 167` | 0 | [foundation-f3-fingerprints.txt](foundation-f3-fingerprints.txt) — 503 relations and links, 0 stale (the six WAY-09 dependants renewed) |
| `git diff --check` (before commit) | 0 | [foundation-f3-diff-check.txt](foundation-f3-diff-check.txt) |

### Changed files (commit `eb9ff1e`)

`foundations/glossary.md` 7 added, 0 removed; `foundations/invariants.md` 86 added, 6 removed;
`foundations/part_map.md` 30 added, 3 removed.

### Unresolved concerns

- Red until the slices: the part-map guard (3 errors) and its own-map test (1 failure) until S1/S2;
  the invariants' methods name `product-guidelines/form_check.py` and `gate/run_tests.py
  product-guidelines`, which the gate reports `unchecked` (missing script) until S2/F4.
- `guidelines-check-carrier` names the heading `### Each role in its meaning`: S1 must write that
  heading word for word, or the sentence and its version change.
- `guidelines-form` and `guidelines-reference-current` are sentences a product copies unchanged
  (spec §3.3); a product that rewords one breaks the form check's version-1 citation (root C8).
- The F2/F3 entries reach the independent assessment (WAY-10) together with the F4 check, as the
  plan gives it; the search against the `foundations` tip before integration is still to run.

## Return step

Handoff: [return-handoff.md](return-handoff.md). Range read: `96623ed..896071a` (foundation stage
`96623ed..8ea4679`, slices `8ea4679..9dd9880`, fix `896071a`), by file: `product-guidelines/template.md`,
`styleguide/template.md`, `styleguide/SKILL.md` (whole), `form_check.py` (its checks and what each
records under `guidelines-form/1`), `installation/install.py`, `installation/README.md`, `README.md`;
`cycle.md` C5–C31; `reports/sdd/sdd-ledger.md`; `reports/final-review.md` (Minor findings and
"Ledger lines graded", as candidates). `foundations/` was not changed by any slice
(`git diff eb9ff1e..896071a -- foundations` empty). Foundation selection refreshed by "Reading the
foundation" for the real diff: touched parts `product-guidelines`, `installation`,
`agent-instructions` (entry points, `README.md` left out on purpose), and the foundation files;
decisions selected by *Scope* (all naming one of these, WAY-167…192 among them) re-read where a
candidate touches them.

### Candidates and how each was settled

1. **The *Part* of `guidelines-reference-current/1`** (slice 3 ⚠️). WAY-62: the parts where a
   change can make the sentence false. In the-way the sentence holds for want of any file
   `guidelines/<name>.md`, so a change to `relation-model` or `elements-common` cannot make it false
   here; in a product, the template's copy names the part holding `.the-way`, which covers a moved
   fingerprint script (`product-guidelines/template.md:160-175`). The script's code path through
   `elements-common` and `relation-model` is what the six `guidelines-check-*` cover, with that wider
   *Part*. **No change** — a choice line, as the final review also judged.
2. **The 1 MiB read limit on a product's decision log and invariants file** (slice 3 M3). Changing
   the limit would violate no requirement or settled rule: it is a constant bounding reads at a
   trust boundary, chosen with the 1 MiB limit on files of guidelines (spec §5.4, autonomous). It
   fails loudly (exit 1, an error naming the file). **Replaceable detail**, kept in ordinary tests
   and the request (the-way's own log: 41% of the limit).
3. **The part-map change under *Settlements to record* (spec §6.2) vs *To do* (the skill).** No entry
   says otherwise: WAY-134 names a candidate as a decision, an invariant, a glossary term or a fact,
   and WAY-167 says only which part holds `guidelines/**`. The skill is right; **no change**.
4. **WAY-167 vs the form check on `guidelines/<discipline>-<part>.md`** (slice 1 M6, slice 2). Spec
   §2.2 ("for a discipline with one document") and §5.3 item 5a, reviewed under R9, give the name
   `<discipline>-<part>.md` for any discipline; WAY-167 gave it to the styleguide alone — a row the
   foundation step wrote narrower than the reviewed spec, with the check and the F4 tests following
   the spec. **WAY-167 edited in place** to give `guidelines/<discipline>-<part>.md` to any discipline
   whose guidelines differ between parts of the map, the styleguide always per user interface; its
   complying and violating examples, rationale and *Rejected* follow. Fitting the check instead
   would change F4 tests (WAY-03) and code for a narrower rule nobody settled.
5. **The guidance sentence's trigger, "before every merge"** (C31). WAY-170 says "checks before a
   merge" with no narrower trigger; no entry gives the old one. **No change.**
6. **WAY-186 wider than the skill** (slice 4 note b). *To do* 8 and row 15 tie the starting set to a
   styleguide written before the first screen; row 16's "zestaw na start" is that set. **WAY-186
   edited in place**: the starting rules of a styleguide written before the first screen of its user
   interface; research again at every refresh or extension; a product with screens starts from the
   audit (complying example and rationale added). Meaning kept as row 16 and *To do* 8 give it.
7. **`guidelines-form/1` narrower than what its check records** (final review, ledger Task 1 M5).
   `form_check.py` records under `guidelines-form/1` the table of roles — its columns, *Kind* off the
   list, a background whose *Text on it* names no text role, a role's *Decision* form, a role
   decision missing from "Each role in its meaning" (`form_check.py:780-834`) — while the sentence
   spoke of header lines, sections, rules and rule fields only, so a product's verdict could fail on
   what its sentence does not state (WAY-61). **Sentence widened** to "header lines, sections, rules,
   rule fields and tables … each with the values and the links those templates give it". Version
   stays 1 (no main branch). It needs its copy in `product-guidelines/template.md:150` changed word
   for word — a file of the slices, so not mine (question 1).
8. **Final-review Minor 1–4** (required examples unchecked, an example with *Decision*, order of
   further rules, *Applies to* vs the file's part): gaps between a template's wording and the check.
   The foundation requires none of them: examples bind nothing (WAY-168), WAY-173 binds adoption of
   rules, and the widened `guidelines-form` speaks of what the templates require. **Code or template
   findings for the request**, no entry.
9. **The trust boundary's behaviour** (no path from a product's file reaches git, no socket, reads
   bounded, `lstat` per component). Would changing it violate a requirement? The part map's failure
   mode records the damage as high and "not detected", as `instruction-files` does for its check
   script, whose same behaviour also stands in ordinary tests (WAY-48 checks a boundary change for
   crafted input). **Kept in ordinary tests** (`product-guidelines/test_form_check.py`, the
   adversarial cases of spec §10) — a choice line; an invariant would make the failure mode
   "detected", a later decision for both scripts.
10. **"Fenced code"** in the reference invariants: the code follows CommonMark (backticks and
    tildes, C28.4). The meaning is the field's, as in the other sentences of the foundation that use
    the words; **no fact, no change**.
11. **Rows of *Settlements to record***: all 27 written (final review's mapping, re-read); none
    missed. **Terms**: no new word in a binding part. **Facts**: none the code rests on beyond
    `json-lines` and git's, already held. **Part map**: every new file falls under
    `product-guidelines/**`, `installation/**` or `agent-instructions` patterns; `README.md` is left
    out on purpose; the guard is clean now that the files exist.

No invariant needing a new check author: the only invariant changed is `guidelines-form/1`, whose
check is the form check itself on the-way (`--record .runs/guidelines-form.jsonl`), run below; the
widening names what that code already records, so no code changes.

### Entries changed (commit `19d28f8`)

| Entry | Lines | Change | Fingerprint |
|---|---|---|---|
| WAY-167/1 | 5439-5492 | binding: `guidelines/<discipline>-<part>.md` for any discipline whose guidelines differ between parts; examples, rationale, *Rejected* | 681d47ff → b1087bdb |
| WAY-186/1 | 6124-6164 | binding: the starting rules of a styleguide written before the first screen; complying example, rationale | f2b98895 → d78fb521 |
| `guidelines-form/1` | invariants 2133-2141 | sentence: "rule fields and tables … each with the values and the links those templates give it" | 91ee4865 → 93fc6096 |

No relation or link carries WAY-167's, WAY-186's or `guidelines-form`'s fingerprint (fingerprint
script: 0 stale); the form check cites `guidelines-form/1` by version, unchanged.

Polish meaning sentences:
- **WAY-167:** wytyczne dziedziny stoją w `guidelines/<dziedzina>.md`, a gdy różnią się między
  częściami mapy — w `guidelines/<dziedzina>-<część>.md` dla każdej takiej części; styleguide zawsze
  jako `guidelines/styleguide-<część>.md` na każdy interfejs użytkownika.
- **WAY-186:** reguły na start (z preferencji człowieka albo z researchu z krytyką) dotyczą
  styleguide'a pisanego przed pierwszym ekranem; research powtarza się przy odświeżeniu i
  rozszerzeniu, a produkt z ekranami zaczyna od audytu kodu.
- **`guidelines-form`:** plik wytycznych ma też tabele wymagane przez szablony, z wartościami i
  powiązaniami, które szablony im dają (np. rodzaj roli, rola tekstu na tle, decyzja roli).

### Second whole-foundation search (WAY-33), against `origin/foundations`

`origin/foundations` fetched: `96623ed`, the branch's base — no change merged there since, so the
foundation the merge goes onto is the one searched at turns 1–3. Searched again, the five elements
whole at that commit beside this branch's entries, for every entry this change writes or edits
(WAY-09, 27, 38, 167–192; the term; the part, surface and flow; the eight invariants and six
renewals), with the return step's vocabulary added (file name per part, starting rules, audit,
tables of roles, read limits, fenced code, trigger of the guidance). No entry of `96623ed` absent
from the earlier searches; no new collision; the findings of turns 1–3 stand as settled there.

### Checks (return step)

| Command | Exit | Output |
|---|---|---|
| decision guard `--base none --merge-onto none` | 0 | [return-decision-guard.txt](return-decision-guard.txt) — 0 errors, 32 warnings (5 pre-existing check-by dates, 27 request-link placeholders), 5 unchecked (no-main options) |
| invariants guard `--base none --merge-onto none` | 0 | [return-invariant-guard.txt](return-invariant-guard.txt) — 0 errors, 0 warnings, 3 unchecked (no-main options) |
| glossary guard `--base none --merge-onto none` | 0 | [return-glossary-guard.txt](return-glossary-guard.txt) — 0 errors, 0 warnings, 5 unchecked (no-main options) |
| part-map guard `--base none` | 0 | [return-part-map-guard.txt](return-part-map-guard.txt) — 0 errors (the three errors of F3 gone now that the files exist), 7 unchecked (no coverage file for both flows, promise-level paths, no dependency graph, `--base none` ×3) |
| environment-facts guard `--base none --merge-onto none` | 0 | [return-environment-facts-guard.txt](return-environment-facts-guard.txt) — 0 errors, 3 unchecked |
| `python -B .../foundation_fingerprints.py . --from 167` | 0 | [return-fingerprints.txt](return-fingerprints.txt) — 503 relations and links, 0 stale |
| `git diff --check` (before commit) | 0 | [return-diff-check.txt](return-diff-check.txt) |
| `python -B gate/run_tests.py elements/decisions` | 0 | [return-tests-elements-decisions.txt](return-tests-elements-decisions.txt) — 169 OK |
| `python -B gate/run_tests.py elements/invariants` | 0 | [return-tests-elements-invariants.txt](return-tests-elements-invariants.txt) — 233 OK |
| `python -B gate/run_tests.py elements/glossary` | 0 | [return-tests-elements-glossary.txt](return-tests-elements-glossary.txt) — 204 OK |
| `python -B gate/run_tests.py elements/part-map` | 0 | [return-tests-elements-part-map.txt](return-tests-elements-part-map.txt) — 162 OK (the own-map failure of F3 gone) |
| `python -B gate/run_tests.py elements/environment-facts` | 0 | [return-tests-elements-environment-facts.txt](return-tests-elements-environment-facts.txt) — 165 OK |
| `python -B gate/run_tests.py gate` | 0 | [return-tests-gate.txt](return-tests-gate.txt) — 98 OK |
| `python -B gate/run_tests.py product-guidelines` | 0 | [return-tests-product-guidelines.txt](return-tests-product-guidelines.txt) — 60 OK |
| `python -B product-guidelines/form_check.py --record .runs/guidelines-form.jsonl` | 0 | [return-form-check.txt](return-form-check.txt) — no `guidelines/`, `pass` for `guidelines-form/1`; note: no `--merge-onto` |
| `python -B product-guidelines/form_check.py --merge-onto none --record .runs/guidelines-reference.jsonl` | 0 | [return-form-check-merge.txt](return-form-check-merge.txt) — 1 unchecked: the references after a merge (`--merge-onto none`), the expected state before `main` |

### Changed files (commit `19d28f8`)

`foundations/decisions.md` 22 added, 14 removed; `foundations/invariants.md` 1 added, 1 removed.

### Questions for the root

1. `product-guidelines/template.md:150` holds the sentence of `guidelines-form/1` that products copy;
   it has to read word for word as the widened entry (`foundations/invariants.md:2135`), and
   `product-guidelines/template.md:18-22` restates the old naming of WAY-167. Both are slice files I
   do not edit; who edits them in this change?

### Return step — correction after root ruling C32 (commit `c355004`)

- **WAY-167/1** restored whole to its text of turn 1 (`5439-5486`): one file `guidelines/<discipline>.md`
  per discipline, the styleguide one file `guidelines/styleguide-<part>.md` per user interface. The
  widening, its examples, its rationale sentence and its *Rejected* clause rejecting one file per
  discipline are gone — row 1 settles one document per discipline, and per user interface comes from
  row 13 alone. Fingerprint back to `681d47ff`; no relation or link carries it (`grep "WAY-167@"`
  over `foundations/`, `product-guidelines/`, `installation/`, `README.md`: none). Candidate 4 above
  is settled this way instead: the form check and its F4 tests are narrowed by other agents.
- WAY-186 and `guidelines-form/1` keep the return step's change.
- Polish meaning sentence, **WAY-167** as it now stands: wytyczne produktu pisze się ręcznie, poza
  fundamentem, w katalogu `guidelines/` — jeden plik `guidelines/<dziedzina>.md` na dziedzinę, a
  styleguide jako `guidelines/styleguide-<część>.md` na każdy interfejs użytkownika; katalog należy do
  części, która kieruje pracą agentów.
- Checks: decision guard `--base none --merge-onto none` exit 0, 0 errors, 32 warnings (5 check-by,
  27 placeholders), 5 unchecked ([return-c32-decision-guard.txt](return-c32-decision-guard.txt));
  fingerprint script exit 0, 503 relations and links, 0 stale
  ([return-c32-fingerprints.txt](return-c32-fingerprints.txt)); `git diff --check` exit 0
  ([return-c32-diff-check.txt](return-c32-diff-check.txt)).
- Changed: `foundations/decisions.md` 9 added, 15 removed.
- The template's copies (`product-guidelines/template.md:150`, `:18-22`) go to the template's author
  (C32).

## Assessment settlement

Settlement: [assessment-settlement.md](assessment-settlement.md) (read whole); remarks applied read
in [assessment.md](assessment.md) (A1, A2, A3, A6, A8, A10, A11, A14). Head before the change
`677ef7c`. Commit `04f8754`.

### Entries changed

| Remark | Entry | Lines | Change | Fingerprint |
|---|---|---|---|---|
| A1 | WAY-170/1 | 5571-5613 | third binding sentence: until a gate of the-way runs a product's invariants' methods, the installer's block names the script's two commands, before every merge, beside the format guards; *Review when* names the gate that ends it; a violating example, a rationale sentence and two *Rejected* items follow | c1b230d2 → 175a4fb6 |
| A2, A3 | WAY-175/1 | 5779-5871 | binding names each piece taken by the decision that carries it (WAY-176, 177, 178, 180, 181, 182, 185, 186, 187, 189, 192, and WAY-184 for the moment) without restating it; what no other decision carries (a palette from the code as a proposal, asking what only the team knows, writing for a reader who was not there) and what is left stay; *Based on* carries the observation read from the sources on 2026-10-18 — `10x-ui` at `loop2-10x` `e854fef5`, `om-ux-setup`/`om-ux-shape` at `loop` `715026e` — with the passage behind each piece taken and left; the course's lesson is said to be a private note, not quoted (WAY-27); rationale and *Rejected* name WAY-19 | 3174b1f3 → d895a207 |
| A14 | WAY-172/1 | 5666-5708 | *Review when* `none` | 45806b6e (unchanged) |
| A6 | WAY-183/1 | 6072-6095 | "has no user interface and gets no styleguide" (without "in this sense") | a0357689 → 17222226 |
| A8 | WAY-191/1 | 6337-6372 | "the newest edition that is a W3C Recommendation when the decision is written"; complying example follows | 1f2ebdb9 → d9fff88e |
| A6 | glossary "user interface" | glossary 217-222 | new entry (below) | eaec4d2e |
| A10 | `guidelines-check-carrier/1` | invariants 2163-2171 | "whose *Decision* holds no decision number with the log's prefix followed by `@`, every such rule of a styleguide whose *Invariant* holds no identifier of the invariants file followed by `@`" — what the check decides (`form_check.py:476-483`, `:445-455`); a number or identifier the log or file does not hold stays an error under `guidelines-reference-current` and `guidelines-check-reference-target` | 452551ec → 3b699a99 |
| A11 | `guidelines-reference-current/1` | invariants 2143-2151 | *Part* `product-guidelines · decisions · invariants · agent-instructions · relation-model` | outside the fingerprint (WAY-31) |

Renewed fingerprints (each dependant checked against the new binding part; none changes meaning):
`WAY-189` *Relations* `derives from WAY-191@d9fff88e` (its first invariants still take contrast from
the adopted WCAG); `guidelines-form`, `guidelines-check-form`, `guidelines-check-code-path` *Derives
from* `WAY-170@175a4fb6` (the exception is about the installer's block; the form and the paths are
unchanged). WAY-175, WAY-183 and `guidelines-check-carrier` are carried by no relation or link.
Versions of the invariants stay 1 (no main branch).

Choices, with cost if wrong:
1. **A1 relation.** WAY-170 keeps `derives from WAY-16`, not `narrows`: WAY-16 binds the gate, which
   no product has yet; the exception lives only until that gate, as its *Review when* says. If the
   root reads the installer's two commands as going against WAY-16's one command, the relation
   becomes `narrows WAY-16@5c1d60d4` and the binding sentence already states the area.
2. **A10, the invariant half too.** The check counts any identifier the invariants file holds,
   withdrawn ones included (`Foundation.invariant`), so "names no invariant" was false in the same
   corner; the sentence now says what the check decides for both fields.
3. **A6, *Not* none.** All 23 uses of "user interface" in `foundations/` are new and in this meaning
   (`format_guard.py --uses "user interface"`; WAY-174's "specialist of user interfaces" fits it). The
   bare "interface" of WAY-121, WAY-165, WAY-104 and WAY-49 is another word; the template's rule for
   a term's last word in another meaning is kept by writing the term whole in every use, so nothing
   is rewritten. *Avoid* none: "UI" stands only in quotations and a product name, "view" nowhere for it.

### Glossary — "user interface"

"A user interface is a set of screens that a product draws and through which a person uses it."
*Avoid* none, *Not* none. Needed by WAY-95: the binding sentences (WAY-167, WAY-183 and the others
listed by `--uses`) use the words in a narrower meaning than a reader of the field, who also calls a
terminal's prompts a user interface (root C14). Genus "set of screens" holds no term of the glossary;
no clause is a rule. No identifier reads alike.

### Polish meaning sentences

- **WAY-170:** dopóki bramka the way nie uruchamia metod niezmienników produktu, blok instalatora w
  `AGENTS.md` produktu podaje dwa polecenia skryptu formy wytycznych do uruchomienia przed każdym
  scaleniem, obok strażników formatu; wyjątek kończy się z taką bramką.
- **WAY-175:** the way przejmuje z lekcji i skilla `10x-ui` oraz ze skilli `om-ux-setup` i
  `om-ux-shape` elementy nazwane decyzjami, które je niosą (WAY-176–182, 185–187, 189, 192), a także
  paletę z kodu jako propozycję, pytanie o to, co wie tylko zespół, i pisanie dla czytelnika spoza
  rozmowy; pomija ich polecenia, listy narzędzi, moment po pierwszym ekranie, porównanie zrzutów i
  nazwę roli `surface` — z cytatami ze źródeł w *Based on*.
- **WAY-172:** bez zmiany znaczenia; *Review when* brak.
- **WAY-183:** produkt dostępny tylko przez API albo terminal nie ma interfejsu użytkownika i nie
  dostaje styleguide'a.
- **WAY-191:** domyślna rekomendacja to najnowsza edycja WCAG mająca status rekomendacji W3C (nie
  szkic) w chwili zapisania decyzji, poziom AA, wszystkie ekrany.
- **słownik, „user interface”:** interfejs użytkownika to zestaw ekranów, które produkt rysuje i
  przez które człowiek z niego korzysta.
- **`guidelines-check-carrier`:** skrypt zgłasza regułę, której pole *Decision* nie ma numeru
  decyzji z prefiksem dziennika i `@`, regułę styleguide'a, której pole *Invariant* nie ma
  identyfikatora z pliku niezmienników i `@`, oraz decyzję z tabeli ról pominiętą w regule „każda
  rola w swoim znaczeniu”.
- **`guidelines-reference-current` (*Part*):** niezmiennik obejmuje też części `agent-instructions` i
  `relation-model`.

### Wording the template and skill authors follow

- WCAG phrase (WAY-191): "the newest edition that is a W3C Recommendation when the decision is
  written".
- *Part* of `guidelines-reference-current` in the-way: `product-guidelines · decisions · invariants ·
  agent-instructions · relation-model`.

### Checks

| Command | Exit | Output |
|---|---|---|
| decision guard `--base none --merge-onto none` | 0 | [settlement-decision-guard.txt](settlement-decision-guard.txt) — 0 errors, 32 warnings (5 check-by dates, 27 request-link placeholders), 5 unchecked (no-main options) |
| invariants guard `--base none --merge-onto none` | 0 | [settlement-invariant-guard.txt](settlement-invariant-guard.txt) — 0 errors, 3 unchecked |
| glossary guard `--base none --merge-onto none` | 0 | [settlement-glossary-guard.txt](settlement-glossary-guard.txt) — 0 errors, 5 unchecked (incl. terms and identifiers read alike, `--base none`) |
| part-map guard `--base none` | 0 | [settlement-part-map-guard.txt](settlement-part-map-guard.txt) — 0 errors, 7 unchecked (flows' coverage, promise levels, dependency graph, `--base none` x3) |
| environment-facts guard `--base none --merge-onto none` | 0 | [settlement-environment-facts-guard.txt](settlement-environment-facts-guard.txt) — 0 errors, 3 unchecked |
| `python -B gate/run_tests.py elements/decisions` | 0 | [settlement-tests-elements-decisions.txt](settlement-tests-elements-decisions.txt) — 169 OK |
| `python -B gate/run_tests.py elements/invariants` | 0 | [settlement-tests-elements-invariants.txt](settlement-tests-elements-invariants.txt) — 233 OK |
| `python -B gate/run_tests.py elements/glossary` | 0 | [settlement-tests-elements-glossary.txt](settlement-tests-elements-glossary.txt) — 204 OK |
| `python -B gate/run_tests.py gate` | 0 | [settlement-tests-gate.txt](settlement-tests-gate.txt) — 98 OK |
| `python -B gate/run_tests.py product-guidelines` | 0 | [settlement-tests-product-guidelines.txt](settlement-tests-product-guidelines.txt) — 61 OK |
| fingerprint script `--from 167` | 0 | [settlement-fingerprints.txt](settlement-fingerprints.txt) — 503 relations and links, 0 stale |
| `git diff --check` (before commit) | 0 | [settlement-diff-check.txt](settlement-diff-check.txt) |

### Changed files (commit `04f8754`)

`foundations/decisions.md` 84 added, 47 removed; `foundations/glossary.md` 7 added; `foundations/invariants.md` 5 added, 5 removed.
- Root ruling on choice 1 (commit `8ff8966`): WAY-170's *Relations* now read `derives from WAY-04@29a75d2c · narrows WAY-16@5c1d60d4` — the binding sentence already states the area (the installer's block until a gate runs a product's invariants); the guard takes `derives from` and `narrows` on one entry; decision guard exit 0 (0 errors, 32 warnings, 5 unchecked), fingerprint script exit 0 (503 links, 0 stale), `git diff --check` exit 0 (reports/settlement-narrows-*.txt).
