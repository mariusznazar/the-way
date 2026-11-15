FAIL dfe14f7acba448a90e430d7469941fe1c6ad713c

# Review of the whole change — decisions-log-after-foundation-review

Variant: the whole change (`task-cycle/review/SKILL.md`, `whole_change.md`). Range `0dae56b..dfe14f7`
(six commits `ffa9a44`, `b58ff96`, `a9384de`, `63ed3e4`, `3020643`, `dfe14f7`); `git rev-parse HEAD`
in the worktree is `dfe14f7acba448a90e430d7469941fe1c6ad713c`, as given. Route: one author, no spec,
no plan, no slices — every finding below comes from no slice.

Counts: blocking 1 (Important), Minor 6 (all within the task), out of scope 0 (Declined to judge: 4
lines).

## Findings

### Important

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

### Minor (each within the task)

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

## Concerns of the author, judged

1. **WAY-140 (19.6)** — no finding. The item puts the pointer "przy tym, co 'is no effect of the
   task'", which stands in the first binding sentence, and its parenthesis names what the pointer is
   for — the repository's own working directories outside its directory, which WAY-140 did not name.
   A bare "(WAY-375)" there would hang on the backlog record. The clause binds nothing the log did not
   already bind: WAY-375's second paragraph says "Removing a checkout that git names, also one that
   stands outside the repository's own directory, is a change to the repository's state and no
   effect outside the repository in the sense of WAY-140", and WAY-375 derives from WAY-140; "the
   repository's own working directories" covers the same checkouts. A pointer in the *Rationale*
   alone would leave the binding sentence silent where the item places it. Its line is over-long
   (M-3).
2. **19.19** — verified true at the base: `foundations/part_map.md:198-201` reads "…, for the shared
   reading that selects guidelines for a change and recognizes what is missing, and for the test that
   finds …"; the item was written at `21ecb62`, where the list ended at "the shared reading" without
   "and" (`git show 21ecb62:foundations/part_map.md`, lines 189-191). No change needed.
3. **`claude-code-imports` (12)** — no finding. Item 12 allows § Choose where to put CLAUDE.md files
   where a dependant needs the load moment; WAY-129's *Rationale* ("an import loads the whole file it
   names into every session") needs it. Passage verified on today's page (line "CLAUDE.md and
   CLAUDE.local.md files in the directory hierarchy above the working directory are loaded at
   launch.") and in the 2026-11-14 capture. WAY-129, WAY-132, WAY-141 and `installation-claude-guidance`
   read true against the new sentence; `instruction-files/tool_loading.md:42` no longer says "at
   launch" for an import, and no other "at launch" about imports stands in the repository.
