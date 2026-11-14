# Spec — co trafia do dziennika decyzji: the question "where it goes", the threshold of entry, guideline rules with no decision, the test that names the sentence of a decision

- Task: `.runs/task-cycles/co-trafia-do-dziennika-decyzji/task.md`
- Open choice: three choices the task carries to its cycle — how `elements/common/foundation_check.py` learns the state the branch left; which script lists an invariant whose sentence changed while its test did not, and where the request's description names it; whether the new column "where it goes" replaces or stands beside the column *Kind* of the table *Settlements to record* — and, with them, what the maker would otherwise guess: the exact words of the five questions, where each of points 1–9 of *To do* lands, the form of the line `decision:`, how the script reads it, and how points 7 and 8 are tested.

## Intent

A decision log grows by every description of behaviour that binds after a merge, so its entries repeat lines of skills, rules of guidelines, single values the code holds and parts of one question under several numbers. The change gives each settlement that passed the plan test five questions that send it to its place, makes the log hold only what passes all five, lets guidelines hold a rule that only says how to write with no decision behind it, lets a part of a question be a sentence of the entry that already answers it, and lets a test name the sentence of a decision it holds, so that the script of the foundation can say which decisions nothing holds. It also lets that script name an invariant whose sentence was corrected while its test was not touched.

## Goals and non-goals

Goals:

- The five questions stand once, in `elements/decisions/template.md`, and the decision skill, the return step, the foundation step and the table of a task document point to them.
- The table *Settlements to record* shows each settlement with the place it goes to, whatever that place is; the human still sees and accepts every row; the cycle writes each accepted row in its place in the same change as the code.
- A guidelines rule with no decision, a decision that is a sentence of an older entry, and a test that holds a decision's sentence have a form each.
- `foundation_check.py` reports as an error a decision the change adds or changes that has no invariant, no test line `decision:` and no pair of examples; lists the old ones that have none; lists an invariant whose sentence a change corrected while no file that cites it changed.
- The thirteen decisions the task names say after the change what points 1–8 say (point 9).

Non-goals (each is out of the task or rejected below):

- No rewriting of existing entries of any log, no first pass over a product's decisions to name tests, no generated index of decisions.
- No new argument, switch or exit code of `foundation_check.py`; no change of `request_check.py`, of the definition template of a project, of `elements/decisions/skill/projected.md`, of the discipline templates and skills of guidelines.
- No new invariant, no new glossary term, no new environment fact, no change of the part map.
- WAY-321 (the switch `--skip-test-citations`), WAY-173 and WAY-36 keep their sentences.

## Constraints

- The surface `foundation-check-command` of the part map: the script keeps its path, its one argument (a root) and its exit codes 0, 1, 2; it adds nothing a caller must pass. It stays on the standard library and starts only git (WAY-38).
- WAY-321 stays as it is: the switch `--skip-test-citations` skips the report of an invariant that reads `test` and which no test cites, and no other report. This is the orchestrator's choice, not the human's.
- WAY-35: every rule of an entry's form stands in the element's template, once; a skill, a step file or the task template points to the five questions and does not copy them.
- WAY-05 and its template text: *Rationale* and *Rejected* of an entry the change writes name no file, script or count; what a decision forces on later work stands in a binding sentence or field.
- WAY-18 and WAY-17: a link between entries stands at one end; a test that holds a sentence of a decision names the decision at the test, and a decision names its tests only by a clause that gives no path and no identifier, so no second copy of the link exists.
- WAY-344: each new reading of a file by the script is covered by a test that gives the file without a field it needs. The new readings take a missing field as an absence already reported by the existing check of fields, never as an empty value and never with a crash.
- WAY-30, WAY-315: a decision of the log binds this cycle. A change of the meaning of a decision beyond what the task and this spec carry goes to the human through a blocked request, not into the entry.
- The tests of the script build a small product in a temporary git repository, break one thing, run the script as a product runs it, and read its exit code and report (`elements/common/test_foundation_check.py`). The test products there have no commit, so every existing test runs with no base known and must pass as it stands. A test that needs a base commits on a branch named `main`, and a test of the remote HEAD makes one with `git update-ref` and `git symbolic-ref`, with no network.
- A line of a test product that starts with a comment sign and holds `invariant:` or `decision:` and stands at the start of a line inside a triple-quoted string of the test file is read as a citation of the test file itself; the tests write such lines as one-line strings with `\n`, as the file does today.
- The test of the-way's own foundation (`test_the_way_foundation_passes`) runs the script on the real repository: every decision this change edits keeps its pair of examples, and every `decision:` line a test of the change holds quotes the start of a sentence that stands in its entry.

