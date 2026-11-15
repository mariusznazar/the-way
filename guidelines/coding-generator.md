# Coding guidelines — generator

- **Discipline:** coding
- **Applies to:** agent-instructions

## When to read

Before adding or changing a file of the kind `generator`: a script that writes files into the
repository it runs in, such as the entry points of the skills or the copies of a definition, from
the files it reads.

## Files of this kind

| File | Status | Decision |
|---|---|---|
| `agent-instructions/skill_entry_points.py` | `exemplar` | WAY-388 |
| `agent-instructions/agent_type_copies.py` | `copy` | — |

## Rules

### Writing only with `--write`

- **Decision:** WAY-388
- **Invariant:** generator-writes-only-with-write
- **Good:** a run without `--write` prints each change and orphan it finds, and writes no file
- **Bad:** a run without `--write` creates, changes or removes a file of the repository

A generator of this kind writes a file only where its `--write` option is given. Without the option
it reports each file it would create or change and each orphan it would leave, and it changes
nothing, also where it finds a file to create, a file to change or an orphan to list. A new
generator puts every write behind that option, so that the run without it is only a report.

## Examples

### The rest of the exemplar

The exemplar's reading of each skill's frontmatter, its listing of the repository's files through
git, its message for each orphan, and its exit code 2 at a missing field, which WAY-344 gives, stand
here as examples. The kind holds no rule on these: a new generator may do each of them another way.

## Where in code

- `agent-instructions/`
