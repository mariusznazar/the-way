FAIL 05b46486103be3db6ead33ffff5b53e3c9988331

# Review of the whole change — decision-sources-and-leftouts

- Variant: the whole change of a one-author change (no plan, no slices; WAY-136). Range
  `aba5ee92a0734c2e775cc69662af669bf6455795..05b46486103be3db6ead33ffff5b53e3c9988331`, one commit
  (`05b4648`), one file: `foundations/decisions.md`, 199 added and 88 removed lines.
- `git rev-parse HEAD` in the worktree is `05b46486103be3db6ead33ffff5b53e3c9988331`, the head
  given.
- Blocking findings: 1 (Important). Minor: 2. Out of scope: 1.

## Findings

### Important

**I1 — WAY-142 now names its source, and its *Rejected* still says that source has estimates. The
source says it has none.** Within the task (*To do* 3; *Need*: a reader cannot tell what was taken
from the practice and where its edge lies). Comes from the one author's change, commit `05b4648`
(no slices).

- Place: `foundations/decisions.md:4843-4845`, WAY-142 *Rejected*: "the milestones, the estimates
  and the interview on the order of work of the practice of a roadmap of vertical slices — left out
  of what the step takes from it". The diff changes the line that closes this item (diff hunk
  `@@ -4793,7 +4842,14 @@`, the `-left out of what the step takes from it.` line), and the same
  change adds to the entry's *Rationale* (`:4826-4833`) that "the practice is that of lesson m2l1 of
  the 10xDevs course … and of the skill of a roadmap the lesson brings".
- What is wrong: the practice the change names makes no estimates on purpose. The course skill
  `10x-roadmap` (read from the local archive tag `archive/10x-m2l1`, `.claude/skills/10x-roadmap/SKILL.md`
  line 43): "It NEVER assigns time estimates, t-shirt sizes, points, or human-calendar dates —
  agentic execution is non-linear and time-budgeted estimates would lie." The lesson note of m2l1,
  section "Czego skill świadomie nie robi": the skill does not estimate the time of the work. The
  author's map of the course, lesson m2l1, row "Bez estymat czasu…" (source: lesson section
  "Czego skill świadomie nie robi"; skill, rule 5): **odrzucam** — "nic do przejęcia" (nothing to
  take). So the entry lists, as an element of the named practice that the-way leaves out, an
  element that the practice rejects itself.
- Why it matters: this is the error the task exists to remove. The task's *Need* says a reader has
  to be able to check what was taken from a practice and where the practice stops. A made-up element
  looks the same as a real one. The new WAY-100 *Rationale* also warns that "what is left out would
  be weighed against a text nobody read". Now that the source is named, a reader who trusts the
  entry believes that the course estimates time and that the-way declined that. Someone who checks
  the course finds the opposite, and the entry loses the trust the change was meant to give it. The
  author compared this entry's other *Rejected* items with the source and marked them, for example
  "as the practice of a roadmap holds each of its items" (`:4836-4837`). This item was left as it
  stood.
- Evidence: the three passages above; the course map's m2l1 rows read by script; the skill line 43.
- Fix: drop "the estimates" from the item, so it reads "the milestones and the interview on the
  order of work of the practice … — left out of what the step takes from it". The item's other two
  elements are in the practice: milestones (skill §"Milestone layer", map row "Milestone…") and the
  interview (skill Step 5).

### Minor

**M1 — WAY-143 *Rationale* makes the practice's rule on foundations narrower than the skill states
it.** Within the task (*To do* 3, fidelity of the description of a closed source, WAY-27).

- Place: `foundations/decisions.md:4882-4885`: "The practice is that of the skill of a roadmap of
  lesson m2l1 of the 10xDevs course (WAY-142), whose preparatory work, named foundations, stands
  only with the slice it unlocks".
