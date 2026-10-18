# Independent assessment — agent's way to the running product in the technology step

Assessed range: `77c8a8b..9587b0d` in `C:/Storage/repos/the-way-wt/agent-path-technology-step-assess`
(detached at `9587b0d`). Read whole: the diff; WAY-121, WAY-165, WAY-166 and the new glossary term;
WAY-100, WAY-106, WAY-116, WAY-122, WAY-123, WAY-137, WAY-138, WAY-139, WAY-143; WAY-05, WAY-07,
WAY-08, WAY-10, WAY-19, WAY-24, WAY-25, WAY-30, WAY-33 for the rules applied; invariant
`project-technology-record/1`; `elements/decisions/template.md`; `elements/glossary/template.md`;
`elements/common/rules.md`; `foundations/glossary.md`; the `project-level` entry of
`foundations/part_map.md`; `project-level/readiness_check.py`; `project-level/definition_template.md`
and `project-level/technology/SKILL.md` at `9587b0d`; the resume clause of
`project-level/skill/SKILL.md:55-72`; `agent-instructions/README.md`.

Disclosure: to list the commits of the range I ran `git log` with messages, which carry the author's
account of the change. I read them before realising what they hold. The observations below rest on
the diff and the files, and every claim is anchored in them, not in those messages.

Runs (stdout only; nothing written to the worktree): decisions format guard `--base none
--merge-onto none`: 0 errors, 8 warnings (five pre-existing passed check-by dates on WAY-03/21/52/55/69;
three `merge of <request link>` placeholders at `foundations/decisions.md:3470`, `:5374`, `:5414`),
5 unchecked. Glossary format guard, same options: 0 errors, 0 warnings, 5 unchecked; `--uses
"agent's way to the running product"`: 7 uses, all in `foundations/decisions.md`.
`gate/run_tests.py project-level`: 250 OK. `gate/run_tests.py gate`: 98 OK. Fingerprints recomputed
with `relation-model/fingerprint.py`: WAY-121 `ed19d693`, WAY-123 `f3b45293`, WAY-100 `e7a74a18`,
WAY-106 `63eddf70`, WAY-116 `afbcd2fa` — every reference in the diff matches; WAY-137's current
fingerprint is `86b2a30d` (named in A1).

Weights: **medium** — should be settled before the merge; **low** — worth a settlement line, the
change stands without it; **no concern** — checked, nothing found.

---

## A1 — WAY-166 and WAY-137 can be read as colliding, with no precedence recorded (medium)

**Checked:** whether the two decisions both apply to one option and pull opposite ways (WAY-25).

**Evidence:**
- `foundations/decisions.md:4219-4221` (WAY-137): "For a place to run, how well an agent works with
  an option decides nothing else: it leaves no option out of the comparison and is weighed against
  no consequence for the product."
- `foundations/decisions.md:5395-5398` (WAY-166): "In a choice of an agent's way to the running
  product, whether an agent can use an option is a consequence for the product".
- `foundations/decisions.md:5353-5354` (WAY-165): "a dedicated test environment that persists" is
  an option of the development data choice.
- `foundations/decisions.md:5403`: WAY-166 relates only `derives from WAY-121 · narrows WAY-123`.
- `foundations/decisions.md:5420-5422`: the distinction from WAY-137 stands in *Rationale* only.

A dedicated test environment that persists is somewhere the product runs and is deployed to. For
that option, "can an agent use it" (deploy from a terminal, reset its data by a script) is the
property WAY-137 calls "how well an agent works with" a place to run and keeps out of the
consequences; WAY-166 makes the same property a consequence. Both decisions apply to that one option
by their own words. The rationale of WAY-166 argues they differ in purpose, but WAY-25 and the
template (`elements/decisions/template.md:173-179`) put precedence in *Relations* and in the binding
sentence, not in prose, and an agent meeting the collision must stop.

