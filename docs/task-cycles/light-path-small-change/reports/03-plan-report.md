# Plan report — light cycle for a small change (implement-task, step 8)

Planner: general-purpose agent, Opus 5.5, using Superpowers 6.4.1 `writing-plans` (read in full).
Inputs: `spec.md` (revised), `task_frozen.md`, `reports/02-spec-review.md`, `cycle.md` (C1–C7), and
at base c64a607: `agent-instructions/README.md`, `task-cycle/skill/SKILL.md`,
`task-cycle/record_template.md`, `elements/decisions/skill/SKILL.md`, `elements/decisions/template.md`,
`elements/invariants/skill/SKILL.md`, `elements/common/way_of_working.md`, `elements/common/rules.md`,
the WAY-13/1, WAY-125/1 and `foundation-change-path/1` entries, the three format guards'
`--help` and their placeholder and merge checks, `relation-model/fingerprint.py`,
`installation/install.py`.

## Result

Finished, with no questions. Plan: `.../light-path-small-change/plan.md` (not committed; `.runs/`
is ignored). No repository file was edited; `git status` of the worktree is clean.

## What the plan holds

- **Task 1, the foundation step** (orchestrator, outside `subagent-driven-development`, through
  `record-decision` and `record-invariant`): exact old and new text for WAY-13/1 (one block,
  binding part through *Rejected*), WAY-125/1 (two blocks, leaving *Based on* untouched) and the
  `foundation-change-path/1` *Derives from* line; *Approved by* `Mariusz, merge of <request link>`
  for both; *Rationale*/*Rejected* kept as italic paragraphs; the WAY-33 search commands with
  their expected hits; fingerprint computation from the file's own bytes (`awk` extract to a file,
  `fingerprint.py <` in Git Bash); guards with `--base none --merge-onto none` and their expected
  counts; the `--merge-onto c64a607` diagnostic, including a red run before the invariant link is
  renewed; the meaning sentences to keep for the request; one commit by explicit paths.
- **Task 2** — `task-cycle/skill/SKILL.md`, the six edits of spec §4 (exact old/new text), checks
  for the one-line front matter, line lengths, placement and step references, the §5 acceptance
  reading via `git diff --word-diff`, tests, commit, then `installation` tests on the commit.
- **Task 3** — `task-cycle/record_template.md`, the four edits of spec §6, checks, commit.
- Review Focus (five lines, each pinned to a step), a table of runnable checks with baselines and
  expected results, and the list of what stays unchecked. TDD is stated as not applicable (text
  only); the red/green analogue is the stale-link diagnostic in Task 1 Step 10.

## How the plan was verified

I cloned the worktree into my session scratchpad (a separate repository, not the worktree), checked
out c64a607, and applied every Old/New block of `plan.md` by a script that parses the plan itself.
Results:

- each of the 14 old texts occurs exactly once; `git diff --numstat`: decisions 68/35, invariants
  1/1, record template 21/2, skill 62/12;
- fingerprints of the written file: WAY-13 `97b17d59`, WAY-125 `68b2d563` (spec values);
- every new wording equals the spec's after whitespace normalisation (skill §4.1–4.6, template §6,
  decision fields §7.1–7.2);
- guards `--merge-onto none`: decisions 0/7/5, invariants 0/0/3, glossary 0/0/5;
- diagnostic `--merge-onto c64a607`: decisions 4 errors (two "differs from its copy", two
  placeholder), 7 warnings, 2 unchecked; invariants 0/0/1; before the link renewal, invariants
  1 error naming `WAY-13@c6b33aa9`;
- tests on the simulated commit: `installation`, `gate`, `elements/decisions`,
  `elements/invariants` OK; `task-cycle` NO TESTS RAN;
- line lengths: only the one-line front matter of the skill and the existing 107-character table
  header of the template exceed 100.

## Findings for the orchestrator (no question; each is handled in the plan)

1. **Spec §11.4 says "nothing new expected" from the decisions guard; two new warnings are
   expected.** The guard warns on every `*Approved by*` holding the placeholder `merge of <request
   link>` (`elements/decisions/format_guard.py:654-655`). The plan expects 7 warnings, not 5, and
   uses the count as the check that both *Approved by* fields changed.
2. **`installation/install.py` reads the skill's `description` with `^description: (.+)$`**
   (`installation/install.py:111`), so a wrapped description would install a truncated trigger in
   every product. The spec does not name this; the plan adds a one-line check and
   `python -B gate/run_tests.py installation` (16 OK at base and on the simulated change) after the
   Task 2 commit, since the installer reads committed files.
3. **The WAY-13 block grows by 11 lines, not by the binding part alone**, so every later warning
   and WAY-125 move by 11 lines; the plan compares warnings by message and edits by exact text.
4. **`task-cycle/skill/SKILL.md:38` cites WAY-125** ("names the borrowed methods and the the-way
   adapter's stage boundaries") and six places cite WAY-13 in prose (sharpness only); all stay
   true. The spec's §7.3 search list did not mention them; the plan's Step 2 lists them as
   expected hits.
5. **Rewrapping policy.** To keep the §5 acceptance reading clean, the plan rewraps only lines that
   hold a changed word and leaves the following line untouched, which leaves short lines at the
   end of steps 4, 6, 9 and 13 (the file already has such lines). The alternative — rewrapping each
   paragraph to its end — gives a tidier file and a noisier diff; cost if wrong: a later style
   commit.
6. **Commit types.** The plan uses `feat(foundations)` for Task 1 and `feat(task-cycle)` for
   Tasks 2–3 (the repository's history uses `feat` for new capability, `fix(task-cycle)` for
   corrections). Commit messages are written to files under the run directory and committed with
   `git commit -F`.

## Self-review

- Spec coverage: §3 → Task 2 section text; §4.1–4.6 → Task 2 edits 2a–2f; §5 → Task 2 Step 5;
  §6 → Task 3; §7.1–7.3 → Task 1; §8 → Task 1 Step 2; §10 → carried by the skill text; §11.1–11.7 →
  task checks; §11.8 and step 12's placeholder swap → "After the plan"; §12 → Global Constraints.
  No gap.
- Placeholders: none besides the intentional `<request link>` and the template's `<…>` slots.
- Names consistent across tasks ("light cycle", "full cycle", `## Cycle`, `- Cycle:`).
- Review Focus: five lines, each with a pinning step.
