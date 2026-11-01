FAIL

# Review of the spec — logging-guidelines

Reviewed: `.runs/task-cycles/logging-guidelines/spec.md`, against the frozen `task.md` and the entries
the handoff names, at `ea4694e`. Four findings. The three open choices are otherwise settled soundly:
one entry of its own (D1), the words (D2), and the six headings with their place and fields (D3). All
four findings can be fixed by a revision of a line or two, and none reopens a choice.

## Findings

### 1. The exception for listed identifiers is widened from personal data to secrets (changes To do 1 and row 6)

- Spec, D3 table, `### Secrets and personal data`: "no secret and no personal data in the logs, the
  identifiers `### Logging scope` lists excepted".
- Spec, E6: "the logs hold no secret and no personal data, the identifiers on the product's list
  excepted".
- Task, To do 1 and row 6, in the same words: "w logu nie ma sekretów ani danych osobowych, a wyjątkiem
  od zakazu danych osobowych są identyfikatory z listy zakresu produktu".

In the task the exception applies to the ban on personal data alone, and the ban on secrets has none.
In the spec's sentences it attaches to both.

Why it matters: D1 and E4 let an agent add "any identifier of a thing" to the list on its own, with
only the merge to see it. As the spec words it, an identifier of a thing that is also a secret, such
as a session identifier or a reset token, is exempt from the ban once an agent lists it. The builder
is told the wording stays within D3, and the entry is written from E6, so the wider reading reaches
the template, the log and each product's rule. `### Secrets and personal data` is also the rule the
reviewer of a product's change compares with.

Fix: in D3 and E6, tie the exception to the ban on personal data, as the task does.

### 2. A departure from the ban on personal data alone has no form (the builder must guess)

Row 6 and E6 say the ban on personal data is the template's choice, "so a product may depart from it
with a reason". D3 gives a departure only at the level of a heading: "From one rule: that heading
alone holds the marker". Its table reads `### Secrets and personal data` as dropped whole: "nothing
else; `### Recording a failure` is no longer narrowed".

That one heading also carries the ban on secrets, the ban on whole objects and request bodies, and the
precedence over the rule on the cause. So the only departure D3 gives for what row 6 permits also
removes three things nobody chose to remove, and the original error may then write secrets into the
logs.

The question the builder has to answer: what does a product write that departs from the ban on
personal data and keeps the ban on secrets?

Why the answer changes the build:

- If the heading drops whole, the template, the *Weak points* or the question must warn that a
  departure from it takes the ban on secrets too.
- If the rule stays with its personal-data limb removed, D3 and the table of D1 need that form, since
  WAY-171 and `product-guidelines/template.md` give a dropped rule only `none —` and give a narrowed
  one nothing.
- If the intended route is the list, by putting what points to a person on it with the human's
  consent, D3 must say a departure of this sort goes that way.

Recommended: the third. It needs no new form, and the D1 boundary already holds it. A product that
wants more than a list then drops the heading with that warning stated.

### 3. D3 contradicts itself on a departure from `### Logging scope`

D3, "A product that departs": "From one rule: that heading alone holds the marker and the others
stay." D3's table two lines below: dropped `### Logging scope` — "Goes with it: `### Identifiers in log
lines` and `### Business events`, which have nothing left to read".

Under WAY-171 a required rule that goes holds `none —`, so here three headings hold the marker, not
one. The D1 table has the same gap: its row "departs from one rule" covers this case and names no
rules beyond the one.

Why it matters: the template carries both sentences. The first tells the author of a product's file to
keep two rules that read a list which no longer exists. The skill would also put a one-rule departure
to the human without saying that two more go with it, and WAY-174 has the human see what a choice
does.

Fix: except `### Logging scope` in that sentence, or say that a rule whose subject has gone reads
`none —` too, and that the question says so.

### 4. E2 and E5 collide on a line of the last-resort handler, with no precedence (against WAY-25)

- E2: each program has one last-resort handler, "whose line may carry no identifiers".
- E5: "a line of a case flow carries the identifiers".

D2 defines a case flow as what the product does for one case, "from a request or a background job to
its end". A failure no code handled during a request is therefore a line of a case flow, and D9 treats
it so ("does not require them and does not forbid them"). E5 requires what E2 lets go.

