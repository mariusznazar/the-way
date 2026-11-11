FAIL 9eb2bd637697fd5f3cccdb891091110054f9d292

# Review of the whole change: backlog-line-for-plan-tasks

Range `52f8164a354ee1a704af0d58add2f3be8e4f0247..9eb2bd637697fd5f3cccdb891091110054f9d292` (commits
`74fbd01`, `9eb2bd6`), confirmed by `git rev-parse HEAD`. Variant: the whole change, one author, no
plan, no spec, no slices. Counts: 1 blocking, 6 Minor within the task, 1 out of scope (Minor).

Paths below are relative to the reviewed worktree
`the task's worktree root`.

## Verdict in one paragraph

The change meets every item of *To do* (1-6) and every row of *Settlements to record* (1-5) in the
case where the task place's rules exist, and its *Rejected* hold only ways the task lists, with one
cost in the author's own words (Minor 1). One gap blocks: the rule that makes the line says "in the
turn that first creates the task document" and gives no route for the case the change itself
provides for, a missing `task-rules` entry, nor for a task document that already exists without a
line, nor for an orchestrator that finds no line at acceptance. In each case the line is lost
silently, which is the failure the task exists to fix.

## Blocking findings (Important, within the task)

### B1. No route to a line the first turn could not make, or that never existed

- Place: `project-level/task_line.md:11-14` ("Make the line"), `project-level/task_line.md:46-52`
  ("Move to ready"), `project-level/task/skill/orchestrated_mode.md:40-45`,
  `project-level/task/skill/read_sources.md:23-26`.
- What is wrong: every file ties the making of the line to one moment, "the turn that first creates
  the task document", and says "make one where the task has no line". Three situations leave a task
  with no line after that moment, and no sentence covers any of them:
  1. The rules entry is missing (the case WAY-107 and settlement row 4 provide for). The refiner may
     "write no form of your own" (`task_line.md:7-9`), so it asks in its turn and ends it. After the
     human's agreement it writes the `task-rules` entry in a later turn
     (`orchestrated_mode.md:12-14`), but that later turn is not the one that "first creates the
     document", so the literal text makes no line. A fresh refiner per turn (WAY-154) reads the same
     words.
  2. A task document that exists without a line: one written before this change, or a parked one
     refined again from its text (`project-level/task/skill/draft.md:11-15`). It is never "the turn
     that first creates" the document, so the rule never fires. This is the situation of the author
     of the task today (documents without lines).
  3. The orchestrator at acceptance (`task_line.md:46-52`, `lead/skill/SKILL.md:168-176`) is told to
     "move the line to ready" and holds no instruction for finding none. A line lost in the race the
     task accepts (question 2), or never made, leaves it with an object that does not exist, so it
     improvises.
