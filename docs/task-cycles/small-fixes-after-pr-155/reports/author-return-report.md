# Author report — the return step

**Status:** done. **Commits:** none — nothing in the foundation or the code no longer matches. Head stays
`77ddfbf7`; base `80006b25`. Nothing pushed.

## Return step

### The foundation compared with the code of the change

Compared with the code at `77ddfbf7` (`git diff 80006b25..77ddfbf7`):

- **The entry the change writes — the rule `### Turning off git's automatic maintenance` of
  `guidelines/testing.md`** (row 1). It says a git test sets the maintenance off in the configuration of each
  repository it builds, the bare remote one too, not in environment variables alone, because git passes none
  of them to the side that takes a `push` to a local repository. `Fixture` in
  `task-cycle/test_remove_merged_worktrees.py` now sets `maintenance.auto false` and `gc.auto 0` in
  `origin.git` and in `main`; the rule's sentence and its *Good* line match the code. The rule's phrase
  "git passes none of them" reads "them" as the variables that turn maintenance off, as the reviewer noted
  (review of the whole change, m1); the comments of the test file say it as git does (the variables that
  carry configuration). Matches; no change.
- **The description at the head of `task-cycle/gate_times.py`** (the source of expected values, WAY-394):
  the sentence on memory says the script keeps, over the whole output, the last 100 different places of lines
  that hold `== ` after text, each place once; the code keeps `self.marks` as `deque(maxlen=SUMMARIES_KEPT)`
  with the dedup condition before `append`, and `self.marks.clear()` is gone. Matches. The four new tests name
  that sentence at their expected values.
