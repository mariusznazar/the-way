# Independent assessment brief (WAY-10)

You are the independent assessor of a change to the-way's foundation and invariant tests. Follow
the-way's critique skill, read whole from `/home/user/the-way/elements/common/critique/SKILL.md`
(this checkout), and the files it names. You did not write any of this change. Read-only on
`/home/user/the-way`; never use the Artifact tool or any publishing tool; never ask Mariusz
anything.

- Assessed range: `235b0b4..28b42a2` on branch `claude/gallant-albattani-3k15lc` (base is the
  `foundations` branch). The diff with its commit list and stat:
  `docs/task-cycles/coding-guidelines/reports/assessment/assessed-diff.diff`;
  the file list: `.../reports/assessment/assessed-files.txt`. Read the assessed files at `28b42a2`
  in the checkout as you need them, and the rest of the foundation (`foundations/*.md`) for
  contradictions and duplicates.
- Assess the foundation entries the change writes or edits (`foundations/decisions.md`,
  `foundations/invariants.md`, `foundations/glossary.md`, `foundations/part_map.md`) and the
  invariant tests (`product-guidelines/test_form_check_invariants.py`, the `NAMES` change in
  `installation/test_install.py`), against the code they bind and the rest of the foundation:
  purpose, evidence, cost, source fidelity (WAY-195's quotations against their public sources),
  contradictions, duplicates, and what of the change can be cut, or that nothing can.
- Grade each remark and give its place (`file:line`). Write your full report to
  `docs/task-cycles/coding-guidelines/reports/assessment.md` and return a short
  message: the call, remarks by grade with places, what can be cut.
