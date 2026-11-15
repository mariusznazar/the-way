PASS 0e3cb2a6807d36a50613d07ed90552a968b6bf00

# Review of correction 2, second part (`repository` allowed for `agent-instructions`)

Range `cde07dd..0e3cb2a`, one commit (`0e3cb2a`, parent `cde07dd`). `git rev-parse HEAD` in my
worktree: `0e3cb2a6807d36a50613d07ed90552a968b6bf00`, the head given. Read from a detached worktree of
`0e3cb2a`. The merge `cde07dd` is not part of this review: another reviewer judges it.

Method: `task-cycle/review/SKILL.md` and `fix.md`. The remarks take the findings file's place.
Remarks: the second part of `reports/correction-2-remarks.md`. Author's report:
`reports/author-correction-2b-report.md`, read as claims to check.

## The remarks

**Item 1 — made.** The item: "Add the part `repository` to the allowed dependencies of the part that
holds the CI file (`.github/workflows/tests.yml` reads `/.python-version`), the same way as
`instruction-files` for `installation`."

- **The right part.** The part holding the CI file is `agent-instructions`: its *Files* hold
  `.github/workflows/**` (`foundations/part_map.md:169`).
- **The one change.** Its *Depends on* (`part_map.md:170-172`) now ends "… · foundation-review ·
  process-audit · repository". That keeps the file's form: items joined by ` · `, on the existing
  continuation line, within width.
- **The reach it allows.** `/.python-version` is a file of `repository` (`part_map.md:149-151`), and
  `.github/workflows/tests.yml:41` reads it (`python-version-file: .python-version`). A search of
  `.github/` for the other files of `repository` (`.gitignore`, `.gitattributes`) finds nothing more.
  So this one allowance is the whole of what the item binds.
- **Nothing else changed.** `git diff --stat cde07dd..0e3cb2a` lists `foundations/part_map.md`
  alone, 1 insertion and 1 deletion.

**Item 2 — respected.** The item: "The two prose mentions in `installation/README.md` … are not a
dependency … No change." `git diff --quiet cde07dd 0e3cb2a -- installation/` gives exit 0: the part
`installation`, its README included, is unchanged.

**The citation.** The commit message cites the answer: the comment's address, its date and "item 1
(item 2 there: … no change)". It also names the reach it allows: `tests.yml` reading
`/.python-version`. The part map's form has no field for a source: an entry holds *Files*, *Depends
on* and *Trust boundary* only, and *Depends on* is a list of identifiers. So the commit message is
the place the forms allow, the same as for `instruction-files` in the first part of this correction.

## The map stays sound

- **No cycle.** The part `repository` reads `Depends on: none` (`part_map.md:152`). The allowance
  creates no mutual pair and no cycle. In any case no rule of the part-map template, its skill or
  `foundation_check.py` forbids one (searched in the first part of this correction).
- **The checks pass.** `foundation_check.py` accepts `repository` as a part named by a *Depends on*
  (`0 errors`), and the import check of `elements/part-map` passes.
- **Earlier work is untouched.** Nothing of the earlier corrections is changed: the range is one
  line.

## Findings

None: no Critical, Important or Minor finding in this range.

## Declined to judge

- The merge `cde07dd`, which is judged separately.
- The Minor findings of earlier reviews, which stand in the request's list.

## Checks

| Check | Command (from the worktree of `0e3cb2a`) | Exit code / result |
|---|---|---|
| Head | `git rev-parse HEAD` | 0; `0e3cb2a6807d36a50613d07ed90552a968b6bf00` |
| Range, message and diff | `git log --format='%h %p %s%n%b' cde07dd..0e3cb2a`; `git diff --stat` and `git diff cde07dd..0e3cb2a` | 0; one commit, one line of `foundations/part_map.md` |
| `installation` unchanged | `git diff --quiet cde07dd 0e3cb2a -- installation/` | 0 (no difference) |
| The CI file's reaches to `repository` | `git grep -n "python-version\|\.gitignore\|\.gitattributes" -- .github/` | 0; `tests.yml:41` only |
| Foundation check | `python -B elements/common/foundation_check.py` (without `--skip-test-citations`) | 0; `0 errors` |
| Tests | `python -B gate/run_tests.py elements/part-map` | 0; 40 tests, OK |
| Tests | `python -B gate/run_tests.py elements/common` | 0; 242 tests, OK |

The full gate was not run, as the handoff and the method give.

## Reaches beyond the dispatch

- `foundations/part_map.md:145-172`: the entries `repository` and `agent-instructions`, read whole.
- `.github/workflows/tests.yml`: searched for its reaches to the files of `repository`.

## Working copies

- A detached worktree of `0e3cb2a` at
  `.runs/review-correction-2b/wt`, and the check
  outputs beside it in `.runs\review-correction-2b\`: removed (see the return). Nothing was kept in
  `reports/`.

## Unread material

- WAY-225, the glossary entry "dependency of a part" and the part-map template's "Allowed
  dependencies" were not reread in this range. I read them in the earlier reviews of this cycle,
  and the range changes none of them.

## Searches not found or unclear

none
