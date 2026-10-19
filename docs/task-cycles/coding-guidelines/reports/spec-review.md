# Spec review: coding guidelines (step 7 of the task cycle)

Reviewer: Claude Code general-purpose subagent, claude-opus-5-5, one turn. I did not write the
spec. Read only: no tracked file and no `spec.md` edited, nothing committed. Base `235b0b4`, branch
`claude/gallant-albattani-3k15lc`.

## Verdicts

- **Task compliance: compliant, with one narrowing to fix (I-4).** All eight *To do* items, all 25
  rows and the answers to Q1–Q18 are carried. Nothing out of scope is brought in. One addition the
  rows do not name: a severity threshold for the audit (m-6).
- **Foundation coherence: coherent, with three Important gaps (I-1, I-2, I-3).** I found no direct
  contradiction with a binding sentence that a decision of the spec does not already override by a
  stated precedence. The gaps are the dependency audit's verdict moving with no commit (WAY-61,
  WAY-68), the reach of the product's standing-check invariants (WAY-62, with C5), and F1 test cases
  that cannot be written honestly for some required rules.
- **Rulings C1–C9:** all fit the task and the foundation. C1 needs the I-1 additions. C5 brings
  I-3 with it. C9 needs I-4. C3 needs m-5.
- **Can a plan be written from it: yes.** Files, tests and commands are named and can run. The
  plan must read the spec together with `design-rulings.md`, because §4.3 (C3, C4) and §2/§8.4
  (C2) still show the proposals as they stood before the rulings. It must also add what m-3 names.

Counts: **Critical 0 · Important 4 · Minor 12** (plus 2 observations, ungraded).

## Important

### I-1: F1 test cases cannot be written honestly for some rules the templates require (spec.md:251-264, :293-296, :578; C1)

Evidence:

- **The styleguide's "Every background with its text" runs into a regress.** Its *Invariant* is
  the product's copy of `guidelines-form` (`product-guidelines/styleguide/template.md`, "Every
  background with its text"). Under F1 its good test case is a whole file of guidelines. That file
  must itself pass `guidelines-form`. So it holds its own "Every background with its text" with
  its own good/bad blocks, which hold whole styleguides in turn. The chain ends only with fake
  inner blocks, which pass because the form check looks only for a block and a path (spec.md:293).
  So the template asks for a test case that cannot be honest.
- **Lockfiles hit the read limit.** For `### Dependency audit`, a test case "in place of the file
  there" (spec.md:255) is a whole lockfile. Two lockfiles inside `guidelines/coding.md` can pass
  `MAX_BYTES = 1048576` (`form_check.py`). The form check then refuses to read the file at all
  ("holds more than … bytes; it is not read").
