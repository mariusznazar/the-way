# Report 09 — foundation step 1.5, invariants agent (sentence author) (saved by the orchestrator from the returned text)

Wrote entries in `foundations/invariants.md` only; committed nothing. Invariants guard 0 errors, 0 warnings;
comparison `references checked 378, stale 0`. Followed the process root's `record-invariant` skill; stopped before the
part map and any check.

## Entries as written

Fingerprint renewals (WAY-31, N2): `repository-file-location/1`, `element-directory-contents/1`,
`relation-model-directory-contents/1`, `invariant-example-target/1`, `map-example-target/1`, `glossary-example-target/1`
keep their sentences and `/1`; *Derives from* `WAY-09@16b8026b`. Rechecked: `repository-file-location` already admits any
`agent-instructions` file; the other five rest on WAY-09 sentences 2–3 and its examples clause, unchanged.

`outbound-link-reach/1`, edited in place (N3), brief's wording:
- Old: "No file git tracks contains a link into a private note collection, or into a repository that a reader not
  signed in to its host cannot open." (`e3535bb0`)
- New: "No file git tracks contains a link into a repository that a reader not signed in to its host cannot open, or
  into a private note collection other than to the place of tasks that the `## Backlog` section of the root `AGENTS.md`
  names." (`8577ad1d`)
- *Method* `TODO` · *Rests on* none · *Derives from* `WAY-27@0b40467e` · *Part* every · *Correction* none. Version `/1`
  (no main branch; `--base none` compares nothing).

`skill-entry-points/1`, new (N5), fingerprint `eb5c0fb8`, after `project-technology-record/1`:

> Every file named `SKILL.md` that git tracks, or that stands untracked and not ignored by git, outside the `.claude/` and
> `.agents/` directories at the repository's root, with `<name>` the name its frontmatter gives, has a file
> `.claude/skills/the-way-<name>/SKILL.md` and a byte-identical file `.agents/skills/the-way-<name>/SKILL.md`, whose
> frontmatter names `the-way-<name>` and gives a description starting with the description the frontmatter of that
> `SKILL.md` gives, whose text contains, in backticks, the path of that `SKILL.md` from the repository's root, and contains
> `--show-superproject-working-tree`, `git ls-files --stage -- ':/.the-way'`, `git rev-parse --show-toplevel` and the words
> "If the skill tells you to resolve a link to find the-way, skip that", and whose text holds a sentence that names, each in
> backticks, the name of every such `SKILL.md` and holds the words "with the `the-way-` prefix, never an unprefixed one";
> and every directory in `.claude/skills/` or `.agents/skills/` whose name begins with `the-way-` is named `the-way-<name>`
> for the `<name>` of such a `SKILL.md`.

