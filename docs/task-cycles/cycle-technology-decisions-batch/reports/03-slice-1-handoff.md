# Handoff — slice 1

The person who requested this cycle delegated its intermediate choices to the orchestrator; no answer
here is that person's approval. You never ask the human: a question goes back to the orchestrator in
your report.

- Worktree (work only from its root): `the task's worktree root`, branch `task/cycle-technology-decisions-batch`. This is the-way itself; there is no pinned process.
- Your method and variant: `make-change` — read `task-cycle/change/SKILL.md` whole; your variant is **a slice, or the retry of a slice**, so read `task-cycle/change/slice.md` when the method sends you there. Read `agent-instructions/README.md` too.
- Stage and boundary: slice 1 of `.runs/task-cycles/cycle-technology-decisions-batch/plan.md` only. Change only the files of the slice's *Change* line; commit them with `git add <path>` (no `git add -A`); commit messages in English. Run the slice's *Checks* yourself (focused; never the full `python -B gate/run_tests.py` without a directory). The slice's *Model* sets your class.
- Frozen task (read whole): `.runs/task-cycles/cycle-technology-decisions-batch/task.md` (Polish). Plan: `.runs/task-cycles/cycle-technology-decisions-batch/plan.md` (your slice section is copied below word for word; the plan's *Foundation entries* and *Choices* are in the plan). No spec.
- Foundation entries already written in this cycle (commits `85c5395` .. `f3b90d5` on this branch, in `foundations/decisions.md`; the report is `.runs/task-cycles/cycle-technology-decisions-batch/reports/02-foundation-entries-report.md`): read the plan's *Foundation entries* table, then read the decisions your slice depends on in their current text. Row 1 is the **new decision WAY-322** (current range in the list below if your slice reads it); it covers every matter of an agent's way to the running product that the step lists — the base holds a fifth matter beyond the task's four, the place of the screenshots — and the failure notice; word your files to agree with it. WAY-165, WAY-166 and WAY-139 were reworded in place.
- Answers of step 4: trust boundary — no file of this slice is named as a trust boundary (the change as a whole touches one, in slice 3); irreversible operation — no.
- **Drift:** the task's line numbers and the plan's cite older commits; find each place by its content. Where the current text of a place already says what the item asks, change nothing there and say so in your report.
- Report path: `.runs/task-cycles/cycle-technology-decisions-batch/reports/03-slice-1-report.md` (full report as the method gives it, with the own-work check, **Searches not found or unclear**, reaches beyond this handoff, and each check with its command and exit code).
- Return: status, your commits, a one-line check result naming what failed or did not run, and the report path.

## The slice (plan section, word for word)

### Slice 1 — The cycle skill's merge, base-check and exception sentences

- **Goal:** `task-cycle/skill/SKILL.md` and `task-cycle/skill/correction.md` say, each place found by its content: (item 1) the correction's merge of the remote target branch — both places in `correction.md` that merge it — does there what step 12 does with its merge: where the merge changes code the cycle reviewed, a fresh reviewer reviews the merge with `review-change` as step 12 gives (WAY-306), and the checks the merge touches run again; (item 2) step 12 merges the remote target branch, not "the current target branch", as `correction.md` and WAY-298 give, in a product too; (item 3) the sentence "The cycle writes only in the task's worktree and changes nothing outside the product repository" names as its exception the fast-forward of the checkout in step 4, and the paragraph does not end with two things each called "the one exception"; (item 5) step 4's second way of running the base checks, a separate copy of the base commit under the worktree's ignored `.runs/`, says that in a product the copy gets its dependencies installed, as the product's own rules give, and its `.the-way` populated before the checks run, since otherwise they fail for that reason and not on the base. Prose only; no other rule changes.
- **Change:** `task-cycle/skill/SKILL.md` · `task-cycle/skill/correction.md`
- **Read:** `.runs/task-cycles/cycle-technology-decisions-batch/task.md:28-30` To do, items 1 to 3 · `.runs/task-cycles/cycle-technology-decisions-batch/task.md:32-32` To do, item 5 · `foundations/decisions.md:9370-9425` WAY-298 · `foundations/decisions.md:9675-9715` WAY-306 · `foundations/invariants.md:86-94` tracked-file-private-paths
- **Model:** cheaper
- **Risk:** none
- **Checks:** `python -B elements/common/foundation_check.py --skip-test-citations` · `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` · `python -B gate/run_tests.py task-cycle` · `git diff --check`
- **Depends on:** none

## Passages the slice reads

#### Task passage: To do, items 1 to 3 (task.md:28-30)

```text
1. Poprawka po uwagach człowieka, scalając gałąź docelową, robi przy tym to, co krok 12: gdzie scalenie zmienia zrecenzowany kod, świeży recenzent recenzuje scalenie, a sprawdzenia, których scalenie dotyka, biegną znowu (theway#022-1; `skill/correction.md:26-27` wobec `skill/SKILL.md:415-417`).
2. Uzgodnienie przed otwarciem PR-a w kroku 12 scala zdalną gałąź docelową, jak poprawka (`correction.md:26`) i jak uzasadnia WAY-298 (theway#076-4; `skill/SKILL.md:416`).
3. Zdanie „The cycle writes only in the task's worktree” wymienia jedyny wyjątek, przewinięcie gałęzi docelowej z kroku 4 (theway#076-2; `skill/SKILL.md:68` wobec `:116-117` i WAY-298).
```

#### Task passage: To do, item 5 (task.md:32-32)

```text
5. Druga droga sprawdzeń bazy — osobna kopia bazy pod `.runs/` — mówi, że w produkcie trzeba w tej kopii przed sprawdzeniami zainstalować zależności i wypełnić `.the-way`, bo inaczej sprawdzenia padają z tego powodu, a nie na bazie (theway#061-2; `skill/SKILL.md:125-127`).
```

## Entries and files the slice reads, with current ranges

- `foundations/decisions.md:9432-9487` WAY-298 (current range)
- `foundations/decisions.md:9737-9777` WAY-306 (current range)
- `foundations/invariants.md:86-94` tracked-file-private-paths
