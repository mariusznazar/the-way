Return step of the one author, on head `41921006168c95b1de449ea546fab2271ec815e9`; one commit, `fb60dc7d`.

**Status:** done.

**Foundation compared with code.** Compared: the entries the change writes or changes (WAY-255, WAY-25, WAY-136, WAY-418, and the templates and skills of `decisions`, `part-map`, `environment-facts`), the decisions of the task's *Decisions in play* (WAY-229, 160, 12, 148, 339, 390, 18, 225) and the decisions of the foundation step's search (WAY-344, 365, 385, 150, 164, 406), the invariants whose sentences name the changed scripts (the one on absolute paths in tracked files, `gate-exit-code`, `command-runner-passes-exit-code`, `check-instructions-refuses-outside-links`, `function-and-file-size`), the glossary entries `slice` and `gate`, and the part-map entries of `task-cycle`, `elements-common`, `instruction-files`, `gate`, `decisions`, `part-map`, `environment-facts`, `installation`. My own search covered the names and words the code adds: `--decision` (found only in the script, its tests and `way_of_working.md`), `fits by ranges of`, `shutil.which`, `Ran <n> tests`, the levels `info` and `warn` of the instruction check, `size report`, `series`. Two mismatches found and corrected in the same change (commit `fb60dc7d`):
- `task-cycle/skill/planning.md` (the orchestrator's review of a plan) asked for "a size report in which every slice fits"; a slice reported `fits by ranges of <file>` is accepted as it stands, so it now reads "fits, by ranges of a file or not".
- `instruction-files/SKILL.md` step 1 listed what the `info` lines of the check say it left out; it now names also an absolute path of another machine and a path under a name the root `.gitignore` gives alone.
No mismatch found in the rest: the part-map entries still match the files (no file added or moved, no new dependency between parts: `decision_index.py` imports from its own part, `task-cycle` names `installation/README.md` and `elements/decisions/template.md`, both allowed; `decisions` no longer names a file of `task-cycle`); the invariant on absolute paths in tracked files and the one on gate times hold (their tests pass); the new series of gate times (WAY-339) is derived from the git history by the audit, and no file lists series, so nothing is written for it.

**Decisions written or changed.** None beyond the foundation step's: WAY-255, WAY-25, WAY-136 edited, WAY-418 new (rows 1–4). None of them carries a part held by a test: no test of the change holds a sentence of them by a line `decision:`, so each pair of examples stays whole. The lines `decision: WAY-344 ...` of the tests of `decision_index.py` hold sentences of WAY-344, which the change does not write; its *Verification* clause (a test that gives a file without a field) already covers them.

**Invariants written or changed.** None. No rule here is set by the task, a decision or the human as an invariant.

**Environment facts.** None. The change rests on no source outside the product that a decision's *Based on* or an invariant's *Rests on* would name (WAY-73): the behaviour of `shutil.which` on Windows is the code's own reliance, held by a test, and the Internet Archive text is a form in a template, not a citation.

**Glossary terms.** None: the change uses no word in a meaning for which WAY-95 gives an entry, and no term against its entry.

**Part-map changes.** None; the entries match the files (see above).

**Projected entries written whole or in part.** None; the task carries none.

**Rows of *Settlements to record* written (the place each went to).** Row 1 — a paragraph of WAY-255 (with *Rejected* rows, *Rationale*); row 2 — a paragraph of WAY-25 and the bullet of the template of decisions; row 3 — a sentence of WAY-136; row 4 — the new decision WAY-418 (end of the section "Instruction files"), with the README paragraph and the sentence of `task-cycle/review/whole_change.md`. All written by the foundation step; the return step wrote none further, and no choice that binds after the merge was left over (the choices of the author stand in `author-report.md` and its *Choices*, which WAY-36 leaves to the questions table).

Not fixed, as the handoff says: the Minor finding of the review of the fix (the comment at `instruction-files/check_instructions.py:454` writes the idiom as `'''`); it goes to the request's list.

**Checks run.** `python -B elements/common/foundation_check.py` exit 0 (`0 errors`), before and after the commit; `python -B instruction-files/check_instructions.py .` exit 0 (0 warn); `python -B gate/run_tests.py instruction-files` exit 0, `... agent-instructions` exit 0, `... product-guidelines` exit 0. The gate was not run.

**Unread material.** none beyond the earlier reports' lists: this step I read the handoff and `return_step.md` whole, and the entries above by search, not the whole of each invariant file.

**Searches not found or unclear.** none

**Working copies.** None made: I created no directory under `.runs/author-return/` and no worktree or clone; a temporary file `.runs/rs.txt` held three exit codes and was removed (`rm` by its path) before I returned.