4. **Facts for WAY-255 (15)** — three facts are right by the template ("two facts from one edition
   whose sentences are about different things stand as two entries"); their passages stand on today's
   page; the binding "five minutes by default" now rests on `claude-code-subagent-cache-default`. The
   archived copies of the expiry and subagent facts hold their passages; the third fact's missing copy
   is M-2. Archived copies of the other facts (`openai-model-states` 20261114004355,
   `anthropic-model-states` 20261114003641, `claude-code-project-skills` 20261114004012,
   `claude-code-imports` 20261114174608) are the latest captures in the archive's index from
   2026-11-01 on, and each holds every passage its fact quotes.
5. **WAY-363 *Rationale*** — no finding. "with the same chance in the grade that a remark on the form
   of an entry shows (WAY-364)" compares two judgments that WAY-363 and WAY-364 both grade Minor; it
   holds no "as today" and stays true. Item 14 names *Rejected* only.
6. **"the audit of the process shows …"** — the wording is M-4; the fact is held by WAY-337/WAY-339.
7. **WAY-229 *Rejected* widened, "every other reviewer"** — no finding. WAY-134 gives a decision
   written from a row the ways not chosen that the row's source keeps; the five added ways are those
   of P1 (b) and P1a, in general terms, with no model name. "every other reviewer work on no class
   cheaper than the orchestrator's" keeps the base rule for the reviews the task does not name (slice
   reviews, reviews of fixes, of the reconciliation, of corrections, the spec's reviewer), as item 1
   changes only the review of the whole change and of the return step.

## Checks against the task

- *To do* 1 (WAY-229, P1, P1a): "the strongest class available" is defined once in the first binding
  paragraph ("which is the strongest that the cycle's session lets its agents use") and used with that
  meaning at design slices, at the top of a retry ("an executor of the strongest class available"),
  for the two reviews, in *Verification* and *Rationale*; no model name or tool-setting name added
  (`Sonnet 5.5`/`Opus 5.5` stand from the base, in the measurement); the three places of *Verification*
  and *Rationale* the item names are changed; `task-cycle/skill/SKILL.md:451-452` and `:498` are
  changed. Other places that state a review's class: `git grep` for `class cheaper`, `orchestrator's
  class`, `strongest`, `no class cheaper`, `class` in `task-cycle/**/*.md`, agent types and
  `.claude/agents/` — none contradicts; `task-cycle/skill/SKILL.md:429` "An executor of the strongest
  class" (see Declined). Exceptions: M-4, M-5.
- 2 (WAY-10): price in *Rationale*, P2 (b) in *Rejected*. ✓
- 3 (WAY-27, WAY-320): general exception, "and nowhere else" gone, example follows; WAY-320 clause
  in its own paragraph, *Verification* example, *Rationale*, both ways of P4 in *Rejected*. ✓ The
  compliance example "the instructions of the audit name the entry that holds the register of
  problems" holds (`process-audit/SKILL.md:28`).
- 4 (WAY-241, template line): ✓ both.
- 5 (WAY-287): new paragraph; template lists every kind (`task-cycle/skill/request_template.md:324-334`,
  kinds 12 and 13 for WAY-308 and WAY-316); *Rejected* gives today's search result — rerun: the three
  words hit 66 entries, WAY-308 and WAY-316 among them — and weighs the general item again. ✓
- 6 (WAY-313): *Rejected* carries the way of question 5 of `07cbcf8:docs/task-cycles/decisions-as-material-at-refinement/task.md`
  with its cost word for word in meaning; `unknown` kept for the opening sentences. ✓
- 7 (WAY-330): price rewritten as the row says ✓; its rejected way missing — I-1.
- 8, 9, 10 (invariants): ✓. `git grep -n "elements-no-pending-marker" dfe14f7 -- .` → exit 1 (no
  use left); new identifier in the heading, WAY-35 *Verification*, the test's docstring and its
  `# invariant:` line. Changed invariant test: `elements/common/test_elements_pending_marker.py`,
  docstring line 1 and citation line 27 only (+2/−2), assertions unchanged.
- 11, 12, 19.21, 19.22 (facts): every quoted passage found on today's page and in the cited capture;
  dependants WAY-85 (needs only that models leave service — the Shutdown state gives it), WAY-127,
  WAY-129, WAY-132, WAY-141 and `installation-claude-guidance` read true.
- 13 (WAY-162, WAY-229): every binding paragraph of both entries has at most three sentences; WAY-162
  is word for word the base text (rewrap-only by word comparison). ✓
- 14 (WAY-360, WAY-363 *Rejected*): ✓.
- 15 (WAY-255): ✓ but M-2.
- 16 (`cut_tasks.md`), 17 (`starting_rules.md`), 18 (`guideline_findings.md`): ✓. Item 18's paragraph
  matches `product-guidelines/coding/hand_back.md:29-31` and `testing/hand_back.md:17` and names both
  directions, as `audit_end.md:69` does.
- 19.1–19.23: rewrap-only items verified by word comparison — a script splitting each entry of the
  log at base and head into words: WAY-90, 124, 126, 162, 206, 216, 243, 328, 339, 365, 372 are
  word-identical (rewrap only); WAY-320 and WAY-360 hold only the words items 3 and 14 add; the short
  lines named by the data file are gone except M-1. 19.3, 19.6, 19.7, 19.8, 19.11, 19.20, 19.23 ✓;
  19.19 true at base.
- Rows 1–11 of *Settlements to record*: rows 1–9 and 11 carried with their ways not chosen; row 10
  short of its way not chosen (I-1).
- Nothing outside the items: the 12 changed files map onto items 1, 4, 8–10, 9, 12, 16, 17, 18,
  19.1, 19.20 and the log and facts; the 29 changed decision entries are exactly those *Decisions in
  play* names.
- WAY-05 on the rewritten entries: sentence counts hold; no file, script or count in the new
  author-written prose beyond measurements and names already used in the log. WAY-10's "the process
  has no reviewer from another provider" is the price the task's P2 mandates and concerns which models
  the human has, not a tool of the process; I raise nothing on it.
- Structure: `change_file_sizes.py` shows the log +70 lines, the facts +18, other files +0 to +6; the
  the-way has no coding guidelines (WAY-328), so no size test exists; no code changed.
- The author's own-work check (WAY-164): it targeted the one-meaning requirement of item 1 and its
  check (a search of WAY-229 for `strongest`, model and setting names) would catch a second meaning
  of "the strongest class available"; it missed "the strongest model" (M-5), which that search
  would have shown.

## Declined to judge

- `task-cycle/skill/SKILL.md:429` "An executor of the strongest class that fails" without "available" —
  item 1 limits the skill to its two places, and the meaning is the same.
- WAY-216's binding line "gives it and its kind guidelines" (`foundations/decisions.md:8370`) — a
  short line item 19.10 does not name.
- The other short lines of WAY-287 that stand from the base (e.g. "and gives the", "or *Derives from*
  or a") — no item names them.
- `foundations/part_map.md` sentence of `project-level` with five "and for" — the task sends it to
  another task (data file item 23).

## Checks run

- `git rev-parse HEAD` → `dfe14f7acba448a90e430d7469941fe1c6ad713c`; `git status --short` → clean.
- `git log --oneline 0dae56b..dfe14f7`, `git diff --stat`, `git diff` of the range; `git diff
  --word-diff=plain --word-diff-regex='[^[:space:]]+'` of the log → read whole.
- Script mapping each hunk of the log to its entry (61 hunks, 29 entries), and script comparing each
  entry's words at base and head (11 rewrap-only, 18 with word changes).
- Script listing mid-paragraph lines under 75 or over 100 characters in the touched entries at base
  and head; compared with the places of the data file at `21ecb62` (`sed -n` on
  `git show 21ecb62:foundations/decisions.md`).
- `python -B elements/common/foundation_check.py` → exit 0, `0 errors`.
- `python -B task-cycle/change_file_sizes.py 0dae56b dfe14f7` → exit 0.
- `python -B gate/run_tests.py <dir>` → exit 0 each: `elements/common` (242), `agent-instructions`
  (27), `instruction-files` (105, 5 skipped), `product-guidelines` (14), `project-level` (278),
  `elements/part-map` (40), `task-cycle` (514). Full gate not run (the orchestrator's run).
- `curl` of today's pages (`code.claude.com/docs/en/prompt-caching.md`, `memory.md`, `skills.md`,
  `platform.claude.com/.../model-deprecations`, `developers.openai.com/api/docs/deprecations`) and of
  the five cited captures (`id_` form); a script checking every quoted passage of the seven facts
  against both → 20 of 20 found in each. Positive controls: the old passages "at launch alongside" and
  "may be deprecated in the future" → 0 hits on today's pages; the first run without the
  punctuation-space normalisation reported the ttls passage missing in the capture, which reading the
  capture's text showed to be a link boundary, not a different wording.
- Archive index (CDX) of each page from 2026-11-01: the cited captures are the latest.
- `python -B elements/common/decision_index.py` with `--sections`, then 21 `--section`, 12 `--part` and
  43 `--decision` switches → index of 156 decisions in full and 42 by heading, read whole.
- Searches: `git grep` for review classes (above), for `at launch`, for `gate_runs`, for
  `starting_rules.md`, for `locations` in `process-audit/`, and over the review's data file.

## Reaches beyond the dispatch

- The review's data file in the author's notes (`foundation_review_2026-11-14.md`, section "Drobne
  poprawki brzmienia", lines 2110-2145) — the task's *Context* names it as the source of item 19; read
  to find the two WAY-339 places and the item numbering.
- `git show 21ecb62:foundations/decisions.md` and `:foundations/part_map.md` — the line numbers of the
  data file refer to that commit.
- `git show 07cbcf8:docs/task-cycles/decisions-as-material-at-refinement/task.md` question 5 — the
  source of item 6, named in the task's *Context*.
- `elements/environment-facts/template.md` whole — the rule on archived copies and one fact per entry.
- `task-cycle/skill/request_template.md` (kinds 12, 13), `process-audit/SKILL.md:28`,
  `task-cycle/gate_times.py:21,282`, `product-guidelines/audit_end.md:54-77`,
  `product-guidelines/coding/hand_back.md`, `product-guidelines/testing/hand_back.md` — to check that
  the new sentences of WAY-287, WAY-27, WAY-320 and item 18 are true of the files.
- `foundations/glossary.md` entries *binding part*, *binding sentence*, *return step*, *slice*.
- The web pages and archive captures above.

## Working copies

- `.runs/review-whole/` — diffs,
  scripts, the index, the downloaded pages and captures, test outputs. Removed before return; nothing
  kept in `reports/` (this report quotes what it needs). No worktree or clone was made.

## Unread material

Decisions of the index read whole: 33 — WAY-05, 07, 10, 27, 35, 44, 85, 121, 129, 130, 131, 132,
133, 140, 141, 147, 161, 229, 241, 255, 287, 313, 320, 330, 360, 363, 375, and WAY-162 (binding whole,
the rest by its hunk), WAY-134 (binding whole), WAY-339 (binding and the changed hunks), and the
rewrap-only entries by word comparison rather than reading. Decisions bearing on the change that
stayed unread whole: WAY-09, WAY-52, WAY-173, WAY-372 (index text only; the change only points to
them or matches their wording), WAY-308 and WAY-316 (index text only), WAY-337 (index text only),
WAY-90, 124, 126, 206, 216, 243, 328, 365 (word-identical rewraps; not read for meaning). Guideline
files: none selected — the-way has no product guidelines (WAY-328), and `product-guidelines/reading.md`
finds none. Invariants read whole: `repository-file-location`, `elements-pending-marker`,
`generated-overview`, `installation-claude-guidance`; other invariants of the touched parts not read.

## Searches not found or unclear

- The author's report says the 2026-11-14 capture of the prompt-caching page words the TTL sentence
  as "bills cache writes at a higher rate"; no such text stands in that capture or on today's page
  (M-2).
- Item 19.15 names "two places" of WAY-339; at `0dae56b` the first place of the data file
  (`21ecb62:8176-8177`, the binding text "…the times of the gate: a new") no longer stands as a
  short line, so which two places the item means at the base is unclear; the second place stands
  unchanged (M-1).
