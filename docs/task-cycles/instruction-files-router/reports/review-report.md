PASS 634fa3b4e2fdb890dafbbdc5aa2ef0c69df9b931

# Review of the whole change — instruction-files-router

Range `0b8c1bd613b94bce290e49aad9eaf1d0b2587b02..634fa3b` (one commit, `634fa3b`), one author
without a plan; no spec, no slices. `git rev-parse HEAD` in the worktree is
`634fa3b4e2fdb890dafbbdc5aa2ef0c69df9b931`, the head given.

Counts: blocking 0 · Minor 6 · out of scope 0 (and 4 lines of Declined to judge).

## Coverage of the task

| Item | Met by | Verdict |
|---|---|---|
| To do 1 — `SKILL.md` holds the criterion and shared principles; the step names the kind file; no repetitions, no kind file points onward | `instruction-files/SKILL.md:87-94` (table of kinds read after the mode is chosen), `:139-192` (criterion), three kind files | met, with Minor 2 |
| To do 2 — part on skills, per-fragment question, every skill incl. process skills | `instruction-files/kind_skill.md:7-22` | met |
| To do 3 — second question; reword the condition first, rule whole only after a recorded miss | `instruction-files/SKILL.md:148-150`, `:169-173` | met |
| To do 4 — every row shows the criterion whatever the verdict | `instruction-files/judging.md:17-27` | met |
| To do 5 — description names skills; entry points regenerated | `instruction-files/SKILL.md:3`; both `.claude/` and `.agents/` entry points; `skill_entry_points.py` reports current | met |
| To do 6 — "Length has no threshold" replaced by the conclusion from both facts | `instruction-files/SKILL.md:185-192` | met, with Minor 6 |
| To do 7 — one-level rule sourced by a fact, as the maker's recommendation for Claude | `instruction-files/SKILL.md:215-218`; fact `claude-skill-nested-references` | met |
| To do 8 — `instruction-density-accuracy` says accuracy falls as density rises, in its source's words | `foundations/environment_facts.md:56-58` | met; quotes checked against the source |
| To do 9 — the two outside references point where the content now stands | `instruction-files/check_instructions.py:3-4` (docstring only), `product-guidelines/template.md:127` | met |
| Row 1 | WAY-256 (binding sentence, process skills included, WAY-35 carve-out, binds proposals and every change to a the-way skill, unchanged fragments exempt); WAY-128's last sentence now names WAY-256 | met |
| Row 2 | WAY-128 first sentence gains the reworded-pointer case and its evidence threshold, with matching Verification and *Rejected*; asking part in WAY-257 | met |
| Row 3 | WAY-257 | met |
| Row 4 | WAY-256 rationale and *Rejected* (course's "close to zero" not adopted; WAY-100 named) | met |
| Row 5 | WAY-258 | met |
| Row 6 | fact `claude-skill-nested-references`; WAY-258 rationale (Claude only, kept for Codex and Cursor) and *Rejected* (the "under 500 lines" cap) | met; the page does say "Keep the `SKILL.md` body under 500 lines" |
| Row 7 | `instruction-density-accuracy` changed; named in WAY-256 *Based on* | met |

Answers under *Questions to settle*: kept (variant A on process skills, A on length, A on one file
per kind, option 1/3 on shared rules, A′ on the reworded pointer, A on whom the criterion binds, A
on guidelines). *Out of scope*: nothing in the vault, `the-way-global` or the lesson map is touched;
the rebuild of the-way's skills is not started.

**The author's main concern — `instruction-files/judging.md`.** Confirmed as a correct application,
not an addition nobody asked for. To do 1 sets what `SKILL.md` and the kind files hold; it does not
limit the files to those. WAY-258, written by this change, provides for it in words ("or in a file a
step names as WAY-256 gives"), and WAY-256 requires it: the judge procedure, typical defects,
judging in operation, removal and clean-up are needed only in the judge mode. The step names it
directly (`instruction-files/SKILL.md:96-99`) and it points to no further file of the skill.

## Findings

### Critical

None.

### Important

None.

### Minor

**Minor 1 — `instruction-files/SKILL.md:101-137`: the Change, Place and Write procedures were
reworded and stay in `SKILL.md`, against WAY-256, which this change writes.** The author moved the
judge mode to `judging.md` because a mode is a variant only some uses need (author report, choice
2), but kept the other three modes in `SKILL.md` as "unchanged in meaning" (choice 5). Place step 2
did change meaning — "Find the rule's trigger (section 3)" became "Answer the two questions of
'Where a rule stands'" (`:113`); Change (`:103-105`) and Write step 3 (`:133-134`) were reworded to
the kind files. WAY-256 binds "one a change to a skill of the-way adds or rewords" that "only one
step or one variant of the skill needs". Why it matters: the first skill shaped by WAY-256 applies it
to one mode and not to three others, which a later rebuild may take as the reading of "variant". The
cost in context is small (about 35 lines), and none of WAY-256's verification examples ("a page of
rules only its review step uses") is met, so it does not block. Either move the three modes beside
`SKILL.md` or name the reading ("a mode's own short procedure stays in `SKILL.md`") in the request.
Evidence: `git diff 0b8c1bd..634fa3b -- instruction-files/SKILL.md`, lines quoted above.

**Minor 2 — `instruction-files/kind_skill.md:14-16` repeats the one-level rule that stands in
`instruction-files/SKILL.md:160` and `:215-218`.** `kind_skill.md`: "the step names the file
directly, and that file points to no further file"; `SKILL.md:215`: "A step of a route points
directly and one level deep (step → file)". WAY-258: "No rule stands in two of its files"; its
rationale says "A rule kept in two files drifts". The author's own-work check compared sentences of
more than 40 identical characters, and its manual reading did not catch this restatement in other
words; the author also says the check had no positive control. The rule applies to every kind of
file that has a route, so it belongs in `SKILL.md` alone; `kind_skill.md` can stop at "it stands in
a file beside the skill, which that step tells the agent to read". Minor because both wordings say
the same today and the cost is one clause.

**Minor 3 — two tool-documentation sources disappeared with the *Sources* list of
`principles.md`.** The author's report says "tool documentation stays in `tool_loading.md`", but
`https://code.claude.com/docs/en/best-practices` and `https://learn.chatgpt.com/guides/best-practices`
now stand nowhere in `instruction-files/` or `foundations/environment_facts.md` (grep over both).
The new `SKILL.md:16-19` says a principle rests on the fact or the address beside it, so principles
that once rested on that list — e.g. "Matching by description fails in two situations"
(`SKILL.md:210-214`) — now show no source at all. Why it matters: the principles say what they rest
on, and a reader can no longer check these. Either cite the two addresses beside the principles
that rest on them, or say in the request that they were dropped and why.

**Minor 4 — WAY-256 and the reading rule of WAY-125 are not reconciled.** WAY-125 and
`task-cycle/skill/SKILL.md:68-69` say "Each stage agent reads the method of its stage, and what it
names, whole"; the cycle's handoffs read that as "read `SKILL.md` whole, with every file it names"
(this review's own handoff, line 9; `author-handoff.md:12`), that is, everything at the start.
WAY-256's rationale assumes the opposite: "only the instructions of steps not yet reached leave".
If the rebuild of the-way's process skills moves step fragments into files beside them while stage
agents keep reading every named file at the start, the reduction WAY-256 is based on does not happen
for the skills it most aims at. The author's WAY-33 note ("WAY-125 fits a step file read when its
step comes") reads "whole" as "complete", not "at the start", and that reading is plausible. The
handoffs show the other reading is the one in use, though. Nothing breaks today, since no process
skill has been rebuilt yet. Recommend naming this in the request as an open point for the rebuild
task, or a clarifying clause in WAY-125 ("each step's file when the step comes"), which changes
WAY-125's meaning and is the human's call (WAY-114).

**Minor 5 — reflow leftovers.** `foundations/decisions.md`, WAY-128 *Rejected*: the edit leaves a
short line "stand today — every" before "unchanged line would become…". And
`instruction-files/check_instructions.py:4` is now 123 characters, while the rest of the docstring
wraps near 100. Cosmetic only. The checker's behaviour is unchanged: the diff of that file touches
docstring lines 3-4 only.

**Minor 6 — `instruction-files/SKILL.md:186-188` states `single-rule-compliance` more broadly than
the fact does.** The fact says none of the four variables "produces a detectable contrast after
multiple-testing correction" in compliance with "a trivial target annotation". The principle says
they "showed no detectable effect on compliance with one rule". Dropping "trivial" and "after
multiple-testing correction" widens the finding the length conclusion (To do 6) rests on. Add both
qualifiers back, as the deleted *Sources* entry had them.

## Declined to judge

- WAY-212's two-step route from `AGENTS.md` to `guidelines/coding-<kind>.md` against the
  one-level principle the skill now cites a source for: it existed before, WAY-258 binds only the
  skill of `instruction-files`, and the task does not reach it (the author noted it too).
- Whether `tool_loading.md` (about 2,250 words), read in full at every use (`SKILL.md:51`), should
  be split by WAY-256: its content is untouched, and the rebuild of skills by the new criterion is
  *Out of scope*.
- The long lines of the "which copy governs" block (`SKILL.md:29`, `:40`): they stood like this on
  the base.
- The order of the per-kind tables inside each kind file (one table row per file): it follows the
  base's section 4 and affects no rule.

## Checks run

| Command / method | Result |
|---|---|
| `python -B elements/common/foundation_check.py` | exit 0, "0 errors" |
| `python -B agent-instructions/skill_entry_points.py` | exit 0, "entry points are current" |
| `python -B gate/run_tests.py instruction-files` | exit 0, 104 tests, OK (skipped=5) |
| `python -B gate/run_tests.py agent-instructions` | exit 0, 18 tests, OK |
| `python -B instruction-files/check_instructions.py . --file instruction-files/SKILL.md --file instruction-files/judging.md --file instruction-files/kind_main_file.md --file instruction-files/kind_skill.md --file instruction-files/kind_path_rule.md` | exit 0; 0 errors, 5 `dead-path` warnings, all on example paths (`.claude/rules/`, `x/AGENTS.md`, `.the-way/instruction-files/SKILL.md`, and `_zadania\` in the root `AGENTS.md`) |
| `git diff --check 0b8c1bd..634fa3b` | exit 0 |
| `git ls-files --eol` on the changed files | every file `i/lf` |
| Manual: diff of `check_instructions.py` | only docstring lines 3-4 change; no handling of the files it reads is altered (trust boundary) |
| Manual: grep for `principles.md`, section numbers of the old principles, and the new file names across the worktree (without `.runs/`) | no dangling reference; `tool_loading.md`, `judging.md` and `kind_*.md` are named only by `SKILL.md` |
| Manual: the old `principles.md` and old `SKILL.md`, section by section, against the new files | every section lands somewhere except the two sources of Minor 3 and the two qualifiers of Minor 6 |
| Manual: quotes of `claude-skill-nested-references` against the live page | all three quotes match (the page has `head -100` and `SKILL.md` in code formatting); the page also says "Keep the `SKILL.md` body under 500 lines", which WAY-258 rejects |
| Manual: new quotes of `instruction-density-accuracy` against `https://arxiv.org/html/2507.11538v1` | Figure 2 caption and the § 4.4 sentences match |
| Manual: WAY-256 *Scope* against the parts that hold a `SKILL.md` (Glob `**/SKILL.md`) | covers every part that holds a skill of the-way |

Not run: the full gate (`python -B gate/run_tests.py` without a directory) — the orchestrator's.
Not read: `konwencje_skilli_i_commandow.md` (an optional reference in the handoff; the text was
judged against `knowledge_artifacts.md` and the-way's own decisions).

## Reaches beyond the dispatch

- `elements/common/way_of_working.md` § "Reading the foundation" — to select the foundation, as
  the method gives.
- Decisions read whole: WAY-125, WAY-128 to WAY-133, WAY-192, WAY-212, WAY-245, WAY-254 (*Scope*
  names `instruction-files`), and WAY-256 to WAY-258 (new). WAY-35, WAY-100, WAY-127 and WAY-09 were
  read through the task's quotes, plus a grep of the log for statements on what a skill holds.
- Facts `single-rule-compliance`, `context-file-effect`, `codex-repository-skills`,
  `agent-run-variance` — the principles moved into new files cite them.
- Part map entry `instruction-files`; invariants with *Part* `every`, `agent-instructions` or an
  element part (`repository-file-location`, `skill-rule-source`, `outbound-link-reach`,
  `skill-entry-points`, `instruction-file-imports`, `element-directory-contents`,
  `derived-file-content`); glossary grep for `instruction file`.
- `task-cycle/skill/SKILL.md:66-70` — the stage-agent reading rule behind Minor 4.
- `elements/environment-facts/template.md` (archived-copy form) and the form of archived links
  across `foundations/environment_facts.md`.
- The Anthropic page and the arXiv HTML — to check the quotes of rows 6 and 7.
- `C:/Storage/The Brain/The Brain/.ai/rules/knowledge_artifacts.md` — the handoff's reference for
  judging the text; the new text holds no dates, history or incidents.
