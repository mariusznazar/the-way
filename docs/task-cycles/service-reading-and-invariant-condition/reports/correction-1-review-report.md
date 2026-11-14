PASS 43ffa5a85bc567dde0e1b2a26bf88ebe6a3139d6

# Review for correction 1: the fourteen unread decisions against the whole change

Range `0e1cd3cd804433f7a82ffb631e96917ef74c1040..43ffa5a` (commits `19efdfd`, `8680824`, `4f26b6b`, `43ffa5a`). `git rev-parse HEAD` in the worktree is `72b354d`, not `43ffa5a`: the two commits after `43ffa5a` add and remove the record's copy, and `git diff 43ffa5a HEAD` is empty, so the tree I read is the tree of `43ffa5a`. Worktree status was clean before and after my work; I changed nothing in it.

Counts: blocking 0, Minor within the task 2, out of scope 1.

Remark 1 of the human (item 1 of *Fix or let through*), word for word in `reports/correction-1-remarks.md`: a fresh reviewer reads whole the fourteen decisions and compares the example pairs of WAY-56 and WAY-73 with the new invariant; the correction fixes what that reading finds. The reading is made (below). It finds no Critical or Important defect, and three smaller points that the earlier reviews could not have found without it.

## Findings

### Blocking

none.

### Minor, within the task

**M1 — WAY-60 and the invariants template now tell a writer to put an identifier in the sentence, while WAY-56 and the template line that cites it say the links stand beside the sentence, not inside it, and nothing says the two do not collide.**

- Places: `foundations/decisions.md` WAY-60, first paragraph, last sentence ("…names by identifier the entry or the decision that holds the condition, in a field where the template gives one and otherwise in its sentence"), and its *Verification* complies example ("names that decision's number in its sentence, its template giving no field for it"); `elements/invariants/template.md:81-83` ("…and otherwise in the sentence (WAY-60)"). Against: WAY-56 binding paragraph ("The method of checking and the links that WAY-08 and WAY-17 require stand beside that sentence, not inside it") and `elements/invariants/template.md:74-78` ("The method and the links stand beside it, not inside it (WAY-56)"), five lines above the new text. WAY-60 itself carries `derives from WAY-56`.
- What is wrong: the new sentence is the one case in which an identifier of a decision stands in the sentence, which is the binding part (WAY-56). A reader who takes "the links" of WAY-56 as any naming of an entry reads WAY-60 as breaking WAY-56; a reader who takes it as the two fields (the template's *Links* section, `elements/invariants/template.md:107-118`) reads them as agreeing. The files do not say which, and WAY-25 says a collision between two decisions with no precedence recorded is not settled silently. The harmonising reading exists and is what I take: a decision of the pinned the-way is no decision entry of the product's log (WAY-58), so naming it in the sentence is no link that WAY-17 requires; and the foundation already does this (`foundations/invariants.md` `tracked-file-private-paths`, "as WAY-309 and WAY-323 name them").
- Why it matters: the task's aim is that a writer finds one answer where the identifier of such a condition goes (settlement row 5). A writer who reads WAY-56 first, or a reviewer who does, can reject the form that WAY-60 mandates. Graded Minor, not Important: the departure is a missing sentence of reconciliation, not an instruction the files cannot both be followed by, and a reading that keeps both stands (WAY-263 does not reach it, since WAY-56 is not an entry the change writes).
- Evidence: the passages above read side by side; `grep -n "stand beside it" elements/invariants/template.md` gives line 74.
- Way out, the author's choice: a clause in WAY-60 and in the template line 81-83 that the identifier so placed is no link of WAY-17 (a decision of the pinned the-way is no entry of the product's log, WAY-58); or a clause in WAY-56 that it speaks of the links of WAY-17.

**M2 — The identifier `elements-no-pending-marker` names what the sentence demands, where the invariants template says an identifier names what the sentence constrains, never what it demands.**

