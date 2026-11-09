PASS 7c3161a20f4d2082c3095f0fbff1e6cb4b3219c2

# Review of fix 1 — Minor findings of the review of the whole change

- Range: `e3fcc20..7c3161a` (one commit, `7c3161a`); `git rev-parse HEAD` in the worktree is
  `7c3161a20f4d2082c3095f0fbff1e6cb4b3219c2` — matches the dispatch.
- Method: `task-cycle/review/SKILL.md`, variant the fix of earlier findings (`task-cycle/review/fix.md`).
  The findings file held Minor findings alone, so only a new Critical or Important finding in the fix
  would fail this review (WAY-162).
- Counts: blocking 0; Minor remaining 0; new Minor 0; out of scope 0.

## Findings of the findings file

- **M1 — fixed.** `foundations/decisions.md:1498-1500` now reads "A change is judged as a whole, once
  finished, so an invariant written before its test within one change may read `test` from its
  writing, and a later slice that writes the test leaves the entry as it is." It agrees with the
  binding sentence (`:1471-1472`, "may read") and with `elements/invariants/template.md:59-61`; the
  rest of the rationale is only rewrapped (the diff changes no other word).
  - The smaller point of M1 (the *Rejected* clause on `TODO`, `:1506-1507`), contested by the author:
    **withdrawn.** The author's reason holds: the clause rejects the value `TODO` as a method held
    until a test exists, and with the finished-change sentence now in the binding part and the
    rationale, "meanwhile" reads across changes; nothing a later author does follows differently from
    it. It was no defect, only a reading.
- **M2 — fixed.** `foundations/invariants.md:162` reads `- **Derives from:** WAY-61 · WAY-321`, and
  WAY-61's *Verification* (`foundations/decisions.md:1482-1483`) opens with
  `invariants: test-method-citation. For the rest, an agent compares the change with the decision:`,
  the same form as the entries at `:18` and `:1132`; the pair of examples is unchanged. WAY-321's
  *Verification* (`:10282`) still names the invariant, so each decision the invariant derives from
  names it, and it names both. The foundation check resolves both references (exit 0 below).
- **M3 — fixed.** `elements/common/foundation_check.py:499` is now
  `"""Report each invariant that reads `test` and no line `check_citations` read cites."""`, and no
  line of the file is over 100 characters (measured). The docstring says the same as before.

## What the fix diff itself broke

Nothing found. The diff touches two foundation entries' text and one docstring; no code path, test
or other file changes. No binding sentence of WAY-61 changed, nor any of the three places question 4
of the task keeps.

## Declined to judge

none

## Checks run

- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`.
- `python -B gate/run_tests.py elements/common` — exit 0, OK (`test_the_way_foundation_passes`
  among them, which cites `test-method-citation`).
- `python -B task-cycle/private_paths_check.py <file>` on `elements/common/foundation_check.py`,
  `foundations/decisions.md`, `foundations/invariants.md` — exit 0 each.
- Manual: line lengths of `elements/common/foundation_check.py` (whole file) and of
  `foundations/decisions.md:1478-1510` measured — none over 100.
- Manual: `git grep` for `For the rest, an agent compares` in `foundations/decisions.md` — the form
  of the new *Verification* line has precedent (`:18`, `:1132`).
- `git status --short` empty after the checks — the worktree is untouched.
- Not run: the full gate (the orchestrator's, WAY-160); `elements/part-map` and `installation` tests
  (the fix touches no file their tests read beyond the foundation, which the check above covers).

## Reaches beyond the dispatch

none — the findings file was my own review report; I read the fix report and the fix diff only.

## Searches not found or unclear

none
