Uwagi doradcy dnia w imieniu Mariusza — decyzja Mariusza z 16.11, rano

1. Fix it as the finding says: add "unless it reads `none` or opens with ..." in the four places (the rule's sentence, its test clause and the two comments in the code), so the sentence says what the code does.

2. Fix the small remarks of the reviewers in the same round: the rare shapes of a record listed in item 2 (a second reason word in a detail line, a second attempt with a malformed reason word, a continuation at the left margin, and the two places where the rule is silent). Where a fix would change what the audit answers, make the rule say what the code does and add the test; do not widen the change beyond these.

3. `foundations` moved since this branch was cut: the-way#140 (CI as the final gate) changed `process-audit/audit_count.py` and moved the pricing of stage rows into `process-audit/stage_pricing.py`. Merge the target branch into this one and resolve the conflicts (expected: the import block, two lines of constants, a tuple of file names in one test).

The rest of the request is accepted, including the narrowing of WAY-344.

