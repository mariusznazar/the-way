FAIL dcb1a1907f3ad63d9fcef22facb6a4877566a044

# Review of the fix of the merge review's findings (correction 1)

Range `7d00a48..dcb1a19`, one commit (`dcb1a19`). `git rev-parse HEAD` in my worktree:
`dcb1a1907f3ad63d9fcef22facb6a4877566a044`, the head given. Read from a detached worktree of `dcb1a19`,
never from the task's working tree.

Method: `task-cycle/review/SKILL.md` and `task-cycle/review/fix.md` at `dcb1a19`. The findings file
`reports/review-merge-findings.md` bounds this review. It holds my two blocking findings of the
merge review; my Minor finding 3 stays unfixed by design. The author's report
`reports/author-fix-merge-report.md` was read as claims to check.

## The findings of the findings file

### Finding 1 — fixed

The CI rule now defers to WAY-261 in each of the five places:

| Place | What it says now |
|---|---|
| WAY-160, its binding sentence, `foundations/decisions.md:2683-2685` | "treats a red result as a failed gate, handled as the cycle's gate gives — a fix and its review, save a check outside the task's scope that passes when run again, which WAY-261 governs —" |
| WAY-160, the *complies* example of its *Verification*, `foundations/decisions.md:2696-2697` | "(a check outside the task's scope that passes when run again goes as WAY-261 gives)" |
| Step 12, `task-cycle/skill/SKILL.md:596-601` | "handled as step 10 gives … save a check outside the task's scope that passes when run again, which step 10 leaves to WAY-261: the cycle goes on, and the description names that check and the task that fixes it, or proposes that task" |
| `task-cycle/skill/correction.md:59-61` | the same exception, "which WAY-261 governs" |
| `agent-instructions/README.md:107-109` | "save a check outside the task's scope that passes when run again, which the description names with the task that fixes it (WAY-261)" |

How they read against the rules around them:

- **WAY-261.** Each place uses WAY-261's own words for the case: "a check outside the task's scope
  that passes when run again"; the cycle goes on; the request names the check and the task, or
  proposes the task. Nothing in them is wider than WAY-261 or adds to it.
- **Step 10.** Step 10 carries the same exception (`SKILL.md:490-494`), and step 12 now points to
  step 10 with "handled as step 10 gives".
- **WAY-243.** No place asks for a rerun to make the result green.
- **WAY-161.** No place has an out-of-scope test fixed in this request.
- **The violated example of WAY-160.** "a red CI result is left for the human to find"
  (`decisions.md:2705-2706`) still holds: under the exception the description names the check, so
  the result is not left for the human to find.

I searched for any other place that still says a red result is always fixed:
`git grep -n -i -E "red (CI )?result|red run|failed gate|a red result"` over `task-cycle/`,
`agent-instructions/`, `installation/` and `foundations/decisions.md`. Besides the five places it
finds:
- the gate wording of step 10, `return_step.md` and the WAY-160 rationale, none of which says that a
  red result is always fixed;
- `installation/README.md:142`, "a red result shows before the merge", which is about a product's
  CI and states no consequence.

So nothing in the merged tree now says that a red CI result is always fixed.

### Finding 2 — remains (the route the fix took records a rule that nobody set and that the task set the opposite of)

The fix leaves `foundations/part_map.md` unchanged. It adds the invariant
`installation-instruction-files-dependency` (`foundations/invariants.md:428-436`): "The part
`installation` does not depend on `instruction-files`.", *Method* `review`, *Derives from* WAY-225 ·
WAY-51, `Violated: yes`.

The handoff asks me to judge this route and to say so with evidence if I hold it wrong. I hold it
wrong, for these reasons.

1. **The invariant states a rule that no task, decision or human set, and the task set the
   opposite.**
   - WAY-11 (`foundations/decisions.md:5397-5398`): the return step "writes an invariant only for a
     rule the task, a decision or a human sets, never for code behaviour merely because no
     invariant covers it". Its rationale: "An invariant written for behaviour no task, decision or
     human sets binds a detail nobody chose".
   - Here a human did choose, and chose the reach:
     - The task's requirement 3 (`.runs/task-cycles/ci-on-merge-requests/task.md:30`) asks that the
       installer's block in a product's `AGENTS.md` say that the one command also runs
       `check_instructions.py`.
     - The question at `task.md:66-67` was answered "Tak" (yes), and that answer became settlement 5
       (`task.md:120`, "wybór Mariusza", that is, the human's choice): "Jedno polecenie testów
       produktu uruchamia też `check_instructions.py`" (the product's one test command also runs
       `check_instructions.py`).
   - So the reach of `installation` to `instruction-files` is the rule the human set for this task.
     The invariant says the opposite rule binds, and WAY-51 makes that binding:
     - the invariant's *Violated* mark is to be cleared by "the change in which it starts to pass",
       which means a later change that removes the guidance the human asked for;
     - meanwhile "the review of each change to the files of the parts the invariant names keeps a
       cleaned file or a new one from breaking it again" (WAY-51, `decisions.md`, index line). Every
       later review of `installation/` is then bound to keep that part from reaching
       `instruction-files` further.
