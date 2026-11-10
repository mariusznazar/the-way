# Author report — unread-material (the one author of the change)

- **Status:** done with concerns (the concerns are below: a row 4 handled as an edit of WAY-287, the
  item numbered 14, a gap of my own reading, one edge of `remarks_check.py`)
- **Worktree / branch:** `.runs/worktrees/unread-material`, `task/unread-material`, base `02c3d47`.
- **Commits:**
  - `ca376a0` — foundation: WAY-325 and WAY-326 new, WAY-150 and WAY-287 edited in place, the
    reading step of `elements/common/way_of_working.md`.
  - `afa4343` — methods: `task-cycle/skill/SKILL.md`, `task-cycle/skill/request_template.md`,
    `task-cycle/review/SKILL.md`, `task-cycle/change/SKILL.md`, `task-cycle/plan/SKILL.md`,
    `task-cycle/spec/design.md`, `task-cycle/spec/review.md`, and a test in
    `task-cycle/test_remarks_check.py`.
- **Files changed (added/removed lines, from `git diff --stat` before the commits):**
  `foundations/decisions.md` 143 (+/-), `elements/common/way_of_working.md` 12, `task-cycle/skill/SKILL.md` 43,
  `task-cycle/skill/request_template.md` +9, `task-cycle/review/SKILL.md` 13, `task-cycle/change/SKILL.md` +2,
  `task-cycle/plan/SKILL.md` 8, `task-cycle/spec/design.md` 8, `task-cycle/spec/review.md` 8,
  `task-cycle/test_remarks_check.py` +23. Total 220 insertions, 49 deletions.

## What was done, against the four points of *To do*

1. **Dopisek** — `task-cycle/skill/SKILL.md`, the paragraph "Each agent writes its full report…",
   straight after "add what it found to the handoffs that follow." The sentence is the one quoted in
   the task, word for word; the dropped last sentence of the older note is not added. WAY-325 is
   cited in the list of identifiers earlier in that paragraph, not inside the sentence, so the
   quoted text stays exact.
