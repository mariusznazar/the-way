# Spec — coding guidelines as the second discipline of product guidelines

Task: [task-frozen.md](task-frozen.md) (frozen from the-brain `cf7eefd`; `Status: ready for cycle`,
independent, Human actions none). Base: `foundations` `235b0b4` (= the task's search commit).
Design report, with the brainstorming classification, the foundation selection, every question with
its evidence and the rejected ways: [reports/design.md](reports/design.md) (its section "Revision
after spec review" maps each finding of [reports/spec-review.md](reports/spec-review.md) to the
change below). Orchestrator rulings: [reports/design-rulings.md](reports/design-rulings.md), cited
here as C1–C17.

The task binds over this spec. Rows of *Settlements to record* are cited as "row N", the task's
questions as "Q N", its carried questions as "CQ N" (numbered 1–7 in the order the task lists them).
The meaning of every row is the human's and needs no new approval; how each becomes an entry, and
its wording, is the cycle's (WAY-134). Choices no row, answer or entry settles were ruled by the
orchestrator provisionally under the user's delegation (C1–C17), never as the human's approval, and
the request lists them. Wordings below are meanings to carry, not final text: the foundation author
writes each entry through the skill of its element, which shapes the words (WAY-35, WAY-114).

## 1. Intent

An agent that writes a product's code finds, from one line of the product's root `AGENTS.md`, one
source of how that product's code is written: a general file `guidelines/coding.md` with the
product's standing checks — a linter, a formatter, an audit of dependencies — and its whole-product
rules, and, for each kind of code that has an exemplar (an endpoint, a migration, a module), a file
`guidelines/coding-<kind>.md` naming that exemplar and the rules a script checks from it. Every
rule of those files names the product's decision that carries it and at least one invariant that
checks it, and its good and bad uses are test cases of that invariant. A skill of the-way,
`maintain-coding-guidelines`, leads the refinement of the task that writes or extends them; the form
check of guidelines checks their form.

The-way gains:

- a template of the coding discipline, `product-guidelines/coding/template.md`, with two file forms;
- the skill `maintain-coding-guidelines`, `product-guidelines/coding/SKILL.md`, its entry points and
  its entry in the installer's `SKILLS`;
- a change to the template every product's guidelines share: the file names of the coding
  discipline, and the good and bad use of a rule that names an invariant as test cases of that
  invariant, given as files;
- changes to the form check `product-guidelines/form_check.py` for the coding discipline and for
  the test cases;
- a sentence in the task cycle for the code reviewer to run the test cases until a gate does (C8);
- 20 new decisions (WAY-193..WAY-212), edits in place of WAY-167 and WAY-168, two glossary terms,
  one edited and four new invariants of the-way, and two failure modes at the part
  `product-guidelines` (C6).

Out of scope (task, binding): review of code against guidelines; the review that looks only for
what can be removed or merged; running the gate automatically before a merge, and with it the audit
of all dependencies by the clock; detecting in `refine-task` a task that creates the first code of
a kind with no exemplar, or the first code of a product with no coding guidelines. Nothing here
changes `refine-task`, as nothing changed it for the styleguide (the skill attaches at its step 3).

Success: the-way at the merge commit lets a product refine a coding-guidelines task with the skill,
take it through `implement-task`, and end with `guidelines/coding.md` (and a kind file where the
task settles an exemplar) that the form check passes, product decisions adopting or departing from
each standing check, invariants whose methods run the product's declared commands, and the pointer
in `AGENTS.md`. `loop2`'s coding guidelines come after the merge, in a product task.

## 2. Words (CQ4; open design choice, settled through `record-glossary-term`)

| Meaning | Word in entries | Entry | Why not the obvious word |
|---|---|---|---|
| a file a product's decision designates as the model later code of its kind is written after (row 24) | **exemplar** | glossary term (row 24) | "pattern" already means a path pattern (WAY-44, WAY-167) and a non-binding model (WAY-179); "reference" is the fingerprint reference of WAY-169 inside guidelines |
| the linter, the formatter and the audit of dependencies, as checks of the whole product's code (row 25) | **standing check** | glossary term (row 25) | "guard" is the last word of the term "format guard" and stands for it (WAY-94); a second meaning would break WAY-99 |
| endpoint, migration, module… | **kind of code**, plain words | none | "element" is a glossary term (a division of the foundation). "kind" is used in its plain sense here, as it is in WAY-176's binding text ("of the kind `background`, `text` or `other`") and in the styleguide's column `Kind`; WAY-99 renames a word only where one of its meanings is one a reader of the field would not give it, and neither use is |
| a report of a linter that leads to no change of code worth making, technically right or not (row 8, Q14, Google's "effective false positive") | plain words in WAY-203 and WAY-204 | none planned (C2) | if the glossary skill's WAY-95 test on the final sentences still requires an entry, the foundation author writes it as an entry that follows with no way open, and the request lists it as new |

The definitions are the glossary skill's (WAY-96). For "exemplar", the definition keeps what sets
the term apart from its plain English sense — that a decision of the product designates the file
for its kind — or the entry records why it still takes an entry under WAY-95; a definition reduced
to the plain sense would leave row 24's entry with no ground (WAY-95's violating case "a word takes
an entry for its plain meaning only"). For "standing check", the definition names the three checks
of the whole of a product's code; whether "required by the template" stays in it or in WAY-202 is
the skill's call under WAY-96. *Avoid* candidates the skill weighs: "reference implementation",
"reference file", "template module" (exemplar); "baseline check", "code guard" (standing check).
"pattern" cannot stand in *Avoid* (WAY-98: it has other uses).

## 3. Where it lives

### 3.1 In the-way

| Path | Change |
|---|---|
| `product-guidelines/coding/template.md` | new — the template of the coding discipline (§4) |
| `product-guidelines/coding/SKILL.md` | new — the skill `maintain-coding-guidelines` (§6) |
| `product-guidelines/template.md` | changed — "Where guidelines go" gains `guidelines/coding.md` and `guidelines/coding-<kind>.md` as WAY-167 now names them (WAY-171: the templates follow the decisions); *Good* and *Bad* "describe" a use; test cases of a rule naming an invariant, and the exemption of §5.1 (WAY-168) |
| `product-guidelines/form_check.py` | changed (§5.2) |
| `product-guidelines/test_form_check_invariants.py` | changed by the invariant-test author (§9) |
| `product-guidelines/test_form_check.py` | changed (§9) |
| `task-cycle/skill/SKILL.md` | one sentence in steps 10 and 11 (§7, C8) |
| `installation/install.py`, `installation/README.md`, `installation/test_install.py`, new `installation/test_coding_guidelines_installation.py` | `SKILLS` entry and its reflections (§6.6) |
| `.claude/skills/the-way-maintain-coding-guidelines/SKILL.md`, `.agents/skills/…` and every other entry point's sibling list | regenerated by `python -B agent-instructions/skill_entry_points.py --write` |
| `foundations/decisions.md`, `foundations/glossary.md`, `foundations/invariants.md`, `foundations/part_map.md` | §8 |

`product-guidelines/**` already belongs to the part `product-guidelines`; WAY-09's text ("for each
discipline of work whose guidelines the-way gives a template of, that template with the skill that
leads the work on them") already covers `product-guidelines/coding/`, so WAY-09 is not edited.

### 3.2 In a product

- `guidelines/coding.md` — one per product (rows 1, 18). `guidelines/coding-<kind>.md` — one per
  kind of code that has an exemplar, `<kind>` a lower-case identifier of words joined by hyphens,
  the one the decision designating its exemplar gives (row 1, Q8a).
- The configuration files of the three standing checks go, through `update-part-map` in the
  product's task, to the part of the product's map that holds its build configuration (CQ2, C5);
  the-way fixes no part, and the product's map decides.
- The product declares, for each invariant of a standing check, a command that runs the tool at
  its pinned version and writes the-way's record of a run (CQ7, §4.4).

## 4. The template of the coding discipline (`product-guidelines/coding/template.md`)

It opens like the styleguide template: what it binds (WAY-193), that each of its rules cites the
decision of the-way that sets it (WAY-171), and that the rules every file of guidelines keeps stand
in `product-guidelines/template.md`. It gives two required forms, each in a fenced block the form
check reads (CQ5).

### 4.1 Required form — the general file `guidelines/coding.md` (section `## Required form`)

```markdown
# Coding guidelines — <the product>

- **Discipline:** coding
- **Applies to:** <part> · …

## When to read

## Kinds of code

| Kind | File | When to read |
|---|---|---|

## Rules

### Linter
### Formatter
### Dependency audit
### <further rules of the whole product>

## Examples

### <example name>

## Where in code
```

### 4.2 Required form of a kind — `guidelines/coding-<kind>.md` (section `## Required form of a kind`)

```markdown
# Coding guidelines — <kind>

- **Discipline:** coding
- **Applies to:** <part> · …

## When to read

## Files of this kind

| File | Status | Decision |
|---|---|---|

## Rules

### <rule a script checks from the exemplar>

## Examples

### <example name>

## Where in code
```

Both forms: each `### ` under `## Rules` carries *Decision*, *Invariant*, *Good*, *Bad*, and its
*Invariant* names at least one invariant that checks it, by a script where a script can decide it
and otherwise by an agent whose method sets k of n, never by an agent judging whether new code
follows the exemplar (WAY-196). The sentence "its *Invariant* names at least one invariant" stands
in each form section, as the form check detects it there (§5.2). A rule neither a script nor such an
agent can check is an example (WAY-196).

### 4.3 What each section carries (rule or example, with the decision and invariant the skill proposes)

- *Applies to* — general file: every part of the product's map that holds code, scripts of its
  build included (WAY-208); kind file: the parts the kind's files lie in.
- `## When to read` — general file: before any change of the product's code (WAY-212); kind file:
  before adding or changing a file of that kind.
- `## Kinds of code` — a table, one row per kind file: *Kind* the identifier, *File*
  `guidelines/coding-<kind>.md` in backticks, *When to read* the condition, e.g. "before adding or
  changing an endpoint" (WAY-212). No row where the product has no exemplar yet; the table stays
  with its header.
- `### Linter` — rule. *Decision*: the product's decision adopting the linter and its rule set,
  naming the set, its edition, the parts and the rules of the set that stand among the examples
  for their false alarms (WAY-202, WAY-203, WAY-204, WAY-86). *Invariant*:
  1. by a script, no file of the parts named breaks a rule of the set that blocks, resting on the
     environment fact of the set's edition; the template proposes that an inline suppression of a
     blocking rule counts as a break, since a rule with no false alarm has no sound suppression and
     a fault is fixed in the file (WAY-203, WAY-193 — it binds a product only through its adopting
     decision; C3);
  2. the rules that block are exactly the adopting decision's list, and turning one off fails the
     gate until that decision changes (WAY-207, WAY-60; C4), in one of two ways the skill names in
     the task, by what the tool allows: where the method of invariant 1 passes the list itself, that
     invariant already holds it and no second invariant is written; where the method reads the
     product's configuration, a second invariant, by a script, keeps that configuration to the list;
  3. where the code already breaks the blocking rules, invariant 1 on the list of violated
     invariants and beside it the invariant that no file holds more reports of those rules than on
     `{fork-point}` and a file not on `{fork-point}` holds none (WAY-205).
- `### Formatter` — rule. *Decision*: the product's decision adopting the formatter and its
  configuration (WAY-202). *Invariant*: by a script, every file of the parts named is as the
  formatter leaves it. Entering a product whose code is not so formatted, the task reformats all of
  it once; no second invariant (WAY-205).
- `### Dependency audit` — rule. *Decision*: the product's decision adopting the audit, naming its
  tool and the advisory database it reads, and the severity from which a vulnerability counts — a
  choice the skill puts to the human with "every severity" open beside a threshold (WAY-202,
  WAY-206, WAY-60). *Invariant*: by a script, the change against `{fork-point}` brings in no version
  of a dependency with a known vulnerability of that severity, as that database gives it when the
  check runs (WAY-206).
- **The *Part* of each standing-check invariant** names the parts that hold code the check reads
  and the part that holds the build configuration and the lockfile, where the tools' configuration
  and the pinned versions stand (C5); the audit's *Part* names the parts holding every manifest and
  lockfile it reads. So a change touching only a configuration file or the lockfile reaches the
  invariant (WAY-62).
- **What the product's copy of `guidelines-form` carries**, stated in the template as the
  styleguide template states it for its table of roles: the table of kinds of code and its
  agreement with the kind files, the closed list of *Status*, the one exemplar and its decision
  naming path and kind, each *File* naming something git tracks, the test-case blocks and their
  paths (C14).
- A standing check the product goes without reads `none — <PREFIX-NN>@<fingerprint>`, naming the
  product's decision that departs from it with its reason (WAY-202, WAY-171).
- Further rules of the whole product — rule each, an invariant each (WAY-196).
- `## Files of this kind` — a table: *File* a path in backticks that git tracks; *Status* one of
  `exemplar`, `copy` or `do not copy`; *Decision* the product's decision designating the exemplar,
  with its fingerprint, on the `exemplar` row, and `—` on the others. Exactly one row is the
  exemplar, and its decision's binding sentences name, in backticks, that path and the kind
  (WAY-198, WAY-199). At the audit that writes or refreshes it, the table lists every existing file
  of the kind with its status (WAY-200; row 3); a file added after that audit needs no row until the
  guidelines are refreshed or extended, and the form check asks no completeness (C13).
- Rules of a kind file — what a script can check of the exemplar: where such a file lies, what it
  calls, how it validates its input; a rule and an invariant each (WAY-198).
- `## Examples` — the rest of the exemplar (WAY-198); rules of the linter's set kept for their false
  alarms, each naming the rule as the tool names it (WAY-203); nothing here binds (WAY-168).
- `## Where in code` — general file: the configuration files of the standing checks and the
  product's scripts of their invariants; kind file: the directories the kind lies in. No value is
  copied from them (WAY-171).
- **Test cases of the standing checks** (C12, C18; the shape §5.1 gives — a pair for each invariant
  the rule names): for `### Linter` invariant 1, a short new source file at a new path within the
  parts named, breaking one blocking rule and following it; for invariant 2 where it is written, the
  linter's configuration file at its path, once with one blocking rule of the decision's list turned
  off and once holding the list exactly; for invariant 3 where it is written, a short new source file
  holding one report of a blocking rule and one holding none (a file not on `{fork-point}` holds
  none); for `### Formatter`, a short new source file left unformatted and formatted; for
  `### Dependency audit`, a one-dependency manifest and lockfile at a new path within the parts the
  audit reads, naming a version with a known vulnerability, and one naming a version with none. The
  product's scripts are written so that a short file at a new path within the parts they read is a
  file they check: the linter and the formatter read every file of those parts, the audit every
  manifest and lockfile there. Where invariant 1 stands on the list of violated invariants, its pair
  is read against the commit's own result, and invariant 3's pair carries the strict reading (§5.1,
  C19).

### 4.4 Rules for the standing checks' tools (template text, each citing the decision it applies)

- **Pinned versions** (CQ6). Each standing check's tool stands at an exact version in the product's
  declared dependencies and lockfile, and each method runs that pinned version from the product's
  own environment, never one fetched at run time: a command is the same on every run (WAY-61). A
  new version of a linter that changes the edition of the adopted rule set is a change of the
  adopting decision and of its fact (WAY-86, WAY-172). The advisory database the audit reads is
  read as it stands when the check runs (WAY-206, C10).
- **One environment fact per edition of a rule set** (CQ6). The fact's sentence holds which rules
  the set holds at the edition the decision adopts, quoting the page of the tool's documentation of
  that version that lists them. It is one fact under WAY-76: one source edition, one thing — the
  set's membership — and one reason to change, a new edition; as WAY-76's complying case keeps git's
  path-pattern rule with its page's exceptions in one fact. A WCAG criterion stands as a fact of its
  own (WAY-191) because each is a requirement of its own in prose; a rule of a set is a requirement
  whose content the pinned tool executes, so what the invariant takes from the catalogue is the
  membership alone. The blocking invariant rests on that fact (WAY-73). No fact per rule.
- **The blocking rules stand in the adopting decision**, as the set taken whole minus the rules it
  keeps among the examples (WAY-60, WAY-204); invariant 1 or 2 of `### Linter` keeps them there
  (WAY-207, C4).
- **Inline suppressions** of a blocking rule count as breaks in invariant 1 (WAY-203, WAY-193; C3).
- **The record of a run** (CQ7). Each invariant's command is a script the product declares, which
  runs the tool and writes the-way's record of a run: a line per invariant it gives a verdict for,
  `pass` or `fail` from the tool's result, and a failure for no entry where the tool could not run
  (WAY-61, WAY-74), as the styleguide's scripts do (WAY-189). The-way adds no adapter: the gate
  that would read tools' own reports is outside this task, and WAY-38 lets a product's command
  stand where the-way has none.
- **No command of its own in the instructions** (WAY-16): the guidelines and `AGENTS.md` name the
  invariants, never a lint command to run beside the gate.

### 4.5 Writing the files (for the cycle's author)

Take every tool, rule set, exemplar, status and departure from the task's settlements and the
decisions the foundation step wrote, never from memory (WAY-172, WAY-211); point to configuration
and code, copy no value (WAY-171); write each test case as §5.1 gives it; run the form check. A
choice the task did not settle stops the cycle at a blocked draft request (WAY-172).

## 5. Common template and form check

### 5.1 Test cases in `product-guidelines/template.md` (row 11, CQ1, C1, C11, C12)

A rule of the common template, citing WAY-168:

- In a rule whose *Invariant* names an invariant, *Good* and *Bad* describe a use in one line, and
  the rule's body, after its four fields, holds, for each invariant the rule names other than
  `guidelines-form`, exactly one fenced code block whose info string is
  `good <identifier> <path>` and exactly one whose info string is `bad <identifier> <path>`,
  `<identifier>` that invariant's, each holding the whole text of the file at that path of the
  product (C18). A test case is that file, added at that path or in place of the file there, on the
  commit checked; the method of the invariant its info string names passes with the good one and
  fails with the bad one (WAY-168).
- For an invariant on the list of violated invariants, a case is read against the commit's own
  result: the good case adds no failure the commit does not already have, and the bad case adds
  one. The per-file companion invariant of WAY-205 or WAY-190, which holds from its first day,
  takes the strict reading: passes with the good case and fails with the bad (C19; WAY-51).
- In a rule that carries test cases, every fenced block of its body is a test case, so code that
  only illustrates stands under `## Examples`.
- A test case is a short file and may stand at a path that does not exist, so that it stays
  instructive (Q7: the author's bad use is meant to teach); `<path>` is relative to the root, with no
  `..`, drive, `\`, `:` or leading `/`. The file of guidelines that holds the cases stays under the
  form check's limit of 1048576 bytes, beyond which it is not read.
- The outer fence is three backticks, and the text of a test case holds no line that opens a fence
  (three backticks or three tildes after at most three spaces), since
  `instruction-files/check_instructions.py` toggles code on any such line once the product's
  `AGENTS.md` names the file. Paths and texts thus stay in fenced code, where that script reads no
  path or import. A bare three-backtick line inside a case closes the block there, as the form check
  reads fences, so the rest of the case reads as body text and the case's own closing line opens a
  block with no info string; the form check reports that block as a malformed test case (§5.2 item
  5, C21).
- **Exemption.** A rule whose *Invariant* is the product's copy of `guidelines-form` gives *Good*
  and *Bad* as descriptions with no test-case blocks: its test cases are the-way's own tests of the
  form check (the `guidelines-check-*` invariants with their good and bad fixtures), and a whole
  file of guidelines as a case would need cases of its own without end (C11). Today that is the
  styleguide's "Every background with its text".

This applies to every discipline, as row 11 changes WAY-168 for all guidelines (C1): a styleguide
rule naming an invariant other than `guidelines-form` gains its two blocks too.

### 5.2 `product-guidelines/form_check.py`

Reads (stdlib alone, WAY-38; trusts nothing it reads, WAY-48):

1. **Two forms per discipline.** `read_templates` reads, besides `## Required form`, an optional
   section `## Required form of a kind`; a discipline with it takes `<discipline>.md` in the first
   form and `<discipline>-<kind>.md` in the second, `<kind>` matching the identifier pattern.
   `check_parts` gains that case beside `per_part`: `coding-<kind>.md` names no part, and its name
   agrees with *Discipline* `coding`; `coding-.md`, `coding-Endpoint.md`, `coding--x.md` disagree.
   `requires_invariant` is detected in each form's section.
2. **Tables beyond the roles.** `read_templates` no longer demands the role columns of every table
   of a discipline: the role checks run on a table whose columns are those of the roles; every
   other table is checked for its header and its number of cells, and the two tables of the coding
   template for what §4.3 gives them. Their structural words (`Kinds of code`, `Files of this
   kind`, the columns, the closed list of *Status*) are read back from the template, which raises
   `TemplateError` where one is missing, as the styleguide's words are. This change lands with or
   before the coding template, which `read_templates` would otherwise refuse.
3. **The index of kinds** (new invariant `guidelines-check-kind-index`): every file
   `guidelines/coding-<kind>.md` git lists is named by a row of `## Kinds of code` of
   `guidelines/coding.md`, whose *File* is that path; every row names a `<kind>` whose file git
   lists; a kind file with no `guidelines/coding.md` is an error.
4. **The files of a kind** (new invariant `guidelines-check-exemplar`): in `## Files of this kind`,
   exactly one row `exemplar`; every *Status* on the closed list; every *File* passing the existing
   `refused()` test and naming something git tracks; the exemplar row's *Decision* naming a
   decision of the log whose binding sentences hold `` `<path>` `` and `` `<kind>` `` after their
   whitespace is collapsed (plain substring search); `—` on the other rows. The fingerprint of that
   reference is checked as every reference is (WAY-169). `Foundation` keeps each decision's binding
   text for this. No completeness of the table is asked (C13).
5. **The test cases** (new invariant `guidelines-check-example-files`): in every kept rule whose
   *Invariant* names an invariant other than `guidelines-form`, for each such invariant one
   `good <identifier> <path>` block and one `bad <identifier> <path>` block after the fields, each
   path passing `refused()` (C18); a block whose `<identifier>` the rule's *Invariant* does not
   name is an error. The info string is read only from an opening fence; a line inside a test case
   that would open a fence (a tilde fence, or backticks followed by text, which do not close the
   block) is an error. Every other fenced block of such a rule's body — one whose opening line has
   no info string of those two forms, as left by a bare three-backtick line that closed a case early
   (C21) — is an error reported at its opening line as a malformed test case, and a test case left
   open to the end of the file is an error at its opening line. A rule whose *Invariant* names only
   `guidelines-form` needs no blocks. No such path is opened, given to git
   or written; only the gate, later, or the reviewer, now, applies a test case, and never to the
   working tree (§7).
6. **Invariant in every coding rule** (edited `guidelines-check-carrier`): as for the styleguide,
   through `requires_invariant`.
7. Every finding of 1–6 is an error of `guidelines-form` in the product's record, as every other
   form finding is: its sentence's "rules, rule fields and tables … each with the values and the
   links those templates give it" covers them — a *File* that must exist is a link the template
   gives (Q15: "skrypt formy sprawdza, że te pliki istnieją") — so `guidelines-form/1` is not edited
   and its product copies stay word for word (C14); the coding template states which of its checks
   that copy carries (§4.3).

The docstring's list of what it reports gains these cases; `PROGRAM`, the command, its options and
exit codes stay (`guidelines-form-check-command`).

### 5.3 Crafted input (WAY-48; the file is a trust boundary)

The plan's tests cover, each read without leaving the repository, without git seeing a refused
path, without a socket and within a time bound:

- a *File*, an index *File* or a test-case path that is absolute, a UNC prefix, holds `..`, `\`,
  `:`, a drive, a character that is not printable, or a pathspec magic word; a path of 200 KiB;
- kind names `coding-.md`, `coding--a.md`, `coding-A.md`, `coding-a/b.md` (git lists it under a
  directory: warned and not read), `coding-a.md.md`, `Coding-a.md`, a name differing from an index
  row only by case or a Unicode look-alike;
- a table row with a `|` inside backticks, too few or too many cells, a separator row in the middle,
  a header that differs by one space, two `exemplar` rows, none;
- a fence left open to the end, a tilde fence, a fence of four backticks closing three, a line
  inside a test case that opens a fence, an info string `good` with no identifier or path,
  `good x  a.ts b.ts`, `GOOD x a.ts`, a `good` block naming an invariant the rule does not name, a
  rule naming two invariants with a pair for one only, a 1 MiB info string, an info string on a
  closing fence; expected reports (C21): a bare three-backtick line inside a `good` case reports a
  malformed test case at the line of the case's former closing fence, now an opening fence with no
  info string (the shortened `good` block itself still counts as that invariant's good case); a
  tilde or a backticks-with-text line inside a case reports a fence-opening line inside a test case
  at that line; a case left open reports at its opening line;
- a rule naming `guidelines-form` with and without blocks, a rule naming `guidelines-form` and
  another invariant;
- a decision whose binding text holds the path only outside backticks, or `` `src/a.ts` `` where the
  row says `src/a.tsx` (substring traps), a decision number of another log's prefix, a repealed
  decision;
- a line of one MiB of `|` or of backticks (the existing bound on matching applies to the new
  regular expressions: anchored, no nested repetition); a file just over 1048576 bytes of test
  cases, refused unread.

## 6. The skill `maintain-coding-guidelines` (`product-guidelines/coding/SKILL.md`)

### 6.1 Frontmatter and place

`name: maintain-coding-guidelines`; description, starting "Use when": a product's code needs coding
guidelines written before its first code, its existing code audited for them, an exemplar settled
for a kind of code, or its coding guidelines refreshed or extended — leading those matters of a
coding-guidelines task's refinement with the human. Like `maintain-styleguide`: it says where the-way
lies (the checkout in the-way, `.the-way` in a product), names skills with the `the-way-` prefix,
uses no Superpowers method (WAY-125), holds the order of the work only and restates no rule
(WAY-35 by analogy), and takes over from `refine-task` at its step 3 and hands back at its step 4.
It writes the task document and research reports under `.runs/coding/`; never the foundation, the
guidelines or the product's code, and it leaves every file git tracks as it was.

### 6.2 Steps

0. **Read** both templates of guidelines, `refine-task` and the task template, "How a skill asks"
   and "Critique before collective review", the critique skill; the product's root `AGENTS.md` and
   `guidelines/`; its foundation by "Reading the foundation" (WAY-150), including the decisions of
   its technology and every decision already adopting a tool, a rule set or an exemplar.
1. **Recognize** (WAY-210): the parts that hold code (WAY-208); what the product has — a linter, a
   formatter, an audit, kinds of code with several files, or nothing — read off its files; whether
   coding guidelines exist. That gives the mode: no code (step 2); code and no guidelines (steps 2
   and 3); a task creating the first code of a kind (step 3, "a new kind"); existing guidelines,
   refresh or extension (step 2, and step 3, which audits each kind again). A new tool is a question
   of the task, never settled by the skill (WAY-210).
2. **Starting set** (WAY-211, WAY-210): ask the human's preferences for the standing checks in the
   product's technology as one question of assessment; where none, and at every refresh or
   extension, research each standing check for that technology in a report of its own under
   `.runs/coding/<question>.md`, each source a page with its version, among them which tool is most
   used in that technology (the default recommendation, WAY-210); one fresh critic refutes every
   claim no source supports before anything reaches the human; no critic, no research. For a
   product with no code, the rules the tool's documentation marks as recommended (WAY-204).
3. **Audit and trial** (where code exists):
   - *Trial run* (WAY-204): run the rule set on the product's code in a scratch worktree or a
     temporary environment, never installing the tool into the product's tracked files, its
     output into `.runs/coding/`; one fresh agent that wrote none of that code judges each report by
     whether it leads to a change of code worth making; a rule with one false alarm goes among the
     examples; the split goes to step 4 with its evidence. Where the code breaks the blocking rules,
     the pair of invariants of WAY-205; where it is not formatted, the one reformatting (WAY-205).
   - *Kinds* (WAY-200, WAY-201): for each kind with several files, judge every existing file of the
     kind, compare them and propose the exemplar, with one sentence of what the product gains, the
     files `do not copy`, each with the file and line of the place that breaks a rule, and `copy` for
     the rest (C13). A kind with no file yet: the task creating its first file designates it ("a new
     kind").
   - A choice read off the code is a proposal until the human settles it; an existing choice the
     human keeps becomes a decision whose rationale is the human's words or `unknown` (WAY-29).
4. **Settle with the human** (WAY-194): every choice, a recommended one included, shown by its
   effect on the product in plain words — "a change that adds a library with a known security hole
   does not get in", "every new endpoint checks its input as the exemplar does" — never by a rule's
   name or a configuration value; decisions, never single rules: a rule set is adopted whole, with
   the split shown as "N rules will block; these M flagged sound code here and become examples";
   after a choice entering a binding part, the one question "How a skill asks" gives. It settles:
   each standing check adopted or departed from with the reason (WAY-202), the tool, set, edition,
   parts, the audit's database and severity ("every severity" among the ways), the exemplar and
   statuses per kind, the script-checkable rules of each exemplar, each invariant of §4.3 and its
   kind (script or agent k of n), and which way of `### Linter` invariant 2 applies. It names to the
   human, as the weak point of the audit, that a vulnerability published after a change was checked
   can fail a later run of the same commit (WAY-206). Then the critique of the complete set
   (WAY-120). Write each answer before the next question.
5. **Hand back** to `refine-task` step 4; its step 5 builds *Settlements to record*.

### 6.3 Orchestrated mode

As `maintain-styleguide`'s: questions go into the conversation turn; research agents, critics and
the fresh agent that judges the trial run's reports are requested from the project orchestrator,
their reports under `.runs/coding/`; the skill starts no child agent.

### 6.4 What reaches the task document

*To do*: write `guidelines/coding.md` (and `coding-<kind>.md` per settled exemplar) from
`.the-way/product-guidelines/coding/template.md`; install and configure each adopted tool at its
pinned version; reformat once where settled; write each invariant's script (by agents other than
the code's, WAY-69), able to read a test case at a new path (§4.3); apply `maintain-instruction-files`
for the pointer of WAY-212; assign the tools' configuration files, through `update-part-map`, to the
part holding the build configuration (C5); for the product's first guidelines, `guidelines/**` to the
agent-directing part and the copies of the two invariants of guidelines (WAY-167, WAY-170); each
item the audit calls for. *Questions to settle*, *Context* (trial-run evidence, the audit's charges
and deferred ones, research sources) and *Settlements to record* as the styleguide skill gives them.

### 6.5 CQ3 — a product with the-way already installed

No new mechanism: a product receives the skill in the task that moves its pin, which deletes the
installed wrappers and runs the installer at the new commit (`installation/README.md`); the block
of `AGENTS.md` changes because `product_guidance()` lists every name of `SKILLS`, so that task
removes the block first, as the README says. The request carries the line on what moving the pin
changes (promise level `pinned`).

### 6.6 Installer

`SKILLS` gains `"maintain-coding-guidelines": "product-guidelines/coding/SKILL.md"`;
`installation/test_install.py` `NAMES` and `installation/README.md` (table and test list) gain it by
hand; a new ordinary test, on the pattern of `test_styleguide_installation.py`, installs a product
and checks both wrappers and the block naming `the-way-maintain-coding-guidelines`. The
`installation-command` surface keeps its wording. `installation/install.py` is a trust boundary
(WAY-48): the change adds one entry and no parsing, and the plan's check of crafted input for it is
that the existing refusals (a conflicting wrapper at the new skill's path in either directory, a
directory or a non-UTF-8 file there) still stop the run before anything is written, now for the new
wrapper too.

## 7. The test cases in the cycle until a gate runs them (rows 11–13, Q12, C8)

`task-cycle/skill/SKILL.md`, where the code reviewer writes a deliberate break (step 10, and step
11 for return-step checks), gains one sentence: for an invariant a rule of the product's guidelines
names with test cases, whose sentence the change adds or alters or one of whose test cases it
rewrites, the reviewer also runs the check, in a scratch worktree of the commit, once with that
invariant's good file and once with its bad file in place (the pair whose info string names it,
C18), records that it passes and fails there — for an invariant on the list of violated invariants,
that the good file adds no failure the commit lacks and the bad file adds one, the per-file
companion invariant taking the strict reading (C19) — and the check is not accepted otherwise; the bad file is a case beside the deliberate break, never the break
(WAY-168, WAY-197, WAY-69). A test case is applied only inside that scratch worktree, never in the
working tree. This is the whole change to the cycle; review of code against guidelines stays out of
scope (Q5).

## 8. Foundation entries (meanings; numbers in order from WAY-193)

### 8.1 Edits in place before `main` (`agent-instructions/README.md`; WAY-07: shown for renewed acceptance)

- **WAY-167** (row 1) — its file names gain the coding discipline: `guidelines/coding.md` for the
  standing checks and the rules of the whole product, and `guidelines/coding-<kind>.md` for each
  kind of code that has an exemplar, holding that exemplar and its rules, `<kind>` the identifier
  the decision designating it gives; and the general file holds a table of the kind files, each with
  when to read it (row 1 written whole, C20). *Verification* gains level 1
  `guidelines-check-kind-index`, which derives from WAY-167 as well as WAY-212; WAY-212 keeps the
  pointer and the "when to read" of each row. Level 2 gains complying and violating cases.
  No fingerprinted dependent (checked: none carries `@681d47ff`).
- **WAY-168** (row 11) — gains: in a rule that names an invariant other than one checking the
  guidelines' own form, the use that follows and the use that breaks it each give, for each
  invariant the rule names, the text of a file at a path of the product, and are cases on which that
  invariant's method passes and fails (C18), read for an invariant on the list of violated
  invariants against the commit's own result (C19); they are
  checked only when a change adds or alters the invariant's sentence or rewrites either use, never
  on every run of the gate. Three binding sentences at most (WAY-05). *Verification* level 1 gains
  `guidelines-check-example-files` and `gate-guidelines-example-evidence`. Dependents carrying
  `@47d9d53e`, each read against the new binding part and renewed (WAY-31): WAY-171 (derives from —
  stays true: the blocks stand in a rule's body, which its four fields do not exclude), WAY-173
  (derives from), WAY-188 (narrows — its sentence on WAY-168 stays true), `guidelines-check-carrier`
  (*Derives from*).
- WAY-114 is not edited: WAY-194 narrows it (row 14), as WAY-174 does.

### 8.2 New decisions

Scope `product-guidelines` unless noted; *Approved by* the merge of the request; *Based on* `none`
except WAY-195; *Origin* `none`. *Review when* as ruled (C7).

| No. | Row | Question (proposed) and meaning | Relations | Verification | Review when |
|---|---|---|---|---|---|
| WAY-193 | 16 | Does what the-way's template of coding guidelines carries bind a product directly? — binds only through a product decision adopting it; a decision of the-way on template or skill binds them, never a product's code | derives from WAY-168, WAY-100 | level 2 | none |
| WAY-194 | 14 | How does the coding-guidelines skill ask the human? — every choice, a recommended one included, by its effect in plain words, never rule names or configuration values; decisions, not single rules; prevails over WAY-114 in that area | derives from WAY-113 · narrows WAY-114; Scope + decisions | level 2 | none |
| WAY-195 | 17 | What do coding guidelines take from Open Mercato and from Google's static analysis lessons, and what do they leave? — §8.3 | derives from WAY-100 | level 2 | none |
| WAY-196 | 10 | What checks a binding rule of coding guidelines? — at least one invariant, script or agent with k of n, never a judge of following the exemplar; uncheckable → example; prevails over WAY-168 in the coding discipline | narrows WAY-168 · derives from WAY-08; Scope + invariants | level 1: `guidelines-check-carrier` | none |
| WAY-197 | 12 | Who writes the use that breaks a rule, and does it replace the deliberate break? — the guidelines' author; an extra case the check fails on beside the reviewer's break, which stays (WAY-69 unchanged); until a gate reports the cases, the reviewer who writes the break runs both | derives from WAY-168, WAY-69; Scope + invariants, task-cycle | level 2 (and level 3 as WAY-69 for who wrote what) | a gate of the-way reports the cases WAY-168 names · check by: 2027-03-31 |
| WAY-198 | 2 | How does a product's exemplar bind? — a product decision designates it by path for a kind; what a script can check of it are rules with invariants; the rest is example | derives from WAY-22, WAY-193 | level 1: `guidelines-check-exemplar` | none |
| WAY-199 | 4 | What change of an exemplar takes approval? — another file, or a changed checked rule, is a decision change; an edit keeping those rules is none; status beside each path in the kind file | derives from WAY-172, WAY-198 | level 1: `guidelines-check-exemplar` | none |
| WAY-200 | 3 | Who designates an exemplar, and when? — the task creating the first file of the kind; where several exist, the skill's audit judges every existing file and proposes the exemplar from their comparison, with the status `copy` or `do not copy` of each; the human approves | derives from WAY-198 | level 2 | none |
| WAY-201 | 22 | How does the skill's audit of a product with code end? — a proposed exemplar per kind with one sentence of gain, and `do not copy` files with file and line of the place breaking a rule | derives from WAY-200 | level 2 | none |
| WAY-202 | 5 | Which standing checks does the template require, and from when do they bind? — linter, formatter, dependency audit, named in the binding sentence (WAY-139's rejected "list in a template alone"); departure only by a decision with reason; bind from the task writing the coding guidelines, which ends with an adopting or departing decision for each | derives from WAY-193 | level 1: `guidelines-check-form` (the required rules) | none |
| WAY-203 | 7 | Which rules of a linter block a change? — only rules that give no report leading to no change of code worth making, technically right or not; such a rule is no rule, may stand among the examples, and the gate does not run it | derives from WAY-202 | level 2 | none |
| WAY-204 | 8 | How is the split of a rule set into blocking rules and examples found? — trial run judged by an agent that did not write the code, each report weighed by whether it leads to a change of code worth making; no-code product takes the recommended rules, blocking without evidence (weak point in rationale); a later such report moves the rule to examples by a decision change the human approves. Its rationale says what the fact of an edition holds and why it is one fact (§4.4) | derives from WAY-203 | level 2 | the first product without code that adopted recommended rules meets a report leading to no change worth making, or merges ten changes without one · check by: 2027-03-31 |
| WAY-205 | 9 | How do standing checks enter code that already breaks them? — linter: full invariant on the violated list plus the fork-point invariant per file; formatter: one reformatting in the task that brings it, no second invariant | derives from WAY-51, WAY-60; Scope + invariants | level 2 | none |
| WAY-206 | 6 | What does the audit of dependencies check? — the change, failing only on vulnerabilities it brings in against `{fork-point}`, read from the named advisory database as it stands when the check runs, from the severity the product's decision sets; no audit of the whole tree by the clock. Rationale names two weak points: Q13's (a vulnerability found in a dependency the product already holds gives no signal until a change touches it), and that a later run on the same commit may fail where an earlier one passed when an advisory is published for a version that commit brings in, a flip WAY-68 answers unchanged (C10) | derives from WAY-202, WAY-60; Scope + invariants | level 2 | a gate or clock of the-way runs a product's checks apart from a change · check by: 2027-03-31 |
| WAY-207 | 23 | Where is a fault of one file fixed? — in that file, never by turning a linter rule off for the whole product nor by changing the exemplar; turning a rule off for the product is a change of the adopting decision the human approves | derives from WAY-172, WAY-193 | level 2 | none |
| WAY-208 | 18 | Which parts of a product get coding guidelines? — every part that holds code; the general file names them in *Applies to* | derives from WAY-193 | level 2 | none |
| WAY-209 | 19 | When do a product's coding guidelines come into being? — in a product with no code, the general file with its standing checks before the first task that writes code; a kind file with the task creating the first file of that kind | derives from WAY-193 | level 2 | the first product whose coding guidelines were written before its first code has merged that code · check by: 2027-03-31 |
| WAY-210 | 20 | What does the coding-guidelines skill look at first? — what the product has; extend, never a second tool beside it; a new tool is the human's question, with the default recommendation of the most used tool in the technology, from research with sources | derives from WAY-193 | level 2 | none |
| WAY-211 | 21 | Where do the tools and rule sets come from? — the human's preferences, else research with page and version and critique before the human, again at refresh or extension | derives from WAY-122, WAY-120 | level 2 | none |
| WAY-212 | 15 | How does a product's instruction file lead to its coding guidelines? — one line in root `AGENTS.md`, outside the installer's block, to `guidelines/coding.md` with "before you change code"; the kind files through the general file's table, each with when to read; no line per kind file | derives from WAY-128, WAY-129; Scope + instruction-files | level 1: `guidelines-check-kind-index` (the table); level 2 for the pointer | none |

Notes:

- The rationale of each decision is the cycle's to write (WAY-29's last sentence), from the task's
  answers and sources: e.g. WAY-203 carries K1 ("Trzyma się" — a rule that once flagged sound code
  goes to the examples, and in its area the agent is free again; the 10% review threshold rejected);
  WAY-199 carries K3; WAY-210 carries K2. The rejected options are the task's.
- WAY-203 and WAY-204 carry the meaning of a false alarm in plain words (C2); no glossary entry is
  planned for it (§2).
- WAY-197 and WAY-206 hold a clause bounded by a gate that does not exist yet, as WAY-170 does,
  with a *Review when*; WAY-36 lets it stand because it binds after the merge until that gate
  arrives.
- Each decision's *Verification* level 1 identifier must stand in that invariant's *Derives from*
  (`verification-invariant-derivation`).

### 8.3 WAY-195 — what is taken and what is left (row 17, Q16 B, Q18)

*Based on*: observation of the public repository `open-mercato/open-mercato` at commit
`4374c48def1654927805c4b760f0e7f8648280f2` and of the paper Sadowski, Aftandilian, Eagle,
Miller-Cushon, Jaspan, "Lessons from Building Static Analysis Tools at Google", CACM 61(4), April
2018, as read from a public copy; each quotation re-read by the cycle's author from the public source,
with its path and line or page, never copied from the task's private research (WAY-27, WAY-90). If
the author cannot reach a source, it stops and asks through the orchestrator.

- Taken from Open Mercato: the exemplar declared with a table of files to copy from (the module
  `customers`: "MUST use this module as the template for new CRUD modules — copy file structure and
  patterns", "Key Reference Files — Copy From Here", "Ask before changing this module's reference
  patterns") → WAY-198, WAY-199; the status of a file after an audit (`readStatus` `readable` /
  `qa-only`) → WAY-199, WAY-200; the audit of dependencies against a base (`--baseline <base
  yarn.lock>`) → WAY-206; the table of work → files to read ("A single task often maps to
  **multiple rows** … Read **all** matching guides first") → WAY-212.
- Left from Open Mercato (named, what the cycle would otherwise guess): its review checklist and
  review engine (review against guidelines is another task's); its lessons catalogue (a register of
  rules beside the foundation, WAY-04); the byte budget of `AGENTS.md` with its ratchet (instruction
  files answer to WAY-128); fact sheets generated from the code; the advisory, warning-only lint job
  (the gate knows no warning, WAY-63); the daily audit of the whole tree by the clock (no method of
  this check, WAY-206); its fixed audit threshold `--severity high` (the severity is the product's
  choice, "every severity" among the ways, WAY-206); agents' hooks; the evaluation harness of
  instructions.
- Taken from Google: a check blocks only at **zero** effective false positives → WAY-203; the
  effective false positive as a report a developer does not act on → WAY-204.
- Left from Google (Q18): "correctness, not style" — coding guidelines block on style too, because
  a style remark in review never blocks (WAY-161) and the human does not judge style; "fixed across
  the code base before it is turned on" — replaced by the pair of invariants of WAY-205.

### 8.4 Rulings applied

| Ruling | What it settles | Where |
|---|---|---|
| C1 | test cases as whole files in `good`/`bad` blocks, every discipline, enforced by the form check; a case may be a short new file | §5.1, §5.2 item 5 |
| C2 | no planned third glossary term; the meaning in plain words | §2, §8.2 notes |
| C3 | inline suppressions counted as breaks, as template text citing WAY-203 and WAY-193, binding by adoption | §4.3, §4.4 |
| C4 | both ways of keeping the blocking list, the skill naming which | §4.3 `### Linter` 2, §6.2 step 4 |
| C5 | the tools' configuration to the product's build-configuration part, the-way fixing no part | §3.2, §6.4 |
| C6 | two failure modes at `product-guidelines` | §8.6 |
| C7 | *Review when* as in §8.2 | §8.2 |
| C8 | the task-cycle sentence | §7 |
| C9 | the kind file's table | §4.2, §4.3, §5.2 item 4 |
| C10 | the audit reads the live database; the flip named; WAY-68 unchanged | §4.3, §4.4, §6.2 step 4, §8.2 WAY-206, §10 |
| C11 | rules whose invariant is `guidelines-form` exempt from blocks | §5.1, §5.2 item 5, §8.1 WAY-168 |
| C12 | shape of cases, size limit, fences | §4.3, §5.1, §5.3 |
| C13 | every existing file judged at the audit; later files need no row | §4.3, §5.2 item 4, §6.2 step 3, WAY-200 |
| C14 | `guidelines-form/1` not edited; the template states what its copy carries | §4.3, §5.2 item 7 |
| C15 | Minors 2–11 | design report, "Revision after spec review" |
| C16 | nothing runs product invariants before a gate: said in the request | §9 |
| C18 | a good/bad pair per named invariant other than `guidelines-form`, `good <identifier> <path>` | §4.3, §5.1, §5.2 item 5, §5.3, §7, §8.1 WAY-168, §8.5 |
| C19 | cases of a listed invariant read against the commit's own result; the per-file companion strict | §4.3, §5.1, §7, §8.1 WAY-168, §8.5 |
| C20 | WAY-167 keeps the table of kind files; level 1 `guidelines-check-kind-index`, also deriving from WAY-167 | §8.1 WAY-167, §8.5 |
| C21 | the bare-fence result and the crafted input's expected report | §5.1, §5.2 item 5, §5.3 |

### 8.5 Invariants of the-way

| Identifier | Change | Meaning | Derives from | Part | Method |
|---|---|---|---|---|---|
| `guidelines-check-carrier/1` | edited in place, version kept (pre-`main` precedent: `guidelines-form` was edited at /1 in `19d28f8`) | "every such rule of a styleguide" becomes "every such rule of a discipline whose template requires an invariant in every rule" (the styleguide and coding today) | + WAY-196 (renewed WAY-168) | unchanged | unchanged |
| `guidelines-check-kind-index/1` | new | §5.2 item 3 | WAY-167, WAY-212 | as the other `guidelines-check-*` | `python -B gate/run_tests.py product-guidelines --record .runs/product-guidelines-tests.jsonl` |
| `guidelines-check-exemplar/1` | new | §5.2 item 4 | WAY-198, WAY-199 | same | same |
| `guidelines-check-example-files/1` | new | §5.2 item 5: a pair per named invariant, the exemption, the fence rule and the malformed test case included | WAY-168 | same | same |
| `gate-guidelines-example-evidence/1` | new (row 13) | For every invariant a rule of a file `guidelines/<name>.md` names with test cases, whose sentence a change adds or alters against "{fork-point}", or one of whose test cases the change alters, the gate's report states whether the entry's method passes with the good file and fails with the bad file whose info strings name it — for an entry on the list of violated invariants, whether the good file adds no failure the commit lacks and the bad file adds one — or that this could not be checked | WAY-168 | gate · product-guidelines | `TODO` until a gate can (Q12) |

Unchanged on purpose: `guidelines-form/1` (products copy it word for word; its sentence covers the
new findings — §5.2 item 7, C14), `guidelines-check-form/1` (its generic sentence — required parts
of the discipline's template, name agreeing with *Discipline* — covers the two forms and the required
standing-check rules; its tests gain coding cases citing /1, and *Derives from* gains WAY-202),
`guidelines-reference-current/1`, `invariant-test-break/1`, `gate-fork-point-evidence/1` (row 12,
Q7, Q12). The product-side invariants of §4.3 are written in products, not here.

### 8.6 Part map (C6)

`product-guidelines` keeps its responsibility, files and trust boundary. Two failure modes, through
`update-part-map`: "the form check passes a kind file whose exemplar no decision designates — agents
copy a file nobody approved — high — detected by guidelines-check-exemplar"; "the skill proposes as
blocking a linter rule that gives false alarms — the gate blocks sound code, and only a change of
decision lifts it — high — not detected".

### 8.7 Environment facts

None in the-way. A product writes the fact of its adopted rule set's edition (§4.4).

## 9. Verification a plan can run

- Three different agents for each new or changed invariant's sentence (foundation author), its check
  (invariant-test author) and the form check's code (code author); the code reviewer writes each
  deliberate break from the sentence (WAY-69).
- Invariant tests (`test_form_check_invariants.py`, invariant-test author; a change to invariant
  tests assessed under WAY-10): coding files valid in both forms pass; a coding rule naming no
  invariant (carrier); a missing standing-check rule and a dropped one (`guidelines-check-form/1`);
  name cases of §5.2 item 1 (`guidelines-check-form/1`); index both ways and a kind file with no
  general file (kind-index); the exemplar table cases and the decision not naming path or kind
  (exemplar); a rule naming an invariant without a good or bad block, a rule naming two invariants
  with a pair for one only, a block naming an invariant the rule does not name, a refused path, a
  fence line inside a case, a bare fence closing a case early (malformed test case), and a rule
  naming `guidelines-form` passing without blocks (example files); the
  existing valid styleguide fixture gains its blocks for every rule naming an invariant other than
  `guidelines-form`.
- Ordinary tests (`test_form_check.py`): its fixtures using `guidelines/coding.md` as a discipline
  with no template (`:142-145`, `:264-277`) move to another discipline name (e.g. `observability`);
  the crafted inputs of §5.3; no new path reaches git or is opened; record and report lines for the
  new findings.
- Installer: the new installation test and the refusals of §6.6 (WAY-48).
- `python -B gate/run_tests.py product-guidelines`, `installation`, `agent-instructions`,
  `task-cycle`, `gate` (critical flows, WAY-45); `skill_entry_points.py --write` then
  `skill-entry-points` through the gate tests; the element format guards on the changed foundation
  files with `--base none` and `--merge-onto none` (the form check's own record holds `unchecked`
  for `--merge-onto none`).
- Not checkable here: the new gate invariant (method `TODO`); the product invariants of §4.3 (no
  product in this repository); Python 3.14 behaviour (the harness has 3.13.16, cycle choice O3).
- The request says, besides the rulings: nothing runs a product's standing-check invariants before a
  gate exists, other than a cycle running the methods of the invariants a change reaches — running
  the gate automatically is out of scope (Q1, C16); and the weak point of the audit named in WAY-206
  (C10), for Mariusz, who may prefer narrowing WAY-68 at the request.

## 10. Readings and contradictions checked

- WAY-61 "a check fed input made up for it is the method of a sentence about that check": the test
  cases are such input, so they are evidence about the check reported by the gate (row 13), never a
  method of the product's invariant, and never results (the invariants template's open line on
  runs on a deliberate break).
- WAY-61 "a command is the same on every run" and WAY-68: the tools are pinned; the audit's
  database is not, by the human's choice of a live audit of the change (Q3, Q13); a flip on one
  commit is answered as WAY-68 gives it, and no decision is narrowed (C10).
- WAY-62: each standing-check invariant names the part holding the configuration and the lockfile,
  so a change to either alone reaches it (§4.3).
- WAY-63 has no warning result: a rule with false alarms is no rule (WAY-203), never a warning.
- WAY-60: every condition of a product invariant of §4.3 stands in its sentence or in a decision
  that places it (blocking list, severity, database, edition).
- WAY-16: no lint command in instructions; the invariants' methods are the product's declared
  commands, run by the gate.
- WAY-04: the exemplar binds through a decision and invariants, never as a copy of code turned law;
  the audit's statuses are approved by the human (WAY-200).
- WAY-139: the three standing checks stand in WAY-202's binding sentence, not in the template alone.
- WAY-171: unchanged; the test-case blocks stand in a rule's body after its four fields (§5.1).
- WAY-192 is not narrowed: it governs styleguides; WAY-212 governs coding guidelines.
- WAY-172: designating another exemplar or changing a checked rule is a change of a decision; an
  edit of the exemplar keeping its rules is a value kept with its meaning (WAY-199).
- WAY-69 and `invariant-test-break` unchanged: the author's bad file never replaces the reviewer's
  break (WAY-197).
