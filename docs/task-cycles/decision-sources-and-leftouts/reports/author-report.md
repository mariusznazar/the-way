# Author report — decision-sources-and-leftouts (the whole change as the one author)

**Status:** done with concerns

Concerns, each detailed below: (1) WAY-145 adopts a part of the same roadmap practice and has no
`derives from WAY-100`; it is on no list of the task, so it is untouched. (2) The leftovers of the
course decisions rest partly on the author's map of the course package and on the course's own skill
files read from a local archive outside both allowed places (a Reach). (3) WAY-100 is marked
`the cycle's` because its pair of examples was changed to agree with the new sentences.

## Files changed and commits

- `foundations/decisions.md` — 198 added, 88 removed lines (before the last two small edits made
  before the commit; the commit holds the final state).
- Commit `05b4648` — "Name the sources of adopted practices and what the decisions leave out of
  them", on `task/decision-sources-and-leftouts`, author address `mariusznn@gmail.com`. Not pushed.

Decisions changed (25): WAY-100, 121, 138, 142, 143, 144, 146, 147, 148, 164, 167, 199, 203, 206,
212, 228, 233, 236, 237, 256, 268, 270, 273, 280, 374. WAY-136 unchanged (evidence only, below).

## Checks run

| Command | Exit | Result |
|---|---|---|
| `python -B elements/common/foundation_check.py` (after the first round of edits) | 0 | `0 errors` |
| `python -B elements/common/foundation_check.py` (after the last edits, before the commit) | 0 | `0 errors` |
| `python -B .runs/author/scripts/compare_binding.py . aba5ee92…` (own-work check, below) | 0 | binding sentences changed only in WAY-100 |
| `python -B gate/run_tests.py elements/common` | 0 | `Ran 246 tests … OK` (run before the last two prose edits of WAY-100 — a line re-wrapped in its *Verification* and the word "today" removed from its *Rejected*; the foundation check after them exits 0) |

Not run: the full gate (`python -B gate/run_tests.py` with no directory) — the orchestrator's run,
as the handoff gives. No test cites WAY-100's wording: a search of the whole repository for
`WAY-100` finds it only in `foundations/decisions.md` and `elements/decisions/template.md:49`
(a pointer by number), and no line `decision:` names it. This change writes no code and no test, so
no test was written first.

## Own-work check

- **Requirement most likely missed:** acceptance criterion 1 — the binding sentences of no decision
  named in *Need* change. Many edits sit in long entries next to the binding paragraphs.
- **Check:** a script that splits the log at base `aba5ee92` and at the working tree by `### WAY-NN`,
  compares the text before `- **Scope:**` of each decision, and lists separately the decisions whose
  fields or prose changed.
- **Result:** binding changed: `['WAY-100']` (the positive control: the one decision meant to
  change shows up). Fields or prose changed: the 25 decisions above, every one of them on a list of
  the task. No decision added or removed. A search for `Based on:** TODO` in the log finds nothing
  now; a search for vault paths (a vault name, a drive-letter path, a note link) in the log finds nothing.

## Foundation entries (foundation step)

**WAY-100** — `the cycle's`; it carries rows 1 and 2 whole in its second binding paragraph, and is
the cycle's because the pair of examples in *Verification* was changed (the old `complies` quoted
"the article that describes the process", which the new sentence forbids).

- EN: A decision that adopts an outside practice names as its source the place the practice was in
  fact taken from, found by its trace and never a document that only describes it, and where a
  reader of the repository cannot open that source, it describes the source in *Rationale* and says
  it is not open to that reader.
- PL: Decyzja, która przejmuje praktykę z zewnątrz, podaje jako źródło miejsce, z którego praktykę
  naprawdę wzięto, znalezione po śladzie, a nie dokument, który ją tylko opisuje; a gdy czytelnik
  repozytorium tego źródła nie otworzy, opisuje je w *Rationale* i mówi, że nie jest dla niego
  otwarte.
