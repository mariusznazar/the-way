# Findings to fix — review of the return step, task `testing-guidelines`

Source: `reports/return-review.md` (first line `FAIL f3c7f7e4cd6cb8ba6fcc19af87c50fe50c316697`), the blocking finding in the reviewer's words:

## Important

### 1. WAY-228's binding sentence and the template rule no longer say what Q13 settled; correction 1 rests on a false premise

- **Place:** `foundations/decisions.md:6062` (WAY-228 binding sentence, "a condition kept after
  every step" in place of "an invariant's sentence"); `product-guidelines/testing/template.md:158-159`
  (rule "Test inputs and expected values", same change).
- **What is wrong:** the task's settlement for this sentence, Q13
  (`.runs/task-cycles/testing-guidelines/task.md:97`), lists the relations a property test takes its
  expected value from as "odwrócenie operacji, **zdanie niezmiennika** albo prostsza wersja napisana
  z wymagania" — the sentence of an invariant. Row 14 (`task.md:177`) carries Q13 into the decision.
  The return step replaced that item with "a condition kept after every step", claiming that "the
  meaning intended here is the field's" and that "the meaning of WAY-228 does not change"
  (`reports/return.md`, Corrections 1).
- **Why the premise is false:** Q13 names its source as `raport_wytyczne_testow.md`, section 1. That
  section says, at line 29: "Biblioteka Hypothesis ma testy stanowe ze sprawdzeniem „prawdziwe po
  każdym kroku". To naturalna postać niezmiennika the way: losowy ciąg akcji, a po każdej
  sprawdzenie zdania niezmiennika (wniosek badacza)." and its table at line 46 files the Hypothesis
  quotation as "odpowiednik niezmiennika". The source thus uses "zdanie niezmiennika" for the
  sentence of a the-way invariant — exactly the glossary meaning ("An invariant is a sentence about
  the product that is true or false on every commit", `foundations/glossary.md:87`). The task's
  Polish uses "niezmiennik" in the same sense elsewhere (e.g. `task.md:19`, the "niezmiennika" test
  level). "An invariant's sentence" was therefore not a term used against its entry, and step 11 of
  `task-cycle/skill/SKILL.md` (lines 317–331) gives the return step no ground to rewrite it.
- **Why it matters:** the meaning does change. Before, a property test could take its expected value
  from the sentence of one of the product's invariants (the raport's own proposal: a random sequence
  of actions, the invariant's sentence checked after each); the human approved that list in Q13.
  Now the binding sentence names only "a condition kept after every step", which neither names the
  product's invariants nor covers an invariant's sentence checked over generated inputs without
  steps (e.g. a refusal invariant of a trust boundary checked over generated requests). The change
  alters a settled decision against its source — what the whole-change review's fidelity check
  forbids — and the return report's line "the meaning of WAY-228 does not change", meant "for the
  request", would tell the human the opposite of what happened.
- **Fix expected:** restore "an invariant's sentence" in the binding sentence of WAY-228 and in the
  template rule (`template.md:158`), and drop the request-facing claim. The *Rationale*'s change
  (`decisions.md:6095`, "a condition kept after every step" for developers' practice, read off
  Goldstein and Hypothesis) can stay: there the word was in the field sense, and the binding
  sentence's "invariant's sentence" is bridged to it by the raport's section 1.
- **Evidence:** `git diff a2f1165..f3c7f7e -- foundations/decisions.md product-guidelines/testing/template.md`;
  `task.md:97`, `:98` (Q13 source naming raport section 1); `raport_wytyczne_testow.md:29`, `:46`, `:53`.

