# Invariants

What the-way states as true or false on every commit, each with its method of checking. The rules
of an entry stand in `elements/invariants/template.md`.

## decision-guard-stale-reference/1

The decision guard, given "{merge-onto}", reports every `derives from` or `narrows` relation, in the latest version of a decision in the log a merge onto that commit leaves, whose fingerprint differs from the current fingerprint there of the decision it names.

- **Method:** `python -B gate/run_tests.py gate --record .runs/gate-tests.jsonl`
- **Rests on:** none
- **Derives from:** WAY-02@af08ee5d · WAY-31@509d69d9
- **Part:** decisions · relation-model
- **Correction:** none
- **Recovered:** none

## decision-fingerprint-input/1

The fingerprint the decision guard gives a decision version is the fingerprint of its binding sentences alone.

- **Method:** `python -B gate/run_tests.py elements/decisions --record .runs/decisions-tests.jsonl`
- **Rests on:** none
- **Derives from:** WAY-02@af08ee5d
- **Part:** decisions · relation-model
- **Correction:** none
- **Recovered:** none

## log-reference-target/1

Every decision number the decision log refers to is the number of a decision in the log.

- **Method:** `python -B elements/decisions/format_guard.py foundations/decisions.md --record .runs/decisions.jsonl`
- **Rests on:** none
- **Derives from:** WAY-02@af08ee5d
- **Part:** decisions
- **Correction:** none
- **Recovered:** none

## invariant-test-change-acceptance/1

Where {merge-onto} exists, no change alters, against {fork-point}, an invariant test without carrying an accepted foundation change.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-03@4fa941a4 · WAY-10@a5941d52
- **Part:** every
- **Correction:** none
- **Recovered:** none

## foundation-file-kinds/1

Every file in `foundations/` holds the entries of one of the five foundation elements, or is a file an element's template names.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-04@f7328944
- **Part:** every
- **Correction:** none
- **Recovered:** none

## binding-sentence-count/1

Every decision version in the decision log, other than a repeal, opens with one to three binding sentences.

- **Method:** `python -B elements/decisions/format_guard.py foundations/decisions.md --record .runs/decisions.jsonl`
- **Rests on:** none
- **Derives from:** WAY-05@f0c14f2c · WAY-20@6aa77560
- **Part:** decisions
- **Correction:** none
- **Recovered:** none

## binding-sentence-words/1

No binding sentence in the decision log contains, outside code, a word the decision template forbids there.

- **Method:** `python -B elements/decisions/format_guard.py foundations/decisions.md --record .runs/decisions.jsonl`
- **Rests on:** none
- **Derives from:** WAY-05@f0c14f2c
- **Part:** decisions
- **Correction:** none
- **Recovered:** none

## decision-example-copy/1

Every example in `elements/decisions/examples.md` matches, word for word, the version of the decision log it copies.

- **Method:** `python -B elements/decisions/format_guard.py foundations/decisions.md --record .runs/decisions.jsonl`
- **Rests on:** none
- **Derives from:** WAY-05@f0c14f2c
- **Part:** decisions
- **Correction:** none
- **Recovered:** none

## decision-template-change/1

A change that, against {fork-point}, alters `elements/decisions/template.md` also adds a version to the decision log.

- **Method:** `python -B elements/decisions/format_guard.py foundations/decisions.md --base {fork-point} --record .runs/decisions-base.jsonl`
- **Rests on:** none
- **Derives from:** WAY-05@f0c14f2c
- **Part:** decisions
- **Correction:** none
- **Recovered:** none

## foundation-change-merge-route/1

Where {merge-onto} exists, every commit of the first-parent history of {merge-onto} that alters a foundation entry against its first parent is a merge.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-06@fe7c4068
- **Part:** every
- **Correction:** none
- **Recovered:** none

## log-existing-lines/1

The decision log begins with every line it held on {fork-point}, unchanged and in the same order.

- **Method:** `python -B elements/decisions/format_guard.py foundations/decisions.md --base {fork-point} --record .runs/decisions-base.jsonl`
- **Rests on:** none
- **Derives from:** WAY-07@cce4679b
- **Part:** decisions
- **Correction:** none
- **Recovered:** none

## log-versions-added-per-number/1

Against {fork-point}, the decision log gains at most one version of each number.

- **Method:** `python -B elements/decisions/format_guard.py foundations/decisions.md --base {fork-point} --record .runs/decisions-base.jsonl`
- **Rests on:** none
- **Derives from:** WAY-07@cce4679b
- **Part:** decisions
- **Correction:** none
- **Recovered:** none

## invariant-method-form/1

Every entry of `foundations/invariants.md` names as its method a command that begins with the name of the program it runs, the path alone of a file that exists, or `TODO`, alone or followed by ` — ` and what is missing.

- **Method:** `python -B elements/invariants/format_guard.py foundations/invariants.md --record .runs/invariants.jsonl`
- **Rests on:** none
- **Derives from:** WAY-08@a0bbac21 · WAY-61@c6bdfd7c · WAY-63@f16348c8
- **Part:** every
- **Correction:** none
- **Recovered:** none

## invariant-test-break/1

Every check that cites an invariant fails, in k of n runs where its command sets them, on the deliberate break it was accepted on.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-08@a0bbac21
- **Part:** every
- **Correction:** none
- **Recovered:** none

## human-verdict-trace/1

Every human verdict on an invariant names who gave it, when, and the commit it assessed.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-08@a0bbac21 · WAY-63@f16348c8
- **Part:** every
- **Correction:** none
- **Recovered:** none

## repository-file-location/1

Where {merge-onto} exists, every file git tracks lies in `foundations/` or in the directory of a part of the process, belongs to the `repository` part of the part map, or is the `README.md` at the root.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-09@6535fe83
- **Part:** every
- **Correction:** none
- **Recovered:** none

## element-directory-contents/1

Where {merge-onto} exists, every element directory holds a template, examples, a skill and a script that checks its entries.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-09@6535fe83
- **Part:** decisions · part-map · invariants · glossary · environment-facts
- **Correction:** none
- **Recovered:** none

## relation-model-directory-contents/1

Where {merge-onto} exists, `relation-model/` holds the script that computes content fingerprints.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-09@6535fe83
- **Part:** relation-model
- **Correction:** none
- **Recovered:** none

## foundation-change-panel-record/1

Where {merge-onto} exists, no change alters, against {fork-point}, an invariant test or a foundation entry without a record of the panel's two assessments and its settlement.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-10@a5941d52
- **Part:** every
- **Correction:** none
- **Recovered:** none

## return-step-record/1

Where {merge-onto} exists, every change against {fork-point} carries the record of its task's return step.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-11@a7e08204
- **Part:** every
- **Correction:** none
- **Recovered:** none

## decision-verification-level/1

Every decision version in the decision log names its level of verification, or holds `TODO` in *Verification*.

- **Method:** `python -B elements/decisions/format_guard.py foundations/decisions.md --record .runs/decisions.jsonl`
- **Rests on:** none
- **Derives from:** WAY-12@55e89140 · WAY-71@cab47c5b
- **Part:** decisions
- **Correction:** none
- **Recovered:** none

## level-one-decision-invariants/1

Every decision in force whose verification includes level 1 has at least one entry of `foundations/invariants.md` deriving from it.

- **Method:** `python -B elements/invariants/format_guard.py foundations/invariants.md --record .runs/invariants.jsonl`
- **Rests on:** none
- **Derives from:** WAY-12@55e89140 · WAY-17@ab01c0e5
- **Part:** every
- **Correction:** none
- **Recovered:** none

## verification-invariant-derivation/1

Every identifier the level 1 verification of the latest version of a decision in the decision log names is an entry of `foundations/invariants.md` whose *Derives from* names that decision.

- **Method:** `python -B elements/invariants/format_guard.py foundations/invariants.md --record .runs/invariants.jsonl`
- **Rests on:** none
- **Derives from:** WAY-12@55e89140 · WAY-17@ab01c0e5
- **Part:** every
- **Correction:** none
- **Recovered:** none

## foundation-change-path/1

No change that, against {fork-point}, alters a foundation entry runs on the path for tasks that leave the foundation unchanged.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-13@cc5e612f
- **Part:** every
- **Correction:** none
- **Recovered:** none

## decision-approval-record/1

Every decision version in the decision log records in *Approved by* who approved it and on what date.

- **Method:** `python -B elements/decisions/format_guard.py foundations/decisions.md --record .runs/decisions.jsonl`
- **Rests on:** none
- **Derives from:** WAY-14@eb86d14b
- **Part:** decisions
- **Correction:** none
- **Recovered:** none

## decision-approver/1

Every decision version in the decision log names in *Approved by* Mariusz, or the approver its *Approver override* names.

- **Method:** `python -B elements/decisions/format_guard.py foundations/decisions.md --record .runs/decisions.jsonl`
- **Rests on:** none
- **Derives from:** WAY-14@eb86d14b
- **Part:** decisions
- **Correction:** none
- **Recovered:** none

## derived-file-content/1