- **WAY-03** (names a test that alters an invariant test or holds a decision's sentence): the changed test
  `ApplyTest.test_a_dry_run_removes_nothing_and_apply_removes_only_what_is_marked` cites
  `repository-changer-acts-only-when-told`, and its assertions did not change; no `decision:` or `invariant:`
  line was added, dropped or altered in either test file (`git diff` searched for those two words: no
  hit). The request names the one test above.
- **WAY-394:** each new test takes its value from the description of the script, worked out by hand, named in
  a comment at the value. Matches.
- **WAY-402:** `### Mutation testing` of `guidelines/testing.md` still reads `none — WAY-402`; the mutants were
  a check made once by hand in a copy, no tool added. Matches.
- **WAY-350, WAY-390 and the invariants `command-runner-passes-exit-code` and
  `gate-times-refuses-impossible-entry`** (found by the search of `gate_times`): they speak of the exit code
  and the registry of `gate_times.py`, which the change does not touch; their tests are unchanged. Matches.
  The invariant `repository-changer-acts-only-when-told` (the sentence: without `--apply`, the script changes
  no tracked file and no working directory) is not changed by a fixture that only turns maintenance off.
- **The part map**, entry `task-cycle` in `foundations/part_map.md`: its files `task-cycle/**` and its trust
  boundary `task-cycle/gate_times.py` are as before; no file was added or moved. The part `agent-instructions`
  names none of the files changed (a search of `agent-instructions/`, `instruction-files/` and
  `elements/part-map/` for `gate_times`, `test_remove_merged`, `test_gate_times` and `guidelines/testing.md`
  gave no hit).

### The search of the foundation by the names and words the code adds

One search, in the whole worktree outside `.runs/`, for `maintenance.auto`, `gc.auto`, `self.marks`,
`failing_dir`, `automatic maintenance`, `different places`, `marks.clear`, `last 100 lines` and `places of
the last`: hits only in the code of the change, in `guidelines/testing.md` (the new rule) and in two
unrelated places (`elements/common/migrate_foundation.py:69`, "different places" in a comment on two
scripts; `foundations/decisions.md:2333`, "different places of a sentence" in the text on a word with two
meanings). Neither speaks of what the change did; no entry holds the maintenance setting, the marks of
`gate_times.py` or the old wording of the description. `separator` and `then` are parameters of a test helper
and name nothing the foundation holds. Nothing no longer matches.

### Decisions, invariants, environment facts, glossary terms, part-map changes, projected entries

- **Decisions written or changed:** none. A choice that binds after the merge (WAY-36): none — the one
  binding choice, the rule of row 1, is a rule of the guidelines with *Decision* `none`, as the row and the
  template of guidelines give (a rule that only says how to write tests stands alone with its reason in one
  sentence); the task's answer under *Questions to settle* is the code change of row 2.
- **Invariants written or changed:** none (an invariant only for a rule the task, a decision or the human
  sets; none asks for one here).
- **Environment facts written:** none. The fact the rule rests on, that git runs `git-receive-pack` after
  `unset GIT_CONFIG_COUNT GIT_CONFIG_PARAMETERS GIT_PREFIX`, was shown by the own `GIT_TRACE` of this
  product's author on git 2.55.0.windows.3 on 2026-11-21. The template of environment facts writes no fact
  for a measurement the product's own people made whose record a reader of the repository cannot open, and a
  fact stands only while an invariant's *Rests on* or a decision's *Based on* names it; the rule has
  *Decision* `none` and *Invariant* `none`, so nothing would name it. I found no published page of git that
  says it, and did not look further, since a fact needs a passage word for word.
- **Glossary terms written:** none. The rule says "git test", which `foundations/glossary.md:211` defines as a
  test that works on git repositories it builds in a temporary directory; the rule uses it in that meaning.
- **Part-map changes:** none.
- **Projected entries:** none (the task is independent and carries none).

### Where each row of *Settlements to record* went

- **Row 1** (a git test that turns off the maintenance sets it in each repository's configuration, the bare
  remote one too): `guidelines/testing.md`, the rule `### Turning off git's automatic maintenance`, written
  in the foundation step (`ac7f22a0`), whose code side is `Fixture.__init__` in
  `task-cycle/test_remove_merged_worktrees.py` (`ac7f22a0`, `77ddfbf7`). No shared helper for building test
  repositories was founded: each test file of the-way keeps its own `git` function, and this task changes one
  fixture.
- **Row 2** (no line that changes no result in `gate_times.py`; the description says the last 100 different
  places over the whole output): the code of `task-cycle/gate_times.py` (`73909788`); no entry.

## Check

`python -B elements/common/foundation_check.py` — exit 0, `0 errors`. (Run once, though no foundation entry
changed in this step, to show the foundation as it stands at `77ddfbf7`.)

## Own-work check

- The requirement most likely unmet: "correct in the same change whatever no longer matches" — a
  foundation or guideline sentence that still describes the old marks (cleared at each summary line) or the
  old fixture (variables of `ENVIRONMENT` alone). Check: the search above for `marks.clear`, `places of the
  last`, `last 100 lines`, `maintenance.auto`, `gc.auto` and `automatic maintenance` in the whole worktree
  outside `.runs/`. It showed only the new text; no old statement stands.
- Weakest point: the choice to write no environment fact rests on my reading of "a fact stands only while a
  decision's *Based on* or an invariant's *Rests on* names it" and on "a measurement the product's own people
  made whose record a reader cannot open is written as no fact". If the human wants git's behaviour recorded as
  a fact, it needs a source a reader can open (a passage of git's documentation or code at a fixed commit),
  which I did not have.

## Working copies

None made in this step; `.runs/author/` does not exist (removed after the fix, as that report says).
Remainder: none.

## Unread material

none — read whole: `task-cycle/skill/return_step.md`, `task-cycle/skill/foundation_step.md` (in the first
step), the handoff, `elements/environment-facts/skill/SKILL.md`, `decide_entry.md` and `template.md`,
WAY-03, WAY-350, WAY-390, WAY-394 and WAY-402 whole, the three invariants named, and the entry `task-cycle` of
the part map. Not read: `elements/environment-facts/skill/read.md`, `draft.md`, `write.md`, `projected.md`
(no fact was written), and the skills of the other elements (no entry of theirs was written).

## Searches not found or unclear

none
