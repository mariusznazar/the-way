# Handoff — reviewer of the whole change

You review the whole change of a task in a task cycle of the-way, as an agent that made none of it. The person who requested the cycle has delegated every intermediate choice to the orchestrator; no answer you get is that person's approval. You never ask the human; questions go back to the orchestrator in your report. You are read-only: you change no file of the worktree and make no commit.

- Worktree (your working directory): `the worktree root`, task branch `task/small-fixes-from-ai-review-and-audit`. The range you review: base `268b2b074691a331ed8db136343b4060bdd44539` to head `f52c565772f125fe5ebb17f0a0fb98ee7e56fe6e` (`git rev-parse HEAD` must print it; if it does not, ask the orchestrator which range to review). Compute `git diff 268b2b07..f52c5657` and `git log 268b2b07..f52c5657` yourself.
- Method: `task-cycle/review/SKILL.md` (`review-change`) in the worktree, read whole; read `task-cycle/review/whole_change.md` beside it and follow it (what you read and what you check besides section 2, the structure of the code, the numbers from `python -B task-cycle/change_file_sizes.py`). You select your own foundation and guidelines: the entries of the parts the change touches by "Reading the foundation" in `elements/common/way_of_working.md`, and the guidelines of those parts by `product-guidelines/reading.md`, each guideline file whole. Write the index of your selection of decisions with the script the method gives (into your directory for working copies, not into the repository) and count, for your report, how many decisions of it you read whole. The skill tool is not yours: a skill a file names is the `SKILL.md` whose frontmatter `name:` is that name, read as a file under the same root.
- Trust boundary: yes. The change touches `task-cycle/gate_times.py` (slice 2) and the docstring of `process-audit/audit_count.py` (slice 8), both named by the part map as trust boundaries; check crafted input at them (the invariants `gate-times-refuses-impossible-entry` and `audit-count-refuses-record-links`, the testing guidelines' *Trust boundaries*). Irreversible operation: no. A pin: none moved (the-way itself).
- Report path: `.runs/task-cycles/small-fixes-from-ai-review-and-audit/reports/review-whole-report.md`. Its first line is `PASS <sha>` or `FAIL <sha>` (the full sha of the head), or `questions`. The report file is the input of the cycle's scripts (`task-cycle/remarks_check.py` reads it); write it there although its name could look like one Claude Code refuses a subagent to write; if the write is refused all the same, return the report whole as your answer.
- Your directory for working copies: `.runs/review-whole/`.
- Do not read `cycle.md` or any file of `.runs/task-cycles/small-fixes-from-ai-review-and-audit/` that this handoff does not name. The files named below are yours.

## What you are given

- The frozen task, whole: `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md`. Judge the change against all nine points of its *To do*, its *Questions to settle* with their answers, its *Settlements to record* (3 rows), *Decisions in play*, *Out of scope* and its sources.
- The plan, whole: `.runs/task-cycles/small-fixes-from-ai-review-and-audit/plan.md` (eight slices and the plan's *Foundation entries*, rows 1 to 3 of the task's *Settlements to record*). Two changes of the orchestrator to the plan: slice 8's *Model* is `same`, not `cheaper`; and the shared file of point 9 is named `elements/common/reaching_another_skill.md` (the plan says `elements/common/hand_over.md`: a skill of the plan, `project-level/plan/skill/`, already holds an unrelated `hand_over.md`, so the orchestrator had executor 4 rename the file and add to it the words "never a personal copy of the same name", which the lead skill carried; commit `5bdef59f`).
- The orchestrator's own check of point 9, made once on the finished tree and not a test (the testing guidelines' *Not tested on purpose*): a fresh agent given the entry point of `record-decision` read `elements/decisions/skill/SKILL.md`, then `elements/common/reaching_another_skill.md`, then `elements/invariants/skill/SKILL.md` by its path, and made no call of the skill tool; its tool calls: `.runs/task-cycles/small-fixes-from-ai-review-and-audit/reports/point9-check-tool-calls.txt`. It says nothing of the other fourteen skills.

## The slices, their ranges and whether each had a review of its own

