FAIL

# Review of the spec: co trafia do dziennika decyzji

Spec reviewed: `.runs/task-cycles/co-trafia-do-dziennika-decyzji/spec.md`. Task: `.runs/task-cycles/co-trafia-do-dziennika-decyzji/task.md`. Reviewed as the builder who must plan and build from it without the author.

Four findings, two of them (1 and 2) that would make the build go wrong or leave a stated rule with no home. Findings 3 and 4 are smaller. After the findings: how the spec stands on the three autonomous answers, the gaps the designer stated, and notes that are not findings.

## Findings

### 1. The one line for "base unknown" breaks an existing test the spec does not mention

Place: D1, third bullet ("Where no such branch or no merge base exists (… no commit) … the report holds one line, `foundations/decisions.md: listed: ...`"), and Constraints, the bullet "The test products there have no commit … every existing test runs with no base known and must pass as it stands".

Why a builder goes wrong. The spec checks only the tests in `elements/common/test_foundation_check.py` against the new line. But `installation/test_install.py`, `test_empty_foundations_have_valid_form` (about line 667), installs into a product made by `git init` with no commit, runs `foundation_check.py` on it and does this:

- `errors = result.stdout.splitlines()[:-1]`, which is everything but the count line;
- `for line in errors: self.assertIn(": no part claims it:", line)`.

With D1 as written, that product has no commit, so the base is unknown, so the report holds the `foundations/decisions.md: listed: ...` line before the count line. That line holds no `: no part claims it:`, so the test fails. The comment in that test says the check "reports nothing about the form of the empty foundation files". The gate runs the installation tests (WAY-16), so the change cannot be merged as the spec stands. The builder meets the red test late and has two bad ways out: weaken an installer test, or drop the line from the output without the spec's leave. The spec's D9 and Constraints speak of "every existing test", but only of one file.

Way to settle. The orchestrator decides one of these and the spec says it: (a) the unknown-base line is written only where the working tree's `foundations/decisions.md` holds at least one decision (with no decision there is nothing the base could have been compared for, and WAY-38's "reports what it could not check" is met where something was to be checked); or (b) the line stays as it is and the spec names `installation/test_install.py::test_empty_foundations_have_valid_form` among the tests the change edits, with its new assertion. I recommend (a): it keeps the installer test as it stands, and an empty log has nothing to report. Either way the spec's sentence "every existing test … must pass as it stands" should name the installation tests as well.

### 2. The temporary pair of examples is a rule with no file to carry it

Place: D2, the paragraph "Line for the request's decisions for the human": "a decision pinned only by a test that a later slice writes gets a pair of examples at the foundation step … and the return step removes the part of the pair the test then holds."

Why a builder goes wrong. This is the chosen behaviour (the orchestrator's answer: the switch `--skip-test-citations` skips only the report WAY-321 names), and the spec says it costs "a pair written and trimmed in every cycle that has such a decision". But the spec's lists of what lands where (D6 "Who applies it", D5 "Where it lands", D3) never put this rule in a file:

- `elements/decisions/skill/SKILL.md` step 3 is given as "the pair only for the part no test holds", which says the opposite of writing a pair now for a test not yet written;
- `task-cycle/skill/foundation_step.md` is edited only for the sentence "as an entry of its kind";
- `task-cycle/skill/return_step.md` is edited only for the clause "a choice that binds after the merge" and the report naming the place. Nothing tells the return step to trim a pair.

The foundation step's own run of the script, right after writing a new decision whose sentence a test of a later slice will hold, ends with the new error. The writer will clear it with a pair, because nothing else is stated. Then no agent is told to trim it, so every such decision keeps a pair for a sentence a test holds, which is what point 6 and the spec's Goal 3 ("a pair only for the part no test holds") forbid. No check sees it, as the script does not read the `tests:` clause.

Way to settle. Say in the spec where the two halves of the rule stand: one bullet in `elements/decisions/skill/SKILL.md` step 3 (a decision whose test a later slice writes carries a pair for now, because the run after writing reports a changed decision with nothing holding it) and one clause in `task-cycle/skill/return_step.md` (it removes from the pair the part a test then holds and names that test by the clause `tests:`). Or choose the other way the spec names (the switch also skips this error, WAY-321 changed in one clause with its test) and say that this is what the human is shown; the spec records both and picks the first, so the pick needs its files.

### 3. Task row 8 / point 6 sentence "rationale and rejected options stay in whole" is not in the spec's WAY-12

Place: the list "Foundation entries", the line for WAY-12; D3.

Why a builder goes wrong. The frozen task, point 6 (last sentence: "Uzasadnienie i warianty odrzucone zostają we wpisie w całości") and row 8 of *Settlements to record* ("… a uzasadnienie i warianty odrzucone zostają w całości"), and *To do* 9 ("the decisions listed as changed say after the change what points 1–8 say"), require WAY-12 to say it. The spec's line for WAY-12 lists the line `decision:`, the clause, the pair "only for the part no test holds" and the report of the check, and not this. Nothing in the spec contradicts it, but the builder writes the thirteen entries "from the lines above" (the spec's *Left to the maker*), and the sentence is the one a later cleaning of the log leans on when it shortens entries that a test holds. Dropped, a cleaner may cut *Rationale* of such entries and have nothing to stop it.

