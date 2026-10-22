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

## relation-model-directory-contents

Where {merge-onto} exists, `relation-model/` holds the script that computes fingerprints.

- **Method:** review
- **Rests on:** none
- **Derives from:** WAY-09
- **Part:** relation-model
- **Violated:** no

## return-step-record

Where {merge-onto} exists, every change against {fork-point} holds, in one of its commits, the record of its task's return step.

- **Method:** review
- **Rests on:** none
- **Derives from:** WAY-11
- **Part:** every
- **Violated:** no

## foundation-change-path

No change that, against {fork-point}, alters a foundation entry runs on the path for tasks that leave the foundation unchanged.

- **Method:** review
- **Rests on:** none
- **Derives from:** WAY-13
- **Part:** every
- **Violated:** no

## derived-file-content

Every derived file git tracks that its generator can produce from scratch is identical to what the generator produces on the same commit, except for the values that file declares as varying between runs.

- **Method:** review
- **Rests on:** none
- **Derives from:** WAY-04 · WAY-53
- **Part:** every
- **Violated:** no

## ci-checking-commands

No CI configuration git tracks runs a checking command other than `python -B gate/run_tests.py`.

- **Method:** review
- **Rests on:** none
- **Derives from:** WAY-16
- **Part:** every
- **Violated:** no

## decisions-found-for-change

The decisions found for a change against {fork-point} include every decision whose scope names a part the change touches.

- **Method:** review
- **Rests on:** git-path-patterns
- **Derives from:** WAY-21
- **Part:** every
- **Violated:** no

## outbound-link-reach

No file git tracks contains a link into a repository that a reader not signed in to its host cannot open, or into a private note collection, other than a link in the `## Backlog` section of the root `AGENTS.md` to the place of the repository's tasks.

- **Method:** review
- **Rests on:** none
- **Derives from:** WAY-27
- **Part:** every
- **Violated:** no

## inherited-rationale-source

The *Rationale* of every inherited decision in the decision log is `unknown`, a quotation with its source, or attributed to the human who gave it.

- **Method:** review
- **Rests on:** none
- **Derives from:** WAY-29
- **Part:** decisions
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

No script git tracks starts a program other than git or a command the product declares in its repository.

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

Every part map identifier referred to from the foundation, a test or a generated rule file stands in the part map as an entry or as a withdrawn identifier.

- **Method:** review
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

## invariant-tests-of-change

The invariant tests of a change include every file that is an invariant test on "{fork-point}" or on the commit being checked.

- **Method:** review
- **Rests on:** none
- **Derives from:** WAY-65
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

Before approval, the project readiness check rejects a definition whose Technology section is missing or reads `none`, or holds a line that is no choice item, a choice still open, or a choice that names neither a decision as `<PREFIX>-<NN>/<version>` nor a question a heading of a projected decision holds.

- **Method:** test
- **Rests on:** none
- **Derives from:** WAY-121
- **Part:** project-level
- **Violated:** no

## project-plan-form

The project plan check rejects a plan with no valid `Status:` line, a header that names no
definition it can read or a fingerprint other than the one that definition's gate record holds and
its text gives, a definition whose In scope is not `none` and holds no top-level list item, a
second-level section that is missing, repeated, out of order, empty, without the table the template
puts in it or not one of the template's, a change log with no dated item, a table with no row or
whose header row, separator row or any cell differs from the form the plan template gives, a number
or a name held by two tasks, or a task whose state the template's list does not hold or names the
task itself.

- **Method:** test
- **Rests on:** none
- **Derives from:** WAY-142 · WAY-144 · WAY-146 · WAY-147
- **Part:** project-level
- **Violated:** no

## project-plan-check

The project plan check rejects a plan in which a projected entry of its definition has no task
realizing it, not exactly one of those tasks writing it into the foundation, or more than one row;
an item of the definition's In scope has no task; a task depends on itself, directly or through
other tasks; a preparatory task has no task depending on it; an open question of the definition
does not stand in the plan exactly once, word for word with the place its definition gives it, with
a task of the plan or an answer; or a cell or an item
names a task, a projected entry, an In scope item or an open question that the plan or its
definition does not hold.

