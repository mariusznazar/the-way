# Return-step handoff (step 11)

You are resumed as this cycle's foundation author for the return step of WAY-11 on the real diff.
You wrote the foundation entries and the invariant sentences; you wrote no code and no check, and
that stays so: an invariant you find here gets its check from another agent and its covered code
from another (WAY-69) — name it and return; the root dispatches them.

- Worktree `C:/Storage/repos/the-way-wt/product-guidelines-styleguide`, head `896071a`; the range of
  the change is `96623ed..896071a` (the foundation stage `96623ed..8ea4679`, slices `8ea4679..9dd9880`,
  final-review fix `896071a`). `origin/foundations` is still `96623ed` (fetched now).
- Read: the diff (`git diff 96623ed..896071a`, by file as you need), the cycle's choice log — the
  questions table of `.runs/task-cycles/product-guidelines-styleguide/cycle.md` (C5–C31) — and the
  ledger `.runs/task-cycles/product-guidelines-styleguide/reports/sdd/sdd-ledger.md` (its rulings
  and notes), the whole-branch review `reports/final-review.md` (its "Ledger lines graded" and
  Minor findings, as candidates only, not as a list to fix).
- Refresh the foundation selection by "Reading the foundation" for the real diff and the current
  foundation.

Do the return step: identify newly learned decisions, rules, uncovered behaviour, environment
facts, terms and part-map changes; compare the touched parts of the foundation with the code. For
uncovered behaviour ask: would changing it in a later task violate a requirement or a settled rule?
If yes, it needs an invariant; if no, it is a replaceable detail kept in ordinary tests and the
change's description — record which, with the supporting requirement or the test path. Do not
inventory every function. Known candidates to settle (no outcome is prescribed):

- the *Part* of `guidelines-reference-current/1`, whose check now runs through `elements-common`
  and `relation-model` code (slice 3 review ⚠️; WAY-62);
- the 1 MiB read limit the form check now applies to a product's decision log and invariants file
  (slice 3 concern, final review grading);
- spec §6.2 listed the part-map change under *Settlements to record*; the skill puts it in *To do*
  (slice 4) — does any entry say otherwise;
- WAY-167 gives `guidelines/<discipline>.md` while the form check and its tests accept
  `guidelines/<discipline>-<part>.md` for every discipline (slice 1 M6, slice 2);
- the guidance sentence's trigger, now "before every merge" (C31) — does any entry say otherwise;
- the skill runs starting-rules research before the first screen and at refresh or extension,
  while WAY-186 is wider (slice 4 concern).

Read the 27 rows of the frozen task's *Settlements to record*: write a row the foundation step
missed. Write a new entry only for a rule no row states; every other choice stays a line of the
choice table. No entry is deferred. Write each entry as the foundation step did (*Approved by*
`Mariusz, merge of <request link>`, *Review when* set by you, fingerprints renewed); keep a Polish
meaning sentence for each in your report. Then run the second whole-foundation search (WAY-33)
against `origin/foundations` `96623ed` and record it.

Checks, outputs saved as `return-*.txt` in `reports/` with command and exit code: the five guards
with the no-main options; `python -B gate/run_tests.py` for every directory you touched and for
`gate` and `product-guidelines`; the fingerprint script; `git diff --check`. Commit by explicit
paths. Report in a "Return step" section of `reports/foundation.md`: candidates found and how each
was settled, entries written or changed, the search, checks, changed files with line counts, any
invariant needing a check author, questions for the root. Return status, commits, checks,
questions.
