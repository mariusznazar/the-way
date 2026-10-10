# Foundation step — m1l5-adoptions

- Agent: foundation agent, claude-opus-5-5
- Skill: `elements/decisions/skill/SKILL.md` of this worktree, with `elements/common/way_of_working.md`,
  `elements/common/rules.md`, `elements/decisions/template.md`, `elements/decisions/examples.md` (WAY-03)
- Read: frozen task in full; plan § Foundation entries; decisions WAY-03, WAY-04, WAY-07, WAY-12,
  WAY-24, WAY-27, WAY-32, WAY-100, WAY-113, WAY-120–WAY-126, WAY-128, WAY-129, WAY-134–WAY-136;
  glossary in full; part map (parts); `project-level/technology/SKILL.md` steps 1–3;
  `task-cycle/skill/SKILL.md` lines 10–25, 44–48, 64–70
- Commit: `53b3827132664fb820b64734a603716537dc53dc` on `task/m1l5-adoptions` (only `foundations/decisions.md`)
- Commit message file: `.runs/task-cycles/m1l5-adoptions/commit-foundation.txt`

## Entries

| Entry | Question | Fingerprint | Relations | Scope |
|---|---|---|---|---|
| WAY-137/1 | What decides between places to run that the simplest and cheapest option leaves tied? | 86b2a30d | derives from WAY-100@e7a74a18 · narrows WAY-123@f3b45293 | project-level, decisions |
| WAY-138/1 | Which option of a technology choice is tested for what choosing it could break, and where do the risks found go? | 414f7dbd | derives from WAY-100@e7a74a18 · WAY-122@b343277a · WAY-123@f3b45293 | project-level, decisions |
| WAY-139/1 | What does the-way hold for the skill that deploys a product, and which step checks that a product has one? | 90e87598 | derives from WAY-100@e7a74a18 | project-level |
| WAY-140/1 | How does a task change something outside the product's repository? | d02ede05 | derives from WAY-100@e7a74a18 · WAY-125@441e3a6a | project-level, task-cycle |
| WAY-124/1 (edited in place) | When is a task ready for its cycle? | 9eaf23e6 (was f1687673) | + derives from WAY-140@d02ede05 | unchanged |