2. **The route WAY-225 gives is for a dependency the human accepts as it stands, not for one the
   task means.**
   - The part-map template (`elements/part-map/template.md:113-119`): "A dependency of a part that
     the code holds and *Depends on* does not allow goes to the human. Where the human accepts it as
     it stands, it is written as an invariant … that reads `Violated: yes`".
   - The skill (`elements/part-map/skill/SKILL.md:38-42`) gives the same: "the difference goes to
     the human in step 4; a dependency of a part the human accepts as it stands is written … marked
     violated".
   - "Accepts it as it stands" is debt the human tolerates against a rule that stays. It is not a
     dependency the human asked for.
   - For a dependency the change means, the same template gives the other route at line 25: "A
     change of the code that changes what a part answers for, which files are its or what it may
     depend on, … rewrites the entry in the same change (WAY-11)".
   - WAY-225's "never by rewriting the allowed dependencies of a part to fit the code" forbids
     copying into the map what the code happens to reach for. It does not forbid writing the
     dependency that a task and the human's settlement set, together with the code that uses it.
3. **The invariant opens the import check for a reach that is no import.**
   - `elements/part-map/test_cross_part_imports.py:141-157` (`marked_dependencies`) reads every
     invariant of this form marked `Violated: yes` as an allowed pair.
   - From `dcb1a19` on, any Python import from a file of `installation/` into `instruction-files/`
     passes `cross-part-imports`, where before the fix it failed.
   - The template allows that pass only "where the dependency is an import" (`template.md:117`).
     The reach recorded here is a path in text and a test's `git cat-file` (`install.py:201`,
     `test_install.py:145-146`, `:161-168`).
   - So the entry widens the check for a kind of reach nobody uses. The author's report says the
     check "is neither relaxed nor changed". Its code is unchanged, but what it lets pass is wider.
4. **The method departs from the form the template gives for this kind of invariant.**
   - `template.md:115` says such an invariant has "its test standing as an expected failure until
     the code meets it".
   - The entry reads *Method* `review` and has no test. The author's reason (no cheap test checks
     "any reach") is fair under `elements/invariants/template.md:46-48`. But it confirms that this
     template route was made for imports, not for the reach this task records.

Grade: **Important, within the task.**
- The foundation the request merges would hold an invariant that contradicts the task's settlement 5
  and WAY-11's limit on what an invariant may state.
- It would mark as violated a rule nobody set, and so bind later reviews of `installation/` and a
  later task to undo what the human asked for.
- Under fix.md, a finding the fix tried but did not remove remains. The defect my finding named is
  still there: the part map does not allow a reach the task meant. And the fix adds a recorded rule
  against it.

Repair I recommend:
- remove the invariant;
- add `instruction-files` to `installation`'s *Depends on* (`foundations/part_map.md:192-193`) as
  the change's own part-map edit, citing settlement 5 as the human's setting (template line 25,
  WAY-11);
- name the changed part-map entry in the request's *Foundation entries*, so the human sees the widened
  dependency when merging.

If the orchestrator holds that only the human can widen *Depends on* even with settlement 5, the
skill's step 4 route is a question to the human, put in the request with both answers:
- (a) allow the dependency in the map;
- (b) accept it as debt with this invariant.

That is not a violated invariant chosen by the cycle.

Rejected alternative: keeping the invariant and only pointing to it in the request. The human would
then be asked to accept, by merging, a rule against his own settlement, with the import allowance as
a side effect.

## New findings in the fix diff

### Minor

**A. Three edited lines run past the width of the paragraphs around them.**
- `agent-instructions/README.md:109` is 132 characters.
- `task-cycle/skill/SKILL.md:601` is about 135.
- `foundations/decisions.md:2685-2686` leaves a short line "cycle leaves blocked for unfinished".

The paragraphs were not rewrapped after the insertion. The files already hold some lines over 100
characters (for example `SKILL.md:580`, `correction.md:29`), so this is cosmetic, with no effect on
any reader. It blocks nothing.

