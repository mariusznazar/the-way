# Handoff — slice 4

The person who requested this cycle delegated its intermediate choices to the orchestrator; no answer
here is that person's approval. You never ask the human: a question goes back to the orchestrator in
your report.

- Worktree (work only from its root): `the task's worktree root`, branch `task/cycle-technology-decisions-batch`. This is the-way itself; there is no pinned process.
- Your method and variant: `make-change` — read `task-cycle/change/SKILL.md` whole; your variant is **a slice, or the retry of a slice**, so read `task-cycle/change/slice.md` when the method sends you there. Read `agent-instructions/README.md` too.
- Stage and boundary: slice 4 of `.runs/task-cycles/cycle-technology-decisions-batch/plan.md` only. Change only the files of the slice's *Change* line; commit them with `git add <path>` (no `git add -A`); commit messages in English. Run the slice's *Checks* yourself (focused; never the full `python -B gate/run_tests.py` without a directory). The slice's *Model* sets your class.
- Frozen task (read whole): `.runs/task-cycles/cycle-technology-decisions-batch/task.md` (Polish). Plan: `.runs/task-cycles/cycle-technology-decisions-batch/plan.md` (your slice section is copied below word for word; the plan's *Foundation entries* and *Choices* are in the plan). No spec.
- Foundation entries already written in this cycle (commits `85c5395` .. `f3b90d5` on this branch, in `foundations/decisions.md`; the report is `.runs/task-cycles/cycle-technology-decisions-batch/reports/02-foundation-entries-report.md`): read the plan's *Foundation entries* table, then read the decisions your slice depends on in their current text. Row 1 is the **new decision WAY-322** (current range in the list below if your slice reads it); it covers every matter of an agent's way to the running product that the step lists — the base holds a fifth matter beyond the task's four, the place of the screenshots — and the failure notice; word your files to agree with it. WAY-165, WAY-166 and WAY-139 were reworded in place.
- Answers of step 4: trust boundary — no file of this slice is named as a trust boundary (the change as a whole touches one, in slice 3); irreversible operation — no.
- **Drift:** the task's line numbers and the plan's cite older commits; find each place by its content. Where the current text of a place already says what the item asks, change nothing there and say so in your report.
- Report path: `.runs/task-cycles/cycle-technology-decisions-batch/reports/07-slice-4-report.md` (full report as the method gives it, with the own-work check, **Searches not found or unclear**, reaches beyond this handoff, and each check with its command and exit code).
- Return: status, your commits, a one-line check result naming what failed or did not run, and the report path.

## The slice (plan section, word for word)

### Slice 4 — The remarks script reads reports by name

- **Goal:** (item 8 and row 5) `task-cycle/remarks_check.py` reads as reports every `.md` file of `reports/` whose name holds neither `handoff` nor `findings`, in the order of their names; a handoff, a findings file and any file that is not `.md` are not read. The module docstring says it in the words item 8 gives, and its description of what an item of a section is says what the code does (a paragraph after a list is an item too), in the words item 8 gives. `test_only_files_whose_name_ends_in_report_are_read` in `task-cycle/test_remarks_check.py` becomes a test of the new rule with the files item 8 names: `review_whole.md` and `report-planner.md` are read; `01-author-handoff.md`, `handoff_author.md`, `slice-1-findings.md`, `notes.txt` and `gate.log` are not; write that test first and see it fail. Where no test pins that a paragraph after a list is read as an item, add one. In `task-cycle/skill/SKILL.md` the sentence that says where a stage's handoff stands in `reports/` says it is a file whose name holds `handoff`, and the sentence under "The process remarks check" that says which reports the script reads adds ", a file whose name holds neither `handoff` nor `findings`"; the script's exit codes stay as they are. The match on the names is a literal, case-sensitive match of the two words, as the settlement words it.
- **Change:** `task-cycle/remarks_check.py` · `task-cycle/test_remarks_check.py` · `task-cycle/skill/SKILL.md`
- **Read:** `.runs/task-cycles/cycle-technology-decisions-batch/task.md:37-41` To do, item 8 · `.runs/task-cycles/cycle-technology-decisions-batch/task.md:166-169` Settlements to record, header · `.runs/task-cycles/cycle-technology-decisions-batch/task.md:174-174` Settlements to record, row 5 · Foundation entries row 5 · `foundations/decisions.md:9235-9274` WAY-294 · `foundations/decisions.md:9275-9307` WAY-295 · `foundations/decisions.md:9308-9329` WAY-296 · `task-cycle/record_template.md:176-195` Request handoff · `foundations/invariants.md:86-94` tracked-file-private-paths
- **Model:** cheaper
- **Risk:** none
- **Checks:** `python -B -m unittest discover -s task-cycle -p "test_remarks_check.py"` (the rewritten test first fails, then passes) · `python -B gate/run_tests.py task-cycle` · `python -B elements/common/foundation_check.py --skip-test-citations` · `git diff --check`
- **Depends on:** Slice 1 · Foundation entries row 5

## Passages the slice reads

#### Task passage: To do, item 8 (task.md:37-41)

```text
8. Skrypt uwag (`remarks_check.py`) czyta raporty po nazwie tak, jak ustalił ai-review (AIR-607; theway#074, #075, #079, #080), a jego opis pozycji sekcji mówi to, co robi kod (AIR-617):
   - czyta wszystkie pliki `.md` z `reports/`, których nazwa nie zawiera `handoff` ani `findings`; docstring: „The reports are the `.md` files of `reports/` whose name holds neither `handoff` nor `findings`, read in the order of their names; a handoff, a findings file and a log are not read.” (`:12-13`, `:318`);
   - test `test_only_files_whose_name_ends_in_report_are_read` (`test_remarks_check.py:362`) sprawdza, że `review_whole.md` i `report-planner.md` są czytane, a `01-author-handoff.md`, `handoff_author.md`, `slice-1-findings.md`, `notes.txt` i `gate.log` nie;
   - `skill/SKILL.md:140` mówi, że zlecenie stoi w pliku `reports/`, którego nazwa zawiera `handoff`; `:474` dopisuje „, a file whose name holds neither `handoff` nor `findings`”;
   - opis pozycji sekcji w docstringu (`:26-27`) mówi to, co robi kod (`:165-168`) — akapit pod listą też jest pozycją (AIR-617; the-way PR #85, `define-project-skill-shape/cycle.md:174`): „The items of a section are its list items, each with the lines that continue it and its sub-items, and its paragraphs, a paragraph after a list included, so that nothing written in the section goes unread.”
```

#### Task passage: Settlements to record, header (task.md:166-169)

```text
Candidates: 8 shown, 5 accepted — 2026-11-08

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
```

#### Task passage: Settlements to record, row 5 (task.md:174-174)

```text
| 5 | Raportami etapu, które czyta skrypt uwag, są pliki `.md` z `reports/`, których nazwa nie zawiera `handoff` ani `findings`. | decision | punkt 8 *To do*; ai-review 2026-11-07, po krytyce, sprawdzone na sześciu kopiach zapisów cykli; Mariusz, 2026-11-08: „tak jak rekomendujesz” — na rekomendację agenta, by przyjąć wiersz, bo *Rejected* decyzji zachowa odrzucone drogi; nie wybrane: kod wyjścia 2 przy zerze raportów — nie łapie przypadku, gdy skrypt czyta część raportów, i przeczy `task-cycle/skill/SKILL.md:486` („Exit 2 is no listing: fix the call, or the file that could not be read”, `a3206c1`); linia `not read:` w wyniku skryptu — wygląda jak pozycja do dopisania | czy dopisać regułę nazw do WAY-294, czy zostawić ją w skillu i docstringu skryptu |
```

## Entries and files the slice reads, with current ranges

- Foundation entries row 5
- `foundations/decisions.md:9285-9336` WAY-294 (current range)
- `foundations/decisions.md:9337-9369` WAY-295 (current range)
- `foundations/decisions.md:9370-9391` WAY-296 (current range)
- `task-cycle/record_template.md:176-195` Request handoff
- `foundations/invariants.md:86-94` tracked-file-private-paths