## Decisions

### D1. How the script learns the state the branch left (point 7, point 8)

The script asks git itself and takes no new input.

- The main branch is the branch `refs/remotes/origin/HEAD` names; where that does not exist, the local branch `main`; where that does not exist, `master`.
- The state the branch left is `git merge-base HEAD <that branch>` — the `{fork-point}` of `elements/common/rules.md` and WAY-65. It reads at that commit `foundations/decisions.md`, `foundations/invariants.md` and the files that hold a citing line (`git show`, `git grep`), and compares them with the working tree, which is what the script reads everywhere else. A change not yet committed is therefore compared too.
- Where no such branch or no merge base exists (no remote HEAD, no `main`, no `master`, shallow history, no commit), the base is unknown: no decision counts as new or changed, no invariant is listed under D4, and the report holds one line, `foundations/decisions.md: listed: ...` (a path and no line number), that says that the commit the branch left the main branch from is not known and so nothing was compared. Exit codes do not change: the base is read to inform, and a failure to read it is no `2`.
- `elements/common/rules.md`, under `{fork-point}`, gets one bullet: where a script reads the commit and nobody names the main branch, it takes the branch in this order.

Rejected:

- A new optional switch `--base <commit>`: the one command that runs a product's tests has no place to pass it, so the gate would have no teeth where it matters, and the surface promises the argument.
- An environment variable: an input nobody sees.
- Reading the base from the cycle's record: a change made outside a cycle would stay unchecked, the reason WAY-321 gives for a check in the product's own command.

Cost if wrong: where a product's remote HEAD names a branch other than the one its work merges into, the base is too old (an error for a decision merged earlier, which a pair or a test clears) or too new (no error, as today). Where git cannot give a base, the gate keeps its old strength and says so in one line.

### D2. The report of decisions that nothing holds (point 7)

A decision is *held* when any one of these stands:

1. its *Verification* names at least one invariant after `invariants:` (the form the script already reads);
2. a tracked file other than Markdown holds a line `decision:` that names its number (D3), valid or not — a stale line is reported by D3 and is not reported a second time here;
3. its *Verification* holds a line that begins `- complies:` and a line that begins `- violates:`.

A decision is *changed by the change* when its heading is absent at the base, or its *binding part* differs from that at the base. The binding part of an entry is the text from the line after the heading to the line before its first field line `- **<Name>:**`, compared after every run of spaces and line breaks becomes one space and both ends are trimmed — the normalisation WAY-02 gives for a fingerprint. A change of *Rationale*, *Rejected* or a field alone does not change the decision here. An entry of the earlier form (a version in its heading) and an entry that lacks *Verification* are left out: the existing check of fields reports them.

Output:

- A decision changed by the change that is not held is an error at its heading line: it has no invariant, no `decision:` line and no pair of examples.
- Any other decision that is not held is listed, not an error, at its heading line.
- Listed items stand after the errors and before the count line, each as `<path>:<line>: listed: <message>`; the count line `N errors` and the exit code count errors only. The switch `--skip-test-citations` skips the report of an invariant with no citing test and nothing else, so the error of this report stands in every run.

Line for the request's decisions for the human (the item of *You accept by merging*, kind 5): a decision pinned only by a test that a later slice writes gets a pair of examples at the foundation step, because the error also stands in the run made right after an entry is written, and the return step removes the part of the pair the test then holds. The open alternative is that the switch also skips this error, so that the foundation step writes the decision alone and the later slice writes the test. It changes WAY-321, which the task does not list and the human did not see; its cost is one clause of WAY-321 and its test, and what the choice taken costs is a pair written and trimmed in every cycle that has such a decision.

Rejected:

