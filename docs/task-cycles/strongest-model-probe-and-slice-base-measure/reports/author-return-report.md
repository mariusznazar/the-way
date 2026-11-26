Status: done with concerns

# Author report — the return step

**Commits:** none; the step changed nothing (head stays `15bf941a`).

## Foundation compared with code

I compared WAY-229, WAY-136 (written or changed), WAY-227 (named by the task), the entries the search of the foundation
found (WAY-160 and WAY-125, read whole in the first stage and unchanged) and the part map entry `task-cycle` with the files
of the repository, and made my own search over the tracked files for the words the change adds (`probe`, `model probe`,
`Strongest class`, `under *Author*`, `announces`, `base`, `leaves failing`, `availableModels`, `fails as expected`).

- WAY-229 (probe in every cycle and in every later session; first candidate the model named at the start, checked; next
  model down on substitution; every dispatch of the class in the session on the model fixed; no question to the human; the
  record gives the tries) matches `task-cycle/skill/SKILL.md` (paragraph before step 9, step 9 sub-step 2, the whole-change
  review, step 11, step 12 and the early stops), `task-cycle/record_template.md` (*Strongest class*, *Author*, *Slices*,
  *Events*) and WAY-227 (the probe asks no human). No file holds the old source (`availableModels`, "every model the session
  offers"): none left.
- WAY-136 (measure on the base, its two exceptions, the base result in the report; the announced test in the *Checks* of the
  repairing slice) matches `task-cycle/change/slice.md`, `task-cycle/change/SKILL.md` (variants table), `task-cycle/plan/SKILL.md`,
  `task-cycle/skill/planning.md` and step 9 sub-steps 2-4 of `SKILL.md`. No file still lists tests the plan leaves failing
  in a dispatch or compares a report with such a list: none left.
- The part map entry `task-cycle` names no file and no rule this change touches; no correction.
- Nothing needed correcting; the other uses of "probe" in the repository (a deployment guide, a migration script, the walkthrough)
  are ordinary uses with no bearing.

## Decisions written or changed

WAY-229 and WAY-136 (written by the earlier stages; no change in this step).

## Invariants written or changed

none. No rule here is a rule of a commit that a test could show false; both entries are decisions of the process.

## Environment facts

**None written; returned as a concern.** The change rests on a source outside the product that the foundation does not hold:
the Claude Code documentation on what a subagent runs on when an allowlist blocks the model it was asked for
(https://code.claude.com/docs/en/sub-agents.md, section "When an allowlist blocks a subagent model", read 2026-11-26, as the
task's *Context* quotes it). It is the behaviour of a tool the process uses, on which the probe rests (WAY-90), so the template
asks for a fact. I did not write it because `elements/environment-facts/template.md` and the skill's `draft.md` and `write.md`
demand what I cannot get inside the repository without a fetch:
- for a page without editions, "the closest archived copy that already exists and holds the passage", found through the
  Internet Archive's CDX index and opened to find the passage in it, or the statement that none exists, checked on a date;
- a mechanical check, before the entry is shown, that the address opens and the passage stands there word for word. The
  task's *Context* quotes the passage with an ellipsis (`[…]`) and I cannot use it as the passage of a source.
The handoff forbids a fetch of an external archive. The existing facts of the same page (`claude-code-subagent-cache-ttl` and
others) cite an archived copy of 2026-10-19, which predates the passage and is not known to hold it. What a later task or the
human has to supply: the passage word for word from the live page, and the archived copy found through the CDX index (or the
statement that none exists), with their dates. Until then WAY-229's *Based on* names the open-mercato sources only; its
*Rationale* states the substitution as an observation of this product's own cycles. Where the human holds that the entry may
carry a `TODO` meanwhile, the form is the last item of *Based on*: `· TODO — <environment fact for ... , with its source>`; I did
not write it, since it was not asked and would put a pending line on the main branch.

## Glossary terms

none. "Probe", "strongest class" and "base" are used in their ordinary meaning, for which WAY-95 asks no entry; no term of the
glossary is used against its entry (the glossary holds no word of this change).

## Part-map changes

none (no file added, removed or moved; `task-cycle/**` already names the part).

## Projected entries written whole or in part

none (the task is independent and carries none).

## Rows of *Settlements to record* written

- Row 1 (probe in every cycle, the model named at the start the first candidate, not taken on faith) — WAY-229, second paragraph.
- Row 2 (measure on the base in place of the guessed list, with the exception announced in the slice's own *Goal*) — WAY-136, third
  paragraph.
- Row 3 (the duty stands in the *Checks* of the slice that repairs the announced test, and the failure shows in the slice that
  did not repair it) — WAY-136, third paragraph (the *Checks* hold the tests of the file; the exception makes a test that an earlier
  slice's *Goal* announces and the slice's own *Checks* hold a failing check of that slice though it failed on the base too).
Each row went to the place its column names (a sentence of an existing decision); the writer's meaning sentences stand in
`reports/author-report.md`. No row is left unwritten.

## A choice that binds after the merge

None beyond what the entries and the skills carry. The choices of the first report (paragraph placement, the probe's place in
`SKILL.md`, the plan review's added check, rows completed at step 12) are rules of skills and files, not of the log, so by
the questions of the decisions template they stay where they stand; the task excludes no entry. No row of the questions
table is added by this step.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` — exit 0, "0 errors".
- `python -B instruction-files/check_instructions.py .` — exit 0, "0 error, 0 warn, 5 info".
- No test directory run: nothing changed in this step. Not run: the product's gate.

## Unread material

none (the entries and files this step names were read in the earlier stages or here: `task-cycle/skill/return_step.md` whole,
the element template and the four files of the environment-facts skill whole).

## Searches not found or unclear

none

## Working copies

None made.
