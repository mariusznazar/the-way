# Coding guidelines — the-way

- **Discipline:** coding
- **Applies to:** elements-common · part-map · relation-model · project-level · task-cycle · gate · agent-instructions · instruction-files · installation · process-audit · product-guidelines

## When to read

Before any change of the code of the-way: a script, a module the scripts import, or a test, in a
part named above. These are the coding guidelines of the-way's own code, which WAY-379 adopts. Read
a file in the table below as well where its condition matches the work.

## Kinds of code

| Kind | File | When to read |
|---|---|---|
| `check` | `guidelines/coding-check.md` | before adding or changing a check: a script that reads the files of a repository, or one file it names, and reports the places that break a rule |
| `measuring-report` | `guidelines/coding-measuring-report.md` | before adding or changing a measuring report: a script that counts figures from the files of a run, a history or a repository and writes them as a report |
| `generator` | `guidelines/coding-generator.md` | before adding or changing a generator: a script that writes files into the repository it runs in from the files it reads |
| `repository-changer` | `guidelines/coding-repository-changer.md` | before adding or changing a repository changer: a script that removes, rewrites or moves files or directories of the repository it runs in |
| `command-runner` | `guidelines/coding-command-runner.md` | before adding or changing a command runner: a script that starts one command and passes its output on |
| `shared-module` | `guidelines/coding-shared-module.md` | before adding or changing a shared module: a module that other scripts import |

## Rules

### Linter

- **Decision:** WAY-380 · WAY-381
- **Invariant:** ruff-blocking-rules
- **Good:** a report of `F841` in a file is fixed in that file, and `ruff.toml` stays as it is
- **Bad:** a `noqa` comment that turns a blocking rule off stays in a file, or a rule is turned off in `ruff.toml` on meeting a report

The linter reads the code of every part named above, tests included, and the gate runs it. The
invariant takes the rules that block a change from the environment fact `ruff-default-rules`, less
the rules under `## Examples`. A report of a rule that blocks is fixed in the file it names. A
comment that turns a rule off has no effect: the test of the invariant runs the linter with its
flag that ignores such comments, so the report stays, and the review of each change finds a comment
the flag cannot reach. Turning a rule off in `ruff.toml`, or moving a rule between the rules that
block and the examples, is a change of WAY-380 that the human approves. A rule under `## Examples`
blocks nothing and no invariant checks it; an agent reads its reports and may pass them by. The
review of each change compares the changed files with this rule. No command of the linter stands
beside the one command of the gate (WAY-16).

### Formatter

- **Decision:** WAY-382 · WAY-381
- **Invariant:** formatter-layout
- **Good:** a file laid out by the formatter at the width the decision names, with no comment that switches the formatter off
- **Bad:** a file laid out by hand against the formatter, or a comment `fmt: off`, `fmt: on`, `fmt: skip`, `yapf: disable` or `yapf: enable` in one

The formatter is the one of Ruff that WAY-381 pins, run with the configuration `ruff.toml`, at a
line width of 100 and every other setting at its default. It covers the `.py` files of the parts
named above and no Python example in a Markdown file. Every such file stands as the formatter
leaves it, and a comment `fmt: off`, `fmt: on`, `fmt: skip`, `yapf: disable` or `yapf: enable` in
one is no way out: the test of the invariant fails on it. No command of the formatter stands beside the one command of the gate
(WAY-16).

### Dependency audit

none — WAY-383

### Recording a failure

none — WAY-384

### Hiding a failure

none — WAY-384

### Identifiers in log lines

none — WAY-384

### Business events

none — WAY-384

### Secrets and personal data

none — WAY-384

### Logging scope

none — WAY-384

### Size of a function and a file

- **Decision:** WAY-385
- **Invariant:** function-and-file-size
- **Good:** a function that grows past its threshold is divided where its parts have a name of their own
- **Bad:** a function cut at an arbitrary line only so that it stands under its threshold

