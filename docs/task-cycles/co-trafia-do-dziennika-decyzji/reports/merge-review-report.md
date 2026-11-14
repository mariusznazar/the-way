PASS f398251a0368737d88d3b1b77816aef1e49ad96a

# Review of the reconciliation with the target branch

Worktree `the root of the task's worktree`, branch `task/co-trafia-do-dziennika-decyzji`. `git rev-parse HEAD` is `f398251a0368737d88d3b1b77816aef1e49ad96a`, as the handoff gave it. The range is `ff69628..HEAD`, the merge of `origin/foundations` at `d40d1cb`, which holds #116, #117 and #118 since `ac75340`.

## Findings

Blocking: none. Minor: none. Out of scope: none.

## What I confirmed

### The merge holds both sides, and only them

- Ten of the twelve files the target branch changed are byte for byte as `origin/foundations` has them: `git diff --quiet origin/foundations HEAD -- <file>` is clean. These are `elements/environment-facts/template.md`, `foundations/environment_facts.md`, `foundations/invariants.md`, `installation/*` (four files) and `project-level/plan/*` (three files).
- The two files both sides changed are `elements/decisions/template.md` and `foundations/decisions.md`.
  - For the decisions template, `git merge-file` of `ff69628`, `ac75340` and `origin/foundations` equals the merged file.
  - For the log, I split both sides into entries. The entries this change edited (WAY-02, 03, 05, 11, 12, 17, 19, 22, 115, 134, 167, 168, 171, 172, 293) equal `ff69628`'s. All other entries equal `origin/foundations`'s, which carries the target's 22 edits (WAY-90, 136, 146, 164, 229, 255, 256, 300, 308, 309, 316, 319, 320, 323, 350, 352, 353, 362, 364, 368, 369, 371).
  - The two sets of edited entries do not overlap, and the entry sets of the three versions are the same.
- Every file this change changed, apart from those two, is unchanged by the merge against `ff69628`.

### The decisions template as merged is one text

- The target adds one bullet, after the *Based on* bullet (`elements/decisions/template.md:53-58`). No other bullet on the topic exists, and nothing is duplicated.
- The bullet agrees with the sentences this change wrote or changed.
  - Its words "no such source" refer to the *Based on* bullet just above.
  - The *Rationale* and *Rejected* bullet (line 74 ff., from WAY-05) lets "a measurement the choice rests on" stand "with what was measured and under which conditions". The new bullet asks for the same plus the sentence that the measurement is the product's own.
  - The bullet on *Rejected* of a decision written from a settlement row (WAY-134) bars ways the writer derives. The new bullet speaks only of a measured way not chosen that the source holds, so the two do not collide.
  - The new text sits beside the questions "where it goes" and the `decision:` / `tests:` text without touching either.
- The environment facts template (`elements/environment-facts/template.md:55-60`) says the same as the decisions template and as WAY-90.
- `elements/decisions/skill/SKILL.md:31` (*Based on*) and the settlements table of `project-level/task/template.md` say nothing on measurements, so there is no second wording to contradict. `git grep` for "measurement" in `elements`, `task-cycle`, `project-level`, `product-guidelines` and `agent-instructions` finds only the two templates and `elements/common/critique/check.md:21`, which is unrelated.

### The foundation entries the target brought in, read against this change

I read whole in the merged log WAY-05, 17, 90, 27, 80, 12, 134, 22, 03, 293, 368, 364, 256, 229 and 146, and the full diff of the target's 22 edits to the log, plus the new invariant `installation-paths-through-links` and the new fact `python-junction-detection`.

- **WAY-90 against WAY-05, WAY-17, WAY-27, WAY-80 and the template.** WAY-90 gives the same rule as the template's bullet. It cites WAY-05 for "a measurement may stand", and WAY-05 as this change reworded it still says so (the clause on a measurement is unchanged). Its *Rejected* answers WAY-27 and WAY-80, which this change did not touch. It binds only "a measurement that the product's own people made … whose record a reader cannot open"; WAY-17's chain of links is untouched.
- **The 20 other edited entries.** They add sentences of the form "the measurement is this product's own, and its record is not open to a reader of this repository" to *Rationale* or *Rejected*, which is what WAY-90 and the new bullet ask. None changes a binding sentence of an entry this change edited, and none cites a sentence this change reworded. WAY-146 (task size in the plan critique) adds binding text and a pair; it names no part this change touches.
- **WAY-256, WAY-229 and WAY-368.** Their binding sentences contradict none of the sentences this change wrote. WAY-368's binding paragraph and WAY-256's both stand at three sentences or fewer, as this change's WAY-05 requires. WAY-229's first paragraph runs to five sentences. It was so at `ac75340`, the target did not touch its binding sentences, and this change did not either, so it is not a reconciliation defect.
- **The new invariant `installation-paths-through-links`.** It derives from WAY-48, WAY-235 and WAY-368, so several decisions stand on it. That is the case in which this change's WAY-22 and the template keep an invariant. No decision of this change names it, and it is cited by `# invariant:` lines in the installer tests, so the "uncited `test` invariant" report does not fire.
- **The new fact.** `python-junction-detection` has the form the check reads (source with address, archive, date and passage).

### The foundation check of the merged tree