- How the wording differs from what the rows strictly need: the old second paragraph had two
  sentences; it now has three — the first keeps "names the practice and what it takes … and puts
  what it leaves out in *Rejected*", the second carries rows 1 and 2 together with the old clause on
  *Based on* and *Rationale* (WAY-27), the third is the old sentence on lists unchanged. The row-1
  wording is general ("the place the practice was in fact taken from") rather than "the-way", since
  WAY-100 binds every product. "found by following the trace of that taking" renders "znalezione po
  śladzie"; it names no kind of trace (git, notes), which the row does not list either.
- *Rationale* added: why a found-afterwards public page is no source, and why a closed source is
  said to be closed — both from the rows' column "What the cycle would otherwise guess" and the
  reasons kept in *Questions to settle* 1 and 3.
- *Rejected* added: the four ways not chosen that the rows' sources keep (Q1: any public document
  describing the practice; origin plus a public description marked as such where no trace exists;
  Q3: the sentence only in the course decisions with no rule here; nothing written, the answer only
  in the task document), each with the cost the task keeps.
- The changed pair of examples, word for word:
  - complies: "a decision adopts only the risk assessment step of an outside process for task
    planning and gives its reason; an agent offers an unadopted technique as a proposal; the
    decision on that step names the step and what it takes from the process in its *Rationale*,
    quotes in *Based on* the article the step was in fact taken from, with its address, the passage
    and the date it was read, and puts the steps it does not take in *Rejected*; a decision that
    takes one practice from a course whose lessons a reader cannot open describes in its *Rationale*
    what the lesson showed and says that the lessons are not open to that reader; the rules taken
    from one outside source each stand in the decision that carries them, with no decision of its
    own for the list of what is taken;"
  - violates: "a skill makes an outside planning ritual mandatory because an agent recognizes it,
    without a decision adopting it; a decision adopts an outside practice and says nowhere what it
    takes from it; a decision answers the question "what do we take from this source" with a list
    of the rules taken, each of which a decision of its own would carry; a decision whose practice
    came from a course cites in *Based on* a public page found afterwards that describes the same
    practice; a decision that takes a practice from a lesson its reader cannot open describes the
    lesson and leaves the reader to guess whether its address was forgotten."
