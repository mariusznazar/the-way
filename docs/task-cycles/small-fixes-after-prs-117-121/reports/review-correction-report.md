FAIL 5cb2e1fcc28645f2af7f790bc672a131f208daa6

# Review of correction 1 — task `small-fixes-after-prs-117-121`

Range `aefe984..5cb2e1f`, one commit, five files; `git rev-parse HEAD` = `5cb2e1f`, confirmed. The remarks in
`correction-1-remarks.md` (the day advisor in the human's name) take the place of a findings file.

## Each remark

| Remark | Made? | Evidence |
|---|---|---|
| 1 (o1) — an entry that is `the cycle's` because of an added pair quotes that pair word for word under its entry | **made, and no wider in the template** | `task-cycle/skill/request_template.md:301-306` (top part, item 6) and `:498-501` (*Foundation entries*): the rule reaches only an entry marked `the cycle's` for an added *complies*/*violates*, and names the two cases that make no mark (a pair kept until a test holds the sentence; a link in *Relations*), the same limits as `task-cycle/skill/foundation_step.md:30-34`. |
| r1 — README says the listing covers an invariant that reads `test` | **made** | `agent-instructions/README.md:17-18` "an invariant that reads `test` whose sentence a change rewords and whose copy at that commit lacks *Method* or *Part* it lists too, naming the field, whether or not a file citing it changes" — matches `elements/common/foundation_check.py:737-745` (reads `test` now, sentence differs, base copy lacks a field; the citing files are not consulted on that path). |
| r2 — the template row says the line names the invariant and the field, not whether a citing file changed | **made** | `elements/invariants/template.md:176` "…whether or not a file citing it changed, one that reads `test` whose sentence a change reworded and whose copy at the base lacks *Method* or *Part*, the line naming the invariant and the field (WAY-344)" — matches the message at `foundation_check.py:742-745`. |

The clause added to `task-cycle/skill/foundation_step.md:34-35` ("the writer keeps in its report the added
pair word for word for the description to quote under the entry") gives the description's writer the
material the template rule needs; it does what the rule requires.

## The change of WAY-114

`foundations/decisions.md:1226-1228` (binding sentence), `:1240-1242` and `:1246-1247` (*Verification*),
`:1258-1260` (*Rejected*).

- Is it a clarification or a change of meaning? It is a change of the binding text: WAY-114 gains an
  obligation on what the description shows, which it did not hold before (before, nothing in it required
  or forbade quoting a pair). I do not hold it a clarification only. I do hold it within the human's
  consent: its meaning is exactly the behaviour remark 1 orders, so it changes nothing the human did not
  rule, and WAY-30's question is answered by the remark. Without it WAY-114 would still say "each by its
  identifier with one English sentence of its meaning" for the lower part, which a reader takes as the
  whole of what stands there; the WAY-33 search the author made found that, and keeping one decision
  silent beside the template's new rule is the worse state. So I raise no finding on the edit itself.
  It must, however, reach the human as a changed decision — see I1.
- Readability: the sentence reads correctly ("…stands in the description's lower part, and an entry that is
  marked as the cycle's because of a pair of examples its writer added has that pair there word for word
  under it."). Line `:1227` is 131 characters where its neighbours wrap at about 100; Minor m2.

## Findings

### Critical

none

### Important (blocking, within the remarks' scope)

**I1 — WAY-114 gains an added pair of examples, so by the rule this correction writes it is `the cycle's` and its added clauses must be quoted under it; the author's report says it is not.**

- Place: `docs/task-cycles/small-fixes-after-prs-117-121/reports/correction-1-report.md:16` — "WAY-114 is a
  decision that changed by the human's remark, not by an added pair of the cycle; the orchestrator may show
  the added clauses with the entry". The added clauses are, word for word:
  - *complies* (`foundations/decisions.md:1240-1242`): "and an entry that gained a pair of examples the row did
    not give has the pair there word for word";
  - *violates* (`:1246-1247`): "an entry marked as the cycle's for an added pair of examples reaches the merge
    with the pair not shown".
- What is wrong: the remark ordered a rule, not these examples; their wording is the writer's, and no row or
  projected entry carries them. By `task-cycle/skill/foundation_step.md:30-34` and the rule this commit adds
  to `task-cycle/skill/request_template.md:301-306` and `:498-501`, WAY-114 is `the cycle's` (no row carries
  its change at all) with a pair its writer added, so section 6 must say so and the lower part must quote the
  two clauses. "May show" leaves the first application of the new rule optional.
- Why it matters: it is the same gap as I2 of the whole-change review — examples that agents will measure every
  later change by, merged unseen — on the very decision that now requires them to be shown.
- Fix: no commit. Mark WAY-114 `the cycle's` in the correction's report (one sentence of meaning in English and
  in Polish) and have the orchestrator put it under section 6 of the request, with the two clauses above quoted
  under it in *Foundation entries*.

### Minor, within the remarks' scope

**m1 — "each as the entry holds it" can be read as quoting the whole *complies*/*violates* field, not the added clauses.**
`task-cycle/skill/request_template.md:499-501` "the pair word for word, the *complies* and the *violates*
sentence each as the entry holds it". Where the writer appended clauses to an existing pair (WAY-139, WAY-344,
WAY-60, WAY-114 here), "as the entry holds it" points to the whole field, which for WAY-139 is a paragraph
long; `foundation_step.md:34-35` says "the added pair". Suggest "the added *complies* and *violates* sentences
or clauses, each as the entry holds it".

**m2 — One line of WAY-114's binding sentence is not rewrapped.**
`foundations/decisions.md:1227` is 131 characters, its neighbours about 100; `task-cycle/skill/foundation_step.md:35`
likewise. No effect on meaning.

### Outside the scope

none

## Declined to judge

- Finding r3 of the return step's review (a meaning sentence for WAY-344) — the author's report gives it to the
  orchestrator; it is outside this correction's diff.
- Whether the request's description as it stands already quotes WAY-139's, WAY-344's and WAY-60's pairs — the
  description is not in this range.

## Checks run

In a worktree of `5cb2e1f` at `.runs/review-correction/head`:

| Command | Exit | Result |
|---|---|---|
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `python -B gate/run_tests.py task-cycle` | 0 | OK (skipped=1) |
| `python -B gate/run_tests.py agent-instructions` | 0 | OK (expected failures=2, as before) |
| manual: README and template row against `elements/common/foundation_check.py:735-747` | — | agree (r1, r2) |
| manual: line lengths of the changed lines (`awk 'length>100'`) | — | `foundations/decisions.md:1227` 131 |

Not run: the full gate (the orchestrator's, after the start signal).

## Entries read and reaches

WAY-114 whole; WAY-30 and WAY-314 binding sentences (consent to a change of a decision);
`agent-instructions/README.md` "Make the change" (`:33-43`). No guideline applies (no code or test changed).

## Working copies

`.runs/review-correction/head` (worktree of `5cb2e1f`): removed with `git worktree remove --force` and
`git worktree prune`; output files deleted; `.runs/review-correction/` stands empty. Remainder: none.

## Unread material

none of the dispatch. WAY-10, WAY-134 and WAY-25, named in WAY-114's rationale, were not opened: they do not
bear on the insert.

## Searches not found or unclear

none
