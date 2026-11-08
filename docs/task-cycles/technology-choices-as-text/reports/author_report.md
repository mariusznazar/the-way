# Report of the one author — technology-choices-as-text

**Status:** done with concerns (concerns: the meaning change of WAY-123, the length of its third binding sentence, one wording choice in `settle.md`; see below).

**Commits:** `78c32c7` "Show technology choices to the human as text, not as a table" (9 files, +94 / -57).

## Files changed

| File | Added / removed |
|---|---|
| `foundations/decisions.md` | +about 60 / -about 30 (WAY-123, WAY-137, WAY-138, WAY-165, WAY-166, WAY-267, WAY-268) |
| `project-level/technology/settle.md` | +14 / -9 |
| `project-level/technology/task_run.md` | +7 / -6 |
| `project-level/technology/SKILL.md` | +1 / -1 |
| `project-level/definition_template.md` | +4 / -3 |
| `project-level/task/template.md` | +2 / -2 |
| `project-level/task/skill/orchestrated_mode.md` | +1 / -1 |
| `project-level/lead/conversation_template.md` | +3 / -2 |
| `project-level/lead/skill/SKILL.md` | +1 / -1 |

(`git diff --stat HEAD~1`: 9 files, 94 insertions, 57 deletions.)

## Checks

| Check | Command | Exit |
|---|---|---|
| foundation form | `python -B elements/common/foundation_check.py` (from the worktree root) | 0 ("0 errors"), run after the last edit of `decisions.md` |
| tests of `project-level` | `python -B gate/run_tests.py project-level` | 0 (271 tests OK) |
| tests of `elements/common` | `python -B gate/run_tests.py elements/common` | first run, in parallel with two other runs: 1 (2 failures in `test_foundation_check.py` with an empty report: `test_based_on_names_by_identifier_alone_no_fact`, `test_file_left_out_on_purpose_needs_no_part`); run again alone: 0 (109 tests OK) |
| tests of `installation` | `python -B gate/run_tests.py installation` | 1 on a run across my commit, see the line below the table; `python -B -m unittest discover -s installation -p "test_styleguide_installation.py"` after it: 0 |
| verbatim text of task points 1, 2 and 5 | `python -B -I <session scratchpad outside the repository>/verbatim_check.py` (read-only; whitespace-normalised search of the four task sentences in `settle.md` and `task_run.md`) | 0: found 4 of 4 |

The first failing run of `elements/common` is a guess to be explained by contention: three `gate/run_tests.py` runs were started at once, and these two tests build temporary git repositories; the same directory passed alone and I changed no file of `elements/common`. I did not verify the cause.

Not run: the full gate (`python -B gate/run_tests.py`), by the handoff; `python -B agent-instructions/skill_entry_points.py --write`, because no skill's name, location or description changed (only a body line of `project-level/technology/SKILL.md`); `request_check.py` and `private_paths_check.py`, because the request description is the orchestrator's.

Installation: `python -B gate/run_tests.py installation` ran across my commit: exit 1, one failure, `test_styleguide_installation.StyleguideInstallationTest.test_preview_apply_repeat_exposes_the_styleguide_skill_and_preserves_product`, which compares the pinned commit with the HEAD it found at the start (`a3206c1` expected, `78c32c7` found because I committed during the run). Run again after the commit: `python -B -m unittest discover -s installation -p "test_styleguide_installation.py"` exit 0 (2 tests OK). The rest of `installation` (43 other tests) passed in the first run. I did not rerun the whole directory (about five minutes).