Way to settle. Add to the WAY-12 line: where a test holds a sentence, the entry keeps its *Rationale* and *Rejected* whole.

### 4. A file missing at the base is neither "unknown base" nor "empty"

Place: D1 (reads `foundations/decisions.md` and `foundations/invariants.md` at the merge-base commit); D2 ("heading absent at the base" = new); D4 ("stands … at the base").

Why a builder may go wrong. D1 lists what makes the base unknown (no branch, no merge base) but not a base that exists and lacks the file (`git show <base>:foundations/decisions.md` fails). Read as D2 words it, every decision is absent at the base, so every decision of the log is "changed by the change" and each unheld one is an error; read as D1's "failure to read it is no `2`" it is no comparison at all. The two readings differ for a branch that creates the log, for instance a product whose first foundation commit is the branch. WAY-344 asks that a missing thing is never read as empty, and this spec's own Constraints repeat it for fields, not for files.

Way to settle. One sentence in D1: a file the base lacks makes the base unknown for that file (no decision counts as changed, and the unknown-base line is written), or counts as empty (all new); the first is the reading WAY-38 and WAY-344 point to. Lower weight than findings 1 to 3.

## The three answers the orchestrator gave the designer

1. The switch `--skip-test-citations` skips only the WAY-321 report, WAY-321 unchanged. The spec follows it (Constraints, D2, Non-goals). The spec states the cost. A wrong answer would not break the build, but this answer is what makes finding 2 real; the spec carries the open alternative in one paragraph.
2. "A decision the change changes" means its binding part, whitespace-normalised. D2 follows it and defines the binding part as the text from the line after the heading to the line before the first field line. That agrees with WAY-02's normalisation. I checked the real log: 323 of its 329 entries carry both a `- complies:` and a `- violates:` line after the field reader strips them, 40 name invariants, and only WAY-17 (`Verification: none`) has neither, so the held rules work on the real log. A wrong answer here would make errors too loud (if fields counted) or too quiet; neither breaks the build.
3. Rows 11 and 12 become attached paragraphs of WAY-12 and WAY-03. D8 follows it and says no invariant is written and the tests of the script carry `decision:` lines for those sentences. It does not break the build whichever way it is chosen. One remark: the request must tie rows 11 and 12 to the entries they joined, which WAY-134 already requires for a kept row stated elsewhere; the spec need not repeat it.

## The gaps the designer stated

