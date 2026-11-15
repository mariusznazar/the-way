# Report: author, correction 1 (remark 2 of the human)

**Status:** done

## Commits

- `7d00a48` Record the reading of the branch rule of foundations and name it in WAY-16 (on top of `3eacbc1`).
  - `foundations/environment_facts.md`: +11 lines (new entry `foundations-branch-ruleset`, before the withdrawn identifiers).
  - `foundations/decisions.md`: +1 / -4 lines (WAY-16 *Based on*).

## What was made

Remark 2 (carried out): the rule was read by me, and written as an environment fact, and WAY-16 names it.

1. The reading (run by me on 2026-11-15, `gh` 2.88.1, GET only, narrowed with `--jq`; no token or secret is in the output):
   - `gh api repos/mariusznazar/the-way/rulesets/27308872 --jq '{name, enforcement, include: .conditions.ref_name.include, rules: [.rules[] | {type, parameters}], bypass_actors, current_user_can_bypass}'`
   - `gh api repos/mariusznazar/the-way/collaborators/mariusznazar/permission --jq '{permission, role_name}'`
   - Output, word for word: `{"bypass_actors":[{"actor_id":5,"actor_type":"RepositoryRole","bypass_mode":"always"}],"current_user_can_bypass":"always","enforcement":"active","include":["refs/heads/foundations"],"name":"foundations_tests","rules":[{"parameters":{"do_not_enforce_on_create":false,"required_status_checks":[{"context":"tests","integration_id":15368}],"strict_required_status_checks_policy":false},"type":"required_status_checks"},{"parameters":null,"type":"deletion"},{"parameters":null,"type":"non_fast_forward"}]}` and `{"permission":"admin","role_name":"admin"}`. Both exit 0. The entry quotes both lines; I compared each line to the entry by string search, both found.
   - The full unfiltered answer of the first call was also read once to see what it holds (it holds no secret; node id and links only), and is not quoted.
2. The entry `foundations-branch-ruleset` (the identifier names what it is about, not a value). Its sentence: the repository `mariusznazar/the-way` has an active branch ruleset `foundations_tests` that targets `refs/heads/foundations`, requires the status check `tests` of the integration 15368 without requiring the branch to be up to date, its one bypass actor is the repository role with the id 5 in the mode `always`, and the account `mariusznazar`, which holds the permission `admin` on the repository, is reported able to bypass it always. The source is a reading (WAY-84), in the form of the element's template, the two commands in a code block under the line. Marked `row`-less: it is the correction's entry, carried by the human's remark 2.
   - English: the branch rule of `foundations` now exists as the ruleset `foundations_tests`, requires the check `tests`, and lets the owner's admin role bypass it.
   - In the task document's language (the frozen task is written in English; no second sentence is needed beyond this).
3. WAY-16 *Based on*: the descriptive `TODO` (four lines) replaced by the identifier `foundations-branch-ruleset`, after the two facts already there. The rest of WAY-16 I read whole (binding sentences, *Rationale*, *Rejected*, *Verification*): none says the rule is unset or unread, so nothing else in it changed.

## Choices (with the way rejected and the cost if wrong)

