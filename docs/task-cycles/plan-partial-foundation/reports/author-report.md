# Author report — plan-partial-foundation

**Status:** done

**Change:** Updated `task-cycle/plan/SKILL.md` (9 lines added, 9 removed). The Foundation entries instructions now include the part of a projected entry the task's code makes true when the task carries the entry, including when the project plan assigns it elsewhere, as well as entries assigned by the task's plan item. The `Change` instructions now place the part-map change needed for a newly added file in the slice that adds that file. Removed the previous part-map example from the Foundation entries paragraph.

**Commit:** `90e826a` — `📝 Clarify task-cycle foundation entries`

**Checks run:**

- `git diff --check` — exit 0.
- `git diff -- task-cycle/plan/SKILL.md` — exit 0; reviewed the complete change against both requested outcomes.
- `rg -n 'Foundation entries|part map needed|part-map change for a file' task-cycle/plan/SKILL.md` — exit 0; confirmed the revised guidance is present and the old example is absent.
- `git status --short --branch` before staging — exit 0; branch was `task/plan-partial-foundation` and only the intended skill file was modified.
- No tests were run: this is prose in an instruction skill and the task requests no UI, executable code or test changes.

**Own-work check (weakest requirement):** The most failure-prone requirement is retaining the projected-entry case where the plan assigns the entry to a different task, without implying that this task may write an entry it does not carry. I checked the final sentence against Q1 and WAY-126: it says the task carries the projected entry, in full or in the part its code makes true, and expressly names the assigned-elsewhere case; the separately stated plan-item rule remains. The focused `rg` check above confirmed the text is in the intended paragraph. No test was written because the target is prose.

**Foundation and instruction material read:** The task and the full changed skill; the whole-change author method and its own-work check; the instruction-file skill method for skill placement; the foundation-step instructions; the `task-cycle` part-map entry; all invariants whose `Part` is `every`; all glossary entries; and full decision entries WAY-01, WAY-03, WAY-09, WAY-10, WAY-11, WAY-13, WAY-30, WAY-33, WAY-36, WAY-44, WAY-69, WAY-124, WAY-125, WAY-126, WAY-127, WAY-134, WAY-135, WAY-136, WAY-148, WAY-150, WAY-159, WAY-164, WAY-213, WAY-229, WAY-256, WAY-260 and WAY-262. Also read the required knowledge-artifact, skill-convention, git and script-writing rules. WAY-126 and `foundation_step.md` settle which partial and assigned entries the table must cover; WAY-44 supports putting the new file's part-map change with the file; WAY-256 governs placement in the skill; WAY-164 requires the manual weakest-requirement check below.

**Reading history:** The first report recorded a deviation because I had not completed the full handoff reading set. I then completed that set before dependent review, including every named decision, every `Part: every` invariant, the glossary, and the foundation-step instructions. The earlier deviation is retained here as session history; it is resolved and is not an outstanding concern.

**Manual own-work scenarios (WAY-164):** I checked the weakest requirement against three concrete planning cases and the final wording in `task-cycle/plan/SKILL.md:105-119`:

1. A source-only task carries a projected entry in its document; the project plan assigns writing it to another task, while this task's code makes one part true. **Observed:** the Foundation entries sentence includes the part its code makes true and explicitly includes the assigned-elsewhere case, so the plan must list the part this task realizes.
2. A task's plan item assigns it a projected entry, including a portion the code does not yet make true. **Observed:** the separate phrase “every entry its plan item assigns” includes that row; this agrees with WAY-126 and `foundation_step.md` on the assigned task writing what the foundation does not yet hold.
3. A slice adds a new tracked file whose path requires a new part-map pattern. **Observed:** the `Change` sentence puts the part-map change in the slice that adds the file, keeping the new pattern and the tracked file together as WAY-44 requires.

These are manual scenario checks of the instruction's behavior; no permanent wording test was added. `git show --check --format=fuller HEAD -- task-cycle/plan/SKILL.md` exited 0 after completing the reading. The focused `rg` check recorded above also exited 0. No full gate was run; the change is prose-only and the author stage returns before the orchestrator's gate.

**Searches not found or unclear:** `none`.

**Choices:** Kept the Foundation entries rule within one paragraph and made the file/part-map timing rule a sentence in the existing `Change` instructions. This follows the task's settled scope and the skill's existing structure. Full reading confirmed that the wording matches the task, WAY-126 and `foundation_step.md`; no correction to the committed change was necessary.
