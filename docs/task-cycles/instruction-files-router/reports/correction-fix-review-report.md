PASS 2ba7a47

# Review of the fix — correction after review, instruction-files-router, PR #49

Range `44475cf..2ba7a47`, one commit (`2ba7a47`); `git rev-parse HEAD` is
`2ba7a476560b8092f0d6f547aab3254788aa733c`, the head given. Bounded by `correction-findings.md`
(I1, I2 of `correction-review-report.md`); fix report `correction-fix-report.md`. Counts: 0
blocking, 1 Minor, 0 out of scope.

## The findings

**I1 — the second half of WAY-133 — fixed.** `instruction-files/SKILL.md:117`, the note of the row
"every time, without exception", now reads "an instruction says what the check is for, or carries
what the check cannot catch; it does not replace the check (WAY-133)", which carries both halves of
WAY-133's last sentence ("says what the mechanism is for, or carries what the mechanism cannot
check"). `instruction-files/placing.md:7-8` keeps the pointer and now names the note: "propose first
the mechanism that section gives, and the instruction its note allows". The rule stands once, in
`SKILL.md`; `grep -n -i "cannot catch"` finds only `SKILL.md:117`.

**I2 — restatements between files — fixed.**
- `instruction-files/judging.md:80-81` now reads "A rule that carries a decision or a step leaves by
  the way out 'When to add a rule' gives it, not by this test." The way out of a decision-carrying
  rule now stands only in `SKILL.md:249-252`. `SKILL.md:262` "the named mistake is later its way
  out" stays beside `judging.md:79-80`; I hold that pair as a summary in `SKILL.md` and the removal
  procedure in `judging.md`, not one rule twice — the blocking part of I2 was the decision-carrying
  exception, and that is gone.
- `instruction-files/kind_main_file.md:19-22` now reads "Pointers to ways in, where condition 1 of
  the criterion allows one, in the form of the shared layout …"; the clause "for activities whose
  way in the agent will not recognise from the request alone" is cut. When the main file carries a
  pointer now stands only in `SKILL.md:116` and `:122`. The kind file names a section of `SKILL.md`,
  which every use reads, not another file, so WAY-258's "No file of a kind points to another file"
  holds.

## The fix diff beyond the findings

- **WAY-129's condition** (`SKILL.md:203`): the shared carrier now reads "a pointer as a path in
  backticks with the condition under which to read it: 'Before X, read `path`' (WAY-129)". This
  matches WAY-129 ("names the file to read by its path in backticks with the condition under which to
  read it"), and puts back what the cut row "using `@path` as a pointer" and the cut defect "a pointer
  without a condition" had carried. It is not a second statement: `kind_main_file.md:21` says how the
  condition is worded ("as the criterion asks"), and so points to `SKILL.md:127`.
- **The check-script list** (`SKILL.md:268-276`): three items now name the pitfall or layout row
  they check instead of restating it. I compared each with its target: the two pitfalls of
  `kind_main_file.md:45-49` (`@path`, `CLAUDE.local.md`), the pointing line of
  `kind_path_rule.md:11`, and the pointer or copy of `kind_skill.md:25`. Nothing the old items said
  is missing from the targets. Nothing in `foundations/` or the tests quotes the old items
  (`git grep` below). The module docstring of `check_instructions.py` still points to the section by
  its title, which is unchanged.
- I looked for a new restatement among the four changed files and their targets and found none.
  I also found no content of a decision in play (WAY-128 to WAY-133, WAY-256 to WAY-258) that the
  fix dropped. The four changed files stay LF.

### Minor

**M1 — two items of the check-script list are hard to parse.** `SKILL.md:271-273`: "the pointing
line the layout of files loaded with some files gives an `AGENTS.md` in a subdirectory" and "the
pointer or copy the layout of skills gives a skill needed in Codex". A reader first takes "the layout
of files … gives an `AGENTS.md`" as the clause. For example, "an `AGENTS.md` in a subdirectory has
the pointing line its layout gives" and "a skill needed in Codex has the pointer or copy its layout
gives" are easier to read. This is wording only, and the meaning is right.

The Minor and out-of-scope findings of `correction-review-report.md` (M1–M4, O1) were not fixed. As
the findings file says, they go to the request. This review does not reopen them.

## Declined to judge

- `SKILL.md:262` against `judging.md:79-80` (the named mistake as the way out): a summary in one file
  and the procedure in the other. See I2 above.
- The docstring of `check_instructions.py` names more checks (emphasis, size) than the list in
  `SKILL.md` does. This was already so before the fix and lies outside the fix diff.

## Checks

| Command / method | Exit / result |
|---|---|
| `git rev-parse HEAD` | `2ba7a476…`, matches |
| `python -B gate/run_tests.py instruction-files` | 0 — 104 tests, OK (5 skipped) |
| `python -B elements/common/foundation_check.py` | 0 — "0 errors" |
| `python -B agent-instructions/skill_entry_points.py` | 0 — "entry points are current" |
| `python -B instruction-files/check_instructions.py . --file` each of the 8 skill files (not `tool_loading.md`) | 0 — 0 errors, 5 warnings |
| `git diff --check 44475cf..2ba7a47` | 0 |
| CR count in each changed file at `2ba7a47` (`git show … \| grep -c $'\r'`) | 0 in all four |
| `grep -n -i "cannot catch\|condition under which" instruction-files/*.md` | `SKILL.md:117` and `:203` only |
| `git grep -n -i "check script settles\|has no \`CLAUDE.local.md\`\|pointing line in the main file\|copy in \`.agents/skills/\`" 2ba7a47 -- . ':!*.runs*'` | only the section heading, the docstring pointer, and the layout row of `kind_skill.md`; nothing quotes the old list items |
| Manual: read the fix diff, its targets, and WAY-129, WAY-133, WAY-258 | as above |
| `git status --short` after the checks | clean |

Not run: the full gate, as the dispatch says.

## Reaches beyond the dispatch

- WAY-129 and WAY-133 as quoted in the frozen task's *Decisions in play*, to judge the two pointer
  targets.
- `instruction-files/test_check_instructions.py` and `foundations/` (grep), to see whether anything
  quotes the rewritten check-script items.
