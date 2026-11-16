# Author correction report — correction 1, decision-sources-and-leftouts

**Status:** done

Commit `d48638a` — "Correction 1: name the course practice that WAY-139, WAY-145 and WAY-165 take,
and what they leave out" — `foundations/decisions.md`, 42 added, 14 removed lines; on
`task/decision-sources-and-leftouts` above `b679864`. Not pushed.

## The remarks, as made, and how

1. "The three decisions that seem to take part of a course practice and say nothing about it … —
   **fix them in this request.** … Follow the same rule as the other entries: the source the
   practice was in fact taken from, the leftovers in *Rejected*, a reason only where the entry, the
   source or the author's map gives one. If for one of the three no taking can be traced, say so in
   the request and leave that entry as it was." — **Done.** A taking was traced for all three; each
   now names its practice, says its lessons are not open to a reader, lists its leftovers and
   derives from WAY-100. Below, decision by decision.
2. The unread reading — not mine (the fresh reviewer's); not touched.

## The three decisions

| Decision | Where I searched | What I found, and where in the source | Adopts? | *Based on* | *Rationale* | *Rejected* | *Relations* |
|---|---|---|---|---|---|---|---|
| WAY-145 | `git log` of the entry (`97b7212`, `e8629d5`, `4e6b53c`, `8d04d89`: it never named a practice nor derived from WAY-100); the author's map of the course package, lesson m2l1, row "Blokery zewnętrzne odróżnione od niewiadomych…" (verdict "przejmuję w zmienionej postaci", carrier WAY-145) and its note on trial A (the skill moved the definition's questions silently; the-way moves them openly, with a line in the log); the course skill `10x-roadmap` from the local archive of course trials, Step 6e–6g and the template of "## Open Roadmap Questions" | 6f: "PRD's `## Open Questions` — copy verbatim … New questions surfaced during Step 5"; 6e: per-slice Blockers (external: vendor, design, stakeholder) and Unknowns with owner and Block flag; 6g: Parked | **Yes**, in changed form: the source's open questions carried into the plan word for word, and a question the breakdown raises put before the human. The written move with its reason is the-way's own | unchanged `none` (course closed) | + what it takes from the practice (WAY-142 describes it), its lessons not open, the logged move the rule's own | existing "flag … beside a list of deferred work" marked "as the practice of a roadmap has them"; + external blockers kept apart from unknowns; + an owner for each unknown | + `derives from WAY-100` |
| WAY-139 | `git log -S "how long the record lives"` → `4a3ee37` (the entry then derived from WAY-100), `8d04d89` and the second-round foundation report (`cfd275c`), row F3 (c), which removed `derives from WAY-100` ("the entry no longer claims to adopt a practice from outside"); the map, lesson m1l5, row "`infrastructure.md` jako trzeci kontrakt" (verdict "przejmuję w zmienionej postaci" → WAY-139: "the way … spisuje listę elementów, które skill wdrożeniowy produktu powinien mieć (z lekcji i A): podgląd wdrożeń, gdzie leżą sekrety i jak je obracać, cofanie …, co robi agent, a co człowiek, jak czytać logi"); lesson m3l5 rows 4, 7, 8 (carrier "WAY-165, WAY-270, WAY-139"); the lesson note m1l5, section "infrastructure.md - nowy kontrakt", read whole | The lesson's skeleton of the document: choice and justification, stack fit, CLI/MCP/API fit (logs through an API), preview of deployments, secrets, rollback (minutes and steps), permissions (which actions take a human), risks, technical decisions (region, runtime, plan), signal of a change of the decision | **Yes**: five items of its list from the m1l5 document, two from m3l5 (as WAY-270 already says) | unchanged `none` | + what the list takes from m1l5 and m3l5, lessons not open | existing "a document of operations kept beside the product" marked as the lesson's document; + platform chosen and its reasons (reason from the map row: the decisions carry a choice and its reasons); + stack fit; + known risks; + region, runtime, plan; + signal that would change the choice | + `derives from WAY-100` |
| WAY-165 | `git log -S "how long the record lives"` → `4a3ee37` (added the record's life and `derives from WAY-270`); WAY-270's *Rationale* ("they bind by this decision, by WAY-165 and by WAY-139, and nowhere else"); the map, lesson m3l5, rows 4, 7, 8; the lesson note m3l5, sections "Dane o zgłoszeniu i działaniu aplikacji" and "Observability - klucz do efektywnego debugowania" | The lesson weighs the platform's log retention; its table of sources of a diagnosis: report with screenshot, logs and stack trace, request identifiers, technical and business metrics, history of changes and deployments; map row 4: the identifiers live in code and go to the guidelines | **Yes**: the question of how long the record lives | unchanged `none` | + the record's life comes from lesson m3l5, lessons not open | existing "what the product logs and in what form" now names the lesson's identifiers of requests among it (reason the entry's own); + metrics; + history of changes and deployments | + `derives from WAY-100` |

