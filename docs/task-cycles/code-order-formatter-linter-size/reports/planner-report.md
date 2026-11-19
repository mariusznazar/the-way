# Planner report — code-order-formatter-linter-size

- Status: done with concerns
- Plan: `.runs/task-cycles/code-order-formatter-linter-size/plan.md`
- Size report: `.runs/task-cycles/code-order-formatter-linter-size/plan-size.md`
- Check: `python -B task-cycle/slice_size.py .runs/task-cycles/code-order-formatter-linter-size/plan.md`
  — exit code 0, all 19 slices `fits`, none unchecked.
- Commits: none (the plan and its size report are ignored files).

## What the plan does

Nine entries written before slice 1 (F1–F9), then 19 slices made one after another: the formatter's
configuration (1), the one reformatting commit (2), the formatter's test, rule, documents and
`.git-blame-ignore-revs` (3), the full check of the foundation in the gate (4), the linter faults in
four slices ending with the linter's mark cleared (5–8), the flaky worktree test (9), the word
"entry" (10), the divisions of functions and files (11–18) and the size test turned strict with its
mark cleared (19). Slices with their own review (trust boundary): 2, 5, 10, 11, 13, 15, 16, 18.
Model classes: `same` for 5 and 11 (each spans four trust boundaries in several parts), `cheaper`
for the rest.

## Measurements made for the cut (in a worktree at `d69fb20b`, Ruff 0.17.1)

- `ruff format --check --line-length 100` from the root, with the base `ruff.toml`: 79 files would be
  reformatted — the 78 `.py` files and `installation/README.md` (Ruff 0.17.1 formats Python blocks in
  Markdown by default); 1 `.py` file is already formatted.
- Reformatting the 78 files at width 100: 16 104 lines added, 7 505 removed; every reformatted file
  parses with `ast` to the same tree as before (no docstring was changed in value).
- Linter: 24 reports in 20 files, the same after reformatting and the same with `line-length = 100`
  in the configuration. List: `reports/planner-lint-base.txt`.