Every derived file git tracks that its generator can produce from scratch is identical to what the generator produces on the same commit, except for the values that file declares as varying between runs.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-15@72eb2240 · WAY-52@93101108 · WAY-53@aaeafada
- **Part:** every
- **Correction:** none
- **Recovered:** none

## derived-subset-naming/1

Every derived file compared as a subset of its version on {fork-point} is named in the template of its element.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-53@aaeafada
- **Part:** decisions · part-map · invariants · glossary · environment-facts
- **Correction:** none
- **Recovered:** none

## ci-checking-commands/1

No CI configuration git tracks runs a checking command other than the gate's command.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-16@dd3e3cc1
- **Part:** every
- **Correction:** none
- **Recovered:** none

## gate-check-source/1

Every check the gate runs comes from a method of checking written in an entry.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-16@dd3e3cc1
- **Part:** gate · invariants
- **Correction:** none
- **Recovered:** none

## view-versions/1

The view of the decisions in force holds only the latest version of every number in the decision log, and a single line in place of a repealed number.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-18@b32c0eea
- **Part:** every
- **Correction:** none
- **Recovered:** none

## view-links/1

The view of the decisions in force shows every link the decision log writes at both of its ends.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-18@b32c0eea
- **Part:** every
- **Correction:** none
- **Recovered:** none

## decision-heading-form/1

The heading of every decision version in the decision log has the form `### <prefix>-NN/V — <question>`.

- **Method:** `python -B elements/decisions/format_guard.py foundations/decisions.md --record .runs/decisions.jsonl`
- **Rests on:** none
- **Derives from:** WAY-19@4dc13deb
- **Part:** decisions
- **Correction:** none
- **Recovered:** none

## decision-version-sequence/1

The versions of each number in the decision log are consecutive.

- **Method:** `python -B elements/decisions/format_guard.py foundations/decisions.md --record .runs/decisions.jsonl`
- **Rests on:** none
- **Derives from:** WAY-19@4dc13deb
- **Part:** decisions
- **Correction:** none
- **Recovered:** none

## decision-change-rationale/1

Every decision version after the first gives a rationale for the change, or holds `TODO` in *Rationale for change*.

- **Method:** `python -B elements/decisions/format_guard.py foundations/decisions.md --record .runs/decisions.jsonl`
- **Rests on:** none
- **Derives from:** WAY-19@4dc13deb · WAY-71@cab47c5b
- **Part:** decisions
- **Correction:** none
- **Recovered:** none

## decision-change-kind/1

Every decision version after the first names its kind of change from the list in the decision template, or holds `TODO` in *Change*.

- **Method:** `python -B elements/decisions/format_guard.py foundations/decisions.md --record .runs/decisions.jsonl`
- **Rests on:** none
- **Derives from:** WAY-20@6aa77560 · WAY-71@cab47c5b
- **Part:** decisions
- **Correction:** none
- **Recovered:** none

## decision-binding-across-versions/1

Every rationale change, field change and challenge in the decision log keeps the binding sentences of the version before it word for word.

- **Method:** `python -B elements/decisions/format_guard.py foundations/decisions.md --record .runs/decisions.jsonl`
- **Rests on:** none
- **Derives from:** WAY-20@6aa77560
- **Part:** decisions
- **Correction:** none
- **Recovered:** none

## repeal-binding-sentences/1

No repeal in the decision log has binding sentences.

- **Method:** `python -B elements/decisions/format_guard.py foundations/decisions.md --record .runs/decisions.jsonl`
- **Rests on:** none
- **Derives from:** WAY-20@6aa77560
- **Part:** decisions
- **Correction:** none
- **Recovered:** none

## decision-scope-names/1

Every name in the scope of the latest version of a decision in the decision log is the identifier of a part in the part map.

- **Method:** `python -B elements/part-map/format_guard.py foundations/part_map.md --record .runs/part-map.jsonl`
- **Rests on:** none
- **Derives from:** WAY-21@586e4a38 · WAY-41@40134aeb
- **Part:** every
- **Correction:** none
- **Recovered:** none

## decisions-found-for-change/1

The decisions found for a change against {fork-point} include every decision whose scope names a part the change touches.

- **Method:** `TODO`
- **Rests on:** git-path-patterns@1519f3f7
- **Derives from:** WAY-21@586e4a38
- **Part:** every
- **Correction:** none
- **Recovered:** none

## review-when-form/1

Every *Review when* in the decision log other than `none` or `TODO` names both a state and a date.

- **Method:** `python -B elements/decisions/format_guard.py foundations/decisions.md --record .runs/decisions.jsonl`
- **Rests on:** none
- **Derives from:** WAY-24@058a356a · WAY-71@cab47c5b
- **Part:** decisions
- **Correction:** none
- **Recovered:** none

## decision-guard-overdue-review/1

The decision guard, given a date, warns of every check-by date earlier than it that no later review entry answers.

- **Method:** `python -B gate/run_tests.py elements/decisions --record .runs/decisions-tests.jsonl`
- **Rests on:** none
- **Derives from:** WAY-24@058a356a
- **Part:** decisions
- **Correction:** none
- **Recovered:** none

## review-next-check/1

Every review entry in the decision log whose result is that the state has not come names a date, or holds `TODO`, in *Next check*.

- **Method:** `python -B elements/decisions/format_guard.py foundations/decisions.md --record .runs/decisions.jsonl`
- **Rests on:** none
- **Derives from:** WAY-24@058a356a · WAY-71@cab47c5b
- **Part:** decisions
- **Correction:** none
- **Recovered:** none

## review-named-version/1

Every version of a decision that a review entry names exists in the decision log.

- **Method:** `python -B elements/decisions/format_guard.py foundations/decisions.md --record .runs/decisions.jsonl`
- **Rests on:** none
- **Derives from:** WAY-24@058a356a
- **Part:** decisions
- **Correction:** none
- **Recovered:** none

## outranks-pairs/1

No two decisions in the decision log outrank each other.

- **Method:** `python -B elements/decisions/format_guard.py foundations/decisions.md --record .runs/decisions.jsonl`
- **Rests on:** none
- **Derives from:** WAY-25@eb0ce2c4
- **Part:** decisions
- **Correction:** none
- **Recovered:** none

## outbound-link-reach/1

No file git tracks contains a link into a private note collection, or into a repository that a reader not signed in to its host cannot open.

- **Method:** `TODO`
- **Rests on:** dequelabs-axe-core-visibility@d0762f1e · github-spec-kit-visibility@483cec57 · doorstop-dev-doorstop-visibility@fff695c4 · obi1kenobi-cargo-semver-checks-visibility@347970d8 · shopify-packwerk-visibility@1860c0d7 · backstage-backstage-visibility@1f71d395 · kubernetes-enhancements-visibility@28969041 · owasp-pytm-visibility@28909543 · oasdiff-oasdiff-visibility@ea766246 · chromium-src-visibility@9af96eac
- **Derives from:** WAY-27@c4976d74
- **Part:** every
- **Correction:** none
- **Recovered:** none

## inherited-origin-form/1

Every inherited decision in the decision log has *Origin* in the form `inherited — searched: <…>; found: <…>`.

- **Method:** `python -B elements/decisions/format_guard.py foundations/decisions.md --record .runs/decisions.jsonl`
- **Rests on:** none
- **Derives from:** WAY-29@306edf37
- **Part:** decisions
- **Correction:** none
- **Recovered:** none

## inherited-rationale-source/1

The *Rationale* of every inherited decision in the decision log is `unknown`, a quotation with its source, or attributed to the human who gave it.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-29@306edf37
- **Part:** decisions
- **Correction:** none
- **Recovered:** none

## relation-fingerprint-presence/1

A relation in the decision log carries a fingerprint when, and only when, its type is `derives from` or `narrows`.

- **Method:** `python -B elements/decisions/format_guard.py foundations/decisions.md --record .runs/decisions.jsonl`
- **Rests on:** none
- **Derives from:** WAY-31@509d69d9
- **Part:** decisions
- **Correction:** none
- **Recovered:** none

## relation-fingerprint-value/1

Where {merge-onto} exists, every fingerprint a relation carries in the latest version of a decision, in the decision log a merge onto {merge-onto} leaves, equals the current fingerprint there of the decision it names.

- **Method:** `python -B elements/decisions/format_guard.py foundations/decisions.md --merge-onto {merge-onto} --record .runs/decisions-merge-onto.jsonl`
- **Rests on:** none
- **Derives from:** WAY-02@af08ee5d · WAY-31@509d69d9
- **Part:** decisions · relation-model
- **Correction:** none
- **Recovered:** none

## relation-type/1

Every relation in the decision log has one of the three types the decision template lists.

- **Method:** `python -B elements/decisions/format_guard.py foundations/decisions.md --record .runs/decisions.jsonl`
- **Rests on:** none
- **Derives from:** WAY-32@b3ee3f37
- **Part:** decisions
- **Correction:** none
- **Recovered:** none

## foundation-search-record/1

Where {merge-onto} exists, no change alters, against {fork-point}, a foundation entry without the record of the search made when the entry was written and of the search against {merge-onto}.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-33@3eb4881b
- **Part:** every
- **Correction:** none
- **Recovered:** none