- Search of the foundation (WAY-33): `WAY-100` in every tracked file outside `.runs/`; the phrases
  "what was seen there", "adopts a method or practice", "practice from outside", "borrowed from",
  "cannot open". Findings: `elements/decisions/template.md:49` points to WAY-100 by number (no
  change needed); `elements/decisions/template.md:57-62` and `elements/environment-facts/template.md:56`
  speak of a measurement a reader cannot open (WAY-90's rule, consistent, no change); the decisions
  that derive from WAY-100 are the ones this change edits or ones whose Rationale already names the
  practice; WAY-145 is a finding (concern 1). No collision with WAY-27, WAY-71 or WAY-90.

The other 24 changes are edits of *Based on*, *Rationale*, *Rejected* and, in WAY-148, *Relations*;
they write no new meaning of a binding sentence, so they carry no row mark. Each is described in the
table below for the request's description.

## The decisions, one by one (for the request's description, To do 9)

"The map of the course" below is the author's private note that maps each lesson of the 10xDevs
course, element by element, to a verdict (take / reject / open) and to the WAY decision that carries
it (a private note). "The lesson note" is the author's private copy of a lesson's text.

| Decision | Where I searched | What I found, and where in the source | *Based on* | *Rationale* | *Rejected* (added) | *Relations* |
|---|---|---|---|---|---|---|
| WAY-138 | `git log -S "devil's advocate"` → `53b3827` (task "m1l5-adoptions", row 2); the map of the course, lesson m1l5, row "Testy przeciw efektowi potwierdzenia"; the lesson note m1l5, section "Anti-Confirmation Bias prompting" | The three tests come from lesson m1l5 ("Od localhost po produkcję – Deployment z Agentem"), section "Anti-Confirmation Bias prompting", built into the course skill of platform research; each test ends in accept / record as known limitation / change the choice; the lesson adds two more techniques (comparison of three alternatives, change of roles) | TODO → `none` (course not open) | names the lesson, what it shows, that the lessons are not open | known limitation recorded in a document of the infrastructure; comparison of three alternatives; change of roles | unchanged |
| WAY-142 | `git log -S "practice of a roadmap"` → `e8629d5` (assessment of the breakdown, remark 5), `97b7212`, `4e6b53c`; vault search "vertical slice" → the map of the course, lesson m2l1 (row "`10x-roadmap` jako całość" → WAY-142, and rows 2–20); the lesson note m2l1; the course skill `10x-roadmap` (Reach) | Source: lesson m2l1 "Roadmapa MVP: milestony, zależności i priorytety" and its skill `10x-roadmap` (milestone, readiness score 0–4, code audit by parallel agents, three-question interview, F-NN/S-NN, fields, Parked, Backlog Handoff, self-review) | TODO → `none` | names the lesson and the skill, what it does, that the lessons are not open | readiness check of the documents; stock of the code by parallel agents; fields that feed acceptance criteria and the "why here" sentence; list of parked items; blocked state of an item; existing "three copies" position marked as the practice's | unchanged |
| WAY-143 | as WAY-142; the map's row "Pionowe plasterki…" → WAY-143; the lesson's sections "Vertical-first", "Co z fundamentami?" | Vertical slices and foundations that must name the slice they unlock (`Unlocks: S-NN`) | TODO → `none` | names the skill of lesson m2l1 (WAY-142), not open | existing positions marked as the practice's: the field of what a foundation unlocks; the word slice for an item | unchanged |
| WAY-144 | as WAY-142; the map's row "Graf zależności…" → WAY-144; skill §6c–6d (Parallel with, order, north star) | Graph of prerequisites, `Parallel with`, order tilted by the interview's goal, north star as early as dependencies allow | TODO → `none` | names the skill (WAY-142), not open | existing "order tilted by a goal" marked as the practice's; the slice that proves the product placed early | unchanged |
| WAY-146 | as WAY-142; the map's row "Samokontrola przed zapisem" → WAY-146; skill Step 8 (15 self-review checks) | Self-review by the same agent; form checks (sections, table parity); "No invented slices"; "Slice granularity balance" | TODO → `none` | names the skill (WAY-142), not open | existing positions marked (self-review by the author; form checks across copies); no slice beyond the source; comparable size of slices | unchanged |
| WAY-147 | as WAY-142; the map's row "Stały identyfikator zmiany (Change ID)…" → WAY-147; skill §6 and "Relationship to other skills" | Stable kebab-case Change ID; Backlog Handoff table; statuses flipped by later skills by Change ID | TODO → `none` | names the skill (WAY-142), not open | existing "table for a tracker" marked as the practice's; states moved by later steps by the name | unchanged |
| WAY-164 | `git log -S "most likely does not meet"` → `0761d6d`, `1554c6d`; the frozen task in history `git show 1554c6d:docs/task-cycles/review-loop-end/task.md` (*Context*: "Limen, `templates/worker.md:25`" at `e746877`); the author's research note on Limen and Open Mercato | Source: Limen, public repository, `templates/worker.md` line 25 at `e746877` (resolved to the full SHA with `gh api`), fetched and read 2026-11-16 | TODO → the Limen citation (address, line 25, passage word for word, read 2026-11-16) | names Limen and states the whole of that line's practice is taken | none — the decision takes the whole of the practice it names (the one sentence of line 25); the rest of the worker template are other practices | unchanged |
| WAY-268 | the map, lesson m2l4, row 3 → WAY-268; the lesson note m2l4, sections "External research dla agentów", "Agentic search", "Exa.ai…", "Context7…" (read by search and passages, see Unread) | Grounding; the lesson reaches the source by a search engine for agents (Exa, by MCP) and puts current library docs into context (Context7) | unchanged (`none`) | + lessons not open | search engine for agents through a tool server; library documentation put into context before the plan | unchanged |
| WAY-270 | the map, lesson m3l5, rows 4, 7, 8 → WAY-165, 270, 139; rows 6, 22; the lesson note m3l5, sections "Sentry MCP", "Krok 3", "Zadania praktyczne" 2 | Two questions taken; the lesson sets up Sentry through its path `/10x-new → /10x-plan → /10x-implement` and reads failures through Sentry MCP | unchanged | + lessons not open | a failure tool set up ahead of the choice; an agent reaching failures through the tool's server | unchanged |
| WAY-273 | the map, lesson m3l5, rows 10, 11; the lesson note m3l5, sections "Fix", "Połknięte błędy…", practical task 1 | Rule "stop swallowing first"; the class of swallowed errors searched by an audit of one critical flow | unchanged | + lessons not open | search for hidden failures as a class by an audit of one critical flow | unchanged |
| WAY-374 | the map, lesson m2l2, row "Sondowanie terminów…"; the course skill `10x-plan-review` (Reach), "Blind Spots" and the note on ranking terms | Probe of undefined terms (`10x-plan` step 1.1.4) and its repeat in the plan review's Blind Spots | unchanged | + lessons not open | the same probe repeated by a review of the finished plan | unchanged |
| WAY-136 | commit `8ccbd6e`; the author's plan of the slimming work, item P30; the author's research note on Limen and Open Mercato, point "OM: bramki zależne od ryzyka" and the section on per-step review; the cited `step-review.md` (fetched) | **Evidence only.** In the same item P30 the author writes of WAY-148 and WAY-229 "Praktyka przejęta z Open Mercato" (practice taken from Open Mercato), but of the review of risky slices only "praktyka zgodna z Open Mercato" (practice consistent with Open Mercato), with Mariusz's choice dated 2026-10-23 against the recommendation; the research note calls Open Mercato's risk gates "częściowo zbieżne" (partly convergent) with "dwa pytania, które zostają" — the trust-boundary and irreversible-operation questions that the-way had before reading Open Mercato (row 5 of the slimming work). The criterion is the-way's own; the Open Mercato sentence on cost is cited as support | unchanged | unchanged | unchanged | unchanged |
| WAY-148 | the same item P30; `8ccbd6e`; the cited `executor-dispatch.md` at `e320bd5` fetched and read whole | **Adopts.** P30: "WAY-148 przepisany … Praktyka przejęta z Open Mercato (`om-auto-create-pr-loop`, `references/executor-dispatch.md`: „Full description: {paste…}”) — źródło w *Based on* WAY-148". The prompt pastes the step's bullets and names the plan's path among the step's anchors; its return format is a concise report under 300 words in the message | unchanged | names Open Mercato's executor prompt and what is taken (the section word for word with the plan's file as its address) | the executor's concise report under 300 words in its message | + `derives from WAY-100` |
| WAY-167 | the cited `AGENTS.md` at `4374c48` fetched (Task Router, lines 59–75); the frozen task of the coding-guidelines cycle in history (`git show 3b36c02:docs/task-cycles/coding-guidelines/task-frozen.md`, question 8a); the author's research note on Open Mercato, §1.1 | Task Router table with "→ Section" rows naming a heading inside a guide; guides kept per package (`packages/<pkg>/AGENTS.md`) | unchanged | unchanged | existing "a file … for each part of the map" marked as Open Mercato's per-package guides; a row naming a section inside a guide | unchanged |
| WAY-212 | as WAY-167 | The router stands in the root `AGENTS.md`; "Only use Explore agents for topics no AGENTS.md covers" | unchanged | unchanged | the table standing in the root instruction file (reason taken from the entry's own Rejected); an agent sent to explore for a topic no guide covers | unchanged |
| WAY-199 | the cited `README.md` of the example module fetched; frozen task of the coding-guidelines cycle (context line 105, questions 2, 6, 15, row 17); research note on Open Mercato §2.2; `packages/core/src/modules/customers/AGENTS.md` at `4374c48` fetched | Open Mercato has two statuses, `readable` and `qa-only`, on files of a reference module that does not run; the-way's third status `exemplar` comes from Open Mercato's `customers` module declared "the template for new CRUD modules" (line 7), which the coding-guidelines task document names | + citation of `customers/AGENTS.md` line 7, read 2026-11-16 | + `readable`/`qa-only` become `copy`/`do not copy`; the third status marks the file a decision designates (WAY-198), as Open Mercato declares a template module | statuses on a reference module the product does not run | unchanged |
| WAY-203 | the cited Google paper fetched (PDF, text extracted), "Criteria for compiler checks" and "Criteria for code-review checks" | Compiler-check criteria: easily understood; actionable and easy to fix with a suggested fix; no effective false positives; correctness only. Code review: up to 10% | unchanged | unchanged | the 10% limit and "correctness only" now marked as ways from Google's practice, left out; + easily understood; + easy to act on and fix with a suggested fix | unchanged |
| WAY-206 | the cited `.github/workflows/audit.yml` at `4374c48` fetched and read | Scheduled daily audit over the unchanged graph with a tracking issue; `--severity high`; an allowlist of accepted advisories | unchanged | unchanged | existing "fixed threshold" and "daily run" marked as Open Mercato's; + list of accepted advisories | unchanged |
| WAY-228 | the cited ICSE 2024 paper fetched, §4.3 read whole | Four kinds: classical, round-trip, catastrophic failure, differential | unchanged | unchanged | classical properties; catastrophic failure properties | unchanged |
| WAY-233 | the cited Open Mercato `review-checklist.md` at `e320bd5` fetched, section 4 | The item on weakened assertions is graded `(major)` | unchanged | unchanged | the grade `major` | unchanged |
| WAY-236 | the cited Anthropic page fetched live (not the archive), "Step 5: Design graders thoughtfully" read whole | Also: grade the outcome not the path; partial credit; a way out "Unknown"; a rubric with each dimension graded by an isolated judge | unchanged | unchanged | partial credit; "Unknown" way out; rubric per dimension with its own judge. "Grade the outcome, not the path" not added: WAY-234 carries that rule, not this decision | unchanged |
| WAY-121, 237, 256, 280 | the entries; the map of the course for 237 (m3l1 row 7) and 280 (m3l5 row 15) | — | unchanged | + one sentence: the lesson (121) / lessons of the course are not open to a reader of this repository | unchanged | unchanged |

Reasons in *Rejected*: added only where the entry already gives one (WAY-212 reuses its own reason
"`AGENTS.md`, loaded into every session, grows with each kind"); existing positions marked as the
practice's keep their reasons. Sources and the author's notes give reasons I did not copy:
- The map of the course gives the author's reason for every rejected roadmap element (e.g. the
  readiness score — the-way's readiness gate is stricter; Parked — a copy of "Out of scope"; the
  Backlog Handoff table — a second copy; the Risk field — order lives in the dependencies) and for
  the m2l4 and m3l5 leftovers (Exa — a choice of a provider, not a step; Context7 — docs fetched
  when needed; Sentry set up ahead — the tool is chosen by the step with "no tool"). I left these
  out because they come from the trace, not from the source or the entry; a reviewer may judge
  they should go in.
- Open Mercato's `audit.yml` gives its reason for the daily run (advisories are published against
  dependencies that never change); not copied, since the position already has the entry's reason.

## Choices

- *Based on* `none` for a course source a reader cannot open (WAY-138, 142–147), following WAY-121,
  268, 270, 273, 280 and 374, with the source described in *Rationale*. Rejected: keeping
  `TODO — …` — the source is found, so nothing is missing; cost if wrong: a reviewer wants a TODO
  back in seven entries.
- WAY-142 carries the full description of the roadmap practice; 143, 144, 146, 147 point to it by
  `(WAY-142)`. Rejected: the description repeated in five entries — five copies drift.
- WAY-164's *Rejected* gets nothing: the decision takes the whole sentence it names. Rejected:
  listing the other rules of Limen's worker template — they are other practices, and WAY-100 asks
  for what is left out of *the* practice.
- The "classical properties" leftover of WAY-228 states what the rule does not take; it does not
  say such tests are barred, since the binding sentence's list of sources of an expected value is
  what decides that.
- WAY-268's leftovers: only the two tools by which the lesson reaches the source; the other rows of
  m2l4 (research subagents, research document, framing) are other practices of the lesson, not of
  grounding.
- WAY-142 leftovers exclude the lesson's practices beside the roadmap (external backlog, backlog
  access limits, agent keeping a backlog, rhythm of three slices) and two rules of conduct of the
  skill (defining a term on first use, one recommended next move), which are no part of the
  roadmap practice.