1. The titles-only decisions (WAY-41, 52, 53, 84, 85, 89, 101 to 104, 121 to 123, 137, 138, 165, 166, 267, 270, 322). I read the heading and the first lines of each. None bears on the change. WAY-53 (a derived file equals its generator's output) is the only one near: no file generated from a file the change edits was found (the entry points under `.claude/skills/` and `.agents/skills/` hold only a description and a pointer, and no description changes).
2. The search of *Scope* lines for `project-level`, `task-cycle` and `product-guidelines`. I searched the log's binding parts and *Verification* for the phrases the change touches. Found and not named in the spec: WAY-241 ("a field naming none standing as an example"), WAY-237 (an item of the section "Not tested on purpose" names a decision), WAY-235 (narrows WAY-168 for trust boundaries), WAY-135, WAY-136 and WAY-268 (the questions table). None contradicts the spec. WAY-241 and WAY-237 say "names no decision stands as an example" for fields and items of the testing template, which D7 leaves standing because WAY-173 still binds a product only through its adopting decision. The search of the whole foundation (WAY-33) at the foundation step will meet WAY-241; the spec's list of "Other decisions of the log the change reaches" could name it. Not a finding.
3. `foundations/invariants.md`. I listed the invariants whose *Part* names `decisions`, `elements-common`, `project-level`, `task-cycle`, `product-guidelines` or `every`, and those deriving from the changed decisions. None is violated by the spec. `skill-entry-points` (test): the change edits the bodies of `SKILL.md` files and no description, and the entry points hold a description and a pointer only, so no copy is out of date. `test-method-citation`, `script-imports`, `script-subprocesses`, `cross-part-imports` and `derived-file-content` hold as the spec states. `test_cross_part_imports.py` imports names from `foundation_check.py` (`EMPTY`, `ENTRY`, `INVARIANTS`, `LEFT_OUT`, `PART_MAP`, and others), which the builder must keep.
4. `task-cycle/request_check.py`. The docstring says "The script judges no content", reads the two files and runs nothing, and its headings and the three group names do not mention the items of the lower part or the kinds. So the spec's claim that D4's naming of a listed invariant and of a changed test with a `decision:` line lives in `request_template.md` and not in the script is right, and no change of `request_check.py` is needed. Kinds 5, 6 and 7 and the lower part *Foundation entries* are as the spec says. `test_request_check.py` reads the template for headings only.

## Notes, not findings

- The spec uses "binding part" for the text before the first field. The glossary defines a binding part as the text of an entry that whatever relies on the entry depends on, which for a decision may include its fields (*Relations*, *Scope*). The spec's definition is explicit, so a builder follows it; the entries WAY-12 and its attached paragraph should say "binding sentences" for what the script compares, or the glossary reading and the script differ.
- WAY-17 (`Verification: none`) is the one decision of the real log the new check would list as unheld. If the foundation step's search edits its binding part, the change makes it "changed" and an error unless it gets a pair. The spec says WAY-17 stays unless the search finds the chain stated as closed; the builder should know the consequence.
- D9 lists a test for a decision with no *Verification* but none for an invariant with no *Method* at the base or now; the Constraints bullet on WAY-344 covers it and the builder should add it.
- `elements/common/skill/read.md` (step 1 of the skill that finds entries) tells the reader to read "the plan test in the decisions' template"; the spec changes step 1 of `task_variant.md` to read the questions too, so the shared line stays correct for the definition variant.

## Unread material

- Decisions of the log, each read whole unless said: WAY-01, 02, 03, 07, 10, 11, 12, 14, 17, 18, 19, 21, 22, 30, 33, 35, 36, 38, 60, 65, 95, 114, 115, 124, 126, 167, 168, 169, 170, 171, 172, 173, 174, 237, 241, 265, 293, 315, 321.
- Decisions read in part: WAY-05 (to the end of its first paragraph only; its fields and prose not read); WAY-26 (not opened; only the sentence quoted in the task and the spec read); WAY-61 (to its *Rejected*, tail cut); WAY-134 (to its *Verification*, *Rationale* and *Rejected* not read); WAY-113 (to the middle of *Rejected*); WAY-256 (to *Rationale*); WAY-328, WAY-290, WAY-344, WAY-235, WAY-135, WAY-136, WAY-268, WAY-112, WAY-24 (binding part and *Verification*, prose cut); WAY-41, 52, 53, 84, 85, 89, 101, 102, 103, 104, 121, 122, 123, 137, 138, 165, 166, 267, 270, 322 (heading and about eight lines each).
- `foundations/part_map.md`: not read whole; I read the surface `foundation-check-command` and searched it for `foundation_check`.
- `foundations/invariants.md`: not read whole; read through a script listing of the entries by *Part* and *Derives from*, and `skill-entry-points` whole.
- `task-cycle/request_check.py`: lines 1 to 120 (docstring and constants); the rest not read.
- `task-cycle/skill/request_template.md`: lines 90 to 135, 265 to 330 and 436 to 460, and a search for the kinds; not whole.
- `project-level/task/template.md`: lines 60 to 110 and 190 to 236; not whole.
- `elements/common/test_foundation_check.py`: lines 1 to 330 and 990 to 1052; the middle (about 660 lines) read only by searching for `invariant:`.
- `agent-instructions/README.md`: the first 60 lines.
- Read whole: `task-cycle/spec/SKILL.md`, `task-cycle/spec/review.md`, the handoff, the spec, the task, `elements/common/foundation_check.py`, `elements/decisions/template.md`, `elements/decisions/skill/decide_entry.md`, `SKILL.md`, `projected.md`, `read.md`, `elements/common/skill/task_variant.md`, `build_table.md`, `read.md`, `task-cycle/skill/return_step.md`, `foundation_step.md`, `product-guidelines/template.md`, `elements/common/rules.md`.
- I did not run any test or the script.

## Searches not found or unclear

- Where the spec puts the rule that the foundation step writes a pair that the return step then trims (finding 2): not found in any file list of the spec; D2 states it only as prose about the request.
- Where in `elements/decisions/template.md` the form of the line `decision:`, the clause `tests:` and the change to the bullet "Tests live only with invariants" and to the sections "Verification" and "Changing a decision" land: the spec names the bullet of the five questions exactly and leaves the rest to "the sentences of the template … as long as they say what is above"; I read that as covered by the task's points 5 and 6. Unclear, not a finding.
- Any file other than `elements/common/test_foundation_check.py` that runs `foundation_check.py` and reads its output: found `installation/test_install.py:667` (finding 1); `test_cross_part_imports.py` imports its names; `installation/test_styleguide_installation.py` names the command only as text.
- Any non-Markdown tracked file holding a comment-sign line with `decision:` that the new reading would take for a citation: none found.
- A script that reads the *Kind* column of a task document's table: none found (only a fixture in `project-level/test_plan_state_invariant.py`, and `readiness_check.py` reads the `Candidates:` line only).
- A decision of the log that says the main branch of a script's base is `origin/HEAD`, `main`, `master` in that order: none; `elements/common/rules.md` ("`{fork-point}`") and WAY-60 name `<main branch>` without saying how a script finds it, so D1's order is new text, as the spec says.