- What is wrong: the skill lets a foundation stand on any of three things: a slice it unlocks, a
  named blocking unknown it reduces, or a named verification path it enables. Skill line 344:
  "unless you can name the downstream `S-NN` item it unlocks, the blocking unknown it reduces, or
  the verification path it enables". Step 8, check 10, line 615: "`Unlocks` populated with at least
  one downstream `S-NN`, a named blocking unknown, or a named verification path". The lesson note
  (its line 444) gives only the slice, which is where the entry's wording comes from. WAY-143's
  binding sentence admits a preparatory task "only where a task of the plan depends on it". So the
  practice's foundation that stands on an unknown or a verification path is an element the-way
  leaves out, and the entry describes it as absent from the practice.
- Why Minor: the error is in a description, and no binding sentence or check rests on it. A reader
  learns less about the practice than the skill holds but is not led into a wrong action.
- Fix (either): say "stands only with what it unlocks, in the lesson a slice"; or add to *Rejected*
  "a foundation that stands on a blocking unknown it reduces or a verification path it enables, as
  the practice's skill allows — left out of what the rule takes from it".

**M2 — The trace holds reasons for several of the new *Rejected* items, and the entries carry none
of them.** Within the task. The task allowed leaving them out (*To do* 3: "powód stoi przy pozycji
tylko tam, gdzie podaje go wpis albo źródło"), so this is an observation the author asked a reviewer
to judge (author report, "Reasons in *Rejected*"), not a defect.

- Place: the new reason-less items in WAY-138 (`:4073-4078`), WAY-142 (`:4845-4852`), WAY-268
  (`:4211-4214`), WAY-270 (`:4361-4364`).
- What the trace holds: the course map gives the-way's reason for each item. Three-alternatives
  table: "krok technologii już robi (porównanie opcji, *Rejected*)" (the step already compares the
  options). Readiness score 0–4: "the way ma ostrzejszą bramkę przed rozbiciem (…WAY-118…)" (the-way
  has a stricter gate before the breakdown). Parked: "*Parked* w A to kopia „Out of scope”" (a copy
  of Out of scope). Exa: "wybór dostawcy wyszukiwania, nie krok procesu" (a choice of search
  provider, not a step of the process). Context7: documentation fetched when it is needed. Sentry
  set up ahead: the tool is chosen by the observability question, with "no tool" among the options.
- Why it matters: WAY-27 asks every entry to carry its whole reasoning. Without these reasons, an
  agent that proposes, for example, the readiness score finds it rejected with no reason (the
  template has *Rejected* read by "the agent proposing an option already weighed"), and it has to
  work the reason out again. The reason for the three-alternatives item also stops a reader from
  taking "left out" to mean that the step compares no alternatives. My view: the map is the record
  where each of these choices was made, so it is a source in the sense of the answer to question 1
  ("notatka/research w vaulcie"). Carrying these reasons is better, but the frozen task does not
  require it.

### Outside the task's scope

**O1 — WAY-145, and also WAY-139 and WAY-165, take parts of a course practice and say nothing about
it.** Outside the task: none of the three stands on a list of the task, and the change does not
break them.

- WAY-145 (`foundations/decisions.md:3721`): the course map, lesson m2l1, row "Blokery
  zewnętrzne…", carries **przejmuję w zmienionej postaci** (take in changed form) → WAY-145. The
  entry has *Based on* `none`, no `derives from WAY-100` and no sentence naming the practice. I agree
  with the author's report.
- The new WAY-100 sentence makes the same gap visible in two more entries. In the map, lesson m3l5,
  rows 4, 7 and 8 have the carrier "WAY-165, WAY-270, WAY-139". WAY-270's own *Rationale* says the
  two adopted questions "bind by this decision, by WAY-165 and by WAY-139, and nowhere else". My
  search of the log for decisions that name a course or lesson found that WAY-139 and WAY-165
  mention neither the course nor WAY-100. If they take a part of the course practice, they now lack
  the closed-source sentence that WAY-100 requires. A task of its own, as the author recommends,
  should cover WAY-145, WAY-139 and WAY-165 together.

## Declined to judge

- The decisions that cite a public source without a relation to WAY-100 and outside the lists
  (WAY-89, 205, 234, 235, 238, 239, 241). The task's question 4 left them out on purpose (*Not
  chosen*).
