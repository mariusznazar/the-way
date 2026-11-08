# Report of correction 1 - the human's remarks on request #85

**Status:** `done`

The remarks, which bind: `remarks.md` beside this file. The human chose "1, 5, 6 + 4 w skillu":
- remove the orchestrator's sentence;
- give the template's full path;
- apply "named below…" in the other skills;
- write "the readiness gate" only in the files of this skill, leaving WAY-118 and the template
  unchanged.

Each remark is made as below.

## Commit

`3f25d61` "Apply the request's proposals 1, 4, 5 and 6 at the human's request". It sits on
`task/define-project-skill-shape`, from its head `a0c56bb`. Not pushed.

| File | Added | Removed |
|---|---|---|
| `project-level/skill/SKILL.md` | 5 | 5 |
| `project-level/skill/delegated_mode.md` | 12 | 14 |
| `project-level/skill/existing_definition.md` | 5 | 6 |
| `project-level/skill/readiness_gate.md` | 5 | 5 |
| `elements/common/skill/SKILL.md` | 2 | 2 |
| `product-guidelines/coding/SKILL.md` | 4 | 3 |
| `product-guidelines/styleguide/SKILL.md` | 4 | 3 |
| `product-guidelines/testing/SKILL.md` | 4 | 3 |
| `project-level/plan/skill/SKILL.md` | 2 | 2 |

No `description`, no Python, no foundation file and no entry point changed. The added and removed
line counts come from rewrapped lines. `check_correction.py 3f25d61` (beside this file) shows that
each of the nine files differs from its parent only by the substitutions listed below, with line
breaks ignored.

## Each remark, as made

### 1. Proposal 1 - the orchestrator's sentence removed

`delegated_mode.md` no longer holds "The project orchestrator may make the initial text edit only
when that full text is already before it and needs no other definition-section or foundation
reading; otherwise it delegates the edit." Its paragraph now begins "A subagent always performs
step 7, including the whole-foundation collision search and all checks." (`delegated_mode.md:15`),
and that sentence stays, as the proposal says. The paragraph was rewrapped to the
100-character width. Its other words are unchanged.

- **What the removal switches off:** a rule the dispatched agent read and never acted on. The
  orchestrator still holds it in `project-level/lead/skill/SKILL.md:206-207` and WAY-156.
- **Condition compared with the base:** the sentence had no condition of its own; it stood under
  the delegated mode's, which is unchanged in `SKILL.md`. No route of the dispatched agent is lost:
  - the agent's acts are editing, step 7, and returning through the conversation, and none of them
    depended on the sentence;
  - the edit reaches the agent by its dispatch, whatever the sentence said.
- **Words:** the dispatched turn carries 31 words fewer.

### 2. Proposal 5 - the template by its path

`SKILL.md:13` and `:45` now name `project-level/definition_template.md`. No other file of the skill
names the template by a file name: the step files say "the template".

- **Switches off:** a reader looking for `definition_template.md` beside the skill, where nine files
  now stand.
- **Condition:** none changes. Step 0 still reads the template in full.
- **Check:** `check_instructions.py` no longer reports the two INFO lines that it gave for the bare
  name, on the base and up to `09b0dd0`.

### 3. Proposal 6 - "each skill named below" in the other skills

I ran `grep -rl "each skill named below" --include=SKILL.md` and, for each candidate, listed the
skills of the-way that the files beside it name and that its `SKILL.md` does not name below the
sentence.

| Skill | Files beside it name a skill its `SKILL.md` does not | Made |
|---|---|---|
| `elements/common/skill/SKILL.md` | yes: `definition_variant.md` names `find-foundation-entries`, `record-decision`, `record-invariant`, `record-glossary-term`, `record-environment-fact`, `update-part-map` | reworded |
| `product-guidelines/coding/SKILL.md` | yes: `research.md` names `critique`, `settle.md` names `settle-technology`, `hand_back.md` names `find-foundation-entries`, `recognize.md` names `update-part-map`, among others | reworded |
| `product-guidelines/styleguide/SKILL.md` | yes: `research.md` names `critique`, `orchestrated_mode.md` names `lead-project`, `hand_back.md` names `find-foundation-entries`, among others | reworded |
| `product-guidelines/testing/SKILL.md` | yes: `research.md` names `critique`, `hand_back.md` names `find-foundation-entries` and `maintain-coding-guidelines`, among others | reworded |
| `project-level/plan/skill/SKILL.md` | yes: `critique_plan.md` names `critique`, `existing_plan.md` and `read.md` name `define-project`, `guideline_tasks.md` names `maintain-coding-guidelines` and `maintain-testing-guidelines` | reworded |
| `task-cycle/plan/SKILL.md` | no: its one file beside it, `too_large.md`, names no skill | left as it is |