**Contradiction with the frozen task, named:** the task's *Out of scope* lists WAY-139 among the
decisions that "use the source as evidence, not adopt a practice from it" — the judgment of the
second round of the log (row F3 (c)). The trace contradicts it (the map's m1l5 and m3l5 rows carry
the taken items to WAY-139, and the entry itself derived from WAY-100 until that round), and the
human's later remark names WAY-139 among the three to fix. I followed the remark.

**Not changed, though related:** WAY-142 already lists the parked list and the blocked state among
what it leaves out, and WAY-145 now marks the same two as the practice's in its own *Rejected*. The
two do not contradict each other; I left WAY-142 as it is (the handoff: change the 25 entries only
where needed), and N1 stays with the request's list.

## Meaning and mark of each entry

- WAY-145 — `the cycle's` (no row carries it). EN: The rule on where an open question of a project
  is resolved takes from the course's roadmap practice the carrying of each open question into the
  plan word for word and the new question put before the human, and leaves out its external
  blockers and its owner of each unknown. PL: Reguła o tym, gdzie rozstrzyga się otwarte pytanie
  projektu, bierze z praktyki roadmapy z kursu przeniesienie każdego otwartego pytania do planu
  słowo w słowo i nowe pytanie postawione człowiekowi, a pomija jej blokery zewnętrzne i właściciela
  każdej niewiadomej.
- WAY-139 — `the cycle's`. EN: The list of what a product's deployment skill covers takes five items
  from the course's document of a product's infrastructure and two from its lesson on debugging, and
  leaves out the platform choice and its reasons, the fit of the stack, the risks, the region and
  plan, and the signal of a change. PL: Lista tego, co obejmuje skill wdrożeniowy produktu, bierze
  pięć pozycji z kursowego dokumentu infrastruktury produktu i dwie z lekcji o debugowaniu, a pomija
  wybór platformy z uzasadnieniem, dopasowanie stosu, ryzyka, region i plan oraz sygnał zmiany.
- WAY-165 — `the cycle's`. EN: The matter of the logs takes from the course's lesson on debugging
  the question of how long the record lives, and leaves out the lesson's metrics and history of
  changes as sources of a diagnosis. PL: Kwestia logów bierze z lekcji kursu o debugowaniu pytanie,
  jak długo żyje zapis, a pomija metryki i historię zmian, które lekcja liczy do źródeł diagnozy.

No pair of examples was added or changed, so nothing is to be quoted under the entries.

## For the request's table

Three rows to add: WAY-139, WAY-145, WAY-165, as in the table above. Nothing changes for WAY-138,
142, 143, 268 or 270.

## Checks

| Command | Exit | Result |
|---|---|---|
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `python -B .runs/author/compare_binding.py . aba5ee92a0734c2e775cc69662af669bf6455795` | 0 | binding changed vs base: `['WAY-100']` only; entries changed vs `b679864`: `['WAY-139', 'WAY-145', 'WAY-165']`; none added or removed |

Not run: the full gate (the orchestrator's).

## Own-work check

- Requirement most likely missed: the human's "a reason only where the entry, the source or the
  author's map gives one", and no binding sentence changed.
- Check: each reason compared with its place — WAY-139's reason for the platform choice is the map's
  m1l5 row ("wybór i jego powody niosą decyzje the way"); WAY-145's and WAY-165's marked positions
  keep their existing reasons; every other new item has none. The script above for the binding
  sentences and for the set of entries changed.
- Result: reasons all traced; binding sentences unchanged outside WAY-100; only the three entries
  changed.

## Working copies

`.runs/author/` recreated for a copy of the course skill `10x-roadmap` (from the local archive) and
the comparison script; removed with `rm -rf` before returning. `.runs/pp_list.txt`, which I did not
make, is left in place.

## Unread material

- The lesson note m3l5: read by headings and the two sections named above, not whole.
- The skill `10x-roadmap`: Step 6e–6g, the template of "Open Roadmap Questions" and the field rules;
  not whole.
- The reviewer's reports (`review-whole-report.md`, `review-fix-report.md`): not read; the handoff
  quotes finding O1's places.

## Searches not found or unclear

- The lesson "Towards Autonomous Product Development" behind WAY-121 may also be where WAY-165's
  other matters (interface, development data) come from; WAY-121 already credits that lesson for
  them, and WAY-165 derives from WAY-121, so I credited WAY-165 only with what the trace ties to it
  (the record's life, from m3l5).