- **Method:** test
- **Rests on:** none
- **Derives from:** WAY-143 · WAY-145 · WAY-146
- **Part:** project-level
- **Violated:** no

## skill-entry-points

Every file named `SKILL.md` that git tracks, or that stands untracked and not ignored by git, outside the `.claude/` and `.agents/` directories at the repository's root, with `<name>` the name its frontmatter gives, has a file `.claude/skills/the-way-<name>/SKILL.md` and a byte-identical file `.agents/skills/the-way-<name>/SKILL.md`, whose frontmatter names `the-way-<name>` and gives a description starting with the description the frontmatter of that `SKILL.md` gives, whose text contains, in backticks, the path of that `SKILL.md` from the repository's root, and contains `--show-superproject-working-tree`, `git ls-files --stage -- ':/.the-way'`, `git rev-parse --show-toplevel` and the words "If the skill tells you to resolve a link to find the-way, skip that", and whose text holds a sentence that names, each in backticks, the name of every such `SKILL.md` and holds the words "with the `the-way-` prefix, never an unprefixed one"; and every directory in `.claude/skills/` or `.agents/skills/` whose name begins with `the-way-` is named `the-way-<name>` for the `<name>` of such a `SKILL.md`.

- **Method:** test
- **Rests on:** none
- **Derives from:** WAY-127
- **Part:** every
- **Violated:** no

## instruction-file-imports

No repository instruction file of the-way holds, outside code spans and fenced code blocks, an `@` that stands at the start of a line or right after whitespace, `(`, `[`, `{`, `"`, `'`, `“`, `‘` or `„` and is followed by a character other than whitespace, except the first line of the root `CLAUDE.md` when it reads `@AGENTS.md` and nothing else; the root `AGENTS.md` or `CLAUDE.md` names by its path a Markdown file that git tracks, one whose name ends in `.md` or `.markdown`, when that file's path from the repository's root, written with `/` or with `\` between directories, stands anywhere in its text with no ASCII letter or digit and none of `.`, `-`, `_`, `/` and `\` right before it, a code span runs from a run of backticks to the next run of as many backticks on the same line, and a fenced code block runs from a line whose first characters other than spaces are three backticks or three tildes to the next such line.

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

For each task of a valid handed-over plan with an approved definition, the plan-state reader uses
existing recorded task provenance to establish that cycle traces belong to the current plan's
task before proposing ready for cycle to in cycle only from a matching working-cycle directory
in a Git-listed worktree or a commit touching that task's exact archived cycle directory or in
cycle to done only from a cycle-record commit reachable in freshly fetched product integration
history, reports both transitions together when both proofs hold for a ready task, reports
missing or ambiguous task provenance as unchecked and contradictory task provenance for human
reconciliation without proposing progress from either, and exposes incomplete, failed or
conflicting observations without unsupported progress or edits to the plan or task documents.

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

## guidelines-form

Every file `guidelines/<name>.md` holds, in their order, the header lines, sections, rules, rule fields and tables that the template of guidelines and the template of its discipline require at the commit of the-way the repository uses — the commit checked, in the-way itself, and the pinned commit, in a product — each with the values and the links those templates give it, with a name that agrees with its *Discipline*, each section or rule it drops reading `none —` with a decision of the log and that decision's fingerprint, each part it names being a part of the map, and each path under `## Where in code` naming something git tracks.

- **Method:** test
- **Rests on:** none
- **Derives from:** WAY-170 · WAY-171
- **Part:** every
- **Violated:** no

## guidelines-reference-current

Every reference outside fenced code in a file `guidelines/<name>.md` — a decision number of the log or an identifier of the invariants file followed by `@` and a run of letters and digits, or any identifier followed by `@` and eight lower-case hexadecimal characters — names a decision of the log that is not repealed or an invariant of the file that is not withdrawn, and carries the fingerprint of that entry's binding part in the foundation of the same commit and, where {merge-onto} exists, in the foundation a merge onto {merge-onto} leaves.

