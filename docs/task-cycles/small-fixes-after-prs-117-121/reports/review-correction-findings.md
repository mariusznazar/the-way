# Findings of the review of correction 1 (`review-correction-report.md`, head 5cb2e1f), for the fix

The blocking finding, in the reviewer's words. The reviewer's Minor findings m1 and m2 are of a correction review and are not fixed.

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
