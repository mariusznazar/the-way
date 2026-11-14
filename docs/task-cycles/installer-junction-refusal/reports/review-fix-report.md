PASS ee6126cd7899630918d1e3b07dbfd18df5150904

# Review of the fix — installer-junction-refusal

Range `474df77904b199e3ba1acb438c5a88c9a47d13c1..ee6126cd7899630918d1e3b07dbfd18df5150904` (`git rev-parse HEAD` in the worktree: `ee6126cd7899630918d1e3b07dbfd18df5150904`; commits `62ec7c1`, `ee6126c`). Bound: `reports/whole-review-findings.md` (finding 1 blocking, findings 2 to 6 Minor within the task). Trust boundary yes; no irreversible operation is added by the fix.

Result: every finding of the file is fixed; no new Critical or Important finding in the fix diff; two new Minor notes (below), which block nothing.

## Findings of the file, one by one

1. **Blocking: sentence broader than the code — fixed.** `foundations/invariants.md:303` now reads "The installation command, with its own code, neither writes nor deletes anything through a symbolic link or a Windows junction that stands in a path of a product, `.the-way` included, and it refuses before it writes anything where such a link stands on the path of a file it is to write or is `.the-way`." Git's writes under `.git` (case B of my first review: `git submodule add` filling a folder through a junction at `.git/modules`) are no longer claimed. I re-read every write and delete in `installation/install.py` (`mkdir`, `open("x")`, `write_bytes`, `open("ab")`, `unlink`, `rmdir`): each acts on a path that went through `check_parents` or is in `stale_*`, or on `.gitmodules`/shared files the existing file checks refuse when they are links or not regular files; the rest is git (`submodule add`, `checkout`, `update`, `add`). The sentence and the code now agree. This keeps the orchestrator's ruling (narrow the sentence, no check of `.git`), which fits the task: item 1 asks for refusal on the path of a file the installer writes. The hole is stated openly in the author's report for the human; see Minor note A.
2. **Minor: three checks untested — fixed.** New test `test_the_scan_for_stale_files_does_not_enter_a_junction_at_their_directory` (`installation/test_install.py:736-771`) calls `install.stale_agent_definitions` and `install.stale_entry_points` directly: two controls with real directories (the scan must return the one stale file, so an empty result below a junction is the junction's doing), then a junction at `.claude/agents`, `.claude`, `.agents/skills`, `.agents` (must return `[]`, outside file unchanged). It cites the invariant. I ran it: pass. I mutated two ways in a separate worktree of the head: reverting only the one-line change gives `FAILED (failures=1)` at `junction='.agents', scan='stale_entry_points'`; turning `stale_agent_definitions`'s `.claude` and `agents` checks back into `is_symlink()` gives `FAILED (failures=2)` at `junction='.claude/agents'` and `junction='.claude'`. The `is_link(skills)` guard (the third original site) is covered by the `.agents/skills` case; I did not mutate it separately (the author's mutation of all four gives four failures).
3. **Minor: "directory path" — fixed with 1.** The sentence now says "a path of a product". The author's table of covered tests (report, finding 3) is right: the three new-test and the `.the-way` test sit under clause 2 or "deletes nothing through ... a path"; the two existing symlink tests (`installation/test_agent_types_installation.py:221`, `:257`) put the link at the definition itself, which reads as a link "on the path of a file it is to write" and as a path of a product. Every citing test is covered by its words. (Changed invariant tests of the whole change: those two, plus `installation/test_install.py` the four junction tests, citing at `:698`, `:719`, the new one, `:737`-region.)
4. **Minor: `Rests on: none` — fixed.** `foundations/invariants.md:306` reads `Rests on: python-junction-detection`; the entry `python-junction-detection` stands in `foundations/environment_facts.md` before the withdrawn identifiers. See (c).
5. **Minor: README "folder of an agent type" — fixed.** `installation/README.md:183-188` now reads "a junction at the folder of a skill the commit lacks, or at the path of an agent type's file, is not followed, so nothing is deleted through it" — true to the code (a file junction is skipped because `is_file()` is false; I showed it earlier in case J).
6. **Minor: sizes — no change asked, none made.** Confirmed by the diff.

## The points asked

**(a) The narrowed sentence and its tests.** Read above: the sentence is true to the code, the table matches the tests. "With its own code" is a phrase a reader may take either way; see Minor note A.

**(b) The one-line change to `installation/install.py:379`:** `if is_link(target / directory) or is_link(skills) or not skills.is_dir(): continue`. Correct and within the task. `stale_agent_definitions` already checks `.claude` itself; `stale_entry_points` checked `skills` and each entry but not `.claude` or `.agents`, so a link there let the scan list a stale `SKILL.md` through it (the test found it: failing run on `.agents`). Item 2 of the task asks to recognise a junction wherever a symlink was recognised and not to remove anything a junction leads to; this is the same rule at a site the original code and the first change both left unchecked. It changes the behaviour of no run: `plan` refuses such a path first (`check_parents`), and for a real directory `is_link` is false. A fix of Minor findings may change code that a finding needs, and this change is what the finding's test needs to pass; I keep it.

**(c) The environment fact `python-junction-detection`** against `elements/environment-facts/template.md`, `elements/common/rules.md` and the skill's form:
- One sentence stating one fact: "In Python 3.14, `os.path.isjunction` returns true for an existing directory entry that is a junction, and always returns false where the current platform supports no junctions." One source, one reason to change.
- Identifier names what the fact is about (junction detection), not a value or an edition; lower case, hyphens; unique in the shared space of identifiers (`foundation_check.py`: 0 errors).
- *Source* is in the "page with archived copy" form: address, `(archived: <address>, <date>)`, § place, the passage word for word, `read <date>`. Dates in order (archive capture 2026-10-24, read 2026-11-14).
- The quotation against the page: I fetched `https://docs.python.org/3.14/library/os.path.html` (HTTP 200) and the archived copy `http://web.archive.org/web/20261024070950/https://docs.python.org/3.14/library/os.path.html` (HTTP 200) with `curl`, took the text after the first `os.path.isjunction` with markup stripped, and found "Return True if path refers to an existing directory entry that is a junction. Always return False if junctions are not supported on the current platform." in both (exit 0 each). The quotation is the page's, word for word.
- The sentence says no more than the passage (it does not say a junction is no symbolic link, which the page does not say).
- Used by an invariant's *Rests on*, so it stands (WAY-73). It is a fact about what decides whether a commit makes the sentence true (what the code calls to find a junction), not about what runs the test.
- Minor note B: the code calls `Path.is_junction` (`install.py:308`), and the fact is about `os.path.isjunction`. They are one check (pathlib calls the os.path function), but the page quoted is the `os.path` one, so a reader has to know it. Not a defect of the fact.

**(d) Line counts.** The author's report says `installation/test_install.py` +41/-0; `git diff 474df77..ee6126c --numstat` shows 37/0 for that file (and 6/0, 2/2, 2/2, 1/1 for the others, which match the report). The report is wrong by four lines; the commits are fine. Minor note C, no action on the code.

**(e) New Critical or Important finding in the fix:** none. The new test asserts on the scan's return and on the outside file; both fail on the mutations; the fix touches no behaviour of a run.

## Minor notes (not blocking)

- **A. "with its own code" leaves the hole in place and says it in few words.** `foundations/invariants.md:303`. A junction at `.git/modules` is still written through by git with exit 0; the sentence no longer promises otherwise, but a reader of the entry alone does not learn that git's writes under `.git` are outside it (the part map and README say nothing either). The human sees it in the author's report; a one-clause note in `installation/README.md` ("git's own writes under `.git` are not checked") would put it where an installer user reads. Out of the findings file; Minor; not required.
- **B.** As above, `os.path.isjunction` versus `Path.is_junction`.
- **C.** Author report +41 versus the diff's +37.

## Checks I ran

| Check | Command | Exit | Result |
|---|---|---|---|
| Head | `git rev-parse HEAD` in the worktree | 0 | `ee6126cd7899630918d1e3b07dbfd18df5150904` |
| New test | `python -B -m unittest installation.test_install -k scan_for_stale` | 0 | `Ran 1 test in 2.039s`, `OK` |
| Mutation: the one-line change reverted (separate worktree of the head, removed after) | same command | 1 | `FAILED (failures=1)`, `junction='.agents', scan='stale_entry_points'` |
| Mutation: `.claude` and `agents` checks of `stale_agent_definitions` back to `is_symlink()` (separate worktree) | same command | 1 | `FAILED (failures=2)`, `.claude/agents` and `.claude` |
| Foundation check | `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| Quotation against the page and its archived copy | `curl -sL` of both addresses (HTTP 200), text search of the quoted passage after markup stripped | 0 | found in both |
| Line counts | `git diff 474df77..ee6126c --numstat` | 0 | 37/0 for `test_install.py` |

Not run: the whole gate and `gate/run_tests.py installation` (the orchestrator's; the author reports 60 tests, exit 0, in 814 s); the earlier junction tests of the first review were not re-run, since the fix changes no line they exercise except through the one-line change, which `plan` never reaches differently. The scratch worktree was removed; the reviewed worktree, its index and branch are unchanged.

## Unread material

- `reports/review-whole-report.md` was not re-read; the findings file was enough.
- The environment-facts skill's own files (`elements/environment-facts/skill/*`) were not read; I judged the entry against the template, `elements/common/rules.md` (read in the first review) and the existing entries around it (`python-stdlib-modules`, `codex-agent-skills-config`), not against the skill's steps.
- The whole-change counts of decisions from the first review stand (10 read whole; titles for the rest); the fix reads no new decision.

## Searches not found or unclear

- None. (The `isjunction` page text was found in both copies; no glossary entry for "junction" exists, as before, and no sentence is read wrongly for lack of it.)
