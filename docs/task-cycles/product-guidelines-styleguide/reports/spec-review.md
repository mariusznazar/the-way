# Spec review — product guidelines, with the styleguide as the first guidelines

Step 7 of `task-cycle/skill/SKILL.md`: an independent review of
`.runs/task-cycles/product-guidelines-styleguide/spec.md` by an agent that did not write it.
Worktree `C:/Storage/repos/the-way-wt/product-guidelines-styleguide`, base `96623ed` (`foundations`),
clean when read. Nothing outside this report was written.

## Verdicts

- **Task compliance: not yet compliant — compliant after findings 7, 8 and 9.** Every *To do* item
  (1–11) and every one of the 27 rows has a carrier in the spec (row-to-section check below). Three
  rows are carried with a meaning narrower than the human accepted: row 18 (a rule about what a
  colour means gets an invariant — the role table carries none), row 3 (every reference of a
  guideline stops the merge — only some are checked) and row 2 (anything that names no decision is
  an example — four template sections are neither rule nor example).
- **Design coherence: not coherent as written — one Critical, eleven Important.** The form check's
  verdicts for the product invariants cannot be cited without breaking the-way's own
  `invariant-citation-target` (finding 1); the record the shared report writes drops the checks of
  `guidelines-form` under the given method (2); two sets of invariants do not reach the changes
  that can make them false (3, 4); G5 collides with WAY-114 without `narrows` (10); the skill has
  no form for orchestrated refinement (11). The refinement/cycle split (root C5) is stated well
  enough for a cycle author to write the file, except for where the chosen token values travel (12).

Findings by grade: **Critical 1 · Important 11 · Minor 12.**

All findings open a new thread; none adds to an existing one.

## How the review was done

- Read whole: `task.md`, `spec.md`, `cycle.md` (questions C1–C10), the review playbook,
  `elements/common/way_of_working.md`, `foundations/part_map.md`; `foundations/decisions.md` entries
  WAY-01–05, 07–09, 17–22, 24–38, 44–49, 51–58, 60–65, 68–69, 71–74, 76–86, 93–114, 121–137,
  154–155, 165–166; `foundations/invariants.md:1-210` and the entries named below; glossary
  headings and the entries "repository instruction file", "result", "surface", "verdict".
- Code read: `relation-model/fingerprint.py`, `elements/common/guard_shared.py` whole;
  `elements/decisions/format_guard.py:1-300, 800-1000, 1131-1242`;
  `elements/invariants/format_guard.py:1133-1189, 1400-1650`;
  `instruction-files/check_instructions.py:1-120, 300-610`; `installation/install.py:1-200`;
  `installation/README.md` (moving the pin, the table); `agent-instructions/skill_entry_points.py:1-80`;
  `project-level/task/skill/SKILL.md` whole; `task-cycle/skill/SKILL.md` (blocked draft rule);
  `elements/glossary/format_guard.py:1300-1360`; `gate/run_tests.py` (discovery).
- Outside sources: `C:/Storage/repos/loop2-10x/.claude/skills/10x-ui/SKILL.md:86-220`;
  `om-ux-shape/SKILL.md` at `loop` `715026e` whole; `mapa_pakietu_10x.md` section `## m2l5` whole.
- `reports/foundation-selection.md` used as a map only; `reports/design.md` and the three research
  reports were not read.

### Row-to-section check

| Row | Carrier in the spec | Holds the row's meaning? |
|---|---|---|
| 1 | §1, §2.2, G1 | yes |
| 2 | §3.1, G2 | partly — finding 9 |
| 3 | §3.2, §5.3.5, G3 | partly — finding 8 |
| 4 | §5, G4 | yes |
| 5, 6 | §4 `## Roles`, G7 | yes; reading of *To do* 5 — finding 22 |
| 7 | §4 `## Components and states`, G8 | yes |
| 8, 9, 10, 11, 12 | §4 table, G9–G13 | yes, status of the sections — finding 9 |
| 13, 15 | §2.2, §6.3 step 2, G14, G15 | yes; the word "interface" — finding 5 |
| 14 | §6.3 step 1, G16 | yes |
| 16 | §6.3 step 2, G17 | yes |
| 17 | §6.3 step 3, G18 | yes |
| 18 | §3.1, §5.3.2, §6.3 step 4, G19 | partly — finding 7 |
| 19, 20 | §6.3 step 4, G20, G21 | yes; focus and WCAG — finding 20 |
| 21 | §6.3 step 4, G22 | yes |
| 22 | §6.6, G23 | yes |
| 23 | §6.3 step 4, §6.5, G24 | yes |
| 24 | §7, G5 | yes; relation — finding 10 |
| 25 | §9.2 | yes; the word "domain" — finding 19 |
| 26 | §3.1 (`none —`), G6 | yes; misused for *Derives from* — finding 6 |
| 27 | §6.3 step 4, G5, G24 | yes; relation — finding 10 |

---

## Critical

### 1. The form check cannot cite `guidelines-form/1` and `guidelines-reference-current/1` without breaking the-way's own gate

**Anchor:** `spec.md:145-165`, `spec.md:217-218`, `spec.md:600`; source
`elements/invariants/format_guard.py:1141-1183`, `foundations/invariants.md:1317-1324`
(`invariant-citation-target/1`), `foundations/decisions.md:1897-1899` (WAY-65).

**To paste:** A verdict for `guidelines-form/1` needs a line `# invariant: guidelines-form/1` in
`form_check.py` (WAY-65), and the-way's invariants guard reports every such line in a tracked
non-Markdown file of the-way that names no entry of the-way's `foundations/invariants.md` — which
these two product invariants are not. Which of the two rules gives way?

