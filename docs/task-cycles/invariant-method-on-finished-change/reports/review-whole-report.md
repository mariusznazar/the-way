PASS e3fcc2025fa436467400f3ba56711c60f47f9c91

# Review of the whole change — invariant method held on the finished change

- Range: `46bba355e51bc671a4af604e11757d91574949b6..e3fcc2025fa436467400f3ba56711c60f47f9c91`
  (`9d499d0`, `e3fcc20`); `git rev-parse HEAD` in the worktree is `e3fcc20…` — matches the dispatch.
- Route: one author, no plan, no spec; every finding below comes from no slice.
- Method: `task-cycle/review/SKILL.md` and `task-cycle/review/whole_change.md`, variant: the whole change.
- Counts: blocking 0; Minor 3 (all within the task); out of scope 0 findings (Declined to judge: 3 lines).

## Findings

### Critical

none

### Important

none

### Minor

**M1 — WAY-61's *Rationale* restates the permission as a fact, in a sentence that misreads.**
Within the task (To do 1: the rationale must agree with the new sentence).
Place: `foundations/decisions.md:1497-1499`:
"A change is judged finished, so an invariant written before its test within one change reads `test`
from its writing, and a later slice that writes the test leaves the entry as it is."
What is wrong: (a) "A change is judged finished" reads as "a change is deemed finished", not "a change
is judged once it is finished"; (b) the binding sentence (`:1471-1472`) and the template
(`elements/invariants/template.md:59-61`) grant "may read `test`", while the rationale says the
invariant "reads `test`", which a reader in a borderline case — the agent who forgot the switch and
turns the method back to `review`, the direction WAY-321's rationale calls safe — can take as an
obligation. A smaller point of the same entry: *Rejected* keeps "`TODO` as the method until the test
exists — it names nothing that keeps the rule meanwhile" (`:1505-1506`), a reason that now also fits
`test` mid-change; it holds only across changes, which the entry leaves to the reader.
Why it matters: *Rationale* is what an agent reads in a borderline case (decisions template, "Fields
and their readers"). The binding sentence and the examples carry the right meaning, so this is
polish, not a wrong rule.
Suggested wording: "A change is judged as a whole, once finished, so an invariant written before its
test within one change may read `test` from its writing, and a later slice that writes the test
leaves the entry as it is."
Evidence: reading of the entry against its binding sentence and the template line.

**M2 — `test-method-citation` derives from WAY-321 only, while its sentence is WAY-61's rule.**
Within the task (row 3 of *Settlements to record*; the row leaves the derivation to the writer).
Place: `foundations/invariants.md:162` (`- **Derives from:** WAY-321`); WAY-61's *Verification*
`foundations/decisions.md:1482` names no invariant.
What is wrong: the invariant's sentence ("Every invariant whose method is `test` is cited by …") is the
checkable form of WAY-61's own violates example "an invariant reads `test` on the finished change
while no test cites it" (`foundations/decisions.md:1491-1492`); WAY-321 answers when the check
reports, not what the data must hold. The model the row names, `map-reference-target`
(`foundations/invariants.md:146-154`), derives from the decision of its data rule (WAY-41), not from
a decision about a check. `elements/invariants/template.md:122-124`: *Derives from* names every
decision the invariant derives from, "neither link is optional".
Why it matters: the writer of a later change to WAY-61 who follows its *Verification* finds no
invariant to revisit. The harm is small, because WAY-321 "derives from WAY-61" and the search of the
foundation (WAY-33) reaches the invariant through it. The author's reason — avoiding an edit of
WAY-61's *Verification* — is a cost, not a reason for the link to be absent, and does not lower the
grade.
Suggested fix: `- **Derives from:** WAY-61 · WAY-321`, and WAY-61's *Verification* opens with
`invariants: test-method-citation.` before the pair of examples (the template's form allows both).
Evidence: the passages cited above.

**M3 — one docstring line over the file's line width.**
Within the task (To do 3).
Place: `elements/common/foundation_check.py:499` — 101 characters; it is the only line of the file
over 100, and the neighbouring code keeps 100.
Why it matters: style only; no linter of the-way enforces it.
Evidence: a scratch measurement of the line lengths (no file changed).

## The orchestrator's five points

1. **WAY-61.** The new sentence stands word for word as To do 1 gives it, after "no script."
   (`foundations/decisions.md:1471-1472`). The complies example (`:1486-1488`) and the violates
   example (`:1489-1492`, "on the finished change while no test cites it") agree with it; the old
   rationale sentence "An invariant may be written before its test, … the review." is gone, and the
   new rationale carries row 1's weak point ("The price taken", `:1500-1503`) faithfully — see M1
   for wording. The rejected way of question 1 stands in *Rejected* (`:1506-1511`) with both costs
   of the source, without a file name; the template (WAY-134) allows it, and row 1's last column
   asked exactly this. `task-cycle/plan/SKILL.md` holds no sentence turning `review` into `test`
   (searched; `:113-118` and `:165-176` read). Search of the whole repository (`git grep`, outside
   `.runs`) for "reads `review` until", "until then", "not written yet", "before its test",
   "turns … to `test`", "written before … test", "whose test is not": no statement of the old rule is
   left except the three places question 4 keeps — `elements/invariants/skill/SKILL.md:57-58`,
   WAY-71's rationale `foundations/decisions.md:1692-1693`, WAY-117's complies example
   `foundations/decisions.md:2747-2748` — all three unchanged by the range (diff of those files
   shows no hunk there). `elements/invariants/skill/write.md:7-9` ("the test is written in the
   change that brings the entry") agrees with the new rule.
2. **`test-method-citation`.** All five fields of the template, words the template gives, English,
   one sentence, identifier in lower case with hyphens, unique (the check passes); *Part* `every`
   and *Rests on* `none` as its model. Cited at `elements/common/test_foundation_check.py:846`
   inside `test_the_way_foundation_passes`, which runs the script on the-way itself without the
   switch, so it checks the real data (WAY-61's third sentence) — seen failing in a scratch copy
   (below). WAY-321's *Verification* names it after `invariants:` (`foundations/decisions.md:10281`),
   as the decisions template requires for a derived invariant. Derivation: M2.
3. **Script.** `check_test_citations` (`foundation_check.py:498-504`) reads the set filled by
   `check_citations`, which runs only on paths of `git ls-files` not ending in `.md`
   (`:613-616`), and only on lines in comment form (`CITATION`), so "tracked by git, not Markdown"
   holds; one error per invariant, at its *Method* line. The switch guards only that call
   (`:618-619`). `main` (`:627-638`): an unknown `--` argument or two roots print the usage line and
   exit 2; the switch may stand before or after ROOT; the default run is unchanged apart from the
   new report. Tests cover report, other-file citation, Markdown, untracked file, switch, switch
   position, switch skipping no other error, unknown switch; each asserts the place or the code.
4. **The two README edits.** Not required by any item of *To do*, and not a finding either way.
   `README.md:80-82` keeps the one-sentence summary of what the script reports true now that it
   reports one more thing. `installation/README.md:72-75` states WAY-321's second binding sentence at
   the place a product reads to build its one command, and WAY-321's *Scope* names `installation`;
   neither changes the command the task's question 2 says stays unchanged. Both are within the reach
   of the change; I would keep them.
5. **Language and form.** All entries and the changed text are in English; `private_paths_check.py`
   exits 0 on each of the eight files; no personal data.

Other judgements: the part map needs no change — `foundation-check-command`
(`foundations/part_map.md:197-201`) keeps its path, its one positional argument and its exit codes;
an optional switch adds to the surface without breaking a caller, and the new report on a product's
data is what "Moving the pin" (`installation/README.md:111-114`) already warns of. WAY-321 is the
next free number (last entry before it WAY-320; not on the withdrawn list). Its *Rejected* holds the
three ways question 2 keeps, each with its cost; its rationale holds question 2's weak point. No
reserved choice is taken (no language, library or store added). No trust boundary is touched
(`installation/install.py`, the `installation` part's boundary, is not in the range). No
screenshot. The author's own-work check names the requirement where the code is weakest
("tracked, not Markdown") and its tests would catch it unmet; the weakest place of the change is
rather its entries' wording (M1, M2), which the check does not reach.

## Declined to judge

- WAY-61's *Scope* not gaining `task-cycle` (the author's open point): the task does not change
  *Scope*; a plan writing invariants touches the `invariants` part, which WAY-61 names.
- A planned slice whose focused checks include `test_the_way_foundation_passes` will report an
  invariant written before the slice that writes its test (the task's *Context*, sixth bullet): the
  task records it as context and carries no item for it.
- The projected-mode sentence of `elements/invariants/skill/SKILL.md:57-58` that can be read as
  allowing `test` only in the slice writing the test: settled by question 4 as a weak point taken.

## Checks run

- `python -B gate/run_tests.py elements/common` — exit 0, 117 tests OK.
- `python -B elements/common/foundation_check.py` (worktree) — exit 0, `0 errors`.
- `python -B elements/common/foundation_check.py --skip-test-citations .` (worktree) — exit 0.
- `python -B gate/run_tests.py elements/part-map` — exit 0, 39 tests OK (it imports constants of
  the script).
- `python -B task-cycle/private_paths_check.py <file>` for each of `README.md`,
  `elements/common/foundation_check.py`, `elements/common/test_foundation_check.py`,
  `elements/common/way_of_working.md`, `elements/invariants/template.md`, `foundations/decisions.md`,
  `foundations/invariants.md`, `installation/README.md` — exit 0 each.
- Scratch, empty git repository with one tracked file (no foundation): the script without switch —
  exit 1, only the "no part claims it" error (no crash on a product with no invariants file); with
  the switch twice — exit 1, same; two roots — exit 2 with the usage line; `--x` — exit 2 with the
  usage line.
- Scratch copy of `e3fcc20` (`git archive` into a fresh repository in the session scratchpad), the
  line `# invariant: map-reference-target` deleted from the test file: the script — exit 1,
  `foundations/invariants.md:150: \`map-reference-target\` reads \`test\` and no test cites it …`,
  `1 error`; with `--skip-test-citations` — exit 0. 19 invariants read `test` in that tree.
- Manual: line lengths of the changed lines measured (M3); `git status --short` empty after all
  checks — the reviewed worktree is untouched.
- Not run: the full gate (the orchestrator's, WAY-160); `python -B gate/run_tests.py installation`
  (the range changes only `installation/README.md` there, which no installation test reads — searched
  `installation/*.py` for the changed wording).

## Reaches beyond the dispatch

- Foundation selection: the decisions whose *Scope* names a part the change touches number 110
  (`elements-common`, `invariants`, `installation`, `gate`, `decisions`, `repository`); I did not
  read them all. Read whole: WAY-61 and WAY-321 (written), WAY-65 (citation form), the passages of
  WAY-71 and WAY-117 named by question 4; the binding sentences of WAY-16, WAY-63, WAY-160 as the
  task quotes them; the invariants `test-method-citation`, `map-reference-target` and the sentences
  of every `review` invariant whose *Part* is `every`, `invariants` or `decisions`
  (`script-language`, `script-imports`, `script-subprocesses`, `ci-checking-commands`,
  `skill-rule-source`, `element-directory-contents` and the rest); the part map entries
  `foundation-check-command` and the touched parts' *Trust boundary*. Instead of the rest, the
  log was searched for the words of the change (old-rule phrases, `foundation_check`, the switch).
  Why: the selection rule would read a large share of the log for a change of one decision, one new
  decision and one script.
- `elements/decisions/template.md` and `elements/invariants/template.md` whole, `elements/common/rules.md`
  whole — to judge the entries' form.
- `elements/common/way_of_working.md:75-160`, `elements/part-map/skill/first_map.md:1-7`,
  `agent-instructions/README.md:10-15`, `README.md:150-160`, `installation/README.md:105-150`,
  `task-cycle/plan/SKILL.md:110-176`, `elements/invariants/skill/SKILL.md:28-62`,
  `elements/invariants/skill/write.md` — every other place that runs or describes the script, and
  the places question 4 and row 1 name.
- `elements/common/test_foundation_check.py:187-230` — the fixture, to confirm the untracked-file
  test writes after `git add -A`.

## Searches not found or unclear

- The handoff's point 4 speaks of "the task's return-step duty (entries true to the code)"; the task
  document holds no such phrase. I judged the README edits against the task and WAY-321 instead.
- No `guidelines/` directory in the-way, so no guideline was compared (settled by the task's
  question 3).