## Reach beyond the handoff

- The course skills `10x-roadmap` (`SKILL.md`, read by search of headings and passages: Step 6,
  field rules, Step 8 self-review) and `10x-plan-review` (passages on "Blind Spots"), read from the
  local archive of the course trials (`git show` of the tags `archive/10x-m2l1` and
  `archive/10x-m2l2` in a local repository of the author outside this repository and outside the
  vault). Why: the lesson note alone does not list the self-review checks of WAY-146 or the Blind
  Spots of WAY-374; I would otherwise have written them from the map's summary. Reading only.
- The author's plan of the slimming work (the note of the plan, item P30) and the note on the-way's
  own skills replacing Superpowers, found by searching the vault for `om-auto-create-pr-loop` — the
  trace that settled WAY-136 and WAY-148.
- The author's research note on Open Mercato's coding standards (the note of the research) and
  the coding-guidelines cycle record in history (`3b36c02`) — for WAY-199's third status.
- `gh api repos/overment/limen/commits/e746877` — to turn the short commit of the review-loop task
  into the full SHA of the citation (a read of public metadata).

## Working copies

Directory `.runs/author/` of the worktree: downloaded sources (`sources/`: Limen `worker.md`, five
Open Mercato files, the Google PDF and its text, the ICSE paper and its text, the Anthropic page and
its text, the copy of `10x-roadmap/SKILL.md`), two scripts (`scripts/mapa_rows.py`,
`scripts/compare_binding.py`), their outputs, the commit message file and the outputs of the
foundation check. The whole directory `.runs/author/` was removed with `rm -rf` before returning
(exit 0; `.runs/` now holds only `task-cycles/`). No worktree or clone was made. Nothing kept in
`reports/` beyond this report.