In the five reworded files, "each skill named below is the project skill of that name with the
`the-way-` prefix" reads "each skill named below or in the files beside this skill is the project
skill of that name with the `the-way-` prefix". The rest of its paragraph was rewrapped to the
100-character width, and nothing else changed (`check_correction.py`).

- **Switches off:** a reader of the `SKILL.md` alone taking "below" narrowly and calling a skill
  named in a file beside it without the prefix.
- **Condition:** none. The prefix rule widens back to every skill the skill names, as it covered
  when every skill stood in its `SKILL.md`.
- **Meaning:** WAY-127's paragraph keeps its meaning.

### 4. Proposal 4 inside this skill - "the readiness gate"

Every use of "gate" for the readiness gate in the files of `project-level/skill/` now reads "the
readiness gate".

| File | Line | Before | After |
|---|---|---|---|
| `SKILL.md` | 40 | "after the gate goes through the gate again" | "after the readiness gate goes through the readiness gate again" |
| `delegated_mode.md` | 20 | "blocks the gate" | "blocks the readiness gate" |
| `delegated_mode.md` | 24 | "Keep the pending gate" | "Keep the pending readiness gate" |
| `delegated_mode.md` | 27 | "while that gate or" | "while that readiness gate or" |
| `existing_definition.md` | 11 | "changed after the gate" | "changed after the readiness gate" |
| `existing_definition.md` | 15 | "through the gate again" | "through the readiness gate again" |
| `readiness_gate.md` | 23 | "on the way to the gate" | "on the way to the readiness gate" |
| `readiness_gate.md` | 24 | "before the gate" | "before the readiness gate" |

Left as they are, as the remark says:
- the heading "Delegated definition change and gate" (`SKILL.md:26`, `delegated_mode.md:1`; task
  To do 2);
- "gate record" (the template's section; `delegated_mode.md:21`, `first_write.md:9`,
  `readiness_gate.md:8`, `:40`);
- the status `ready for gate` (`technology.md:9`);
- the file name `readiness_gate.md`.

WAY-118, `project-level/definition_template.md` and `foundations/glossary.md` are unchanged, so the
skill's words now differ from WAY-118's "goes through the gate again", as the human accepted.

- **Switches off:** reading any of these uses as the glossary's "gate", the command that runs all
  tests.
- **Condition:** none changes; each sentence refers to the same act at the same step.
- **Check:** `grep -n -i -P "(?<!readiness )(?<!readiness_)\bgate\b(?! record)" project-level/skill/*.md`,
  with `ready for gate` set apart, prints only the two headings. `compare_sentences.py` now also
  confirms that each reworded unit of the base stands in the files once the named substitutions
  are made, and that the two units of the removed sentence stand in none. Shown failing: with
  "blocks the readiness gate" turned back to "blocks the gate", it exited 1. Restored, `cmp`
  identical, it exited 0.

## Reports brought up to date

- **`assessment.md`** is regenerated by `make_assessment.py`:
  - the rows of base lines 6-14, 36-40, 41-45, 47-51, 55-56, 57-63, 64-70, 152-162 and 182-183 name
    the applied proposal;
  - the new places are the lines of `3f25d61` (for example `delegated_mode.md` lines 15-17,
    `existing_definition.md` lines 13-19);
  - section 1 gives the check script's `0 error, 1 warn, 12 info` and says that the INFO lines on
    the bare template name are gone;
  - section 4 marks proposals 1, 4 (inside this skill), 5 and 6 as applied, each under "Applied",
    and proposals 2 and 3 as kept.
- **`word-counts.md`** is regenerated by `make_word_counts.py` after the last change to a counted
  file. Proposal 1's 31 words are now quoted from the base `SKILL.md`. The generator also checks
  that the sentence no longer stands in `delegated_mode.md`.
- **`author_report.md`** keeps the figures of `eeca32c`. Its top now points here and to
  `word-counts.md` for the figures that stand. `fix_report.md` and `return_report.md` stay as
  written for their commits.
- The request's own check, `verify_request.py`, is the orchestrator's, and I did not run or change
  it.