- Place: `foundations/invariants.md`, heading `## elements-no-pending-marker`, with its citation at `elements/common/test_elements_pending_marker.py:27`, its listing in WAY-35's *Verification*, and the module's name; template rule at `elements/invariants/template.md:18-20` ("The identifier names what the sentence constrains, never what it demands, so that a reworded sentence leaves it true"). WAY-64 gives the identifier's form as words; this is a template rule, not WAY-64's.
- What is wrong: the "no" in the identifier is the demand. The neighbours constrain a thing (`tracked-file-private-paths`, `outbound-link-reach`, `script-imports`). `elements-pending-marker` would name what is constrained.
- Why it matters: if the sentence is ever reworded to allow the marker in one place, the identifier stays and says the opposite. Low cost today; the rename touches the heading, the citation line, WAY-35's *Verification* and the test's module name.
- Evidence: the template line and the heading read side by side; `git grep -n "elements-no-pending-marker"` lists the four places.

### Out of scope

**O1 — The invariant `elements-no-pending-marker` derives from WAY-35, whose binding sentence says nothing about a pending marker.** Place: `foundations/invariants.md` (`Derives from: WAY-35`), WAY-35 `foundations/decisions.md` (binding paragraph; *Verification* now naming the invariant). WAY-35 says every rule of an element's entries stands in the template or once in the part the elements share; a pending marker in a template is a rule that does not yet stand there, which is a reading, not a sentence of the decision. WAY-22 asks an invariant to be derived from the decision whose choice it keeps, and WAY-17 asks the link to be written; the nearer decisions are WAY-37 (entries that wait for something) and WAY-71 (where `TODO` may stand), and neither holds the rule either. This lies outside the task: the human settled it ("wyprowadzony z WAY-35", question on the test and the invariant, answer a), so I record it for the human and do not ask the cycle to change it. If the human wants the chain readable, one sentence in WAY-35 that a template or a skill carries no note that a rule is pending would close it.

## Reading of the fourteen decisions

Each read whole, from its heading to the next heading, in `foundations/decisions.md`.

