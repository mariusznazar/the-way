PASS d48638a7d493c4913be74d08477c3eb2f4d35906

# Review of correction 1 and the unread reading: decision-sources-and-leftouts

- Variant: a later change to an open request, a correction (`task-cycle/review/fix.md`). The
  human's remarks take the place of a findings file. Correction range: `b679864..d48638a`, one
  commit, `foundations/decisions.md`, 42 lines added and 14 removed. Whole change for context:
  `aba5ee92a0734c2e775cc69662af669bf6455795..d48638a`.
- `git rev-parse HEAD` in the worktree gives `d48638a7d493c4913be74d08477c3eb2f4d35906`, the head
  I was given. The worktree is clean.
- Blocking findings: 0. Minor: 6 (Part A: 5, Part B: 1). Out of scope: 1.

## The remarks, made or not

1. **Item 1 (fix WAY-145, WAY-139 and WAY-165 by the rule of the 25 entries): made.** Each of the
   three now names the course practice it takes, says that the course's lessons are not open to a
   reader of this repository, lists its leftovers in *Rejected*, and has `derives from WAY-100`.
   Every element the entries say the practice has is in the source (see the table under Part A,
   check 1). No leftover is invented, which was the I1 fault, and no reason fails the trace. Five
   Minor findings remain on precision and completeness (M1 to M5).
2. **Item 2 (read what the review of the whole change left unread): made by this review.** See
   Part B.
3. Items 3 to 6 of "You accept by merging" need no change. I did not run the full gate.

## Part A: review of the correction

### Check 1: source fidelity, element by element

