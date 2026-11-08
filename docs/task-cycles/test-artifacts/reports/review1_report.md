FAIL d0d3ce6c913b04481fff652de175eeae37099013

# Review of the whole change — task cycle `test-artifacts`

Range `f218b5542ae55b72a95832adde67591365abb72a..d0d3ce6c913b04481fff652de175eeae37099013`
(`dd84fba`, `d0d3ce6`), branch `task/test-artifacts`; `git rev-parse HEAD` = the head given. One
author, no plan, no spec, no slice reviews: this review is the only one the change gets. Blocking
findings come from no slice (there is no plan); each names its commit.

Counts: blocking 3 (Important), Minor 5, out of scope 0 (Declined to judge: 2 lines).

## Critical

none

## Important

### I-1. The glossary's widened "agent's way to the running product" leaves its uses on the old meaning, and makes WAY-317's case and WAY-219's case one case (commit `dd84fba`)

- Place: `foundations/glossary.md:9`; the uses it moves: `foundations/decisions.md:6400-6404`
  (WAY-219, "inspect a screenshot through the agent's way to the running product that its
  foundation settles. Where the foundation settles no such way, they inspect the states in code and
  mark the screenshot unchecked for that reason"), `foundations/decisions.md` WAY-317 (binding
  sentence "A screenshot left unchecked for want of a settled way to the running product is reported
  as WAY-219 gives"; Verification "a product whose foundation settles a way to its running screens
  but no place for screenshots" beside "a product whose foundation settles no way to the running
  product"), `task-cycle/skill/request_template.md:236-237` (item 13, "for want of a settled way to
  the running product stands in item 4"), `task-cycle/change/ui_check.md:6-7`,
  `product-guidelines/styleguide/audit.md:12`, `product-guidelines/audit_end.md:115`.
- What is wrong: the change rewrites the definition to "the means through which an agent checks
  behaviour ... together with the place where the screenshots of that check lie for the human". Under
  that meaning, a product whose foundation settles a browser route but no place for screenshots has
  not settled "the agent's way to the running product" — so WAY-219's "no such way" applies to it,
  and the author inspects in code and marks the screenshot unchecked. WAY-317, written in the same
  change, sends that same product the other way: the author inspects the screenshot and the request
  says no place is settled. The distinction the task needs (To do 4, question 4: the agent *does*
  look at the screenshot and only has nowhere to put it) now depends on which reading of the term the
  agent takes. Likewise the styleguide audit "Where the product's foundation settles the agent's way
  to the running product, open the screens that way" now reads as not applying to a product without
  a place for screenshots.
- Why it matters: the glossary template's "A changed meaning" (`elements/glossary/template.md:95-99`,
  WAY-97) requires the author of a changed definition to search every use and rewrite each whose
  meaning moves, in the same change; the author's report names no such search ("only the definition
  of an existing one changed"). The change's own files (WAY-317, item 13, ui_check) use the term in
  the old meaning, so they restate the entry the change writes differently — Important by WAY-263 /
  WAY-297. No row of *Settlements to record* asks for the glossary change; it is the author's own.
