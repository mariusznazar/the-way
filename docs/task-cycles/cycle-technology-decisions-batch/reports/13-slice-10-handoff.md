# Handoff — slice 10

The person who requested this cycle delegated its intermediate choices to the orchestrator; no answer
here is that person's approval. You never ask the human: a question goes back to the orchestrator in
your report.

- Worktree (work only from its root): `the task's worktree root`, branch `task/cycle-technology-decisions-batch`. This is the-way itself; there is no pinned process.
- Your method and variant: `make-change` — read `task-cycle/change/SKILL.md` whole; your variant is **a slice, or the retry of a slice**, so read `task-cycle/change/slice.md` when the method sends you there. Read `agent-instructions/README.md` too.
- Stage and boundary: slice 10 of `.runs/task-cycles/cycle-technology-decisions-batch/plan.md` only. Change only the files of the slice's *Change* line; commit them with `git add <path>` (no `git add -A`); commit messages in English. Run the slice's *Checks* yourself (focused; never the full `python -B gate/run_tests.py` without a directory). The slice's *Model* sets your class.
- Frozen task (read whole): `.runs/task-cycles/cycle-technology-decisions-batch/task.md` (Polish). Plan: `.runs/task-cycles/cycle-technology-decisions-batch/plan.md` (your slice section is copied below word for word; the plan's *Foundation entries* and *Choices* are in the plan). No spec.
- Foundation entries already written in this cycle (commits `85c5395` .. `f3b90d5` on this branch, in `foundations/decisions.md`; the report is `.runs/task-cycles/cycle-technology-decisions-batch/reports/02-foundation-entries-report.md`): read the plan's *Foundation entries* table, then read the decisions your slice depends on in their current text. Row 1 is the **new decision WAY-322** (current range in the list below if your slice reads it); it covers every matter of an agent's way to the running product that the step lists — the base holds a fifth matter beyond the task's four, the place of the screenshots — and the failure notice; word your files to agree with it. WAY-165, WAY-166 and WAY-139 were reworded in place.
- Answers of step 4: trust boundary — no file of this slice is named as a trust boundary (the change as a whole touches one, in slice 3); irreversible operation — no.
- **Drift:** the task's line numbers and the plan's cite older commits; find each place by its content. Where the current text of a place already says what the item asks, change nothing there and say so in your report.
- Report path: `.runs/task-cycles/cycle-technology-decisions-batch/reports/13-slice-10-report.md` (full report as the method gives it, with the own-work check, **Searches not found or unclear**, reaches beyond this handoff, and each check with its command and exit code).
- Return: status, your commits, a one-line check result naming what failed or did not run, and the report path.

## The slice (plan section, word for word)

### Slice 10 — The instruction-files skill: names and emphasis

- **Goal:** (item 28) in `instruction-files/SKILL.md`, section "How to write a single rule": (a) a rule says that things are named in the words of the readers of the product, which now stands only in the mode of writing (`instruction-files/writing.md`, step 4); (b) the sentence on piled-on emphasis says what its source says — cautiously and about Claude, not categorically about every model. The source is the page named in the sentence (https://code.claude.com/docs/en/best-practices, § "What you can stop doing"): read that passage and word the sentence to say no more than it; where the page cannot be read, leave the sentence as it is and return the item as a question with the passage not found. `instruction-files/kind_main_file.md` cites the same page; report what it says there, change nothing in it. One rule keeps one place (the section's own bullet "A rule has one place"): word (a) so that the two files do not give two accounts.
- **Change:** `instruction-files/SKILL.md`
- **Read:** `.runs/task-cycles/cycle-technology-decisions-batch/task.md:75-77` To do, item 28 · `instruction-files/writing.md` · `instruction-files/kind_main_file.md:10-22` emphasis · `foundations/decisions.md:3313-3349` WAY-130 · `foundations/decisions.md:3414-3444` WAY-133 · `foundations/environment_facts.md:162-166` single-rule-compliance · `foundations/invariants.md:86-94` tracked-file-private-paths
- **Model:** cheaper
- **Risk:** none
- **Checks:** `python -B gate/run_tests.py instruction-files` · `python -B elements/common/foundation_check.py --skip-test-citations` · `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` · `git diff --check`
- **Depends on:** none

## Passages the slice reads

#### Task passage: To do, item 28 (task.md:75-77)

```text
28. Skill plików instrukcji (`instruction-files/SKILL.md`):
    - „How to write a single rule” mówi, że rzeczy nazywa się słowami czytelników produktu, co dziś stoi tylko w trybie pisania (`writing.md:14`) (theway#049-2);
    - zdanie o nadmiarze wyróżnień mówi tyle, co źródło — ostrożnie i o Claude, nie stanowczo o każdym modelu (theway#049-5; `:230-231`).
```

## Entries and files the slice reads, with current ranges

- `instruction-files/writing.md`
- `instruction-files/kind_main_file.md:10-22` emphasis
- `foundations/decisions.md:3317-3353` WAY-130 (current range)
- `foundations/decisions.md:3418-3448` WAY-133 (current range)
- `foundations/environment_facts.md:162-166` single-rule-compliance
- `foundations/invariants.md:86-94` tracked-file-private-paths
