# Handoff — slice 3

The person who requested this cycle delegated its intermediate choices to the orchestrator; no answer
here is that person's approval. You never ask the human: a question goes back to the orchestrator in
your report.

- Worktree (work only from its root): `the task's worktree root`, branch `task/cycle-technology-decisions-batch`. This is the-way itself; there is no pinned process.
- Your method and variant: `make-change` — read `task-cycle/change/SKILL.md` whole; your variant is **a slice, or the retry of a slice**, so read `task-cycle/change/slice.md` when the method sends you there. Read `agent-instructions/README.md` too.
- Stage and boundary: slice 3 of `.runs/task-cycles/cycle-technology-decisions-batch/plan.md` only. Change only the files of the slice's *Change* line; commit them with `git add <path>` (no `git add -A`); commit messages in English. Run the slice's *Checks* yourself (focused; never the full `python -B gate/run_tests.py` without a directory). The slice's *Model* sets your class.
- Frozen task (read whole): `.runs/task-cycles/cycle-technology-decisions-batch/task.md` (Polish). Plan: `.runs/task-cycles/cycle-technology-decisions-batch/plan.md` (your slice section is copied below word for word; the plan's *Foundation entries* and *Choices* are in the plan). No spec.
- Foundation entries already written in this cycle (commits `85c5395` .. `f3b90d5` on this branch, in `foundations/decisions.md`; the report is `.runs/task-cycles/cycle-technology-decisions-batch/reports/02-foundation-entries-report.md`): read the plan's *Foundation entries* table, then read the decisions your slice depends on in their current text. Row 1 is the **new decision WAY-322** (current range in the list below if your slice reads it); it covers every matter of an agent's way to the running product that the step lists — the base holds a fifth matter beyond the task's four, the place of the screenshots — and the failure notice; word your files to agree with it. WAY-165, WAY-166 and WAY-139 were reworded in place.
- Answers of step 4: trust boundary — yes — `project-level/plan_state.py` is named as a trust boundary by the part map and this slice changes it; irreversible operation — no.
- **Drift:** the task's line numbers and the plan's cite older commits; find each place by its content. Where the current text of a place already says what the item asks, change nothing there and say so in your report.
- Report path: `.runs/task-cycles/cycle-technology-decisions-batch/reports/05-slice-3-report.md` (full report as the method gives it, with the own-work check, **Searches not found or unclear**, reaches beyond this handoff, and each check with its command and exit code).
- Return: status, your commits, a one-line check result naming what failed or did not run, and the report path.

- **Trust boundary, crafted input:** `project-level/plan_state.py` reads archived cycle records (text from the repository's history, any author) as data. Every line it prints from such text must be built from fixed words and the match, as `display` and the precedent test `test_record_instructions_are_data_and_markdown_is_not_part_of_pr_url` do; test a record whose *Request URL and status* line carries look-alike text, control characters, an instruction in the line, and a line that is only part of the wording. A reviewer of this slice will check crafted input at that boundary.
- **Test first:** write the new test in `project-level/test_plan_state.py` before the change, run it, and keep in the report the command, the exit code and the failure text of the failing run, then the passing run (the method's rules for a test written first apply).


## The slice (plan section, word for word)

### Slice 3 — A blocked draft request shown as blocked by the plan-state reader

- **Goal:** (item 7) a task whose cycle ended in a blocked draft request opened after the record was written is reported by `project-level/plan_state.py` as blocked, not as a task with no request. The record's field *Request URL and status* then reads `blocked draft, opened on this commit` — the wording `task-cycle/skill/reserved_return.md` (step 2 of "Open the request") already gives — and `task-cycle/skill/blocked_finding.md` says the same of its record copy, which is committed before the request exists; the script recognises that wording on the field's line in an archived record, in the same way and from the same Git reads that it finds the pointer to a request today (`record_pointers`, `PR_LINK`), and prints one evidence line for such a record naming the task, the commit and the record file and saying the request is a blocked draft. The line is built from fixed words and the match; no other text of the record reaches the output (test `test_record_instructions_are_data_and_markdown_is_not_part_of_pr_url` is the precedent). It adds no proposal, no conflict, no exit code and changes no existing line (the surface `project-plan-state-command`); every subprocess it starts is Git (`project-plan-state-subprocesses`). Write first a test in `project-level/test_plan_state.py` that fails for the reason stated, using the fixture helpers there (`archive`, `cycle`, `run_reader`), and make it pass; the test covers a record carrying the wording, a record carrying look-alike text elsewhere (not on the field's line), and a record with a real pull-request URL, which keeps its existing pointer line.
- **Change:** `project-level/plan_state.py` · `project-level/test_plan_state.py` · `task-cycle/skill/blocked_finding.md` · `task-cycle/skill/reserved_return.md`
- **Read:** `.runs/task-cycles/cycle-technology-decisions-batch/task.md:36-36` To do, item 7 · `task-cycle/record_template.md:176-195` Request handoff · `foundations/decisions.md:4302-4333` WAY-153 · `foundations/decisions.md:4678-4715` WAY-163 · `foundations/decisions.md:8228-8292` WAY-269 · `foundations/invariants.md:301-327` project-plan-state-evidence and project-plan-state-subprocesses · `foundations/part_map.md:77-101` project-level and task-cycle · `foundations/part_map.md:203-210` project-plan-state-command · `project-level/test_plan_state_invariant.py:290-345` tests citing project-plan-state-evidence
- **Model:** same — a script that reads untrusted record text at a trust boundary and keeps a pinned output surface
- **Risk:** trust boundary — `project-level/plan_state.py` is named as a trust boundary by the part map entry `project-level`
- **Checks:** `python -B -m unittest discover -s project-level -p "test_plan_state.py"` (the new test first fails, then passes) · `python -B gate/run_tests.py project-level` · `python -B elements/common/foundation_check.py --skip-test-citations` · `git diff --check`
- **Depends on:** none

## Passages the slice reads

#### Task passage: To do, item 7 (task.md:36-36)

```text
7. Odczyt stanu planu (`project-level/plan_state.py`) pokazuje zadanie, którego cykl skończył się zablokowanym szkicem PR-a otwartym po zapisie (`skill/blocked_finding.md`, `skill/reserved_return.md`), jako zablokowane, a nie jako zadanie bez PR-a; zapis cyklu na obu drogach ma w *Request URL and status* brzmienie, które skrypt rozpoznaje (theway#071-17; `blocked_finding.md:10-14`, `reserved_return.md:56`, `plan_state.py:27`, `:146-158`).
```

## Entries and files the slice reads, with current ranges

- `task-cycle/record_template.md:176-195` Request handoff
- `foundations/decisions.md:4331-4362` WAY-153 (current range)
- `foundations/decisions.md:4707-4744` WAY-163 (current range)
- `foundations/decisions.md:8276-8340` WAY-269 (current range)
- `foundations/invariants.md:301-327` project-plan-state-evidence and project-plan-state-subprocesses
- `foundations/part_map.md:77-101` project-level and task-cycle
- `foundations/part_map.md:203-210` project-plan-state-command
- `project-level/test_plan_state_invariant.py:290-345` tests citing project-plan-state-evidence
