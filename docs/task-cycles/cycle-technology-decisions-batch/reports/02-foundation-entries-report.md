# Report — foundation entries (the foundation step of the plan)

**Status:** done with concerns (one concern, under "Searches not found or unclear": the family of matters in row 1).

Worktree `the task's worktree root`, branch `task/cycle-technology-decisions-batch`, base `f238e4ffdfc2396ae0009fefa90b3af8d1e931e1`. Only `foundations/decisions.md` is changed (+about 120 lines, -about 30). Every entry is an edit in place except row 1, which is the new decision WAY-322 (the next free number; no withdrawn number holds it).

## Entries

Each entry: its mark, the decision, one sentence in English, one in Polish, the commit.

1. `row 1` — **WAY-322 (new)** — `f3b90d5`
   - EN: A matter of an agent's way to the running product that the technology step lists, and the matter of how a human learns of a failure, cannot be struck from the list; a human to whom it does not apply answers it like any choice, the answer settles it, and a resumed run does not list it as open again.
   - PL: Sprawy drogi agenta do działającego produktu, które krok technologii wymienia, i sprawy powiadamiania o awarii nie da się wykreślić z listy; człowiek, którego sprawa nie dotyczy, odpowiada na nią jak na każdy wybór, odpowiedź ją rozstrzyga, więc przy wznowieniu nie wraca jako otwarta.
   - Judgement (WAY-33, WAY-07): a new decision, not an edit of WAY-121 or WAY-165. The search of the whole foundation finds no sentence stating it (grep for "strike", "struck", "from the list", "leaves out", "confirm it"); WAY-121 states only that a matter is listed even where the product has none of what it names, WAY-270 that the failure matter is listed. The question (may a human strike a listed matter) is a new one beside WAY-121's (where a project settles technology), so WAY-19 gives it a number; WAY-121's single binding sentence is already too long to carry it. *Relations:* derives from WAY-121, WAY-165, WAY-270. *Rejected* holds the two ways of the task's question 1, "Not chosen". No invariant: the rule is checked by review, and the foundation step writes an invariant only for a rule the task sets as one.
