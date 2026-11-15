# Coding guidelines — command-runner

- **Discipline:** coding
- **Applies to:** task-cycle · gate

## When to read

Before adding or changing a file of the kind `command-runner`: a script that starts one command, such
as the gate of a product, and passes its output on.

## Files of this kind

| File | Status | Decision |
|---|---|---|
| `task-cycle/gate_times.py` | `exemplar` | WAY-390 |
| `gate/run_tests.py` | `copy` | — |

## Rules

### Passing on the exit code

- **Decision:** WAY-390
- **Invariant:** command-runner-passes-exit-code
- **Good:** a script that ends with the exit code of its command, and with 128 plus the signal number
  where a signal ends the command
- **Bad:** a script that ends with one fixed exit code whatever its command ends with

A script of this kind ends with the exit code of the command it started, unchanged. Where a signal
ends that command, the script ends with 128 plus the number of that signal.

## Examples

### The rest of the exemplar

The exemplar's relay of the command's output as it comes, its reading of the run's times from that
output, its record of the runs at the same time in a shared registry, and its own exit code, with an
`Error:` line on its error output, for its own failures, such as a command it cannot start, stand
here as examples. The kind holds no rule on these: a new script of the kind may do each of them
another way.

## Where in code

- `task-cycle/`
- `gate/`
