# Return step — guidelines-no-inventory

Saved by the orchestrator from the author's returned text (a subagent may not write report files).

Status: done. The return step changed nothing, so no commit was made. The head is still `ae5dff6` and the worktree is clean.

**Commits:** none.

## Foundation compared with the repository

- **WAY-312** (`foundations/decisions.md`):
  - Sentence 1 matches the new bullet in `product-guidelines/template.md` ("A rule lists no state and repeats no decision or value"). That bullet's exemption is the `### Logging scope` list only, as WAY-274 gives it.
  - Sentences 2 and 3 bind the editors and the skills. The template needs no further text for them, because row 2 asked only for the one sentence in it.
  - *Scope* `product-guidelines` is the part whose files carry the rule. *Relations* are WAY-168, WAY-225 and WAY-173, and nothing contradicts them.
- **Fact `shorter-guidelines-trial`** (`foundations/environment_facts.md`):
  - Both *Source* passages still occur word for word in `request.md` at `9c0dfc8faa7b3024dfa1e488b18b955f087b57a0`, read from the local clone with `**` dropped. A Python check printed `2 [True, True]`.
  - The sentence says no more than the passages. The repository name stands only in the fact's *Source* line (`git grep -i loop2` outside `.runs` gives 1 match).
- **Decisions the task names:**
  - **WAY-168, WAY-171, WAY-173, WAY-213, WAY-271:** consistent. The template bullet adds to WAY-168 and WAY-171 and conflicts with none of them.
  - **WAY-169 and WAY-172:** consistent. No rule of the-way's own guidelines names an entry that changed, since the-way has no `guidelines/`.
  - **WAY-100:** consistent, and WAY-312's *Rationale* cites it correctly.
  - **WAY-130:** *Scope* (`instruction-files, agent-instructions`) needs no change. It governs rules in the-way's own instruction files, not the shared template of product guidelines.
- **Entries the search found:** WAY-225, 170, 221, 251, 278, 279 and WAY-274 to 276 need no correction. The "copy no value" bullets in the coding and testing templates agree with the new bullet.
- **Part map:**
  - **`decisions`:** files `elements/decisions/**` and `foundations/decisions.md`. Responsibility and dependencies are unchanged.
  - **`environment-facts`:** files `elements/environment-facts/**` and `foundations/environment_facts.md`. Responsibility and dependencies are unchanged.
  - **`product-guidelines`:** responsibility ("the form every product's guidelines share, ...") already covers the template bullet. No file moved, and no new dependency or surface.
  - **Conclusion:** no map entry changes.

## Decisions written or changed

- WAY-312, written by the foundation step in `cd9d5af` and corrected in `6df733c` and `ae5dff6`.
- No other decision is written or changed in this step.

## Invariants

- None written. No invariant is set by the task, a decision or the human; WAY-312 names none in *Verification*.

## Environment facts

- `shorter-guidelines-trial`, written in `6df733c` and corrected in `ae5dff6`. It is the only outside source the change rests on, and WAY-312's *Based on* names it.
- No other source outside the product is missing from the foundation.

## Glossary terms

- None. The words used in non-ordinary senses are "guidelines", "decision" and "environment fact", all used as their entries give them. "State", "arm", "case" and "promise" are ordinary words and need no WAY-95 entry. No term is used against its entry.

## Part-map changes

- None.

## Projected entries

- None. The task is independent and no project definition projects entries into it.

## Rows of *Settlements to record*, each confirmed written

| Row | Written as |
|---|---|
| 1 | WAY-312, sentences 1 and 2, with the *Verification* examples |
| 2 | WAY-312, sentence 3 (the product's own task cleans existing guidelines; the skills get no search step), and the bullet "A rule lists no state and repeats no decision or value" in `product-guidelines/template.md` |
| 3 | Environment fact `shorter-guidelines-trial`, named in WAY-312's *Based on* |

None was missed.

## A choice that binds after the merge (WAY-36)

- None. Every choice of the change is in a row or in a review finding, and the task excludes none.

## Checks

| Command | Exit |
|---|---|
| `python -B elements/common/foundation_check.py` (worktree root) | 0 ("0 errors") |
| Python substring check of both *Source* passages against `git -C the local clone of the game repository show 9c0dfc8:docs/task-cycles/proba-krotszych-wytycznych/request.md` | both found |

Not run: `gate/run_tests.py` (the orchestrator's, passed on `ae5dff6`) and focused tests (no file with tests changed).

## Left alone, as the handoff said

- The 130-character line near line 9822 of `foundations/decisions.md`.
- Whether sentence 2 of WAY-312 should mention the WAY-173 route.

Both stay for the request's list.

## Searches not found or unclear

- None.
