PASS 7d00a48159afae181ec5e749b516588143951c20

# Review of correction 1 (the human's remarks on the request)

Range `3eacbc1..7d00a48`, one commit `7d00a48` "Record the reading of the branch rule of foundations and name it in WAY-16". `git rev-parse HEAD` in my worktree of the head: `7d00a48159afae181ec5e749b516588143951c20`, the head given. The diff changes `foundations/environment_facts.md` (+11, new entry `foundations-branch-ruleset`) and `foundations/decisions.md` (+1/-4, the *Based on* of WAY-16) and nothing else. The merge `3eacbc1` is judged by another reviewer and not by me.

## Findings

### Critical

none

### Important

none

### Minor (within the task; none blocks)

**M1. The quoted reading does not show the account that `current_user_can_bypass` describes, which is the link from the fact to "the owner of the repository may bypass it" in WAY-16.** Place: `foundations/environment_facts.md:278` (the sentence's last clause) and `:280`, `:283` (*Source*, first command).
- What is wrong: the sentence says "the account `mariusznazar`, which holds the permission `admin` on that repository, is reported able to bypass it always". The quoted output shows `"current_user_can_bypass":"always"`. That field describes the account that makes the call, and no line of the quoted output names that account. The second call shows that `mariusznazar` holds `admin`. Neither call shows that the bypass actor `RepositoryRole` with id 5 is the admin role. So, from the quote alone, the step from "role 5 may bypass" and "`mariusznazar` is admin" to "the owner may bypass" relies on a link the quote does not show: either which account ran the call, or the name of role 5. The template says "The sentence says no more than its source says" (`elements/environment-facts/template.md:84`).
- Why it matters: WAY-84's rationale says the quoted reading is "what a reader with access compares with it" (`foundations/decisions.md:2022-2023`). A reader with read access who is not an admin runs the same command and gets `current_user_can_bypass` for their own account, not `always`. They see output that no longer matches the quote and may read the fact as false, even though the rule has not changed. The entry does not say whose call the quote records.
- Why only Minor: the sentence is true. My own run of `gh api user --jq .login` printed `mariusznazar` (exit 0) with the same `gh` 2.88.1 on this machine, and its rerun of the ruleset call gave `current_user_can_bypass` `always`. No reader would take a false meaning from the sentence. The gap is in whether the source can be checked again, not in what the sentence says (by analogy with WAY-364, a departure from the template's form where the content agrees with the world).
- Evidence and fix: rerun output below. Adding `gh api user --jq .login` as a third line of the reading's code block, with its output `mariusznazar` quoted after ` · `, would show the link. A further option is the next finding.

**M2. Nothing in the foundation shows that the integration 15368 is GitHub Actions, the source of the `tests` job in `.github/workflows/tests.yml`.** Place: `foundations/environment_facts.md:278` ("the status check `tests` of the integration 15368").
- What is wrong: WAY-16 says "The result of that run is a check the repository requires before a merge" (`foundations/decisions.md:2527-2528`). The fact shows that the required check is `tests` from integration 15368. The author deliberately left "GitHub Actions" out of the sentence because the reading did not show it. That choice is correct for the sentence as written. But it means the only link between the CI run and the required check is the shared name `tests`.
- Why it matters: it is a small gap in the chain that WAY-16 rests on, and no reader would draw a wrong conclusion from it. A public read closes it: `gh api apps/github-actions --jq '{id, slug}'` printed `{"id":15368,"slug":"github-actions"}` (exit 0). If that line were added to the reading, the sentence could truthfully say "of GitHub Actions (integration 15368)".
- Optional. No decision is wrong without it.

**M3. The first command reads fields the sentence does not rest on.** Place: `foundations/environment_facts.md:283`.
- What is wrong: the template says "The command reads only the fields the sentence rests on" (`elements/environment-facts/template.md:126-128`). The filter `rules: [.rules[] | {type, parameters}]` keeps the rules `deletion` and `non_fast_forward`, and the second command keeps `role_name`, though the sentence names neither. The author's report explains why both rules were kept in the output and left out of the sentence.
- Why only Minor: the rule exists to keep secrets out, and these fields hold none. The only effect is that a change to these unrelated rules would make the quote stale while the sentence stays true. Narrowing the filter to `[.rules[] | select(.type == "required_status_checks")]` would remove that.

## Remarks of the human, as made

- Remark 1 (a done human action, binds no code): nothing to make. The reading matches what the human states: name `foundations_tests`, `enforcement` `active`, include `refs/heads/foundations`, required check `tests` with integration 15368, `strict_required_status_checks_policy` `false`, bypass `RepositoryRole` 5 with mode `always`, and the rules `deletion` and `non_fast_forward`. The only part of his account the reading does not show is the role's name, "Repository admin" (see M1). The correction takes nothing from the human's account as a source.
- Remark 2: **made.** WAY-16's *Based on* now reads `github-required-status-checks · github-ruleset-bypass · foundations-branch-ruleset`. The descriptive `TODO` is gone, and the new fact is named by its identifier alone, as WAY-90 requires (`foundations/decisions.md:2063-2066`). No other line of WAY-16 changed: the diff against `3eacbc1` touches only line 2532 of `decisions.md`, plus the four lines of the `TODO` it replaces. No other entry changed. The new fact is written in the form the template gives for a reading of a setting changed outside the repository, as WAY-84 requires (`foundations/decisions.md:2000-2002`):
  - The source is a reading: `reading: the command below on the GitHub API (api.github.com), with the GitHub CLI gh 2.88.1, whose option --jq filters the answer — “…” · “…”; run 2026-11-15`. The two commands sit in a code block indented under the item, as `template.md:120-125` gives for a command of several lines. The tool and its version are named, and the filter is named as part of that tool.
  - The output is quoted word for word, and the two lines are joined by ` · ` (`template.md:116-118`). The curly quotes “…” around output that contains `"` follow the template's rule for passages of code (`template.md:153-154`). The template's general form shows straight quotes, so this is an extension of a rule given elsewhere, not a departure from it.
  - The quote is what the commands print today: my rerun matches it character for character (check 3).
  - The output holds no secret: names, ids, booleans and a role. Both calls filter their answer.
  - The identifier names what the fact is about, the ruleset of the branch `foundations`, and not a value or an edition (`template.md:23-24`). It is unique in the three files of identifiers (`git grep`, one heading and one reference).
  - The sentence is one sentence about one reading. "Branch ruleset" and "without requiring the branch to be up to date" are read from `refs/heads/…` and `strict_required_status_checks_policy:false`; the live `target` is `branch` (check 3). M1 and M2 cover where the sentence and WAY-16 depend on links the quote does not show.
- Remark 3 (binds no code): nothing to make. The diff touches neither `task-cycle/test_remove_merged_worktrees.py` nor `.github/workflows/tests.yml`.

Remaining marks of the gap: none in tracked files. Searches are listed under check 5. The `TODO` lines left in `foundations/decisions.md` (3907, 4644, 4690, 4728, 4770, 4802, 5829) are other gaps: devil's advocate, roadmap, vertical slices, agent harness. The sentences at `agent-instructions/README.md:68-71`, `installation/README.md:167-169`, `installation/install.py:205-209` and `.github/workflows/tests.yml:5-6` describe the owner's setting as something the product asks of the owner. They are true now and do not say the rule is missing.

## Declined to judge

- The merge `3eacbc1`: judged by a separate reviewer, as the handoff says.
- The request's description, item 2 (still describing the gap as open) and the list of entries in its lower part, which by WAY-114 should now include `foundations-branch-ruleset` with one English sentence: the orchestrator writes these; they are not files of the diff.
- The `TODO` entries of other decisions in `foundations/decisions.md`: other gaps, outside the task.
- Whether `agent-instructions/README.md:70` should name the new fact: not asked for by remark 2; the sentence is true as written.

## Checks run

1. `git rev-parse HEAD` in my worktree of `7d00a48`: `7d00a48159afae181ec5e749b516588143951c20`, exit 0.
2. `git log 3eacbc1..7d00a48 --stat` and `git diff 3eacbc1..7d00a48`: exit 0, two files as above. `git diff --check 3eacbc1..7d00a48`: exit 0. The diff has no CR characters.
3. Repeat of the reading, GET only, `gh version 2.88.1 (2026-03-12)`, run 2026-11-15:
   - `gh api repos/mariusznazar/the-way/rulesets/27308872 --jq '{name, enforcement, include: .conditions.ref_name.include, rules: [.rules[] | {type, parameters}], bypass_actors, current_user_can_bypass}'`: exit 0.
   - `gh api repos/mariusznazar/the-way/collaborators/mariusznazar/permission --jq '{permission, role_name}'`: exit 0.
   - Both outputs, joined as `“<a>” · “<b>”; run 2026-11-15`, found exactly once in `foundations/environment_facts.md` with `grep -cF`: count 1, exit 0. The live rule has not changed since the author's reading. Its `updated_at` is `2026-11-15T11:02:52.014+01:00`, the time the human gives for setting it, and that is earlier than the commit at 11:16.
   - Further reads, GET only, each exit 0: `gh api repos/mariusznazar/the-way/rulesets/27308872 --jq '{target, source_type, source, exclude: .conditions.ref_name.exclude, updated_at}'` gave `target` `branch`, `exclude` `[]`. `gh api user --jq .login` gave `mariusznazar`. `gh api apps/github-actions --jq '{id, slug}'` gave `{"id":15368,"slug":"github-actions"}`.
4. `python -B elements/common/foundation_check.py` (without `--skip-test-citations`): `0 errors`, exit 0. `python -B gate/run_tests.py elements/common`: `Ran 235 tests in 138.155s`, `OK`, exit 0.
5. Searches for remaining marks of the gap, in my worktree of the head:
   - `git grep -n -i -E "no such rule|once the owner has set|not yet set|not set yet|until the owner|owner has set|has not set|no (branch )?rule stands|rule stands yet|no reading"`: exit 0. No hit concerns this rule; the hits are unrelated sentences.
   - `git grep -n "TODO" -- foundations` filtered for `rule|ruleset|branch|owner|required|bypass|reading|status check|CI`: exit 0. Only the text of WAY-71, WAY-84 and other rules, plus the other gaps named above.
   - `git grep -n -i -E "ruleset|required check|branch rule|bypass"`: exit 0. The sentences listed above, all true now.
6. `python -B elements/common/decision_index.py --output … --sections .` and `--section "Environment facts" --section "Scripts and the gate" --part environment-facts --part decisions .`: both exit 0. This was the selection of my own foundation that the handoff asked for.

The full gate was not run: the handoff reserves it for the orchestrator.

## Reach beyond the dispatch

- I selected my own foundation by "Reading the foundation" in `elements/common/way_of_working.md:58-124`, for the parts `decisions` and `environment-facts`, as the handoff asked. From the index I read whole WAY-16, WAY-71, WAY-82, WAY-84 and WAY-90, which the handoff names. I also read whole WAY-73 (a fact stands only while named), WAY-10 (who assesses a change to the foundation) and WAY-114 (what the human accepts of an entry), because their questions bear on a new fact entry. None of them changes the judgement; WAY-114 bears only on the request's description, which I declined to judge.
- `elements/common/rules.md`: I searched it for `identifier` (lines 40-76) to check the form of the identifier and the shared space of identifiers.
- The three live GitHub reads in check 3, beyond the two of the entry: `target`, `gh api user` and `apps/github-actions`. All are GET calls. I made them to judge whether the sentence and WAY-16 rest on what the quote shows (M1, M2).
- `agent-instructions/README.md:64-74`, `.github/workflows/tests.yml:1-10` and `installation/install.py:200-212`: read to judge whether a sentence there marks the gap.

## Working copies

- `.runs/review-correction-1/wt`, a detached worktree of `7d00a48`: removed with `git worktree remove --force` (exit 0), then `git worktree prune` (exit 0).
- `.runs/review-correction-1/sections.md`, `index.md` and `run_tests.log` (the decision index and the test log): deleted, and the empty directory `.runs/review-correction-1/` removed.
- No remainder. Nothing is kept in `reports/` beside this report.

## Unread material

- Of the decision index: WAY-85, WAY-38, WAY-55, WAY-63, WAY-89, WAY-160, WAY-328 and WAY-344 were read only as index lines (sentence and *Scope*), not whole. The decisions listed only by heading were read as headings. None bears on a new fact entry or on one line of a *Based on*.
- `elements/common/rules.md`: read only at the lines about identifiers (40-76), not whole. The rest (language of an entry, `none` and `TODO`) is covered by WAY-71, which I read whole, and by the checker's pass.
- `elements/environment-facts/` skill files (`read.md`, `decide_entry.md`, `draft.md`, `write.md`): not read. I judged against the template and the decisions instead.

## Searches not found or unclear

- A read that names the repository role with id 5 (that is, shows it is "Repository admin"): I tried none, and the author's search of GitHub's REST page of rules found none. Whether any endpoint open to the repository's owner shows this mapping is unclear. M1 offers a way to show the owner's bypass without it.
