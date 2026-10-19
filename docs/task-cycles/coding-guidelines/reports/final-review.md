# Final whole-branch review — coding guidelines (`235b0b4..2eabf42`)

Reviewer: final whole-branch reviewer (fresh, wrote none of the change), Superpowers 6.4.1
`requesting-code-review/code-reviewer.md` from the clone named in the handoff. Read-only on
`/home/user/the-way`; I ran everything in a detached worktree of `2eabf42` under the scratchpad and
removed it afterwards. HEAD, the index and the working tree were not touched.

I read: the handoff; the frozen task whole (To do 1–8, Q1–Q18, K1–K3, rows 1–25, Out of scope);
`spec.md` whole; `cycle.md` whole (C22–C37); `reports/design-rulings.md` (C1–C21); the SDD ledger
`reports/sdd/progress.md`; the whole diff by file: `foundations/decisions.md`, `glossary.md`,
`invariants.md` and `part_map.md`, `product-guidelines/template.md`, `coding/template.md` and
`coding/SKILL.md` in full, the `form_check.py` diff (with the surrounding code it relies on), the
task-cycle sentence, the installer, its README and its tests, and the root README. For the three
test files I read their structure, the coding fixtures and the new installation test; I did not
read every assertion line (they were reviewed per slice). I did it in one pass per area, not by
subagents.

## What I ran (Python 3.13.16 at `2eabf42`; the repository declares 3.14)

| Command | Result |
|---|---|
| `gate/run_tests.py` for `product-guidelines` (137), `installation` (35), `agent-instructions` (18), `task-cycle` (41), `gate` (98), `elements/decisions` (169), `elements/invariants` (233), `elements/glossary` (204), `elements/part-map` (162), `relation-model` (19) | all OK |
| `agent-instructions/skill_entry_points.py` | "entry points are current", exit 0 |
| `product-guidelines/form_check.py .` | 0 errors, exit 0 (the-way holds no `guidelines/`) |
| `reports/gate-final/` | read: all exit 0 except `instruction-files`, 3 failures (Windows network path and macOS `/net`) the base already had |
| My own crafted runs through the invariant-test harness (scratchpad `probe/probe.py`) | the valid coding set passes; a test case holding lines that start with `## `, `### `, `- **Decision:**` and `|` passes (headings and fields inside code are ignored, as they should be); an exemplar row naming two decisions reports the one that does not name the path and kind; a path with a space reports a malformed case and a missing `good` case; a case path `.git/hooks/pre-commit` **passes** (see M3) |
| WAY-195 quotations against the public sources | every Open Mercato quote checked at commit `4374c48` (`AGENTS.md:5,16,61,126,144`, `audit.yml:11,23-24`, `customers/AGENTS.md:7,16,33`, `example/README.md:46-47`, `ci.yml:436,503-506`) and the seven quotes from the CACM PDF: all present, word for word |

Commit order: the foundation entries `a45956f`, `b03c5da`, `05e44b1` and the invariant tests
`64344a3` come before the first code commit `7976b54`. The one later change to the invariant tests,
`dfa9e15`, was written by check author D through the foundation step (C34), not by an executor. No
reference still carries an old fingerprint (`@47d9d53e`, `@681d47ff`, `@3b699a99` appear nowhere
outside `.runs/`).