The rule covers scripts; a test file stands outside it. A function is counted with the functions
nested in it, and a file by its lines. The thresholds and the exceptions stand in WAY-385 alone.
A change that adds to a function or a file over its threshold begins with a move of a part of it out,
with no change of behaviour (WAY-365). The test of the invariant runs apart from the linter and,
where it fails, names every function and file over a threshold with its size; no command of its own
that counts sizes stands beside the one command of the gate (WAY-361). The review of each change
compares the changed files with the thresholds.

### How a script starts and ends

- **Decision:** none
- **Invariant:** none
- **Good:** a script that opens with a description of how it is run, `python -B …`, and of what each of its exit codes means, and ends with `sys.exit(main())` of a function `main` that returns the exit code
- **Bad:** a script with no description of its run or its exit codes, or one that starts at its top level or from several places and loses the exit code

Each script that is started from the command line opens with a description of how it is run
(`python -B …`) and of what its exit codes mean, and has one fixed place of start that returns the
exit code. A module that other scripts import and that has no more for the command line than a fixed
`if __name__ == "__main__":` block, as a file of the kind `shared-module` has, is no such script,
and this rule does not reach it. The reason: the one who runs a script, a human or an agent, finds
there how to run it and what an exit code tells, and the exit code reaches the caller only through
one place that returns it. The review of each change that adds or changes a script compares it with
this rule.

### A field missing from a file a script reads

- **Decision:** WAY-344
- **Invariant:** none
- **Good:** none
- **Bad:** none

A field missing from a file a script reads is handled as WAY-344 gives. The review of each change
that adds or changes a script compares its reading of files with that decision.

## Examples

### Rules of the linter's set that stay examples

The rules below are in the default set, and no change is blocked by them: each gave at least one
report on the code of the-way that led to no change worth making (WAY-380, WAY-203). Each is named
as `ruff rule <code>` names it. Nothing here binds.

| Code | Name | What it checks for |
|---|---|---|
| `UP031` | `printf-string-formatting` | `printf`-style string formatting, which it offers to replace with `str.format` calls |
| `ISC004` | `implicit-string-concatenation-in-collection-literal` | implicitly concatenated strings inside list, tuple and set literals |
| `PLW1510` | `subprocess-run-without-check` | `subprocess.run` called without an explicit `check` argument |
| `RUF100` | `unused-noqa` | `noqa` directives that are no longer applicable |
| `FURB167` | `regex-flag-alias` | shorthand aliases for regular expression flags, such as `re.I` for `re.IGNORECASE` |
| `FLY002` | `static-join-to-f-string` | `str.join` calls that can be replaced with f-strings |
| `I001` | `unsorted-imports` | imports that are not de-duplicated, grouped and sorted |
| `B023` | `function-uses-loop-variable` | function definitions that use a loop variable |
| `UP017` | `datetime-timezone-utc` | uses of `datetime.timezone.utc`, for which `datetime.UTC` is an alias |
| `SIM117` | `multiple-with-statements` | unnecessary nesting of multiple consecutive context managers |
| `UP012` | `unnecessary-encode-utf8` | unnecessary calls to `encode` as UTF-8 and unnecessary explicit UTF-8 encoding arguments |
| `RUF015` | `unnecessary-iterable-allocation-for-first-element` | constructs that can be replaced by `next(iter(...))`, such as `list(...)[0]` |
| `SIM102` | `collapsible-if` | nested `if` statements that can be collapsed into a single `if` |
| `C419` | `unnecessary-comprehension-in-call` | unnecessary list or set comprehensions passed to builtin functions that take an iterable |
| `RUF012` | `mutable-class-default` | mutable default values in class attributes |
| `SIM114` | `if-with-same-arms` | `if` branches with identical arm bodies |
| `SIM905` | `split-static-string` | static `str.split` calls that can be replaced with list literals |
| `SIM115` | `open-file-with-context-handler` | files opened without a context manager |

## Where in code

- `ruff.toml`
- `requirements-quality.in`
- `requirements-quality.txt`
- `agent-instructions/test_linter_invariant.py`
- `agent-instructions/test_size_invariant.py`
- `task-cycle/`
- `process-audit/`
- `project-level/`
- `elements/common/`
- `instruction-files/`
- `agent-instructions/`
- `installation/`
- `gate/`
- `relation-model/`