| Route | Skill text before | Total before | Skill text after | Total after |
|---|---|---|---|---|
| 1 | 1937 | 5869 | 1844 (-4.8%) | 5776 (-1.6%) |
| 2 | 1937 | 5366 | 1522 (-21.4%) | 4951 (-7.7%) |
| 3a | 1937 | 6785 | 1662 (-14.2%) | 6510 (-4.1%) |
| 3b | 1937 | 6785 | 2365 (+22.1%) | 7213 (+6.3%) |
| 4 | 1937 | 5366 | 1348 (-30.4%) | 4777 (-11.0%) |
| 5 | 1937 | 5366 | 1414 (-27.0%) | 4843 (-9.7%) |

- `SKILL.md` alone: 572 words.
- `delegated_mode.md`: 314 words.
- `readiness_gate.md`: 569 words.
- All ten files: 2365 words.

## Checks

All on `3f25d61`.

| Command | Exit code |
|---|---|
| `python -B gate/run_tests.py project-level` | 0, 271 tests OK |
| `python -B gate/run_tests.py elements/common` | 0, 109 tests OK |
| `python -B gate/run_tests.py product-guidelines` | 1, "no test found in product-guidelines". The directory holds no `test_*.py` (`git ls-files` finds none), and the runner exits 1 for a directory with no test (WAY-63). The parent `a0c56bb`, in a temporary detached worktree since removed, gives the same exit 1 and message. No test of the files I changed exists to run there. |
| `python -B gate/run_tests.py agent-instructions` | 0, 18 tests OK |
| `python -B elements/common/foundation_check.py .` | 0, "0 errors" |
| `python -B agent-instructions/skill_entry_points.py` | 0, "entry points are current" |
| `python -B instruction-files/check_instructions.py . --file <each of the nine changed files>` | 0, `0 error, 6 warn, 8 info`. The six warnings (root `AGENTS.md` `_zadania\`; `product-guidelines/coding/SKILL.md` and `testing/SKILL.md` naming a product's `.runs/` and `guidelines/` paths) and the two `audit_end.md` INFO lines stand on the parent too, one line earlier where the rewrap added a line. The parent also gives the two INFO lines on the bare `definition_template.md`, which this correction removes. |
| `python -B instruction-files/check_instructions.py . --file <each of the ten files of project-level/skill/>` | 0, `0 error, 1 warn, 12 info` |
| `python -B <reports>/check_correction.py 3f25d61` | 0, 9 files, 0 differ beyond the named substitutions; on `eeca32c`, exit 1 |
| `python -B <reports>/make_word_counts.py`, `make_assessment.py` | 0; 54 rows, 0 errors |
| `python -B <reports>/compare_sentences.py` | 0, 121 units of the base, 19 not word for word, all named; 0 unexpected |
| `python -B <reports>/check_pointers.py` | 0, 10 files, 0 failures |
| `python -B <reports>/verify_counts.py <reports>/word-counts.md <reports>/assessment.md <reports>/correction_report.md` | 0, 263 figures compared, 0 differ; wc -w cross-check on 15 files in two locales |

Not run:
- `gate/run_tests.py task-cycle`: no file of `task-cycle/` changed.
- `installation`: no description and no file the installer names changed.
- The whole gate, which is the orchestrator's.

## Own-work check

- **The requirement most likely missed:** "Change nothing else in those files", and, inside the
  skill, a use of "gate" missed or a fixed name changed. A rewrap by script can drop or move a word
  unseen in a diff of whole paragraphs.
- **The check:**
  - `check_correction.py 3f25d61` compares each changed file with its parent word for word, after
    the named substitutions only.
  - The negative-lookbehind grep above lists every "gate" left in the skill.
  - `compare_sentences.py` checks each reworded unit of the base and the absence of the removed
    one.
- **What it showed:**
  - Nine files changed, 0 differing beyond the substitutions. The same script on `eeca32c`, a
    commit with other changes, exits 1 and names its three files.
  - The grep prints only the two headings the remark keeps.
  - `compare_sentences.py`: 0 unexpected.
  - My first rewrap of `delegated_mode.md` had also rewrapped its untouched first paragraph. I
    restored that paragraph from the parent commit before committing, so only the paragraphs that
    changed are rewrapped.

## Searches not found or unclear

- The remark counts six candidates for proposal 6. The grep finds seven files, the seventh being
  `project-level/skill/SKILL.md` itself, which the fix of finding M-1 had already reworded. Of the
  six, five are reworded and `task-cycle/plan/SKILL.md` is not, for the reason in its row.
- "the readiness gate goes through the readiness gate again" (`SKILL.md:40`) repeats the term, as
  the remark's "write 'the readiness gate'" gives. "goes through it again" would read better, but I
  kept the literal form so that no reader has to resolve the pronoun.