2. `row 2` — **WAY-166 (edit in place)** — `2ec17d4`
   - EN: Where no option of an agent's way to the running product can be used by an agent, the recommendation goes by the other consequences and says in one sentence that no option lets an agent check the running product this way, so the check stays with the human.
   - PL: Gdy żadna opcja drogi agenta do działającego produktu nie pozwala agentowi jej użyć, rekomendacja idzie według pozostałych skutków i mówi jednym zdaniem, że żadna opcja nie pozwala agentowi sprawdzić działającego produktu tą drogą, więc sprawdzenie zostaje przy człowieku.
   - Edited in place because WAY-166 already answers the question (how the agent's use of an option weighs); the row adds the case where every option is passed over. *Rejected* gained the three ways of the task's question 2; the weak point of the way chosen stands in *Rationale* as a price. Item 18 (below) is in the same commit.
3. `row 3` — **WAY-139 (edit in place)** — `a0c6607`
   - EN: The deployment skill's item "how to read the logs" is tied to the decision on the logs like the items on the record's life and on a failure: a decision of the foundation or an approved definition that answers it is quoted and the task gains the item that writes it into the skill, a logs decision silent on how an agent reads the logs answers nothing, and without such a decision the item goes as the other items of the list.
   - PL: Pozycję skilla wdrożenia „how to read the logs" wiąże się z decyzją o logach tak jak pozycje o życiu zapisu i o awarii: decyzja fundamentu albo zatwierdzonej definicji, która odpowiada, jest cytowana, a zadanie dostaje punkt przepisujący odpowiedź do skilla; decyzja o logach milcząca o tym, jak agent czyta logi, nic nie rozstrzyga, a bez takiej decyzji pozycja idzie jak inne pozycje listy.
   - *Relations* gained `derives from WAY-165` (it is the source of the answer). *Rejected* gained the two ways of the task's question 3.
4. `row 4` and `item 24` — **WAY-148 (edit in place)** — `a407365`
   - EN: Every task-cycle stage that runs a test or another check, not only a stage that checks the product, gives the one-line check result in its short return.
   - PL: Każdy etap cyklu, który uruchamia test albo inne sprawdzenie, a nie tylko etap sprawdzający produkt, podaje w krótkim zwrocie jednolinijkowy wynik sprawdzeń.
   - "of the product" removed from the binding sentence; *Rationale* gained the reason and the price (a stage that runs no check gives no line); *Rejected* gained the two ways of question 5. The planner's skill stays, as the task says.
5. `row 5` — **WAY-294 (edit in place)** — `932726d`
   - EN: The stage reports the remarks check reads are the `.md` files of the cycle's `reports/` directory whose name holds neither `handoff` nor `findings`.
   - PL: Raportami etapu, które czyta skrypt uwag, są pliki `.md` z katalogu `reports/` cyklu, których nazwa nie zawiera ani `handoff`, ani `findings`.
   - Edited in place: WAY-294 says "the record's stage reports" without defining them; the search found no other entry that does. *Verification* carries the file names of the task's item 8. *Rejected* holds the two ways the row's source keeps (exit code 2 on no report; a "not read" line in the listing), each with its reason, with no file or script named. Whether the name match is case-sensitive is left to the code (slice 4) and not written in the entry.
6. `item 17` — **WAY-165 (edit in place)** — `e651200`
   - EN: The data set up from scratch and the dedicated test environment that persists are examples of options of the development data, none ruled out (the options come from the research, WAY-122), and the citation of WAY-270 no longer stands on the sentence about an entry that answers part of a matter but on the sentence about the record's life, which WAY-270 does state.
   - PL: Dane stawiane od zera i trwałe środowisko testowe są przykładami opcji danych deweloperskich, żadna nie jest wykluczona (opcje daje badanie, WAY-122), a odesłanie do WAY-270 nie stoi już przy zdaniu o wpisie odpowiadającym na część sprawy, tylko przy zdaniu o życiu zapisu, które WAY-270 rzeczywiście mówi.
   - Point 1 (examples): changed in the binding sentence and in *Rationale*. Point 2 (the reservation "opens only on the human's word"): **changed nothing** — the current WAY-165 has no such wording; it already says the step "may open a decision of the foundation" (WAY-313), and only decisions of the foundation. Point 3: "(WAY-270)" removed from the sentence on an entry that answers part of a matter; the relation `derives from WAY-270` is kept because the sentence on a record that dies with each deployment rests on WAY-270's rationale and its adoption of the question of the record's life, and the citation now stands there.
7. `item 18` — **WAY-166** — `2ec17d4` (same commit as row 2)
   - EN: The example of compliance has the server container's output kept in a store that outlives a redeployment.
   - PL: Przykład zgodności ma wyjście kontenera serwera trzymane w magazynie, który przeżywa ponowne wdrożenie.
8. `item 19` — **WAY-128** — `111b655`
   - EN: The closing sentence on process skills and their entry points names WAY-259 as well as WAY-35, WAY-127 and WAY-256.
   - PL: Zdanie końcowe o skillach procesu i ich punktach wejścia wymienia także WAY-259 obok WAY-35, WAY-127 i WAY-256.
9. `item 20` — **WAY-292** — `a8562d7`
   - EN: *Verification* says the form check reports the repeated block wherever it reads the task document as English.
   - PL: *Verification* mówi, że skrypt formy zgłasza powtórzony blok wszędzie tam, gdzie odczytuje dokument zadania jako angielski.
10. `item 21` — **WAY-05** — `85c5395`
    - EN: *Verification* holds two pairs of `complies`/`violates`, one for the fields and one for the rationale, in the form WAY-29 already uses.
    - PL: *Verification* ma dwie pary `complies`/`violates`, jedną dla pól i jedną dla uzasadnienia, w formie, której już używa WAY-29.
11. `item 22` — **WAY-293** — `0b84bb5`
    - EN: *Rationale* gives the reason without describing what the request template does or lacks, and the rejected way "no change" says that no change leaves the return step without a precedence.
    - PL: *Rationale* podaje powód bez opisu tego, co robi albo czego nie ma szablon opisu PR-a, a odrzucona droga „no change" mówi, że brak zmiany zostawia krok powrotu bez pierwszeństwa.
    - The two sentences that described the request ("the request puts it before the human…", "the human sees, at the merge, … no line saying it has no entry") are replaced by a citation of WAY-287 and by "nothing in the foundation says the choice has no entry". The old reason of the rejected way ("small remarks keep coming in requests… with no harm to the product") is dropped, because it is the reason the task replaces.
12. `item 23` — **WAY-287** — `a8562d7` (same commit as item 20; the message names both)
    - EN: The list of what the section for the human's decisions holds names also a listing of the remarks check that the cycle holds wrong (WAY-295) and an error of the form check that the cycle holds wrong (WAY-291).
    - PL: Lista tego, co mieści sekcja decyzji człowieka, wymienia też listing skryptu uwag uznany za błędny (WAY-295) i błąd skryptu formy uznany za błędny (WAY-291).
    - One example added to *Verification*.

All twelve entries are written. None is marked `the cycle's`; none raised a question for the human.

## Commits (base `f238e4f`, oldest first)

`85c5395` item 21 · `111b655` item 19 · `a407365` row 4 / item 24 · `2ec17d4` row 2 and item 18 · `e651200` item 17 · `a0c6607` row 3 · `a8562d7` items 20 and 23 · `0b84bb5` item 22 · `932726d` row 5 · `f3b90d5` row 1.

Files added with `git add foundations/decisions.md`. Commit `a8562d7` was amended once, before anything else was built on it, to name both entries it holds; no other commit was amended.

## Checks

| Command | Exit code |
|---|---|
| `python -B elements/common/foundation_check.py --skip-test-citations` (run after each entry, and at the end on the last commit; output `0 errors`) | 0 |
| `git diff --check f238e4f..HEAD` | 0 |

`python -B gate/run_tests.py` was not run (the handoff forbids a full run); no focused test is called for by an edit of the decision log alone.

## Own-work check (`task-cycle/change/SKILL.md`, section 3)

- Requirement most likely not met: WAY-05 on the text I wrote myself (*Rationale* and *Rejected* name no file, script or count, and say nothing of what the process's tools do or lack today; no account of how a decision was reached). Check: I listed every added line that holds the words script, file, template, tool (`git diff f238e4f..HEAD`, filtered). Result: only generic uses ("the files the cycle names otherwise", "the templates and the readiness check" in the *Rejected* of WAY-322, which restates the cost the task's question 1 keeps); no path, script name or count. The "readiness check" in that cost is quoted from the row's source. Second check: `grep` for "only on the human's word" and "no change, which withdraws" in `foundations/decisions.md` finds nothing, so the old wordings are gone.
- Second requirement: row 1 must change no meaning. See the concern below.

## Searches not found or unclear

- **Row 1 and the family of matters.** The task and the plan name the four matters as logs, interface, development data and failure notice. The base already holds a further matter in the same family, the place of the screenshots (WAY-121, WAY-165, `project-level/technology/running_product.md`), added after the task text was written. WAY-322 is worded by the family as the foundation holds it ("a matter of an agent's way to the running product that the step lists") plus the failure matter, so it covers the screenshots matter too. I judged that a rule on three of four matters of one listed family would contradict itself; this goes slightly beyond the words of the row. Recommendation: accept; the cost of narrowing is a second decision later for the screenshots. The orchestrator should confirm, and slice 6 must word `list.md`, `start.md` and `running_product.md` by the same family.
- The decision's text of the task's quotes are from `a3206c1`; the base differs in WAY-121 (four matters including screenshots), WAY-165 (no "only on the human's word"), WAY-293 and WAY-294 (unchanged). Item 17 point 2 is met by the base and changed nothing.
- No source found for the cause of the old "small remarks keep coming in requests" reason in WAY-293; I dropped it rather than guess.
- `elements/decisions/examples.md` names only WAY-03; the form of two pairs in *Verification* was taken from WAY-29, found by a search of entries with two `complies` lines (also WAY-90 and WAY-127).
- None else.

## Reaches beyond the handoff's reading list

- `elements/common/rules.md` and `elements/common/way_of_working.md` whole (the decisions skill's step 1 names them).
- `foundations/decisions.md`: WAY-317 and WAY-319 (read whole, because they concern the agent's way and screenshots), WAY-29 and WAY-90 (whole, for the form of two pairs), a search of the text of WAY-308 and the entry that cites WAY-139 around line 5760 (a standing-checks decision) for references to the changed entries; also grep over all of `foundations/*.md` for references to WAY-05, 128, 139, 148, 165, 166, 287, 292, 293, 294 and for "strike", "check result", "ends in report".
- `project-level/technology/list.md`, `start.md` and `running_product.md` (read, not changed) to see how the step names its matters, which is how I found the screenshots matter.
- `foundations/invariants.md` read whole instead of by `- **Part:**` (it is short); no invariant derives from the changed decisions, and no invariant was added or changed.

## Choices (way rejected, cost if wrong)

- Row 1 a new decision, not an edit of WAY-121: rejected the edit because WAY-121's one binding sentence is already very long and a new rule beside a decision is a new question (WAY-19). If wrong: one more entry to merge into WAY-121 later.
- Row 5 an edit of WAY-294 and not a new decision: rejected a new decision because the rule is a definition of a term WAY-294 already uses. If wrong: a reader looks in WAY-294 for a term it defines.
- Row 3 `derives from WAY-165` added to WAY-139: rejected leaving the relation out because the logs answer comes from WAY-165. If wrong: a removed relation.

## Problems observed

None beyond the above. Lines in WAY-294's first paragraph are about 115 characters long in one place (not reflowed); the check does not mind.
