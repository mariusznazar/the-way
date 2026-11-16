PASS 000a7639dc1b819dfa766d6690a7d00b1a3c551e

# Review of correction 1 — relations-todo-for-unwritten-decision

Range: `f496f05f40d5852c3501f28ba8b556a65fe6f64e..000a7639dc1b819dfa766d6690a7d00b1a3c551e`, one commit
("Add a decision's Relations to the descriptive TODO places of WAY-287 and the second required check to
the ruleset fact"). `git rev-parse HEAD` in the worktree is `000a7639dc1b819dfa766d6690a7d00b1a3c551e`, the
head given; worktree clean. Diff read whole: `foundations/decisions.md` (WAY-287, three places) and
`foundations/environment_facts.md` (`foundations-branch-ruleset`, sentence and *Source*).

## Findings

Blocking: none.

### Minor

**m-a — WAY-287's *complies* list still gives no example of a *Relations* `TODO` (outside what the remark
asked; not blocking).** `foundations/decisions.md:7047-7054`: the complies examples name an invariant's
`Rests on: TODO — …`, a decision's `Based on: TODO — …` and an invariant's `Derives from: TODO — …`, but no
decision reading `Relations: TODO — <the decision, and where it is expected>`. The binding sentence
(`:7006-7008`), the *violates* line (`:7064-7067`) and the *Rationale* (`:7082-7086`) now name *Relations*,
so no sentence a reader follows excludes the fourth field; M4 itself noted that a reviewer comparing a
request with WAY-287's examples finds no such case. Remark 1 named the binding sentence, the *Verification*
lines and the *Rationale* "as M4 names them", and M4's places are the violates line, not the complies
examples, so the author kept to the remark. One more example clause would close it; leaving it costs
nothing today.

**m-b — Two reflowed lines of WAY-287 run wider than the paragraph (style).** `foundations/decisions.md:7008`
(119 characters) and `:7084` (117); the paragraph wraps at about 100. The entry already held a 121-character
line (`:7074`) and a 103-character one before the change, and no check covers width in the log, so this is
style only.

## Remarks

- **Remark 1 — made.** WAY-287 now names "a decision's *Based on* or *Relations*" in the binding sentence
  (`foundations/decisions.md:7007`), the *violates* line (`:7066`) and the *Rationale* (`:7083`) — the three
  places M4 names (`reports/review-whole-report.md:90-101`). The diff touches nothing else of the entry:
  identifier, fields, *Rejected* unchanged, no version (WAY-07). The entry now agrees with item 16 of
  `task-cycle/skill/request_template.md:269-274` (four places, citing WAY-287) and with WAY-71
  (`foundations/decisions.md:603-611`, which names *Relations* among the places and says "a change that
  leaves one there puts it before the human"). `elements/common/rules.md:25-27` holds the same four places.
- **Remark 2 — made by this review.** I read WAY-287 whole (`foundations/decisions.md:6994-7120`), its
  *Rejected* included. In the part not read earlier (the end of *Rejected*, `:7113-7120`: one group mixing
  skipped steps with what the request cannot go on without; only the groups holding an item; three
  sections instead of groups; bold lines instead of headings) nothing bears on the change: these options are
  about the grouping of the section, not about which places of a descriptive `TODO` it lists. Of the
  *Rejected* part read earlier, one sentence bears on it and supports it: "Listing both kinds in this
  entry's sentence — … a forgotten change giving the same gap between the decision and this entry" — the gap
  the correction closes. Extending the existing item of descriptive `TODO`s by one field adds no new kind
  of item, so it does not run against the rejected option of enumerating kinds in the sentence. The
  *Rationale*'s mention of WAY-308 "for the relation line it cleaned" is about a different kind of item and
  is untouched.
- **Remarks 3-5 — no change asked, none made.**
- **Remark 6 — made.** The fact `foundations-branch-ruleset` (`foundations/environment_facts.md:294-303`)
  now says the rule "requires the status checks `tests` and `tests-windows`, each of the integration 15368";
  the rest of the sentence is unchanged and still true. I ran the fact's two read commands today (gh
  2.88.1, GET only): the ruleset output and the permission output equal the text quoted in *Source*
  character for character (fixed-string search of `“<ruleset>” · “<permission>”; run 2026-11-16` in the file:
  1 match). The date `run 2026-11-16` is today's. Form against `elements/environment-facts/template.md`: a
  reading with a multi-line command under the line, `reading: the command below`, the service
  (api.github.com), each tool and its version (gh 2.88.1, its `--jq`), outputs word for word joined by
  ` · `, `run <date>`; the identifier names what the fact is about, not its value; edited in place, no
  version; the outputs hold no secret. The sentence says no more than the output does.