All: *Based on* `none`, *Origin* `none`, *Approved by* `Mariusz, merge of <request link>`,
*Verification* level 2 with complies/violates examples written for each rule. *Review when*: `none`
except WAY-138 (row 2's scope condition, check by 2026-12-31).

## Meaning sentences (Polish, for the request)

- **WAY-137** — Przy miejscu uruchomienia, gdy po regule „najprostsza i najtańsza” (WAY-123) nadal
  jest remis, krok technologii poleca opcję, z którą agentowi pracuje się najlepiej (obsługa z
  terminala, wdrożenie skryptem, dokumentacja czytelna dla agenta); poza tym ta cecha niczego nie
  odsiewa i nie jest ważona wobec skutków dla produktu.
- **WAY-138** — Krok technologii poddaje opcję zalecaną każdego wyboru rozstrzyganego w projekcie
  (także wziętego z ograniczenia) testom „co to zepsuje” — adwokat diabła, pre-mortem, nieznane
  niewiadome — nigdy wyborów trzymanych przez zastane decyzje ani wstecz; ryzyka to hipotezy bez
  źródła, których krytyka nie skreśla, człowiek widzi je w tabeli przy opcji zalecanej przed wyborem,
  a wybierając ją, przyjmuje je i trafiają do *Rationale* decyzji obok braków opcji, oznaczone jako
  hipotezy; zakres wraca do przeglądu, gdy testy poza miejscem uruchomienia nie dadzą nowego ryzyka
  (sprawdzić do 2026-12-31).
- **WAY-139** — The way nie zawiera skilli produktu, tylko listę tego, co ma pokrywać skill
  wdrożeniowy produktu (podgląd wdrożeń; gdzie leżą sekrety i jak je obracać; cofanie — ile kroków,
  co z danymi; co robi agent, a co człowiek; jak czytać logi); `refine-task` przy zadaniu, które
  wdraża produkt albo zmienia, jak i gdzie działa, sprawdza pokrycie listy, a brak daje punkt w To
  do albo osobne zadanie wydzielone przez człowieka.
- **WAY-140** — Skutek zadania poza repozytorium (serwer, DNS, klucze, zewnętrzne konto) wykonuje
  tylko człowiek, jako czynność nazwaną w dokumencie zadania — przed cyklem (zadanie nie jest gotowe,
  dopóki jej nie zrobi) albo w cyklu (cykl robi, co da się w repozytorium, i oddaje zablokowany szkic
  PR z listą czynności, które człowiek wykonuje przy PR-ze); odczyty zostają agentowi; miejsce każdej
  czynności rozstrzyga człowiek przy doprecyzowaniu, na propozycję agenta („przed”, gdy kod cyklu
  potrzebuje jej skutku; „w cyklu”, gdy czynność korzysta z kodu cyklu).
- **WAY-124 (zmiana sensu)** — Zadanie jest gotowe do cyklu dopiero, gdy każda czynność człowieka,
  którą dokument zadania umieszcza przed cyklem, jest wykonana (WAY-140); reszta bez zmian.

## Choices made under the orchestrator's delegation

1. Wording of every binding sentence (WAY-134), checked against rows 1–5 clause by clause.
2. WAY-137's second sentence limited to a place to run ("For a place to run, how well an agent
   works with an option decides nothing else"): a first draft said the property decides "nowhere
   else", which would collide with WAY-122, whose properties for a language, framework, library or
   store of data already bear on how well an agent works in the stack.
3. WAY-138's *Review when* wording: "the tests run on choices other than a place to run give no
   risk that the comparison of their choice did not already show, and the tests then narrow to a
   place to run · check by: 2026-12-31" — no count of projects added, since the row gives none.
4. WAY-138 derives from WAY-122 and WAY-123 (it adds a check before the human sees the options and
   serves the table with recommendation and weak point); no `narrows WAY-120/WAY-122`, since the
   binding sentence states the risks are not claimed differences, so WAY-122's critique does not
   apply to them — no collision to record.
5. WAY-140 derives from WAY-125 (blocked draft request, single review point); WAY-125 unchanged.
   WAY-140 cites WAY-124 in its binding text and WAY-124 derives from WAY-140 — a citation, not a
   relation, so no pair of relations.
6. WAY-124: the readiness condition placed among the existing conditions with "(WAY-140)"; one
   sentence added to its *Rationale*; verification examples extended (complies: external account
   opened before readiness; violates: ready while a before-cycle action is undone).
7. Scope of WAY-139 is `project-level` only (`refine-task` lives there); WAY-140 `project-level,
   task-cycle` as WAY-124.
8. Verification level 2 for all: each rule binds the judgment of an agent in technology research or
   refinement and the content of a task document kept outside the repository, so no sentence a
   commit of the-way makes false was found; no invariant written (plan *Choices*).
9. Rationale examples chosen for the rule's range (a plan with no backup, a framework dropping a
   driver, a free tier below expected traffic; a mail service account, a DNS record, free disk
   space), not taken from the trial evidence; no course or file outside the repository cited (WAY-27).

## Foundation search (WAY-33)

- WAY-04 rejects assumptions as a kind of entry: WAY-138 keeps risks inside the chosen option's
  decision and names WAY-04 in *Rejected*. No collision.
- WAY-122 rationale ("a place to run ... weighed by its consequences alone"): rationale, not binding;
  WAY-137 narrows WAY-123's binding "decides nothing" for the tie only. No change to WAY-122.
- WAY-24: WAY-138's review condition carries a check-by date.
- Glossary: no term used in another meaning; no *Avoid* word used; glossary guard 0 errors, 0 warnings.
- Carriers of WAY-124's fingerprint: `grep -rn 'WAY-124@' foundations/` → no match (exit 1); no
  invariant names WAY-124. Every relation fingerprint in the log matches its target's current
  fingerprint (scratch script over the guard's parser: 0 stale), since the guard leaves that unchecked
  with `--merge-onto none`.

## Checks

| Command | Exit | Result |
|---|---|---|
| `python -B elements/decisions/format_guard.py --base none --merge-onto none` | 0 | 0 errors, 10 warnings (5 passed check-by dates WAY-03, 21, 52, 55, 69; 5 `<request link>` placeholders: WAY-124, 137, 138, 139, 140), 5 unchecked (no main branch) |
| `python -B gate/run_tests.py elements/decisions` | 0 | 169 tests OK |
| `python -B gate/run_tests.py gate` | 0 | 98 tests OK |
| `python -B elements/glossary/format_guard.py --base none` | 0 | 0 errors, 0 warnings |
| `python -B elements/part-map/format_guard.py --base none` | 0 | 0 errors, 0 warnings |

## Questions for the orchestrator

- None blocking. Proposed for the request: list WAY-124 among the entries whose meaning the human
  accepts again at the merge (WAY-07), and replace the five `<request link>` placeholders once the
  request exists.
