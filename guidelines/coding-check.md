# Coding guidelines — check

- **Discipline:** coding
- **Applies to:** task-cycle · project-level · elements-common · instruction-files

## When to read

Before adding or changing a file of the kind `check`: a script that reads the files of a repository,
or one file it names, and reports the places that break a rule.

## Files of this kind

| File | Status | Decision |
|---|---|---|
| `task-cycle/tracked_private_paths_check.py` | `exemplar` | WAY-386 |
| `task-cycle/image_files_check.py` | `copy` | — |
| `task-cycle/private_paths_check.py` | `copy` | — |
| `task-cycle/remarks_check.py` | `copy` | — |
| `task-cycle/request_check.py` | `do not copy` | — |
| `project-level/readiness_check.py` | `copy` | — |
| `project-level/plan_check.py` | `copy` | — |
| `elements/common/foundation_check.py` | `copy` | — |
| `instruction-files/check_instructions.py` | `copy` | — |

## Rules

none — WAY-386

## Examples

### The rest of the exemplar

The exemplar's way of reading its one argument, of listing the files git tracks, and of reporting
each hit with its place and its exit code stands here as an example. The kind holds no rule on
these: a new check of the kind may do each of them another way.

## Where in code

- `task-cycle/`
- `project-level/`
- `elements/common/`
- `instruction-files/`
