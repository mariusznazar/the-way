# Report — the one author, guidelines-no-inventory

Saved by the orchestrator from the author's returned text: the harness forbids a subagent to write
report files (the author's first attempt was rejected: "Subagents should return findings as text, not
write report files."). The first return was status `blocked` for the source of row 3 (below, "First
return"); the text after it is the final report returned after the orchestrator's answer.

## First return (status `blocked`, commit `cd9d5af`)

Blocked on row 3: the environment fact needed the passage of request #68 of the product `loop2`
word for word, its address and the date read, and the environment-facts template offers no clean form
for a private repository's request. The author recommended the page-without-editions form without an
archive, or dropping row 3 and keeping the measurement in WAY-312's *Rationale* with *Based on* `none`.
Its **Searches not found or unclear** then: "The source of the fact is unavailable to this cycle, and
the template has no clean form for a private request (above)." · "The handoff says both "return
`blocked`" and "commit what you have". I committed WAY-312 and the template bullet with *Based on*
`none`. If you prefer WAY-312 to wait for the fact, reset `cd9d5af`."

## Final report (status `done`)

**Worktree:** `.runs/worktrees/guidelines-no-inventory`, branch `task/guidelines-no-inventory`, base `deded3f`.

**Commits**
- `cd9d5af` Keep state and repetitions of decisions out of a product's guidelines (WAY-312 and the template bullet).
- `6df733c` Record the shorter-guidelines trial as an environment fact (the fact; WAY-312 *Based on* and *Rationale* updated).

**Files changed** (total +65, no removals)
- `foundations/decisions.md`: +54 lines, new WAY-312 before `## Withdrawn identifiers`. WAY-312 is the next free number.
- `foundations/environment_facts.md`: +6 lines, new entry `shorter-guidelines-trial`.
- `product-guidelines/template.md`: +5 lines, one bullet in "Required form".

### Entries

| Entry | Mark | English | Polish |
|---|---|---|---|
| WAY-312 `foundations/decisions.md` | row 1, plus the part of row 2 on the product's own cleaning task and the skills getting no search step | The shared template holds that a rule of a product's guidelines lists no state of the code or the product and repeats neither a decision nor a configuration value. Known-practice sentences and derivable cases are neither renamed nor taken out. A product's own task cleans existing guidelines, and the skills get no search step. | Wspólny szablon mówi, że reguła wytycznych produktu nie spisuje stanu kodu ani produktu i nie powtarza decyzji ani wartości z konfiguracji. Zdań znanej praktyki i przypadków wyprowadzalnych z celu nie zamienia się na nazwę ani nie zdejmuje. Istniejące wytyczne czyści zadanie produktu, a skille wytycznych nie dostają kroku ich szukania. |
| Bullet "A rule lists no state and repeats no decision or value" in `product-guidelines/template.md` | row 2 | A rule does not list the state of the code or the product and repeats neither a decision nor a configuration value. A list that is the product's promise is no such state. | Reguła nie spisuje stanu kodu ani produktu i nie powtarza decyzji ani wartości z konfiguracji. Lista będąca obietnicą produktu nie jest takim stanem. |
| `shorter-guidelines-trial` `foundations/environment_facts.md` | row 3 | The report of a trial of a shorter guidelines file in one product says all 45 runs of three tasks with hidden tests passed (five per task per arm: old file, shorter file, no file), and gives one model, Sonnet 5.5, for every stage of the cycle that ran it. | Raport próby krótszego pliku wytycznych w jednym produkcie mówi, że wszystkie 45 przebiegów trzech zadań z ukrytymi testami przeszło (po pięć na zadanie i wariant: stary plik, krótszy, brak pliku) i podaje jeden model, Sonnet 5.5, dla każdego etapu cyklu, który prowadził próbę. |

### Checks

| Command | When | Exit |
|---|---|---|
| `python -B elements/common/foundation_check.py` (worktree root) | after the first edits, before `cd9d5af` | 0 ("0 errors") |
| `python -B elements/common/foundation_check.py` (worktree root) | after the fact and the WAY-312 update, before `6df733c` | 0 ("0 errors") |
| `git -C the local clone of the game repository show 9c0dfc8:docs/task-cycles/proba-krotszych-wytycznych/request.md` (read only) | source read | 0 |
| A Python substring check that both quoted passages occur word for word in that file with `**` markup dropped | before writing the fact | both found |

- `git rev-parse 9c0dfc8` printed `9c0dfc8faa7b3024dfa1e488b18b955f087b57a0`, the full SHA used in the address.
- Not run: `gate/run_tests.py` (the orchestrator's) and focused tests (no changed file has tests).

### Own-work check

- **Requirement most likely unmet:** the fact's sentence says no more than its source says, and WAY-312's *Rationale* matches it.
- **First run, finding the gap:** the first *Rationale* draft carried claims the cited passages do not give: "the tests do not see the file", "the code carries the behaviour", and that the shorter text "named practices and left out derivable cases".
- **Fix:** the *Rationale* was rewritten in `6df733c`. It now states only the 45 of 45 result, the three arms and the model.
- **Second run, after the fix:** two conclusions in it are the author's own derivations from the fact and are marked as such: that a passing no-file arm means the tests cannot tell whether the file is followed, and that a pass rate near 55% still gives five of five about once in twenty sets (0.55^5 ≈ 0.05).
- **Name check:** `git grep -i loop2` outside `.runs` finds the repository name only in the fact's *Source* line, as the orchestrator required.
- **Contradiction check:** no contradiction with WAY-274 (the `### Logging scope` list is a promise, not an inventory) or WAY-171 (`## Where in code` copies no value). The coding and testing templates' "copy no value" bullets stay consistent.

### Search of the whole foundation (way_of_working step 2), re-run after the fact

- Searched the decision log by words and by every decision whose *Scope* names `product-guidelines`, plus the part map, invariants, glossary, environment facts, `product-guidelines/**` and `task-cycle/review/SKILL.md`.
- Read whole: WAY-168, 169, 171, 172, 173, 213, 130, 100, 271–276, plus WAY-225, 170, 221, 251, 278 and 279 from the search.
- **WAY-130 *Scope*** (`instruction-files, agent-instructions`) is unchanged. WAY-130 governs rules in the-way's own instruction files, not the shared template of product guidelines, and it already lets a rule that carries a decision stand.
- Nothing else names `shorter-guidelines-trial`, other than WAY-312's *Based on*.
- No invariant has *Part* `product-guidelines`. The glossary term "guidelines" is used in its own meaning. The part map entry `product-guidelines` is unchanged.
- No other correction found. The review skill and the discipline templates reach the new rule through the shared template.

### Reaches beyond the dispatch

- Read WAY-225, 170, 221, 251, 278 and 279 (found by the search) and `product-guidelines/coding/template.md` and `coding/settle.md` (search hits).
- For the source, the `loop2` request through the local clone, as the orchestrator's message said.

### Choices

- **Fact source:** the form "edition with the publisher's own address": the file at the full commit SHA. Two passages of one page, from "What you will see" (the whole bullet) and from "Cost" (the sentence naming Sonnet 5.5), `read 2026-11-08`. No archived copy, because the template does not ask for one for this form.
- **Fact identifier:** `shorter-guidelines-trial` names the topic, not the value. It is unique across the three files.
- **Fact sentence:** does not name the repository; says "one product"; says "a shorter guidelines file", not "coding guidelines", because the quoted passages do not say "coding".
- **WAY-312 *Based on*** is now `shorter-guidelines-trial` (it was `none` in `cd9d5af`).
- **WAY-312 *Rejected*** holds only the "Not chosen" ways of the task's questions 5 and 7, each with its cost. The cost figures (about 2¼ hours, 119 million tokens) are the task's.
- **WAY-312 *Scope*** is `product-guidelines`; *Relations* derives from WAY-168 · WAY-225 · WAY-173; *Origin* is `none`, because the task document is removed with the cycle.
- **Template bullet:** adds the examples "endpoints the code has today" and "version of a tool", and the promise-list exemption citing WAY-274. These come from the task's Context and *To do*, not from the row.

### Concerns

- **Private repository in a published file:** the fact's *Source* line names a private GitHub repository and its request file. The orchestrator approved this and said to name the repository nowhere else. Anyone without access to the repository cannot open the address.
- **WAY-308 / WAY-309:** `private_paths_check.py` was not run on the changed files. The address is a URL, not an absolute path or a note title.

### Searches not found or unclear

- None remain open for the foundation entries. The earlier gaps are closed: the source is read and the form is settled by the orchestrator.
- The check command in the handoff (`foundation_check.py`) does not verify that the cited address opens. The passages were verified against the local clone at the full SHA only, not against GitHub.
