# Handoff — slice 9

The person who requested this cycle delegated its intermediate choices to the orchestrator; no answer
here is that person's approval. You never ask the human: a question goes back to the orchestrator in
your report.

- Worktree (work only from its root): `the task's worktree root`, branch `task/cycle-technology-decisions-batch`. This is the-way itself; there is no pinned process.
- Your method and variant: `make-change` — read `task-cycle/change/SKILL.md` whole; your variant is **a slice, or the retry of a slice**, so read `task-cycle/change/slice.md` when the method sends you there. Read `agent-instructions/README.md` too.
- Stage and boundary: slice 9 of `.runs/task-cycles/cycle-technology-decisions-batch/plan.md` only. Change only the files of the slice's *Change* line; commit them with `git add <path>` (no `git add -A`); commit messages in English. Run the slice's *Checks* yourself (focused; never the full `python -B gate/run_tests.py` without a directory). The slice's *Model* sets your class.
- Frozen task (read whole): `.runs/task-cycles/cycle-technology-decisions-batch/task.md` (Polish). Plan: `.runs/task-cycles/cycle-technology-decisions-batch/plan.md` (your slice section is copied below word for word; the plan's *Foundation entries* and *Choices* are in the plan). No spec.
- Foundation entries already written in this cycle (commits `85c5395` .. `f3b90d5` on this branch, in `foundations/decisions.md`; the report is `.runs/task-cycles/cycle-technology-decisions-batch/reports/02-foundation-entries-report.md`): read the plan's *Foundation entries* table, then read the decisions your slice depends on in their current text. Row 1 is the **new decision WAY-322** (current range in the list below if your slice reads it); it covers every matter of an agent's way to the running product that the step lists — the base holds a fifth matter beyond the task's four, the place of the screenshots — and the failure notice; word your files to agree with it. WAY-165, WAY-166 and WAY-139 were reworded in place.
- Answers of step 4: trust boundary — no file of this slice is named as a trust boundary (the change as a whole touches one, in slice 3); irreversible operation — no.
- **Drift:** the task's line numbers and the plan's cite older commits; find each place by its content. Where the current text of a place already says what the item asks, change nothing there and say so in your report.
- Report path: `.runs/task-cycles/cycle-technology-decisions-batch/reports/12-slice-9-report.md` (full report as the method gives it, with the own-work check, **Searches not found or unclear**, reaches beyond this handoff, and each check with its command and exit code).
- Return: status, your commits, a one-line check result naming what failed or did not run, and the report path.

## The slice (plan section, word for word)

### Slice 9 — README: product guidelines and the host-state source

- **Goal:** (item 27) in `README.md`: the sentence on `product-guidelines/` says it holds the template, and the skill that leads the work on it, for each discipline of work for which the-way gives a template, as WAY-09 says (where the current sentence already says it, change nothing); the sentences on the sources a rule rests on (the list of what the foundation keeps and the row of `environment_facts.md` in the table of the five files) also cover the reading of the state of a host that the product's people run — the command, the host, the tool, its output and the date — as WAY-80 gives. The README binds nothing (WAY-09; the part map's "Files left out on purpose"), so no decision and no guarantee changes. Prose only.
- **Change:** `README.md`
- **Read:** `.runs/task-cycles/cycle-technology-decisions-batch/task.md:72-74` To do, item 27 · `.runs/task-cycles/cycle-technology-decisions-batch/task.md:126-126` Context · `foundations/decisions.md:219-296` WAY-09 · `foundations/decisions.md:1829-1868` WAY-80 · `foundations/glossary.md:49-53` environment fact · `foundations/glossary.md:121-125` read off · `foundations/invariants.md:86-94` tracked-file-private-paths
- **Model:** cheaper
- **Risk:** none
- **Checks:** `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` · `python -B elements/common/foundation_check.py --skip-test-citations` · `git diff --check`
- **Depends on:** none

## Passages the slice reads

#### Task passage: To do, item 27 (task.md:72-74)

```text
27. README:
    - zdanie o `product-guidelines/` mówi o szablonie i skillu dla każdej dyscypliny, dla której the-way daje szablon, jak WAY-09 (theway#025-29; `README.md:115-116`);
    - zdania o źródłach (`README.md:48-49`, `:75`) obejmują też odczyt stanu hosta, który ludzie produktu uruchamiają, jak WAY-80 (theway#047-2).
```

#### Task passage: Context (task.md:126-126)

```text
- README nie wiąże niczego (WAY-09, `foundations/part_map.md`, „Files left out on purpose”), więc punkt 27 nie zmienia gwarancji ani decyzji.
```

## Entries and files the slice reads, with current ranges

- `foundations/decisions.md:222-299` WAY-09 (current range)
- `foundations/decisions.md:1832-1871` WAY-80 (current range)
- `foundations/glossary.md:49-53` environment fact
- `foundations/glossary.md:121-125` read off
- `foundations/invariants.md:86-94` tracked-file-private-paths