- "Changed" as any text of the entry: every old decision touched by a reference rewritten after a withdrawal, or by a typo in *Rationale*, would stop the gate until it is held.
- The error for every unheld decision: no product passes until a separate cleaning is done (the task's own rejected way).
- The same list only, with no error: unheld new decisions keep arriving.

### D3. The line `decision:` and how the script reads it (point 6)

Form: a comment line in a tracked file other than Markdown, in the comment forms of the line `invariant:` the script already reads, holding `decision:`, one decision number as the heading writes it, and one quotation in straight double quotation marks to the end of the line (a closing `*/` or `-->` after it allowed). The quotation holds no `"`. The line stands at the test that holds the sentence.

How the script reads it, for each such line, in every run:

- The number is checked as any decision number of any file already is (it names a decision of the log and none withdrawn).
- The quotation, with the normalisation of D2, must stand in the binding part of the entry of that number, begin at the start of a sentence — the start of the binding part, the start of one of its paragraphs, or the first word after a full stop and a space — and hold at least three words.
- A line that has no number or no quotation, or has anything after the quotation but a comment closer, is an error at the line. A quotation that stands nowhere in the binding part of its entry, or not at a sentence start, or has fewer than three words, is an error at the line that names the decision and the line; that error is also the report that points to the test whose sentence was reworded.
- A line in a Markdown file or in a file git does not track counts for nothing; the mention of a number in a test with no such line holds no sentence.

*Verification* of a decision names the tests that hold its sentences with a clause `tests: <the parts of the sentences they hold, in words>`, with no path, no test name and no number: the lines `decision:` find the tests, and the script does not read the clause (an agent compares it). A decision whose sentence a test holds in whole carries no pair of examples; one whose test holds part of it carries a pair only for the part no test holds. A decision whose sentence such a test holds gets no invariant derived from it (WAY-22); an invariant stays for a rule with no choice behind it and for a rule that several decisions stand on.

Rejected: the number alone (the larger entry is pointed to, the weakness of the choice on parts of one question); numbered sentences or paragraphs (a reordered paragraph breaks the references, and WAY-02 rejects suffixes beside a number); naming test files or test names in *Verification* (a second copy of the link, WAY-18, which breaks when a file moves); a script check that *Verification* holds the clause when a line exists, and the converse (a second place kept in step by hand; the lines are the source).

Cost if wrong: every rewording of a sentence a test holds needs its quotation corrected, which the error points to.

### D4. The invariant whose sentence changed while its test did not (point 8), and where the request names it

The script `elements/common/foundation_check.py` lists it, in the same run: it already reads the invariants and the lines that cite them, and D1 gives it the base. `task-cycle/request_check.py` cannot hold it: it reads the description and the task only, judges no content, and runs nothing (WAY-290).

An invariant is listed, at its heading line as `listed: <message>`, when all of these hold: it stands in `foundations/invariants.md` at the base and now; its sentence — the text from the line after the heading to the line before its first field, normalised as in D2 — differs; its *Method* now reads `test`; at least one file other than Markdown holds a line `invariant: <its identifier>` at the base or now (WAY-65: either commit makes the file an invariant test); and no such file differs between the base and the working tree — a file counts as changed when its content differs, or it was added or deleted. An invariant with no citing file at all is no listing: the existing report of an uncited `test` invariant covers it. An added invariant is not listed.

The description of the request names it (kind 7 of `task-cycle/skill/request_template.md`, in *You accept by merging*, and the lower part *Foundation entries*): the writer of the description runs `python -B elements/common/foundation_check.py` (in a product, `.the-way/elements/common/foundation_check.py`) on the finished change, without the switch, and reads its `listed:` lines; each invariant listed for a corrected sentence goes into kind 7 in plain words — what the sentence now says and that the test that checks it was left as it was — and into *Foundation entries*; and each test whose line `decision:` the change adds, drops or alters (a changed file with such a line) is named in kind 7 as a changed invariant test is (WAY-03). The gate's run is not kept for this, so the writer runs the script itself.

Rejected: a new script (a second reader of the same files and of git); the script stopping the gate on it (the task asks only to list it; the count of false alarms from a sentence reworded in words alone is not known); a new kind of item (kind 7 is the item for changed tests and entries a human sees at the merge).

### D5. The column *Goes to* replaces *Kind*

In the table *Settlements to record* of the task document one column *Goes to* stands in place of *Kind*, so the header reads `| # | Settlement | Goes to | Source | What the cycle would otherwise guess |`. Its values, in English as the other markers are:

- `decision`, `invariant`, `glossary term`, `environment fact` — as *Kind* reads today, so those rows read as before; `decision` is a new entry of the log, that passed all five questions;
- `sentence of <PREFIX-NN>` — question 5: the settlement becomes a sentence of that entry;
- `skill or instruction file: <its name or path>` — question 1;
- `guidelines: <discipline>` — question 2, for a rule that only says how to write; a rule that carries a choice with a real cost is a `decision` row and the rule names it;
- `data or code: <the place>` — question 3; the cycle writes the value with a test that holds it and, where the reason is not obvious, a comment at the value.

A settlement the five questions answer "nothing" (question 4) is shown as a rejected row with that reason and is taken out at the close, like every rejected row. An accepted row stays in the document with its place, so the human sees and accepts each settlement, those that go outside the log included. A row whose *Goes to* is not a kind of entry is written in its place by the cycle's foundation step, or its return step where the foundation step missed it, in the same change as the code, as WAY-134 now says of an entry.

Where it lands: the skeleton and the paragraph "Settlements to record" under "What each section carries" in `project-level/task/template.md` (the sentence about *Kind* becomes the sentence about *Goes to*, and a candidate becomes a decision, an invariant, a glossary term, an environment fact, or a settlement that goes to another place the questions give); step 1 (also read the questions in the decisions template), step 2 (a candidate that is a decision passes the questions, and the table is built with the column) and step 5 of `elements/common/skill/task_variant.md`; the sentence of `elements/common/skill/build_table.md` that gives the row's kind (it keeps *kind* for the definition variant and says the task variant's lines give the column in task mode); the sentence of `task-cycle/skill/foundation_step.md` that writes a row "as an entry of its kind" (it writes the row in the place the column names). Each of these points to the questions and does not copy them.