- **Method:** test
- **Rests on:** none
- **Derives from:** WAY-169
- **Part:** product-guidelines · decisions · invariants · agent-instructions · relation-model
- **Violated:** no

## guidelines-check-form

The form check of guidelines, `product-guidelines/form_check.py`, reports as an error every header line, section, rule or rule field that the template of guidelines or the template of a file's discipline requires and a file `guidelines/<name>.md` lacks or holds out of order, every section or rule dropped with a text other than `none —` followed by a decision of the log and a fingerprint, every part named in *Applies to* or in a file's name that the part map does not hold, and every file whose name and *Discipline* disagree.

- **Method:** test
- **Rests on:** none
- **Derives from:** WAY-170 · WAY-171 · WAY-202
- **Part:** product-guidelines · decisions · invariants · part-map · elements-common · relation-model
- **Violated:** no

## guidelines-check-carrier

The form check of guidelines, `product-guidelines/form_check.py`, reports as an error every rule under `## Rules` of a file `guidelines/<name>.md` whose *Decision* holds no decision number with the log's prefix followed by `@`, every such rule whose *Invariant* holds no identifier of the invariants file followed by `@` in a file whose discipline's template requires an invariant in every rule, and every decision the table of roles of a styleguide names that the rule `### Each role in its meaning` does not name, unless that rule is dropped.

- **Method:** test
- **Rests on:** none
- **Derives from:** WAY-168 · WAY-188 · WAY-189 · WAY-196
- **Part:** product-guidelines · decisions · invariants · part-map · elements-common · relation-model
- **Violated:** no

## guidelines-check-colour-pair

The form check of guidelines, `product-guidelines/form_check.py`, reports as an error every role of the kind `background` in the table of roles of a styleguide whose *Text on it* is empty or names no role of the kind `text` in that table.

- **Method:** test
- **Rests on:** none
- **Derives from:** WAY-176
- **Part:** product-guidelines · decisions · invariants · part-map · elements-common · relation-model
- **Violated:** no

## guidelines-check-reference-target

The form check of guidelines, `product-guidelines/form_check.py`, reports as an error every reference outside fenced code in a file `guidelines/<name>.md` — a decision number of the log or an identifier of the invariants file followed by `@` and a run of letters and digits, or any identifier followed by `@` and eight lower-case hexadecimal characters — that names a decision the log does not hold or has repealed, or an invariant the file does not hold or has withdrawn, and every such reference after a decision number or an invariant's identifier whose part after `@` is not eight lower-case hexadecimal characters.

- **Method:** test
- **Rests on:** none
- **Derives from:** WAY-169
- **Part:** product-guidelines · decisions · invariants · part-map · elements-common · relation-model
- **Violated:** no

## guidelines-check-stale-reference

The form check of guidelines, `product-guidelines/form_check.py`, reports as an error every reference outside fenced code in a file `guidelines/<name>.md` to a decision of the log or an invariant of the file whose fingerprint differs from that entry's current fingerprint on the commit checked and, given "{merge-onto}", every one whose fingerprint differs from that entry's current fingerprint in the foundation a merge onto that commit leaves.

- **Method:** test
- **Rests on:** none
- **Derives from:** WAY-169
- **Part:** product-guidelines · decisions · invariants · part-map · elements-common · relation-model
- **Violated:** no

## guidelines-check-code-path

The form check of guidelines, `product-guidelines/form_check.py`, reports as an error every path under `## Where in code` of a file `guidelines/<name>.md` that is absolute, holds a `..` segment, a drive or a UNC prefix, or names nothing git tracks.

- **Method:** test
- **Rests on:** none
- **Derives from:** WAY-170
- **Part:** product-guidelines · decisions · invariants · part-map · elements-common · relation-model
- **Violated:** no

## guidelines-check-kind-index

The form check of guidelines, `product-guidelines/form_check.py`, reports as an error every file `guidelines/coding-<kind>.md` git tracks that no row of the table under `## Kinds of code` in `guidelines/coding.md` names by its path in *File*, every row of that table whose *File* names no file git tracks, whose *Kind* is not the `<kind>` of the file its *File* names or whose *When to read* is empty, and every file `guidelines/coding-<kind>.md` git tracks where git tracks no `guidelines/coding.md`.

