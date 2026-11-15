# Findings for the fix — review of the whole change, `FAIL dfe14f7`

From `reports/review-whole-report.md`, in the reviewer's words: the blocking finding, then the Minor findings within the task (WAY-161), all of which this fix takes in.

## Blocking

**I-1. WAY-330 carries no rejected way for row 10 of *Settlements to record*.**
Place: `foundations/decisions.md:7653` (WAY-330 *Rejected*), commit `3020643`.
What is wrong: row 10 rewrites the price of WAY-330, and its source keeps a way not chosen with its
reason: "droga niewybrana: (b) zostawić zdanie, bo warunkowe jest dalej prawdziwe dla każdego nowego
użytkownika — czytelnik wpisu bierze audyt za narzędzie, które dziś nie ma czego liczyć" (task,
*Settlements to record*, row 10, column *Source*). WAY-134 binds the cycle to give "a decision
written from a row as its rejected options only the ways not chosen that the row's source keeps".
WAY-330's *Rejected* still holds only its two older ways ("the audit reading the records of cycles
itself …", "the-way taking over the review of the remarks of cycles …"); the way of leaving the
conditional sentence is not there. The change applies the same rule to every other row that keeps a
way not chosen — row 1 (WAY-229, five ways), 2 (WAY-10), 3 (WAY-27), 4 (WAY-320, two ways), 5
(WAY-287), 6 (WAY-35), 9 (WAY-44) — so row 10 is the one row whose rejected way was dropped.
Why it matters: the row is carried in part, and the next reader of WAY-330 who finds the old
conditional price "still true for each new user" — the exact argument the human weighed and
rejected — has nothing in the entry that says it was weighed, and may restore it.
Evidence: `awk 'NR>=7625 && NR<=7665' foundations/decisions.md` shows *Rejected* ending at "…instead
of every night."; the word diff of WAY-330 (`git diff --word-diff 0dae56b..dfe14f7 --
foundations/decisions.md`, hunk `@@ -7577`) changes only the price sentence.
Fix: append to WAY-330 *Rejected* the way not chosen, e.g. "the price left in its conditional
form, true for every new user — a reader takes the audit for a tool that has nothing to count today".

## Minor findings within the task

**M-1. Item 19.15 is done in one of its two places: WAY-339 still holds the line "WAY-350 and the".**
Place: `foundations/decisions.md:7802` (WAY-339 *Rejected*), commit `dfe14f7`.
What is wrong: the review's data file names two places for WAY-339 at `21ecb62` — `:8176-8177` and
`:8234-8236`. The second is the 15-character line "WAY-350 and the" between "…the tables of the gate
times and of" and "reading of the audit, …"; at the head it stands unchanged at line 7802. The
author reflowed two other short lines of WAY-339 (the line "of the tool it changed. A column of"
and the end of the *Rationale*), which match the first place as the base reads, but not this one.
Evidence: `sed -n '8232,8237p'` of `git show 21ecb62:foundations/decisions.md` and
`grep -n "^WAY-350 and the$" foundations/decisions.md` → `7802`.

**M-2. The fact `claude-code-prompt-cache-ttls` gives no archived copy, though one holds its passage.**
Place: `foundations/environment_facts.md:222-226`, commit `63ed3e4`.
What is wrong: the template of environment facts gives a page without editions "the closest archived
copy that already exists and its date". The author's report (Choices 6) says the closest copy
(2026-11-14) "words the sentence differently ("bills cache writes at a higher rate")". It does not:
the capture `https://web.archive.org/web/20261114163725/https://code.claude.com/docs/en/prompt-caching`
— the same copy the two sibling facts cite — holds, under § Cache lifetime, "The API offers two: a
five-minute TTL, and a one-hour TTL that keeps the cache warm through longer breaks but charges a
higher rate for cache writes." word for word ("cache writes" is a link there), and "bills cache
writes" stands nowhere in it. The fact's content is right; only its *Source* lacks the copy a reader
needs once the live page changes.
Evidence: raw capture (`…/web/20261114163725id_/…`), decompressed, normalised (tags, link markup and
the space before punctuation removed): all 20 passages of the seven changed or new facts found,
this one included; `grep -c "bills cache writes"` → 0 in both the capture and today's page.
Fix: add `(archived: https://web.archive.org/web/20261114163725/https://code.claude.com/docs/en/prompt-caching, 2026-11-14)`.

**M-3. The change leaves new over-long and short lines in a log it partly reflows.**
Places (characters): `foundations/decisions.md:2441` (WAY-44, 122), `:5183` (WAY-140, 105), `:6465`
(WAY-10, 154), `:9507` (WAY-241, 132), `:6931` (WAY-287 *Rejected*, a 59-character line in the middle
of a paragraph, "same gap between the decision and this entry. A sentence of");
`task-cycle/skill/SKILL.md:454` (102). Commits `ffa9a44`, `3020643`, `dfe14f7`, `a9384de`.
What is wrong: each of these lines was made by the change — an edit that joined text to a line and
did not rewrap the paragraph — while item 19 exists to remove exactly such lines. No check enforces
a width (the log holds 371 lines over 100 characters at the head, mostly addresses), so nothing
breaks; the next review of the foundation will list them again.
Evidence: a script over the `-U0` diff counting Unicode characters of added lines; the two long
lines of WAY-44 and WAY-10 do not stand at `0dae56b` (`grep -F` in the base file finds neither).

**M-4. WAY-229's *Rationale* says "the version after the change", which has no antecedent in the entry.**
Place: `foundations/decisions.md:6023-6024`, commit `ffa9a44`.
What is wrong: "the audit of the process shows what the version after the change costs" renders the
task's "audyt procesu pokaże koszt wersji po zmianie" word for word; in the entry "the change" points
to the change that brought the decision — its history, which WAY-05 keeps out of the prose ("does
not tell how the decision was reached") — or reads as the change a review judges. On author's
concern 6: the fact itself is held by the log — WAY-339's *Rationale* says "the audit exists to say
whether the process got dearer", and WAY-337 measures a cycle's cost — so the sentence can rest on
them: e.g. "and the audit of the process shows what it costs (WAY-337, WAY-339)".

**M-5. WAY-229's *Rejected* uses "the strongest model" beside "the strongest class available".**
Place: `foundations/decisions.md:6053` ("never above the strongest model") and `:6055` ("a bound on
the strongest model has to stand somewhere all the same"), commit `ffa9a44`.
What is wrong: item 1 asks that "the strongest" have one meaning in the whole entry. Here a second
phrase stands for something else: in the source the option capped the review at one named model
("najwyżej Opus") and the reason was that a line keeping one model out of cycles must be drawn
somewhere ("granicę na Fable i tak trzeba gdzieś postawić"). Read with the entry's own definition,
the strongest the session allows, "a bound on the strongest model" says nothing — the bound is
already there. Fix: "never above a model the human names" / "a line that keeps a model out of the
cycle's work has to be drawn somewhere all the same".

**M-6. WAY-44's new *Rejected* item says "the map goes on with no effect".**
Place: `foundations/decisions.md:2489`, commit `3020643`.
What is wrong: the source (question "pozycja 28", way (b)) says "rozjazd bez skutków" — the gap
between the sentence and the map has no effect. "The map goes on with no effect" reads as the map
having no effect. Fix: "the gap has no effect on the map or its check, but a reader … ".
