# Report of the one author — task `glossary-three-questions`

**Status:** done

## Commits

- `24e092c` docs: glossary rules — narrower meaning, sentence test for two meanings and for process words in a product, English text only, grading of word remarks (WAY-293)

## Files changed (added / removed lines)

- `foundations/decisions.md` +~140 / -~60 (WAY-11 wording, WAY-95, WAY-97, WAY-99, WAY-104, new WAY-293)
- `elements/glossary/template.md` (48 lines touched)
- `task-cycle/review/SKILL.md` +5 / -0
- `elements/common/way_of_working.md` +3 / -2
- `elements/glossary/skill/decide_entry.md` +4 / -4 (rewrap included)
- `task-cycle/record_template.md` +2 / -2
- `task-cycle/skill/return_step.md` +2 / -2
- total: 7 files, 191 insertions, 83 deletions

## Entries written (foundation step)

All five rows are carried by edits in place of existing decisions and one new decision; no glossary entry of `foundations/glossary.md` is added or changed (no row asks for one).

| Entry | Row | English | Polish |
|---|---|---|---|
| WAY-95 (edited) | row 1 | A word the product uses more narrowly than its field takes a glossary entry only where a reader taking the field's meaning would read a sentence of the product's English files wrongly. | Słowo użyte w produkcie węziej niż w branży dostaje wpis w słowniku tylko tam, gdzie czytelnik biorący znaczenie branżowe przeczytałby zdanie angielskich plików produktu błędnie. |
| WAY-99 (edited) | row 3 and row 5 | Two uses of a word carry two meanings when a sentence the files hold is true in the meaning of one use and false in the meaning of the other (either way, never a made-up sentence), and the glossary rules bind English text, a file in another language keeping its words in that language's meaning. | Dwa użycia słowa niosą dwa znaczenia, gdy zdanie, które pliki zawierają, jest prawdziwe w znaczeniu jednego użycia i fałszywe w znaczeniu drugiego (w którąkolwiek stronę, nigdy zdanie wymyślone), a reguły słownika wiążą tekst angielski — plik w innym języku zachowuje słowa w znaczeniu tego języka. |
| WAY-97 (edited) | row 5 | The search that follows a changed definition covers the English text of the files git tracks, not text in another language. | Szukanie po zmianie definicji obejmuje angielski tekst plików w gicie, nie tekst w innym języku. |
| WAY-104 (rewritten in place) | row 4 | A word of the glossary of the-way, or the last word of its term, takes a qualifier in a sentence of a product's foundation that could otherwise be read in the other meaning, in either direction; a bare use no sentence reads two ways stays bare. | Słowo ze słownika the-way, albo ostatnie słowo jego terminu, dostaje dookreślenie w zdaniu fundamentu produktu, które dałoby się przeczytać w drugim znaczeniu, w którąkolwiek stronę; gołe użycie, którego żadne zdanie nie czyta dwojako, zostaje gołe. |
| WAY-293 (new, scope `task-cycle`, `glossary`) | row 2 | A reviewer grades a finding about a missing glossary entry or missing qualifier as Minor unless it cites a sentence a reader would read wrongly; WAY-99 renaming is graded as before and a glossary entry the change writes stays under WAY-263. | Recenzent ocenia uwagę o brakującym wpisie albo dookreśleniu jako Minor, chyba że wskazuje zdanie czytane błędnie; zmiana nazwy (WAY-99) jak dotąd, a wpis, który zmiana pisze, zostaje pod WAY-263. |

