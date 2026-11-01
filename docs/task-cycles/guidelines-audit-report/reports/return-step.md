# Return step — guidelines-audit-report

**Status:** done

One correction, one commit: `aee18e4` — docs: WAY-281 names the rules that block, as the trial run gives them. Base of the step `0ee0cd9`, not pushed, tree clean.

## Foundation compared with code

Compared with the files at `0ee0cd9`, reading each entry's binding sentences, *Verification* and *Rationale* against the file that carries it.

| Entry | Compared with | Result |
|---|---|---|
| WAY-280 | `product-guidelines/audit_end.md`, "Weigh", opening | matches |
| WAY-281 | `audit_end.md`, "Merge into causes"; `coding/trial_run.md:21-24`; `testing/audit.md:14-18` | **disagreed, corrected**, below |
| WAY-282 | `audit_end.md`, "Order", "A task joining code and tests" | matches |
| WAY-283 | `audit_end.md`, "The top of the list", "The list"; `coding/kinds.md:19-21` | matches |
| WAY-284 | `audit_end.md`, "At step 4"; `guideline_findings.md`, "A deferred cause of an audit"; the three `hand_back.md` | matches |
| WAY-285 | `audit_end.md`, "Go back", "The list" | matches |
| WAY-187 | `styleguide/audit.md` | matches |
| WAY-201 | `coding/kinds.md`, `coding/trial_run.md` | matches |
| WAY-250 | `testing/audit.md` | matches |
| Named by the task: WAY-200, WAY-204, WAY-205, WAY-216, WAY-235, WAY-247, WAY-251, WAY-174, WAY-173, WAY-120, WAY-256, WAY-100, WAY-27, WAY-30, WAY-24, WAY-26, WAY-51, WAY-161 | the files of the change | match; none needs a change |
| Found by the search: WAY-215, WAY-219, WAY-172, WAY-199, WAY-207, WAY-265, WAY-36 | the files of the change | match; none needs a change |
| Part map: `product-guidelines`, `project-level`, `decisions` | the changed files | match, below |

**The one disagreement, by my own comparison.** The review's finding 4 names the same place; I do not act on the finding, and the review grades it Minor on reading the entry together with the glossary and WAY-203. The comparison on its own:

- WAY-281 said the list holds "the rules of a linter's set broken for one reason".
- `coding/trial_run.md:21-24` says "the rules that block" enter, and "The rules that went among the examples flagged sound code and yield no cause."
- So an agent comparing work with the entry alone finds the audit leaving out reports of a set's rule that the entry's words reach, and the file's sentence is the reviewed spec's decision 11. The file is right and the entry was wider.

I corrected the entry to "the rules of a linter's set that block, broken for one reason". The other Minor findings are not entry-and-file disagreements and stand for the request. Finding 5 is one between the files and the task's example: WAY-280 and `audit_end.md` agree with each other, so the comparison gives nothing to correct.

**The part map's sentence on `product-guidelines`:** no change. It names "the template of each discipline of guidelines with the skill that leads the work on them" and "the shared reading". `audit_end.md` is the end of those skills' audits, read only by them, so it falls under the skill that leads the work. The shared reading is named on its own because other workflows use it, which is not so of this file. The sentence stays true and whole, and `product-guidelines/**` holds the file. The sentence on `project-level` covers the new section as refinement of a task. *Depends on* of both parts already names the other. `decisions` is unchanged.

**"Weight" in WAY-13:** no change and no entry. WAY-13 asks what sets the weight of a task's process, how much process a change gets, and the audits' weight says how serious a cause is. Those are two meanings, and each is one a reader who knows the field gives the word, so `elements/glossary/template.md:42-43` gives no entry "however many meanings it has", and the renaming of WAY-99 reaches only a meaning such a reader would not give.

## Written or changed

- **Decisions:** WAY-281 changed in place. WAY-280, WAY-282 to WAY-285, WAY-187, WAY-201 and WAY-250 unchanged by this step.
- **Invariants:** none. No rule of the task, a decision or the human asks for one.
- **Environment facts:** none. The course stands in WAY-280's *Rationale*, described and with `Based on: none`, as the spec gives and as WAY-273 stands.
- **Glossary terms:** none. `finding`, `cause` and the four weights keep the spec's reading; no word of the change stands against a term's entry, `debt` in WAY-281 included, since the rules that block are rules the product's foundation holds.
- **Part-map changes:** none.
- **Projected entries written whole or in part:** none; the task is independent.

## Rows of *Settlements to record* written

| Row | Identifier | By which step |
|---|---|---|
| 1 | WAY-280 | foundation step |
| 2 | WAY-281 | foundation step, corrected here |
| 3 | WAY-282 | foundation step |
| 4 | WAY-283, with WAY-187, WAY-201 and WAY-250 changed | foundation step |
| 5 | WAY-284 | foundation step |
| 6 | WAY-285 | foundation step |

No row was missed.

## Choices that bind after the merge

The spec's decision 2, how a fix shows its cost, and decision 9, how the top fills up to five, stand as text of `audit_end.md`, inside the bounds WAY-282 and WAY-283 state. The spec's *Foundation entries* says "No other entry", so I wrote none. They are the two I would look at first if a reader holds that either binds as a decision.

## Meaning where the step changes it

- **WAY-281** (row 2): Kilka naruszeń z jednego źródła to jedna przyczyna i jedna naprawa, a przyczyna niesie swoje miejsca; spis obejmuje też granicę zaufania, na której test odmowy jest należny i go nie ma, oraz reguły lintera, które blokują, łamane z jednego powodu, opisane skutkiem, z liczbą plików i bez nazw reguł, a ponowne formatowanie nie jest ustaleniem.

The change keeps row 2's meaning, since a rule among the examples binds no code and so nothing breaks it. No question goes to the human under `foundation_step.md`.

## Checks

Run after the last commit, `aee18e4`, with no commit landing during a run, `HEAD` the same before and after; each exit code taken from the command itself, through no pipe.

| Command | Exit code |
|---|---:|
| `python -B elements/common/foundation_check.py .` | 0 |
| `python -B gate/run_tests.py elements/common` | 0 |

Not run: the full gate, as the handoff gives; any other directory, since the commit changes one sentence of the log and no other test reads its wording.

## Searches not found or unclear

- **Whether the two choices above bind as decisions:** unclear; the return step's "a choice that binds after the merge" and the spec's "No other entry" pull apart a little, and I followed the spec.
- **Finding 3's reach into `coding/recognize.md`:** the wording is the review's Minor finding and I left it. I name it because no entry disagrees with it: WAY-278 says what a refresh proposes and not which skill's step puts it.
- **WAY-284's complies example** reads "the backlog of an independent task"; the backlog is the product's. It matches the file in meaning, so I left it.
- **The Glob tool** was not used here; the comparisons rest on `git grep`, `grep` and whole reads.