## Unread material

- `foundations/decisions.md`: each decision of *Decisions in play* read whole by its heading;
  WAY-145, WAY-198 read whole as reaches; the log was not read whole.
- The lesson notes m2l4 (`09-research-i-implementacja…`) and m3l5 (`16-debugowanie-z-ai…`): read by
  headings and by search for the passages the leftovers rest on, not whole. The lesson note m1l5:
  section "Anti-Confirmation Bias prompting" read whole, the rest not. The lesson note m2l1 read
  whole.
- The map of the course: read whole for lessons m1l5 (rows with WAY numbers) and m2l1; for m2l2,
  m2l4, m3l1 and m3l5 through a script that printed each row's element, source, verdict and carrier
  (the long status line of each lesson was not read).
- The skill `10x-roadmap` (775 lines): read by headings and passages, not whole.
- The author's research note on Limen and Open Mercato: read whole up to its line 200 (the end of
  the report sections); the note on the-way's own skills: lines 1–12, 84, 125–163.
- The data file of the foundation review (P7), named by the handoff: not opened — the task's
  *Context* quotes what it says of WAY-136, and the trace in P30 settled the question.
- `guidelines/coding.md`, `guidelines/testing.md`: not read — no code and no test changed, as the
  handoff allows.

## Searches not found or unclear

