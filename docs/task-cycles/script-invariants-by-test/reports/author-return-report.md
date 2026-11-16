# Report of the return step — script-invariants-by-test

**Status:** done

## Commits

- `3043e760` — "Return step: name the tests of the script rules and of the element directories in the part map" (head compared: `540aed04`; base `604907c8`). It changes `foundations/part_map.md` only (+5 / -3).

## Foundation compared with code

Compared: the four invariants the change moved to `Method: test` (`python-version-declared`, `script-language`, `script-imports`, `element-directory-contents`); the decisions the task names (WAY-38, WAY-89, WAY-09, WAY-08, WAY-61) and those my search found (WAY-03, WAY-44, WAY-60, WAY-62, WAY-63, WAY-69, WAY-321, WAY-344, WAY-379, WAY-385, WAY-392, WAY-393, WAY-394, WAY-395, WAY-401); the facts `python-stdlib-modules` and `git-path-patterns`; the part map of the touched parts (`agent-instructions`, `elements-common`, `invariants`, and `part-map`, whose test file left).

- The four invariants: each sentence is what its test checks, on the real checkout. `python-version-declared` — `.python-version` tracked, one line, `3.14` or `3.14.<patch>`. `script-language` — every tracked file is `.py`, `.md`, a listed name, or a `.yml` under `.github/workflows/`; any other is reported. `script-imports` — the reach of `cross-part-imports`, on the interpreter that `.python-version` declares, refused with both versions otherwise, and `Rests on: python-stdlib-modules` still holds (the list comes from `sys.stdlib_module_names` of that interpreter). `element-directory-contents` — a template, `examples.md` or a pointer, and `skill/SKILL.md` for every directory under `elements/` but `common`, where one of the main branches of `rules.md` exists. Their *Part*, *Rests on*, *Derives from* and *Violated* fields need no change; the *Method* fields read `test` and `foundation_check.py` without `--skip-test-citations` finds a citing test for each (exit 0, `0 errors`).
- The decisions: WAY-38 (*Verification*: `script-language · script-imports · script-subprocesses`), WAY-89 (`python-version-declared · script-imports`) and WAY-09 (`repository-file-location · element-directory-contents`) already name the four invariants, and their sentences are unchanged and still true of the code; WAY-08 and WAY-61 (an invariant reads `test` once a test of the suite cites it, run by the command that runs the tests) are met. WAY-44 (tests belong to the part they test) and the *Scope* of WAY-379, WAY-385, WAY-392, WAY-394, WAY-395 and WAY-401 name `agent-instructions` and `elements-common`, so the two new test files stand inside them; WAY-38's and WAY-89's *Scope* name `agent-instructions`, which the moved file stands in. No decision needed a change.
- The part map — what did not match: the sentence of `agent-instructions` named the guidelines of the-way's own code and the instructions, but not the tests of the rules of every script (language, Python version, imports) that now stand in `agent-instructions/test_script_invariants.py`; the sentence of `elements-common` did not name the test of the contents of the element directories that stands in `elements/common/test_element_directory_contents.py`. The *Files* patterns already claim both files (`agent-instructions/**`, `elements/common/**`), and the *Depends on* of `agent-instructions` already names `part-map` and `repository`, so the import of the reader from `elements/part-map/test_cross_part_imports.py` is allowed (the test of `cross-part-imports` passes on the moved file). No *Depends on*, *Files* or *Trust boundary* changed.

## What was written or changed

- Decisions: none. Invariants: none beyond the four `Method` fields the change already switched (`review` to `test`, first commit `4bc1667c`; sentences unchanged). Environment facts: none. Glossary terms: none (the tests use `repository test`, `element` and `files test` in their glossary meanings).
- Part map (`3043e760`): `agent-instructions` gains "and for the tests of the rules every script of the-way keeps: the language it is written in, the version of Python it runs on and the modules it imports"; `elements-common` gains "and the test that every directory of an element holds its template, its examples or a pointer to them, and its skill". Followed `elements/part-map/skill/SKILL.md` with `write.md`: the binding sentences changed, so the entries that name the parts were searched; a part's identifier did not change and no decision, invariant or other entry quotes these sentences, so none needed a change. `foundation_check.py` — exit 0, `0 errors`, with the change in place. `python -B gate/run_tests.py elements/part-map` — exit 0, 40 tests.
- Projected entries: none (the task is no projected one).
- Rows of *Settlements to record*, each written in the code in the first commit and kept through the fix: row 1 (the list of kinds that are no script, with a reason at each kind) in `agent-instructions/test_script_invariants.py`, `SUFFIXES`, `NAMES` and `PLACES`; row 2 (refusal on another interpreter, naming both versions) the same file, `wrong_interpreter` and its use in the test of `script-imports`; row 3 (the reach of `cross-part-imports`, an import whose name cannot be worked out reported) the same file, `outside_imports`, which calls `imports` of `elements/part-map/test_cross_part_imports.py`. The three went to "data or code", so no entry was written for any of them.
- The choices of the first report (1 to 6) and of the fix (the file moved to `agent-instructions`): judged by the rule "a choice that binds after the merge goes to the place the questions of the decisions template give it". None is a rule that a later change or product has to keep: they are the form of tests that cite invariants whose sentences already bind (the skip where no main branch exists is the condition of the sentence of `element-directory-contents`; the pointer form follows WAY-09 and the template of the environment facts; the element directories follow the invariant's *Part*; the versions follow `python-version-declared`). They stay rows of the questions table of the request, and no decision was written. The move of the file is stated in the part map's sentence of `agent-instructions` now.

## Unwritten on purpose

- No invariant was written for the behaviour that the tests use but no decision sets: that a `.py` file holds Python (the settlement of row 1 chose kinds by name), and that an unsourced `cgi` / `annotationlib` difference between Python 3.12 and 3.14 stands in a comment of the test of `script-imports` (the task's own source for it is a run on this machine on 2026-11-14; the fact the test rests on, `python-stdlib-modules`, already says that the list of the running 3.14 interpreter is the library's; the comment illustrates and nothing rests on it, so no environment fact was written).

## Working copies

Stood in `.runs/author/` (outputs of the focused runs of the first report and of the fix; ignored by git, kept as evidence). No worktree, clone or other copy was made in this step, and the worktree has no uncommitted change.

## Unread material

none — `return_step.md` and `foundation_step.md` were read whole; the `SKILL.md` of `update-part-map` with its `write.md`, `decide_entry.md` and the template of the part map were read for the change of the map; the entries named above were read in the first report, WAY-344 and WAY-395 whole in the fix. I did not read the reports of the two reviews, as the handoff says.

## Searches not found or unclear

none