- `python -B elements/common/foundation_check.py`: exit 0, `0 errors`, no listed line. I ran it myself.
- The merge base the script finds is `d40d1cb` (`refs/remotes/origin/HEAD` names `origin/foundations`). Against that base, the decisions the target changed are not "altered by the change", and only this change's 15 are. To judge whether the target's decisions are read correctly, I ran the script's `run()` in process with its base forced to `ac75340` and to `ff69628`. Both give `0 errors` and no listed line. So the 22 entries the target edited and the new invariant are held and read without error, and the check lists no reworded invariant, because the target only added one.
- The `decision:` lines of this change, 18 in `elements/common/test_foundation_check.py`, quote WAY-12 (lines 1067-1364) and WAY-03 (lines 1429-1497). The target did not edit either entry (neither is among its 22), and the check, which compares each quotation with the merged log, reports none.
- `python -B agent-instructions/skill_entry_points.py`: exit 0, "entry points are current". `python -B agent-instructions/agent_type_copies.py`: exit 0, "agent type copies are current".

### The target's tests against this change's script and files

- This change did not touch `installation/install.py` or its tests, and the target did not touch `foundation_check.py`. The one place the two meet is `installation/test_install.py::test_empty_foundations_have_valid_form`. It runs the new `foundation_check.py` on an installed product with an empty foundation and requires each output line but the last to say "no part claims it". The new script's second-kind lines (unheld decisions, reworded invariants, unknown base) are written only where `foundations/decisions.md` holds a decision, so none appears. I ran it with `test_empty_foundations_are_in_the_current_form`: both pass.
- `migrate_foundation.py` on the merged tree is a trial run that writes nothing; it exits 1 with 8 "places for a human". They are old-reference texts in fixtures and quoted forms (WAY-02, WAY-169, WAY-301, three test files) and the *Based on* of WAY-229, none of which the merge brought or changed.

## Declined to judge

- `project-level/task/template.md:206-210`, the settlements paragraph, holds an unwrapped line over 100 characters from this change's earlier commit (`f20a62c`/`aef5b88`). It was in the ranges reviewed before and is no matter of the reconciliation; Minor at most.
- WAY-229's first paragraph holds five sentences. It was so before either side's change and the target did not touch it, so it is outside this review.
- The pending migration report's 8 places: pre-existing and not made by the merge.

## Checks I ran (all in the worktree, read-only; no gate)

| Check | Result |
|---|---|
| `git rev-parse HEAD` | `f398251a0368737d88d3b1b77816aef1e49ad96a` |
| `git diff ff69628..HEAD`, `git diff ac75340..origin/foundations`, `git log --first-parent ac75340..HEAD` | same 12 files; no conflict |
| `git diff --quiet origin/foundations HEAD -- <each of the 10 target-only files>` | clean |
| `git merge-file -p` of the template (cycle, base, target) compared with the merged template | equal |
| Entry-by-entry comparison of `foundations/decisions.md` of the merge with each side | no mismatch; same entry sets |
| `python -B elements/common/foundation_check.py` | exit 0, `0 errors` |
| the same `run()` in process with the base forced to `ac75340` and `ff69628` | exit 0, `0 errors` each |
| `python -B agent-instructions/skill_entry_points.py` | exit 0 |
| `python -B agent-instructions/agent_type_copies.py` | exit 0 |
| `python -B -m unittest installation.test_install.InstallTest.test_empty_foundations_have_valid_form installation.test_install.InstallTest.test_empty_foundations_are_in_the_current_form` | `Ran 2 tests ... OK` (the shell's exit code shown was that of `tail`) |
| `python -B elements/common/migrate_foundation.py . --report <scratchpad>` (trial run) | exit 1 with 8 pre-existing places for a human; wrote nothing in the worktree |

`git status --short` was clean after the checks. I started no background process.

## Reaches beyond the dispatch

- WAY-27, WAY-80, WAY-17, WAY-12, WAY-22, WAY-03, WAY-293, WAY-368, WAY-364, WAY-256, WAY-229, WAY-146, each read whole from the merged `foundations/decisions.md`, to judge the target's bearing on this change's sentences (WAY-27, 80 and 17 are WAY-90's neighbours; the others are the entries the dispatch names or the ones this change reworded).
- `foundations/invariants.md` (the new entry) and `foundations/environment_facts.md` (the new fact) in the hunks the target added.
- `elements/environment-facts/template.md`, `elements/decisions/skill/SKILL.md` and `project-level/task/template.md`, to see whether a second wording of the measurement rule exists.
- `elements/common/foundation_check.py` lines 60-125 and `fork_point`, to learn which base the check takes after the merge.

## Unread material

- The dispatch named no passages beyond the handoff. I read the handoff and `task-cycle/review/SKILL.md` whole.
- Of the target's 22 edited entries, I read WAY-90, 229, 256, 146, 364 and 368 whole; for the other 16 (WAY-136, 164, 255, 300, 308, 309, 316, 319, 320, 323, 350, 352, 353, 362, 369, 371) I read their diff hunks and the binding paragraph counts, not each whole entry. The hunks of 14 of them only add the "product's own, record not open" sentence or reflow a line; I judged them on the hunk. WAY-136 and WAY-164, whose hunks I read in the diff output, did not appear to bear on any part this change touched.
- I did not read `elements/decisions/examples.md` or the cycle's earlier review reports.

## Searches not found or unclear

- No decision names the hidden cycle behaviour "the target's decisions reported by the check after a merge". The script reports a decision as changed only against the merge base, which after this merge is the target's own head, so a decision the target changed is not listed as changed. I found no sentence of WAY-12 that asks otherwise; WAY-12 says "a decision that a change adds, or whose binding sentences the change alters". I judged this as correct behaviour and checked it by forcing the base. Stated here only because the handoff's third question could read the other way.
- `git ls-files` of a test of a decision's binding-sentence count (to find whether the new "one to three sentences" rule is enforced by a script): none found. It is enforced by review only, so I counted the target's edited entries by hand.