## Point (4) — WAY-16 and what rests on the fact

I read WAY-16 whole (`foundations/decisions.md:2655-2708`), its *Rejected* included. No sentence of it
names one check: the binding sentence says CI runs "on every system the product runs on" and "The result
of each such run is a check the repository requires" (`:2659-2663`) — one required check per run, which
with Linux and Windows runs is two, and which the corrected fact now matches (the old fact, one check,
was the narrower one). *Verification* (`:2670-2680`) says "the result of each run is set as a required
check" and names Linux and Windows; *Rationale* and *Rejected* speak of "a result the repository
requires", "a required check with no bypass", "CI on one system alone" — none of them a single named check.
The other two facts of its *Based on* (`github-required-status-checks`, `github-ruleset-bypass`,
`foundations/environment_facts.md:282-292`) are general GitHub documentation and name no check. A search of
the repository (outside `.runs/`) for `foundations-branch-ruleset`, `foundations_tests` and `27308872` finds
only the fact and WAY-16's *Based on* line. The author's decision to leave WAY-16 unchanged holds.

## Point (5) — anything the correction brings that needs a further correction

None beyond m-a. Searches of the repository: `tests-windows` — `.github/workflows/tests.yml:8` ("two
checks, named `tests` (Linux) and `tests-windows`"), `agent-instructions/README.md:73` ("the owner of the
repository sets both as required"), `task-cycle/test_change_file_sizes.py:161` (a comment) and the fact: all
agree with two required checks. "required check"/"requires check" — `installation/README.md:174` ("The
result of each job is a required check"), WAY-16, a third-party quotation at `foundations/decisions.md:9414`
and an unrelated skill line: none states one check as the rule. For WAY-287: a search for a descriptive
`TODO` or gap beside "decision's *Based on*" finds only WAY-71's own *violates* line (`:633`, about a bare
`TODO`, a different matter and the task's own), the environment-facts template (`:102`, about facts only,
where *Relations* does not apply) and `elements/common/rules.md:27` (four places already). No script of
`task-cycle/` lists the fields (no `.py` file there names "Derives from"), so no code waits for a change.

## Declined to judge

- M5, N1, N2, m1 — named by the handoff as going to the request's list; not re-graded.
- WAY-71's *violates* wording at `foundations/decisions.md:633` (bare `TODO` places) — the task's own change,
  reviewed in the review of the whole change, not part of this correction's diff.

## Checks

- `git rev-parse HEAD` — `000a7639dc1b819dfa766d6690a7d00b1a3c551e`, matches the given head; `git status
  --short` empty.
- `gh api repos/mariusznazar/the-way/rulesets/27308872 --jq '…'` (the fact's command) — exit 0; output
  shown above in remark 6.
- `gh api repos/mariusznazar/the-way/collaborators/mariusznazar/permission --jq '{permission, role_name}'` —
  exit 0; `{"permission":"admin","role_name":"admin"}`.
- Fixed-string comparison of the two fresh outputs, joined as *Source* joins them with the date, against
  `foundations/environment_facts.md` (`grep -cF`) — exit 0, 1 match.
- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`.
- `python -B gate/run_tests.py elements/common` — exit 0, 257 tests OK.
- Line widths of WAY-287 before and after (`awk` over `:6996-7094` of both trees) — manual, gave m-b.
- Not run: the full gate (the handoff forbids it; CI is the final gate).

## Reach beyond the dispatch

- `foundations/decisions.md:599-663`, WAY-71 whole — to confirm the decision WAY-287 should agree with.
- `task-cycle/skill/request_template.md:268-279` (item 16) — the text WAY-287 must agree with.
- `elements/common/rules.md:25-27` — the shared rule of form, for the list of places.
- `elements/environment-facts/template.md`, whole — the form of the fact (named by the handoff).
- `foundations/environment_facts.md:282-303` — the fact and the two other facts of WAY-16's *Based on*.
- `foundations/decisions.md:2655-2708`, WAY-16 whole, and the first decisions after it only to see where
  it ends — point (4).
- `reports/review-whole-report.md:80-109` and its *Unread material* lines — M4's places and what the
  earlier review left unread.

## Working copies

None made; `.runs/review-correction/` was not created.

## Unread material

none

## Searches not found or unclear

- No script in `task-cycle/` names "Derives from" — searched to see whether code lists the places of a
  descriptive `TODO`; none found, which I take as no code to change (the orchestrator writes item 16 by
  hand from the template).