## skill-rule-source/1

Every element's skill names its element's template as the source of the rules.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-35@81666508
- **Part:** decisions · part-map · invariants · glossary · environment-facts
- **Correction:** none
- **Recovered:** none

## script-language/1

Every script git tracks is a Python file.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-38@6e10c3fd
- **Part:** every
- **Correction:** none
- **Recovered:** none

## script-imports/1

No script git tracks imports a module other than one of the standard library of Python 3.14 or a Python file git tracks.

- **Method:** `TODO`
- **Rests on:** python-stdlib-modules@258d2586
- **Derives from:** WAY-38@6e10c3fd · WAY-89@fbb25ae3
- **Part:** every
- **Correction:** none
- **Recovered:** none

## script-subprocesses/1

No script git tracks starts a program other than git or a command the product declares in its repository.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-38@6e10c3fd
- **Part:** every
- **Correction:** none
- **Recovered:** none

## map-guard-missing-command/1

The map guard reports a check whose declared command the product lacks as unchecked, never as agreement.

- **Method:** `python -B gate/run_tests.py elements/part-map --record .runs/part-map-tests.jsonl`
- **Rests on:** none
- **Derives from:** WAY-38@6e10c3fd
- **Part:** part-map
- **Correction:** none
- **Recovered:** none

## fingerprint-definition/1

The relation model's script gives a text the first eight characters, in lower-case hexadecimal, of the SHA-256 digest of that text encoded in UTF-8, after every run of spaces and line breaks is replaced by a single space and both ends are trimmed.

- **Method:** `python -B gate/run_tests.py relation-model --record .runs/relation-model-tests.jsonl`
- **Rests on:** sha-256@e3a30c6f · utf-8@6afd686d
- **Derives from:** WAY-39@a3b77692
- **Part:** relation-model
- **Correction:** none
- **Recovered:** none

## map-entry-kinds/1

Every entry of the part map is a part, a critical flow or a surface.

- **Method:** `python -B elements/part-map/format_guard.py foundations/part_map.md --record .runs/part-map.jsonl`
- **Rests on:** none
- **Derives from:** WAY-40@aeabb301
- **Part:** part-map
- **Correction:** none
- **Recovered:** none

## map-section-kinds/1

The part map holds no section other than its entries and the lists its template names.

- **Method:** `python -B elements/part-map/format_guard.py foundations/part_map.md --record .runs/part-map.jsonl`
- **Rests on:** none
- **Derives from:** WAY-40@aeabb301
- **Part:** part-map
- **Correction:** none
- **Recovered:** none

## part-map-file/1

The repository holds exactly one part map, `foundations/part_map.md`.

- **Method:** `python -B elements/part-map/format_guard.py foundations/part_map.md --record .runs/part-map.jsonl`
- **Rests on:** none
- **Derives from:** WAY-40@aeabb301
- **Part:** every
- **Correction:** none
- **Recovered:** none

## map-identifier-form/1

Every identifier of an entry in the part map is made of words.

- **Method:** `python -B elements/part-map/format_guard.py foundations/part_map.md --record .runs/part-map.jsonl`
- **Rests on:** none
- **Derives from:** WAY-41@40134aeb
- **Part:** part-map
- **Correction:** none
- **Recovered:** none

## identifier-holders/1

No identifier is held by two entries or withdrawal lines of the part map, `foundations/invariants.md` and `foundations/environment_facts.md` taken together.

- **Method:** `python -B elements/invariants/format_guard.py foundations/invariants.md --record .runs/invariants.jsonl`
- **Rests on:** none
- **Derives from:** WAY-41@40134aeb · WAY-64@4b25a234 · WAY-75@753ce78b
- **Part:** part-map · invariants · environment-facts
- **Correction:** none
- **Recovered:** none

## map-reference-target/1

Every part map identifier referred to from the foundation, a test or a generated rule file stands in the part map as an entry or as a withdrawal line.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-41@40134aeb
- **Part:** every
- **Correction:** none
- **Recovered:** none

## map-fingerprint-input/1

The fingerprint a script of the-way gives an entry of the part map is the fingerprint of the entry's binding sentence alone.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-42@9b00b854
- **Part:** part-map · relation-model
- **Correction:** none
- **Recovered:** none

## map-entry-version/1

No entry of the part map carries a version.

- **Method:** `python -B elements/part-map/format_guard.py foundations/part_map.md --record .runs/part-map.jsonl`
- **Rests on:** none
- **Derives from:** WAY-43@2914f0cf
- **Part:** part-map
- **Correction:** none
- **Recovered:** none

## file-part-assignment/1

Every file git tracks matches the path patterns of exactly one part of the part map, or stands on the map's list of files left out on purpose.

- **Method:** `python -B elements/part-map/format_guard.py foundations/part_map.md --record .runs/part-map.jsonl`
- **Rests on:** git-path-patterns@1519f3f7
- **Derives from:** WAY-44@220f5b85
- **Part:** every
- **Correction:** none
- **Recovered:** none

## path-pattern-reach/1

Every path pattern in the part map matches at least one file git tracks.

- **Method:** `python -B elements/part-map/format_guard.py foundations/part_map.md --record .runs/part-map.jsonl`
- **Rests on:** git-path-patterns@1519f3f7
- **Derives from:** WAY-44@220f5b85
- **Part:** every
- **Correction:** none
- **Recovered:** none

## left-out-file-assignment/1

No file on the part map's list of files left out on purpose matches the path patterns of a part.

- **Method:** `python -B elements/part-map/format_guard.py foundations/part_map.md --record .runs/part-map.jsonl`
- **Rests on:** git-path-patterns@1519f3f7
- **Derives from:** WAY-44@220f5b85
- **Part:** part-map
- **Correction:** none
- **Recovered:** none

## flow-part-names/1

Every part a critical flow of the part map lists is a part of the map.

- **Method:** `python -B elements/part-map/format_guard.py foundations/part_map.md --record .runs/part-map.jsonl`
- **Rests on:** none
- **Derives from:** WAY-45@3991b544
- **Part:** part-map
- **Correction:** none
- **Recovered:** none

## flow-invariant-link/1

Every critical flow in the part map names an invariant and a test that names the flow.

- **Method:** `python -B elements/part-map/format_guard.py foundations/part_map.md --record .runs/part-map.jsonl`
- **Rests on:** none
- **Derives from:** WAY-45@3991b544
- **Part:** part-map · gate
- **Correction:** none
- **Recovered:** none

## map-invariant-names/1

Every invariant identifier the part map names is an entry of `foundations/invariants.md`.

- **Method:** `python -B elements/part-map/format_guard.py foundations/part_map.md --record .runs/part-map.jsonl`
- **Rests on:** none
- **Derives from:** WAY-64@4b25a234
- **Part:** every
- **Correction:** none
- **Recovered:** none

## failure-mode-severity/1

Every failure mode recorded in the part map names its severity.

- **Method:** `python -B elements/part-map/format_guard.py foundations/part_map.md --record .runs/part-map.jsonl`
- **Rests on:** none
- **Derives from:** WAY-46@b0cef8dd
- **Part:** part-map
- **Correction:** none
- **Recovered:** none

## failure-mode-detection/1

Every failure mode recorded in the part map names an invariant that detects it before release, or reads "not detected".

- **Method:** `python -B elements/part-map/format_guard.py foundations/part_map.md --record .runs/part-map.jsonl`
- **Rests on:** none
- **Derives from:** WAY-46@b0cef8dd
- **Part:** part-map
- **Correction:** none
- **Recovered:** none

## part-criticality-field/1

No part of the part map carries a criticality written by hand.

- **Method:** `python -B elements/part-map/format_guard.py foundations/part_map.md --record .runs/part-map.jsonl`
- **Rests on:** none
- **Derives from:** WAY-46@b0cef8dd
- **Part:** part-map
- **Correction:** none
- **Recovered:** none

## map-guard-unrecorded-criticality/1

The map guard computes the highest criticality of the map's scale for a part with no failure modes recorded.

- **Method:** `python -B gate/run_tests.py elements/part-map --record .runs/part-map-tests.jsonl`
- **Rests on:** none
- **Derives from:** WAY-46@b0cef8dd
- **Part:** part-map
- **Correction:** none
- **Recovered:** none

## map-guard-dependency-report/1

The map guard reports every dependency running from a part of higher criticality to one of lower criticality with no separation recorded.

- **Method:** `python -B gate/run_tests.py elements/part-map --record .runs/part-map-tests.jsonl`
- **Rests on:** none
- **Derives from:** WAY-46@b0cef8dd
- **Part:** part-map
- **Correction:** none
- **Recovered:** none

## flow-coverage-parts/1

For every critical flow whose test leaves a coverage file, every part that coverage names stands in the flow's list of parts.

- **Method:** `python -B elements/part-map/format_guard.py foundations/part_map.md --record .runs/part-map.jsonl`
- **Rests on:** git-path-patterns@1519f3f7
- **Derives from:** WAY-47@f4daadb2
- **Part:** every
- **Correction:** none
- **Recovered:** none