No test was written first: the change is prose and foundation entries; no test of the-way checks the wording of these sentences (the task's Context says the same), and a test of wording would check text, not behaviour (method, section 2).

## Own-work check (WAY-164)

- **The requirement most likely not met:** task point 4 — every site where "table" names what the human receives is changed, and no ordinary table is.
- **The check:** `git grep -n -i -w -E "tables?" -- project-level ':!*.py'`, reading every remaining hit, and the same for `foundations/` (`Grep` for `\btables?\b`, 98 lines before, then re-read after the edit).
- **What it showed:** every remaining hit in `project-level/` is an ordinary table (the marker table of `definition_template.md:175`, the working table `:269/:283`, the questions table of `reserved_choices.md`, the candidate table, the table of tasks of the plan, the routing table of `lead/skill/SKILL.md:155`, "table rows" of `reading_definition_and_plan.md:13`, the plan template's "no table of its tasks"). In `foundations/decisions.md` the remaining hits are the same kinds, listed below as "found by my search, left alone".
- **A second failure I looked for and found:** while re-reading the row 2 wording against `settle.md` I saw that my first draft of WAY-123 said the checking agent "sees only the message", whereas `settle.md` (point 2 of the task, sentence kept word for word) gives the same agent the document as well. I changed WAY-123 to "has checked, in the message as first shown" — the row's own sense (the check reads the first message, not the follow-ups; that is the cost the task names in question 1). Not a failed command; a draft corrected before the commit.

## Reaches beyond the dispatch (section 1)

- `foundations/decisions.md` WAY-166 (found by my own `table` search; heading read whole, `4695-4724`), to judge the site at its "violates" line.
- `product-guidelines/{coding,styleguide,testing}/new_tools.md` (read by `git grep` of WAY-123 citations, the first one whole): they cite WAY-123 and say "show the options by their consequences" without the word table; left unchanged, they do not contradict the new WAY-123.
- `elements/decisions/template.md` and `elements/common/way_of_working.md` (read whole through the foundation step and the skill, as the skill requires), `elements/decisions/skill/{read,decide_entry}.md`.
- Whole reads of the files I changed: `settle.md`, `task_run.md`, `SKILL.md`, `start.md`, `list.md`, `definition_template.md`, `task/template.md`, `orchestrated_mode.md`, `conversation_template.md`, `lead/skill/SKILL.md`.
- Entries read whole: WAY-123, 138, 113, 120, 165, 267, 268, 137, 114, 166. Not read, because the search of `table` did not touch them: WAY-270 (named only in the heading list).
- No reach for a decision or invariant the handoff did not give beyond the above. I did not search the glossary for "message"; the word is used in its ordinary meaning.

## Foundation entries (foundation step)

| Entry | Mark | Meaning in English | Znaczenie po polsku |
|---|---|---|---|
| WAY-123, changed | row 1 | A wave of technology choices reaches the human in one message of plain text, choice after choice; only the options that decide a choice are described at length, under their own names, the others get one line and the lines of the options left out stay; the table, the table with a paragraph beneath and the "tool name only where it carries a consequence" rule are rejected. | Wybory jednej fali docierają do człowieka jedną wiadomością zwykłego tekstu, wybór po wyborze; pełny opis pod własną nazwą dostają tylko opcje rozstrzygające, pozostałe po jednej linii, linie opcji odpadłych zostają; tabela, tabela z akapitem i zasada „nazwa narzędzia tylko tam, gdzie niesie konsekwencję” odpadły. |
| WAY-123, changed | row 2 | Before the wave reaches the human, a fresh agent checks the first message for an option shown by figures or features instead of what it changes for the product and for a word a person who does not know the technology cannot follow without an explanation; the check stays an agent's judgement and sees only the first message; variant A (figures and features alone) is rejected. | Zanim fala dotrze do człowieka, świeży agent sprawdza pierwszą wiadomość pod kątem opcji pokazanej liczbami albo cechami zamiast tym, co zmienia w produkcie, i słowa, którego osoba nieznająca technologii nie odczyta bez wyjaśnienia; to ocena agenta, a sprawdzenie widzi tylko pierwszą wiadomość; wariant A (same liczby i cechy) odpadł. |
| WAY-165, changed | row 3 | In a run at a task, the list shown to the human keeps an item held by a decision that is silent on part of its matter as `— held by`, with one sentence saying what that decision leaves unsaid. | W przebiegu przy zadaniu pozycja trzymana przez decyzję, która milczy o części sprawy, stoi na liście pokazanej człowiekowi jako `— held by` z jednym zdaniem o tym, czego ta decyzja nie mówi. |

No entry is marked `projected` or `the cycle's`: there was no projected entry, and every changed sentence of WAY-123 and WAY-165 carries a row. Other decisions (137, 138, 166, 267, 268) changed one word ("table" to "message" or a rephrase) with no change of meaning; they carry no row of their own and need no meaning sentence for the human.

### Row-to-entry ties and the questions the rows left to the writer

- **Row 1:** tied to WAY-123 (the question "How does a technology choice reach a human who cannot assess the technology?" already holds the form of the showing, so a new decision would answer the same question, `decide_entry.md`). WAY-123's *Rationale* and *Rejected* take the form of text, the rejected table, the table with a plain paragraph beneath it, the rule "tool name only where it carries a consequence" and "leave as it is" (reworded as "the options in one table as before"), each with the cost the task keeps. Not carried: the MVP2 story (counts and the incident), because the decisions template forbids a rationale that tells how the decision was reached, and counts.
- **Row 2:** tied to WAY-123, not WAY-120. Reason: WAY-120 is the general rule of the critique of collectively reviewed sets, and the check sits in this one area's showing; WAY-123 already narrows WAY-114 for the same area and is the entry `settle.md` cites for the check. *Rejected* gets variant A with the cost the task gives. `settle.md` is not the only place: it is the step's text, the decision binds it.
- **Row 3:** tied to WAY-165 (not WAY-267): WAY-165 already says "in a run at a task, the item stays `— held by` until the human's word opens it" in its *Verification*, so the sentence belongs next to that. WAY-267's own sentence ("a choice a decision of the foundation holds opens only on the human's word") needed no change. The row's source (To do point 5) keeps no *Not chosen*; I added none to WAY-165's existing *Rejected*.
- **WAY-123 binding sentences:** the entry had three sentences and has three, the third now long (the form of the showing, the critique, the check, the prevailing over WAY-114). That is my weakest wording choice; see the weakest point.
- **Order of rows on the template:** *Based on* and *Relations* of WAY-123 unchanged (`none`; derives from WAY-121 and WAY-113, narrows WAY-114). I did not add `derives from WAY-120`: the row does not ask for it.

## Meaning change to put before the human (task point 3)

WAY-123 is an accepted decision whose meaning changes: "in one table" becomes "in one message, one choice after another, in plain text" and "in separate tables" becomes "in separate messages". The *Rejected* "the tables come one choice at a time" is reworded "the choices reach the human one at a time". The request must put this before the human at the merge (WAY-114). The new binding sentences also add what the rows add: the form of the description (only deciding options at length) and the fresh agent's check.

## Sites changed (task points 3, 4, 5, and my own search)

In `project-level/`:
- `technology/settle.md`: the sentence "Then show the wave together, in one table: ..." replaced by the task's text (point 1), the contradictions sentence extended by the task's text (point 2), and "table" to "message" at the critique's input ("the whole message with the risks"), "of the message contradicts in another", "the message did not name", "next message" (twice, line 59 and 67), and the closing "message. Start the next wave" (line 75).
- `technology/task_run.md`: sentence of point 5 as given, wtrącenie of question 3 as given; `before the next message` (line 84).
- `technology/SKILL.md:58`: "of a message".
- `definition_template.md:237`: a repetition of WAY-123 and now says "in one message, one choice after another and in plain text ... and a fresh agent has checked that message" (the task says it repeats the sentence; I repeated the new meaning); `:255` "stand in the message".
- `task/template.md:42,134`: "as the message gave them".
- `task/skill/orchestrated_mode.md:26`: "the message on the choices".
- `lead/conversation_template.md:101`: "the message on the choices with their consequences".
- `lead/skill/SKILL.md:133`: "its message on the choices".

In `foundations/decisions.md`:
- WAY-123 (binding, *Verification* violates, *Rationale*, *Rejected*) — as above.
- WAY-137: "violates" example, rephrased (see ambiguous sites).
- WAY-138: binding "they stand in the message beside", complies "the message shows beside each option", violates "strikes a risk from the message".
- WAY-165: row 3 (binding sentence, complies, violates, *Rationale*).
- WAY-166 (found by my search, not in the task list): violates "the message shows the service with no word on whether an agent can use it".
- WAY-267: "shows the message" and "the message goes in the round package".
- WAY-268: "a message for the human", twice (*Rationale* and *Rejected*).

## Ordinary tables left alone (as the task lists)

`reserved_choices.md:22,42` questions table; WAY-268 `…questions table` (three places in its *Verification* and *Rationale*, and the same phrase in the decision at the "reserved-choice exclusion"); `start.md:7` working table; `definition_template.md:175` marker table (and `:269,:282` working table); the candidate table of `find-foundation-entries`.

## Ambiguous sites and my decision

- **WAY-137 "the table of consequences" (a violates example):** changed. The sentence is about what the human receives: a comparison of hosts that "scores how well an agent works with each host beside its cost"; nowhere in `project-level/technology/` is the report's comparison called a table (`research.md` and `settle.md` call it "the comparison"), so "table of consequences" can only be the shown table. Reworded "the consequences shown to the human score ...". If the task author meant the comparison in the report, the cost is one reworded violates example with no change of meaning.
- **WAY-138 (task's lines :3573,3583,3590 in its numbering):** three sites, all about what is shown before the human chooses; changed to "message".
- **Candidate tables of `find-foundation-entries`** (`decisions.md` WAY-109/WAY-115-area lines at 2514–2637, 3340–3413; `lead/answering.md:54`; `lead/conversation_template.md:95`, `lead/skill/SKILL.md:127`; `orchestrated_mode.md:17`): found by my search; they are a real table of rows and columns the human cuts, in another step, not in the technology step. Left alone.
- **`project-level/plan/skill/hand_over.md:7` "the whole table of tasks"** and the plan decisions (3778–3995): a real table of the plan; left alone.

## Found by my search, not on the task's list

- WAY-166 `decisions.md` (violates example) — changed (names what the human receives).
- WAY-268's *Rationale* and *Rejected* "a table for the human" — these are the task's own list (its lines `:7967,7979` in the old numbering), so not new.
- Not changed, other kinds: `decisions.md` uses of "table" for the plan's tables, the permissions table, the styleguide's roles table, `guidelines/coding.md`'s table, the table of levels, the `instruction-files` judgement table, the questions table of the cycle record (WAY-268, WAY-… at 9019–9043 about a reserved-choice exclusion), WAY-270's "a table of its own" (a database table; line 8164 region, an alert).
- `product-guidelines/{coding,styleguide,testing}/new_tools.md` cite WAY-123 and ask for options by consequences with no table; compatible, unchanged.

## Weakest point (WAY-164 / section 3)

1. **The third binding sentence of WAY-123 carries five things** (the showing in one message, the critique first, the fresh agent's check, the recommendation with its weak point, the precedence over WAY-114). It is one grammatical sentence but long; a reviewer may ask to split it into a fourth sentence, which the template forbids (one to three), or to move the check elsewhere (WAY-120). My reasoning: the check is part of when the wave reaches the human, so it stands where "once every one of their comparisons has passed the critique" stands. Cost if wrong: a reader finds the check harder to see; no behaviour changes.
2. **"has checked, in the message as first shown"** is my wording for the row's "the check sees only the first message". If the task author meant a stricter rule (the agent receives nothing but the message, not even the document), `settle.md` as the task gives it (point 2) contradicts it, because the same fresh agent is given the document. I kept the task's sentences word for word. A question for the orchestrator below.
3. **The "table" vs "message" sweep in the settle step's sentences** ("what one choice of the message contradicts in another"): the task's point 2 quotes "what one choice of the table contradicts in another" and asks to add after it, while point 4 lists `settle.md:46` among the sites to change. I changed the word (as point 4) and added the text (as point 2) in the same sentence; a literal reading of point 2 would have kept "table" there.

## Choices made, with the way rejected and its cost if wrong

- WAY-123 as the home of the check (row 2), not WAY-120 — cost if wrong: WAY-120 would be the place a reader looks for the critique rules, and the check would sit in the area-specific entry (a later move is one edit, with the number kept).
- WAY-165 as the home of row 3, not WAY-267 — cost if wrong: one sentence would need moving to WAY-267; both entries are in the same area.
- "plain text" and "in words a person who does not know the technology can follow" put into WAY-123's *first* sentence, so the form of the description is binding, as the row says — cost if wrong: the first sentence is longer than before.
- Used the task's example word "bundler" in WAY-123's *violates*, the task's Q2 giving it; the "compiler" sentence is not quoted.
- The check's Verification examples are mine (a violates example for each new rule). They are optional by the template; the cost is that a reviewer may find them over-writing what the rows say. I derived them only from the row text and from the task's *Need* and *Questions to settle* 2.
- No change to WAY-267 beyond "table to message": the task's row 3 says "czy zmienia się tylko `task_run.md`, czy WAY-165 albo WAY-267", and I judged WAY-165 the home.

## Problems observed

- Two tests of `elements/common` failed once when three test runners ran in parallel and passed alone (see Checks); guess: contention on temporary git repositories; not verified.
- None other.

## Questions and concerns for the orchestrator

1. Concern (not a question): the meaning change of WAY-123 must reach the human at the merge (WAY-114).
2. Question with a recommendation: should the fresh agent of the check be told that it sees only the first message, in `settle.md`? The task's point 1/2 text does not say it, and I did not add it. Recommended answer: no — the decision binds it and `settle.md` already hands the agent exactly the first message to read.
3. Question with a recommendation: is it right to leave the candidate tables of `find-foundation-entries` as tables (they are a different step)? Recommended answer: yes.

## Searches not found or unclear

- Task point 4 lists line numbers "@ 52889bc" for `decisions.md`; they have moved (orchestrator finding C1). I found every site by heading and quoted words. All sites the task names were found; WAY-137's task-line (`:3547`) is the "table of consequences" violates example, now at `3573` — found, but only after checking the headings.
- The task's point 3 cites `"in separate tables"` at `:2897-2898` and `"the tables come one choice at a time"` at `:2912`; both were found in WAY-123 (now `2922-2923`, `2937`).
- The task's point 2 phrase "what one choice of the table contradicts in another" was found at `settle.md:45-46` but the point 4 list also tells to change the word "table" on `settle.md:46`; unclear which should win in that exact phrase, see the weakest point 3.
- The row 2 of *Settlements to record* says the check "sees only the first message"; unclear whether that means "the agent gets only the message as first shown" or "the agent receives nothing but the message". `settle.md` as the task gives it also gives the document, so I took the first meaning; see the weakest point 2.
- Row 1 says "the table with a plain paragraph beneath" and "leave as is" are rejected ways; the *Not chosen* of question 1 gives the first as "tabela z akapitem prostym językiem pod spodem" and the third as "zostawić jak jest"; I used both. No separate source keeps "the rejected table" apart from "leave as is", so the *Rejected* gives it once ("the options in one table as before").
- `foundation_check.py --help` does not exist as a flag (it ran with an error message about the working directory on that call); the script takes only the root directory. Not a finding about the work.
