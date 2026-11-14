---
title: Druga tura porządków fundamentu the-way
status: draft
created: 2026-10-23
updated: 2026-11-14
tags: [wznowienie]
related: "a note of the author's vault"
---

## Po co to

- **Jak jest dziś:** Czytając zasady the way, czyli procesu pracy nad produktami z agentami, trafiasz na osobne decyzje opisujące samą treść szablonów oraz odwołania do zewnętrznych praktyk bez jasnego wskazania, co z nich przejęto. Dziennik nie ma podziału tematycznego, a spośród około trzydziestu wskazanych wpisów trzeba dopiero oddzielić rzeczywiste wybory od treści, która może zostać wyłącznie w szablonach.
- **Kto to odczuwa:** Mariusz i agent przeglądający lub zmieniający zasady muszą czytać te wpisy i odróżniać obowiązujące wybory od szczegółów szablonu. Przy zapożyczeniach muszą też ustalać, czy źródło tylko uzasadnia regułę, czy świadomie przejęto z niego konkretną praktykę.
- **Co jeśli nic:** Nadmiar wpisów i niejasność zapożyczeń już stwierdzono podczas przeglądu dokumentacji; bez porządków pozostaną przy kolejnych lekturach i zmianach. Źródła nie dokumentują błędu produktu ani zablokowanego zadania spowodowanego tym stanem — potwierdzona potrzeba dotyczy czytelności i utrzymania zasad.

# Ułatwić rozumienie i znajdowanie zasad the way oraz powodów ich przyjęcia — w tym jak decyzja nazywa praktykę przejętą z zewnątrz

Status: ready for cycle
Project relation: independent
Defect introduced by: none

## Description

### Need

