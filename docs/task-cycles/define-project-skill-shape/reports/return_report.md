# Report of the return step

**Status:** `done with concerns`. The concern: several uses of "the gate" that the change moved but
did not write still mean the readiness gate, while the glossary's entry "gate" means the test
command. The same words stand in WAY-118 and the template, so the change carries them as they are.
See the glossary row below. No answer is needed before the request.

Method: `task-cycle/skill/return_step.md` and `foundation_step.md`, read whole, applied to the
reviewed head `eeca32c` and the files as they stand.

## Commit

`09b0dd0` "Name define-project's step 7 file readiness_gate.md, since the glossary's gate is the
test command".

| File | Added | Removed |
|---|---|---|
| `project-level/skill/gate.md` renamed to `project-level/skill/readiness_gate.md` | 0 | 0 |
| `project-level/skill/SKILL.md` (steps 6 and 7, the two pointers) | 4 | 4 |
| `project-level/skill/existing_definition.md` (the jump to step 7) | 1 | 1 |

Only `project-level/skill/` changed. I made the commit first with the rename alone (my `git add`
named the old path, which no longer existed, so it staged nothing else). I amended it at once,
before any check or review, to add the two pointer edits, so that no commit holds a broken pointer.
Neither form was pushed.

What the rename switches off: a reader taking `gate.md` for a file about the-way's `gate`, the test
runner of `gate/run_tests.py` that the glossary names "gate". No condition changed. Each pointer
names the same file at the same step with the same condition, and only the name differs. The word
counts are unchanged, since a file name is one token.

## The comparison

Every entry is compared with the ten files of `project-level/skill/` at `09b0dd0`.

### Decisions

| Entry | What the files hold | Matches |
|---|---|---|
| WAY-256 | `SKILL.md`: the picture of the whole, "Rules that hold across the steps", pointers. Step 0's two one-instruction items stay in `SKILL.md`. Each step's procedure is in its file. `readiness_gate.md`, consulted at steps 6 and 7, is named by both, and step 7 reads it "unless step 6 had you read it". | yes |
| WAY-265 | `delegated_mode.md`, pointed to from `readiness_gate.md`, is named in `SKILL.md` at step 7 with the condition "in a turn dispatched through a refinement conversation path". `existing_definition.md` points only to step files. | yes |
| WAY-257 | concerns the skill of `instruction-files`; the assessment's rows each show *Needed* and *Recognised*. | yes |
| WAY-106 | `SKILL.md:23-24`, unchanged. | yes |
| WAY-112 | Goal confirmed before the first write (`idea.md`, `first_write.md`). Each answer and its status line come before the next question (`SKILL.md`, rules). Work resumes from the status line and the candidate table (`existing_definition.md`). Largest gaps first, anchored challenges, files read rather than asked (`rounds.md`; `SKILL.md`, rules). | yes |
| WAY-118 | One search of the whole foundation (`readiness_gate.md` 7.2), the fingerprint and gate record (7.4), a change after approval goes through the gate again (`SKILL.md`, rules; `existing_definition.md`). | yes |
| WAY-156 | `delegated_mode.md`, word for word the base's section, with an orientation line. The critique is dispatched by the orchestrator and approval goes through it. `readiness_gate.md` opens with the same limbs for a dispatched turn. | yes |
| WAY-120 | `readiness_gate.md` 7.3. | yes |
| WAY-113 | "How a skill asks" read at step 0 (`SKILL.md`). | yes |
| WAY-111, WAY-150 | `read_foundation.md`. | yes |
| WAY-127 | `SKILL.md:17-21`: where the-way lies, and "each skill named below or in the files beside this skill" takes the prefix. Entry points unchanged; `skill_entry_points.py`: current. | yes |
| WAY-259 | The installer and its entry points are unchanged; the skill names its files by step. | yes |
| WAY-30 | `read_foundation.md`, a touched decision asked to change or fit. | yes |
| WAY-114 | `readiness_gate.md` 7.3, the list of meanings in the human's language. | yes |
| WAY-121 | `technology.md`, `existing_definition.md` (reopening), `rounds.md`, `find_entries.md`. | yes |
| WAY-142 | `readiness_gate.md` 7.5. | yes |

### Invariants

| Entry | Matches | Why |
|---|---|---|
| `skill-rule-source` | not affected | binds element skills; `define-project` is none |
| `outbound-link-reach` | yes | `grep -n "http\|Brain\|_zadania\|\.\./" project-level/skill/*.md` finds nothing |
| `project-definition-form`, `project-readiness-gate` | yes | `readiness_check.py` and its tests unchanged; `run_tests.py project-level` passes |
| `skill-entry-points` | yes | no `SKILL.md` added, renamed or re-described; `skill_entry_points.py` reports current; `run_tests.py agent-instructions` passes |
| `derived-file-content` | yes | the generated entry points are unchanged |

### Part map

`project-level`: its responsibility (the definition and its readiness gate among others), *Files*
`project-level/**`, *Depends on* and *Trust boundary* (`readiness_check.py`, `plan_check.py`,
`plan_state.py`, all unchanged) match. No part's files moved outside it.