## map-guard-missing-coverage/1

The map guard reports a critical flow whose test leaves no coverage file as "list of parts unchecked", never as agreeing with the map.

- **Method:** `python -B gate/run_tests.py elements/part-map --record .runs/part-map-tests.jsonl`
- **Rests on:** none
- **Derives from:** WAY-47@f4daadb2
- **Part:** part-map
- **Correction:** none
- **Recovered:** none

## map-guard-test-runs/1

The map guard starts no test run of its own.

- **Method:** `python -B gate/run_tests.py elements/part-map --record .runs/part-map-tests.jsonl`
- **Rests on:** none
- **Derives from:** WAY-47@f4daadb2
- **Part:** part-map
- **Correction:** none
- **Recovered:** none

## trust-boundary-pattern/1

Every trust boundary in the part map names a pattern of files that matches at least one file git tracks.

- **Method:** `python -B elements/part-map/format_guard.py foundations/part_map.md --record .runs/part-map.jsonl`
- **Rests on:** git-path-patterns@1519f3f7
- **Derives from:** WAY-48@7f42c295
- **Part:** every
- **Correction:** none
- **Recovered:** none

## external-exchange-row/1

Every exchange with the external context in the part map records its direction, whether what comes in is trusted, and whether its consumer updates together with the product.

- **Method:** `python -B elements/part-map/format_guard.py foundations/part_map.md --record .runs/part-map.jsonl`
- **Rests on:** none
- **Derives from:** WAY-48@7f42c295 · WAY-50@56465170
- **Part:** part-map
- **Correction:** none
- **Recovered:** none

## gate-boundary-change/1

The gate runs the check for crafted input on every change that, against "{fork-point}", touches the files of a trust boundary.

- **Method:** `TODO`
- **Rests on:** git-path-patterns@1519f3f7
- **Derives from:** WAY-48@7f42c295
- **Part:** gate
- **Correction:** none
- **Recovered:** none

## surface-promise-level/1

Every symbol or schema element declared a surface carries a level of promise.

- **Method:** `python -B elements/part-map/format_guard.py foundations/part_map.md --record .runs/part-map.jsonl`
- **Rests on:** none
- **Derives from:** WAY-49@631b41c6
- **Part:** every
- **Correction:** none
- **Recovered:** none

## surface-declaration/1

Every surface in the part map names a declaration that exists, or says that it cannot be marked at the element and names the test that checks it.

- **Method:** `python -B elements/part-map/format_guard.py foundations/part_map.md --record .runs/part-map.jsonl`
- **Rests on:** none
- **Derives from:** WAY-49@631b41c6
- **Part:** every
- **Correction:** none
- **Recovered:** none

## map-withdrawal-date/1

No withdrawal date is written in the part map.

- **Method:** `python -B elements/part-map/format_guard.py foundations/part_map.md --record .runs/part-map.jsonl`
- **Rests on:** none
- **Derives from:** WAY-49@631b41c6
- **Part:** part-map
- **Correction:** none
- **Recovered:** none

## promise-level-policy/1

Every level of promise a declaration uses has a policy in the part map.

- **Method:** `python -B elements/part-map/format_guard.py foundations/part_map.md --record .runs/part-map.jsonl`
- **Rests on:** none
- **Derives from:** WAY-50@56465170
- **Part:** every
- **Correction:** none
- **Recovered:** none

## surface-change-path/1

No surface in the part map carries a change path of its own.

- **Method:** `python -B elements/part-map/format_guard.py foundations/part_map.md --record .runs/part-map.jsonl`
- **Rests on:** none
- **Derives from:** WAY-50@56465170
- **Part:** part-map
- **Correction:** none
- **Recovered:** none

## known-violation-coverage/1

Every violation of a part map rule that the code holds stands on the list of known violations.

- **Method:** `python -B elements/part-map/format_guard.py foundations/part_map.md --record .runs/part-map.jsonl`
- **Rests on:** none
- **Derives from:** WAY-51@83d3d193
- **Part:** every
- **Correction:** none
- **Recovered:** none

## known-violations-growth/1

The list of known violations is a subset of its version on {fork-point}.

- **Method:** `python -B elements/part-map/format_guard.py foundations/part_map.md --base {fork-point} --record .runs/part-map-base.jsonl`
- **Rests on:** none
- **Derives from:** WAY-51@83d3d193
- **Part:** part-map
- **Correction:** none
- **Recovered:** none

## known-violation-currency/1

Every position on the list of known violations names a violation the code holds.

- **Method:** `python -B elements/part-map/format_guard.py foundations/part_map.md --record .runs/part-map.jsonl`
- **Rests on:** none
- **Derives from:** WAY-51@83d3d193
- **Part:** every
- **Correction:** none
- **Recovered:** none

## known-violation-fields/1

Every position on the list of known violations names a source part, a target part, a file and what it reaches for.

- **Method:** `python -B elements/part-map/format_guard.py foundations/part_map.md --record .runs/part-map.jsonl`
- **Rests on:** none
- **Derives from:** WAY-51@83d3d193
- **Part:** part-map
- **Correction:** none
- **Recovered:** none

## known-violation-line-number/1

No position on the list of known violations names a line number.

- **Method:** `python -B elements/part-map/format_guard.py foundations/part_map.md --record .runs/part-map.jsonl`
- **Rests on:** none
- **Derives from:** WAY-51@83d3d193
- **Part:** part-map
- **Correction:** none
- **Recovered:** none

## generated-pattern-source/1

Every path pattern in a generated rule file comes from a part's rule for assigning files.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-52@93101108
- **Part:** part-map
- **Correction:** none
- **Recovered:** none

## generated-overview/1

No file generated for an agent holds an overview of the repository's directories.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-52@93101108
- **Part:** part-map
- **Correction:** none
- **Recovered:** none

## flow-test-location/1

Every critical flow in the part map names a test whose path lies under `gate/`.

- **Method:** `python -B elements/part-map/format_guard.py foundations/part_map.md --record .runs/part-map.jsonl`
- **Rests on:** none
- **Derives from:** WAY-55@97b25b1c
- **Part:** part-map · gate
- **Correction:** none
- **Recovered:** none

## invariant-sentence-count/1

Every entry of `foundations/invariants.md` states its invariant in one sentence.

- **Method:** `python -B elements/invariants/format_guard.py foundations/invariants.md --record .runs/invariants.jsonl`
- **Rests on:** none
- **Derives from:** WAY-56@3213162c
- **Part:** invariants
- **Correction:** none
- **Recovered:** none

## invariant-identifier-form/1

The identifier in the heading of every entry of `foundations/invariants.md` has the form the invariants template gives.

- **Method:** `python -B elements/invariants/format_guard.py foundations/invariants.md --record .runs/invariants.jsonl`
- **Rests on:** none
- **Derives from:** WAY-64@4b25a234
- **Part:** invariants
- **Correction:** none
- **Recovered:** none

## invariant-version-number/1

The heading of every entry of `foundations/invariants.md` carries a version number.

- **Method:** `python -B elements/invariants/format_guard.py foundations/invariants.md --record .runs/invariants.jsonl`
- **Rests on:** none
- **Derives from:** WAY-57@29edb491
- **Part:** invariants
- **Correction:** none
- **Recovered:** none

## invariant-version-new/1

Every entry of `foundations/invariants.md` with no fingerprint on {fork-point} carries version 1 and declares no correction.

- **Method:** `python -B elements/invariants/format_guard.py foundations/invariants.md --base {fork-point} --record .runs/invariants-base.jsonl`
- **Rests on:** none
- **Derives from:** WAY-57@29edb491
- **Part:** invariants
- **Correction:** none
- **Recovered:** none

## invariant-version-changed/1

Every entry of `foundations/invariants.md` whose fingerprint differs from its fingerprint on {fork-point} carries either a version one higher than there and no correction, or the version it has there and a correction naming both fingerprints.

- **Method:** `python -B elements/invariants/format_guard.py foundations/invariants.md --base {fork-point} --record .runs/invariants-base.jsonl`
- **Rests on:** none
- **Derives from:** WAY-57@29edb491
- **Part:** invariants
- **Correction:** none
- **Recovered:** none

## invariant-version-unchanged/1

Every entry of `foundations/invariants.md` whose fingerprint equals its fingerprint on {fork-point} carries the version it has there, and declares no correction whose second fingerprint differs from it.

- **Method:** `python -B elements/invariants/format_guard.py foundations/invariants.md --base {fork-point} --record .runs/invariants-base.jsonl`
- **Rests on:** none
- **Derives from:** WAY-57@29edb491
- **Part:** invariants
- **Correction:** none
- **Recovered:** none

## invariant-earlier-wording/1

No entry of `foundations/invariants.md` holds, beside its current sentence, a sentence it held on {fork-point}.

- **Method:** `python -B elements/invariants/format_guard.py foundations/invariants.md --base {fork-point} --record .runs/invariants-base.jsonl`
- **Rests on:** none
- **Derives from:** WAY-57@29edb491
- **Part:** invariants
- **Correction:** none
- **Recovered:** none

