# Spec — product guidelines, with the styleguide as the first guidelines

Task: [task.md](task.md) (frozen; `Status: ready for cycle`, independent, Human actions none).
Base: `foundations` `96623ed7710100fe6e11a0ce3c052fc44d4af52d`. Design report:
[reports/design.md](reports/design.md) (its "Revision after spec review" maps each finding of
[reports/spec-review.md](reports/spec-review.md) to the change below). Foundation selection:
[reports/foundation-selection.md](reports/foundation-selection.md).

The task binds over this spec. Rows of *Settlements to record* are cited as "row N"; their meanings
are the human's and need no new approval, their wording into entries is the cycle's. Choices this
spec makes that no row or entry settles are marked **autonomous** with their price in
`reports/design.md`; answers the root orchestrator gave provisionally under the user's delegation
are marked **root C5–C10** (recorded in `cycle.md`); the root's rulings on the spec review (recorded as C11–C22) are marked **root, finding N**, by the finding of `reports/spec-review.md` they answer.

## 1. Intent

An agent that writes or changes a product's user interface gets one source of meanings for
colours, components and states — the product's styleguide — found from the product's
instructions, whose every binding rule points to the decision and invariant that carry it and is
kept current by a script. The-way gains:

- the notion of **guidelines** (row 1, row 25): hand-written product documents outside the
  foundation, one per discipline of work on the product (the styleguide first; later, for example,
  coding standards, testing, observability), lying in the product's part that directs agents' work;
- a template every guidelines document shares, and a template of the styleguide;
- a skill, `maintain-styleguide`, that leads the styleguide matters of a styleguide task's
  refinement with the human, in three modes — before the first screen, audit of a product with
  screens, refresh or extension;
- a form check: a script checking the form of a product's guidelines and the currency of every
  reference they carry (rows 3, 4);
- the decisions, glossary term, part-map part and invariants of the-way that carry all of this.

"User interface" means what a user of the product sees and operates on screens — an application's
screens, or an admin panel added to a backend. Every new binding sentence and the skill's
description say "user interface" (or "screens"), never bare "interface", which WAY-165 uses for any
way a user operates a product, an API and a terminal included (root, finding 5). No glossary entry is
needed: the field gives "user interface" this meaning.

Success: a product with the-way pinned at the merge commit can refine a styleguide task with the
skill, take it through `implement-task`, and end with a styleguide file the form check passes,
product decisions and invariants carrying its rules, and a pointer from its instructions. The
`loop2` styleguide and the retention check of m2l5 row 17 come after the merge, in a product task
(task, question 1); they are not a condition of this merge.

Out of scope (task): the task cycle for view changes and the blocking rule, `loop2`'s styleguide,
observability guidelines and code quality. Nothing here changes `implement-task` or `refine-task`
(root C5).

**Cost the request shows (root, closing ruling).** Under root C5 the skill leads a refinement and the cycle
writes the file, so every styleguide change, however small — one new role, one renamed path —
goes through a refinement and a full cycle. This is a provisional reading of *To do* 7 ("Skill the
way tworzy i utrzymuje styleguide"); the request names it as such.

## 2. Where it lives

### 2.1 In the-way

A new part `product-guidelines` (root C6) with directory `product-guidelines/`:

| Path | What it is |
|---|---|
| `product-guidelines/template.md` | the form every guidelines document of a product shares (§3) |
| `product-guidelines/styleguide/template.md` | what the styleguide adds to that form (§4), and what each section carries, written for the cycle's author who writes the file |
| `product-guidelines/styleguide/SKILL.md` | the skill `maintain-styleguide` (§6) |
| `product-guidelines/form_check.py` | the form check (§5) |
| `product-guidelines/test_form_check.py` | its tests, at the directory's root because `gate/run_tests.py` does not descend into a subdirectory without `__init__.py` |

The identifier is `product-guidelines`, not `guidelines`: a part `guidelines` beside the glossary
term "guidelines" reads alike under WAY-93 and `glossary-term-collision`, and WAY-93 exempts only
element directories. The part is named after what it answers for, and its directory after the part,
as every other directory of WAY-09.

**Edits in place** (pre-`main`, WAY-07, `agent-instructions/README.md`; root C10), each shown at the
request:

- WAY-09: the list of directories gains `product-guidelines/`; the list of what each holds gains
  "`product-guidelines/` the template the guidelines of every product share, the template of each
  discipline of guidelines with the skill that leads its writing, and the form check of guidelines
  with its tests"; *Verification* level 2 gains a complying case (the templates, the skill and the
  form check stand together in `product-guidelines/`); *Scope* gains `product-guidelines`. Its
  binding part changes, so the six invariants deriving from it (`repository-file-location`,
  `element-directory-contents`, `relation-model-directory-contents`, `invariant-example-target`,
  `map-example-target`, `glossary-example-target`, `foundations/invariants.md:146-202`) are each
  checked against the new binding part and carry its fingerprint; their sentences, and so their
  versions, stay (WAY-31, WAY-57).
