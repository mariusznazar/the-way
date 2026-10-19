# Return step — coding guidelines (task cycle step 11, WAY-11)

Agent: return-step agent R (fresh general-purpose subagent, claude-opus-5-5); wrote no code, no
check and no test of this change. Worktree `/home/user/the-way`, branch
`claude/gallant-albattani-3k15lc`, base `5a00041`. Skills `the-way-record-invariant`
(`elements/invariants/skill/SKILL.md`) and `the-way-update-part-map`
(`elements/part-map/skill/SKILL.md`) of this checkout, with their templates, `examples.md`,
`elements/common/rules.md` and `elements/common/way_of_working.md`, read whole. Python 3.13.16 (the
repository declares 3.14; O3).

**Status:** done. One commit, `355a240`. Two foundation changes written (one invariant sentence
edited in place, one part-map dependency). No new decision, glossary term or environment fact. One
question for the orchestrator (Q1, the deferral of a kind against WAY-201). Nothing pushed.

## Inputs read

- Handoff `reports/return-step-handoff.md`; `cycle.md` whole (O1–O4, C1–C38, events);
  `task-frozen.md` whole (To do 1–8, Q1–Q18, K1–K3, rows 1–25, *Decisions in play*, *Out of
  scope*); `reports/foundation.md` whole (F1a, F1b, F2, F3, C38 fix); `reports/final-review.md`
  whole (I1, M1–M4, graded ledger, review of the fix, N1); the `Ruling:` and `Task N: minor` lines
  of `reports/sdd/progress.md`; `spec.md` at the passages on the kind index (§5.2 item 3, §4.3,
  §6.5).
- The real diff `235b0b4..5a00041` (51 files, +4147 −212) by `git diff --stat` and by file where
  the comparison needed it: `task-cycle/skill/SKILL.md` (whole diff), `product-guidelines/template.md`
  (whole diff), `README.md`, `installation/README.md` (whole diffs), `product-guidelines/form_check.py`
  (`refused`, `check_paths`, `kind_of`, `check_kind_index`, the listing of `guidelines/`,
  `tracked_paths`), `product-guidelines/coding/SKILL.md` (lines 28–40, 176–226 and the references
  to other parts), `product-guidelines/coding/template.md` (references to other parts, lines
  236–246), `product-guidelines/test_form_check_invariants.py` (KindIndex, CodingFixtures, the
  inner-fence test) and the test names of `product-guidelines/test_form_check.py`.

## Reading the foundation (WAY-150)

- Revision: `5a00041`, then the written change `355a240`.
- Part map read whole. Touched parts by the real diff: `agent-instructions` (`.claude/skills/**`,
  `.agents/skills/**`), `installation`, `product-guidelines`, `task-cycle`; by the entries the
  change adds or edits (WAY-44): `decisions`, `invariants`, `gate`, `instruction-files` (*Scope* of
  WAY-167, 168, 193–212), `glossary`, `part-map`, `elements-common`, `relation-model` (*Part* of the
  `guidelines-check-*` entries). `README.md` is left out on purpose.
- *Scope* of all 198 decisions inspected by script (wrapped values joined, latest version of each
  number): 180 name a touched part; the 18 that do not are WAY-80 (`environment-facts`) and WAY-108,
  109, 110, 111, 112, 118, 139, 142, 143, 145, 146, 151, 152, 153, 154, 155, 156 (`project-level`).
  No missing or malformed *Scope*.
- Read: the binding sentences, *Scope* and title of all 198 decisions (dump in the scratchpad);
  whole entries (all fields, rationale, *Rejected*) of WAY-11, WAY-31, WAY-36, WAY-57, WAY-134,
  WAY-150, WAY-167, WAY-168, WAY-193, WAY-194, WAY-196, WAY-197, WAY-198, WAY-199, WAY-200,
  WAY-201, WAY-202, WAY-203; the *Rationale*, *Review when* and *Based on* lines of WAY-204 and
  WAY-206. The remaining 162 matched decisions were read by binding sentence only — discovered, not
  read whole; none of them is touched by what this step writes, and each relevant one is named
  under the searches below.
- Invariants: every `guidelines-*` entry whole (ten), `gate-guidelines-example-evidence`,
  `gate-fork-point-evidence`; headings of the whole file; *Part* of entries naming
  `product-guidelines` or `task-cycle`.
