FAIL 63fa039

# Review of the fix — logs-life-and-failure-notice

Range `4a3ee37..63fa039`, one commit. `git rev-parse HEAD` is the head given. Bounded by
`reports/whole-review-findings.md` as `task-cycle/review/fix.md` gives. The author contests no finding.

Counts: 1 blocking (new in the fix diff), 1 Minor, 0 out-of-scope. The four findings of the first
review are fixed; the blocking finding below is what the fix itself broke, which counts as one that
remains. The six Minor findings of `reports/whole-review.md` were not to be fixed and stand as written
there.

## The four findings

### 1. WAY-270 drops the alert — fixed

The binding part reads "answered by a tool that collects failures, an alert or a deliberate absence"
(`foundations/decisions.md:7903-7904`), the complying example holds an alert (`:7921`), and the
rationale gives answer 1's weak point (`:7948`). No product is named, and the step's files still name
only the deliberate absence, as spec D5 gives. The kinds in a binding sentence read close to a closed
list, but they are row 2's own words, the sentence count stays three, and a research agent does not
open the entry, so `research.md`'s "never from a fixed list" stands. No finding.

### 2. WAY-270's rationale keeps the replaced reason — fixed

`foundations/decisions.md:7941-7943` now reads "so at a definition the question comes with it; at a
task the deployment skill's check carries it (WAY-139)". This matches the mark under answer 2, the
binding part at `:7904` and the *Rejected* way on a task that chooses a place to run.

### 3. "The last two items" of WAY-139 — fixed

The record's life is an item of its own, so the list holds seven (`foundations/decisions.md:3503-3505`),
and the sentence reads "For the two items on the record's life and on a failure" (`:3509-3510`), which
names the same two as `resolve_gaps.md:56-57`. A search of `foundations` and `project-level` finds no
"last two items" and no count that disagrees.

### 4. A new list over a silent decision is not nested — fixed

- New list: `list.md:23-26` puts the item `— open` with the decision nested, and
  `running_product.md:22-27` gives the form for a new list and heads the section so that it fits both.
  The path `SKILL.md` step 1 → `list.md` → `settle.md` sub-step 1 and `research.md` step 1 → sub-step 7
  now carries the decision, its answer as an option and the entry the result rewrites. A resumed list
  and a new list behave alike. No reference to the old heading remains; the phrase "a list already
  written" that remains is prose, at `failure_notice.md:5` and `running_product.md:5,16,26`.
- Run at a task: the item stands `— open` with the decision nested, as spec D6 reads. The defect is
  gone, by a route that gives the new finding below.

## Important (blocking, new in the fix diff)

### N1. `task_run.md` gains a rule by which a held decision opens at a task with no human's word

- **Place:** `project-level/technology/task_run.md:50-54`, the sentence added right after "An agent never
  opens one.": "A decision silent on part of what a matter of the logs, the interface or the development
  data asks (`running_product.md`) holds nothing, where the note touches the matter: the item stands
  `— open`, with that decision nested under it as `Changes:`."
- **What is wrong:** the condition is that the note touches the matter, not that the human gave the
  word. A note is not always the human's: `task_run.md:20`, "A run that refinement starts for a reserved
  choice takes that choice as its note". The deployment route needs no such sentence, since
  `resolve_gaps.md:65-66` already makes the human's yes "the human's word that the run asks for where a
  logs decision stands", and a note in a request is the human's word already. So what the sentence adds
  beyond the existing exception is exactly the case with no human's word: an agent's run on a reserved
  choice that touches the logs opens a decision of the foundation, and its result changes that decision.
- **Why it matters, against what:**
  - Answer 5 is the human's settlement, and it rejects this. Its question gives "każe agentowi otwierać
    decyzję" as the reason to drop the way, its *Not chosen* counts "trzeba dopisać reguły na otwieranie
    decyzji przez agenta" as a cost, and it says "WAY-267 zostaje bez zmian". The change's own *Rejected*
    in WAY-139 and WAY-270 repeat that cost ("rules are needed on an agent opening a decision").
  - WAY-267 binds "a choice a decision of the foundation holds opens only on the human's word", with the
    violating example "an agent opens a choice a decision holds on its own". The entry is unchanged, and
    the new sentence, placed as a qualification of "An agent never opens one", is an exception that
    lives only in a file beside the skill (WAY-30: "no exception lives only in a task document, plan or
    cycle record", by its reasoning; WAY-25 for a collision with no precedence written).
  - Spec D1, "Who may open what": at a task "the logs reach a run only through a note the human agreed
    to (D6), which is the human's word", and of the rule of `task_run.md` and WAY-267's sentence, "Both
    stay as they are". Spec D7: "Nothing else changes". The spec's *Files* row for `task_run.md` is D7
    alone.
  - WAY-165 does give a way to read the two as compatible, "holds" as "settles", and the human still sees
    the list and accepts the whole document, so the damage is bounded. What it costs is the rule the human
    kept: at a task, opening a decision takes the human's word. `task_run.md:78` also shows the seam:
    only "A choice the human opened says in its *Answer* which decision it changes", so an item opened
    this way has no line telling the run to say it, and the first review's concern is met only by the
    nested line.
- **How this came about:** finding 4 raised that the exception might not fire, because `list.md` says a
  silent decision holds nothing. Its fix line named `list.md` only. The right ending there is that the
  exception does fire, not that the decision stops counting.
- **Evidence:** the passages above; a read of `task_run.md` *Start* and *List* and `resolve_gaps.md:23-31`.
  No test pins the step's text.
- **Fix in one line:** make the sentence keep the human's word: for this rule a decision silent on part of
  such a matter counts as one that holds the choice, so it opens only on the human's word and then stands
  `— open` with the decision nested. The deployment route already gives that word, and a reserved choice
  whose note touches the logs then asks the human.

## Minor (new in the fix diff)

1. Unwrapped lines the fix leaves in `foundations/decisions.md`: `:7904` (165 characters), `:7924` (140) and
   `:7948` (187), against the file's width of about 100.

## Declined to judge

none

## Checks

- `python -B elements/common/foundation_check.py .`: exit 0, "0 errors".
- `python -B agent-instructions/skill_entry_points.py`: exit 0, "entry points are current".
- `python -B gate/run_tests.py project-level`: exit 0, 268 tests OK.
- `git diff --check 4a3ee37..63fa039`: exit 0.
- Manual: read `4a3ee37..63fa039` whole, then the paths of a new list, a resumed list and a run at a task
  on the new head. Searches of tracked files for "A list already written", "last two items", "five items",
  "seven items", "an alert" and "An agent never opens".
- Not run: the full gate, the cycle's own; an agent following the texts, which no test exercises.

## Reaches beyond the dispatch

`foundations/decisions.md`, WAY-267, WAY-30 and WAY-25, read in the first review, for finding N1; the task's
answer 5, spec D1, D6 and D7, for the same.

## Searches not found or unclear

- Unclear: whether the human means "the human's word" to cover a note a refinement agent derives from a
  reserved choice. `task_run.md:50` gives "in the note", and WAY-267 gives "the human's word"; spec D1 says
  "a note the human agreed to", which I took as the binding reading. If the orchestrator's reading is that
  every note counts, N1 falls to a Minor on the wording of `task_run.md:78`, and that reading is the
  question to settle.
- The fix report's claim that *Write* in `task_run.md` "names which decision is changed" holds only for a
  choice the human opened, as N1 says.
