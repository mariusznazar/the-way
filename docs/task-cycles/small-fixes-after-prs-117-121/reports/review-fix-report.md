PASS eaf815c13c56c91b050ad436848c3cddaefb413b

# Review of the fix of the whole-change review — task `small-fixes-after-prs-117-121`

Fix range `e9aea95..eaf815c` (`b23275b`, `eaf815c`); `git rev-parse HEAD` = `eaf815c`, confirmed. Bounded
by the findings file `review-whole-findings.md` (I1, I2, m1–m8); `o1` was outside the scope and not fixed.

## Each finding

| Finding | State | Evidence |
|---|---|---|
| I1 — `„…”` not read as a quotation | **fixed** | `elements/common/foundation_check.py:164` now `[“„][^”]*”`; docstring `:79` and `elements/decisions/template.md:240` name `„…”`; the test loops over a third pair (`elements/common/test_foundation_check.py:1154`). With the old pattern restored in a worktree of the head, `-k full_stop` gave `FAILED (failures=1)`; with the fix, OK. The side effect the author names (`todo_item` and `unquoted` now mask `„…”` too) changes nothing in the-way: `git grep` finds no `„` in `foundations/`, `guidelines/` or `elements/` outside the three changed lines, and the check gives `0 errors`. |
| I2 — marks of WAY-139, WAY-344, WAY-60 | **fixed** (outside the commits, as the handoff says) | The corrected table in `author-fix-report.md:34-44` marks the three `the cycle's` and quotes the added clauses. I compared each quotation with `foundations/decisions.md` at `eaf815c`: WAY-139 `:4372-4374`, `:4382-4383`; WAY-344 `:2904-2906`, `:2914-2916`; WAY-60 complies (as changed by m1) `:1847-1849` and violates `:1853-1855` — all word for word. It stays for the orchestrator to carry the table into section 6 of the request. |
| m1 — WAY-60 example contradicting itself | **fixed** | The first example is back as it stood; the new one is an invariant of the-way citing WAY-309 of its own log in its sentence and in *Derives from* — the task's own case, with no tension with `elements/invariants/template.md:139-142`. |
| m2 — `availableModels` unqualified, no rule without a list | **fixed** | WAY-229 `:5950-5952` "(in Claude Code the setting `availableModels`; where the session has no such list, every model it offers)"; the same in `task-cycle/skill/SKILL.md:452-454` and `:503-505`. |
| m3 — harness behaviour stated as general | **fixed** | Rationale `:6031-6034` "got another model, in the one session observed the session's own"; *Rejected* `:6061` "got another model". |
| m4 — the switch run vs WAY-321's exemption | **fixed** | `task-cycle/plan/SKILL.md:178-182` "as the run right after the entry is written that WAY-321 exempts". |
| m5 — path in a product | **fixed** | the same sentence names `.the-way/elements/common/foundation_check.py` for a product. |
| m6 — no test with a changed citing file | **fixed** | New test `test_reworded_invariant_lacking_a_field_at_base_is_listed_though_its_citing_file_changed` (`elements/common/test_foundation_check.py:1606-1614`) touches `tests/test_saving.py` and expects one listed line naming *Method*; it would fail under the mutation I described (the author reports seeing it fail so). |
| m7 — descriptions broader than the code | **fixed** as to breadth; see n1 | `agent-instructions/README.md:15-18`, `elements/invariants/template.md:176`. |
| m8 — the list hanging on the guide sentence | **fixed** | `project-level/task/skill/resolve_gaps.md:91-93` ends "(WAY-139):" before the bullets; the pointer sentence stands after the list (`:114-116`), and its "the item of the first paragraph of this check" names the paragraph at `:80-88` that gives the guide. |

## New findings in the fix diff

### Critical / Important

none

### Minor, within the task

**n1 — The two descriptions of the base-copy listing now read narrower than the code.**
`agent-instructions/README.md:16-18` ("where such an invariant's copy at that commit lacks *Method* or *Part*,
it lists it naming the field") and `elements/invariants/template.md:176` ("and, naming the field, one of them
whose copy at the base lacks *Method* or *Part*"). "such an invariant" and "one of them" refer back to
invariants whose sentence was reworded *while no file citing them changed*; the code lists a base-lacking
invariant whether or not a citing file changed (`elements/common/foundation_check.py:740-747`), which the
new test of m6 now holds. A reader of either text would not expect the listing when a citing file changed.
Suggest "where the copy at that commit of an invariant whose sentence a change rewords lacks…", without the
citing-file condition. Blocks nothing.

### Outside the task's scope

none new. `o1` of the earlier review stands as it was.

## Declined to judge

- The long lines left in `foundations/decisions.md:5952` and `elements/decisions/template.md:241` — no
  formatter rule (WAY-382), no effect on a reader.

## Checks run

In a worktree of `eaf815c` at `.runs/review-fix/head`:

| Command | Exit | Result |
|---|---|---|
| `python -B gate/run_tests.py elements/common` | 0 | 246 tests OK |
| `python -B gate/run_tests.py agent-instructions` | 0 | OK (expected failures=2, as on the base) |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `QUOTED` set back to the `“`-only form, then `python -B -m unittest discover -s elements/common -p test_foundation_check.py -k full_stop` | 1 | `FAILED (failures=1)` — the `„` case catches I1; file restored with `git checkout`, pattern confirmed back |
| `git grep -n „ eaf815c -- foundations guidelines elements` (via a Python call) | 0 | 3 hits, all the fix's own lines |
| manual: each quotation of the corrected table against `foundations/decisions.md` at `eaf815c` | — | word for word |

Not run: the full gate (the orchestrator's). The m6 mutation was not repeated; the test's assertion
(`len(listed) == 1`) with the citing file touched is the case the mutation would break.

## Reaches beyond the dispatch

None beyond the fix range and the files its lines point to (`project-level/task/skill/resolve_gaps.md:80-88`
for m8's reference).

## Working copies

`.runs/review-fix/head` (worktree of `eaf815c`): removed with `git worktree remove --force` and `git worktree
prune`; its output files deleted; `.runs/review-fix/` stands empty. Remainder: none.

## Unread material

none — the fix diff, the findings file (as my own findings), the author's fix report and the corrected
table were read whole.

## Searches not found or unclear

none