- Glossary: every term and *Avoid* (36 terms); whole entries of guidelines, invariant, invariant
  test, exemplar, standing check.
- Environment facts: every heading (30 entries).

## Settlements to record (WAY-134)

All 25 rows are written; none was missed by the foundation step: 1 WAY-167 (with WAY-212 for the
table), 2 WAY-198, 3 WAY-200, 4 WAY-199, 5 WAY-202, 6 WAY-206, 7 WAY-203, 8 WAY-204, 9 WAY-205,
10 WAY-196, 11 WAY-168, 12 WAY-197, 13 `gate-guidelines-example-evidence/1`, 14 WAY-194, 15
WAY-212, 16 WAY-193, 17 WAY-195, 18 WAY-208, 19 WAY-209, 20 WAY-210, 21 WAY-211, 22 WAY-201 (after
C38), 23 WAY-207, 24 `exemplar`, 25 `standing check`. I read each binding sentence against its row;
the weak points rows 6 and 8 ask the decision to name stand in WAY-206's and WAY-204's rationale.
The task is independent: no projected entries (WAY-126).

## Candidates found and how each was settled

| # | Candidate | Source | Settled as | Requirement or reason; tests or change description |
|---|---|---|---|---|
| 1 | `guidelines-check-kind-index/1` says "git lists" where the form check reads what git tracks | ledger T3, final review (Minor in scope); `form_check.py` `check_kind_index` uses `tracked_paths` (`git ls-files -z`, tracked only), while the listing of `guidelines/` uses `--others`; the checks citing it already treat an untracked general file or row target as absent | **entry edited** (below) | WAY-167, WAY-212 (level 1); the sibling `guidelines-check-exemplar/1` and the coding template say "git tracks" |
| 2 | `task-cycle` now restates the form of a product's guidelines' test cases (steps 10 and 11) | diff of `task-cycle/skill/SKILL.md` (`faf43c9`); before `235b0b4` the skill named no guidelines | **part map changed**: `task-cycle` *Depends on* gains `product-guidelines` (below) | WAY-40, WAY-44: an allowed dependency stands at the part it starts from |
| 3 | The skill lets the human defer a kind of code; WAY-201 asks a proposed exemplar for every kind the product holds files of | final review N1; C35, C38; `product-guidelines/coding/SKILL.md:180-183`, `:221-223` | **no entry; question Q1** | An exception in WAY-201 would change row 22's meaning, which takes the human (WAY-134, WAY-30); the other way changes code, which is not this step's |
| 4 | The form check refuses a case path or *File* holding `\`, `:` or a character that is not printable, beyond the invariant's list (absolute, `..`, drive, UNC) | `form_check.py:1202-1214` | **detail** | The extra refusals are how the check detects a drive or UNC prefix and keep crafted paths from git; relaxing one violates no decision as long as the invariant's four still hold. `product-guidelines/test_form_check.py:812`, `:952`, `:1313`, `:1382`, `:1762`; the common template's *Test cases of a rule* |
| 5 | A fence line inside a case is reported at any indentation and after every line break Python splits lines on (C33), while the invariant tests check up to three spaces | `test_form_check_invariants.py:1368`; ledger C33 | **detail** | The invariant's "would open a fence" is read as the template defines it; the wider reading keeps `check_instructions.py`'s toggling right, which the template's note says is "no rule of the template". `product-guidelines/test_form_check.py:1148`, `:1165`, `:1184`, `:1214`; change description (C33) |
| 6 | A file of a kind left out of `## Files of this kind` passes: the form check asks no completeness (C13) | `coding/template.md:177-180` | **detail** | Rows 3 and 4 give a status to every file at the audit, not a duty of completeness later; `product-guidelines/test_form_check.py:934` |
| 7 | A kind's name that is no identifier (`coding-.md`, `coding--a.md`, `coding-A.md`) is an error; a file below a directory named like a kind is warned of and not read | `form_check.py` `kind_of`, listing of `guidelines/` | **detail** | The template's form of a name, under `guidelines-form/1`; `product-guidelines/test_form_check.py:446`, `:461` |
| 8 | The reviewer applies a test case only in a scratch worktree of the commit, never in the task's worktree | `task-cycle/skill/SKILL.md` step 10 | **detail** | WAY-197 sets that the reviewer runs the method with both uses and records it, not where; the request's description carries it (Markdown, no test) |
| 9 | The installer refuses a conflicting file, a directory or a non-UTF-8 file at the new skill's entry points | `installation/test_coding_guidelines_installation.py` | **covered** | the surface `installation-command` (replaces no existing file) and `installation-claude-guidance/1` (`NAMES`) |
| 10 | The coding skill gives the configuration of the standing checks to the part holding the build configuration (C5) | `coding/SKILL.md:68-69` | **covered** | WAY-44 already sets the build configuration as a part of its own; the product's map decides through `update-part-map` |
| 11 | The coding skill points to `installation/README.md` for a product that pinned the-way before the skill existed | `coding/SKILL.md:33` | **no part-map change** | A pointer to where the procedure stands; no behaviour of `product-guidelines` rests on the README's content, as with the styleguide skill's mention of the installer's block (no such dependency on the map) |
| 12 | "test case" in the common template, the coding template and the task-cycle skill | diff | **no glossary entry** | Used in the meaning a reader of the field gives it (an input with its expected outcome), never in a binding part (WAY-168 says "use"); no second meaning; it is no invariant test (WAY-65, F1a) — WAY-95 asks for none. "scratch worktree" is git's plain sense; "kind", "general file", "trial run" weighed by F2 |
| 13 | A case path naming `.git/…` passes the form check | final review M3 | **no entry** | Nothing in the-way applies a case outside a linked scratch worktree (where `.git` is a file, so no hook can be written); the gate that would apply cases has `Method: TODO` and is out of scope. It stays a review finding the request lists (step 13), not a failure mode written now |
| 14 | Environment facts the change rests on | WAY-195 *Based on*; `git ls-files` | **none** | WAY-195 cites a fixed commit and a published edition (WAY-90), as F1a found; the sibling invariants that say "git tracks" rest on no fact |
| 15 | Choices C3, C4, C12, C28, C36, C37 | cycle choice table | **one line each in the choice table** | template text adopted only by a product's decision (WAY-193), WAY-60/WAY-133, template form, already in WAY-200, ordinary tests; none binds as a the-way rule after the merge beyond what entries state (WAY-36) |