- WAY-300 ("as an outside harness runs its quality review") and WAY-113 (a course "whose recording …
  a reader of this repository cannot open"). Both are on no list of the task. WAY-113 already says
  its source is closed.
- Whether the lesson "Towards Autonomous Product Development" of WAY-121 is public. The human's
  answer to question 3 settles that the lessons of WAY-121, 237, 256, 268, 270, 273, 280 and 374 are
  not public. The author records that a private note gives a public-looking address; I did not open
  it.

## How the task is covered

| Item | Verdict | Evidence |
|---|---|---|
| *To do* 1–2, seven `TODO` decisions | met. No `TODO` is left in *Based on* (search of `Based on:** TODO` finds none). WAY-138 and WAY-142–147 have `none`, and their *Rationale* describes the lesson and says it is not open, following the existing course decisions (WAY-121, 268, 270, 273, 280, 374). WAY-164 cites Limen. | WAY-138 trace: commit `53b3827`, "Foundation step of the task m1l5-adoptions". Roadmap trace: `e8629d5` and the map, m2l1, carrier column. WAY-164 trace: `git show 1554c6d:docs/task-cycles/review-loop-end/task.md`, *Context*, which quotes `templates/worker.md:25` at `e746877`. The HBR article in the quality-patterns research is a candidate the trace does not reach, and it is rightly not cited. |
| WAY-164 citation | word for word | `templates/worker.md` at `e746877e8ef195ab9a34a070bdd3b000d0b6cf10`: line 25 is the bullet "The discriminating check first, …" and holds the quoted sentence exactly. Read 2026-11-16, commit dated 2026-11-16. |
| *To do* 3, seventeen decisions | met, save I1 and M1 | Each new item was checked against its source. WAY-138: the m1l5 lesson note, § Anti-Confirmation Bias, holds the infrastructure.md "known limitation", the three-alternatives table and the change of roles. WAY-142/143/144/146/147: skill Steps 3, 4, 6c–6g, 7, 8 (checks 8 and 12), lines 58–59; map m2l1. WAY-268: map m2l4, rows 4–5. WAY-270: map m3l5, rows 6 and 22. WAY-273: map m3l5, row 11. WAY-374: `10x-plan-review` line 89, "a term it uses but never decides at the tie". WAY-167/212: root `AGENTS.md` lines 61, 63 (Task Router, "Only use Explore agents…", "`→ Section` names the heading"); per-package guides. WAY-199: example `README.md` lines 1–3 ("This module does not run."). WAY-203: Google paper, "Criteria for compiler checks" ("easily understood; actionable and easy to fix (whenever possible … a suggested fix …); produce no effective false positives; … correctness rather than style"), code review "up to 10%". WAY-206: `audit.yml` lines 11, 41–43 (daily schedule), 113 (`--severity high`), 161 (`scripts/audit-ci-allowlist.json`). WAY-228: ICSE paper §4.3 (classical: commutativity, repeated sorting; catastrophic failure). WAY-233: checklist "(major)". WAY-236: Anthropic page, Step 5 (partial credit; "Unknown"; isolated judge per dimension). No reason was invented: every new reason comes from the entry (WAY-212 reuses its own). |
| *To do* 4, WAY-136 | evidence only, which I agree with | P30 of the author's slimming plan uses two different words. It calls the executor prompt "Praktyka przejęta z Open Mercato" (taken), and it calls the review of risky slices only "praktyka zgodna z Open Mercato" (consistent with). Open Mercato's `step-review.md` sets the mode for the whole run (`final` / `checkpoint` / `per-step`, lines 9–11). The-way gives a review per slice, by a mark of trust boundary or irreversible operation. The research note on Limen and Open Mercato calls those two questions the-way's own ("dwa pytania, które zostają"), with Open Mercato "częściowo zbieżne". I read the P7 item of the foundation review, which the author left unread. It asserts that the binding sentence takes exactly this practice and gives no trace, so it does not outweigh P30. |
| *To do* 4, WAY-148 | adopts, which I agree with | P30: "Praktyka przejęta z Open Mercato (… `executor-dispatch.md` …) — źródło w *Based on* WAY-148". `executor-dispatch.md` line 37 ("Full description: {paste…}"), line 40 ("PLAN.md: {plan path}" under "Spec anchors"), line 54 ("concise report, < 300 words"). `derives from WAY-100` added; *Rationale* and *Rejected* agree with the source. |
| *To do* 5, WAY-199 | met | `customers/AGENTS.md` at `4374c48`, line 7, word for word apart from the list marker "1."; read 2026-11-16. Trace: the research note on Open Mercato §2.2 quotes the same line; frozen task of the coding-guidelines cycle (`3b36c02`), *Context* and question 16 (B). |
| *To do* 6, WAY-203 | met | `:8818-8829` |
| *To do* 7, eight lesson decisions | met: one clause or sentence each, no address | WAY-121 `:3838-3839`, 237 `:9451-9452`, 256 `:3430`, 268 `:4189-4190`, 270 `:4341-4342`, 273 `:4643-4644`, 280 `:4599-4600`, 374 `:5536` |
| *To do* 8, WAY-100; rows 1 and 2 | met | Second paragraph: three sentences, within the limit (WAY-05). Row 1 ↔ "Its source is the place the practice was in fact taken from, found by following the trace of that taking, never a document that only describes the practice". Row 2 ↔ "says that the source is not open to that reader". *Rejected* adds exactly the four ways not chosen that questions 1 and 3 keep, with their costs (WAY-134). *Rationale* and the pair of examples agree. Edited in place (WAY-07). Search of the foundation (WAY-33): `elements/decisions/template.md:49` points by number. `elements/common/rules.md:19-21` and `template.md:64-66` (`none` / `TODO`) agree with `none` plus a *Rationale* description for a closed source. No test cites WAY-100. |
| Acceptance criterion 1 | met | My own script compares the text before `- **Scope:**` of all 223 entries at base and head. Binding changed: `['WAY-100']` only (positive control). Entries changed: 25, every one of them named by the task. None added or removed. |
| Acceptance criterion 2 | met | Both added citations were re-fetched in this review and match. The dates read are 2026-11-16, the commit's date. |
| Privacy and form | met | Added lines hold no vault path, absolute path or `[[` link. Lesson codes (`m1l5`, `m2l1`) follow the existing use in WAY-268, 270, 273. |

## Checks run

| Command or method | Exit | Result |
|---|---|---|
| `git rev-parse HEAD` | 0 | `05b46486…` |
| `git diff aba5ee9 05b4648`, `git log aba5ee9..05b4648` | 0 | one commit, one file |
| `python -B elements/common/decision_index.py --output … --sections .` | 0 | 29 sections |
| `python -B elements/common/decision_index.py --output … --section "The foundation and its entries" --section "Decision entries and the decision log" --section "Environment facts" --part decisions --decision WAY-… (36 numbers) .` | 0 | 54 listed in full, 40 by heading. The first try used bare numbers and stopped with exit 2: "no decision 100". |
| `python -B <working dir>/scripts/compare_entries.py . aba5ee9 05b4648 <out>` (own script) | 0 | binding changed only in WAY-100; 25 entries changed |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `python -B task-cycle/change_file_sizes.py aba5ee9 05b4648` | 0 | `foundations/decisions.md` 10559 → 10670 (+111) |
| `python -B gate/run_tests.py elements/common` | 0 | `Ran 246 tests … OK` |
| `python -B gate/run_tests.py elements/decisions` | 1 | "no test found in elements/decisions": the directory holds no test, so this says nothing against the change |
| `curl` of the public sources | 0 each | Limen `templates/worker.md`; Open Mercato `customers/AGENTS.md`, example `README.md`, root `AGENTS.md`, `audit.yml`, `executor-dispatch.md`, `step-review.md`; Google paper (PDF, `pdftotext`); ICSE paper (PDF, `pdftotext`); Anthropic evals page (live) |
| manual: search of the added lines for a vault name, a note link, a drive-letter path, `Users`, `TODO` | — | none |
| manual: search of the log for decisions that name a course, lesson or harness, with or without the closed-source sentence | — | gives O1 |

Not run: the full gate, which is the orchestrator's. The size invariant of `guidelines/coding.md`
was not run either. The change touches no code, so the rule of the size of a function and a file
does not reach it, and a structure finding has no place here.

## Reaches beyond the dispatch

- The author's course map (the note of the map), read by a script that printed rows of lessons
  m1l5, m2l1, m2l2, m2l4, m3l1 and m3l5, and in full for the rows behind I1, M1 and M2. Why: these
  rows are the trace of every course leftover.
- The lesson notes of m1l5 (§ "Anti-Confirmation Bias prompting", whole) and m2l1 (§ "Czego skill
  świadomie nie robi"; § "Co zrobić, jeśli twój projekt naprawdę potrzebuje horizontal-first"). Why:
  I1 and M1, and the WAY-138 leftovers.
- The course skills `10x-roadmap` and `10x-plan-review`, read with `git show` of the tags
  `archive/10x-m2l1` and `archive/10x-m2l2` in the author's local course-trial repository
  (the author's repository of course trials, the same archive the author used). Read only. Why: I1, M1, the WAY-146 and WAY-374
  leftovers.
- The author's slimming plan (the note of the plan, row P30), the foundation review data file
  (the data file of the review, item P7 whole), the research note on Limen and Open Mercato
  (the note of the research on Limen, by search) and the research note on Open Mercato (the note of the research,
  §2.2). Why: the WAY-136 and WAY-148 judgments, and the third status of WAY-199.
- Git history: `1554c6d` (frozen task of review-loop-end), `3b36c02` (frozen task of
  coding-guidelines), `53b3827` and `e8629d5` (commit messages). Why: the traces.
- Decisions outside my index, read whole: WAY-198, 267, 284. WAY-234 read up to its *Rejected*. Why:
  WAY-199's third status, the context of WAY-138 and WAY-280, and the author's claim that WAY-234
  carries "grade the outcome, not the path". WAY-234 carries it from the Abseil book, so leaving it
  out of WAY-236's *Rejected* is right.

## Working copies

- `.runs/review-whole/` of the worktree held the saved diff, the indexes, the downloaded sources,
  two scripts (`map_rows.py`, `compare_entries.py`), the extracted map rows and the test outputs. It
  was removed with `rm -rf` (exit 0), and `.runs/` now holds only `task-cycles/`. No worktree or
  clone was made. Nothing was kept in `reports/` beyond this report.

## Unread material

- I read 26 of the 94 decisions of the index of my selection whole: WAY-27, 100, 121, 136, 138,
  142, 143, 144, 146, 147, 148, 164, 167, 199, 203, 206, 212, 228, 233, 236, 237, 268, 270, 273, 280
  and 374.
- WAY-256 (changed by the task): read from its heading through *Rationale* to its line 3440. The rest
  of its *Rationale* and its *Rejected* were not read. The change touches only `:3429-3431`.
- WAY-71, 90, 19, 07, 30, 33, 134, 314 and 145: their binding sentences were read in the index, not
  the whole entries. They bear on the change through those sentences alone.
- `elements/decisions/template.md`: lines 29–116 and 286–295 were read, not the whole file.
  `elements/common/rules.md`: lines 15–25 only.
- Guideline files: none selected, since no code and no test changed.
- The lesson notes of m2l4 and m3l5 were not opened. I relied on the map's rows, whose element and
  source cells quote the lesson sections.
- `10x-roadmap/SKILL.md` (775 lines): read by search and Step 8 whole. `10x-plan-review/SKILL.md`:
  read by search.

## Searches not found or unclear

- `elements/decisions/` holds no test (`gate/run_tests.py elements/decisions`: "no test found").
- Whether the course skills `10x-roadmap` and `10x-plan-review` are open to a reader: I treated them
  as course material that a reader cannot open, as the author did. Not verified against the course's
  terms.
- Whether the lesson of WAY-121 is public: settled by the human's answer to question 3, not checked
  (see Declined to judge).
