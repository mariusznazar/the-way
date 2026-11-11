# Findings of the review of the whole change (head 9eb2bd637697fd5f3cccdb891091110054f9d292), in the reviewer's words

Source: `reports/whole-review-report.md`, lines 22-124, copied without change. The one blocking finding comes first, the six Minor findings within the task after it (WAY-161). Paths are relative to the worktree.

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