Sources read: the course skill `10x-roadmap` (`git show archive/10x-m2l1:.claude/skills/10x-roadmap/SKILL.md`
in the author's local repository of course trials, the author's repository of course trials), the author's map of the course
package (rows of m1l5, m2l1, m2l4 and m3l5), the lesson note of m1l5 (§ "infrastructure.md - nowy
kontrakt", whole) and the lesson note of m3l5 (whole).

| Entry, element the change writes | Where the source holds it | Verdict |
|---|---|---|
| WAY-145, taken: each open question of the source carried into the plan word for word | skill 6f, line 411: "PRD's `## Open Questions` — copy verbatim" | in the practice; but see M1 for which entry carries it |
| WAY-145, taken: a question arising in the breakdown put before the human | skill 6f, line 412 (new questions from Step 5 go into Open Roadmap Questions); line 407 ("surface these so the user can resolve them"); map m2l1, row "Blokery zewnętrzne…", verdict (ii) | holds, in changed form as the map gives it |
| WAY-145, own: the move written into the log of changes | map, same row: the questions were moved silently in trial A | holds |
| WAY-145, existing item marked: blocked flag and list of deferred work "as the practice of a roadmap has them" | skill 6e–6g, lines 407, 416, 593; map row "Odrzucam flagę blokady … i listę *Parked*" | in the practice; the reason for the list goes beyond the skill, see M5 |
| WAY-145, new: blockers outside the team kept apart from unknowns | skill line 404 ("vendor approval, design asset, stakeholder decision"), line 592 | in the practice; no reason, and the map gives none |
| WAY-145, new: an owner for each unknown | skill lines 405, 543 ("Owner: <user\|team\|TBD>") | in the practice; no reason, and the map gives none |
| WAY-139, taken from m1l5: preview of deployments, where the secrets lie, rollback and its steps, which actions take a human, how the agent reaches the logs | lesson note m1l5, the document's skeleton: "Podgląd wdrożenia", "Sekrety", "Rollback - ile minut i ile kroków", "Uprawnienia", "CLI / MCP / API fit … czy logi są dostępne przez API"; map m1l5 row "`infrastructure.md` jako trzeci kontrakt" | holds; the last item narrows its element, see M2 |
| WAY-139, taken from m3l5: the record's life and a failure (WAY-270) | map m3l5 rows 4, 7, 8, carrier "WAY-165, WAY-270, WAY-139" | holds |
| WAY-139, new: the platform chosen and its reasons, with a reason | lesson "Wybór i uzasadnienie"; reason from the map row: "wybór i jego powody niosą decyzje the way" | in the practice; the reason is traced |
| WAY-139, new: stack fit; known risks; region, runtime and plan; the signal of a change | lesson "Dopasowanie stacku", "Ryzyka - lista znanych ograniczeń", "Decyzje techniczne - region, runtime, plan abonamentowy", "Sygnał zmiany decyzji … gdy projekt wyjdzie z fazy MVP" | all in the practice; no reasons |
| WAY-139, existing item marked: a document of operations "as the lesson's document of the infrastructure is" | lesson § "infrastructure.md - nowy kontrakt" | the document exists; the reason next to it reads ambiguously, see M3 |
| WAY-165, taken: how long the record lives | lesson note m3l5 § "Observability", the table of Workers Logs retention (3 and 7 days); map row 7 ("retencja") | holds |
| WAY-165, existing item extended: the identifiers that tie the events of one operation | lesson table "Identyfikatory żądań … Jak połączyć zdarzenia dotyczące jednej operacji"; map row 4 ("identyfikatory … są w kodzie, więc idą do wytycznych") | in the practice; the reason is the entry's own and agrees with the map |
| WAY-165, new: technical and business metrics; history of changes and deployments | lesson table "Metryki techniczne i biznesowe", "Historia zmian i wdrożeń" | in the practice; no reasons, and the map gives none |

### Check 2: what the remarks allow

- Reasons: each reason the correction adds or ties to the practice comes from the entry itself
  (WAY-145's blocked flag and list, WAY-139's document of operations, WAY-165's identifiers) or from
  the map (WAY-139's platform choice). No new item carries a reason the trace does not give.
- `derives from WAY-100` is added to all three (`foundations/decisions.md:3735`, `:4411-4412`,
  `:4535`).
- The closed-lessons clause is in all three (`:3759`, `:4483-4484`, `:4595-4596`).
- Privacy: none of the added lines holds a vault name, a note link, a drive-letter path, a drive letter with forward slashes, `Users`, `vault`, `TODO` or
  `mapa`. The search did match the `+++` header line, which shows that it works.
- Binding sentences: my own script compares the text before `- **Scope:**` of every decision.
  Base to head: 223 entries at each commit, none added or removed; binding text changed only in
  `['WAY-100']`. `b679864` to head: binding changed `[]`; entries changed
  `['WAY-139', 'WAY-145', 'WAY-165']`.

### Check 3: WAY-139's history

- Trace: WAY-139 came from the m1l5 adoptions (`53b3827`, "Adopt … a deployment skill's list").
  It had `derives from WAY-100` at `597edec`, at `4a3ee37` and at `8d04d89~1`, and lost it at
  `8d04d89`. Its *Based on* was `none` at every one of those commits.
- Second round (`cfd275c`): its plan, row F3 (c), reads "loses `derives from WAY-100`, its source
  staying in *Based on*". Its foundation report gives the reason "the entry no longer claims to adopt
  a practice from outside". The rule of that task (question 3) is: "only those that name the
  adopted practice" carry the relation. So the removal judged WAY-139's text, which named no
  practice. It did not judge the trace. The row's own label, "its source staying in *Based on*",
  did not fit WAY-139, which had no source there.
- Judgment: the fix follows the source. The map's m1l5 row names WAY-139 as the carrier of the list
  ("przejmuję w zmienionej postaci" → WAY-139), and the m3l5 rows 4, 7 and 8 carry it too. Now that
  the entry names the practice, the same second-round rule gives it the relation back. That earlier
  statement gives no reason that this fix contradicts without saying so. The frozen task's *Out of
  scope* lists WAY-139 as "use the source as evidence". That came from the F3 (c) grouping, and for
  WAY-139 there was no source to use. The correction does contradict that *Out of scope* line. The
  author's report says so. The human's remark names WAY-139 and binds. **For the request:** the
  description must say that this correction goes against that line of the task's *Out of scope*,
  and why.

### Check 4: consistency

- WAY-270 (`:4351-4354`) says the two questions bind "by this decision, by WAY-165 and by WAY-139,
  and nowhere else". WAY-165 now credits m3l5 only with the record's life, and WAY-139 credits it
  with the record's life and the failure item "(WAY-270)". The three entries agree.
- WAY-142 (`:4887-4890`) and WAY-145 (`:3761-3764`) both put the parked list and the blocked state
  outside what they take. Their reasons agree: the plan's states hold waiting for the human, and
  the list repeats or copies the definition's exclusions. There is no contradiction. The same leftover
  now stands in two entries, which is a duplicate but not a defect.
- WAY-143, 144, 146 and 147 have nothing on owners, external blockers or parked items that the new
  items of WAY-145 would contradict. WAY-121 (`:3838` area) credits the lesson "Towards Autonomous
  Product Development" with the logs, the interface and the development data. WAY-165 credits m3l5
  only with the record's life. These agree.
- `python -B elements/common/foundation_check.py`: exit 0, `0 errors`.

## Findings

### Minor

**M1: WAY-145 credits its own rule with carrying each open question word for word, but that rule
stands in WAY-142 and WAY-146.** Within the task (correction item 1).
- Place: `foundations/decisions.md:3756-3758`: "The rule takes from the practice of a roadmap
  (WAY-142) the carrying of each open question of the source into the plan word for word".
- What is wrong: WAY-145's binding sentences (`:3723-3730`) say who sets where a question is
  resolved, how the plan moves a question, and that a new question goes to the human. They do not
  say that the plan copies the questions word for word. That copying is WAY-142's binding sentence
  ("The plan also holds each open question of the definition, word for word", `:4834`), and
  WAY-146's script checks it (`:4974-4975`). WAY-142's *Rationale* does not credit the practice
  with it.
- Why it matters: WAY-100 asks a decision to name "what it takes from" the practice. A reader of
  WAY-145 thinks this rule carries the copying. A reader who changes WAY-142's "word for word" does
  not learn there that it came from the course. The element is real in the practice (skill 6f, line
  411), so this is a misplaced credit, not a made-up one.
- Possible wording: "The rule builds on the plan holding each open question word for word, as the
  practice of a roadmap (WAY-142) carries it, and takes from that practice a question that arises in
  the breakdown put before the human; …".

**M2: WAY-139 reduces the lesson's "CLI / MCP / API fit" to "how the agent reaches the logs". The
rest of that element is neither taken nor in *Rejected*.** Within the task.
- Place: `:4482`, "and how the agent reaches the logs"; *Rejected* `:4492-4500`.
- What is wrong: the lesson note m1l5 defines the element as "co platforma daje agentowi do
  operability po deployment (jakie CLI, czy jest gotowy serwer MCP, czy logi są dostępne przez
  API)", that is, what the platform gives the agent to operate the product after deployment.
  WAY-139 takes the logs part. The CLI and the MCP server for operating the product appear nowhere
  among the leftovers. The new leftover list is thorough for the other five elements of the same
  document. Two smaller parts are dropped in the same silent way: the minutes of a rollback ("ile
  minut i ile kroków"; the entry takes the steps only) and who has access to the secrets
  ("kto ma dostęp").
- Why Minor: this is the same kind of fault as M1 of the first review. The entry describes the
  practice as narrower than it is. No binding sentence rests on it.
- Fix: add "the CLI and the server of tools the platform gives an agent to operate the product,
  which that document holds — left out of what the list takes from the lesson". The minutes and
  the access can be added the same way, or left with a word in the request.

**M3: tied to the lesson's document, WAY-139's existing reason "no step reads it" reads as a claim
about the practice, and the lesson contradicts that claim.** Within the task.
- Place: `:4492-4493`: "a document of operations kept beside the product, as the lesson's document
  of the infrastructure is — no step reads it, so it goes stale unread".
- What is wrong: in the lesson the document is read. The lesson note m1l5 says "Plik
  **infrastructure.md** jest wsadem do **Plan Mode** … Agent dostaje go razem z **tech-stack.md**",
  so the document is the input to the plan of the deployment. The map's own notes on m1l5 record
  that the trial's plan B took items from it. The reason is true of the-way's rejected option, since
  no step of the-way would read such a document. The map row's evidence is given "soczewki the way,
  `loop2`". But the inserted "as the lesson's document … is" puts the lesson's document in front of
  "no step reads it". Grammatically the reason belongs to the-way's option. Even so, a reader
  checking the course finds the opposite of what the sentence seems to say, which is the risk the
  task exists to remove. In the same place, the *Rationale* (`:4479-4480`) says the lesson "has an
  agent keep" the document. The lesson has a skill write it and makes the content the human's
  ("ostateczna treść **infrastructure.md** jest twoja … Skill jest tu silnikiem, nie redaktorem").
- Why Minor: the reason is the entry's own and is true for the-way; the fault is in how the
  sentence reads.
- Possible wording: "… as the lesson's document of the infrastructure is, which there feeds the plan
  of the deployment — no step of the-way reads it, so it goes stale unread"; and "the document of
  the infrastructure the lesson keeps beside the product".

**M4: WAY-165's new leftovers from the lesson's table of the sources of a diagnosis are
incomplete.** Within the task.
- Place: `:4601-4607`.
- What is wrong: the entry now lists three sources of a diagnosis from the lesson's table: the
  identifiers, the metrics, and the history of changes and deployments. The table "Dane o
  zgłoszeniu i działaniu aplikacji" has five rows. The first row, "Ticket, screenshot lub nagranie",
  meaning the user's report, is neither taken nor left out. The second row, logs and stack trace,
  matches the logs matter. The section WAY-165 takes the record's life from ("Observability",
  Workers Logs: sampling, retention, cost; map row 7) also holds sampling
  (`head_sampling_rate`), which is not listed.
- Why Minor: no leftover is false. The list is shorter than the practice it now enumerates, so a
  reader may take the user's report as weighed and dropped by nothing.
- Fix: add "the report of the user, with a screenshot or a recording, that the lesson counts among
  those sources — left out of what the matter takes from the lesson" and, if wanted, the sampling of
  the platform's logs.

**M5: WAY-145's reason for the list of deferred work is now tied to the practice, and it repeats
N1's overgeneralization.** Within the task. It is the same matter as N1 of the review of the fix
(WAY-142), and one wording fixes both.
- Place: `:3762-3764`: "a flag … beside a list of deferred work, as the practice of a roadmap has
  them — … the list repeats the definition's exclusions".
- What is wrong: skill Step 6g (line 416) builds Parked from the PRD's Non-Goals "Also append[ing]
  anything Step 5 surfaced as deferred". Before the correction, the reason described a list that
  the-way rejected in general. Since the correction marks it as the practice's list, it now states
  something about the practice that the skill holds only for part of the list. The map's row gives
  "*Parked* w A to kopia „Out of scope”", which describes the trial A, not the skill.
- Why Minor: as with N1, it changes no rule.
- Possible wording: "the list mostly repeats the definition's exclusions".

### Outside the task's scope

**O1: the course name is spelled two ways in the log.** The base already had both spellings
(`10xDEVS` 4 times, `10xDevs` twice). At the head there are 5 and 10. The correction follows WAY-270
and WAY-273 in WAY-165 (`10xDEVS`) and WAY-142 in WAY-139 and WAY-145 (`10xDevs`). This is polish
outside the task. Making the spelling uniform belongs to a pass over the whole log.

## Part B: what the review of the whole change left unread

### Read whole

- **WAY-256** (`:3361-3473`): heading, binding sentences, *Scope*, *Based on*, *Relations*,
  *Verification*, *Origin*, *Rationale* and *Rejected*, every field.
- **The lesson note of m2l4** (the course's lesson on research and implementation, 438 lines).
- **The lesson note of m3l5** (the course's lesson on debugging with AI, 473 lines).
- **The map rows** that carry the leftovers of these lessons: m2l4 rows 1 to 19 (the whole table and
  its notes); m3l5 rows 1 to 23 (the whole table), its notes, and its state line, which I read only
  for the carriers and the dates.

### WAY-256 against the change's addition

The change adds "whose lessons are not open to a reader of this repository" to the sentence that
says the shape "is borrowed from a course on steering models through context" (`:3429-3431`).
Read whole, the entry agrees with it:
- It names what it takes ("only that shape is adopted (WAY-100)").
- It says what it does not take: the course's claim about long skills, with a reason in *Rationale*
  ("since no measurement stands behind it") and in *Rejected* ("a short skill as the aim, after the
  course's claim — no measurement stands behind it", `:3448`).
- Its *Based on* (`single-rule-compliance · instruction-density-accuracy`) names environment facts,
  not the course, so the course is described in *Rationale*, as WAY-27 and the new WAY-100 ask.
- The entry already uses the same wording for its own estimate ("its record is not open to a reader
  of this repository", `:3417`, `:3458-3459`).
Nothing in the rest of *Rationale* or in *Rejected* conflicts with the addition. No finding.

### The leftovers and reasons against the lesson notes

| Entry, item | Lesson note | Verdict |
|---|---|---|
| WAY-268, taken: a decision resting on a source that can be checked, not on a model's memory (`:4197-4200`) | m2l4: grounding ("Nie zrobiliśmy tzw. **groundingu**"); "zamiast na pamięci modelu opieramy decyzje na źródłach, które da się sprawdzić" | holds |
| WAY-268, leftover: a search engine built for agents, reached through a tool server; reason: a choice of a provider of search, not a step (`:4221-4223`) | m2l4 § "Exa.ai jako AI-native search" ("Potrzebujemy MCP"); map m2l4 row 4 | holds; the lesson itself advises against switching a working provider |
| WAY-268, leftover: current documentation of a library put into context before the plan; reason: an agent fetches it when it needs it, "rather than all of it ahead" (`:4223-4226`) | m2l4 § "Context7 jako live library docs": `query-docs` returns documentation "docięty pod budżet tokenów", fetched for the chosen library and the slice | the leftover holds; the reason's contrast "all of it" does not, see M6 |
| WAY-270, taken: how long the record lives, how a human learns of a failure (`:4351-4354`) | m3l5 § "Observability" (retention table); § "Sentry MCP" | holds |
| WAY-270, leftover: a tool that collects failures set up ahead of the choice, through the lesson's own path of a change; reason: the step chooses the tool, absence among the options (`:4373-4375`) | m3l5: "Jeśli nie masz jeszcze Sentry … przejdziemy przez konfigurację"; "Możesz skorzystać ze ścieżki /10x-new → /10x-plan → /10x-implement"; exercise 2; map row 22 | holds |
| WAY-270, leftover: an agent reaching the failures through the tool's server instead of being given them; reason: WAY-121 settles how an agent reads the record (`:4375-4378`) | m3l5 § "Krok 3: Sentry MCP"; § "Połącz agenta…" ("bez czekania, aż wkleisz je do rozmowy"); map row 6 | holds |
| WAY-273, taken: a failure not hidden; first stop hiding, then fix the cause (`:4676-4678`) | m3l5 § "Fix": "Najpierw przestajesz ukrywać, co dzieje się w systemie, a dopiero gdy błąd jest widoczny, możesz go porządnie obsłużyć i naprawić" | holds |
| WAY-273, leftover: the search for hidden failures as a class, by an audit of one critical flow before a user reports them (`:4690-4692`) | m3l5 § "Połknięte błędy": "nie warto czekać, aż każde z nich wypłynie w tickecie. Uruchom na krytycznych przepływach…"; exercise 1 "dla jednego krytycznego przepływu" | holds |
| WAY-139, taken from m3l5: the record's life and a failure | as WAY-270 | holds |
| WAY-165, taken and left out from m3l5 | as in Part A check 1 | holds; incomplete, see M4 |

One remark that I do not count as a finding: map m3l5 row 11 gives a reason for WAY-273's leftover
("przychodzi z wierszem 10 … i istniejącym audytem całego kodu przy rozszerzeniu wytycznych"),
and the entry carries none. The task allows this ("powód stoi przy pozycji tylko tam, gdzie…"). It is
the kind of gap M2 of the first review observed, and it was outside the four entries that M2 named.

### Finding of Part B

**M6 (Minor): the reason of WAY-268's second leftover says the lesson puts "all of" the
documentation into context, and the lesson does not.** Within the task (WAY-268 is a changed
entry).
- Place: `foundations/decisions.md:4225-4226`: "an agent fetches the documentation when it needs it,
  rather than all of it ahead".
- What is wrong: the lesson fetches, before the plan, documentation of the one chosen library,
  "docięty pod budżet tokenów" (cut to a token budget), with `resolve-library-id` and then
  `query-docs` for the parts the slice needs. The contrast that holds is "ahead of the plan" against
  "when it needs it". "All of it" overstates what the lesson does. The words come from the map row
  ("a nie zaciągać całej z góry"), so the remark's rule on reasons allows them. The lesson note does
  not bear them out.
- Why Minor: no rule rests on it. A reader only gets a slightly worse picture of the lesson.
- Possible wording: "an agent fetches the part of the documentation it needs when it needs it,
  rather than ahead of the plan".

## Declined to judge

- Whether WAY-268, WAY-270 and WAY-273 should list more leftovers from their lessons (for example,
  m2l4 rows 1, 2 and 11, research before the plan and the plan pointing to its sources). Part B asks
  whether the lesson notes contradict a leftover or a reason, and the first review judged these
  lists complete against the map's rows.
- The long lines of the added text (`:3758` at 149 characters, `:4500` at 125). The log already
  holds 458 lines over 100 characters at the base, and no check enforces the width.

## Checks run

| Command or method | Exit | Result |
|---|---|---|
| `git rev-parse HEAD`; `git log --oneline aba5ee9..HEAD`; `git diff b679864..d48638a`; `git status --short` | 0 | head as given; one commit in the correction; clean tree |
| `python -B .runs/review-correction/compare_binding.py . aba5ee92a0734c2e775cc69662af669bf6455795 d48638a` (own script) | 0 | 223 / 223 entries; binding changed `['WAY-100']`; 28 entries changed: the 25 of the task and WAY-139, 145, 165 |
| `python -B .runs/review-correction/compare_binding.py . b679864 d48638a` | 0 | binding changed `[]`; entries changed `['WAY-139', 'WAY-145', 'WAY-165']` |
| `git diff b679864..d48638a \| grep '^+' \| grep -i -E <a pattern of vault names, note links, drive letters, user directories and file extensions>` | 0 | only the `+++ b/foundations/decisions.md` header, so the search works and the added text holds none of the terms |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `python -B gate/run_tests.py elements/common` (one directory, not the full gate) | 0 | `Ran 246 tests in 85.021s`, `OK` |
| `git log -S` and `git show <commit>:foundations/decisions.md` for WAY-139 at `597edec`, `4a3ee37`, `8d04d89~1`, `8d04d89` | 0 | relation history in check 3 |
| `git show cfd275c:` the second round's plan, task and foundation report | 0 | row F3 (c), question 3 |
| manual: each element and reason against the skill, the lesson notes and the map (tables above) | — | 6 Minor findings, no invented leftover |

Not run: the full gate. It is the orchestrator's and waits for the day advisor's signal.

## Reaches beyond the dispatch

- The second round's plan and task at `cfd275c` (`docs/task-cycles/decision-log-second-round/plan.md`,
  row F3; `task.md`, question 3). Why: to see what the removal of WAY-139's relation rested on
  (check 3).
- The commits `53b3827`, `597edec`, `4a3ee37` and `8d04d89`. Why: the trace of WAY-139.
- Decisions read whole beyond the three corrected ones: WAY-142, WAY-146, WAY-268, WAY-270,
  WAY-273 and WAY-256. Read in part: WAY-121 (by search for its lesson sentence), WAY-143, 144 and
  147 (by search for owners, blockers, unknowns and parked items). Why: consistency (check 4) and
  Part B.
- The map's m1l5 notes (the line on trial B reading `infrastructure.md`), its verdicts of the
  other m1l5 rows, and the m2l1 notes on moved questions. Why: M3 and WAY-145.
- `elements/decisions/template.md` and the log, searched for *Review when*. Why: the map maps the
  lesson's "signal of a change" to *Review when*. That field is withdrawn (WAY-119), so WAY-139's
  leftover "the signal that would change the choice" holds.

## Working copies

- `.runs/review-correction/` (directly under the ignored `.runs/` of the worktree) held: a copy of
  the course skill `10x-roadmap`, the extracts of the map's m1l5 and m2l1 sections, the second
  round's plan, task and foundation report from `cfd275c`, copies of `foundations/decisions.md` at
  three commits, extracts of WAY-121, 139, 143, 144, 146 and 147, the comparison script
  `compare_binding.py`, and the test output. No worktree or clone was made. I removed the directory
  with `rm -rf` before returning. Nothing was kept in `reports/` beyond this report; the script's
  output is quoted above.

## Unread material

- The course skill `10x-roadmap` (775 lines): read by search for open questions, blockers, unknowns,
  owners and parked items, and lines 395–424 whole. It was not read whole.
- The lesson note of m1l5: § "infrastructure.md - nowy kontrakt" whole, plus its headings. The rest
  was not read.
- The author's map of the course package: the sections of m1l5, m2l1 (rows "Blokery zewnętrzne…"
  and notes on moved questions), m2l4 (whole) and m3l5 (whole). The other lessons were not read.
- The lesson note of m2l1: not opened. WAY-145's elements were checked against the skill and the
  map.
- WAY-143, 144 and 147 at the head: read by search, not whole.

## Searches not found or unclear

- The skill's new questions (Step 6f, "surfaced during Step 5") come from the interview, which runs
  before the breakdown. Whether "a question that arises in the breakdown" is that practice's
  element or the-way's own is a matter of reading. The map files it under the taking "in changed
  form", and I accepted that.
- The author's map gives "*Review when* ↔ sygnał zmiany decyzji" as the-way's equivalent. That
  field is withdrawn (WAY-119), so this part of the map is out of date. It does not change any
  verdict.
