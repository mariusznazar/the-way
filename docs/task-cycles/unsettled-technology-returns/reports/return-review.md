PASS 6f34b64b9000760e645e48913e54037eb7103677

# Review — the return step

Range `9849f4b..6f34b64` on `task/unsettled-technology-returns`, one commit, `6f34b64` `docs: hold the
GitHub source of WAY-267 as an environment fact`. `git rev-parse HEAD` is the head given. The diff
touches `foundations/environment_facts.md` (+6) and `foundations/decisions.md` (+3, -5), the counts
the author's report gives. No code, no test and no invariant test changes. No reserved choice is
settled: the range is two foundation entries. Trust boundary and operation that cannot be undone: none
in the range, as the dispatch's answers of step 4 say.

## Findings

**Critical:** none.

**Important:** none.

**Blocking findings:** none.

**Minor:**

1. `foundations/decisions.md:7744-7745`, *Rationale* of WAY-267. The sentence ends "so the request
   holds no finished change for a gate to run on (WAY-160), and after a correction it is the tree the
   request already holds." "It" means "the tree", which stands before "the request", "change" and
   "gate", and the added clause hangs on a "so" whose result is that the request holds no finished
   change. After a correction the request does hold one: "the request's code stands"
   (`task-cycle/skill/reserved_return.md:83`). The sentence does not state the opposite, and what it
   says matches `reserved_return.md:85-86`, so a reader who follows the file is not misled and this is
   no departure under WAY-263. It is polish: the sentence reads better as two statements, the second
   naming its subject, such as "After a correction the tree is the one the request already holds."
   Evidence: the diff of this range and the two lines of `reserved_return.md`.

## What was compared