- Evidence: the cited lines; `git grep -n "way to the running product"` lists the uses above.
- Fix (the fixer's choice): revert the glossary change, keeping the definition as the means of
  checking, and let WAY-121 / WAY-165 carry the place as the fourth matter looked at with the way;
  or keep the widening and rewrite every use whose meaning moves (WAY-219's "no such way", item 4 and
  item 13 of the request template, ui_check, the two styleguide audit lines, WAY-317) to name the
  means of reaching the interface explicitly.

### I-2. WAY-319's second sentence and `research.md` turn row 6's condition into a lack the human may choose (commits `dd84fba`, `d0d3ce6`)

- Place: `foundations/decisions.md` WAY-319 binding sentence 2 ("In the step that settles technology
  an option that cannot meet this stays in the comparison with that lack said, as WAY-166 gives for
  an option an agent cannot use") and its rationale ("a way that fails it is seen as a lack in the
  comparison, where the human can weigh it"); `project-level/technology/research.md:69-72`.
- What is wrong: row 6 and question 6 of the task set a condition on the way a product's foundation
  settles ("the-way stawia warunek drodze agenta ... pozwala dwóm cyklom ... sprawdzać naraz"), the
  rejected alternative being to leave the matter to the product. WAY-166, which sentence 2 invokes,
  keeps such an option "open to the human, who chooses between consequences"
  (`foundations/decisions.md:4827-4828`). So by sentence 2 the step may settle an interface option
  that shares one browser between worktrees, and the product's foundation then holds exactly what
  sentence 1 and WAY-319's own *violates* example ("a way in which the second session started in
  another worktree takes over the page of the first") forbid. The entry is in conflict with itself,
  and it weakens what the human settled from a condition to a weighed consequence. It also takes only
  half of WAY-166 (no "the recommendation passes over it"), so not even the recommendation is bound.
- Why it matters: source fidelity — the change alters what it takes from the task (the author marks
  the sentence `the cycle's` and calls it beyond the literal row); a product reading WAY-319 gets two
  incompatible answers to whether its chosen browser route may fail the condition.
- Evidence: the cited sentences; task.md question 6 and row 6.
- Fix: remove sentence 2 of WAY-319, its share of the rationale and the `research.md` sentence (the
  author states removal leaves the row intact, and I agree); whether the technology step should test
  the condition, and with what force, is a question for the human, not for this cycle.

### I-3. Row 7 is written narrower than accepted: no entry says that a committed record copy holds no image file (commit `dd84fba`)

- Place: `foundations/invariants.md:318-326` (`record-copy-image-check`); WAY-316's binding sentence
  ("No file of a screenshot is committed to the product's repository, the copy of the task cycle's
  record that a commit adds to it included").
- What is wrong: row 7 (kind: invariant) reads "Kopia zapisu cyklu dodawana commitem do repozytorium
  produktu nie zawiera żadnego pliku obrazu; sprawdza to skrypt". The invariant written states only
  the script's behaviour (which files it lists, its exit codes); the property itself — the copy holds
  no image file, of any kind — stands in no foundation entry. WAY-316 carries only "no file of a
  screenshot", which is narrower: a diagram or any other image in the copy breaks row 7 and step 5 of
  `task-cycle/skill/SKILL.md` ("checked for image files, which no copy holds"), but not WAY-316, so a
  reviewer judging by the foundation would not find it.
- Why it matters: a row of *Settlements to record* the human accepted ("tak, przyjmuję 1–7") is met
  only in part. The author's two reasons do not hold: (a) "no commit of the-way's own history keeps
  such a copy" — the-way's task cycles commit record copies, e.g. `07cbcf8`, `53ed6b5`, `dcf6908`,
  `f0f44f6` (added and removed in the next commit), and its report also claims "no record copy is
  committed there" from `agent-instructions/README.md`; (b) "its method would be `review` only" —
  `review` is a method the template gives for exactly this (`elements/invariants/template.md:57-60`),
  used by several invariants of the-way (`return-step-record` included).
- Evidence: the cited lines; `git log --oneline f218b55 | Select-String record`.
- Fix (the fixer's choice): write row 7's property as an invariant (e.g. every record copy a commit
  adds holds no image file, `Method: review`, or one sentence covering both the copy and the script
  that checks it, keeping the test), or at least widen WAY-316's binding sentence from "file of a
  screenshot" to "image file" for the record's copy.

## Minor (each within the task unless it says otherwise)

1. `foundations/decisions.md:8094-8095` (WAY-267, *violates*): "a run adds the logs, the interface or
   the development data to its list though the note does not touch them" still lists three of the
   four matters the change makes; the change edited WAY-267 for the count ("up to four further
   choices") but missed this list. The example stays true, only incomplete. The author's own-work
   grep covered "three matters" wording and missed this enumeration.
2. Lines left unwrapped in prose otherwise wrapped at 100 columns: `foundations/decisions.md:2806`
   (125), `:2822` (117), `:2828` (153); `project-level/definition_template.md:169` (131);
   `project-level/technology/start.md:15` (127); `project-level/technology/task_run.md:55` (128);
   `task-cycle/skill/SKILL.md:507` (159). Polish; no check reads it.
3. `foundations/decisions.md` WAY-316 *Rejected*: "the attachments of a release in the product's
   repository" and "an external file store" are rejected as alternatives to a rule whose point is
   that the product chooses the place; a reader can take them as places a product may not settle,
   while WAY-165's new *complies* example accepts "a store outside the product's repository". The
   items come from task question 1, where they were rejected as the answer to "where do they lie";
   saying they were rejected as a place the-way would name would keep the source and remove the
   wrong reading.
4. `task-cycle/review/SKILL.md:86-87`: WAY-316, the request template's *What you will see* and To do
   1 name screenshots "the author or the reviewer shows", but the review skill gives a reviewer no
   word on where its screenshot lies or that its report names the address; it only makes a
   screenshot file in the range a finding. The author listed this as unclear. Today no reviewer step
   takes a screenshot, so nothing breaks yet.
5. Author's report (not a tracked file): "agent-instructions/README.md ... no record copy is
   committed there" is false for the-way's own cycles (see I-3). It concerns only the reasoning of
   I-3; listed so that the fixer does not rely on it.

## The task, item by item

- To do 1 — met: `request_template.md` *What you will see*, WAY-316; reviewer half see Minor 4.
- To do 2 — met: WAY-316, `ui_check.md`, step 5 of "The record before it is committed",
  `review/SKILL.md` finding; see I-3 for the foundation wording.
- To do 3 — met: no place named in any normative text; WAY-316 *violates* "a template of the-way
  names the place".
- To do 4 — met in the text (WAY-317, item 13, ui_check, record template), but made ambiguous by
  I-1.
- To do 5 — met: WAY-318, ui_check, request template.
- To do 6 — met (WAY-319 sentence 1, ui_check); the addition of I-2 goes beyond it.
- To do 7 — met: WAY-121 and every copy of "three matters" in `project-level/` and the template;
  WAY-165 extended (see below); one enumeration missed (Minor 1).
- To do 8 — met: `task-cycle/image_files_check.py`, step 5, *Checks* line of the request template;
  tests pass.
- Rows 1, 2 → WAY-316: faithful. Row 3 → WAY-317: faithful, see I-1. Row 4 → WAY-121: faithful.
  Row 5 → WAY-318: faithful. Row 6 → WAY-319: sentence 1 faithful, sentence 2 see I-2. Row 7 → see
  I-3.

Judgement of the author's changes beyond the literal rows, as the handoff asks:

- WAY-165 (what the fourth matter asks): accepted, not a widening. `running_product.md` settles a
  matter "only where it answers everything the matter asks as the template gives it (WAY-165)";
  without a definition of the fourth matter that rule could not run. Both halves ("where the files
  lie, outside the product's repository" and "how the description shows each as an image") come
  from rows 1 and 4.
- WAY-267 ("three" → "four") and WAY-270 ("a fourth matter" → "a further matter"): accepted; wording
  only, needed for consistency. One enumeration of WAY-267 left (Minor 1).
- WAY-319 sentence 2 and `research.md`: not accepted — I-2.
- Glossary change: not asked for by any row; not accepted as made — I-1.

Own-work check (WAY-164): the requirement named (item 8 on a realistic record; no "three matters"
left) fits where the change is weakest for item 8, and its check would catch the script failing on a
real record. It missed the WAY-267 enumeration and did not look at the glossary change's uses, where
the change is weakest in fact (I-1).

Tests: the test file fails when the behaviour breaks (the per-extension test carries its own list;
the process test checks the exit code; the `.png` text file shows content is never read). No
invariant test was changed; one new invariant test (`record-copy-image-check`, four citing tests).
No reserved choice is taken (standard library only, no new tool). No trust boundary: the script reads
file names only and writes nothing. No screenshot file in the range.

## Declined to judge

- `agent-instructions/README.md` does not describe the record copy or its checks for the-way's own
  changes — present before this change; outside the task.
- Two sessions started from one directory with Playwright MCP (AIR-454) — the task's Context keeps it
  a separate task.

## Checks

- `git rev-parse HEAD` → `d0d3ce6c913b04481fff652de175eeae37099013` (matches the head given).
- `git diff f218b55..HEAD`, `git log f218b55..HEAD` → 2 commits, 16 files.
- `python -B elements/common/foundation_check.py` → `0 errors`, exit 0.
- `python -B agent-instructions/skill_entry_points.py` → `entry points are current`, exit 0.
- `python -B -m unittest discover -s task-cycle -p "test_image_files_check.py"` → 13 tests OK, exit 0.
- `python -B gate/run_tests.py task-cycle` → 200 tests OK, exit 0.
- `python -B gate/run_tests.py project-level` → 271 tests OK, exit 0.
- `python -B gate/run_tests.py elements/common` → 109 tests OK, exit 0.
- Scratch run, temporary directory outside the worktree (removed after): `python -B
  task-cycle/image_files_check.py <dir with cycle.md, reports/Shot.PNG, .png>` → both images listed,
  `checked: 3 files, 2 listed`, exit 1; a missing path → `Error: ...`, exit 2.
- Manual: line lengths of the added Markdown lines (a PowerShell pass over `git diff -U0`) → Minor 2.
- Not run: the full gate (the orchestrator's run, by the handoff).

## Reaches beyond the dispatch

- `foundations/decisions.md` WAY-166 (whole) — what "as WAY-166 gives" binds in WAY-319 (I-2).
- `foundations/decisions.md` WAY-219 (binding sentences), WAY-267 (whole) — uses of the changed
  glossary term (I-1) and the count edits (Minor 1).
- `elements/glossary/template.md` "A changed meaning", `elements/glossary/skill/write.md` — the rule
  for a changed definition (I-1).
- `elements/invariants/template.md` "Method and test"; `foundations/invariants.md` headings and the
  first entries — whether `review` is available for row 7 (I-3).
- `product-guidelines/styleguide/audit.md`, `product-guidelines/audit_end.md:115` — uses of the term
  (I-1).
- `agent-instructions/README.md` whole and `git log` of record commits — the author's premise for
  row 7 (I-3).
- `task-cycle/skill/SKILL.md:420-580`, `task-cycle/record_template.md:90-196`,
  `task-cycle/change/SKILL.md:86` — where the new step and rules sit.

## Searches not found or unclear

- Who puts a reviewer's screenshot in the product's place, and how a read-only reviewer does so: the
  task says "autor albo recenzent pokazuje"; neither the task nor the review skill says how (Minor 4).
- Whether the-way's invariants may state a property of a product's repository (row 7 says "do
  repozytorium produktu") or only of the-way's own commits: `foundations/invariants.md:3` says "What
  the-way states as true or false on every commit"; unclear which repository's commits; I-3's fix
  offers wording that holds for the-way's own record copies.
