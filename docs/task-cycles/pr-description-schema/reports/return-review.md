PASS e6f24b08baec6151035cbdc80516d4f7fd77157b

# Review of the return step's commits — pr-description-schema

Range: `4327974..e6f24b0`, one commit (`git log 4327974..e6f24b0`). `git rev-parse HEAD` is
`e6f24b08baec6151035cbdc80516d4f7fd77157b`, the head the handoff gives; the worktree is clean.
Reviewed against `task-cycle/skill/return_step.md` (WAY-11, WAY-36), the entries the commit writes
or corrects, WAY-256, and the return step's report `reports/return-step.md`, read as claims.

Counts: blocking 0, Minor 3, out of scope 0.

## Findings

### Critical

none

### Important

none

### Minor

**m-1. WAY-292's *Verification* still says what the binding sentence no longer says.**
`foundations/decisions.md:8772-8773`: "the form check passes it; the form check reports a block that
repeats the top part for an English task". The return step narrowed the binding sentence
(`:8763-8765`) to "the form check, wherever it reads the task document as English, holds the block
to `none`", for M-5 of `whole-review-2.md`, but left the *Verification* unqualified. The script
judges no language for a task document with fewer than `MINIMUM_WORDS` (20) words
(`task-cycle/request_check.py:83`, `:269-273`) and then raises no language error (`:424-440`), so an
agent following *Verification* on a short English task whose block repeats the top part would find
"does not comply" where the sentence now holds. WAY-11 asks the return step to correct whatever no
longer matches, and the corrected entry now disagrees with itself. Minor, on M-5's own grounds: a
real task document runs well past 20 words, and the binding part is the sentence, which is now
right. A fix: "the form check reports a block that repeats the top part for a task it reads as
English".

**m-2. One more place writes the description "as step 13 gives" without naming the template.**
`task-cycle/skill/SKILL.md:193-197` (changed by this task in `5b685df`): a stage agent's `blocked`
that no source can help leads to "open the blocked draft request, the question or the missing fact
or permission in its section for the human's decisions, as step 13 gives." The return step's
correction 3 claims "the steps that use the template did not all name it … Each now names
`task-cycle/skill/request_template.md`", by WAY-256 ("a file beside the skill that each of those
steps names"), and corrected the 9.4 stop, step 12 and `blocked_finding.md`, but not this one. The
template's own list of readers (`task-cycle/skill/request_template.md:3-5`) omits this route too
(from the change already reviewed, not this range). Minor: "as step 13 gives" still leads to the
template one hop away, exactly as the three places corrected did; the claim of the report is
incomplete, not the route broken. `reserved_return.md:56` also says only "as step 13 gives", but
the same file names the template at `:67`, so that one holds.

**m-3. Step 12's corrected line runs to 139 characters.**
`task-cycle/skill/SKILL.md:381`: "`task-cycle/skill/request_template.md` as step 13 gives, and open
the request from it as a draft by the pull or merge request route the" — the surrounding text wraps
at 100 (`awk 'length>100'` over the file finds lines 3, 71, 381 and 392; at `4327974` it found 3, 71
and 391, so 381 is new). The report's *Checks* names a run "after the line reflow"; the reflow
reached `blocked_finding.md` and the 9.4 stop but not this line. No rule of the-way sets a width
and nothing reads it, so polish only.

## What holds

