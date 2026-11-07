# Report of the one author — merge-review-questions

**Status:** done

## Commits and files

Base `52889bc700123b50258c4201835034f0529351df`; two commits on `task/merge-review-questions`, nothing pushed.

- `5932216` — `docs: record WAY-306 ... and WAY-307 ...`
  - `foundations/decisions.md` +69 −0 (two new entries before *Withdrawn identifiers*)
- `3601aba` — `docs: the merge review asks whether the two sides hold together, ...`
  - `task-cycle/skill/SKILL.md` +4 −2 (step 12, now at lines 415-420)
  - `task-cycle/skill/return_step.md` +4 −3
  - `task-cycle/skill/spec_review.md` +3 −2
  - `task-cycle/spec/SKILL.md` +2 −1
  - `task-cycle/spec/review.md` +2 −2
- `task-cycle/review/SKILL.md` is unchanged (`git diff task-cycle/review` is empty).

The wording of *To do* 1–4 is applied word for word; the text wraps differently from the task's quotes, the words are identical.

## Checks

| Command (from the worktree root) | Exit |
|---|---|
| `python -B elements/common/foundation_check.py` (before the entries: `0 errors`; after: `0 errors`) | 0 |
| `python -B gate/run_tests.py task-cycle` (151 tests, OK) | 0 |
| `python -B gate/run_tests.py elements/common` (109 tests, OK; tests of `foundation_check.py` and the migration) | 0 |
| own-work check script (below) | 0, six of six `True` |

Not run: `python -B gate/run_tests.py` (the whole gate; the orchestrator runs it, per the handoff).
No test written first: the change is prose of skills and foundation entries, which `make-change` section 2 does not test ("prose for people gets no test"; a text that instructs agents is tested by what an agent does with it, which is the reviewer's and the gate's reading). No invariant is written or changed.

## Own-work check

Requirement most likely unmet: the six quoted sentences of *To do* 1–4 are to appear word for word (a missed word, a leftover "or a term used against its entry", or a wrong target). Check: a short script (`python -I`) collapsed whitespace in each target file and tested that the exact quoted sentence is a substring. Result: all six `True`; and `grep -rn "against its entry"` over `foundations`, `elements`, `task-cycle` finds only the new sentence in `return_step.md`.

## Foundation entries

Both rows of *Settlements to record* are written whole through `record-decision`, as new decisions. The search of the whole foundation (WAY-33) found neither settlement already stated: searches for "hold together", "reconcil", "current target branch", "merge the current", "brought in", "spec-reviewed", "revis", "reviewed spec" in `foundations/*.md`, the elements and `task-cycle` show only WAY-162's mentions of the reconciliation (its ending, which stays) and the skill text itself. So no row is tied to an existing entry.

### WAY-306 — What does the review of the merge of the target branch ask?  (`row 1`, kind decision)

