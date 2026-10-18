# Independent assessment — product guidelines and the styleguide discipline

Assessed range: `96623ed..677ef7c`, read in the worktree
`C:/Storage/repos/the-way-wt/product-guidelines-styleguide-assess` (detached at `677ef7c`).
Method: `elements/common/critique/SKILL.md` of that worktree, read whole first. The critic read
the diff and the files at `677ef7c`, never commit messages or the cycle's own records. No session
transcript and no file outside the worktree was read.

All `file:line` anchors below are paths under the worktree root at `677ef7c`.

## What was run

| Check | Result |
|---|---|
| `elements/decisions/format_guard.py foundations/decisions.md` (no base) | 0 errors, 32 warnings (27 `Approved by` placeholders, 5 overdue check-by dates that predate this change) |
| the same with `--base 96623ed --merge-onto 96623ed` | 31 errors: 27 placeholders counted as errors after a merge, plus WAY-09, WAY-27 and WAY-38 "differ from their copy" and "the log differs here". All four are the edits in place that `agent-instructions/README.md:20-24` allows before `main`; no fingerprint of a relation is reported stale |
| `elements/invariants/format_guard.py` with and without `--base/--merge-onto 96623ed` | 0 errors, 0 warnings: every `Derives from` fingerprint, the renewed `WAY-09@ce6bd9c0` included, matches the current binding part |
| `elements/glossary/format_guard.py`, `elements/part-map/format_guard.py` | 0 errors; the map's 4 `unchecked` lines predate the change |
| `gate/run_tests.py product-guidelines` | 61 tests pass; the record gives `pass` to all six `guidelines-check-*` invariants (form 10, carrier 6, reference-target 5, stale-reference 5, code-path 4, colour-pair 2 lines) |
| `python -B -m unittest installation.test_styleguide_installation` | 3 tests pass |
| `product-guidelines/form_check.py` on the-way itself, with and without `--merge-onto 96623ed` | exit 0, note "the repository holds no guidelines/"; records `pass` for `guidelines-form/1` and `guidelines-reference-current/1` respectively |

Frequency: the brief asks how often the problems the change answers have occurred. It cannot be
measured from this repository: no product pinned to the-way keeps a `guidelines/` directory in
it, and no run record or transcript was in scope. WAY-184's rationale says itself that the way of
working "has not yet been tried on a product" (`foundations/decisions.md:6082`), and WAY-191's
rationale names "the faults of focus seen in the first trial" (`foundations/decisions.md:6333`)
without a record a reader of the repository can open.

## Observations

Weights: **medium** — would mislead an agent or human or leaves two sources that drift; **low** —
a wording, a corner, or a cost worth knowing. Nothing found is **high**: no entry contradicts the
code in a way a merge would let through unseen, and no invariant test passes on a broken check.

### A1 — medium — WAY-170 and WAY-192 reject what the installer's guidance now does

Checked: contradiction between the entries and the installer that implements them.

Evidence:
- `installation/install.py:176-180` adds to every product's `AGENTS.md` block: "Where this
  repository holds `guidelines/`, run `python -B .the-way/product-guidelines/form_check.py` and
  `python -B .the-way/product-guidelines/form_check.py --merge-onto <main commit>` before every
  merge." `installation/README.md:58` and `installation/test_styleguide_installation.py:16-21`
  fix that sentence.
- WAY-170's binding sentences (`foundations/decisions.md:5573-5578`): the invariants' methods
  run the script "so the gate runs it with the other checks a change calls for"; its *violates*
  (`:5589-5590`): "a product's instruction file names a command of its own for checking
  guidelines, beside the gate"; its *Rejected* (`:5600-5602`): "a command named in the product's
  instructions beside the gate — of two commands an agent runs one (WAY-16)".
- WAY-192's rationale (`foundations/decisions.md:6362-6366`): "the gate runs that invariant, so
  the instruction names no command of its own (WAY-16)".
- WAY-16's *violates* (`foundations/decisions.md:506-507`): "the instructions for agents list
  test and lint commands of their own".

