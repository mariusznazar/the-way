PASS 3c26a24635695e4e9ab21a906a2a42436d8469af

# Review of the merge of `origin/foundations` into `task/cycle-remarks-batch-4` (WAY-306)

Range reviewed: merge commit `3c26a24` (`git rev-parse HEAD` confirmed it). First parent `1b37abb`,
second parent `5b20e75`, base of the task branch `e3825a8`. I computed `git diff 1b37abb..3c26a24`
(6 files), `git diff 5b20e75..3c26a24` (11 files), and `git log e3825a8..5b20e75` (6 commits, the
request-decision-groups task). No conflict markers are left in `foundations`, `task-cycle` or
`elements`.

Answer to the question of the handoff: the two sides hold together. The resolution of both conflicts
is faithful to both sides, with one gap that comes from the join and is not a conflict: kind 16 was
added to *Fix or let through* but the places that say what "do it in this request" runs for each kind
of that group were not extended to it (finding 1, Minor).

## Findings

### Blocking (Critical or Important)

none

### Minor

**1. Minor — within the task. The answer "do it in this request" to kind 16 is defined only in
the kind's own paragraph; the three other places that list what that answer runs for each kind of
*Fix or let through* do not name kind 16.**

- `task-cycle/skill/correction.md:55-64`: the paragraph "An answer to do it in this request, to an
  item of *Fix or let through* other than item 8" lists items 4, 9 and 14 and no 16. The sentence
  before the list ("runs the correction the same way, the item it names being the remark the
  correction binds") is general, so a correction for kind 16 can still start; what the list lacks is
  what that correction does (write the missing fact, decision or source, in what form, and whether
  the foundation entry it writes is reviewed as an entry written by the return step is).
- `task-cycle/skill/request_template.md:446` (variant table, row "A correction"): "whether it ran on
  an answer to item 8, 4, 9 or 14, carries only 'Make a task of it?'" omits 16, so the rule that a
  correction's leftovers carry only the task question is stated for four kinds and not for the fifth.
- `foundations/decisions.md:9111-9117` (WAY-289 binding): "the same answer is offered for a step or a
  check the cycle skipped, a proposal of the task's own sections not applied and an incomplete
  reading of the review" does not name the gap of kind 16, although WAY-287 (`:9159-9163`) now says
  the human can "have the missing thing written in the request". WAY-289's title ("things the cycle
  left unfixed or undone") also fits a gap that stands from before the task less well than the three
  it lists.
- Why it matters: the template promises at `request_template.md:194-195` that what "do it in this
  request" runs for each kind "stands under that kind below and in `correction.md`". For kind 16 it
  stands only below. Today nothing contradicts anything, since kind 16's paragraph says what the
  answer does, so a correction is possible; the cost is that the orchestrator running a correction
  for kind 16 reads `correction.md`, finds no case for it and has to infer one. Note that the merge
  did not make this wrong: before it, kind 15 (the old number) had the question "Merge with the
  gap?" and no such answer; the target branch's lists and the task's kind meet here.
- Evidence: `grep -n "item 14\|item 4\|item 9" task-cycle/skill/correction.md
  task-cycle/skill/request_template.md` shows 4, 9, 14 and 8 named in both and 16 in neither.
- Cheapest repair: add a fourth bullet to `correction.md` ("for a descriptive `TODO` (item 16): the
  correction writes the missing fact, decision or source by the foundation skill that owns that
  entry, and the entry is reviewed as the return step's are"), add 16 to the list at
  `request_template.md:446` and a clause to WAY-289's binding sentence. I give no wording for the
  foundation skill route, since I have not read how the return step writes entries.

### Out of scope

none

## Declined to judge

- The target branch's own earlier line-length slips in WAY-287 (`foundations/decisions.md:9098`,
  `9099`, `9101`, `9124`, `9131`, `9150`, `9154`, `9182`, `9187`, 101-121 characters): the same line
  breaks stand in `5b20e75` (checked with `git show 5b20e75:foundations/decisions.md`), so the merge
  did not make them; they belong to the request-decision-groups task, not this one.
- Whether kind 16, the other kinds and WAY-327 together are the best shape for the section: the
  question of the handoff is whether the two sides hold together, not whether the target branch's
  design is right.

## What I checked, one by one

1. **Placement of kind 16** (`request_template.md:256-267`). It stands in *Fix or let through*, the
   group of "something the cycle did not do or did not fix and that can still be done in this
   request" (`:191-197`): the gap can be written in the request, made a task, or let through. Its
   three answers are the group's three answers. The group's rule that what cannot be done carries
   only "Make a task of it?" (`:195-197`) is compatible. Consistent with WAY-287's binding sentence
   (`foundations/decisions.md:9097-9099`, `9101-9107`) and its Rationale (`:9159-9163`). The earlier
   wording "Merge with the gap?" (task branch, kind 15) is gone, which is right: that question
   belongs to *You accept by merging*, and WAY-287's *Verification* now says the gap with no way to
   answer under that group is a violation (`:9145-9147`).
2. **Numbering.** Kinds run 1-3 (*Needed from you*), 4, 8, 9, 14, 16 (*Fix or let through*), 5, 6, 7,
   10, 11, 12, 13, 15 (*You accept by merging*). The numbers are unique, 1-16 with none missing, the
   kinds of a group come in ascending order, and the numbers other files use still point to the kinds
   they meant: item 15 in `request_template.md:58` and `:448` (form error held wrong) is still the
   kind 15 at `:312`; item 10 (`:449`) is the remarks listing at `:294`; item 12 in
   `task-cycle/skill/SKILL.md:567` is the relation-line kind at `:302`; item 4 in `:311` and `:450`
   is the skipped-steps kind. `grep` for `Merge with the gap`, `item 15`, `kind 15`, `kind 16`,
   `item 16` outside `.runs` finds no stale reference.
3. **WAY-287 as the merge leaves it** (`foundations/decisions.md:9086-9188`). The three places of the
   conflict: the binding sentence has the target branch's three groups and the task's "each
   descriptive `TODO` ... (WAY-71)" clause, in the same list position the task branch had it before
   the groups (`git diff 1b37abb..3c26a24`); *Verification* has the task's TODO cases rewritten as
   "puts it ... under *Fix or let through*" and one extra violation; *Rationale* has the target's
   group paragraph and the task's TODO paragraph, rewritten from "the merge accepts" and "for the
   human to accept" to "the merge leaves" and "have the missing thing written in the request, make a
   task of it or let it through" (this follows from the new placement; the old wording would have
   contradicted it). *Rejected* is the target branch's, unchanged; it does not discuss placing the
   TODO gap under *You accept by merging*, but WAY-287's Rationale gives the reason (the gap can
   still be written in the request), so I raise nothing.