Deliberate breaks: I read every `reports/sdd/slice-*-break-*.txt` and `slice-4-fix1-rebreak.txt`.
Each names its break and the run, and each run fails: `guidelines-check-form` ×2 and
`guidelines-check-carrier` ×2 (S2), `guidelines-check-kind-index` and `guidelines-check-exemplar`
(S3), `guidelines-check-example-files` (S4: the indented inner fence; "guidelines-form beside
another" caught after the fix; the case left open to the end caught by an ordinary test only), and
the installer's `SKILLS` entry (S11). The method of `gate-guidelines-example-evidence` is `TODO`, so
it has no break, which is correct.

## Coverage of the task

- **To do 1–8:** all present. (1) Template, two forms, WAY-167 and the file-name rule, an invariant
  for every rule (WAY-196), A → WAY-193. (2) The skill: recognize, extend, a new tool left as a
  question with a default recommendation, preferences then research with critique, every part with
  code, ask about every choice by its effect. (3) Exemplar decision, approval (WAY-199), rules a
  script can check, first-file and audit routes, "copy / do not copy" with file:line (WAY-200,
  WAY-201). (4) WAY-202–207 and the template's sections on the standing checks. (5) WAY-168 edit,
  common template section, `gate-guidelines-example-evidence`, WAY-197. (6) WAY-195, including both
  Google conditions it leaves out. (7) The skill's *To do* pointer and the general file's table.
  (8) The form check, the edited `guidelines-check-carrier`, the entry points and `SKILLS`.
- **Rows 1–25:** each has its entry: 1 WAY-167, 2 WAY-198, 3 WAY-200, 4 WAY-199, 5 WAY-202, 6
  WAY-206, 7 WAY-203, 8 WAY-204, 9 WAY-205, 10 WAY-196, 11 WAY-168, 12 WAY-197, 13
  `gate-guidelines-example-evidence/1`, 14 WAY-194, 15 WAY-212, 16 WAY-193, 17 WAY-195, 18 WAY-208,
  19 WAY-209, 20 WAY-210, 21 WAY-211, 22 WAY-201, 23 WAY-207, 24 "exemplar", 25 "standing check".
  Each meaning is the row's, with one exception: row 22 together with row 3 (I1 below).
- **Spec entries:** every entry in spec §8.1–8.6 is present, with the *Verification* level-1
  identifiers standing in each invariant's *Derives from*. Out of scope stays out: `refine-task` is
  not changed, there is no review against guidelines, no automatic gate and no audit by the clock.

## Strengths

- The foundation is faithful and careful. Each new decision carries the human's answer, its
  rejected options and the named weak points: K1 in WAY-203, K3 in WAY-199, K2 in WAY-210, Q13's
  weak point and the C10 flip in WAY-206, and the weak point of a product without code in WAY-204.
  WAY-195's *Based on* quotes from the public sources, and every quote I checked is exact.
- `form_check.py` stays disciplined at its trust boundary. No path of a test case or of a table is
  opened or passed to git (`row_path` and `refused` run before `tracked()` is consulted). Fences are
  parsed once (`fenced_blocks`) and shared by `blocks()`, `prose()` and the case check, so a
  heading or field line inside a case cannot split a rule (I confirmed this by probe). An inner line
  is split the way `check_instructions.py` splits it (`splitlines`), and that was found and fixed
  test-first.
- Template words are read back from the template (`read_coding_words`, the *Status* list, the table
  columns) and a missing one raises `TemplateError`, as for the styleguide. The template stays the
  single source of form (WAY-171).
- The separation of roles holds throughout (sentence author B, check author D, executors S2–S4 and
  reviewers). The one undetected break (S4 I1) went back through the foundation step rather than
  to an executor.
- The installer change is minimal, and its crafted-input test covers both skill directories, all
  three refusals and both preview and apply. It asserts that the tree is untouched and that nothing
  is staged.

## Issues

### Critical (Must Fix)

None.

### Important (Should Fix)

**I1. The skill lets the human choose which kinds of code to audit, with no recommendation, which
narrows rows 3 and 22 (ledger S6 minor 1 / C35, regraded).**
- Where: `product-guidelines/coding/SKILL.md:180-183` ("the human settles which kinds the task
  audits, and a kind left out stays in *Context*, deferred with its reason"). The narrowing
  reaches the foundation in `foundations/decisions.md:6819-6822`, WAY-201's binding sentence: "a
  proposed exemplar for each kind of code **it audits**".
- What is wrong: the human settled that where a product already has several files of a kind, the
  skill audits them (row 3, Q6), and that the audit ends with a proposed exemplar "dla każdego
  rodzaju", for every kind (row 22). This choice was the executor's and is ruled only
  provisionally (C35). The step offers it with no recommendation, which WAY-194 requires for every
  choice; the skill's own "How to show" sits in step 4 and is not tied to this step-3 choice.
  WAY-201's "it audits" then makes leaving kinds out compliant.
- Why it matters: the human who settles this cannot judge code (Q10, WAY-194). Asked "which kinds?"
  with no default, they can leave a kind unaudited, and agents then copy whichever file they find.
  That is exactly the harm WAY-200's rationale and *Rejected* name ("until then every agent copies
  what it finds").
- Fix (one sentence): in SKILL.md step 3, recommend auditing every kind the product holds files
  of, shown by its effect. The human may defer a kind, and the deferral goes into *Context* with its
  reason. Either reword WAY-201 to "for each kind of code the product holds files of", or keep "it
  audits" and list C35 in the request as a narrowing for Mariusz to accept.

### Minor (Nice to Have)

New findings from this review:

- **M1.** The styleguide side of row 11 is not reflected in the styleguide's own template and
  skill. `product-guidelines/styleguide/template.md:12-14` lists the common rules every file keeps
  without "the test cases of a rule", although the coding template's own list
  (`coding/template.md:16-18`) includes them. Its "Writing the file" (end of the file) does not say
  to write the cases, and `styleguide/SKILL.md:55` ("write a check for each new invariant") does
  not ask the check to read a case at a new path, as `coding/SKILL.md:61-63` does. The form check
  catches a missing case, so nothing passes unseen. The cost is that a styleguide script written
  without that instruction may be unable to evaluate a new-path case, which only the reviewer would
  find. This is a gap in the spec, whose §3.1 lists no styleguide file. Fix: one clause in each of
  the three places.
- **M2.** WAY-168's change becomes a breaking change for a product that moves its pin. Every
  existing rule of `guidelines/` that names an invariant other than `guidelines-form` (today: the
  styleguide's script rules) starts failing `guidelines-form` until it gains its `good` and `bad`
  cases. Spec §6.5 has the request name what moving the pin changes for the skill only. Fix: the
  request's pin line also names this, as its promise level requires.
- **M3.** The path of a test case may name `.git/...`.
  - What: `refused()` (`form_check.py:1202-1214`, applied at `:1014`) refuses absolute, `..`, `\`,
    `:` and non-printable paths, but not a `.git` segment. `.git/hooks/pre-commit` passes (probe).
  - Why it is harmless today: nothing applies a case, and in a linked scratch worktree `.git` is a
    file.
  - When it matters: once a reviewer applies cases in a fresh clone, or the gate of
    `gate-guidelines-example-evidence` applies them anywhere, a case could plant a hook.
  - Fix: for that gate task (or the step-10 sentence, `task-cycle/skill/SKILL.md:340-347`), refuse
    or skip a `.git` segment, and paths into `foundations/` that would rewrite the invariant being
    checked.
- **M4.** `coding/SKILL.md` step 4's "What it settles" (`:210-223`) never names the tool's version.
  *To do* (`:56-58`) installs "at the version … the task settles", and the template requires an
  exact pinned version. This is the same as ledger S6 minor 4. Add the version beside the set's
  edition.

The ledger's deferred lines, each graded as a finding of this review:

| Ledger line | Grade | Reading |
|---|---|---|
| T1: artifact published by the executor | **outside the task's scope** | a process event, already reported to Mariusz; the contract was amended; it belongs in the process remarks |
| T1: WAY-197 cited for the bad case's teaching purpose (`template.md:116-118`) | Minor, no change needed | WAY-197's rationale is exactly that teaching purpose; the citation is right |
| T1: rule naming `guidelines-form` with another invariant (S4 tests) | resolved | C34 fix round: `dfa9e15` and `d743c2e`; the repeated break fails 5 invariant subtests and 2 ordinary tests |
| T1: bare-fence sentence redundant after C33 (`template.md:125-128`) | Minor | it explains the result the form check reports, so keeping it is defensible |
| T2: `check_tables` branches untested (header with no separator right under it, `form_check.py:1084`, `:1096`) | Minor | test gap on a form finding; the separator-in-middle branch (`:1091`) is tested |
| T2: docstring "as Markdown reads a row" overstates (`form_check.py:44`, `:1052`) | Minor | Markdown keeps an escaped `\|` in a cell, while the code splits it; the error is stricter, never laxer |
| T2: `coding/template.md:177-180` omits "the form check asks no completeness" | Minor | the meaning is there ("takes no row until…"); the form check's docstring states it |
| T2: `read_roles` and its `TemplateError` lack ordinary tests | Minor | test gap on a template-error path that only a broken template of the-way reaches |
| T2: ragged docstring line | Minor | still at `form_check.py:82-84` ("A / decision is / named by a number"); rewrap |
| T2: `TemplateWords` message check for Kind/File always true | Minor | weak assertion in an ordinary test |
| T3: `guidelines-check-kind-index/1` says "git lists" for "git tracks" (`invariants.md:2215`) | Minor, **in scope** | the sentence is the task's own (F3); its sibling `guidelines-check-exemplar/1` says "git tracks". Edit in place before `main` through `record-invariant`, then refresh its fingerprint |
| T3: `names_in_backticks` re-collapses whitespace per call (`form_check.py:608`) | Minor | negligible cost |
| T3: no test for a tracked directory as a *File* of `## Files of this kind`, nor a 1 MiB line in the kinds table | Minor | test gap; the code refuses a directory (`path not in files`), which is the right result for a table of files |
| T4: docstring wrap `form_check.py:82-85` | Minor | same as the ragged line above |
| T4: a `- **Name:**` line after the cases counts as a field (`form_check.py:978`) | Minor | fails safe: the cases before it become "before the fields end" and are reported |
| T4: `Fence.closing` typed `int` but may be `None` (`form_check.py:519`); fields parsed twice | Minor | type annotation `int \| None`; no behaviour change |
| T4: executor concerns 1–4 (form-only rule with blocks; place of a four-backtick close; open-to-end ordinary only; tab-indented bare fence) | Minor | 1, 2 and 4 hold on their merits (a tab-indented bare fence still ends in a malformed-case report). For 3, the invariant clause "left open to the end of the file" of `guidelines-check-example-files/1` has no invariant test, nor does the "kind file lacking `## Files of this kind`" clause of `guidelines-check-exemplar/1` (C32). The request must list both as unchecked clauses; adding the two subtests by the check author is a cheap follow-up |
| T5: step 11 sentence omits step 10's trigger (`task-cycle/skill/SKILL.md:392-394`) | Minor | "as step 10 gives" reaches it |
| T5: `SKILL.md:63` "writes only in the task's worktree" vs the scratch worktree of `:341-347` | Minor, in scope | a textual contradiction this change introduced. WAY-140 is about effects outside the repository, so no decision is crossed; one clause ("…and the reviewer's scratch worktrees") resolves it |
| T6: `SKILL.md:181` kinds to audit has no recommendation (C35) | **Important** | regraded as I1 |
| T6: `SKILL.md:162` "Where the product has code:" vs the new-kind mode | Minor | step 1 sends a product whose task creates its first file of a kind to "A new kind" under a heading gated on having code; move "A new kind" out of the gate |
| T6: `SKILL.md:98` orchestrated mode writes the trial-run output vs `refine-task`'s orchestrated mode | Minor | the output lands under the git-ignored `.runs/coding/`; name it in `refine-task`'s orchestrated mode, or accept the difference |
| T6: `SKILL.md:56` tool version "the task settles" — nothing settles a version | Minor | same as M4 |
| T6: `SKILL.md:164-175` no rerun of the trial when the human picks another tool or set | Minor | WAY-204 needs the split from a trial of the adopted set; add "a different tool or set chosen in step 4 goes back to the trial run" |
| T6: `SKILL.md:38` "any other file git tracks" vs a backlog kept in the repository | Minor | "other" already excludes the task document; clarify if the backlog is tracked |
| T6: `SKILL.md:167` "never into a file git tracks" ambiguous for the scratch worktree | Minor | "never into the product's working tree" says what is meant |
| T11: citation scope of `installation-claude-guidance/1` in the test that caught the break | **outside the task's scope** | pre-existing test structure; a separate task |
| T11: `slice-11-weakest.txt` gaps | Minor | a gap in the record, not in the code |
| T11: crafted test reassigns `self.product` per subtest (`test_coding_guidelines_installation.py:136-140`) | Minor | works, since `git()` reads `self.product`; a local variable would be clearer |
| T11: non-UTF-8 subtests could assert that stderr names the error | Minor | pinned by C37 to the exit code and the untouched tree |
| T11: carried C37 traceback and C32 `NAMES` gaps | **outside the task's scope** | pre-existing; separate tasks, named in the request |

No `parked` line stands in the ledger.

## Recommendations

- Apply I1's one-sentence fix in the skill, and either reword WAY-201 or carry C35 into the request
  as a narrowing for Mariusz. These are the only blocking items.
- The request handoff (cycle step 11) should carry:
  - the renewed acceptance of WAY-167 and WAY-168 (edited in place; WAY-07);
  - the provisional rulings, including C28's widening of WAY-200 to the one-file case;
  - the unchecked invariant clauses (C32 / T4-3);
  - the WAY-206 weak point (C10);
  - "nothing runs a product's standing-check invariants before a gate" (C16);
  - the pin-move consequence of M2;
  - the follow-ups for M3 and for the pre-existing C32/C37 items.
- In-place cleanups worth doing in the same request, each one line:
  - "git lists" → "git tracks" in `guidelines-check-kind-index/1`;
  - the `task-cycle/skill/SKILL.md:63` clause;
  - the ragged docstring.

## Declined to judge

- Behaviour on Python 3.14: the harness has 3.13.16 only (O3). Nothing in the diff uses
  version-specific syntax, but I could not run it.
- The product-side invariants and scripts of the coding template (linter, formatter, audit
  methods, the record of a run): no product in this repository, as the spec says (§9).
- `gate-guidelines-example-evidence/1`, method `TODO`: the gate that would implement it is out of
  scope (Q1, Q12). M3 is my only note on it.
- The 3 `instruction-files` failures: platform-specific and present at `235b0b4`.
- The installer's `UnicodeDecodeError` traceback on a non-UTF-8 wrapper (C37) and `NAMES` lacking
  `lead-project` and `maintain-styleguide` (C32): pre-existing, ruled separate.
- Whether the harness branch name `claude/…` should be `task/coding-guidelines` (O1): a process
  matter for Mariusz at the merge.
- Every assertion of the 1849-line `test_form_check.py` and the 1445-line
  `test_form_check_invariants.py`: I read their structure, fixtures and the tests listed above, and
  relied on the per-slice reviews and the recorded breaks for the rest.

## Assessment

**Ready to merge? With fixes.**

**Reasoning:** The foundation, templates, form check, skill and installer implement every *To do*
item, all 25 rows and every spec entry with careful source fidelity and a well-guarded trust
boundary. All suites pass apart from the base's platform failures, and every deliberate break of
a checkable invariant is caught. The one Important issue is a small deviation from the human's
settled meaning (rows 3 and 22) in how the skill chooses kinds to audit, fixable in one sentence.
The rest are Minor items for the request or follow-ups.

Counts: Critical 0 · Important 1 (I1, which is also ledger line T6-1) · Minor 29 distinct: 3 new
(M1–M3) and 26 graded from the ledger. M4 is the same finding as ledger line T6 `SKILL.md:56`, so
it is not counted twice. One ledger line, T1-3, is resolved · outside the task's scope 3. The
ledger's 31 lines: 26 Minor, 1 Important, 1 resolved, 3 outside the task's scope.

## Review of the fix of I1

Scoped re-review under Superpowers 6.4.1 `subagent-driven-development/re-review-prompt.md`.
FIX_BASE `2eabf42`, HEAD `5a00041`. Commits reviewed:

- `5808fc7`: WAY-201, by foundation author A;
- `5a00041`: the skill, by executor S6.

What I read:

- `reports/sdd/final-fix-review-package.diff`, read whole;
- the C38 section of `reports/foundation.md` and the fix section of `reports/sdd/slice-6-report.md`;
- C38 in `cycle.md`;
- `git grep "WAY-201@" 5a00041`: it finds no relation carrying WAY-201's fingerprint, so the
  fingerprint change (`70344859` → `d98d2f0e`) leaves nothing stale.

Read-only; no tests were rerun. The diff touches prose only, and the reports show the decisions
guard, the invariants guard, `elements/decisions` (169 OK) and the entry points (current), each
with exit 0.

### Finding Verdicts

- **I1 — the skill (`SKILL.md:180-183`) and WAY-201's binding sentence narrow rows 3 and 22 to the
  kinds the task audits, with no recommendation** — ADDRESSED.
  - `foundations/decisions.md:6819-6822`: WAY-201 now reads "a proposed exemplar for each kind of
    code the product holds files of". That is row 22's meaning, with every other clause and field
    unchanged.
  - `product-guidelines/coding/SKILL.md:180-184`: "the human settles which kinds the task audits"
    is gone. Step 3 now says to "recommend auditing every one of them".
  - A deferral is now "a choice put to them in step 4", whose "How to show" gives every choice its
    ways, cost and recommendation (WAY-194). Step 4's list of what it settles names deferred kinds
    with their reason (`:221-223`), and *Context* records them (`:81-84`).
  - The defect I named, a narrowing by default with no recommendation, no longer exists.

### New Breakage in the Fix Diff

- **N1 (Minor) — the deferral leaves a narrow gap between the skill and WAY-201.**
  - Where: `SKILL.md:181-183` and `:222`.
  - What: the skill still lets the human defer a kind, but WAY-201 (`decisions.md:6819-6822`) now
    binds the audit to end with a proposal for *every* kind the product holds files of, with no
    exception. A task in which the human deferred a kind therefore ends its audit against the
    letter of WAY-201.
  - Why it is not Important: the default now follows rows 3 and 22. The deferral is an explicit,
    recommended-against human choice, recorded with its reason. The executor names the gap in its
    report.
  - The part of this finding that is mine: my own I1 fix recommendation paired both changes.
  - Fix (either one):
    - the request lists "the human may defer a kind" as the remaining provisional choice from C35
      for Mariusz to accept or strike. C38's "list as narrowing for Mariusz" was rejected only as
      the *alternative* to rewording WAY-201, so this is still open;
    - or the skill drops the deferral.

  No Critical or Important breakage. The wording is consistent across the three edited places, the
  frontmatter is unchanged, and no rule is restated.

### Out-of-Scope Observations

None.

### Verdict

**Fix round:** All findings addressed, no new Critical/Important breakage. I1 is ADDRESSED. One new
Minor (N1) goes to the request. The whole change is now **ready to merge** as far as this review is
concerned; the Minor items of the main report remain for the request or for follow-ups.