The block's commands are the-way's, not the product's, and the same block already says that
nothing runs the checks automatically — the sentence exists because WAY-170's second sentence
(a product holds the two invariants) is verified at level 2 only, so nothing mechanical runs the
form check in a product that writes guidelines and no invariant. Still, a reader holding
`AGENTS.md` beside WAY-170 reads a breach of the decision's own *violates* example, and when a
product gate exists the sentence has to leave with nothing reminding anyone (WAY-37 catches
only entries that wait).

What would have to change: write the exception into the binding sentences of WAY-170 (WAY-30:
"an exception foreseen in advance is written into the binding sentences"), such as "until the
product's gate runs the invariants' methods, the block the installer writes names the script's
two commands", and name in WAY-170's *Review when* the state that ends it; or take the sentence
out of the installer and accept that today nothing runs the check in a product.

### A2 — medium — WAY-175 and WAY-176–182, WAY-192 settle the same content twice, with no relation

Checked: duplicated settlements between the new entries; relations.

Evidence: WAY-175's binding sentences (`foundations/decisions.md:5773-5811`) state, as what
the-way takes, "a background always paired with the text on it", "the states default, hover,
visible focus, disabled, error, empty and loading of each shared control, each shown or marked
as not applying with its reason", "a page showing the components in every state", "the order of
a plan for a change to a user interface, as an example", "a fault of one screen fixed in its
component", "every value kept with where it comes from", "an instruction file that points to
the styleguide and forbids values written in place of design tokens". The same content binds
again in WAY-176 (`:5837-5845`), WAY-177 (`:5877-5881`), WAY-178 (`:5905-5908`), WAY-180
(`:5958-5961`), WAY-181 (`:5984-5986`), WAY-182 (`:6010-6012`) and WAY-192 (`:6338-6342`).
None of those derives from WAY-175; WAY-176–182 derive from WAY-173, WAY-192 from WAY-128,
WAY-129 and WAY-133.

Consequence: a change to the list of states, or dropping the page of every state, must be made
in two binding parts, and nothing links them; WAY-175's fingerprint changes with any of them,
flagging nothing, since nothing carries it. WAY-19 moves a sentence answered in passing to the
decision that answers the question.

What would have to change: WAY-175 names each piece taken at the level of the decision that
carries it ("the pairing of a background with its text (WAY-176)") without restating its
content, or WAY-176–182 and WAY-192 add `derives from WAY-175@…` so that a change of what is
taken reaches them. Either way one of the two copies of each list stops being binding text.

### A3 — medium — WAY-175's claims about the outside skills cannot be checked, and carry no source

Checked: source fidelity of every substantive claim; *Based on*.

Evidence: WAY-175 (`foundations/decisions.md:5773-5811`) states in its binding sentences what
"a course's lesson", its skill `10x-ui`, and the skills `om-ux-setup` and `om-ux-shape` "of the
Open Mercato collection" contain and lack — commands, folders, lists of tools, a scoring rubric,
a refusal to work on a screen that does not exist. *Based on* reads `none` (`:5815`). The
course is unnamed, no edition, version, address or date read is given, and no passage is
quoted. The repository holds nothing that lets a reader verify one of these claims. By contrast
WAY-125 (`foundations/decisions.md:3685-3695`), which also adopts outside skills, records in
*Based on* the observation: version, path read, tool, platform, date and a passage from each
skill.

WAY-27 lets an entry describe what was seen in a source its readers cannot reach, and WAY-175
does describe; but the template of a decision has *Based on* quote "every citation with its
source, given as an environment fact's source is given (WAY-80)"
(`elements/decisions/template.md:48-50`), and WAY-100 wants later work to "distinguish [an
adopted piece] from a resemblance", which needs the reader to know what was read.

What would have to change: *Based on* carries an observation in the form WAY-125 uses — the
source's name, version or date, where it was read and the passages that show each piece taken
and each left — or, where the source is not reachable, *Origin* says so and the entry names
what cannot be re-read. I could verify none of the claims and do not claim any is wrong.

### A4 — medium — WAY-168's second sentence leaves a rule naming only an invariant undecided

Checked: whether the entry and the code agree; template conformance of the binding sentences.