- What the sentence does NOT say, because the reading does not show it: (a) that the integration 15368 is GitHub Actions — the reading shows only the number (the human's account says Actions; that is not my source); (b) that the role with id 5 is named "Repository admin" — the answer carries the type `RepositoryRole` and `actor_id` 5 and no role name, and the REST page of rules (https://docs.github.com/en/rest/repos/rules) does not map the number to a name (I fetched it and found no such passage). To tie the bypass to the owner nevertheless, the reading holds a second call that shows the account `mariusznazar` as `admin` on the repository, and the first call reports `current_user_can_bypass: always` for the account that ran it. Rejected: writing "repository admin role" in the sentence (a claim of the human's account, shown by no output); omitting the second call (then the entry would not support WAY-16's "the owner of the repository may bypass it"). Cost if wrong: if the reading account were not the owner, the sentence would still be true as written (it says the account `mariusznazar`), and the owner link would be the repository's path itself.
- The rules `deletion` and `non_fast_forward` stand in the quoted output but not in the sentence: no decision rests on them, and a sentence with more in it would change when unrelated rules change (the template: one reason to change). Rejected: naming them in the sentence. Cost if wrong: a later decision that rests on them adds a sentence (the output is already quoted).
- One fact, not two (a fact about the required check and one about the bypass): the two are one reading of one ruleset and change together.

## Remarks, as made

- Remark 1: a done human action; used only as the pointer to the rule (id 27308872). No account of the human is taken as a source.
- Remark 2: carried out as above.
- Remark 3: no code, no task; I touched neither `task-cycle/test_remove_merged_worktrees.py` nor `.github/workflows/tests.yml`.

## Search for other open marks of the gap (step 3)

Searched `git grep` over the tracked files (the files of this change included; `.runs/` excluded) for: `no such rule stands`, `no reading`, `once the owner has set`, `not yet set`, `not set yet`, `until the owner`, `owner has set`, `has not set`, `branch rule`, `ruleset`, `required check`, and, for `TODO`, the lines with `reading|rule|ruleset|branch|owner` in `foundations`, the READMEs, `installation`, `agent-instructions`, `task-cycle`. Result: no other mark of the gap. The remaining `TODO` lines of `foundations/decisions.md` (the practice of a roadmap, the practice of an agent harness) are other gaps, not this one, and I left them. The sentences that describe the rule as the owner's setting (`agent-instructions/README.md:70`, `installation/README.md:167`, the comment of `.github/workflows/tests.yml:6`, WAY-16's *Verification*) state what the product asks of the owner and are true now; unchanged. The request's description is the orchestrator's and I did not edit it; it still says the gap is open and the orchestrator will need to update item 2 of it.

## Checks

- `python -B elements/common/foundation_check.py` (without `--skip-test-citations`): `0 errors`, exit 0.
- `python -B gate/run_tests.py elements/common`: 235 tests OK, exit 0. (The change touches only `foundations/`, which holds no tests; `elements/common` holds `foundation_check.py` and its tests, which read the foundation.)
- Not run: the full gate (the handoff forbids it); `elements/environment-facts` has no tests directory to run.
- Own-work check: the requirement most likely not met is "no marked gap is left on the main branch". The check: search of the whole tracked tree for a `TODO` that names this reading (`git grep -n "TODO — a reading" -- foundations`: no hit) and the count of `TODO` in `foundations/environment_facts.md` (0), plus the checker's pass, which reports a named fact the file does not hold (exit 0, so the identifier in WAY-16 resolves).

## Reach beyond the handoff

- WebFetch of https://docs.github.com/en/rest/repos/rules to look for a mapping of the actor id 5 to a role name: what — a page of GitHub's REST docs; why — to decide whether the sentence could say "repository admin role"; result — no mapping on the page.
- `gh api repos/mariusznazar/the-way/collaborators/mariusznazar/permission` (GET): to show the role of the account that bears on the bypass. Within the reading only; no setting changed.

## Unread material

none. (WAY-16, WAY-84, WAY-90, WAY-71, WAY-82, WAY-34 were each read to their end; the three GitHub facts read whole; `read.md`, `decide_entry.md`, `draft.md`, `write.md` of the element's skill and its `template.md` read whole. `elements/common/way_of_working.md`'s "Reading the foundation" I did not open: the handoff named the decisions and files to read and the decision index script was not needed for a single entry.)

## Searches not found or unclear

- The mapping of `actor_id` 5 of a `RepositoryRole` bypass actor to the name "Repository admin": not found in GitHub's REST page of rules; not shown by the reading. Left out of the sentence, as above; the human may wish a reader to see the role's name, which only a page open to a reader with access shows.
- `decision_index.py --decision 16`: failed with "no decision 16" (it takes the form `WAY-16`, which I did not retry); I read the entries by their headings with `grep`/`sed` instead.

## Working copies

`.runs/author-correction-1/` held the file `reading.txt` (the output of the reading, kept only for comparison with the entry) and `idx.md` was not made. Removed before return; no remainder.
