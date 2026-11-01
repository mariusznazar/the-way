PASS d78f148

# Review of the fix — logging-guidelines

Range `1740c02..d78f148`, one commit. `git rev-parse HEAD` is the head given. The findings file holds
one finding. Counts for this review: 0 blocking, 2 Minor, 0 out of scope. The six Minor findings and
the one line of Declined to judge in `reports/whole-review.md` were not to be fixed and go to the
request as they stand; see "Places that moved" for their anchors.

## Findings of the findings file

### 1. No rule tells a line of a case flow to carry the identifiers the list names: fixed

The author does not contest it. The defect no longer exists at `d78f148`:

- `product-guidelines/coding/template.md:194-199`: a line of a case flow "carries those of the
  identifiers `### Logging scope` lists that join the events of that case flow, each under the same
  name in every line, the name the list gives it". The third of the three rules now names the list,
  as D3's chosen way has it (`spec.md:142`).
- `foundations/decisions.md:8141-8146`, WAY-275, holds the same clause, so the template does not
  restate the entry differently (WAY-263). The only difference is "the logging scope" for the heading,
  which is how the entry's first sentence already names it.
- The case of the finding: where the list names an order's number and an id of a request and both join
  the events of the case flow, a line carrying the id of the request alone now breaks the rule.
- "The name the list gives it" ties a line's name to the list, the second half of the finding.
- `template.md:270`, "which have nothing left to read", is now true of `### Identifiers in log lines`:
  with the list gone, the rule has nothing to read.
- "The same name in every line" and "so that a search finds the whole case" stay, so row 5's words
  stand. WAY-275's exception for the last-resort handler stands, and its grammar still holds.

## What the fix diff itself brought

Nothing Critical or Important. Two Minor notes.

### Minor

#### A. A secret on the list is now required by WAY-275 and banned by WAY-276, and no relation says which wins

`foundations/decisions.md:8143` has a line carry the listed identifiers that join a case flow.
WAY-276 keeps out a secret that stands on the list. Before the fix WAY-275 did not read the list, so
the two did not meet there. They do now, for a listed identifier that is a secret, and WAY-276's
*Relations* (`:8194`) names only `narrows WAY-272`, where WAY-25 asks the entry that prevails to name
the other. No wrong outcome follows: WAY-276's sentence says the list is an exception "to this second
ban alone", its *Verification* keeps out "an access token that stands on the list", and
`template.md:203-204` says such an identifier "stays out even where it stands on the list". An agent
reading the file meets the answer, which is why this is Minor. Fix, if taken: add `narrows WAY-275` to
WAY-276's *Relations*.

#### B. WAY-275's rationale names the new limit of the rule for events only

`foundations/decisions.md`, WAY-275's *Rationale*: "the rule covers only listed events, which an agent
adds, so a function nobody lists leaves no line". The identifiers rule now has the same limit: a case
flow whose joining identifier is not on the list requires nothing of its lines, and the fix report
says so under its choices. This follows from To do 3 and D3, where the scope settles which identifiers
the product logs, and WAY-274 has the agent add a fitting item in the change that brings it, so I
judge the narrowing sound and no loss of To do 1 or row 5. The entry's rationale just does not yet
state it. The wording I gave in the finding brought this. `settle.md`'s weak points stay as they are,
since To do 4 names those five. Fix, if taken: one clause in the rationale.

## Declined to judge

None.

## Places that moved

The fix adds one line to `product-guidelines/coding/template.md`, so for the request the anchors of
`reports/whole-review.md` in that file below line 198 read one later: finding 4 `:199-200`, its
`:182-183` unchanged; finding 5 `:254-256`; finding 6 `:213-215` and `:246-248`; finding 7 `:275`.
Anchors in `foundations/decisions.md` above WAY-275 do not move.

## Checks run

| Command or method | Result |
|---|---|
| `git rev-parse HEAD` | `d78f148…`, the head given |
| `git diff 1740c02..d78f148` | two files, the two passages the fix report names, nothing else |
| `python -B elements/common/foundation_check.py .` at head | exit 0, 0 errors |
| `python -B gate/run_tests.py instruction-files` at head | exit 0 |
| `python -B gate/run_tests.py agent-instructions` at head | exit 0 |
| `git diff --check 1740c02 d78f148` | exit 0 |
| `git grep 'those of the identifiers' -- '*.md'` | the two passages, no third restatement |
| Manual: the case of the finding, the departure table and WAY-275's *Verification* read against the new text | as above; the *Verification* examples stay true |

`git status` stayed clean.

Not run: the full suite, the cycle's own run; `task-cycle` and `project-level`, which read none of the
two changed files' changed passages and passed at `1740c02`; a test of how an agent acts on the text,
as in the first review.

## Reaches beyond the dispatch

None. `task-cycle/review/fix.md`, the fix report and the findings file are what the dispatch names,
and nothing outside the worktree was read in this round.

## Searches not found or unclear

- Unclear: whether a collision that arises only for a state the rules already forbid, a secret on the
  list, counts as one WAY-25 requires a relation for. Graded Minor in note A on the ground that the
  binding sentence of WAY-276 already states the outcome.
- The first review's points of this section stand unchanged; the fix touches none of them.