D3's table reconciles the two in the template, but the entries do not: E5's row carries no exception,
and "How rows meet the rest" does not mention the pair, though it handles E6 and E2 in exactly this
way (`narrows`, with the area stated).

Why it matters: WAY-25 leaves an unrecorded collision to a human, and `agent-instructions/README.md`
sends a finding "such as two decisions colliding with no precedence written" to Mariusz before the
change goes on. A one-clause fix now spares that stop.

Fix: E5's sentence carries the exception, which WAY-30 allows for one written in advance, or E2 names
E5 as `narrows` with its sentence stating the area. E5 carrying the exception is simpler, and row 5
loses nothing by it.

## Weighed and not reported

- D9's reading of the last-resort line. To do 1 ("nie niesie") and row 2 ("może nie nieść") differ
  within the task itself, the spec names the difference, and the reading it picks satisfies both. No
  finding, apart from the collision in finding 4.
- E7's *Rejected* reading `unknown`, although row 7's source, question 4, keeps two ways not chosen.
  WAY-134's verification reads literally as asking for those two. They answer the form of a line,
  stand in E5 and are no ways of choosing who picks a library, so the build does not go wrong either
  way. The whole-change reviewer may ask about it.
- The refresh's proposal at step 1. Its weak points stand in `settle.md`, read at step 4, but they are
  arguments against adoption, a "yes" reaches step 4, and a "no" loses nothing by not hearing them.
- E9's readiness condition and the example in `reserved_choices.md`. Neither is named in *To do*, but
  each is what To do 3 (`hand_back.md`) and row 7's guess need.

## Claims of the spec checked

- WAY-271 is free. No entry or withdrawn number holds it.
- The part map names no trust boundary in `product-guidelines`, `task-cycle` or `decisions`; in
  `project-level` it names the three scripts alone.
- No test reads the text of the files changed: `git grep` over `*.py` finds their paths only in
  `installation/install.py` and `installation/test_coding_guidelines_installation.py`, and the tests
  that walk skill files name none of them by content.
- `README.md` and `installation/README.md` do not say what coding guidelines hold, and "standing
  check" appears in no skill or template outside `product-guidelines/`.
- A search of `foundations/` for "swallow", "personal data", "hides a failure", "error tracker" and
  "what the product logs" finds no row already stated (WAY-134, WAY-33).
- The five weak points of D5 match questions 1, 3, 5, 8 and 9. The *Rejected* sources of E2–E6 and E8
  match their rows. The D2 words collide with no term of the glossary.

## Reaches beyond the handoff

- WAY-45, `foundations/decisions.md:1094`, its first lines: the spec cites it in D2.
- `elements/common/foundation_check.py:485-511`: to see how guidelines are read.
- `installation/test_coding_guidelines_installation.py` and a search of the tests: the spec's claim on
  tests.
- `README.md:110-125`, and `git grep` over tracked Markdown outside the foundation: the spec's "searched
  once" list.
- `foundations/glossary.md` headings, all of them, for collisions with the words of D2.
- `.runs/task-cycles/logging-guidelines/cycle.md`, its first 30 lines, for the step 4 answers.
- `agent-instructions/README.md`, whole: named by the root `AGENTS.md`.
- `C:\Storage\The Brain\The Brain\.ai\rules\subagents.md`, read alongside the handoff, before its
  restriction was seen. It lies outside the worktree and is a rule on working with subagents, naming
  no product and nothing on logs. Nothing in this review rests on it.
- One read-only Python extraction of the named entries, into the session's scratchpad. The personal
  rule on scripts was not read first, and after the restriction it was left unread.

The designer's report `.runs/task-cycles/logging-guidelines/reports/designer.md` was not read, so that
this reading stays independent of it.

## Searches not found or unclear

- Unclear, in the task: To do 1 and row 2 differ on whether the last-resort line carries identifiers
  (see "Weighed and not reported").
- Unclear, in the foundation: whether WAY-134's "ways not chosen that the row's source keeps" covers a
  source whose ways answer only another limb of its question (E7).
