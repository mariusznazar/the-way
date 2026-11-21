# Handoff — the agent of the plan's *Foundation entries*

You write the foundation entries that the plan of this task lists, before any slice is made, in a task cycle of the-way. The person who requested the cycle has delegated every intermediate choice to the orchestrator; no answer you get is that person's approval. You never ask the human; questions go back to the orchestrator in your report.

- Worktree (your working directory for everything): `the worktree root`, task branch `task/small-fixes-from-ai-review-and-audit`, base `268b2b074691a331ed8db136343b4060bdd44539`. Start from its root. You commit on this branch and nowhere else.
- Method: `task-cycle/change/SKILL.md` (`make-change`), read whole, as the agent of the plan's *Foundation entries*: you take none of the rows of its table of variants; your stage is the foundation step. Read `task-cycle/skill/foundation_step.md` whole, and, when you write an entry of an element, the `SKILL.md` of that element at the path that file gives (a decision: `elements/decisions/skill/SKILL.md`), whole, and the files it names when the step that names them comes. The skill tool is not yours: a skill a file names is the `SKILL.md` whose frontmatter `name:` is that name, read as a file under the same root.
- Stage and boundary: write the three entries below and commit them; write no code and no test, change no file of the audit or of the cycle, and return before any slice is made. Slice 1 starts from your last commit.
- Report path: `.runs/task-cycles/small-fixes-from-ai-review-and-audit/reports/foundation-entries-report.md`. The report file is the input of the cycle's scripts (`task-cycle/remarks_check.py` reads it); write it there although its name could look like one Claude Code refuses a subagent to write; if the write is refused all the same, return the report whole as your answer.
- Your directory for working copies: `.runs/foundation-entries/` (under the worktree's ignored `.runs/`).
- `cycle.md` and the other files of the cycle's record directory — other agents' handoffs, reports and findings — are not yours to read, unless this handoff names them. The files named below are yours.
- Frozen task, whole: `.runs/task-cycles/small-fixes-from-ai-review-and-audit/task.md`. Plan: `.runs/task-cycles/small-fixes-from-ai-review-and-audit/plan.md`, its section *Foundation entries* (lines 7–13) and no more of it. Spec: none.
- Answers of the cycle's step 4: trust boundary yes (files of `task-cycle` and `process-audit` that the later slices change); irreversible operation no; open design choice none.
- Where the rows' settlements stand in the code: nowhere yet. The later slices make the code true to them: the image of each series and Q1 as numbers (slice 6), the comparison before and after a fix (slice 7), the text of `process-audit/SKILL.md` (slice 8). You write the entries; you do not describe code that does not exist, you state the rule it will keep.

## What you write (the task's rows, word for word, with the plan's *Foundation entries* rows that carry them)

The plan's *Foundation entries* holds three rows: row 1, a sentence added to WAY-339, its other sentences unchanged; row 2, a sentence added to WAY-339, its other sentences unchanged; row 3, a new decision. The task's *Settlements to record*:

```
Candidates: 7 shown, 3 accepted — 2026-11-21

| # | Settlement | Goes to | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Punkt 4 audytu pokazuje obraz każdej serii (to, co niesie jej rodzaj, ze wszystkich jej cykli, bez Q3 i bez „spada”; Q3 i „spada” tylko w porównaniach dwóch grup) oraz porównanie „przed i po zmianie” wewnątrz serii — cykle na wersjach z daną zmianą wobec cykli na wersjach bez niej, obie grupy w tej samej serii. | sentence of WAY-339 | *Questions to settle*: „Co pokazuje punkt 4 audytu zamiast samych wierszy per wersja?” | czy grupowanie po wersji wewnątrz serii wiąże dalej, czy jest tylko formą tego wyniku, którą późniejsza zmiana może zastąpić porównaniem po dacie |
| 2 | Porównanie „przed i po” dostaje każda naprawiona sprawa z rejestru problemów (z commitem poprawki). | sentence of WAY-339 | *Questions to settle*: „Które zmiany dostają porównanie »przed i po« wewnątrz serii?” | po jakich zmianach liczenie rozbiera serię: po każdym scaleniu, po liście prowadzonej ręcznie czy po poprawkach z rejestru |
| 3 | Odpowiedź Q1 dla każdej grupy cykli — wersji, obrazu serii i strony porównania — to liczby cykli (tak · nie · nieznane), a Q3 i „spada” stoją tylko tam, gdzie są dwie grupy. | decision | *Questions to settle*: „Jak wyglądają odpowiedzi Q1–Q3 dla grupy wielu cykli…?” | czy Q1 grupy brzmi `yes`, gdy jeden cykl daje `yes`, jak dziś dla wersji |
```

The answers they come from, in the task's *Questions to settle* (lines 56–74 of the frozen task): read them whole, with their *Not chosen* options and their *Source* lines, and take the *Rejected* of the new decision from the *Not chosen* of the question of row 3 and the *Source* line of its answer. The task's *Decisions in play*, for WAY-339 and WAY-350 (lines 111–112 of the frozen task):

```
- WAY-339 — dostaje zdania z wierszy 1–2 *Settlements to record*, bez zmiany tego, co już mówi; punkty 4–7 liczą w obrębie serii: „The audit compares each measure only within a series of its own kind, and judges a version of the process by the cycles that ran on it, never one week against another; […]”; poprawka z punktu 8 zaczyna nową serię czasów bramki: „a new series of those starts only with a change of the script that counts them or of the script that records them, and, for the times of the gate, also with a change of the test runner of the process”.
- WAY-350 — punkty 4–5 dokładają porównania czasów bramki ponad wersją, z tym samym ograniczeniem do przebiegów porównywanych: „The audit compares the times of the gate between versions of the process — the median of each version and whether it falls against the previous version of the same series — only over the runs that passed and during which no other such run was going, and shows the other runs apart.”
```

Constraints from the task, which bind your wording: *Out of scope* — WAY-84 is not changed and `elements/common/way_of_working.md` is not changed. WAY-339 keeps everything it says now; rows 1 and 2 add sentences, none is reworded, and the rule "Set no number of one series beside a number of another […] and no week's count beside the week before" that the task names (it stands in `process-audit/SKILL.md`, in the skill's rule "Measures are compared inside a series only") stays true: the entry you write about series must not say anything that contradicts it. The point 8 sentence of WAY-339 that the *Decisions in play* quotes (a new series of the gate times starts with a change of the test runner of the process) is already in WAY-339 or is a quotation of how it reads after the change of slice 2 — check it in the entry: where it already stands, add nothing for it; where it does not stand, the slice-2 change does not need it (it changes the script that counts the times, which WAY-339 already names as a start of a new series) and you add nothing for it either; say which in your report.

## What you read (the orchestrator's selection, WAY-150)

- The steps of `elements/common/way_of_working.md`, and the element's own `template.md`, `elements/common/rules.md`, examples and skill files that `elements/decisions/skill/SKILL.md` has you read.
- The decisions, each whole, as the range from its heading to the next heading in `foundations/decisions.md`: WAY-339, WAY-350, WAY-330, WAY-337, WAY-404, WAY-405, WAY-416 and WAY-385 (the last for the size of what you write), and the decisions your own search of the foundation (WAY-33) finds that the new decision touches. The index of the decisions of this work, for orientation only: `.runs/index.md` (it lists the decisions of the sections "Process audit", "Skills and agent types in sessions", "Environment facts" and "Scripts and the gate" and of the parts `process-audit`, `task-cycle`, `environment-facts`, `agent-instructions`, `gate`, `elements-common`, `project-level`, `product-guidelines` and `foundation-review`).
- The part map, whole (`foundations/part_map.md`); the glossary, whole (`foundations/glossary.md`); the invariants whose *Part* names `process-audit` or `task-cycle` or is `every`, and `audit-series-script-paths` and `audit-count-refuses-record-links` (`foundations/invariants.md`).
- `process-audit/SKILL.md` whole: it says today what point 4 of its step 3 shows and the rule "Measures are compared inside a series only" (lines 52–61); the decision must agree with both and the slices that follow change the skill to say what you write. You change none of it.
- `process-audit/audit_count.py` lines 1–80, its description of what the result gives (a docstring), to see the words the audit uses for a series, a version and Q1 to Q3. Read no more of the code.
- The checks of the form of the foundation: `python -B elements/common/foundation_check.py` (the-way's own check) after you write; it must report no error. Where it lists a decision over the length limits that you add or whose binding sentences you alter, cut it as the check says. Run no test and no gate.

## What you return

The usual foundation-step report: for each entry, one sentence of its meaning in English and one in the task document's language (Polish), and the mark `row <n>`, `projected` or `the cycle's`; the identifier of the new decision and the lines you changed in WAY-339; the search of the foundation of WAY-33 and its findings; each reach beyond this handoff; each working copy; **Unread material** and **Searches not found or unclear** sections (each `none` or the list). Commit each entry or all three in as many commits as you find clear, by path (`git add <path>`, never `git add -A`), with messages in English, and name the commits in the report.

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
