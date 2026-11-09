# Author report — invariant method held on the finished change

**Status:** done

## Commits

- `9d499d0` Hold an invariant's method on the finished change and record the check of its citing test (foundation entries: WAY-61 edited, WAY-321 added, invariant `test-method-citation` added)
- `e3fcc20` Report an invariant that reads test and has no citing test, skipped after writing an entry (script, tests, template, way of working, two READMEs)

Both on `task/invariant-method-on-finished-change`; nothing pushed. Each commit is green on the focused checks (the first commit alone also passes the old script, since the citing line comes with the second).

## Files changed (added / removed lines, base `46bba35`)

| File | + | - |
|---|---|---|
| `foundations/decisions.md` | 59 | 10 |
| `foundations/invariants.md` | 10 | 0 |
| `elements/common/foundation_check.py` | 31 | 6 |
| `elements/common/test_foundation_check.py` | 61 | 1 |
| `elements/common/way_of_working.md` | 5 | 2 |
| `elements/invariants/template.md` | 6 | 3 |
| `README.md` | 2 | 2 |
| `installation/README.md` | 4 | 2 |

## The four To do items

1. WAY-61: new third binding sentence after "no script."; complies example, violates example ("... on the finished change while no test cites it") and Rationale made to agree; weak point of row 1 in Rationale as "The price taken"; the rejected way in *Rejected* (see choices).
2. `elements/invariants/template.md`, "Method and test": the old sentence replaced by the finished-change sentence plus a pointer to the check (WAY-321); *Method* row of "Fields and their readers" gained `foundation_check.py` as a reader.
3. `foundation_check.py`: `check_test_citations` reports each invariant with `Method: test` that no citing line names. Reuses the existing `tracked` list and `check_citations` (the single loop over `git ls-files` for non-Markdown files); no second way of listing files. Message: `foundations/invariants.md:<line of Method>: \`x\` reads \`test\` and no test cites it: ...`.
4. `way_of_working.md` step 4.3 passes `--skip-test-citations`.

## Switch

Name: `--skip-test-citations`. Documented in the script's module docstring (usage line and a paragraph), in `way_of_working.md` step 4.3, in `elements/invariants/template.md`, in `installation/README.md` (the product's one command runs the script without it). A switch the script does not know, or more than one root, prints `usage: foundation_check.py [--skip-test-citations] [ROOT]` and exits 2. The switch may stand before or after ROOT.

### Other places that run `foundation_check.py` — judged

| Place | Runs it | Switch? |
|---|---|---|
| `elements/common/way_of_working.md` step 4.3 (used by all five element skills, `record-*` and `update-part-map`, and by the foundation step / return step through them) | right after writing an entry | yes (done) |
| `elements/part-map/skill/first_map.md:5` | repeatedly while writing the first part map, to find files no part claims | no — it runs after part-map entries, not invariant entries, and the new report only reflects invariants already present; hiding it there would hide a real gap |
| `installation/install.py:168-176` (generated `AGENTS.md` block) | before a merge, and on its own while the product's one command lacks it | no — a pre-merge run must report the uncited `test` |
| `installation/README.md:71-74` | the product's one command of tests (WAY-16) | no, by WAY-321; text now says so |
| `elements/common/test_foundation_check.py::test_the_way_foundation_passes` | the-way's gate | no, by WAY-321 |
| `elements/common/projected_mode.md:21` | "Run no foundation check" in projected mode | not applicable |
| `project-level/definition_template.md:352`, `agent-instructions/README.md:13`, other mentions | describe, do not run | not applicable |

`installation/test_install.py` and `installation/test_styleguide_installation.py` run the script on freshly installed (empty) products; they pass (installation directory run below).

## Checks (command and exit code)

