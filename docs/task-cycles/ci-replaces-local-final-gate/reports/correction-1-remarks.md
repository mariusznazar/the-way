Uwagi doradcy dnia w imieniu Mariusza

1. Needed from you — the required check `tests-windows` in the rule `foundations_tests`: this stays with the owner, as a change of the repository's GitHub settings, and it does not hold the merge. Until he adds it, the environment fact about the ruleset stays true (the rule requires `tests` only), so leave the fact as it is in this request; its correction will follow his action. Mark the request ready when the correction below is done.

2. Of the eight Minor findings, fix N-3 in this request: add the line in the guidelines that places `process-audit/stage_pricing.py` under the kind `shared-module` (its *Applies to* in `guidelines/coding-shared-module.md`, beside `relation-model`). As your own weak point says, without it the next author who adds a file of that kind finds no row for it. Let the other seven through, no task.

3–4. Accepted.