Other texts changed: `elements/glossary/template.md` ("Two glossaries", "Which words take an entry" with the new narrower-meaning rule, the sentence test replacing the `TODO — decision pending: which decision sets when two uses of a word carry two meanings`, the English-text rule, "A changed meaning"); `task-cycle/review/SKILL.md` section 3 (one sentence after WAY-263's, nothing removed); `elements/common/way_of_working.md` search bullet; `elements/glossary/skill/decide_entry.md` search line.

## Placement choices (each with the way rejected and cost if wrong)

(a) The sentence test of question 1b stands in **WAY-99** (the orchestrator's reading). Rejected: a new decision, or WAY-95 — WAY-99 already answers "when does a word carry two meanings" and its Rationale already rests on "a sentence a test cites carries its words as they stand"; a second home would make two entries answer one question (WAY-19). Cost if wrong: WAY-99 grows to carry three things (test, rename, language); a later split is a small edit.

(b) The new decision **WAY-293** carries questions 1a and 2 for the review: Minor unless a sentence is cited, with the two carve-outs, relation `narrows WAY-161` only. WAY-263 stays as it is and is named in the new decision as holding the glossary-entry case. Rejected: (i) putting the criterion into WAY-161 (WAY-263's *Rejected* already refused that for its criterion — a general rule carrying a long specific criterion); (ii) `derives from` WAY-95 / WAY-104 as well — the grading rule serves the review, not the glossary rules, and a second relation adds a link nothing reads; (iii) putting row 3's test in WAY-293 — it is about meaning, not grading. Cost if wrong: if the human reads the Minor default as not "narrowing" WAY-161 but as WAY-161 applied, the relation line changes.

(c) Row 5 (English text only) stands in **WAY-99**, with WAY-95 and WAY-97 saying "English" and referring to it, and the template stating it as a bullet. Rejected: a separate decision — the task commands narrowing WAY-99, WAY-97 and the template, so one carrier plus two narrowed references. WAY-104 needs no change for it (it reaches `foundations/`, English by WAY-72).

(d) WAY-104 *Rejected*, variant "reported as a warning rather than an error": the task asks for it "with the reason for which its cost is now acceptable". I read the cost as "one word carrying two meanings in the repository", now accepted wherever no sentence reads in the other meaning, and I kept the variant refused only for a sentence readable both ways (a mark beside the word tells the reader nothing at the use). This is my reading of an ambiguous instruction (see Searches). Cost if wrong: one clause of one *Rejected* item to reword.

(e) WAY-104 binding sentence: the qualifier goes on "the use the sentence leaves open", for either meaning, per the row ("domain use in the meaning of the process or process use in the meaning of the domain"). The old "the bare word keeps there the meaning of the process" is gone; a bare use no sentence reads two ways "keeps the meaning it has there". Rejected: keeping a default for bare words (the row has none).

(f) The *Rejected* lists of WAY-95, WAY-99, WAY-104 and WAY-293 take the "Not chosen" ways of the row's source and nothing derived (WAY-134), phrased without PR numbers, files or counts (decisions template). The only addition beyond the sources is the reason the task commands in (d).

## Searches (WAY-33) — what the search found and what I did

- Phrases of the old rules (`bare word`, `keeps there the`, `definition true of`, the `TODO — decision pending`, `two meanings`, `other than`, `last word`, `qualifier`, `every file git tracks`) and every mention of WAY-95/97/99/104/161/263 across the repository outside `.runs`, `.claude`, `.agents`.
- Changed: `elements/glossary/template.md` (all three named places plus "A changed meaning"); `elements/common/way_of_working.md:98-101` (the search bullet said every word in a meaning a reader would not give takes `record-glossary-term`; now only where WAY-95 gives an entry); `elements/glossary/skill/decide_entry.md:10` (search every file → English text); WAY-11 (`foundations/decisions.md`, "a meaning other than the usual one" → "a meaning for which WAY-95 gives it an entry"), `task-cycle/skill/return_step.md:10` and `task-cycle/record_template.md:154` which restated WAY-11's loose phrase more broadly than the narrowed WAY-95 (same reasoning as WAY-263: a second account broader than the entry). The meaning of WAY-11 is not moved; it now defers to WAY-95.
- Looked at and left alone: `foundations/decisions.md` WAY-93 (line ~1987) and WAY-176 (~4958, cites WAY-104 for a product's code using its own words — still true), WAY-240 (~6858, "integration" as a term defined by resources; a level name it requires to be a glossary term regardless — a decision of its own about test levels, not a restatement of WAY-95 — see Searches), WAY-94 and the template's *Not* bullet ("the files git tracks" for the meanings a word carried — outside the task's list), `README.md:39` and `:76` (loose summary of the glossary, "other than usual"), skill front matter (`description` of `record-glossary-term`: "something other than a reader of its field takes it to mean" — a description is not the rule, changing it would need `skill_entry_points.py --write` and I judged it unneeded), `product-guidelines/testing/settle.md:9` and `template.md:111` (same as WAY-240), `foundations/glossary.md` (no entry affected; no entry's definition changed).

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py .` -> `0 errors`, exit 0 (run on the worktree after the final edits).
- `python -B gate/run_tests.py task-cycle` -> exit 0 (92 tests OK in the earlier run, exit 0 again after the final edits).
- `python -B gate/run_tests.py elements/common` -> exit 0 (after the final edits).
- Not run: the full `python -B gate/run_tests.py` (the orchestrator's run, step 10); no test written first, because the change is prose and no invariant is added.
- First attempt `python -B gate/run_tests.py elements/common task-cycle` exited 2: the runner takes one directory; I ran them separately.

## Own-work check

Requirement most likely unmet: the task's test of question 2 and 1b "works in both directions and only on sentences the files already hold" — a rule that is stated in one direction in one of the places (WAY-99, WAY-104, the template) or an old rule left standing elsewhere.
Check: (1) read each of the three places for both directions: WAY-99 "whichever of the two the sentence uses ... a sentence made up for the test does not count"; WAY-104 "a sentence that uses the word for the product's domain and could be read as the process's, or one that uses it for the process and could be read as the domain's"; template bullets restate both. (2) grep for the old rule's phrases across the repository (list above): the only hits left are the new text and unrelated `TODO — decision pending` in the environment-facts template. (3) apply the new text to the task's two examples: loop2 `foundations/decisions.md:2166` ("leaving the sentence unchanged", process use readable as a message to the player) takes a qualifier under WAY-104; bare "map" for the game's map, readable by no sentence as the part map, stays bare — both decided by the text without further judgment. (4) WAY-263's paragraph in the review skill and WAY-263's entry are byte-for-byte unchanged (`git diff` of `task-cycle/review/SKILL.md` has no removed line; no hunk in WAY-263).
Showed: (1)-(4) hold. What the text does not decide: whether "could be read" in WAY-104 asks for a plausible reader's confusion or any logical possibility; the example sentences give the bar (a reader of the field would take it so), the text does not say it again.

## Reaches beyond the handoff

- `elements/glossary/skill/read.md`, `write.md`, `decide_entry.md`, and `elements/common/skill/SKILL.md`, `task-cycle/skill/return_step.md`, `task-cycle/record_template.md` — to see whether they restated the rules (search); `elements/decisions/skill/read.md`, `decide_entry.md` and `template.md` — as the decisions skill's steps 1 and 2 require, and the decisions template for *Rejected* of a row's decision.
- Next free decision number: the end of `foundations/decisions.md` and its withdrawn table (WAY-293 free).

## Searches not found or unclear

- The handoff's "decisions lines near 1981–2008, 4958, 6858" were found (WAY-93, WAY-176, WAY-240). Only WAY-240 has a rule shaped like WAY-95 ("a level whose name means in the product something other than in the field ... is a term of the product's glossary"); I left it, since it fixes a particular case (test levels) in a product's guidelines and the task does not name it. It now reads as stricter than WAY-95; the human may want it aligned in a later change.
- The task's instruction that the *Rejected* of WAY-104 keep the variant "reported as a warning rather than an error" "with the reason for which its cost is now acceptable" is ambiguous (whose cost). I took it as the variant's cost (placement choice d).
- No test or script checks a rule of this change; focused tests only confirm the foundation and templates still parse.
- The handoff says "WAY-07" among the entries to edit; WAY-07 (edit in place) needs no change and was not edited.
- `agent-instructions/README.md` says the integration route; I made no request.