| Part | Range (commits, in order on the branch) | Review of its own |
|---|---|---|
| plan's *Foundation entries* (rows 1–3: two sentences and a clause in WAY-339, new WAY-417) | `268b2b07..a946862b` (`a946862b`) | no — judged by you; its writer's report: `.runs/task-cycles/small-fixes-from-ai-review-and-audit/reports/foundation-entries-report.md` |
| slice 1 — the tests of the versions moved into `process-audit/test_process_versions.py` | `a946862b..93d3e0d7` (`93d3e0d7`), and its repair `bcd8e551` (it defines `HERE` in the new file so the import check can resolve it) | no — judged by you; report: `reports/executor-1-report.md` |
| slice 2 — `task-cycle/gate_times.py`: nested runner output (point 8) | `93d3e0d7..8359dc25` (`8359dc25`) | yes: `PASS 8359dc257827d7861ae97a8f1e9fbefddc673869`, report `reports/review-slice-2-report.md`, three Minor findings (below) |
| slice 3 — `elements/common/reaching_another_skill.md` (first named `hand_over.md`) and the six skills of the elements, the line of WAY-127's *Verification* | `bcd8e551..5160a7b9` (`5160a7b9`) | no — judged by you; report: `reports/executor-3-report.md` |
| slice 4 — the nine other skills, and the rename of the shared file with its added words | `5160a7b9..d6ab032d` (`d6ab032d`) and `d6ab032d..5bdef59f` (`5bdef59f`, the rename) | no — judged by you; report: `reports/executor-4-report.md` |
| slice 5 — the three wordings of points 1–3 | `5bdef59f..3b34de03` (`3b34de03`) | no — judged by you; report: `reports/executor-5-report.md` |
| slice 6 — the image of each series, Q1 as numbers (new `process-audit/series_summary.py`) | `3b34de03..29a1c6ae` (`0ee90d8e`, `29a1c6ae`) | no — judged by you; report: `reports/executor-6-report.md` |
| slice 7 — the comparison before and after a fix inside each series | `29a1c6ae..ca55d4e8` (`ca55d4e8`) | no — judged by you; report: `reports/executor-7-report.md` |
| slice 8 — `process-audit/SKILL.md` and the docstring of `process-audit/audit_count.py` (points 6–7) | `ca55d4e8..f52c5657` (`f52c5657`) | yes: `PASS f52c565772f125fe5ebb17f0a0fb98ee7e56fe6e`, report `reports/review-slice-8-report.md`, three Minor findings (below) |

The reports (the paths are under `.runs/task-cycles/small-fixes-from-ai-review-and-audit/`) are sets of claims to verify, not evidence. Their **Problems as observed** and concerns, which the orchestrator's mechanical check passed on, are information for you, not findings:

- Slice 6's executor found that `AuditCountCase.section` in `process-audit/test_audit_count.py` reads all table lines under a series heading and is wrong for a series with an image; only `process-audit/test_process_versions.py` uses it and overrides it in a subclass.
- Slice 7's executor found that a mechanism comparison stands wherever cycles stand on both sides, also where no cycle gives a value (copies of records without `mechanism_measures.md`): then it gives 15 pairs of rows with `unknown` and 15 pairs in *Unknown values* for each fixed issue and series; and that its calls of git grow with the fixed issues times the versions, not measured on the real register.
- Slice 4's executor first reported three "dangling pointers" to `hand_over.md` beside the plan skill (`project-level/plan/skill/SKILL.md:85`, `assign_entries.md:15`, `existing_plan.md:14`); they point to `project-level/plan/skill/hand_over.md`, a file that exists and is not the shared one.
- The agents' handoffs in the cycle named some passages of the task by lines instead of copying them (slices 2–5); judge the slices by the task, not by those handoffs.

## Minor findings of the slice reviews, word for word from their reports

Grade each as a finding of this review (`whole_change.md`).

### From `reports/review-slice-2-report.md` (slice 2, `8359dc25`)


### M1 — The rule the plan gives misreads two directories that each print a nested run, and a nested output cut off before its summary line ahead of one that has it

- **Place:** `task-cycle/gate_times.py:233-248` (`Times.nested`), the cap `taken = min(lines, directories, surplus)`.
- **What is wrong:** each earlier summary line takes up to its own `<m>` lines from the lines
  `== ` since the summary line before it. In a failure message the first nested directory stands
  after text, so a nested run has only `<m> - 1` lines at the start of a line; the cap of `<m>`
  therefore lets a summary line take one line more than its run printed, and the surplus is the only
  limit. Where the segment before a summary line also holds the real line `== <directory>` of the
  enclosing block, and an earlier nested run leaves surplus over, the real line is taken.