- English: Where merging the target branch changes the reviewed code, the dispatch of the merge review asks whether the two sides still hold together and names, by identifier, the foundation entries the merge brought in that bear on the parts the change touches, chosen by the orchestrator.
- Polish: Gdy scalenie gałęzi docelowej zmienia przeglądany kod, zlecenie przeglądu scalenia pyta, czy obie strony nadal do siebie pasują, i nazywa — po identyfikatorach — wpisy fundamentu przyniesione przez scalenie, które dotyczą części ruszanych przez zmianę; wpisy wybiera prowadzący cykl.
- Fields: Scope `task-cycle`; Based on `none`; Relations derives from WAY-150 · derives from WAY-162; Origin `none`.
- *Rejected* holds the three ways the row's source keeps (they stand in the row and in the task's *Context*): the reviewer of the merge choosing the entries; the question "whether the merge changed anything beyond conflicts"; the narrower question "whether the change still holds against what the merge brought in". The risk the human accepted (the reviewer may judge the change from the beginning; the commits of the merge are the boundary; a missed fault costs a correction after the request, an excess remark at most one round of a fix, WAY-162) stands in *Rationale* as the price taken. I wrote no count into the *Rationale* ("13 of 17 reports" of the task's *Context* is left out, since the template bars counts of the kind not being a measurement the choice rests on).

### WAY-307 — What happens to a spec whose review fails?  (`row 2`, kind decision)

- English: Where the review of a spec fails, the spec as reviewed stays beside it as `spec-reviewed.md`, and the reviewer of the revision compares the revision with it.
- Polish: Po odrzuceniu specu jego przejrzana wersja zostaje obok jako `spec-reviewed.md`, a recenzent poprawki porównuje obie wersje.
- Fields: Scope `task-cycle`; Based on `none`; Relations derives from WAY-135; Origin `none`.
- *Rejected* holds the two ways the row's source keeps: the designer told to change only what the findings ask (conflicts with the duty to remove contradictions the findings expose); the spec reviewer's method left without the copy (question 3's *Not chosen*).

### Choice named: new decisions rather than additions

The handoff allowed carrying a rule as an addition to WAY-162, WAY-135 or WAY-150. I chose new entries. Reason: the template's "Changing a decision" says a new rule beside an existing decision is a new question (WAY-19), and each row answers a question no entry answers. WAY-162 answers how a code review ends, WAY-150 who selects the reading, WAY-135 when a spec is written; none says what the merge review asks or what happens to a failed spec's text. The revise-once-review-once rule of `spec_review.md` is in no entry of the log (searched), so WAY-307's binding sentence does not restate it; it stays in the skill text. Way rejected: an addition to WAY-162 would put the dispatch's content into a decision about how reviews end. Cost if wrong: the reviewer of the whole change may ask to fold them into WAY-162/WAY-135, which means moving two entries and renumbering nothing (WAY-306 and WAY-307 have no referrers).

### Entries not written, and why

- *To do* 2 (term used against its entry): no entry. It aligns the skill with WAY-11, whose binding sentence names only a word used in a meaning for which WAY-95 gives an entry. WAY-11 is read and unchanged; the glossary needs no entry (task: "wpisu tu nie trzeba").
- Part map: the `task-cycle` entry lists `task-cycle/**`; no file added, moved or removed. Unchanged.
- No other entry names the changed sentences (searched).

## Reaches beyond the handoff

- `elements/decisions/skill/read.md`, `decide_entry.md`, `elements/common/way_of_working.md`, `elements/decisions/template.md`, `elements/decisions/examples.md`, `elements/common/rules.md`: read whole because the pinned `record-decision` skill names them (the handoff said to read the skill of the decision element when writing one). Not a gap.
- `task-cycle/review/SKILL.md` lines 1-50 and `task-cycle/skill/SKILL.md` lines 360-404: read selectively to ground WAY-306's "range of the merge the dispatch gives" and to confirm step 12's neighbours. The handoff named step 12's location only.
- Searched `foundations/decisions.md` and `foundations/invariants.md` (grep, passages read) for the WAY-33 search.

## Searches not found or unclear

- The handoff says the step-12 sentence is at `task-cycle/skill/SKILL.md:415-418`; it was (now 415-420 after the edit). The task's cited numbers (`389-391`, `:10-11`, `:6-7`, `:18-19`, `:18-20`) matched the files at the base commit for the four other targets, within a line or two. None unclear.
- A mismatch in the task text: *To do* 2 quotes a sentence that PR #75 changed; the answer to question 1 resolves it and I followed it. Not unclear.
- `elements/decisions/examples.md` names WAY-03 as the example; not read separately beyond the template and the entries read for the handoff (WAY-01, 11, 30 ... follow the same form). Recorded here in case the reviewer holds that reading was required.
- Otherwise: none.

## Problems observed

None. Note that the first Python heredoc of the entry insertion failed (`/tmp` path not visible to Windows Python), nothing was written by it; the second run wrote the entries. `foundation_check.py` printed `0 errors` both before and after, as the log shows.