Rejected: *Goes to* beside *Kind* — a row of a skill line would read Kind `decision` and Goes to `skill`, two columns that contradict, and *Kind* would repeat *Goes to* in three rows of four. Cost if wrong: WAY-115 says the table shows "its kind"; in task mode the new column carries the kind for the entries, so WAY-115 needs no change, but the table of a project definition (`definition_template.md`, which keeps *Kind*) and the table of a task now differ by one header.

### D6. The five questions (point 1)

Where: `elements/decisions/template.md`, section "Decision or invariant", a new bullet **Where it goes:** directly after **Plan test:** and before the bullet on tests. The plan test (WAY-36) stays the first threshold. The bullet gives a settlement that passed the plan test five questions in order; the first "yes" names its place; what passes all five is an entry. The words of each, in English:

1. "Is it an instruction for how an agent works?" — it goes to a skill or an instruction file.
2. "Is it a rule only for how to write code, tests or the look of the product?" — it goes to the guidelines of that discipline, as a rule with its reason in one sentence; a rule that carries a choice with a real cost stays a decision and the rule names it.
3. "Is it a single text, number, list or location?" — it goes to the product's data or code, with the test that holds it and, where the reason is not obvious, a comment at the value.
4. "Is it only the lack of a feature?" — it is not written, unless another entry stands on it (WAY-26).
5. "Does an entry of the log already answer the question it answers, in whole or in part?" — it becomes a sentence of that entry.

Below them the threshold sentence: an entry stands only where someone who does not know the decision would do otherwise and a test that stops them would not tell them why. Below that, a paragraph for the log of the-way itself, the wording of question 1 there: "Is it an instruction for how an agent works and does it stand in one skill or template of the-way?" — it stands there with one sentence of its reason, and is an entry only where it carries a choice with a real cost, one for which someone could reasonably propose the rejected way, in which case the skill or template names the decision. In a product's log question 1 stays as above.

Who applies it: `elements/decisions/skill/decide_entry.md` (the bullet that opens "Apply the template's plan test" takes the questions after the plan test: where the first yes is not the log, no entry is written and the rule goes to its place in the same change, a rule going to guidelines being written as the guidelines template gives; where it is question 5, the entry is edited as "Changing a decision" says); `task-cycle/skill/return_step.md` (the clause "a choice that binds after the merge (WAY-36)" becomes "in the place the questions of the decisions template give it", the exclusion sentence stays, and the report of the step names the place of each settlement); `elements/decisions/skill/SKILL.md` step 3 (the *Verification* bullet gives the invariants, the clause `tests:` and the pair only for the part no test holds). They point to the template and do not repeat the questions.

### D7. Guidelines rules with no decision (point 4)

