# Invariants

What the-way states as true or false on every commit, each checked by a test or by review. The
rules of an entry stand in `elements/invariants/template.md`.

## foundation-file-kinds

Every file in `foundations/` holds the entries of one of the five foundation elements, or is a file an element's template or the part the elements share names.

- **Method:** review
- **Rests on:** none
- **Derives from:** WAY-04
- **Part:** every
- **Violated:** no

## foundation-change-merge-route

Where {merge-onto} exists, every commit of the first-parent history of {merge-onto} that alters a foundation entry against its first parent is a merge.

- **Method:** review
- **Rests on:** none
- **Derives from:** WAY-01
- **Part:** every
- **Violated:** no

## repository-file-location

Where {merge-onto} exists, every file git tracks lies in `foundations/` or in a directory WAY-09 names for a part of the process, belongs to the `repository` or the `agent-instructions` part of the part map, or is the `README.md` at the root.

- **Method:** review
- **Rests on:** none
- **Derives from:** WAY-09
- **Part:** every
- **Violated:** no

## element-directory-contents

Where {merge-onto} exists, every element directory holds a template, examples or a pointer to entries of the-way that serve as its examples, and a skill.

- **Method:** review
- **Rests on:** none
- **Derives from:** WAY-09
- **Part:** decisions · part-map · invariants · glossary · environment-facts
- **Violated:** no

## return-step-record

Where {merge-onto} exists, every change against {fork-point} holds, in one of its commits, the record of its task's return step.

- **Method:** review
- **Rests on:** none
- **Derives from:** WAY-11
- **Part:** every
- **Violated:** no

## derived-file-content

Every derived file git tracks that its generator can produce from scratch is identical to what the generator produces on the same commit, except for the values that file declares as varying between runs.

- **Method:** test
- **Rests on:** none
- **Derives from:** WAY-225 · WAY-53
- **Part:** every
- **Violated:** no

## ci-checking-commands

No CI configuration git tracks runs a checking command other than `python -B gate/run_tests.py`.

- **Method:** review
- **Rests on:** none
- **Derives from:** WAY-16
- **Part:** every
- **Violated:** no

## outbound-link-reach

No file git tracks contains a link into a repository that a reader not signed in to its host cannot open, or into a private note collection, other than a link in the `## Backlog` section of the root `AGENTS.md` to the place of the repository's tasks.

- **Method:** review
- **Rests on:** none
- **Derives from:** WAY-27
- **Part:** every
- **Violated:** no

## skill-rule-source

Every element's skill names its element's template and `elements/common/` as the source of the rules of its entries, and `elements/common/` as the source of the way of working the skills share.

- **Method:** review
- **Rests on:** none
- **Derives from:** WAY-35
- **Part:** decisions · part-map · invariants · glossary · environment-facts
- **Violated:** no

## script-language

Every script git tracks is a Python file.

- **Method:** review
- **Rests on:** none
- **Derives from:** WAY-38
- **Part:** every
- **Violated:** no

## script-imports

No script git tracks imports a module other than one of the standard library of Python 3.14 or a Python file git tracks.

- **Method:** review
- **Rests on:** python-stdlib-modules
- **Derives from:** WAY-38 · WAY-89
- **Part:** every
- **Violated:** no

## script-subprocesses

No script git tracks starts a program other than git, the Python interpreter running the script, or a command the product declares in its repository.

- **Method:** review
- **Rests on:** none
- **Derives from:** WAY-38
- **Part:** every
- **Violated:** no

## fingerprint-definition

The script of `relation-model` gives a text the first eight characters, in lower-case hexadecimal, of the SHA-256 digest of that text encoded in UTF-8, after every run of spaces and line breaks is replaced by a single space and both ends are trimmed.

- **Method:** test
- **Rests on:** sha-256 · utf-8
- **Derives from:** WAY-02
- **Part:** relation-model
- **Violated:** no

## map-reference-target

Every part map identifier a field of a foundation entry names is an entry of the part map.

- **Method:** test
- **Rests on:** none
- **Derives from:** WAY-41
- **Part:** every
- **Violated:** no

## generated-overview

No file generated for an agent holds an overview of the repository's directories.

- **Method:** review
- **Rests on:** none
- **Derives from:** WAY-52
- **Part:** part-map · agent-instructions
- **Violated:** no

## gate-exit-code

`gate/run_tests.py` exits non-zero when a test it runs fails or errs, a test module it finds cannot be imported, a test marked as an expected failure passes or a directory it runs holds no test, and zero when every test it runs passes; run without a directory, it runs the tests of every directory holding a `test_*.py` file that git tracks and the working tree holds, and exits non-zero also when no directory holds such a file or a directory's run exits zero without a report that `unittest` ends with OK.

- **Method:** test
- **Rests on:** none
- **Derives from:** WAY-63 · WAY-16
- **Part:** gate
- **Violated:** no

## python-version-declared

The repository declares Python 3.14 in `.python-version`.

- **Method:** review
- **Rests on:** none
- **Derives from:** WAY-89
- **Part:** repository
- **Violated:** no

## project-definition-form

The project readiness check rejects a definition with no valid `Status:` line, a missing,
repeated or unexpected required second-level section, or required sections out of order.