Evidence: WAY-168 (`foundations/decisions.md:5489-5493`): first sentence — a binding rule
"names by identifier the decision of the product's log that carries its choice and each
invariant that checks it"; second sentence — "What a product's guidelines hold that names
neither such a decision nor an invariant is an example, not a rule." Read literally, text that
names an invariant and no decision is neither covered by the first sentence nor an example by
the second. The code decides it: `product-guidelines/form_check.py:756-759` reports a rule
naming no decision whatever its *Invariant* holds, and the test
`product-guidelines/test_form_check_invariants.py:511-513` ("a styleguide's rule naming an
invariant only") expects the error. WAY-168's *violates* (`:5507`) agrees with the code.

What would have to change: the second sentence reads "What a product's guidelines hold that
names no such decision is an example, not a rule", so that the sentence and the check agree
and the fingerprint covers the rule the check keeps.

### A5 — medium — the glossary definition of "guidelines" carries a rule, and the term is plural

Checked: glossary template conformance of the new entry.

Evidence: `foundations/glossary.md:107`: "Guidelines are text a product keeps outside its
foundation that tells agents what to do and how in a discipline of work on the product." The
glossary template (`elements/glossary/template.md:141-144`, WAY-96): "The definition says what
the word means, never a rule about the thing it names … A definition carries a rule when it
holds something the decision or invariant setting it could change while the word went on naming
the same thing." Where guidelines stand is WAY-167's choice (`foundations/decisions.md:5441`),
and WAY-167's *Rejected* (`:5476-5477`) weighed "guidelines as a sixth element of the
foundation" — the word would name the same thing under that rejected option. "Outside its
foundation" is therefore a rule in the definition.

The heading is the plural "guidelines"; the template asks for "a noun in the singular"
(`elements/glossary/template.md:41-43`, a rule still waiting for its decision), and the glossary
already holds "mechanics", so the plural has a precedent and is low on its own.

What would have to change: "Guidelines are text that tells agents what to do and how in a
discipline of work on a product." The rule stays in WAY-167, which the template's first
paragraph already cites.

### A6 — medium — WAY-183 gives "user interface" a meaning of its own without a glossary entry

Checked: glossary terms used in a meaning the glossary does not give; words that need an
entry (WAY-95).

Evidence: WAY-183 (`foundations/decisions.md:6037-6039`): "A product whose users reach it only
through an API or a terminal has no user interface in this sense and gets no styleguide." A
reader of the field would call a terminal's prompts and output a user interface; the binding
sentence says "in this sense" because it means something narrower, and WAY-167 (`:5441-5445`),
WAY-184, WAY-185 and the skill (`product-guidelines/styleguide/SKILL.md:101-104`) rest on that
narrower sense. The glossary template (`elements/glossary/template.md:65-68`): a word takes an
entry when a binding sentence uses it in a meaning a reader of the field would not give it,
and "Where a binding sentence says what a term is, the entry takes that" (`:96-98`).

What would have to change: an entry "user interface" in `foundations/glossary.md` (for
instance: "A user interface is what of a product a person uses by looking at screens it
draws") and WAY-183's sentence without "in this sense"; or WAY-183 reworded to the word it
means, such as "screens".

### A7 — low — "part" and "entry" used in other meanings in the styleguide template and skill

Checked: glossary terms used in a meaning the glossary does not give.

Evidence:
- `product-guidelines/styleguide/template.md:73-75`: "## What each part carries — Each part
  below is marked as a rule or an example"; `product-guidelines/styleguide/SKILL.md:190`: "the
  invariant its entry under 'What each part carries' names". The glossary gives "part" to a
  piece of a product (`foundations/glossary.md:149`) and "entry" to text of a foundation file
  (`:65`); the same template, at line 175, lists `part` and `entry` among the words a role must
  not be named after because the-way's glossary holds them.
- `product-guidelines/styleguide/SKILL.md:53` and `product-guidelines/styleguide/template.md:186`:
  "the exact address of the source and the entry in it the value is read from" — "entry" for a
  line of a theme or catalogue.

These files are not among those the glossary guard searches (`elements/glossary/template.md:150-157`),
so no check reports it, but an agent reads them beside the foundation, which is what WAY-104's
rationale protects.

What would have to change: "What each section carries" / "Each piece below"; "the item of the
source the value is read from".

### A8 — low — "newest edition published" of WCAG can be read as a draft

Checked: source fidelity of the claims about WCAG.

Evidence: WAY-191 (`foundations/decisions.md:6302-6306`): "the newest edition published when
the decision is written, named by its number as the W3C's page gives it at that time, at level
AA"; `product-guidelines/styleguide/SKILL.md:181-183` repeats it. The W3C publishes Working
Drafts as well as Recommendations; a draft of the next major version of WCAG is published, and
its drafts do not grade conformance by levels A/AA/AAA. An agent following the sentence
literally could name a draft and then find no "level AA" to adopt.

The rest of the WCAG claims hold against the catalogue as commonly read: success criteria of
contrast and of visible focus exist at level AA, and WAY-86's own example
(`foundations/decisions.md:2468-2469`) adopts WCAG with edition, level AA and screens, which
WAY-191 follows.

What would have to change: "the newest edition that is a W3C Recommendation when the decision
is written".

### A9 — low — "the contrast WCAG sets" is several thresholds; a script over token values alone cannot pick

Checked: whether the rule would act in the cases it targets; what the product's invariant needs.

Evidence: `product-guidelines/styleguide/template.md:114-118`: "Every pair of a background and
the text on it reaches the contrast WCAG sets, computed from the values of the file of design
tokens"; WAY-189 (`foundations/decisions.md:6231-6236`) binds the same. The catalogue sets one
ratio for ordinary text and a lower one for large text, and another criterion for non-text
parts of controls; which applies depends on where a pair is used, which the file of design
tokens does not say. The rule leaves the threshold to the product's decision adopting WCAG,
which WAY-60 allows, but neither the template nor the skill's step 4
(`product-guidelines/styleguide/SKILL.md:176-186`) asks the human which criteria and which
threshold the script applies to every pair.

What would have to change: the skill's accessibility step names, among the facts it proposes,
the criterion each invariant takes its condition from and the one ratio the script holds every
pair to (the stricter one, where text size is unknown), as a question with a recommendation.

### A10 — low — `guidelines-check-carrier` says "no decision of the log"; the check accepts any number with the log's prefix

Checked: whether the invariant test could pass while the sentence is false.

Evidence: `foundations/invariants.md:2165`: "reports as an error every rule … that names no
decision of the log". `product-guidelines/form_check.py:445-451` (`Foundation.decision`) takes
any `PREFIX-NN` with the log's prefix, whether the log holds it or not, and `:756-759` reports
only when nothing of that form stands in *Decision*. A rule whose *Decision* is `ABC-09@0123abcd`
passes the carrier check; the run still fails, but through `check_references`
(`:947-950`), recorded under `guidelines-reference-current`, not under `guidelines-form`. No
test in `product-guidelines/test_form_check_invariants.py:505-559` covers a rule naming only a
decision the log does not hold, so the tests pass with the sentence false in that corner.

What would have to change: the sentence reads "names no decision number with the log's prefix
followed by `@`" (what the check decides), or the check looks the number up in the log and a
test breaks it. Low: the gate fails either way, under another invariant.

### A11 — low — `guidelines-reference-current`'s *Part* in the-way leaves out the parts the template itself names

Checked: *Part* fields against WAY-62 (who can make the sentence false).

Evidence: `foundations/invariants.md:2149`: `Part: product-guidelines · decisions · invariants`;
`product-guidelines/template.md:173-177` reasons that in a product the part holding
`guidelines/**`, the foundation and the pinned the-way are named, and that in the-way the field
"reads `product-guidelines · decisions · invariants`". In the-way, `guidelines/**` would belong
to `agent-instructions` by WAY-167 (`foundations/decisions.md:5445-5447`), and `relation-model`
is what changes how a fingerprint is read, which the template gives as the reason for naming
the part holding the pin. The sentence is vacuous in the-way today (no `guidelines/`), so
nothing breaks; WAY-62 says a writer in doubt names more.

What would have to change: add `agent-instructions · relation-model`, or state in the template
why they are left out in the-way.

### A12 — low — the product's copies read `Derives from: none` while the-way's decisions carry them

Checked: links of the product-side invariants against WAY-17, WAY-60 and WAY-71.

Evidence: `product-guidelines/template.md:143-145`: "A product's copy reads `Derives from:
none`, since no decision of the product's log carries it; its sentence comes from the decisions
of the-way named above." The invariants template (`elements/invariants/template.md:132-138`)
lets an entry link to "a decision of the-way at the commit the product pins" that holds its
condition, and WAY-71 reads `none` as "nothing is there". What protects the copy is the version
the form check cites: a reworded sentence in the-way leaves the product's `/1` entry with no
verdict once the pin moves. The template says this (`:134-138`). Whether a product's invariants
guard can resolve `WAY-170@c1b230d2` across the pin is not shown anywhere I could read, so
`none` may be the only form that passes the guard.

What would have to change: nothing, if the product guard cannot resolve a the-way number; else
the copies carry `WAY-170@… · WAY-171@…` and `WAY-169@…`, and the template says which.

### A13 — low — the script and its tests point to a "spec" the repository does not hold

Checked: WAY-27 (nothing points to a source readers cannot reach; *Scope* now names
`product-guidelines`).

Evidence: `product-guidelines/form_check.py:32`, `:45`, `:48`, `:488` cite "spec §5.3, items
1–6 and 5a", "spec §3.2"; `product-guidelines/test_form_check.py:312`, `:354`, `:387`, `:408`,
`:466`, `:482` cite "spec §5.1", "§5.2", "finding 15". `git ls-files` lists no spec, and the
cycle's `.runs/` is ignored by git.

What would have to change: the pointers name the invariant or decision that holds the rule
(`guidelines-form`, `guidelines-reference-current`, WAY-169, WAY-171) or are dropped.

### A14 — low — WAY-172's *Review when* names a breach, not a prediction

Checked: template conformance (WAY-24: *Review when* is "a state of the world or the product
that someone is waiting for" that the decision rests on).

Evidence: `foundations/decisions.md:5687-5688`: "a merged change of a product that pins the-way
uses, on a screen, a meaning that no decision of the product's log carries · check by:
2026-12-31". That state is the decision being broken, not the prediction the decision rests on
(that approval before the code saves rework at the merge).

What would have to change: *Review when* names the prediction — for instance, that a styleguide
task of a product has gone through the cycle with every meaning settled before its code — or
reads `none`.

### A15 — low — WAY-186 sends every refresh or extension through fresh research and a critique

Checked: error when applied too widely; cost of running.

Evidence: WAY-186 (`foundations/decisions.md:6120-6126`): the skill "researches again whenever a
styleguide is refreshed or extended"; `product-guidelines/styleguide/SKILL.md:120-135`: at every
refresh or extension, split the research into questions, one fresh agent each, a critique, and
"Where no fresh agent can run, the research does not go on: stop". An extension that adds one
role to an existing table would run the whole starting research again. The rationale
(`:6150-6151`) gives the reason — recommendations move — but sets no proportion.

What would have to change: bind the research at a refresh or extension to the matters the
change touches ("the questions the extension raises"), leaving the full research to a refresh
the human asks for.

### A16 — low — the form check does not read the title line, and lets a rule carry extra fields

Checked: the implementation against WAY-171 and WAY-168; whether the invariant tests could
pass while the sentence is false (they cannot: neither sentence claims these).

Evidence: `product-guidelines/form_check.py:299-312` (`parse_form`) reads `## `, `### `, field
lines and table rows of the fenced form; the line `# <Discipline> guidelines — <what they
cover>` (`product-guidelines/template.md:35`) is not read, so a file with no title or another
title passes. `check_rules` (`:752-755`) checks the order and presence of the template's fields
and ignores others, so a rule holding `- **Why:** …` passes, while the template says "A rule
carries no rationale and no rejected options" (`product-guidelines/template.md:73-74`, WAY-168).
Neither `guidelines-form` nor `guidelines-check-form` claims either, so no test is wrong.

What would have to change: either the sentences stay as they are and the template says the
title and a rule's other fields are not checked, or the check reports a title off the form and a
field the template does not give a rule.

## Checks that found no concern

- **Template conformance of every new and changed entry.** All four guards report 0 errors on
  the branch; the decisions guard's errors with `--base/--merge-onto` are the 27 placeholders
  and the edits in place of WAY-09, WAY-27 and WAY-38, which `agent-instructions/README.md:20-24`
  allows before `main`. WAY-09 keeps its meaning but its binding sentences changed, so resetting
  its *Approved by* to the placeholder (`foundations/decisions.md:294`) is the renewed acceptance
  WAY-07 asks for; WAY-27 and WAY-38 change only *Scope*, and keep their approvals.
- **Fingerprints.** Every `derives from` / `narrows` fingerprint in WAY-167–192 and every
  `Derives from` fingerprint of the eight new invariants matches the current binding part (the
  invariants guard with `--merge-onto` reports none stale; the decisions guard reports none).
  The six renewed `WAY-09@ce6bd9c0` links are the only existing links WAY-09's edit touched.
- **Level 1 verification against *Derives from*.** WAY-168, WAY-188 and WAY-189 name
  `guidelines-check-carrier`, which derives from all three; WAY-169 names the three reference
  invariants, which derive from it; WAY-170 and WAY-171 name `guidelines-form` and
  `guidelines-check-form`, which derive from both, and WAY-170 alone names
  `guidelines-check-code-path`, which derives from it alone; WAY-176 names
  `guidelines-check-colour-pair`. The guard's `verification-invariant-derivation` passed.
- **Narrowing.** WAY-172 and WAY-174 each narrow WAY-114 in areas they state (new or changed
  meanings of guidelines; the questions the styleguide skill asks), and their accounts of
  WAY-114 are faithful to `foundations/decisions.md:3231-3235`. WAY-188 narrows WAY-168 and
  states its area. No two decisions narrow each other.
- **Citations checked and found faithful:** WAY-30 (`:871-878`) for WAY-172; WAY-108
  (`:3058-3060`) for WAY-171's language rule; WAY-122 (`:3531-3532`) for WAY-186's critique;
  WAY-86 (`:2456-2461`) for WAY-191 and the skill's accessibility step; WAY-128, WAY-129 and
  WAY-133 (`:3835-3842`, `:3877-3880`, `:4013-4018`) for WAY-192; WAY-130 (`:3905-3906`) for
  WAY-168's rationale; WAY-104 (`:2903-2910`) for WAY-176's qualifier and for leaving `surface`
  out; WAY-125 (`:3676-3677`) for the blocked draft request and for the skill's "no
  Superpowers method" line; WAY-100 (`:2802-2804`) for naming each piece taken.
- **Claims about how tools read files.** The note in `product-guidelines/template.md:115-130`
  matches `instruction-files/check_instructions.py`: a backtick span is taken for a path by
  `looks_like_path` (`:368-376`), a missing one is a `dead-path` warning (`:506`); an `@`
  followed by a word holding `.` or `/` is an import (`:35-36`, `:60`, `:511-532`); emphasis
  is the capitalised words of `EMPHASIS` (`:56`) and a second emphasised line warns
  (`:533-537`). The fingerprint description in `product-guidelines/template.md:94-96` matches
  WAY-02 (`foundations/decisions.md:45-48`).
- **Invariant sentences against WAY-60–WAY-69.** Each is one sentence; none names a branch;
  `guidelines-reference-current` names `{merge-onto}` as a gate value and its method takes it;
  the `guidelines-check-*` sentences name `"{merge-onto}"` in quotation marks as what the check
  is given, as the template asks for a sentence about a check. Methods begin with the program,
  name no commit, and the test runner is the method of the sentences about the check while the
  form check on the real repository is the method of the sentences about the data (WAY-61).
  *Part* fields name parts of the map, no flow or surface; `guidelines-form` names `every` with
  the reason given in the template. The check invariants' *Part* lists the parts whose code the
  form check borrows (`product-guidelines/form_check.py:155-170`).
- **Tests against WAY-69.** Expected fingerprints and fragments are literals
  (`product-guidelines/test_form_check_invariants.py:39-67`); `with_line` and `replaced`
  (`:229-243`) fail loudly when the fixture moves; every test cites its invariant inside the
  method body; the control tests (valid fixture, a drop that passes, a tracked path) separate a
  fixture's own error from a break's. Each break the tests make is one a product could write.
- **Reference detection.** The two forms of a reference (`product-guidelines/template.md:88-93`)
  match `REFERENCE_TOKEN`, `IDENTIFIER` and `FINGERPRINT` (`product-guidelines/form_check.py:131-135`)
  and `references()` (`:486-503`); versioned package names and bare identifiers are not
  references (`:623-632`); fenced code is skipped and inline code is not, as WAY-169 says
  "outside fenced code". Both regular expressions are bounded as the docstring claims.
- **Part map.** The `product-guidelines` part (`foundations/part_map.md:261-279`) has every
  field; each failure mode names a kind of damage, a degree on the scale and a detection that
  is an existing invariant or "not detected"; the trust boundary is the script that reads a
  product's files; the surface `guidelines-form-check-command` (`:355-360`) follows the form of
  the other guards' surfaces; the flow `skills-reach-the-way-sessions` (`:291-301`) and the
  dependencies of `agent-instructions` and `installation` take in the new part. WAY-09's list
  of directories (`foundations/decisions.md:236-262`) matches what `product-guidelines/` holds.
- **Code against the entries.** `check_parts` (`product-guidelines/form_check.py:837-878`)
  enforces WAY-167's file names, including that only the styleguide names a part; `check_roles`
  (`:774-834`) enforces WAY-176's pair and the kinds the template lists; `check_paths` and
  `refused` (`:881-928`) enforce WAY-170's and WAY-171's rule on `## Where in code`;
  `check_drop` (`:716-722`) enforces WAY-171's `none —` marker; the read of untrusted files
  (`:198-255`) does what the docstring and the part's trust boundary promise. The installer
  registers the skill (`installation/install.py:39`) and its test checks the entry points byte
  for byte and runs both commands in a product.
- **Skill against the entries and the files it names.** The steps of `refine-task` it hands to
  exist (`project-level/task/skill/SKILL.md:61-164`: steps 1–6), the task template holds *To do*,
  *Questions to settle*, *Context* and *Settlements to record*
  (`project-level/task/template.md:24-56`), and the sections of `elements/common/way_of_working.md`
  it names exist (`:12`, `:20`, `:60`). Step 4's "How to show" follows WAY-174; step 1 follows
  WAY-183 and WAY-185; step 3 follows WAY-187; the accessibility step follows WAY-86 and WAY-191
  but for A8 and A9.
- **README and installation README** describe what the change adds and nothing more
  (`README.md:81-83`, `:88-90`; `installation/README.md:56-58`, `:131-132`).
- **Generated entry points** (glance): the 32 files add `maintain-styleguide` to each sibling
  list; the new entry point names its source skill and the product rule; the installer's test
  expects 15 skills in each of two directories.
- **Cheaper ways.** No existing rule, template or check covers a product's guidelines: the five
  elements are closed (WAY-04), the instruction-files check reads a guidelines file only once an
  instruction file names it and checks none of this form, and the glossary and decision guards
  read `foundations/` alone. The form check borrows the guards' parsers rather than parsing the
  log again, which is the cheaper way available.

## What of the change can be cut

Nothing has to be cut for the change to hold together. One entry can be cut without loss:
**WAY-181** (`foundations/decisions.md:5982-6006`) binds only that the template carries the
plan order "among its examples, never as a rule", and WAY-175's binding sentences already say
the-way takes "the order of a plan for a change to a user interface, as an example"
(`:5785`); an example cites no decision under WAY-168 and WAY-171, so the template's "(WAY-181)"
can read "(WAY-175)". **WAY-179** stands on the same footing, except that its rationale gives
the reason no check can decide a mockup's use, which WAY-175 does not; cutting it costs that
reason. Cutting either is the author's call under A2, which asks the opposite question: whether
WAY-175 should stop restating what the later decisions carry.

The note in `product-guidelines/template.md:115-130` cites no decision and says so; it is
knowledge an author needs when a guidelines file becomes an instruction file, and I would keep
it.