In `product-guidelines/template.md`: the opening paragraph says a rule that only says how to write code, tests or the look of the product stands alone with its reason in one sentence and its *Decision* reads `none`, and a rule that carries a choice with a real cost names the decision that carries it; the line `- **Decision:** <PREFIX-NN> · … | none` of "Required form" and the bullet "A binding rule" allow `none`; the bullet "What names no decision is an example, not a rule" is reworded so that an example is what holds no rule (it stands under `## Examples` with no *Decision* field), since a rule with no decision now binds; the rule that a rule carries no rationale stays, except that a rule with *Decision* `none` carries its reason in one sentence. A change adding such a rule is accepted as a row of the task's table (*Goes to* `guidelines: <discipline>`) before the code; a rule the cycle found itself is named in the request's kind 6 among what the human did not see at the task, extended to name it, and in *Foundation entries* of the lower part, and the human accepts it at the merge. The script needs no change: it reads decision numbers anywhere and a rule's *Invariant*, never a *Decision* that reads `none`.

### D8. Rows 11 and 12 are attached parts, not new numbers

The report of D2 is an attached paragraph of WAY-12 (*To do* 7 already lists WAY-12 as changed); the listing of D4 is an attached paragraph of WAY-03; each has its own one to three binding sentences (point 5). No invariant is written for them; the tests of the script carry `decision:` lines that quote the start of those sentences (point 6 applied to its own sentences).

### D9. Tests of the script

In `elements/common/test_foundation_check.py`, in its style. The line `decision:`: a good line passes; a quotation standing nowhere; a quotation only in *Rationale*; a quotation not at a sentence start; a quotation wrapped over two lines in the entry; fewer than three words; no quotation; text after the quotation; a number that names no decision; the line in a Markdown file; the line in an untracked file. Base: no commit (the existing tests); a base on `main`; a base through a remote HEAD that points to a branch not called `main`, preferred over `main`; no base (listed line, exit 0). Point 7: a new decision with no invariant, line or pair (error, exit 1); the same with a pair, with a line, with an invariant (each passes); a decision whose binding sentence changed and none held (error); only *Rationale* changed (listed, exit 0); an old decision with none held (listed, exit 0); an entry with no *Verification* (the existing error, no second report, no crash); the switch skipping nothing of it. Point 8: sentence changed and citing file unchanged (listed); citing file changed (not listed); sentence changed in spacing only; *Method* `review`; invariant added; citing file deleted; no citing file; and that no listing changes an exit code. The existing tests keep their assertions.

## Foundation entries

Changed (each by its number, edited in place, with its pair of examples kept):

- WAY-11 (decision): the return step, like the foundation step, writes the accepted settlements in the places the questions of the decisions template give, no longer only in the foundation.
- WAY-293 (decision, changed in part): a choice that binds after the merge goes where the questions place it; where a task or spec excludes an entry the choice stays a row of the questions table as before; in the log of the-way a rule that stands in one skill or template stands there with one sentence of its reason, and is an entry only where it carries a choice with a real cost. The rejected way "an exception for every choice written in the text of a skill or template, with no entry" is kept as rejected for choices with a real cost and in products, and no longer rejected for the rest in the-way.
- WAY-134 (decision): the table has the column *Goes to*; a candidate is also a settlement that goes to guidelines, a skill, or data and code; the cycle writes each kept row in its place.
- WAY-19 (decision): a part of the question an existing entry answers is that entry's sentence where it cannot change without changing that entry; independent questions get their own numbers.
- WAY-05 (decision): the first paragraph answers the main question in one to three sentences, and each attached part has its own paragraph of one to three sentences.
- WAY-12 (decision, with an attached part for D2): a test may hold a decision's sentence, marked by the line `decision:`; *Verification* names such tests by the clause and keeps the pair only for the part no test holds; the check of the foundation reports a changed decision with no invariant, no such test and no pair as an error, and an old one as a listed item.
- WAY-22 (decision): a sentence of a decision that a test holds by a line `decision:` gets no derived invariant; a single text, number, list or location (question 3) stands in the product's data or code with its test and comment and is no entry. The rejected way "moving a checkable sentence out of its decision" stays rejected for sentences and is accepted for such single values.
- WAY-03 (decision, with an attached part for D4): a change that alters a test that holds a decision's sentence names it in its request as it names an invariant test, and names an invariant whose sentence it corrected while no test citing it changed, as the check of the foundation lists it.
- WAY-02 (decision): the line `decision:` carries the number and a quotation of the start of the sentence it holds, and a reference to a decision still names it by its number alone elsewhere.
- WAY-168, WAY-167, WAY-171 (decisions): a guidelines rule that only says how to write stands with its reason in one sentence and *Decision* `none`; one that executes a choice with a real cost names its decision; the guidelines hold rules of their own, so the part of WAY-167's rationale that says they hold no rule of their own is brought in line, and WAY-171 says the field *Decision* may read `none`.
- WAY-172 (decision): a rule with no decision is accepted as a row of the task's table before the code, or at the merge where the cycle found it; only a rule with a decision waits for approval before the code.

