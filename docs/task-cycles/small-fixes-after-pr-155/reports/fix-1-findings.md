# Findings of the review of the whole change, to be fixed — `reports/fix-1-findings.md`

Source: `reports/review-whole-report.md`, first line `PASS 739097886195c9ea02b30cc03894e2c64cebb4cf`, range
`80006b25feb4c5a6ffdb8f75d993051eecbc745d..739097886195c9ea02b30cc03894e2c64cebb4cf`.

Blocking findings: none. The Minor findings within the task that the reviewer lists and has not marked
outside the task's scope follow, in the reviewer's words (`m1`–`m5`; the reviewer's `o1` is outside the
task's scope and is not fixed).

**m1 — `task-cycle/test_remove_merged_worktrees.py:120-123` and `:37-39`: the new comments say the
receiving side gets none of the variables of `ENVIRONMENT`, which is wider than what git does.**
The comment in `Fixture.__init__` reads "Git hands the side that takes a `push` to a local
repository none of the variables of ENVIRONMENT"; the one at `ENVIRONMENT` reads "it takes a `push`
through git's own receive-pack, which gets none of these variables" and calls the bare repository "no
such process of the tests" (a repository is no process). Git unsets before `git-receive-pack` only
`GIT_CONFIG_COUNT GIT_CONFIG_PARAMETERS GIT_PREFIX` (and the variables that locate a repository): the
author's own trace shows the line `run_command: unset GIT_CONFIG_COUNT GIT_CONFIG_PARAMETERS
GIT_PREFIX; 'git-receive-pack …origin.git'` (`reports/author-trace-before.txt:13`), and the same trace
holds receive-pack's own lines (`built-in: git receive-pack …`, line 16), which it could write only
because `GIT_TRACE`, a variable of `ENVIRONMENT` in that run, reached it. `GIT_CONFIG_GLOBAL`,
`GIT_CONFIG_NOSYSTEM` and the author and committer variables reach it as well. Why it matters: To do 1
asks these comments to say what is true after the earlier ones did not; a later reader who takes the
comment at its word believes receive-pack also reads the user's global configuration, and reasons
about the fixture from a wrong fact. Suggested wording: "none of the variables that carry
configuration (`GIT_CONFIG_COUNT` and its keys and values)". The rule in `guidelines/testing.md:181`
("git passes none of them") follows the wording of row 1 of *Settlements to record*, where "them" reads
as the variables that turn maintenance off; it needs no change of its own.

**m2 — `guidelines/testing.md:179-182` against `task-cycle/test_remove_merged_worktrees.py:126`: the
fixture the rule comes from does not do what the rule's sentence says for its second repository.**
The rule: "A git test that turns off git's automatic maintenance sets it in the configuration of each
repository it builds, the bare remote one too, and not in environment variables alone". `Fixture`
builds two repositories, `origin.git` and `main` (`git(self.root, "init", "-b", target,
str(self.main))`, line 126), and sets `maintenance.auto`/`gc.auto` in the configuration of
`origin.git` alone; `main` has them from `ENVIRONMENT` alone. Today this has no effect: every git
process in `main` is started by the tests or by the script under test with `env=ENVIRONMENT` (lines 67,
197, 209), and `state()` leaves `.git` out of the snapshot (line 86). Why it matters: the only test the
rule reaches is the one it was written from, and it departs from the rule's sentence (its *Good* line,
line 176, is narrower and is met); the next review that compares a git test with the rule finds the
rule and its source disagreeing. The rule's wording is row 1 of the task's settlements, accepted by
the human, so the cheap fix lies in the code: two lines `git(self.main, "config", "maintenance.auto",
"false")` and `git(self.main, "config", "gc.auto", "0")`. Narrowing the rule instead would change an
accepted settlement and needs the human.

**m3 — `task-cycle/test_gate_times.py:454-455`: the comment of the test of change (v) restates the
description's sentence in words that contradict the test.** It says "the places of the last 100
different lines that hold `== ` after text are kept, each place once, so the 101 lines of `y2` are one
place"; the description at `task-cycle/gate_times.py:32-33` says "the last 100 different places of
lines that hold `== ` after text, each place once". "The last 100 different lines" counts lines, and the
101 lines of `y2` are 101 different lines, so the first half of the comment's sentence says the
opposite of its second half. To do 2 asks each new test to name the sentence of the description its
value comes from (WAY-394, `guidelines/testing.md`, "Where the expected value comes from"); the
sentence is named, but misquoted. Fix: quote the description's words.

**m4 — `task-cycle/test_gate_times.py:435-438`: the output of the test of change (iii) is not what
unittest prints, against the class's own statement.** The `then` text gives `gate1` a second failing
test, while `gate1`'s report still prints `F`, `Ran 1 test in 0.500s` and `FAILED (failures=1)` (from
`failing_with`, lines 195 and 200); the docstring of `NestedRunTest` says "The outputs are written out
by hand, as the runner and unittest print them" (line 219). No expected value depends on it (the time
is the first `Ran` line after the nested summary, whatever its count), and the author named it. Fix:
let `failing_with` take the test-count line, or print `FF`, `Ran 2 tests` and `FAILED (failures=2)`
when `then` is given.

**m5 — `reports/author-report.md`: no sentence on whether the change alters behaviour a user sees.**
`task-cycle/change/SKILL.md:172-177` asks the one author, where the change alters no behaviour a user
sees in the running product, to say "that it alters none, with one sentence why" (WAY-406); the report
holds no walk and no such sentence (a search for "walk", "running product" and "behaviour a user" in it
finds nothing). The judgment the sentence would carry is right: the change alters no result of
`gate_times.py` (my mutant `iv_clear_back`, the code with `self.marks.clear()` restored, passes every
test of `NestedRunTest`; the argument under *Trust boundary* below), and the rest is tests, comments
and a guideline. The request's description should carry the sentence.