4. **WAY-327 and kind 16** (`:10720-10757`; `request_template.md:315-332`). The four parts apply to
   each item of *Needed from you* and *Fix or let through* but one that asks for an action; kind 16
   is such an item, and step 2 of "Write, check, publish" (`request_template.md:11-13`) makes the
   writer read it against the four parts. Kind 16's wording asks for part 1 (the rule the invariant
   states or the question the decision answers, and what is missing, in plain words) and gives, for
   part 2, what each of the three ways does. It does not give costs or a recommendation; kinds 4, 8,
   9 and 14 do not either, and the rule makes the writer supply them, so I raise nothing. No entry
   number is required in the item: kind 16 itself cites WAY-71 and WAY-287 only in the template,
   which is addressed to the writer.
5. **WAY-289 / `correction.md`**: finding 1. The rest of `correction.md` (the merge-review paragraph
   at `:32-39`, the item 8 paragraph at `:48-53`) agrees with the template.
6. **WAY-290 and `task-cycle/request_check.py` with its tests.** The task branch did not touch
   either (`git diff 5b20e75..3c26a24 -- task-cycle/request_check.py task-cycle/test_request_check.py`
   is empty); the target branch's versions, with the three group headings, stand. The script judges
   no content (WAY-290), so it neither requires nor forbids kind 16; no new test is needed. The
   focused suite passes (below).
7. **WAY-317**: the target branch rewrote its *Verification* (the screenshot case is now accepted by
   merging, kind 13). The task does not touch it; the template's kind 13 (`:307-311`) and WAY-317
   agree.