- **Method:** test
- **Rests on:** none
- **Derives from:** WAY-167 · WAY-212
- **Part:** product-guidelines · decisions · invariants · part-map · elements-common · relation-model
- **Violated:** no

## guidelines-check-exemplar

The form check of guidelines, `product-guidelines/form_check.py`, reports as an error every file `guidelines/coding-<kind>.md` whose table under `## Files of this kind` holds no row, or more than one, whose *Status* is `exemplar`, every row of that table whose *Status* is not `exemplar`, `copy` or `do not copy`, whose *File* is absolute, holds a `..` segment, a drive or a UNC prefix or names nothing git tracks, or which is not the `exemplar` row and whose *Decision* is not `—`, and every `exemplar` row whose *Decision* names no decision the log holds and has not repealed, or names one whose binding sentences, their whitespace collapsed, lack its *File* in backticks or the file's `<kind>` in backticks.

- **Method:** test
- **Rests on:** none
- **Derives from:** WAY-198 · WAY-199
- **Part:** product-guidelines · decisions · invariants · part-map · elements-common · relation-model
- **Violated:** no

## guidelines-check-example-files

The form check of guidelines, `product-guidelines/form_check.py`, reports as an error every rule under `## Rules` of a file `guidelines/<name>.md` whose *Invariant* names an invariant other than `guidelines-form` and whose text after its fields does not hold, for each such invariant, exactly one fenced block whose opening line's info string reads `good <identifier> <path>` and exactly one whose info string reads `bad <identifier> <path>`, optionally with exactly one `base <identifier> <path>` block whose path equals both cases' paths, `<identifier>` being that invariant's, and, in such a rule, every such block whose `<identifier>` its *Invariant* does not name or whose `<path>` is absolute, holds a `..` segment, a drive or a UNC prefix, every line inside such a block that would open a fence, every other fenced block, and every such block left open to the end of the file, and every `base` block under any rule naming no invariant other than `guidelines-form`.

- **Method:** test
- **Rests on:** none
- **Derives from:** WAY-168
- **Part:** product-guidelines · decisions · invariants · part-map · elements-common · relation-model
- **Violated:** no

## Withdrawn identifiers