**Why I raise it:** Root C8 makes the form check, a script of the-way, record verdicts for two
invariants that live only in each product's `foundations/invariants.md`. WAY-65's binding sentence
says "A check cites … each invariant it gives a verdict for as `invariant: <identifier>/<version>`,
and a run records no verdict for an invariant its check does not cite." The precedent is the
decisions guard, which cites `# invariant: log-merge-copies/1` at the function that records it
(`elements/decisions/format_guard.py:824`). So `form_check.py` must carry
`# invariant: guidelines-form/1`. But `check_citations` (`elements/invariants/format_guard.py:1145-1183`)
reads every tracked file of the-way that does not end in `.md`, and for each `invariant:` line whose
identifier is not an entry raises "cites `guidelines-form`, which is not an entry" — the invariant
`invariant-citation-target/1`, *Part* `every`, says "Every `invariant:` line in a check names an
entry of `foundations/invariants.md`." In the-way the file holds no `guidelines-form`. The plan
therefore has two moves, both wrong: cite (the-way's invariants guard fails on its own repository,
and the gate with it), or record without citing (WAY-65 broken, and the-way's next reader of the
record cannot tell which code gave the verdict). This is not an implementation detail: whichever
way is taken changes a decision or the design of C8, and the spec does not choose.

Ways open, with what each costs:

- (a) The-way holds both entries too. In the-way the sentence "every file `guidelines/<name>.md` …"
  is true with no such file; the method (`form_check.py`) runs and passes; the citation resolves;
  products write the same entries with the same sentences, as the template already requires
  (`spec.md:162-165`). Cost: two more entries in the-way, and the template must say a product's
  copies keep the-way's identifiers and sentences. It also settles finding 6 (*Derives from* can
  name G3/G4 in the-way).
- (b) No product invariants: the form check is run as the format guards are, by the installer's
  guidance before a merge (`spec.md:451-453` already adds that sentence), with only the-way's
  `guidelines-check-*` invariants (§9.3) on the script. Cost: rows 3 and 4's "stops the merge"
  then rests on the guidance until products have a gate — the same footing as every format guard
  today.
- (c) A new decision narrowing WAY-65 / `invariant-citation-target` for citations of product
  invariants by the-way's scripts. Cost: a change to a rule of the gate for one script, and the
  invariants guard must learn to tell such citations apart.

Recommendation: (a) — it keeps C8's protection, needs no rule changed, and fixes finding 6 in the
same move. Whichever is taken, §10 needs a test that the-way's invariants guard passes on the
branch with `form_check.py` in place.

---

## Important

### 2. With the method the spec gives, `guidelines-form` gets no verdict at all

**Anchor:** `spec.md:156-157`, `spec.md:213-218`; source `elements/common/guard_shared.py:241-246`,
`elements/decisions/format_guard.py:57-62`.

**To paste:** Both product invariants name one method with `--merge-onto {merge-onto}`, and the
shared report records, when an option is given, only the checks that option selects. The checks of
form (sections, fields, pairs, paths) read the file alone, so a run with `--merge-onto` writes no
line for `guidelines-form/1`, and the gate reads that as no pass (WAY-61).