- **Evidence (a probe that fed hand-written output to `Times` of the head, run once):**
  - Case A: `other` passes; `gate1` fails with a nested run of `a` (after text) and `b`; `gate2`
    fails with a nested run of `c` (after text) and `d`; each nested summary is
    `2 tests in 2 directories; …`; the run's own summary counts 3 directories. Expected by hand:
    `other 0.002`, `gate1 0.500`, `gate2 0.600`. Got:
    `[['other', '0.002'], ['gate1', '0.001'], ['b', '0.600']]` — `gate2` and `d` are taken as
    nested, `b` is listed as a directory with `gate2`'s time, and `gate1` gets the nested run's
    `Ran` line. This is the very misreading point 8 of the task removes.
  - Case C: one block `gate` with two failing tests; the first prints a nested output cut off before
    its summary line (`p` after text, `q`, `r`), the second a whole nested run (`s` after text, `t`).
    Got `[['gate', '0.001'], ['q', '0.900']]`: the surplus of the cut-off output is charged to the
    second run's segment, `r` and `t` are taken, `q` stays a directory and takes the time of `gate`.
- **Why it matters, and why Minor:** the plan's Goal mandates "each such summary line taking at most
  its own `<m>`", so this is a defect of the planned rule, named as such, not a departure of the code
  from it. In the-way the case cannot arise today: of the test directories only `gate/`
  (`gate/test_run_tests.py`) prints a nested runner output in a failure message (the other test that
  runs the runner, `task-cycle/test_gate_times.py:438`, passes bytes as the message, which unittest
  prints as one `repr` line), so two such blocks never meet in one run; and the rows concerned are of
  failed runs, which WAY-350 does not compare. A product whose gate has two directories that test a
  copy of the runner would get case A. Case C needs a nested output without its summary line (an
  interrupted nested run) beside a whole one. A direction, if the orchestrator wants the rule
  tightened: start a nested run's lines after the last line of its segment that holds `== ` after
  text (the marker of a failure message), rather than capping by `<m>`; that is a change of the
  planned rule.

### M2 — The ceiling of memory for crafted output is four times today's

- **Place:** `task-cycle/gate_times.py:75` (`PIECES_KEPT = 100`), `:165` and `:167` (`Piece.own`,
  `Piece.after`), `:205-209`.
- **What is wrong:** a piece keeps the seconds of its first `Ran` line and of the first `Ran` line
  after a summary line, each as printed, and a line may hold up to `LINE_LIMIT` (1 MiB). Today 50
  blocks keep one such string each (about 50 MiB at worst); now 100 pieces keep two each (about
  200 MiB at worst), and `own` and `after` are separate copies even when they come from the same
  line. The probe measured 20 MB kept for 200 pieces with `Ran` lines of 100 KB each (100 kept × 2 ×
  100 KB).
- **Why Minor:** the memory stays bounded whatever the output holds, as the Goal requires; only the
  bound grew. Cutting the seconds at a length no real time reaches, or keeping one string where both
  fields come from one line, would bring it back; the executor names the same point under its
  weakest point and chose not to cut.

### M3 — A summary line is recognised with Unicode digits

- **Place:** `task-cycle/gate_times.py:82-84`, `SUMMARY` uses `\d`, while `RAN` (`:80`) uses
  `[0-9]`.
- **What is wrong:** in a `str` pattern `\d` matches every decimal digit of Unicode, so a crafted line
  `٣ tests in ٣ directories; every directory passed` (Arabic-Indic three) is a summary line with
  `<m>` = 3. The probe: `== a`, that line, `== b`, then `1 tests in 1 directories; …` gave
  `[ ['b', '0.002'] ]` — `a` was taken as nested. No crash: `int()` reads those digits.
- **Why Minor:** the runner prints only ASCII digits, so only crafted output reaches it, and the
  effect is a wrong row, no failure of the script and no change of its exit code. `[0-9]{1,9}`
  would match what the runner prints and nothing else, as `RAN` does.



### From `reports/review-slice-8-report.md` (slice 8, `f52c5657`), its Minor findings and the lines it declined to judge

### Minor

