# Report — foundation entries of the plan

**Status:** done

- Worktree: `the worktree root`, branch `task/small-fixes-from-ai-review-and-audit`, base `268b2b074691a331ed8db136343b4060bdd44539`.
- Commit (one, all three entries; they stand in one file and the two edits of WAY-339 and the new decision cannot be told apart by path): `a946862b557fc3bd1b3e04976a2bcf66054a1ace` — "Record in WAY-339 the image of each audit series and the comparison before and after a fix, and add WAY-417 on the answers Q1 to Q3 for a group of cycles". Slice 1 starts from it.
- File changed: `foundations/decisions.md`, +58 −2 lines (the 2 removed lines are the two lines of WAY-339 that gained text at their end; no sentence was reworded).
- Check run: `python -B elements/common/foundation_check.py` — `0 errors`, exit 0; also with `--skip-test-citations` — `0 errors`. No test and no gate run.

## Entries

### Row 1 — a sentence added to WAY-339 (mark: `row 1`)

- Lines in `foundations/decisions.md`: 8627–8633 (the paragraph beginning "The audit compares each measure only within a series", after its unchanged sentence; the sentence "The audit compares each measure only within a series of its own kind, …" starts where it started, so the `decision:` quotations of the tests still stand); the part of its *Verification* pair at 8668–8671 and 8673–8675 (see "Added parts" below).
- Meaning (EN): the audit shows each series as an image of all its cycles (what the kind of the series carries) and, inside the series, a comparison before and after a change — cycles on the versions that hold the change against cycles on the versions that lack it, both groups of that series, the version and never the date deciding the group; the answer Q3 and the fall stand only where two groups meet (WAY-417).
- Meaning (PL): audyt pokazuje każdą serię jako obraz wszystkich jej cykli (to, co niesie jej rodzaj) oraz, wewnątrz serii, porównanie „przed i po zmianie” — cykle na wersjach z daną zmianą wobec cykli na wersjach bez niej, obie grupy w tej samej serii, o grupie rozstrzyga wersja, nigdy data; Q3 i „spada” stoją tylko tam, gdzie są dwie grupy (WAY-417).

### Row 2 — a sentence added to WAY-339 (mark: `row 2`)

- Lines: 8632–8633 (the second added sentence: "That comparison is made for each fixed issue of the register of problems with a fix commit, and for no other change.").
- Meaning (EN): the comparison before and after is made for each fixed issue of the register of problems that has a fix commit, and for no other change of the process.
- Meaning (PL): porównanie „przed i po” dostaje każda naprawiona sprawa z rejestru problemów, która ma commit poprawki, i żadna inna zmiana procesu.

WAY-339 now has 3 sentences in its second paragraph (at most 3) and 600 words or fewer in all (the check passes). I cut my own added words to fit; no existing sentence was cut.

### Row 3 — a new decision, WAY-417 (mark: `row 3`)

- Identifier: **WAY-417**, heading "How are the answers Q1 to Q3 of the audit of the process given for a group of many cycles?", in the section "Process audit" at the end of it (after WAY-416), lines 8995–9038. 417 is the next free number: the log's highest is 416, no withdrawn number stands above 371 and none is 417 or higher; WAY-403 renumbers it if the target branch takes 417 first.
- Meaning (EN): the answer Q1 of each group of cycles (a version, a whole series, one side of a before-and-after comparison) is the numbers of cycles that answer yes, no and unknown, never one word; the answer Q3 and the fall stand only where two groups meet, and the image of a series gives a measure's median and the number of cycles with a known value.
- Meaning (PL): odpowiedź Q1 dla każdej grupy cykli (wersji, całej serii, strony porównania „przed i po”) to liczby cykli z odpowiedzią tak, nie i nieznane, nigdy jedno słowo; Q3 i „spada” stoją tylko tam, gdzie są dwie grupy, a obraz serii daje medianę miary i liczbę cykli ze znaną wartością.
- Fields: *Scope* `process-audit`; *Based on* `none`; *Relations* `derives from WAY-339 · derives from WAY-404`; *Origin* `none`.
- *Rejected* (from the *Not chosen* of the question of row 3, the two ways, each with its reason; the *Source* line of the answer keeps no other way — its "weak point (two forms of Q1)" is the second way, and its condition about what reads the result is a check of the code, not a way):
  1. "the rules that give an answer for a version applied to the whole group — the answer Q1 of any longer series comes out `yes` almost always, since one cycle is enough, and the answer Q3 of one group has nothing to be compared with";
  2. "numbers for the image of a series and for the comparisons before and after a change alone, with the answer Q1 of the rows of the versions as a word — two forms of the same answer in one result".
- *Verification*: a pair of examples, kept for now (see below).