**What would change:** one of —
(a) WAY-166 gains `narrows WAY-137@86b2a30d`; its binding sentence already names its area ("In a
choice of an agent's way to the running product"), which is what WAY-25 asks of the prevailing
decision. No mutual narrowing arises (WAY-137 does not narrow WAY-166), so `narrows-pairs` holds.
(b) Or the binding sentence of WAY-166 adds "even where the option is a place the product runs",
which still leaves the relation unrecorded.
(a) is cheaper and is the form the foundation uses.

**If left:** the first comparison of development data that includes a persistent environment hands
an agent two applicable rules; by WAY-25 it stops and asks, and a human records the precedence then
— the same edit, made later and in the middle of a project.

## A2 — Overlap between the logs matter and WAY-139's deployment skill item (low)

**Checked:** whether the new entries duplicate a settlement elsewhere or leave the join unsaid.

**Evidence:** `foundations/decisions.md:4306-4309` (WAY-139): the deployment skill covers "how to
read the logs". `foundations/decisions.md:5348-5349` (WAY-165): the logs ask "where the record of
what the running product does goes and how an agent reads it". `foundations/decisions.md:3502-3504`
(WAY-121 *Rejected*) says why the deployment skill alone does not serve, but no sentence says how the
two answers relate once both exist for a deployed product.

**What would change:** nothing is required. If the author wants the join, one clause in WAY-139 or
WAY-165 — the deployment skill's item on logs follows the decision of the logs where one stands —
would do; it changes WAY-139's or WAY-165's fingerprint.

**If left:** two places may answer how logs are read, for a product that is deployed; they can
drift. The cost shows only in a product with both, and `refine-task` would meet the drift when it
checks the deployment skill.

## A3 — Frequency of the problem cannot be measured from the repository (low, by the skill's rule)

**Checked:** how often an agent in a task cycle lacked a way to the running product.

**Evidence:** the worktree holds no project definition (`grep -rl "^## Technology"` finds only the
template), no cycle record (the two latest commits before the range removed cycle evidence from the
tree), and no run log. The rationale's claim at `foundations/decisions.md:3477-3479` ("an agent with
no way to the running product either leaves that check undone or improvises its access") is the
motivating case and is not evidenced in the repository. Session transcripts were out of bounds.

**What would change:** nothing in the entries. The author's settlement can say where the recorded
case lives (a cycle record outside the tree, a conversation), so a reader of the assessment knows the
rule rests on a case and not on an estimate.

## A4 — Source fidelity: the borrowed lesson is not in the repository (low)

**Checked:** every substantive claim against a source in the worktree.

**Evidence:** `foundations/decisions.md:3485-3488` names the lesson "Towards Autonomous Product
Development", what is taken (logs, interface, development data) and what is left out (the hard limit
on the production database and root access). The lesson is not in the worktree; *Origin* reads
`none` (`:3469`). I cannot confirm that the lesson says this. WAY-100 asks only that the decision
name what is adopted, where it applies and why — the binding sentence and rationale do that, so
WAY-100 is met. WAY-143 does the same with "the practice of vertical slices" and `Origin: none`, so
this follows precedent.

**What would change:** nothing is required. A pointer to the lesson in *Origin* (a document, which
is what *Origin* holds per `elements/decisions/template.md:260-263`) would let a later reader check
what was taken and left; its absence leaves "leaves out the lesson's hard limit" unverifiable.

Every other substantive claim in the three entries and the template is a settlement, not a report of
a source, and matches its source entry: WAY-123's list of consequences (`:3568-3569`) is what WAY-166
extends; WAY-137's tie rule is restated unchanged in SKILL.md step 2.5 (`SKILL.md:122-124`);
WAY-122's research rule is untouched.

## A5 — Settled matters are omitted, not listed `held by`: an asymmetry the step has to carry (low)

**Checked:** whether the exception would act in the cases it targets and what it asks of the agent.

**Evidence:** `foundations/decisions.md:3438-3439`: the step "lists as a choice of its own each matter
that no decision of the foundation settles"; `project-level/definition_template.md:172-173`: "a matter
a decision of the foundation already settles for that behaviour is not listed". Every other choice
the foundation holds is listed `— held by:` (`definition_template.md:190, 197-199`). The *Review
when* of WAY-121 (`:3465-3466`) treats listing a settled matter as a signal.

The design is coherent — the matters are not "choices the project needs" by the rule of belonging,
so they enter only when open — but an agent used to the rest of the list may list a settled matter
`held by` out of consistency, which is harmless to the project yet fires the review condition.

**What would change:** nothing is required. Two ways if the author wants the asymmetry gone: allow a
settled matter to stand `held by` (one clause in WAY-121's exception and the template; then *Review
when* condition 1 loses its object and goes), or keep the omission and accept that the first
condition catches a harmless act as well as the over-listing it is meant for.

**If left:** no project is harmed; the review of 2027-03-31 may record a "condition met" that was
not the signal intended.

## A6 — The third binding sentence of WAY-121 carries a rule that belongs with WAY-165 (low)

**Checked:** whether each settlement sits in the entry that answers its question (WAY-19).

**Evidence:** `foundations/decisions.md:3440-3441`: "even where the product has none of what the
matter names, whose answer then says what an agent uses in its place" — a rule about the content of a
matter's answer, inside WAY-121's rule about which matters are listed. WAY-165 (`:5348-5354`) is the
decision on what each matter asks. The third sentence of WAY-121 is 92 words.

