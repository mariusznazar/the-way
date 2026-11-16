# Findings of the review of the whole change — for the fix

Review: `reports/review-whole-report.md`, first line `FAIL 05b46486103be3db6ead33ffff5b53e3c9988331`,
range `aba5ee92a0734c2e775cc69662af669bf6455795..05b46486103be3db6ead33ffff5b53e3c9988331`. The blocking
finding is I1; M1 and M2 are the Minor findings of the review of the whole change within the task, which
are fixed with it (`task-cycle/skill/SKILL.md`, "The end of a code review"). The reviewer's words follow.

## Blocking

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

## Minor findings of the review of the whole change, within the task

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