## Entries written

### `guidelines-check-kind-index/1` — edited in place (version 1, *Correction* `none`)

The entry is new in this change and there is no main branch, so the version stays 1 and no
correction is declared (WAY-57, `elements/common/rules.md`). Fingerprint `2a02b7c1` → `e19f30f2`;
no link, guidelines file or code carries the old one (grep outside `.runs/`). Every other field
unchanged.

- Old: The form check of guidelines, `product-guidelines/form_check.py`, reports as an error every
  file `guidelines/coding-<kind>.md` git lists that no row of the table under `## Kinds of code` in
  `guidelines/coding.md` names by its path in *File*, every row of that table whose *File* names no
  file git lists, whose *Kind* is not the `<kind>` of the file its *File* names or whose *When to
  read* is empty, and every file `guidelines/coding-<kind>.md` git lists where git lists no
  `guidelines/coding.md`.
- New: The form check of guidelines, `product-guidelines/form_check.py`, reports as an error every
  file `guidelines/coding-<kind>.md` git tracks that no row of the table under `## Kinds of code` in
  `guidelines/coding.md` names by its path in *File*, every row of that table whose *File* names no
  file git tracks, whose *Kind* is not the `<kind>` of the file its *File* names or whose *When to
  read* is empty, and every file `guidelines/coding-<kind>.md` git tracks where git tracks no
  `guidelines/coding.md`.
- Meaning (pl): Skrypt formy zgłasza jako błąd każdy śledzony przez git plik rodzaju
  `guidelines/coding-<rodzaj>.md`, którego nie wymienia tabela `## Kinds of code` w
  `guidelines/coding.md`, każdy wiersz tej tabeli wskazujący plik, którego git nie śledzi, z *Kind*
  niezgodnym z rodzajem pliku albo z pustym *When to read*, oraz każdy śledzony plik rodzaju, gdy git
  nie śledzi `guidelines/coding.md`.
- Authors (WAY-69): sentence — return-step agent R (the original sentence: foundation author B);
  check — check author D (`64344a3`); covered code — executor S3 (`0607656`).

### Part map, part `task-cycle` — *Depends on*

- Old: `decisions · invariants · glossary · part-map · environment-facts · elements-common ·
  project-level · gate · relation-model`
