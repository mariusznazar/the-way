# Slice 5 report — the task cycle: the reviewer runs the test cases

Executor: general-purpose subagent, Claude Opus 5.5 (`claude-opus-5-5`). Python 3.13.16 (`python3`;
the repository declares 3.14). Worktree `/home/user/the-way`, branch
`claude/gallant-albattani-3k15lc`. BASE `d743c2e`, HEAD `faf43c9`.

## What I implemented

One commit, `faf43c9` — `docs(task-cycle): the reviewer runs the test cases of guidelines rules (S5)`,
changing `task-cycle/skill/SKILL.md` alone; frontmatter untouched (first hunk at line 336).

- **Step 10**, right after "the code reviewer writes the break from the invariant's sentence, runs the
  check on it and reports whether it fails (WAY-69, WAY-08).", the sentence of spec §7:

  > For an invariant a rule of the product's guidelines names with test cases, whose sentence the
  > change adds or alters or one of whose test cases it rewrites, that reviewer also runs the check
  > in a scratch worktree of the commit, once with the invariant's `good` file and once with its
  > `bad` file in place — the pair whose info string names that invariant — and records that it
  > passes with the first and fails with the second, or, for an invariant on the list of violated
  > invariants, that the first adds no failure the commit does not already have and the second adds
  > one, its per-file companion taking the strict reading; the check is not accepted otherwise, the
  > `bad` file is a case beside the deliberate break and never the break, and a test case is applied
  > only in that scratch worktree, never in the task's worktree (WAY-168, WAY-197, WAY-69).

- **Step 11**, right after the return-step reviewer's "recording the required failure before
  accepting it (WAY-149, WAY-69, WAY-08).":

  > Where a rule of the product's guidelines names that check's invariant with test cases, the
  > reviewer also runs the check with the invariant's `good` and `bad` files in a scratch worktree
  > of the commit, as step 10 gives, and does not accept it otherwise (WAY-168, WAY-197).

Nothing else changed. No review of code against guidelines was added (Q5).

## TDD evidence

Not applicable: process prose that no test asserts (brief, *Checks*). No behaviour changed.

## Checks (all exit 0; complete output beside this report)

| Check | Exit | Output |
|---|---|---|
| `python3 -B agent-instructions/skill_entry_points.py` → `entry points are current` | 0 | `slice-5-entry-points.txt` |
| `python3 -B gate/run_tests.py task-cycle` → 41 tests OK | 0 | `slice-5-tests-task-cycle.txt` |
| `python3 -B gate/run_tests.py gate` → 98 tests OK | 0 | `slice-5-tests-gate.txt` |
| `git diff --stat d743c2e..HEAD` → this file alone, 12 insertions, no hunk in lines 1–4 | 0 | below |
| weakest-point check (element mapping, Q5 scan, frontmatter hunk) | 0 | `slice-5-weakest-point.txt` |

Failed checks: none. Unchecked: none of those the brief names.

## Changed files (`git diff --numstat d743c2e..HEAD`)

    12	0	task-cycle/skill/SKILL.md

## Manual check (brief): the sentence in steps 10 and 11, each element of §7, Q5

Element-by-element against spec §7, from `slice-5-weakest-point.txt` (method: a script normalising
whitespace in each step's text and searching for each element's wording; actor: this executor):

| §7 element | Step 10 | Step 11 |
|---|---|---|
| invariant a guidelines rule names with test cases | yes | yes |
| trigger: sentence added/altered or a case rewritten | yes | by "as step 10 gives" (a return-step check's invariant has a new sentence anyway) |
| the reviewer who writes the break runs it (WAY-197) | yes | yes ("the reviewer" of that paragraph is the break's writer) |
| scratch worktree of the commit | yes | yes |
| good file and bad file in place | yes | yes |
| the pair whose info string names that invariant (C18) | yes | by reference |
| records passes / fails | yes | by reference |
| relative reading for a listed invariant (C19) | yes | by reference |
| per-file companion strict (C19) | yes | by reference |
| not accepted otherwise | yes | yes |
| bad file beside the break, never the break (WAY-197, WAY-69) | yes | by reference |
| cases applied only in the scratch worktree | yes | by reference |

Added lines mentioning review against guidelines or a checklist: none (Q5 holds).

## Weakest point (WAY-164)

- **Requirement most likely not met:** "the one sentence of spec §7" at step 11 as well as step 10 —
  I wrote the full sentence in step 10 and a shorter sentence in step 11 that names the cases, the
  scratch worktree and the acceptance and takes the readings, the pair and the worktree rule from step
  10 by reference.
- **Check:** the element mapping above (`slice-5-weakest-point.txt`, exit 0).
- **Result:** step 10 carries all twelve elements; step 11 carries five literally and seven through
  "as step 10 gives". A reviewer who reads the brief as wanting the sentence written out twice would
  grade this a finding; I hold the reference form as the way to make what is settled (C8 says "one
  sentence in steps 10 and 11"), consistent with the file's own cross-references ("Checks added in the
  return step follow step 11's order", "as 'The end of a code review' gives"), and it keeps one
  wording that cannot drift from a second copy.

## Choices settled (how to make, not open design choices)

1. **Step 11 by reference** — as above.
2. **"that reviewer"** in step 10 — names the reviewer who writes the break, as WAY-197 ("the
   reviewer who writes that deliberate break also runs the method").
3. **"never in the task's worktree"** for spec's "never in the working tree" — the skill calls the
   cycle's working tree "the task's worktree" (line 63, step 1).
4. **No "until a gate does" clause** — spec §7's sentence carries none; WAY-197's *Review when*
   (a gate reports it, check by 2027-03-31) is what removes or revises the sentence.

## Sharpness inputs (from the actual diff)

- Parts touched (`foundations/part_map.md`): `task-cycle` only.
- Trust-boundary files touched: none.
- Irreversible operations: none. Not pushed.

## Self-review findings

- Frontmatter unchanged; entry points current; line widths of the added lines within 100.
- The new lines use the file's em-dash style and its citation-in-parentheses form.

## Concerns

1. **A change that only rewrites a case.** The step 10 sentence keeps spec §7's "the check is not
   accepted otherwise"; where a change rewrites a case of an invariant whose sentence and check it
   leaves alone, there is no check being accepted in the cycle, so what is withheld is implicit (the
   rewritten case would be a finding). This follows the spec and WAY-197 word for word; I did not widen
   it.
2. **Scratch worktree vs. "The cycle writes only in the task's worktree" (line 63).** The scratch
   worktree is a git worktree of the product repository, so WAY-140 (effects outside the repository)
   is not touched, but line 63's wording reads narrowly. Spec §7 settles the scratch worktree; I left
   line 63 as it is (outside this slice).
