PASS 8f9be27f7686ddfa95ed305d464a376586afd80a

# Review of the reconciliation with the target branch (review-change, section 2)

Reviewed: worktree `the worktree of the task`, branch `task/weekly-process-audit`, HEAD `8f9be27` (confirmed by `git rev-parse HEAD`; worktree clean). Ranges: `b36014a..897bc0c` (renumbering), `897bc0c..8f9be27` (what the target branch brought in). Merge parents confirmed: first `897bc0c`, second `e9a0f92`.

## Findings

Blocking: 0. Minor: 0. Out of scope: 0.

None. The two sides hold together. Evidence per question of the handoff:

### 1. The renumbering

- **Every changed line is the audit's own number moved by exactly one.** I took every added and removed line of `git diff b36014a..897bc0c -U0` (74 removed, 74 added, 8 files: `foundations/decisions.md`, `process-audit/{SKILL.md,audit_count.py,price_list.md,problem_register.md,test_audit_count.py}`, `task-cycle/cycle_stages.py`, `task-cycle/skill/SKILL.md`) and checked by script that adding 1 to each `WAY-329`…`WAY-342` in the removed line gives the added line exactly. Mismatches: 0. No line changed in any other way, so no reference to WAY-327, WAY-328 or any decision outside 329…342 moved.
- **No reference was missed.** `git grep -E 'WAY-(32[6-9]|3[3-4][0-9])'` over the whole tree outside `foundations/decisions.md`, each hit read in its sentence:
  - `process-audit/*`, `task-cycle/cycle_stages.py:65-66`, `task-cycle/skill/SKILL.md:168`, `task-cycle/test_cycle_stages.py`: every WAY-330…WAY-343 reference is about the audit (class and weight WAY-330, results outside repositories WAY-332, grading WAY-333, count of problems WAY-334, fix by version WAY-335, frequency WAY-336, cost WAY-337, time WAY-338, comparability WAY-339, replay WAY-340, schedule WAY-341). Each matches the title of the decision of that number in the merged log.
  - `task-cycle/skill/SKILL.md:200,214,318` (WAY-325, WAY-326) and `task-cycle/skill/request_template.md:14,247,320` (WAY-326, WAY-327): decisions of the target branch, untouched by the renumbering (`request_template.md` is in neither diff).
  - `project-level/task_line.md:36`: WAY-329, the target branch's decision on the identifier of a task line, which is what the sentence is about.
  - No reference to WAY-344 or above; no reference to the audit's old number 329 survives meaning an audit decision.