**Why I raise it:** The spec says the output and record are "the shared report" in "the shared
form" (`spec.md:217-220`). `Report.recorded` (`guard_shared.py:241-246`) returns, when the run was
given any option, `self.selected_by.get(check) in self.options` — a check not mapped to an option is
not recorded. That is deliberate: the decisions guard's invariants of the log alone, such as
`binding-sentence-count`, name a method without options, and `log-merge-copies` a method with
`--merge-onto` (`foundations/invariants.md:50` against `:120`). Example: a product runs
`form_check.py --merge-onto 3f2a… --record .runs/guidelines-form.jsonl`; the record holds lines for
`guidelines-reference-current/1` only; the gate gives `guidelines-form/1` no `pass`, and with
WAY-63 an entry with no verdict is `error`. Fix: either two methods, as the decisions guard has
(`form_check.py --record .runs/guidelines-form.jsonl` for `guidelines-form`, and the `--merge-onto`
run for `guidelines-reference-current`), or say in §5.1 that the form check maps no check to an
option and records every check whatever the options — a departure from the shared semantics that
needs its reason. Also say what `--merge-onto none` records for the same-commit half of
`guidelines-reference-current` (a `pass` beside the merge check's `unchecked`).

### 3. `guidelines-form` names parts that miss the files it points to

**Anchor:** `spec.md:157-159`, `spec.md:132-133`, `spec.md:256-257`; source
`foundations/decisions.md:1789-1793` (WAY-62).

**To paste:** `guidelines-form` fails when a path in `## Where in code` stops being tracked, but its
*Part* names only the agent-directing part and the part holding `foundations/**`; a change that
renames the tokens file touches only the interface's part and never reaches the invariant. Should
the path check's invariant name `every`, or the parts its paths lie in?

**Why I raise it:** WAY-62: "An invariant entry names the parts of the part map where a change can
make its sentence false … A change … reaches an invariant that names `every` or a part the change
touches, or whose method names a file the change alters." The sentence of `guidelines-form` covers
error 6 of §5.3 (a path git does not list). Example in `loop2`: the styleguide points to
`src/browser/tokens.css` (part `browser-view`); a task renames it to `theme.css` and touches only
`browser-view`; the invariant names `agent-workflow` and `product-foundation`, so the gate does not
run it, and the styleguide's pointer to a missing file reaches the main branch — the agent of the
next task follows it to nothing. The same holds for the pin: a pin move that changes the
template's required sections makes `guidelines-form` false through `.the-way`, which `loop2`
happens to give to `agent-workflow` but another product need not. Fix: *Part* `every` for
`guidelines-form` (WAY-62's rationale: "A missing part fails silently, an extra one costs a run,
so doubt names more"), or split the path check into an invariant of its own with `every`.

### 4. The-way's invariants on the form check do not reach changes to the code it loads, and no flow covers it

**Anchor:** `spec.md:224-227`, `spec.md:282-283`, `spec.md:531-533`; source
`foundations/part_map.md:261-269` (`wording-reaches-dependants`).

**To paste:** The form check loads the decisions and invariants guards for `parse_log`,
`merged_log`, `read_rules` and `parse_file`, yet the six `guidelines-check-*` invariants name only
`product-guidelines` (and `relation-model`); a change to `elements/decisions/format_guard.py` that
alters `parse_log` does not reach `guidelines-check-stale-reference`, and with no critical flow
nothing else runs it.

**Why I raise it:** The spec chooses reuse to avoid a second computation (`spec.md:226-227`, WAY-02
*Rejected*), which makes the form check depend on code of three other parts. WAY-62 reaches an
invariant through its *Part* or through a file its method names; the method names
`gate/run_tests.py product-guidelines`. Example: a task changes how `parse_entry` joins wrapped
binding sentences in the decisions guard (part `decisions`); the decisions tests pass; the
fingerprint the form check computes for a product decision now differs from the one in the
guidelines; nothing in that change runs `product-guidelines` tests, so the break surfaces later as
a product's form check flagging every reference for nothing — the failure mode the relation-model
part records ("flags raised for nothing are cleared unread"). The analogous flow for decision
relations, `wording-reaches-dependants`, names `relation-model · decisions · gate`. The spec's
autonomous "no new critical flow" (`spec.md:282-283`) is defensible only if the *Part* fields do
the reaching. Fix: name `decisions · invariants · elements-common · relation-model` beside
`product-guidelines` in the *Part* of every `guidelines-check-*` whose code path runs through those
modules; or add the flow at the price of one gate test.

### 5. "Interface" carries two meanings: WAY-165's (API and terminal included) and the spec's (screens)

**Anchor:** `spec.md:516-518`, `spec.md:75-79`, `spec.md:482` (G14), `spec.md:291`; source
`foundations/decisions.md:5347-5350` (WAY-165), `foundations/decisions.md:3436-3438` (WAY-121).

**To paste:** WAY-165 says "the interface asks how an agent operates the product as its user does —
through a screen in a browser, a call to its API or a command in a terminal"; the spec chooses
"interface" for what has screens, so G14 ("which interfaces get a styleguide") read beside WAY-165
gives a command-line tool or an API a styleguide. Which word do the new binding sentences use?

**Why I raise it:** The spec's own wording rule picks "interface" to avoid "view" (WAY-18), but the
foundation already uses "interface" in a binding sentence for any way a user operates a product.
WAY-99: "Where a word carries two meanings in the files of `foundations/` … and one of them is a
meaning a reader who knows the product's field would not give it, one of the two is renamed." A
reader of the field gives "interface" the broad meaning; the spec's is the narrower "user interface
with screens". Example: an agent refining a task for a CLI product reads G14 "every interface of a
product gets a styleguide, an admin panel included" and the skill's description "an interface of a
product … needs a styleguide", and opens a styleguide task for the terminal output. Fix: "user
interface" or "screens" in every binding sentence and the skill's description, or a glossary entry
whose definition sets the narrower meaning (WAY-95) — the designer's concern "possible extra
glossary terms" lands here.

### 6. The product invariants derive from a decision that does not cover them

**Anchor:** `spec.md:159-161`; task `task.md:166` (row 26), `task.md:143-144` (rows 3, 4).

**To paste:** `guidelines-form` and `guidelines-reference-current` are to derive from "the product's
decision adopting the template (row 26)", but row 26 is about the styleguide template's content
(rows 5–13 and 15), while rows 3 and 4 bind the guidelines of every domain; a product whose first
guidelines are, say, its testing standards has no such decision to derive from.

**Why I raise it:** Row 26's text: "Treść szablonu styleguide'a i propozycje skilla (wiersze 5–13 i
15) to decyzje the way o tym, co szablon niesie…". Rows 3 and 4 are not in that list and bind
directly. The spec's *Derives from* therefore either fails for a non-styleguide first document or
widens row 26 to "the template of guidelines" without saying so. It also makes a product write a
decision only to give an invariant a parent: WAY-17 wants the link where the invariant does derive
from a decision, and WAY-71's complying example is "an invariant whose author searched the log and
found no decision it derives from reads `Derives from: none`". Fix: `Derives from: none` in the
product, with the template saying which decisions of the-way the sentences come from; or, with
finding 1's way (a), the-way's own copies derive from G3 and G4.

### 7. A role's meaning is binding but carries no invariant — row 18 says it does

**Anchor:** `spec.md:175`, `spec.md:191-197`, `spec.md:391-402`; task `task.md:158` (row 18).

**To paste:** Row 18 settles that in the styleguide every binding rule has an invariant, agent-run
with k of n where a script cannot decide it, and its last column names exactly this case ("czy
reguła o znaczeniu koloru zostaje bez niezmiennika, bo skrypt jej nie sprawdzi"). The `## Roles`
table gives each role a decision and no invariant, the form check requires none for it, and the
first invariants of step 4 check hard-coded values, focus and contrast — none checks that a role is
used in its meaning.

**Why I raise it:** The meanings are the core of the styleguide: charge C1 of the trial was "one
colour in several meanings" (green for "may act", "running", "later" and "won"). With the spec as
written, a cycle can pass every check of the styleguide while a screen uses `destructive` for
"unsaved changes": the roles are written down, the decision exists, nothing checks the use. That is
the state row 18 rejected ("część reguł trzyma tylko pamięć agenta, przed czym miał chronić
styleguide"). Fix: give `## Roles` an *Invariant* column (or one rule under `## Rules`, "each role
is used only in its meaning", naming the role decisions and an agent-run invariant with k of n), add
it to step 4's first invariants as the skill's proposal, and make the form check require it.

### 8. Not every fingerprinted reference is checked — the `none —` departure line escapes

**Anchor:** `spec.md:134-135`, `spec.md:152-155`, `spec.md:248-255`; task `task.md:143` (row 3).

**To paste:** Error 5 checks the fingerprints of references in *Decision*, *Invariant* and `## Roles`
rows only; the `none — <PREFIX-NN>@<fingerprint>` line of a dropped section, and any fingerprinted
reference in a rule's prose or under `## Examples`, are checked for form (error 4) but never for
currency. Row 3 stops the merge for any reference whose entry changed wording.

**Why I raise it:** Example: a product departs from the template with `## Kitchen sink` reading
`none — LOOP-31@a1b2c3d4`, LOOP-31 saying "the product shows no sample page because it has one
screen". A later task adds four screens and rewords LOOP-31 to "…until it has a second screen";
the fingerprint moves, the departure line keeps the old one, the form check passes, and the
styleguide goes on telling agents the section is dropped for good. The product invariant's own
sentence has the same gap ("Every decision or invariant a rule of a file … names"). Fix: error 5
and the sentence of `guidelines-reference-current` cover every token of the form
`<PREFIX-NN>@<hex>` or `<identifier>@<hex>` in a guidelines file outside fenced code, whatever
section it stands in; a test for the departure line.

### 9. Four sections of the styleguide template are neither rules nor examples

**Anchor:** `spec.md:125-131`, `spec.md:176-181`; task `task.md:142` (row 2), `task.md:158` (row 18).

**To paste:** Row 2 settles that a binding guideline names its decision (and in the styleguide its
invariant), and that anything naming no decision is an example; the spec gives `## Changing a
meaning`, `## Mockups`, `## Kitchen sink`, `## Where values come from` (and the state list of
`## Components and states`) sections of their own, outside `## Rules` and `## Examples`, with no
*Decision* or *Invariant* field. Are their sentences binding or examples?

**Why I raise it:** These sections carry rows 7–10 and 12, each a decision of the-way the product
adopts (row 26), so after adoption they bind — yet the form the form check enforces gives them no
carrier, and an agent reading "a fault of one screen is fixed in its component" cannot tell whether
it may depart from it. Under row 18 a binding rule without an invariant must either get one or
become an example; "fixed in its component" can be checked by an agent with k of n, "a mockup is a
pattern" probably not. Fix: state for each section whether it is a rule (written as a `### rule`
with *Decision* — the adopting decision — and *Invariant*) or an example under `## Examples`, and
let §5.3 check it accordingly; at the same time give the merged order of common and styleguide
sections (finding 13).

### 10. G5's approval before code goes against WAY-114 without naming it

**Anchor:** `spec.md:473` (G5), `spec.md:492` (G24), `spec.md:496-499`; source
`foundations/decisions.md:3219-3223` (WAY-114), `foundations/decisions.md:710-714` (WAY-25).

**To paste:** WAY-114 has the agent write an entry and the human accept it at the merge; G5 holds
that a new meaning is approved before the code that uses it, and that a cycle meeting an unsettled
meaning stops with a blocked draft request — a departure from WAY-114 in the area of guidelines,
yet G5 names only `derives from WAY-30`, and the `narrows WAY-114` stands on G24, which carries only
the asking.

**Why I raise it:** Row 27: "nowe znaczenie w wytycznych człowiek zatwierdza przed kodem, który go
używa — tym wytyczne odchodzą od WAY-114/1". The spec moves that clause into G5 (rightly, WAY-19) but
leaves the relation on G24. WAY-25: "the one that prevails names the other in *Relations* as
`narrows`, and its binding sentences state the area where it prevails … A collision between two
decisions with no precedence recorded is never settled by the agent that meets it." Example: a
cycle meets an unsettled role; WAY-114 says "write it on your recommendation, the human accepts at
the merge", G5 says "stop"; with no `narrows` on G5 the cycle's agent has two applicable decisions
with no recorded precedence and must stop to ask which holds — or picks one. WAY-30 itself covers
changes to a decision, not a new one, so it does not carry the precedence either. Fix: G5 names
`narrows WAY-114@<fp>` and its binding sentence states the area (new or changed meanings of a
product's guidelines).

### 11. The skill has no form for orchestrated refinement

**Anchor:** `spec.md:307-312`, `spec.md:346-353`, `spec.md:403-404`, `spec.md:372-376`; source
`project-level/task/skill/SKILL.md:26-35`, `foundations/decisions.md:4903-4916` (WAY-154),
`:4941-4950` (WAY-155).

**To paste:** The skill asks the human directly and starts fresh agents for research and critique;
a styleguide task that belongs to a project plan is refined in orchestrated mode, where the refiner
"Never ask[s] the human directly" and "Start[s] no child agent". How does `maintain-styleguide` run
there?

**Why I raise it:** Row 15 puts the styleguide before the first screen, and the first screen of a
product most often arrives in a project (WAY-121's own example: "a project that brings a product's
first screen"), so the styleguide task is likely a member of a project plan led by `lead-project`.
The skill wraps `refine-task` steps 1–2 and 4–6 but says nothing of the orchestrated mode those
steps have. An agent following the spec in an orchestrated round either breaks WAY-154/155 (asks
the human past the project orchestrator, starts research agents itself) or stalls. Fix: one
paragraph in §6: in orchestrated mode the skill's questions, the WCAG proposal and the shown choices
go into the conversation turn as `refine-task` routes them, and research and critique agents are
requested from the project orchestrator, with the reports' paths in the turn; or state that a
styleguide task is refined manually only, with the reason.

### 12. The chosen token values have no carrier from the refinement to the cycle

**Anchor:** `spec.md:181`, `spec.md:199-202`, `spec.md:314-329`, `spec.md:377-381`; task
`task.md:152` (row 12).

**To paste:** The cycle's author is told to "take every meaning from the task's settlements … take
no value from memory or from a mockup" and to put the role values in the tokens file with their
sources, but the record that reaches the task document (§6.2) carries meanings, the source of
values and research sources — not the values the human saw and chose. Where does the author read
"the delete button is red, its text white" as values?

**Why I raise it:** Values are not decisions (WAY-04: values stand in code), so
`find-foundation-entries` will not make rows of them, and *Questions to settle* holds "each
meaning, role, pair, state rule, departure … and WCAG answer". For a product before its first
screen nothing in the repository holds values yet. Example: the human chooses, from options shown
as what the user sees, a warm neutral scale and a red `destructive`; the task document carries the
role meanings and "source: research of Tailwind v4 defaults, page X version Y"; the author must pick
the hex values of "warm neutral" from that source by judgment — exactly the guess the template
forbids — or stop the cycle. Fix: *To do* names, per role, the value and its source as settled in
the conversation (or the exact source address and the entry in it the values are read from), and
the template's "Writing the file" says the author takes values from there.

---

## Minor

### 13. The merged order of sections is not given, and one section is placed under another `##`

**Anchor:** `spec.md:93-118`, `spec.md:173-181`, `spec.md:240-243`.

**To paste:** Error 1 reports a section "out of order", but the spec does not say where the seven
styleguide sections stand among `When to read`, `Rules`, `Examples` and `Where in code`, and
`## Plan of an interface change` is said to stand "under `## Examples`", which a `##` heading
cannot.

**Why I raise it:** The form check needs one total order to test, and the template author will
otherwise choose one the human never saw. Fix: give the styleguide skeleton whole, with
`### Plan of an interface change` under `## Examples` if that is the intent.

### 14. The shared report prints one path for every finding

**Anchor:** `spec.md:219-220`; source `elements/common/guard_shared.py:183-186, 230-233`.

**To paste:** `Report.print` writes `"%s:%s: error: …" % (self.path, line)` with a single path; the
form check reads several guidelines files, so either it keeps a report per file (and merges their
records) or its messages name the file.

**Why I raise it:** With two styleguides (`styleguide-web.md`, `styleguide-admin.md`) every error
would print under one path, and the anchor `<path>:<line>` the spec promises would point into the
wrong file. A sentence in §5.1 settles it.

### 15. Reusing `merged_log` brings the decisions guard's findings into the form check

**Anchor:** `spec.md:224-227`, `spec.md:235-238`; source `elements/decisions/format_guard.py:824-859`.

**To paste:** `merged_log` takes a report, records `log-merge-copies/1` on it and reports differing
copies as errors; called with the form check's report, it makes the form check exit 1 on a decision
log conflict and record a verdict for a decisions invariant.

**Why I raise it:** Say in §5.1 that the form check passes a report of its own to the borrowed
functions and carries over only failures of the run (git cannot read the log), so its exit code and
record speak of guidelines alone.

### 16. Two claims about `check_instructions.py` do not hold

**Anchor:** `spec.md:139-141`, `spec.md:581-582`; source `instruction-files/check_instructions.py:60`,
`:515-516`, `:368-382`.

**To paste:** An `@theme` or `@media` outside a code span is not reported — the script reports an
`@` word only when it holds a `.` or `/` — and a Tailwind class with a slash in backticks, such as
`bg-primary/90` or `w-1/2`, is taken for a path and reported as a dead path (`warn`).

**Why I raise it:** The rule "code names in backticks" stays right, but its stated reason is wrong,
and §10's check on the temporary product ("no `error`, no `at-import`") will show `dead-path`
warnings for the template's own good/bad examples if they use such classes. Fix: correct the reason
in §3.2, and have the template put class examples with slashes in fenced code, which the script
skips (`prose_lines`).

### 17. Files under `guidelines/` the check does not read pass in silence

**Anchor:** `spec.md:231-233`.

**To paste:** A file `guidelines/styleguide/web.md` or `guidelines/styleguide-web.MD` is not
`guidelines/<name>.md` one level deep, so it is skipped and the run passes.

**Why I raise it:** A misplaced styleguide is then never checked, and its stale references never
stop a merge. A `warning:` per tracked path under `guidelines/` that the check does not read costs
one line.

### 18. Tests: the 1 MiB line, the invariant side of `--merge-onto`, and the network test

**Anchor:** `spec.md:598-599`, `spec.md:602-607`.

**To paste:** "A line of 1 MiB of backticks and `@`" makes the file exceed the 1 MiB limit, so it is
refused before any regular expression runs; there is no test of an invariant changed or withdrawn
only on the onto commit; and a patched `socket` cannot see the git subprocess.

**Why I raise it:** Use a line just under the limit; add the invariant cases the version rule of
`spec.md:235-238` introduces (it mirrors the facts guard's merge, not the invariants guard's); say
that the network test covers the script's own code and that git sees no path that failed the shape
test.

### 19. "Domain" collides with WAY-95 and WAY-104's "a product's domain"

**Anchor:** `spec.md:97-99`, `spec.md:120-123`, `spec.md:524-525`; source
`foundations/decisions.md:2614-2616` (WAY-95), `:2891` (WAY-104).

**To paste:** The glossary entry and G1 will say "one domain of the product" for styling, testing or
observability, while WAY-95 and WAY-104 use "a product's domain" for its business area ("a game's
glossary defines 'level'").

**Why I raise it:** WAY-99 asks one word per meaning in `foundations/`. The collision is cheap to
avoid before the term enters a binding part ("area", "subject"); after the main branch a new meaning
takes a new word (WAY-97). The header field `**Domain:**` would follow.

### 20. The focus invariant does not rest on the WCAG fact row 21 gives it

**Anchor:** `spec.md:391-397`; task `task.md:161` (row 21).

**To paste:** Row 21 takes "wymóg widocznego fokusu" from WCAG through the adopting decision; the
spec's contrast invariant rests on the WCAG fact, but the focus invariant ("every control … carries
the focus style of the focus role") names no fact and no derivation from the adopting decision.

**Why I raise it:** Without the link, a new WCAG edition flags the contrast invariant and leaves
focus unreviewed (WAY-73, WAY-31). One clause in step 4.

### 21. Scope of WAY-09 (and WAY-38, WAY-27) does not gain the new part

**Anchor:** `spec.md:60-71`; source `foundations/decisions.md:263-265`, `:1111-1112`, `:771-772`.

**To paste:** WAY-09's *Scope* lists every part with a directory; editing it to name
`product-guidelines/` without adding `product-guidelines` to its *Scope* leaves the decision unfound
for a later change to that directory (WAY-21). WAY-38 (scripts) and WAY-27 (pointers outside the
repository) govern the new files as well.

**Why I raise it:** "Reading the foundation" step 2 selects decisions by *Scope*; a later change to
`form_check.py` would not select WAY-38. WAY-38 already lacks `gate` and `project-level`, so this
follows a known gap rather than opening one — still, the edit of WAY-09 is in hand.

### 22. *To do* 5 says pairs are pointed to in code, not copied — the spec writes them down

**Anchor:** `spec.md:175`, `spec.md:191-197`; task `task.md:30` (*To do* 5), `task.md:146` (row 6).

**To paste:** *To do* 5 ends "Wartości, pary i spis komponentów styleguide wskazuje w kodzie, nie
przepisuje"; the spec puts each background's text role in `## Roles` and in a product decision.

**Why I raise it:** Row 6 supports the spec (the pair stands in the styleguide), and WAY-60 needs the
pairs in a decision; read as "pair values in code, the pairing rule written by hand", the two agree
(WAY-04: rules are written by hand). State that reading in §4 so the reviewer of the request does not
take it for a departure.

### 23. Smaller gaps in the skill and the part map

**Anchor:** `spec.md:333-337`, `spec.md:355-358`, `spec.md:550-551`, `spec.md:100`.

**To paste:** Step 0 does not list `refine-task` and the task template, which the skill drives
through steps 1–2 and 4–6; the skill text must describe `om-ux-shape`'s step 7 rather than name it
(WAY-27); `product-guidelines` *Depends on* omits `task-cycle`, on whose blocked draft rule §7
rests; *Applies to* names parts nothing checks against the map, and the file name
`styleguide-<part>` goes stale when a part is renamed.

**Why I raise it:** Each is a line in the spec; together they keep the skill from reading less than
it relies on, and the map from hiding a dependency.

### 24. Template rules and choices that no decision carries

**Anchor:** `spec.md:90-91`, `spec.md:136-144`, `spec.md:175`, `spec.md:183-189`.

**To paste:** The spec says each rule of the template cites its decision (WAY-35 by analogy), but
the G list has no decision for the common form (header lines, the four sections, *Good*/*Bad*),
the closed list of *Kind*, the words role names avoid, or guidelines written in English
(autonomous).

**Why I raise it:** WAY-22: "A rule that records a choice is a decision". Without a carrier, the
template's rules cite nothing and the English rule — which binds every product's guidelines and
which WAY-108 would answer the other way for a human-facing document — reaches the human only as
prose of the request. Fix: let G2 or G4's binding sentences name the form's parts and the language,
or add one decision for the form, marked autonomous with its price. I grade it Minor because the
human sees every G entry at the request anyway; it becomes Important if the template is expected to
cite a decision per rule.

---

## Good

- The split of meanings between product decisions and the styleguide's table under fingerprints
  (`spec.md:191-197`) answers WAY-18, WAY-22 and WAY-60 together and keeps row 5's table for the
  agent at work; grouping meanings into decisions of at most three sentences is a sound reading of
  WAY-05.
- The trust boundary of the form check (`spec.md:259-273`) follows `check_instructions.py`'s
  precedent closely (1 MiB, regular files only, no network shapes, `:(literal)` pathspecs), so the
  1 MiB limit is not invented but borrowed.
- The `--merge-onto` rule for invariants (branch copy where the branch changed it since the fork
  point, the onto copy otherwise) matches the facts guard's merge
  (`elements/invariants/format_guard.py:1446-1470`); the decisions side reuses `merged_log`. The
  version rule can be built with the standard library.
- §7 places a new meaning met by a cycle on `implement-task`'s existing blocked-draft rule
  (`task-cycle/skill/SKILL.md:20-21`) without changing the cycle — consistent with the task's
  *Out of scope*.
- The departure syntax `none — <decision>@<fp>` (root C9) gives row 26 a mechanical form.
- Contradictions 1–5 of §11 are each settled with the rule that settles them.

## Not checked

- `reports/design.md` and the three research reports — not read; no finding needed a claimed
  source checked there.
- `elements/decisions/format_guard.py` between lines 300 and 800 (the per-field checks), and the
  invariants guard outside the ranges listed; repeal detection for "repealed" in error 5 was not
  traced.
- Whether `gate/test_skills_reach_the_way_sessions.py` needs more than the flow's *Parts* list to
  accept the new skill; whether the installer's tests assert the full guidance text.
- No command was run; nothing was built or tested. The fingerprint of WAY-09 after the edit and the
  renewed fingerprints of its six invariants were not computed.
- Decisions WAY-138–153 and 156–164 were read only through their headings and selection map; none
  was found relevant beyond those cited.

## Unresolved concerns for the root

- Root C5 reads *To do* 7 ("Skill the way tworzy i utrzymuje styleguide") as "leads the
  refinement; the cycle writes the file". It is coherent with WAY-01/WAY-28, but it changes how a
  human-accepted sentence is carried; the request should show it as a provisional answer, with the
  cost (every styleguide change, however small, goes through refinement and a full cycle).
- Root C8's weak point (fixed literals `guidelines-form/1`) remains under every way of finding 1;
  way (a) makes it visible in the-way's own invariants.

---

## Re-review of the revision

Second pass, by the same reviewer, over `spec.md` as rewritten (817 lines), read whole, against the
24 findings above, the root's rulings C11–C22 (`cycle.md` questions table) and the section
"Revision after spec review" of `reports/design.md` (read alone, as instructed). Sources re-opened
for the new choices: a search for "disciplin" in `foundations/`, `elements/`, `project-level/`,
`task-cycle/`, `instruction-files/`, `installation/`, `agent-instructions/` (no hit), and the task's
rows 8, 24 and *To do* 5. No command was run.

### Verdicts

- **Task compliance: compliant, except new finding R1.** Rows 2, 3 and 18 are now carried with the
  meaning the human accepted (§3.1, §3.2, §4.1–§4.2, §5.3 items 3 and 7). R1 widens rows 8 and 24
  from a change of a design token's *meaning* to a change of its *value*.
- **Design coherence: coherent, except R1.** The Critical is resolved by way (a) without changing a
  rule of the gate; the record semantics, the reach of the invariants, the `narrows` on G5 and the
  orchestrated mode now agree with the foundation and the code they rely on.

Status of the 24 findings: **addressed 23 · partly 1 · not addressed 0.**
New issues the revision introduced: **Critical 0 · Important 1 · Minor 8.**

### Status of each finding

| # | Status | Anchor in the revised spec | Note |
|---|---|---|---|
| 1 | addressed | `spec.md:185-216`, `:743-746`, `:687-689` | The-way holds both entries, so `# invariant: guidelines-form/1` names an entry of `foundations/invariants.md`; §10 runs the invariants guard with the script in place. See R8 for the sentence's "pinned commit" in the-way. |
| 2 | addressed | `spec.md:194`, `:202`, `:322-332`, `:776-777` | Two methods; checks of form selected by no option, checks of references by `--merge-onto`, matching `guard_shared.py:241-246`. |
| 3 | addressed | `spec.md:196-197` | `guidelines-form` *Part* `every`. Residual for the reference invariant in a product: R7. |
| 4 | addressed | `spec.md:690-693`, `:407-409` | `guidelines-check-*` name every part whose code the form check loads, `part-map` included. |
| 5 | addressed | `spec.md:33-37`, `:417`, `:629`, `:815` | "user interface" throughout new sentences and the description. |
| 6 | addressed | `spec.md:206-208` | Product copies `Derives from: none`; WAY-58's list does not take them (written for a feature being built). |
| 7 | addressed | `spec.md:237`, `:266`, `:367-369`, `:531-532`, `:698` | Rule, agent-run invariant, form check requirement, G20. Residual on how the invariant reads changes: R3. |
| 8 | addressed | `spec.md:164-169`, `:198-201`, `:376-382`, `:769-771` | Every token outside fenced code. Residual on what the pattern catches: R5. |
| 9 | addressed | `spec.md:220-279` | Each part is a rule with carriers or an example. Two of the new rows carry new issues: R1, R2. |
| 10 | addressed | `spec.md:585-587`, `:620`, `:649-652` | G5 `narrows WAY-114` with its area. |
| 11 | addressed | `spec.md:545-553` | Orchestrated routing, no child agent, research and critique requested from the project orchestrator. |
| 12 | addressed | `spec.md:302-304`, `:444-453`, `:506-507` | Value and source per role in *To do*; R1 contradicts it. |
| 13 | addressed | `spec.md:222-259` | Merged form whole; examples as `###` under `## Examples`. |
| 14 | addressed | `spec.md:333-336`, `:777-778` | A report per file. |
| 15 | addressed | `spec.md:337-342`, `:778-779` | Borrowed code gets a discarded report. |
| 16 | addressed | `spec.md:170-176`, `:751-752` | Reasons corrected; classes with `/` in fenced code. |
| 17 | addressed | `spec.md:351-353`, `:780-781` | A `warning:` per unread path. |
| 18 | addressed | `spec.md:772-773`, `:784-789` | File under the limit; onto-only invariant cases; git calls captured. |
| 19 | partly | `spec.md:670-672`, `:482`, `:23`, `:225` | "Discipline" collides with nothing in the foundation, but the spec itself uses it in a second sense and names the styleguide's discipline two ways: R4. |
| 20 | addressed | `spec.md:525-527` | Focus derives from the adoption decision and rests on the visible-focus fact. |
| 21 | addressed | `spec.md:76-87` | *Scope* of WAY-09, WAY-38, WAY-27. |
| 22 | addressed | `spec.md:281-285` | Reading stated. |
| 23 | addressed | `spec.md:461-463`, `:424-425`, `:713-714`, `:372-373` | All four items. |
| 24 | addressed | `spec.md:619`, `:642-646`, `:177-181` | G26 carries the common form and the language rule. Residual on the language rule's price: R6. |
| C5 concern | addressed | `spec.md:49-52` | The cost is shown as a provisional reading of *To do* 7. |

### New issues

#### Important

##### R1. A change of a design token's value is made a decision — rows 8 and 24 say meaning

**Anchor:** `spec.md:272`; task `task.md:148` (row 8), `task.md:164` (row 24), `task.md:30`
(*To do* 5); contradicts `spec.md:302-304`, `spec.md:444-447`.

**To paste:** The rule "A fault of one screen is fixed in its component" now reads "changing its
value or meaning is a new or changed decision", and proposes a script comparing the tokens file
with `{fork-point}`; the task settles a decision only for a new or changed *meaning* (row 24, *To
do* 5: "zmiana jego znaczenia idzie drogą WAY-30"), and the spec itself carries values in *To do*,
not in decisions.

**Why I raise it:** Row 8 says a fault of one screen is fixed in the component, not by changing a
global token, *because* a global token is a meaning for the whole product; row 24 makes a new or
changed meaning a decision and adds "użycie istniejącego znaczenia nie wymaga zatwierdzenia". Values
stand in the tokens file (WAY-04) and reach the cycle through *To do* (finding 12's fix,
`spec.md:302-304`). With "value" in the rule, two things follow. First, a product invariant "the
tokens file differs from `{fork-point}` only with a decision changed in the same change" fails every
value change. Example: the contrast invariant fails because `--muted-foreground` is too light on
`--muted`; the cycle darkens it from `#71717a` to `#52525b` — the meaning ("secondary text")
unchanged — and now needs a decision approved by the human before the code (G5), so a fix the
contrast invariant asks for blocks the cycle as a blocked draft request. Second, the decisions grow
a row per value, which WAY-04 keeps in code. Fix: "changing its meaning is a new or changed
decision", as the task says; the rule's check then compares *meanings*, not values — an agent-run
invariant over changes to the tokens file asking whether a change alters what a role means, or a
script asserting that a changed role keeps its name and *Kind* — and a value changed for one screen
is what the rule's first half forbids (fix it in the component), which an agent can judge.

#### Minor

##### R2. "Every background with its text" checks the table, not the code it also names

**Anchor:** `spec.md:267`.

**To paste:** The rule says a background role is always written with its text role "in the table
and in code", but its proposed invariant is `guidelines-form`, which reads only the table; under row
18 the code half is then a binding sentence no invariant checks.

**Why I raise it:** Either drop "and in code" from the rule (the table and the contrast invariant
already hold the pairing), or propose the code half's check beside it (a script: every element
whose background reads a background role reads its text role).

##### R3. The role-meaning invariant's reach is worded two ways, and misses reworded meanings

**Anchor:** `spec.md:531-532`; design report, "New autonomous choices in the revision".

**To paste:** "Over the files of the part a change touches" can mean "over the part's files, run
when a change touches the part" (WAY-62's reach, the design report's reading) or "over the files the
change touches"; read the second way, the sentence speaks of a change and must measure it against
`{fork-point}` (WAY-60), and a method reading less than its sentence checks something else (WAY-61).
A reworded role decision also changes what the screens must hold, so its *Part* names the part
holding `foundations/**` as well.

**Why I raise it:** The product's cycle writes this invariant through `record-invariant` from these
words; one sentence in step 4 fixes the reading.

##### R4. "Discipline" in two senses, and the styleguide's discipline named two ways

**Anchor:** `spec.md:482` ("the discipline taken from WAY-122 by G17"); `spec.md:23` ("styling
first") against `spec.md:225` (`Discipline: styleguide`) and `:675-676`; task question 2a ("pełną
dyscypliną z WAY-122").

**To paste:** The spec uses "discipline" for what one guidelines document covers and, at step 2, for
the rigour of WAY-122's research — the source of G17's binding sentence; and the discipline of the
styleguide is "styling" in §1 but `styleguide` in the header and in "the guidelines of the
styleguide discipline".

**Why I raise it:** G17's sentence is likely to carry the second sense into a binding part beside
the glossary entry's first (WAY-99). Use "method" or "rules" for WAY-122's rigour, and pick one value
for the discipline (the header value is read by the form check to select the template, so it is the
one that binds).

##### R5. The reference pattern catches versioned package names in prose

**Anchor:** `spec.md:164-169`, `spec.md:376-379`.

**To paste:** `<identifier>@<hex>` matches `tailwindcss@4`, `lucide-react@0` or `react@18`, which a
styleguide's sources or a rule's prose may well name; each then fails as a reference whose hex part
is not eight characters.

**Why I raise it:** The spec's escape is fenced code "for an address, a sample"; name versioned
package names in that sentence of the template, so the cycle's author fences them before the form
check says so.

##### R6. The language rule's price leaves out the restated meanings

**Anchor:** `spec.md:177-181`, `spec.md:287-291`.

**To paste:** With prose in the product's language, the `## Roles` table's *Meaning for the user*
and each rule's text become a translation of the English decision they restate; the fingerprint
flags a reworded decision, never a drifted translation — the reason WAY-114 keeps translations out
of the foundation.

**Why I raise it:** The choice is defensible (WAY-108's precedent; the reader is the product's
agent), but the price the request shows should name this, beside mixed languages within one
document (English required-rule headings over Polish prose), which the design report already lists.

##### R7. The product copy of `guidelines-reference-current` may miss a pin move

**Anchor:** `spec.md:203-205`.

**To paste:** A pin move can change how the form check computes or reads a fingerprint, but the
product copy names only the agent-directing part and the part holding `foundations/**`; it reaches a
pin move only where the product gives `.the-way` to its agent-directing part, as `loop2` does.

**Why I raise it:** Name the part holding `.the-way` as well (or have the template require the
product to name it).

##### R8. "The pinned commit" in `guidelines-form`'s sentence has no referent in the-way

**Anchor:** `spec.md:189-193`.

**To paste:** The same sentence now stands in the-way, which pins no commit of itself; say "the
template of guidelines of the-way the repository uses — the commit checked in the-way, the pinned
commit in a product", or the-way's copy rests on a condition that names nothing (WAY-60).

**Why I raise it:** The sentence is a binding part copied word for word into products; fixing it
after products copy it raises every copy's version and breaks the literal citation (root C8's weak
point).

##### R9. A styleguide file's header and its name are not tied

**Anchor:** `spec.md:91-96`, `spec.md:372-373`.

**To paste:** The form check selects the styleguide template by *Discipline* and checks the `<part>`
of a file named `styleguide-<part>.md`, but nothing reports `guidelines/styleguide-web.md` whose
header names another discipline, or a `Discipline: styleguide` file not named `styleguide-<part>.md`.

**Why I raise it:** Such a file is held to the wrong template without a word; one error item in
§5.3 and a test close it.

### Concerns remaining

- `guidelines-reference-current` with `--merge-onto none` records a `pass` and an `unchecked` for
  one invariant from two checks; WAY-65 says only when such a set is a `pass`, and the spec's
  "otherwise not `pass`" (`spec.md:330-331`) leaves the gate's reading of the pair to the gate.
  The-way's own copy shows that state until `main` exists; the request should say so, as the design
  report notes.
- Root C5's reading and C8's version-1 literals stand as provisional choices shown at the request.
