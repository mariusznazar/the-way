# Fix — guidelines-audit-report

**Status:** done

One commit on the reviewed head `aee18e4`: `ccb20de` — docs: the audit's end takes the trial run's reports of the rules that block, as WAY-281 gives. Not pushed, tree clean.

| File | Added | Removed |
|---|---:|---:|
| `product-guidelines/audit_end.md` | 3 | 3 |

The three lines are one clause and its rewrapping. No entry changed.

## The blocking finding

**1. The correction gives WAY-281 a qualification that `audit_end.md` repeats the entry without: fixed.**

- **Held right.** At `aee18e4` `product-guidelines/audit_end.md:15` read "the trial run's reports", and the next section has every finding merged into a cause, while WAY-281 and `coding/trial_run.md:21-24` take only the rules that block. My return step compared WAY-281 with "Merge into causes" and not with the file's opening, so it missed this line.
- **How.** The clause now reads "the trial run's reports of the rules that block", as the finding gives.
- **The check that shows it.** A `git grep` for `trial run` and `reports` over `audit_end.md` and the coding skill's `SKILL.md`, `kinds.md`, `task_document.md` and `hand_back.md` shows line 15 with the qualification, and no other line saying what enters the list. `audit_end.md:107` speaks of the reports behind a cause's number, and `coding/task_document.md:44` of the trial run's evidence, which covers each rule by design.

## Checks

Run after the commit `ccb20de`, with no commit landing during a run, `HEAD` the same before and after; each exit code taken from the command itself, through no pipe.

| Command | Exit code |
|---|---:|
| `python -B elements/common/foundation_check.py .` | 0 |
| `python -B gate/run_tests.py elements/common` | 0 |
| `git diff --check aee18e4 HEAD` | 0 |

Not run: the full gate, as the handoff gives; any other directory, since the commit changes one clause of a Markdown file no test reads.

## Not fixed

The review's Minor findings 2 and 3 are not this fix's, as the handoff and WAY-161 give. `audit_end.md:131`, "for a linter's rules the number of files", stays: the review reads it as the label of a kind of cause, outside finding 1, and I read it so too.

## Searches not found or unclear

none
