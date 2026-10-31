PASS b9b93afcb9a68a88f5404ed6eeed20c58270c4c9

# Review of the whole change, task `base-checks-place`

Range `00c0a747272a9a179b7a855f256daff985ea2ee1..b9b93af`: one commit, one file,
`task-cycle/skill/SKILL.md`, +5 -3. `git rev-parse HEAD` is the head given. One author, no plan, no
slices; this review is the only one the change gets. No blocking finding.

## Findings

Critical: none. Important: none.

### Minor

1. `task-cycle/skill/SKILL.md:113` — "Run those checks on the base alone". Mandated word for word by
   the task's *To do* item 1, so it is named here as the task's wording, not the author's.
   "Those checks" points back at "the checks already failing on it", and read literally that is a
   set nobody knows until the run this sentence orders has ended: what is run is the product's
   checks, and what is recorded is those that fail. The orchestrator a sentence earlier is already
   told to record failures, and the meaning is plain from the task's *Need*, so no wrong run
   follows; this is why it is Minor. The same phrase in step 4's last sentence, "those checks already
   stand", is correct, since there it means the recorded result.

### Out of scope

None beyond the lines of *Declined to judge*.

## Against the task

- *To do* item 1: met. The sentence in the head, whitespace collapsed, equals the sentence of the
  task exactly, and it stands right after "Record the base commit and the checks already failing
  on it". The head's text equals the base's text with only the sentence inserted and ", and keep a
  frozen copy" split into a sentence of its own, as the orchestrator's choice 2 gave. Nothing else
  in the file moved; the rewrap keeps lines 113-117 within 100 columns and the file stays LF.
- *Questions to settle*: line 68 stays unchanged and no exception arises, as the answer gives; the
  checkout stands in the worktree's ignored `.runs/`, deleted after the run, as step 2's clone is.
- *Questions carried to cycle*, `task-cycle/record_template.md:116`: the orchestrator's answer holds.
  The template's *Verification* table at line 113 has the column "Actor, commit and environment",
  which takes the commit and the place of the run, and its line 116 says nothing the new sentence
  contradicts. No second account was added.
- *Settlements to record*: none, and the commit writes no foundation entry. *Human actions*: none.
  *Out of scope*: nothing about two full runs at once entered the change.
- Nothing added that nobody asked for.

## Against the foundation

- Parts touched: `task-cycle` only. Read whole: the 73 decisions whose *Scope* names `task-cycle` or
  the task's *Decisions in play* names, and the 13 invariants whose *Part* names `task-cycle` or
  `every`.
- WAY-256: the sentence is one instruction of one step and stands in `SKILL.md`, where a pointer
  would stand.
- WAY-160: the run is on the base, by the agent step 4 addresses; no handoff or other agent gains
  a run of the gate, and the run on the finished tree is unchanged.
- WAY-140: the checkout is inside the task's worktree and nothing outside the repository changes.
- WAY-34 and step 2: step 2 records the base and its failing checks "as step 4 gives", so the new
  sentence reaches a task that moves the pin, and "a tracked file" covers the commit that moves the
  pin, which comes after that measurement in step 2's order.
- Invariants of `every` whose method is review, compared with the diff: no foundation file, new
  file, link, script, CI configuration or `@` is added. `return-step-record` is not judged here,
  since the return step comes after this review. `skill-entry-points` and `derived-file-content`: the name and description are unchanged, so no
  entry point needs regenerating, and the tests of `agent-instructions` pass.
- No invariant test changed. No foundation entry states a rule on the base run for the change to
  depart from.

## The claim most likely false: the checkout under `.runs/` stays out of the run in the worktree

Checked, since the second way lets a checkout sit in the worktree while the author works there.

- `gate/run_tests.py:54` finds tests with `git ls-files`, and `.gitignore:2` ignores `.runs/`
  (`git check-ignore -v .runs/base-checks` confirms it).
- `instruction-files/check_instructions.py:50` skips `.runs`; `gate/test_skills_reach_the_way_sessions.py`
  discovers with `--exclude-standard`; `agent-instructions/test_skill_entry_points.py:121-122`
  already covers an ignored `.runs/copy/SKILL.md`.
- `project-level/plan_state.py:337-348` walks only `.runs/task-cycles/<task>`, so a checkout beside
  that directory is not read.
- The other file walkers in tracked code work in temporary products or a home directory, not in
  the repository root.

## Tests and the author's own-work check

The change is instruction text and adds no test, which is right: none of the task's requirement is
behaviour a test can hold, and no test reads this sentence. The author's own-work check names the
requirement most likely missed as the placement of the sentence, with file wrapping and line
endings, and it fits: that is the one item of *To do*, and comparing the diff would catch a
misplaced or altered sentence. My own comparison above confirms what it reports.

## Declined to judge

- What happens when the deletion of the checkout fails, and how it is deleted where the checkout is
  a `git worktree` and not a clone: the task leaves the open question on failed deletion to its
  separate task on temporary files.
- A second way run in a product whose checkout lacks `node_modules` or `.the-way`, where checks
  could fail for that reason and be recorded as failing on the base: the task's *Context* weighs
  this and expects the first way there, and any warning would go past the sentence the task fixes
  word for word.
- A ban on two full test runs at once: named in the task's *Out of scope*.

## Checks

| Command or method | Exit code or result |
|---|---|
| `git diff 00c0a747272a9a179b7a855f256daff985ea2ee1..b9b93af`, `git log` of the range, `git rev-parse HEAD` | 0; head matches |
| `python -B gate/run_tests.py task-cycle` | 0; 42 tests OK |
| `python -B gate/run_tests.py agent-instructions` | 0; 18 tests OK |
| `python -B elements/common/foundation_check.py .` | 0; 0 errors |
| `python -B instruction-files/check_instructions.py .` | 0; 0 errors, 1 warning at `AGENTS.md:21`, the private `_zadania\` path, not in this change |
| Scratch comparison in Python of the task's sentence and of base plus sentence against the head, whitespace collapsed | sentence found in task and head; head equals base plus the sentence and the split; no CR |
| `git ls-files --eol task-cycle/skill/SKILL.md` | `i/lf w/lf` |
| Line widths of the file by `awk` | only lines 3, 71 and 389 pass 100 columns, none of them changed |
| `git status --short` after the runs | empty; worktree unchanged |

Not run: the full gate, which is the orchestrator's (WAY-160), and for which the handoff says so.

## Reaches beyond the dispatch

- `git show a2c1164:docs/task-cycles/rejected-from-refinement/cycle.md`, lines 41-47 and 135: to
  check the task's cited source. It says what the task says: the base run shared the worktree with
  the author and was discarded.
- `project-level/plan_state.py:330-364`, `gate/test_skills_reach_the_way_sessions.py:30-59`,
  `gate/run_tests.py:54` and `instruction-files/check_instructions.py:50`: to test whether a checkout
  under `.runs/` reaches another run.
- `elements/common/way_of_working.md`, `product-guidelines/reading.md`: named by the method.

## Searches not found or unclear

- Guidelines of the-way itself: no file under `guidelines/`; the change writes no code, test or
  interface, so nothing is missing for it.
- Otherwise none.
