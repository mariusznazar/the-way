# Return step — task `testing-guidelines`

**Status:** `done`

Worktree `C:/Storage/repos/the-way-wt/testing-guidelines`, branch `task/testing-guidelines`, from
the reviewed head `a2f1165`. Method: `make-change`, step 11 of `task-cycle/skill/SKILL.md`, the
the-way form of `agent-instructions/README.md` ("Make the change": no hunt for behaviour no invariant
covers).

## Commit and files

- `f3c7f7e` "Keep invariant in its glossary meaning in WAY-228 and the testing template, and name
  tests in refinement's wait for missing guidelines", author `mariusznn@gmail.com`, explicit paths,
  no push, tree clean after.
  - `foundations/decisions.md` +4 / −4 (WAY-228: binding sentence and *Rationale*)
  - `product-guidelines/testing/template.md` +2 / −2 (rule "Test inputs and expected values")
  - `project-level/task/skill/SKILL.md` +1 / −1 (step 3, missing discipline guidelines)

Range for the review of the return step: `a2f1165..f3c7f7e`.

## Corrections

1. **A term used against its entry — `invariant` (through `record-glossary-term`).** WAY-228's
   binding sentence listed, among the relations a property test takes its expected value from, "an
   invariant's sentence"; its *Rationale* said "an invariant kept after every step"; the testing
   template's rule (`product-guidelines/testing/template.md:158`) repeated the binding wording. The
   glossary defines an invariant as "a sentence about the product that is true or false on every
   commit", and the log uses "an invariant's sentence" throughout for the sentence of a foundation
   invariant (WAY-69, WAY-03 area, lines 164, 1365, 1395, 1564 and others). The meaning intended
   here is the field's — a condition a stateful property test checks after every step: the source is
   Hypothesis's "invariants that you want to ensure are met after every step in a process" (WAY-228
   *Based on*), and the template's yes/no table words the same item "something kept after every
   step". Read with the glossary, the binding sentence would have narrowed that source of a
   property's relation to the sentences of the product's foundation invariants. All three uses now
   read "a condition kept after every step". No entry is written or changed: the field meaning needs
   none, and once the uses are reworded the word carries one meaning in the files git tracks (the
   same correction the foundation step made for "standing check", "entry" and "element"). Uses
   listed: every added line with `invariant` (`git diff -U0 4302f72..a2f1165`), 40-odd; only those
   three were in the field sense; the Hypothesis quotation stays as quoted. For the request: the
   task's Polish "zdanie niezmiennika" (Q13) is rendered as "a condition kept after every step";
   the meaning of WAY-228 does not change.
2. **WAY-215 against refine-task step 3.** WAY-215, edited by this change, keeps a task waiting
   "whether or not the product already has screens, code or tests"; `project-level/task/skill/SKILL.md:148`
   still said "even in a product with screens or code". Now "with screens, code or tests", as
   `product-guidelines/reading.md:67` already reads.

## Compared and found matching

- **Entries the change writes or changes** against the code at `a2f1165`:
  - WAY-231–WAY-243 against `product-guidelines/testing/template.md` (required form, each rule's
    *Decision* and *Invariant*, recipes, `## Not tested on purpose`, `## Examples`,
    `## Where in code`), the coding template and skill (kinds exclude tests).
  - WAY-244–WAY-250 against `product-guidelines/testing/SKILL.md` (modes of step 1, step 2's
    preferences then research with critique, step 3's per-level audit and boundaries, "A new level",
    step 4's settlements, invariants and weak points, *To do* with the `AGENTS.md` pointer).
  - WAY-174 (skill step 4 "How to show"), WAY-214 (`reading.md` "Name the affected work"), WAY-215
    (`reading.md` "Distinguish the gaps"; task skill step 3 — corrected above), WAY-218 (plan skill
    step 2), WAY-228 (testing template; no use left in `product-guidelines/coding/`; corrected
    above).
  - Glossary `exemplar` (widened): uses in the coding discipline keep their meaning; "exemplar test"
    in the testing files fits the new definition.
  - Facts `llm-test-oracle-actual-behaviour` (WAY-232) and `computer-use-agent-web-testing`
    (WAY-236): each relied on by its decision.
  - Installer: `SKILLS` entry, the generated block naming every `SKILLS` skill, `installation/README.md:57`
    and `:172`; `README.md` names the new directory.
- **Entries the task names** (WAY-08, 13, 16, 48, 51, 121, 167, 168, 171, 172, 173, 198, 199, 200,
  209, 212, 213): binding sentences read against the files; none made untrue. WAY-173's "never a
  product's screens or code directly" covers tests as code of the product (the template says
  "tests"); WAY-168's limit on invariants is narrowed by WAY-235 as recorded (C10); WAY-171 admits
  the testing template's added sections "at the places that template names".
- **Entries the foundation agent's searches found** (WAY-03, 24, 68, 77, 107, 114, 128, 129, 184,
  187, 192, 201, 210, 211, 216, 217, 226, withdrawn WAY-70's row): consistent; WAY-174 still narrows
  WAY-114; WAY-70's row ("for a product's tests it stands in WAY-228") stays true.
- **Part map** of `product-guidelines`, `installation`, `agent-instructions`, `project-level`,
  `decisions`, `glossary`, `environment-facts`: responsibilities and files cover the new template,
  skill, entry points and installer line; every reference the new files make (`elements/common/`,
  `project-level/task/`, `installation/README.md`, `instruction-files`, `update-part-map`,
  `implement-task`) lies in a part *Depends on* names; `installation`, `project-level` and
  `agent-instructions` already depend on `product-guidelines`. No change. Surfaces unchanged
  (`installation-command` speaks of project skills generally).