- WAY-38 and WAY-27: *Scope* gains `product-guidelines` (they govern the new script and the new
  files' pointers; a field, not a binding part — no fingerprint changes) (root, finding 21).

### 2.2 In a product

- Guidelines lie in `guidelines/` at the product root: `guidelines/<discipline>.md` for a
  discipline with one document, and for the styleguide one file per user interface,
  `guidelines/styleguide-<part>.md`, `<part>` the identifier of the part of the product's map whose
  files draw that user interface (root C7). A product with screens and an admin panel added to its
  backend holds two styleguides (row 13). The form check reports a file whose `<part>` is not a
  part of the map, so a renamed part cannot leave a stale file name unseen (§5.3).
- `guidelines/**` belongs to the product's part that directs agents' work (row 1, WAY-44); the cycle
  that writes the first guidelines adds the pattern to that part through `update-part-map` (in
  `loop2` that part is `agent-workflow`, whose files today claim no such path).
- Nothing of the template is copied into a product (WAY-34): the product's styleguide is an
  instance, checked against the template at the pinned commit.
- The installer creates no guidelines file: a product with no user interface has no styleguide, and
  a styleguide starts in a task.

## 3. The guidelines template (`product-guidelines/template.md`)

The template opens, like the elements' templates, with what it binds; each of its rules cites the
decision that sets it — G26 for the common form, G2 for what a rule holds, G3 for references
(§9.1).

### 3.1 Required form

A fenced Markdown skeleton the form check reads (as the element guards read `template.md`); a
discipline's template adds sections and required rules at the places it names (§4.1 gives the
styleguide's merged form whole):

```markdown
# <Discipline> guidelines — <what they cover>

- **Discipline:** <discipline>
- **Applies to:** <part> · …

## When to read

## Rules

### <rule name>

- **Decision:** <PREFIX-NN>@<fingerprint> · …
- **Invariant:** <identifier>@<fingerprint> · … | none
- **Good:** <a use that follows the rule>
- **Bad:** <a use that breaks it>

<how to apply the rule: what to do, and how>

## Examples

### <example name>

## Where in code
```

- *Discipline* names the discipline; where the-way holds a template of it
  (`product-guidelines/<discipline>/template.md`), that template adds to this form; otherwise this
  form alone applies (**autonomous**: a product may write guidelines of a discipline the-way has no
  template for, row 1).
- *Applies to* names parts of the product's map; the form check reports one the map does not hold.
- **A binding rule** stands under `## Rules` as a `### ` heading with the four fields; *Decision*
  names at least one decision of the product's log, *Invariant* the invariants that check it, or
  `none`; it carries no rationale and no rejected options — those stand in the decision (row 2,
  WAY-18, WAY-22). A discipline's template may require an invariant for every rule — the
  styleguide's does (row 18).
- **Anything that names no decision is an example** and stands under `## Examples` (row 2); an
  example carries no *Decision* field.
- **`## Where in code`** lists, as paths in backticks, the files and directories of the product the
  guidelines point to — never values copied from them (row 2, row 5, WAY-04).
- **A required section or required rule the product drops** reads, as its only body,
  `none — <PREFIX-NN>@<fingerprint>`, naming the product's decision that departs from the template
  (row 26; root C9). Text the departing decision keeps as an example may then stand under
  `## Examples`.

### 3.2 Rules of writing

- **References.** A reference is a token anywhere in the file outside fenced code — in a field, a
  `none —` line, a table row, a rule's prose, an example — of one of two forms: a decision number
  with the log's prefix (`<PREFIX-NN>`) or an identifier the invariants file holds, as an entry or a
  withdrawn identifier, followed by `@` and a run of letters and digits; or any identifier followed
  by `@` and exactly eight lower-case hexadecimal characters with no letter or digit after them. A
  reference relies on the entry's binding part and carries its fingerprint, eight lower-case
  hexadecimal characters (row 3, WAY-02; root, findings 8 and R5). A versioned package name such as
  `react@18`, `tailwindcss@4` or `lucide-react@0` fits neither form and is no reference, so a
  mistyped fingerprint after a real decision number or invariant is still caught while a package
  name is not. A bare identifier is allowed anywhere and never flagged (WAY-02). Text that would
  read as a reference but is none — an address, a sample, a package name whose version happens to be
  eight hexadecimal characters — stands in fenced code.
- **Code in backticks or fenced code.** Code names, at-rules and selectors stand in backticks;
  a class or value holding a `/` (`bg-primary/90`, `w-1/2`) stands in fenced code, because
  `instruction-files/check_instructions.py`, which follows the file once the product's root
  `AGENTS.md` names it (it is then a repository instruction file, glossary `:177`), takes a
  backticked token holding `/` for a path and reports it as a dead path, and takes an `@` word
  holding `.` or `/` outside code for an import (root, finding 16). No emphasis words (that
  script's `emphasis` check).
- **Language** (G26, **autonomous**): the structural words — headings of the required form, field
  names, the values of closed lists, the headings of required rules, `none —` — stay in English,
  because the form check reads them (as WAY-108 keeps a definition's headings and markers in
  English); the prose is in the language the product writes its guidelines in, which the-way does
  not set. Price: one product may mix languages across documents; a later decision can fix one.

### 3.3 The invariants of guidelines (root, findings 1, 2, 3, 6)

Two invariants whose identifiers and sentences the template gives. **The-way holds both**, deriving
from its own decisions; a product that writes guidelines holds copies with the same identifiers
and sentences, written by the cycle that writes its first guidelines, through `record-invariant`.

- `guidelines-form` — "Every file `guidelines/<name>.md` holds the header lines, sections, rules and
  rule fields the template of guidelines of the-way requires, at the commit of the-way the repository
  uses — the commit checked, in the-way itself; the pinned commit, in a product — and those its
  discipline's template adds, in their order, a dropped section or rule reading `none —` with a
  decision of the log and its fingerprint, every part it names being a part of the map, and every
  path under `## Where in code` naming something git tracks."
  - *Method*: `python -B <the-way>/product-guidelines/form_check.py --record .runs/guidelines-form.jsonl`
    — in the-way `product-guidelines/form_check.py`, in a product `.the-way/product-guidelines/form_check.py`.
  - *Part*: `every` — a renamed tokens file, a renamed part or a pin move can make it false
    whatever part the change touches (WAY-62).
- `guidelines-reference-current` — "Every token outside fenced code in a file
  `guidelines/<name>.md` that is a decision number of the log or an identifier of the invariants
  file followed by `@` and a run of letters and digits, or an identifier followed by `@` and eight
  lower-case hexadecimal characters, names a current, not repealed decision or a current, not
  withdrawn invariant and carries the fingerprint of its binding part in the foundation of the same
  commit, and, where {merge-onto} exists, in the foundation a merge onto {merge-onto} leaves."
  - *Method*: `python -B <the-way>/product-guidelines/form_check.py --merge-onto {merge-onto} --record .runs/guidelines-reference.jsonl`.
  - *Part*: in the-way `product-guidelines · decisions · invariants`; in a product, its
    agent-directing part, the part holding `foundations/**` and the part holding `.the-way`
    (WAY-62: a reworded decision, and a pin move that changes how fingerprints are read, must reach
    it; root, finding R7).
- *Derives from*: in the-way, `guidelines-form` from G4 and G26, `guidelines-reference-current`
  from G3; in a product, `none`, the template naming the-way's decisions the sentences come from
  (WAY-71's complying case for an invariant no decision of the log carries; finding 6).
- In the-way, with no `guidelines/`, both sentences hold and both methods record `pass`; the
  form check's citations (`# invariant: guidelines-form/1`, `# invariant: guidelines-reference-current/1`,
  WAY-65) name entries of the-way's `foundations/invariants.md`, so `invariant-citation-target`
  holds (finding 1).
- Weak point (root C8): the citations carry version 1 as literals; a product that rewords either
  copy raises its version and breaks the citation. The template says the sentences are given, not
  the product's to reword; a change to them is a change of the-way, which raises the-way's own
  entry and the script's citation together.

## 4. The styleguide template (`product-guidelines/styleguide/template.md`)

### 4.1 Merged form (root, finding 13)

```markdown
# Styleguide guidelines — <the user interface it covers>

- **Discipline:** styleguide
- **Applies to:** <part>

## When to read

## Roles

| Role | Kind | Meaning for the user | Text on it | Decision |
|---|---|---|---|---|

## Rules

### Each role in its meaning
### Every background with its text
### No value in place of a design token
### Visible focus
### Contrast of every pair
### States of shared controls
### A fault of one screen is fixed in its component
### Every value with its source
### The kitchen-sink page
### <further rules of the product>

## Examples

### Mockups
### Plan of a user-interface change
### <further examples>

## Where in code
```

Each `### ` under `## Rules` carries the four fields of §3.1, the styleguide requiring at least one
invariant in each (row 18); each required rule is present, in this order, or reads
`none — <decision>@<fingerprint>`.

### 4.2 What each part carries (root, finding 9)

| Part | Kind | Carries | *Decision* / *Invariant* the skill proposes | Row |
|---|---|---|---|---|
| `## Roles` | table | *Role*: the role's name in code, a role, never a colour (`primary`, `muted`); *Kind*: `background`, `text` or `other`; *Meaning for the user*: one sentence of what someone using the product understands on seeing it; *Text on it*: for a background role, the text role that stands on it, a role of the table of kind `text`, else `—`; *Decision*: the decision carrying the meaning, with its fingerprint. No values: `## Where in code` points to the tokens file | — | 5, 6, 24 |
| Each role in its meaning | rule | a screen uses each role only in the meaning its decision gives; a new meaning is a new decision (§7) | *Decision*: every decision the `## Roles` table names; *Invariant*: an agent-run invariant with k of n (§6.3 step 4) | 5, 18, 24 |
| Every background with its text | rule | a background role is always written with the text role on it in the table; the pair's values in code are held by the contrast rule | the adopting decision; `guidelines-form` | 6 |
| No value in place of a design token | rule | the user interface's files read colours, lengths and fonts from design tokens | the decision defining such a value; the product's script invariant (and the companion, where the product cleans gradually) | 19, 20 |
| Visible focus | rule | every control shows focus with the focus role's style | the WCAG adoption decision; the product's script invariant, resting on the WCAG fact | 19, 21 |
| Contrast of every pair | rule | every background–text pair reaches the contrast WCAG sets | the role decisions and the WCAG adoption decision; the product's script invariant, resting on the WCAG fact | 19, 21 |
| States of shared controls | rule | the directory of shared components, by path; every shared control has default, hover, focus visible, disabled, error, empty and loading, each shown on the kitchen-sink page or marked N/A with a reason; a component named by path only where it departs from that list — no inventory | the adopting decision; an agent-run invariant reading the kitchen-sink page, or a script where the product's stack lets one decide it | 7 |
| A fault of one screen is fixed in its component | rule | a global design token is a meaning for the whole product, so changing its meaning is a new or changed decision, while a change of its value that keeps its meaning is not; a fault of one screen is fixed in its component, not by changing a global design token's value for that screen | the adopting decision; an agent-run invariant over changes to the tokens file, judging whether a change alters what a role means or changes a global value for one screen's sake, or a script asserting that every role on `{fork-point}` keeps its name and *Kind* | 8, 24 |
| Every value with its source | rule | each value of the tokens file carries, beside it, where it comes from; the styleguide names the source the skill chose, not a list of tools | the adopting decision; the product's script invariant | 12 |
| The kitchen-sink page | rule | the path of the page showing the components and samples in every state, reachable only in development mode; the page is product code, not part of the document | the adopting decision; the product's script invariant that production does not serve it | 10 |
| Mockups | example | a mockup is a pattern to compare against, not a specification: meanings and values come from the guidelines and the tokens file | none (no check settles it) | 9 |
| Plan of a user-interface change | example | the order environment and library → values in their source → one screen → states, as an example, not a rule | none | 11 |

A rule for which neither a script nor an agent can give a verdict is not a rule (row 18): the
product drops it by a decision (`none — …`) and may keep its text under `## Examples`.

**Pairs in code and in writing (finding 22).** *To do* 5 says the styleguide points to "values,
pairs and the list of components" in code rather than copying them; read with row 6 and WAY-60 (a
contrast invariant's pairs stand in its sentence, a foundation entry or a decision) and WAY-04
(rules are written by hand), the pairing — which text role stands on which background — is a rule
written in a decision and in `## Roles`, while the pair's values live only in the tokens file.

**Why the meanings stand twice.** A role's meaning must stand in a product decision (row 24, WAY-60);
the styleguide's table says the same meaning for the agent at work (row 5), and the fingerprint in
*Decision* makes a reworded decision stop the merge until the table follows (row 3). A decision
holds one to three binding sentences (WAY-05), so the skill groups roles into several decisions —
signal colours, neutral scale, focus — each with its roles' meanings and pairs.

**Translated meanings (root, finding R6).** Where the product writes its guidelines' prose in
another language than its English decisions (G26), *Meaning for the user* and each rule's text are
a translation of the decision they restate. The fingerprint flags a reworded decision, never a
drifted translation, and no invariant of this change compares the two: a translation that drifts
while its decision stands is **not caught** by any check — only by a reader, the review of the
change that edits the table, or the agent-run invariant "each role in its meaning", which judges
screens against the decisions, not the table. This is the price of G26's language rule, shown at the
request beside the mixed languages of English required-rule headings over prose in the product's
language; a product that wants it caught writes its guidelines' prose in English.

**Role names** (G7): role names avoid the words the-way's glossary holds in another sense
(`surface`, `element`, `part`, `entry`, `result`, `verdict`, `gate`); the template's own examples are
`primary`, `muted`, `destructive`, `background`/`foreground`. Where a product's technology names a
role with such a word, the code and the styleguide keep it, and the product's foundation entries
write it with a qualifier (WAY-104), e.g. "the `surface` colour role".

### 4.3 Writing the file (for the cycle's author; root C5, C20)

- Take every meaning from the task's settlements and the decisions the foundation step wrote.
- Take every value, and its source, from the task's *To do*, which names per role the value and
  its source as settled, or the exact source address and the entry in it the value is read from
  (§6.2); never from memory or from a mockup.
- Point to values; write none into the styleguide.
- Run the form check; a meaning the task did not settle is a question that stops the cycle under
  row 24 (§7), never a row of `## Roles`.

## 5. The form check (`product-guidelines/form_check.py`)

### 5.1 Command

```text
python -B <the-way>/product-guidelines/form_check.py [ROOT] [--merge-onto REF|none] [--record PATH]
```

- `ROOT`: the repository root, default the working directory; it must be what
  `git rev-parse --show-toplevel` prints there.
- `--merge-onto`: the commit of the main branch a merge goes onto; the fork point is
  `git merge-base HEAD <REF>`, as the decisions guard computes it.
- `--record`: a JSON Lines record (`.jsonl`) in the shared form (WAY-74).
- **Which checks a run records (root, finding 2)**, by the shared report's semantics
  (`Report.recorded`, `elements/common/guard_shared.py:241-246`): the checks of form are selected
  by no option; the checks of references — same commit and after the merge — are selected by
  `--merge-onto`. A run with no option records the checks of form (`guidelines-form/1`); a run with
  `--merge-onto` records the checks of references (`guidelines-reference-current/1`), hence the two
  methods of §3.3. Every check still runs and prints in every run. With `--merge-onto none` the
  same-commit check records `pass` or `fail` and the merge check `unchecked` with the shared reason
  (`guard_shared.NO_COMMIT_REASON`); the invariant's result is then `fail` where the same-commit
  check failed and otherwise not `pass` (WAY-65: several checks citing one invariant give `pass`
  only when each records `pass`). **Before a main branch exists** — the-way today, a product before
  its first `main` — `guidelines-reference-current` therefore records `pass` from the same-commit
  check beside `unchecked` from the merge check; this is the expected state, and the request names
  it as such, as the README names the guards' unchecked lines. Without `--merge-onto`, the merge
  check does not run and a `note:` says so.
- **Report per file (finding 14).** One shared `Report` per guidelines file, so each finding prints
  as `guidelines/<name>.md:<line>: error: …`, and one for the run (templates, foundation, git);
  the record merges the lines of all reports. A check citing an invariant in several reports gives
  it `pass` only when each does.
- **Borrowed code reports nothing of its own (finding 15).** The parsers of the decisions,
  invariants and part-map guards (`detect_prefix`, `parse_log`, `merged_log`, latest versions in
  force; `read_rules`, `parse_file`; the map's part headings) are loaded by path and given a report
  of the form check's own, discarded after the call; only a failure of the run (git cannot read
  the log, a file cannot be read) carries over to the run's report. The form check's exit code and
  record speak of guidelines alone, never of the log's own rules (e.g. `log-merge-copies`).
- Exit codes: 0 without errors, 1 with errors, 2 when it cannot run (not a repository root, a
  template of the-way unreadable, a record path not ending in `.jsonl` or not writable).
- Python standard library, git as the only subprocess (WAY-38, `script-imports`,
  `script-subprocesses`); it parses Markdown only and computes every fingerprint through
  `relation-model/fingerprint.py` (WAY-02 rejected one computation per element).

### 5.2 What it reads

- The guidelines: `git ls-files -z --cached --others --exclude-standard -- ':(literal)guidelines/'`.
  It reads each path of the form `guidelines/<name>.md`, one level deep, lower-case `.md`; every
  other path git lists under `guidelines/` gets a `warning:` naming it as not read (finding 17).
  No `guidelines/` → a `note:`, no error, both invariants `pass`.
- The templates: from the-way checkout the script lies in — in a product, its pinned `.the-way`.
- The foundation: `foundations/decisions.md`, `foundations/invariants.md`,
  `foundations/part_map.md` of the working tree; with `--merge-onto`, decisions as the log a merge
  onto the commit leaves (the decisions guard's merged log), and an invariant as on the branch where
  its sentence differs from the fork point, else as on the onto commit (an invariant the onto commit
  withdrew or removed, and the branch did not change, is not current).

### 5.3 What it reports as an error

1. A missing or misplaced header line, section, required rule or rule field (`guidelines-form`).
2. A rule under `## Rules` naming no decision; in a styleguide, naming no invariant
   (`guidelines-form`).
3. In `## Roles`: a *Kind* outside its list; a background role whose *Text on it* is empty or names
   no text role of the table; a *Decision* missing; a decision the table names that the rule "Each
   role in its meaning" does not name in its *Decision*, unless that rule is dropped (`guidelines-form`).
4. A dropped section or rule whose body is anything but `none — <PREFIX-NN>@<8 hex>`
   (`guidelines-form`).
5. A part in *Applies to*, or the `<part>` of a file name `styleguide-<part>.md`, that the product's
   map does not hold as a part (`guidelines-form`).
5a. A file whose name and *Discipline* disagree: the name is `<discipline>.md` or
   `<discipline>-<part>.md` with `<discipline>` the header's *Discipline*, and a styleguide is always
   `styleguide-<part>.md`; `guidelines/styleguide-web.md` naming another discipline, or a
   `Discipline: styleguide` file named otherwise, is an error, so no file is held to the wrong
   template in silence (`guidelines-form`; root, finding R9).
6. A path of `## Where in code` that is absolute, holds a `..` segment, a drive or a UNC prefix, or
   that `git ls-files -- ':(literal)<path>'` does not list (`guidelines-form`).
7. A reference, in the two forms of §3.2, anywhere outside fenced code: whose part after `@` is not
   eight lower-case hexadecimal characters; naming a decision that is not in the log or repealed, or an
   invariant not in the file or withdrawn; carrying a fingerprint other than the current one on the
   same commit; and, with `--merge-onto`, other than the current one after the merge
   (`guidelines-reference-current`). The message names the reference, the entry and its current
   fingerprint, like the decisions guard's stale-relation message. It never offers to renew
   fingerprints (WAY-31 *violates*).

### 5.4 Trust boundary (WAY-48)

The script reads files a product writes; the part map records it as the part's trust boundary. It
treats each as untrusted:

- a guidelines path that is a symlink, a directory, or not a regular file → error for that path,
  nothing read through it; `guidelines` itself a symlink or a file → error;
- text that is not UTF-8 → error, no decoding guess; a file over 1 MiB (**autonomous**, as
  `check_instructions.py`) → error, not read;
- references and paths are matched by anchored regular expressions with no nested repetition, so a
  long or crafted line cannot make matching run away;
- paths go to git only as `:(literal)` pathspecs after the shape test, never to the file system; no
  path the file names is opened;
- a UNC or URL-shaped path is refused before git sees it; the script's own code opens no socket;
- it writes nothing but `--record`.

### 5.5 How it joins the checks

- In a product: the two copies of §3.3 name it as their methods, so the product's gate, when it
  exists, runs it; until then the installer's product guidance names it (§8), as it names the
  format guards today.
- In the-way: the two invariants of §3.3 run it on the-way itself (no guidelines: `pass`), and the
  invariants on the script (§9.3) are checked by `python -B gate/run_tests.py product-guidelines`.
- No new critical flow (**autonomous**; root, finding 4): the reaching is done by the *Part* fields of
  §9.3, which name every part whose code the form check runs; a flow can be added later at the cost
  of one gate test.

## 6. The skill `maintain-styleguide` (`product-guidelines/styleguide/SKILL.md`)

### 6.1 Frontmatter and place

```yaml
name: maintain-styleguide
description: Use when a product's user interface — its screens, an admin panel added to a backend included — needs a styleguide created before its first screen, audited where screens exist, or refreshed or extended, leading those matters of a styleguide task's refinement with the human.
```

The description is one line and a safe plain YAML scalar (no `": "`, no `" #"`), as
`skill_entry_points.py` requires. The opening paragraph says where the-way lies, as the other
skills do (the session's checkout in the-way itself, `.the-way` in a product), and that every skill
it names is the project skill with the `the-way-` prefix. The skill does not use Superpowers
(WAY-125 adopts it for the cycle only). It describes what it takes from outside sources rather than
naming or pointing to them (WAY-27; finding 23).

### 6.2 The split between refinement and the cycle (root C5)

| | The skill, in the refinement | The cycle's author, in `implement-task` |
|---|---|---|
| Writes | the task document only — through `refine-task`'s steps and its *Settlements to record* — and research reports under `.runs/styleguide/<part>/`, which the product's git ignores | product entries through the element skills in the foundation step; `guidelines/styleguide-<part>.md` from the template; the token values with their sources; the kitchen-sink page; the checks of the invariants, by other agents (WAY-69); the instruction-file change through the instruction-files skill; the `guidelines/**` pattern through `update-part-map` |
| Never writes | the foundation, the styleguide file, product code (WAY-01, WAY-28: entries reach the main branch with the code that follows them, in a task that touches the parts they govern) | a meaning the task did not settle (§7) |

The skill runs inside a task's refinement. It is invoked on a styleguide task — new or existing in
the product's backlog (WAY-107). It has the task opened or continued by `refine-task` steps 1–2,
takes over at `refine-task` step 3 for the styleguide's matters, and hands back to `refine-task`
step 4, whose step 5 turns what was settled into rows through `find-foundation-entries` in task
mode, from the conversation and this skill's record as source. `refine-task` and `implement-task`
are not changed.

What reaches the task document, so the cycle's author can write the styleguide without the
conversation:

- *To do*: the fixed items — write `guidelines/styleguide-<part>.md` from
  `.the-way/product-guidelines/styleguide/template.md`; put the role values in the tokens file with
  their sources, **naming per role the value and its source as the human settled them, or the exact
  source address and the entry in it the value is read from** (root, finding 12); build or
  extend the kitchen-sink page; write a check for each new invariant; apply the instruction-files
  skill for the pointer and the rule (§6.6); add `guidelines/**` to the agent-directing part; for
  the first guidelines, write the copies of `guidelines-form` and `guidelines-reference-current` —
  and the items the audit's charges call for, or each charge `deferred` with its reason.
- *Questions to settle*: each meaning, role, pair, value, state rule, departure from the template
  and WCAG answer, with the human's words as its source.
- *Context*: the charges with `file:line`; the research's sources (page and version); what the
  audit could not see.
- *Settlements to record*: through `find-foundation-entries` — the product's decisions (grouped,
  §4.2), invariants, environment facts, and the part-map change.

### 6.3 Steps

**0. Read.** The styleguide template and the guidelines template whole;
`project-level/task/skill/SKILL.md` and `project-level/task/template.md`, whose steps and sections
the skill drives (finding 23); "How a skill asks" in `elements/common/way_of_working.md`;
`elements/common/critique/SKILL.md`; the product's `AGENTS.md` and existing guidelines; the
product's foundation by "Reading the foundation" (WAY-150), including the decisions that settle the
user interface's technology and the agent's way to the running product (WAY-165).

**1. Recognize** (row 14). Which user interface (a part of the map); what it has — a tokens file the
screens read, one nothing reads, shared components, nothing; whether it has screens; whether a
styleguide exists. That gives the mode: no screens → before the first screen; screens → audit; a
styleguide exists → refresh or extension (with an audit where screens changed). The skill extends
what exists; a new library of components or a new styling technology is a technology choice it
records as an open question of the task, never settles (row 9's rejected part, WAY-121).

**2. Starting rules** (rows 15, 16; mode before the first screen, and every refresh or extension).
- Ask, as a question of assessment, for the human's preferences for the user interface's
  technology (the one the foundation settles).
- Without preferences, research the basic styleguide rules for that technology: one fresh agent per
  question, each source a page with its version, a report each under `.runs/styleguide/<part>/`;
  one fresh agent following `critique` refutes every claimed difference no source supports before
  anything reaches the human, and the report ends `critique: passed`; with no fresh agent, stop and
  say so. The research proposes, never imposes (row 16; the method of research taken from WAY-122 by
  G17, not WAY-122's properties of typed, documented technologies).
- Add the product's meanings: from the definition, plan, specs and mockups, describe each screen the
  product announces — what the user sees, the components it is built from, its states with the
  messages the user reads.
- The starting set is wider than the first task that uses it (row 15).

**3. Audit** (row 17; mode with screens). Both directions: from the source of values to the screens
that read it, and from each value in a screen to the design token or component that should cover
it. End with 3–5 charges, each with `file:line` and one sentence of its effect on the user, in four
categories — missing design token, missing shared component, accidental architecture, meaning (one
colour in several meanings); ask every time "what will someone see without data, straight from a
link, after a refresh". Use the agent's way to the running product where the product's foundation
settles one; otherwise audit from code and mark as unchecked what cannot be seen without the
running product. A charge not taken into the task stays, marked deferred with its reason. An
existing choice the human keeps becomes a decision whose rationale is the human's words or
`unknown`, never one the agent infers (WAY-29).

**4. Settle with the human** (rows 23, 27; WAY-113).
- Each choice is shown through what the user will see — "the button that saves stands out; the one
  that deletes is red, and its text white" — never through token names or values; ways, their
  cost, a recommendation; the skill asks even where it has a recommendation (row 27), and after a
  choice entering a binding part, the one question WAY-113 gives. A term of the field (contrast,
  focus) is said once in plain words before it is used (row 23, *Need* 4).
- What it settles: the roles, each named by its role, with its meaning, its value and source, and,
  for a background, its text role (rows 5, 6, 12); the states of shared controls (row 7); the
  product's decision adopting the template, and each departure from it by a decision with its
  reason (row 26); the kitchen-sink page (row 10); the meanings grouped into decisions of at most
  three binding sentences (§4.2).
- **Accessibility** (row 21). First ask whether a law or a contract binds the user interface's
  accessibility (WAY-86's last sentence, WAY-46): where one does, it is an environment fact and a
  failure mode of the part, not an adoption. Then propose the decision adopting WCAG, with the
  default recommendation to adopt: the newest edition published when the decision is written,
  named by its number as read on the W3C's page at that time, never from memory (WAY-80); level AA;
  every screen of the user interface. Another variant only where the human deliberately wants it;
  nothing is adopted without the human's acceptance. The environment facts are the success
  criteria the invariants take conditions from — contrast and visible focus at least — each with
  the W3C edition's address and the passage word for word (WAY-76, WAY-77, WAY-80).
- **Invariants** (rows 18, 19, 20; root, finding 7). Every binding rule gets an invariant: a script where a
  script can decide it, otherwise an agent with k of n; a rule even an agent cannot check is an
  example. The skill proposes, each as a product command the product declares (WAY-38):
  - no file of the user interface's part holds a value written in place of a design token, as a
    decision of the product defines such a value (WAY-60);
  - every control the part's files draw carries the focus style of the focus role; it derives from
    the WCAG adoption decision and rests on the WCAG fact of visible focus (WAY-73; root,
    finding 20);
  - every background–text pair a decision names reaches, with the values of the tokens file, the
    contrast ratio the WCAG fact gives; it derives from the role decisions and the adoption
    decision and rests on that fact (WAY-73);
  - **each role is used only in its meaning** — an agent-run invariant with k of n whose sentence
    speaks of the state of every file of the user interface's part ("no file of `<part>` uses a
    role in a meaning other than its decision gives"), never of a change, and whose method reads
    all of them; it runs when a change reaches it, its *Part* naming the user interface's part and
    the part holding `foundations/**`, since a reworded role decision changes what the files must
    hold (WAY-60, WAY-61, WAY-62; row 18; root, findings 7 and R3);
  - where the product cleans its screens task by task, the companion: no file of the part holds
    more values written in place of design tokens than on `{fork-point}`, and a file not on
    `{fork-point}` holds none; withdrawn once the full invariant holds; not proposed under a single
    clean-up. The full invariant then stands on the list of violated invariants by a foundation
    change the human accepts (WAY-51). Weak point: a renamed file looks new.
  - the invariants the rules of §4.2 call for (states, the fix in the component, sources of values,
    the kitchen-sink page), each a script or an agent with k of n.
- The set of proposals is critiqued by one fresh agent before it is shown together
  (`way_of_working.md`, "Critique before collective review").

**5. Hand back** to `refine-task` step 4 with the record of §6.2.

### 6.4 Orchestrated refinement (root, finding 11)

When `refine-task` runs in orchestrated mode — a styleguide task of a project plan led by
`lead-project` (WAY-154, WAY-155) — the skill follows that mode's routing: every question, the
WCAG proposal and every choice shown through what the user sees go into the conversation turn as
`refine-task` routes them, and the skill ends the turn rather than asking the human; the research
agents and the critique are requested from the project orchestrator, which starts them, with the
reports' paths under `.runs/styleguide/<part>/` named in the turn; the skill starts no child agent
and edits only the task document and its turn.

### 6.5 What the skill holds and what it leaves

It holds the order of the styleguide's work. Rules of a guidelines file stand in the templates, each
citing its decision; how to ask stands in `way_of_working.md`; how entries are written stands in
the element skills. The skill restates none of them (WAY-35 by analogy).

### 6.6 The instruction file (row 22)

The cycle's author applies `.the-way/instruction-files/SKILL.md` (the pinned copy, WAY-127) to:
- a pointer in the product's root `AGENTS.md`, outside the installer's block, naming
  `guidelines/styleguide-<part>.md` in backticks with the condition "before you change a file of
  `<part>`" (WAY-128: work an agent would not otherwise find; WAY-129);
- the rule forbidding values written in place of design tokens in the user interface's files,
  placed where that skill's principles put a rule for some files (WAY-128: a file the tools load
  with those files), admissible because it carries the product's decision (WAY-130), and saying
  what its mechanism — the product invariant — is for (WAY-133); no lint command of its own
  (WAY-16).

Once named from `AGENTS.md`, the styleguide is a repository instruction file (glossary `:177`):
`check_instructions.py` follows it (§3.2).

## 7. Row 24 — where a new meaning is approved (root C5)

- A new or changed meaning settled in the refinement is approved **in the task document**: it
  stands in *Questions to settle* and *Settlements to record*, and the human's acceptance of the
  whole document before the cycle (WAY-124) is the decision approver's approval before the code
  that needs it (WAY-30).
- A new meaning a cycle meets without the task having settled it is a decision the cycle's agents
  cannot write on their recommendation: `implement-task` already prepares a **blocked draft
  request** with the evidence and stops when "a binding rule reserves a decision to a human and code
  cannot proceed without it"; G5 is that binding rule, and it **narrows WAY-114** in the area of new
  or changed meanings of a product's guidelines, which WAY-114 would otherwise have the agent write
  and the human accept at the merge (root, finding 10; WAY-25). `implement-task` is
  not changed; teaching the cycle to recognise such a meaning is the task "cycle for view changes".
- Using a meaning that exists needs no approval.

## 8. Installer and entry points

> Revised in the cycle (root C31): the guidance sentence runs both form-check commands **before every merge** where `guidelines/` exists, not only before a merge changing `guidelines/` or `foundations/` (whole-branch review, Important 1; fix `896071a`).

- `installation/install.py` `SKILLS` gains `"maintain-styleguide":
  "product-guidelines/styleguide/SKILL.md"`. `installation/test_install.py` `NAMES` and
  `installation/README.md:56` gain it by hand (no test compares them with `SKILLS`).
- `product_guidance()` gains one sentence: where the repository holds `guidelines/`, run
  `python -B .the-way/product-guidelines/form_check.py` and
  `python -B .the-way/product-guidelines/form_check.py --merge-onto <main commit>` before a merge in
  which a file of `guidelines/` or of `foundations/` changed. `guidelines/` is a path of the-way's
  convention, like `foundations/`, not a product's choice (WAY-107 keeps product-chosen paths out of
  the block). The block text changes, and so does it whenever `SKILLS` grows: a product moving its
  pin removes the old block, as `installation/README.md` already says; that is how `loop2` gets the
  skill. The `installation-command` surface keeps its wording; the request carries the line on what
  moving the pin changes (promise level `pinned`).
- `python -B agent-instructions/skill_entry_points.py --write` writes
  `.claude/skills/the-way-maintain-styleguide/SKILL.md` and its `.agents/` twin; committed with the
  skill.

## 9. Entries the change writes (names, not wordings)

### 9.1 Decisions of the-way (new numbers in order from WAY-167, given at writing)

| # | Question (proposed) | Rows | Relations (proposed) | Scope |
|---|---|---|---|---|
| G1 | What are a product's guidelines, and where do they lie? | 1 | derives from WAY-44, WAY-04 | product-guidelines |
| G2 | What does a guideline hold, beside the foundation entries that carry it? | 2 | derives from WAY-22, WAY-18 | product-guidelines, decisions, invariants |
| G3 | What happens to a guideline's reference when its entry's wording changes? | 3 | derives from WAY-02, WAY-31 | product-guidelines, relation-model |
| G4 | What checks the form of guidelines? | 4 | derives from WAY-04 | product-guidelines |
| G26 | What form does every guidelines document take? | common form (finding 24) | derives from G2 | product-guidelines |
| G5 | How is a new meaning of guidelines approved? | 24, and row 27's approval before code | derives from WAY-30 · narrows WAY-114 | product-guidelines, decisions |
| G6 | Does the styleguide template bind a product directly? | 26 | derives from WAY-34 | product-guidelines |
| G7 | How does a styleguide name and pair its colour roles? | 5, 6 | derives from G6 | product-guidelines |
| G8 | What does a styleguide say of shared controls? | 7 | derives from G6 | product-guidelines |
| G9 | Where is a fault of one screen fixed? | 8 | derives from G6 | product-guidelines |
| G10 | What is a mockup to a styleguide? | 9 | derives from G6 | product-guidelines |
| G11 | What is the kitchen-sink page? | 10 | derives from G6 | product-guidelines |
| G12 | Does a styleguide carry an order for the plan of a user-interface change? | 11 | derives from G6, WAY-36 | product-guidelines |
| G13 | Where does a value of the tokens file say it comes from, and who picks the source? | 12 | derives from G6 | product-guidelines |
| G14 | Which user interfaces get a styleguide? | 13 | derives from G6 | product-guidelines |
| G15 | When does a product's styleguide come into being? | 15 | derives from G6 | product-guidelines |
| G16 | What does the styleguide skill look at first? | 14 | — | product-guidelines |
| G17 | Where do a styleguide's starting rules come from? | 16 | derives from WAY-122, WAY-120 | product-guidelines |
| G18 | How does the skill audit a product that has screens? | 17 | — | product-guidelines |
| G19 | What checks a binding rule of a styleguide? | 18 | narrows G2 | product-guidelines, invariants |
| G20 | Which invariants does a styleguide start with? | 19 (with "each role in its meaning"; root, finding 7) | derives from G19 | product-guidelines, invariants |
| G21 | What keeps a product cleaned gradually from adding hard-coded values back? | 20 | derives from WAY-51, WAY-60 | product-guidelines, invariants |
| G22 | Where do the thresholds of contrast and focus come from? | 21 | derives from WAY-86 | product-guidelines, environment-facts |
| G23 | How does a product's instruction file lead to its styleguide? | 22 | derives from WAY-128, WAY-133 | product-guidelines, instruction-files |
| G24 | How does the styleguide skill talk with the human? | 23, 27 | narrows WAY-114 | product-guidelines, decisions |
| G25 | What does the-way take from 10x-ui and the Open Mercato skills? | WAY-100 (*Decisions in play*) | derives from WAY-100 | product-guidelines |

- **G26** (root, finding 24; **autonomous** in its language rule): the common form — the header
  lines *Discipline* and *Applies to*, the sections `## When to read`, `## Rules`, `## Examples`,
  `## Where in code` in that order, a rule as a heading with *Decision*, *Invariant*, *Good*, *Bad*,
  the `none —` departure, and the structural words in English with the prose in the product's own
  language (§3.2). G7 carries the closed list of *Kind* and the words role names avoid.
- Rows 5–13 and 15 are written as G6's subjects: what the template carries and the skill proposes,
  each binding a product through the product's own adopting decision (row 26).
- G5 carries the approval-before-code clause of row 27 once (WAY-19) and narrows WAY-114 in the area
  of new or changed meanings of guidelines; G24 carries asking with a recommendation and showing
  through what the user sees, and narrows WAY-114 in the area of the styleguide skill's questions.
  Two decisions narrowing one decision in disjoint areas; neither names the other.
- G25 names what is adopted and what is left, describing what was seen rather than pointing to the
  sources (WAY-27). Adopted from `10x-ui`: role-named tokens in one source with components kept in
  the repository; the background–text pair (from the lesson behind it); the two-way audit with 3–5
  charges, `file:line` and the effect on the user, deferred charges kept; the standing question
  (with "after a refresh", without "logged out"); recognising what exists and extending it; values
  deposited with their source; the scan for hard-coded values as an invariant's method; the
  seven-state matrix with N/A and a reason; the kitchen-sink page; the plan order as an example; the
  fix in the component; the instruction-file block, as a pointer and a rule. Left: its commands and
  change folders, the tool lists (shadcn, tweakcn, presets), "not now: a view that does not exist
  yet", one view per change, model routing, the screenshot test (open), Figma, and its example role
  `surface` (a glossary word of the-way). Adopted from `om-ux-setup`: reading what a repository's
  design already holds and saying plainly when it holds nothing; a palette derived from code is a
  proposal, never a rule, until declared; asking what only the team knows. From `om-ux-shape`:
  describing each screen with what the user sees, its components and its states with the messages
  the user reads (its workflow step 7 and Shape template — its handoff mode lists no screens);
  writing for a reader who was not in the conversation. Left: the extractor and its files, the AI
  guidance, the scoring rubric.
- Wording: "guidelines" as the glossary term; "discipline", never "domain", for what one guidelines
  document covers (WAY-95 and WAY-104 use "a product's domain" for its field of business; no file
  of the foundation or of `elements/common/` uses "discipline"; root, finding 19); "user
  interface" and "screen", never bare "interface" or "view" (WAY-165; WAY-18's view of decisions);
  "design token", never bare "token" (WAY-84's secret, WAY-162's model tokens); "form check", never
  "checker" (format guard's *Avoid*). "Styleguide" is written as "the guidelines of the styleguide
  discipline" where a binding sentence defines it.

### 9.2 Glossary

- "guidelines" (row 25) through `record-glossary-term`: a hand-written document of a product,
  outside its foundation, that tells agents what to do and how in one discipline of work on the
  product. *Avoid* must not hold "guide": WAY-128, WAY-130 and WAY-133 use it for the-way's
  integration guide, and every use of an *Avoid* word is an error (WAY-98).

### 9.3 Invariants of the-way

The two of §3.3 — `guidelines-form` (*Part* `every`; derives from G4, G26) and
`guidelines-reference-current` (*Part* `product-guidelines · decisions · invariants`; derives from
G3) — and six on the script (WAY-22: what the form check makes true), each through
`record-invariant`, *Method* `python -B gate/run_tests.py product-guidelines --record
.runs/product-guidelines-tests.jsonl`, *Part* `product-guidelines · decisions · invariants ·
part-map · elements-common · relation-model` — every part whose code the form check loads, so a
change to a borrowed parser reaches them (root, finding 4):

| Identifier (proposed) | Sentence (shape) | Derives from |
|---|---|---|
| `guidelines-check-form` | the form check reports as an error each missing or misplaced header line, section, required rule or rule field its templates require, each dropped section or rule naming no decision with a fingerprint, each part named that the map does not hold, and each file whose name and *Discipline* disagree | G4, G26 |
| `guidelines-check-carrier` | it reports as an error each rule naming no decision, in a styleguide each naming no invariant, and each role decision the rule of roles' meanings does not name | G2, G19, G20 |
| `guidelines-check-colour-pair` | it reports as an error each background role of a styleguide naming no text role of its table | G7 |
| `guidelines-check-reference-target` | it reports as an error each reference of the two forms §3.2 gives, outside fenced code, naming no current decision or invariant, and each whose part after `@` is not eight lower-case hexadecimal characters | G3 |
| `guidelines-check-stale-reference` | it reports as an error each such token whose fingerprint differs from the named entry's current one on the commit checked and, given `{merge-onto}`, after the merge | G3 |
| `guidelines-check-code-path` | it reports as an error each path of `## Where in code` that leaves the repository or names nothing git tracks | G4 |

Each of G2, G3, G4, G7, G19, G20 and G26 is verified at level 1 by the invariants above that derive
from it, named in its *Verification* (WAY-12, WAY-17); the other decisions are verified at level 2.
The six WAY-09 invariants carry WAY-09's new fingerprint (§2.1).

### 9.4 Part map

- New part `product-guidelines`: responsibility "the form of a product's guidelines, the templates
  of each discipline with the skill that leads writing them, and the form check"; *Files*
  `product-guidelines/**`; *Depends on* decisions · invariants · glossary · part-map ·
  environment-facts · elements-common · relation-model · project-level · instruction-files ·
  task-cycle (§7 rests on its blocked-draft rule; finding 23); *Trust boundary*
  `product-guidelines/form_check.py`; *Failure modes*, each with severity and detection:
  - the form check passes a reference whose entry changed wording — the styleguide tells agents an
    old rule — high — detected by `guidelines-check-stale-reference`;
  - the skill settles a meaning the human did not accept — the cycle builds screens on it — high —
    not detected;
  - the research shows a difference between options that no source supports — the human chooses on
    an invented consequence — high — not detected;
  - the form check, reading a crafted guidelines file, reads outside the repository, reaches a
    network host or stops without a report — high — not detected.
- `installation` *Depends on* gains `product-guidelines`; `agent-instructions` *Depends on* gains
  `product-guidelines`; the flow `skills-reach-the-way-sessions` gains `product-guidelines` in
  *Parts*.

### 9.5 Environment facts

None of the-way. The WCAG facts are a product's, written when a product's styleguide task adopts
WCAG (§6.3 step 4).

## 10. Verification a plan can run

Commands that exist, run from the worktree root (no-main options per the README):

- `python -B gate/run_tests.py product-guidelines` (new), `installation`, `agent-instructions`,
  `gate`, and every directory of the baseline (`reports/run_checks.py`).
- `python -B product-guidelines/form_check.py --record .runs/guidelines-form.jsonl` and
  `python -B product-guidelines/form_check.py --merge-onto none --record .runs/guidelines-reference.jsonl`
  on the-way itself: exit 0, the record holding `pass` for `guidelines-form/1`, and for
  `guidelines-reference-current/1` the same-commit `pass` and the merge `unchecked`.
- **The invariants guard with the form check in place (root, finding 1):**
  `python -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none`
  reports no error, in particular no `invariant-citation-target` finding for the form check's
  `# invariant:` lines.
- `python -B agent-instructions/skill_entry_points.py` reports entry points current after `--write`.
- Format guards with no-main options on the changed foundation files: decisions
  (`--base none --merge-onto none`), invariants, glossary, part map, environment facts.
- `python -B instruction-files/check_instructions.py <temp product>` on a temporary repository
  whose root `AGENTS.md` names a styleguide filled from the template: no `error`, no `dead-path`, no
  `at-import`.

Tests in `product-guidelines/test_form_check.py`, in temporary git repositories, with expected
fingerprints and messages written as literals (WAY-69) and a test guarding the fixture's wording
(as `gate/test_wording_reaches_dependants.py`); each test cites the invariant it gives a verdict for
in its body (`# invariant: <id>/1`, WAY-65); each invariant's deliberate break (a guard line
removed) makes its tests fail:

- form: a complete styleguide passes; each required section, header line, required rule or field
  removed or moved in turn fails; a dropped section or rule with `none — <decision>@<fp>` passes,
  with a bare `none` fails; a discipline with no template is held to the common form only; a part
  in *Applies to* or in the file name missing from the map fails; `styleguide-web.md` with another
  *Discipline*, and a `Discipline: styleguide` file named otherwise, fail;
- carriers and pairs: a rule with no decision; a styleguide rule with no invariant; a role decision
  absent from "Each role in its meaning"; a background role with no text role, or naming a
  background role;
- references: current passes; changed decision wording fails with both fingerprints in the message;
  changed invariant sentence fails; repealed decision, withdrawn or missing invariant fails; a
  seven-character or upper-case fingerprint after a decision number or an invariant identifier
  fails; `react@18`, `tailwindcss@4` and `lucide-react@0` in prose are no references and pass; a
  bare identifier in prose passes; **a stale
  reference in a `none —` departure line, in a rule's prose, in a table row and under `## Examples`
  each fails** (root, finding 8); a token in fenced code is ignored; `--merge-onto` with the
  decision changed only on the onto commit fails, **with an invariant changed or withdrawn only on
  the onto commit fails, with the invariant changed on the branch takes the branch's** (finding 18);
  `--merge-onto none` records the same-commit verdict and `unchecked` for the merge; without the
  option, a `note:`;
- records and reports: a run with no option records `guidelines-form/1` lines only, a run with
  `--merge-onto` `guidelines-reference-current/1` lines only; findings of two guidelines files print
  under their own paths; a decision log whose copies conflict with the onto commit makes no
  `log-merge-copies` line and no exit 1 of the form check; a non-`.jsonl` record path exits 2;
- what it does not read: `guidelines/styleguide/web.md` and `guidelines/x.MD` each give a
  `warning:` naming the path;
- adversarial inputs (WAY-48): a guidelines file that is a symlink (skipped where the platform
  cannot create one, as the installer's tests do), a directory named `x.md`, `guidelines` as a file;
  non-UTF-8 bytes; a file over 1 MiB refused unread; **a file just under 1 MiB holding one line of
  backticks, `@` and hex runs, finished within a bound** (finding 18); paths `../outside.md`,
  `/etc/passwd`, `C:\x`, `\\host\share\x`, `:(glob)**`, `http://host/x` — each refused, and **the
  test, capturing the git subprocess calls, asserts no such path reaches git**; the script's own code
  opens no socket (a patched `socket` fails the test if called — this covers the script's code, not
  git's);
- exit codes 0, 1, 2 and each report's count line.

Installer tests: `NAMES` gains the skill, so the existing assertions cover both wrappers and the
sibling sentence; the guidance test asserts the form-check sentence.

The skill's text is process prose that no test asserts: it is checked by the generated entry point
(frontmatter and description), by the independent assessment of the change (WAY-10,
`elements/common/critique/SKILL.md`), and by a row-to-text table in the request mapping each of rows
5–24, 26 and 27 to the sentence of the skill or template that carries it, which the whole-change
reviewer verifies. A trial on a product is the `loop2` task after the merge (task, question 1).

## 11. Contradictions and readings (root C10)

1. The task asks for "a new version of WAY-09"; before `main`, WAY-07 and the README require an edit
   in place — WAY-09 is edited in place, the change of meaning shown at the request.
2. The task's question 2a models announced screens on `om-ux-shape`'s handoff mode; no mode of it
   enumerates a product's screens — its workflow step 7 and Shape template describe each screen,
   and those are taken.
3. A part `guidelines` collides with the term "guidelines" (WAY-93) — the part is
   `product-guidelines`.
4. Meanings and pairs cannot stand only in the styleguide (WAY-60, row 24) — they stand in product
   decisions of at most three binding sentences each, and the styleguide's table repeats them under
   fingerprints.
5. Writing product entries outside a task's foundation step (WAY-01, WAY-28, WAY-106) — settled by
   the split of §6.2.
6. "Interface" in WAY-165 covers an API and a terminal — the new sentences say "user interface".
7. "Domain" in WAY-95 and WAY-104 is a product's field of business — the new sentences say
   "discipline".