- **Method:** test
- **Rests on:** none
- **Derives from:** WAY-108
- **Part:** project-level
- **Violated:** no

## project-readiness-gate

Before approval, the project readiness check rejects a definition with a missing or unresolved
required section, an open question with no place of resolution, or an unfinished candidate search.

- **Method:** test
- **Rests on:** none
- **Derives from:** WAY-118
- **Part:** project-level
- **Violated:** no

## project-technology-record

Before approval, the project readiness check rejects a definition whose Technology section is missing or reads `none`, or holds a line that is no choice item, a choice still open, or a choice that names neither a decision as `<PREFIX>-<NN>` nor a question a heading of a projected decision holds.

- **Method:** test
- **Rests on:** none
- **Derives from:** WAY-121
- **Part:** project-level
- **Violated:** no

## project-plan-form

The project plan check rejects a plan whose `Status:` line, sections, tables, change log or task
states depart from the form the plan template gives, in which two tasks hold one number or one name
or a task's state names the task itself, whose header names no definition the check can read or a
fingerprint other than the one that definition's gate record holds and its text gives, or whose
definition holds an In scope that is neither `none` nor a list.

- **Method:** test
- **Rests on:** none
- **Derives from:** WAY-142 · WAY-144 · WAY-146 · WAY-147
- **Part:** project-level
- **Violated:** no

## project-plan-check

The project plan check rejects a plan in which a projected entry of its definition has no task
realizing it, not exactly one task writing it into the foundation, or more than one row; an item of
the definition's In scope has no task; a task depends on itself, directly or through other tasks; a
preparatory task has no task depending on it; two tasks, neither done, delivered by another task
or dropped, realize the same projected entry while neither depends on the other, directly or
through other tasks, and no item of the change log lets the two go side by side on that entry with
a reason; an open question of the definition does not stand in the plan exactly once, word for
word with the place its definition gives it, with a task of the plan or an answer; or a cell or an
item of the open questions names a task, an entry, an item or a question that the plan or its
definition does not hold.

- **Method:** test
- **Rests on:** none
- **Derives from:** WAY-143 · WAY-145 · WAY-146 · WAY-230
- **Part:** project-level
- **Violated:** no

## skill-entry-points

Every file named `SKILL.md` that git tracks, or that stands untracked and not ignored by git, outside the `.claude/` and `.agents/` directories at the repository's root, with `<name>` the name its frontmatter gives, has a byte-identical pair of entry points, `.claude/skills/the-way-<name>/SKILL.md` and `.agents/skills/the-way-<name>/SKILL.md`, whose frontmatter names `the-way-<name>` and gives a description starting with that skill's description, and whose text leads a session to that `SKILL.md` in the checkout or worktree it works in and names every such skill to be called with the `the-way-` prefix, never an unprefixed one; and every directory in `.claude/skills/` or `.agents/skills/` whose name begins with `the-way-` is named `the-way-<name>` for the `<name>` of such a `SKILL.md`.

- **Method:** test
- **Rests on:** none
- **Derives from:** WAY-127
- **Part:** every
- **Violated:** no

## instruction-file-imports

No repository instruction file of the-way holds, outside code spans and fenced code blocks, an `@` that a tool loading the file would take for an import, except the first line of the root `CLAUDE.md` when it reads `@AGENTS.md` and nothing else.

- **Method:** test
- **Rests on:** none
- **Derives from:** WAY-129
- **Part:** every
- **Violated:** no

## root-claude-md-import

Where git tracks a `CLAUDE.md` at the repository's root, its text begins with `@AGENTS.md` followed directly by a line break, `\n` or `\r\n`, or by the end of the text.

- **Method:** test
- **Rests on:** none
- **Derives from:** WAY-132
- **Part:** agent-instructions
- **Violated:** no

## installation-claude-guidance

For a product with no root `CLAUDE.md`, the installation command creates that file with `@AGENTS.md` as its sole line; for a product with an existing root `CLAUDE.md`, it preserves the file byte for byte and warns in the installation plan before confirmation when the file has no effective `@AGENTS.md` import; in neither case does it write `.claude/rules/the-way.md`.

- **Method:** test
- **Rests on:** claude-code-imports
- **Derives from:** WAY-141
- **Part:** installation
- **Violated:** no

## project-plan-state-evidence

For each task of a valid handed-over plan with an approved definition, the plan-state reader
proposes a move to in cycle only from the task's working cycle directory in a worktree git lists or
a commit of its archived cycle directory, and a move to done only from a cycle record reachable in
the product's freshly fetched integration history, each tied to the task by its recorded
provenance; it proposes both moves together where both proofs hold, reports missing or ambiguous
provenance as unchecked and contradictory provenance for the human to reconcile, reports
incomplete, failed or conflicting evidence instead of proposing progress from it, and edits no plan
or task document.

- **Method:** test
- **Rests on:** none
- **Derives from:** WAY-153
- **Part:** project-level
- **Violated:** no

## project-plan-state-subprocesses

Every subprocess the plan-state reader starts runs Git.

- **Method:** test
- **Rests on:** none
- **Derives from:** WAY-153
- **Part:** project-level
- **Violated:** no