- Failing run first (new tests before the code): `python -B gate/run_tests.py elements/common` — exit 1, 8 failures: `test_citation_in_a_file_git_does_not_track_does_not_count`, `test_citation_in_markdown_does_not_count`, `test_invariant_reading_test_that_no_test_cites_is_reported`, `test_skip_switch_before_or_after_the_root`, `test_skip_switch_skips_no_other_error`, `test_skip_switch_skips_the_report_of_an_uncited_test_invariant`, `test_the_way_foundation_passes` (the cited invariant did not exist yet), `test_unknown_switch_cannot_run`. They failed on assertions (exit code 0 where 1 expected; the switch read as a ROOT, giving exit 2 "git cannot run"; no usage line), not on missing modules. `test_invariant_reading_test_cited_in_another_file_passes` passed already (a guard that the check does not over-report).
- Script finished, entries not yet written: same command, exit 1, one failure, `test_the_way_foundation_passes`: `test-method-citation names no invariant`.
- The invariant's test seen failing for its own reason: the citing line `# invariant: test-method-citation` removed for a moment from `test_the_way_foundation_passes`, `python -B -m unittest discover -s elements/common -p "test_foundation_check.py" -k test_the_way_foundation_passes` — exit 1, `foundations/invariants.md:160: \`test-method-citation\` reads \`test\` and no test cites it ...`; line restored before the commit.
- Passing: `python -B gate/run_tests.py elements/common` — exit 0, 117 tests OK. `python -B gate/run_tests.py elements/part-map` — exit 0, 39 OK. `python -B gate/run_tests.py installation` — exit 0, 44 OK.
- `python -B elements/common/foundation_check.py` on the committed tree — exit 0, `0 errors` (all 19 `test` invariants of the-way, the new one included, are cited).
- `python -B task-cycle/private_paths_check.py <file>` on each of the eight changed files — exit 0 each.
- Not run: the full gate (`python -B gate/run_tests.py`, the orchestrator's alone, WAY-160); `python -B -m unittest discover -s gate` (no change to `gate/`); `request_check.py` (no request is mine).

## Own-work check (WAY-164)

Requirement most likely unmet: the new check reports on "tracked by git" the same way as the existing citation check, and does not count Markdown or untracked files. Check: three tests — `test_citation_in_markdown_does_not_count` (a `<!-- invariant: ... -->` line in `README.md`), `test_citation_in_a_file_git_does_not_track_does_not_count` (a `.js` file written after `git add -A`, so not tracked), `test_invariant_reading_test_cited_in_another_file_passes` (tracked `.js` file counts). All pass; the first two failed before the code. Second candidate: the switch skips only this report: `test_skip_switch_skips_no_other_error` (an unrelated `ABC-07` error still fails, exactly 1 error).

Mutation in head: inverting `skip_test_citations` (switch tests), comparing `Method` to `review` (report test), counting Markdown citations (markdown test), counting untracked files (untracked test), dropping the `--` usage guard (unknown-switch test), reporting at the wrong line (the report test asserts `foundations/invariants.md:7:`). Unprotected: a citing line of an old form `x@fingerprint` is counted through `NAMED` (the good fixture cites `save-round-trip/1`, so the `/version` form is covered; the `@fingerprint` form is not tested separately).

## Choices (with the way rejected and its cost if wrong)

- **Row 1, *Rejected* of WAY-61:** the rejected way (a sentence in the planning skill) goes into WAY-61's *Rejected*, with its cost from the task's question 1, written without file names (the decisions' template keeps *Rejected* free of file names). Basis: `elements/decisions/template.md` and WAY-134 — *Rejected* of a decision written from a row takes the ways not chosen that the row's source keeps, and question 1 keeps it. Rejected: leaving it only in the task's history (the task's own row 1 asks). Cost if wrong: one clause to delete.
- **Row 2 is a decision of its own, WAY-321**, not part of WAY-61: it answers a different question (when the check reports, which run skips it), has its own *Rejected* (three ways kept by question 2) and its own invariant. Rejected: folding it into WAY-61 — would mix the method rule with the check's placement. Cost if wrong: merge two entries, the invariant's *Derives from* changes.
- **Row 3, `test-method-citation` derives from WAY-321 only**, not also from WAY-61. Reason: the template wants a decision's *Verification* to name the invariants that derive from it; deriving from WAY-61 as well would call for editing WAY-61's *Verification* too. Rejected: WAY-321 · WAY-61. Cost if wrong: add WAY-61 to *Derives from* and an `invariants:` line to WAY-61's *Verification*.
- **Identifier `test-method-citation`**, *Part* `every` (a change to the invariants file or to any test file can make it false), *Rests on* `none` (as `map-reference-target`), *Method* `test`, cited in `test_the_way_foundation_passes`. The sentence says "comment line" because the script only reads a citation in comment form.
- **WAY-321 *Scope*:** `elements-common, invariants, gate, installation` (script and way of working; the invariant file; the gate runs the script through a test; the installation README states the product's command). Rejected `agent-instructions`, `task-cycle` (nothing of those parts changes). Cost if wrong: a change to a part not named does not read WAY-321.
- **WAY-321 *Relations*:** derives from WAY-61 · WAY-63 · WAY-16.
- **Message and report line:** the error stands at the `Method` line of the invariant, so a reader goes to the entry.
- **Switch name** `--skip-test-citations` (plain; says what it skips). Rejected `--before-tests` / `--entry-mode` (name the situation, not the effect).
- **README.md and installation/README.md edited** (one clause each) so the description of what the script checks and of the product's command are true. Not in the task's list; cost if wrong: revert two clauses.
- **WAY-61 violates example:** added "on the finished change" to "an invariant reads `test` ... while no test cites it", so it agrees with the new sentence (before: ambiguous mid-change).
- **Not changed (question 4):** the sentence in `elements/invariants/skill/SKILL.md` (projected mode), WAY-71's rationale, WAY-117's complies example — confirmed unchanged.
- **Part map unchanged:** `foundation-check-command` ("keeps its path, its argument and its exit codes") — an optional switch is added, the codes keep their meaning; the new report only adds failures on foundations that break WAY-61, which the pin-move paragraph of `installation/README.md` already covers ("may judge the same files differently"). Cost if wrong: add "an optional switch" to the surface.

## Entries (foundation step), sentence of meaning in English and Polish

1. **WAY-61** (edited in place) — mark `row 1`.
   - EN: An invariant's method is judged on the finished change, so an invariant whose test a later slice of the same change writes may read `test` from the moment it is written.
   - PL: Metodę niezmiennika ocenia się na gotowej zmianie, więc niezmiennik, którego test pisze późniejszy kawałek tej samej zmiany, może czytać `test` od momentu zapisania.
2. **WAY-321** (new) — mark `row 2`.
   - EN: The foundation check reports every invariant that reads `test` and that no test cites, in every run, and only the run made right after writing an entry skips that report with a switch.
   - PL: Sprawdzenie fundamentu zgłasza każdy niezmiennik, który czyta `test`, a którego nie cytuje żaden test, w każdym uruchomieniu, a pomija to tylko uruchomienie zaraz po zapisaniu wpisu, z przełącznikiem.
3. **`test-method-citation`** (new invariant) — mark `row 3`.
   - EN: Every invariant whose method is `test` is cited by a comment line `invariant: <its identifier>` in a file git tracks other than a Markdown file.
   - PL: Każdy niezmiennik, którego metoda to `test`, jest cytowany linią komentarza `invariant: <jego identyfikator>` w pliku śledzonym przez git innym niż Markdown.

No entry is `the cycle's`. Search of the foundation (WAY-33): searched the whole foundation for the phrases "reads `review`", "not written yet", "until then", "before its test"; WAY-71 rationale ("An invariant with no test reads `review` ... (WAY-61)") still true; WAY-117's example and WAY-71 untouched by the task's question 4; no other entry states the old rule.

## Reaches beyond the handoff

- Search of the decision log and the repository for `foundation_check` and for the phrases above (all files, `Grep`), to find every place that runs the script and every statement of the old rule. Why: the handoff asks to find other runs; the old-rule statements for WAY-33.
- Read `project-level`, `task-cycle/skill/foundation_step.md`, `elements/part-map/skill/first_map.md`, `installation/install.py:160-182`, `agent-instructions/README.md`, `glossary.md` entries (gate, invariant, invariant test, foundation step, return step, slice), `elements/decisions/skill/{SKILL,read,decide_entry}.md`, `elements/invariants/skill/{decide_entry,draft,write}.md`, `examples.md` of both elements. Why: the pinned skills' steps and the writer's selection of reading.
- Part map entries `decisions`, `invariants`, `elements-common`, `foundation-check-command`, `test-runner-command` read as the handoff names.

## Searches not found or unclear

- The handoff names `installation/README.md:71-74` among the files to read; no instruction says whether a product's description of its command must repeat the switch rule — I added a clause (see choices).
- No `guidelines/` directory in the-way (settled by the task's question 3), so no guideline to follow; the style of the neighbouring script and tests was followed.
- Unclear whether *Scope* of WAY-61 should gain `task-cycle`, since its new sentence now speaks of the cycle's slices; left unchanged (not in the task).
- The task says 16 `test` invariants at `a3206c1`; the base holds 18 and the tree 19 with the new one (`grep -c` of the `Method: test` lines). The check passes on all of them.

## Concerns

- None blocking. The weak points named in the task are in the entries: the shortened gap on the task branch (WAY-61 Rationale, "The price taken") and the one switch to remember (WAY-321 Rationale).
- An unusual side effect to know: the order of the commits makes the first commit green only under the old script; the second adds the citing line and the check together.

## Problems observed

None. `elements/common` run takes about 35 seconds, installation about 180.