- New: the same, followed by `· product-guidelines`.
- Meaning (pl): Część `task-cycle` może zależeć od części `product-guidelines`: kroki 10 i 11 cyklu
  zadania powtarzają formę przypadków testowych reguł wytycznych, którą ustala szablon wytycznych.
- The binding sentence of the part is unchanged (the fingerprint covers it alone, WAY-42); the
  files its pattern claims are unchanged. `product-guidelines` already depends on `task-cycle`, so
  the two now depend on each other, as `elements-common` and `project-level` already do. Both parts
  are `high`; no computed criticality is lowered (the guard reports the lowering `unchecked` with
  `--base none`). No dependency graph command exists, so the comparison with the code stays
  unchecked, as before.

## Invariants whose check must be written or changed

- `guidelines-check-kind-index/1` (sentence above): no check needs a different expected value. The
  existing checks citing it — `product-guidelines/test_form_check_invariants.py` `CodingFixtures`
  (line 1021) and `KindIndex` (lines 1145–1199) — already treat an untracked
  `guidelines/coding.md` and an untracked row target as absent, which the new sentence states. As
  `record-invariant` gives it after step 4.4, hand the entry and its method to an agent that wrote
  neither the sentence nor the code (check author D) to confirm that no citing check needs a change.
  For the reviewer who wrote neither the check nor the sentence, a deliberate break from the new
  sentence: make `check_kind_index` count `guidelines/coding.md` as present when it stands in the
  working tree but git does not track it; the subtest "the general file untracked" of
  `test_a_kind_file_with_no_general_file_is_reported` must fail. No rule of a `guidelines/` file
  names this invariant (the-way has no `guidelines/`), so no `good`/`bad` run applies.
- No invariant is new in this step, so no check is to be written.
- For the request, not from this step: the invariant tests still lack the two clauses C32 left
  unchecked (`guidelines-check-example-files/1` "left open to the end of the file";
  `guidelines-check-exemplar/1` for a kind file lacking `## Files of this kind`); ordinary tests
  cover both (`test_form_check.py:1117`, `:867`).

## Foundation compared with the code (parts the task touched)

- `product-guidelines`: WAY-167, 168, 170, 171, 193–212 against the templates, the skill and the
  form check — they agree, except Q1 (skill defers a kind, WAY-201 does not allow it) and candidate
  1 (fixed). The form check's new behaviour is under `guidelines-check-form`, `-carrier`,
  `-kind-index`, `-exemplar` and `-example-files`; what lies beyond their sentences is in candidates
  4–7. The part's sentence ("the template of each discipline … with the skill that leads the work
  on them") covers the coding discipline; its trust boundary `product-guidelines/form_check.py` is
  right (case and table paths are refused before git and never opened).
- `task-cycle`: steps 10 and 11 implement WAY-197 and WAY-168's runs of the uses; the dependency is
  now on the map (candidate 2). The textual tension between line 63 ("writes only in the task's
  worktree", WAY-140) and step 10's scratch worktree crosses no decision (WAY-140 is about effects
  outside the repository); it is a review finding of the request (T5).
- `installation`: `SKILLS` gains `maintain-coding-guidelines`; WAY-127, WAY-141 and the surface
  `installation-command` hold; `installation-claude-guidance/1` checks the names.
- `agent-instructions`: the 34 entry points (17 skills, two directories) are current
  (`skill-entry-points/1`; `agent-instructions/skill_entry_points.py` exit 0); WAY-127 holds.
- `decisions`, `invariants`, `glossary`, `part-map`: every level 1 identifier of WAY-167, 168, 196,
  198, 199, 202, 212 stands in its invariant's *Derives from*; guards report no error.
- `gate`: `gate-guidelines-example-evidence/1` with `Method: TODO`, reported `unchecked`; no code.
- `instruction-files`: WAY-212 binds a product's `AGENTS.md`; nothing in this repository's
  instruction files changed.

## Searches of the whole foundation (WAY-33)

At `5a00041` and on the written change:

- For the invariant: "git lists", "git tracks" and the identifier in `foundations/`, `elements/`,
  `product-guidelines/*.md`, `product-guidelines/*/*.md`, `task-cycle/`; "git lists" stands
  nowhere else in `foundations/` (only in docstrings of the elements' guards, in git's own sense);
  the coding and common templates say "git tracks". Decisions whose level 1 names it, WAY-167 and
  WAY-212, read against the new sentence: both still hold. No failure mode or flow names it; no
  link carries its fingerprint.
