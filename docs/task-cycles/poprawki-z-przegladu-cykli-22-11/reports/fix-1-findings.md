# Findings of the review of the whole change (range 2a2f4106..ae37fca3, head ae37fca3310ce6efe7e7939413b8b7a1205b0ead), in the reviewer's words

Blocking findings (Important), each with the reviewer's mark of contradiction with the settlements, then the Minor finding within the task's scope. Source: reports/review-whole-report.md.

### Important

**I1. Point 3 of the task: what the quoted wording asks of the orchestrator reaches no file the
orchestrator reads.** Place: `task-cycle/plan/SKILL.md:189-195` (the new bullet) against
`task-cycle/skill/planning.md:26-37` ("A slice's handoff") and `task-cycle/skill/SKILL.md:463-469`
(step 9, sub-step 2, what a slice's handoff carries) and `:481-484` (sub-step 4, the retry);
commit `b7d99dfa`.
What is wrong: the accepted wording has three duties that are the orchestrator's — "The handoff of
each later slice lists the tests the plan leaves failing at its base, with their owners", the
executor reporting "a listed test that fails as expected" (which it can do only when its handoff
lists it), and "the orchestrator gives it an owner by editing the plan before the next slice is
dispatched". The change writes them only into `task-cycle/plan/SKILL.md`, the planner's method.
The orchestrator reads "this skill and no method you do not conduct" (`task-cycle/skill/SKILL.md:76-77`,
WAY-125), and it builds a slice's handoff by sub-step 2 and `planning.md` "A slice's handoff",
neither of which names the tests the plan leaves failing; nothing it reads tells it to edit the plan
for a failure no *Goal* names. The one half-sentence added to sub-step 3 ("and the failures its
report names against those the plan lists") makes the comparison a mechanical check whose mismatch
"goes as information to the review", and sub-step 4 still retries an executor that "reports a
failing check of its slice".
Why it matters: an executor of slice 3 that runs "the tests of the code you touched" meets a test
slice 1 left red for slice 4, finds no list of it in its handoff (its section of the plan holds only
its own *Goal*), reports a failing check and is retried a class higher — the failure AIR-708 names
and the task's *Need* gives as its first cause: "reguła stoi w pliku, którego agent nie czyta w
chwili działania". The task's *Miejsca* for point 3 name where the quoted wording stands; they do
not make the orchestrator's duties optional, and the author raises the same gap as doubt (a).
Evidence: the three passages above, read in the worktree at the head; a search of
`task-cycle/skill/` for `leaves failing|tests the plan|failing at its base` finds nothing, while the
same search of `task-cycle/plan/` finds `SKILL.md:191-192` (control).
Contradiction: no

**I2. `decision_index.py` reads the list of withdrawn identifiers with no check of its fields, and
reads a missing column as an empty list of successors.** Place:
`elements/common/decision_index.py:134-149` (`withdrawn_numbers`, `why, successors = (cells + ["",
""])[1:3]`); commit `943d4153`.
What is wrong: the change reworks the script's reading of the decision log — it now reads the table
under "## Withdrawn identifiers" and its columns *Why* and *Successors* — but takes the columns by
position, never by their names in the header, and pads a short row with empty cells. A log whose
table lacks the column *Successors* (or names it otherwise) gives, for a withdrawn number, the line
"`<ID>` is withdrawn: `<why>`; it has no successor" and exit code 0. WAY-344 asks of a script a
change changes, for "the whole reading of each file whose way of reading the change reworks", that a
missing field or one under another name ends it "with exit code 2 and a message that names the file
and the field, … never guessing and never reading the absence as an empty value", and that "each
reading of a file that the rule covers has one test that gives the file without one of the fields it
needs"; its *violates* names "a change that reworks the reading of a file checks the field it added
and leaves the other fields of that file unchecked" and "a changed script's reworked reading of a
file, has no test that gives the file without a field". Here even the fields added are unchecked
and no such test exists. The check of the foundation does not catch the shape either
(`elements/common/foundation_check.py:403` reads `cells[2] if len(cells) > 2 else ""` for the
decision log).
Why it matters: the line "it has no successor" is the answer the agent reads in place of the
decisions it should have read; a malformed table turns a withdrawn number with living successors
into a silent "nothing to read" — the quiet pass WAY-344 exists to stop. `guidelines/coding.md`
("A field missing from a file a script reads") makes this comparison a duty of the review of each
change that changes a script.
Evidence: probe `reports/review-whole-probe-withdrawn/` (input `foundations/decisions.md`, command
and output in `command.txt`): exit code 0 and "GAME-00 is withdrawn: merged into GAME-01; it has no
successor" on the head; the base ends with exit code 2.
Contradiction: yes — WAY-344

**I3. Point 5.1: text with a quotation mark is taken out of the lookup only for the ASCII double
quotation mark.** Place: `instruction-files/check_instructions.py:444` (the characters
`'*<>{}|$…"=,'`), its docstring at `:18-20` and the test
`instruction-files/test_check_instructions.py:323-333`; commit `89ae582c`.
What is wrong: point 5.1 makes "tekst z cudzysłowem" no path. The 17 warnings that the task's
*Context* (point 5) counts as "tekst, który nie jest ścieżką" on loop2 are, at the base: 7 addresses
`#/...`, 2 `.css`, 2 `restrict,command="/usr/local/bin/loop2-deploy"` and 6 `'\''` (the shell idiom
that closes a single-quoted text). The 6 `'\''` hold no `#`, `=`, `,` or bare extension, so they are
the case "tekst z cudzysłowem" stands for — the 2 `restrict,…` are taken out by `,` and `=` already.
The head still warns on all 6; typographic quotation marks, which the-way's own decision template
counts as quotation marks (`"…"`, `“…”`, `„…”`, `elements/decisions/template.md`, "Verification"),
are not taken out either. The author names the 6 as unclear in its report.
Why it matters: under WAY-418, which this change writes, each of those 6 warnings is an Important
finding of the review of loop2's change that moves its pin, and the task's *Out of scope* leaves to
that change only the real warnings — `'\''` is not among them; the noise point 5 is to cure stays in
part.
Evidence: probe `reports/review-whole-probe-quote/` (input `repo/AGENTS.md`, command and output in
`command.txt`): `'\''` and `‘docs/a.md’` warn, `"\""` does not; the base and head scripts on the
local loop2 checkout, read only: base 143 warnings, head 21, of which 6 are `'\''`.
Contradiction: no

**I4. The author's judgment that the change alters no behaviour a user sees disagrees with the
change, and no case of the walk is drawn up.** Place: `reports/author-report.md`, section
"Walkthrough (`walkthrough.md`)"; the commits `0b3a8ab1`, `4efde783`, `2a03c166`, `943d4153`,
`89ae582c`.
What is wrong: the change alters what five commands print and how they end in a terminal —
`decision_index.py --decision` for a withdrawn number exits 0 with a new line where it ended with
exit code 2; `slice_size.py` prints the verdict `fits by ranges of <file>` and exits 0 for it;
`check_instructions.py` prints `INFO` where it printed `WARN`; `gate_times.py` starts `npm` on
Windows where it failed; `run_tests.py` prints another count. WAY-406 requires the walk "for every
change of behaviour that the user sees in the running product — … a command in a terminal", and
its *violates* reads "the author of a change that alters what a command prints reports only that its
tests pass". The author judged "the-way has no running product" and did not read
`task-cycle/change/walkthrough.md`, which `task-cycle/change/SKILL.md:112-113` sends it to for such
a change. The-way's foundation settles no way to its running product, so WAY-406's third paragraph
holds: the walk is not performed "with that reason in the report and in the description of the
request", and "the author … still draws up the cases from the requirements of the task and marks
each as unchecked with that reason" (`walkthrough.md:26-28`). The report holds no such cases.
Why it matters: the request's description, built from the report, would tell the human that no
behaviour a user sees changed, and would carry no list of cases for a check by hand, which is what
WAY-406 gives the human where no way is settled. The author's own runs by hand hold: my runs of the
same commands (checks below) show the behaviour the requirements ask for; what is missing is the
judgment, the cases from the requirements and their state in the report.
Evidence: the author's report, section named above; `foundations/decisions.md`, WAY-406 (lines
7087-7108 at the head).
Contradiction: yes — WAY-406

### Minor (within the task's scope)

**M1. `task-cycle/review/whole_change.md:27-30` names `installation/README.md` with no product
form and gives the reviewer no command for its run.** The sentence added for point 5.4 says "the
check of the product's instruction files, which the product's one command runs as
`installation/README.md` gives, in a run on the head of the change". Elsewhere the file gives the
product form of each path of the-way (`:43-44`, "in a product `python -B
.the-way/task-cycle/change_file_sizes.py`"); in a product the README stands at
`.the-way/installation/README.md`. The reviewer does not run the product's one command (WAY-160), so
"a run on the head" has to be its own run of the script — `python -B
.the-way/instruction-files/check_instructions.py` from the product's root, as the README gives —
which the sentence does not say. A reviewer that reads it as the CI run finds no run before its
review. Evidence: the line itself.