- **`foundations/decisions.md:294`** (`(WAY-331)`, in the decision about where the audit's files stand): read in its sentence; WAY-331 is "Where in the repository does the audit of the process stand?". Correct.
- **Order and entries whole.** Last 22 headings read 322, 323 … 343 in sequence, no duplicate heading numbers in the file, no conflict markers (`<<<<<<<`, `>>>>>>>`, `=======`: 0). The join is at `foundations/decisions.md:10909` (WAY-329, whole: Scope, Based on, Relations, Verification, Origin, Rationale, Rejected) followed at line 10947 by WAY-330 (whole). The entry before it, WAY-328, ends with its *Rejected* paragraph before the WAY-329 heading. No half entry.
- **Relations of the audit's decisions** (all read): WAY-333, WAY-334 derive from WAY-330 (class and weight in the register: correct); WAY-342 derives from WAY-320 (the locations file), WAY-330 (the register entry), WAY-332 (the results directory): each is what WAY-342 uses; WAY-343 derives from WAY-335 (the version that holds a fix): correct. These agree with the old Relations moved by one (the script check above covers the lines). None names WAY-329.
- **The merge changed nothing of the audit.** `git diff e9a0f92 8f9be27 --stat` (second parent against the head) is the audit's 58-file change and nothing else. `git diff 897bc0c 8f9be27 --name-only` lists only files the target branch changed. The two files both sides changed, `foundations/decisions.md` and `foundations/part_map.md`, hold both sides' content (the target's hunks listed below; the audit's decisions and the `process-audit` part-map entry are intact).

### 2. What the merge brought in

- **WAY-329** (new), **WAY-154**, **WAY-107**, **WAY-27**, **WAY-320** changed by the target branch; read in the diff and the changed ones whole in the merged file.
  - WAY-329 derives from WAY-147, WAY-107, WAY-154; nothing in it touches the audit. Its identifier derivation is for project plan tasks; the audit's weekly task is a task the human keeps in his own backlog and the skill (`process-audit/SKILL.md:26-28,53`) writes no line of it.
  - WAY-154 and WAY-107 concern the refiner, the project orchestrator and the task place's rules. WAY-107's *violates* clause forbids a skill of the-way writing a status of a task's line, a dependency symbol or a rule of how a line is found or changed into its own text. `git grep -E '\[/\]|\[>\]|Ready|task line|task-rules|task_line'` over `process-audit`, `task-cycle` and `elements` finds nothing: the audit and the cycle do not do what the clause forbids. The removed line of the root `AGENTS.md` (move to Ready on `ready for cycle`) is not relied on by any file of the change.
- **WAY-320 against WAY-342.** WAY-320 now lists the entries "such as `tasks`, `projects` and `task-rules`", an open list; its new *violates* clause forbids one `task-rules` entry shared at the top level of the file. WAY-342's entries `problem_register` and `audit_results` stand under `the-way` and `repository` under each product's key, so neither is a top-level shared entry; `repository` under key X is X's own checkout, not "an entry of one repository under the name of another". No collision. The audit's decisions did not change WAY-320 and the merge did not need to.
- **`project-level/backlog_place.md`** against `process-audit/SKILL.md` step 1 (`:66-78`). The skill reads the section "Resolve an entry of the locations file"; that section is unchanged in structure, and its added words ("or the file of rules", "the place, or the file of rules, is missing") do not alter what the audit does. What the skill says matches what the section says for a missing file, key, entry or path: ask the human where the place is, offer to add the entry, write only on the human's yes (the skill adds the WAY-113 form of the question). The section's rule that a task cycle does not change the locations file (WAY-140) is kept by the skill's "write only on the human's yes" and by `:75-78`. The new `Task rules` line and `task-rules` entry are not among the entries the audit reads and the audit reads none of them.
- **`project-level/task_line.md`** (new) is read by `refine-task` and `lead-project` only; the audit and the cycle name it nowhere.
- **Root `AGENTS.md`** (a line `Task rules` replaces the line on moving to Ready): the audit's files cite no `## Backlog` line.
- **Part map.** Three lines changed in `foundations/part_map.md`: the `project-level` entry now also answers for "how the line of a task in the product's backlog is made, given its dependencies and moved to ready" (`:83-84`). `process-audit` (`:114-122`: Files `process-audit/**`, Depends on `task-cycle · project-level`, Trust boundary `process-audit/audit_count.py`) and `task-cycle` (`:93-101`) are not touched by the target branch's change; `process-audit` still depends on `project-level`, whose file `backlog_place.md` it reads, so the dependency is still true. No file of the target branch's change falls under `process-audit/**` or `task-cycle/**`.

## Declined to judge

- The line wrapping of WAY-27 and WAY-107 in the target branch's changes (a rationale sentence ends a short line at `foundations/decisions.md:~751`): the target branch's own text, outside this task.
- Whether the target branch's text of WAY-154, WAY-107 and WAY-329 is right: the task is the audit; the reconciliation is judged only for collision with it.

## Checks run

- `git rev-parse HEAD` → `8f9be27f7686ddfa95ed305d464a376586afd80a`; `git status --short` → empty, before and after the checks.
- `python -B elements/common/foundation_check.py` → `0 errors`, exit 0.
- Script on `git diff b36014a..897bc0c -U0`: 74 removed lines each equal to the added line with `WAY-329…342` moved +1 → 0 mismatches.
- `git grep -n -E 'WAY-(32[6-9]|3[3-4][0-9])'` over the tree (all hits read) → as listed above.
- `python -B gate/run_tests.py process-audit` → 118 tests OK, exit 0.
- `python -B gate/run_tests.py task-cycle` → 286 tests OK, exit 0.
- `python -B gate/run_tests.py elements/part-map` → 39 tests OK, exit 0.
- `python -B gate/run_tests.py project-level` → 275 tests OK, exit 0.
- `python -B gate/run_tests.py agent-instructions` → 18 tests OK, exit 0.
- `git diff e9a0f92 8f9be27 --stat`, `git diff 897bc0c 8f9be27 --name-only`, `git merge-base` → as in section 1.
- Not run: the full suite (the cycle's own run, per the handoff). The test runs wrote no file to the worktree (clean status).

## Reaches beyond the dispatch

- `foundations/decisions.md` read selectively: the join region (WAY-328 end through WAY-331), WAY-342 and WAY-343 whole, the heading list, and the diff `897bc0c..8f9be27` for this file, to check Relations and the target's changes. Why: the handoff asks about order, wholeness and Relations.
- `foundations/part_map.md`: the entries `project-level`, `task-cycle`, `process-audit` read. Why: the handoff names the part map entries.
- `task-cycle/skill/request_template.md` lines 14, 247, 320 (hits of the WAY-32x search) and `task-cycle/skill/SKILL.md` hits: read in their sentences to tell the target's decisions from the audit's.
- WAY-320 and WAY-27 text as the diff shows it (not the whole entry of WAY-320 from the file beyond its changed hunks and its Scope): read to judge the collision with WAY-342.
- No reading of the task document or the author's report; the handoff names none and the question is about the join.

## Unread material

The review is of the reconciliation, not of the whole change; no decision screening applies. Of the handoff's selection: WAY-320 was read through the changed hunks of the merge diff (the full entry was not read from the file; its text outside the hunks is the audit branch's and the base's, unchanged by the merge); WAY-107 and WAY-154 were read whole in the diff's new text, not from the file as a separate read; `project-level/task_line.md` and `project-level/backlog_place.md` read whole. Everything else named: read whole.

## Searches not found or unclear

- Unclear, not caused by the merge and not a finding: `project-level/backlog_place.md` ("Resolve an entry of the locations file") says to take "the key named in the line and, under it, the entry named in the line", while the audit's skill uses the section for entries it names itself (`problem_register`, `audit_results`, `repository`) with no `## Backlog` line behind them. The sentence is identical before the merge (same text in `897bc0c`), and the skill's own step 1 states the entries; the reader is not misled. Not graded.
- No search came back empty where a hit was expected; `WAY-344` and later: none (expected).
