# Task 6 report

Status: DONE. Commits: bcb0298 (SKILL.md), 9c5c722 (README.md). Worktree clean afterwards.

## Checks
- grep for checker / resolve it first / realpath / Get-Item / component directory in SKILL.md: no line (`grep 1`).
- No `.runs`, `C:\`, `Brain` in SKILL.md.
- `skill_entry_points.py`: `entry points are current`.
- `gate/run_tests.py gate` last line: OK. `agent-instructions`: OK.
- loop2 (run with `C:/` paths, because `MSYS_NO_PATHCONV=1` leaves `/c/...` unconverted for git.exe): `160000 c64a6071384fb57cdb9d7e9db4560ddc43e3b355 0	.the-way`; `git cat-file -e HEAD:instruction-files/SKILL.md` -> `fatal: path ... does not exist`, exit 128.
- Task worktree: `rev-parse --show-superproject-working-tree` empty, exit 0.

## Adjustments to the brief's text (script as of f97cbdd)
1. Section 1, check-script step: "Read every file the check script lists" -> "every file named in its `size` lines" (the script lists files only through its `size` info findings). Added: a network `--file` is refused with exit code 2; and read what its `info` lines say was left out (link out of the repository, network path, file cut at the size limit), since the check did not cover it.
2. Judge, output item 1: added "and its `info` lines that say something was not read or not checked".
No procedure step added. Frontmatter unchanged. The text was produced by a python script extracting the brief's block (no backslashes in it) rather than the Write tool; file is LF, no CR.

## Files changed
instruction-files/SKILL.md, README.md (the bullet after the agent-instructions bullet, and the first sentence of "Using the skills").

## Concerns
- `tool_loading.md` has no "Settings that change loading" section yet (Task 8 fills it); the skill names it as the brief says.
- Check script on the worktree itself reports one WARN: `_zadania\` in AGENTS.md:20 (private backlog folder reference, not this task's).

## Fix round 1
Only `instruction-files/SKILL.md` changed; frontmatter untouched; `entry points are current`.
1. Read step: "Read too what its `info` lines say was left out ... since the check did not cover it." -> the `info` lines go into the judgement and are never followed: a network path is never read; a link out of the repository only after the human confirms; the part of a file cut at the size limit may be read.
2. WAY-130 exception: Judge ground gains a third ground, "a carried decision or step" (the decision the repository records or the activity step the file leads, named); Place step 1 gains "unless it carries a decision ... or a step of an activity ...; then name it".
3. "A removal whose mistake cannot be named is proposed as a removal test, never as a plain cut" -> "A rule whose mistake can no longer be named is proposed for removal; a rule whose mistake is named but may no longer happen is proposed as a removal test".
4. "(a network path is refused, with exit code 2)" -> "(on Windows a network path is refused, with exit code 2)".
5. The list of left-out items now says "for example" and adds a link to a directory and a directory that could not be listed.
6. Pin check: when the pinned commit has no `instruction-files/`, `cat-file -e HEAD:instruction-files/SKILL.md` failing with `.the-way/` holding files means move the pin; an empty `.the-way/` means initialise the submodule.
7. Mistakes-table row: "a path in backticks" -> "a path in backticks, with the condition under which to read it".

## Fix round 2
Only `instruction-files/SKILL.md`; frontmatter untouched; `entry points are current`.
1. Threshold sentence: "...is listed as not recommended, with the search named." -> "...is listed as not recommended, with the search named, unless the rule carries a decision the repository records or a step of the activity its file leads."
2. Removal: "A rule whose mistake can no longer be named is proposed for removal; ..." -> "A rule added for a mistake that can no longer be named is proposed for removal; a rule whose mistake is named but may no longer happen is proposed as a removal test (section 7 of the principles)."
3. Pin check: "`git -C <the repository under review>/.the-way cat-file -e HEAD:instruction-files/SKILL.md` fails and `.the-way/` holds files ..." -> "take the hash that the `ls-files --stage` line prints and run `git -C <the repository>/.the-way cat-file -e <that hash>:instruction-files/SKILL.md`. It fails and `.the-way/` holds files — the pin lacks the directory ...; `.the-way/` is empty — the submodule is not initialised ..." (placeholder shortened so the line stays within 100 columns).
4. The over-long line at old SKILL.md:27 rewrapped to 100 columns. Remaining lines over 100 are the frontmatter description and table rows (unchanged).