1. **`process-audit/SKILL.md:244-254`: the text says Q2 of a version is the sums, but the rows
   for each version do not show the sums.** The bullet "*The rows per version* ... a series of the
   count of remarks shows Q1 and Q2 of each version" is followed by "Q2 of a group is the sum of
   the slices planned and the sum of the slices returned too large over the cycles whose plans are
   read, with `yes`, `no` or `unknown` as the answer those sums give". The definition of a group
   includes a version ("Q1 of a group of cycles — a version, a whole series, one side of a
   comparison"). But the row of a version that `version_analysis.py:1026-1035` writes under
   `COUNT_HEADER` (`audit_report.py:73-80`) holds *Plans read* and the Q2 answer only. It has no
   *Slices planned* and no *Slices returned too large*, while the image
   (`COUNT_IMAGE_HEADER`, `audit_report.py:57-64`) and each side of a comparison have both. So a
   session that reads the skill looks for sums in the rows of the versions that are not there. The
   wording follows WAY-417 word for word, which is why the text and that code differ: the code that
   writes the version rows belongs to slice 6 and lies outside this range. A fix in the text would
   say that the rows of a version give *Plans read* and the answer of Q2, and the image and the
   sides also give the sums. I grade it Minor because nothing here would lead a human to a wrong
   conclusion: the sums are missing from the result, and no wrong figure is shown.
   Evidence: `audit_report.py:57-64`, `73-80`; `version_analysis.py:1016-1035`.

2. **`process-audit/SKILL.md:276-277`: "the series whose rows give nothing but `unknown`" no
   longer fits a series of the count of remarks.** Q1 is now always the three numbers
   (`series_summary.py:91-97`). So the Q1 cell of a version is never the word `unknown`, even when
   every cycle of the version answers unknown (`yes 0 · no 0 · unknown 3`). Read literally, the
   sentence never groups a series of the count of remarks. Read for its intent, it groups the series
   whose cycles answer nothing. The slice changed the form of Q1 in this same paragraph and left
   this sentence as it was. A clause such as "for Q1, a series whose every version reads
   `yes 0 · no 0 · unknown n`" would settle it. Minor: the session can still tell what the sentence
   means.

3. **`process-audit/audit_count.py:201`, and also `:157` and `:160`: docstring lines over the
   width of 100 that the rest of the text keeps.** Line 201 is 146 characters long. The added text
   ends at "The count reads" on line 200, and the old line ("these measures and shows them with a
   median and a comparison for each version, because the numbers lie in the records of cycles,
   which the session") was joined into one long line without rewrapping. Lines 157 and 160 are
   101 and 104 characters. The formatter does not reflow strings and the linter does not enforce
   the width here: the base already had docstring lines of 158 and 172 characters, and the tests
   pass. So this is layout only. Minor.

No finding contradicts a settlement, and none blocks.



## Declined to judge

- `process-audit/version_analysis.py:1026-1035`: the row of a version in a series of the count of
  remarks has no sums of slices, which WAY-417 calls Q2 of every group. That is code of slice 6,
  outside this range. I record it only as the cause of Minor 1, and whether the code departs from
  WAY-417 is for the review of that slice or of the whole change.
- `process-audit/audit_count.py:128` ("in which the answers Q1 and Q2 are compared") and `:338`
  ("the section *Measure versions* gives them per version"): these lie outside the two paragraphs
  the slice may change, and they are not wrong enough to matter here.
- `process-audit/SKILL.md:154-160`, the opening of step 3 ("*Measure versions* gives their medians
  per version ... series by series"). It does not mention the image or the comparisons. The slice
  names point 4 only, and the author left this sentence as it was on purpose.


## What your report holds

Your report holds, after its first line, what the method gives: the graded findings (blocking and Minor, each with the place in the code, the reason and — for a blocking one — whether it contradicts the settlements, with the mark `Contradiction: yes` or `Contradiction: no` as the method asks), the findings outside the task's scope, the checks you ran each with its command and exit code, each reach beyond this handoff (what, where, why), each working copy (where it stood and that you removed it, or the remainder with its full path), **Unread material:** each file, entry or passage this handoff names that you did not read whole or read in part, or `none`, and **Searches not found or unclear:** each thing you looked for and did not find or that was unclear, or `none`. Return the report's first line, the checks you ran with their results, and the report's path.

## Working copies (word for word from the process of the cycle)

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
in the system's temporary directory, in the scratch directory of a session or in the main checkout
of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by
itself under its session's directory is moved into the agent's directory and the original removed,
except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md`
says, to the place the product's foundation settles for screenshots, and into the agent's directory
only where no such place is settled. The files that a product's own tools and tests make by
themselves are no working copy of the agent and stay outside this rule. Before the agent returns,
each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then
`git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in
the report where each copy stood and that it was removed. Where a removal fails, the agent finishes
all the same and names in the report the remainder, with its full path and the reason it stayed. It
removes a copy, as any directory, by its path written out in full in the command, never through a
shell variable: an empty variable turns the removal on the directory the shell stands in.
