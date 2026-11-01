FAIL 1740c02

# Review of the whole change — logging-guidelines

Range `ea4694e..1740c02`, four commits, one author, no plan, so no slice stands apart. `git rev-parse
HEAD` is the head given. Counts: 1 blocking, 6 Minor, 1 out of scope.

Everything in the coverage below is met save for the one blocking finding. The eight rows, the nine
entries, To do 2 to 5, both questions carried to the cycle and answers 1 to 12, read with their marks
of replacement, stand in the commits.

## Findings

### Important

#### 1. No rule tells a line of a case flow to carry the identifiers the list names

Place: `product-guidelines/coding/template.md:194-197`, the bullet **Identifiers in log lines**, from
commit `aa4a41c`, and `foundations/decisions.md:8143`, WAY-275, from `8b563cd`.

What is wrong. The spec's chosen way for the six rules reads, at D3: "a sixth rule holding both lists;
the identifiers, events and personal-data rules name it" (`spec.md:142`). Two of the three do:

- `template.md:200`: "Each business event `### Logging scope` lists leaves a log line";
- `template.md:204`: "the identifiers `### Logging scope` lists being the one exception";
- `template.md:194-197`: "carries the identifiers that join the events of that case flow, each under
  the same name in every line", with no word of the list.

The departure table rests on the missing link. `template.md:269` says that `### Identifiers in log
lines` goes with `### Logging scope` because it has "nothing left to read". As written it reads
nothing of the list, and it would stand unchanged with the list gone.

Why it matters. The list is the product's promise of which identifiers it logs (To do 3, row 4), and
the rule is the one a change is compared with (WAY-168, To do 5). As written, a change whose lines
carry only an id of a request meets the rule for an order's case flow, since that id joins the events,
while the list promises the number of the order. No rule then requires what the list promises, so a
reviewer has nothing to hold the change to, and a reviewer reading `### Logging scope` alone finds "a
promise and no inventory". Events have a rule of their own for this reason: question 8 turned down
"bez reguły, tylko decyzja produktu" because the promise would act only when someone happened on it.
Identifiers get that outcome by omission. Nothing also ties the name a line uses to "the name it takes
in every line" that the list gives, so the sameness of names rests on each agent happening to read the
later rule for it.

Evidence: the three lines above and `spec.md:142`, `:216`. The table at `spec.md:153` is silent on the
list, so the spec's own row of the heading is narrower than its chosen way, which is where the omission
comes from. The author's own-work script could not see this: it checks that phrases stand, and all of
them do.

The fix is one clause: the bullet says the line carries those of the identifiers `### Logging scope`
lists that join the events of the case flow, under the name the list gives. WAY-275's second sentence
takes the same clause, so that the template does not restate it differently (WAY-263).

### Minor

#### 2. The refresh's check at step 1 needs two files that step does not name

`product-guidelines/coding/recognize.md:27-32`, `product-guidelines/coding/SKILL.md:98`.
`recognize.md` has an agent at step 1 look for "the required headings of the rules on failures and
logs" and propose the rules "as `settle.md` beside this skill words them". It names no heading and does
not say where they stand: the coding template is first read at step 2 (`SKILL.md:102-105`) and
`settle.md` at step 4. `SKILL.md` at step 1 names neither, while its steps 2 and 4 name each such file
"(WAY-265)". WAY-265 and WAY-256 ask that a step's `SKILL.md` line names the file its step's file
points to, with the condition. An agent will most likely open both, since `recognize.md` names one and
the top of `SKILL.md` the other, which is why this is Minor. The risk is one rule of a product's own,
such as `### Logging`, taken for the six.

#### 3. A product that departed from the rules can be asked again at each extension

`product-guidelines/coding/settle.md:31`, `product-guidelines/coding/hand_back.md:9`. Both turn on
whether `guidelines/coding.md` "does not yet hold" the rules. `recognize.md:28` and WAY-278 say that a
heading holding `none —` is no absence, but only for a refresh. At an extension, read literally, a
file of six markers does not hold the rules, so the skill proposes them again and `hand_back.md` wants
the decision among the choices settled. The human's "no" is reopened at every extension, against
WAY-173's "holds in every later task alike". The author's report says of this wording "with no case
that goes differently"; this is one. Fix: the same half sentence as in `recognize.md`.

#### 4. A rule's text carries a reason