- **github-collapsed-section** (`foundations/environment_facts.md:192-196`) has the template's form
  (`elements/environment-facts/template.md`, "Form of an entry"): one sentence, one *Source* field,
  a page without editions with its archived copy and date, two passages of one place joined by
  ` · `, the date read. The sentence says no more than the second passage ("Any Markdown within the
  <details> block will be collapsed until the reader clicks to expand the details."). The archived
  copy is the latest capture the CDX index lists (20261010140709), so it already existed and is the
  closest to the read date. Both passages stand word for word, markup dropped and whitespace
  collapsed, in the live page and in the archived copy, under the heading "Creating a collapsed
  section" (manual check below).
- **WAY-288** (`foundations/decisions.md:8645`) names the fact in *Based on*; its rationale ("stays
  collapsed, so the request opens in English for every other reader") is the citation the fact
  holds, so WAY-90's test — a citation whose falsity calls the decision into question — is met. The
  fact now has a dependant, so it stands by WAY-73.
- **WAY-292**'s binding sentence matches `request_check.py:433-434`: where the task reads as English,
  any block not reading `none` is reported.
- The 9.4 stop (`SKILL.md:297-303`), step 12 (`SKILL.md:380-381`) and `blocked_finding.md:10-14`
  name `task-cycle/skill/request_template.md`, with no change of meaning: each still writes "as step
  13 gives", in the same variant, with the same link and draft.
- Nothing is deferred or proposed for later; no invariant is written; no reserved choice is taken
  (the commit changes only Markdown).

## Declined to judge

- Whether WAY-288 needs a fact for a host other than GitHub (a merge request on GitLab) — the
  decision rests on the-way's own public GitHub repositories and the foundation's other host facts
  are GitHub's alone (`github-closed-pull-request-branch`, `github-private-repository-response`);
  extending it is a question about the decision's reach, not about this range.
- The new fact's place in the file, before `github-closed-pull-request-branch` rather than after it
  — no rule of `elements/environment-facts/template.md` or `elements/common/rules.md` I found orders
  the entries.
- The Polish meanings in the return step's table and the request's *For you to decide* item 6 —
  the request's description is not in this range.
- `foundation_check.py` takes an uppercase word in *Based on* (`github-collapsed-sectionX`) for a
  quoted source and reports nothing (seen in my positive control) — the script is not in this range
  and fact identifiers are lowercase.

## Checks

| Command or method | Exit | Result |
|---|---|---|
| `git rev-parse HEAD` | 0 | `e6f24b08…`, the given head |
| `git diff 4327974..e6f24b0`, `git log 4327974..e6f24b0`, `git show --stat e6f24b0` | 0 | one commit, four files, 20+/13− |
| `python -B elements/common/foundation_check.py .` (worktree) | 0 | 0 errors |
| `python -B gate/run_tests.py task-cycle` | 0 | 92 tests, OK |
| positive control: `git archive e6f24b0` into a scratch repository, *Based on* of WAY-288 changed to `github-collapsed-sectionzz`, `python -B elements/common/foundation_check.py .` | 1 | "`github-collapsed-sectionzz` names no fact"; restored, exit 0, 0 errors |
| manual: `curl` of the live page and of the archived copy 20261010140709; a scratch script (`python -I`) dropping scripts, styles and tags, unescaping entities and collapsing whitespace, searching both passages | — | both passages found in both copies, after the heading "Creating a collapsed section" and before "Further reading" |
| manual: CDX index of web.archive.org for the page, from 2026 | — | latest capture 20261010140709, status 200 |
| `awk 'length>100'` over `SKILL.md` at head and at `4327974`, and over `blocked_finding.md` | 0 | line 381 new at 139 characters (m-3) |
| `grep -rn "step 13"` and `grep -rn "request_template.md"` over `task-cycle`, `agent-instructions`, `elements`, `foundations` | 0 | m-2 |

Not run: the full gate, which is the cycle's.

## Reaches beyond the handoff

- `foundations/decisions.md` WAY-256, whole — the rule the return step's correction 3 cites.
- `elements/environment-facts/template.md`, whole — the form of the new fact.
- `task-cycle/request_check.py:2-44, 82-83, 255-273, 423-440` — what the form check does, for WAY-292.
- `reports/whole-review-2.md` M-5 — the finding WAY-292's correction answers.
- `task-cycle/skill/request_template.md:1-12` — its list of readers, for m-2.
- `elements/common/foundation_check.py:124-200, 225-280, 340-365, 569-591` — why the first positive
  control reported nothing.
- The GitHub docs page and its archived copy and CDX index — to check the fact's source.

## Searches not found or unclear

- A rule ordering the entries of `foundations/environment_facts.md` — not found.
- A rule of the-way setting the width of a line of its Markdown — not found.