## invariant-citation-version/1

Every `invariant:` line in a check that names an entry of `foundations/invariants.md` cites its current version.

- **Method:** `python -B elements/invariants/format_guard.py foundations/invariants.md --record .runs/invariants.jsonl`
- **Rests on:** none
- **Derives from:** WAY-57@29edb491 · WAY-65@58d1f2c3
- **Part:** every
- **Correction:** none
- **Recovered:** none

## invariant-correction-confirmation/1

Every correction an entry of `foundations/invariants.md` declares is confirmed by the human deciding the change, with both wordings in front of them.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-57@29edb491
- **Part:** invariants
- **Correction:** none
- **Recovered:** none

## invariant-recovered-form/1

Every entry of `foundations/invariants.md` holds in *Recovered* either `none` or a value of the form `recovered — searched: <…>; found: <…>`.

- **Method:** `python -B elements/invariants/format_guard.py foundations/invariants.md --record .runs/invariants.jsonl`
- **Rests on:** none
- **Derives from:** WAY-58@793400ae
- **Part:** invariants
- **Correction:** none
- **Recovered:** none

## invariant-recovered-derived/1

Every entry of `foundations/invariants.md` that names a decision it derives from holds `none` in *Recovered*.

- **Method:** `python -B elements/invariants/format_guard.py foundations/invariants.md --record .runs/invariants.jsonl`
- **Rests on:** none
- **Derives from:** WAY-58@793400ae
- **Part:** invariants
- **Correction:** none
- **Recovered:** none

## gate-fork-point-evidence/1

For every entry whose sentence a change adds or alters against "{fork-point}", the gate's report states whether the entry's method passes on "{fork-point}" and fails there on a deliberate break, or that this could not be checked.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-58@793400ae
- **Part:** gate
- **Correction:** none
- **Recovered:** none

## invariant-fingerprint-input/1

The fingerprint the invariants guard gives an invariant entry is the fingerprint of its sentence alone.

- **Method:** `python -B gate/run_tests.py elements/invariants --record .runs/invariants-tests.jsonl`
- **Rests on:** none
- **Derives from:** WAY-59@6ceadf4e
- **Part:** invariants · relation-model
- **Correction:** none
- **Recovered:** none

## sentence-branch-names/1

No sentence in `foundations/invariants.md`, outside quoted text, contains the words "main branch" or "task branch".

- **Method:** `python -B elements/invariants/format_guard.py foundations/invariants.md --record .runs/invariants.jsonl`
- **Rests on:** none
- **Derives from:** WAY-60@c85d1ac0
- **Part:** invariants
- **Correction:** none
- **Recovered:** none

## sentence-gate-values/1

Every value from the gate's list that a sentence of `foundations/invariants.md` names outside quoted text is taken by its command, unless its method is not a command.

- **Method:** `python -B elements/invariants/format_guard.py foundations/invariants.md --record .runs/invariants.jsonl`
- **Rests on:** none
- **Derives from:** WAY-60@c85d1ac0
- **Part:** invariants
- **Correction:** none
- **Recovered:** none

## method-gate-values/1

Every value a command in `foundations/invariants.md` takes from the gate stands on the list in the invariants template.

- **Method:** `python -B elements/invariants/format_guard.py foundations/invariants.md --record .runs/invariants.jsonl`
- **Rests on:** none
- **Derives from:** WAY-61@c6bdfd7c
- **Part:** invariants
- **Correction:** none
- **Recovered:** none

## gate-verdict-per-entry/1

For every invariant whose command a run of the gate carried out, the gate's report shows the verdict that run recorded for the entry's identifier and current version.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-61@c6bdfd7c
- **Part:** gate
- **Correction:** none
- **Recovered:** none

## gate-pass-without-verdict/1

The gate reports no pass for an invariant that no run recorded a verdict for.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-61@c6bdfd7c
- **Part:** gate
- **Correction:** none
- **Recovered:** none

## invariant-part-names/1

Every part an entry of `foundations/invariants.md` names is a part of the part map.

- **Method:** `python -B elements/invariants/format_guard.py foundations/invariants.md --record .runs/invariants.jsonl`
- **Rests on:** none
- **Derives from:** WAY-62@d9c21624
- **Part:** invariants · part-map
- **Correction:** none
- **Recovered:** none

## invariant-part-form/1

Every entry of `foundations/invariants.md` names `every` or at least one part, never both.

- **Method:** `python -B elements/invariants/format_guard.py foundations/invariants.md --record .runs/invariants.jsonl`
- **Rests on:** none
- **Derives from:** WAY-62@d9c21624
- **Part:** invariants
- **Correction:** none
- **Recovered:** none

## change-reach/1

The invariants the gate finds a change against "{fork-point}" reaching include every entry naming `every` or a part the change touches, and every entry whose method names a file the change alters.

- **Method:** `TODO`
- **Rests on:** git-path-patterns@1519f3f7
- **Derives from:** WAY-62@d9c21624
- **Part:** gate
- **Correction:** none
- **Recovered:** none

## gate-result-values/1

Every result the gate reports for an invariant is `pass`, `fail`, `unchecked` or `error`.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-63@f16348c8
- **Part:** gate
- **Correction:** none
- **Recovered:** none

## gate-unchecked-reason/1

Every `unchecked` the gate reports names a reason on the list in the invariants template.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-63@f16348c8
- **Part:** gate · invariants
- **Correction:** none
- **Recovered:** none

## gate-reported-set/1

The gate reports a result for every invariant a change against "{fork-point}" reaches, and for every invariant a critical flow names.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-45@3991b544 · WAY-63@f16348c8
- **Part:** gate
- **Correction:** none
- **Recovered:** none

## flow-test-run/1

The gate runs, on every change, the test that every critical flow of the part map names.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-45@3991b544
- **Part:** gate · part-map
- **Correction:** none
- **Recovered:** none

## gate-exit-code/1

The gate's command exits non-zero when some result it reports is `error`, an invariant on the list of violated invariants results `pass`, an invariant off that list or an environment fact results `fail`, or a run records a failure for no entry, and zero otherwise.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-63@f16348c8 · WAY-67@7a06f2c0 · WAY-82@2ebe205b
- **Part:** gate
- **Correction:** none
- **Recovered:** none

## invariants-file/1

The repository holds exactly one file of invariant entries, `foundations/invariants.md`.

- **Method:** `python -B elements/invariants/format_guard.py foundations/invariants.md --record .runs/invariants.jsonl`
- **Rests on:** none
- **Derives from:** WAY-64@4b25a234
- **Part:** every
- **Correction:** none
- **Recovered:** none

## invariant-identifier-persistence/1

Every identifier `foundations/invariants.md` held on {fork-point} stands in it as an entry or as a withdrawal line.

- **Method:** `python -B elements/invariants/format_guard.py foundations/invariants.md --base {fork-point} --record .runs/invariants-base.jsonl`
- **Rests on:** none
- **Derives from:** WAY-64@4b25a234
- **Part:** invariants
- **Correction:** none
- **Recovered:** none

## invariant-withdrawal-persistence/1

Every identifier that stood as a withdrawal line of `foundations/invariants.md` on {fork-point} is still a withdrawal line of that file.

- **Method:** `python -B elements/invariants/format_guard.py foundations/invariants.md --base {fork-point} --record .runs/invariants-base.jsonl`
- **Rests on:** none
- **Derives from:** WAY-64@4b25a234
- **Part:** invariants
- **Correction:** none
- **Recovered:** none

## withdrawal-successors/1

Every successor a withdrawal line of `foundations/invariants.md` names is an entry or a withdrawal line of that file, or `none`.

- **Method:** `python -B elements/invariants/format_guard.py foundations/invariants.md --record .runs/invariants.jsonl`
- **Rests on:** none
- **Derives from:** WAY-64@4b25a234
- **Part:** invariants
- **Correction:** none
- **Recovered:** none

## invariant-citation-target/1

Every `invariant:` line in a check names an entry of `foundations/invariants.md`.

- **Method:** `python -B elements/invariants/format_guard.py foundations/invariants.md --record .runs/invariants.jsonl`
- **Rests on:** none
- **Derives from:** WAY-12@55e89140 · WAY-17@ab01c0e5 · WAY-65@58d1f2c3
- **Part:** every
- **Correction:** none
- **Recovered:** none

## data-line-target/1

Every `data:` line in an invariant test names a file that exists.

- **Method:** `python -B elements/invariants/format_guard.py foundations/invariants.md --record .runs/invariants.jsonl`
- **Rests on:** none
- **Derives from:** WAY-65@58d1f2c3
- **Part:** every
- **Correction:** none
- **Recovered:** none

## invariant-tests-of-change/1

The invariant tests of a change include the file of every check that cites an invariant on "{fork-point}" or on the commit being checked, and every file such a check names on a `data:` line.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-65@58d1f2c3
- **Part:** gate
- **Correction:** none
- **Recovered:** none

## link-fingerprint-presence/1

