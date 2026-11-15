# Coding guidelines — shared-module

- **Discipline:** coding
- **Applies to:** relation-model

## When to read

Before adding or changing a file of the kind `shared-module`: a module that other scripts import.

## Files of this kind

| File | Status | Decision |
|---|---|---|
| `relation-model/fingerprint.py` | `exemplar` | WAY-391 |

## Rules

### Importing runs nothing

- **Decision:** WAY-391
- **Invariant:** shared-module-import-runs-nothing
- **Good:** a module whose top level only defines functions and constants
- **Bad:** a module that reads its input, writes output or starts a program when it is imported

A file of this kind holds what other scripts import. Code that reads input or writes output stays
under `if __name__ == "__main__":`, so that importing the file runs nothing. The invariant's test
starts a new interpreter that imports the module with its input closed, and checks that it ends with
exit code 0 and writes and reads nothing.

## Examples

### The rest of the exemplar

The exemplar's normalization of a text before its digest, and its choice of the leading characters
of that digest, stand here as an example. The kind holds no rule on these; the rule on importing
above is the one that binds.

## Where in code

- `relation-model/`