Unchanged by the task and read by it: WAY-36 (first threshold, stays), WAY-173 (a rule of the-way's template binds a product only through a decision adopting it), WAY-65 (the model of `decision:` and the basis of point 8), WAY-26 (question 4).

Not written: no invariant, glossary term, environment fact or part-map entry.

### Other decisions of the log the change reaches

Named so the reviewer can check each. Each is read, and none is changed unless the sentence says so.

- WAY-17: its chain "fact → decision → invariant → test" and "a check names its invariant" read the same with a test that names a decision's sentence; no change unless the foundation step finds the chain stated as closed.
- WAY-18: a link is written at one end, the one exception being a decision's invariants; the `tests:` clause names no test, so it adds no second link.
- WAY-35: the questions and the line's form stand once, in the template; steps point to them.
- WAY-38: the new reading uses git and the standard library only.
- WAY-33: the search of the whole foundation at the foundation step finds the rest of the entries that say "tests live only with invariants" or "a rule that names no decision is an example", and brings them in line.
- WAY-61 and WAY-321: unchanged; the switch skips the report of an uncited `test` invariant only.
- WAY-344: each new reading of a file is tested without a field it needs (D9).
- WAY-114, WAY-30, WAY-315, WAY-14: an entry the cycle changes beyond what the human accepted goes to the human; a guidelines rule the cycle found stands in the request among what the human did not see, and is accepted at the merge.
- WAY-115: says the table shows "its kind"; in task mode *Goes to* carries it; a wording touch is the foundation step's to judge.
- WAY-113: the question against a choice the human made, asked at refinement only against a sentence the human said earlier, applies to a row whatever its place.
- WAY-126, WAY-124: a projected entry and the readiness of a task are unchanged.
- WAY-169, WAY-170, WAY-174: a guidelines rule that names a changed decision is brought in line; the check of references reads no *Decision* `none`; the skills of guidelines keep asking for decisions, a rule with no decision coming through a row.
- WAY-256, WAY-265: a changed skill puts a fragment in the file beside it that a step names; the changes here are lines of existing files and need no new file.
- WAY-60, WAY-07, WAY-10, WAY-01: no new invariant; entries are edited in place; the review reads the whole change.
- WAY-328: no part is added to the part map.

Read by title only, as bearing nothing here: WAY-41, WAY-52, WAY-53, WAY-84, WAY-85, WAY-89, WAY-101, WAY-102, WAY-103, WAY-104, WAY-121, WAY-122, WAY-123, WAY-137, WAY-138, WAY-165, WAY-166, WAY-267, WAY-270, WAY-322.

## Left to the maker

- The exact paragraphs of the thirteen entries and of the sentences of the template, as long as they say what is above; the numbering of the questions inside the bullet; the wording of the messages of the script, which begin as D2 and D4 give (a position, `listed:` for a listed item) and never contain the text `N error` or `N errors` of the count line, so that a test reading that line is not satisfied by a listing.
- How the base is read (which git commands), how the working tree is compared, the helper names, the docstring of `foundation_check.py` (it states what the script reports, now with the two lists, the base and the line `decision:`), and the lines of `README.md` and `agent-instructions/README.md` that say what the script checks.
- Whether the guidelines template's *Examples* and *Rules* bullets are merged or kept apart, and whether a guidelines rule the cycle found stands in kind 6 or in a new kind of the request template (a new number breaks no reference).
- The names and order of the tests of D9, and which of the script's tests carry `decision:` lines for the new sentences of WAY-12 and WAY-03.
- The ordering of the five edits into slices; the foundation entries and the script are independent of the template wording, but the decisions' texts must be written last, after the files they describe.
- Other places the search of the whole foundation finds that say the old rule (for instance a README line), brought in line in the same change.