8. **WAY-160 as the task has it** (`:4573`) and the cycle skill (`task-cycle/skill/SKILL.md` steps 10
   and the 9.4 recovery, `task-cycle/skill/blocked_finding.md`): the task's change to when the gate
   runs does not interact with the groups; the target branch changed `SKILL.md:511-514` (remarks
   check, group *You accept by merging*) and the task changed `:45-50`, `:323-327`, `:357-364`, all
   in different hunks, and the merge holds both.
9. **WAY-71, `elements/common/rules.md`, `elements/decisions/template.md`,
   `elements/invariants/template.md`** (the task's side): they say "a change that leaves one there
   puts it before the human (WAY-71)", which agrees with kind 16 and WAY-287; none names the group,
   so the move of kind 16 from *You accept by merging* to *Fix or let through* needs no edit there.
10. **WAY-326, WAY-295, WAY-291, WAY-274, WAY-288, WAY-292**: opened by title or by the line that
    names them in the files above; nothing in them bears on the join.

## Checks I ran

- `python -B gate/run_tests.py task-cycle` — exit 0, 257 tests OK.
- `python -B gate/run_tests.py elements/common` — exit 0, 144 tests OK.
- `python -B elements/common/foundation_check.py .` — exit 0, `0 errors`.
- `git diff`, `git log`, `git show 5b20e75:foundations/decisions.md`, `grep`, `awk` for line lengths
  and stale references (read-only).
- Not run, as the handoff says: the other gate directories and the full gate (the orchestrator runs
  it on the merge).
- Not checked: a real description written by the template (no scratch run of `request_check.py` on a
  description with kind 16; the script judges no content, so such a run would show nothing about the
  join).

## Reaches beyond the dispatch

- `task-cycle/skill/SKILL.md:555-570` and `:505-515`, to see which kind numbers other files cite
  after the renumbering (what: item-number references; why: kind 16's addition could break them).
- `grep -rn` of `For you to decide|Fix or let through|Needed from you|You accept by merging` and of
  `descriptive TODO|Merge with the gap|item 15|kind 16` over the worktree outside `.runs`, to find
  every place that cites the groups or the kind.
- WAY-290 and WAY-317 read whole from `foundations/decisions.md`, since the dispatch names them.
- `git show e3825a8..1b37abb` hunks for `request_template.md` and WAY-287, to see what the task
  intended before the merge (the original kind 15 and its question "Merge with the gap?").

## Unread material

Dispatch material read whole: the handoff, `task-cycle/review/SKILL.md`, WAY-287 (as the merge
leaves it; the target branch's version through `git show 5b20e75`), WAY-289, WAY-290, WAY-317 and
WAY-327 as they stand in the file, `task-cycle/skill/correction.md`, the "A correction" variant row
and the kind list of `request_template.md`.
Read in part: WAY-71 (its whole entry in the diff hunk, not the file's neighbours) and WAY-160 (its
heading and binding paragraph from the file; its *Verification*, *Rationale* and *Rejected* through
the diff hunk of the task, which holds them whole as changed); `task-cycle/skill/SKILL.md` (the
hunks of both sides and the passages named above, not the whole file); `elements/common/rules.md`,
`elements/decisions/template.md` and `elements/invariants/template.md` (the task's hunks only);
`task-cycle/request_check.py` and `task-cycle/test_request_check.py` (not opened beyond the empty
diff of the task's side and the passing suite).
Not read: `task-cycle/test_remarks_check.py` and `task-cycle/remarks_check.py` (task's change, no
bearing on the join); the other decisions of the log.

## Searches not found or unclear

- I looked in `task-cycle/skill/correction.md`, `task-cycle/skill/request_template.md` and
  WAY-289 for a rule on what "do it in this request" does for a descriptive `TODO` and found it only
  in kind 16's own paragraph (finding 1).
- I looked for a statement of how a correction writes a foundation entry (which skill, whether it is
  reviewed) and did not find one in the files read; I did not read `task-cycle/skill/foundation_step.md`
  or the return step's file, so I cannot say whether they hold it.
- The handoff speaks of "the wording of WAY-287's binding sentence, *Verification* and *Rationale*,
  its *Rejected*" without naming the task's own wording of *Rejected*; the task branch before the
  merge had no edit to WAY-287's *Rejected* (`git diff e3825a8 1b37abb`), so the merged *Rejected* is
  the target branch's.