- **Nested fences go unspecified.** Test cases whose text holds fences (Markdown files, the
  styleguide above) need a longer or tilde outer fence. The spec lists these only as crafted inputs
  (spec.md:319). `instruction-files/check_instructions.py` toggles on any line that starts with
  ```` ``` ```` or `~~~` (its `FENCE`, line 57), whatever the fence length. Once a product's
  `AGENTS.md` points to the file, inner fences flip its code/prose reading.

What the spec should say:

1. Which fences a test-case block may use, and that the form check reads the info string only from
   an opening fence.
2. That a test case may be a new short file at a path that does not exist, which C1 allows. The
   template should say so and name the size limit, and give the shape of the test cases for each of
   the three standing-check rules (for example, a new one-dependency lockfile at a new path for the
   audit, where the product's audit script reads it).
3. What a rule whose invariant is the form check itself gives as its test cases. Either it is
   exempt from the blocks or the regress is cut by rule. **This needs an orchestrator ruling (Q-B).**

### I-2: the audit's verdict on one commit moves with the advisory database (spec.md:196-200, :468, :485-487; ruling point 2)

**What the foundation says.**

- WAY-61/1: "A method checks what its sentence is about, as it stands on the commit being checked".
- WAY-68/1: "A check that cites an invariant and records both `pass` and `fail` for one commit is
  answered by a foundation change, quarantine last". Its binding text does not ask what caused the
  flip.
- The task's own CQ6 asks how the verdict stays "ten sam przy każdym uruchomieniu (WAY-61)".

**What the spec does.** It pins the tools' versions (§4.4), but the invariant reads "as that
database gives it" (spec.md:199-200), with no moment fixed. So a rerun on one commit can turn
`pass` into `fail` when an advisory is published for a version the change brings in.

**WAY-60 holds only by its letter.** A decision may place the condition in a named database.
WAY-60's rationale, though, is that "a condition outside the sentence moves unseen by the
fingerprint … so it stands only where moving it takes a decision". That rationale is not kept: the
database moves with no decision.

**Q13 covers only part of this.** Its question names "baza podatności zmienia się bez commita", and
its answer accepts a weak point only for dependencies the product already has. It does not settle a
flip on a version the change itself brings in.

The spec only mentions this ("see the design report's concerns"). It must settle one of:

- (a) WAY-206 names the flip and narrows WAY-68 for it (a later `fail` is the entry's result and no
  flipping check). This is a new meaning no row gives, so under WAY-30/WAY-172 it needs Mariusz's
  approval before the code, through a blocked draft request.
- (b) The adopting decision pins the advisory database to a snapshot the product commits, so the
  verdict follows the commit. WAY-61 and WAY-68 stay untouched. The cost: a change bringing in a
  version first flagged after the snapshot passes until the snapshot moves, which is weaker than
  Q3's "pada tylko na podatnościach, które sama wprowadza".
- (c) WAY-68 applies unchanged. WAY-206's rationale says a flip is answered as WAY-68 gives it, and
  in practice by a new commit that drops the vulnerable version. The commit that flipped keeps its
  `fail`.

**This needs an orchestrator ruling (Q-A).** Recommendation: (c) as the smallest reading that keeps
every current decision, with the flip named in WAY-206's weak point. (a) only on Mariusz's word.

### I-3: the standing-check invariants miss their reach, because their configuration and the lockfile sit in another part (spec.md:97-99, :182-200; WAY-62; C5)

**What WAY-62 says.** A change reaches an invariant only through a part that invariant names, or
through a file its method's command names.

**Why this matters here.**

- C5 puts the tools' configuration in the part that holds the build configuration.
- WAY-44 puts the lockfile in that same part.
- The methods are product scripts, whose commands name neither file.

**What the spec leaves out.** §4.3 gives no *Part* for any product invariant. The styleguide
template, by contrast, names the parts for its invariants ("whose *Part* names that part and the
part holding `foundations/**`").

**The consequences, if the template names only the code's parts:**

- A change touching only the lockfile never reaches the audit invariant, though that is exactly the
  change the audit is for.
- A change touching only the linter's configuration never reaches invariant (2), which exists to
  catch a rule turned off (row 23, C4).
- Neither reaches the linter or formatter invariants either.

**What the spec should say.** Template §4.3 should give each standing-check invariant's *Part*: the
parts holding code, plus the part holding the build configuration and the lockfile. The audit's
*Part* in particular must include the lockfile's part.

### I-4: "a status for each file" from row 3 is narrowed (spec.md:208, :366-369)

**What the task says.**

- Row 3 / Q6: the audit proposes the exemplar "ze statusem każdego pliku „kopiować / nie
  kopiować”".
- Row 4: the status stands beside the paths in the kind file.
- To do 3 repeats "ze statusem każdego pliku".

**What the spec says.**

- §4.3: "Files not listed have no status; the table is no inventory of the kind."
- §6.2 step 3 gives `copy` only "for the others judged", without saying that every file of the
  kind is judged.
- The design report's rejected alternative reads "An inventory of every file of a kind … no row
  asks for it". That misreads row 3 as it applies at the audit.

**What the spec should say.** The audit judges every existing file of a kind and gives each a
status, and the kind file lists each file with its status at that audit. Whether files added after
the audit need a row is a separate choice of the cycle, to be stated explicitly. **Orchestrator
ruling advised (Q-C)**, though the fix is a wording change.

## Minor

1. **Ruling point 3: `guidelines-form/1` covering the new findings (spec.md:299-302).** The
   reading mostly holds.
   - **Where it holds.** The styleguide template already relies on the product's copy of
     `guidelines-form` for a table check ("Every background with its text": "whose form check
     reports a background with no text role"). Commit `19d28f8` widened that sentence to "the values
     and the links those templates give it". That covers the index, the closed list of *Status*,
     exactly one exemplar row, and the presence of the blocks.
   - **Where it is weakest.** First, the check that each *File* "names something git tracks": the
     sentence names git-tracked paths only "under `## Where in code`". Second, the check of the
     decision's binding text for path and kind.
   - **Recommendation.** The coding template should state, as the styleguide template does, which
     of its checks the product's copy of `guidelines-form` carries. If the git-tracked *File* check
     stays, either reword `guidelines-form/1` before `main`, or accept it as read. No product holds
     a copy yet, since PR #25 merged today, so a pre-`main` edit at /1 breaks nothing.
2. **Ruling point 1: WAY-171 after the WAY-168 edit (spec.md:251-259, :438-445).** No edit is
   needed. WAY-171 sets the four fields, and a rule's body ("followed by how to apply it" in the
   common template) can hold the blocks. The renewal under WAY-31 finds WAY-171 still true. Two
   follow-ups:
   - The common template's line "*Good* gives a use that follows the rule and *Bad* one that breaks
     it" must become "describes", since under the edited WAY-168 the use is the file.
   - §5.1 should say where the blocks stand: after the four fields, in the rule's body.
3. **The common template's "Where guidelines go" is missing from §3.1 (spec.md:79).** That section
   restates WAY-167's file names. Once WAY-167 is edited, its text must gain `coding.md` and
   `coding-<kind>.md` (WAY-171: templates follow decisions). §3.1 lists the template only for the
   test cases.
4. **WAY-167 stays level 2 though `guidelines-check-kind-index` checks the table it now names
   (spec.md:436-437).** WAY-12's violating example is "a decision whose rule a lint check could
   enforce is left at level 2". Either WAY-167's *Verification* level 1 names `kind-index` (and
   that invariant derives from WAY-167 too), or the spec says the table's binding text stands in
   WAY-212 alone.
5. **C3's suppression clause needs a decision to cite (spec.md:185-186).** WAY-171: "a rule of
   the-way's templates of guidelines changes only with a decision of the-way and cites its number".
   C3 makes the clause template text the skill proposes, not a sentence of a decision of the-way.
   So the template must cite the decisions it rests on: WAY-203 and WAY-193. WAY-207's "in that
   file" can be read as allowing a per-file suppression, so WAY-207 alone is not enough.
6. **The severity threshold of the audit is not in row 6 or Q13 (spec.md:197-199).** Row 6 says it
   fails "tylko na podatnościach, które sama wprowadza", with no threshold. A threshold is a valid
   choice for the product, settled with the human and placed by its decision (WAY-60). The template
   should present it as a choice, with "every severity" open, not as a given. If it comes from Open
   Mercato's `--severity high`, WAY-195 should name it as taken.
7. **One environment fact per edition (spec.md:224-227).** This is defensible: one fact for the
   set's membership, one source edition, one reason to change, as with WAY-76's "path-pattern rule
   with its page's two exceptions". But WAY-86 says "a requirement … is an environment fact", and
   the styleguide precedent WAY-191 went one fact per criterion. The template or WAY-204's rationale
   should state what the fact's sentence holds (the list of rules of the set at that edition) and
   why that is one fact under WAY-76, so that the assessment of WAY-10 does not reopen it.
8. **The trial run (spec.md:360-365, :384-388).**
   - The spec does not say that running a rule set on a product with no linter yet leaves the
     product's tracked files untouched. The skill writes only `.runs/coding/` (spec.md:338-339), and
     installing a tool would change the lockfile. It should say the run happens in a scratch
     worktree or a temporary environment.
   - §6.3, orchestrated mode, asks the orchestrator for research agents and critics, but not for the
     fresh agent that judges the trial run (WAY-204).
9. **WAY-48 for the installer.** `installation/install.py` is a trust boundary at its part, and
   WAY-48 says "A change that touches the files of a boundary is checked for crafted input,
   whatever the criticality". §5.3 covers only the form check. The plan should name a check for the
   installer, even if it is short, since the change adds one `SKILLS` entry and no new parsing.
10. **The justification for "kind" is inaccurate (spec.md:61).** It says the `Kind` column lives
    outside the files WAY-99 counts. But WAY-176's binding text in `foundations/decisions.md` uses
    "of the kind `background`, `text` or `other`". The conclusion stands, because both uses carry
    the plain meaning a reader of the field gives (WAY-99 applies only to an unusual meaning). Only
    the reason should be corrected.
11. **"exemplar" and WAY-95 (spec.md:64-66).** If the definition drops "designated by a decision",
    which §2 allows under WAY-96, what is left is the plain English sense of "exemplar". WAY-95 then
    gives no ground for the entry row 24 requires ("a word takes an entry for its plain meaning only"
    is a violation). The glossary skill should keep in the definition whatever separates the term
    from its plain sense, or record why the entry still qualifies.
12. **Nothing runs the standing-check invariants in a product before a gate exists.** WAY-170
    gives the form check an exception: the installer's block names its commands. The styleguide's
    invariants already carry the same gap, and WAY-16 forbids naming a lint command. Running the
    gate automatically is out of scope (Q1), so this is not a finding to fix here. The request
    should still say so, because the *Need*'s "bez czyjejś pamięci" holds only when a cycle runs the
    methods of the invariants a change reaches.

## Observations (ungraded)

- `cycle.md` (Foundation route) counts "23 decisions, 1 invariant, 2 glossary terms" for 25 rows.
  The rows hold 22 decisions (20 new, 2 edits), 1 invariant and 2 terms, as the spec has it.
- Spec §4.3 (2), §4.3 (1) and §2/§8.4 still read as proposals. The plan's inputs must apply C2,
  C3 and C4 as ruled.

## Task compliance, item by item

| Item | Where in the spec | Result |
|---|---|---|
| To do 1 (template, two forms, every rule an invariant, binding by adoption, names) | §4, §8.1 WAY-167, WAY-193, WAY-196 | carried |
| To do 2 (skill: recognize, extend, new tool as question with default, research, every part with code, ask each choice by effect) | §6, WAY-194, WAY-208–211 | carried |
| To do 3 (exemplar, approval, checked rules, audit with status, proposal with gain and file:line) | §4.2–4.3, §6.2 step 3, WAY-198–201 | carried, narrowed: I-4 |
| To do 4 (standing checks, departure, rule set by decision, change-only audit, no-false-alarm blocking, trial split, known-violation pair, one reformat, fix in file, bind from task) | §4.3–4.4, WAY-202–207 | carried; I-2, I-3, m-6 |
| To do 5 (test cases, checked only on change, gate invariant, WAY-69 unchanged) | §5.1, §7, WAY-168 edit, WAY-197, `gate-guidelines-example-evidence` | carried; I-1 |
| To do 6 (WAY-195 with citations, two Google conditions left) | §8.3 | carried |
| To do 7 (AGENTS.md pointer outside block; index with when to read) | §4.3, §6.4, WAY-212 | carried |
| To do 8 (form check and invariants accept `coding`; entry points; `SKILLS`) | §5.2, §6.6, §8.5 | carried |
| Rows 1–25 | §8.1–§8.5, §2 | each carried with its meaning; row 3: I-4; row 6: I-2, m-6 |
| Q1–Q18 | throughout | respected; Q13 partly (I-2) |
| Out of scope | §1 | nothing brought in |

## Foundation entries read

Read whole: WAY-04, 05, 08, 09, 12, 16, 22, 29, 30, 31, 36, 44, 48, 51, 60, 61, 62, 63, 68, 69,
73, 74, 76, 82, 86, 94–100, 113, 114, 122, 127, 128, 129, 133, 139, 160, 161, 167–192. Invariants:
`invariant-test-break`, `level-one-decision-invariants`, `verification-invariant-derivation`,
`gate-fork-point-evidence`, `gate-check-source`, `skill-rule-source`, `script-language`,
`invariant-tests-of-change`, `skill-entry-points`, `instruction-file-imports`,
`root-claude-md-import`, `installation-claude-guidance`, all eight `guidelines-*`. Also read: the
part map's `product-guidelines`, `installation`, `skills-reach-the-way-sessions` and
`installation-command` entries, and the glossary's headings with *Avoid* and *Not*.

Code and templates: `product-guidelines/template.md`, `styleguide/template.md`, `styleguide/SKILL.md`
(whole); `form_check.py` (lines 1–1000 and the function list of the rest); `install.py` (`SKILLS`,
`skill_wrapper`, `product_guidance`); `task-cycle/skill/SKILL.md` steps 8–11 and "The end of a code
review"; `installation/README.md` on pin moves; `instruction-files/check_instructions.py` (fence
handling); `relation-model/fingerprint.py`; research `research_open_mercato.md` (the lines quoted
by WAY-195).

Dependents found by a fingerprint search over the whole repository: `@681d47ff` has none;
`@47d9d53e` is carried by WAY-171, WAY-173, WAY-188 and `guidelines-check-carrier`. That matches
spec §8.1.

## Questions needing an orchestrator ruling

- **Q-A (I-2): how the audit's verdict stays the same on a commit.** The ways are (a) narrow WAY-68
  (needs Mariusz), (b) pin a snapshot of the database, (c) WAY-68 applies unchanged, with the flip
  named as a weak point. Recommendation: (c).
- **Q-B (I-1): what test cases a rule gives when its invariant is the form check itself.** For
  example the styleguide's "Every background with its text": either it is exempt from the blocks,
  or the regress is cut by rule. Also confirm that the template may state that a test case is a new
  short file at a path that does not exist, under the 1 MiB limit.
- **Q-C (I-4): whether the audit's statuses cover every existing file of a kind.** Row 3 asks for
  it. Also decide whether files added later need a row.

## Re-review of the revision

Turn 2, same reviewer, read only. Inputs: the revised `spec.md` (read whole, 699 lines), rulings
C10–C17 in `design-rulings.md`, and "Revision after spec review" in `design.md`. Line numbers
below are those of the revised `spec.md`. Of the 16 earlier findings, 15 are addressed and 1 is
partly addressed. I found 3 new Important findings and 1 new Minor finding.

### Earlier findings

| Finding | Status | Where |
|---|---|---|
| I-1 test cases | **addressed** | Exemption: spec.md:307-311, :344-348, WAY-168 edit at :510-511 (C11). Shape and size limit: :241-248, :298-301 (C12). Fences: :302-306, :375-377. A new gap in the same area remains (N-1, N-2). |
| I-2 audit database | **addressed** | :211-213, :256-257, :444-445, :542, :672-673, :681-683 (C10) |
| I-3 *Part* and reach | **addressed** | :214-218, :684-685 |
| I-4 every file's status | **addressed** | :231-233, :427-430, :536 (WAY-200) (C13) |
| Minor 1 `guidelines-form` | **addressed** | :219-223, :353-358 (C14) |
| Minor 2 WAY-171 | **addressed** | :85, :292-293, :516-517, :694 |
| Minor 3 "Where guidelines go" | **addressed** | :85 |
| Minor 4 WAY-167 level | **partly** | The choice made at :506-508 drops the index from row 1's entry. See N-3. |
| Minor 5 suppression citation | **addressed** | :191-195, :269 |
| Minor 6 severity | **addressed** | :208-210, :441, :585 |
| Minor 7 fact per edition | **addressed** | :258-265, :540 |
| Minor 8 trial run | **addressed** | :399, :421-423, :451-453 |
| Minor 9 installer WAY-48 | **addressed** | :481-485, :662 |
| Minor 10 "kind" | **addressed** | :64 |
| Minor 11 "exemplar" | **addressed** | :67-71 |
| Minor 12 no runner before a gate | **addressed** (C16, said in the request) | :670-673 |

### New findings

#### N-1 (Important): one good/bad pair per rule cannot serve a rule whose invariants check different things (spec.md:196-200, :241-243, :292-297, :491-495, :623)

**What the spec requires.** A rule holds "exactly one" `good` block and "exactly one" `bad` block
(:293-294). The invariant's method must pass with the good file and fail with the bad one (:296).
Under §7 the check "is not accepted otherwise" (:494-495). The gate invariant reports this for
every invariant the rule names (:623).

**Where that breaks.** `### Linter` can name up to three invariants (:191-203):

- Invariant 1: no file breaks a blocking rule.
- Invariant 2: the configuration matches the adopting decision's list. This is C4's second
  invariant, written wherever the method reads the configuration.
- Invariant 3: the per-file comparison with `{fork-point}`.

The test cases §4.3 gives the linter are "a short new source file … breaking one blocking rule and
following it" (:241-243). Invariant 2 checks a configuration file, so it passes on that bad source
file. Its check then cannot be accepted under §7, and the gate invariant would report its evidence
as failing.

**A second form of the same gap.** The form check asks for blocks in a rule naming
`guidelines-form` together with another invariant (:345-348, crafted input :378-379). The one pair
cannot be a whole guidelines file for the first invariant (that is C11's regress) and a code file
for the second.

**This gap was there before the revision; I missed it in turn 1.** The task gives no way to choose:
row 11 says "zły musi go złamać, dobry musi przejść" for "tego niezmiennika", in the singular.

**Fix (needs a ruling, Q-D).** Either:

- (a) Each invariant the rule names gets its own pair, for example info strings
  `good <identifier> <path>` and `bad <identifier> <path>`. The exempt `guidelines-form` needs none.
- (b) The template requires one invariant per rule, and moves invariant 2 into a rule of its own.
  This touches the required rules of WAY-202's form and C4.

#### N-2 (Important): a good case cannot pass an invariant that stands on the list of violated invariants (spec.md:201-203, :296, :494-495)

**Where it happens.** WAY-205 (:201-203) and, for styleguides, WAY-190 put the full invariant on
the list of violated invariants while the old code still breaks it. In a scratch worktree of such a
product's commit, that invariant's method fails whatever good file is added. So "passes with the
good one" (:296) never holds. Under §7 (:494-495) the reviewer then cannot accept a new or reworded
listed invariant whose rule carries test cases. This is exactly the linter in a product such as
`loop2`.

**Why the spec cannot leave it.** WAY-51 makes a listed `fail` the expected state, but neither §5.1
nor §7 says how a test case is read for such an invariant. The gate invariant's "or that this could
not be checked" (:623) covers the gate, not the cycle sentence. This gap was also there before the
revision.

**Fix (needs a ruling, Q-E).** For an invariant on the list of violated invariants, the good case
counts as passing when it adds no failure the commit does not already have, and the bad case must
add one. The per-file companion invariant of WAY-205/WAY-190 carries the strict pass/fail. Or: the
cases of a listed invariant are recorded "could not be checked", and §7 accepts the check on the
deliberate break and on the companion invariant's cases.

#### N-3 (Important, small fix): row 1 is not written whole (spec.md:503-508)

**What row 1 says.** The general file carries the standing checks, the whole-product rules "i spis
plików rodzajów, każdy z warunkiem, kiedy go czytać". Row 1 is carried by the WAY-167 edit.

**What the revision does.** It answers Minor 4 by taking the table out of WAY-167: "The table of
kind files stands in WAY-212 alone".

**Why that conflicts.** WAY-134 says "The task's cycle writes each kept row whole into the
foundation", and `task-cycle/skill/SKILL.md:271` says "Write each row of *Settlements to record*
whole, as an entry of its kind". WAY-212 (row 15) carries the same table, so the meaning reaches
the foundation. But row 1's own entry is then written short of its row.

**Fix.** Take the other option of Minor 4. WAY-167's edited text keeps the general file's table of
kind files, each with when to read. WAY-167's *Verification* gains level 1
`guidelines-check-kind-index`, which then derives from WAY-167 as well as WAY-212.

#### N-4 (Minor): the form check cannot see a bare fence line inside a test case (spec.md:302-303, :346-347, :376)

A bare three-backtick line inside a case closes the block, as the form check's `fenced_lines` reads
fences. So such a line never stands "inside a test case" to be reported. The case's remaining text
then reads as prose.

**What the form check sees instead.** It finds a block whose content ends early, followed by stray
text and a later fence opening with no info string. A tilde or info-bearing line it can detect. The
spec should say what the form check reports there, for example a rule body holding a fence whose
opening line has no `good`/`bad` info string after a `good`/`bad` block, so that the crafted input
at :376 has a defined expected result.

### Verdicts after the revision

- **Task compliance: compliant except N-3**, where row 1 is written short of its row. The fix is
  one sentence and a *Verification* line. Nothing out of scope is brought in. C10–C17 fit the task.
  C11 and C13 now carry rows 3 and 11 as the human gave them.
- **Foundation coherence: coherent except N-1 and N-2.** Both concern how row 11's test cases meet
  the rules the template itself requires (several invariants per rule; listed invariants under
  WAY-51/WAY-205). Neither contradicts a decision, but each makes §7's acceptance condition
  impossible to meet in a case the spec itself sets up.
- **Plan: can be written once Q-D and Q-E are ruled.** The rulings change the text of the common
  template (§5.1), the form check's block rule (§5.2 item 5), §7's sentence, and possibly the gate
  invariant's wording. Everything else (files, tests, commands, ordering at :331-332) stands and can
  run.

Counts this turn: **Critical 0 · Important 3 (N-1, N-2, N-3) · Minor 1 (N-4)**. Earlier findings:
15 addressed, 1 partly (Minor 4, now N-3).

### Questions needing an orchestrator ruling

- **Q-D (N-1): what test cases does a rule naming several invariants give?** (a) a pair per
  invariant, with the identifier in the info string; or (b) one invariant per rule, with the linter
  configuration invariant moved into a rule of its own. Recommendation: (a), as it changes no
  required rule.
- **Q-E (N-2): how is a test case read for an invariant on the list of violated invariants?**
  Recommendation: the good case adds no failure the commit lacks and the bad case adds one, while
  the companion per-file invariant of WAY-205/WAY-190 carries the strict cases. The alternative is
  that such cases are recorded "could not be checked" and §7 accepts on the break alone.
- N-3 needs no ruling beyond taking the other option of C15/Minor 4. Name it if you want it recorded
  as a ruling.