- Dziennik decyzji the way (`foundations/decisions.md`) ma 331 wpisów (stan `foundations` `f4af75d`); w losowej próbie 30 wpisów ok. 13 opisywało tylko to, co mówi jeden szablon albo skill the way, który tę regułę i tak zawiera (raport o dzienniku decyzji, ustalenie 9).
- Od prośby #120 the way szablon decyzji ma pytania „dokąd to idzie”, a WAY-293 mówi, że w dzienniku the way reguła stojąca w jednym skillu albo szablonie stoi tam z jednym zdaniem powodu, a wpisem zostaje tylko wybór z realnym kosztem; istniejących wpisów nikt według tego nie przejrzał — prośba #120 zostawiła to temu zadaniu.
- Mariusz i agent przeglądający albo zmieniający zasady czytają te wpisy i muszą sami odróżniać obowiązujące wybory od powtórzonej treści szablonu.
- Przy zapożyczeniach z zewnątrz nie widać, czy źródło tylko uzasadnia regułę, czy świadomie przejęto z niego praktykę: 23 decyzje mają relację `derives from WAY-100` (WAY-121, 128–133, 137–140, 142–144, 146, 147, 164, 173, 256, 268, 270, 273, 280); część z nich nie mówi, co przejmuje (np. WAY-128–133, WAY-137–140, WAY-173), część mówi to w różnej formie (np. WAY-121, WAY-142–147, WAY-164).
- WAY-100 każe zapożyczenie nazwać decyzją, a szablon decyzji mówi, że „co bierzemy z X” nie jest pytaniem decyzji (WAY-19); skill szukający kandydatów na wpisy przy doprecyzowaniu zadania do tej reguły nie kieruje, więc w zadaniu wytycznych testowania (the way, prośba #42) przyjęto wiersz „decyzja nazywa, co szablon testów bierze ze źródeł”, a cykl rozłożył go potem na inne decyzje bez decyzji Mariusza (AIR-518).
- Decyzja odzyskana z kodu produktu ma *Rationale* `unknown`, gdy nikt nie zna powodu; szablon decyzji nie każe przedtem zajrzeć do opisu commita ani prośby o scalenie, które wprowadziły dany kształt kodu.

### To do

1. Każdy wpis dziennika decyzji the way dostaje ocenę pytaniami „dokąd to idzie” z szablonu decyzji (`elements/decisions/template.md`, punkt **Where it goes:** w sekcji „Decision or invariant”), z pytaniem 1 w brzmieniu dla dziennika the way (WAY-293). Ocena powstała w doprecyzowaniu i stoi niżej („Lista ocen do To do 1”); cykl nanosi wiersze, które Mariusz przyjął, i nie ocenia wpisów od nowa (pytanie 1).
2. Wpis oceniony „stoi w skillu albo szablonie” wychodzi z dziennika: jego numer idzie na listę wycofanych, a reguła stoi w swoim skillu albo szablonie z jednym zdaniem powodu; każde odwołanie do wycofanego numeru jest przepięte albo zdjęte (WAY-02).
3. Wpis oceniony „część pytania innego wpisu” staje się akapitem tamtego wpisu (WAY-19, WAY-05), a jego numer idzie na listę wycofanych z tamtym wpisem jako następcą.
4. Każda decyzja the way, która przejmuje praktykę z zewnątrz, ma relację `derives from WAY-100` i mówi jednym wzorem, co przejmuje i czego nie; decyzja, której źródło tylko uzasadnia regułę, ma to źródło w *Based on* i tej relacji nie ma (pytanie 3). Dotyczy co najmniej 23 decyzji, które tę relację dziś mają, i decyzji, które przejmują praktykę bez niej. Wzorem jest dopisek do WAY-100 z odpowiedzi na pytanie 2: decyzja nazywa praktykę i to, co z niej bierze, w zdaniach wiążących albo w *Rationale*; źródło stoi w *Based on*, a źródło, którego czytelnik repozytorium nie otworzy, jest opisane w *Rationale* (WAY-27); to, czego z praktyki nie bierze, stoi w *Rejected* (pytanie 2).
5. Skill szukający kandydatów na wpisy fundamentu (`elements/common/skill/read.md`, punkt, który otwiera „Read in each element's template what makes something an entry of it”) kieruje też do reguły o pytaniu decyzji z szablonu decyzji (punkt, który otwiera „The question names a choice someone could answer otherwise”): lista tego, co bierze się ze źródeł, nie jest kandydatem na decyzję. Reguła godząca to z WAY-100 stoi w WAY-100 (dopisek z odpowiedzi na pytanie 2); szablon decyzji przy regule o pytaniu odsyła do WAY-100, a `read.md` tylko kieruje do tej reguły szablonu, bez własnego brzmienia (pytanie 2).
6. Szablon decyzji (sekcja „Recovered decisions”) i WAY-29: opis commita albo prośby o scalenie, które wprowadziły dany kształt kodu, jest źródłem do zacytowania z identyfikatorem commita, a agent zagląda tam, zanim wpisze `unknown`. Krok specyfikacji (`task-cycle/spec/`) przy zadaniu, które przebudowuje zastany kod, pyta o to samo.

#### Lista ocen do To do 1

Ocena wszystkich 331 wpisów (stan `foundations` `f4af75d`), 2026-11-14: dziesięciu agentów ocenia partie według reguł spisanych dla tego zadania (pytania „dokąd to idzie” i WAY-293); próba 20 wpisów z ziarnem 20261114 i 9 wpisów wskazanych przez agentów jako wątpliwe przeczytana w całości; poprawki próby oznaczone w grupie F. Grupy A–E to wiersze inne niż „zostaje”; Mariusz przyjmuje tabelę przed cyklem, grupy B i C rozstrzyga grupą.

**Przyjęte przez Mariusza 2026-11-14 w komplecie:** grupy A, D i E według tabeli; grupa B zostaje w dzienniku; grupa C wychodzi do szablonów elementów (WAY-293, akapit drugi). Grupa F zostaje.

#### A. Wraca do skilla albo szablonu (115)

Wpis wychodzi z dziennika, reguła zostaje w miejscu z kolumny „Miejsce” z jednym zdaniem powodu. Uzasadnienie agenta po angielsku.

| Wpis | Pytanie wpisu | Miejsce | Pewność | Uzasadnienie agenta |
|---|---|---|---|---|
| WAY-301 | What marks the last review of a repository's foundation? | foundation-review/SKILL.md | m | Tag naming and message rule stated at step 7 of the review skill; rejected is only the merge marker. |
| WAY-302 | How does a review of the foundation go, and what does it change? | foundation-review/SKILL.md | m | Course of a review lives in the foundation-review skill directory; one skill, files already state it. |
| WAY-304 | Which skill reviews a repository's foundation, and whose requests does it read? | foundation-review/SKILL.md | h | One skill per repository, own requests only; stated at SKILL.md and remarks.md. |
| WAY-354 | What does a review of the foundation do with a decision that describes a transitional state? | foundation-review/proposals.md | m | behaviour of one skill; the four files of foundation-review already state it; no-field choice fits one sentence |
| WAY-303 | Which unfixed remarks of merged requests does a review of the foundation check? | foundation-review/remarks.md | m | Which remarks the review reads is remarks.md content, same skill directory. |
| WAY-305 | What does a review of the foundation do with the weak points that decisions name? | foundation-review/weak_points.md | h | Weak-point listing and cheap read-only checks are weak_points.md content. |
| WAY-331 | Where in the repository does the audit of the process stand? | foundations/part_map.md | m | says audit is its own part with its own directory; part map already holds process-audit with files process-audit/** |
| WAY-366 | Do the directories of a product's tests run at the same time, and how does a product keep them from it? | gate/run_tests.py | m | default of one runner and its limit option; not cited outside; rule belongs to the runner's docs |
| WAY-259 | What does an installed skill entry point tell an agent to read from the pinned the-way? | installation/install.py | m | Wording of the installed entry point lives in install.py and agent-instructions/skill_entry_points.py with tests; no markdown file cites it, rule is cheap. |
| WAY-257 | What does the skill of `instruction-files` show as the ground of each verdict? | instruction-files/judging.md | m | Says what each row of the instruction-files judgement shows; judging.md and SKILL.md already state both questions; cheap form rule of one skill. |
| WAY-311 | How do the rows of a judgement of instruction files stand for a fragment that goes to several places and for a proposal? | instruction-files/judging.md | h | Row format of a judgement table is judging.md content; cheap. |
| WAY-332 | Where do the results of the audit lie? | process-audit/SKILL.md | h | results outside every repository; skill states it with reference to the locations file; reason is one sentence |
| WAY-335 | What decides whether a fix of the process works? | process-audit/SKILL.md | m | version not date decides fix; skill states it without the reason, which fits one sentence; 343 and 348 derive from it |
| WAY-336 | Does how often an issue comes back set its priority? | process-audit/SKILL.md | h | frequency of return is material not priority; skill states it as a standing rule |
| WAY-340 | Does the audit replay frozen earlier tasks on an old and a new version of the process? | process-audit/SKILL.md | h | records a lack of replay; skill states it with a sentence to give when asked; nothing else stands on it |
| WAY-341 | How often does the audit run, and what starts it? | process-audit/SKILL.md | h | weekly cadence and what starts the session already stated in the skill |
| WAY-338 | What is the time of a cycle? | process-audit/audit_count.py | m | definition of a cycle's time; only the script cites it; reason fits one sentence beside its code |
| WAY-342 | Which entries of the locations file does the audit of the process read? | process-audit/audit_count.py | m | names the locations-file entries the audit reads; contract of the counting command and skill; no file cites it by number |
| WAY-343 | Which version of the-way did a cycle of the-way itself run on? | process-audit/audit_count.py | m | how a cycle of the-way's own repository gets its version; script header already states it |
| WAY-346 | Where does the result of the audit's count show the cost of an occurrence? | process-audit/audit_count.py | h | says the count gives cost levels per issue not per cycle; script and skill already state it |
| WAY-348 | Does the weekly count of the audit read the measures of context and cache use and the gate times, and compare them? | process-audit/audit_count.py | m | the count reads the measures and gate times and compares medians per version; script and skill describe it; Rejected is cheap |
| WAY-352 | From which table of the stage report is the cost of a cycle counted? | process-audit/audit_count.py | m | reading the older stage-report form is a transitional fallback in one script; script already states it |
| WAY-333 | How is a problem that the audit counts graded and classed? | process-audit/problem_register.md | m | weight scale and widening class list stated in register template and skill; Rejected unknown; cheap form rule of the register |
| WAY-334 | What does the audit count, remarks or problems? | process-audit/problem_register.md | h | a problem reported by several stages counts once; already stated in the register template |
| WAY-345 | How is the cost of one occurrence of a problem that the audit counts graded? | process-audit/problem_register.md | m | five fixed levels of cost of an occurrence stated in the register template and script; reason fits one sentence |
| WAY-359 | How does the template of the register of problems record a defect found at the request or after the merge? | process-audit/problem_register.md | m | classes and column rules of the register template; the template is the one place; not cited elsewhere |
| WAY-281 | What does an audit of the skills of guidelines merge, and what does its list hold? | product-guidelines/audit_end.md | m | Cause-merging rule of one audit procedure; audit_end.md states it, the linter and boundary parts repeat in kind files. |
| WAY-282 | In what order do the causes of an audit of the skills of guidelines stand? | product-guidelines/audit_end.md | m | Order of repair stands in audit_end.md; weight-then-gain is cheap to keep with one sentence of reason. |
| WAY-283 | What of an audit's list of causes does the human decide on? | product-guidelines/audit_end.md | m | Top-of-list count rule stands whole in audit_end.md; a number-and-limit rule, cheap choice. |
| WAY-285 | How is a cause of the top of an audit's list checked? | product-guidelines/audit_end.md | m | Check-before-human rule stands in audit_end.md; independence cost fits one sentence. |
| WAY-210 | What does the coding-guidelines skill look at first? | product-guidelines/coding/SKILL.md | m | Coding skill reads what the product has first and leaves new tools to the human; applies WAY-121 and WAY-211; cheap with one sentence of reason |
| WAY-266 | What does a session do that did not read the refinement steps a skill of guidelines relies on? | product-guidelines/coding/SKILL.md | m | One sentence each in three guideline skills sending a session to refine-task steps 1-2; cheap, already stated in all three SKILL.md files. |
| WAY-200 | Who designates a product's exemplar for a kind of code, and when? | product-guidelines/coding/kinds.md | m | Who designates the exemplar and when: first-file task or comparison by the skill; kinds.md and SKILL.md state it; cheap rule. |
| WAY-201 | How does the coding-guidelines skill's audit of a product with code end? | product-guidelines/coding/kinds.md | h | What the coding audit ends with (exemplar, gain sentence, do-not-copy with line); kinds.md already gives it; nothing else stands on it. |
| WAY-208 | Which parts of a product get coding guidelines? | product-guidelines/coding/recognize.md | h | Every part holding code, build scripts included, gets coding guidelines; recognize.md and template state it; one reason sentence suffices. |
| WAY-209 | When do a product's coding guidelines come into being? | product-guidelines/coding/recognize.md | m | General coding file before first code, file of a kind with first file of that kind; recognize.md modes and SKILL.md state it. |
| WAY-278 | How do the rules on failures and logs reach a product that has coding guidelines? | product-guidelines/coding/recognize.md | h | How the coding skill's refresh handles missing rules (propose, yes makes extension); recognize.md states it; applies WAY-251. |
| WAY-277 | Who chooses a library that writes a product's log lines? | product-guidelines/coding/settle.md | h | Who chooses a log library; settle.md:14 and SKILL.md state it; Rejected is unknown; the choice is cheap. |
| WAY-279 | What does a product's decision on the rules on failures and logs hold? | product-guidelines/coding/settle.md | m | What the product's own decision on failure and log rules holds; stated across coding skill files; one skill directory, cheap to keep with a reason. |
| WAY-211 | Where do the tools of the standing checks and a linter's set of rules come from? | product-guidelines/coding/starting_set.md | m | Where tool choices and research come from, research at extension not refresh; one skill's route; research.md and starting_set.md already state it |
| WAY-202 | Which standing checks must a product's coding guidelines settle, and from when do they bind? | product-guidelines/coding/template.md | m | Three required standing checks and binding from the coding-guidelines task; template and settle.md state them; reason fits one sentence, though some risk of being weakened. |
| WAY-207 | Where is a fault of one file of a product's code fixed? | product-guidelines/coding/template.md | h | Fault of one file fixed in that file, turning rule off is decision change; template lines 149-152 state it; mirrors WAY-178 for code. |
| WAY-271 | Which rules on failures and logs does the template of the coding discipline require? | product-guidelines/coding/template.md | h | Lists which six rules the coding template requires and where; the template states it; Rejected is unknown; the entry mainly describes the template. |
| WAY-272 | What counts as a failure, and where is it written? | product-guidelines/coding/template.md | m | Definition of a failure and last-resort handler is template content; one sentence of reason (a refusal is the product working) keeps it. |
| WAY-275 | Which lines do a product's logs hold, and what joins them? | product-guidelines/coding/template.md | m | Template content on business events and identifier names in log lines; template.md:208-210 states it; cheap form rule. |
| WAY-310 | How does a product's rule on secrets and personal data show a departure from the ban on personal data alone? | product-guidelines/coding/template.md | h | Names one field of one rule in one template; narrow form rule. |
| WAY-217 | Does an approved departure count as missing guidelines? | product-guidelines/reading.md | m | An approved departure removes the missing-guidelines finding only in its scope; reading.md states it whole; one sentence of reason suffices |
| WAY-187 | How does the styleguide skill audit a product that has screens? | product-guidelines/styleguide/audit.md | m | Two-direction audit with standing question and fallback without running product; audit.md carries it; list form lives in audit_end.md. |
| WAY-183 | Which user interfaces of a product get a styleguide? | product-guidelines/styleguide/recognize.md | m | Which user interfaces get a styleguide: recognize.md step already says every one, admin panel included; reason fits one sentence. |
| WAY-185 | What does the styleguide skill look at first? | product-guidelines/styleguide/recognize.md | m | Skill reads what product has first and extends it; new library left to human; recognize.md, new_tools.md and audit.md each state their part. |
| WAY-189 | Which invariants does a styleguide start with? | product-guidelines/styleguide/settle.md | h | First three invariants a styleguide proposes; settle.md names them with tests; reason (test decides each cheaply, review reads meanings) is one sentence. |
| WAY-191 | Where do a styleguide's thresholds of contrast and its demand of visible focus come from? | product-guidelines/styleguide/settle.md | m | WCAG adopted through a product decision with facts for criteria; settle.md states it fully; coding template only cites the fact mechanism. |
| WAY-184 | When does a product's styleguide come into being? | product-guidelines/styleguide/starting_rules.md | m | Styleguide before first screen with wider starting set; starting_rules.md states the width, timing stands in the skill; one reason sentence enough. |
| WAY-186 | Where do a styleguide's starting rules come from? | product-guidelines/styleguide/starting_rules.md | m | Sources of starting rules (preferences, then critiqued research, not at refresh); starting_rules.md and research.md already hold the procedure. |
| WAY-192 | How does a product's instruction file lead to its styleguide? | product-guidelines/styleguide/task_document.md | m | How product's AGENTS.md leads to the styleguide; task_document.md and template state it; the pointer and rules-file placement derive from instruction-files rules. |
| WAY-176 | How does a styleguide name its colour roles and pair them? | product-guidelines/styleguide/template.md | h | Roles table naming and background-text pairing is a template content rule; template section Roles states it; cheap reasons. |
| WAY-177 | What does a styleguide say of shared controls? | product-guidelines/styleguide/template.md | h | Shared-control states rule of the styleguide template; template already states it including path-only naming; cheap form rule. |
| WAY-178 | Where is a fault of one screen fixed? | product-guidelines/styleguide/template.md | h | Fault of one screen fixed in its component is a template rule, stated at template line 128; points to WAY-172 for approval. |
| WAY-180 | Does a styleguide require a page showing the product's components in every state, and where is it served? | product-guidelines/styleguide/template.md | h | Kitchen-sink page rule of the styleguide template; template names it, served in development only; nothing outside the template needs the entry. |
| WAY-182 | Where does a value of design tokens say it comes from, and who picks the source? | product-guidelines/styleguide/template.md | h | Each design-token value carries its source, skill chooses source; stated in template and task_document; cheap rule with one-sentence reason. |
| WAY-169 | What happens to a reference of guidelines when the entry it names changes? | product-guidelines/template.md | m | Changed entry brings its rules along; template line 112 already states it. One sentence of reason (agents keep following old rule) suffices. |
| WAY-170 | What checks the form of a product's guidelines? | product-guidelines/template.md | m | Records that no script checks guidelines form; review compares with template, foundation_check reports references. Template states it; part_map cites it only as a withdrawal reason. |
| WAY-171 | What form does a file of a product's guidelines take? | product-guidelines/template.md | h | Describes the form of a guidelines file (header lines, sections, rule fields, English headings); the template is exactly that form and carries it. |
| WAY-248 | What does the testing-guidelines skill look at first? | product-guidelines/testing/SKILL.md | m | Mirror of the coding skill's rule: extend existing tool, new tool is a technology question; testing SKILL.md and new_tools.md already state it. |
| WAY-250 | How does the testing-guidelines skill's audit of a product with tests end? | product-guidelines/testing/audit.md | h | Describes how the testing skill's audit ends; audit.md already carries levels, exemplar and trust-boundary items; only that file cites it. |
| WAY-249 | Where does the testing-guidelines skill's starting set come from? | product-guidelines/testing/starting_set.md | m | Starting-set sourcing and when research runs is the testing skill's step; starting_set.md and research.md hold it, a one-sentence reason suffices. |
| WAY-245 | How does a product's instruction file lead to its testing guidelines? | product-guidelines/testing/task_document.md | m | One-line pointer to testing guidelines outside the installer block, naming no command; mirror of WAY-212; task_document.md states it |
| WAY-246 | Which parts do testing guidelines apply to, and when are they read? | product-guidelines/testing/template.md | h | Applies-to parts and when-to-read condition of testing guidelines; the template states both; rejected narrower part sets are cheap to explain in one sentence |
| WAY-108 | What form does a project definition take? | project-level/definition_template.md | m | Form of a project definition; template states it. Invariant project-definition-form derives from it, so that link needs repointing. |
| WAY-109 | What may a project definition treat as settled without the human's answer? | project-level/definition_template.md | m | Background, success and risks come from the human's answers; template already says it with the falsification marker. |
| WAY-110 | When does a deadline enter a project definition? | project-level/definition_template.md | h | Deadline only when the human names one; template states it. One sentence of reason keeps the rule. |
| WAY-116 | Which foundation entries may a project definition project? | project-level/definition_template.md | m | Which entry kinds a definition may project; template and part-map skill state it. Rejected ways cheap. |
| WAY-152 | What does leading a project plan leave to others? | project-level/lead/skill/SKILL.md | h | What leading leaves to others is the lead skill's own scope; SKILL.md opens with it; cheap choice, nothing cites it. |
| WAY-156 | How does project leading route a plan or definition change? | project-level/lead/skill/route_changes.md | m | Routing of plan or definition changes is lead's route_changes step; plan delegated_mode follows it; Rejected options are cheap. |
| WAY-218 | Where does project breakdown place missing guidelines and first-kind work? | project-level/plan/skill/guideline_tasks.md | m | Plan-project places guideline tasks before consumers and exemplar work with first-kind task; applies WAY-216 and WAY-242 in one skill |
| WAY-151 | How much of large project definitions and existing plans does plan-project read? | project-level/plan/skill/reading_definition_and_plan.md | h | Reading rule of plan-project, held by its own step file and SKILL.md; no entry cites it; reasons survive in one sentence. |
| WAY-112 | How does an agent develop and resume a project definition? | project-level/skill/SKILL.md | m | How an agent develops and resumes a definition; skill, first_write.md and rounds.md state it. Rejected ways are cheap. |
| WAY-111 | What does the project level read in the current foundation? | project-level/skill/read_foundation.md | m | What the project level reads in the foundation; read_foundation.md states it and delegates selection to WAY-150. |
| WAY-214 | How does task refinement find missing product guidelines? | project-level/task/skill/read_sources.md | m | Refinement uses the shared reading by parts and exposes uncertainty; mostly points to reading.md; refine-task step states it |
| WAY-353 | How does a task document point at a place to change in a file? | project-level/task/template.md | m | how a task document points at a place; template and draft step already state it with reason |
| WAY-356 | Where is a defect found after a merge recorded, and in what form? | project-level/task/template.md | m | line in every task header; template and draft step state it; register class half sits in WAY-359 |
| WAY-329 | How is the identifier of a project task's line in the backlog derived? | project-level/task_line.md | h | derivation of a task's identifier already stated with an example in task_line.md; reason fits one sentence |
| WAY-322 | May a human strike from the list of the technology step a matter of an agent's way to the running product or of how a human learns of a failure? | project-level/technology/ | m | four files of the technology step already state that the human cannot strike the matter; one sentence of reason suffices |
| WAY-262 | What does an author report when a check fails and passes when run again? | task-cycle/change/SKILL.md | h | One report line of the author: command and exit code of both runs; change/SKILL.md states it; Rejected is unknown. |
| WAY-219 | What does an author check before a user-interface change reaches review? | task-cycle/change/ui_check.md | m | Author checks states and screenshot before review, with fallback when no way to the running product; ui_check.md holds it whole |
| WAY-351 | How are the tokens written again to the prompt cache counted? | task-cycle/cycle_measures.py | m | counting rule of one measure with its thresholds; the script holds it; the rejected way costs one sentence |
| WAY-264 | How does a task plan represent output written together by one command? | task-cycle/plan/SKILL.md | m | Plan skill lines 127-136 state the pattern and command rule; mechanical check pointer sits in task-cycle/skill/SKILL.md; no file cites the number. |
| WAY-296 | In what form does the cycle record hold its process remarks? | task-cycle/record_template.md | h | Form of process remarks is what the record template gives; SKILL.md points to it. |
| WAY-357 | Where does the cycle record the cause of a correction after the request opened? | task-cycle/record_template.md | m | one record item per correction; record template and correction step state it |
| WAY-220 | How does a code reviewer grade a finding about appearance? | task-cycle/review/SKILL.md | h | Reviewer grades appearance by effect on the user; review skill already states it in one sentence |
| WAY-221 | When can departure from a guideline example support a blocking finding? | task-cycle/review/SKILL.md | h | Departure from a guideline example blocks only through a named consequence; review skill already states it; orchestrator authority is WAY-161 |
| WAY-263 | Which foundation mismatches are Important findings? | task-cycle/review/SKILL.md | m | Grading criterion of the reviewer; review/SKILL.md states it in full; one sentence of reason (restated broader is a conflict) keeps it. |
| WAY-297 | How does a reviewer grade a finding about a missing glossary entry or a missing qualifier? | task-cycle/review/SKILL.md | h | Grading rule for glossary findings stated in review skill; a cheap grading limit. |
| WAY-363 | How does a reviewer grade a finding about the structure of code? | task-cycle/review/SKILL.md | m | grading rule of one review skill; coding docs only mention the consequence; one sentence of reason fits |
| WAY-364 | How does a reviewer grade a finding that a foundation entry departs from the form of its template? | task-cycle/review/SKILL.md | m | grading rule of one review skill, already stated with its exception; reason fits one sentence |
| WAY-362 | What does the review of the whole change ask about the structure of the code a change leaves, and from which numbers? | task-cycle/review/whole_change.md | h | describes what one review step asks and which numbers it reads; script and step already state it |
| WAY-158 | Who reads the full diff of a task-cycle change or slice? | task-cycle/skill/SKILL.md | m | Orchestrator uses file list and first review line; SKILL.md step states it; reviewer's full-diff reading belongs to review skill. Cheap choice. |
| WAY-159 | When does the task-cycle orchestrator rely on focused-check evidence? | task-cycle/skill/SKILL.md | h | Orchestrator relies on command and exit code of focused checks; SKILL.md states it twice; cheap rule, only the orchestrator applies it. |
| WAY-294 | How does the cycle make sure its process remarks hold every item its stage reports give? | task-cycle/skill/SKILL.md | m | Remarks-check script step stands in SKILL.md "record before it is committed"; reason is one sentence. |
| WAY-295 | What does the cycle do with a listing of the remarks check that it holds wrong? | task-cycle/skill/SKILL.md | m | Listing-held-wrong procedure stated in SKILL.md; exception path of WAY-294 script. |
| WAY-298 | How does a cycle on the-way itself start from the current rules? | task-cycle/skill/SKILL.md | m | Fast-forward start stated at SKILL.md step 4 and correction.md; no decision number cited but text present. |
| WAY-325 | What does the orchestrator of a task cycle do when a stage report says material its handoff names stayed unread? | task-cycle/skill/SKILL.md | m | orchestrator's handling of unread-material reports belongs in the cycle skill; Rejected is unknown; skill names the section but not the three ways |
| WAY-326 | What does a task-cycle stage report about the material its handoff names that stayed unread? | task-cycle/skill/SKILL.md | h | the report section Unread material and its repair rule already stand in the skill and request template; one sentence of reason suffices |
| WAY-349 | How does the orchestrator of a task cycle run the product's gate so that the gate times reach the cycle's record? | task-cycle/skill/SKILL.md | m | orchestrator runs gate through the script; script holds the form; cited only by scripts; one sentence of reason fits the cycle skill |
| WAY-367 | Does a task cycle run the gate on its starting state? | task-cycle/skill/SKILL.md | m | step 4 of the cycle skill states the skip and its fallback; request template only reports it |
| WAY-163 | What does the cycle run before it opens a request its code review blocked? | task-cycle/skill/blocked_finding.md | m | What runs before a blocked request is blocked_finding.md's content; correction.md and request_template only cite it; cheap choice. |
| WAY-306 | What does the review of the merge of the target branch ask? | task-cycle/skill/correction.md | m | Merge-review dispatch question stated in correction.md and implement step 12; cheap wording rule. |
| WAY-286 | What form does the description of a request a task cycle opens take? | task-cycle/skill/request_template.md | m | Skeleton of request description is the template's content; README only points to it. |
| WAY-287 | What does a request put before the human for a decision? | task-cycle/skill/request_template.md | m | Content of the decisions section is defined item by item in request_template.md; long but one file. |
| WAY-290 | How is the form of a request's description checked? | task-cycle/skill/request_template.md | m | Run form-check script before opening request; template gives the steps, script has own tests. |
| WAY-291 | What does the cycle do with an error of the form check that it holds wrong? | task-cycle/skill/request_template.md | m | Error-held-wrong path stated in template section "An error you hold wrong"; exception to the check rule. |
| WAY-318 | Which artifacts of a change's check reach the description of its request? | task-cycle/skill/request_template.md | m | says only screenshots reach the request description; both request_template.md and ui_check.md carry it; cheap form rule, reason fits one sentence |
| WAY-327 | What does an item of a request's section for the human's decisions carry where the human chooses? | task-cycle/skill/request_template.md | h | form of items where the human chooses; template already states four parts and fifth part with steps; single file rule |
| WAY-307 | What happens to a spec whose review fails? | task-cycle/skill/spec_review.md | h | Keeping spec-reviewed.md on FAIL is stated in spec_review.md and spec SKILL.md; cheap file rule. |
| WAY-371 | What reading limit does a slice of a plan have? | task-cycle/slice_size.py | m | one constant of one script with measured basis; rationale fits a comment of one sentence |

#### B. Wraca do szablonu, ale wpis ma źródło zewnętrzne albo relację do WAY-100 (29)

Agent dał „do szablonu”, lecz wpis cytuje źródło w *Based on* albo przejmuje praktykę (WAY-100); szablon nie ma miejsca na źródło, a fakt środowiska bez wpisu, który na nim stoi, wychodzi z fundamentu (WAY-73). Decyzja Mariusza 2026-11-14: zostaje.

| Wpis | Pytanie wpisu | Miejsce | Pewność | Uzasadnienie agenta |
|---|---|---|---|---|
| WAY-84 | How is a setting that people of the product change outside its repository written? | elements/environment-facts/template.md | m | A setting changed outside the repository is a fact; template states it in full, decisions only where the product declares the choice. |
| WAY-85 | How is a finding of a study written as an environment fact? | elements/environment-facts/template.md | m | How a study finding is written as a fact; template states it, including the cross-publisher sentence for decisions. |
| WAY-130 | When does a rule enter an instruction file, and when does it leave? | instruction-files/SKILL.md | m | Skill states the repeated-mistake entry rule and its way out three times; one sentence of reason keeps it. Covers the-way's own AGENTS.md changes too. |
| WAY-133 | How is a rule of an instruction file kept when it has to hold every time? | instruction-files/SKILL.md | m | Skill's table and pitfalls already carry the mechanism-for-every-time rule with the hook caveat; the change-rule for the-way files is the same skill's. |
| WAY-258 | How are the files of the skill of `instruction-files` laid out? | instruction-files/SKILL.md | m | Layout of one skill's own files, one kind per file, no cross-pointers; SKILL.md states the kind files and one-level-deep rule, not every clause. |
| WAY-265 | Where is the file of a variant named, when a step's file points to it? | instruction-files/SKILL.md | m | Says only that a skill's SKILL.md also names a variant file with its condition; cheap form rule of skill layout, extends WAY-256. |
| WAY-131 | How is it settled whether a rule of an instruction file works? | instruction-files/judging.md | h | Three-question way of judging a rule is the content of judging.md's in-operation section; only that skill uses it. |
| WAY-129 | How does an instruction file point an agent to another file? | instruction-files/kind_main_file.md | m | The @ import only as @AGENTS.md and pointers by path with condition; kind_main_file.md pitfalls state it. Invariant instruction-file-imports derives from it. |
| WAY-280 | On what scale does an audit of the skills of guidelines weigh what it found? | product-guidelines/audit_end.md | m | One shared file already holds the weight scale for the three guideline skills; rule stated there with its reason; siblings 281-283 cite it. |
| WAY-204 | How are the rules of a linter's set split between the rules that block and the examples? | product-guidelines/coding/settle.md | m | Procedure of the skill: trial run, fresh judge, human approves split, one environment fact for the set; the criterion itself stays in WAY-203. |
| WAY-205 | How do a linter and a formatter enter a product whose code already breaks their rules? | product-guidelines/coding/settle.md | m | Linter invariant marked violated for dirty code, formatter reformats once; settle.md and task_document.md state it; rests on WAY-51 principle. |
| WAY-212 | How does a product's instruction file lead to its coding guidelines? | product-guidelines/coding/task_document.md | m | One-line pointer in AGENTS.md and kind files named by the index table; template and task_document already state it; the cost is one sentence |
| WAY-199 | What change of a product's exemplar takes approval? | product-guidelines/coding/template.md | m | Approval for changing exemplar applies WAY-172 to one case; status column of the files table stands in the coding template; rest in settle.md. |
| WAY-206 | What does the audit of a product's dependencies check? | product-guidelines/coding/template.md | m | Dependency audit checks only what the change brings against fork point; template Dependency audit rule states it with severity from the decision. |
| WAY-273 | May a product hide a failure? | product-guidelines/coding/template.md | h | One rule of the coding template with its line at template.md:201; Rejected repeats WAY-272; no other entry cites it. |
| WAY-276 | What do a product's logs not hold? | product-guidelines/coding/template.md | m | Template's ban on secrets and personal data with its exceptions; template.md states it with the departure; the GDPR source can stay beside it. |
| WAY-228 | Where does a test take the input it asserts on and the value it expects? | product-guidelines/testing/template.md | m | Testing template rule that input and expected value are written out, with property-test relation; template states it whole; cheap rule of that template |
| WAY-232 | Where does a test's expected value come from? | product-guidelines/testing/template.md | m | Expected value comes from a source other than the code, snapshots included; the testing template carries the rule whole; one sentence of reason suffices |
| WAY-233 | What does a change to an existing test need? | product-guidelines/testing/template.md | h | Changing, skipping or weakening a test needs a cause and evidence; the testing template states rule and list of weakenings |
| WAY-234 | What may a test's assertion check? | product-guidelines/testing/template.md | h | Assertions check required behaviour, not detail; the testing template states it with the precondition allowance |
| WAY-236 | How does AI enter a product's tests? | product-guidelines/testing/template.md | m | AI is no level of test; judge and self-healing terms; the testing template states it; guidelines silent on AI is the only rejected rival |
| WAY-237 | What does a product deliberately not test, and where is it said? | product-guidelines/testing/template.md | m | Required section Not tested on purpose with decision per item; the template and settle.md state it whole |
| WAY-239 | What does a bug caught only by a high-level test or by a human get? | product-guidelines/testing/template.md | h | A bug caught only high or by a human also gets a lowest-level test; one rule of the testing template, already stated there |
| WAY-241 | What does the recipe of a test level hold? | product-guidelines/testing/template.md | m | Recipe of the same fields per level, gate-only command, time limit by pointer; template states it; the rejected per-level commands is a form choice |
| WAY-243 | How is a flaky test treated? | product-guidelines/testing/template.md | m | Rerunning a flaky test only diagnoses, never passes the gate; the template carries it and the cycle applies it; sentence of reason suffices |
| WAY-137 | What decides between places to run that the simplest and cheapest option leaves tied? | project-level/definition_template.md | m | Tie-break for place to run stands in the template and settle.md with its reason; one sentence keeps agent-friendliness from becoming a filter. |
| WAY-139 | What does the-way hold for the skill that deploys a product, and which step checks that a product has one? | project-level/task/skill/resolve_gaps.md | l | Check lives in resolve_gaps.md and guide; only the item list stands solely in the entry and would have to move there. |
| WAY-370 | What does a task cycle do where the session has none of the-way's agent types? | task-cycle/skill/SKILL.md | m | fallback when the session lacks the types; cycle skill states it with the record line |
| WAY-288 | In what language is a request's description written? | task-cycle/skill/request_template.md | m | Language rule of request description stated in template; reason (public repo, Polish reader) is one sentence. |

#### C. Forma elementów fundamentu (26)

Agent dał „do szablonu elementu”; to forma fundamentu każdego produktu, której pytania 1–4 „dokąd to idzie” nigdzie nie kierują, a WAY-293 (akapit drugi) kieruje ją do szablonu. Decyzja Mariusza 2026-11-14: cała grupa wychodzi do szablonów elementów, jak grupa A.

| Wpis | Pytanie wpisu | Miejsce | Pewność | Uzasadnienie agenta |
|---|---|---|---|---|
| WAY-117 | How does a foundation entry stand in a project definition before it is written? | elements/common/projected_mode.md | m | How a projected entry stands in a definition; projected_mode.md carries it and each element skill points there. |
| WAY-41 | What identifies an entry of the part map? | elements/common/rules.md | m | Identifier rule for part map already stands in common rules with its withdrawn-identifier form; one sentence of reason (words, not numbers) suffices. |
| WAY-64 | Where do invariant and environment fact entries stand, and what identifies one? | elements/common/rules.md | m | Placement and identifier rules of invariants and facts already stand in common rules under Withdrawn identifiers; reason fits one sentence. |
| WAY-72 | In what language is a product's foundation written? | elements/common/rules.md | m | Common rules already state English for every element; the reason fits one sentence there. Cheap to restate for any template. |
| WAY-115 | How are foundation entries found in a project's source? | elements/common/skill/build_table.md | m | Candidate-table procedure of find-foundation-entries; skill and templates carry it. WAY-134 and WAY-315 cite it, but rows rule is the skill's. |
| WAY-37 | What happens to entries that wait for something when it arrives? | elements/common/way_of_working.md | h | Fix waiting entries in the same change is a step of the shared way of working; no real rival; rejected only periodic review. |
| WAY-32 | What types of relation can a decision name? | elements/decisions/template.md | h | Closed list of two relation types is a form rule already in the template; rejected related-to is cheap. |
| WAY-76 | How much does one environment fact entry hold? | elements/environment-facts/template.md | h | One sentence, one source, one reason to change; template states it with the same rule on invariants-as-facts. |
| WAY-77 | What shows what an environment fact is true of? | elements/environment-facts/template.md | h | What a fact is true of is shown by the edition or date read; the template states it in full. |
| WAY-78 | What is the binding part of an environment fact entry? | elements/environment-facts/template.md | h | Binding part of a fact is its sentence; template states it with the reason about re-read sources. |
| WAY-80 | What is an environment fact's source? | elements/environment-facts/template.md | m | Source form of a fact including readings of hosts; template carries it in detail. Long rejected list is about form of one field. |
| WAY-86 | How does a catalogue of requirements or a binding rule reach a product? | elements/environment-facts/template.md | m | Voluntary catalogue binds through an adopting decision, binding rule needs none; template states both; coding and styleguide files only cite. |
| WAY-93 | Where do glossary entries stand, and what identifies one? | elements/glossary/template.md | m | Where glossary entries stand and how they are headed; template repeats it. Cheap form rule, nothing cites the entry inside the log. |
| WAY-94 | What does a glossary entry hold, and what is its binding part? | elements/glossary/template.md | m | What a glossary entry holds and that the definition is the binding part; template states it with the same reason. |
| WAY-96 | How is a glossary definition written? | elements/glossary/template.md | h | One-sentence definition; template states it. Rejected fixed shapes are cheap and one sentence of reason keeps the rule. |
| WAY-97 | How does a sentence rely on a glossary term, and what does a change to a definition go through? | elements/glossary/template.md | m | Author of a changed definition searches the word and rewrites uses; template states it whole. Some cross-file reach, but one home. |
| WAY-226 | Which glossary holds a word of the process, and which a word of a product's domain? | elements/glossary/template.md | m | Glossary of the-way holds process words, product glossary domain words; the glossary template states it twice; rejected way is only that copies drift |
| WAY-56 | How much does one invariant entry hold, and what is its binding part? | elements/invariants/template.md | m | One invariant per entry is stated in the invariants template, which also points to this entry's Verification pair for judging what one sentence may join. |
| WAY-58 | What does an invariant entry record in *Derives from* when no decision entry of the product's log carries it? | elements/invariants/template.md | h | Form of the Derives from field for invariants with no decision entry; template already states it with the same example. |
| WAY-65 | How does a check cite its invariant, and which files are invariant tests? | elements/invariants/template.md | h | How a test cites an invariant and which files count; template states it fully, nothing else relies on this entry. |
| WAY-68 | What happens to a check that gives different verdicts on one commit? | elements/invariants/template.md | m | Template already says a flipping test is fixed and no quarantine is recorded; a one-sentence reason keeps the rule. |
| WAY-40 | What kinds of entry does the part map hold? | elements/part-map/template.md | h | Two kinds of part-map entry, dependency and boundary as fields, one file; template states it whole; rejected shapes cheap. |
| WAY-42 | What is the binding part of a part map entry? | elements/part-map/template.md | h | Says what the binding sentence of a part map entry is; template states it, rejected ways are cheap. |
| WAY-45 | How is a critical flow recorded and tested? | elements/part-map/template.md | m | Template already says a critical flow has no map entry and the invariant's Part names the parts; one sentence of reason keeps it. |
| WAY-49 | How does the part map record a surface, and how is a change to it made known? | elements/part-map/template.md | m | Surface entry form and naming the surface in the request already stand in the part map template; request template merely repeats it. |
| WAY-299 | How does a product keep the code of its parts within the dependencies its part map allows? | elements/part-map/template.md | m | Duty of cross-part-imports invariant is stated in part-map template; invariant can be repointed. |

#### D. Staje się zdaniem innego wpisu (6)

Wpis staje się akapitem wpisu z kolumny „Do wpisu”, numer idzie na listę wycofanych z tym wpisem jako następcą.

| Wpis | Pytanie wpisu | Do wpisu | Pewność | Uzasadnienie agenta |
|---|---|---|---|---|
| WAY-292 | What does the collapsed block of a request's description hold where the task document is in English? | WAY-288 | m | Narrows the block's content in the English-task case; part of the block question WAY-288 answers. |
| WAY-317 | What does a task cycle do when the foundation of a product settles no place for screenshots? | WAY-316 | m | the no-place case is the other half of the question where screenshots lie; WAY-316 already points to it; one rejected way mirrors WAY-219 |
| WAY-323 | What does the script of WAY-309 take for an absolute path and for a note link? | WAY-309 | h | narrows WAY-309; says what its script takes for a path or link; cannot change without changing WAY-309 |
| WAY-347 | How are the measures of how a cycle's agents use context and the prompt cache counted? | WAY-339 | m | exception to WAY-339 for context and cache measures; a file of their own avoids starting a series; part of the same question |
| WAY-358 | What causes does the line of a correction give? | WAY-357 | m | content of the correction line that WAY-357 introduces; cannot change without it; WAY-287 cites it for the sentence only |
| WAY-369 | Do the agent types of a task cycle start with the instruction files? | WAY-368 | m | one sentence on what the types' definitions set; changes only together with the types; not cited outside |

#### E. Mieszane (2)

Część zdań wraca do miejsca z kolumny „Miejsce”, reszta zostaje wpisem.

| Wpis | Pytanie wpisu | Miejsce | Pewność | Uzasadnienie agenta |
|---|---|---|---|---|
| WAY-09 | What may enter the process repository? | foundations/part_map.md | m | Directory inventory repeats the part map and goes there; the rule that a directory merges only when complete and no tools/ directory stays keep. |
| WAY-312 | Which sentences does a rule of a product's guidelines not hold? | product-guidelines/template.md | m | First sentence (rule holds no state or copies) is template content, home; the ban on rewriting known practices and audit steps stays keep. |

#### F. Zostaje (153)

Wpis zostaje w dzienniku. „Poprawka próby” to ocena zmieniona przy sprawdzeniu próby.

| Wpis | Pytanie wpisu | Dowód agenta | Uzasadnienie |
|---|---|---|---|
| WAY-01 | What state does the foundation describe? | stood on by: WAY-02, WAY-03, WAY-07, WAY-09, WAY-11, WAY-30, WAY-32, WAY-33, WAY-36 | Principle of the whole process: what the foundation describes; binds every element and the task cycle; real rejected ways (target-state foundation). |
| WAY-02 | How does whatever depends on an entry refer to it? | no single home: elements/common/rules.md, decisions template, relation-model/fingerprint.py, tests | Reference form binds all elements, tests and code; fingerprint or version beside references is a reasonable proposal with real cost. |
| WAY-03 | Who may change an invariant test, and when? | invariant tests read-only during implementation, kept so by a check at the merge | Naming-not-blocking is a costed choice; the read-only alternative is natural to propose; spans task-cycle, invariants and check script. |
| WAY-04 | What makes up a product's foundation? | stood on by: WAY-09, WAY-40, WAY-94, WAY-138, WAY-167 | Closed list of five elements and the mechanism-only rule for new patterns; a principle of the foundation no one file holds. |
| WAY-05 | How is a decision entry written? | - | poprawka próby: forma wpisu każdego produktu; brzmienie wybrane między wariantami w prośbie #120 |
| WAY-07 | How is a foundation entry changed? | a log that only grows on the main branch, every change a new version | Edit-in-place rule binds all five elements; versioned log is a reasonable alternative; stated in rules.md and each template, no single home. |
| WAY-08 | How is an invariant checked? | test coverage for every invariant — untestable ones leave the foundation | Method choice (test vs review, test seen failing) with real rejected rivals such as mutation-style breaking; reaches guidelines and invariants template. |
| WAY-10 | Who assesses a change to an invariant test or to the foundation? | one independent assessor on a model other than the author's | Who assesses foundation changes spans task cycle and agent instructions; costed rejected assessor stage; stood on by nine entries. |
| WAY-11 | How does a task end? | no single home: task-cycle/skill/return_step.md, element templates, agent-instructions/README.md | Return step writes facts, words, settlements and invariants across elements; rejected invariant-for-every-behaviour search is a real cost; central to the cycle. |
| WAY-12 | How is a decision checked? | an error for every decision that nothing holds — no change passes | How decisions are held: invariant, line decision:, examples; error vs list is a costed choice; spans template, invariants, check script, plan skill. |
| WAY-13 | What sets the weight of a task's process? | the path chosen by size — size misleads | Principle of task weight: same checks for every size, two risk questions; spans plan and cycle skills; real rejected size-based paths. |
| WAY-14 | Who accepts a decision? | stood on by: WAY-12, WAY-18, WAY-19, WAY-30, WAY-123, WAY-172, WAY-267, WAY-302, WAY-313 | Who accepts a decision; short but eleven entries derive from it; field recording the approver is a plausible proposal. |
| WAY-16 | How are the checks of invariants run? | separate commands for an agent, a human and whatever runs the tests | One command for every test is a principle reaching gate, installation, guidelines and invariants; stood on by many entries and invariants. |
| WAY-17 | Which links between foundation entries are mandatory? | optional links — a missing one looks unneeded | Mandatory link chain across decisions, invariants and environment facts; no one template states it whole; links written at dependent end is a costed choice. |
| WAY-18 | How is a product's decision log kept? | - | poprawka próby: jeden dziennik; zmienia go zadanie o czytaniu dziennika, wybór z realnymi wariantami |
| WAY-19 | How are decisions numbered? | - | poprawka próby: numeracja; brzmienie wybrane między wariantami w prośbie #120 |
| WAY-21 | What is a decision's scope? | - | poprawka próby: zakres decyzji po częściach; zadanie o czytaniu dziennika waży tu tematy |
| WAY-22 | Is a rule a decision or an invariant? | one kind of entry for both — either the gate reads prose or reasons are lost | Decision-versus-invariant split spans decisions and invariants templates and the invariants skill; central taxonomy others stand on. |
| WAY-24 | How is a decision that rests on a prediction reviewed? | Review when in each entry, with a check-by date | No review dates and review as a human-run skill; check-by date is a natural proposal that passes unseen; spans decisions, facts, foundation-review. |
| WAY-25 | What settles a collision between two decisions? | every precedence recorded by a human alone, the agent stopping at each collision | Costed rule for collisions between decisions; spans template, decision skill, foundation step and request template; ranked-list alternatives plausible. |
| WAY-26 | How are trade-off principles and non-goals written? | - | poprawka próby: zasady kompromisu i non-goals każdego produktu; pytanie 4 „dokąd to idzie” na nim stoi |
| WAY-27 | Where may this repository point for its reasoning? | no single home: every part of the repository, invariant outbound-link-reach | Repo-wide rule on unreachable sources with a narrow backlog exception; rejected path in AGENTS.md would leak the disk layout. |
| WAY-28 | How does the process enter a product that already exists? | recovering the whole foundation at the start — slow, with reasons invented | How the process enters an existing product; spans part-map, invariants skills and guidelines; recover-everything is a plausible rival. |
| WAY-29 | How is a decision recovered from an existing product written? | - | poprawka próby: decyzja odzyskana z kodu; zmienia ją to zadanie (To do 6); ma źródło |
| WAY-30 | What happens when a change contradicts a decision? | a justified violation recorded in the plan, the decision unchanged | Contradiction handling narrows WAY-114; spans task-cycle foundation step, templates and guidelines; stood on by seven entries. |
| WAY-33 | What does the author of a foundation change search for? | a second search against the main branch before the merge, with the record | One whole-foundation search by the author, no record; spans task cycle, skills, review; eleven entries cite it; real rejected alternatives. |
| WAY-34 | Which version of the process does a product use? | every product on the newest the-way — results change with no change | Pinned version policy binds installation, task cycle and every element; costed rejected rivals; ten entries stand on it. |
| WAY-35 | What does an element's skill hold? | rules restated in the skill next to the template — two copies that drift | Skills hold only element-specific way; rules live in templates or rules.md; spans all five element skills and an invariant; restating is a likely edit. |
| WAY-36 | Is a rule a decision or does it belong in a plan? | - | poprawka próby: test planu, pierwszy próg wejścia do dziennika każdego produktu |
| WAY-38 | In what are the scripts of the-way written? | Node.js without packages — no abler than Python, and a second interpreter | Script language and stdlib-only rule binds every script in many parts; invariants enforce it; costed alternatives (Node, Go, shell). |
| WAY-44 | What assigns a file to a part? | tests as a part of their own | Cross-part file assignment rule; many entries and invariants stand on it, and its long rejected list holds real proposals. |
| WAY-48 | How is a trust boundary recorded? | no single home: part-map template, task-cycle plan and skill, testing guidelines | Trust boundary rule binds the map and the review step of the cycle; rejected ways (every file-reading script) are plausible. |
| WAY-51 | What does the main branch hold where the product does not meet an invariant? | stood on by: WAY-01, WAY-225, WAY-299, WAY-360 and the Violated field of invariants | Principle of how the main branch holds unmet invariants; spans invariants, gate, task cycle, guidelines; rejected ways tempting. |
| WAY-52 | What is generated from the part map for an agent? | rules pinned to path patterns, generated from the map | Records a lack of generation, but an invariant (generated-overview) derives from it and generating rule files is a plausible proposal. |
| WAY-53 | How is a derived file compared with what its generator produces? | stood on by: invariant derived-file-content, WAY-60 | Equality of derived file with generator output is a process-wide principle of the gate with no single home; invariant stands on it. |
| WAY-54 | Where does the value of a field in a template come from? | no single home: elements/common/rules.md, way_of_working.md, every element template | Principle across all templates: read values off the product, never nearest value of a closed list; no one file states it whole. |
| WAY-55 | Which part of the process holds the gate? | gate inside task-cycle — code coupled to task steps | A structural choice of where the gate lives with real alternatives; no skill file holds it, WAY-366 cites it, only the part map would. |
| WAY-60 | Where may a condition that decides an invariant stand, and how does its sentence name commits and measured quantities? | a commit's parent as the base | Fork-point and merge-onto measuring plus where a deciding condition stands span common rules, invariants template, gate and guidelines; WAY-61, 72, 73, 82 cite it. |
| WAY-61 | How is an invariant's method of checking written? | a command per invariant that a gate of its own runs | Method test or review across invariants template, gate check and guidelines; cited by eight entries; rejected ways are plausible proposals. |
| WAY-62 | What does an invariant entry name in the part map? | parts computed from what the test reads | How a change reaches invariants binds invariants template, part map, planning and way of working; WAY-44, 45, 63 stand on it. |
| WAY-63 | What is an invariant's result, and when does the command running the tests fail? | stood on by: invariant gate-exit-code, WAY-51, WAY-68, WAY-160, WAY-321 | Defines invariant result and the exit code of the test command; spans invariants, gate and review; rejected result vocabulary is plausible. |
| WAY-69 | Who writes an invariant's sentence, its test and the code the test covers? | three different agents for the sentence, the test and the code | Who writes sentence, test and code binds invariants template and the plan skill; WAY-135, 136 stand on it; separate test-writer agent is a plausible proposal. |
| WAY-71 | Does every field of a foundation entry appear in every entry, and what may it hold? | no single home: elements/common/rules.md, foundation_check.py, every element template | Fields, none and TODO rules apply to every element and the check; cited in ten files; rejected ways are real. |
| WAY-73 | Which entries name an environment fact, and when does a fact leave the foundation? | every fact in the Based on of the decisions it derives from | Which facts Rests on names binds invariants, environment facts and decisions templates and the fact skill; WAY-76, 77, 86, 191 stand on it. |
| WAY-82 | How does an environment fact keep up with what its source says? | a method for each fact — a command testing the behaviour | No check or clock for facts; a later agent could well propose re-verification; foundation-review and the template both rely on it. |
| WAY-89 | Which version of Python do the scripts of the-way run on, and when does it move? | a move at each new release — a yearly review nothing here needs | Python version choice and when it moves; invariants python-version-declared and script-imports stand on it; alternatives are real and costly. |
| WAY-90 | Which citations of a decision's *Based on* become environment fact entries, and how are they named? | no single home: elements/decisions/template.md, environment-facts skill and template | Which Based on citations become facts and how the product's own measurements are stated spans two elements; rejected ways are real and tied to WAY-27. |
| WAY-95 | Which words take a glossary entry? | an entry for every narrower meaning — the glossary grows | Which words take an entry is a disputed boundary; four files and four entries cite it, no single home. |
| WAY-99 | How does one word keep one meaning in the foundation? | a test of whether a definition true of one use fails | Criterion for two meanings has several plausible rejected tests; binds decisions, invariants and review skill, cited by four entries. |
| WAY-100 | When does a method or practice borrowed from elsewhere bind a product? | importing a whole outside method by default | Principle of the whole process; 24 entries cite it as the ground they derive from, no file states it whole. |
| WAY-101 | Who chooses the backlog tool used with the-way? | stood on by: WAY-107, WAY-161 | Process requires no particular backlog tool; principle across project-level and task-cycle, other entries derive from it. |
| WAY-102 | What is the-way for? | no single home: purpose of the whole process, spans every part | Statement of what the-way is for; no skill or template could hold it, and it frames the foundation-routing rule. |
| WAY-103 | Who is the-way for? | no single home: audience of the whole process, every skill's wording | Audience principle (author first, agents execute) applies to every skill and step; WAY-330 stands on it. |
| WAY-104 | How does a product write a word of its domain that the glossary of the-way holds? | the bare word of the process in a product's glossary | Real cost choice with long Rejected; changes independently of WAY-99 and binds products' foundations, glossary template and review skill. |
| WAY-106 | What does the project level write before tasks exist? | stood on by: WAY-121, WAY-124, WAY-126, WAY-142, WAY-144, WAY-145, WAY-152, WAY-267 | Project level writes no foundation entries; six files and eight entries stand on it, definition and plan split. |
| WAY-107 | Where does a product tell the project level where its backlog stands? | the file for every place, the section only naming the entry | Backlog place and task-rules routing with real costs; eleven files and eight entries stand on it across skills. |
| WAY-113 | How does an agent of the-way ask a human decision? | no single home: every skill of the-way that asks the human | Cross-skill rule for asking decisions; twelve files and five entries cite it, with a layered exception at refinement. |
| WAY-114 | What does a human accept of an entry, and when? | stood on by: WAY-14, WAY-25, WAY-95, WAY-97, WAY-99, WAY-134, WAY-155, WAY-172, WAY-314 | What a human accepts and when; spans readiness gate, task document, request; ten files and seventeen entries cite it. |
| WAY-118 | What makes a project definition ready for breakdown? | stood on by: WAY-117, WAY-121, WAY-124, WAY-126, WAY-142, WAY-145, WAY-156, WAY-267, WAY-313 | Readiness gate with script and invariant; fourteen files and nine entries stand on it, a final checklist that only warns is the cost. |
| WAY-120 | How does the-way critique an agent's proposal? | no single home: critique across foundation-review, guidelines skills, plan, technology, readiness gate | When critique runs and its form binds thirteen files in many skills; eight entries cite it. |
| WAY-121 | Where does a project settle the technology it needs? | the first tasks of the breakdown — the cut may depend | Technology step before the gate with the running-product exception; fifteen files and thirteen entries stand on it. |
| WAY-122 | How are the options of a technology choice found and checked before a human sees them? | stood on by: WAY-123, WAY-165, WAY-166, WAY-186, WAY-210, WAY-249 | Research of options with properties and critique; other technology and guidelines entries derive from it. Technology skill carries it. |
| WAY-123 | How does a technology choice reach a human who cannot assess the technology? | the options in one table as before — nothing breaks at once | How a technology choice reaches a human; prevails over WAY-114 in its area and is cited by three guidelines skills plus technology. |
| WAY-124 | When is a task ready for its cycle? | stood on by: WAY-152, WAY-154, WAY-172, WAY-215 | Task readiness spans task skill files, guidelines skills and task cycle; cost of readiness by candidate rows alone is real. |
| WAY-125 | Which methods does the autonomous task cycle use? | methods of an outside plugin, with or without a required version | Cycle uses the-way's own methods; plugin alternative is plausible and costly. Also states read-on-demand rule across stage skills. |
| WAY-126 | How does a projected entry enter the foundation? | holding a projected entry back — foundation would lag behind the code | How projected entries enter the foundation; spans plan, task and return step; WAY-124, 135, 136, 145 stand on it. |
| WAY-127 | How does a session working on the-way itself reach the-way's skills? | entry points written per checkout, ignored by git | Entry points with generator and invariant skill-entry-points; rules reach skills, scripts and global link; real rejected ways. |
| WAY-128 | What may a line of an instruction file that a tool loads into every session hold, and where does any other rule stand? | a rule kept whole whenever an agent might miss its moment | Admission rule for always-loaded lines; any rule could be kept on that ground. WAY-192, 212, 245, 256, 257 stand on it. |
| WAY-132 | Which file carries the instructions Claude Code, Codex and Cursor share? | stood on by: invariant root-claude-md-import | Symlink, full copy and relying on auto-read are real proposals; the invariant derives from it; kind_main_file.md only cites it. |
| WAY-134 | How does a task carry what its refinement settles for the foundation? | no single home: elements/common, project-level/task, task-cycle, guideline task docs, lead | Binds 19 files across refinement, cycle and orchestration; cited by ten entries; real Rejected alternatives. |
| WAY-135 | When does a task's cycle write a spec? | no single home: task-cycle/skill, spec, plan, change; stood on by WAY-307, WAY-365 | Route rule across several cycle skills; Rejected "spec for every task" is a real proposal with real cost. |
| WAY-136 | When does a task's change need a plan, and who makes and reviews it? | stood on by: WAY-135, WAY-158, WAY-161, WAY-162, WAY-229, WAY-264 | Route and review structure of the cycle across plan, change, review, skill; measured Rejected; eleven entries cite it. |
| WAY-138 | Which option of a technology choice is tested for what choosing it could break, and where do the risks found go? | no single home: technology/settle.md, decisions template, task template, definition_template | Rule binds the technology step and two templates; Rejected (test every option, risks in Based on) are real proposals. |
| WAY-140 | How does a task change something outside the product's repository? | no single home: task template, resolve_gaps, task-cycle skill, request_template, process-audit, backlog_place | Principle of who makes effects outside the repository; binds refinement, cycle and audit; cited by four entries. |
| WAY-141 | How does the installer give Claude Code the guidance in a product's root AGENTS.md? | stood on by: invariant installation-claude-guidance | Installer's CLAUDE.md import; Rejected (generated rule, editing existing file) are real proposals; invariant derives from it. |
| WAY-142 | What does the breakdown of a project write, and in what form? | stood on by: invariant project-plan-form; WAY-153, WAY-154 | Plan form decided against plan-inside-definition and per-task sections; script, template, gate and invariant all rest on it. |
| WAY-143 | What does a task of a project plan end with? | stood on by: invariant project-plan-check; WAY-218, WAY-372 | Cut by checkable outcome versus layers is a core principle a later agent could reverse; invariant derives from it. |
| WAY-144 | How does a project plan show which tasks can be worked on side by side? | no single home: lead skill, plan cut_tasks, plan template, task-cycle plan_member; stood on by invariant | Dependencies bind cycle starts not refinement across lead, plan and cycle; cited by five entries and an invariant. |
| WAY-145 | Who sets where an open question of an approved project definition is resolved? | no single home: definition_template, lead route_changes, plan place_questions, task skill | Ownership of question placement after the gate spans definition, plan and leading; invariant project-plan-check derives from it. |
| WAY-146 | What checks a project plan before it is handed over? | stood on by: invariants project-plan-form, project-plan-check | Script-versus-critique split is a principle across plan_check.py, critique_plan and template; invariants derive from it. |
| WAY-147 | How is a task of a project plan named, and what does its cycle take from the name? | stood on by: invariant project-plan-form; WAY-153, WAY-154, WAY-269, WAY-329 | Stable task name links plan, backlog and cycle record naming; binds plan and task-cycle; invariant derives from it. |
| WAY-148 | How do task-cycle stages pass their work to the orchestrator? | no single home: task-cycle change, plan, review, spec, skill | File-transfer contract binding every stage; fourteen entries cite it; long set of real Rejected alternatives. |
| WAY-150 | How do the-way skills choose which product foundation material to read? | no single home: way_of_working, project-level skills, task-cycle skills, guidelines recognize files | Foundation-reading selection binds sixteen files across the process; nine entries cite it. |
| WAY-153 | What evidence supports a task state in a project plan? | stood on by: invariants project-plan-state-evidence, project-plan-state-subprocesses | Evidence rule for plan state; invariants derive from it only; Rejected (reader queries PR host, infer from trace) are real. |
| WAY-154 | How do agents exchange a project task refinement and keep its result? | no single home: lead skill, task skill, guideline orchestrated modes, plan template, task_line | Exchange file and ownership rule across fifteen files and three orchestrated modes; large costed Rejected list. |
| WAY-155 | What may the answering agent settle during a refinement round? | no single home: lead/answering.md, task orchestrated_mode, guideline orchestrated modes | Limits of the answering agent bind lead and every orchestrated refinement; overrides WAY-114 in one area. |
| WAY-160 | How does the task-cycle orchestrator run the finished change's gate? | no single home: task-cycle change, plan, skill, request_template; stood on by WAY-261, WAY-349 | Gate is orchestrator's alone, binding change, plan and request; Rejected "gate after every slice" is a real proposal. |
| WAY-161 | Which findings of the review of the whole change are fixed, and how does the request carry the rest? | no single home: task-cycle review, change, skill, request_template, process-audit | Blocking line and Minor-finding handling across reviews and request; twelve entries cite it; large costed Rejected list. |
| WAY-162 | How does a code review of a task's change end when its findings block? | no single home: task-cycle review, skill, request_template, reserved_return | One-fix bound for every review kind with revert rule; five entries and a check script stand on it. |
| WAY-164 | What does the author of a change check of its own work before review? | no single home: task-cycle change, review/whole_change, skill, request_template | Own-work check binds author, reviewer and request; Rejected holds a measured review-without-report result; WAY-219 cites it. |
| WAY-165 | What must an answer to each matter of an agent's way to the running product settle? | stood on by: WAY-139, WAY-219, WAY-270, WAY-271, WAY-322 | Matters of an agent's way to the running product bind definition template, technology step and guidelines; five entries derive from it. |
| WAY-166 | How does whether an agent can use an option weigh in a choice of its way to the running product? | recommend a cheaper service an agent cannot use | Real cost: agent-unusable option stays compared with lack said; cheaper-service and look-further-first ways are plausible. Binds definition template, research and settle steps. |
| WAY-167 | Where do a product's guidelines stand, and what are their files named? | guidelines as a sixth element of the foundation | Where guidelines live and how files are named binds every guidelines skill, template and the part map; real alternatives rejected; other entries derive from it. |
| WAY-168 | What does a rule of a product's guidelines hold beside the foundation entries that carry it? | stood on by: WAY-171, WAY-173, WAY-176, WAY-189, WAY-202, WAY-271, WAY-360 | Principle of all guidelines: rule, decision link, invariant only where cheap test checks; cited by twelve entries and eight files across disciplines. |
| WAY-172 | How is a new or changed meaning of a product's guidelines approved? | new meaning written by the cycle and shown at the merge | Approval before code for a meaning with real cost, prevailing over WAY-114; binds styleguide, coding, testing skills, task cycle and task refinement. |
| WAY-173 | Does what the-way's template of a discipline of guidelines carries bind a product directly? | stood on by: WAY-172, WAY-176, WAY-198, WAY-202, WAY-207, WAY-312 | Principle that template rules bind a product only through its own decision; forty-six entries and every discipline template stand on it. |
| WAY-174 | How do the-way's skills of guidelines ask the human? | no single home: styleguide, coding and testing skills | Plain-words asking binds three skills and prevails over WAY-114; rejected way (skill writes what it recommends unasked) is plausible and costly. |
| WAY-198 | How does a product's exemplar bind? | the exemplar as an example alone | Only what a script checks of an exemplar binds; agents could well make all of it binding or none; WAY-199 to 201 derive from it. |
| WAY-203 | Which rules of a linter's set block a change of a product's code? | rule blocking while fewer than one report in ten leads to no change | Criterion for blocking linter rules has real cost and plausible alternatives (whole set, Google tolerance, correctness only); WAY-204, 207, 271, 360 stand on it. |
| WAY-213 | How do the agents of a task's cycle read the product's guidelines? | no single home: product-guidelines/reading.md, task-cycle/change, plan, review, spec, skill | Reading of guidelines by every agent of the cycle binds across several skills; rejected selection by each agent, excerpts, checklists carry real cost |
| WAY-215 | What happens to a task that needs missing discipline guidelines? | missing guidelines merely added to the consuming task | Wait for guidelines task before refinement, with plan-member routes; binds refine-task, plan and three guidelines skills; rejected ways are plausible and costly |
| WAY-216 | What does refinement assign to a task creating an unindexed kind of code? | blocking every unindexed kind — a genuinely first instance could never arrive | First file of a kind carries its exemplar, with extension exception; spans coding skill, refinement and plan; many plausible wrong readings |
| WAY-225 | What in a product's foundation is derived rather than written by hand? | stood on by: WAY-28, WAY-51, WAY-53, WAY-171, WAY-172, WAY-177, WAY-185, WAY-198, WAY-200 | Principle of what is derived and what is written by hand across the part map, invariants, styleguide; twelve entries derive from it |
| WAY-227 | Where does the human meet a task cycle's work? | no single home: orchestrator delegation across task-cycle; stood on by WAY-135, WAY-140, WAY-161, WAY-172 | Who approves what in a cycle and where the human first reviews; nine entries stand on it and no file outside the log states it |
| WAY-229 | On which class of model do the executor of a slice and the one author work? | every slice on the orchestrator's model — it pays the strongest price for transcription | Model class by role, one retry a class higher; binds planner, orchestrator, fix and review across task-cycle skills; rejected ways are plausible and costly |
| WAY-230 | How does a project plan order two tasks that realize the same projected entry? | no single home: plan skill assign_entries/hand_over, plan template, plan_check.py; invariant derives from it | Order between tasks realizing one entry, script-checked with a shown reason; rejected extra field and unfailing remark are plausible; an invariant derives from it |
| WAY-231 | Where do the rules of a product's tests stand? | the rules of tests added to the coding template as a kind of code named "test" | Testing is its own discipline apart from coding; shapes the coding and testing templates and both skills; a test taken as a kind of code is plausible |
| WAY-235 | How do a product's tests keep its trust boundaries? | a permanent test of refusal with no invariant — a second rule of a test seen failing | Trust boundary gets a refusal invariant, overriding WAY-168 in this area; ties the testing template, invariants and part map; the invariants file derives from it |
| WAY-238 | At which level does a test stand, and who chooses it? | a pyramid or a share of each level — numbers to even out rather than breaks to catch | Lowest level that shows the break, chosen by the cycle's author, not in refinement; binds testing template, cycle, review and refinement; WAY-237, 239, 242 cite it |
| WAY-240 | How do a product's testing guidelines name its test levels? | no single home: elements/glossary/template.md and product-guidelines/testing/template.md; narrows WAY-95 | Names of test levels take a glossary entry, overriding WAY-95; both templates state it; the precedence and the rejected unprecedenced pair carry a cost |
| WAY-242 | How is the exemplar test of a level designated? | the exemplar chosen by an agent of the cycle with no approval | Exemplar test of a level: comparison or first test, approved in refinement or at a blocked draft request; spans testing skill, refinement, plan and cycle; WAY-218 and WAY-250 cite it |
| WAY-244 | When do a product's testing guidelines come into being? | stood on by: WAY-215, WAY-218, WAY-247 | Testing guidelines before the first test; refinement wait and project breakdown derive from it; the lazy alternative is plausible and costs every later test |
| WAY-247 | May one task write a product's coding and testing guidelines together? | a task of its own for each discipline's guidelines | Binds coding skill, testing skill and plan/refinement skills; separate tasks would hold first code back for two refinements; no one file states it whole. |
| WAY-251 | What distinguishes a refresh from an extension of guidelines? | stood on by: WAY-186, WAY-211, WAY-216, WAY-249, WAY-278 | One boundary shared by coding, styleguide and testing skills; cited by eight files across skills and five entries. |
| WAY-252 | How does a mutation tool check a product's tests? | a threshold on the share of copies the tests fail | Rejected threshold is a plausible proposal that makes agents chase a number; WAY-253 and WAY-254 derive from it. |
| WAY-253 | Who runs a mutation tool in a task's cycle, and what does the author check in its place? | the author runs the tool and passes the surviving copies to the reviewer | Splits roles between author and reviewer across task-cycle change and review skills and the testing template; the rejected way is plausible. |
| WAY-254 | Where does the command of a mutation tool stand? | a mode of mutation in the gate | Carries precedence over WAY-16, an explicit exception that needs its own entry; rejected CI run and gate mode are plausible proposals. |
| WAY-255 | How does an agent of a task's cycle wait for a command that runs long? | a longer cache lifetime for every agent | Measured cost trade-off over agent types; binds change and review skills and the author type (WAY-368); an hour for all is a plausible proposal. |
| WAY-256 | Where does a fragment of a skill stand? | stood on by: WAY-125, WAY-127, WAY-128, WAY-258, WAY-259, WAY-265, WAY-360 | Principle of the whole process for where any skill fragment stands; binds every skill, long rejected list of plausible alternatives. |
| WAY-260 | What does each task-cycle stage report about what it could not find or understand? | collecting reports only from authors and reviewers | Binds every task-cycle stage's report plus orchestrator copying and remarks_check.py; cited by four entries; no single file states it whole. |
| WAY-261 | What does a task cycle report about a check that fails and passes when run again? | omitting counts — a one-off environment failure and a repeated product defect | Rule spans cycle record, request template and orchestrator skill with part-map logic; rejected ways are plausible and cost real defects. |
| WAY-267 | How does the step that settles technology run outside a project definition? | stood on by: WAY-121, WAY-122, WAY-123, WAY-137, WAY-138, WAY-139, WAY-165, WAY-268 | Binds technology step, task refinement, lead skill and cycle; real rejected ways (write log at once, change approved definition); ten entries rest on it. |
| WAY-268 | Who settles a technology choice that no decision or definition settles? | every new element of the stack, the smallest dependency included | Precedence over WAY-114 and a boundary decision across refinement and cycle; glossary term rests on it; rejected ways carry real cost. |
| WAY-269 | How does a task leave a cycle that met a reserved choice, and how does it come back? | no request, the stop reported only in the record or the conversation | Spans cycle, request template, lead skill, plan template; many plausible rejected ways with real costs; rests on WAY-268. |
| WAY-270 | When does the step that settles technology ask how a human learns of a failure of the running product? | the matter as part of the logs item | Narrows WAY-121 and WAY-122 with explicit precedence; real rejected alternatives; stood on by seven entries and seven files across skills. |
| WAY-274 | Where does a product's logging scope stand, and who adds to it? | the list alone — the human sees each item, but each new one changes the decision | Decides where a list stands so adding items changes no decision (WAY-30) and sets the consent boundary; spans template, settle.md and request template. |
| WAY-284 | What decides which causes of an audit a task takes? | no single home: audit_end.md, project-level/task/skill/guideline_findings.md, three settle/hand_back pairs | Binds across guideline skills and refine-task; rejected "weight deciding alone, all grave enter" swells tasks. |
| WAY-289 | Which things the cycle left unfixed or undone does a request put before the human for a decision? | no single home: task-cycle/skill/SKILL.md, correction.md, request_template.md, agent-instructions/README.md | Judging felt findings plus one-correction loop binds several files; rejected "only whether finding becomes a task". |
| WAY-293 | What prevails where a task or its spec excludes the entry for a choice? | no single home: elements/decisions/template.md, task-cycle, decisions log rule | Meta-rule on when a rule is an entry; precedence over WAY-22 and WAY-18; others stand on it. |
| WAY-300 | When does a request tell the human that the foundation waits for a review? | no single home: task-cycle/skill/SKILL.md, request_template.md, foundation-review/SKILL.md | Rejected "10 merges", "50 merges", "gate check" are real proposals; binds two skills and others derive. |
| WAY-308 | How does a task cycle keep the paths and the notes of its human out of what it publishes? | no single home: task-cycle/skill/SKILL.md, request_template.md, agent-instructions/README.md, project-level plan-state reader | Rejected "clean only in public repos" has severe cost; spans record and description, plan reader loss. |
| WAY-309 | How does the cycle find the private paths and notes in what it publishes? | stood on by: WAY-320, WAY-323, invariant tracked-file-private-paths | Invariant and two entries derive from it; script-by-pattern choice spans README, SKILL.md, template, installation. |
| WAY-313 | What is a decision of the foundation to the refinement of a project or a task? | no single home: project-level definition_template.md, task skill files, technology skill, elements-common | Decision is material not limit across refinement; stood on by WAY-165, 267, 314, 315. |
| WAY-314 | Which act of the human consents to a change of a decision that refinement shows? | no single home: project-level definition, lead, task and technology skills (12 files) | Rejected "acceptance of whole document as consent" is plausible; binds many skills; WAY-315 and others stand on it. |
| WAY-315 | From when does a decision of the foundation bind the work on a task? | binding only from the writing of code, the spec treating a decision as material | boundary of when decisions bind; refinement entries 113, 313, 314 stand on it; rule spans refine and cycle skills; rejected way is plausible |
| WAY-316 | Where do the screenshots that a change shows the human lie, and how do they reach the request? | screenshots kept in the record in the product's repository, embedded by link to the commit | real cost choice with several rejected places; invariants stand on it; binds task-cycle and project-level templates and skills |
| WAY-319 | What must an agent's way to the running product allow when two task cycles run at once? | - | poprawka próby: wiąże dwa miejsca procesu (krok technologii i sprawdzenie w cyklu) i stoi na pomiarze |
| WAY-320 | Where does a user keep the places outside every repository that the files of the-way name? | file found through an environment variable, as the private layer of another project does | stood on by: WAY-27, WAY-107, WAY-323, WAY-324, WAY-330, WAY-332, WAY-342; invariant rests on it; binds many skills |
| WAY-321 | When does the check of a foundation report an invariant that reads `test` and has no test citing it? | a separate mode of the script that a product adds to its own command | choice with real cost and plausible rejected modes; invariant stands on it; spans foundation_check.py, way_of_working.md and installation |
| WAY-324 | How does a product check the files it tracks for private paths and notes? | the installer copies the test file into the product | spans installation README, check script and invariant; plausible rejected alternatives with real cost for public products |
| WAY-328 | Does the-way hold its own code and tests to the general coding guidelines and the testing guidelines of a product? | stood on by: WAY-344, WAY-363 | the recorded basis WAY-217 requires for the-way's departure from guidelines; no single home; other entries stand on it; not merely transitional |
| WAY-330 | Where does the audit of the process get the class, weight and cost of an occurrence of each problem, and the tie of a problem to the fix meant to remove it? | the audit reading the records of cycles itself and giving the class, weight and cost | stood on by: WAY-333, WAY-334, WAY-342, WAY-345, WAY-356, WAY-359; register-versus-audit split is a real choice |
| WAY-337 | How is the cost of a cycle measured? | a cost divided by a measure of the size of the task | binds task-cycle dispatch messages and record plus audit script; glossary stands on it; several plausible rejected ties |
| WAY-339 | When do the measures of the audit stop being comparable? | stood on by: WAY-345, WAY-347, WAY-348 | rules of when measures stop being comparable span audit, cycle scripts and the gate runner; several rejected splits with real cost |
| WAY-344 | What does a script of the-way do when a file it reads lacks a field it needs? | review alone with the test left to the choice of the cycle | no single home: every script of every part; many rejected variants with real cost; binds new and changed scripts |
| WAY-350 | Which runs of the gate does the audit compare between versions of the process? | median of all runs, as for the other measures | rejected ways (shortest run, failed runs in median) are tempting; rule spans gate script and audit comparison |
| WAY-355 | Which task fixes a defect found after a merge? | stood on by: WAY-356, WAY-358 | definition of defect after a merge, used by task template, task skill, audit and correction entries as one test |
| WAY-360 | Does the template of the coding discipline require a rule of the size of a function and a file, and how does it reach a product? | rule proposed as a further rule a product may take up | rejected way leaves product with no threshold; stood on by WAY-361, WAY-365; spans template, settle, recognize |
| WAY-361 | How does the review of a change get the sizes of functions and files from a product? | no single home: product-guidelines/coding/template.md, task-cycle/review/whole_change.md, task-cycle/plan/SKILL.md | one-test-command exception rule links product template and review; rejected second command is tempting |
| WAY-365 | What does a change do where it adds to a function or a file that stands over the threshold of the rule of size? | treating the addition as an open design choice, with a spec | no single home: task-cycle/plan/SKILL.md, task-cycle/change/SKILL.md; rejected spec route is plausible and costly |
| WAY-368 | Which agents run the stages of a task cycle in Claude Code? | stood on by: WAY-369, WAY-370, WAY-255 | binds task-cycle, installation and agent-instructions; types, installer and tracked copies; invariants derive from it |
| WAY-372 | When is a task split into several tasks? | no single home: project-level/task/skill/read_sources.md, project-level/plan/skill/cut_tasks.md | rule binds task refinement and plan cut; many rejected ways are tempting; WAY-13 derives from it |
| WAY-373 | Where does an agent of a task cycle make a working copy to check something, and what happens to it? | no single home: task-cycle/plan, change, review, skill | one rule for every agent of the cycle and the orchestrator; stated in six files; rejected ways plausible |


### Questions to settle

- 1. Kiedy powstaje lista ocen wpisów dziennika the way i kto ją przyjmuje?
  - Answer: (a) — w doprecyzowaniu: agenci oceniają wszystkie wpisy pytaniami „dokąd to idzie”, próba czytana w całości poprawia oceny, a tabelę przyjmuje Mariusz przed cyklem; przyjęta lista stoi w tym dokumencie, a cykl ją nanosi.
  - Not chosen:
    - (b) ocena w cyklu, przyjęcie przy scaleniu z opisu prośby — tabelę Mariusz czyta później, odrzucenie wierszy w prośbie oznacza rundę poprawek przywracającą wpisy i odwołania, a cykl, który nie może zapytać w trakcie, sam rozstrzyga przypadki graniczne.
  - Source: Mariusz (przez doradcę dnia), 2026-11-14, „1 — a, ocena teraz. Ale przyjęcia tabeli nie robię za Mariusza — wycofanie ponad stu wpisów dziennika the way to sprawa procesu dla niego.” (odpowiedź na pytanie z drogami a, b i rekomendacją a).
- 2. Gdzie stoi reguła, która godzi WAY-100 (zapożyczenie wiąże przez decyzję, która je nazywa) z regułą szablonu decyzji, że „co bierzemy z X” nie jest pytaniem decyzji?
  - Answer: (a) — w WAY-100, dopiskiem w brzmieniu: „A decision that adopts a method or practice from outside names the practice and what it takes from it, in its binding sentences or its *Rationale*; names the source in *Based on*, or, for a source a reader of the repository cannot open, describes in *Rationale* what was seen there (WAY-27); and puts what it leaves out of the practice in *Rejected*. A list of what is taken from one source is no decision: each rule taken stands in the decision that carries it (WAY-19).” Szablon decyzji przy regule o pytaniu odsyła do WAY-100; `elements/common/skill/read.md` kieruje do reguły o pytaniu z szablonu decyzji.
  - Not chosen:
    - (b) zdanie tylko w `elements/common/skill/read.md` — lżejsza zmiana, ale WAY-100 i szablon decyzji dalej czytają się jak sprzeczne, wzór dla 23 decyzji z *To do* 4 nie ma miejsca w fundamencie, na które można się powołać, a kto pisze decyzję poza szukaniem kandydatów (np. skillem `record-decision`), reguły nie widzi.
  - Source: Mariusz (przez doradcę dnia), 2026-11-14, „2 — a, dopisek do WAY-100 w zaproponowanym brzmieniu.” (odpowiedź na pytanie z drogami a, b, kosztem pozostawienia bez zmian i rekomendacją a).
- 3. Które decyzje niosą relację `derives from WAY-100`?
  - Answer: tylko te, które nazywają przejętą praktykę; dowód, na którym decyzja stoi (artykuł, repozytorium, wynik pomiaru), idzie do jej *Based on* z adresem, cytatem i datą odczytu, bez tej relacji.
  - Source: notatka Mariusza do tego zadania, sekcja „Gdzie jestem”, punkt 2 (stan z 2026-11-06): „Ustaliliśmy zasadę: dowód, na którym decyzja stoi (artykuł, repozytorium, wynik pomiaru), idzie do jej pola *Based on* z adresem, cytatem i datą odczytu; relacja „derives from WAY-100” zostaje tylko tam, gdzie decyzja nazywa przejętą praktykę.”

## Context

- Zadanie powstało z drugiej tury porządków fundamentu the way, odłożonej po pierwszej turze (the way, prośba #37, `foundations` `f0b2130`).
- Mariusz 12.11.2026, przy przeglądzie raportu `the task's note in the author's backlog` (ustalenia 8 i 9, karta D6): ocena „wybór zostaje / treść do szablonu” obejmuje cały dziennik, nie tylko WAY-176–192 i WAY-198–211; metoda — agenci nadają rodzaj według spisanych reguł, próba czytana w całości z ustalonym ziarnem, tabela do przyjęcia.
- Skrypty tej metody (rozbiór dziennika, partie dla agentów, scalanie klas, tabela) leżą w `the author's analysis data directory in the notes vault` i działają na obu dziennikach; tamtejsze reguły klasyfikacji powstały przed prośbą #120 i opisują klasy gry (K, R, G, T, O, P), nie pytania z szablonu.
- Kryterium oceny jest już w procesie: prośba #120 the way (zadanie „co trafia do dziennika decyzji”) dodała pytania „dokąd to idzie” i zmieniła WAY-293; jej zadanie wyłączyło przepisywanie istniejących wpisów dziennika the way do tego zadania.
- Podział dziennika the way na sekcje tematyczne przeszedł do zadania „jak agent czyta dziennik decyzji” (notatka `zadanie_the_way_jak_agent_czyta_dziennik_decyzji.md` obok tej), które przestawia mniejszy dziennik, gdy to zadanie jest scalone wcześniej.
- Pierwsza tura ustaliła zasadę: dowód, na którym decyzja stoi (artykuł, repozytorium, wynik pomiaru), idzie do jej *Based on* z adresem, cytatem i datą odczytu, a relacja `derives from WAY-100` zostaje tylko tam, gdzie decyzja nazywa przejętą praktykę; siedem decyzji wytycznych kodowania dostało wtedy cytaty (WAY-167, WAY-199, WAY-203–206, WAY-212).
- Źródło prywatne (kurs, własne skille) nie stoi w *Based on*: decyzja opisuje wtedy w uzasadnieniu, co tam widziano (WAY-27).
- AIR-518: w zadaniu wytycznych testowania (prośba #42) wiersz 25 tabeli rozstrzygnięć brzmiał „Decyzja the way nazywa, co szablon testów bierze ze źródeł — OWASP, Google, Open Mercato, Limen, kurs 10xDevs, Anthropic — i co zostawia…”; cykl rozłożył go na *Based on* i *Rejected* siedmiu innych decyzji, jawnie w prośbie (zapis cyklu: `git -C the main checkout of the repository show 4b2cdb4:docs/task-cycles/testing-guidelines/cycle.md`, rozstrzygnięcie C3).
- Od tamtej pory skill szukający kandydatów w trybie zadania czyta pytania „dokąd to idzie” (`elements/common/skill/task_variant.md`, „Step 1 — read”), ale ani on, ani `read.md` nie kierują do reguły o pytaniu decyzji.
- Punkt 6 pochodzi z karty D4 raportu `the task's note in the author's backlog`, przyjętej przez Mariusza 12.11.2026 (sprawa 10 analiz); WAY-29 ma dziś przypadek „agent znajduje powód w scalonej prośbie i go cytuje” tylko w przykładzie zgodności.
- Odpadło: przenumerowanie decyzji — numer jest identyfikatorem, na który powołują się skille, szablony, commity, notatki i produkty przypięte do starszych wersji.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

TODO — lista poniżej czeka na przyjęcie tabeli ocen przez Mariusza: wpisy wycofywane z grup A, D i E (i z B, C, jeśli je przyjmie) dojdą jako zmieniane, a decyzje z relacją do WAY-100 jako zmieniane według *To do* 4.

- **WAY-293 — What prevails where a task or its spec excludes the entry for a choice?** Bez zmiany; jego drugi akapit jest kryterium oceny (*To do* 1).
  > In the log of the-way, a rule that stands in one skill or template of the-way stands there with one sentence of its reason. It is an entry of the log only where it carries a choice with a real cost, one for which someone could reasonably propose the rejected way, and the skill or template then names that decision.
- **WAY-19 — How are decisions numbered?** Bez zmiany; mówi, kiedy wpis staje się zdaniem innego wpisu (*To do* 3).
  > […] a new question gets the next free number, a question independent of every existing entry included, while a part of the question an existing entry answers is a sentence of that entry where it cannot change without changing that entry. […]
- **WAY-02 — How does whatever depends on an entry refer to it?** Bez zmiany; każde odwołanie do wycofanego numeru musi zniknąć (*To do* 2, 3).
  > Every foundation entry has a permanent identifier, and everything that depends on it — other entries, tests, documents and code comments — refers to it by that identifier alone, with no fingerprint and no version beside it, and names an entry the foundation holds. […]
- **WAY-100 — When does a method or practice borrowed from elsewhere bind a product?** Zmiana: dopisek z odpowiedzi na pytanie 2 — jak decyzja nazywa praktykę przejętą z zewnątrz i że lista tego, co bierze się z jednego źródła, decyzją nie jest; *Verification* dostaje przykład według dopisku (*To do* 4, 5).
  > A method or practice borrowed from outside a product binds its way of working only through a decision that names what is adopted, where it applies, and why. When an agent recognizes a likeness to a method or practice no decision has adopted, it asks a human before treating it as a rule.
- **WAY-90 — Which citations of a decision's *Based on* become environment fact entries, and how are they named?** Bez zmiany; mówi, jak dowód stoi w *Based on* (*To do* 4).
  > A decision's *Based on* quotes every source outside the product that the decision rests on with its address, the place in it, the passage word for word and the date it was read; […]
- **WAY-27 — Where may this repository point for its reasoning?** Bez zmiany; źródło, którego czytelnik nie otworzy, jest opisane we wpisie (*To do* 4).
  > Nothing in this repository points to a source outside it that its readers cannot reach: every entry carries its whole reasoning, and what is seen only in such a source is described in the entry instead of being pointed to. […]
- **WAY-29 — How is a decision recovered from an existing product written?** Zmiana: opis commita albo prośby o scalenie, które wprowadziły kształt kodu, jest źródłem, do którego agent zagląda, zanim wpisze `unknown` (*To do* 6).
  > A decision recovered from the code of an existing product says in *Origin*, in one sentence, that it was recovered from the code and where in the code it shows, and its rationale and rejected options are quoted from a source, given by a human who knows them, or written as `unknown`. […]

## Settlements to record

TODO

## Out of scope

- Podział dziennika decyzji the way na sekcje tematyczne — zadanie „jak agent czyta dziennik decyzji”.
- Przesunięcie przypięcia the way w produkcie loop2 po scaleniu — osobna prośba w repozytorium loop2.
- Porządki dziennika decyzji gry — zadanie w projekcie Loop.

# Notatka sprzed doprecyzowania

Treść poniżej to materiał, z którego powstał dokument zadania wyżej; znika przy akceptacji dokumentu.

## Gdzie jestem

Pierwsza tura porządków fundamentu the-way jest scalona (PR #37, `foundations` `f0b2130`). Przegląd całego fundamentu po odchudzaniu dał 102 uwagi; przyjąłeś 63 poprawki partią i rozstrzygnąłeś jedenaście pytań. Wycofaliśmy 17 decyzji, rozbiliśmy cztery, które odpowiadały na dwa pytania naraz (nowe numery WAY-225–228), i wycięliśmy listę wycofanych niezmienników. Do szablonu decyzji doszła linia, że pytanie decyzji ma nazywać wybór, który ktoś mógłby rozstrzygnąć inaczej — „co bierzemy z X” albo „co się zmieniło” pytaniem nie jest (WAY-19).

Trzy rzeczy świadomie odłożyliśmy do drugiej tury, bo każda jest większa niż pojedyncza poprawka:

**1. Decyzje szablonów wytycznych.** Około trzydziestu decyzji, WAY-176–192 i WAY-198–211, istnieje tylko dlatego, że dawna klauzula WAY-171 kazała każdą regułę szablonu wytycznych (styleguide, kod) zmieniać osobną decyzją. W pierwszej turze tę klauzulę usunęliśmy: szablony wytycznych zmienia się teraz jak każdy tekst the-way, tak jak szablony elementów fundamentu. Część tych decyzji to nadal prawdziwy wybór, który wiąże produkt albo agenta — na przykład próg audytu zależności czy to, że reguła dostaje niezmiennik tylko z tanim testem (WAY-168). Część to sama treść szablonu, zapisana jako decyzja tylko z powodu tamtej klauzuli. Takie wpisy można wycofać, a ich treść zostawić w szablonie. Do każdej z trzydziestu trzeba odpowiedzieć „wybór zostaje” albo „treść idzie do szablonu”, a listę zaakceptujesz przed naniesieniem.

**2. Źródła i relacja do WAY-100.** WAY-100 mówi, że praktyka wzięta z zewnątrz wiąże tylko przez decyzję, która nazywa, co przejmuje. Ustaliliśmy zasadę: dowód, na którym decyzja stoi (artykuł, repozytorium, wynik pomiaru), idzie do jej pola *Based on* z adresem, cytatem i datą odczytu; relacja „derives from WAY-100” zostaje tylko tam, gdzie decyzja nazywa przejętą praktykę. Siedem decyzji wytycznych kodowania dostało już cytaty w pierwszej turze (WAY-167, 199, 203–206, 212). Do ujednolicenia zostają decyzje, które mają relację do WAY-100, a nie mówią, co przejmują: WAY-128–133, WAY-137–140 i WAY-173, oraz te, które mówią, ale innym wzorem: WAY-121, WAY-142–147, WAY-164. Pamiętaj, że źródła prywatne (kurs, własne skille) nie mogą stać w *Based on* — tam decyzja stoi na własnym uzasadnieniu (WAY-27).

**3. Podział dziennika decyzji na sekcje tematyczne.** Bez przenumerowania — numer decyzji to identyfikator, na który powołują się skille, szablony, commity, notatki i produkty przypięte do starszych wersji. Sekcje według obszaru (elementy fundamentu, zmiana samego the-way, cykl zadania, poziom projektu, wytyczne produktu, instalacja) i przestawienie wpisów; treść każdego wpisu ma zostać bajt w bajt ta sama, co potwierdza skrypt porównujący wpisy przed i po. Najlepiej po punkcie 1, bo wtedy przestawia się mniejszy dziennik.

Sprawdziłem i odpadło: przenumerowanie decyzji (koszt w odwołaniach poza repo, zysk kosmetyczny).

## Pierwszy ruch

Zacznij od punktu 1: niech agent przeczyta każdą z decyzji WAY-176–192 i WAY-198–211 i przy każdej zaproponuje „wybór zostaje” albo „treść do szablonu” z jednym zdaniem powodu i listą miejsc, które się na nią powołują. Wynik przejrzyj jak tabelę — partią. Naniesienie i przegląd idą potem tak jak w pierwszej turze: jeden autor, recenzent, który zmiany nie robił, jeden PR.

## Do doczytania

- `foundations/decisions.md` w the-way — dziennik decyzji; WAY-171 (forma wytycznych produktu, już bez klauzuli), WAY-168 (kiedy reguła wytycznych dostaje niezmiennik), WAY-100 (praktyka z zewnątrz), WAY-27 (wpis niesie całe swoje rozumowanie).
- `elements/decisions/template.md` — szablon decyzji z nową linią o pytaniu.
- Opis PR #37 w the-way (https://github.com/mariusznazar/the-way/pull/37) — co zrobiła pierwsza tura i co z niej świadomie zostało.
- a note of the author's vault — notatka stanu całego odchudzania.

## Otwarte wątki / decyzje

- Przy punkcie 1: decyzje o treści szablonu, które wycofamy, mają odwołania w szablonach i skillach wytycznych (`product-guidelines/`). Odwołanie do wycofanego numeru `foundation_check.py` zgłosi jako błąd, więc każde trzeba przepiąć albo zdjąć. Czy reguła w szablonie ma wtedy wskazywać decyzję, która niesie wybór, czy nic — rozstrzygnąć na pierwszych kilku przykładach.

## Dopisek z 12.11.2026 — analiza dziennika decyzji

Analiza dziennika decyzji (raport `the task's note in the author's backlog`, ustalenia 8 i 9) i moje decyzje z jej przeglądu zmieniają to zadanie w trzech miejscach:

- **Punkt 1 obejmuje cały dziennik, nie trzydzieści wpisów.** W losowej próbie 30 wpisów dziennika the way 13 opisywało treść jednego szablonu albo skilla — prawdopodobnie jest ich ponad sto, nie tylko w zakresach WAY-176–192 i WAY-198–211. Zdecydowałem, że reguła, która mówi tylko, jak pisać kod, testy albo wygląd, może stać w wytycznych bez decyzji (zmienia to zadanie the way: co trafia do dziennika decyzji — pytanie „dokąd to idzie”, próg wejścia, reguły wytycznych bez wpisu, test wskazujący zdanie decyzji), więc ocenę „wybór zostaje / treść do szablonu” warto zrobić na wszystkich 304 wpisach. Metoda z analizy: agenci nadają rodzaj według spisanych reguł, próba czytana w całości z ustalonym ziarnem, tabela do przyjęcia. Skrypty leżą w katalogu `odchudzenie_dziennika_decyzji_dane\` obok raportu i działają na obu dziennikach. Najlepiej po zadaniu o tym, co trafia do dziennika — wtedy kryterium jest już zapisane w procesie.
- **Punkt 3 (podział dziennika na tematy) przeszedł do zadania a note of the author's vault**, razem z regułą, że agent wybiera tematy zadania zamiast wszystkich decyzji części. Tu zostają punkty 1 i 2.
- **Kierunek „decyzja czytana → sprawdzenie” w innym kształcie.** Masowa zamiana decyzji na sprawdzenia się nie opłaca; zamiast niej test wskazuje zdanie decyzji, którego pilnuje, a skrypt wylicza decyzje, których nic nie pilnuje — to część zadania o tym, co trafia do dziennika. W the way da to mało (tylko 21 z 304 wpisów cytują testy, bo reguły procesu żyją w szablonach, nie w programie).
- **Historia gita jako źródło uzasadnienia odzyskanej decyzji** (przyjęte 12.11.2026, sprawa 10 analiz). W szablonie decyzji, w części o decyzjach odzyskanych z kodu: opis commita albo prośby o scalenie, które wprowadziły dany kształt, jest źródłem do zacytowania (z identyfikatorem commita), i agent zagląda tam, zanim wpisze „unknown”; w kroku specyfikacji pytanie o to przy zadaniu, które przebudowuje zastany kod. W grze nic to dziś nie zmienia; w produkcie z historią chroni przed uznaniem celowego ograniczenia za bałagan. Źródło: karta D4 w `the task's note in the author's backlog`.

## Handoff dla AI

```text
Pracujemy nad drugą turą porządków fundamentu repozytorium the-way (the main checkout of the repository, gałąź integracyjna `foundations`). Zadaniem tej sesji jest przygotować dla Mariusza tabelę oceny decyzji szablonów wytycznych (punkt 1 notatki), a po jego akceptacji poprowadzić naniesienie.

Stan wątku, pierwszy ruch i otwarte pytania są opisane w notatce:
the task's note in the author's backlog
Przeczytaj ją w całości, zanim cokolwiek ruszysz. Jest pisana do Mariusza, nie do Ciebie — nie przejmuj z niej tonu ani skrótów, tylko treść.

Zmiana the-way idzie trybem z `agent-instructions/README.md`: gałąź od `foundations`, autor, recenzent, który zmiany nie robił, z jedną rundą poprawek, pełne `python -B gate/run_tests.py` i `python -B elements/common/foundation_check.py` na każdym commicie, PR, scala Mariusz. Nie przenumerowuj decyzji. Nie zmieniaj znaczenia decyzji bez akceptacji Mariusza — tabela idzie do niego przed naniesieniem. Po zmianie the-way produkt `loop2` przesuwa przypięcie osobnym PR-em (instalator: `installation/README.md`, sekcja „Moving the pin”).

Pełny zapis sesji, w której to powstało — wygasa ~2026-11-22, grepuj po konkretach zamiast czytać w całości (17,9 MB / 9509 linii; przy `[Omitted long matching line]` zawężaj wzorzec albo używaj `-o`). Plik jest lokalny, poza repo:
a transcript of an earlier session of the author
```

## Włączone zadanie: Doprecyzowanie zadania nie przyjmuje „decyzji” typu „co bierzemy z X” (AIR-518)

Włączone 2026-11-06 (przegląd focusowy). Oba zadania dotyczą tego, jak the way zapisuje praktykę przejętą z zewnątrz: porządki fundamentu mają wyjaśnić, co z zewnętrznych praktyk przejęto, a ta sprawa — jak pogodzić WAY-100 (zapożyczenie nazywa decyzja) z szablonem decyzji, który zabrania decyzji-listy zapożyczeń. Uwaga: poprawka ma stanąć w skillu `find-foundation-entries`, który przebudowuje seria skilli 7/11 — sprawdzić, czy nie wejdzie tam wcześniej.

Treść przeniesiona z dawnej notatki zadania bez zmian:

### Po co to

- **Jak jest dziś:** Przy doprecyzowaniu zadania możesz zaakceptować do zapisania „decyzję”, która jest tylko listą tego, co bierzemy z różnych źródeł — a szablon decyzji takiego wpisu nie dopuszcza. Wychodzi to dopiero w trakcie wykonania: agent zatrzymuje się z pytaniem, a drugi agent sam rozkłada treść na inne decyzje, bez Twojej zgody.
- **Kto to odczuwa:** Mariusz — akceptuje przy doprecyzowaniu wiersz, który cykl potem zmienia na własną rękę; o zmianie dowiaduje się dopiero z PR-a. Agenci cyklu — jeden traci krok na pytanie, drugi musi rozstrzygać za człowieka.
- **Co jeśli nic:** Stało się raz — w zadaniu wytycznych testowania (the-way PR #42), jeden przypadek na trzy cykle; rozłożenie było tam poprawne i jawnie opisane w PR-ze. Może się powtórzyć przy każdym zadaniu, które przejmuje praktyki z zewnętrznych źródeł, bo jedna reguła fundamentu każe nazwać zapożyczenie decyzją, a szablon zabrania decyzji-listy zapożyczeń.


### Gdzie jestem

Przy doprecyzowaniu zadania the-way powstaje tabela *Settlements to record* — rozstrzygnięć,
które cykl ma wpisać do fundamentu. Kandydatów do niej szuka skill `find-foundation-entries`
(`project-level/task/skill/SKILL.md:195-199`), który każe przeczytać w szablonach, co jest
wpisem danego rodzaju (`elements/common/skill/SKILL.md:49-52`). Dla decyzji wymienia tam tylko
„the plan test" (WAY-36, WAY-26).

W zadaniu wytycznych testowania (the-way PR #42) wiersz 25 brzmiał: „Decyzja the way nazywa,
co szablon testów bierze ze źródeł — OWASP, Google, Open Mercato, Limen, kurs 10xDevs,
Anthropic — i co zostawia: plan testów projektu, mapę ryzyk, proporcje poziomów…". Został
zaakceptowany. Szablon decyzji zabrania jednak takiego wpisu
(`elements/decisions/template.md:40-42`): „"what do we take from X" or "what changed" is no
question, and what such a list carries goes to the decisions that carry each rule (WAY-19)".
Wyłapał to dopiero projektant w cyklu. Orkiestrator rozłożył treść wiersza na pola *Based on*
(na czym oparte) i *Rejected* (co odrzucono) siedmiu innych decyzji — jawnie, w PR-ze, ale
bez decyzji Mariusza (zapis cyklu, wiersz 102, rozstrzygnięcie C3).

Doprecyzowanie miało jednak podstawę: wiersz 25 powoływał się na WAY-100
(`foundations/decisions.md:2102`): „A method or practice borrowed from outside a product binds
its way of working only through a decision that names what is adopted, where it applies, and
why." Dwa wpisy fundamentu ciągną więc w przeciwne strony — WAY-100 każe zapożyczenie nazwać
decyzją, szablon zabrania decyzji-listy zapożyczeń. Godzi je to, co zrobił orkiestrator:
każda decyzja, która przyjmuje regułę ze źródła, nazywa to źródło w *Based on*.

Reguła szablonu weszła 22 października (`277936b`), dwa dni przed akceptacją zadania — czyli
istniała, zawiodło tylko skierowanie do niej. Przypadek jeden na trzy cykle po refaktorze.

Co odpadło: wersja nocnego skanu, która kazała tylko sprawdzać regułę z szablonu, bez wzmianki
o WAY-100 — zostawiłaby doprecyzowaniu dwie sprzeczne reguły.

### Pierwszy ruch

Dopisać zdanie w `elements/common/skill/SKILL.md:49-50` (szkic niżej), drogą the-way:
`refine-task`, potem `implement-task`. Przy okazji sprawdzić, czy WAY-100 nie powinien sam
wskazać *Based on* jako drogi nazwania zapożyczenia — wtedy zdanie w skillu tylko do niego odsyła.
Priorytet niski.

### Do doczytania

Ścieżki w the-way na stan z 25 października (`foundations` @ `2895e0e`).

- `elements\common\skill\SKILL.md:49-52` — co skill szukający
  kandydatów każe czytać w szablonach. Tu ma stanąć zdanie.
- `elements\decisions\template.md:40-42` — reguła o pytaniu decyzji.
- `foundations\decisions.md:2102-2106` — WAY-100.
- `project-level\task\skill\SKILL.md:195-199` — gdzie doprecyzowanie
  woła szukanie kandydatów.
- Zapis cyklu w gicie: `git -C the main checkout of the repository show
  4b2cdb4:docs/task-cycles/testing-guidelines/cycle.md` (wiersz 102 — rozstrzygnięcie C3,
  wiersz 166 — uwaga procesowa) i `…/task.md` (wiersz 188 — wiersz 25 tabeli).
- Sprawa AIR-518 w `the task's note in the author's backlog`
  (po 14 dniach w `ai_review_ledger_archive.md`).

### Otwarte wątki / decyzje

**Gdzie pogodzić WAY-100 z szablonem.** Szkic do skilla: „Read in each element's template what
makes something an entry of it: the plan test and the rule on the question in the decisions'
template (WAY-36, WAY-26, WAY-19) — a list of what is taken from sources is no candidate: what
WAY-100 asks of a borrowing is met by each decision that adopts a rule naming its source in
*Based on*, and what is left out goes to the *Rejected* of the decision it would have
changed; …". Wyjście drugie: dopisać to samo do WAY-100 (jako sposób spełnienia) i w skillu
tylko odesłać. Za drugim: reguła ma jeden dom w fundamencie. Przeciw: zmiana wpisu fundamentu
to cięższa droga niż zdanie w skillu.

### Handoff dla AI

Blok do wklejenia świeżej sesji. Nie powtarza stanu wątku — odsyła po niego
do treści wyżej.

```text
Pracujemy nad zmianą w the-way: szukanie kandydatów na wpisy fundamentu przy doprecyzowaniu
zadania ma odrzucać „decyzję" będącą listą zapożyczeń, i pogodzić to z WAY-100.
Zadaniem tej sesji jest wybrać miejsce i brzmienie poprawki i przeprowadzić ją drogą the-way.

Stan wątku, pierwszy ruch i otwarte pytania są opisane w notatce:
the task's note in the author's backlog
Przeczytaj ją w całości, zanim cokolwiek ruszysz. Jest pisana do Mariusza,
nie do Ciebie — nie przejmuj z niej tonu ani skrótów, tylko treść.

Zmiana w the-way idzie przez refine-task i implement-task, nie edycją od ręki.
Numery linii w notatce są z 25 października — sprawdź je na bieżącym foundations.
Nie usuwaj WAY-100 ani reguły o pytaniu z szablonu decyzji — obie zostają, chodzi o ich pogodzenie.

Pełny zapis sesji, w której to powstało — wygasa ~2026-11-24, grepuj po
konkretach zamiast czytać w całości (plik lokalny, poza repo):
a transcript of an earlier session of the author
```