**What would change:** move "whose answer then says what an agent uses in its place" into WAY-165
(as part of what each matter asks), leaving WAY-121's exception to say the matter is listed "even
where the product has none of what the matter names". Cost: WAY-121's fingerprint changes again, so
WAY-122, WAY-123, WAY-166, WAY-165 and `project-technology-record/1` renew it; the template bullets
change accordingly. Not required; the sentence is correct where it stands.

## A7 — SKILL.md step 0 tells history in a rule (low, cuttable)

**Checked:** the skill text as implementation of WAY-121.

**Evidence:** `project-level/technology/SKILL.md:37-41`: "the list may have been written before the
step looked at an agent's way to the running product: first take the look step 1 gives…". The
behaviour (re-look on resume before approval) is right and needed for definitions in flight; the
clause saying why ("may have been written before…") is a chronicle of the process's own change. The
repository has precedent for such clauses (`project-level/skill/SKILL.md:64-70`, a definition with no
Technology section), so this follows a convention rather than breaking one.

**What would change:** the bullet can read "Where it holds a list, first take the look step 1 gives
at the logs, the interface and the development data, add each matter it finds missing as an item
ending `— open`, and, where it adds one, show the list again as step 1 does before going on
(WAY-121). A definition the gate has approved does not come back to this step for these matters."
Behaviour unchanged. Cuttable, not required.

## A8 — SKILL.md step 2.5 restates WAY-137's scope a second time (low, cuttable)

**Evidence:** `project-level/technology/SKILL.md:124`: "that tie rule serves a place to run alone".
The template already carries WAY-137's binding sentence whole (`definition_template.md:229-234`),
and WAY-137 itself says "For a place to run, how well an agent works with an option decides nothing
else". The clause repeats what the cited rule says.

**What would change:** the clause can go; the sentence "In a choice of an agent's way to the running
product, the recommendation passes over an option an agent cannot use (WAY-166)" that follows it
carries the distinction. If A1 is settled with `narrows WAY-137`, the clause is also no longer the
only place the two rules are kept apart.

## A9 — The exception acts on the-way's own next project (low, applied as intended)

**Checked:** error when applied too widely.

**Evidence:** `foundations/decisions.md:4489-4490` (WAY-143 complies): "in the-way, a task ends
with a skill a session runs on a real definition" — the-way treats its own skills as its running
product. The exception (`:3436`) triggers "where the project brings behaviour a user sees in the
running product", so the first project definition of the-way written after this change lists the
logs, the interface and the development data of the-way (a session's output, a skill run in a
session, sample definitions), each as a projected decision. That is the design — settled once, found
later — but the author should know it acts here too, and the answers for a process-as-product are
less obvious than for a game or a shop.

**What would change:** nothing; if the-way does not write project definitions for itself, the case
never arises.

## A10 — WAY-165's fixed pair of options beside WAY-122's "no fixed list" (low)

**Evidence:** `foundations/decisions.md:5353-5354`: "Data set up from scratch and a dedicated test
environment that persists are both options of that choice." WAY-122 (`:3508-3510`): options "come
from research of that choice against the project definition, rather than from a fixed list of
bundled stacks". These do not contradict — WAY-122 targets bundles, and WAY-165 names two kinds the
research must not drop, the violates example at `:5368-5370` showing the one it protects — and the
research still finds their concrete form. WAY-165 relates only to WAY-121.

**What would change:** nothing is required. If the author reads the sentence as constraining
WAY-122's research, `derives from WAY-122@b343277a` records it.

---

## Checks that found no concern

- **Template conformance of WAY-121, WAY-165, WAY-166** (`elements/decisions/template.md`): every
  field present; binding sentences count 3, 3 and 1; present tense; no normative or forbidden words;
  *Scope* names parts of the map; *Relations* use the two allowed types with fingerprints that
  recompute to the values written; *Verification* level 1 of WAY-121 names an invariant whose
  *Derives from* names WAY-121 back; *Review when* of WAY-121 is an observable state with a date;
  *Approved by* uses the template's second form (`<who>, merge of <request URL>`) as a placeholder
  that the guard warns on, the same as the other two pre-merge entries at this commit, to be filled
  at the request. The decisions guard reports 0 errors.
- **Edit of WAY-121 in place** conforms to WAY-07 and `agent-instructions/README.md:20-23`: no main
  branch, meaning changed, approval renewed by the merge; the first and last old sentences were merged
  without loss (old `:3429-3433` versus new `:3429-3433`).