Method `python -B gate/run_tests.py gate --record .runs/gate-tests.jsonl` · Rests on none · Derives from WAY-127@b40a68e5
· Part every · Correction none. Wording vs brief: "contains the words" (the generator's sentence continues ": the root is
the one above."); path "in backticks, from the repository's root"; names and prefix words in one sentence. Method is a
command run by the gate's flow test (WAY-45, WAY-55, WAY-61). Part `every`: any part can add, rename or re-describe a
`SKILL.md`. Rests on `none`: the four facts are WAY-127's reasons (WAY-73); a change reaches this entry through WAY-127's
fingerprint.

`generated-overview/1`, *Part* changed (not in the brief) to `part-map · agent-instructions`; sentence and fingerprint
unchanged; WAY-62: `agent-instructions` will now generate files for agents. Reversible in one line.

## WAY-56 weighing

One entry; the flow `skills-reach-the-way-sessions` names it. Items 1–3 are the required contents of one pair (splitting
would match the violating "one entry per field"); item 4 is the reverse side of item 1 — together: entry points and
skills match one to one, each pair complete. Cost: rewording one literal raises the version of the whole entry; one test
cites it.

## Search findings (WAY-33)

1. Link: *Derives from* WAY-127; WAY-127's level 1 met (guard 0 errors).
2. Change: six WAY-09 renewals and `outbound-link-reach`.
3. Change: `generated-overview` *Part*; entry points list skill names, not directories — comply.
4. Hand-off to 1.6: flow naming `skill-entry-points`; failure mode "detected by skill-entry-points"; patterns
   `.claude/skills/**`, `.agents/skills/**`. Question: `path-pattern-reach/1` fails while the patterns match no tracked
   file, so the foundation commit carrying them must not land before the entry points exist.
5. Question: the exception is about the target (as WAY-27's), so a link from a decision's *Origin* to a vault task
   description passes this invariant; WAY-27's level 2 still catches it. Provisional: keep the wording; the narrower
   alternative adds a rule WAY-27 does not hold.
6. Question: "the place of tasks" includes the `_zadania\` folder the section names. Provisional: yes.
7. Question: `outbound-link-reach` does not cover a local file path such as WAY-125's plugin cache path
   (`foundations/decisions.md:3571`). Provisional: outside the task; return step.
8. No *Derives from* WAY-107 (the heading comes through WAY-27); a rename would fail loudly.
9. Question: "untracked and not ignored" only widens the check in a working tree; *Rests on* `none` rather than
   `gitignore-paths@3218da8f`. Provisional: keep both.
10. Question: "frontmatter" has no glossary entry or fact; both sides read by the same rule. Provisional: none.
11. No change needed: `derived-file-content` (its `every` reaches the entry points; method `TODO`; the generator's own
    test checks equality); `skill-rule-source` (rewritten paragraphs must keep naming the template and `elements/common/`
    — note for the implementer); `script-*`, `flow-invariant-link`, `flow-test-location`, `flow-test-run`,
    `test-runner-pass-line`, `invariant-citation-version`; `identifier-holders`, `glossary-term-collision`; glossary — the
    sentence avoids "entry point"; no *Avoid* word added.
12. Per the orchestrator's answers: no separate invariant for "not installed in itself", no relation to WAY-34.

## Guards

Invariants guard (process root's copy, byte-identical to the worktree's): exit 0, `0 error(s), 0 warning(s), 3
unchecked` (one from `--base none`, two from `--merge-onto none`, among them "the fingerprints the links of the entries
carry"); no `human_verdicts.md`. Decisions guard `0 error(s), 8 warning(s), 5 unchecked`; glossary guard `0 error(s),
0 warning(s), 5 unchecked`. `stale_refs.py`: exit 0, `references checked 378, stale 0`.

## Instruction for the check author

The entry verbatim and its method; a `test_*.py` under `gate/`; citation `# invariant: skill-entry-points/1` inside the
test method; assert every property the sentence states on the real repository, with literal strings, path forms and
directory names written out as the sentence gives them; read names, descriptions and paths from the `SKILL.md` files,
never from the generator's code (WAY-69); the deliberate break belongs to the code's reviewer; no check cites a retired
identifier or raised version.

## Polish meaning sentences (WAY-114)

- skill-entry-points: Każdy plik `SKILL.md` the-way (śledzony albo nieśledzony i nieignorowany) spoza `.claude/` i
  `.agents/` w korzeniu ma dwa identyczne bajt w bajt wskaźniki `.claude/skills/the-way-<nazwa>/SKILL.md` i
  `.agents/skills/the-way-<nazwa>/SKILL.md`, które noszą nazwę `the-way-<nazwa>`, zaczynają opis od opisu skilla, podają
  jego ścieżkę, oba polecenia rozpoznające produkt, polecenie wyznaczające korzeń, zdanie o pominięciu rozwiązywania
  dowiązania i zdanie o prefiksie `the-way-` z nazwami wszystkich skilli; a każdy katalog `the-way-*` w tych dwóch
  miejscach należy do jakiegoś skilla.
- outbound-link-reach: Żaden plik śledzony w gicie nie odsyła do repozytorium, którego nie otworzy czytelnik
  niezalogowany u jego dostawcy, ani do prywatnego zbioru notatek — poza odesłaniem do miejsca zadań, które wskazuje
  sekcja `## Backlog` głównego `AGENTS.md`.
- repository-file-location, element-directory-contents, relation-model-directory-contents, invariant-example-target,
  map-example-target, glossary-example-target: sens bez zmian, nowy odcisk WAY-09.
- generated-overview: Żaden plik generowany dla agenta nie zawiera przeglądu katalogów repozytorium — sens bez zmian;
  teraz sprawdzany także przy zmianie w części `agent-instructions`, która zaczyna generować pliki dla agentów.