- WAY-145 (who places an open question after the readiness gate): the map of the course carries
  its row "Blokery zewnętrzne…" ("przejmuję w zmienionej postaci", take in changed form) to WAY-145,
  yet WAY-145 has *Based on* `none`, no `derives from WAY-100` and no sentence naming the practice.
  It stands on no list of the task, so I changed nothing; it looks like the same gap as WAY-136 had.
  Recommendation: a task of its own, or the orchestrator's call whether this cycle should take it.
- Whether the course skill `10x-roadmap` is open to a reader: it comes in the course's package for
  the lesson (fetched with the course's CLI); I treated it as course material that a reader cannot
  open, as the task's answer to question 3 treats the lessons. Not verified against the CLI's terms.
- WAY-121's lesson "Towards Autonomous Product Development": the author's note on it records a
  public-looking address on mega.dev; I followed the task (question 3: the lessons are not public)
  and did not check the page.
- WAY-164: the commit `e746877` the review-loop task names is a short hash; `gh api` resolved it to
  `e746877e8ef195ab9a34a070bdd3b000d0b6cf10` (2026-10-17). The line number 25 holds at that commit.
- WAY-236: the archived copy named in *Based on* was not fetched; the live page was, and its
  passages match the two quoted ones word for word.
- No decision of either list was left without a found source: no `TODO` stays.

## Questions

none
