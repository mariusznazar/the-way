# Fix handoff — the review's blocking findings

Variant of `task-cycle/change/SKILL.md`: **"the fix of a review's findings"**. Read what that variant
names when it comes.

- Worktree, branch and the rules of your first handoff stand. Fix base: `802b56de85c63afdb8ba5a42c83bd1f5ea060260`.
- Findings file: `.runs/task-cycles/styleguide-skill-shape/reports/findings.md`, in the reviewer's
  words. It holds two findings. Fix both, or answer with evidence one you hold wrong.
- The review's other findings are Minor: they are not fixed and go to the request. Do not touch them.
- One fix is allowed; a new blocking finding in it counts as one that remains.

What the fix has to leave right:

- `recognize.md` changes by a word or so, so its count changes: regenerate `word-counts.md` after the
  edit, not before. The figures in the findings file were computed before that edit; yours will
  differ from them by the words the edit adds. The figures the request takes are yours, from the
  regenerated lists.
- `word-counts.md`, the assessment row the finding names, and any sentence in those materials or in
  your report that says "three files" or gives the old figures, agree with the regenerated counts.
- `author.md` keeps what it said; put your account in `fix.md`, and there correct the two statements
  review finding 8 shows wrong: the reason given at `author.md:110` for missing the estimate of about
  5900 words, and the count of 216 lines at `author.md:76`. The request takes the account from
  `fix.md`, so state there what the 5900 gap consists of, by your own figures.
- The orchestrator's ruling on review finding 8's first point: the exclusion at `word-counts.md:8`
  stands. The files `refine-task` sends the session to are equal in both states and stay out of the
  counts; say so in `word-counts.md` in plain words as the cycle's rule.

Run again the checks your change affects, with their commands and exit codes, including
`check_instructions.py` and `tools/verify_reports.py` or its equivalent. Do not run the whole gate.
Commit by paths on the task branch; do not push.

Full report: `.runs/task-cycles/styleguide-skill-shape/reports/fix.md`, with **Searches not found or
unclear**. Return: your status, your commits, a one-line check result naming what failed or did not
run, and the report's path.