| Identifier | Why | Successors |
|---|---|---|
| invariant-test-change-acceptance | replaced: a change to an invariant test is covered by the one independent assessment of any change to an invariant test or to the foundation | foundation-change-assessment-record |
| foundation-change-panel-record | replaced: the record of a panel of two assessors and two settlements became the record of one independent assessment and of how each remark was settled | foundation-change-assessment-record |
| foundation-search-record | withdrawn: the author's one search of the foundation is not repeated before the merge and leaves no record (WAY-33) | none |
| view-versions | withdrawn: the decision log holds one entry for each decision and says what binds today, with no view generated from it (WAY-18) | none |
| view-links | withdrawn: the decision log holds one entry for each decision and says what binds today, with no view generated from it (WAY-18) | none |
| foundation-change-assessment-record | withdrawn: a change to an invariant test or to the foundation has no assessment of its own; the review of the change and the human at the merge read it (WAY-10) | none |
| invariant-test-break | withdrawn: an invariant's test is seen failing once by the agent that writes it, with no deliberate break accepted apart from that (WAY-08) | none |
| invariant-correction-confirmation | withdrawn: an invariant carries no version, so no correction keeps one (WAY-57) | none |
| gate-fork-point-evidence | withdrawn: a recovered invariant names in *Derives from* the place in the code that shows it, with no run on the older commit (WAY-58) | none |
| gate-method-order | withdrawn: an invariant's method is a test of the product's suite, which reads no other method's run (WAY-61) | none |
| gate-unchecked-reason | withdrawn: the invariants template keeps no closed list of reasons for `unchecked` (WAY-63) | none |
| gate-missing-script | withdrawn: an invariant's method names no command and no script (WAY-105) | none |
| gate-quarantine-result | withdrawn: a test giving different verdicts on one commit is fixed as any test is, with no quarantine (WAY-68) | none |
| fact-verdict-citation | withdrawn: an environment fact names no method, and no check cites it (WAY-81) | none |
| gate-fact-run | withdrawn: no check of an environment fact runs on a change (WAY-82) | none |
| fact-clock-exit | withdrawn: no clock runs the checks of environment facts (WAY-82) | none |
| map-fingerprint-input | withdrawn: a reference names an entry of the part map by its identifier alone, and no fingerprint is computed for it (WAY-42) | none |
| flow-test-run | withdrawn: a critical flow has no entry in the part map, and its test runs with the rest of the product's suite (WAY-45) | none |
| generated-pattern-source | withdrawn: no rule file is generated from the part map for an agent (WAY-52) | none |
| derived-subset-naming | withdrawn: no derived file is compared as a subset of its earlier version (WAY-53) | none |
| decision-guard-stale-reference | withdrawn: a reference names an entry by its identifier alone, with no fingerprint for a guard to compare with the current wording (WAY-02) | none |
| gate-check-source | withdrawn: no program picks checks from the methods written in the entries; one command runs all of a product's tests (WAY-16) | none |
| gate-boundary-change | withdrawn: no program picks the checks of a change; a change touching the files of a trust boundary is checked for crafted input and reviewed for that risk (WAY-48) | none |
| gate-verdict-per-entry | withdrawn: no run records a verdict for each entry; an invariant's result is the outcome of the tests citing it (WAY-63, WAY-74) | none |
| gate-pass-without-verdict | withdrawn: no program reports a result for each invariant; a run in which no test citing an invariant ran gives it no pass (WAY-61, WAY-63) | none |
| change-reach | withdrawn: no program finds the invariants a change reaches; the agent making the change reads them (WAY-62) | none |
| gate-result-values | withdrawn: no program reports a result for each invariant; an invariant's result is `pass` or `fail` from the tests citing it (WAY-63) | none |
| gate-reported-set | withdrawn: no program reports a result for each invariant a change reaches; every test runs on every change (WAY-16, WAY-63) | none |
| run-record-form | withdrawn: the-way keeps no record of a run of its own (WAY-74) | none |
| run-record-lines | withdrawn: the-way keeps no record of a run of its own (WAY-74) | none |
| test-runner-pass-line | withdrawn: the test runner records no verdict for each invariant a test cites; its exit code says whether a test failed (WAY-63, WAY-74) | none |
| log-reference-target | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| binding-sentence-count | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| binding-sentence-words | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| decision-example-numbers | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| decision-template-change | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| log-existing-lines | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| log-versions-added-per-number | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| log-merge-copies | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| invariant-method-form | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| invariant-example-target | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| map-example-target | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| glossary-example-target | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| decision-verification-level | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| level-one-decision-invariants | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| verification-invariant-derivation | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| decision-approval-record | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| decision-approver | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| decision-heading-form | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| decision-version-sequence | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| decision-change-kind | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| decision-binding-across-versions | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| repeal-binding-sentences | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| decision-scope-names | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| review-when-form | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| review-next-check | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| review-named-version | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| narrows-pairs | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| inherited-origin-form | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| relation-fingerprint-presence | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| relation-fingerprint-value | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| relation-type | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| map-entry-kinds | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| map-section-kinds | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| part-map-file | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| map-identifier-form | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| identifier-holders | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| map-withdrawal-successors | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| map-identifier-persistence | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| map-entry-version | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| file-part-assignment | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| path-pattern-reach | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| left-out-file-assignment | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| flow-part-names | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| flow-invariant-link | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| map-invariant-names | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| failure-mode-severity | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| failure-mode-detection | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| part-criticality-field | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| flow-coverage-parts | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| external-exchange-row | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| surface-promise-level | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| surface-declaration | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| map-withdrawal-date | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| promise-level-policy | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| surface-change-path | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| known-violation-coverage | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| known-violations-growth | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| known-violation-currency | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| known-violation-fields | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| known-violation-line-number | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| flow-test-location | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| invariant-sentence-count | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| invariant-identifier-form | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| invariant-version-number | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| invariant-version-new | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| invariant-version-changed | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| invariant-version-unchanged | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| invariant-earlier-wording | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| invariant-citation-version | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| invariant-recovered-form | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| invariant-recovered-derived | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| sentence-branch-names | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| sentence-gate-values | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| method-gate-values | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| invariant-part-names | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| invariant-part-form | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| invariants-file | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| invariant-identifier-persistence | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| invariant-withdrawal-persistence | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| withdrawal-successors | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| invariant-citation-target | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| data-line-target | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| link-fingerprint-presence | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| link-fingerprint-value | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| violated-list-growth | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| violated-position-version | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| quarantine-position-form | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| quarantine-flow-invariants | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| log-entry-field-presence | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| log-entry-field-words | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| log-entry-merge-todo | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| map-entry-field-presence | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| map-entry-field-words | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| invariant-entry-field-presence | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| invariant-entry-field-words | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| invariant-entry-merge-todo | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| run-record-path | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| environment-facts-file | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| fact-identifier-form | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| fact-identifier-persistence | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| fact-withdrawal-persistence | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| fact-withdrawal-successors | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| fact-sentence-count | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| fact-scope-word | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| fact-version-new | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| fact-version-changed | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| fact-version-unchanged | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| fact-citation-version | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| fact-source-form | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| fact-method-form | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| fact-citation-target | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| based-on-fact-fingerprint | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| based-on-fact-fingerprint-value | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| human-verdict-invariant-row | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| human-verdict-fact-row | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| fact-dependants | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| fact-entry-field-presence | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| fact-entry-field-words | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| glossary-file | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| glossary-file-sections | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| glossary-term-holder | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| glossary-entry-field-presence | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| glossary-entry-field-words | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| glossary-term-use | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| glossary-definition-count | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| glossary-definition-words | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| glossary-entry-version | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| glossary-avoid-growth | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| glossary-avoid-single | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| glossary-avoid-term | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| glossary-avoid-carrier | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| glossary-not-target | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| glossary-not-quoted-word | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| glossary-entry-merge-todo | withdrawn: no format guard checks the foundation; `elements/common/foundation_check.py` checks its identifiers, references and fields | none |
| decision-fingerprint-input | withdrawn: it held a behaviour of a format guard, and no format guard checks the foundation | none |
| decision-guard-overdue-review | withdrawn: it held a behaviour of a format guard, and no format guard checks the foundation | none |
| map-guard-missing-command | withdrawn: it held a behaviour of a format guard, and no format guard checks the foundation | none |
| map-guard-unrecorded-criticality | withdrawn: it held a behaviour of a format guard, and no format guard checks the foundation | none |
| map-guard-dependency-report | withdrawn: it held a behaviour of a format guard, and no format guard checks the foundation | none |
| criticality-lowering-report | withdrawn: it held a behaviour of a format guard, and no format guard checks the foundation | none |
| map-guard-missing-coverage | withdrawn: it held a behaviour of a format guard, and no format guard checks the foundation | none |
| map-guard-test-runs | withdrawn: it held a behaviour of a format guard, and no format guard checks the foundation | none |
| invariant-fingerprint-input | withdrawn: it held a behaviour of a format guard, and no format guard checks the foundation | none |
| fact-fingerprint-input | withdrawn: it held a behaviour of a format guard, and no format guard checks the foundation | none |
| glossary-term-collision | withdrawn: it held a behaviour of a format guard, and no format guard checks the foundation | none |
| glossary-definition-uses | withdrawn: it held a behaviour of a format guard, and no format guard checks the foundation | none |
| glossary-process-terms | withdrawn: it held a behaviour of a format guard, and no format guard checks the foundation | none |
| gate-human-verdict | withdrawn: the foundation records no human verdict | none |
| gate-guidelines-example-evidence | withdrawn: no gate reports how the method of an invariant meets the uses of a rule of guidelines | none |
