# Author report — agent-test-bypass

**Status:** done with concerns (concerns 1, 2 and 3 below need the orchestrator's eye; none stops the change).

Worktree `the root of the task's worktree`, branch `task/agent-test-bypass`, base `4758840f`.

## Commits

- `477ea5ad` — Add three environment facts for test special-casing and the option to hand a task to a human
- `c8eef488` — Review looks for code that passes a test without meeting the requirement; the author stops on a test the requirement contradicts

## Files changed (added / removed lines, `git diff --stat` of the range)

| File | + / - |
|---|---|
| `foundations/decisions.md` | 133 / 0 |
| `foundations/environment_facts.md` | 18 / 0 |
| `task-cycle/change/SKILL.md` | about 16 / 2 |
| `task-cycle/review/SKILL.md` | 9 / 0 |
| `task-cycle/review/fix.md` | 2 / 1 |
| `task-cycle/skill/SKILL.md` | about 36 / 4 |
| `task-cycle/skill/correction.md` | 5 / 2 |
| `task-cycle/skill/request_template.md` | 7 / 6 |

Total 224 added, 17 removed. No test file and no script changed (reason under *Checks*).

## What the change does, by task item

1. *To do* 1 — `task-cycle/review/SKILL.md` section 2, a new bullet after "The tests: …": the four signals, the narrow qualifier ("Only code whose branch, value or comparison exists to make a test pass is the finding: a special case that the requirement itself asks for is none"), and the grade in section 3 (Important at the least, in every review, so that it blocks). `task-cycle/review/fix.md` names the same look for the review of a fix, since that file bounds what the review of a fix inspects. Section 2 already governs the other reviews (slice, whole change, return step, reconciliation, correction).
2. *To do* 2 — `task-cycle/change/SKILL.md` section 2, a new bullet after "Never weaken an assertion …": no code for the test's input, test and its expected value untouched, commit, return `questions` with a question that names the test, quotes the requirement and says what was tried, plus the recommended answer; a test of behaviour the task expressly changes is changed, with its cause named in the report. Pointers in section 1 (the paragraph "When a value … does not pass your own reckoning"), section 5 (it is no third case of `returned`; commits stay) and section 6 (the `questions` item).
3. *To do* 3 — `task-cycle/skill/SKILL.md`: a paragraph after the paragraph "An agent that returns `questions` gets your answers …" (answer only from the task, the spec, a decision or the sentence of an invariant, the passage quoted; never by the smallest reversible reading; where none settles it, a blocked draft request, by the mechanics of step 9 sub-step 4 for a slice failed twice, with four named differences: no reset, no discard, the wording of *Request URL and status* from `blocked_finding.md`, the template's variant); step 9 sub-step 4 (no retry for an executor that returns such a question); the early-stop sentence at the head of the skill; the list of copies of the record "The record before it is committed". `task-cycle/skill/correction.md`: the human's answer to such a request is the input of a correction, and it is not waited for in CI, as for the other blocked kinds.
4. *To do* 4 — `task-cycle/skill/request_template.md`: kind 2 admits the question; a new row of the table of variants, between "A question from the foundation step" and "An impossible task"; the intro list names the case.
5. *To do* 5 — three environment facts, each read by me from the source (see *Sources*), and two decisions.

## Foundation entries

| Entry | Mark | English meaning (one sentence) | Polish meaning (one sentence) |
|---|---|---|---|
| WAY-409 | `the cycle's` (row 1, whole; a pair of examples added, see below) | Every code review of a cycle looks in the product's code for code that passes a test without meeting the requirement, grades such a finding Important at the least so that it blocks, and judges only code that exists to make a test pass; the rule stands in the review's skill, in every cycle. | Każdy przegląd kodu w cyklu szuka w kodzie produktu kodu, który przechodzi test bez spełnienia wymagania, ocenia takie znalezisko co najmniej jako Important, więc blokuje, i sądzi tylko kod istniejący po to, by test przeszedł; reguła stoi w skillu recenzenta, w każdym cyklu. |
| WAY-410 | `the cycle's` (row 2, whole; a pair of examples added) | An agent that meets a test the requirement contradicts, or that it cannot pass by general code, writes no code for the test's input and does not change the test but commits and asks the orchestrator, which answers only from the task, the spec, a decision or an invariant and otherwise opens a blocked draft request with the question; a slice's executor gets no retry on a higher class. | Agent, który trafia na test przeczący wymaganiu albo taki, którego nie umie przejść kodem ogólnym, nie pisze kodu pod wejście testu i nie zmienia testu, tylko commituje i pyta orkiestratora, który odpowiada wyłącznie z zadania, specyfikacji, decyzji albo niezmiennika, a inaczej otwiera zablokowany szkic PR-a z pytaniem; wykonawca części planu nie dostaje ponowienia z wyższą klasą. |
| `claude-test-special-casing` | `the cycle's` (no row; commanded by *To do* 5) | The system card of Claude 3.7 Sonnet reports that the model occasionally special-cases tests (returning expected values, modifying tests), often marking it with a comment, and names monitoring for such comments and for test modifications among its mitigations. | Karta systemowa Claude 3.7 Sonnet podaje, że model czasem obchodzi testy (zwraca oczekiwane wartości, zmienia testy), często znacząc to komentarzem, i wymienia monitorowanie takich komentarzy i zmian testów wśród łagodzeń. |
| `impossiblebench-cheating-strategies` | `the cycle's` (no row) | ImpossibleBench names four cheating strategies and reports that the latter three work around instructions not to modify tests while technically complying. | ImpossibleBench wymienia cztery strategie oszukiwania i podaje, że trzy ostatnie omijają zakaz zmiany testów, formalnie go przestrzegając. |
| `impossiblebench-abort-option` | `the cycle's` (no row) | In ImpossibleBench, an option to abort with a flag for a human lowered the cheating rate of GPT-5 from 54% to 9% and of o3 from 49% to 12%, with a much less pronounced effect on Claude Opus 4.1. | W ImpossibleBench opcja przerwania z flagą dla człowieka obniżyła odsetek oszustw GPT-5 z 54% do 9% i o3 z 49% do 12%, a dla Claude Opus 4.1 efekt był znacznie słabszy. |

Why every entry is marked `the cycle's`: the two decisions carry a pair of examples that neither row gives (the foundation check reports a decision that nothing holds, and the rows give no test, since the rule is a text that instructs agents), and the three facts are carried by no row; *To do* 5 asks for them.

### The pairs of examples I added, word for word (for the description to quote under the entries)

WAY-409:

- complies: a reviewer finds that a function of the product returns 180 for the input 200 that a test uses, where the requirement gives a general rule that would not return it, grades the finding Important and the review fails; the same for a branch under a comment that says "special case for the test", and for a comparison operator overloaded so that the comparison a test makes comes out true; a product whose guidelines hold no testing discipline gets the same look; a branch on a value that the requirement itself names is no finding;
- violates: a reviewer reads the files of tests and leaves the code of the product unread for this; a finding of such code is graded Minor and the change passes; a reviewer reports every special case of the product's code, the ones the requirement asks for among them; a review of a fix or of a correction leaves the look out.

WAY-410:

- complies: an author whose test expects 180 for an input of 200, where the requirement says the discount never exceeds 10 percent, writes no branch for 200, leaves the test as it is, commits its work and returns a question that names the test, quotes the requirement and says what it tried; the orchestrator finds in the task the sentence that settles it and resumes the author with that sentence quoted, or, where the task, the spec, the decisions and the invariants say nothing, opens a blocked draft request with the question under *Needed from you*; the executor of a slice that returned such a question is not replaced by one of a higher class; a test that checks behaviour the task expressly changes is changed by the author, who names the requirement as its cause;
- violates: an author writes a branch or a returned value for the input of the test; an author changes the expected value of a test to the code's output to turn it green; an author continues after meeting a contradiction and notes it in its report; the orchestrator answers such a question by the smallest reversible reading of the requirement; the cycle opens a blocked draft request for a contradiction that a sentence of the task settles; the executor of a slice that returned such a question gets a retry on a class higher.

Placement: WAY-409 closes the section *Review of a change* (after WAY-364), WAY-410 closes *The work of a cycle's agents* (after WAY-408); the numbers 409 and 410 are the next free after the highest entry (408) and the highest withdrawn number (371). The facts stand after `impossiblebench-test-modification`. No topical section is opened, no glossary entry, no invariant, no part-map change (`task-cycle/**` already holds every changed file).

Search of the whole foundation (WAY-33): entries touched are WAY-229 (narrowed by WAY-410, named in its *Relations*; left unedited, since the narrowing stands in the new entry), WAY-227 (WAY-410 derives from it), WAY-161 and WAY-13 (WAY-409 derives from them), WAY-03 (cites `impossiblebench-test-modification`, unchanged), WAY-135 and WAY-268 (a contradiction of a test is no open design choice and no reserved choice; WAY-410's *Rationale* says so for WAY-135), WAY-233 and WAY-232 (the test side, unchanged). No invariant names the changed rules. Nothing else needed a correction.

## Sources (the facts of *To do* 5)

- The system card of Claude 3.7 Sonnet: fetched from `https://www-cdn.anthropic.com/9ff93dfa8f445c932415d335c88852ef47f1201e.pdf`, text extracted with `pdftotext -enc UTF-8`; chapter 6 and 6.2 read by me. Every passage in the entry was matched word for word against the extracted text by a script (the apostrophe in "code’s output" is U+2019, as the card sets it). I did not quote the sentence in 6.2 that holds the typo "epecial-casing".
- ImpossibleBench, `https://arxiv.org/html/2510.20270v1` (the edition the existing fact cites) and the PDF `https://arxiv.org/pdf/2510.20270v1`: I read § 3.1, § 4.1, § 4.2, § 5.2 and § 5.3 in the HTML and matched the figures in the PDF text (`from 54% to 9%`, `o3 from 49% to 12%`, "much less pronounced for Claude Opus 4.1", "The latter three strategies …"). Every passage in the two entries matched the HTML text word for word. Both numbers of the task are confirmed. "Three of four strategies" is confirmed in § 4.1 as "The latter three strategies are especially concerning, as they demonstrate that models can devise creative workarounds even when they technically comply with instructions not to modify tests."

## Checks

- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`.
- `python -B gate/run_tests.py task-cycle` — exit 0 (534 tests, 2 skipped; the tail is kept in `reports/author-task-cycle-gate-tail.txt`). It includes `test_request_check.py`, whose template tests read `request_template.md`, so the new row of the table and the edited kind 2 are covered by them.
- Not run: the full gate (not mine, WAY-160). No test written: the change is prose for agents and entries of the foundation; the method says a text that instructs agents is tested by what an agent does with it, and a mechanical text-match would test wording (see own-work check). Hence the pairs of examples in the two decisions.
- `task-cycle/request_check.py` and `task-cycle/test_request_check.py` are unchanged on purpose: the form check reads headings, the three groups, content or `none` and the language; it reads no row of the table of variants and judges no content (its docstring says so), and its `State:` line already admits `blocked`. The new row therefore needs nothing in it. (The handoff said "where the form check reads the table of variants"; it does not.)

## Own-work check (WAY-164)

- Requirement most likely not met: the one the orchestrator's caution (b) and WAY-263 name together — that the skills restate the decisions without widening them or dropping a qualification. Likeliest slip: the reviewer's wording widening to every special case, or the orchestrator's wording answering "from the sources" without "never the smallest reversible reading", or the executor getting a retry on a path I did not name.
- Check: `reports/author-own-work-check.py` (a script that reads the five edited files and asserts each element of the two decisions in the skills' words, with 18 assertions: the four signals, the narrow qualifier, the grade and "in every review", the author's three acts and its exception, the four sources, the ban on the smallest reversible reading, the blocked draft, the no-retry sentence, the template row and kind 2, the two entries and the `narrows WAY-229` relation).
- What it showed: `python -B author-own-work-check.py <worktree>` — 18 of 18 ok, exit 0. Run against the base files (`git show 4758840f:<file>` into a scratch directory) it failed 18 of 18, so it separates the changed text from the unchanged. It checks wording, so it proves that each element is present, not that an agent reads it as intended; the reviewer's reading remains the real test.
- A real gap the check led me to: step 9 sub-step 4 retries an executor "that reports a failing check of its slice", and an executor stopped by a red test it cannot pass fits that words exactly; without the no-retry sentence the cycle would have reset the slice and re-run it on a stronger class, which is what the task forbids. The sentence is in.

## Walk through the running product (WAY-406)

The change alters no behaviour a user sees in a running product: it changes the text of the process (four skill files, a template) and the-way's foundation; no screen, API, command or data the product shows changes. So no walk, no cases, no screenshot.

## Choices (each with the way rejected and its cost if wrong)

1. **The layout of the new row of the request template** (*To do* 4). Made on the pattern of "A question from the foundation step" (its first line, its *Needed from you*) and "A reserved choice" (its lower part with **Route**, *Checks*, *How to merge*: do not merge). Rejected: a row copied from "A blocking finding remains" with **Blocking findings left**, since nothing was reviewed and no finding exists. Cost if wrong: one row to rewrite.
2. **Status of the author's return: `questions`**, not `blocked` and not `returned`. The task says "commits what it has and returns to the orchestrator with a question"; `questions` is the status of exactly that in the method (section 6), the orchestrator already answers it, and the branch stays. Rejected: `returned` (the attempt would be discarded and the work lost, and the task's text forbids a third reason of return without code); `blocked` (it is for a missing fact or permission and for a question the foundation step leaves to the human; the orchestrator would then have no occasion to answer from the sources first). Cost if wrong: the status word in four places.
3. **The blocked draft by pointer, in `SKILL.md`, not a new file.** The procedure of the stop (gate, stages, record copy, draft, no CI wait) already stands inline in step 9 sub-step 4; I point to it and name four differences (no reset, no discard, the wording from `blocked_finding.md`, the variant). Rejected: a new `task-cycle/skill/test_question.md` (WAY-256 would put a fragment only one variant needs into a file, but this one is a pointer plus four differences and would name two files from one; it also would need naming in `SKILL.md` by WAY-265 and a place in the list of the record's copies) and an extension of `blocked_finding.md` (its title and its trigger are a remaining blocking finding). Cost if wrong: moving the paragraph to a file later.
4. **Three new facts, not one.** The task asks for one fact (the card) and the numbers "in the entries"; I wrote the card as `claude-test-special-casing` and the ImpossibleBench findings as two entries by what each says and what changes it: `impossiblebench-cheating-strategies` (the strategies, supports WAY-409) and `impossiblebench-abort-option` (the 54%/9% figures, supports WAY-410). Rejected: putting the figures into the existing `impossiblebench-test-modification` (the template: one entry, one fact, one reason to change; WAY-03 rests on that entry and would be checked for a change it does not need). WAY-409 and WAY-410 both cite the card fact and `impossiblebench-test-modification` as the task asks, and each cites the one extra fact it needs. Cost if wrong: merge two entries.
5. **`review/fix.md` and `correction.md` touched** (beyond the four files): the review of a fix names the look, since that file bounds what the review of a fix inspects and says only "what the fix itself broke"; the correction after review gets the human's answer to the blocked draft as its input, and the no-wait-for-CI clause names the new blocked kind. Rejected: leaving them (a fix that special-cases a test would pass its review by the file's letter; the blocked request would have no way on). Cost if wrong: two small edits to revert.
6. **Pair of examples, hence `the cycle's`** for WAY-409 and WAY-410 (above); the alternative was a test that holds a sentence of the decision by a line `decision:`, rejected as testing wording.
7. **No new `Discarded attempt` marker, no record template change.** The blocked draft keeps the commits and discards nothing, so WAY-404 and WAY-405 (the form of the contradiction mark and of the reason of a discarded attempt) are not touched. The question stands as a row of the questions table by the existing rules.

## Concerns

1. **The abort-option evidence is much weaker for Claude than the task's text says.** The task's *Context* and *Not chosen* give "54% to 9%" for GPT-5; the paper says the strategy was "quite effective for OpenAI models" and that "the effect is much less pronounced for Claude Opus 4.1". The process's agents run on Claude. I wrote the fact whole, with the caveat, and WAY-410's *Rationale* says that the quantified part is taken across publishers (WAY-85), that its size is no promise for the process's agents, and that the reason for the way out stands without it. Whoever accepts the task's source should know the task's line "obniżyła odsetek oszustw GPT-5 z 54% do 9%" carries only half of it.
2. **WAY-328 is withdrawn.** The task cites it ("the-way od przewodnika testów odstępuje (WAY-328)"); the log lists it as withdrawn, "the coding guidelines and the testing guidelines of the-way's own are written, so neither is missing and the departure … has ended", successors WAY-379 and WAY-392, and the-way now adopts the testing template (WAY-392). So the reason "the rule in the template works only in a product, not in the-way" of the task's *Not chosen* is stale. In WAY-409's *Rejected* I kept the reasons that still hold (it works only in a product that adopted the template; it is no rule on the content of a test file) and dropped the stale one. The *Rejected* of a decision written from a row should hold the source's reasons; this is a departure from the source's wording, made because the reference no longer exists. A human may want to say it explicitly at the merge.
3. **The figure "83 task cycles".** WAY-409's *Rejected* carries "no case is known from the 83 task cycles of the process's author counted in his register of problems of 2026-11-12 (his own record, not open to a reader of this repository)", taken from the task's *Not chosen* and *Context*; I could not open that register and the date of the count is my reading of the task's *Context* (the register of 2026-11-12). The sentence says the record is the author's own and not open, as WAY-90 asks. If the count or its date is wrong, the entry quotes a wrong figure.
4. The new paragraph of `SKILL.md` and the row of the template apply to a fix and a correction as well as to the author, since `change/SKILL.md` section 2 binds all variants; I did not write a separate case for a correction that meets the question while the request is open (it returns the request to a draft marked `blocked`, branch not reset). The text allows it and does not spell it out.
5. The two decisions are long in *Rationale*, within the form (no file names, no counts but the measurement named).

## Reaches beyond the handoff (what, where, why)

- `task-cycle/review/fix.md`, `task-cycle/review/whole_change.md`, `task-cycle/change/slice.md`, `task-cycle/change/fix.md`, `task-cycle/skill/blocked_finding.md`, `task-cycle/skill/reserved_return.md`, `task-cycle/skill/correction.md`: read to find what the rule reaches and to keep wording consistent (the handoff said "decide by reading").
- `task-cycle/record_template.md` (grep and the parts on *Discarded attempt*, questions table, *Request URL and status*), `project-level/plan_state.py` and `project-level/test_blocked_request_line.py` (by grep): to see that the wording of the blocked record needs no change and that the invariant `blocked-request-wording` names only two files.
- `foundations/decisions.md`: WAY-256, WAY-265, WAY-33, WAY-134, WAY-263, WAY-297, WAY-364, WAY-392, WAY-268 (the *Rationale* and *Verification* of the entry on reserved choices) and the withdrawn list, for the form, placement and the stale WAY-328; `foundations/part_map.md` (the entry `task-cycle`); `foundations/invariants.md` (by grep for the changed decisions); `elements/decisions/template.md`, `elements/decisions/skill/*.md`, `elements/environment-facts/template.md`, `elements/environment-facts/skill/*.md` (as the foundation step names).
- `task-cycle/request_check.py` (head) and `task-cycle/test_request_check.py` (the `TemplateTest`): to settle that the form check needs no change.
- `elements/common/foundation_check.py` (by grep, for the rule that a changed decision with nothing holding it is an error): reason for the pairs of examples.
- The handoff names `guidelines/coding.md` and `guidelines/testing.md` for a change that reaches a script or a test; this change reaches none, so I did not read them.

## Unread material

- `foundations/glossary.md`: the handoff says to read it whole; I searched it (grep) for the words I use and did not read it whole. Words searched: "blocked draft", "reserved choice" (the latter has an entry; the former none).
- `elements/common/way_of_working.md` and `elements/common/rules.md`: the element templates name them; I did not read them, and wrote the entries by the templates and the skills of the elements and by the pattern of neighbouring entries; `foundation_check.py` passes.
- `foundations/environment_facts.md`: read from the top through `visible-scoring-reward-hacking`, `oracle-in-loop-building` and the tail (`ruff-default-rules` printed by accident, not read for content, the last entries and the withdrawn list); the rest not read.
- Decisions of the handoff read from the index only (binding sentences), not whole: WAY-13, WAY-69, WAY-73, WAY-82, WAY-85, WAY-136, WAY-161, WAY-162, WAY-232, WAY-233, WAY-263 (the whole entry was read afterwards), WAY-287, WAY-289, WAY-90 (its sentences, plus the template's *Based on* rules). Read whole: WAY-03, WAY-100, WAY-135, WAY-164, WAY-227, WAY-229, WAY-404, WAY-405.
- `task-cycle/change/walkthrough.md` and `task-cycle/change/ui_check.md`: not read; the change alters no behaviour a user sees and no screen.
- `agent-instructions/README.md`: read whole. `task-cycle/skill/SKILL.md`, `request_template.md`, `change/SKILL.md`, `review/SKILL.md` and `foundation_step.md`: read whole.

## Searches not found or unclear

- WAY-328, which the task cites, is not an entry: it is on the list of withdrawn numbers (successors WAY-379 and WAY-392).
- The task's line numbers (`~84`, `~263`, `~396`, `~500`) are those of an older commit; the passages were found by their words (as the handoff said).
- The handoff says the form check "reads the table of variants"; `task-cycle/request_check.py` reads no such table (see *Checks*).
- The register of problems of 2026-11-12 and the count of 83 cycles that the task cites: not found in the repository and not opened (private notes of the author); the figure in WAY-409's *Rejected* rests on the task's words alone.
- A rule of the-way that says where the author's question for the human belongs in the record's questions table, with a status for it: the record template has the table and no row for a question the cycle could not answer; I wrote none, since the existing rows ("every question, answer and choice") cover it, but the form of that row for "no source settles it" is unclear.

## Working copies

- `.runs/author/` of the worktree, holding the downloaded card (`card.pdf`, `card.txt`), the ImpossibleBench HTML and PDF with their extracted texts, a scratch directory of the base copies of five files for the check, the output of the gate and the check script: all removed. Kept in `.runs/task-cycles/agent-test-bypass/reports/`: `author-own-work-check.py` (the check) and `author-task-cycle-gate-tail.txt` (the tail of the gate's output). No worktree or clone was made; nothing remains.