- For the dependency: WAY-40, WAY-44, WAY-45, WAY-46, WAY-55; the flow
  `skills-reach-the-way-sessions` (lists both parts already); every part's *Depends on*. No
  collision; no decision rests on the boundary between the two parts.
- Glossary words in the new text: "part", "invariant" in their term meanings; no paraphrase of a
  definition.

## Checks (Python 3.13.16, at the written change; output in this directory, exit code on the last line)

| Command | Exit | Output | Result |
|---|---|---|---|
| `python3 -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none` | 0 | `return-guard-decisions.txt` | 0 errors; 27 warnings (5 passed check-by dates, 22 `merge of <request link>` placeholders), as at `5a00041`; 5 unchecked for the missing base |
| `python3 -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none` | 0 | `return-guard-invariants.txt` | 0 errors; 3 unchecked for the missing base |
| `python3 -B elements/glossary/format_guard.py foundations/glossary.md --base none --merge-onto none` | 0 | `return-guard-glossary.txt` | 0 errors; 5 unchecked |
| `python3 -B elements/part-map/format_guard.py foundations/part_map.md --base none` | 0 | `return-guard-part-map.txt` | 0 errors; 7 unchecked (coverage of two flows, change paths, dependency graph, known violations, identifiers, lowering of criticality) |
| `python3 -B elements/environment-facts/format_guard.py foundations/environment_facts.md --base none --merge-onto none` | 0 | `return-guard-environment-facts.txt` | 0 errors; 3 unchecked |
| `python3 -B gate/run_tests.py elements/decisions` | 0 | `return-tests-elements_decisions.txt` | 169 OK |
| `python3 -B gate/run_tests.py elements/invariants` | 0 | `return-tests-elements_invariants.txt` | 233 OK |
| `python3 -B gate/run_tests.py elements/glossary` | 0 | `return-tests-elements_glossary.txt` | 204 OK |
| `python3 -B gate/run_tests.py elements/part-map` | 0 | `return-tests-elements_part-map.txt` | 162 OK |
| `python3 -B gate/run_tests.py gate` (critical flows) | 0 | `return-tests-gate.txt` | 98 OK |
| `python3 -B gate/run_tests.py product-guidelines` | 0 | `return-tests-product-guidelines.txt` | 137 OK (the tests citing `guidelines-check-kind-index/1` pass) |
| `python3 -B gate/run_tests.py relation-model` | 0 | `return-tests-relation-model.txt` | 19 OK |
| `python3 -B gate/run_tests.py task-cycle` | 0 | `return-tests-task-cycle.txt` | 41 OK |
| `python3 -B agent-instructions/skill_entry_points.py` | 0 | `return-entry-points.txt` | entry points are current |
| `git diff --check` | 0 | — | clean |

Not a pass of the full gate. Fingerprints in links and `TODO` are `unchecked` with `--merge-onto
none`; the old fingerprint of the edited invariant is carried by nothing (grep).

## Commits

- `355a240` — `docs(foundations): return step — kind-index says "git tracks"; task-cycle depends on
  product-guidelines`. Changed: `foundations/invariants.md` (+1 −1), `foundations/part_map.md`
  (+1 −1). The message carries the WAY-33 search record and the checks. Not pushed.

## Questions

- **Q1 (for the orchestrator).** `product-guidelines/coding/SKILL.md:180-183` (and `:221-223`,
  *Context* at `:81-84`) lets the human defer a kind of code from the audit; WAY-201 binds the audit
  to end with a proposed exemplar for each kind the product holds files of, with no exception (row
  22, Q6). That is a contradiction between code and a decision (WAY-30): an exception lives only in
  a decision's binding sentences, never in a skill or a cycle record. Ways: (a) executor S6 drops
  the deferral from the skill, which brings the code in line with row 22 and needs no human; one
  scoped re-review; (b) a blocked draft request asking Mariusz whether WAY-201 takes the exception
  "unless the human defers a kind, recorded with the reason", since it changes the meaning of his
  row 22 (WAY-134). Recommendation: (a) — C38 already restored row 22 as the human's meaning, and
  the skill keeps its recommendation to audit every kind; cost: a human who wants to postpone a
  kind runs the audit anyway or opens another task. I wrote no entry for it.
- Outside the task, for the process remarks: `elements/part-map/examples.md` describes `task-cycle`
  as "a part whose tool does not exist yet, so it holds no files", while the part holds
  `task-cycle/**`.