Every name in the *Derives from* or *Rests on* of an entry of `foundations/invariants.md`, other than `none` or `TODO`, carries a fingerprint.

- **Method:** `python -B elements/invariants/format_guard.py foundations/invariants.md --record .runs/invariants.jsonl`
- **Rests on:** none
- **Derives from:** WAY-66@d5ae207f
- **Part:** invariants
- **Correction:** none
- **Recovered:** none

## link-fingerprint-value/1

Where {merge-onto} exists, every fingerprint in the *Derives from* or *Rests on* of an entry of `foundations/invariants.md` equals the current fingerprint of the entry it names.

- **Method:** `python -B elements/invariants/format_guard.py foundations/invariants.md --merge-onto {merge-onto} --record .runs/invariants-merge-onto.jsonl`
- **Rests on:** none
- **Derives from:** WAY-66@d5ae207f
- **Part:** every
- **Correction:** none
- **Recovered:** none

## violated-list-growth/1

The list of violated invariants is a subset of its version on {fork-point}.

- **Method:** `python -B elements/invariants/format_guard.py foundations/invariants.md --base {fork-point} --record .runs/invariants-base.jsonl`
- **Rests on:** none
- **Derives from:** WAY-67@7a06f2c0
- **Part:** invariants
- **Correction:** none
- **Recovered:** none

## violated-position-version/1

Every position on the list of violated invariants names an entry of `foundations/invariants.md` at its current version and no other.

- **Method:** `python -B elements/invariants/format_guard.py foundations/invariants.md --record .runs/invariants.jsonl`
- **Rests on:** none
- **Derives from:** WAY-67@7a06f2c0
- **Part:** invariants
- **Correction:** none
- **Recovered:** none

## quarantine-position-form/1

Every quarantine position in `foundations/invariants.md` names an entry at its current version and an end date.

- **Method:** `python -B elements/invariants/format_guard.py foundations/invariants.md --record .runs/invariants.jsonl`
- **Rests on:** none
- **Derives from:** WAY-68@55b95268
- **Part:** invariants
- **Correction:** none
- **Recovered:** none

## quarantine-flow-invariants/1

No quarantine position in `foundations/invariants.md` names an invariant a critical flow names.

- **Method:** `python -B elements/invariants/format_guard.py foundations/invariants.md --record .runs/invariants.jsonl`
- **Rests on:** none
- **Derives from:** WAY-68@55b95268
- **Part:** invariants · part-map
- **Correction:** none
- **Recovered:** none

## gate-quarantine-result/1

The gate reports a quarantined entry `unchecked` while the checked commit's committer date is no later than its end date, and `error` after.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-68@55b95268
- **Part:** gate
- **Correction:** none
- **Recovered:** none

## log-entry-field-presence/1

Every entry of the decision log carries every field the decision template gives an entry of its kind.

- **Method:** `python -B elements/decisions/format_guard.py foundations/decisions.md --record .runs/decisions.jsonl`
- **Rests on:** none
- **Derives from:** WAY-71@cab47c5b
- **Part:** decisions
- **Correction:** none
- **Recovered:** none

## log-entry-field-words/1

No field of an entry of the decision log holds `none` or `TODO` where the decision template does not give it that word.

- **Method:** `python -B elements/decisions/format_guard.py foundations/decisions.md --record .runs/decisions.jsonl`
- **Rests on:** none
- **Derives from:** WAY-71@cab47c5b
- **Part:** decisions
- **Correction:** none
- **Recovered:** none

## log-entry-merge-todo/1

Where {merge-onto} exists, no field of an entry of the decision log holds `TODO`.

- **Method:** `python -B elements/decisions/format_guard.py foundations/decisions.md --merge-onto {merge-onto} --record .runs/decisions-merge-onto.jsonl`
- **Rests on:** none
- **Derives from:** WAY-71@cab47c5b
- **Part:** decisions
- **Correction:** none
- **Recovered:** none

## map-entry-field-presence/1

Every entry of the part map carries every field the part map template gives an entry of its kind.

- **Method:** `python -B elements/part-map/format_guard.py foundations/part_map.md --record .runs/part-map.jsonl`
- **Rests on:** none
- **Derives from:** WAY-71@cab47c5b
- **Part:** part-map
- **Correction:** none
- **Recovered:** none

## map-entry-field-words/1

No field of an entry of the part map holds `none` or `TODO` where the part map template does not give it that word.

- **Method:** `python -B elements/part-map/format_guard.py foundations/part_map.md --record .runs/part-map.jsonl`
- **Rests on:** none
- **Derives from:** WAY-71@cab47c5b
- **Part:** part-map
- **Correction:** none
- **Recovered:** none

## invariant-entry-field-presence/1

Every entry of `foundations/invariants.md` carries every field the invariants template gives an entry.

- **Method:** `python -B elements/invariants/format_guard.py foundations/invariants.md --record .runs/invariants.jsonl`
- **Rests on:** none
- **Derives from:** WAY-71@cab47c5b
- **Part:** invariants
- **Correction:** none
- **Recovered:** none

## invariant-entry-field-words/1

No field of an entry of `foundations/invariants.md` holds `none` or `TODO` where the invariants template does not give it that word.

- **Method:** `python -B elements/invariants/format_guard.py foundations/invariants.md --record .runs/invariants.jsonl`
- **Rests on:** none
- **Derives from:** WAY-71@cab47c5b
- **Part:** invariants
- **Correction:** none
- **Recovered:** none

## invariant-entry-merge-todo/2

Where {merge-onto} exists, no field of an entry of `foundations/invariants.md` other than *Method* and *Rests on* holds `TODO`, and *Rests on* holds it only while the environment facts that merge leaves hold no entry.

- **Method:** `python -B elements/invariants/format_guard.py foundations/invariants.md --merge-onto {merge-onto} --record .runs/invariants-merge-onto.jsonl`
- **Rests on:** none
- **Derives from:** WAY-71@cab47c5b
- **Part:** invariants · environment-facts
- **Correction:** none
- **Recovered:** none

## template-language/1

Every element's template states that its entries are written in English.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-72@ac27f7ee
- **Part:** decisions · part-map · invariants · glossary · environment-facts
- **Correction:** none
- **Recovered:** none

## run-record-form/1

Every line of the-way's own record of a run is one JSON object holding `check`, `verdict` as `pass` or `fail` or as `unchecked` beside a `reason`, and `invariant` or `fact` as `<identifier>/<version>` or `invariant` as `null`, and beside them at most `description`.

- **Method:** `TODO`
- **Rests on:** json-text@8141eb36 · json-lines@f16c5b84
- **Derives from:** WAY-74@6b4968d0
- **Part:** decisions · part-map · invariants · gate · environment-facts
- **Correction:** none
- **Recovered:** none

## run-record-path/1

Every path ending in `.jsonl` that a command in `foundations/invariants.md` names is one git ignores, and no such command names two.

- **Method:** `python -B elements/invariants/format_guard.py foundations/invariants.md --record .runs/invariants.jsonl`
- **Rests on:** gitignore-paths@3218da8f
- **Derives from:** WAY-74@6b4968d0
- **Part:** invariants · repository
- **Correction:** none
- **Recovered:** none

## run-record-lines/1

The gate reads, from the-way's own record of a run, only the lines the run it started for that command wrote.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-74@6b4968d0
- **Part:** gate
- **Correction:** none
- **Recovered:** none

## test-runner-pass-line/1

The test runner's record of a run holds a `pass` line for an invariant's identifier and version, and no `fail` line naming them, only when the body of every test method citing them in a `test_*.py` file under the directory the runner was given, as the run starts, executed in that run while its own test ran, and returned, with nothing raised out of that body, its set-up, its tear-down or any of its subtests.

- **Method:** `python -B gate/run_tests.py gate --record .runs/gate-tests.jsonl`
- **Rests on:** none
- **Derives from:** WAY-61@c6bdfd7c · WAY-65@58d1f2c3
- **Part:** gate
- **Correction:** none
- **Recovered:** none

## python-version-declared/1

The repository declares Python 3.14 in `.python-version`.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-89@fbb25ae3
- **Part:** repository
- **Correction:** none
- **Recovered:** none

## environment-facts-file/1

Every environment fact entry the repository holds stands in `foundations/environment_facts.md`.

- **Method:** `python -B elements/environment-facts/format_guard.py foundations/environment_facts.md --record .runs/environment-facts.jsonl`
- **Rests on:** none
- **Derives from:** WAY-75@753ce78b
- **Part:** every
- **Correction:** none
- **Recovered:** none

## fact-identifier-form/1

The identifier in the heading of every entry of `foundations/environment_facts.md` has the form the environment facts template gives.

- **Method:** `python -B elements/environment-facts/format_guard.py foundations/environment_facts.md --record .runs/environment-facts.jsonl`
- **Rests on:** none
- **Derives from:** WAY-75@753ce78b
- **Part:** environment-facts
- **Correction:** none
- **Recovered:** none

## fact-identifier-persistence/1

Every identifier `foundations/environment_facts.md` held on {fork-point} stands in it as an entry or as a withdrawn identifier.

