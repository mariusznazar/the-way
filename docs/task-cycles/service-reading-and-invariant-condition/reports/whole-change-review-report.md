FAIL 8680824c3c81f9a932eb20e3e2ff93ce503798c3

# Review of the whole change: service-reading-and-invariant-condition

Range `0e1cd3cd804433f7a82ffb631e96917ef74c1040..8680824` (commits `19efdfd`, `8680824`). `git rev-parse HEAD` in the worktree is `8680824c3c81f9a932eb20e3e2ff93ce503798c3`, as dispatched. Worktree status was clean before and after my work. A scratch worktree of the head in the scratchpad was used for the negative controls and is removed.

Counts: blocking 1, Minor 5, out of scope 0.

## Findings

### Blocking

**B1 — Important, within the task (items 3 and 4, settlement row 3). The template and the decision's rationale tell a writer "nothing is cut from the output afterwards", which contradicts the form of a reading that the same text gives and goes beyond WAY-80's binding part.**

- Place: `elements/environment-facts/template.md:125-128` ("nothing is cut from the output afterwards, and no marker stands in its place (WAY-80)"), against `elements/environment-facts/template.md:111-117` (the reading is "its output word for word, or the lines of it the sentence rests on, joined by ` · `"). The decision carries the same words in its *Rationale*, `foundations/decisions.md` WAY-80 ("nothing is cut from the result afterwards"), beside the binding sentence of the same entry, which still allows "the lines of it the sentence rests on".
- What is wrong: choosing the lines a sentence rests on is cutting the output afterwards. A writer following the template gets two instructions that cannot both be kept: quote only the lines the sentence rests on, and cut nothing. The ban is stated as a rule in the template and as reasoning only in the decision; the binding sentence of WAY-80 says only that the command reads only the fields the sentence rests on and that the quoted output holds no secret. The task's settlement row 3 says exactly that and nothing about cutting, so the template restates WAY-80 differently and more broadly (WAY-263, graded Important when the change's files restate an entry more broadly). It also reads as if a secret on a line outside "the lines the sentence rests on" could be dropped by line selection, which is the cut the *Rejected* clause on a marker refuses, so the reader cannot tell which cut is allowed.
- Why it matters: an agent writing the first reading in a service (the case the task exists for) gets an instruction it cannot follow, or follows one half and the review rejects it by the other half; the task's aim was to stop agents inventing the form.
- Evidence: the three passages above, read side by side. Fix direction (the author's choice): say what is meant, for example that no part of the output that holds a secret is removed or replaced to make it fit, and that the secret is kept out by what the command asks for; or drop "nothing is cut from the output afterwards" and the matching words of the *Rationale*, which the binding sentence does not need.

### Minor, within the task

**M1 — WAY-80's binding paragraph has five sentences and WAY-60's four; the decisions template and WAY-05 allow one to three.** Places: `foundations/decisions.md` WAY-80 (paragraph after the heading; five sentences, four before the change) and WAY-60 (four sentences, three before the change). WAY-05's own *Verification* names "a paragraph of five sentences" as a violating example. The author reported WAY-80 and not WAY-60. The task requires the content (items 1, 3, 5, 7), not the count; the foundation does not allow the count. Graded Minor because the content agrees with the code and the template departure is by form (WAY-364), and no sentence is read wrongly for it. The way out inside the template is a second paragraph for "a part of another question" (WAY-05), or merging the new sentence into one of the existing ones; judged here as the template gives, the author's choice to leave WAY-80 unrestructured is not allowed by the foundation, and the same departure in WAY-60 is a new one the report did not name.

**M2 — The new test `test_fact_source_with_a_command_of_several_lines_in_a_code_block` does not fail for the regressions its comment and the author's report say it catches.** Place: `elements/common/test_foundation_check.py:891-905`. I made five changes in a scratch worktree, each restored: `blocks` reading an indented `#` line as a heading; `FIELD` accepting leading whitespace; `blocks` reading an indented `## ` line as a heading and matching `level` after `lstrip`; the same with the heading in the test changed to a valid identifier; and the line `## a line that looks like a heading` moved to column 0 in the test. The test passed (exit 0) in every case. Reason, read in `elements/common/foundation_check.py:155,240-270`: the entry check ignores a heading whose text is no identifier (`ENTRY.match`), a repeated field is ignored (the first `Source` is kept), and `fields` ends a field at the blank line, so the code block under *Source* is never part of the value; the test passes for any fact whose first *Source* line is valid. It stands as an example that the form passes, and would fail only if the check began to reject such an entry. The task asked only the question (answer: no fix needed, which I confirmed by the same reading and by the `0 errors` run); the test is the author's addition, and its claim to catch the break is wrong. Suggested: drop the claim from the comment, or make the block hold what a break would change.

**M3 — The test of the new invariant matches `decision\s+pending`, broader than the invariant's sentence.** Place: `elements/common/test_elements_pending_marker.py:17` against `foundations/invariants.md` `elements-no-pending-marker` ("holds the text "decision pending""). A file that wraps "decision" and "pending" across a line end fails the test though it does not hold that text. The author named this choice (a wrapped marker would otherwise pass); no such file exists today. Either word the sentence to match ("a line end or several spaces between the two words count") or narrow the pattern. Case-sensitive, as the sentence; a "Decision pending" passes (verified).

**M4 — Item 6's template rule cites WAY-80, which does not hold it.** Place: `elements/environment-facts/template.md:150-154` ("... not in straight quotation marks (WAY-80)"). The task says the rule is template text "bez zmiany dziennika", so the citation sends a reader to a decision that says nothing of symbols, collapsed whitespace or “…”. The neighbouring bullets cite WAY-80 for rules that WAY-80 does hold; this one would be read as WAY-80's. Drop the citation or cite the decision that holds the edition form only for the address.

**M5 — Partial rewrapping leaves uneven lines.** Places: `foundations/decisions.md` WAY-84 binding paragraph (line `shown, or, where no page open ... that` of about 150 characters), WAY-60 binding paragraph (the line `sentence. An invariant's sentence names no branch, ...` of about 107 characters), `elements/environment-facts/template.md:67-68` (`... (WAY-84, WAY-80). A` then a short line), `foundations/decisions.md` WAY-35 *Verification* (`invariants: ... · elements-no-pending-marker. For` then a short line). No rule or test of the repository limits line length (699 lines of the file are over 100 characters at the head, 692 at the base), so this is polish only.

### Out of scope

none.

## Declined to judge

- The four-sentence form WAY-80 already had before the change: judged only as far as the change widened it (M1).
- Whether a reading of another's service meets WAY-27 ("no entry may point to a source a reader cannot open"): the task's questions chose the variant and WAY-80 already allowed a reading of a host; no finding is made against the choice.
- The long lines of `foundations/decisions.md` that the change did not touch.
- No trust boundary and no irreversible operation (handoff step 4); no user interface; no reserved choice taken (the change settles no language, framework, store, login or place to run); no guideline files apply (the-way departs from the coding and testing guidelines under WAY-328).

## Against the task

Frozen task `.runs/task-cycles/service-reading-and-invariant-condition/task.md`.

*To do* 1-8:

1. WAY-80 gives the reading for a setting on another's service, form as for a host (command or API call, service, tool with version, output, date): met (`foundations/decisions.md` WAY-80, first binding paragraph; wording of the settlement used: "a setting they set on another's service, which no page open without their access shows").
2. WAY-84 says the setting has a reading for its source (WAY-80) and its *Rejected* now rejects the repeated reading, not the one quoted: met.
3. WAY-80 says the quoted output holds no secret and the command reads only the fields the sentence rests on: met in the decision; the template and *Rationale* add the ban of B1.
4. Facts template: the `TODO — decision pending` bullet replaced by a rule citing WAY-80 and WAY-84 (`template.md:148-149`); reading form in the opening paragraph, the form line, the three-forms bullet; skill `draft.md` (Source step: the call from the service's documentation, the fields by name or a filter, a run once to see what the answer holds, a question where no narrower call exists); `README.md` list and table row: met.
5. WAY-80 "one invocation quoted word for word however many commands and lines", multi-line command in a code block under *Source*, version of each tool; the template says the same twice (three-forms bullet and the new bullet `template.md:119-124`): met. Question carried to the cycle (does `foundation_check.py` read such a fact): answered no fix needed, confirmed by me (`0 errors` run and reading of `blocks`/`fields`); the test the author added is M2.
6. Code at a fixed commit — symbol place, one statement or line, whitespace collapsed to one space, ` · `, “…” for a passage with `"`: met in the template (`template.md:150-154`), no decision changed; the citation is M4.
7. WAY-60 got the sentence (identifier of the entry or decision that holds the condition, in a field if the template gives one, otherwise in the sentence); the invariants template lost the `TODO` and cites WAY-60: met. The template's gloss "in *Derives from* or *Rests on* where one of them is the link the form gives" agrees with the form: a decision of the product's log is *Derives from*, a fact is *Rests on*, a decision of the pinned the-way has no field (WAY-58) and stands in the sentence.
8. New invariant `elements-no-pending-marker` in `foundations/invariants.md` (method `test`, derives from WAY-35, rests on none, *Violated* no); test `elements/common/test_elements_pending_marker.py` cites it as `# invariant: elements-no-pending-marker` and fails when a tracked file holds the text (negative control below): met.

*Settlements to record*, rows 1-6: each is in the decision or invariant the row names; the wordings of rows 1, 2, 3, 4 and 5 equal the task's. *Questions to settle*: every answer is carried out (a, a, yes, a, a, a); the not-chosen ways of the questions on the reading, the secret, the several-command reading and the invariant's condition stand in *Rejected* of WAY-84, WAY-80 and WAY-60 with the cost the task keeps beside each, and none is derived by the author (WAY-134). The "25-line script" figure is left out of the clause on a command of many lines, which the decisions template permits (no count in prose).

## Against the foundation

- Decisions changed in place (WAY-07): WAY-80, WAY-84, WAY-60, WAY-35 (*Verification* only), each describing the state, not the change. Foundation check `0 errors` without the skip switch, so the new invariant's citation is found.
- Entries that name the changed ones (WAY-33): my own search for "people run", "a reading", "reading:", "own server", "access to the host", WAY-80, WAY-84, WAY-60 and the replaced `TODO` texts found no entry still saying the host-only form; the two `README.md` places and the skill step are changed; WAY-90's rationale, the decision at `foundations/decisions.md:5996-6002` and `product-guidelines/styleguide/settle.md` cite WAY-80 for the source of a fact and are unaffected; no invariant derives from WAY-60, WAY-80 or WAY-84 other than the new one derives from WAY-35.
- Invariant test changed or added: `elements/common/test_elements_pending_marker.py` (new, cites `elements-no-pending-marker`); `elements/common/test_foundation_check.py` holds no invariant citation for the added test.
- Part list of the invariant: `decisions · part-map · invariants · glossary · environment-facts · elements-common`. The part map assigns `elements/**` files to exactly these six parts (`elements/decisions/**`, `elements/part-map/**`, `elements/invariants/**`, `elements/glossary/**`, `elements/environment-facts/**`, `elements/common/**`), so a change that can introduce the marker touches one of them; the list is complete and no part is named that holds no file under `elements/`. Allowed by WAY-62.
- Test place: `elements/common/test_elements_pending_marker.py` is in the part `elements-common`, which the *Part* list names, imports only the standard library (so the part-map dependency test is unaffected) and is run by `gate/run_tests.py elements/common`. Allowed: the task does not place the test, WAY-61 asks only a test of the product's suite, and WAY-328 holds for it. A place in `gate/` was properly refused (that part answers for the runner).
- The author's three named choices, each judged by the method and the foundation:
  - *Rejected* of WAY-80 saying "a host or a service": allowed. It edits a clause that was already there so that it stays true; it adds no way the writer derived (WAY-134 bars that), and the unchanged clause would have contradicted the new reading.
  - An example in the *Verification* pairs of WAY-80, WAY-84 and WAY-60: allowed. The decisions template makes the pair optional and keeps it for the part no test holds; none of the three has a test; the examples are consistent with the changed sentences and with the task's wording. The pair of WAY-35 is untouched.
  - Five sentences in WAY-80's binding paragraph: not allowed by the foundation (decisions template "Binding sentences", WAY-05), and not required by the task; Minor, M1. WAY-60's four sentences is the same departure, not reported by the author.
- Glossary: terms used are "environment fact", "invariant", "invariant test", "binding sentence", "read off"; the change uses each in its entry's sense. "Reading" has no entry and is used in the sense WAY-80 already gave it; no sentence of the change is read wrongly for that, so not a finding.
- WAY-328: the new test does not wait for guidelines; consistent.

## Structure of the code the change leaves

`python -B task-cycle/change_file_sizes.py 0e1cd3c 8680824` (exit 0): `README.md` 173 to 174; `elements/common/test_elements_pending_marker.py` new, 44 lines; `elements/common/test_foundation_check.py` 1516 to 1532; `elements/environment-facts/skill/draft.md` 8 to 12; `elements/environment-facts/template.md` 189 to 205; `elements/invariants/template.md` 182 to 182; `foundations/decisions.md` 12786 to 12823; `foundations/invariants.md` 366 to 376. The-way has no rule of size in coding guidelines (WAY-328), so no threshold test exists and a finding of structure would be Minor (WAY-363); I make none. The new test file holds two functions and one class, each short; no name stopped being true; no code lost its user.

## Checks (command, exit code)

| Check | Command (from the worktree root) | Exit |
|---|---|---|
| Foundation check | `python -B elements/common/foundation_check.py` | 0 (`0 errors`) |
| Directory gate | `python -B gate/run_tests.py elements/common` | 0 (201 tests, OK, 227 s) |
| New invariant test | `python -B -m unittest elements/common/test_elements_pending_marker.py` | 0 |
| Private paths | `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` | 0 (`checked: 298 files, 0 listed`) |
| Whitespace in range | `git diff --check 0e1cd3c..HEAD` | 0 |
| File sizes | `python -B task-cycle/change_file_sizes.py 0e1cd3c 8680824` | 0 |
| Marker gone | `git grep -il "decision pending" -- elements` | 1 (no match); the only hit of the text in the repository outside `.runs` is the invariant's sentence |
| Full gate | not run (as dispatched) | — |

Negative controls, in a scratch worktree of `8680824` (detached, outside the reviewed worktree, removed afterwards; nothing committed):

- `<!-- decision pending -->` appended to the tracked `elements/common/rules.md`: new test exit 1, `files under elements/ hold the pending-decision marker` (the author's report names the line number; mine printed the empty-list diff, same verdict). File restored with `git checkout`.
- `Decision pending: x` (capital): exit 0, as the sentence is case-sensitive.
- An untracked new file under `elements/common/` holding the text: exit 0 (not a file git tracks, as the sentence says); the test reads `git ls-files`, so a staged file counts.
- The test of the invariant therefore fails when a tracked file holds the text and passes on the committed tree.
- For the added foundation-check test: five changes to `foundation_check.py` or to the test (M2), each exit 0, so the test does not fail for them; all restored with `git checkout`, `git status --short` empty.

## Reaches beyond the dispatch (section 1)

- `foundations/part_map.md` (whole): to name the parts of the changed files and verify the invariant's *Part* list.
- `foundations/decisions.md`: WAY-05, WAY-17, WAY-08, WAY-61, WAY-65, WAY-134 read whole — WAY-05 for the sentence count, WAY-134 for what *Rejected* of a decision written from a row may hold, WAY-61, WAY-65, WAY-08 and WAY-17 for the form and the citation of an invariant's test and the links of the chain.
- `elements/decisions/template.md` and `elements/invariants/template.md` (whole): the form the changed entries are judged against.
- `elements/common/foundation_check.py` (lines 155, 236-275, 620-660): to judge the test of the carried question (M2).
- `foundations/glossary.md` (list of terms; the entries named above read whole).
- A search of the repository for the replaced wording and the host-only form (`git grep` with the terms listed under "Against the foundation").

## Unread material

- Decisions of my selection (parts `decisions`, `environment-facts`, `invariants`, `elements-common`, plus the decisions the task and the handoff name): 112 by *Scope* (script over `foundations/decisions.md`). Read whole: 14 (WAY-05, WAY-07, WAY-08, WAY-17, WAY-33, WAY-35, WAY-60, WAY-61, WAY-65, WAY-80, WAY-82, WAY-84, WAY-134, WAY-328). Run through by title only: 98.
- Decisions whose title points to a bearing on the change and that I did not read whole: WAY-56 (what one invariant entry holds), WAY-58 (*Derives from*; I read it only through the sentence the invariants template quotes), WAY-62 (*Part*; I read the template's account of it), WAY-71, WAY-73 (what *Rests on* names; template account only), WAY-76, WAY-77, WAY-78, WAY-90, WAY-02, WAY-03, WAY-12, WAY-64, WAY-321 (read only through the templates). My findings do not rest on them, but the pairs of examples of WAY-56 and WAY-73 were not compared with the new invariant.
- Invariants: read whole `foundations/invariants.md` lines 1 to 130 (through `script-imports`), which include the new entry and the ones of the parts the change touches that I met; the rest of the file (from `script-imports` on) not read.
- Part map: read whole.
- Glossary: read the entries "binding part", "binding sentence", "entry", "environment fact", "invariant", "invariant test", "read off"; the other entries not read.
- `examples.md` of the invariants element: read whole; the facts element has none (its template names the-way's own `foundations/environment_facts.md`, which I did not open); the decisions `examples.md` not opened.
- `README.md`: read through the diff only.
- Guidelines: no file read; none applies to the-way's own code (WAY-328).
- Author's report, task and method files: read whole. The reports of executors of slices: none exist (no plan).

## Searches not found or unclear

- Not found: a glossary entry for "reading" (also the author's finding); the word is used as WAY-80 gives it, no finding.
- Unclear: the author's report says the carried question's scratch run printed `the entry lacks *Source*` with a heading in column 0; I did not reproduce that run; I reproduced the passing run and the passing mutations of M2.
- Unclear: no rule I found fixes how a binding paragraph answers a question that already has four sentences (WAY-05 gives "one paragraph for each part of another question"); the way out in M1 is mine.
- `git worktree add` for the scratch worktree adds an entry to the shared worktree list while it exists; it was removed with `git worktree remove --force` and is absent from `git worktree list`.
