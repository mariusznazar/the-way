# Findings of the review of the whole change — for the fix

Review: `reports/review-whole-report.md`, `PASS 225bf1c5eb30667afb8e5079f6d36d256aebd021`, range `07aa55df..225bf1c5`. No blocking finding. One Minor finding within the task, which the cycle fixes before the request opens (WAY-161), copied in the reviewer's words.

## Blocking findings

none

## Minor findings within the task

1. **Two wrapped lines in the new text run past the 100 columns of their paragraphs** (within the task; polish).
   - `README.md:94` is 105 characters (`whose sentence a change rewords while no file citing it changes. All of these compare the change with the`) and `agent-instructions/README.md:24` is 126 characters (`of the two entries as a whole, and lists any other such invariant. The script \`elements/common/migrate_foundation.py\` brings a`). Every other line of both paragraphs is 100 or fewer (README.md 86-93: 94-100; agent-instructions/README.md 17-23: 94-99), and on the base only one line of agent-instructions/README.md and none of the README paragraph passed 100.
   - Why it matters: nothing is wrong in meaning; the paragraphs were re-wrapped by hand and the joins left two long lines, which makes the next diff of the paragraph noisier.
   - Evidence: `awk '{print FNR": "length($0)}'` over the two ranges (output above). No script checks it.