- **Invariants:** `skill-entry-points` holds (generator reports current); `outbound-link-reach` —
  the new links were checked by the foundation step and the whole review; no other invariant reads
  the touched files. No invariant written: the task, the decisions and the human set no new rule of
  the-way itself for one.
- **Rows of *Settlements to record*:** 1–24 each carried by an entry, row 25 per C3; nothing the
  code makes true is missing.
- **Sources outside the product:** none beyond the two facts and the quoted *Based on* sources; the
  yes/no table and the recipe defaults are practice proposed as examples or adopted by a product's
  decision, not findings about agents, models or tools (WAY-90).
- **Choices binding after the merge (WAY-36):** C4, C10, C12, C13 are carried by WAY-242, WAY-235,
  WAY-250; C3, C8, C9, C11 end with this change or are wording. The `.runs/testing/` report
  directory follows the coding and styleguide skills, which no decision records either.

## Not corrected, with the reason

- Review Minor 1–4 and the out-of-scope finding: not this step's (WAY-161), including the wording
  "A missing coding and a missing testing guidelines" at `project-level/task/skill/SKILL.md:160-161`
  next to the line corrected.
- WAY-242's *Scope* (`product-guidelines, project-level`) names no `task-cycle`, though its binding
  sentence says what a cycle's author does with a level's first test. The rule reaches the cycle
  through `product-guidelines/reading.md` and WAY-172's existing route, and no task-cycle file
  carries it, so the Scope matches where the code holds it. Left as is.

## Checks

| Command | Exit | Result |
|---|---|---|
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `python -B agent-instructions/skill_entry_points.py` | 0 | `entry points are current` |
| `python -B gate/run_tests.py elements/common` | 0 | 109 tests OK |
| `python -B gate/run_tests.py project-level` | 0 | 259 tests OK (task skill text changed) |
| `git diff --check a2f1165` | 0 | empty |
| `git grep` for "invariant's sentence" / "invariant kept" in WAY-228 and the template | — | gone; remaining hits are the glossary sense elsewhere in the log |

No test written: the corrections are prose of entries and skills (`make-change` §2).

## Own-work check

- Requirement most likely unmet: "a term used against its entry" across every entry the change
  writes. Check: every added line of `4302f72..a2f1165` in `foundations/`, `product-guidelines/`,
  `project-level/`, `installation/README.md` and `README.md` scanned for each glossary term
  (`entry`, `element`, `slice`, `surface`, `debt`, `read off`, `critical flow`, `human action`,
  `open design choice`, `preparatory`, `standing`, `binding part`, `foundation step`, `return
  step`, `user interface`, `gate`, `invariant`) and each hit read. Result: only `invariant`, three
  uses, corrected.

## Reaches beyond the handoff

- `foundations/decisions.md` WAY-36, WAY-167, WAY-168, WAY-171–WAY-173, WAY-199, WAY-200,
  WAY-209, WAY-212, WAY-213 binding parts, read for the comparison the handoff asks.
- `foundations/invariants.md` (list and `derived-file-content`, `outbound-link-reach`,
  `generated-overview`, `return-step-record`), `foundations/glossary.md` whole,
  `elements/glossary/skill/SKILL.md` and `template.md` whole (for correction 1),
  `product-guidelines/template.md` whole, `installation/install.py` (block generation),
  `installation/test_install.py:20-35`, `task-cycle/review/SKILL.md` (test criteria).

## Fix after review

**Status:** `done`. Finding 1 (Important) of `reports/return-review.md` accepted, not contested.

- **Why the finding holds:** Q13 names `raport_wytyczne_testow.md` section 1 as its source, and that
  section reads at line 29: "To naturalna postać niezmiennika the way: losowy ciąg akcji, a po każdej
  sprawdzenie zdania niezmiennika", filing the Hypothesis quotation as "odpowiednik niezmiennika"
  (line 46). "Zdanie niezmiennika" in Q13 is the sentence of a the-way invariant, the glossary
  meaning, so "an invariant's sentence" in WAY-228's binding sentence was no term used against its
  entry. Correction 1 above rested on a wrong premise.
- **What changed:** commit `8c74925` "Restore an invariant's sentence among the relations of a
  property test in WAY-228 and the testing template" (author `mariusznn@gmail.com`, explicit paths,
  no push, tree clean):
  - `foundations/decisions.md` +3 / −3 — WAY-228's binding sentence reads again "undoing the
    operation, an invariant's sentence, or a simpler version written from the requirement";
  - `product-guidelines/testing/template.md` +2 / −2 — the rule "Test inputs and expected values"
    reads the same; the file is now identical to `a2f1165`.
  - Kept, as the review allows: WAY-228's *Rationale* "a condition kept after every step", which
    describes developers' practice read off Goldstein and Hypothesis in the field sense.
  - Correction 2 (refine-task step 3, WAY-215) stands unchanged.
- **Corrected statement on WAY-228's meaning:** the commit `f3c7f7e` did change the meaning of
  WAY-228 — it dropped the sentence of a product's invariant from the relations a property test may
  take its expected value from, against Q13. This fix restores the binding sentence to its wording at
  `a2f1165`; after `8c74925` WAY-228's binding part is as the foundation step wrote it, and the return
  step leaves its meaning unchanged. The earlier line "the meaning of WAY-228 does not change" and the
  rendering note for the request are withdrawn; the request carries no rendering of "zdanie
  niezmiennika" from this step.
- **Checks:**

  | Command | Exit | Result |
  |---|---|---|
  | `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
  | `python -B gate/run_tests.py elements/common` | 0 | OK |
  | `git diff --check f3c7f7e` | 0 | empty |

- **Not fixed:** the review's Minor finding, as the dispatch gives.
- **Reach:** `research_wytyczne_testow/raport_wytyczne_testow.md` lines 29 and 46, to verify the
  finding's evidence.