2. **The fixed section** — named **Unread material** in all five methods, the orchestrator's skill
   and the request template.
   - Methods: `task-cycle/change/SKILL.md` (report list), `task-cycle/review/SKILL.md` section 4,
     `task-cycle/plan/SKILL.md` section 5, `task-cycle/spec/design.md` "Return",
     `task-cycle/spec/review.md` "Return". In each it stands before **Searches not found or
     unclear** and apart from it.
   - Orchestrator (`task-cycle/skill/SKILL.md`): the paragraph of what a report holds; the line "In
     every report read its checks, reaches, unread material and searches; read the rest of it where
     the status is other than `done`" (this is the line that says what is read at `done`/`PASS`);
     the repair rule ("A report that lacks its **Unread material** (WAY-326) or its **Searches not
     found or unclear** (WAY-260) … returns to its agent for repair the same way"); the slice
     executor's mechanical check (step 9, sub-step 3: "a report missing one of these sections").
   - Places that mention **Searches not found or unclear** and deliberately did not change, because
     they are about the process remarks and not about what a report holds: `SKILL.md` line 72
     (copying into the remarks), "The process remarks check", `task-cycle/record_template.md`
     (form of a remark entry). `record_template.md` lists no report sections, so it needed nothing.
   - `task-cycle/remarks_check.py`: not changed. Checked by running it on seven fixture reports
     (scratchpad, not committed). With **Unread material** placed before **Searches not found or
     unclear** (the order the methods give) it is never read as, or inside, that section, in bullet,
     bold-label and heading forms; the script lists the Searches items only. One edge, see
     *Questions* below. I added two characterization tests to `task-cycle/test_remarks_check.py`.
3. **Request template** — `task-cycle/skill/request_template.md`, *For you to decide*, new item 14,
   with the example shape of the task ("The review of the whole change read 40 of 151 selected
   decisions whole; merge anyway?") in plain words. Present only when the reviewer did not run
   through the rest of its selection by title, or itself named a decision concerning the change as
   unread, and the gap was not closed on the way (the reviewer, or a fresh one, reading it). A
   reviewer that screened by title and named none unread gives no item. `request_check.py` does not
   enumerate the items (it checks headings, content or `none`, language), so no change to the script.
4. **WAY-150 and carriers** — WAY-150 changed in place (binding sentence, *Verification* complies
   and violates, *Rationale*, and *Rejected* with three ways not chosen added from the answer to the
   task's question 3, the existing *Rejected* kept). Carriers: `task-cycle/review/SKILL.md` "Read"
   (screening for decisions only; invariants, part-map and glossary entries read whole; guideline
   files read whole, WAY-213 untouched) and `elements/common/way_of_working.md` step 2 of "Reading
   the foundation" ("The whole log is not read." became "The log beyond the decisions found is not
   read.", followed by the reviewer's screening and "no other agent skims"; "Read each decision
   found whole" now carries "save as the reviewer of the whole change reads them below").
   `task-cycle/review/whole_change.md` states no foundation reading, so it is unchanged.

## Checks (command and exit code)

- `python -B gate/run_tests.py task-cycle` — exit 0 (234 tests OK).
- `python -B gate/run_tests.py elements/common` — exit 0 (117 tests OK).
- `python -B gate/run_tests.py agent-instructions` — exit 0 (18 tests OK).
- `python -B gate/run_tests.py instruction-files` — exit 0 (104 tests OK, 5 skipped).
- `python -B -m unittest task-cycle/test_remarks_check.py` — exit 0 (49 tests OK).
- `python -B elements/common/foundation_check.py --skip-test-citations` — exit 0, "0 errors" (run
  after the decisions were written and again after the last wording fix).
- Not run: the full gate (`python -B gate/run_tests.py` without argument), as the handoff says. The
  foundation check without the switch was not run; no invariant of mine reads `test`.
- The two tests I added are characterization tests of behaviour the script already has; they passed
  on their first run and were not seen failing. They catch a change of the script that would read an
  **Unread material** section placed before **Searches not found or unclear** as an item of it.

## Own-work check (WAY-164)

- Requirement most likely unmet: "update every place in the orchestrator's skill that lists what a
  report holds or what the orchestrator reads or checks in it".
- Check: `grep -rn "Searches not found" task-cycle` against `grep -rn "Unread material"` — every
  place that lists the report's sections or what is read has both (SKILL.md paragraph at 191-210,
  SKILL.md step 9 sub-step 3, five methods); the places that have only Searches are the three about
  the process remarks listed above.
- Shown: no listing place missed. What the check does not cover: a place in a file of another part
  that quotes the section list in other words — none found by the grep.

## Foundation entries (marks as `foundation_step.md` gives; sentences are of meaning)

- **WAY-325 (new), `row 1`.**
  - EN: When a stage report says that something its handoff names stayed unread or was read in
    part, the orchestrator decides before it acts on the status: resume the agent, carry the gap to
    the next agent able to judge it, or record an autonomous choice with the reason it bears on
    nothing the agent judged.
  - PL: Gdy raport etapu mówi, że coś, co wskazało mu zlecenie, zostało nieprzeczytane albo
    przeczytane w części, prowadzący cykl przed działaniem na statusie wybiera: wznawia agenta,
    przenosi lukę do następnego agenta, który może ją ocenić, albo zapisuje autonomiczny wybór z
    powodem, dla którego luka nie dotyczy niczego, co agent ocenił.
  - *Rejected:* `unknown` — the source of the row (point 1) keeps no way not chosen.
  - Search of the whole foundation (WAY-33) for a row-1 statement already made: WAY-148 (a missing
    or incomplete report is repaired) and WAY-260 do not state what to do with a reported gap, so a
    new entry.
- **WAY-326 (new), `row 2`.**
  - EN: Every stage report holds a section of its own, **Unread material**, naming what its handoff
    (for the reviewer of the whole change: its own selection) names that stayed unread or was read
    in part, or `none`, apart from WAY-260's account; the orchestrator reads it in every report
    whatever the status, and a report without it returns for repair.
  - PL: Raport każdego etapu ma osobny dział **Unread material** o tym, co ze zlecenia (u
    recenzenta całej zmiany: z własnego wyboru) zostało nieprzeczytane albo przeczytane w części,
    albo `none`, odrębny od działu z WAY-260; prowadzący czyta go w każdym raporcie bez względu na
    status, a raport bez niego wraca do agenta do uzupełnienia.
  - *Rejected:* the two ways of the task's question 1 (into the account of WAY-260; the orchestrator's
    choice alone), plus the record of every agent's selection that WAY-150 already rejects (the
    task's control question kept it). 
- **WAY-150 (edited in place), `row 3`.**
  - EN: The reviewer of the whole change reads whole the decisions of its selection that concern the
    change's topic, skims the rest of its decisions by title, opens every one whose title points to
    a bearing on the change, and states in its report how many it read whole and how many by title
    only; every other agent reads what its handoff names whole.
  - PL: Recenzent całej zmiany czyta w całości decyzje swojego wyboru, które dotyczą tematu zmiany,
    resztę decyzji przegląda po tytułach i otwiera każdą, której tytuł wskazuje na związek ze zmianą,
    a w raporcie podaje, ile przeczytał w całości, a ile tylko po tytule; pozostali agenci czytają w
    całości to, co wskazuje im zlecenie.
- **WAY-287 (edited in place), `row 4`.**
  - EN: The request's section for the human's decisions holds the incomplete reading of the review
    of the whole change — only where its reviewer did not run through the rest of its selection by
    title or itself named a decision concerning the change as unread, and the gap was not closed on
    the way — with the question whether to merge anyway.
  - PL: Sekcja opisu PR-a dla decyzji człowieka obejmuje niepełną lekturę przeglądu całej zmiany —
    tylko wtedy, gdy recenzent nie przejrzał reszty swojego wyboru po tytułach albo sam przyznał, że
    decyzja dotycząca zmiany została nieprzeczytana, a luki nie zamknięto po drodze — z pytaniem,
    czy scalić mimo to.
  - *Rejected* (added): the sentence in the top part outside the section; the lower part in the
    section of the checks — both from the answer to the task's question 2.

## Choices (with the way rejected and cost if wrong)

- **Row 4 is an edit of WAY-287, not a new decision.** The handoff said rows 1, 2 and 4 are new
  unless already stated. WAY-287's binding sentence lists "everything whose merge needs the human's
  yes", so a new item has to enter that list or its `none` would be false; and the decisions
  template says a new answer to a question the log holds rewrites that entry (WAY-19, WAY-07).
  Rejected: a third new entry (WAY-327) beside WAY-287 — it would leave WAY-287's list incomplete.
  Cost if wrong: the orchestrator and the human may have expected a new number for row 4; the
  meaning is the task's row either way.
- **The request item is numbered 14, appended after item 13, not placed beside item 4.** Placing it
  next to "skipped steps" would renumber items 5-13 and break references by number
  (`task-cycle/skill/correction.md` "item 8", `task-cycle/skill/SKILL.md` "item 12 of *For you to
  decide*"). Rejected: insert as 5 and renumber. Cost if wrong: the reader finds it at the end of
  the list, not next to the skipped steps; easy to move later.
- **"Closed on the way" means the reviewer, or a fresh one, read what stayed unread.** An
  autonomous choice of the orchestrator that the gap bears on nothing does not close it for the
  whole-change review (that review judges the whole change). Rejected: letting WAY-325's third way
  close it. Cost if wrong: an item stands in a request where the orchestrator had a reason.
- **Section order: Unread material before Searches in every method.** So the section never falls
  inside the Searches section that the remarks check reads (see *Questions*).
- **The reviewer's counts live inside the Unread material section** (WAY-326 says so), so the
  section always carries two numbers for a whole-change review and `none` follows them when nothing
  is unread. Rejected: counts in a separate report line (no place for it in the report list).

## Reaches beyond the handoff

- Read whole beyond the named seven: WAY-114, WAY-134, WAY-158, WAY-227, WAY-289, WAY-294 (to judge
  the item list, the settlements, the reviewer's full-diff reading, the orchestrator's reading and the
  remarks check); the invariants file (all of it, 356 lines); `elements/common/rules.md`;
  `elements/decisions/examples.md`; `elements/decisions/skill/{SKILL,read,decide_entry}.md`,
  `elements/decisions/template.md`; `task-cycle/skill/foundation_step.md`.
- Searched, passage read: `grep` for `Searches not found`, `Unread`, `item N`, `The whole log is not
  read`, `selects for its own review`, `read whole` across the repository (to find the carriers and
  the references by number); `task-cycle/request_check.py` and `task-cycle/remarks_check.py` (head,
  to see whether they enumerate items or sections).
- Read for the checks only: the head of `product-guidelines/reading.md` (it says the reviewer selects
  the guidelines; unchanged).

## Unread material

- **Decisions of my selection:** the selection by *Scope* (task-cycle, elements-common, decisions)
  is 160 decisions. Read whole: 65 (52 from WAY-01 to WAY-73 in order, plus WAY-114, WAY-134, WAY-148, WAY-150, WAY-158, WAY-159, WAY-213, WAY-227, WAY-260, WAY-286,
  WAY-287, WAY-289, WAY-294). Skimmed by title only: 94 (the rest from WAY-84 on, taken from a list of
  titles). Not seen even by title: none.
  I did this by judgment of the size of the reading, not by a rule the repository gave me; the rule
  being written here (WAY-150) did not exist when I read.
- **Read in part:** WAY-82 (to its second sentence). `foundations/decisions.md` itself was read in
  the passages I name (WAY-148, WAY-150, WAY-159, WAY-213, WAY-260, WAY-286, WAY-287 whole; the rest
  through an extract of the selected entries).
- **Not read:** the glossary entries of the terms the work uses ("Reading the foundation" step 4);
  the part-map entries other than `task-cycle`, `elements-common`, `decisions`; `slice.md`,
  `fix.md`, `ui_check.md`, `projected.md` (not the variant). **A decision of the titled-only 94 that
  bears on the change could have passed unopened;** I opened every title that named reports,
  handoffs, requests, the reviewer's reading or the remarks.

## Searches not found or unclear

- The task cites "`task-cycle/skill/SKILL.md:191-193`", "`:193`" and WAY-150 at line 4060; they
  have moved (the handoff said so), and I found the places by content.
- *To do* point 4 says "keep *Rejected* as the task's sources describe it, which stands". I read it
  as "do not remove the existing ways" and added three ways not chosen from question 3's answer,
  as the decisions template asks of a decision written from a row; if the intent was to leave
  *Rejected* of WAY-150 entirely untouched, the added three sentences are the change to drop.
- The handoff asked for the new section to be separate from **Searches not found or unclear**; the
  task's wording for the section ("stały dział") gives no name. I named it **Unread material**.

## Questions (with a recommended answer)

1. `task-cycle/remarks_check.py` reads a **Searches not found or unclear** section that is written
   as a bold label *outside a list* to the next line "that is no list item and starts with bold
   text". If an agent writes **Unread material** as a bullet (`- **Unread material:** …`) *after*
   such a Searches label, the Unread line is read as part of Searches and listed into the remarks
   (seen on a fixture). The methods place Unread material first, so a report that follows them is
   safe; I did not change the script. Recommend: leave as it is, and let a first real listing
   decide; if it turns up, end the section at a bold label named `Unread material`.
2. Should the item in the request template stand next to item 4 (and renumber the later items and
   the references by number), as the task's "obok pominiętych kroków" may mean? Recommend: no, keep
   14.

## Problems observed

- The first Edit of WAY-150 failed on a retyped passage and was redone on a smaller anchor; no
  residue. No test failed. The pretooluse guard blocked one `rm -rf` with a variable in the path; I
  removed nothing and used `mkdir -p` into a fresh directory instead.

---

# Fix of the Minor findings of the review of the whole change

- **Status:** done
- **Commit:** `613f100` (on `afa43439b39b66fc1e737897b0c6b8b0e11aa129`); files: `foundations/decisions.md`,
  `elements/common/way_of_working.md`, `task-cycle/skill/SKILL.md`, `task-cycle/test_remarks_check.py`.
  `task-cycle/skill/request_template.md` needed nothing: item 14 already says the gap is closed by "the
  reviewer or a fresh one reading what stayed unread", which WAY-287 now says too.

## Findings, each as fixed

1. **"Closed on the way" defined only in the template** — fixed. WAY-287's binding sentence now reads
   "…and the gap was not closed on the way by that reviewer, or a fresh one, reading what stayed unread".
   Chosen within the direction: the orchestrator's autonomous choice of WAY-325 does not close the gap for
   the request (as in the template). Check: `foundation_check.py` 0 errors; the template wording and the entry agree.
2. **A title-read decision not said to be "no gap"** — fixed in two places: WAY-326 (third binding
   sentence: "A decision the reviewer of the whole change read by title as WAY-150 gives is no gap and
   stands in the section only in the counts.") and the orchestrator's skill, as its own sentence straight
   after the quoted dopisek: "A decision the reviewer of the whole change read by title as WAY-150 gives
   is no gap." The dopisek itself is unchanged word for word (its lines were re-wrapped only after it).
3. **The `questions` exception not in the entry** — fixed in WAY-326: "…returns to its agent for
   repair, as a report without the account of WAY-260 does, save a report that returns `questions`."
   Chosen: put it in the entry (rather than drop it from the skill), as directed.
4. **Reverse order leaks an Unread line** — a test records it, the script is untouched:
   `test_an_unread_material_bullet_after_a_non_list_searches_label_is_an_item` in
   `task-cycle/test_remarks_check.py` asserts the two leaking forms (a non-list Searches label then a
   bullet **Unread material**, with items and with `none`) and the two forms that stay apart. It is a
   characterization test: it passed on first run, was not seen failing, and catches a change of the
   script's section ends that would alter this behaviour.
5. **Long lines and the clumsy sentence** — fixed: the WAY-150 line and the WAY-287 line re-wrapped;
   the `SKILL.md` lines re-wrapped (only the lines the fix touched, no paragraph reflow); the
   `way_of_working.md` sentence split to "Read each decision found whole, as the range of lines from its
   heading to the next heading (…), with its rationale and *Rejected*, except as the reviewer of the
   whole change reads them below: a search hit or a binding sentence locates an entry, never replaces
   it." Check: no added line over 101 characters in `git diff -U0` (`awk 'length>101'` on the added lines
   shows only the two 102-character diff lines, 101 characters plus the `+`).

## Checks (command and exit code)

- `python -B gate/run_tests.py task-cycle` — exit 0 (235 tests OK; the first run after my edit failed
  with a SyntaxError in my new test, a shell escape slip, and passed after I wrote the string again).
- `python -B -m unittest task-cycle/test_remarks_check.py` — exit 0 (50 tests OK).
- `python -B gate/run_tests.py elements/common` — exit 0 (117 tests OK).
- `python -B elements/common/foundation_check.py --skip-test-citations` — exit 0, 0 errors.
- Not run: the full gate.

## Own-work check

- Requirement most likely unmet: "keep all four points of the task met and the quoted dopisek word for
  word".
- Check: read the `SKILL.md` paragraph after the edit and compared the sentence with the quotation in
  *To do* point 1: "Where a report says that something its handoff names stayed unread or was read in
  part, decide before you act on its status: resume the agent to read it, carry the gap into the handoff
  of the next agent able to judge it, or record an autonomous choice saying why it bears on nothing the
  agent judged." stands unchanged, followed by the new sentence. The four points are touched only by
  clauses added (WAY-287, WAY-326, SKILL.md), none removed.
- Shown: the dopisek matches; the sections, item 14 and WAY-150 carriers are as before.

## Unread material

- Read whole for this fix: the findings file; `task-cycle/change/fix.md`; the passages of
  `foundations/decisions.md` (WAY-150, WAY-287, WAY-326), `task-cycle/skill/SKILL.md` and
  `elements/common/way_of_working.md` that the findings name. Not read: `review_whole_report.md` (no
  finding needed it); the decisions of my earlier selection are as stated in the first part of this report.

## Searches not found or unclear

- none

---

# Return step

- **Status:** done (nothing to correct)
- **Commits:** none. The tree is as at `613f100`.

## What was compared

- **The entries the change edits or writes**, WAY-150, WAY-287, WAY-325, WAY-326, each read whole in
  their final wording, against the files:
  - WAY-150 against `elements/common/way_of_working.md` (step 2 of "Reading the foundation"),
    `task-cycle/review/SKILL.md` section 1 "Read", `product-guidelines/reading.md` (the reviewer
    selects its own guidelines; unchanged and still true), and `task-cycle/skill/SKILL.md` (handoff
    paragraph: the reviewer selects its own foundation). They agree: the screening is for decisions
    of the reviewer of the whole change only; invariants, part-map and glossary entries are read whole.
  - WAY-287 against `task-cycle/skill/request_template.md` item 14. The condition (no run through the
    rest by title, or a decision concerning the change named unread, and not closed by the reviewer or a
    fresh one reading it) is the same in both.
  - WAY-325 against `task-cycle/skill/SKILL.md` (the dopisek sentence, word for word the one quoted in
    *To do* point 1).
  - WAY-326 against the five methods (`task-cycle/change/SKILL.md`, `task-cycle/review/SKILL.md`,
    `task-cycle/plan/SKILL.md`, `task-cycle/spec/design.md`, `task-cycle/spec/review.md`), the
    orchestrator's reading and repair rule in `task-cycle/skill/SKILL.md`, and the step 9 mechanical
    check. They agree: one section name, **Unread material**, in every place; the `questions`
    exception and "a title-read decision is no gap" stand in the entry and in the skill.
- **The entries the task names** (*Decisions in play*): WAY-148, WAY-213, WAY-159, WAY-260, WAY-286
  read against the changed files. None says anything the change makes false: WAY-148 lists what stands
  in a report without being exhaustive and WAY-326 adds the section; WAY-213 leaves the guidelines
  whole, which the review method keeps; WAY-159 and WAY-286 are untouched by the new section and item;
  WAY-260 still sends only **Searches not found or unclear** to the remarks, which
  `task-cycle/remarks_check.py` and its tests keep.
- **The entries my search found** (the search made while writing, WAY-33): WAY-114, WAY-134, WAY-158,
  WAY-227, WAY-289, WAY-294. WAY-294 reads only the Searches section, which is right. WAY-134 and
  WAY-114 still hold: rows 1-4 are written as rows, row 3 and row 4 as edits of WAY-150 and WAY-287.
- **The part map**, entries `task-cycle`, `elements-common`, `decisions`: the change adds and removes no
  file and changes no part's responsibility, dependency or trust boundary; no line is out of date.
- `python -B elements/common/foundation_check.py --skip-test-citations` — exit 0, 0 errors (run again
  for this step).

## Corrected

none.

## Written

- Decisions: none new in this step (WAY-325, WAY-326 and the edits of WAY-150 and WAY-287 came with the
  code in the foundation step).
- Invariants: none (the task, no decision and not the human set a rule needing one).
- Environment facts: none (the change rests on no source outside the product).
- Glossary terms: none (**Unread material** is a section name, not a word used in a meaning WAY-95 gives
  an entry; no term used against its entry).
- Part-map changes: none.
- Rows of *Settlements to record* written: row 1 — WAY-325; row 2 — WAY-326; row 3 — WAY-150 (edited in
  place); row 4 — WAY-287 (edited in place). No row was missed by the foundation step.
- A choice that binds after the merge (WAY-36), considered and not written: the position of the section
  before **Searches not found or unclear**. It stands in the list order of the five methods and is no
  rule the task or a decision set; the reverse order is recorded by the new test, and the reviewer's
  Minor about that test goes to the request's list, not fixed here.

## Checks

- `python -B elements/common/foundation_check.py --skip-test-citations` — exit 0.
- No other check run: nothing changed in this step.

## Unread material

- Read whole for this step: `task-cycle/skill/return_step.md`; the final wording of WAY-287 and WAY-326
  and the lines around the edited places of WAY-150 and WAY-325; `task-cycle/skill/request_template.md`
  item 14. Compared by search and the passage found, not by reading whole again: the glossary (titles
  of its entries and a search for `selection`, `unread`, `screen`: no hit), the part-map entries beyond
  the three named. WAY-148, WAY-213, WAY-159, WAY-260, WAY-286 were not read again whole in this step;
  I read them whole in the first part of this work and checked them here only for the clauses the change
  touches.

## Searches not found or unclear

- none