`product-guidelines/coding/template.md:198-199`: "since that handler usually does not know what the
case was". The same bullet list says at `:182-183` that a rule carries no reason, the bullets give "what
the product's text says", and `product-guidelines/template.md:82` and WAY-168 hold the same. To do 1
gives the clause as the reason for the task's own rule, the task's Context keeps reasons out of the
template, and D3's row does not have it. A product that copies the bullet writes a rule the review of
that change would ask to remove (WAY-170, its example). Fix: drop the clause; WAY-272's rationale
already carries the reason.

#### 5. The English label stands outside WAY-171's list

`product-guidelines/coding/template.md:253-255`. The author settled that `Personal data:` stays in
English in every product. WAY-171 and `product-guidelines/template.md:104-107` close the list of what
stays in English, and "the rest of the text" follows the product. The label is on no such list and no
entry adds it. No script reads it and nothing goes wrong either way, so this is Minor, but of the two
readings the spec review left open, the one chosen is the one a decision speaks against. Fix: say the
label follows the product's language and only the marker stays, or drop the sentence.

#### 6. How the human's consent to an item is recorded reads two ways

`product-guidelines/coding/template.md:212-214` says an item that points to a person is added "only
with the human's consent, as a new meaning (WAY-274, WAY-172)". WAY-172's first sentence makes a new
meaning "a decision of the product's log, new or changed". `template.md:245-247` says of the same act
"nothing else changes", and WAY-274's rationale (`foundations/decisions.md:8114`) that adding an item
changes no decision. Two cycles can settle this differently, the dispute question 12's first rejected
way warned of, here only for items that point to a person. The cycle stops for the human on either
reading, so nothing goes in unapproved. The wording comes from the spec (D3, `through WAY-172`) and
from question 1. Fix: say the consent stands in the task's document or at a blocked draft request and
writes no decision.

#### 7. A departure from `### Recording a failure` takes more than the table says

`product-guidelines/coding/template.md:274`: "nothing else". That rule alone holds what a failure and
an expected refusal are and what the last-resort handler is, so `### Hiding a failure` keeps a word
with no definition and a wrong password is no longer set apart, and `### Identifiers in log lines` and
`### Secrets and personal data` keep references to what has gone. The spec mandates the row (D3,
`spec.md:221`), and it is still a defect, of a departure few products make. Fix: the row names the
definition as what the kept rules still read, and says where it then stands.

## Declined to judge

- That the audit does not reach the file where a program starts, where the last-resort handler usually
  stands: the task's Context says so, D8 keeps it, and widening the audit is outside the task.

## Coverage

| Item | Met by | Result |
|---|---|---|
| To do 1, five rules, and the rule of scope | `template.md:41-50`, `:165-214` | met, save finding 1 |
| To do 2, proposal on the three routes | `settle.md:31`, `recognize.md:27-32` | met; findings 2, 3 |
| To do 3, four items of the decision | `settle.md:32-54`, WAY-279, WAY-274 | met |
| To do 4, library and five weak points | `settle.md:8-15`, `:83-95`, `new_tools.md` unchanged | met |
| To do 5, two lines naming none of these rules | `task-cycle/review/SKILL.md:66-73` | met |
| Rows 1 to 8 | WAY-271 to WAY-278 | each stands whole; each *Rejected* compared by hand with questions 1 to 5, 8 to 10 and 12: no way missing, none added |
| Spec's E9 | WAY-279 | met |
| Questions carried to the cycle | WAY-279; `case flow`, `the rules on failures and logs` | met |
| Answers 1 to 12 and replacements | read in the replaced form: 9 over 5, 10 over 3, 12 over 1 and the Context | met |

Spec D1 to D9 were each compared with the text. Only D3's chosen way is unmet, in finding 1.

Foundation and other method lines:

- The entries say what the template and the skill say; finding 1 is the one restatement to bring in
  line. No text of the change names a product; a scan of the capitalized words of the added lines and
  a reading found none. The one outside name is the course, as row 3 and WAY-270 give.
- Reserved choice: the change settles none.
- Tests: the change has none, as the spec gives. No invariant test changed.
- Trust boundary and operation that cannot be undone: none, confirmed against the part map.
- Author's own-work check: the requirement it names, each row whole, was met when I read it. It is not
  where the change is weakest. That is how the rules read one another and how the skill leads a human,
  where findings 1 to 3 lie. The check, phrases written by hand, could not catch those, and the report
  says it proves presence and not meaning.

## Checks run

