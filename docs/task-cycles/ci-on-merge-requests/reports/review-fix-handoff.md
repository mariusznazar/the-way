# Handoff — the review of the fix (you, resumed)

You reviewed the whole change of the task `ci-on-merge-requests` and returned `FAIL 345b6bd`. The
author has made one fix for your three blocking findings and your four Minor findings within the
task. You review that fix once.

- Method: `task-cycle/review/SKILL.md`, and `task-cycle/review/fix.md` as the skill tells for a fix;
  read it whole. Delegation, worktree and the rules of your first handoff
  (`reports/review-whole-handoff.md`) stand: read-only, grades and scope yours, single directories
  only, never the whole gate.
- The range of the fix: `345b6bd832326872f96e301337451762d004c60d..23f08e9` — compute it yourself
  (`git diff 345b6bd..23f08e9`, `git log 345b6bd..23f08e9`) and confirm `git rev-parse HEAD`
  gives `23f08e9...`; three commits (`21777bd`, `827f716`, `23f08e9`), 12 files.
- The findings the fix answers: `reports/review-whole-findings.md` (your words; I-1, I-2, I-3, M-1
  to M-4), and the author's report of the fix: `reports/author-fix-report.md` (its evidence of the
  pages it read: `reports/author-fix-sources-check.txt`), all in
  `.runs/task-cycles/ci-on-merge-requests/reports/`. The report is a set of claims to verify.
- The orchestrator's answers that bound the fix (in `reports/author-fix-handoff.md`): I-1 environment
  facts from pages of GitHub's documentation, with `TODO — ...` in *Based on* where no reading
  exists; I-2 the wait covers every push to a request open for review or waiting only for human
  actions, corrections included, and a request left blocked for a remaining blocking finding, a slice
  failed twice or a reserved choice is out of the wait; I-3/M-4 one edit of the block's sentence;
  M-1, M-2, M-3 as you proposed. Judge whether the fix does what each finding asks and whether the
  answer holds together; a different but sound way is no finding.
- Judge, as the skill gives, whether any finding remains, and whether the fix itself brings a new
  Critical or Important one: in the environment facts it wrote (is each value taken from its page, with
  the address and the date; does a fact say what the page says and no more), in WAY-16, WAY-206 and
  WAY-160 (are the sentences, *Verification*, *Rationale* and *Rejected* in step with each other and
  with the task's rows 1, 2, 4 and 6), in the installer's block and its tests, and in the routes
  `correction.md`, `blocked_finding.md`, `reserved_return.md` and step 12. Trust boundary: yes, as
  before (the installer's block is again a constant string; check that nothing else in
  `installation/install.py` changed). The foundation entries it wrote are those of the author's
  report, "The foundation step"; read each of them whole.
- A Minor finding that remains or that you find new does not block; grade it as usual and say whether
  the task covers it. The author's open points, to judge: a claim that a check can be chosen only after
  it has run, which it could not source and removed from `installation/README.md` while the task's
  *Human actions* item still carries it; the latest archived copy of the Dependabot page holding an older
  text than the live page; two blocked variants of the request template (a question from the foundation
  step, an impossible task) covered by WAY-160's wording only.
- Your report: `.runs/task-cycles/ci-on-merge-requests/reports/review-fix-report.md`, first line
  `PASS <sha>` or `FAIL <sha>`, with the checks you ran (command, exit code), **Unread material** and
  **Searches not found or unclear** (`none` is an answer), and your working copies. Your directory for
  working copies: `.runs/review-fix/`; it is removed before you return.

Working copies: the paragraph of your first handoff, "Working copies", stands word for word.