- Sizes after reformatting, at 110/1200 (the size test's counting): 11 functions and 2 files over —
  `installation/install.py` `run` 149; `instruction-files/check_instructions.py` `check_file` 137;
  `process-audit/audit_count.py` `read_gate` 153, `analyse` 219, `render` 206, file 3606;
  `project-level/plan_check.py` `check_header` 123; `project-level/plan_state.py` `provenance` 130,
  `task_report` 140; `task-cycle/cycle_stages.py` `read_codex_agent` 131, `read_claude_agent` 114,
  file 1273; `task-cycle/request_check.py` `check` 195. List: `reports/planner-sizes-formatted.txt`.
- `foundation_check.py` on the worktree: 0 errors, exit 0. In a clone with no
  `refs/remotes/origin/HEAD` and a local `main` at `f16616c0`, HEAD at `d69fb20b`: 0 errors, exit 0;
  with `main` at `d69fb20b`: exit 0.

## Concerns

1. **An entry beyond the five rows: F9 (WAY-339 and `audit-series-script-paths`).** WAY-339 names
   the script that measures the cost as `task-cycle/cycle_stages.py`, and
   `process-audit/audit_count.py` starts a series of the cost only on a change of the paths in
   `COST_SCRIPTS = ("task-cycle/cycle_stages.py",)`. Every part of `cycle_stages.py` measures the
   cost, so the division To do 4 requires moves code into a second file whose later changes would
   start no series unless the list, the decision and the invariant name it. I judged this no open
   design choice: the meaning of WAY-339 stays, and the only other ways break it (list left as is)
   or break the rule of size (`cycle_stages.py` compacted under 1200 without division). It is
   planned as F9, marked `the cycle's`, for the request to put before the human, with the code in
   Slice 17. If the orchestrator reads it otherwise, the way open is to return for a spec on this
   point alone; the rest of the plan does not depend on it except Slices 13 and 17.
2. **The audit loses comparability across this change.** The reformatting (and the divisions)
   change `task-cycle/cycle_stages.py`, `task-cycle/cycle_measures.py`, `task-cycle/gate_times.py`
   and `gate/run_tests.py`, so by WAY-339 the version of the-way that holds this change starts new
   series of the cost, of the count of remarks, of the measures of context and cache use and of the
   gate times, and this cycle's own measures of those tools come out unknown. This follows from the
   task as settled; the human may not have weighed it, and the request should say so.
3. **Behaviour of the audit changes in Slice 17**, by design of F9: a later change of
   `task-cycle/stage_transcripts.py` starts a series of the cost, and the reason the report gives
   names both files. The slice is marked `Risk: none` because `version_analysis.py` is no trust
   boundary; the review of the whole change judges it.
4. **Reading close to the limit.** At execution Slice 17 also reads `version_analysis.py`, which does
   not exist at the base and so counts zero in the size report (about 45 000 characters more, some
   140 000 tokens in all); Slices 5 and 8 read about 131 000 tokens. All fit the script's limit.
5. **A gap the rows leave.** Ruff's formatter also obeys `# yapf: disable` and `# yapf: enable` as
   `fmt: off`/`fmt: on`; rows 5 and To do 2 forbid only `fmt:` comments, so the plan forbids those
   alone. The-way's code holds no `yapf:` comment today. Recommendation: name it in the request as a
   finding outside the task's scope.
6. **The window of uncited invariants.** F3 and F4 read `test` from the entries' commit, and their
   tests come in Slices 4 and 3. Slices 1–3 therefore run no test of `elements/common` and Slice 3
   runs `foundation_check.py --skip-test-citations` (WAY-61, WAY-321); the agent of the entries runs
   its check with that switch.
7. **The return step** should compare with the code the Markdown files that call
   `task-cycle/cycle_stages.py` the script that measures the cost (nine `.md` files mention the
   script) and the description of `process-audit/test_audit_series_scripts.py`.

## Guidelines found missing or uncertain

- `guidelines/coding-shared-module.md` lists only `relation-model/fingerprint.py`, while
  `process-audit/stage_pricing.py`, `process-audit/record_items.py` and
  `elements/common/foundation_source.py` are modules other scripts import; its *Applies to* names
  `relation-model · process-audit` and not `elements-common` or `task-cycle`, where Slice 13 adds a
  module. The plan adds no row (Choices 12); the discrepancy belongs to `maintain-coding-guidelines`.
- `guidelines/coding.md` gives no rule on how an agent lays out its own change once a formatter
  stands; Slice 3 writes `### Formatter`, and the template's section "The tools of the standing
  checks" forbids naming a command of the tool there, so the command stands in `README.md` only.

## Order of work

No user interface is touched, so the styleguide's example of the order of work does not apply.
The order follows the cycle's hard order: the reformatting commit alone (Slice 2) after its
configuration (Slice 1), the divisions after it (Slices 11–18), and the linter fixes after it too,
for the reasons in *Choices* row 1.

## Reaches beyond the handoff

- `task-cycle/skill/SKILL.md:425-514` (Execute, verify and review) and
  `task-cycle/skill/foundation_step.md` whole — to learn that the plan's *Foundation entries* are
  written by one agent before slice 1 and what that agent may write.
- `task-cycle/slice_size.py:1-80` — the limits (150 000 tokens, 10 files) and how *Change* files and
  patterns are counted; they decided where decisions are edited (only by the agent of the entries,
  since `foundations/decisions.md` alone is 891 642 characters) and the cut of `audit_count.py`.
- `foundations/decisions.md` WAY-339 (8399–8534), WAY-48 (2565–2593), WAY-07 (532–559) read whole —
  the series of the cost, trust boundaries of moved modules, entries edited in place; WAY-344
  (2923–3091) located and named in Slice 5's *Read* for the missing-field rule behind TRY004, not
  read by me (the task's Context and the code at `task-cycle/cycle_stages.py:340-395` gave what the
  cut needed).
- `foundations/invariants.md` — `audit-series-script-paths`, `shared-module-import-runs-nothing`,
  the trust-boundary invariants (`project-plan-form`, `installation-paths-through-links`,
  `project-plan-state-evidence`, `readiness-check-refuses-non-utf-8`,
  `cycle-stages-refuses-crafted-names`, `cycle-measures-refuses-nested-line`,
  `audit-count-refuses-record-links`, `check-instructions-refuses-outside-links`) by their sentences.
- `guidelines/coding-command-runner.md`, `coding-generator.md`, `coding-repository-changer.md`
  (tables of files) — which kinds the changed files belong to.
- `product-guidelines/coding/template.md:20-68`, `:127-162`, `:319-343` — the rule *Formatter* and the
  tools of the standing checks.
- `elements/common/way_of_working.md:68-134` (Reading the foundation) — what *Read* selects.
- `elements/common/foundation_check.py:1-150`, `elements/common/test_foundation_check.py:1675-1752`,
  `task-cycle/test_remove_merged_worktrees.py:1-130` and `:360-420`, `task-cycle/cycle_stages.py:340-395`,
  `task-cycle/change_file_sizes.py:1-40`, `process-audit/test_audit_count.py` (ranges 190–215,
  2335–2370, 3262–3280, 3600–3616), `process-audit/stage_pricing.py:1-30`,
  `process-audit/record_items.py:1-20`, `process-audit/audit_count.py` (structure by `ast`, constants
  433–453), `task-cycle/cycle_stages.py` (structure by `ast`), `installation/README.md:105-128`,
  `README.md:95-220` — to name each slice's files and what it reaches.

## Unread material

- `elements/common/way_of_working.md` — read 68–134 only (Reading the foundation).
- `elements/decisions/template.md`, `elements/glossary/template.md` — not read; they serve the agent
  of the entries, who reads them through `foundation_step.md`.
- `elements/decisions/skill/SKILL.md`, `elements/invariants/skill/SKILL.md`,
  `elements/glossary/skill/SKILL.md` — not read, for the same reason (the handoff names them as
  `elements/*/SKILL.md`; they stand under `elements/*/skill/`).
- `foundations/environment_facts.md` — read its list of headings and the facts `ruff-default-rules`
  and `ruff-required-version`, not the other facts.
- `elements/common/foundation_check.py` — read 1–150 (its description), not its code.
- `elements/common/test_foundation_check.py` — read 1675–1752, not the rest.
- `task-cycle/test_remove_merged_worktrees.py` — read 1–130 and 360–420.
- `task-cycle/remove_merged_worktrees.py` — not read; Slice 9 changes only its test.
- `installation/README.md` — read 105–128 and its headings.
- `foundations/decisions.md` WAY-160 — not read beyond the method's citation; WAY-135, WAY-136,
  WAY-229 read whole.
- `product-guidelines/coding/template.md` — read the ranges above, not whole.

## Searches not found or unclear

- `elements/decisions/SKILL.md`, `elements/invariants/SKILL.md`, `elements/glossary/SKILL.md`, as the
  handoff names them: no such files; the skills stand at `elements/<element>/skill/SKILL.md`.
- The sections "Installing the linter" and the paragraph "Two invariants of the foundation of
  the-way": not in `agent-instructions/README.md`, as the handoff's list could be read; they stand in
  the root `README.md` (lines 185 and 177).
- Whether a trust boundary the part map names must have an invariant of its own: the rule
  *Trust boundaries* of `guidelines/testing.md` says "each trust boundary … has at least one
  invariant"; it is unclear whether a moved module listed as a boundary needs one beyond the
  command's. The precedent `process-audit/record_items.py` has none of its own; the plan follows it.
- Next free decision number: the log's highest is WAY-410; the plan writes no new decision.

## Working copies

All under `.runs/planner/` of the worktree, the directory the handoff names:

- `.runs/planner/base` — a git worktree at `d69fb20b`, reformatted for the measurements; removed
  with `git worktree remove --force`, then `git worktree prune`.
- `.runs/planner/clone-main` — a clone of the main checkout for the run of the check with a local
  `main`; removed.
- Scripts and outputs (`sizes.py`, `toplevel.py`, `astcmp.py`, lint and check outputs) — removed
  with the directory. Kept beside this report: `reports/planner-lint-base.txt` and
  `reports/planner-sizes-formatted.txt`.

No remainder.
