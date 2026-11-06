# Findings 1 — blocking findings of the review of the whole change

Source: `reports/04-review-report.md`, `FAIL b4a55092d8710ff59ec0110b2038f32ff5705ad2`, range `dfd50e5..b4a5509`. The reviewer's words, copied:

**I1 — the invariant `cross-part-imports` states its marked-invariant exception without its
direction, more broadly than row 3, WAY-299 and its own test.**

- Place: `foundations/invariants.md:310`, the clause "or an invariant "the part `<X>` does not
  depend on `<Y>`" naming the two parts reads `Violated: yes`".
- What is wrong: the clause binds `<X>` and `<Y>` to nothing; "naming the two parts" is met by an
  invariant in either order. Read as written, a marked "the part `shell` does not depend on `core`"
  names the two parts of an import `core` → `shell` and lets it pass. The settlement it is written
  from keeps the direction — row 3 of *Settlements to record*: "importu objętego niezmiennikiem
  „część X nie zależy od Y” oznaczonym jako naruszony" (the import the invariant covers, X → Y) —
  and so does everything else the change writes: WAY-299 (`foundations/decisions.md:9107`, "says
  part X depends on today"), the template (`elements/part-map/template.md:98`, "says it depends on
  today") and the test, which passes only the ordered pair (`elements/part-map/test_cross_part_imports.py:274`,
  `(part, other) in marked`).
- Why it matters: WAY-263 — an entry the change writes that restates its source more broadly or
  without a qualification is Important; WAY-114's *Rationale* names the review of the whole change
  as the only place a row's wording drift is caught, since the human accepted the meaning with the
  row and is not asked again. A later reader of the invariant (a return step, a product copying the
  example, which `elements/invariants/examples.md` now invites) can take the looser reading and the
  test then disagrees with its own sentence.
- Evidence: the three quoted lines above; the test's code at :274.
- Recommended fix: e.g. "…or an invariant "the part `<X>` does not depend on `<Y>`" reads
  `Violated: yes`, where X is the part of the importing file and Y the part of the imported one."