| Command or method | Result |
|---|---|
| `git rev-parse HEAD` | `1740c02…`, the head given |
| `python -B elements/common/foundation_check.py .` at head | exit 0, 0 errors |
| `python -B gate/run_tests.py instruction-files` at head | exit 0, 104 tests, 5 skipped |
| `python -B gate/run_tests.py agent-instructions` at head | exit 0, 18 tests |
| `python -B gate/run_tests.py task-cycle` at head | exit 0, 42 tests |
| `python -B gate/run_tests.py project-level` at head | OK, 268 tests; the printed exit code is that of the pipe to `tail`, so the pass rests on the line `OK` |
| `python -B -m unittest installation.test_coding_guidelines_installation` at head | OK, 2 tests, read from the same kind of pipe |
| `git diff --check ea4694e 1740c02` | exit 0 |
| `git ls-files .runs` | no file tracked |
| Scan of added lines for bare `flow` and for `should` or `will` | none, save a quoted passage of WAY-276 |
| Manual: the skill walked at first guidelines, at an extension on another subject, at a refresh with a yes and a no, and at a later extension of a product that departed | gave findings 2 and 3 |
| Manual: the template read as a product's author, and each departure of the table traced through the rules | gave findings 1, 4, 5, 6, 7 |

`git status` stayed clean after every run.

Not run:

- The full suite: the cycle's own run before the request.
- A test of how an agent acts on the text: a review dispatches no subagent, so the route was walked by
  hand only, and no agent has tried it.
- The other test directories, as no file they read changed.

## Reaches beyond the dispatch

- Foundation, selected as "Reading the foundation" gives, for `product-guidelines`, `task-cycle`,
  `project-level` and `decisions`. Read whole: WAY-05, 19, 25, 27, 30, 86, 90, 100, 104, 121, 124, 134,
  150, 161, 165, 167 to 174, 200 to 204, 208 to 213, 215, 216, 221, 225, 251, 263, 265 to 268, 270, and
  the first paragraph of WAY-256. Not every entry of those parts' scopes was read: they number some 200,
  and I chose by the matters this change reaches. The part map's entries of the three parts, and the
  glossary's terms read off, critical flow, guidelines and standing check.
- `elements/decisions/template.md`, `product-guidelines/template.md`, and the skill's files `kinds.md`,
  `new_tools.md`, `starting_set.md`, `research.md`, `orchestrated_mode.md`: to compare.
- `agent-instructions/README.md`, as the root `AGENTS.md` asks.
- `reports/spec-review.md`, `reports/spec-review-2.md`, `cycle.md`: what they left to this review.
- **One file outside the worktree:** `C:/Storage/The Brain/The Brain/.ai/rules/scripts.md`, read before
  writing a scratch script, as the user's global instructions demand, while the handoff says to stay in
  this worktree's tracked files and the cycle's directory. It is a rule on line endings, console output
  and backslashes, it names no product and nothing on logs, and nothing in this review rests on it. The
  same case as Q3 of the cycle record. No note and no repository of any product was read.
- A scratch script in the session's scratchpad extracted the entries; it wrote nothing in the worktree.

## Searches not found or unclear

- WAY-277's *Rejected*, `unknown`, asked of this review by both spec reviews. Read literally, WAY-134's
  verification wants the two ways under question 4. I judge `unknown` sound and raise no finding: both
  ways answer the form of a line, stand in WAY-275, and say nothing of who chooses a library, so in
  WAY-277 they would be options nobody weighed for its question. The foundation does not say which
  reading holds where a source's ways answer another limb of its question.
- WAY-277 and WAY-268, asked by the designer: whether "the tools the skills of guidelines choose stay on
  those skills' routes" exempts a reserved library, which would need `narrows`. I read that clause as
  belonging to the sentence on "every other choice", so a reserved library is outside it, and a library
  on the skill's route is what the clause covers, so "a cycle chooses none alone" agrees with it. No
  finding. WAY-268's sentence does not settle this in so many words.
- Unclear: whether the audit at step 3 compares code with the six rules at an extension on another
  subject, since they are proposed only at step 4 and `kinds.md:15` speaks of a rule "the task settles".
  The task's Context expects the audit to show where code breaks them. At a refresh with a yes, and at a
  task about these rules, it does.
- Unclear: "each separately running program" is left undefined on purpose (D9), including whether a
  build script is one.
- Not found: any record of an agent having acted on this text. The author says so too.