- Why it matters: WAY-154 (as the change writes it) accepts one named cost, a line lost to two writes
  in the same instant, and its rationale says that loss "shows afterwards as a task with no line".
  The three cases above are not that cost: they are certain, not rare, and they are the cases the
  change's own rule produces (case 1 is the first thing a product without a `Task rules` line meets).
  Item 2 of the task asks for the line to be made in that turn; it is silent on what follows when it
  cannot be, and "silence is not permission". A fix is a sentence in `task_line.md` ("Make the
  line"): where the line could not be made in that turn, or the document exists without one, make it
  in the first turn where the rules are known, and say in the turn that it stands unmade; and in
  "Move to ready": where no line stands at acceptance, make it, already ready, and say so. The
  sentences in `orchestrated_mode.md` and `read_sources.md` then point to it instead of repeating the
  moment.
- Evidence: text of the cited lines read whole; no test reaches these files
  (`grep` of `test_*.py` for the skill files found none), so the finding rests on reading the text.
- Slice: not applicable (no plan).

## Minor findings (within the task)

1. **A cost in WAY-107's *Rejected* is the author's wording, not the source's.**
   `foundations/decisions.md:2486-2488` ("the rules of the task place kept in the product ... — a
   rule of a place kept in two files, and the rulebook of the place says it in the place"). The task
   lists this way under question 3 *Not chosen* with the human's words only ("a nie żeby były
   zapisane gdzieś przy produkcie") and gives no cost; WAY-134 gives such a way's cost only from its
   source, or `unknown`. The cost sentence is a reasonable inference from the task's Context, but it
   is the cycle's. Same place, `decisions.md:2476-2479`: the rationale's price "a product whose tasks
   lie in a place with no such rules finds an agent asking where they are" is the author's concern 1,
   not question 5's cost (which is only "the same path repeated"). Fix: write `unknown` for the first
   cost, or mark both as the cycle's; keep the price in the rationale only if the human accepts it at
   the request.

2. **The identifier derivation guarantees less than `task_line.md` says, and the file does not name
   the assumption.** `project-level/task_line.md:24-34`. The rulebook requires an identifier
   unambiguous "in the whole place" (the task's carried question says the whole vault). The
   derivation is plan file name + `-` + task name. It clashes when two plans in the place share a file
   name (the plan template gives no naming rule: `project-level/plan/template.md`, "in a file of its
   own"), and also when the join is ambiguous: I ran the derivation (`python -I`, exit 0) and plan
   `a-b.md` with task `c` and plan `a.md` with task `b-c` both give `a-b-c`. The author's report
   names the first assumption (choice 1) but the file that agents read does not. The author's own-work
   check ran the derivation on two inputs and never reached this, which is the weak point. Fix: say in
   the file that the identifier is unambiguous only while plan file names are distinct in the place,
   and add to "Make the line" a step: where another line already carries the identifier, ask the
   human. I judge the choice itself (the orchestrator's Q1, with runs collapsed and ends trimmed)
   sound and the collapse of runs a correct repair of the first wording.

3. **Three guidelines skills still say a refiner "edits only the task document and its turn".**
   `product-guidelines/coding/orchestrated_mode.md:9`, `product-guidelines/testing/orchestrated_mode.md:8`,
   `product-guidelines/styleguide/orchestrated_mode.md:9` (author's concern 2). They run under
   `refine-task` in orchestrated mode ("this skill follows that mode's routing"), which now makes the
   line in the first turn, so a refiner of such a task reads two statements of its writes. The
   statements can be read as limiting only what the guidelines skill itself edits, so I grade it
   Minor, not blocking, and within the task because they restate the rule of item 1. Effect if left:
   a refiner of a coding, testing or styleguide task may skip the line, which for those tasks is the
   silent loss the task removes. Fix: add "and the task's line, as `refine-task` gives" to each, or
   point them to `project-level/task/skill/orchestrated_mode.md` instead of restating.

4. **The same rule stands in five places a refiner or orchestrator reads.** "Make the line in the
   turn that first creates the document, in parallel, with no queue": `task_line.md:11-14`,
   `orchestrated_mode.md:40-45`, `read_sources.md:23-24`, `lead/conversation_template.md:22-24`,
   `lead/skill/SKILL.md:104-107`, besides WAY-154. A rule has one place (`instruction-files/SKILL.md`,
   "How to write a single rule"); a change to B1's moment would have to be made five times and the
   copies will drift (WAY-263's concern). The orchestrator's copy (`no order between writes`) and the
   refiner's copy are role-specific and may stay; the refiner's three (`read_sources.md`,
   `orchestrated_mode.md`, `task_line.md`) should become pointers to one.

5. **WAY-154's wording of the dependency step does not match `route_changes.md`.**
   `foundations/decisions.md:4449-4451` ("brings the dependencies in the task lines in step with the
   plan when it changes them") against `project-level/lead/skill/route_changes.md:11-13` (after the
   plan-project agent altered a `Depends on` cell). By WAY-156 the orchestrator never changes
   dependencies itself, so read literally the entry's condition is never true and the files act on
   a broader one. The task's own words ("gdy zmienia zależności w planie") carry the same ambiguity,
   and the files do what the task means, so I do not grade it Important under WAY-263. Fix: "when the
   plan's dependencies change".

6. **Vocabulary.** The same object is "the task's entry in the backlog" in
   `project-level/task/skill/final_review.md:27` and `read_sources.md:23` and "the task's line"
   everywhere else; `final_review.md:27-29` then uses "entry" for the locations-file entry in the
   same sentence. "Entry" is a glossary term of the foundation (`foundations/glossary.md`, "entry")
   and a locations-file key; "the task place" is used throughout and is not defined (it is readable
   from `backlog_place.md:1-4`). No sentence is read wrongly, so Minor (WAY-297). Fix: "line" in the
   two files named.

## Out of scope (outside the task)

1. **A task returned to refinement keeps a Ready line.** `project-level/task/skill/draft.md:11-15`
   and `project-level/lead/skill/task_return.md:7-10` return a task (document `refining`, plan row
   `to refine`) with no word about its backlog line, so after this change a line moved to Ready
   stays Ready while the document is in refinement, and the vault's check of notes against lines
   would report it. The task's *Out of scope* names only `in cycle` and `done`; this transition is in
   neither the task nor its sources. Minor, for the human to put into a task.

## Declined to judge

- What an agent does where the task place has no rules at all and the answer to "where are they" is
  "none" (author's concern 1): WAY-107's rationale, as the change writes it, accepts that cost
  ("finds an agent asking where they are"), and question 5 and settlement row 4 give only "ask once
  and offer the entry". Set aside as decided.
- The `Task rules` line of loop2's `AGENTS.md`: the task's Context puts loop2's `## Backlog` outside
  the task.
- Whether the status the rulebook of the vault gives a new line, or the symbols of its dependency
  fields, are right: they live in the author's private notes, are not in the change, and the task
  forbids the-way to name them (WAY-107). I checked only that the change names none (grep, below).
- Behaviour of a refinement of a task that belongs to no plan: the identifier and dependencies apply
  to plan tasks only; the task says nothing more.

## Judgement of the points the handoff put to me

- **Q1, the identifier:** answers the carried question, with the two caveats of Minor 2.
- **Q2, unread instruction-files material:** I read `judging.md`, `placing.md`, `writing.md`,
  `kind_path_rule.md`, `kind_skill.md`, `kind_main_file.md`, `changing.md`, `tool_loading.md` and
  `instruction-files/SKILL.md` whole. The new file `project-level/task_line.md` and the edited skills
  break none of their rules in a way that bears: pointers name a path in backticks with their
  condition (WAY-129); the new `AGENTS.md` item carries a decision (WAY-130); no `@` was added; the
  file lies in `project-level/` beside `backlog_place.md`, which two skills read, as WAY-256 places a
  fragment several skills need. The only rule that bears is "a rule has one place" (Minor 4).
  Nothing in `judging.md`, `placing.md`, `writing.md` or `kind_path_rule.md` reaches the change.
  The author's partial reading bears on nothing it judged, as the orchestrator accepted.
- **Q3, concerns 1 and 2:** concern 1 declined (above); concern 2 is Minor 3.
- **The three files outside the handoff:** `project-level/lead/skill/route_changes.md` is within the
  task (item 4, the orchestrator corrects lines when the plan's dependencies change; WAY-156 puts the
  plan edit with the plan agent, so after it returns is the right place). `project-level/task/template.md:104-106`
  and `project-level/plan/skill/delegated_mode.md:9-10` are within the task: each stated who writes
  what, which the change made inexact (the search of WAY-33), and each edit is minimal and agrees with
  the entry.
- **WAY-27, marked `the cycle's`:** judged against WAY-27's own text and WAY-263. The new binding
  sentence ("the place of its tasks and the rules of that place, named in `## Backlog` ... each by an
  entry of the locations file ... never by a path") says exactly what the changed `AGENTS.md` does,
  so the files do not restate it more broadly or differently. Without the edit the new `AGENTS.md`
  item would violate WAY-27's old sentence ("the place of its tasks ... and nowhere else"), and the
  task's item 6 requires that item, so the change is necessary and within the task although WAY-27
  is not in *Decisions in play*. The procedure fits WAY-30 (an edit of a decision proposed on the task
  branch, found by the search of WAY-33, accepted only at the merge by the human, WAY-14). It is an
  entry no row carries, so by WAY-114 the request must put it in the section for the human's
  decisions, as the author asked. Not a finding.
- **Foundation entries against the task:** WAY-154, WAY-107 and WAY-320 carry settlement rows 1-5
  (checked sentence by sentence against the rows); WAY-144 untouched, as the task says. WAY-154's
  *Rejected* items map to question 1, 2 and 4 *Not chosen* with costs from the sources; WAY-320's
  new item maps to question 5 with its cost; WAY-107's five new items map to questions 3 and 5, cost
  of the first in the author's words (Minor 1). No way is derived by the author.
- **Own-work check:** the requirement named (the identifier) is the carried question and a fair
  choice, but its check ran the derivation on two inputs and so could not catch the requirement most
  likely unmet by this change, B1 (no route when the moment passes), nor the clash of Minor 2. A
  changed invariant test: none, and no invariant is changed.
- **Tests:** none added or changed; the change is prose and foundation entries, and no test of this
  repository reads the changed skill text (grep). The author's unexplained `F` in a first
  `project-level` run is not reproduced by their second run (275 tests OK); I did not repeat the
  12-minute directory run, and nothing in it reads a changed file, so I treat it as unverified, not
  as a finding.
- **Reserved choice, trust boundary, irreversible operation:** none in the change (agree with the
  orchestrator; no file the part map names as a trust boundary changed; the change writes no
  language, framework, library, store, login or place to run). The one write outside the repository
  it asks of an agent is the `task-rules` entry in the user's locations file, after the human's
  agreement is recorded, which WAY-107 and `backlog_place.md` allow outside a task cycle (WAY-140).
- **User interface:** none involved.
- **Guidelines:** the-way has no guidelines directory; WAY-328 departs from the coding and testing
  guidelines for its own code and tests, and no code or test was written. Read whole.

## Checks run

All from the reviewed worktree, read-only, with `python -B`; `git status --short` was empty before
and after.

| Check | Command | Exit |
|---|---|---|
| Foundation identifiers and references | `python -B elements/common/foundation_check.py` | 0 ("0 errors") |
| Instruction files | `python -B instruction-files/check_instructions.py .` | 0 ("0 error, 0 warn, 3 info") |
| Private paths and note links in tracked files (invariant `tracked-file-private-paths`) | `python -B task-cycle/test_tracked_files_private_paths.py` | 0 (1 test OK) |
| Instruction-file imports and root `CLAUDE.md` (invariants `instruction-file-imports`, `root-claude-md-import`) | `python -B -m unittest test_instruction_files` in `agent-instructions/` | 0 (5 tests OK) |
| Skill entry points (invariant `skill-entry-points`; no description changed) | `python -B -m unittest test_skill_entry_points` in `agent-instructions/` | 0 (13 tests OK) |
| Identifier derivation, as `task_line.md` words it, on 7 inputs including the clash `a-b.md`+`c` against `a.md`+`b-c` | one-off `python -I` expression | 0 (output as in Minor 2) |
| Diff and log | `git diff <base>..<head>`, `git log <base>..<head>`, `git rev-parse HEAD` | 0; head confirmed |
| Foundation search of the change's topic | `grep` of `foundations/*.md` and `*.md` for `task-rules`, "task's line/entry", "locations file", `## Backlog`, `edits only the task document` | 0; found the three guidelines files (Minor 3), WAY-147's "a task's entry there links its document" (consistent), WAY-140 (consistent), `draft.md`/`task_return.md` (out of scope 1) |

Not run: the full `gate/run_tests.py` and the 12-minute `project-level` directory run (the cycle's
own; nothing in `project-level/test_*.py` reads a changed file); the tests in `installation/` that
mention `## Backlog` write their own fixture `AGENTS.md` and read no changed file.

Checks of mine in the report's text above used no result of the author without saying so.

## Reaches beyond the dispatch

- `project-level/plan/template.md` (lines 1-60), to see whether plan file names are constrained, for
  Minor 2. Found none.
- `project-level/task/skill/draft.md:8-20` and `project-level/lead/skill/task_return.md:1-25`, to see
  what happens to a task that returns to refinement, for out of scope 1 and B1 case 2.
- `project-level/task/skill/guideline_findings.md` (grep hits at lines 14 and 57), which add a
  task to the backlog "by the rules of `read_sources.md`": consistent with the change, no finding.
- `product-guidelines/{coding,testing,styleguide}/orchestrated_mode.md`, whole, for Minor 3.
- `task-cycle/skill/SKILL.md:77-78` (grep hit): the cycle's own write to the task's entry; untouched
  and within the task's *Out of scope*.
- `foundations/decisions.md` WAY-14, WAY-30, WAY-33, WAY-263 and WAY-297 headings, and the user's
  `.ai/rules/scripts.md` before the one-off script.

## Unread material

Decisions of my selection: the parts touched are `decisions`, `project-level` and `agent-instructions`
(plus the decisions the task and the reading method name). Search by *Scope* gave 141 decisions, to
which I added WAY-263 and the task's *Decisions in play*.

- Read whole: **24** (WAY-14, 27, 30, 33, 101, 107, 124, 129, 130, 134, 140, 144, 147, 152, 154,
  155, 156, 256, 263, 313, 314, 315, 320, 328), and by reading also WAY-113, WAY-114, WAY-308 and
  WAY-99 whole after their titles pointed to a bearing; that makes **28** whole in total.
- Run through by title only: **114** (of the 28 read whole, 27 lie among the 141 found by *Scope*;
  WAY-263 does not, as its *Scope* is `task-cycle`; 141 minus 27 is 114).
- Decisions that bear on the change and stayed unread: WAY-150 (how skills choose what to read:
  concerns the selection method, not what the change writes), WAY-142 and WAY-143 (what the plan
  holds; the change adds no plan field), WAY-161 and WAY-164 (grading and own-work check: read as
  quoted in `task-cycle/review/SKILL.md`, not as entries), WAY-297 (read as quoted in the method).
  None changes a finding.
- Invariants (the whole file), `foundations/part_map.md` and `foundations/glossary.md`: read whole.
- Guidelines: none (the-way has no guidelines directory; WAY-328).
- Files of the change: every changed file read in the diff and, for the skill files, the surrounding
  text of the changed passage; `project-level/lead/skill/SKILL.md` and
  `project-level/lead/conversation_template.md` read in the passages around the changes, not whole.
  The author's report and the frozen task read whole.

## Searches not found or unclear

- A rule for the first turn that cannot make the line, for a document that exists without a line, or
  for an orchestrator that finds no line: looked for in `task_line.md`, `orchestrated_mode.md`,
  `read_sources.md`, `lead/skill/SKILL.md`, `route_changes.md`, WAY-154 and WAY-107; not found (B1).
- A rule that plan file names are distinct in the place: looked for in the plan template, the plan
  skill's `write_and_check.md` area (grep for "file name") and `plan_check.py`'s documented checks;
  not found (Minor 2).
- A source in the task for the cost of the rejected way "rules kept in the product": not found
  beyond the human's quoted sentence (Minor 1).
- Where the rules of the task place say what to do for a task returned to refinement: they lie in the
  author's private notes and are out of my reach; unclear whether they cover it (out of scope 1).
- Whether "the task place" means a directory, a file or a tool in a sentence such as
  `task_line.md:7`: clear from `backlog_place.md:1-4`, but not defined where it is first used
  (Minor 6).