## Added parts (the pair of examples, kept until a test of a later slice holds the sentence; they do not make an entry `the cycle's` — task-cycle foundation step, "save a pair kept only until a test of the same change holds the sentence"). The text word for word, for the description to quote:

WAY-339, *Verification*, added to the existing pair (lines 8668–8671 and 8673–8675):

- complies, added at the end of its sentence: "a series of the cost is shown as the median cost of all its cycles with a known cost, and, for a fixed issue with a fix commit, as that median over its cycles on the versions that hold the fix against that over its cycles on the versions that lack it;"
- violates, added after the existing items: "the cycles before a fix are told from the cycles after it by the date of the fix; the image of a series carries the answer Q3 or a fall; a change of the process that has no fixed issue with a fix commit in the register gets a comparison before and after;"

WAY-417, *Verification* (the whole pair):

- complies: "a series of five cycles, two of which answer yes to Q1, two no and one unknown, is shown with Q1 as `yes 2 · no 2 · unknown 1` in its image, in the row of each version for the cycles of that version and on each side of a comparison before and after a fix; a series of the cost shows in its image the median cost and the number of cycles with a known cost and no Q3, and shows Q3 in the row that sets a version against the previous version of its series and in the comparison before and after a fix;"
- violates: "the Q1 of a version or of a group reads `yes` because one of its cycles answers yes; the rows of the versions of a series give Q1 as a word while its image gives it as numbers; the image of a series carries the answer Q3 or a fall."

The return step takes out of both pairs the part that a test of slices 6 and 7 holds by a line `decision:`, and writes the clause `tests:` in its place (decision skill, step 3).

## The point 8 sentence of WAY-339 (the test runner)

"a new series of those starts only with a change of the script that counts them or of the script that records them, and, for the times of the gate, also with a change of the test runner of the process" **already stands in WAY-339** (first paragraph, word for word at 8613–8616, unchanged). Nothing was added for it. The slice-2 change (the script that records the gate times) is a change of "the script that records them", which WAY-339 names as a start of a new series; it needs nothing more.

## Search of the foundation (WAY-33)

Search by the words `WAY-339`, `WAY-350`, `Q1`, `Q2`, `Q3`, `before and after`, `image of`, `each version`, `per version`, `series`, `median`, `fall`, `Fate`, `fixed issue`, `answer Q` in `foundations/` (all five files), and by `decision: WAY-339` / `decision: WAY-350` in the `.py` files. Findings:

- WAY-337 (the cost, its median): not touched; WAY-417 and the WAY-339 sentences take the cost's median over a series as the image of a cost series, and WAY-337 says nothing of groups.
- WAY-350 (gate times, runs compared): read whole; **left unchanged**. The WAY-339 sentence names it ("for the times of the gate both take only the runs that WAY-350 compares") so that the image and the comparison of gate times keep its restriction; the task's *Decisions in play* says the comparison keeps "the same restriction". Choice and its rejected way below.
- WAY-404, WAY-405 (Q1's meaning and its unknown): WAY-417 derives from WAY-404 and names it for Q1; neither changes. The meaning of "yes / no / unknown" per cycle stays theirs.
- WAY-416 (the command and missing fields): the line "gives the values that need a missing field as unknown" stays; a group with unknown cycles counts them under `unknown n`, which does not collide.
- WAY-330 (the register, the tie of an issue to its fix): the "fixed issue with a fix commit" of the sentence is its notion; nothing changes.
- WAY-385 (size of what I write) read for the limits; WAY-339 fits (see above), WAY-417 stands at about 190 words of binding sentences.
- Line 8604 of `decisions.md` (WAY-337's *Rejected*) names "Q1" in passing; no change needed.
- Invariants `audit-series-script-paths` (paths of the scripts that start a series; row-independent) and `audit-count-refuses-record-links`: neither is touched by the new sentences; no invariant derives from the new sentences.
- Tests that quote WAY-339 (`process-audit/test_audit_count.py`, `task-cycle/test_cycle_stages.py`, lines `decision: WAY-339 "…"`): the quoted sentence starts remain the starts of sentences of the unchanged text; the check with test citations passes.
- Glossary: no word of the new text takes a glossary entry under WAY-95 ("image", "fall", "group" are plain words in the sentences, each explained in the sentence or in WAY-417); no glossary change.
- Part map: no part's responsibility changes (`process-audit` already answers "how the whole process fares over many cycles"); no change.
- Environment facts: no entry names the audit's series or answers; no change.
- `process-audit/SKILL.md` (not changed by me): its rule "Measures are compared inside a series only" and its point 4 "What each version of the process shows" are to be made true to the entries by slices 6–8; the rule's last sentence ("Set no number of one series beside a number of another, … and no week's count beside the week before; a version of the process is judged by the cycles that ran on it") is consistent with the new sentences, which compare two groups inside one series and decide the group by the version.

Each reach beyond this handoff: none. I ran a grep for `WAY-4[1-9][0-9]` to find the next free number (in the instructions' spirit of "inspect the log's numbers"), and `git ls-remote` / `git branch -a` to see the branches that could take a number; both inside the foundation-step method.

## Choices (with the way rejected and its cost if wrong)

1. **Where the two added sentences stand.** In the second paragraph of WAY-339 (after its one sentence, which is unchanged), so that the entry holds all the rule of "what is compared in a series". Rejected: a new third paragraph set apart. Cost if wrong: none to the meaning; the paragraph limits are the same.
2. **The clause "for the times of the gate both take only the runs that WAY-350 compares" in WAY-339.** The rows 1–2 do not give it; the task's *Decisions in play* for WAY-350 does ("with the same restriction to the runs compared"), and without it the image and the comparison of the gate times would stand under no stated restriction. Rejected: leaving WAY-350 to bind alone (it speaks of a comparison "between versions", not of an image of a whole series or a group of versions) and changing WAY-350 (the task leaves WAY-84 and the way of working alone, and keeps WAY-350's quotation as it stands). Cost if wrong: if the slices prefer the restriction elsewhere, 13 words of the sentence go; nothing else depends on them.
3. **Q2 in WAY-417.** Row 3 names Q1, Q3 and the fall; Q2 comes from the answer to the question the row's *Source* names ("Q2 to sumy odcinków planowanych i zbyt dużych z odpowiedzią z tych sum, jak dziś dla wersji"). I wrote it as the sum of the slices planned and of the slices returned too large, "with the answer that those sums give", since the foundation does not hold the rule that turns the sums into an answer (it stands in the code only; see "Searches not found or unclear"). Rejected: leaving Q2 out (the heading says Q1 to Q3, and the question's answer holds it). Cost if wrong: a sentence of 36 words to cut or reword.
4. **Q3 and the fall defined in words.** Q3 as "whether the median cost of a group is lower than that of the group it is set against" and the fall as "a median lower than that of the group it is set against", from points 4–5 *To do* and the task's *Context* (Q3 compares the median cost with the previous version). Rejected: leaving "Q3" undefined (WAY-339 and WAY-417 would rest on a name only the audit's script and skill hold). Cost if wrong: a wording to correct.
5. **One commit for all three entries**, as they are one file and one hunk series.
6. **Verification by pairs now, `tests:` clause later**, as the decision skill's step 3 gives where a later slice's test will hold the sentence. WAY-417 has no `tests:` clause since no `decision:` line cites it yet.
7. **Heading question of WAY-417** says "of the process" and "Q1 to Q3" (the audit's own names, used by `process-audit/SKILL.md`); WAY-417 explains Q1 and Q3 in its sentences and Q2 as the sums.

## Questions for the orchestrator

none.

## Working copies

none made; `.runs/foundation-entries/` was not needed and does not exist.

## Unread material

- `process-audit/audit_count.py`: lines 1–80 read, as the handoff says; the rest of its docstring (which may describe Q1–Q3) was not read.
- `foundations/invariants.md`: lines 1–185, 284–569 read; lines 185–283 and 433–460 not read, since the grep of `Part:` shows no invariant of `process-audit`, `task-cycle` or `every` in them.
- `foundations/decisions.md`: read WAY-330, 337, 339, 350, 404, 405, 416 and 385 whole; the others only through `.runs/index.md` and the grep. The log's other entries were not read.
- `elements/decisions/skill/projected.md`: not read (projected mode only; this is not projected mode).
- `process-audit/problem_register.md`, `process-audit/version_analysis.py`: not read (not named).

## Searches not found or unclear

- The rule that gives a group's Q2 answer from its sums of slices (planned and too large) stands in no entry of the foundation I read and in no text I was told to read; it is "as today for a version" by the task. WAY-417 says "the answer that those sums give" for that reason. If the slices want it stated, slice 6 has to read the code for it.
- The task's *Questions to settle* text for row 3 says the image gives "the median and the number of cycles with a known value, no Q3" for the measures; for the series of the count of remarks, the image is Q1 and Q2 (task point 4). WAY-417's last sentence ("a measure as its median and the number of its cycles with a known value") covers measures only; the Q1 and Q2 of the image are in its first paragraph. Clear enough, flagged in case a reviewer reads the pair otherwise.
- The *Source* line of the answer for row 3 (the one the *Rejected* is taken from) is the advisor's reply; I found no way in it beyond the two *Not chosen*.
