# Coding guidelines — measuring-report

- **Discipline:** coding
- **Applies to:** task-cycle · process-audit · project-level

## When to read

Before adding or changing a file of the kind `measuring-report`: a script that counts figures from
the files of a run, a history or a repository, and writes them as a report that a person or a skill
reads.

## Files of this kind

| File | Status | Decision |
|---|---|---|
| `task-cycle/cycle_measures.py` | `exemplar` | WAY-387 |
| `task-cycle/change_file_sizes.py` | `copy` | — |
| `task-cycle/review_reminder.py` | `copy` | — |
| `process-audit/audit_count.py` | `copy` | — |
| `task-cycle/slice_size.py` | `do not copy` | — |
| `task-cycle/cycle_stages.py` | `copy` | — |
| `project-level/plan_state.py` | `do not copy` | — |

## Rules

none — WAY-387

## Examples

### The rest of the exemplar

The exemplar's reading of each session's transcripts and of the homes they lie in, its pairing of
tool calls with their results, and its report of the figures as a Markdown table stand here as
examples. The kind holds no rule on these: a new measure may do each of them another way. Its
reading of a transcript's fields, which ends the run with exit code 2 and a message naming the file
and the field where one is missing, follows WAY-344 and stands here as an example too.

## Where in code

- `task-cycle/`
- `process-audit/`
- `project-level/`