- **Method:** `python -B elements/environment-facts/format_guard.py foundations/environment_facts.md --base {fork-point} --record .runs/environment-facts-base.jsonl`
- **Rests on:** none
- **Derives from:** WAY-75@753ce78b
- **Part:** environment-facts
- **Correction:** none
- **Recovered:** none

## fact-withdrawal-persistence/1

Every identifier that stood as a withdrawn identifier of `foundations/environment_facts.md` on {fork-point} is still a withdrawn identifier of that file.

- **Method:** `python -B elements/environment-facts/format_guard.py foundations/environment_facts.md --base {fork-point} --record .runs/environment-facts-base.jsonl`
- **Rests on:** none
- **Derives from:** WAY-75@753ce78b
- **Part:** environment-facts
- **Correction:** none
- **Recovered:** none

## fact-withdrawal-successors/1

Every withdrawn identifier of `foundations/environment_facts.md` gives why it was withdrawn and names as successors only entries or withdrawn identifiers of that file, or `none`.

- **Method:** `python -B elements/environment-facts/format_guard.py foundations/environment_facts.md --record .runs/environment-facts.jsonl`
- **Rests on:** none
- **Derives from:** WAY-75@753ce78b
- **Part:** environment-facts
- **Correction:** none
- **Recovered:** none

## fact-sentence-count/1

Every entry of `foundations/environment_facts.md` states its fact in one sentence.

- **Method:** `python -B elements/environment-facts/format_guard.py foundations/environment_facts.md --record .runs/environment-facts.jsonl`
- **Rests on:** none
- **Derives from:** WAY-76@c5e903ff
- **Part:** environment-facts
- **Correction:** none
- **Recovered:** none

## fact-scope-word/1

No *Holds for* of an entry of `foundations/environment_facts.md` reads "latest" or "newest".

- **Method:** `python -B elements/environment-facts/format_guard.py foundations/environment_facts.md --record .runs/environment-facts.jsonl`
- **Rests on:** none
- **Derives from:** WAY-77@325df854
- **Part:** environment-facts
- **Correction:** none
- **Recovered:** none

## fact-fingerprint-input/1

The fingerprint the environment facts guard gives an entry is the fingerprint of its sentence and its *Holds for* joined by a line break.

- **Method:** `python -B gate/run_tests.py elements/environment-facts --record .runs/environment-facts-tests.jsonl`
- **Rests on:** none
- **Derives from:** WAY-78@1380794c
- **Part:** environment-facts · relation-model
- **Correction:** none
- **Recovered:** none

## fact-version-new/1

Every entry of `foundations/environment_facts.md` with no fingerprint on {fork-point} carries version 1 and declares no correction.

- **Method:** `python -B elements/environment-facts/format_guard.py foundations/environment_facts.md --base {fork-point} --record .runs/environment-facts-base.jsonl`
- **Rests on:** none
- **Derives from:** WAY-79@b970f1e0
- **Part:** environment-facts
- **Correction:** none
- **Recovered:** none

## fact-version-changed/1

Every entry of `foundations/environment_facts.md` whose fingerprint differs from its fingerprint on {fork-point} carries either a version one higher than there and no correction, or the version it has there and a correction naming both fingerprints.

- **Method:** `python -B elements/environment-facts/format_guard.py foundations/environment_facts.md --base {fork-point} --record .runs/environment-facts-base.jsonl`
- **Rests on:** none
- **Derives from:** WAY-79@b970f1e0
- **Part:** environment-facts
- **Correction:** none
- **Recovered:** none

## fact-version-unchanged/1

Every entry of `foundations/environment_facts.md` whose fingerprint equals its fingerprint on {fork-point} carries the version it has there, and declares no correction whose second fingerprint differs from it.

- **Method:** `python -B elements/environment-facts/format_guard.py foundations/environment_facts.md --base {fork-point} --record .runs/environment-facts-base.jsonl`
- **Rests on:** none
- **Derives from:** WAY-79@b970f1e0
- **Part:** environment-facts
- **Correction:** none
- **Recovered:** none

## fact-citation-version/1

Every `fact:` line in a check that names an entry of `foundations/environment_facts.md` cites its current version.

- **Method:** `python -B elements/environment-facts/format_guard.py foundations/environment_facts.md --record .runs/environment-facts.jsonl`
- **Rests on:** none
- **Derives from:** WAY-79@b970f1e0
- **Part:** every
- **Correction:** none
- **Recovered:** none

## fact-source-form/1

Every *Source* of an entry of `foundations/environment_facts.md` has one of the forms the environment facts template gives.

- **Method:** `python -B elements/environment-facts/format_guard.py foundations/environment_facts.md --record .runs/environment-facts.jsonl`
- **Rests on:** none
- **Derives from:** WAY-80@a111c18e
- **Part:** environment-facts
- **Correction:** none
- **Recovered:** none

## fact-method-form/1

Every entry of `foundations/environment_facts.md` names as its method a command that begins with the name of the program it runs, the path alone of a file that exists, or `TODO`.

- **Method:** `python -B elements/environment-facts/format_guard.py foundations/environment_facts.md --record .runs/environment-facts.jsonl`
- **Rests on:** none
- **Derives from:** WAY-81@ba037b75
- **Part:** environment-facts
- **Correction:** none
- **Recovered:** none

## fact-citation-target/1

Every `fact:` line in a check names an entry of `foundations/environment_facts.md`, never a withdrawn identifier.

- **Method:** `python -B elements/environment-facts/format_guard.py foundations/environment_facts.md --record .runs/environment-facts.jsonl`
- **Rests on:** none
- **Derives from:** WAY-81@ba037b75
- **Part:** every
- **Correction:** none
- **Recovered:** none

## fact-verdict-citation/1

A run records a verdict for an environment fact only from a command that cites the fact on a `fact:` line.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-81@ba037b75
- **Part:** gate
- **Correction:** none
- **Recovered:** none

## based-on-fact-fingerprint/1

Every environment fact the *Based on* of the latest version of a decision names carries a fingerprint.

- **Method:** `python -B elements/environment-facts/format_guard.py foundations/environment_facts.md --record .runs/environment-facts.jsonl`
- **Rests on:** none
- **Derives from:** WAY-90@af633126
- **Part:** decisions · environment-facts
- **Correction:** none
- **Recovered:** none

## based-on-fact-fingerprint-value/1

Where {merge-onto} exists, every fingerprint the *Based on* of the latest version of a decision carries for an environment fact equals that fact's current fingerprint.

- **Method:** `python -B elements/environment-facts/format_guard.py foundations/environment_facts.md --merge-onto {merge-onto} --record .runs/environment-facts-merge-onto.jsonl`
- **Rests on:** none
- **Derives from:** WAY-90@af633126
- **Part:** decisions · environment-facts
- **Correction:** none
- **Recovered:** none

## gate-fact-run/1

The gate runs the method of every environment fact whose entry a change enters or rewords against "{fork-point}", or whose command names a file that change alters.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-82@2ebe205b
- **Part:** gate
- **Correction:** none
- **Recovered:** none

## fact-clock-exit/1

The command that runs the method of every environment fact exits non-zero when some fact's result is `fail` or `error`, and zero otherwise.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-82@2ebe205b
- **Part:** gate · environment-facts
- **Correction:** none
- **Recovered:** none

## human-verdict-invariant-row/1

Every row of `foundations/human_verdicts.md` naming an invariant names an entry of `foundations/invariants.md` whose method is a path, gives `pass` or `fail`, and reads `none` in *Until*.

- **Method:** `python -B elements/invariants/format_guard.py foundations/invariants.md --record .runs/invariants.jsonl`
- **Rests on:** none
- **Derives from:** WAY-83@c3c840c6
- **Part:** invariants
- **Correction:** none
- **Recovered:** none

## human-verdict-fact-row/1

Every row of `foundations/human_verdicts.md` naming an environment fact names an entry of `foundations/environment_facts.md` whose method is a path, gives `pass` or `fail`, names who gave it, when and the commit assessed, and carries a date in *Until*.

- **Method:** `python -B elements/environment-facts/format_guard.py foundations/environment_facts.md --record .runs/environment-facts.jsonl`
- **Rests on:** none
- **Derives from:** WAY-83@c3c840c6
- **Part:** environment-facts
- **Correction:** none
- **Recovered:** none

## gate-human-verdict/1

The gate counts a human verdict for an entry only from the row naming its current version, and for an environment fact only while the committer date of the commit being checked is no later than the row's *Until*.

- **Method:** `TODO`
- **Rests on:** none
- **Derives from:** WAY-83@c3c840c6
- **Part:** gate
- **Correction:** none
- **Recovered:** none

## fact-dependants/1

Where {merge-onto} exists, every entry of `foundations/environment_facts.md` is named by the *Rests on* of an invariant or by the *Based on* of the latest version of a decision.