## Declined to judge

- Whether, under WAY-261's exception, the cycle should rerun a CI job to learn that a check "passes
  when run again". WAY-243 already allows a rerun to diagnose and forbids one to make a run pass.
  The fix adds no rule here, and the question is one of WAY-261 and WAY-243 themselves, outside
  this fix.
- That a request handed over under the exception has a red required check, which the owner's bypass
  merges. This is a consequence of WAY-16 and WAY-261 as both stand (the bypass is in WAY-16), not
  of this fix.
- My Minor finding 3 of the merge review: unfixed by design, for the request's list.

## Checks

| Check | Command (from the worktree of `dcb1a19`) | Exit code / result |
|---|---|---|
| Head | `git rev-parse HEAD` | 0; `dcb1a1907f3ad63d9fcef22facb6a4877566a044` |
| Range | `git log --oneline 7d00a48..dcb1a19`; `git diff --stat 7d00a48..dcb1a19` | 0; one commit, the five files the handoff names |
| Search for a red result fixed without the exception | `git grep -n -i -E "red (CI )?result\|red run\|failed gate\|a red result"` over `task-cycle/`, `agent-instructions/`, `installation/`, `foundations/decisions.md` | 0; only the five corrected places and texts that state no fix |
| How the import check reads the entry | read of `elements/part-map/test_cross_part_imports.py:141-157` | `marked_dependencies` adds (`installation`, `instruction-files`) to the allowed pairs |
| Foundation check | `python -B elements/common/foundation_check.py` (without `--skip-test-citations`) | 0; `0 errors` |
| Tests | `python -B gate/run_tests.py elements/part-map` | 0; 39 tests, OK |
| Tests | `python -B gate/run_tests.py elements/common` | 0; 235 tests, OK |
| Tests | `python -B gate/run_tests.py task-cycle` | 0; 483 tests, OK |
| Tests | `python -B gate/run_tests.py agent-instructions` | 0; 25 tests, OK |
| Line widths of the edited files | a scratch `python -B -c` listing lines over 100 characters | 0; the lines named in Minor A |

The full gate was not run, as the handoff and the method give. Passing tests do not touch finding 2,
which is about what the foundation states, not what a test checks.

## Reaches beyond the dispatch

- WAY-11 whole (`foundations/decisions.md:5386-5431`): the author did not read it, and it decides
  finding 2.
- `elements/part-map/template.md:20-26` and `:88-119`, and `elements/part-map/skill/SKILL.md:30-42`:
  the two routes for a dependency.
- `elements/invariants/template.md:44-70` and `:157-165`: *Method* and *Violated*.
- `elements/part-map/test_cross_part_imports.py:25-70` and `:141-157`: how the check reads the entry.
- `.runs/task-cycles/ci-on-merge-requests/task.md:28-31`, `:64-68` and `:118-121`: the task's
  requirement 3, the human's answer and settlement 5, to see who set the reach.
- `.runs/task-cycles/ci-on-merge-requests/cycle.md:21` (a grep hit): the settlements as the cycle
  recorded them.

## Selection

The decisions bearing on the fix, opened whole: WAY-11, WAY-160 and WAY-261. I already had WAY-225
whole from the merge review, and it is unchanged since `3eacbc1`. WAY-51 and WAY-243 were read in
the index lines and passages cited above. WAY-161 was read through its binding effect as quoted in
the method and in `SKILL.md`. I made no new index: the fix writes no decision outside WAY-160, and
the decisions it reaches are the ones named here.

## Working copies

- A detached worktree of `dcb1a19` at
  `.runs/review-fix-merge/wt`: removed with
  `git worktree remove --force`, then `git worktree prune`.
- The fix diff and the check outputs in
  `.runs/review-fix-merge/`: removed.
- Nothing was kept in `reports/`. No remainder (see the return).

## Unread material

- WAY-51 and WAY-243 were not opened whole. I read their index lines (WAY-51) and the passages that
  `SKILL.md` step 10 and the templates quote.
- WAY-161 was not opened whole. I read it as `SKILL.md` "The end of a code review" and the method
  apply it.
- `task.md` was read only at the lines named above.

## Searches not found or unclear

- Whether the-way intends the WAY-225 route ("accepts it as it stands", a violated invariant) to
  apply to a reach that the human set in the task's settlements. The template and the skill speak
  only of a dependency the human accepts as it stands, and WAY-11 limits invariants to rules someone
  set. I found no text that sends an intended dependency down that route. Hence finding 2.