**The fact enters as a fact (WAY-90, WAY-84, the template's "Which facts are written").** Held, and
this was the claim most worth refuting, since `reports/foundation.md:113` chose the opposite.

- WAY-90 asks for a fact entry for a citation that "once it stopped being true, would call the
  decision into question — a finding about agents or models, the behaviour of a tool the process
  uses". What the host does with a closed request's branch is the behaviour of a tool the process
  uses. The template sends the rest to quotation "as a precedent or a past event", and this citation
  is neither.
- The case against: WAY-267's *Rationale* already says what happens where a host does not keep the
  commits, so a lapse could be read as a cost already counted. It does not settle the matter. That
  text says the next step still has what it needs, and the removal of the branch on the host is the
  one step of the decision git cannot bring back, so a lapse would put that step up for weighing again.
  WAY-90's *Rationale* gives the test as whether the search of whoever changes the fact should find
  the decision (WAY-33), and it should here. I reach the author's conclusion on my own reading.
- WAY-84 itself concerns a setting people change outside the repository, which this is not; nothing in
  it speaks against the entry. It is a precedent only in that `github-private-repository-response`,
  which WAY-84 names, is a fact about this host's behaviour, as the report says.
- WAY-73: WAY-267's *Based on* names the fact, so it has a dependant. WAY-90: by its identifier alone,
  as `foundations/decisions.md:1829` does.

**The form of the entry (`elements/environment-facts/template.md`).**

- Source form: a page without editions, with its closest archived copy, the place, the passage and
  the date read, in the template's order. The page's path names no edition, and the fact
  `github-private-repository-response` takes the same form for a page of the same site.
- Passage word for word, from one run of text, under the place given, in both the live page and the
  archived copy: checked by script (see *Checks*).
- Closest archived copy that already exists: the archive's CDX index (the index `draft.md` names) lists
  captures on 2026-09-14 and 2026-10-16 since 2026-09-01. The second is the one cited, the closest, and
  it predates the read date, so it was not made for the entry.
- The sentence says no more than its source (WAY-80). "Deleted" comes from the heading the passage
  stands under, "On GitHub" from the publisher. It is one fact, in the present tense, with no date-bound
  word.
- The identifier names what the fact is about, lower case with hyphens, and no other entry of the
  shared space of identifiers or the withdrawn lists holds it.
- `outbound-link-reach`: both new links opened with no sign-in (HTTP 200).

**WAY-267.**

- *Based on*: the quotation is gone and nothing else in the repository outside the cycle's reports
  carries the address. The place, the passage and the date moved to the fact unchanged.
- *Rationale*: the old sentence said less than the file. The new one matches `reserved_return.md:45-47`
  on the commit that moved the pin, whose gate step 2 runs (`task-cycle/skill/SKILL.md:48`), and
  `:85-86` on a correction. The binding sentences, *Verification* and the rest of the entry are
  untouched, as the report says. The changed text does what the entry and the file say (WAY-263): no
  second account differs.
- The sentence for the request at `reports/fix.md:90-94` says nothing about what changed, so it stays
  valid, as the report says.

**The return step's rules (`return_step.md`, `foundation_step.md`, WAY-11).**

- The one source the task's cycle rested on as a quotation of a tool's behaviour is now held. The
  report's judgment that `git fetch --prune` needs no fact is sound: the change cites no page for it,
  and were the behaviour to end, the ban would be unneeded while removal by name stands.
- One sentence of meaning in the task document's language stands for each changed entry (WAY-114).
- No entry is deferred. The report's *Concerns* name matters for the request and propose no later
  entry.
- The Minor findings of the earlier reviews did not become entries, as `return_step.md:16` requires.
  The report's choice to leave "ends with its attempt discarded" is of that kind.

**The author's own-work check.** It names the requirement where this change is weakest, the passage
and the name resolving, and its check would catch both unmet. I repeated both by other means.

**Author's claims checked:** the quotations of WAY-90 and the template; `reports/foundation.md`'s two
reasons (`:113`); `github-private-repository-response` named by WAY-84; the file counts; the line
references into `reserved_return.md` and `reports/fix.md`. All hold.

## Declined to judge

- *Based on* of WAY-266 reads `none` while its *Rationale* names lesson m2l4 of the 10xDevs course. The
  entry is neither written nor corrected in this range, `reports/foundation.md:114` argued the choice,
  and WAY-237 likewise names the course only in its *Rationale*. Earlier reviews passed that range.
- The entries of `2dbf1e7..9849f4b` other than WAY-267: the dispatch excludes that range.
- Whether WAY-160 reaches a draft with no code, and WAY-266's `narrows WAY-114`: the report sends both
  to the request, and neither is written by this commit.
- Row 1's narrowing in WAY-265, the report's second concern: from the earlier range, sent to the
  request.

## Checks

| Check | Exit code | What it showed |
|---|---|---|
| `git rev-parse HEAD` | 0 | `6f34b64b9000760e645e48913e54037eb7103677`, the head given |
| `git diff 9849f4b..6f34b64`, `git log --oneline` | 0 | one commit, two files |
| `python -B elements/common/foundation_check.py .` (the reviewed worktree) | 0 | 0 errors; `git status --short` empty after it |
| same, on an export of `6f34b64` in a scratch git repository | 0 | 0 errors |
| same, with the entry removed from the export (mutation) | 1 | `foundations/decisions.md:7720: ... names no fact`; 1 error |
| same, with WAY-267's *Based on* set to `none` in the export (mutation) | 0 | 0 errors: no check reports a fact nothing names, as WAY-73's *Rejected* intends |
| `python -B -m unittest elements.common.test_foundation_check` (in the export) | 0 | 90 tests OK |
| `curl` of the live page, the archived copy and the CDX index | 0 | HTTP 200 for each |
| `python -B <scratchpad>/rev/chk.py` | 0 | the passage read out of the committed entry is one whole `<p>` of both pages; the heading directly above it is the place given in both; a false passage is found in neither |
| CDX query from 2026-10-16, with a wildcard on the address | 0 | one capture, `20261016024619` |
| `git grep`-style searches over the worktree (`grep -rn`) for the page's address, "restore the head" and "the tree equals" in tests | 0 or 1 | the address only in the fact and the cycle's reports; no test holds the changed text |

Not run: the gate, which is the orchestrator's and which the dispatch forbids me; `gate/run_tests.py`,
for the same reason, so the report's 109 tests of `elements/common` stand unrepeated and I ran only the
90 of `test_foundation_check`; the `installation` tests, left to the gate; no agent was run on the
changed text.

## Reaches beyond the dispatch

- `foundations/decisions.md`: WAY-11, WAY-73, WAY-80, WAY-160, WAY-263, whole, for what the return step
  and the fact must do and how a departure is graded. WAY-237, whole, and WAY-265, WAY-266, whole, to
  place the course citation and to read WAY-267 with what it derives from.
- `foundations/invariants.md`: `outbound-link-reach`, for the two new links.
- `elements/common/rules.md` (*References*, *Identifiers*), `elements/environment-facts/skill/` (all
  five files read), for how a fact is written and checked.
- `task-cycle/skill/reserved_return.md`, `task-cycle/skill/correction.md` (lines 1-30),
  `task-cycle/skill/SKILL.md` (lines 37-52, 415-426), `project-level/lead/skill/SKILL.md` (lines 50-80),
  to judge the *Rationale* and the report's `--prune` argument.
- `reports/foundation.md`, `reports/fix.md`, `reports/whole-review.md`, `spec.md`, passages, for the
  earlier choice and the sentence for the request.
- The GitHub page, the archived copy and the CDX index, fetched.

## Searches not found or unclear

- **Whether GitHub keeps a closed request's commits, and for how long.** The page says the head branch
  can be restored and gives no term. WAY-267's *Rationale* reads that as keeping the commits. The
  fact's sentence does not go past the page, and the author's report flags the same gap.
- **Later captures of the page.** The CDX index shows none after 2026-10-16. An index can lag behind
  the archive, so "closest" holds as of what the index shows on the day of this review.
- **Other hosts.** Not looked for: WAY-267 speaks of a host, the fact of GitHub alone, and the decision's
  *Rationale* gives the cost elsewhere.
- **The word "closest" in the template.** It does not say closest to what. I read it as closest to the
  date read, and no other reading changes the capture chosen.