- WAY-56 (one invariant, one sentence). The new invariant is one rule in one sentence; its second clause ("every run of spaces and line breaks counting as one space") fixes what "the text" matches, it is no second rule. It sits with *complies* ("every entry of the log has every field of the template" as one entry) and not with the *violates* pair (a sentence joining "number one to three" and "no *should*"). The method and links stand in fields beside the sentence. The one tension with WAY-56 is M1, for WAY-60's new sentence, not for the invariant.
- WAY-73 (*Rests on*). `Rests on: none` for the new invariant is right: the sentence copies no value from a fact, and a condition of "git tracks" or of how the test is run is no fact of the kind WAY-73 and `elements/environment-facts/template.md:62-64` name; the other invariants that say "git tracks" read `none` as well. It is not the *violates* case (a page's load time bounded by an outside standard's threshold). WAY-84's new *Verification* example (the protection of a branch as a fact with a reading for its source) and WAY-73's rule that a fact stands only while named stay consistent: WAY-84's *Based on* is unchanged.
- WAY-58 (*Derives from* where the log does not carry it): consistent with WAY-60's new sentence only through the reading in M1 (a pinned the-way decision is no entry of the log, so it takes no field). Its *Rejected* ("a decision kept outside the log counted as named") is not touched: naming one in the sentence counts as no link.
- WAY-62 (*Part*): the new invariant's six parts are the six parts that own a path under `elements/`; WAY-62's reach of a test the change alters holds. No contradiction.
- WAY-71 (`TODO` and `none`): the change removes the last two prose notes `TODO — decision pending` from the templates and adds none; the new entry has all five fields; the invariants template keeps the `TODO` forms of *Rests on* and *Derives from*; the facts template keeps "*Source* takes neither `none` nor `TODO`". Consistent.
- WAY-76 (one fact, one source, one reason to change): a reading of "one invocation, however many commands and lines" is one source; the sentence still states one fact. WAY-80's *Rejected* on "each further command a fact of its own" agrees with WAY-73's withdrawal of a fact nothing rests on. Consistent.
- WAY-77 (what a fact is true of): the date run stands in the source line of a reading and no field repeats it; the sentence of the protection example holds no word that moves with the date. The decision speaks of the date "read" and the template of the source "that publishes no editions", where a reading has a date "run"; this was so for a host before the change and is not widened by it.
- WAY-78 (binding part): the reading, its tool versions and its date stand outside the sentence in the template and in WAY-80. Consistent.
- WAY-90 (citations as facts): WAY-80's rationale sentence that an API's output "can carry a token" is a hazard, not a cited finding about agents, models or a tool the process uses, so it needs no fact. WAY-90's rationale says a fact needs "a source a reader can open (WAY-80)"; WAY-80 allowed a reading of a host that only those with access can compare before the change, and the change widens it to a service. Declined below.
- WAY-02 (references by identifier alone): the identifier in WAY-60's new sentence stands alone; `elements/common/foundation_check.py` reports a decision number only with the log's own prefix (lines 537-546), and a product's prefix differs from `WAY`, so a pinned the-way decision named in a product's sentence is not reported. The whitespace clause of the new invariant uses the words WAY-02 uses for its digest.
- WAY-03 (alteration of an invariant test): the new test cites the new invariant, so no listing arises for a reworded sentence with an unchanged test; the request must name the new test file (a matter of the cycle's request, not of the files).
- WAY-12 (how a decision is held): WAY-35 now names the invariant derived from it; WAY-60, WAY-80 and WAY-84 each carry a complies and a violates example, and none of the new *violates* examples replaces the decision together with its code. The invariant's *Derives from* names WAY-35 and WAY-35 names it back.
- WAY-64 (location and identifier): the identifier is made of words and is unique (`foundation_check.py`, 0 errors); the form of the name is M2.
- WAY-321 (test citations): `# invariant: elements-no-pending-marker` stands in a tracked Python file, so the check does not report the invariant; `foundation_check.py` without the skip switch gives `0 errors`.

Pairs of WAY-56 and WAY-73 compared with `elements-no-pending-marker`: complies with both; no finding comes from the pairs.

## Whole change again, against what I read

For each sentence the change writes or edits, whether a decision of the fourteen contradicts it or leaves it unmet:

- WAY-80 (reading in a service; one invocation; code block; no secret): no contradiction with WAY-76, WAY-77, WAY-78, WAY-90, WAY-71; WAY-90's phrase "a source a reader can open" is the declined point.
- WAY-84 (reading as source; *Rejected* rewritten): consistent with WAY-73 and WAY-90.
- WAY-60 (new sentence; examples; *Rejected*): M1.
- The new invariant and its test: M2 and O1; otherwise consistent with WAY-56, WAY-62, WAY-64, WAY-71, WAY-73, WAY-321. The test reads the files git lists under `elements/` and the pattern is `decision[ \n]+pending`; a run of my own on the pattern: `decision pending`, `decision` newline two spaces `pending`, `decision` blank line space `pending` and two spaces newline two spaces all match, a tab and `Decision pending` do not, as the sentence says (`python -B -I -c` over the pattern, exit 0).
- The facts template and its skill step (`elements/environment-facts/template.md`, `elements/environment-facts/skill/draft.md`): no contradiction with WAY-71, WAY-76, WAY-77, WAY-78; the skill's "an answer that carries a token or a password beside those fields is not quoted" agrees with WAY-80's rule and its *Rejected* clause on a marker.
- The invariants template (`elements/invariants/template.md:79-85`): M1; the `TODO` is gone and the `TODO` forms of WAY-71 are kept.
- `README.md` (list of elements, row `environment_facts.md`): says what WAY-80 says.

No decision of the fourteen leaves unmet a sentence the change writes, beyond M1 and M2.

## For each remark of the correction

Remark 1 (read the fourteen whole and compare the pairs of WAY-56 and WAY-73 with the new invariant; the correction fixes what the reading finds): the reading is made as the remark asks; the comparison finds the invariant complies with both pairs; the correction's findings are M1 and M2 (Minor within the task) and O1 (out of scope). Items 2-7 of the remarks are accepted by the human and are not reviewed here.

## Declined to judge

- Whether WAY-90's rationale ("a fact entry needs a source a reader can open (WAY-80)") is true of a reading of a service: it was equally untrue of a reading of a host before the change, the task's questions chose the variant, and WAY-27 is met (the reading is quoted in the entry, "described in the entry instead of being pointed to"). The earlier whole-change review declined the same point.
- The sentence counts and line lengths of WAY-80, WAY-84 and WAY-60: the fix and its review judged them; the paragraphs now hold two or three sentences each (WAY-05).
- The test `test_fact_source_with_a_command_of_several_lines_in_a_code_block`, the unindented-block limit of `foundation_check.py` and the structure numbers of the earlier review: not touched by this correction.
- No trust boundary and no irreversible operation (handoff step 4); no user interface; no reserved choice is taken; no guideline file applies (WAY-328).

## Checks (command, exit code)

| Check | Command (from the worktree root) | Exit |
|---|---|---|
| Foundation check | `python -B elements/common/foundation_check.py` | 0 (`0 errors`) |
| New invariant test | `python -B -m unittest elements/common/test_elements_pending_marker.py` | 0 (1 test, OK) |
| Marker gone from `elements/` | `git grep -il "decision pending" -- elements` | 1 (no match) |
| Whitespace in range | `git diff --check 0e1cd3c..43ffa5a` | 0 |
| Tree of `43ffa5a` equals the worktree head | `git diff --stat 43ffa5a HEAD` | 0, empty |
| Pattern of the test on five spellings | `python -B -I -c` over `decision[ \n]+pending` | 0 (results above) |
| Worktree unchanged | `git status --short` | 0, empty |
| Full gate, directory gate | not run, as dispatched | — |

## Reaches beyond the dispatch (section 1)

- `foundations/decisions.md`: WAY-60, WAY-80 and WAY-84 whole (they are the entries the change edits), WAY-05 (the sentence limits and what a rationale may name), WAY-17, WAY-19, WAY-22, WAY-25 (collision of decisions, for M1), WAY-27 (for WAY-90's rationale), WAY-35, WAY-37, WAY-61, WAY-82 — each whole, because the change writes it or because the fourteen name it or its grade rests on it.
- `elements/invariants/template.md` lines 1-150 and `elements/environment-facts/template.md` whole, `elements/environment-facts/skill/draft.md` (diff): the texts the change edits, read against the fourteen.
- `foundations/invariants.md` lines 86-116 and a search for "git tracks"; `foundations/part_map.md` for the parts that own `elements/` paths.
- `elements/common/foundation_check.py` by search (lines on the log's prefix and on references), `elements/common/test_elements_pending_marker.py` whole, `elements/common/way_of_working.md` "Reading the foundation" whole.
- The task and the earlier `whole-change-review-report.md` (for what was already judged).

## Unread material

My selection, by "Reading the foundation": the decisions whose *Scope* names a part the change touches, found by a script over `foundations/decisions.md` (`decisions`, `invariants`, `environment-facts`, `elements-common`, `glossary`, `part-map`): 123 decisions, among them the fourteen of the dispatch and the ones the task names.

- Read whole: 27 — the fourteen (WAY-56, WAY-58, WAY-62, WAY-71, WAY-73, WAY-76, WAY-77, WAY-78, WAY-90, WAY-02, WAY-03, WAY-12, WAY-64, WAY-321) and WAY-05, WAY-17, WAY-19, WAY-22, WAY-25, WAY-27, WAY-35, WAY-37, WAY-60, WAY-61, WAY-80, WAY-82, WAY-84.
- Run through by title only: 96 (the rest of the listing). Of them, titles that touch the change's topic and that I did not open: WAY-07 (how an entry is changed in place), WAY-33 (the search of the foundation), WAY-44 (what assigns a file to a part), WAY-65 (how a check cites its invariant), WAY-85 and WAY-86 (facts of a study, catalogues), WAY-95, WAY-96, WAY-99, WAY-297 (glossary words and their grade: "reading" has no glossary entry, as the earlier review found; no sentence of the change is read wrongly for it), WAY-134 (how a task's settlements reach the foundation; judged by the earlier review), WAY-150 (reading of the foundation), WAY-328 (the-way and its own code). My findings do not rest on them.
- Not read at all: none of the fourteen was read in part.
- Invariants: read whole `foundations/invariants.md` lines 86-116 (through the new entry) and the *Part*/*Rests on* lines that a search for "git tracks" returned; the rest of the file not read. Part map: searched for the parts that own `elements/`, not read whole. Glossary: not read. Guidelines: none apply (WAY-328).

## Searches not found or unclear

- Not found: a sentence of any decision that forbids a pending marker in a template (O1); a rule that states whether an identifier in the sentence of an invariant is one of "the links" of WAY-56 (M1).
- Unclear: WAY-77 and the facts template speak of "the date it was read" where a reading has "the date run"; unchanged by this change.
- Unclear: whether "the foundation" in WAY-02 ("names an entry the foundation holds") includes the pinned the-way of a product; the check reads only the log's prefix, so nothing reports it, and I took it as not needing a finding.
