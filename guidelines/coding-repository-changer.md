# Coding guidelines — repository-changer

- **Discipline:** coding
- **Applies to:** task-cycle · elements-common · installation

## When to read

Before adding or changing a file of the kind `repository-changer`: a script that removes, rewrites or
moves files or directories of the repository it runs in, such as a script that removes working
directories, one that copies files into a product, or one that installs a submodule.

## Files of this kind

| File | Status | Decision |
|---|---|---|
| `task-cycle/remove_merged_worktrees.py` | `exemplar` | WAY-389 |
| `elements/common/migrate_foundation.py` | `copy` | — |
| `installation/install.py` | `do not copy` | — |

## Rules

### Changing nothing without the act

- **Decision:** WAY-389
- **Invariant:** repository-changer-acts-only-when-told
- **Good:** a run without `--apply` prints what it would change and changes no tracked file and no working directory
- **Bad:** a run without `--apply`, or after the human declines the confirmation, removes or writes a tracked file or a working directory

A script of this kind changes nothing until it is told to. Without `--apply`, or where it asks for a
confirmation and the answer is no, it only reports what it would do and leaves every tracked file and
every working directory as they stand. A report may be written to a path that git ignores. A new
script of the kind puts each change behind that act, so that the run without it is only a report.

## Examples

### The rest of the exemplar

The exemplar's fetch of the remote before it judges, its listing of each working directory with the
reason for keeping or removing it, its removal of nested directories first, and its exit code 1 for a
removal that failed stand here as examples. The kind holds no rule on these: a new script of the kind
may do each of them another way.

## Where in code

- `task-cycle/`
- `elements/common/`
- `installation/`
