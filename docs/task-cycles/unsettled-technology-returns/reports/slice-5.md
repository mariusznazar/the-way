# Slice 5 report

**Status:** `done`

Slice: "The orchestrator stops the cycle on a reserved choice". Variant: a slice. Base `dc13d6a`.

## Files changed and commits

Commit `db126f6` (`docs: stop the cycle on a reserved technology choice`), on
`task/unsettled-technology-returns`, not pushed.

| File | Added | Removed |
|---|---|---|
| `task-cycle/skill/reserved_return.md` (new) | 92 | 0 |
| `task-cycle/skill/SKILL.md` | 35 | 24 |
| `task-cycle/skill/correction.md` | 20 | 7 |
| `task-cycle/skill/planning.md` | 2 | 1 |
| `task-cycle/record_template.md` | 5 | 3 |

The frontmatter of `SKILL.md` is unchanged. Line endings stay `i/lf w/lf` by `git ls-files --eol`,
the new file included. No script changed, so no test comes first (the plan's *Checks*).

## Checks

Each run with no pipe, each exit code read from `$LASTEXITCODE`, on the working tree that became
`db126f6` (the tree was unchanged after them, apart from `git add`).

| Command | Exit code | Result |
|---|---|---|
| `python -B gate/run_tests.py task-cycle` | 0 | 42 tests OK |
| `python -B instruction-files/check_instructions.py . --file task-cycle/skill/reserved_return.md` | 0 | 0 errors, 1 warn, 5 info: the warn is `AGENTS.md:21` `_zadania\` (not of this slice); an info on `reserved_return.md:75` says `stages.md` is a relative name, as it is in `SKILL.md` |
| `git grep -l -F "reserved_return.md" -- task-cycle/skill/SKILL.md` | 0 | lists that file |
| `git grep -n -F "smallest reversible" -- task-cycle` | 0 | 4 lines, read below |
| `python -B agent-instructions/skill_entry_points.py` | 0 | "entry points are current" (extra; confirms no entry point changes) |

`smallest reversible`, each line read:

- `task-cycle/skill/SKILL.md:191` — the sentence reads "otherwise, except for a reserved choice, the
  smallest reversible reading": excepted (the exception stands on line 190).
- `task-cycle/skill/SKILL.md:224` — "otherwise, except for a reserved choice, choose the smallest
  reversible reading": excepted (line 223).
- `task-cycle/spec/design.md:15` — excepted on line 16, by Slice 4.
- `task-cycle/spec/design.md:22` — itself says no such reading settles a reserved choice.

`task-cycle/skill/reserved_return.md:15-16` also says no smallest reversible reading settles one;
the phrase breaks across two lines, so the search does not list it.

Not run: the gate, as the handoff gives (WAY-160). No failing run occurred.

## Own-work check

Requirement most likely unmet: "no stage of the cycle settles a reserved choice" — every way a
reserved choice reaches the orchestrator has to pass the check before an answer, and the one way
that starts with work on the branch, the correction, has to tell the case before it merges anything.

Checks, all exit 0:

- `git grep -n -F "reserved_return.md" -- task-cycle` — four pointers: `SKILL.md:98` (step 4),
  `SKILL.md:218` (the paragraph under "Design and execution choice": agent's `reserved`, the task at
  step 4, a question, a `returned` report), `SKILL.md:421` (step 13), `planning.md:12` (the planner).
- `git grep -n -E "Reserved choice|First merge" -- task-cycle/skill/correction.md` — the field is
  read at line 6, the merge stands at line 20.
- A search for `` `returned` `` in `task-cycle` — every status list that names `returned` now names
  `reserved` too: `change/SKILL.md:129`, `plan/SKILL.md:206`, `skill/SKILL.md:183-186`.

What it showed: all the entries lead to the check, and the correction's case comes first. A text
that instructs agents is tested by what an agent does with it (`make-change`, section 2); no agent
ran it, so whether one recognises the moment stays unproved. The spec names that as its accepted
weak point, with the review as second chance.

## Reaches beyond the dispatch

- `.runs/task-cycles/unsettled-technology-returns/spec.md:404-450`, decision 5 — to word "what
  happens next" and the state after closing in line with it.
- `.runs/task-cycles/unsettled-technology-returns/reports/slice-4.md` — to match the status wording.
- `task-cycle/spec/design.md:10-28` and `task-cycle/plan/SKILL.md:55-73` — to match the pointers.
- `C:/Storage/The Brain/The Brain/.ai/rules/git.md` — before the commit, as the session's global
  instructions require.
- Search of `*.py` for names of the files changed — no test reads them; only a literal fixture
  `project-level/test_plan_state_invariant.py:156` holds the heading *Spec and execution route*,
  and the heading stays.

## Searches not found or unclear

- `task-cycle/record_template.md:89-90` (the paragraph under *Events*) and step 12 say the removal of
  the record is committed "immediately after" the copy. The request now opens between the two for a
  reserved choice. The plan names only two edits of the template, so the sentence stands;
  `reserved_return.md` states the departure itself.
- Whether "that correction's commits" takes in the correction's merge of the target branch: neither
  the spec nor WAY-267 says. Settled by choice 1 below.
- WAY-267's *Verification* and the spec say the request names the spec, the plan and the reviews as
  not run. A stop met after a reviewed spec or after a slice's review has run those stages. Settled
  by choice 2 below.

## Choices made

1. **The reset after a correction goes to the head the request held when the correction began**, the
   correction's merge of the target branch included. Rejected: keep the merge and take back only the
   agent's commits. Then the tree differs from the one the gate checked and the gate has to run.
   Cost if wrong: the merge is made again at the next correction, which starts with it anyway.
2. **The request names as not run each stage above that did not run**, the gate among them, rather
   than the whole list as a fixed text. Rejected: the fixed list, false for a stop after a spec or a
   slice's review. Cost if wrong: none for a stop before them; the list reads as WAY-267's.
3. **A remark that no longer needs the choice sets *Reserved choice* back to `none`**
   (`correction.md`). The spec does not say so, but a field left naming a choice would have a later
   remark read as blocked. Rejected: leave the field. Cost if wrong: one line of the record.
4. **The order's copy of the record cannot hold the request's URL**, since the request opens on that
   commit: step 2 of `reserved_return.md` has *Request URL and status* read
   `blocked draft, opened on this commit`. Rejected: a third commit carrying the URL, which breaks
   the pair. Cost if wrong: the record lacks a link the request already has the other way round.
5. **A review's finding and the orchestrator's check** (`reserved_return.md`, end of "Check the
   choice"): where a fix's agent returns `reserved` and the orchestrator finds no reserved choice, it
   answers the agent and the finding stands for the review of the fix, so the check overrules no
   finding (WAY-161, WAY-162). Rejected: the check clears the finding, which would let the
   orchestrator rule on one. Cost if wrong: one more review round, inside the one WAY-162 allows.
6. **Step 13's *Questions* names a reserved choice beside what the foundation step allows.** The plan
   says only that step 13 points to the file; without this the sentence "only those the foundation
   step allows" would forbid what the file requires. Cost if wrong: none.
7. **Step 12 stays unchanged.** Its first sentence routes only a request a blocking finding blocks.
   The plan's list of edits does not name step 12, and the paragraph under "Design and execution
   choice" and step 13 route this case. Rejected: a clause there. Cost if wrong: an orchestrator
   reading step 12 alone meets no pointer, though it reaches step 12 only by not stopping.
8. **Paths in `reserved_return.md`** name the rule "of the pinned the-way", as `SKILL.md` names its
   files. Slice 4's pointers name both forms because stage agents read them in both places.

No adaptation of the plan to the code; no invariant test changed. Every foundation entry read holds
against the text; nothing to return on WAY-135, WAY-162, WAY-227, WAY-266, WAY-267 or the term
reserved choice.
