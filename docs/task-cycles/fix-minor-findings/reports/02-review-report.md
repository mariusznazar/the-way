PASS 820f9639bfad5e9b185c248f7a813809fe517b05

# Review of the whole change — fix-minor-findings

Range: base `86cc21e876f27f5d7d3ffd811ba11b687ac04cc6`, head `820f963` (`8eafea5` decisions, `820f963` cycle
documents). `git rev-parse HEAD` confirmed as `820f9639bfad5e9b185c248f7a813809fe517b05`. One author, no
plan, no spec. Trust boundary: no. Irreversible operation: no. The change is prose and decision text, so the
review compares texts with the task's rows and with each other.

## Blocking findings

none

## Coverage of the task (verified, not taken from the author's report)

- To do 1 (the cycle fixes in-scope Minor findings of the whole-change review before the request opens, in the
  fix after a blocking finding, else in one fix with one review): met in WAY-161
  (`foundations/decisions.md:4371-4379`), WAY-162 (`:4454-4462`), `task-cycle/skill/SKILL.md:370-381` and
  `:396-408`, step 9 and 10 (`:343-345`), `task-cycle/change/fix.md`, `task-cycle/review/fix.md`,
  `task-cycle/review/whole_change.md`.
- To do 2 (a Minor-only fix whose review finds a new Critical or Important finding is reverted, request opens on
  the accepted code, no third round, Minor findings and the new finding go to the description): met in WAY-162
  (body, Verification, Rationale, Rejected), `SKILL.md:402-408`, `request_template.md` (Technical changes, Minor
  findings), `record_template.md:50-52`. The fix that only carried Minor findings after a blocking one ends as
  before (blocked): in WAY-162 Verification and `SKILL.md:392-394`.
- To do 3 (item 8 asks "fix it in this request" or "make a task of it", one answer may cover the list, "fix"
  runs one correction, what remains asks only for a task): met in WAY-289, `request_template.md:184-193` and the
  correction row of the variants table, `task-cycle/skill/correction.md:43-48`.