- **Fingerprint renewals** in WAY-122 (`:3526`), WAY-123 (`:3578`) and `project-technology-record/1`
  (`foundations/invariants.md:2027`): `740c254e → ed19d693`, and the new value is the fingerprint of
  the new binding part. Each dependant still holds against the new wording: WAY-122 and WAY-123
  govern how listed choices are researched and shown, whatever puts them on the list; the invariant
  checks the item form, which the exception reuses.
- **Glossary entry** (`foundations/glossary.md:7-12`): one-sentence definition in the "<term> is
  <genus> that <difference>" form, no normative word, *Avoid* and *Not* `none`, heading in lower
  case and singular, placed alphabetically; the glossary guard reports 0 errors and finds 7 uses in
  binding parts and rationale, so the term meets WAY-95's condition of a use outside the glossary.
  The rules of `elements/common/rules.md:27-29` are kept: the entries use the term, never a paraphrase.
- **Glossary terms used in a meaning the glossary does not give:** `surface` does not occur in the
  diff; `interface` is used in its field meaning (screen, API, terminal), consistent with its other
  uses in the log (`:1407`, `:2898`); `running product` matches its use in the glossary's
  `preparatory task` entry (`glossary.md:156`), `plan/template.md` and `task-cycle/skill/SKILL.md:340`.
  `matter` and `means` carry their ordinary meanings.
- **Rationale and Rejected prose** (WAY-05): none names a file, script, count or what the tools lack
  today; none tells how the decision was reached; nothing binding stands only in prose except the
  WAY-137 distinction named in A1.
- **Duplicated or missing settlements among the new entries:** WAY-121 (which matters, when listed),
  WAY-165 (what each asks), WAY-166 (how usability weighs) are disjoint. What "an agent can use an
  option" means is left to judgment with one example (`:5407-5410`); a human who still chooses an
  unusable option is caught by WAY-121's second review condition (`:3466-3468`). Nothing missing that
  a decision has to hold.
- **Template as implementation** (`definition_template.md:167-183, 224-228`): each new bullet
  restates its decision's binding sentence and cites it; "No definition has to hold these matters"
  (`:173`) follows from WAY-121's exception and its *Rejected* (`:3493-3494`); the markers table is
  reused unchanged.
- **Skill as implementation** (`technology/SKILL.md:56-63, 105-109, 119-126`): step 1 looks after the
  rule of belonging, applies the "no decision settles it for that behaviour" test, and treats a listed
  matter as an ordinary choice; step 2.3 adds the usability line to the consequences; step 2.5 passes
  over the unusable option in the recommendation and leaves WAY-137 to a place to run; the research
  agent in step 2.1 receives the template's Technology section, which now carries WAY-165's questions.
  The frontmatter description is unchanged, so `skill_entry_points.py` needs no run.
- **`project-level/readiness_check.py`:** condition g (`:27-30`, `:241-269`) checks item form, open
  items and `none`; the exception adds ordinary items with the same markers, so no change is needed;
  the part map's failure mode "a technology choice the project needs is missing from the definition's
  list — not detected" (`part_map.md:116-117`) already covers an omitted matter. 250 project-level
  tests and 98 gate tests pass.
- **Other skills that touch the Technology section** (`project-level/skill/SKILL.md:59-70, 122-139`,
  `project-level/plan/skill/SKILL.md:93`, `elements/decisions/skill/SKILL.md:80`): none states a rule
  the change contradicts; `define-project` hands the section to `settle-technology`, whose step 0 now
  takes the look.
- **Contradictions with other current entries:** WAY-106 (writes into the definition only — kept,
  `SKILL.md:24-25`); WAY-116 (projects decisions the human can settle before the breakdown — the
  matters are such decisions); WAY-118 (settled before the gate — kept); WAY-138 (tests the option
  recommended — a listed matter is tested like any choice); WAY-139, WAY-140, WAY-143 agree, with the
  overlap noted in A2. No other collision found.
- **Trigger "where the project brings behaviour a user sees":** an API consumer counts as a user by
  WAY-165's own list of interfaces (`:5350-5351`), so an API-only project is not excluded; a project of
  pure infrastructure is, which is the intent.

## Cut verdict

Nothing of substance can be cut: each of the three decisions answers a question of its own, and
the template and skill text implement them without adding a rule. Two phrases are cuttable without
loss of behaviour — the historical clause in `project-level/technology/SKILL.md:37-38` (A7) and
"that tie rule serves a place to run alone" at `project-level/technology/SKILL.md:124` (A8). One
relation should be added before the merge (A1).

## Summary by weight

- medium: A1
- low: A2, A3, A4, A5, A6, A7, A8, A9, A10
- no concern: 13 checks listed above