### Glossary

- **"gate"**: the entry says "The gate is the one command that runs all of a product's tests".
  - The change's own new use was the file name `gate.md`, for the readiness gate. Corrected by the
    rename.
  - The uses the change moved word for word from the base still say "the gate" for the readiness
    gate: "goes through the gate again", "blocks the gate", "Keep the pending gate", "the gate
    record".
  - WAY-118's binding sentences ("goes through the gate again"), the template's section "Gate
    record", and `project-level/lead/skill/SKILL.md` use the same words in the same meaning.
  - Correcting them in the skill alone would change the base's text, against task question 1, and
    set the skill against the decision it carries. Correcting them everywhere leaves
    `project-level/skill/`.
  - I left them, as `assessment.md` proposal 4 gives (the readiness gate named in full, or a `Not:`
    line in the glossary entry, outside this change).
- **The other terms the files use** ("foundation", "entry", "binding sentence", "part", "surface",
  "project orchestrator"): used in their entries' meanings.

### What the return step writes

- **Environment fact:** none. The change rests on no source outside the-way.
- **Glossary term:** none. No word is used in a meaning WAY-95 gives an entry for; the one use
  against an entry is corrected above.
- **Settlements to record:** the task has no row, and no projected entry. Nothing was missed by the
  foundation step, which had nothing to write.
- **Choice that binds after the merge:** none new. The shape follows WAY-256 and WAY-265, and the
  file names and the rules section are ways of making what they settle.
- **Invariant:** none. No rule set by the task, a decision or the human lacks one.

### Search of the whole foundation

Searched `foundations/*.md` for entries naming a step, section or file of this skill:
- `grep -n "define-project\|project-level/skill\|Delegated definition\|delegated mode\|delegated_mode\|existing_definition\|read_foundation\|first_write\|rounds\.md\|find_entries\|technology\.md\|gate\.md\|idea\.md"`
- `grep -n -i "definition skill\|skill that defines\|define a project\|defines a project\|skill/SKILL"`
- `grep -n "step 7\|7\.3\|Rules that hold across"`

The only hit is `decisions.md:2761`, WAY-121's "a step of its own", which names no step of this
skill. Positive control: `grep -c "plan-project" foundations/decisions.md` gives 5. No foundation
entry names a step, section or file of `define-project`, so the rebuild leaves none pointing wrong.

## Reports updated

- `make_word_counts.py`, `make_assessment.py`, `check_pointers.py` and `proposals.md` now name
  `readiness_gate.md`. `word-counts.md` and `assessment.md` are regenerated, with the same figures
  as after the fix.
- `author_report.md` gains a line at its top saying `gate.md` there is `readiness_gate.md` under
  its first name. `fix_report.md` is left as written for `eeca32c`.

## Checks

| Command | Exit code |
|---|---|
| `python -B gate/run_tests.py project-level` (on `09b0dd0`) | 0, 271 tests OK |
| `python -B gate/run_tests.py agent-instructions` | 0, 18 tests OK |
| `python -B elements/common/foundation_check.py .` | 0, "0 errors" |
| `python -B agent-instructions/skill_entry_points.py` | 0, "entry points are current" |
| `python -B instruction-files/check_instructions.py . --file <each of the ten files>` | 0, `0 error, 1 warn, 14 info` (the base's root `AGENTS.md` warning; INFO `definition_template.md` at `SKILL.md:13`, `:45`) |
| `python -B <reports>/make_word_counts.py`, `make_assessment.py` | 0; 54 rows, 0 errors |
| `python -B <reports>/compare_sentences.py` | 0 |
| `python -B <reports>/check_pointers.py` | 0 |
| `python -B <reports>/verify_counts.py <reports>/word-counts.md <reports>/assessment.md <reports>/author_report.md <reports>/fix_report.md <reports>/return_report.md` | 0 (run after this report was written; its output is in the last line of this report) |
| `awk 'length>100' project-level/skill/*.md` | prints only `SKILL.md:3`, the frontmatter `description` |

Not run: `gate/run_tests.py installation`, since the rename touches no file the installer copies or
names. Also not run: the whole gate, which the orchestrator runs.

## Own-work check

- **The requirement most likely missed:** a pointer left naming `gate.md` after the rename, or the
  rename sending a step to a file that does not exist.
- **The check:** `grep -rn "gate\.md" --include=*.md --include=*.py .` outside `.runs/`, then
  `check_pointers.py`, which fails on a pointer to a missing file and on a file named at the wrong
  step.
- **What it showed:** the grep finds only `readiness_gate.md` names, and `check_pointers.py` exits
  0. Before the amend, `git status` showed the two pointer edits unstaged, which is how the first
  form of the commit was caught.

## Searches not found or unclear

- Whether the uses of "the gate" moved from the base fall under "a term used against its entry
  takes the use corrected": they predate the change, they stand in WAY-118's binding sentences, and
  correcting them leaves `project-level/skill/`. I read the rule as binding the change's own uses.
  The question is left to proposal 4.

verify_counts result: exit 0, 279 figures compared, 0 differ