- **Method:** `python -B elements/environment-facts/format_guard.py foundations/environment_facts.md --merge-onto {merge-onto} --record .runs/environment-facts-merge-onto.jsonl`
- **Rests on:** none
- **Derives from:** WAY-88@91970f10
- **Part:** environment-facts · invariants · decisions
- **Correction:** none
- **Recovered:** none

## fact-entry-field-presence/1

Every entry of `foundations/environment_facts.md` carries every field the environment facts template gives an entry.

- **Method:** `python -B elements/environment-facts/format_guard.py foundations/environment_facts.md --record .runs/environment-facts.jsonl`
- **Rests on:** none
- **Derives from:** WAY-71@cab47c5b
- **Part:** environment-facts
- **Correction:** none
- **Recovered:** none

## fact-entry-field-words/1

No field of an entry of `foundations/environment_facts.md` holds `none` or `TODO` where the environment facts template does not give it that word.

- **Method:** `python -B elements/environment-facts/format_guard.py foundations/environment_facts.md --record .runs/environment-facts.jsonl`
- **Rests on:** none
- **Derives from:** WAY-71@cab47c5b
- **Part:** environment-facts
- **Correction:** none
- **Recovered:** none

## fact-entry-merge-todo/1

Where {merge-onto} exists, no field of an entry of `foundations/environment_facts.md` other than *Method* holds `TODO`.

- **Method:** `python -B elements/environment-facts/format_guard.py foundations/environment_facts.md --merge-onto {merge-onto} --record .runs/environment-facts-merge-onto.jsonl`
- **Rests on:** none
- **Derives from:** WAY-71@cab47c5b
- **Part:** environment-facts
- **Correction:** none
- **Recovered:** none

## glossary-file/1

Every glossary entry the repository holds, other than a copy in `elements/glossary/examples.md`, stands in `foundations/glossary.md`.

- **Method:** `python -B elements/glossary/format_guard.py foundations/glossary.md --record .runs/glossary.jsonl`
- **Rests on:** none
- **Derives from:** WAY-93@4dc6ce12
- **Part:** every
- **Correction:** none
- **Recovered:** none

## glossary-file-sections/1

`foundations/glossary.md` holds a title, the paragraph under it and its entries, and no other heading.

- **Method:** `python -B elements/glossary/format_guard.py foundations/glossary.md --record .runs/glossary.jsonl`
- **Rests on:** none
- **Derives from:** WAY-93@4dc6ce12
- **Part:** glossary
- **Correction:** none
- **Recovered:** none

## glossary-term-holder/1

No term is held by two entries of `foundations/glossary.md`.

- **Method:** `python -B elements/glossary/format_guard.py foundations/glossary.md --record .runs/glossary.jsonl`
- **Rests on:** none
- **Derives from:** WAY-93@4dc6ce12
- **Part:** glossary
- **Correction:** none
- **Recovered:** none

## glossary-term-collision/1

The glossary guard warns on every change that, against "{fork-point}", adds or renames a term of `foundations/glossary.md` or an identifier of the part map, the invariants or the environment facts so that the two read alike, its hyphens read as spaces, unless the identifier is of a part whose files include `elements/<identifier>/` and the term, in any of its forms, names that element.

- **Method:** `python -B gate/run_tests.py elements/glossary --record .runs/glossary-tests.jsonl`
- **Rests on:** none
- **Derives from:** WAY-93@4dc6ce12
- **Part:** glossary
- **Correction:** none
- **Recovered:** none

## glossary-entry-field-presence/1

Every entry of `foundations/glossary.md` carries every field the glossary template gives an entry.

- **Method:** `python -B elements/glossary/format_guard.py foundations/glossary.md --record .runs/glossary.jsonl`
- **Rests on:** none
- **Derives from:** WAY-94@0ac1fa64 · WAY-71@cab47c5b
- **Part:** glossary
- **Correction:** none
- **Recovered:** none

## glossary-entry-field-words/1

No field of an entry of `foundations/glossary.md` holds `none` or `TODO` where the glossary template does not give it that word.

- **Method:** `python -B elements/glossary/format_guard.py foundations/glossary.md --record .runs/glossary.jsonl`
- **Rests on:** none
- **Derives from:** WAY-94@0ac1fa64 · WAY-71@cab47c5b
- **Part:** glossary
- **Correction:** none
- **Recovered:** none

## glossary-term-use/1

Where {merge-onto} exists, every term of `foundations/glossary.md` has a use outside the glossary in a file of `foundations/` or in an element's template.

- **Method:** `python -B elements/glossary/format_guard.py foundations/glossary.md --merge-onto {merge-onto} --record .runs/glossary-merge-onto.jsonl`
- **Rests on:** none
- **Derives from:** WAY-95@c4b4d6fe
- **Part:** glossary · decisions · invariants · part-map · environment-facts
- **Correction:** none
- **Recovered:** none

## glossary-definition-count/1

Every entry of `foundations/glossary.md` gives its definition in one sentence, counted as the decision guard counts binding sentences.

- **Method:** `python -B elements/glossary/format_guard.py foundations/glossary.md --record .runs/glossary.jsonl`
- **Rests on:** none
- **Derives from:** WAY-96@38f5315a
- **Part:** glossary
- **Correction:** none
- **Recovered:** none

## glossary-definition-words/1

No definition in `foundations/glossary.md` contains, outside code, *must* or a word the decision template forbids in binding sentences.

- **Method:** `python -B elements/glossary/format_guard.py foundations/glossary.md --record .runs/glossary.jsonl`
- **Rests on:** none
- **Derives from:** WAY-96@38f5315a
- **Part:** glossary
- **Correction:** none
- **Recovered:** none

## glossary-entry-version/1

No entry of `foundations/glossary.md` carries a version.

- **Method:** `python -B elements/glossary/format_guard.py foundations/glossary.md --record .runs/glossary.jsonl`
- **Rests on:** none
- **Derives from:** WAY-97@343b8b3b
- **Part:** glossary
- **Correction:** none
- **Recovered:** none

## glossary-definition-uses/1

For every entry of `foundations/glossary.md` whose definition differs from its definition on "{fork-point}", the glossary guard's report lists the uses of its term.

- **Method:** `python -B gate/run_tests.py elements/glossary --record .runs/glossary-tests.jsonl`
- **Rests on:** none
- **Derives from:** WAY-97@343b8b3b
- **Part:** glossary
- **Correction:** none
- **Recovered:** none

## glossary-avoid-growth/1

No word of an *Avoid* in `foundations/glossary.md` stands, outside the text the glossary template leaves out, more times in a file of `foundations/` or in an element's template than on {fork-point}.

- **Method:** `python -B elements/glossary/format_guard.py foundations/glossary.md --base {fork-point} --record .runs/glossary-base.jsonl`
- **Rests on:** none
- **Derives from:** WAY-98@22381f48
- **Part:** every
- **Correction:** none
- **Recovered:** none

## glossary-avoid-single/1

No word stands in the *Avoid* of two entries of `foundations/glossary.md`.

- **Method:** `python -B elements/glossary/format_guard.py foundations/glossary.md --record .runs/glossary.jsonl`
- **Rests on:** none
- **Derives from:** WAY-98@22381f48
- **Part:** glossary
- **Correction:** none
- **Recovered:** none

## glossary-avoid-term/1

No word of an *Avoid* in `foundations/glossary.md` is a term there.

- **Method:** `python -B elements/glossary/format_guard.py foundations/glossary.md --record .runs/glossary.jsonl`
- **Rests on:** none
- **Derives from:** WAY-98@22381f48
- **Part:** glossary
- **Correction:** none
- **Recovered:** none

## glossary-not-target/1

Every term, identifier and closed-list value the *Not* of an entry of `foundations/glossary.md` names exists.

- **Method:** `python -B elements/glossary/format_guard.py foundations/glossary.md --record .runs/glossary.jsonl`
- **Rests on:** none
- **Derives from:** WAY-99@64acf85f
- **Part:** glossary · part-map · invariants · environment-facts
- **Correction:** none
- **Recovered:** none

## glossary-not-quoted-word/1

Nothing the *Not* of an entry of `foundations/glossary.md` names holds the term or its forms, and every word it names in quotation marks stands outside quotation marks and outside the glossary in a file of `foundations/` or in an element's template.

- **Method:** `python -B elements/glossary/format_guard.py foundations/glossary.md --record .runs/glossary.jsonl`
- **Rests on:** none
- **Derives from:** WAY-99@64acf85f
- **Part:** glossary · decisions · invariants · part-map · environment-facts
- **Correction:** none
- **Recovered:** none

## glossary-entry-merge-todo/1

Where {merge-onto} exists, no field of an entry of `foundations/glossary.md` holds `TODO`.

- **Method:** `python -B elements/glossary/format_guard.py foundations/glossary.md --merge-onto {merge-onto} --record .runs/glossary-merge-onto.jsonl`
- **Rests on:** none
- **Derives from:** WAY-99@64acf85f · WAY-71@cab47c5b
- **Part:** glossary
- **Correction:** none
- **Recovered:** none

## Withdrawn identifiers

| Identifier | Successors |
|---|---|

## Quarantined invariants

| Identifier | Version | Until |
|---|---|---|