- Questions carried to cycle: both answered (`correction.md` has its own paragraph; the Minor-only fix is made by
  the one author on its class, on a planned route by a fresh agent on the orchestrator's class).
- Rows of *Settlements to record*: row 1 -> WAY-161, row 2 -> WAY-162, row 3 -> WAY-289; each entry carries the
  row's meaning. *Rejected* holds the task's *Not chosen*: WAY-161 holds A, C, D (`:4421-4430`); WAY-162 holds a,
  c (`:4505-4508`); WAY-289 holds a, c (`:8838-8842`). Nothing invented from the sources: the additions beyond
  the rows (new serious finding of a reverted fix also under WAY-289; a fixer may contest a Minor finding; the
  revert as one commit by the orchestrator; WAY-297 consequence edit) are the cycle's choices, listed in the
  author's report as such, and none contradicts a row.
- WAY-297 (the cycle's consequence edit): needed, since its Rationale and *Rejected* said a Minor glossary
  finding stays before the human and is "never repaired in the cycle", which row 1 makes untrue. The edit is
  minimal and consistent with WAY-161.
- Choices the cycle made that bind the author: judged sound. The Minor-only fix by the same author class, the
  restriction to findings the report lists and does not mark out of scope (it keeps the reviewer the sole judge of
  scope, WAY-161), the new serious finding on the *Minor findings* list with its grade (no change to
  `request_check.py`; the heading list is unchanged, the form tests pass), the own paragraph in `correction.md`
  and the revert by the orchestrator in one commit all agree across the decision, `SKILL.md`, the template and the
  fix files. Leaving `agent-instructions/README.md` unchanged is sound for what it says (see the out-of-scope
  finding below).

## Repository search for lines now untrue

Search of the whole repository outside `.runs/` and `docs/` (`docs/task-cycles/` holds only archives) for
`not fixed|never fixed|without a fix|unfixed|not yours to fix|Make a task of it|blocking findings only|Minor
findings alone|one fix|PASS.*request` and a listing of every `Minor` outside the edited files. Every remaining
hit is new text or still true: WAY-163 (blocked requests only), WAY-287 (the list of what the human's section
holds; "unfixed findings ... will feel" stays true), WAY-229 and WAY-136 (class of the fix; a Minor finding names
no slice, so covered), WAY-220/221/263 (grades), `review/SKILL.md` (grade and report form), `request_template.md:143`
(generic example), `reserved_return.md:26`, `task-cycle/test_request_check.py:63` (quotes a WAY-162 sentence that
is unchanged), `agent-instructions/README.md:62-65` (hand-made route; "the other remarks go into the lists of
the request's lower part" stays true). Invariants, glossary, environment facts and part map hold no statement
about fixing Minor findings.

## Minor findings

1. **Within the task.** `foundations/decisions.md:8836` (and the same idea at `:8841`, *Rejected*): WAY-289's
   Rationale says that of the findings nobody will feel, "those within the task have been fixed already
   (WAY-161)". WAY-161 fixes only the Minor findings the review of the whole change lists; a Minor finding of a
   code review after it, of a slice review the whole-change review does not list, or one a fix left, is within
   the task and not fixed. The sentence restates WAY-161's reach more broadly and without its qualification.
   Why it matters: a later reader takes it that no in-task finding can be waiting unfixed. Grade: Minor, not
   Important under WAY-263, because it stands in a Rationale and *Rejected*, not in the rule text, and the rule
   text of WAY-289 and of WAY-161 are accurate; the behaviour the cycle follows is unaffected. Fix: write "those
   within the task that the review of the whole change lists have been fixed already (WAY-161)" and, in the
   *Rejected* clause, "the cycle fixes those the review of the whole change lists".
2. **Within the task.** `foundations/decisions.md:9105-9107` (WAY-297 *Rejected*, last clause): "a collision shown
   on a sentence is then repaired only by the fix for Minor findings, which the cycle gives up whole when the
   review of that fix finds a new serious finding, so the collision reaches the merge." As written the
   conclusion follows from the first branch only; the fix usually lands and the collision does not reach the
   merge. Why it matters: the reason given for rejecting "Minor always" is overstated. Evidence: compare with the
   original ("is then never repaired in the cycle"), which was true. Fix: "...repaired only by the fix for Minor
   findings of the review of the whole change, which the cycle gives up whole when the review of that fix
   finds a new serious finding, so that in those cases, and for a finding of a later review, the collision
   reaches the merge".
3. **Within the task.** `foundations/decisions.md:4454-4462` (WAY-162 body, new sentence): the one sentence
   holds the Minor-only fix, the revert, the request's lists, and then a "while in the code reviews after the
   review of the whole change, and for a Minor finding that remains after a fix, ..." contrast, and says Minor
   findings "that WAY-161 has fixed" where WAY-161 only has the cycle fix them. It is hard to parse, and
   the rule is correct only when read twice. Fix: split into two sentences (the Minor-only fix and its revert;
   then what the later reviews and a remaining Minor finding do), and write "that WAY-161 has the cycle fix".
4. **Within the task.** `task-cycle/skill/SKILL.md:402-403`: "the request opens on it, not blocked, with no
   further review of that code". Step 12 (`:415-419`) still has a fresh reviewer review the merge of the target
   branch where that changes the reviewed code, and the gate runs on the code the revert leaves (step 10). The
   phrase can be read as forbidding both. Fix: "with no review of the revert itself" or "no further review of
   the fix".

## Findings outside the task's scope

- **Outside the task's scope (Minor).** `task-cycle/skill/request_template.md:5-6` and `:184-193`: the template
  is also read by the hand-made route of `agent-instructions/README.md` (line 5 says so), and item 8 now asks
  "Fix it in this request, or make a task of it?" and points at `correction.md`, which belongs to
  `implement-task`; `agent-instructions/README.md:59-65` gives that route no way to act on "fix it", and a Minor
  finding is never fixed there before the request. The task does not touch the hand-made route, so I do not
  grade it within the task and do not ask the cycle to fix it; it is worth a line in a later task. Cost if left:
  a hand-made request may put a question to the human that its agent has no rule to run.
- Carried from the author's report, noted: the frozen task quotes the old WAY-161 *Rationale* sentence; nothing
  to fix.

## Declined to judge

- The wording of the English and Polish summaries in the author's report against each row's Polish text: the
  entries are what the rows are compared with, not the summaries. Outside the task.
- Whether a hand-made change (`agent-instructions/README.md`) should fix Minor remarks too: the task does not
  decide it. Outside the task.
- The size of the Minor-only fix in the cost model (32 min and 25 M tokens figures in the task's *Need*):
  motivation, not a requirement. Outside the task.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`.
- `python -B gate/run_tests.py task-cycle` — exit 0, 142 tests OK.
- `python -B gate/run_tests.py agent-instructions` — exit 0, 18 tests OK.
- `git diff 86cc21e..HEAD --check` — no whitespace error (one table row over 100 columns in
  `request_template.md:271`, which is a table row).
- Not run: the full gate (the cycle's own run). No test written or changed by the change; no invariant test
  changed. For prose, no test was needed; the focused tests cover `request_check.py`, whose headings are
  unchanged.

## Reaches beyond the dispatch

- `elements/common/way_of_working.md` "Reading the foundation" and the foundation entries of the touched part
  (`task-cycle`): WAY-136, WAY-161, WAY-162, WAY-163, WAY-229, WAY-287, WAY-289, WAY-297, WAY-263 (grading), each
  entry read whole; `foundations/part_map.md` searched for the part entry (no change needed).
- Searches of `foundations/invariants.md`, `glossary.md`, `environment_facts.md` for "Minor", "unfixed", "findings":
  no hit that touches the change.
- `task-cycle/record_template.md`, `task-cycle/skill/correction.md`, `task-cycle/skill/blocked_finding.md`,
  `agent-instructions/README.md` read to judge untruths (why: the repository search the dispatch asked for).

## Searches not found or unclear

- No guideline files exist for the touched part beyond the foundation (no product guidelines apply to the-way
  prose); nothing to compare against.
- Unclear, not a defect: whether the author of a Minor-only fix may contest a finding is stated only in
  `task-cycle/change/fix.md` and WAY-297, not in WAY-161's rule text; WAY-161's "those a fix left" covers it, so I
  did not grade it.
